# AI Stock Agents - Portfolio Strategist
# NEW layer for AI Stock Agents (not in TradingAgents-main)
# Manages 46-stock portfolio with Kelly Criterion and rebalancing

import time
import json
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dataflows.config import get_config


def create_portfolio_strategist(llm):
    """
    Create Portfolio Strategist node for portfolio-level decisions.

    NEW layer specific to AI Stock Agents. Aggregates all 46 stock
    recommendations and makes portfolio-level allocation decisions.

    Responsibilities:
    - Integrate all stock recommendations (BUY/HOLD/SELL)
    - Apply Kelly Criterion for position sizing
    - Enforce category allocation constraints (max 30% per category)
    - Determine rebalancing actions (weekly minor, monthly full)

    Args:
        llm: LangChain LLM instance (deep_thinking_llm - o1-mini)

    Returns:
        function: portfolio_strategist_node function
    """

    def portfolio_strategist_node(state) -> dict:
        """
        Portfolio Strategist node function.

        Expects state to contain:
        - all_stock_recommendations: Dict[ticker, recommendation]
        - portfolio_state: Current portfolio holdings
        - analysis_date: Current date
        - ai_timeline_data: AI milestone context
        - category_scores: CMS scores for all categories

        Returns updated state with:
        - position_sizing: Dict[ticker, size]
        - rebalancing_actions: List of actions
        """

        # Extract portfolio-level context
        all_recommendations = state.get("all_stock_recommendations", {})
        current_portfolio = state.get("portfolio_state", {}).get("positions", {})
        analysis_date = state.get("analysis_date", "Unknown")
        category_scores = state.get("category_scores", {})

        # Get configuration
        config = get_config()
        categories = config.get("categories", {})
        max_position_size = config.get("max_position_size", 0.10)  # 10% per stock
        max_category_size = config.get("max_category_size", 0.30)  # 30% per category
        rebalance_threshold = config.get("rebalance_threshold", 0.05)  # 5% drift

        # Build portfolio context for LLM
        recommendation_summary = ""
        buy_count = 0
        sell_count = 0
        hold_count = 0

        for ticker, rec in all_recommendations.items():
            if "BUY" in rec.upper():
                buy_count += 1
            elif "SELL" in rec.upper():
                sell_count += 1
            else:
                hold_count += 1

        recommendation_summary = f"""
Portfolio-Wide Recommendations:
- BUY: {buy_count} stocks
- SELL: {sell_count} stocks
- HOLD: {hold_count} stocks
- Total analyzed: {len(all_recommendations)} stocks

Individual Stock Recommendations:
{json.dumps(all_recommendations, indent=2)}
"""

        category_summary = f"""
Category Momentum Scores (CMS):
{json.dumps(category_scores, indent=2)}
"""

        current_portfolio_summary = f"""
Current Portfolio Holdings:
{json.dumps(current_portfolio, indent=2) if current_portfolio else "Empty portfolio (initial allocation)"}
"""

        prompt = f"""As the Portfolio Strategist, your role is to manage a 46-stock AI investment portfolio. You receive individual stock recommendations from the Research Manager and must make portfolio-level allocation decisions.

**Your Responsibilities:**

1. **Position Sizing (Kelly Criterion-Inspired):**
   - Allocate capital across BUY recommendations
   - Consider conviction level, risk, and diversification
   - Maximum {max_position_size*100:.0f}% per stock
   - Typical range: 1-10% per position

2. **Category Allocation Constraints:**
   - Maximum {max_category_size*100:.0f}% per category
   - Categories: {', '.join(categories.keys())}
   - Use Category Momentum Scores (CMS) to guide allocation
   - Overweight categories with CMS > 20, underweight CMS < -20

3. **Rebalancing Strategy:**
   - **Weekly (Minor Rebalancing):** Only if drift > {rebalance_threshold*100:.0f}%
   - **Monthly (Full Rebalancing):** Comprehensive portfolio reset
   - Minimize transaction costs and tax implications

4. **Portfolio-Level Thinking:**
   - Diversification across AI value chain (chips, cloud, apps)
   - Correlation management (avoid over-concentration)
   - Risk-adjusted returns (not just maximizing returns)
   - Opportunity cost (selling weak HOLD to buy strong BUY)

**Current Context:**

Analysis Date: {analysis_date}

{recommendation_summary}

{category_summary}

{current_portfolio_summary}

**Your Deliverable:**

Provide a comprehensive portfolio allocation plan with the following structure:

1. **Overall Portfolio Strategy:**
   - Target number of holdings (out of 46 stocks)
   - Cash allocation (if any)
   - Top 3 category overweights/underweights based on CMS

2. **Position Sizing for BUY Recommendations:**
   For each BUY recommendation, specify:
   - Ticker: [Symbol]
   - Target Allocation: [X.X%]
   - Rationale: [Why this size? Conviction level?]
   - Category: [Which category does this contribute to?]

   Example format:
   ```
   MSFT: 8.5% (High conviction AI leader, Big Tech category)
   NVDA: 9.0% (AI chip dominance, Semiconductors_GPU category)
   ```

3. **Rebalancing Actions:**
   For existing holdings:
   - INCREASE: [Ticker, from X% to Y%, reason]
   - DECREASE: [Ticker, from X% to Y%, reason]
   - EXIT: [Ticker, sell completely, reason]
   - HOLD: [Ticker, maintain current X%, reason]

4. **Category Allocation Check:**
   Verify that category allocations respect {max_category_size*100:.0f}% limit:
   ```
   Big Tech: XX.X% (within limit)
   Semiconductors_GPU: YY.Y% (within limit)
   ...
   ```

5. **Risk Considerations:**
   - Portfolio concentration risk
   - Category over-exposure
   - Correlation concerns
   - Tail risk hedges (if any)

**Decision Framework:**

- **High Conviction BUY + High CMS:** 5-10% allocation
- **Medium Conviction BUY + Medium CMS:** 2-5% allocation
- **Low Conviction BUY or Low CMS:** 1-2% allocation or skip
- **SELL:** Exit position (if held) or avoid (if not held)
- **HOLD:** Maintain current allocation or small position if strong category

**Format:**
Provide your portfolio allocation plan in a structured format. Be decisive about position sizes. Justify allocations based on conviction, category momentum, and portfolio constraints.
"""

        response = llm.invoke(prompt)

        # Parse response to extract position_sizing (simplified for now)
        # In production, would parse structured output
        position_sizing = {}
        rebalancing_actions = []

        # Placeholder: In real implementation, parse LLM response
        # For now, store raw response
        portfolio_decision = response.content

        return {
            "portfolio_decision": portfolio_decision,
            "position_sizing": position_sizing,  # TODO: Parse from LLM response
            "rebalancing_actions": rebalancing_actions,  # TODO: Parse from LLM response
        }

    return portfolio_strategist_node
