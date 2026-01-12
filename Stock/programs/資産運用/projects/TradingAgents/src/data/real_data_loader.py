"""
Real Data Loader
Fetches and validates real market data from Yahoo Finance.

Features:
- yfinance integration for Nikkei 225 (^N225)
- Date range: 2020-01-01 to 2025-12-31 (5 years)
- Data validation and quality checks
- Local caching to avoid repeated downloads
- Missing data detection and handling
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple
from pathlib import Path
import sys

# Add src to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


class RealDataLoader:
    """
    Loads real market data from Yahoo Finance with validation and caching.

    Example usage:
        loader = RealDataLoader(ticker="^N225", start_date="2020-01-01", end_date="2025-12-31")
        data = loader.fetch_data()

        # Save to cache
        loader.save_cache("/path/to/cache.csv")

        # Load from cache next time
        data = loader.load_cache("/path/to/cache.csv")

        # Check data quality
        quality = loader.get_data_quality()
    """

    def __init__(
        self,
        ticker: str = "^N225",
        start_date: str = "2020-01-01",
        end_date: str = "2025-12-31"
    ):
        """
        Initialize data loader.

        Args:
            ticker: Yahoo Finance ticker symbol (default: ^N225 for Nikkei 225)
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
        """
        self.ticker = ticker
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.data: Optional[pd.DataFrame] = None
        self._quality_metrics: Optional[Dict] = None

    def fetch_data(self, use_cache: bool = True, cache_path: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch market data from Yahoo Finance or cache.

        Args:
            use_cache: Try to load from cache first (default: True)
            cache_path: Path to cache file (default: None, auto-generate)

        Returns:
            DataFrame with columns: ['date', 'open', 'high', 'low', 'close', 'volume']

        Raises:
            ImportError: If yfinance is not installed
            ValueError: If data fetching fails or validation errors occur
        """
        # Auto-generate cache path if not provided
        if cache_path is None:
            cache_dir = Path(__file__).parent.parent.parent / "data" / "cache"
            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_path = str(cache_dir / f"{self.ticker.replace('^', '')}_{self.start_date.strftime('%Y%m%d')}_{self.end_date.strftime('%Y%m%d')}.csv")

        # Try loading from cache first
        if use_cache and Path(cache_path).exists():
            print(f"Loading data from cache: {cache_path}")
            try:
                self.data = self.load_cache(cache_path)
                return self.data
            except Exception as e:
                print(f"Warning: Failed to load cache ({e}), fetching fresh data...")

        # Fetch fresh data from Yahoo Finance
        try:
            import yfinance as yf
        except ImportError:
            raise ImportError(
                "yfinance is not installed. Install with: pip install yfinance"
            )

        print(f"Fetching {self.ticker} data from {self.start_date.date()} to {self.end_date.date()}...")

        try:
            # Fetch data using yfinance
            ticker_obj = yf.Ticker(self.ticker)
            df = ticker_obj.history(
                start=self.start_date,
                end=self.end_date,
                interval='1d'
            )

            if df.empty:
                raise ValueError(f"No data returned for ticker {self.ticker}")

            # Reset index to make Date a column
            df = df.reset_index()

            # Rename columns to lowercase
            df.columns = [col.lower() for col in df.columns]

            # yfinance uses 'Date' as column name
            if 'date' in df.columns:
                pass  # Already lowercase
            elif 'Date' in df.columns:
                df = df.rename(columns={'Date': 'date'})

            # Validate and clean data
            self.data = self._validate_and_clean(df)

            # Calculate quality metrics
            self._quality_metrics = self._calculate_quality_metrics(self.data)

            # Auto-save to cache
            if cache_path:
                self.save_cache(cache_path)
                print(f"Data cached to: {cache_path}")

            print(f"✅ Fetched {len(self.data)} data points")

            return self.data

        except Exception as e:
            raise ValueError(f"Error fetching data from Yahoo Finance: {e}")

    def _validate_and_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate and clean market data.

        Args:
            df: Raw DataFrame from yfinance

        Returns:
            Cleaned DataFrame with standardized format

        Raises:
            ValueError: If required columns are missing or data is invalid
        """
        # Check required columns (case-insensitive)
        df.columns = [col.lower() for col in df.columns]
        required_cols = {'date', 'open', 'high', 'low', 'close', 'volume'}
        missing_cols = required_cols - set(df.columns)

        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Select only required columns
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']].copy()

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Remove rows with missing data
        initial_count = len(df)
        df = df.dropna()
        removed_na = initial_count - len(df)
        if removed_na > 0:
            print(f"  Removed {removed_na} rows with missing data")

        # Remove rows with zero volume (non-trading days)
        initial_count = len(df)
        df = df[df['volume'] > 0]
        removed_zero_vol = initial_count - len(df)
        if removed_zero_vol > 0:
            print(f"  Removed {removed_zero_vol} rows with zero volume")

        # Sort by date (ascending)
        df = df.sort_values('date').reset_index(drop=True)

        # Convert numeric columns to float
        numeric_cols = ['open', 'high', 'low', 'close', 'volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Final validation: remove any rows that became NaN
        df = df.dropna()

        # Validate OHLC relationship (High >= Low, Close/Open within range)
        invalid_ohlc = df[(df['high'] < df['low']) |
                          (df['close'] > df['high']) |
                          (df['close'] < df['low']) |
                          (df['open'] > df['high']) |
                          (df['open'] < df['low'])]

        if len(invalid_ohlc) > 0:
            print(f"  Warning: Found {len(invalid_ohlc)} rows with invalid OHLC relationships")
            df = df.drop(invalid_ohlc.index)

        # Check date range
        if df['date'].min() > self.start_date + timedelta(days=30):
            print(f"  Warning: Data starts at {df['date'].min().date()}, expected around {self.start_date.date()}")

        if df['date'].max() < self.end_date - timedelta(days=30):
            print(f"  Warning: Data ends at {df['date'].max().date()}, expected around {self.end_date.date()}")

        return df

    def _calculate_quality_metrics(self, df: pd.DataFrame) -> Dict:
        """
        Calculate data quality metrics.

        Args:
            df: Validated DataFrame

        Returns:
            Dict with quality metrics
        """
        # Calculate expected trading days (approximately 250 per year)
        years = (self.end_date - self.start_date).days / 365.25
        expected_points = int(years * 250)
        actual_points = len(df)
        completeness = (actual_points / expected_points) * 100 if expected_points > 0 else 0

        # Detect date gaps (more than 5 days between consecutive dates)
        date_gaps = []
        if len(df) > 1:
            for i in range(1, len(df)):
                current_date = df.iloc[i]['date']
                previous_date = df.iloc[i-1]['date']
                days_diff = (current_date - previous_date).days

                if days_diff > 5:  # More than 5 days (accounting for weekends)
                    date_gaps.append({
                        'from': previous_date.strftime('%Y-%m-%d'),
                        'to': current_date.strftime('%Y-%m-%d'),
                        'days': int(days_diff)
                    })

        # Calculate price statistics
        price_stats = {
            'mean': float(df['close'].mean()),
            'std': float(df['close'].std()),
            'min': float(df['close'].min()),
            'max': float(df['close'].max()),
            'latest': float(df.iloc[-1]['close'])
        }

        return {
            'completeness': round(completeness, 2),
            'expected_points': expected_points,
            'actual_points': actual_points,
            'missing_points': max(0, expected_points - actual_points),
            'date_gaps': date_gaps,
            'date_range': {
                'start': df['date'].min().strftime('%Y-%m-%d'),
                'end': df['date'].max().strftime('%Y-%m-%d')
            },
            'price_stats': price_stats
        }

    def save_cache(self, file_path: str) -> None:
        """
        Save data to CSV cache.

        Args:
            file_path: Path to save cache file

        Raises:
            ValueError: If no data is loaded
        """
        if self.data is None:
            raise ValueError("No data to save. Call fetch_data() first.")

        # Ensure directory exists
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        # Save to CSV
        self.data.to_csv(file_path, index=False)

    def load_cache(self, file_path: str) -> pd.DataFrame:
        """
        Load data from CSV cache.

        Args:
            file_path: Path to cache file

        Returns:
            DataFrame with cached data

        Raises:
            FileNotFoundError: If cache file does not exist
            ValueError: If cache validation fails
        """
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Cache file not found: {file_path}")

        # Load CSV
        df = pd.read_csv(file_path)

        # Validate and clean
        df = self._validate_and_clean(df)

        # Update internal state
        self.data = df
        self._quality_metrics = self._calculate_quality_metrics(df)

        return df

    def get_data_quality(self) -> Dict:
        """
        Get data quality metrics.

        Returns:
            Dict with quality metrics

        Raises:
            ValueError: If no data is loaded
        """
        if self._quality_metrics is None:
            raise ValueError("No quality metrics available. Call fetch_data() first.")

        return self._quality_metrics

    def split_train_test(
        self,
        train_start: str = "2020-01-01",
        train_end: str = "2022-12-31",
        test_start: str = "2023-01-01",
        test_end: str = "2025-12-31"
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Split data into train and test sets.

        Args:
            train_start: Training period start date
            train_end: Training period end date
            test_start: Test period start date
            test_end: Test period end date

        Returns:
            Tuple of (train_data, test_data)

        Raises:
            ValueError: If no data is loaded or date ranges are invalid
        """
        if self.data is None:
            raise ValueError("No data loaded. Call fetch_data() first.")

        # Convert to datetime
        train_start = pd.to_datetime(train_start)
        train_end = pd.to_datetime(train_end)
        test_start = pd.to_datetime(test_start)
        test_end = pd.to_datetime(test_end)

        # Validate date ranges
        if train_start >= train_end:
            raise ValueError("train_start must be before train_end")
        if test_start >= test_end:
            raise ValueError("test_start must be before test_end")
        if train_end >= test_start:
            raise ValueError("train_end must be before test_start (no overlap)")

        # Split data
        train_data = self.data[
            (self.data['date'] >= train_start) &
            (self.data['date'] <= train_end)
        ].copy()

        test_data = self.data[
            (self.data['date'] >= test_start) &
            (self.data['date'] <= test_end)
        ].copy()

        print(f"Train period: {train_start.date()} to {train_end.date()} ({len(train_data)} points)")
        print(f"Test period: {test_start.date()} to {test_end.date()} ({len(test_data)} points)")

        return train_data, test_data


