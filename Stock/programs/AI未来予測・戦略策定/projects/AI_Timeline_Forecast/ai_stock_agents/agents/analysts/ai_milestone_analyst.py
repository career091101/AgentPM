# AI Stock Agents - AI Milestone Analyst (AMPI Analysis)
# NEW analyst type for AI Stock Agents - analyzes proximity to AI milestones

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.ai_timeline_tools import calculate_ampi, get_next_milestone
from dataflows.config import get_config


def create_ai_milestone_analyst(llm):
    """
    Create AI Milestone Analyst node for AMPI (AI Milestone Proximity Index) analysis.

    This is a NEW analyst type specific to AI Stock Agents that analyzes how
    proximity to major AI milestones (GPT-5, AGI, etc.) affects stock valuations.

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: ai_milestone_analyst_node function
    """

    def ai_milestone_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        tools = [
            calculate_ampi,
            get_next_milestone,
        ]

        system_message = """You are an AI Timeline specialist analyzing how upcoming AI technology milestones
will impact stock valuations for AI-related companies.

**Your Tools:**
- calculate_ampi: Calculates AI Milestone Proximity Index (AMPI) for a specific ticker
  * AMPI ≥ 80: Strong buying signal (milestone within ~30 days)
  * AMPI 50-80: Moderate proximity (milestone 60-120 days away)
  * AMPI < 50: Low influence (milestone >120 days away)

- get_next_milestone: Gets information about the next upcoming AI milestone

**Your Analysis Should:**
1. Call calculate_ampi to get the AMPI score for {ticker}
2. Call get_next_milestone to understand which milestone is approaching
3. Identify which AI milestones are most relevant to {ticker}
4. Assess the company's positioning for each major milestone:
   - Does the company benefit from GPT-5 release? (e.g., NVDA, MSFT, GOOGL)
   - Will they capture value from AGI development?
   - Are they well-positioned for autonomous coding agents?
5. Determine if AMPI signals a buying opportunity (score ≥ 80)
6. Provide specific reasoning for how milestone proximity impacts valuation

**Context for {ticker}:**
- Category: {category}
- Analysis Date: {analysis_date}

Format your analysis as:
- AMPI Score: [0-100]
- Key Milestones: [List with dates and days away]
- Company Positioning: [How {ticker} benefits from each milestone]
- Impact Assessment: [STRONG_BUY/MODERATE/LOW_IMPACT]
- Reasoning: [Detailed explanation of milestone impact on valuation]
- Price Catalyst Timing: [When milestone-driven price moves might occur]"""

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
            "ai_milestone_report": report,
            "sender": "AI Milestone Analyst"
        }

    return ai_milestone_analyst_node
