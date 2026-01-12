# AI Stock Agents - Fundamentals Analyst
# Based on TradingAgents-main/tradingagents/agents/analysts/fundamentals_analyst.py
# Adapted for AI company fundamentals with focus on AI-specific metrics

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.core_stock_tools import get_fundamentals
from dataflows.config import get_config


def create_fundamentals_analyst(llm):
    """
    Create Fundamentals Analyst node for AI company analysis.

    Focuses on AI-specific fundamental metrics like:
    - R&D spending (AI investment)
    - Revenue growth from AI products
    - GPU/compute infrastructure spending
    - AI talent acquisition

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: fundamentals_analyst_node function
    """

    def fundamentals_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        tools = [
            get_fundamentals,
        ]

        system_message = """You are a researcher analyzing fundamental information about AI-related companies.

**Your Task:**
Write a comprehensive report of the company's fundamental information including:
- Company profile and business model
- Valuation metrics (P/E, P/B, P/S, EV/Revenue, EV/EBITDA)
- Profitability metrics (margins, ROE, ROA)
- Growth rates (revenue, earnings)
- Financial health (debt/equity, current ratio, cash position)
- Dividend policy

**AI-Specific Analysis Focus:**
For {ticker} in the {category} category, pay special attention to:
1. **R&D Spending**: What percentage of revenue goes to AI R&D?
2. **AI Revenue**: What portion of revenue comes from AI products/services?
3. **Compute Infrastructure**: Evidence of GPU purchases, data center expansion?
4. **AI Talent**: Mentions of AI engineers, researchers hired?
5. **Competitive Positioning**: How does valuation compare to AI peers?
6. **Growth Trajectory**: Is AI driving accelerated growth?

**Instructions:**
1. Use get_fundamentals tool to retrieve company data
2. Analyze the data with AI investment lens
3. Identify AI-specific drivers of value
4. Compare valuation multiples to category peers
5. Assess if fundamentals support current valuation
6. Provide detailed, fine-grained analysis (not just "trends are mixed")
7. Append a Markdown table summarizing key financial metrics

**Context:**
- Analysis Date: {analysis_date}
- Ticker: {ticker}
- Category: {category}

Look for signs of AI-driven revenue acceleration, R&D intensity, and competitive moats in AI."""

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
            "fundamentals_report": report,
            "sender": "Fundamentals Analyst"
        }

    return fundamentals_analyst_node
