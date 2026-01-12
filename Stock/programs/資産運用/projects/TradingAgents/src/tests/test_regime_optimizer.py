"""
Test cases for RegimeSpecificOptimizer
"""

import unittest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType
from strategy.regime_specific_optimizer import RegimeSpecificOptimizer


class TestRegimeSpecificOptimizer(unittest.TestCase):
    """Test cases for regime-specific parameter optimizer."""

    @classmethod
    def setUpClass(cls):
        """Set up test data once for all tests."""
        # Create sample data with clear bull/bear/sideways periods
        dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')

        # Create trending data
        trend = np.zeros(len(dates))
        trend[:600] = np.linspace(0, 1000, 600)  # Bull period
        trend[600:1200] = np.linspace(1000, 500, 600)  # Bear period
        trend[1200:] = np.random.randn(len(dates) - 1200).cumsum() * 10 + 500  # Sideways

        cls.sample_data = pd.DataFrame({
            'date': dates,
            'open': trend + np.random.randn(len(dates)) * 50,
            'high': trend + np.random.randn(len(dates)) * 50 + 100,
            'low': trend + np.random.randn(len(dates)) * 50 - 100,
            'close': trend + np.random.randn(len(dates)) * 50,
            'volume': np.random.randint(1000, 10000, len(dates))
        })
        cls.sample_data['date'] = pd.to_datetime(cls.sample_data['date'])
        cls.sample_data = cls.sample_data.set_index('date')

        # Create detector
        cls.detector = MarketRegimeDetector(cls.sample_data)

        # Dummy backtest function
        def dummy_backtest(data, **params):
            ma_short = params.get('ma_short', 20)
            ma_long = params.get('ma_long', 50)

            sharpe = 1.5 * (ma_short / ma_long) * np.random.uniform(0.8, 1.2)

            return {
                'sharpe_ratio': sharpe,
                'total_return': sharpe * 15,
                'win_rate': 55,
                'max_drawdown': 12
            }

        cls.backtest_fn = dummy_backtest

    def test_initialization(self):
        """Test optimizer initialization."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        self.assertIsNotNone(optimizer.regime_series)
        self.assertIsNotNone(optimizer.regime_periods)

    def test_get_regime_data(self):
        """Test regime data extraction."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        # Get bull regime data
        bull_data = optimizer.get_regime_data(RegimeType.BULL)
        self.assertGreater(len(bull_data), 0)
        self.assertIsInstance(bull_data, pd.DataFrame)

        # Verify data has required columns
        self.assertIn('close', bull_data.columns)
        self.assertIn('high', bull_data.columns)
        self.assertIn('low', bull_data.columns)

    def test_optimize_for_regime(self):
        """Test single regime optimization."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        param_grid = {
            'ma_short': [10, 15, 20],
            'ma_long': [30, 40, 50]
        }

        result = optimizer.optimize_for_regime(
            regime_type=RegimeType.BULL,
            param_grid=param_grid,
            metric='sharpe_ratio'
        )

        # Verify result structure
        self.assertIn('regime', result)
        self.assertIn('best_params', result)
        self.assertIn('best_score', result)
        self.assertIn('regime_stats', result)

        # Verify best params are from grid
        self.assertIn(result['best_params']['ma_short'], param_grid['ma_short'])
        self.assertIn(result['best_params']['ma_long'], param_grid['ma_long'])

    def test_optimize_all_regimes(self):
        """Test optimization for all regimes."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        param_grids = {
            'bull': {'ma_short': [10, 15], 'ma_long': [30, 40]},
            'bear': {'ma_short': [20, 30], 'ma_long': [50, 60]},
            'sideways': {'ma_short': [15, 20], 'ma_long': [40, 50]}
        }

        results = optimizer.optimize_all_regimes(param_grids)

        # Verify all regimes were optimized
        self.assertEqual(len(results), 3)
        self.assertIn('bull', results)
        self.assertIn('bear', results)
        self.assertIn('sideways', results)

        # Verify each result has required fields
        for regime, result in results.items():
            if 'error' not in result:
                self.assertIn('best_params', result)
                self.assertIn('best_score', result)

    def test_backtest_regime_specific(self):
        """Test regime-specific backtesting."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        regime_params = {
            'bull': {'ma_short': 15, 'ma_long': 40},
            'bear': {'ma_short': 30, 'ma_long': 60},
            'sideways': {'ma_short': 20, 'ma_long': 50}
        }

        results = optimizer.backtest_regime_specific(regime_params)

        # Verify result structure
        self.assertIn('by_regime', results)
        self.assertIn('overall', results)

        # Verify each regime has results
        self.assertEqual(len(results['by_regime']), 3)

        # Verify overall statistics
        self.assertIn('weighted_sharpe_ratio', results['overall'])
        self.assertIn('total_days', results['overall'])

    def test_compare_with_baseline(self):
        """Test baseline comparison."""
        optimizer = RegimeSpecificOptimizer(
            data=self.sample_data,
            regime_detector=self.detector,
            backtest_function=self.backtest_fn
        )

        regime_params = {
            'bull': {'ma_short': 15, 'ma_long': 40},
            'bear': {'ma_short': 30, 'ma_long': 60},
            'sideways': {'ma_short': 20, 'ma_long': 50}
        }

        baseline_params = {'ma_short': 20, 'ma_long': 50}

        comparison = optimizer.compare_with_baseline(
            regime_params=regime_params,
            baseline_params=baseline_params,
            metric='sharpe_ratio'
        )

        # Verify comparison structure
        self.assertIn('regime_specific', comparison)
        self.assertIn('baseline', comparison)
        self.assertIn('improvements', comparison)
        self.assertIn('overall_improvement', comparison)

        # Verify improvements calculated for all regimes
        self.assertEqual(len(comparison['improvements']), 3)

        for regime, improvement in comparison['improvements'].items():
            self.assertIn('regime_score', improvement)
            self.assertIn('baseline_score', improvement)
            self.assertIn('improvement_pct', improvement)

    def test_empty_regime_handling(self):
        """Test handling of regimes with no data."""
        # Create data with only one regime
        dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
        monotonic_data = pd.DataFrame({
            'date': dates,
            'open': np.linspace(100, 200, len(dates)),
            'high': np.linspace(101, 201, len(dates)),
            'low': np.linspace(99, 199, len(dates)),
            'close': np.linspace(100, 200, len(dates)),
            'volume': np.random.randint(1000, 10000, len(dates))
        })
        monotonic_data['date'] = pd.to_datetime(monotonic_data['date'])
        monotonic_data = monotonic_data.set_index('date')

        detector = MarketRegimeDetector(monotonic_data)
        optimizer = RegimeSpecificOptimizer(
            data=monotonic_data,
            regime_detector=detector,
            backtest_function=self.backtest_fn
        )

        # Should handle regimes with insufficient data gracefully
        param_grids = {
            'bull': {'ma_short': [10, 15], 'ma_long': [30, 40]},
            'bear': {'ma_short': [20, 30], 'ma_long': [50, 60]},
            'sideways': {'ma_short': [15, 20], 'ma_long': [40, 50]}
        }

        results = optimizer.optimize_all_regimes(param_grids)

        # At least one regime should have results
        self.assertGreater(len(results), 0)


if __name__ == '__main__':
    unittest.main()
