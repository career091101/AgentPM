# AI Stock Agents - Category Momentum Score (CMS) Calculation
# Detects sector rotation across 7 AI categories

from langchain_core.tools import tool
from typing import Annotated, List, Dict
import sys
from pathlib import Path
import json
from datetime import datetime, timedelta

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dataflows.interface import route_to_vendor
from dataflows.config import get_config


def calculate_category_momentum(
    category_name: str,
    category_tickers: List[str],
    curr_date: str,
    look_back_weeks: int = 4
) -> Dict:
    """
    Calculate Category Momentum Score (CMS) for a category.

    Formula:
        CMS = price_momentum * 0.4 + relative_strength * 0.3 +
              volume_trend * 0.2 + sentiment * 0.1

    Args:
        category_name: Category name (e.g., "Big_Tech", "Semiconductors_GPU")
        category_tickers: List of tickers in this category
        curr_date: Current date in yyyy-mm-dd format
        look_back_weeks: Number of weeks to analyze (default: 4)

    Returns:
        dict: CMS score and breakdown
    """
    if not category_tickers:
        return {
            "category": category_name,
            "cms_score": 0,
            "signal": "NEUTRAL",
            "reason": "No tickers in category (indirect holding)"
        }

    # Calculate start date
    curr_date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    start_date = curr_date_obj - timedelta(weeks=look_back_weeks)
    start_date_str = start_date.strftime("%Y-%m-%d")

    # Fetch weekly data for all tickers in category
    try:
        batch_data = route_to_vendor(
            "get_batch_stock_data",
            category_tickers,
            curr_date,
            look_back_weeks
        )
    except Exception as e:
        return {
            "category": category_name,
            "cms_score": 0,
            "signal": "ERROR",
            "reason": f"Failed to fetch data: {str(e)}"
        }

    # Parse returns for each ticker
    ticker_returns = {}

    for ticker, data_csv in batch_data.items():
        if "Error" in data_csv or "No data" in data_csv:
            continue

        # Parse CSV to calculate returns
        lines = data_csv.split("\n")
        data_lines = [line for line in lines if not line.startswith("#") and line.strip()]

        if len(data_lines) <= 1:  # Only header
            continue

        # Extract close prices
        prices = []
        for line in data_lines[1:]:  # Skip header
            fields = line.split(",")
            if len(fields) >= 5:  # Date, Open, High, Low, Close, ...
                try:
                    close_price = float(fields[4])  # Close column
                    prices.append(close_price)
                except (ValueError, IndexError):
                    continue

        if len(prices) >= 2:
            # Calculate return
            period_return = (prices[-1] - prices[0]) / prices[0] * 100
            ticker_returns[ticker] = {
                "return": period_return,
                "prices": prices
            }

    if not ticker_returns:
        return {
            "category": category_name,
            "cms_score": 0,
            "signal": "NO_DATA",
            "reason": "No price data available"
        }

    # 1. Price Momentum (40% weight)
    avg_return = sum(t["return"] for t in ticker_returns.values()) / len(ticker_returns)
    price_momentum = avg_return  # Normalized to percentage

    # 2. Relative Strength (30% weight) - vs SPY
    # For simplicity, use absolute momentum as proxy (in production, fetch SPY)
    # Positive return = outperforming, negative = underperforming
    relative_strength = avg_return  # Simplified

    # 3. Volume Trend (20% weight)
    # Simplified: use price volatility as proxy (higher volatility = higher interest)
    volatilities = []
    for ticker_data in ticker_returns.values():
        prices = ticker_data["prices"]
        if len(prices) >= 2:
            # Simple volatility: std of returns
            returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
            if returns:
                volatility = sum(abs(r) for r in returns) / len(returns) * 100
                volatilities.append(volatility)

    avg_volatility = sum(volatilities) / len(volatilities) if volatilities else 0
    volume_trend = min(avg_volatility * 10, 100)  # Scale and cap at 100

    # 4. Sentiment (10% weight)
    # Simplified: positive if avg return > 0, negative otherwise
    sentiment = 50 + avg_return  # Centered at 50

    # Calculate CMS
    cms = (
        price_momentum * 0.4 +
        relative_strength * 0.3 +
        volume_trend * 0.2 +
        sentiment * 0.1
    )

    # Cap at -100 to 100
    cms = max(-100, min(100, cms))

    # Determine signal
    if cms >= 20:
        signal = "STRONG_MOMENTUM"
    elif cms >= 5:
        signal = "POSITIVE"
    elif cms <= -20:
        signal = "WEAK_MOMENTUM"
    elif cms <= -5:
        signal = "NEGATIVE"
    else:
        signal = "NEUTRAL"

    return {
        "category": category_name,
        "cms_score": round(cms, 2),
        "signal": signal,
        "price_momentum": round(price_momentum, 2),
        "relative_strength": round(relative_strength, 2),
        "volume_trend": round(volume_trend, 2),
        "sentiment": round(sentiment, 2),
        "avg_return_4w": round(avg_return, 2),
        "num_tickers": len(ticker_returns)
    }


