# AI Stock Agents - News Sentiment Velocity (NSV) Tools
# Analyzes sentiment change rate for detecting market sentiment acceleration

from langchain_core.tools import tool
from typing import Annotated, List, Dict
import sys
from pathlib import Path
import json
from datetime import datetime, timedelta
import statistics

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dataflows.interface import route_to_vendor
from dataflows.config import get_config


def calculate_sentiment_velocity(
    ticker: str,
    curr_date: str,
    window_days: int = 7,
    look_back_days: int = 14
) -> Dict:
    """
    Calculate News Sentiment Velocity (NSV) for a stock.

    NSV = (current_avg_sentiment - previous_avg_sentiment) / window_days * 100

    Measures acceleration/deceleration of sentiment change.

    Args:
        ticker: Stock symbol
        curr_date: Current date in yyyy-mm-dd format
        window_days: Window size for averaging (default: 7)
        look_back_days: Total look-back period (default: 14)

    Returns:
        dict: NSV score and sentiment breakdown
    """
    try:
        # Fetch news data from vendor
        news_data = route_to_vendor(
            "get_news_sentiment",
            ticker,
            curr_date,
            look_back_days
        )

        if "Error" in news_data or "No data" in news_data:
            return {
                "ticker": ticker,
                "nsv_score": 0,
                "signal": "NO_DATA",
                "current_sentiment": 0,
                "previous_sentiment": 0,
                "reason": "No news data available"
            }

        # Parse news sentiment data (expecting daily sentiment scores)
        # Format: {"date": "yyyy-mm-dd", "sentiment": -1.0 to 1.0, "article_count": N}
        sentiments = json.loads(news_data)

        if not sentiments or len(sentiments) < window_days * 2:
            return {
                "ticker": ticker,
                "nsv_score": 0,
                "signal": "INSUFFICIENT_DATA",
                "current_sentiment": 0,
                "previous_sentiment": 0,
                "reason": f"Only {len(sentiments)} days of data (need {window_days * 2})"
            }

        # Sort by date
        sentiments.sort(key=lambda x: x["date"], reverse=True)

        # Calculate current window average (most recent N days)
        current_window = sentiments[:window_days]
        current_avg = statistics.mean([s["sentiment"] for s in current_window])

        # Calculate previous window average (next N days)
        previous_window = sentiments[window_days:window_days * 2]
        previous_avg = statistics.mean([s["sentiment"] for s in previous_window])

        # Calculate velocity (change per day, as percentage)
        velocity = (current_avg - previous_avg) / window_days * 100

        # Determine signal
        if velocity > 5:
            signal = "RAPID_IMPROVEMENT"
        elif velocity > 2:
            signal = "IMPROVING"
        elif velocity < -5:
            signal = "RAPID_DETERIORATION"
        elif velocity < -2:
            signal = "DETERIORATING"
        else:
            signal = "STABLE"

        return {
            "ticker": ticker,
            "nsv_score": round(velocity, 2),
            "signal": signal,
            "current_sentiment": round(current_avg, 2),
            "previous_sentiment": round(previous_avg, 2),
            "current_article_count": sum(s["article_count"] for s in current_window),
            "previous_article_count": sum(s["article_count"] for s in previous_window),
            "analysis_date": curr_date,
            "window_days": window_days
        }

    except Exception as e:
        return {
            "ticker": ticker,
            "nsv_score": 0,
            "signal": "ERROR",
            "current_sentiment": 0,
            "previous_sentiment": 0,
            "reason": f"Failed to calculate NSV: {str(e)}"
        }


