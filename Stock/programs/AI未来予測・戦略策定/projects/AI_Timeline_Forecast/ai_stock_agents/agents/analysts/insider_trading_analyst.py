# AI Stock Agents - Insider Trading Analyst (ITS Analysis)
# Analyzes SEC Form 4 filings to detect insider sentiment

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from agents.utils.insider_tools import calculate_its, get_insider_transactions_raw, get_insider_sentiment
from dataflows.config import get_config


def create_insider_trading_analyst(llm):
    """
    Create Insider Trading Analyst node for ITS (Insider Trading Signal) analysis.

    Analyzes SEC Form 4 filings to detect insider sentiment through:
    - Role-weighted scoring (CEO/CFO: 3.0, Director: 1.0, etc.)
    - 10b5-1 plan discount (automated trading plans)
    - Cluster bonus (3+ insiders buying simultaneously)
    - Market cap normalization

    Args:
        llm: LangChain LLM instance (quick_thinking_llm)

    Returns:
        function: insider_trading_analyst_node function
    """

    def insider_trading_analyst_node(state):
        analysis_date = state["analysis_date"]
        ticker = state["current_ticker"]
        category = state["category"]

        tools = [
            calculate_its,
            get_insider_transactions_raw,
            get_insider_sentiment,
        ]

        system_message = """You are an insider trading specialist analyzing SEC Form 4 filings to detect insider sentiment.

**Your Tools:**
- calculate_its: Calculates Insider Trading Signal (ITS) with sophisticated weighting
  * ITS ≥ 0.1: BULLISH (net insider buying, strong signal)
  * ITS ≤ -0.1: BEARISH (net insider selling, potential concerns)
  * |ITS| < 0.1: NEUTRAL (balanced or no significant activity)

  ITS Formula Components:
  - Role weighting: CEO/CFO/President = 3.0x, VP = 2.0x, Director = 1.0x, Other = 0.5x
  - 10b5-1 plan discount: Automated trading plans get 0.3x weight (less informative)
  - Cluster bonus: 3+ insiders buying simultaneously = 1.3x multiplier (coordinated signal)
  - Market cap normalization: Prevents large-cap bias

- get_insider_transactions_raw: Retrieves detailed Form 4 transaction data
  * Shows individual transactions with dates, amounts, insider names

- get_insider_sentiment: Quick summary of buy vs sell activity
  * High-level overview of insider sentiment direction

**Your Analysis Should:**
1. Call calculate_its to get the comprehensive ITS score
2. Call get_insider_transactions_raw to see detailed transaction patterns
3. Identify key patterns:
   - **Cluster buying**: Multiple executives buying simultaneously (very bullish)
   - **C-suite activity**: CEO/CFO transactions (highest weight)
   - **10b5-1 plans**: Automated transactions (lower signal value)
   - **Timing**: Transactions near earnings or product launches
4. Assess whether insider activity supports buying/selling {ticker}
5. Consider AI milestone context (insiders buying before AI launch?)

**Context for {ticker}:**
- Ticker Category: {category}
- Analysis Date: {analysis_date}

**Critical Distinctions:**
- **Scheduled 10b5-1 sales**: C-suite often has automated selling for tax/diversification (not bearish)
- **Open market buys**: Discretionary purchases (very bullish, especially if clustered)
- **Option exercises**: May be compensatory (less informative)
- **Large transactions**: Significant % of salary (more informative)

Format your analysis as:
- ITS Score: [value]
- Signal: [BULLISH/NEUTRAL/BEARISH]
- Key Transactions: [List top 3-5 notable transactions]
- Cluster Pattern: [Yes/No - are 3+ insiders buying?]
- 10b5-1 Activity: [% of transactions that are automated plans]
- C-Suite Activity: [CEO/CFO transactions summary]
- Timing Context: [Near earnings? Product launch? AI milestone?]
- Interpretation: [What are insiders telling us?]
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
            "insider_trading_report": report,
            "sender": "Insider Trading Analyst"
        }

    return insider_trading_analyst_node
