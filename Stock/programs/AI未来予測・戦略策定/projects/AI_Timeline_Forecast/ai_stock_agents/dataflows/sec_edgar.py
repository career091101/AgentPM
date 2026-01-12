# AI Stock Agents - SEC EDGAR Form 4 Fetcher
# Fetches insider trading data from SEC EDGAR database

from typing import Annotated
from datetime import datetime, timedelta
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os


class SECEdgarClient:
    """
    SEC EDGAR API client for Form 4 insider trading data.

    SEC requires a User-Agent header and limits requests to 10 per second.
    Form 4 filings report insider transactions within 2 business days.
    """

    def __init__(self, user_agent=None):
        """
        Initialize SEC EDGAR client.

        Args:
            user_agent: User-Agent string (required by SEC)
                       Format: "Company Name/Version (email)"
        """
        self.user_agent = user_agent or os.getenv(
            "SEC_USER_AGENT",
            "AI Stock Agents/1.0 (contact@example.com)"
        )
        self.base_url = "https://www.sec.gov"
        self.rate_limit_delay = 0.1  # 10 requests/second = 0.1s delay

    def _make_request(self, url):
        """Make HTTP request to SEC with proper headers and rate limiting."""
        headers = {
            "User-Agent": self.user_agent,
            "Accept-Encoding": "gzip, deflate",
            "Host": "www.sec.gov"
        }

        time.sleep(self.rate_limit_delay)  # Respect rate limit

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        return response

    def get_cik(self, ticker):
        """
        Get CIK (Central Index Key) for a given ticker symbol.

        Args:
            ticker: Stock symbol (e.g., "MSFT")

        Returns:
            str: 10-digit CIK with leading zeros
        """
        # SEC provides a ticker to CIK mapping
        url = "https://www.sec.gov/cgi-bin/browse-edgar"
        params = {
            "action": "getcompany",
            "company": ticker.upper(),
            "type": "4",  # Form 4
            "dateb": "",
            "owner": "exclude",
            "output": "atom",
            "count": 1
        }

        try:
            response = self._make_request(url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))

            # Parse XML response to get CIK
            soup = BeautifulSoup(response.content, "xml")
            cik = soup.find("CIK")

            if cik:
                # Pad CIK to 10 digits
                return cik.text.zfill(10)
            else:
                return None

        except Exception as e:
            print(f"Error getting CIK for {ticker}: {e}")
            return None

    def get_form4_filings(self, ticker, start_date, end_date, max_filings=100):
        """
        Get Form 4 filings for a ticker within a date range.

        Args:
            ticker: Stock symbol (e.g., "MSFT")
            start_date: Start date in yyyy-mm-dd format
            end_date: End date in yyyy-mm-dd format
            max_filings: Maximum number of filings to retrieve

        Returns:
            list: List of dictionaries with filing metadata
        """
        cik = self.get_cik(ticker)

        if not cik:
            return []

        # Search for Form 4 filings
        url = "https://www.sec.gov/cgi-bin/browse-edgar"
        params = {
            "action": "getcompany",
            "CIK": cik,
            "type": "4",
            "dateb": end_date.replace("-", ""),
            "datea": start_date.replace("-", ""),
            "owner": "include",  # Include insider transactions
            "output": "atom",
            "count": max_filings
        }

        try:
            response = self._make_request(url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))

            # Parse XML response
            soup = BeautifulSoup(response.content, "xml")
            entries = soup.find_all("entry")

            filings = []

            for entry in entries:
                filing_date = entry.find("filing-date")
                filing_href = entry.find("filing-href")

                if filing_date and filing_href:
                    filings.append({
                        "filing_date": filing_date.text,
                        "filing_url": filing_href.text
                    })

            return filings

        except Exception as e:
            print(f"Error fetching Form 4 filings for {ticker}: {e}")
            return []

    def parse_form4_xml(self, xml_content):
        """
        Parse Form 4 XML to extract transaction details.

        Args:
            xml_content: Raw XML content of Form 4

        Returns:
            list: List of transaction dictionaries
        """
        try:
            root = ET.fromstring(xml_content)

            transactions = []

            # Find all non-derivative transactions
            for trans in root.findall(".//nonDerivativeTransaction"):
                transaction_date = trans.find(".//transactionDate/value")
                transaction_code = trans.find(".//transactionCode")
                transaction_shares = trans.find(".//transactionShares/value")
                transaction_price = trans.find(".//transactionPricePerShare/value")

                # Get reporter information (from ownershipDocument level)
                reporting_owner = root.find(".//reportingOwner")
                owner_name = reporting_owner.find(".//rptOwnerName") if reporting_owner else None

                # Determine if insider or 10b5-1 plan
                is_10b5_1 = trans.find(".//transactionCoding/equitySwapInvolved")

                if transaction_date is not None and transaction_code is not None:
                    trans_code = transaction_code.text
                    trans_type = "BUY" if trans_code in ["P", "M"] else "SELL" if trans_code in ["S"] else "OTHER"

                    transactions.append({
                        "date": transaction_date.text if transaction_date is not None else None,
                        "type": trans_type,
                        "shares": float(transaction_shares.text) if transaction_shares is not None else 0,
                        "price_per_share": float(transaction_price.text) if transaction_price is not None else 0,
                        "owner": owner_name.text if owner_name is not None else "Unknown",
                        "is_10b5_1": is_10b5_1 is not None and is_10b5_1.text == "1"
                    })

            return transactions

        except Exception as e:
            print(f"Error parsing Form 4 XML: {e}")
            return []