@tool
def calculate_nsv(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
) -> str:
    """
    Calculate News Sentiment Velocity (NSV) for a stock.

    NSV measures the acceleration/deceleration of sentiment change:
    - NSV > +5: Rapid sentiment improvement (strong bullish signal)
    - NSV +2 to +5: Improving sentiment (bullish)
    - NSV -2 to +2: Stable sentiment (neutral)
    - NSV -5 to -2: Deteriorating sentiment (bearish)
    - NSV < -5: Rapid sentiment deterioration (strong bearish signal)

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        curr_date: Current date in yyyy-mm-dd format

    Returns:
        str: JSON with NSV score, signal, and sentiment breakdown
    """
    result = calculate_sentiment_velocity(ticker, curr_date)
    return json.dumps(result, indent=2)


@tool
def get_recent_news_headlines(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    max_headlines: Annotated[int, "maximum number of headlines to return"] = 10,
) -> str:
    """
    Get recent news headlines for a stock to understand sentiment context.

    Args:
        ticker: Stock symbol
        curr_date: Current date in yyyy-mm-dd format
        max_headlines: Maximum number of headlines to return (default: 10)

    Returns:
        str: JSON with recent headlines, dates, and sentiment scores
    """
    try:
        # Fetch recent news
        news_data = route_to_vendor(
            "get_recent_news",
            ticker,
            curr_date,
            days_back=7
        )

        if "Error" in news_data or "No data" in news_data:
            return json.dumps({
                "ticker": ticker,
                "headlines": [],
                "reason": "No news available"
            }, indent=2)

        # Parse and limit headlines
        headlines = json.loads(news_data)
        limited_headlines = headlines[:max_headlines]

        return json.dumps({
            "ticker": ticker,
            "analysis_date": curr_date,
            "headline_count": len(limited_headlines),
            "headlines": limited_headlines
        }, indent=2)

    except Exception as e:
        return json.dumps({
            "ticker": ticker,
            "headlines": [],
            "reason": f"Failed to fetch news: {str(e)}"
        }, indent=2)


@tool
def get_sentiment_trend(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    days_back: Annotated[int, "number of days to analyze"] = 30,
) -> str:
    """
    Get sentiment trend over time to visualize sentiment trajectory.

    Args:
        ticker: Stock symbol
        curr_date: Current date in yyyy-mm-dd format
        days_back: Number of days to analyze (default: 30)

    Returns:
        str: JSON with daily sentiment scores and trend direction
    """
    try:
        news_data = route_to_vendor(
            "get_news_sentiment",
            ticker,
            curr_date,
            days_back
        )

        if "Error" in news_data or "No data" in news_data:
            return json.dumps({
                "ticker": ticker,
                "trend": "NO_DATA",
                "daily_sentiment": []
            }, indent=2)

        sentiments = json.loads(news_data)
        sentiments.sort(key=lambda x: x["date"])

        # Calculate trend direction (linear regression would be ideal)
        if len(sentiments) >= 2:
            first_half = sentiments[:len(sentiments)//2]
            second_half = sentiments[len(sentiments)//2:]

            first_avg = statistics.mean([s["sentiment"] for s in first_half])
            second_avg = statistics.mean([s["sentiment"] for s in second_half])

            if second_avg > first_avg + 0.1:
                trend = "UPWARD"
            elif second_avg < first_avg - 0.1:
                trend = "DOWNWARD"
            else:
                trend = "FLAT"
        else:
            trend = "INSUFFICIENT_DATA"

        return json.dumps({
            "ticker": ticker,
            "analysis_date": curr_date,
            "trend": trend,
            "first_period_avg": round(first_avg, 2) if len(sentiments) >= 2 else 0,
            "second_period_avg": round(second_avg, 2) if len(sentiments) >= 2 else 0,
            "daily_sentiment": [
                {
                    "date": s["date"],
                    "sentiment": s["sentiment"],
                    "article_count": s["article_count"]
                }
                for s in sentiments
            ]
        }, indent=2)

    except Exception as e:
        return json.dumps({
            "ticker": ticker,
            "trend": "ERROR",
            "daily_sentiment": [],
            "reason": f"Failed to analyze trend: {str(e)}"
        }, indent=2)
