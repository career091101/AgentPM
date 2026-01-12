"""
Quick Verification Script for Walk-Forward Implementation
Tests the core functionality without pytest dependency.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from backtest.walk_forward_analyzer import WalkForwardAnalyzer
from strategy.adaptive_strategy import AdaptiveStrategy
from utils.market_regime import MarketRegimeDetector


def generate_test_data():
    """Generate 5 years of sample data."""
    dates = pd.date_range('2020-01-01', '2024-12-31', freq='D')
    np.random.seed(42)

    returns = np.random.randn(len(dates)) * 0.01
    prices = 40000 * np.exp(returns.cumsum())

    data = pd.DataFrame({
        'date': dates,
        'open': prices * (1 + np.random.randn(len(dates)) * 0.002),
        'high': prices * (1 + abs(np.random.randn(len(dates)) * 0.005)),
        'low': prices * (1 - abs(np.random.randn(len(dates)) * 0.005)),
        'close': prices,
        'volume': np.random.randint(100000, 200000, len(dates))
    })

    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index('date')

    return data


def create_strategy_function():
    """Create test strategy function."""
    regime_params = {
        'bull': {
            'ma_short': 15,
            'ma_long': 40,
            'rsi_period': 14,
            'rsi_overbought': 70,
            'rsi_oversold': 30
        },
        'bear': {
            'ma_short': 30,
            'ma_long': 60,
            'rsi_period': 14,
            'rsi_overbought': 65,
            'rsi_oversold': 30
        },
        'sideways': {
            'bb_period': 20,
            'bb_std': 2.0,
            'rsi_period': 14,
            'rsi_overbought': 70,
            'rsi_oversold': 30
        }
    }

    def strategy_function(data: pd.DataFrame, **optimization_params):
        """Generate trading signals."""
        if not isinstance(data.index, pd.DatetimeIndex):
            if 'date' in data.columns:
                data = data.set_index('date')

        detector = MarketRegimeDetector(data)
        strategy = AdaptiveStrategy(
            regime_detector=detector,
            regime_params=regime_params,
            stability_days=5,
            min_regime_confidence=0.6
        )

        signals = []
        position_open = None
        trading_dates = data.index[200:]

        for current_date in trading_dates:
            signal_info = strategy.generate_signal(data, current_date)

            action = signal_info['action']
            price = signal_info['price']
            confidence = signal_info['confidence']

            if action == 'buy' and position_open is None and confidence > 0.6:
                stop_loss_pct = optimization_params.get('stop_loss_pct', 0.02)
                risk_reward = optimization_params.get('risk_reward', 2.0)

                signals.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'action': 'buy',
                    'entry_price': price,
                    'stop_loss': price * (1 - stop_loss_pct),
                    'take_profit': price * (1 + stop_loss_pct * risk_reward),
                    'risk_reward_ratio': risk_reward,
                    'confidence': confidence,
                    'regime': signal_info['regime']
                })
                position_open = current_date

            elif action == 'sell' and position_open is not None:
                signals.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'action': 'sell',
                    'exit_price': price,
                    'confidence': confidence,
                    'regime': signal_info['regime']
                })
                position_open = None

            elif position_open is not None:
                days_held = (current_date - position_open).days
                if days_held > 30:
                    signals.append({
                        'date': current_date.strftime('%Y-%m-%d'),
                        'action': 'sell',
                        'exit_price': price,
                        'confidence': 0.5,
                        'regime': signal_info['regime'],
                        'exit_reason': 'max_hold_period'
                    })
                    position_open = None

        return signals

    return strategy_function


def test_window_splitting():
    """Test 1: Window splitting."""
    print("\n[Test 1] Window Splitting")
    print("-" * 60)

    data = generate_test_data()
    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=6,
        test_months=3,
        step_months=3
    )

    windows = analyzer.split_data()

    print(f"   Generated {len(windows)} windows")
    print(f"   Data range: {data.index.min().date()} to {data.index.max().date()}")

    assert len(windows) >= 15, f"Expected >= 15 windows, got {len(windows)}"
    assert len(windows) <= 60, f"Expected <= 60 windows, got {len(windows)}"

    # Verify first window
    train_data, test_data, train_start, test_end = windows[0]
    print(f"   First window: {train_start.date()} to {test_end.date()}")
    print(f"      Train: {len(train_data)} days")
    print(f"      Test: {len(test_data)} days")

    assert len(train_data) > 0
    assert len(test_data) > 0

    print("   ✅ PASSED")


def test_strategy_interface():
    """Test 2: Strategy interface."""
    print("\n[Test 2] Strategy Interface Compatibility")
    print("-" * 60)

    data = generate_test_data()
    strategy_function = create_strategy_function()

    # Test with small dataset
    test_data = data.iloc[:500]

    signals = strategy_function(test_data, stop_loss_pct=0.02, risk_reward=2.0)

    print(f"   Generated {len(signals)} signals")

    assert isinstance(signals, list), "Strategy should return list"
    assert len(signals) > 0, "Strategy should generate signals"

    # Verify signal format
    for signal in signals[:5]:  # Check first 5
        assert 'date' in signal
        assert 'action' in signal
        assert signal['action'] in ['buy', 'sell']

    print(f"   Sample signal: {signals[0]}")
    print("   ✅ PASSED")


def test_walkforward_execution():
    """Test 3: Walk-forward execution."""
    print("\n[Test 3] Walk-Forward Execution (2 windows)")
    print("-" * 60)

    data = generate_test_data()
    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=6,
        test_months=3,
        step_months=12  # Large step for quick test
    )

    strategy_function = create_strategy_function()

    param_grid = {
        'stop_loss_pct': [0.02],
        'risk_reward': [2.0]
    }

    print("   Running walk-forward analysis...")
    results = analyzer.run_analysis(strategy_function, param_grid)

    print(f"\n   Results:")
    print(f"      Windows: {results['num_windows']}")
    print(f"      Median Sharpe: {results['statistics']['sharpe_ratio']['median']:.3f}")
    print(f"      Positive rate: {results['positive_return_rate']:.1f}%")
    print(f"      Avg degradation: {results['avg_degradation']:.1f}%")
    print(f"      Recommendation: {results['recommendation']}")

    assert results['num_windows'] > 0
    assert 'statistics' in results
    assert 'sharpe_ratio' in results['statistics']
    assert results['recommendation'] in ['strong_pass', 'pass', 'warning', 'fail']

    print("   ✅ PASSED")


def test_statistical_calculations():
    """Test 4: Statistical calculations."""
    print("\n[Test 4] Statistical Metric Calculations")
    print("-" * 60)

    data = generate_test_data()
    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=6,
        test_months=3,
        step_months=12
    )

    strategy_function = create_strategy_function()

    param_grid = {
        'stop_loss_pct': [0.02],
        'risk_reward': [2.0]
    }

    results = analyzer.run_analysis(strategy_function, param_grid)

    stats = results['statistics']['sharpe_ratio']

    print(f"   Sharpe statistics:")
    print(f"      Mean: {stats['mean']:.3f}")
    print(f"      Median: {stats['median']:.3f}")
    print(f"      Std: {stats['std']:.3f}")
    print(f"      Q25-Q75: [{stats['q25']:.3f}, {stats['q75']:.3f}]")

    assert not np.isnan(stats['median'])
    assert not np.isinf(stats['median'])
    assert stats['std'] >= 0

    print("   ✅ PASSED")


def main():
    """Run all verification tests."""
    print("=" * 80)
    print("Walk-Forward Implementation Verification")
    print("=" * 80)

    try:
        test_window_splitting()
        test_strategy_interface()
        test_walkforward_execution()
        test_statistical_calculations()

        print("\n" + "=" * 80)
        print("✅ ALL TESTS PASSED")
        print("=" * 80)
        print("\nThe walk-forward implementation is ready for full 57-window execution.")
        print("Run: python3 scripts/run_walk_forward_full.py")

        return 0

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
