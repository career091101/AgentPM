# AI Stock Agents - Insider Trading Signal (ITS) Calculation
# Based on SEC Form 4 analysis with role-weighted scoring

from langchain_core.tools import tool
from typing import Annotated, Dict, List
import sys
from pathlib import Path
import pandas as pd
from datetime import datetime

# Add parent directory to path to import dataflows
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dataflows.interface import route_to_vendor


# Role weight mapping based on position importance
ROLE_WEIGHTS = {
    "CEO": 3.0,
    "CFO": 3.0,
    "COO": 2.5,
    "CTO": 2.5,
    "President": 3.0,
    "Vice President": 2.0,
    "Director": 1.0,
    "Officer": 1.5,
    "10% Owner": 2.0,
    "Other": 0.5,
}


def parse_role(owner_name: str) -> str:
    """
    Infer role from owner name/title.

    Args:
        owner_name: Name/title from Form 4

    Returns:
        str: Inferred role category
    """
    owner_upper = owner_name.upper()

    # Check for specific roles
    if "CEO" in owner_upper or "CHIEF EXECUTIVE" in owner_upper:
        return "CEO"
    elif "CFO" in owner_upper or "CHIEF FINANCIAL" in owner_upper:
        return "CFO"
    elif "COO" in owner_upper or "CHIEF OPERATING" in owner_upper:
        return "COO"
    elif "CTO" in owner_upper or "CHIEF TECHNOLOGY" in owner_upper:
        return "CTO"
    elif "PRESIDENT" in owner_upper:
        return "President"
    elif "VICE PRESIDENT" in owner_upper or "VP" in owner_upper:
        return "Vice President"
    elif "DIRECTOR" in owner_upper:
        return "Director"
    elif "OFFICER" in owner_upper:
        return "Officer"
    elif "10%" in owner_upper or "BENEFICIAL OWNER" in owner_upper:
        return "10% Owner"
    else:
        return "Other"


def calculate_its_from_transactions(
    transactions: List[Dict],
    market_cap: float
) -> Dict:
    """
    Calculate Insider Trading Signal (ITS) from transaction data.

    Formula:
        net_value = Σ (value × role_weight × (0.3 if 10b5-1 else 1.0))
        ITS = (net_value / market_cap) × 10000

    Cluster Bonus: If 3+ insiders buy, multiply net_value by 1.3

    Args:
        transactions: List of transaction dictionaries with keys:
                     - type: "BUY" or "SELL"
                     - shares: number of shares
                     - price_per_share: price per share
                     - owner: owner name/title
                     - is_10b5_1: whether it's a 10b5-1 plan transaction
        market_cap: Company market capitalization in dollars

    Returns:
        dict: ITS score and breakdown
    """
    net_value = 0
    buy_count = 0
    sell_count = 0
    total_buy_value = 0
    total_sell_value = 0

    for trans in transactions:
        trans_type = trans.get("type", "OTHER")
        shares = trans.get("shares", 0)
        price = trans.get("price_per_share", 0)
        owner = trans.get("owner", "Unknown")
        is_10b5_1 = trans.get("is_10b5_1", False)

        # Calculate transaction value
        value = shares * price

        # Get role weight
        role = parse_role(owner)
        weight = ROLE_WEIGHTS.get(role, 0.5)

        # Reduce weight for 10b5-1 plan transactions
        if is_10b5_1:
            weight *= 0.3

        # Apply sign based on transaction type
        if trans_type == "BUY":
            net_value += value * weight
            buy_count += 1
            total_buy_value += value
        elif trans_type == "SELL":
            net_value -= value * weight
            sell_count += 1
            total_sell_value += value

    # Cluster bonus: 3+ insiders buying
    if buy_count >= 3:
        net_value *= 1.3

    # Normalize by market cap
    if market_cap > 0:
        its = (net_value / market_cap) * 10000
    else:
        its = 0

    # Determine signal
    if its >= 0.1:
        signal = "BULLISH"
    elif its <= -0.1:
        signal = "BEARISH"
    else:
        signal = "NEUTRAL"

    return {
        "its_score": its,
        "signal": signal,
        "buy_count": buy_count,
        "sell_count": sell_count,
        "total_buy_value": total_buy_value,
        "total_sell_value": total_sell_value,
        "net_value_weighted": net_value,
        "cluster_bonus_applied": buy_count >= 3
    }


