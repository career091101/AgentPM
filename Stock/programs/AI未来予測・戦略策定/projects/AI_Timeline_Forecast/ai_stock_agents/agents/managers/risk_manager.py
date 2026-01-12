# AI Stock Agents - Risk Manager
# Based on TradingAgents-main/tradingagents/agents/managers/risk_manager.py
# Adapted for AI stock portfolio risk management with deep_thinking_llm

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_risk_manager(llm, memory):
    """
    Create Risk Manager node for final portfolio decision.

    Evaluates Risky vs Safe vs Neutral debate and makes final decision:
    - Synthesizes risk perspectives
    - Adjusts Portfolio Strategist's plan based on risk assessment
    - Makes final portfolio allocation decision

    Uses deep_thinking_llm (o1-mini) for sophisticated risk reasoning.

    Args:
        llm: LangChain LLM instance (deep_thinking_llm - o1-mini)
        memory: ChromaDB FinancialSituationMemory instance

    Returns:
        function: risk_manager_node function
    """

    def risk_manager_node(state) -> dict:
        # Get risk debate history
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")

        # Get portfolio decision from Portfolio Strategist
        portfolio_decision = state.get("portfolio_decision", "")

        # Gather analyst reports for context
        market_report = state.get("market_report", "")
        ai_milestone_report = state.get("ai_milestone_report", "")
        fundamentals_report = state.get("fundamentals_report", "")
        category_report = state.get("category_report", "")
        news_sentiment_report = state.get("news_sentiment_report", "")
        insider_trading_report = state.get("insider_trading_report", "")

        # Get context
        analysis_date = state.get("analysis_date", "Unknown")
        next_milestone = state.get("next_milestone", "Unknown")
        days_to_milestone = state.get("days_to_milestone", 999)

        # Combine situation for memory retrieval
        curr_situation = f"""Analysis Date: {analysis_date}
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

        prompt = f"""As the Risk Manager and final decision-maker, your role is to evaluate the risk debate (Risky vs Safe vs Neutral) and make the final portfolio allocation decision for the AI stock portfolio.

**Portfolio Context:**
- Analysis Date: {analysis_date}
- Next AI Milestone: {next_milestone} in {days_to_milestone} days
- Portfolio: 46 AI stocks across 7 categories
- Strategy: Weekly rebalancing, multi-year AI investment horizon

**Portfolio Strategist's Proposed Plan:**
{portfolio_decision}

**Risk Debate Summary:**
{history}

**Your Decision Framework:**

You must deliver a FINAL portfolio allocation plan that balances:
1. **Opportunity:** Capturing AI upside from upcoming milestones
2. **Risk Management:** Protecting against AI bubble burst, concentration risk
3. **Execution:** Practical rebalancing actions for weekly implementation

**Evaluation Guidelines:**

1. **Assess Risk Debate:**
   - **Risky Analyst:** When are they right? (Strong AI momentum, catalyst proximity, proven execution)
   - **Safe Analyst:** When are they right? (Extended valuations, insider selling, macro headwinds)
   - **Neutral Analyst:** Is balance the optimal strategy, or does it dilute both upside and downside protection?

2. **Adjust Portfolio Strategist's Plan:**
   - If Risky wins: INCREASE AI exposure, concentrate in high-conviction names
   - If Safe wins: DECREASE AI exposure, diversify beyond AI, raise cash
   - If Neutral wins: MODERATE adjustments, maintain balanced 40-60% AI exposure

3. **Portfolio Risk Metrics:**
   - Maximum single stock: 10%
   - Maximum category: 30%
   - Target portfolio beta vs S&P500: 1.2-1.5 (AI overweight but not reckless)
   - Cash reserve: 5-15% for rebalancing or downside protection

4. **Learn from Past Mistakes:**
{past_memory_str}

Use these reflections to avoid repeating errors (e.g., over-allocating before corrections, missing entry points from excessive caution).

**Your Deliverable:**

Provide the FINAL portfolio allocation decision with:

1. **Overall Risk Stance:**
   - Which analyst's perspective is most applicable right now? (Risky/Safe/Neutral)
   - Overall portfolio risk level: [Aggressive / Moderate / Conservative]
   - Target AI exposure: [X%]
   - Target cash/non-AI exposure: [Y%]

2. **Adjusted Position Sizing:**
   - Review Portfolio Strategist's allocations
   - Adjust based on risk debate (increase/decrease specific positions)
   - Ensure category limits (max 30% per category)
   - Ensure position limits (max 10% per stock)

   Format:
   ```
   MSFT: 8.5% → 7.0% (reduce due to valuation concerns per Safe Analyst)
   NVDA: 9.0% → 10.0% (increase due to AI chip momentum per Risky Analyst)
   CASH: 5.0% → 10.0% (increase per Safe Analyst for downside protection)
   ```

3. **Risk Mitigation Actions:**
   - Specific risk controls (stop-losses, hedges, diversification)
   - Rebalancing triggers (when to increase/decrease AI exposure)
   - Downside scenarios and contingency plans

4. **Rationale:**
   - Why did you choose this risk stance?
   - Which arguments from the debate were most compelling?
   - How does this position the portfolio for {next_milestone} in {days_to_milestone} days?

5. **Execution Plan for Trader:**
   - Specific buy/sell actions for this week
   - Order priority (what to execute first)
   - Exit criteria (when to reverse this stance)

**Format:**
Present your final decision clearly and decisively. Avoid excessive hedging. Make a clear call on portfolio risk level and specific allocations. Justify with the strongest arguments from the risk debate.
"""

        response = llm.invoke(prompt)

        new_risk_debate_state = {
            "judge_decision": response.content,
            "history": risk_debate_state.get("history", ""),
            "risky_history": risk_debate_state.get("risky_history", ""),
            "safe_history": risk_debate_state.get("safe_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Risk Manager",
            "current_risky_response": risk_debate_state.get("current_risky_response", ""),
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response": risk_debate_state.get("current_neutral_response", ""),
            "count": risk_debate_state.get("count", 0),
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_portfolio_decision": response.content,  # FINAL allocation for execution
        }

    return risk_manager_node
