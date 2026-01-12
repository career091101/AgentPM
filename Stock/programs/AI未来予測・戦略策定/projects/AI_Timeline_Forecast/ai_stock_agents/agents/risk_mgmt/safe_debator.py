# AI Stock Agents - Safe Risk Analyst
# Based on TradingAgents-main/tradingagents/agents/risk_mgmt/conservative_debator.py
# Adapted for AI stock portfolio risk management

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_safe_debator(llm):
    """
    Create Safe Risk Analyst for portfolio risk debate.

    Champions risk mitigation and capital preservation:
    - Emphasizes AI bubble risks and valuation concerns
    - Advocates for defensive positioning and diversification
    - Challenges aggressive AI stock allocation

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: safe_node function
    """

    def safe_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        safe_history = risk_debate_state.get("safe_history", "")

        current_risky_response = risk_debate_state.get("current_risky_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        # Portfolio decision from Portfolio Strategist
        portfolio_decision = state.get("portfolio_decision", "")

        # Analyst reports for context
        market_report = state.get("market_report", "")
        fundamentals_report = state.get("fundamentals_report", "")
        insider_trading_report = state.get("insider_trading_report", "")

        prompt = f"""As the Safe Risk Analyst for an AI stock portfolio, your role is to prioritize capital preservation and risk mitigation. You believe that AI hype has created bubble-like valuations and excessive risk concentration.

**Your Philosophy:**
- **Protect capital first:** Avoid permanent capital loss from AI bubble burst
- **Valuations matter:** Even great AI companies can be terrible investments at wrong prices
- **Diversification is essential:** AI sector concentration creates unacceptable portfolio risk
- **Risk management beats return chasing:** Steady compounding wins over boom-bust cycles

**Portfolio Decision to Evaluate:**
{portfolio_decision}

**Your Task:**
Argue FOR conservative risk management by:

1. **Emphasizing Downside Risks:**
   - AI bubble indicators: excessive valuations, speculation, crowding
   - Execution risk: AI promises vs actual revenue realization gap
   - Competition intensifying: AI moats are weaker than bulls claim
   - Regulatory risks: AI safety concerns could trigger restrictive regulation
   - Macro headwinds: High interest rates hurt growth stock valuations

2. **Countering Risky Arguments:**
   - Directly respond to Risky Analyst's aggressive positioning
   - Show why "AI revolution" doesn't justify any valuation
   - Demonstrate risks of concentration in single sector
   - Explain opportunity cost of avoiding value opportunities

3. **Countering Neutral Arguments:**
   - Challenge Neutral's balanced approach as insufficiently defensive
   - Show why moderate AI exposure still carries significant risk
   - Argue that current AI valuations require near-perfect execution

4. **Using Data to Support Caution:**
   - Market Research: {market_report}
   - Fundamentals: {fundamentals_report}
   - Insider Trading: {insider_trading_report}

5. **Engagement Style:**
   - Actively debate and persuade with data-driven risk analysis
   - Address specific counterpoints from Risky and Neutral analysts
   - Maintain focus on protecting capital

**Key Arguments to Make:**

- **AI Valuations are Extended:** P/E ratios, P/S ratios far above historical norms
- **Insider Selling:** C-suite selling at AI peaks indicates overvaluation
- **Concentration Risk:** AI sector drawdowns could devastate portfolio
- **Better Risk/Reward Elsewhere:** Diversified portfolio with AI exposure beats AI-only
- **Timing Uncertainty:** AI milestones could be delayed or disappoint

**Debate Context:**

Conversation History:
{history}

Last Risky Analyst Argument:
{current_risky_response}

Last Neutral Analyst Argument:
{current_neutral_response}

**Output:**
Deliver your safe analyst argument conversationally. Challenge the Risky and Neutral positions directly. Show why defensive positioning protects capital while still participating in AI upside through selective exposure.
"""

        response = llm.invoke(prompt)

        argument = f"Safe Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "safe_history": safe_history + "\n" + argument,
            "risky_history": risk_debate_state.get("risky_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Safe",
            "current_safe_response": argument,
            "current_risky_response": risk_debate_state.get("current_risky_response", ""),
            "current_neutral_response": risk_debate_state.get("current_neutral_response", ""),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return safe_node
