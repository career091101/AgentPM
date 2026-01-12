"""
Yahoo Finance Data Parser
Parses and validates OHLCV data from Yahoo Finance.

Note: This module does NOT fetch data directly (Yahoo Finance requires cookie auth).
Data should be fetched by agent-data-collector skill using WebFetch tool,
then passed to this module for parsing and validation.
"""

import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import io
import json


class YahooFinanceParser:
    """
    Parses and validates market data from Yahoo Finance.

    Data should be fetched by agent-data-collector skill using WebFetch,
    then passed to this parser for validation and cleaning.

    Example usage:
        parser = YahooFinanceParser()

        # Parse CSV text (from WebFetch)
        data = parser.parse_csv(csv_text)

        # Parse JSON array (from WebFetch JSON extraction)
        data = parser.parse_json(json_array)

        # Calculate data quality
        quality = parser.calculate_data_quality(data, years=5)
    """

    def parse_csv(self, csv_text: str) -> pd.DataFrame:
        """
        Parse Yahoo Finance CSV data.

        Args:
            csv_text: CSV text data fetched from Yahoo Finance

        Returns:
            DataFrame with columns: ['date', 'open', 'high', 'low', 'close', 'volume']

        Raises:
            ValueError: If CSV parsing fails or required columns missing
        """
        try:
            # Parse CSV
            df = pd.read_csv(io.StringIO(csv_text))

            # Validate and clean
            df = self._validate_and_clean(df)

            return df

        except Exception as e:
            raise ValueError(f"Error parsing Yahoo Finance CSV: {e}")

    def parse_json(self, json_data: List[Dict]) -> pd.DataFrame:
        """
        Parse JSON array of OHLCV data.

        Args:
            json_data: List of dicts with keys: date, open, high, low, close, volume

        Returns:
            DataFrame with columns: ['date', 'open', 'high', 'low', 'close', 'volume']

        Raises:
            ValueError: If JSON parsing fails or required keys missing

        Example input:
            [
                {"date": "2020-01-01", "open": 23000, "high": 23200, "low": 22800, "close": 23100, "volume": 1000000},
                ...
            ]
        """
        try:
            df = pd.DataFrame(json_data)

            # Standardize column names (lowercase)
            df.columns = [col.lower() for col in df.columns]

            # Validate and clean
            df = self._validate_and_clean(df)

            return df

        except Exception as e:
            raise ValueError(f"Error parsing JSON data: {e}")

    def _validate_and_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate and clean market data.

        Args:
            df: Raw DataFrame with market data

        Returns:
            Cleaned DataFrame with standardized columns

        Raises:
            ValueError: If required columns are missing
        """
        # Standardize column names to lowercase
        df.columns = [col.lower() for col in df.columns]

        # Check required columns (lowercase)
        required_cols = {'date', 'open', 'high', 'low', 'close', 'volume'}
        missing_cols = required_cols - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Select only required columns
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']]

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Remove rows with missing data
        df = df.dropna()

        # Remove rows with zero volume (non-trading days)
        df = df[df['volume'] > 0]

        # Sort by date (ascending order)
        df = df.sort_values('date').reset_index(drop=True)

        # Convert numeric columns to float
        numeric_cols = ['open', 'high', 'low', 'close', 'volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Final validation: remove any rows that became NaN
        df = df.dropna()

        return df

    def calculate_data_quality(self, df: pd.DataFrame, years: int = 5) -> Dict:
        """
        Calculate data quality metrics.

        Args:
            df: DataFrame with market data
            years: Expected number of years

        Returns:
            Dict with quality metrics: {
                'completeness': float (percentage),
                'expected_points': int,
                'actual_points': int,
                'missing_points': int,
                'date_gaps': List[Dict]
            }
        """
        # Expected data points (approximately 250 trading days per year)
        expected_points = years * 250
        actual_points = len(df)
        missing_points = max(0, expected_points - actual_points)
        completeness = (actual_points / expected_points) * 100

        # Detect date gaps (more than 5 days between consecutive dates)
        date_gaps = []
        if len(df) > 1:
            df_sorted = df.sort_values('date')
            for i in range(1, len(df_sorted)):
                current_date = df_sorted.iloc[i]['date']
                previous_date = df_sorted.iloc[i-1]['date']
                days_diff = (current_date - previous_date).days

                if days_diff > 5:  # More than 5 days (accounting for weekends)
                    date_gaps.append({
                        'from': previous_date.strftime('%Y-%m-%d'),
                        'to': current_date.strftime('%Y-%m-%d'),
                        'days': int(days_diff)
                    })

        return {
            'completeness': round(completeness, 2),
            'expected_points': expected_points,
            'actual_points': actual_points,
            'missing_points': missing_points,
            'date_gaps': date_gaps
        }

    def get_latest_price(self, df: pd.DataFrame) -> Optional[Dict]:
        """
        Extract latest price from DataFrame.

        Args:
            df: DataFrame with OHLCV data

        Returns:
            Dict with latest price data or None if DataFrame is empty
        """
        if len(df) == 0:
            return None

        latest = df.iloc[-1]

        return {
            'price': float(latest['close']),
            'open': float(latest['open']),
            'high': float(latest['high']),
            'low': float(latest['low']),
            'volume': int(latest['volume']),
            'date': latest['date'].strftime('%Y-%m-%d') if isinstance(latest['date'], pd.Timestamp) else latest['date']
        }


# Convenience function for CSV parsing
def parse_yahoo_csv(csv_text: str) -> pd.DataFrame:
    """
    Convenience function to parse Yahoo Finance CSV data.

    Args:
        csv_text: CSV text from Yahoo Finance

    Returns:
        DataFrame with OHLCV data

    Example:
        # After fetching CSV with WebFetch
        data = parse_yahoo_csv(csv_text)
        print(data.head())
    """
    parser = YahooFinanceParser()
    return parser.parse_csv(csv_text)


def parse_yahoo_json(json_data: List[Dict]) -> pd.DataFrame:
    """
    Convenience function to parse JSON OHLCV data.

    Args:
        json_data: List of dicts with OHLCV data

    Returns:
        DataFrame with OHLCV data

    Example:
        data = parse_yahoo_json(json_array)
        print(data.head())
    """
    parser = YahooFinanceParser()
    return parser.parse_json(json_data)


# Example usage (for testing with sample data)
if __name__ == "__main__":
    print("Yahoo Finance Parser - Test Run")
    print("=" * 60)

    # Sample JSON data (simulating WebFetch results)
    sample_json = [
        {"date": "2025-12-23", "open": 39900, "high": 40100, "low": 39800, "close": 40000, "volume": 100000},
        {"date": "2025-12-24", "open": 40000, "high": 40200, "low": 39950, "close": 40150, "volume": 120000},
        {"date": "2025-12-25", "open": 40150, "high": 40300, "low": 40100, "close": 40250, "volume": 110000},
        {"date": "2025-12-26", "open": 40250, "high": 40400, "low": 40200, "close": 40350, "volume": 130000},
        {"date": "2025-12-27", "open": 40350, "high": 40500, "low": 40300, "close": 40450, "volume": 140000},
    ]

    parser = YahooFinanceParser()

    print("\n1. Parsing JSON data...")
    try:
        data = parser.parse_json(sample_json)
        print(f"✅ Success! Parsed {len(data)} data points")
        print(f"\nData:")
        print(data)

        # Get latest price
        print("\n2. Extract latest price...")
        latest = parser.get_latest_price(data)
        if latest:
            print(f"✅ Latest data:")
            print(f"  Date: {latest['date']}")
            print(f"  Close: ¥{latest['price']:,.0f}")
            print(f"  High: ¥{latest['high']:,.0f}")
            print(f"  Low: ¥{latest['low']:,.0f}")
            print(f"  Volume: {latest['volume']:,}")

        # Data quality (with small sample)
        print("\n3. Data Quality Assessment (sample data):")
        quality = parser.calculate_data_quality(data, years=5)
        print(f"Expected points (5 years): {quality['expected_points']}")
        print(f"Actual points: {quality['actual_points']}")
        print(f"Completeness: {quality['completeness']}%")

        print("\n" + "=" * 60)
        print("✅ Parser test completed")
        print("\nNote: Actual data fetching should be done by agent-data-collector skill using WebFetch")

    except Exception as e:
        print(f"❌ Error: {e}")
