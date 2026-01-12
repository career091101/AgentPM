# AI Stock Agents - Market Analyst (Weekly Technical Analysis)
# Based on TradingAgents-main/tradingagents/agents/analysts/market_analyst.py
# Adapted for weekly timeframe instead of daily

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.core_stock_tools import get_stock_data, get_indicators
from dataflows.config import get_config


def create_market_analyst(llm):
    """
    Create Market Analyst node for weekly technical analysis.

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: market_analyst_node function
    """

    def market_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        # Get AI Timeline context
        next_milestone = state.get("next_milestone", "Unknown")
        days_to_milestone = state.get("days_to_milestone", 999)

        tools = [
            get_stock_data,
            get_indicators,
        ]

        system_message = """You are a trading assistant analyzing **weekly** stock data for AI-related companies.
Your role is to select the **most relevant weekly indicators** for understanding medium to long-term trends. Choose up to **6 indicators** that provide complementary insights without redundancy.

**Available Weekly Indicators:**

Moving Averages:
- close_10_sma: 10-week SMA (short-term trend, ~2.5 months). Usage: Identify short-term trend direction. Tips: More responsive than 40-week SMA; crossovers signal trend changes.
- close_40_sma: 40-week SMA (long-term trend, ~200-day equivalent). Usage: Identify major trend direction and support/resistance levels. Tips: Classic long-term indicator; price above = bullish, below = bearish.

MACD Related:
- macd_weekly: MACD on weekly timeframe (8,17,9 parameters). Usage: Identify trend changes and momentum shifts. Tips: Weekly MACD crossovers are stronger signals than daily.

Momentum Indicators:
- rsi_weekly: 14-week RSI. Usage: Identify overbought (>70) or oversold (<30) conditions. Tips: Weekly RSI is less noisy than daily; extremes are more significant.

Volatility Indicators:
- boll_weekly: Bollinger Bands on weekly data (20-week). Usage: Measure weekly price volatility and identify extremes. Tips: Price touching upper/lower bands indicates potential reversal zones.

**Instructions:**
1. First, call get_stock_data to retrieve weekly OHLCV data (past 52 weeks recommended)
2. Then, call get_indicators for each selected indicator
3. Analyze trends comprehensively - avoid simply stating "trends are mixed"
4. Provide detailed, fine-grained analysis that helps with investment decisions
5. Append a Markdown table at the end summarizing key points

**Context for {ticker}:**
- Category: {category}
- Next AI Milestone: {next_milestone} in {days_to_milestone} days
- Analysis Date: {analysis_date}

Consider how the AI milestone proximity might影響 this stock's technical patterns."""

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " If you or any other assistant has the FINAL INVESTMENT RECOMMENDATION: **BUY/HOLD/SELL** or deliverable,"
                    " prefix your response with FINAL INVESTMENT RECOMMENDATION: **BUY/HOLD/SELL** so the team knows to stop."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    " For your reference, the current analysis date is {analysis_date}. The company we are analyzing is {ticker} ({category} category).",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(analysis_date=analysis_date)
        prompt = prompt.partial(ticker=ticker)
        prompt = prompt.partial(category=category)
        prompt = prompt.partial(next_milestone=next_milestone)
        prompt = prompt.partial(days_to_milestone=days_to_milestone)

        chain = prompt | llm.bind_tools(tools)

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            # Tool-calling complete, extract report
            report = result.content

        return {
            "messages": [result],
            "market_report": report,
            "sender": "Market Analyst"
        }

    return market_analyst_node
