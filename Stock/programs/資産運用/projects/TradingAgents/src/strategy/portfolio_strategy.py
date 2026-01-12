"""
Portfolio Strategy
Combines Mean Reversion and Trend Following strategies for diversification.

Reduces overfitting through:
- Risk diversification across multiple strategies
- Dynamic weight adjustment based on recent performance
- Regime-aware strategy selection
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional, List, Tuple
from pathlib import Path
import sys
from collections import deque

# Add parent to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from strategy.mean_reversion_strategy import MeanReversionStrategy
from strategy.trend_following_strategy import TrendFollowingStrategy
from utils.market_regime import MarketRegimeDetector, RegimeType


class PortfolioStrategy:
    """
    Portfolio strategy combining multiple sub-strategies.

    Features:
    - Combines Mean Reversion (40%) + Trend Following (60%) by default
    - Dynamic weight adjustment based on recent performance
    - Regime-aware strategy selection
    - Risk management through diversification

    Example usage:
        portfolio = PortfolioStrategy(
            mean_reversion_weight=0.4,
            trend_following_weight=0.6,
            use_dynamic_weights=True,
            performance_lookback=20
        )

        signal = portfolio.generate_signal(data, current_date)
    """

    def __init__(
        self,
        mean_reversion_weight: float = 0.4,
        trend_following_weight: float = 0.6,
        use_dynamic_weights: bool = True,
        performance_lookback: int = 20,
        use_regime_filter: bool = True,
        mean_reversion_params: Optional[Dict] = None,
        trend_following_params: Optional[Dict] = None
    ):
        """
        Initialize portfolio strategy.

        Args:
            mean_reversion_weight: Weight for mean reversion strategy (default: 0.4)
            trend_following_weight: Weight for trend following strategy (default: 0.6)
            use_dynamic_weights: Adjust weights based on recent performance (default: True)
            performance_lookback: Number of days to track performance (default: 20)
            use_regime_filter: Use market regime to filter strategies (default: True)
            mean_reversion_params: Custom parameters for mean reversion strategy
            trend_following_params: Custom parameters for trend following strategy
        """
        # Validate weights
        total_weight = mean_reversion_weight + trend_following_weight
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Weights must sum to 1.0, got {total_weight}")

        self.base_mean_reversion_weight = mean_reversion_weight
        self.base_trend_following_weight = trend_following_weight
        self.use_dynamic_weights = use_dynamic_weights
        self.performance_lookback = performance_lookback
        self.use_regime_filter = use_regime_filter

        # Initialize sub-strategies
        mr_params = mean_reversion_params or {}
        tf_params = trend_following_params or {}

        self.mean_reversion = MeanReversionStrategy(**mr_params)
        self.trend_following = TrendFollowingStrategy(**tf_params)

        # Performance tracking
        self.performance_history = {
            'mean_reversion': deque(maxlen=performance_lookback),
            'trend_following': deque(maxlen=performance_lookback)
        }

        # Trade history
        self.trade_history = []
        self.weight_history = []

    def calculate_dynamic_weights(self) -> Tuple[float, float]:
        """
        Calculate dynamic weights based on recent performance.

        Uses exponential moving average of recent returns to adjust weights.
        Better performing strategy gets higher weight.

        Returns:
            Tuple of (mean_reversion_weight, trend_following_weight)
        """
        if not self.use_dynamic_weights:
            return self.base_mean_reversion_weight, self.base_trend_following_weight

        # Need at least 10 samples for reliable adjustment
        if len(self.performance_history['mean_reversion']) < 10:
            return self.base_mean_reversion_weight, self.base_trend_following_weight

        # Calculate average performance
        mr_performance = np.mean(list(self.performance_history['mean_reversion']))
        tf_performance = np.mean(list(self.performance_history['trend_following']))

        # If both negative, use base weights
        if mr_performance <= 0 and tf_performance <= 0:
            return self.base_mean_reversion_weight, self.base_trend_following_weight

        # Normalize performance to positive values
        mr_perf_norm = max(0, mr_performance + abs(min(mr_performance, tf_performance)))
        tf_perf_norm = max(0, tf_performance + abs(min(mr_performance, tf_performance)))

        total_perf = mr_perf_norm + tf_perf_norm

        if total_perf == 0:
            return self.base_mean_reversion_weight, self.base_trend_following_weight

        # Calculate performance-based weights
        mr_weight_perf = mr_perf_norm / total_perf
        tf_weight_perf = tf_perf_norm / total_perf

        # Blend with base weights (50% base, 50% performance)
        # This prevents extreme weight shifts
        mr_weight = 0.5 * self.base_mean_reversion_weight + 0.5 * mr_weight_perf
        tf_weight = 0.5 * self.base_trend_following_weight + 0.5 * tf_weight_perf

        # Normalize to sum to 1.0
        total = mr_weight + tf_weight
        mr_weight /= total
        tf_weight /= total

        # Constrain weights to reasonable bounds (10% - 90%)
        mr_weight = max(0.1, min(0.9, mr_weight))
        tf_weight = 1.0 - mr_weight

        return mr_weight, tf_weight

    def detect_regime(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> str:
        """
        Detect current market regime.

        Args:
            data: Historical OHLCV data
            current_date: Current date

        Returns:
            Regime name ('bull', 'bear', or 'sideways')
        """
        historical_data = data[data.index <= current_date]

        if len(historical_data) < 200:
            return 'sideways'  # Default to conservative regime

        detector = MarketRegimeDetector(historical_data)
        regime_series = detector.detect_regime_combined()

        return regime_series.iloc[-1]

    def generate_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> Dict:
        """
        Generate combined trading signal from portfolio.

        Strategy selection logic:
        - Bull/Bear markets: Trend Following gets higher weight
        - Sideways markets: Mean Reversion gets higher weight
        - Dynamic weights adjust based on recent performance

        Args:
            data: Historical OHLCV data
            current_date: Current date for signal generation

        Returns:
            Combined signal dictionary:
                {
                    'date': pd.Timestamp,
                    'action': 'buy' | 'sell' | 'hold',
                    'confidence': float (0-1),
                    'position_size': float,
                    'price': float,
                    'stop_loss': float,
                    'regime': str,
                    'weights': Dict,
                    'sub_signals': Dict,
                    'reason': str
                }
        """
        # Detect regime
        current_regime = 'neutral'
        if self.use_regime_filter:
            current_regime = self.detect_regime(data, current_date)

        # Calculate dynamic weights
        mr_weight, tf_weight = self.calculate_dynamic_weights()

        # Adjust weights based on regime
        if self.use_regime_filter:
            if current_regime == 'sideways':
                # Favor mean reversion in sideways markets
                mr_weight = min(0.8, mr_weight * 1.5)
                tf_weight = 1.0 - mr_weight
            elif current_regime in ['bull', 'bear']:
                # Favor trend following in trending markets
                tf_weight = min(0.8, tf_weight * 1.5)
                mr_weight = 1.0 - tf_weight

        # Store weight history
        self.weight_history.append({
            'date': current_date,
            'regime': current_regime,
            'mr_weight': mr_weight,
            'tf_weight': tf_weight
        })

        # Generate signals from both strategies
        mr_signal = self.mean_reversion.generate_signal(data, current_date)
        tf_signal = self.trend_following.generate_signal(data, current_date)

        # Combine signals using weighted voting
        combined_signal = self._combine_signals(
            mr_signal,
            tf_signal,
            mr_weight,
            tf_weight,
            current_date,
            current_regime
        )

        return combined_signal

    def _combine_signals(
        self,
        mr_signal: Dict,
        tf_signal: Dict,
        mr_weight: float,
        tf_weight: float,
        current_date: pd.Timestamp,
        regime: str
    ) -> Dict:
        """
        Combine signals from multiple strategies using weighted voting.

        Args:
            mr_signal: Mean reversion signal
            tf_signal: Trend following signal
            mr_weight: Mean reversion weight
            tf_weight: Trend following weight
            current_date: Current date
            regime: Current market regime

        Returns:
            Combined signal dictionary
        """
        # Convert actions to numerical scores
        action_scores = {'buy': 1, 'sell': -1, 'hold': 0}

        mr_score = action_scores[mr_signal['action']] * mr_signal['confidence'] * mr_weight
        tf_score = action_scores[tf_signal['action']] * tf_signal['confidence'] * tf_weight

        combined_score = mr_score + tf_score

        # Determine combined action
        if combined_score > 0.3:
            action = 'buy'
            confidence = min(1.0, combined_score)
        elif combined_score < -0.3:
            action = 'sell'
            confidence = min(1.0, abs(combined_score))
        else:
            action = 'hold'
            confidence = 0.5

        # Calculate combined position size
        if action == 'buy':
            position_size = (mr_signal['position_size'] * mr_weight +
                           tf_signal['position_size'] * tf_weight)
        elif action == 'sell':
            position_size = (mr_signal['position_size'] * mr_weight +
                           tf_signal['position_size'] * tf_weight)
        else:
            position_size = 0.0

        # Use average price
        price = (mr_signal['price'] + tf_signal['price']) / 2

        # Use the more conservative stop loss (closer to entry)
        stop_loss = None
        if action == 'buy':
            stops = [s for s in [mr_signal.get('stop_loss'), tf_signal.get('stop_loss')] if s is not None]
            if stops:
                stop_loss = max(stops)  # Higher stop loss for long positions
        elif action == 'sell':
            stops = [s for s in [mr_signal.get('stop_loss'), tf_signal.get('stop_loss')] if s is not None]
            if stops:
                stop_loss = min(stops)  # Lower stop loss for short positions

        # Build reason
        reasons = []
        if mr_signal['action'] != 'hold':
            reasons.append(f"MR({mr_weight:.1%}): {mr_signal['action']}")
        if tf_signal['action'] != 'hold':
            reasons.append(f"TF({tf_weight:.1%}): {tf_signal['action']}")

        reason = f"Regime={regime}, " + ", ".join(reasons) if reasons else f"Regime={regime}, No strong signals"

        return {
            'date': current_date,
            'action': action,
            'confidence': float(confidence),
            'position_size': float(position_size),
            'price': float(price),
            'stop_loss': stop_loss,
            'regime': regime,
            'weights': {
                'mean_reversion': float(mr_weight),
                'trend_following': float(tf_weight)
            },
            'sub_signals': {
                'mean_reversion': mr_signal,
                'trend_following': tf_signal
            },
            'reason': reason
        }

    def update_performance(
        self,
        strategy_name: str,
        performance: float
    ):
        """
        Update performance tracking for a strategy.

        Args:
            strategy_name: 'mean_reversion' or 'trend_following'
            performance: Performance metric (e.g., return)
        """
        if strategy_name in self.performance_history:
            self.performance_history[strategy_name].append(performance)

    def get_performance_summary(self) -> Dict:
        """
        Get summary of strategy performance tracking.

        Returns:
            Dict with performance statistics
        """
        summary = {}

        for strategy_name, history in self.performance_history.items():
            if len(history) > 0:
                summary[strategy_name] = {
                    'avg_performance': float(np.mean(list(history))),
                    'std_performance': float(np.std(list(history))),
                    'samples': len(history)
                }
            else:
                summary[strategy_name] = {
                    'avg_performance': 0.0,
                    'std_performance': 0.0,
                    'samples': 0
                }

        return summary

    def get_weight_history(self) -> pd.DataFrame:
        """
        Get history of weight adjustments.

        Returns:
            DataFrame with weight history
        """
        if not self.weight_history:
            return pd.DataFrame()

        return pd.DataFrame(self.weight_history)

    def get_parameters(self) -> Dict:
        """
        Get portfolio strategy parameters.

        Returns:
            Dict with all parameters
        """
        return {
            'strategy_name': 'Portfolio',
            'base_mean_reversion_weight': self.base_mean_reversion_weight,
            'base_trend_following_weight': self.base_trend_following_weight,
            'use_dynamic_weights': self.use_dynamic_weights,
            'performance_lookback': self.performance_lookback,
            'use_regime_filter': self.use_regime_filter,
            'mean_reversion_params': self.mean_reversion.get_parameters(),
            'trend_following_params': self.trend_following.get_parameters()
        }


if __name__ == "__main__":
    print("Portfolio Strategy - Test Run")
    print("=" * 60)

    # Sample data
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
    np.random.seed(42)

    # Generate mixed market data (trend + oscillation)
    base_price = 38000
    trend = np.arange(len(dates)) * 3
    oscillation = np.sin(np.arange(len(dates)) / 30) * 1000
    noise = np.random.randn(len(dates)) * 500

    sample_data = pd.DataFrame({
        'date': dates,
        'open': base_price + trend + oscillation + noise,
        'high': base_price + trend + oscillation + noise + np.abs(np.random.randn(len(dates)) * 300),
        'low': base_price + trend + oscillation + noise - np.abs(np.random.randn(len(dates)) * 300),
        'close': base_price + trend + oscillation + noise,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    sample_data['date'] = pd.to_datetime(sample_data['date'])
    sample_data = sample_data.set_index('date')

    # Initialize portfolio
    portfolio = PortfolioStrategy(
        mean_reversion_weight=0.4,
        trend_following_weight=0.6,
        use_dynamic_weights=True,
        use_regime_filter=True
    )

    print("\n1. Portfolio Parameters:")
    params = portfolio.get_parameters()
    print(f"   Base MR weight: {params['base_mean_reversion_weight']}")
    print(f"   Base TF weight: {params['base_trend_following_weight']}")
    print(f"   Dynamic weights: {params['use_dynamic_weights']}")
    print(f"   Regime filter: {params['use_regime_filter']}")

    # Generate signals for last 30 days
    print("\n2. Generating signals for last 30 days...")
    test_dates = sample_data.index[-30:]

    buy_signals = 0
    sell_signals = 0
    hold_signals = 0

    for date in test_dates:
        signal = portfolio.generate_signal(sample_data, date)

        if signal['action'] == 'buy':
            buy_signals += 1
            print(f"   BUY on {date.date()}: {signal['reason']}")
        elif signal['action'] == 'sell':
            sell_signals += 1
            print(f"   SELL on {date.date()}: {signal['reason']}")
        else:
            hold_signals += 1

    print(f"\n3. Signal Summary:")
    print(f"   Buy signals: {buy_signals}")
    print(f"   Sell signals: {sell_signals}")
    print(f"   Hold signals: {hold_signals}")

    # Show weight evolution
    print("\n4. Weight Evolution (last 5 days):")
    weight_df = portfolio.get_weight_history()
    if len(weight_df) > 0:
        for idx, row in weight_df.tail(5).iterrows():
            print(f"   {row['date'].date()}: MR={row['mr_weight']:.2%}, TF={row['tf_weight']:.2%}, Regime={row['regime']}")

    print("\n" + "=" * 60)
    print("Test completed")
