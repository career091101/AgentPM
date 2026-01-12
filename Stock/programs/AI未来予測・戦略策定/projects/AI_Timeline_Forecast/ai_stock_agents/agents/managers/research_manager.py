# AI Stock Agents - Research Manager
# Based on TradingAgents-main/tradingagents/agents/managers/research_manager.py
# Adapted for AI stock investment with deep_thinking_llm

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_research_manager(llm, memory):
    """
    Create Research Manager node for debate synthesis and stock recommendation.

    Evaluates Bull vs Bear debate and makes final recommendation:
    - BUY: Strong bull case backed by AI catalysts and positive indicators
    - SELL: Strong bear case with AI execution risks and negative indicators
    - HOLD: Balanced arguments, wait for clearer signals

    Uses deep_thinking_llm (o1-mini) for sophisticated reasoning.

    Args:
        llm: LangChain LLM instance (deep_thinking_llm - o1-mini)
        memory: ChromaDB FinancialSituationMemory instance

    Returns:
        function: research_manager_node function
    """

    def research_manager_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")

        # Gather all analyst reports for context
        market_report = state.get("market_report", "")
        ai_milestone_report = state.get("ai_milestone_report", "")
        fundamentals_report = state.get("fundamentals_report", "")
        category_report = state.get("category_report", "")
        news_sentiment_report = state.get("news_sentiment_report", "")
        insider_trading_report = state.get("insider_trading_report", "")

        # Get ticker context
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

        prompt = f"""As the Research Manager and portfolio decision-maker, your role is to critically evaluate the Bull vs Bear debate and make a definitive investment decision for {ticker}.

**AI Investment Context:**
- Ticker: {ticker} ({category} category)
- Analysis Date: {analysis_date}
- Next AI Milestone: {next_milestone} in {days_to_milestone} days
- This is a **weekly investment decision** for a portfolio of 46 AI stocks

**Your Decision Framework:**

You must choose ONE of the following:
- **BUY**: Strong bull case with AI catalysts, positive indicators across majority of 6 analysts
- **SELL**: Strong bear case with AI execution risks, negative indicators across majority of 6 analysts
- **HOLD**: Only if genuinely balanced OR waiting for a specific catalyst (be very selective with HOLD)

**Critical Evaluation Guidelines:**

1. **Avoid Default HOLD Bias:**
   - Do NOT default to HOLD just because both sides have valid points
   - HOLD should be reserved for truly balanced situations OR when waiting for a specific event
   - Commit to BUY or SELL based on the stronger argument

2. **AI-Specific Considerations:**
   - **AI Milestone Proximity (AMPI)**: Is {ticker} positioned to benefit from {next_milestone}?
   - **Category Momentum (CMS)**: Is the {category} sector in rotation?
   - **Execution Risk**: Can {ticker} actually deliver on AI promises?
   - **Valuation**: Is AI growth already priced in, or is there upside?

3. **Weight of Evidence:**
   - Count how many of the 6 analysts lean bullish vs bearish
   - Technical (Weekly): Trend direction?
   - AI Milestone: High AMPI or low?
   - Fundamentals: Strong AI investment or weak ROI?
   - Category Momentum: Sector tailwind or headwind?
   - News Sentiment: Improving or deteriorating?
   - Insider Trading: Buying or selling?

4. **Debate Quality:**
   - Which side presented stronger evidence?
   - Which side better addressed counterarguments?
   - Did one side rely on assumptions vs data?

**Past Reflections (Learn from Mistakes):**
{past_memory_str}

**Bull vs Bear Debate:**
{history}

**Your Deliverable:**

Provide a clear, actionable investment recommendation with the following structure:

1. **Decision Summary:**
   - Recommendation: [BUY / SELL / HOLD]
   - Confidence Level: [High / Medium / Low]
   - Key Catalyst: [What's driving this decision?]

2. **Evidence Synthesis:**
   - Bullish Indicators: [List 3-5 strongest bull points from debate and analysts]
   - Bearish Indicators: [List 3-5 strongest bear points from debate and analysts]
   - Analyst Score: [X/6 analysts lean bullish, Y/6 lean bearish]

3. **Rationale:**
   - Why did you choose BUY/SELL/HOLD?
   - What evidence was most compelling?
   - How does AI milestone proximity affect this decision?
   - What counterarguments did you weigh?

4. **Strategic Actions for Trader:**
   - If BUY: Entry price target, position size guidance, stop-loss level
   - If SELL: Exit timing, alternative AI stock recommendations
   - If HOLD: Specific catalyst to watch for, re-evaluation date

5. **Risk Considerations:**
   - Top 2-3 risks to this decision
   - What would invalidate this thesis?
   - Exit criteria

**Format:**
Present your analysis conversationally but decisively. Do not hedge excessively. Make a clear call backed by the strongest arguments from the debate and analyst reports.

**Remember:**
- This is for a weekly rebalancing decision
- You have 45 other AI stocks to choose from
- Opportunity cost matters - if HOLD, explain why not rotating capital elsewhere
"""

        response = llm.invoke(prompt)

        new_investment_debate_state = {
            "judge_decision": response.content,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": response.content,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "stock_recommendation": response.content,  # BUY/HOLD/SELL for this stock
        }

    return research_manager_node
