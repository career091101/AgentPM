# AI Stock Agents - Conditional Logic for Graph Flow
# Based on TradingAgents-main/tradingagents/graph/conditional_logic.py

import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.agent_states import AIStockAgentState


class ConditionalLogic:
    """
    Handles conditional logic for determining graph flow.

    AI Stock Agents version with:
    - 6 analyst types (vs 4 in TradingAgents)
    - max_debate_rounds=2 (vs 1 in TradingAgents)
    - max_risk_discuss_rounds=2 (vs 1 in TradingAgents)
    """

    def __init__(self, max_debate_rounds=2, max_risk_discuss_rounds=2):
        """
        Initialize with configuration parameters.

        Args:
            max_debate_rounds: Maximum debate rounds between Bull/Bear (default: 2)
            max_risk_discuss_rounds: Maximum risk discussion rounds (default: 2)
        """
        self.max_debate_rounds = max_debate_rounds
        self.max_risk_discuss_rounds = max_risk_discuss_rounds

    # ===== Analyst Tool-Calling Logic =====

    def should_continue_market(self, state: AIStockAgentState):
        """Determine if market analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_market"
        return "Msg Clear Market"

    def should_continue_ai_milestone(self, state: AIStockAgentState):
        """Determine if AI milestone analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_ai_milestone"
        return "Msg Clear AI Milestone"

    def should_continue_category_momentum(self, state: AIStockAgentState):
        """Determine if category momentum analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_category_momentum"
        return "Msg Clear Category Momentum"

    def should_continue_news_sentiment(self, state: AIStockAgentState):
        """Determine if news sentiment analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_news_sentiment"
        return "Msg Clear News Sentiment"

    def should_continue_insider_trading(self, state: AIStockAgentState):
        """Determine if insider trading analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_insider_trading"
        return "Msg Clear Insider Trading"

    def should_continue_fundamentals(self, state: AIStockAgentState):
        """Determine if fundamentals analysis should continue (tool calls)."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_fundamentals"
        return "Msg Clear Fundamentals"

    # ===== Debate Logic =====

    def should_continue_debate(self, state: AIStockAgentState) -> str:
        """
        Determine if investment debate should continue.

        With max_debate_rounds=2:
        - Total exchanges: 2 * 2 = 4 (Bull -> Bear -> Bull -> Bear)
        - After 4 exchanges, proceed to Research Manager
        """
        if (
            state["investment_debate_state"]["count"]
            >= 2 * self.max_debate_rounds
        ):
            return "Research Manager"

        # Alternate between Bull and Bear
        if state["investment_debate_state"]["current_response"].startswith("Bull"):
            return "Bear Researcher"
        return "Bull Researcher"

    def should_continue_risk_analysis(self, state: AIStockAgentState) -> str:
        """
        Determine if risk analysis should continue.

        With max_risk_discuss_rounds=2:
        - Total exchanges: 3 * 2 = 6 (Risky -> Safe -> Neutral -> ...)
        - After 6 exchanges, proceed to Risk Manager
        """
        if (
            state["risk_debate_state"]["count"]
            >= 3 * self.max_risk_discuss_rounds
        ):
            return "Risk Manager"

        # Rotate: Risky -> Safe -> Neutral -> Risky ...
        latest_speaker = state["risk_debate_state"]["latest_speaker"]

        if latest_speaker.startswith("Risky"):
            return "Safe Analyst"
        elif latest_speaker.startswith("Safe"):
            return "Neutral Analyst"
        else:
            return "Risky Analyst"

    # ===== Portfolio Strategist Logic [NEW] =====

    def should_continue_portfolio_strategist(self, state: AIStockAgentState) -> str:
        """
        Determine if portfolio strategist should proceed to risk analysis.

        In AI Stock Agents, Portfolio Strategist generates portfolio allocations
        before Risk Team evaluates.
        """
        # Check if portfolio allocation is complete
        if state.get("position_sizing") is not None:
            return "Risky Analyst"  # Proceed to Risk Team
        else:
            return "Portfolio Strategist"  # Re-run if allocation incomplete

    # ===== Analyst Sequencing Logic =====

    def route_after_analyst(
        self, state: AIStockAgentState, current_analyst: str, analyst_sequence: list
    ) -> str:
        """
        Route to next analyst in sequence or proceed to researchers.

        Args:
            state: Current agent state
            current_analyst: Name of current analyst
            analyst_sequence: Ordered list of analyst names

        Returns:
            str: Next node name
        """
        try:
            current_index = analyst_sequence.index(current_analyst)
            if current_index < len(analyst_sequence) - 1:
                # Go to next analyst
                return analyst_sequence[current_index + 1]
            else:
                # All analysts done -> go to Bull Researcher
                return "Bull Researcher"
        except ValueError:
            # Fallback: proceed to Bull Researcher
            return "Bull Researcher"
