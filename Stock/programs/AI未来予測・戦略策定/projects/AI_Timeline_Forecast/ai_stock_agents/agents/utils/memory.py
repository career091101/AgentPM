# AI Stock Agents - ChromaDB Memory for RAG
# Based on TradingAgents-main/tradingagents/agents/utils/memory.py

import chromadb
from chromadb.config import Settings
from openai import OpenAI
import os


class FinancialSituationMemory:
    """
    ChromaDB-based memory for storing and retrieving financial situations.

    Uses OpenAI embeddings for semantic similarity search to find relevant
    past situations and their corresponding recommendations.
    """

    def __init__(self, name, config):
        """
        Initialize memory collection.

        Args:
            name: Name of the ChromaDB collection
            config: Configuration dictionary with backend_url and openai_api_key
        """
        # Determine embedding model based on backend
        if config.get("backend_url") == "http://localhost:11434/v1":
            # Ollama backend
            self.embedding = "nomic-embed-text"
        else:
            # OpenAI backend
            self.embedding = "text-embedding-3-small"

        # Initialize OpenAI client
        api_key = config.get("openai_api_key") or os.getenv("OPENAI_API_KEY")
        backend_url = config.get("backend_url", "https://api.openai.com/v1")

        self.client = OpenAI(api_key=api_key, base_url=backend_url)

        # Initialize ChromaDB client
        self.chroma_client = chromadb.Client(Settings(allow_reset=True))

        # Create or get collection
        try:
            self.situation_collection = self.chroma_client.create_collection(name=name)
        except Exception:
            # Collection already exists
            self.situation_collection = self.chroma_client.get_collection(name=name)

    def get_embedding(self, text):
        """
        Get OpenAI embedding for a text.

        Args:
            text: Input text to embed

        Returns:
            list: Embedding vector
        """
        response = self.client.embeddings.create(model=self.embedding, input=text)
        return response.data[0].embedding

    def add_situations(self, situations_and_advice):
        """
        Add financial situations and their corresponding advice.

        Args:
            situations_and_advice: List of tuples (situation, recommendation)
                                  e.g., [("NVDA shows strong AI demand", "BUY"), ...]
        """
        situations = []
        advice = []
        ids = []
        embeddings = []

        offset = self.situation_collection.count()

        for i, (situation, recommendation) in enumerate(situations_and_advice):
            situations.append(situation)
            advice.append(recommendation)
            ids.append(str(offset + i))
            embeddings.append(self.get_embedding(situation))

        self.situation_collection.add(
            documents=situations,
            metadatas=[{"recommendation": rec} for rec in advice],
            embeddings=embeddings,
            ids=ids,
        )

    def get_memories(self, current_situation, n_matches=2):
        """
        Find matching recommendations using semantic similarity.

        Args:
            current_situation: Current financial situation description
            n_matches: Number of top matches to return (default: 2)

        Returns:
            list: List of dictionaries with matched_situation, recommendation, similarity_score
        """
        query_embedding = self.get_embedding(current_situation)

        results = self.situation_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_matches,
            include=["metadatas", "documents", "distances"],
        )

        matched_results = []

        if results["documents"] and len(results["documents"][0]) > 0:
            for i in range(len(results["documents"][0])):
                matched_results.append(
                    {
                        "matched_situation": results["documents"][0][i],
                        "recommendation": results["metadatas"][0][i][
                            "recommendation"
                        ],
                        "similarity_score": 1 - results["distances"][0][i],
                    }
                )

        return matched_results

    def reset(self):
        """Clear all memories from this collection."""
        self.chroma_client.delete_collection(name=self.situation_collection.name)
        self.situation_collection = self.chroma_client.create_collection(
            name=self.situation_collection.name
        )


def initialize_all_memories(config):
    """
    Initialize all 6 memory collections for AI Stock Agents.

    Args:
        config: Configuration dictionary

    Returns:
        dict: Dictionary mapping memory names to FinancialSituationMemory instances
    """
    memory_names = [
        "bull_memory",
        "bear_memory",
        "research_manager_memory",
        "portfolio_strategist_memory",  # [NEW] for AI Stock Agents
        "risk_manager_memory",
        "trader_memory",
    ]

    memories = {}

    for name in memory_names:
        try:
            memories[name] = FinancialSituationMemory(name, config)
            print(f"Initialized memory: {name}")
        except Exception as e:
            print(f"Error initializing {name}: {e}")
            memories[name] = None

    return memories


# Example usage for testing
if __name__ == "__main__":
    # Test memory initialization
    test_config = {
        "backend_url": "https://api.openai.com/v1",
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
    }

    print("Testing AI Stock Agents Memory System...")

    # Initialize single memory
    test_memory = FinancialSituationMemory("test_memory", test_config)

    # Example data for AI stock investing
    example_data = [
        (
            "NVDA GPU demand surging due to GPT-5 training, AMPI score 92",
            "STRONG BUY - AI milestone proximity very high, expect continued demand",
        ),
        (
            "MSFT Azure AI revenue growing 50% QoQ, insider buying by CEO",
            "BUY - Positive fundamentals + insider sentiment, low execution risk",
        ),
        (
            "AI semiconductor sector showing correction after 30% rally, CMS dropping to 45",
            "HOLD - Sector rotation underway, wait for stabilization before adding",
        ),
        (
            "AGI milestone delayed 6 months, AMPI scores falling across board",
            "REDUCE - AI timeline expectations recalibrating, take profits",
        ),
    ]

    # Add situations
    test_memory.add_situations(example_data)

    # Test query
    current_situation = """
    NVDA showing strong performance with 20% gain this month.
    GPT-5 release confirmed for next quarter. AMPI score at 89.
    Insider transactions show 3 directors buying shares.
    """

    recommendations = test_memory.get_memories(current_situation, n_matches=2)

    print("\nQuery:", current_situation)
    print("\nTop Matches:")
    for i, rec in enumerate(recommendations, 1):
        print(f"\nMatch {i}:")
        print(f"Similarity Score: {rec['similarity_score']:.2f}")
        print(f"Matched Situation: {rec['matched_situation']}")
        print(f"Recommendation: {rec['recommendation']}")

    print("\n✅ Memory system test completed successfully")
