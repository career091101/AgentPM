# AI Stock Agents - Neutral Risk Analyst
# Based on TradingAgents-main/tradingagents/agents/risk_mgmt/neutral_debator.py
# Adapted for AI stock portfolio risk management

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def create_neutral_debator(llm):
    """
    Create Neutral Risk Analyst for portfolio risk debate.

    Advocates for balanced approach between risk and reward:
    - Recognizes AI opportunity while managing risks
    - Advocates for moderate AI exposure with hedging
    - Mediates between aggressive and defensive positioning

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: neutral_node function
    """

    def neutral_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        neutral_history = risk_debate_state.get("neutral_history", "")

        current_risky_response = risk_debate_state.get("current_risky_response", "")
        current_safe_response = risk_debate_state.get("current_safe_response", "")

        # Portfolio decision from Portfolio Strategist
        portfolio_decision = state.get("portfolio_decision", "")

        # Analyst reports for context
        category_report = state.get("category_report", "")
        news_sentiment_report = state.get("news_sentiment_report", "")

        prompt = f"""As the Neutral Risk Analyst for an AI stock portfolio, your role is to advocate for a balanced approach that captures AI upside while managing downside risks. You seek the optimal risk/reward tradeoff.

**Your Philosophy:**
- **Balance is key:** Neither excessive aggression nor excessive caution
- **Selective AI exposure:** Overweight high-conviction AI, avoid speculative AI
- **Dynamic risk management:** Adjust allocation as AI landscape evolves
- **Risk-adjusted returns:** Maximize Sharpe ratio, not raw returns or safety

**Portfolio Decision to Evaluate:**
{portfolio_decision}

**Your Task:**
Argue FOR balanced risk management by:

1. **Acknowledging Both Sides:**
   - **Risky Analyst is right that:** AI is transformative, TAM is massive, early positioning matters
   - **Safe Analyst is right that:** Valuations are elevated, concentration risk exists, bubbles happen
   - **Synthesis:** Moderate AI exposure (40-60%) with quality focus

2. **Proposing Balanced Solutions:**
   - **Core AI Holdings:** 40-50% in proven AI leaders (MSFT, NVDA, GOOGL)
   - **Selective Growth:** 10-20% in high-conviction AI pure-plays (PLTR, AI apps)
   - **Diversification:** 20-30% in AI-adjacent or non-AI for risk management
   - **Cash/Hedging:** 5-10% for rebalancing opportunities or downside protection

3. **Countering Extreme Positions:**
   - **To Risky:** Show why 100% AI allocation risks catastrophic drawdown
   - **To Safe:** Show why avoiding AI entirely misses generational opportunity
   - Both extremes ignore risk-adjusted optimization

4. **Using Data to Support Balance:**
   - Category Momentum: {category_report}
   - News Sentiment: {news_sentiment_report}

5. **Engagement Style:**
   - Mediate between extremes with data-driven reasoning
   - Address specific points from both Risky and Safe analysts
   - Maintain focus on optimal risk/reward tradeoff

**Key Arguments to Make:**

- **Diversification Within AI:** Chips + Cloud + Apps provides AI exposure with sector diversification
- **Quality Over Hype:** Focus on AI companies with proven revenue, not speculation
- **Dynamic Rebalancing:** Adjust AI exposure as valuations, momentum, and milestones evolve
- **Tail Risk Management:** Position sizing limits single-stock catastrophe
- **Opportunity Optionality:** Maintain some cash for AI corrections or new opportunities

**Debate Context:**

Conversation History:
{history}

Last Risky Analyst Argument:
{current_risky_response}

Last Safe Analyst Argument:
{current_safe_response}

**Output:**
Deliver your neutral analyst argument conversationally. Acknowledge valid points from both Risky and Safe, then advocate for a balanced middle path. Show why moderation optimizes risk-adjusted returns in AI investing.
"""

        response = llm.invoke(prompt)

        argument = f"Neutral Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "neutral_history": neutral_history + "\n" + argument,
            "risky_history": risk_debate_state.get("risky_history", ""),
            "safe_history": risk_debate_state.get("safe_history", ""),
            "latest_speaker": "Neutral",
            "current_neutral_response": argument,
            "current_risky_response": risk_debate_state.get("current_risky_response", ""),
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return neutral_node
