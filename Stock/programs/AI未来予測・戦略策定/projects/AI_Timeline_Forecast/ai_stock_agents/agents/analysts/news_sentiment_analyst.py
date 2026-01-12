# AI Stock Agents - News Sentiment Analyst (NSV Analysis)
# Analyzes news sentiment velocity to detect rapid sentiment changes

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.news_tools import calculate_nsv, get_recent_news_headlines, get_sentiment_trend
from dataflows.config import get_config


def create_news_sentiment_analyst(llm):
    """
    Create News Sentiment Analyst node for NSV (News Sentiment Velocity) analysis.

    Analyzes sentiment change acceleration/deceleration to identify:
    - Rapid sentiment improvements (strong bullish signals)
    - Rapid sentiment deterioration (strong bearish signals)
    - Sentiment inflection points

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: news_sentiment_analyst_node function
    """

    def news_sentiment_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        tools = [
            calculate_nsv,
            get_recent_news_headlines,
            get_sentiment_trend,
        ]

        system_message = """You are a news sentiment specialist analyzing sentiment velocity (acceleration) for AI stocks.

**Your Tools:**
- calculate_nsv: Calculates News Sentiment Velocity (NSV) - the rate of sentiment change
  * NSV > +5: Rapid sentiment improvement (STRONG BULLISH)
  * NSV +2 to +5: Improving sentiment (BULLISH)
  * NSV -2 to +2: Stable sentiment (NEUTRAL)
  * NSV -5 to -2: Deteriorating sentiment (BEARISH)
  * NSV < -5: Rapid sentiment deterioration (STRONG BEARISH)

- get_recent_news_headlines: Retrieves recent headlines to understand sentiment context
  * Provides actual news stories driving sentiment changes

- get_sentiment_trend: Visualizes 30-day sentiment trajectory
  * Helps identify inflection points and trend reversals

**Your Analysis Should:**
1. Call calculate_nsv to get NSV score and signal
2. Call get_recent_news_headlines to understand what's driving sentiment
3. Call get_sentiment_trend to visualize sentiment trajectory
4. Identify sentiment inflection points (rapid changes)
5. Assess whether sentiment momentum supports buying/selling {ticker}
6. Distinguish between noise and meaningful sentiment shifts
7. Consider AI milestone proximity in sentiment interpretation

**Context for {ticker}:**
- Ticker Category: {category}
- Analysis Date: {analysis_date}

**Key Questions:**
- Is sentiment accelerating positively or negatively?
- Are recent headlines about AI breakthroughs, earnings, or controversies?
- Is the sentiment shift sustained or a one-day spike?
- How does sentiment velocity align with price momentum?

Format your analysis as:
- NSV Score: [value]
- Signal: [RAPID_IMPROVEMENT/IMPROVING/STABLE/DETERIORATING/RAPID_DETERIORATION]
- Current Sentiment: [value]
- Key Headlines: [List top 3-5 headlines]
- Sentiment Trajectory: [UPWARD/FLAT/DOWNWARD over 30 days]
- Interpretation: [What's driving sentiment change?]
- Investment Impact: [How this affects buy/sell/hold decision]"""

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

        chain = prompt | llm.bind_tools(tools)

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            # Tool-calling complete, extract report
            report = result.content

        return {
            "messages": [result],
            "news_sentiment_report": report,
            "sender": "News Sentiment Analyst"
        }

    return news_sentiment_analyst_node
