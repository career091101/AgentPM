# AI Stock Agents - Category Momentum Analyst (CMS Analysis)
# NEW analyst type for detecting sector rotation across 7 AI categories

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.category_tools import calculate_cms, get_category_rotation_signal
from dataflows.config import get_config


def create_category_momentum_analyst(llm):
    """
    Create Category Momentum Analyst node for sector rotation analysis.

    This is a NEW analyst type specific to AI Stock Agents that analyzes
    momentum across 7 AI categories to detect sector rotation patterns.

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: category_momentum_analyst_node function
    """

    def category_momentum_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        tools = [
            calculate_cms,
            get_category_rotation_signal,
        ]

        system_message = """You are a sector rotation specialist analyzing momentum across 7 AI industry categories.

**Your Tools:**
- calculate_cms: Calculates Category Momentum Score (CMS) for all 7 categories
  * CMS = price_momentum (40%) + relative_strength (30%) + volume_trend (20%) + sentiment (10%)
  * CMS ≥ 20: Strong sector momentum (favorable for allocation)
  * CMS ≤ -20: Weak sector momentum (reduce exposure)

- get_category_rotation_signal: Detects which sectors are gaining/losing momentum

**7 AI Categories:**
1. Big_Tech (MSFT, GOOGL, META, AMZN, AAPL)
2. Semiconductors_GPU (NVDA, AMD, INTC)
3. Semiconductors_Foundry (TSM, MU, SSNLF)
4. Data_Centers (EQIX, DLR, SMCI)
5. AI_Applications (PLTR)
6. Cloud (indirect via Big Tech)
7. AI_Research (indirect via MSFT/GOOGL)

**Your Analysis Should:**
1. Call calculate_cms to get CMS scores for all categories
2. Call get_category_rotation_signal to detect rotation patterns
3. Identify which categories have strong momentum (CMS ≥ 20)
4. Identify which categories are losing momentum (CMS ≤ -20)
5. Assess where {ticker} ({category} category) stands in sector rotation
6. Determine if sector momentum supports buying {ticker}
7. Identify if rotation is occurring (e.g., from Big Tech to Semiconductors)

**Context for {ticker}:**
- Ticker Category: {category}
- Analysis Date: {analysis_date}

Format your analysis as:
- {ticker} Category CMS: [score]
- Category Signal: [STRONG_MOMENTUM/POSITIVE/NEUTRAL/NEGATIVE/WEAK_MOMENTUM]
- Top Momentum Categories: [List top 3 with scores]
- Weakest Categories: [List bottom 3 with scores]
- Rotation Pattern: [Description of sector rotation if detected]
- Impact on {ticker}: [How sector momentum affects this stock]
- Recommendation: [Whether to increase/hold/reduce based on sector momentum]"""

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
            "category_report": report,
            "sender": "Category Momentum Analyst"
        }

    return category_momentum_analyst_node