@tool
def calculate_its(
    ticker: Annotated[str, "ticker symbol of the company"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "number of days to look back"] = 90,
    market_cap: Annotated[float, "company market capitalization in USD"] = None,
) -> str:
    """
    Calculate Insider Trading Signal (ITS) for a given ticker.

    ITS measures insider sentiment through SEC Form 4 filings with:
    - Role-weighted scoring (CEO/CFO: 3.0, Director: 1.0, etc.)
    - 10b5-1 plan discount (0.3x weight)
    - Cluster bonus (1.3x if 3+ insiders buy)
    - Market cap normalization

    Interpretation:
    - ITS ≥ 0.1: BULLISH (insider net buying)
    - ITS ≤ -0.1: BEARISH (insider net selling)
    - |ITS| < 0.1: NEUTRAL

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        curr_date: Current date in yyyy-mm-dd format
        look_back_days: Number of days to look back (default: 90 days)
        market_cap: Company market capitalization (if not provided, will estimate from price × shares)

    Returns:
        str: Formatted ITS analysis report
    """
    # Calculate start date
    curr_date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    from datetime import timedelta
    start_date = curr_date_obj - timedelta(days=look_back_days)
    start_date_str = start_date.strftime("%Y-%m-%d")

    # Fetch insider transactions
    transactions_csv = route_to_vendor(
        "get_insider_transactions",
        ticker,
        start_date_str,
        curr_date
    )

    if "No" in transactions_csv or "Error" in transactions_csv:
        return transactions_csv

    # Parse CSV to extract transactions
    lines = transactions_csv.split("\n")
    data_lines = [line for line in lines if not line.startswith("#") and line.strip()]

    if len(data_lines) <= 1:  # Only header
        return f"No insider transactions for {ticker} in the past {look_back_days} days"

    transactions = []

    for line in data_lines[1:]:  # Skip header
        fields = line.split(",")
        if len(fields) >= 6:
            try:
                transactions.append({
                    "date": fields[0],
                    "type": fields[1],
                    "shares": float(fields[2]) if fields[2] else 0,
                    "price_per_share": float(fields[3]) if fields[3] else 0,
                    "owner": fields[4],
                    "is_10b5_1": fields[5].strip().lower() == "true" if len(fields) > 5 else False
                })
            except (ValueError, IndexError):
                continue

    # Estimate market cap if not provided
    if market_cap is None:
        # Use a simple estimate: average price × estimated shares outstanding
        # This is rough - in production, fetch from yfinance
        avg_price = sum(t["price_per_share"] for t in transactions if t["price_per_share"] > 0) / max(len([t for t in transactions if t["price_per_share"] > 0]), 1)
        # Rough estimate: assume large cap (100B shares for major companies)
        market_cap = avg_price * 1_000_000_000  # Very rough estimate

    # Calculate ITS
    its_result = calculate_its_from_transactions(transactions, market_cap)

    # Format report
    report = f"# Insider Trading Signal (ITS) for {ticker.upper()}\n"
    report += f"# Analysis period: {look_back_days} days ending {curr_date}\n"
    report += f"# Market cap: ${market_cap:,.0f}\n\n"

    report += f"**ITS Score: {its_result['its_score']:.4f}**\n"
    report += f"**Signal: {its_result['signal']}**\n\n"

    report += f"Transaction Summary:\n"
    report += f"- Buy transactions: {its_result['buy_count']} (${its_result['total_buy_value']:,.2f})\n"
    report += f"- Sell transactions: {its_result['sell_count']} (${its_result['total_sell_value']:,.2f})\n"
    report += f"- Net weighted value: ${its_result['net_value_weighted']:,.2f}\n"
    report += f"- Cluster bonus applied: {'Yes' if its_result['cluster_bonus_applied'] else 'No'}\n\n"

    # Interpretation
    report += f"Interpretation:\n"
    if its_result['signal'] == "BULLISH":
        report += f"Strong insider buying signal. Insiders are net buyers, indicating positive outlook.\n"
    elif its_result['signal'] == "BEARISH":
        report += f"Insider selling signal. Insiders are net sellers, may indicate concerns.\n"
    else:
        report += f"Neutral insider activity. No significant directional bias.\n"

    return report


@tool
def get_insider_transactions_raw(
    ticker: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "end date in yyyy-mm-dd format"],
) -> str:
    """
    Get raw insider trading transactions from SEC Form 4 filings.

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        str: CSV string with insider transaction data
    """
    return route_to_vendor("get_insider_transactions", ticker, start_date, end_date)


@tool
def get_insider_sentiment(
    ticker: Annotated[str, "ticker symbol of the company"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "number of days to look back"] = 90,
) -> str:
    """
    Get insider sentiment summary (simple net buying/selling).

    Args:
        ticker: Stock symbol (e.g., "MSFT")
        curr_date: Current date in yyyy-mm-dd format
        look_back_days: Number of days to look back (default: 90 days)

    Returns:
        str: Summary of insider sentiment
    """
    return route_to_vendor("get_insider_sentiment", ticker, curr_date, look_back_days)
