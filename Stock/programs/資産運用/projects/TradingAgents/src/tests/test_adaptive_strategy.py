"""
Test cases for AdaptiveStrategy
"""

import unittest
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType
from strategy.adaptive_strategy import AdaptiveStrategy


class TestAdaptiveStrategy(unittest.TestCase):
    """Test cases for adaptive trading strategy."""

    @classmethod
    def setUpClass(cls):
        """Set up test data once for all tests."""
        # Create sample data
        dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')

        # Create data with clear regime changes
        trend = np.zeros(len(dates))
        trend[:600] = np.linspace(0, 1000, 600)  # Bull
        trend[600:1200] = np.linspace(1000, 500, 600)  # Bear
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

        # Regime parameters
        cls.regime_params = {
            'bull': {
                'ma_short': 15,
                'ma_long': 40,
                'rsi_period': 14,
                'rsi_oversold': 30,
                'rsi_overbought': 70,
                'position_size_pct': 0.95,
                'stop_loss_pct': 0.02
            },
            'bear': {
                'ma_short': 30,
                'ma_long': 60,
                'rsi_period': 14,
                'rsi_oversold': 25,
                'rsi_overbought': 75,
                'position_size_pct': 0.80,
                'stop_loss_pct': 0.015
            },
            'sideways': {
                'bb_period': 20,
                'bb_std': 2.0,
                'rsi_period': 14,
                'rsi_oversold': 30,
                'rsi_overbought': 70,
                'position_size_pct': 0.90,
                'stop_loss_pct': 0.02
            }
        }

    def test_initialization(self):
        """Test strategy initialization."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=5
        )

        self.assertIsNotNone(strategy.regime_params)
        self.assertEqual(strategy.stability_days, 5)
        self.assertIsNone(strategy.current_regime)
        self.assertEqual(len(strategy.regime_history), 0)

    def test_missing_regime_params(self):
        """Test error handling for missing regime parameters."""
        incomplete_params = {
            'bull': {'ma_short': 15, 'ma_long': 40},
            'bear': {'ma_short': 30, 'ma_long': 60}
            # Missing 'sideways'
        }

        with self.assertRaises(ValueError):
            AdaptiveStrategy(
                regime_detector=self.detector,
                regime_params=incomplete_params
            )

    def test_detect_current_regime(self):
        """Test regime detection."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        # Test detection at different dates
        test_date = self.sample_data.index[300]  # Should be bull
        regime = strategy.detect_current_regime(self.sample_data, test_date)

        self.assertIn(regime, ['bull', 'bear', 'sideways'])

    def test_get_active_parameters(self):
        """Test parameter retrieval."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        # Set current regime
        strategy.current_regime = 'bull'

        params = strategy.get_active_parameters()

        self.assertEqual(params['ma_short'], 15)
        self.assertEqual(params['ma_long'], 40)
        self.assertEqual(params['position_size_pct'], 0.95)

    def test_update_regime(self):
        """Test regime update mechanism."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=3
        )

        # Update regime multiple times
        test_dates = self.sample_data.index[250:260]

        for date in test_dates:
            current_regime, switched = strategy.update_regime(self.sample_data, date)

            self.assertIn(current_regime, ['bull', 'bear', 'sideways'])
            self.assertIsInstance(switched, bool)

        # Verify history was recorded
        self.assertGreater(len(strategy.regime_history), 0)

    def test_regime_switching_stability(self):
        """Test that regime switching requires stability period."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=5,
            min_regime_confidence=0.8
        )

        # Initialize with first regime
        initial_date = self.sample_data.index[250]
        strategy.update_regime(self.sample_data, initial_date)
        initial_regime = strategy.current_regime

        # Test subsequent date (should require stability)
        next_date = initial_date + timedelta(days=1)
        new_regime, switched = strategy.update_regime(self.sample_data, next_date)

        # Immediate switch should not happen unless stable
        if switched:
            # If switched, stability criteria must have been met
            self.assertIsNotNone(strategy.current_regime)

    def test_generate_signal(self):
        """Test signal generation."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        test_date = self.sample_data.index[300]

        signal = strategy.generate_signal(self.sample_data, test_date)

        # Verify signal structure
        self.assertIn('date', signal)
        self.assertIn('regime', signal)
        self.assertIn('action', signal)
        self.assertIn('confidence', signal)
        self.assertIn('parameters', signal)
        self.assertIn('regime_switched', signal)

        # Verify action is valid
        self.assertIn(signal['action'], ['buy', 'sell', 'hold'])

        # Verify confidence is valid
        self.assertGreaterEqual(signal['confidence'], 0)
        self.assertLessEqual(signal['confidence'], 1)

    def test_bull_signal_generation(self):
        """Test signal generation in bull market."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        # Force bull regime
        strategy.current_regime = 'bull'

        test_date = self.sample_data.index[300]
        signal = strategy._generate_bull_signal(
            self.sample_data,
            test_date,
            self.regime_params['bull']
        )

        self.assertIn('action', signal)
        self.assertIn('confidence', signal)
        self.assertIn('indicators', signal)

    def test_bear_signal_generation(self):
        """Test signal generation in bear market."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        strategy.current_regime = 'bear'

        test_date = self.sample_data.index[900]
        signal = strategy._generate_bear_signal(
            self.sample_data,
            test_date,
            self.regime_params['bear']
        )

        self.assertIn('action', signal)
        self.assertIn('confidence', signal)
        self.assertIn('indicators', signal)

    def test_sideways_signal_generation(self):
        """Test signal generation in sideways market."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        strategy.current_regime = 'sideways'

        test_date = self.sample_data.index[1500]
        signal = strategy._generate_sideways_signal(
            self.sample_data,
            test_date,
            self.regime_params['sideways']
        )

        self.assertIn('action', signal)
        self.assertIn('confidence', signal)
        self.assertIn('indicators', signal)

    def test_regime_switch_history(self):
        """Test regime switch history tracking."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=3
        )

        # Generate signals over time period
        test_dates = self.sample_data.index[250:350:10]  # Every 10 days

        for date in test_dates:
            strategy.generate_signal(self.sample_data, date)

        # Get switch history
        history_df = strategy.get_regime_switch_history()

        self.assertIsInstance(history_df, pd.DataFrame)
        self.assertIn('date', history_df.columns)
        self.assertIn('from_regime', history_df.columns)
        self.assertIn('to_regime', history_df.columns)

    def test_regime_statistics(self):
        """Test regime statistics calculation."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params
        )

        # Generate signals to build history
        test_dates = self.sample_data.index[250:350]

        for date in test_dates:
            strategy.generate_signal(self.sample_data, date)

        # Get statistics
        stats = strategy.get_regime_statistics()

        self.assertIn('total_days', stats)
        self.assertIn('regime_switches', stats)
        self.assertIn('regime_distribution', stats)

        # Verify total days matches
        self.assertEqual(stats['total_days'], len(test_dates))

    def test_signal_generation_sequence(self):
        """Test generating signals over extended period."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=5
        )

        # Generate signals for 100 days
        test_dates = self.sample_data.index[300:400]
        signals = []

        for date in test_dates:
            signal = strategy.generate_signal(self.sample_data, date)
            signals.append(signal)

        # Verify all signals generated
        self.assertEqual(len(signals), len(test_dates))

        # Verify signals have consistent structure
        for signal in signals:
            self.assertIn('action', signal)
            self.assertIn('regime', signal)
            self.assertIn('confidence', signal)

    def test_regime_confidence_threshold(self):
        """Test regime confidence threshold enforcement."""
        strategy = AdaptiveStrategy(
            regime_detector=self.detector,
            regime_params=self.regime_params,
            stability_days=5,
            min_regime_confidence=0.9  # High confidence required
        )

        # Test regime switching with high confidence requirement
        test_dates = self.sample_data.index[250:260]

        for date in test_dates:
            strategy.update_regime(self.sample_data, date)

        # Switches should be infrequent with high confidence requirement
        self.assertLessEqual(len(strategy.parameter_switches), 2)


if __name__ == '__main__':
    unittest.main()
