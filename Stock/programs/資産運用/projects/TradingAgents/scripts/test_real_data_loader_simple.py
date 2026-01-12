"""
Simple test runner for RealDataLoader (without pytest dependency)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import tempfile
import shutil

# Add src to path
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from data.real_data_loader import RealDataLoader


def create_sample_data():
    """Create sample OHLCV data."""
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


def test_initialization():
    """Test RealDataLoader initialization."""
    print("Testing initialization...", end=" ")
    loader = RealDataLoader(
        ticker="^N225",
        start_date="2020-01-01",
        end_date="2025-12-31"
    )

    assert loader.ticker == "^N225"
    assert loader.start_date == pd.to_datetime("2020-01-01")
    assert loader.end_date == pd.to_datetime("2025-12-31")
    assert loader.data is None
    print("✅ PASS")


def test_validate_and_clean():
    """Test data validation and cleaning."""
    print("Testing validate_and_clean...", end=" ")
    loader = RealDataLoader()

    # Create test data with issues
    data = pd.DataFrame({
        'DATE': pd.date_range('2020-01-01', periods=10),
        'OPEN': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        'HIGH': [105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
        'LOW': [95, 96, 97, 98, 99, 100, 101, 102, 103, 104],
        'CLOSE': [103, 104, 105, 106, None, 108, 109, 110, 111, 112],
        'VOLUME': [1000, 2000, 3000, 4000, 5000, 0, 7000, 8000, 9000, 10000]
    })

    cleaned = loader._validate_and_clean(data)

    # Check column names are lowercase
    assert all(col.islower() for col in cleaned.columns)

    # Check required columns exist
    assert set(cleaned.columns) == {'date', 'open', 'high', 'low', 'close', 'volume'}

    # Check missing data and zero volume removed
    assert len(cleaned) == 8

    # Check data types
    assert cleaned['date'].dtype == 'datetime64[ns]'
    assert cleaned['close'].dtype == float

    print("✅ PASS")


def test_cache_save_load():
    """Test cache save and load functionality."""
    print("Testing cache save/load...", end=" ")

    temp_dir = tempfile.mkdtemp()
    try:
        loader = RealDataLoader()
        sample_data = create_sample_data()
        loader.data = sample_data

        cache_path = str(Path(temp_dir) / "test_cache.csv")

        # Save cache
        loader.save_cache(cache_path)
        assert Path(cache_path).exists()

        # Load cache
        loader2 = RealDataLoader()
        loaded_data = loader2.load_cache(cache_path)

        assert len(loaded_data) == len(sample_data)
        assert list(loaded_data.columns) == ['date', 'open', 'high', 'low', 'close', 'volume']

        print("✅ PASS")
    finally:
        shutil.rmtree(temp_dir)


def test_quality_metrics():
    """Test data quality metrics calculation."""
    print("Testing quality metrics...", end=" ")
    loader = RealDataLoader(start_date="2020-01-01", end_date="2020-12-31")
    sample_data = create_sample_data()
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

    print("✅ PASS")


def test_split_train_test():
    """Test train/test split functionality."""
    print("Testing train/test split...", end=" ")
    loader = RealDataLoader()
    sample_data = create_sample_data()
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

    print("✅ PASS")


def test_error_handling():
    """Test error handling."""
    print("Testing error handling...", end=" ")
    loader = RealDataLoader()

    # Test save without data
    try:
        loader.save_cache("/tmp/test.csv")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Test load nonexistent file
    try:
        loader.load_cache("/nonexistent/path/cache.csv")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected

    # Test get_quality_metrics without data
    try:
        loader.get_data_quality()
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Test split_train_test without data
    try:
        loader.split_train_test()
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    print("✅ PASS")


def test_invalid_ohlc():
    """Test that invalid OHLC relationships are removed."""
    print("Testing invalid OHLC removal...", end=" ")
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

    print("✅ PASS")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("RUNNING UNIT TESTS FOR REALDATALOADER")
    print("=" * 80 + "\n")

    tests = [
        test_initialization,
        test_validate_and_clean,
        test_cache_save_load,
        test_quality_metrics,
        test_split_train_test,
        test_error_handling,
        test_invalid_ohlc
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ FAIL: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1

    print("\n" + "=" * 80)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 80 + "\n")

    if failed == 0:
        print("✅ ALL TESTS PASSED")
        return 0
    else:
        print(f"❌ {failed} TEST(S) FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