@tool
def calculate_cms(
    ticker: Annotated[str, "ticker symbol to determine category"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
) -> str:
    """
    Calculate Category Momentum Score (CMS) for the ticker's category.

    CMS measures sector momentum through:
    - Price momentum (40%)
    - Relative strength vs market (30%)
    - Volume trend (20%)
    - Sentiment (10%)

    Interpretation:
    - CMS ≥ 20: Strong sector momentum
    - CMS 5-20: Positive momentum
    - CMS -5 to 5: Neutral
    - CMS -20 to -5: Negative momentum
    - CMS ≤ -20: Weak sector momentum

    Args:
        ticker: Stock symbol (used to identify category)
        curr_date: Current date in yyyy-mm-dd format

    Returns:
        str: JSON with CMS scores for all 7 categories
    """
    config = get_config()
    categories = config.get("categories", {})

    # Find ticker's category
    ticker_category = None
    for cat_name, cat_tickers in categories.items():
        if ticker.upper() in [t.upper() for t in cat_tickers]:
            ticker_category = cat_name
            break

    # Calculate CMS for all categories
    all_cms = {}

    for category_name, category_tickers in categories.items():
        cms_result = calculate_category_momentum(
            category_name,
            category_tickers,
            curr_date,
            look_back_weeks=4
        )
        all_cms[category_name] = cms_result

    # Sort by CMS score (descending)
    sorted_categories = sorted(
        all_cms.items(),
        key=lambda x: x[1].get("cms_score", 0),
        reverse=True
    )

    result = {
        "analysis_date": curr_date,
        "ticker": ticker.upper(),
        "ticker_category": ticker_category or "Unknown",
        "category_momentum_scores": all_cms,
        "top_momentum_categories": [
            {
                "category": cat,
                "cms_score": data["cms_score"],
                "signal": data["signal"]
            }
            for cat, data in sorted_categories[:3]
        ],
        "bottom_momentum_categories": [
            {
                "category": cat,
                "cms_score": data["cms_score"],
                "signal": data["signal"]
            }
            for cat, data in sorted_categories[-3:]
        ]
    }

    return json.dumps(result, indent=2)


@tool
def get_category_rotation_signal(
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
) -> str:
    """
    Detect sector rotation signals across all 7 AI categories.

    Identifies which categories are gaining/losing momentum for
    portfolio rebalancing decisions.

    Args:
        curr_date: Current date in yyyy-mm-dd format

    Returns:
        str: JSON with rotation signals
    """
    config = get_config()
    categories = config.get("categories", {})

    # Calculate CMS for all categories
    all_cms = []

    for category_name, category_tickers in categories.items():
        cms_result = calculate_category_momentum(
            category_name,
            category_tickers,
            curr_date,
            look_back_weeks=4
        )
        all_cms.append(cms_result)

    # Sort by CMS
    all_cms.sort(key=lambda x: x.get("cms_score", 0), reverse=True)

    # Identify rotation
    gaining_momentum = [c for c in all_cms if c["cms_score"] >= 20]
    losing_momentum = [c for c in all_cms if c["cms_score"] <= -20]

    result = {
        "analysis_date": curr_date,
        "gaining_momentum": [
            {
                "category": c["category"],
                "cms_score": c["cms_score"],
                "signal": c["signal"]
            }
            for c in gaining_momentum
        ],
        "losing_momentum": [
            {
                "category": c["category"],
                "cms_score": c["cms_score"],
                "signal": c["signal"]
            }
            for c in losing_momentum
        ],
        "rotation_signal": "ROTATE_TO_STRONG" if gaining_momentum else "HOLD_DIVERSIFIED",
        "all_categories": all_cms
    }

    return json.dumps(result, indent=2)
