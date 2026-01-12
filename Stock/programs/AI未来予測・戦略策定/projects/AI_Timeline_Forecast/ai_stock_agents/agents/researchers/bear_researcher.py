# AI Stock Agents - Bear Researcher
# Based on TradingAgents-main/tradingagents/agents/researchers/bear_researcher.py
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


def create_bear_researcher(llm, memory):
    """
    Create Bear Researcher node for investment debate.

    Argues AGAINST investing in the stock, emphasizing:
    - Risks and challenges in AI competition
    - Valuation concerns and bubble risks
    - Negative technical, fundamental, and sentiment indicators
    - AI milestone uncertainty and execution risks

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)
        memory: ChromaDB FinancialSituationMemory instance

    Returns:
        function: bear_node function
    """

    def bear_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bear_history = investment_debate_state.get("bear_history", "")
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

        prompt = f"""You are a Bear Analyst making the case AGAINST investing in {ticker}, an AI-related stock in the {category} category. Your goal is to present a well-reasoned argument emphasizing risks, challenges, and negative indicators specific to AI investments.

**AI Timeline Context:**
- Next Major AI Milestone: {next_milestone} in {days_to_milestone} days
- Consider risks: What if the milestone is delayed? What if {ticker} fails to execute?
- AI hype cycle risks: Are valuations already pricing in perfection?

**Key points to focus on:**

1. **AI Competition and Execution Risks:**
   - How fierce is competition in {ticker}'s AI segment?
   - Can {ticker} actually deliver on AI promises?
   - Risk of being disrupted by faster-moving competitors
   - Uncertainty around AI milestone timing and impact
   - "AI bubble" concerns - are expectations too high?

2. **Valuation Concerns:**
   - Is {ticker} overvalued relative to AI fundamentals?
   - Are AI revenue projections realistic or overhyped?
   - Risk of multiple compression if AI growth disappoints
   - Better risk/reward opportunities elsewhere in AI sector

3. **Negative Indicators Across 6 Analysts:**
   - **Technical (Weekly)**: Bearish patterns, overbought conditions, momentum divergence
   - **AI Milestone Proximity (AMPI)**: Low AMPI = limited near-term catalyst
   - **Fundamentals**: Weak AI ROI, excessive R&D burn, declining margins
   - **Category Momentum (CMS)**: Sector rotation AWAY from this category
   - **News Sentiment (NSV)**: Deteriorating sentiment, negative AI headlines
   - **Insider Trading (ITS)**: Insider selling, especially C-suite exits

4. **Bull Counterpoints:**
   - Critically analyze the bull argument with specific data
   - Expose weaknesses or over-optimistic assumptions
   - Show why bear perspective reflects reality for AI stocks

5. **Engagement Style:**
   - Conversational, not just listing risks
   - Directly counter bull analyst's points
   - Use debate tactics to strengthen bear case

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

Last Bull Argument:
{current_response}

Reflections from Similar Situations (Learn from Past Mistakes):
{past_memory_str}

**Your Task:**
Deliver a compelling bear argument that:
1. Highlights AI-specific risks (competition, execution, hype bubble)
2. Leverages all 6 analyst reports to build evidence of weakness
3. Refutes bull's claims with data and reasoning
4. Engages dynamically in debate rather than listing facts
5. Learns from past reflections to avoid mistakes

**Format:**
Present your argument conversationally, addressing the bull's points directly. Focus on WHY {ticker} faces headwinds in the AI revolution, not just WHAT the negative data shows. Be critical but evidence-based.
"""

        response = llm.invoke(prompt)

        argument = f"Bear Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bear_history": bear_history + "\n" + argument,
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bear_node
