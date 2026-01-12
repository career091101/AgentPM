# AI Stock Agents - Core Stock Data Tools
# LangChain tool wrappers for weekly stock data fetching
# Based on TradingAgents-main/tradingagents/agents/utils/core_stock_tools.py

from langchain_core.tools import tool
from typing import Annotated
import sys
from pathlib import Path

# Add parent directory to path to import dataflows
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dataflows.interface import route_to_vendor


@tool
def get_stock_data(
    ticker: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "end date in yyyy-mm-dd format"],
) -> str:
    """
    Retrieve weekly OHLCV stock price data for a given ticker symbol.

    Uses the configured core_stock_apis vendor (default: yfinance).

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA", "GOOGL")
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        str: A CSV string containing weekly OHLCV data with header information
    """
    return route_to_vendor("get_stock_data", ticker, start_date, end_date)


@tool
def get_batch_stock_data(
    tickers: Annotated[list, "list of ticker symbols"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    look_back_weeks: Annotated[int, "number of weeks to look back"] = 4,
) -> dict:
    """
    Retrieve weekly stock data for multiple tickers at once (batch processing).

    Useful for Portfolio Coordinator to fetch data for all 46 companies efficiently.

    Args:
        tickers: List of stock symbols (e.g., ["MSFT", "NVDA", "GOOGL"])
        curr_date: Current date in yyyy-mm-dd format
        look_back_weeks: Number of weeks to look back (default: 4 weeks)

    Returns:
        dict: Dictionary mapping ticker -> weekly data string
    """
    return route_to_vendor("get_batch_stock_data", tickers, curr_date, look_back_weeks)


@tool
def get_fundamentals(
    ticker: Annotated[str, "ticker symbol of the company"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
) -> str:
    """
    Retrieve comprehensive fundamental data for a given ticker symbol.

    Includes company profile, valuation metrics (P/E, P/B, P/S), profitability (margins, ROE),
    growth rates, financial health (debt/equity, current ratio), and dividend info.

    Uses the configured fundamental_data vendor (default: yfinance).

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA", "GOOGL")
        curr_date: Current date in yyyy-mm-dd format

    Returns:
        str: A formatted report containing comprehensive fundamental data
    """
    return route_to_vendor("get_fundamentals", ticker, curr_date)


@tool
def get_indicators(
    ticker: Annotated[str, "ticker symbol of the company"],
    indicator: Annotated[str, "technical indicator name (close_10_sma, close_40_sma, rsi_weekly, macd_weekly, boll_weekly)"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    look_back_weeks: Annotated[int, "number of weeks to look back"] = 52,
) -> str:
    """
    Calculate weekly technical indicators for a given ticker symbol.

    Uses the configured technical_indicators vendor (default: yfinance).

    Available indicators:
    - close_10_sma: 10-week Simple Moving Average (short-term trend)
    - close_40_sma: 40-week Simple Moving Average (long-term trend, ~200-day)
    - rsi_weekly: 14-week Relative Strength Index
    - macd_weekly: MACD on weekly timeframe (8,17,9 parameters)
    - boll_weekly: Bollinger Bands on weekly data (20-week)

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        indicator: Indicator name to calculate
        curr_date: Current date in yyyy-mm-dd format
        look_back_weeks: Number of weeks to look back (default: 52 weeks = 1 year)

    Returns:
        str: A formatted report containing indicator values and interpretation
    """
    return route_to_vendor("get_indicators", ticker, indicator, curr_date, look_back_weeks)
