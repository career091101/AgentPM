# AI Stock Agents - Data Interface Routing
# Based on TradingAgents-main/tradingagents/dataflows/interface.py

from typing import Annotated

# Import vendor-specific modules
from .yfinance_weekly import (
    get_weekly_stock_data,
    get_weekly_indicators,
    get_all_tickers_weekly,
    get_fundamentals
)
from .sec_edgar import (
    get_insider_transactions,
    get_insider_sentiment_summary
)

# Configuration
from .config import get_config

# Tools organized by category
TOOLS_CATEGORIES = {
    "core_stock_apis": {
        "description": "Weekly OHLCV stock price data",
        "tools": [
            "get_stock_data",
            "get_batch_stock_data"
        ]
    },
    "technical_indicators": {
        "description": "Weekly technical analysis indicators",
        "tools": [
            "get_indicators"
        ]
    },
    "insider_data": {
        "description": "Insider trading data from SEC Form 4 filings",
        "tools": [
            "get_insider_transactions",
            "get_insider_sentiment"
        ]
    },
    "fundamental_data": {
        "description": "Company fundamentals and financial metrics",
        "tools": [
            "get_fundamentals"
        ]
    }
}

# Mapping of methods to their vendor-specific implementations
VENDOR_METHODS = {
    # core_stock_apis
    "get_stock_data": {
        "yfinance": get_weekly_stock_data,
    },
    "get_batch_stock_data": {
        "yfinance": get_all_tickers_weekly,
    },
    # technical_indicators
    "get_indicators": {
        "yfinance": get_weekly_indicators,
    },
    # insider_data
    "get_insider_transactions": {
        "sec_edgar": get_insider_transactions,
    },
    "get_insider_sentiment": {
        "sec_edgar": get_insider_sentiment_summary,
    },
    # fundamental_data
    "get_fundamentals": {
        "yfinance": get_fundamentals,
    },
}


def get_category_for_method(method: str) -> str:
    """Get the category that contains the specified method."""
    for category, info in TOOLS_CATEGORIES.items():
        if method in info["tools"]:
            return category
    raise ValueError(f"Method '{method}' not found in any category")


def get_vendor(category: str, method: str = None) -> str:
    """Get the configured vendor for a data category or specific tool method."""
    config = get_config()

    # Check tool-level configuration first (if method provided)
    if method:
        tool_vendors = config.get("tool_vendors", {})
        if method in tool_vendors:
            return tool_vendors[method]

    # Fall back to category-level configuration
    return config.get("data_vendors", {}).get(category, "yfinance")


def route_to_vendor(method: str, *args, **kwargs):
    """Route method calls to appropriate vendor implementation.

    Args:
        method: Method name to call (e.g., "get_stock_data", "get_indicators")
        *args: Positional arguments to pass to the vendor method
        **kwargs: Keyword arguments to pass to the vendor method

    Returns:
        Result from the vendor method

    Raises:
        ValueError: If method is not supported
        RuntimeError: If vendor implementation fails
    """
    category = get_category_for_method(method)
    vendor_config = get_vendor(category, method)

    if method not in VENDOR_METHODS:
        raise ValueError(f"Method '{method}' not supported")

    # Get vendor implementation
    vendor = vendor_config.strip()

    if vendor not in VENDOR_METHODS[method]:
        raise ValueError(
            f"Vendor '{vendor}' not supported for method '{method}'. "
            f"Available vendors: {list(VENDOR_METHODS[method].keys())}"
        )

    vendor_impl = VENDOR_METHODS[method][vendor]

    # Execute vendor method
    try:
        print(f"DEBUG: Calling {method} from vendor '{vendor}'...")
        result = vendor_impl(*args, **kwargs)
        print(f"SUCCESS: {method} from vendor '{vendor}' completed successfully")
        return result

    except Exception as e:
        error_msg = f"Failed to execute {method} from vendor '{vendor}': {str(e)}"
        print(f"ERROR: {error_msg}")
        raise RuntimeError(error_msg) from e
