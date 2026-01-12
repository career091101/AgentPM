# AI Stock Agents - Risky Risk Analyst
# Based on TradingAgents-main/tradingagents/agents/risk_mgmt/aggresive_debator.py
# Adapted for AI stock portfolio risk management

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_risky_debator(llm):
    """
    Create Risky Risk Analyst for portfolio risk debate.

    Champions high-reward, high-risk opportunities in AI sector:
    - Emphasizes AI breakthrough potential and massive TAM
    - Advocates for aggressive AI stock allocation
    - Challenges conservative risk management

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: risky_node function
    """

    def risky_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        risky_history = risk_debate_state.get("risky_history", "")

        current_safe_response = risk_debate_state.get("current_safe_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        # Portfolio decision from Portfolio Strategist
        portfolio_decision = state.get("portfolio_decision", "")

        # Analyst reports for context
        market_report = state.get("market_report", "")
        ai_milestone_report = state.get("ai_milestone_report", "")
        category_report = state.get("category_report", "")

        prompt = f"""As the Risky Risk Analyst for an AI stock portfolio, your role is to champion high-reward, high-risk opportunities in the AI revolution. You believe that bold allocation to high-growth AI stocks will capture the massive value creation from AI breakthroughs (GPT-5, AGI, etc.).

**Your Philosophy:**
- **AI is transformative:** The next decade will create trillions in AI market value
- **Fortune favors the bold:** Conservative portfolios will miss the AI wave
- **Concentrated conviction beats diversification:** Overweight AI winners aggressively
- **Timing matters:** AI milestones create explosive upside - position ahead of catalysts

**Portfolio Decision to Evaluate:**
{portfolio_decision}

**Your Task:**
Argue FOR aggressive AI allocation by:

1. **Emphasizing Upside Potential:**
   - AI market TAM (Total Addressable Market) is $X trillion
   - First-mover advantages in AI compound exponentially
   - AI breakthrough events create step-function value (e.g., GPT-3 → GPT-4)
   - Winner-takes-most dynamics in AI platform competition

2. **Countering Conservative Arguments:**
   - Directly respond to Safe Analyst's risk concerns
   - Show why "AI bubble" fears are overstated
   - Demonstrate why valuation concerns ignore AI growth trajectory
   - Explain why diversification dilutes AI alpha

3. **Countering Neutral Arguments:**
   - Challenge Neutral's balanced approach as missing the AI opportunity
   - Show why waiting for "clear signals" means missing entry points
   - Argue that AI momentum is already confirmed, not speculative

4. **Using Data to Support Aggression:**
   - Market Research: {market_report}
   - AI Milestone Proximity: {ai_milestone_report}
   - Category Momentum: {category_report}

5. **Engagement Style:**
   - Actively debate and persuade, not just present data
   - Address specific counterpoints from Safe and Neutral analysts
   - Maintain focus on opportunity cost of caution

**Key Arguments to Make:**

- **Concentration Risk is Manageable:** AI sector diversification (chips, cloud, apps) provides enough spread
- **Volatility is the Price of Growth:** AI stocks are volatile but directionally up
- **Timing Advantage:** Being early to AI themes captures multi-bagger returns
- **Regret Minimization:** Better to overallocate and trim than underallocate and chase

**Debate Context:**

Conversation History:
{history}

Last Safe Analyst Argument:
{current_safe_response}

Last Neutral Analyst Argument:
{current_neutral_response}

**Output:**
Deliver your risky analyst argument conversationally. Challenge the Safe and Neutral positions directly. Show why aggressive AI allocation is the optimal strategy given the AI revolution's magnitude.
"""

        response = llm.invoke(prompt)

        argument = f"Risky Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "risky_history": risky_history + "\n" + argument,
            "safe_history": risk_debate_state.get("safe_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Risky",
            "current_risky_response": argument,
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response": risk_debate_state.get("current_neutral_response", ""),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return risky_node
