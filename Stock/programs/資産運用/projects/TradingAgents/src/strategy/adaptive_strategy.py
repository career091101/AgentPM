"""
Adaptive Trading Strategy
Dynamically switches parameters based on detected market regime.

Features:
- Real-time regime detection
- Automatic parameter switching
- Regime change validation (noise filtering)
- Trade history logging
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add parent to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType
from utils.technical_indicators import TechnicalIndicators


class AdaptiveStrategy:
    """
    Trading strategy that adapts parameters based on market regime.

    Example usage:
        regime_params = {
            'bull': {'ma_short': 15, 'ma_long': 40, ...},
            'bear': {'ma_short': 30, 'ma_long': 60, ...},
            'sideways': {'bb_period': 20, 'bb_std': 2.0, ...}
        }

        strategy = AdaptiveStrategy(
            regime_detector=detector,
            regime_params=regime_params,
            stability_days=5
        )

        signal = strategy.generate_signal(data, current_date)
    """

    def __init__(
        self,
        regime_detector: MarketRegimeDetector,
        regime_params: Dict[str, Dict],
        stability_days: int = 5,
        min_regime_confidence: float = 0.6
    ):
        """
        Initialize adaptive strategy.

        Args:
            regime_detector: MarketRegimeDetector instance
            regime_params: Dict mapping regime names to their parameters
            stability_days: Minimum days regime must persist before switching (default: 5)
            min_regime_confidence: Minimum confidence for regime detection (default: 0.6)
        """
        self.regime_detector = regime_detector
        self.regime_params = regime_params
        self.stability_days = stability_days
        self.min_regime_confidence = min_regime_confidence

        # State tracking
        self.current_regime = None
        self.regime_history = []  # [(date, regime), ...]
        self.parameter_switches = []  # [(date, old_regime, new_regime), ...]

        # Validate parameters
        self._validate_params()

    def _validate_params(self):
        """Validate that parameters are provided for all regimes."""
        required_regimes = {'bull', 'bear', 'sideways'}
        provided_regimes = set(self.regime_params.keys())

        missing = required_regimes - provided_regimes
        if missing:
            raise ValueError(f"Missing regime parameters for: {missing}")

    def detect_current_regime(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> str:
        """
        Detect current market regime at given date.

        Args:
            data: Historical OHLCV data up to current_date
            current_date: Date to detect regime for

        Returns:
            Regime name ('bull', 'bear', or 'sideways')
        """
        # Use data up to current date (avoid look-ahead bias)
        historical_data = data[data.index <= current_date]

        if len(historical_data) < 200:  # Need enough data for MA-based detection
            return 'sideways'  # Default to conservative regime

        # Create temporary detector with historical data
        temp_detector = MarketRegimeDetector(historical_data)
        regime_series = temp_detector.detect_regime_combined()

        # Get most recent regime
        current_regime = regime_series.iloc[-1]

        return current_regime

    def should_switch_regime(
        self,
        new_regime: str,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> bool:
        """
        Determine if regime should be switched based on stability criteria.

        Args:
            new_regime: Newly detected regime
            data: Historical data
            current_date: Current date

        Returns:
            True if regime should be switched, False otherwise
        """
        # If this is the first detection, switch
        if self.current_regime is None:
            return True

        # If regime hasn't changed, no switch needed
        if new_regime == self.current_regime:
            return False

        # Check if new regime has been stable for stability_days
        lookback_date = current_date - timedelta(days=self.stability_days)
        recent_data = data[(data.index > lookback_date) & (data.index <= current_date)]

        if len(recent_data) < self.stability_days:
            return False  # Not enough data to confirm stability

        # Detect regime for each day in lookback period
        stable_count = 0
        for date in recent_data.index:
            day_regime = self.detect_current_regime(data, date)
            if day_regime == new_regime:
                stable_count += 1

        # Calculate stability ratio
        stability_ratio = stable_count / len(recent_data)

        # Switch if new regime is stable enough
        return stability_ratio >= self.min_regime_confidence

    def get_active_parameters(self, regime: Optional[str] = None) -> Dict:
        """
        Get parameters for current or specified regime.

        Args:
            regime: Regime name (default: use current_regime)

        Returns:
            Parameter dictionary for the regime
        """
        target_regime = regime if regime is not None else self.current_regime

        if target_regime is None:
            target_regime = 'sideways'  # Default to conservative

        return self.regime_params[target_regime].copy()

    def update_regime(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> Tuple[str, bool]:
        """
        Update current regime based on latest data.

        Args:
            data: Historical OHLCV data
            current_date: Current date

        Returns:
            Tuple of (current_regime, regime_switched)
        """
        # Detect new regime
        new_regime = self.detect_current_regime(data, current_date)

        # Log regime detection
        self.regime_history.append((current_date, new_regime))

        # Check if should switch
        should_switch = self.should_switch_regime(new_regime, data, current_date)

        regime_switched = False
        if should_switch:
            old_regime = self.current_regime
            self.current_regime = new_regime

            # Log parameter switch
            if old_regime is not None:
                self.parameter_switches.append((current_date, old_regime, new_regime))
                regime_switched = True

        return self.current_regime, regime_switched

    def generate_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> Dict:
        """
        Generate trading signal based on current regime.

        Args:
            data: Historical OHLCV data
            current_date: Current date

        Returns:
            Signal dictionary:
                {
                    'date': pd.Timestamp,
                    'regime': str,
                    'action': 'buy' | 'sell' | 'hold',
                    'confidence': float (0-1),
                    'parameters': Dict,
                    'regime_switched': bool
                }
        """
        # Update regime
        current_regime, regime_switched = self.update_regime(data, current_date)

        # Get active parameters
        params = self.get_active_parameters(current_regime)

        # Generate signal based on regime-specific strategy
        if current_regime == 'bull':
            signal = self._generate_bull_signal(data, current_date, params)
        elif current_regime == 'bear':
            signal = self._generate_bear_signal(data, current_date, params)
        else:  # sideways
            signal = self._generate_sideways_signal(data, current_date, params)

        # Add metadata
        signal.update({
            'date': current_date,
            'regime': current_regime,
            'parameters': params,
            'regime_switched': regime_switched
        })

        return signal

    def _generate_bull_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp,
        params: Dict
    ) -> Dict:
        """Generate signal for bull market (trend following)."""
        historical_data = data[data.index <= current_date]

        # Calculate indicators using TechnicalIndicators
        ma_short = params.get('ma_short', 15)
        ma_long = params.get('ma_long', 40)

        indicators = TechnicalIndicators(historical_data)
        ma_result = indicators.calculate_sma(periods=[ma_short, ma_long])
        rsi_result = indicators.calculate_rsi(period=params.get('rsi_period', 14))

        current_price = ma_result['current_price']
        current_sma_short = ma_result['sma50']
        current_sma_long = ma_result['sma200']
        current_rsi = rsi_result['rsi']

        # Bull strategy: Buy on MA crossover + RSI confirmation
        if current_sma_short > current_sma_long and current_rsi < params.get('rsi_overbought', 70):
            action = 'buy'
            confidence = min((current_sma_short - current_sma_long) / current_sma_long * 100, 1.0)
        elif current_sma_short < current_sma_long or current_rsi > params.get('rsi_overbought', 70):
            action = 'sell'
            confidence = 0.7
        else:
            action = 'hold'
            confidence = 0.5

        return {
            'action': action,
            'confidence': float(confidence),
            'price': float(current_price),
            'indicators': {
                'sma_short': float(current_sma_short),
                'sma_long': float(current_sma_long),
                'rsi': float(current_rsi)
            }
        }

    def _generate_bear_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp,
        params: Dict
    ) -> Dict:
        """Generate signal for bear market (conservative)."""
        historical_data = data[data.index <= current_date]

        # Calculate indicators with longer periods
        ma_short = params.get('ma_short', 30)
        ma_long = params.get('ma_long', 60)

        indicators = TechnicalIndicators(historical_data)
        ma_result = indicators.calculate_sma(periods=[ma_short, ma_long])
        rsi_result = indicators.calculate_rsi(period=params.get('rsi_period', 14))

        current_price = ma_result['current_price']
        current_sma_short = ma_result['sma50']
        current_sma_long = ma_result['sma200']
        current_rsi = rsi_result['rsi']

        # Bear strategy: Very conservative, avoid false signals
        if (current_sma_short > current_sma_long and
            current_rsi < params.get('rsi_oversold', 30) and
            current_price > current_sma_short):
            action = 'buy'
            confidence = 0.6  # Lower confidence in bear market
        else:
            action = 'hold'  # Default to holding cash in bear market
            confidence = 0.5

        return {
            'action': action,
            'confidence': float(confidence),
            'price': float(current_price),
            'indicators': {
                'sma_short': float(current_sma_short),
                'sma_long': float(current_sma_long),
                'rsi': float(current_rsi)
            }
        }

    def _generate_sideways_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp,
        params: Dict
    ) -> Dict:
        """Generate signal for sideways market (mean reversion)."""
        historical_data = data[data.index <= current_date]

        # Calculate Bollinger Bands and RSI
        bb_period = params.get('bb_period', 20)
        bb_std = params.get('bb_std', 2.0)

        indicators = TechnicalIndicators(historical_data)
        bb_result = indicators.calculate_bollinger_bands(period=bb_period, num_std=bb_std)
        rsi_result = indicators.calculate_rsi(period=params.get('rsi_period', 14))

        current_price = bb_result['current_price']
        current_bb_upper = bb_result['upper']
        current_bb_lower = bb_result['lower']
        current_bb_middle = bb_result['middle']
        current_rsi = rsi_result['rsi']

        # Sideways strategy: Mean reversion with BB
        if current_price < current_bb_lower and current_rsi < params.get('rsi_oversold', 30):
            action = 'buy'  # Oversold, expect reversion
            confidence = 0.8
        elif current_price > current_bb_upper and current_rsi > params.get('rsi_overbought', 70):
            action = 'sell'  # Overbought, expect reversion
            confidence = 0.8
        else:
            action = 'hold'
            confidence = 0.5

        return {
            'action': action,
            'confidence': float(confidence),
            'price': float(current_price),
            'indicators': {
                'bb_upper': float(current_bb_upper),
                'bb_middle': float(current_bb_middle),
                'bb_lower': float(current_bb_lower),
                'rsi': float(current_rsi)
            }
        }

    def get_regime_switch_history(self) -> pd.DataFrame:
        """
        Get history of regime switches.

        Returns:
            DataFrame with regime switch records
        """
        if not self.parameter_switches:
            return pd.DataFrame(columns=['date', 'from_regime', 'to_regime'])

        return pd.DataFrame(
            self.parameter_switches,
            columns=['date', 'from_regime', 'to_regime']
        )

    def get_regime_statistics(self) -> Dict:
        """
        Calculate statistics about regime detection.

        Returns:
            Dict with regime statistics
        """
        if not self.regime_history:
            return {}

        regime_df = pd.DataFrame(self.regime_history, columns=['date', 'regime'])

        stats = {
            'total_days': len(regime_df),
            'regime_switches': len(self.parameter_switches),
            'regime_distribution': regime_df['regime'].value_counts().to_dict(),
            'average_regime_duration': None
        }

        # Calculate average regime duration
        if self.parameter_switches:
            durations = []
            for i in range(len(self.parameter_switches) - 1):
                start = self.parameter_switches[i][0]
                end = self.parameter_switches[i + 1][0]
                durations.append((end - start).days)

            stats['average_regime_duration'] = np.mean(durations)

        return stats


if __name__ == "__main__":
    print("Adaptive Strategy - Test Run")
    print("=" * 60)

    # Sample data
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
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

    # Regime parameters
    regime_params = {
        'bull': {'ma_short': 15, 'ma_long': 40, 'rsi_period': 14},
        'bear': {'ma_short': 30, 'ma_long': 60, 'rsi_period': 14},
        'sideways': {'bb_period': 20, 'bb_std': 2.0, 'rsi_period': 14}
    }

    # Initialize detector and strategy
    detector = MarketRegimeDetector(sample_data)
    strategy = AdaptiveStrategy(
        regime_detector=detector,
        regime_params=regime_params,
        stability_days=5
    )

    # Generate signals for last 30 days
    print("\n1. Generating signals for last 30 days...")
    test_dates = sample_data.index[-30:]

    signals = []
    for date in test_dates:
        signal = strategy.generate_signal(sample_data, date)
        signals.append(signal)

        if signal['regime_switched']:
            print(f"   🔄 Regime switched to {signal['regime']} on {date.date()}")

    print(f"✅ Generated {len(signals)} signals")

    # Show statistics
    print("\n2. Regime Statistics:")
    stats = strategy.get_regime_statistics()
    print(f"   Total regime switches: {stats['regime_switches']}")
    print(f"   Regime distribution: {stats['regime_distribution']}")

    print("\n" + "=" * 60)
    print("✅ Test completed")
