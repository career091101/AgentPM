# AI Stock Agents - Weekly Data Fetcher using yfinance
# Based on TradingAgents-main/tradingagents/dataflows/y_finance.py

from typing import Annotated
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pandas as pd
import pandas_ta as ta


def get_weekly_stock_data(
    ticker: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    """
    Fetch weekly OHLCV data for a given ticker symbol.

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        CSV string with weekly OHLCV data and header information
    """
    # Validate dates
    datetime.strptime(start_date, "%Y-%m-%d")
    datetime.strptime(end_date, "%Y-%m-%d")

    # Create ticker object
    ticker_obj = yf.Ticker(ticker.upper())

    # Fetch weekly historical data
    data = ticker_obj.history(start=start_date, end=end_date, interval="1wk")

    # Check if data is empty
    if data.empty:
        return (
            f"No data found for symbol '{ticker}' between {start_date} and {end_date}"
        )

    # Remove timezone info from index for cleaner output
    if data.index.tz is not None:
        data.index = data.index.tz_localize(None)

    # Round numerical values to 2 decimal places for cleaner display
    numeric_columns = ["Open", "High", "Low", "Close"]
    for col in numeric_columns:
        if col in data.columns:
            data[col] = data[col].round(2)

    # Convert DataFrame to CSV string
    csv_string = data.to_csv()

    # Add header information
    header = f"# Weekly stock data for {ticker.upper()} from {start_date} to {end_date}\n"
    header += f"# Total weeks: {len(data)}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    return header + csv_string


def get_weekly_indicators(
    ticker: Annotated[str, "ticker symbol of the company"],
    indicator: Annotated[str, "technical indicator to get (sma10, sma40, rsi_weekly, macd_weekly, etc.)"],
    curr_date: Annotated[str, "The current trading date, YYYY-mm-dd"],
    look_back_weeks: Annotated[int, "how many weeks to look back"] = 52,
) -> str:
    """
    Calculate weekly technical indicators for a given ticker.

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        indicator: Indicator name (sma10, sma40, rsi_weekly, macd_weekly, boll_weekly)
        curr_date: Current date in yyyy-mm-dd format
        look_back_weeks: Number of weeks to look back (default: 52 weeks = 1 year)

    Returns:
        Formatted string with indicator values and interpretation
    """
    # Indicator descriptions
    indicator_descriptions = {
        "close_10_sma": (
            "10-week SMA: Short-term trend indicator for weekly analysis. "
            "Usage: Identify short-term trend direction (roughly 2.5 months). "
            "Tips: More responsive than 40-week SMA; crossovers signal trend changes."
        ),
        "close_40_sma": (
            "40-week SMA: Long-term trend benchmark (roughly 200-day SMA). "
            "Usage: Identify major trend direction and support/resistance levels. "
            "Tips: Classic long-term trend indicator; price above = bullish, below = bearish."
        ),
        "rsi_weekly": (
            "14-week RSI: Momentum indicator on weekly timeframe. "
            "Usage: Identify overbought (>70) or oversold (<30) conditions. "
            "Tips: Weekly RSI is less noisy than daily; extremes are more significant."
        ),
        "macd_weekly": (
            "MACD Weekly: MACD on weekly timeframe (8,17,9 parameters). "
            "Usage: Identify trend changes and momentum shifts on weekly basis. "
            "Tips: Weekly MACD crossovers are stronger signals than daily."
        ),
        "boll_weekly": (
            "Bollinger Bands Weekly: Volatility bands on weekly data. "
            "Usage: Measure weekly price volatility and identify extremes. "
            "Tips: Price touching upper/lower bands indicates potential reversal zones."
        ),
    }

    # Validate indicator
    if indicator not in indicator_descriptions:
        available = ", ".join(indicator_descriptions.keys())
        return f"Indicator '{indicator}' not supported. Available: {available}"

    # Parse current date
    curr_date_obj = datetime.strptime(curr_date, "%Y-%m-%d")

    # Calculate start date (look back weeks + buffer for indicator calculation)
    buffer_weeks = 50  # Extra weeks for indicator warmup
    start_date = curr_date_obj - timedelta(weeks=look_back_weeks + buffer_weeks)
    start_date_str = start_date.strftime("%Y-%m-%d")

    # Fetch weekly data
    ticker_obj = yf.Ticker(ticker.upper())
    data = ticker_obj.history(start=start_date_str, end=curr_date, interval="1wk")

    if data.empty:
        return f"No data found for {ticker} to calculate {indicator}"

    # Remove timezone
    if data.index.tz is not None:
        data.index = data.index.tz_localize(None)

    # Calculate indicators based on type
    try:
        if indicator == "close_10_sma":
            data["SMA_10"] = data["Close"].rolling(window=10).mean()
            indicator_col = "SMA_10"

        elif indicator == "close_40_sma":
            data["SMA_40"] = data["Close"].rolling(window=40).mean()
            indicator_col = "SMA_40"

        elif indicator == "rsi_weekly":
            data["RSI_14"] = ta.rsi(data["Close"], length=14)
            indicator_col = "RSI_14"

        elif indicator == "macd_weekly":
            # MACD with 8,17,9 parameters for weekly
            macd = ta.macd(data["Close"], fast=8, slow=17, signal=9)
            data = pd.concat([data, macd], axis=1)
            indicator_col = ["MACD_8_17_9", "MACDh_8_17_9", "MACDs_8_17_9"]

        elif indicator == "boll_weekly":
            # Bollinger Bands with 20-week period
            bbands = ta.bbands(data["Close"], length=20, std=2)
            data = pd.concat([data, bbands], axis=1)
            indicator_col = ["BBL_20_2.0", "BBM_20_2.0", "BBU_20_2.0"]

        else:
            return f"Indicator calculation not implemented for {indicator}"

    except Exception as e:
        return f"Error calculating {indicator} for {ticker}: {str(e)}"

    # Filter to requested look_back_weeks
    cutoff_date = curr_date_obj - timedelta(weeks=look_back_weeks)
    data = data[data.index >= cutoff_date]

    # Prepare output
    result = f"# {indicator.upper()} for {ticker.upper()}\n"
    result += f"# {indicator_descriptions[indicator]}\n"
    result += f"# Period: {look_back_weeks} weeks ending {curr_date}\n"
    result += f"# Total data points: {len(data)}\n\n"

    # Add relevant columns to output
    if isinstance(indicator_col, list):
        # Multiple columns (e.g., MACD components)
        output_cols = ["Close"] + indicator_col
    else:
        # Single column
        output_cols = ["Close", indicator_col]

    # Filter existing columns
    output_cols = [col for col in output_cols if col in data.columns]

    # Convert to CSV
    output_data = data[output_cols].dropna()
    result += output_data.round(2).to_csv()

    # Add current value summary
    if not output_data.empty:
        latest = output_data.iloc[-1]
        result += f"\n# Latest values ({output_data.index[-1].date()}):\n"
        for col in output_cols:
            result += f"# {col}: {latest[col]:.2f}\n"

    return result


def get_fundamentals(
    ticker: Annotated[str, "ticker symbol of the company"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
) -> str:
    """
    Get comprehensive fundamental data for a stock using yfinance.

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        curr_date: Current date (for reference, yfinance returns latest data)

    Returns:
        str: Formatted report with company info, financials, valuation metrics
    """
    ticker_obj = yf.Ticker(ticker.upper())

    try:
        # Get company info
        info = ticker_obj.info

        report = f"# Fundamental Analysis for {ticker.upper()}\n"
        report += f"# Analysis Date: {curr_date}\n\n"

        # Company Profile
        report += "## Company Profile\n"
        report += f"Name: {info.get('longName', 'N/A')}\n"
        report += f"Sector: {info.get('sector', 'N/A')}\n"
        report += f"Industry: {info.get('industry', 'N/A')}\n"
        report += f"Market Cap: ${info.get('marketCap', 0):,.0f}\n"
        report += f"Employees: {info.get('fullTimeEmployees', 'N/A')}\n\n"

        # Valuation Metrics
        report += "## Valuation Metrics\n"
        report += f"P/E Ratio (TTM): {info.get('trailingPE', 'N/A')}\n"
        report += f"Forward P/E: {info.get('forwardPE', 'N/A')}\n"
        report += f"PEG Ratio: {info.get('pegRatio', 'N/A')}\n"
        report += f"Price/Book: {info.get('priceToBook', 'N/A')}\n"
        report += f"Price/Sales: {info.get('priceToSalesTrailing12Months', 'N/A')}\n"
        report += f"EV/Revenue: {info.get('enterpriseToRevenue', 'N/A')}\n"
        report += f"EV/EBITDA: {info.get('enterpriseToEbitda', 'N/A')}\n\n"

        # Profitability
        report += "## Profitability\n"
        report += f"Profit Margin: {info.get('profitMargins', 'N/A')}\n"
        report += f"Operating Margin: {info.get('operatingMargins', 'N/A')}\n"
        report += f"ROE: {info.get('returnOnEquity', 'N/A')}\n"
        report += f"ROA: {info.get('returnOnAssets', 'N/A')}\n\n"

        # Growth
        report += "## Growth\n"
        report += f"Revenue Growth (YoY): {info.get('revenueGrowth', 'N/A')}\n"
        report += f"Earnings Growth (YoY): {info.get('earningsGrowth', 'N/A')}\n"
        report += f"Revenue (TTM): ${info.get('totalRevenue', 0):,.0f}\n\n"

        # Financial Health
        report += "## Financial Health\n"
        report += f"Total Cash: ${info.get('totalCash', 0):,.0f}\n"
        report += f"Total Debt: ${info.get('totalDebt', 0):,.0f}\n"
        report += f"Debt/Equity: {info.get('debtToEquity', 'N/A')}\n"
        report += f"Current Ratio: {info.get('currentRatio', 'N/A')}\n"
        report += f"Quick Ratio: {info.get('quickRatio', 'N/A')}\n\n"

        # Dividend
        report += "## Dividend Info\n"
        report += f"Dividend Yield: {info.get('dividendYield', 'N/A')}\n"
        report += f"Payout Ratio: {info.get('payoutRatio', 'N/A')}\n\n"

        # AI-specific metrics (if available)
        report += "## AI-Specific Notes\n"
        report += f"Business Summary: {info.get('longBusinessSummary', 'N/A')[:500]}...\n"

        return report

    except Exception as e:
        return f"Error retrieving fundamentals for {ticker}: {str(e)}"


def get_all_tickers_weekly(
    tickers: Annotated[list, "list of ticker symbols"],
    curr_date: Annotated[str, "The current trading date, YYYY-mm-dd"],
    look_back_weeks: Annotated[int, "how many weeks to look back"] = 4,
) -> dict:
    """
    Fetch weekly data for multiple tickers at once (batch processing).

    Args:
        tickers: List of stock symbols (e.g., ["MSFT", "NVDA", "GOOGL"])
        curr_date: Current date in yyyy-mm-dd format
        look_back_weeks: Number of weeks to look back (default: 4 weeks)

    Returns:
        Dictionary mapping ticker -> weekly data string
    """
    curr_date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    start_date = curr_date_obj - timedelta(weeks=look_back_weeks + 1)
    start_date_str = start_date.strftime("%Y-%m-%d")

    results = {}

    for ticker in tickers:
        try:
            data = get_weekly_stock_data(ticker, start_date_str, curr_date)
            results[ticker] = data
        except Exception as e:
            results[ticker] = f"Error fetching {ticker}: {str(e)}"

    return results