def get_insider_transactions(
    ticker: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "end date in yyyy-mm-dd format"],
) -> str:
    """
    Fetch insider trading transactions from SEC EDGAR Form 4 filings.

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA")
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        str: CSV string with insider transaction data and header information
    """
    client = SECEdgarClient()

    # Get Form 4 filings
    filings = client.get_form4_filings(ticker, start_date, end_date)

    if not filings:
        return f"No Form 4 filings found for {ticker} between {start_date} and {end_date}"

    all_transactions = []

    # Parse each filing (limit to first 20 to avoid rate limiting issues)
    for filing in filings[:20]:
        try:
            # Fetch the actual Form 4 XML
            response = client._make_request(filing["filing_url"])

            # SEC returns HTML page with link to XML - need to extract XML URL
            soup = BeautifulSoup(response.content, "html.parser")
            xml_link = soup.find("a", text=lambda t: t and ".xml" in t.lower())

            if xml_link:
                xml_url = client.base_url + xml_link["href"]
                xml_response = client._make_request(xml_url)

                transactions = client.parse_form4_xml(xml_response.content)

                for trans in transactions:
                    trans["filing_date"] = filing["filing_date"]
                    all_transactions.append(trans)

        except Exception as e:
            print(f"Error processing filing {filing['filing_url']}: {e}")
            continue

    if not all_transactions:
        return f"No insider transactions found in Form 4 filings for {ticker}"

    # Convert to DataFrame for CSV output
    df = pd.DataFrame(all_transactions)

    # Sort by date
    df = df.sort_values("date", ascending=False)

    # Convert to CSV
    csv_string = df.to_csv(index=False)

    # Add header information
    header = f"# Insider Transactions (SEC Form 4) for {ticker.upper()}\n"
    header += f"# Date range: {start_date} to {end_date}\n"
    header += f"# Total transactions: {len(all_transactions)}\n"
    header += f"# Total filings processed: {min(len(filings), 20)}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    return header + csv_string


def get_insider_sentiment_summary(
    ticker: Annotated[str, "ticker symbol of the company"],
    curr_date: Annotated[str, "current date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "number of days to look back"] = 90,
) -> str:
    """
    Get insider sentiment summary (net buying/selling) for a ticker.

    Args:
        ticker: Stock symbol (e.g., "MSFT")
        curr_date: Current date in yyyy-mm-dd format
        look_back_days: Number of days to look back (default: 90 days)

    Returns:
        str: Summary of insider sentiment
    """
    curr_date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    start_date = curr_date_obj - timedelta(days=look_back_days)
    start_date_str = start_date.strftime("%Y-%m-%d")

    # Get transactions
    transactions_csv = get_insider_transactions(ticker, start_date_str, curr_date)

    if "No" in transactions_csv or "Error" in transactions_csv:
        return transactions_csv

    # Parse CSV to calculate summary
    lines = transactions_csv.split("\n")
    data_lines = [line for line in lines if not line.startswith("#") and line.strip()]

    if len(data_lines) <= 1:  # Only header
        return f"No insider transactions for {ticker} in the past {look_back_days} days"

    # Calculate net sentiment
    total_buys = 0
    total_sells = 0
    total_buy_value = 0
    total_sell_value = 0

    for line in data_lines[1:]:  # Skip header
        fields = line.split(",")
        if len(fields) >= 4:
            trans_type = fields[1]
            shares = float(fields[2]) if fields[2] else 0
            price = float(fields[3]) if fields[3] else 0
            value = shares * price

            if trans_type == "BUY":
                total_buys += shares
                total_buy_value += value
            elif trans_type == "SELL":
                total_sells += shares
                total_sell_value += value

    net_shares = total_buys - total_sells
    net_value = total_buy_value - total_sell_value

    sentiment = "BULLISH" if net_value > 0 else "BEARISH" if net_value < 0 else "NEUTRAL"

    summary = f"# Insider Sentiment Summary for {ticker.upper()}\n"
    summary += f"# Period: {look_back_days} days ending {curr_date}\n\n"
    summary += f"Total Buy Transactions: {total_buys:,.0f} shares (${total_buy_value:,.2f})\n"
    summary += f"Total Sell Transactions: {total_sells:,.0f} shares (${total_sell_value:,.2f})\n"
    summary += f"Net Position: {net_shares:,.0f} shares (${net_value:,.2f})\n"
    summary += f"Sentiment: {sentiment}\n"

    return summary
