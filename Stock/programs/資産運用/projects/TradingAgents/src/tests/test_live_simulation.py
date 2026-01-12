"""
リアルタイムシミュレーションのテスト

Usage:
    python3 -m pytest src/tests/test_live_simulation.py -v
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.data.real_data_loader import RealDataLoader
from src.utils.market_regime import MarketRegimeDetector
from src.strategy.adaptive_strategy import AdaptiveStrategy


def test_data_fetch():
    """Test data fetching"""
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")

    loader = RealDataLoader(
        ticker="^N225",
        start_date=start_date,
        end_date=end_date
    )

    data = loader.fetch_data()

    assert data is not None
    assert len(data) > 0
    assert 'close' in data.columns
    print(f"✅ Data fetch test passed: {len(data)} points")


def test_regime_detection():
    """Test regime detection"""
    # Create sample data
    dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
    sample_data = pd.DataFrame({
        'date': dates,
        'open': np.random.randn(len(dates)).cumsum() + 40000,
        'high': np.random.randn(len(dates)).cumsum() + 40100,
        'low': np.random.randn(len(dates)).cumsum() + 39900,
        'close': np.random.randn(len(dates)).cumsum() + 40000,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    sample_data['date'] = pd.to_datetime(sample_data['date'])
    sample_data = sample_data.set_index('date')

    detector = MarketRegimeDetector(sample_data)
    regime_series = detector.detect_regime_combined()

    assert regime_series is not None
    assert len(regime_series) > 0
    assert regime_series.iloc[-1] in ['bull', 'bear', 'sideways']
    print(f"✅ Regime detection test passed: {regime_series.iloc[-1]}")


def test_signal_generation():
    """Test signal generation"""
    # Create sample data
    dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
    sample_data = pd.DataFrame({
        'date': dates,
        'open': np.random.randn(len(dates)).cumsum() + 40000,
        'high': np.random.randn(len(dates)).cumsum() + 40100,
        'low': np.random.randn(len(dates)).cumsum() + 39900,
        'close': np.random.randn(len(dates)).cumsum() + 40000,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    sample_data['date'] = pd.to_datetime(sample_data['date'])
    sample_data = sample_data.set_index('date')

    detector = MarketRegimeDetector(sample_data)

    regime_params = {
        'bull': {'ma_short': 10, 'ma_long': 30, 'position_size_pct': 1.0},
        'bear': {'ma_short': 30, 'ma_long': 60, 'position_size_pct': 0.8},
        'sideways': {'bb_period': 20, 'bb_std': 2.0, 'position_size_pct': 0.9}
    }

    strategy = AdaptiveStrategy(detector, regime_params)

    latest_date = sample_data.index[-1]
    signal = strategy.generate_signal(sample_data, latest_date)

    assert signal is not None
    assert 'action' in signal
    assert signal['action'] in ['buy', 'sell', 'hold']
    print(f"✅ Signal generation test passed: {signal['action']}")


if __name__ == "__main__":
    print("Running Live Simulation Tests")
    print("=" * 60)

    try:
        test_data_fetch()
        test_regime_detection()
        test_signal_generation()

        print("\n" + "=" * 60)
        print("✅ All tests passed")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
