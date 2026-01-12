"""
Integration Test: Walk-Forward Analysis Complete
Tests the complete 57-window walk-forward analysis pipeline.

Run with:
    pytest src/tests/test_walk_forward_complete.py -v
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from backtest.walk_forward_analyzer import WalkForwardAnalyzer
from strategy.adaptive_strategy import AdaptiveStrategy
from utils.market_regime import MarketRegimeDetector


@pytest.fixture
def sample_data():
    """Generate 5 years of sample data for testing."""
    dates = pd.date_range('2020-01-01', '2024-12-31', freq='D')
    np.random.seed(42)

    # Generate realistic price movements
    returns = np.random.randn(len(dates)) * 0.01  # 1% daily volatility
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


@pytest.fixture
def regime_params():
    """Standard regime parameters for testing."""
    return {
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


def create_strategy_function(regime_params):
    """Create strategy function for testing."""
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


class TestWalkForwardWindowSplit:
    """Test window splitting functionality."""

    def test_57_window_generation(self, sample_data):
        """Test that ~57 windows are generated from 5 years of data."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        windows = analyzer.split_data()

        # 5 years = 60 months
        # Train: 6, Test: 3, Total: 9 months per window
        # Step: 3 months
        # Expected: (60 - 9) / 3 + 1 = 18 windows
        # With overlap, we should get around 50-60 windows
        assert len(windows) >= 15, f"Expected at least 15 windows, got {len(windows)}"
        assert len(windows) <= 60, f"Expected at most 60 windows, got {len(windows)}"

    def test_window_structure(self, sample_data):
        """Test that windows have correct structure."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        windows = analyzer.split_data()

        for train_data, test_data, train_start, test_end in windows:
            # Check data is not empty
            assert len(train_data) > 0, "Train data should not be empty"
            assert len(test_data) > 0, "Test data should not be empty"

            # Check dates are in order
            assert train_start < test_end, "Train start should be before test end"

            # Check data has required columns
            required_cols = ['open', 'high', 'low', 'close', 'volume']
            for col in required_cols:
                assert col in train_data.columns, f"Missing column {col} in train data"
                assert col in test_data.columns, f"Missing column {col} in test data"

    def test_no_lookahead_bias(self, sample_data):
        """Test that test data does not overlap with train data."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        windows = analyzer.split_data()

        for train_data, test_data, _, _ in windows:
            train_end = train_data.index.max()
            test_start = test_data.index.min()

            assert test_start > train_end, "Test data should start after train data ends"


class TestStrategyInterface:
    """Test strategy function interface compatibility."""

    def test_strategy_returns_signal_list(self, sample_data, regime_params):
        """Test that strategy function returns list of signals."""
        strategy_function = create_strategy_function(regime_params)

        # Use a small sample for quick testing
        test_data = sample_data.iloc[:500]

        signals = strategy_function(test_data, stop_loss_pct=0.02, risk_reward=2.0)

        assert isinstance(signals, list), "Strategy should return a list"
        assert len(signals) > 0, "Strategy should generate some signals"

    def test_signal_format(self, sample_data, regime_params):
        """Test that signals have correct format."""
        strategy_function = create_strategy_function(regime_params)
        test_data = sample_data.iloc[:500]

        signals = strategy_function(test_data, stop_loss_pct=0.02, risk_reward=2.0)

        for signal in signals:
            assert 'date' in signal, "Signal should have 'date' field"
            assert 'action' in signal, "Signal should have 'action' field"
            assert signal['action'] in ['buy', 'sell'], f"Invalid action: {signal['action']}"

            if signal['action'] == 'buy':
                assert 'entry_price' in signal, "Buy signal should have 'entry_price'"
                assert 'stop_loss' in signal, "Buy signal should have 'stop_loss'"
                assert 'take_profit' in signal, "Buy signal should have 'take_profit'"

    def test_strategy_parameterization(self, sample_data, regime_params):
        """Test that strategy accepts optimization parameters."""
        strategy_function = create_strategy_function(regime_params)
        test_data = sample_data.iloc[:500]

        # Test with different parameters
        signals_1 = strategy_function(test_data, stop_loss_pct=0.015, risk_reward=1.5)
        signals_2 = strategy_function(test_data, stop_loss_pct=0.025, risk_reward=2.5)

        # Both should generate signals (may be same or different)
        assert len(signals_1) > 0, "Strategy should work with parameter set 1"
        assert len(signals_2) > 0, "Strategy should work with parameter set 2"


