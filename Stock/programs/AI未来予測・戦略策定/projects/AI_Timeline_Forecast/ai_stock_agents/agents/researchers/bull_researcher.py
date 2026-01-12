# AI Stock Agents - Bull Researcher
# Based on TradingAgents-main/tradingagents/agents/researchers/bull_researcher.py
# Adapted for AI stock investment with AI Timeline context

from langchain_core.messages import AIMessage
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_bull_researcher(llm, memory):
    """
    Create Bull Researcher node for investment debate.

    Argues FOR investing in the stock, emphasizing:
    - Growth potential and AI-driven revenue opportunities
    - Competitive advantages in AI race
    - Positive technical, fundamental, and sentiment indicators
    - AI milestone proximity as catalyst

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)
        memory: ChromaDB FinancialSituationMemory instance

    Returns:
        function: bull_node function
    """

    def bull_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")
        current_response = investment_debate_state.get("current_response", "")

        # Gather all analyst reports
        market_report = state.get("market_report", "")
        ai_milestone_report = state.get("ai_milestone_report", "")
        fundamentals_report = state.get("fundamentals_report", "")
        category_report = state.get("category_report", "")
        news_sentiment_report = state.get("news_sentiment_report", "")
        insider_trading_report = state.get("insider_trading_report", "")

        # Get AI Timeline context
        ticker = state.get("current_ticker", "Unknown")
        category = state.get("category", "Unknown")
        analysis_date = state.get("analysis_date", "Unknown")
        next_milestone = state.get("next_milestone", "Unknown")
        days_to_milestone = state.get("days_to_milestone", 999)

        # Combine situation for memory retrieval
        curr_situation = f"""Ticker: {ticker} ({category})
Analysis Date: {analysis_date}
Next AI Milestone: {next_milestone} ({days_to_milestone} days away)

{market_report}

{ai_milestone_report}

{fundamentals_report}

{category_report}

{news_sentiment_report}

{insider_trading_report}"""

        # Retrieve past memories
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        if past_memories and "metadatas" in past_memories and past_memories["metadatas"]:
            for metadata in past_memories["metadatas"][0]:
                if "recommendation" in metadata:
                    past_memory_str += metadata["recommendation"] + "\n\n"

        prompt = f"""You are a Bull Analyst advocating for investing in {ticker}, an AI-related stock in the {category} category. Your task is to build a strong, evidence-based case emphasizing growth potential, competitive advantages in AI, and positive market indicators.

**AI Timeline Context:**
- Next Major AI Milestone: {next_milestone} in {days_to_milestone} days
- This milestone could significantly impact {ticker}'s valuation
- Consider how proximity to this milestone creates investment opportunity

**Key points to focus on:**

1. **AI-Driven Growth Potential:**
   - How will {ticker} benefit from upcoming AI milestones (GPT-5, AGI, etc.)?
   - Revenue projections from AI products/services
   - Market opportunity expansion in AI sector
   - Scalability of AI business model

2. **Competitive Advantages in AI Race:**
   - Unique AI technologies, patents, or research capabilities
   - Strong positioning in AI value chain (chips, cloud, applications)
   - Brand strength in AI market
   - Partnerships or ecosystem dominance

3. **Positive Indicators Across 6 Analysts:**
   - **Technical (Weekly)**: Bullish chart patterns, momentum, volume trends
   - **AI Milestone Proximity (AMPI)**: High AMPI score indicating milestone catalyst
   - **Fundamentals**: Strong AI R&D investment, GPU spending, AI revenue growth
   - **Category Momentum (CMS)**: Sector rotation favoring this category
   - **News Sentiment (NSV)**: Improving sentiment velocity, positive AI headlines
   - **Insider Trading (ITS)**: Insider buying, especially C-suite cluster buys

4. **Bear Counterpoints:**
   - Critically analyze the bear argument with specific data
   - Address risks/concerns thoroughly with evidence
   - Show why bull perspective holds stronger merit for AI stocks

5. **Engagement Style:**
   - Conversational, not just listing data
   - Directly counter bear analyst's points
   - Use debate tactics to strengthen bull case

**Resources Available:**

Market Research Report (Weekly Technical):
{market_report}

AI Milestone Proximity Report (AMPI):
{ai_milestone_report}

Company Fundamentals Report (AI-Specific):
{fundamentals_report}

Category Momentum Report (CMS):
{category_report}

News Sentiment Report (NSV):
{news_sentiment_report}

Insider Trading Report (ITS):
{insider_trading_report}

Conversation History of Debate:
{history}

Last Bear Argument:
{current_response}

Reflections from Similar Situations (Learn from Past Mistakes):
{past_memory_str}

**Your Task:**
Deliver a compelling bull argument that:
1. Emphasizes AI milestone proximity as a catalyst
2. Leverages all 6 analyst reports to build evidence
3. Refutes bear's concerns with data and reasoning
4. Engages dynamically in debate rather than listing facts
5. Learns from past reflections to avoid mistakes

**Format:**
Present your argument conversationally, addressing the bear's points directly. Focus on WHY {ticker} is positioned to benefit from the AI revolution, not just WHAT the data shows.
"""

        response = llm.invoke(prompt)

        argument = f"Bull Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node