# Convenience function
def load_nikkei225_data(
    start_date: str = "2020-01-01",
    end_date: str = "2025-12-31",
    use_cache: bool = True
) -> pd.DataFrame:
    """
    Convenience function to load Nikkei 225 data.

    Args:
        start_date: Start date (default: 2020-01-01)
        end_date: End date (default: 2025-12-31)
        use_cache: Use cached data if available (default: True)

    Returns:
        DataFrame with OHLCV data

    Example:
        data = load_nikkei225_data()
        print(data.head())
    """
    loader = RealDataLoader(ticker="^N225", start_date=start_date, end_date=end_date)
    return loader.fetch_data(use_cache=use_cache)


# Example usage (for testing)
if __name__ == "__main__":
    print("Real Data Loader - Test Run")
    print("=" * 60)

    # Initialize loader
    loader = RealDataLoader(
        ticker="^N225",
        start_date="2020-01-01",
        end_date="2025-12-31"
    )

    print("\n1. Fetching Nikkei 225 data...")
    try:
        data = loader.fetch_data(use_cache=True)
        print(f"\n✅ Data loaded successfully!")
        print(f"   Total points: {len(data)}")
        print(f"   Date range: {data['date'].min().date()} to {data['date'].max().date()}")

        # Show sample data
        print("\nFirst 5 rows:")
        print(data.head())

        print("\nLast 5 rows:")
        print(data.tail())

        # Data quality
        print("\n2. Data Quality Metrics:")
        quality = loader.get_data_quality()
        print(f"   Completeness: {quality['completeness']}%")
        print(f"   Expected points: {quality['expected_points']}")
        print(f"   Actual points: {quality['actual_points']}")
        print(f"   Missing points: {quality['missing_points']}")

        if quality['date_gaps']:
            print(f"\n   Date gaps found: {len(quality['date_gaps'])}")
            for gap in quality['date_gaps'][:3]:  # Show first 3
                print(f"     {gap['from']} → {gap['to']} ({gap['days']} days)")

        print(f"\n   Price statistics:")
        print(f"     Mean: ¥{quality['price_stats']['mean']:,.0f}")
        print(f"     Std: ¥{quality['price_stats']['std']:,.0f}")
        print(f"     Min: ¥{quality['price_stats']['min']:,.0f}")
        print(f"     Max: ¥{quality['price_stats']['max']:,.0f}")
        print(f"     Latest: ¥{quality['price_stats']['latest']:,.0f}")

        # Train-test split
        print("\n3. Train-Test Split:")
        train_data, test_data = loader.split_train_test(
            train_start="2020-01-01",
            train_end="2022-12-31",
            test_start="2023-01-01",
            test_end="2025-12-31"
        )

        print("\n" + "=" * 60)
        print("✅ Test completed successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