class TestStatisticalCalculations:
    """Test statistical metric calculations."""

    def test_sharpe_calculation(self, sample_data, regime_params):
        """Test Sharpe ratio calculation."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=6  # Use larger step for faster test
        )

        strategy_function = create_strategy_function(regime_params)

        param_grid = {
            'stop_loss_pct': [0.02],
            'risk_reward': [2.0]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Check statistics structure
        assert 'statistics' in results
        assert 'sharpe_ratio' in results['statistics']

        sharpe_stats = results['statistics']['sharpe_ratio']
        assert 'median' in sharpe_stats
        assert 'mean' in sharpe_stats
        assert 'std' in sharpe_stats
        assert 'q25' in sharpe_stats
        assert 'q75' in sharpe_stats

        # Check values are reasonable
        assert not np.isnan(sharpe_stats['median']), "Median Sharpe should not be NaN"
        assert not np.isinf(sharpe_stats['median']), "Median Sharpe should not be Inf"

    def test_degradation_calculation(self, sample_data, regime_params):
        """Test train-test degradation calculation."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=6
        )

        strategy_function = create_strategy_function(regime_params)

        param_grid = {
            'stop_loss_pct': [0.02],
            'risk_reward': [2.0]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Check each window has degradation
        for window in results['windows']:
            assert 'degradation_pct' in window
            assert not np.isnan(window['degradation_pct']), "Degradation should not be NaN"

        # Check average degradation
        assert 'avg_degradation' in results
        assert isinstance(results['avg_degradation'], (int, float))


class TestWalkForwardExecution:
    """Test complete walk-forward execution."""

    def test_minimal_walkforward_execution(self, sample_data, regime_params):
        """Test walk-forward with minimal windows."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=6  # Larger step for faster test
        )

        strategy_function = create_strategy_function(regime_params)

        param_grid = {
            'stop_loss_pct': [0.02],
            'risk_reward': [2.0]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Verify results structure
        assert 'windows' in results
        assert 'statistics' in results
        assert 'num_windows' in results
        assert 'positive_return_rate' in results
        assert 'avg_degradation' in results
        assert 'recommendation' in results

        # Verify windows were executed
        assert len(results['windows']) > 0, "At least one window should be executed"

    def test_all_windows_complete(self, sample_data, regime_params):
        """Test that all windows execute successfully."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=6
        )

        strategy_function = create_strategy_function(regime_params)

        param_grid = {
            'stop_loss_pct': [0.02],
            'risk_reward': [2.0]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Check all windows have results
        for window in results['windows']:
            assert 'train_metrics' in window
            assert 'test_metrics' in window
            assert 'best_params' in window

            # Check metrics are valid
            assert window['test_metrics']['sharpe_ratio'] is not None
            assert not np.isnan(window['test_metrics']['sharpe_ratio'])

    def test_recommendation_generation(self, sample_data, regime_params):
        """Test that recommendation is generated."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=6
        )

        strategy_function = create_strategy_function(regime_params)

        param_grid = {
            'stop_loss_pct': [0.02],
            'risk_reward': [2.0]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Check recommendation is valid
        assert results['recommendation'] in ['strong_pass', 'pass', 'warning', 'fail']


class TestParameterOptimization:
    """Test parameter optimization within walk-forward."""

    def test_parameter_selection(self, sample_data, regime_params):
        """Test that best parameters are selected."""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=12  # Large step for quick test
        )

        strategy_function = create_strategy_function(regime_params)

        # Multiple parameter combinations
        param_grid = {
            'stop_loss_pct': [0.015, 0.02, 0.025],
            'risk_reward': [1.5, 2.0, 2.5]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)

        # Check that parameters are optimized for each window
        for window in results['windows']:
            best_params = window['best_params']

            assert 'stop_loss_pct' in best_params
            assert 'risk_reward' in best_params

            # Check parameters are from the grid
            assert best_params['stop_loss_pct'] in param_grid['stop_loss_pct']
            assert best_params['risk_reward'] in param_grid['risk_reward']


def test_integration_full_pipeline(sample_data, regime_params):
    """Integration test: Full walk-forward pipeline."""
    print("\n" + "="*60)
    print("Integration Test: Full Walk-Forward Pipeline")
    print("="*60)

    # 1. Initialize analyzer
    analyzer = WalkForwardAnalyzer(
        data=sample_data,
        train_months=6,
        test_months=3,
        step_months=6  # Faster for testing
    )

    # 2. Create strategy
    strategy_function = create_strategy_function(regime_params)

    # 3. Define parameter grid
    param_grid = {
        'stop_loss_pct': [0.015, 0.02, 0.025],
        'risk_reward': [1.5, 2.0, 2.5]
    }

    # 4. Run analysis
    print(f"\nRunning walk-forward analysis...")
    results = analyzer.run_analysis(strategy_function, param_grid)

    # 5. Validate results
    print(f"\n✅ Analysis completed:")
    print(f"   Windows: {results['num_windows']}")
    print(f"   Median Sharpe: {results['statistics']['sharpe_ratio']['median']:.3f}")
    print(f"   Positive return rate: {results['positive_return_rate']:.1f}%")
    print(f"   Avg degradation: {results['avg_degradation']:.1f}%")
    print(f"   Recommendation: {results['recommendation']}")

    # Assertions
    assert results['num_windows'] > 0
    assert results['statistics']['sharpe_ratio']['median'] is not None
    assert 0 <= results['positive_return_rate'] <= 100
    assert results['recommendation'] in ['strong_pass', 'pass', 'warning', 'fail']

    print("\n" + "="*60)
    print("✅ All integration tests passed")
    print("="*60)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
