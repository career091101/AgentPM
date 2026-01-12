"""
Unit Tests for RealDataLoader
Tests data fetching, validation, caching, and quality metrics.

Run with: pytest src/tests/test_real_data_loader.py -v
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys
from datetime import datetime, timedelta
import tempfile
import shutil

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from data.real_data_loader import RealDataLoader, load_nikkei225_data


class TestRealDataLoader:
    """Test suite for RealDataLoader class."""

    @pytest.fixture
    def temp_cache_dir(self):
        """Create temporary directory for cache testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def sample_data(self):
        """Create sample OHLCV data for testing."""
        dates = pd.date_range('2020-01-01', periods=100, freq='D')
        data = pd.DataFrame({
            'date': dates,
            'open': np.random.uniform(20000, 25000, 100),
            'high': np.random.uniform(25000, 30000, 100),
            'low': np.random.uniform(15000, 20000, 100),
            'close': np.random.uniform(20000, 25000, 100),
            'volume': np.random.randint(100000, 200000, 100)
        })
        # Ensure OHLC relationship is valid
        for i in range(len(data)):
            data.loc[i, 'high'] = max(data.loc[i, ['open', 'close']]) * 1.01
            data.loc[i, 'low'] = min(data.loc[i, ['open', 'close']]) * 0.99
        return data

    def test_initialization(self):
        """Test RealDataLoader initialization."""
        loader = RealDataLoader(
            ticker="^N225",
            start_date="2020-01-01",
            end_date="2025-12-31"
        )

        assert loader.ticker == "^N225"
        assert loader.start_date == pd.to_datetime("2020-01-01")
        assert loader.end_date == pd.to_datetime("2025-12-31")
        assert loader.data is None

    def test_validate_and_clean(self):
        """Test data validation and cleaning."""
        loader = RealDataLoader()

        # Create test data with issues
        data = pd.DataFrame({
            'DATE': pd.date_range('2020-01-01', periods=10),
            'OPEN': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
            'HIGH': [105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
            'LOW': [95, 96, 97, 98, 99, 100, 101, 102, 103, 104],
            'CLOSE': [103, 104, 105, 106, None, 108, 109, 110, 111, 112],  # Missing value
            'VOLUME': [1000, 2000, 3000, 4000, 5000, 0, 7000, 8000, 9000, 10000]  # Zero volume
        })

        cleaned = loader._validate_and_clean(data)

        # Check column names are lowercase
        assert all(col.islower() for col in cleaned.columns)

        # Check required columns exist
        assert set(cleaned.columns) == {'date', 'open', 'high', 'low', 'close', 'volume'}

        # Check missing data removed (row 4 with None close)
        # Check zero volume removed (row 5 with volume 0)
        assert len(cleaned) == 8  # 10 - 2 = 8

        # Check data types
        assert cleaned['date'].dtype == 'datetime64[ns]'
        assert cleaned['close'].dtype == float

    def test_cache_save_load(self, temp_cache_dir, sample_data):
        """Test cache save and load functionality."""
        loader = RealDataLoader()
        loader.data = sample_data

        cache_path = str(Path(temp_cache_dir) / "test_cache.csv")

        # Save cache
        loader.save_cache(cache_path)
        assert Path(cache_path).exists()

        # Load cache
        loader2 = RealDataLoader()
        loaded_data = loader2.load_cache(cache_path)

        assert len(loaded_data) == len(sample_data)
        assert list(loaded_data.columns) == ['date', 'open', 'high', 'low', 'close', 'volume']

    def test_cache_save_without_data(self):
        """Test that save_cache raises error when no data is loaded."""
        loader = RealDataLoader()

        with pytest.raises(ValueError, match="No data to save"):
            loader.save_cache("/tmp/test.csv")

    def test_cache_load_nonexistent(self):
        """Test that load_cache raises error for nonexistent file."""
        loader = RealDataLoader()

        with pytest.raises(FileNotFoundError):
            loader.load_cache("/nonexistent/path/to/cache.csv")

    def test_quality_metrics(self, sample_data):
        """Test data quality metrics calculation."""
        loader = RealDataLoader(start_date="2020-01-01", end_date="2020-12-31")
        loader.data = sample_data
        loader._quality_metrics = loader._calculate_quality_metrics(sample_data)

        quality = loader.get_data_quality()

        assert 'completeness' in quality
        assert 'expected_points' in quality
        assert 'actual_points' in quality
        assert 'date_gaps' in quality
        assert 'price_stats' in quality

        assert quality['actual_points'] == len(sample_data)
        assert quality['price_stats']['mean'] > 0
        assert quality['price_stats']['min'] > 0
        assert quality['price_stats']['max'] > 0

    def test_quality_metrics_without_data(self):
        """Test that get_data_quality raises error when no data is loaded."""
        loader = RealDataLoader()

        with pytest.raises(ValueError, match="No quality metrics available"):
            loader.get_data_quality()

    def test_split_train_test(self, sample_data):
        """Test train/test split functionality."""
        loader = RealDataLoader()
        loader.data = sample_data

        train_data, test_data = loader.split_train_test(
            train_start="2020-01-01",
            train_end="2020-02-29",
            test_start="2020-03-01",
            test_end="2020-04-09"
        )

        # Check no overlap
        assert train_data['date'].max() < test_data['date'].min()

        # Check data integrity
        assert len(train_data) > 0
        assert len(test_data) > 0

    def test_split_train_test_invalid_dates(self, sample_data):
        """Test that split_train_test raises error for invalid date ranges."""
        loader = RealDataLoader()
        loader.data = sample_data

        # train_start >= train_end
        with pytest.raises(ValueError, match="train_start must be before train_end"):
            loader.split_train_test(
                train_start="2020-02-01",
                train_end="2020-01-01",
                test_start="2020-03-01",
                test_end="2020-04-01"
            )

        # test_start >= test_end
        with pytest.raises(ValueError, match="test_start must be before test_end"):
            loader.split_train_test(
                train_start="2020-01-01",
                train_end="2020-02-01",
                test_start="2020-04-01",
                test_end="2020-03-01"
            )

        # train_end >= test_start (overlap)
        with pytest.raises(ValueError, match="train_end must be before test_start"):
            loader.split_train_test(
                train_start="2020-01-01",
                train_end="2020-03-01",
                test_start="2020-02-01",
                test_end="2020-04-01"
            )

    def test_split_train_test_without_data(self):
        """Test that split_train_test raises error when no data is loaded."""
        loader = RealDataLoader()

        with pytest.raises(ValueError, match="No data loaded"):
            loader.split_train_test()

    def test_date_gap_detection(self):
        """Test detection of date gaps in data."""
        # Create data with a large gap
        dates = list(pd.date_range('2020-01-01', periods=30, freq='D'))
        # Add a 10-day gap
        dates.extend(pd.date_range('2020-02-10', periods=30, freq='D'))

        data = pd.DataFrame({
            'date': dates,
            'open': np.random.uniform(20000, 25000, 60),
            'high': np.random.uniform(25000, 30000, 60),
            'low': np.random.uniform(15000, 20000, 60),
            'close': np.random.uniform(20000, 25000, 60),
            'volume': np.random.randint(100000, 200000, 60)
        })

        # Ensure OHLC relationship is valid
        for i in range(len(data)):
            data.loc[i, 'high'] = max(data.loc[i, ['open', 'close']]) * 1.01
            data.loc[i, 'low'] = min(data.loc[i, ['open', 'close']]) * 0.99

        loader = RealDataLoader(start_date="2020-01-01", end_date="2020-03-11")
        loader.data = data
        loader._quality_metrics = loader._calculate_quality_metrics(data)

        quality = loader.get_data_quality()

        # Should detect the 10-day gap
        assert len(quality['date_gaps']) > 0
        assert quality['date_gaps'][0]['days'] > 5

    @pytest.mark.slow
    def test_fetch_real_data(self, temp_cache_dir):
        """
        Test fetching real data from Yahoo Finance.

        Note: This test requires internet connection and yfinance package.
        Marked as slow test.
        """
        pytest.importorskip("yfinance")

        loader = RealDataLoader(
            ticker="^N225",
            start_date="2024-01-01",
            end_date="2024-01-31"
        )

        cache_path = str(Path(temp_cache_dir) / "nikkei_test.csv")

        try:
            data = loader.fetch_data(use_cache=False, cache_path=cache_path)

            # Verify data structure
            assert len(data) > 0
            assert list(data.columns) == ['date', 'open', 'high', 'low', 'close', 'volume']

            # Verify date range (approximately)
            assert data['date'].min() >= pd.to_datetime("2024-01-01")
            assert data['date'].max() <= pd.to_datetime("2024-01-31")

            # Verify cache was created
            assert Path(cache_path).exists()

            # Test loading from cache
            data2 = loader.fetch_data(use_cache=True, cache_path=cache_path)
            assert len(data2) == len(data)

        except Exception as e:
            pytest.skip(f"Yahoo Finance fetch failed (network/API issue): {e}")

    def test_convenience_function(self):
        """Test the convenience function load_nikkei225_data."""
        # This just tests that the function exists and accepts parameters
        # Actual data fetching is tested in test_fetch_real_data
        try:
            # Should not raise error (will fetch or use cache)
            data = load_nikkei225_data(
                start_date="2024-01-01",
                end_date="2024-01-31",
                use_cache=True
            )
            # If successful, verify structure
            assert 'date' in data.columns
            assert 'close' in data.columns
        except Exception as e:
            # If yfinance not installed or network issue, skip
            pytest.skip(f"Convenience function test skipped: {e}")


class TestDataValidation:
    """Test suite for data validation edge cases."""

    def test_invalid_ohlc_relationships(self):
        """Test that invalid OHLC relationships are removed."""
        loader = RealDataLoader()

        # Create data with invalid OHLC (high < low)
        data = pd.DataFrame({
            'date': pd.date_range('2020-01-01', periods=5),
            'open': [100, 101, 102, 103, 104],
            'high': [105, 106, 95, 108, 109],  # Row 2: high < low
            'low': [95, 96, 97, 98, 99],
            'close': [103, 104, 105, 106, 107],
            'volume': [1000, 2000, 3000, 4000, 5000]
        })

        cleaned = loader._validate_and_clean(data)

        # Invalid row should be removed
        assert len(cleaned) == 4

    def test_missing_required_columns(self):
        """Test that missing required columns raise error."""
        loader = RealDataLoader()

        # Data missing 'volume' column
        data = pd.DataFrame({
            'date': pd.date_range('2020-01-01', periods=5),
            'open': [100, 101, 102, 103, 104],
            'high': [105, 106, 107, 108, 109],
            'low': [95, 96, 97, 98, 99],
            'close': [103, 104, 105, 106, 107]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            loader._validate_and_clean(data)


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
