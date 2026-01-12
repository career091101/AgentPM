"""
Trend Following Trading Strategy
Implements momentum trading based on MACD crossover and ATR-based position sizing.

Designed for bull/bear (trending) markets.
Uses trend continuation principle: Buy when MACD crosses above signal, Sell when crosses below.
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional
from pathlib import Path
import sys

# Add parent to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.technical_indicators import TechnicalIndicators


class TrendFollowingStrategy:
    """
    Trend following strategy for bull/bear markets.

    Features:
    - MACD crossover signals: Buy MACD>Signal, Sell MACD<Signal
    - ATR-based position sizing: position_size = base_size / (ATR / close)
    - Stop loss: ATR * multiplier
    - Trend confirmation: Use moving averages

    Example usage:
        strategy = TrendFollowingStrategy(
            macd_fast=12,
            macd_slow=26,
            macd_signal=9,
            ma_short=50,
            ma_long=200,
            position_size=1.0,
            atr_period=14,
            stop_loss_atr_multiplier=2.0
        )

        signal = strategy.generate_signal(data, current_date)
    """

    def __init__(
        self,
        macd_fast: int = 12,
        macd_slow: int = 26,
        macd_signal: int = 9,
        ma_short: int = 50,
        ma_long: int = 200,
        position_size: float = 1.0,
        atr_period: int = 14,
        stop_loss_atr_multiplier: float = 2.0,
        use_ma_filter: bool = True
    ):
        """
        Initialize trend following strategy.

        Args:
            macd_fast: MACD fast EMA period (default: 12)
            macd_slow: MACD slow EMA period (default: 26)
            macd_signal: MACD signal line period (default: 9)
            ma_short: Short moving average period (default: 50)
            ma_long: Long moving average period (default: 200)
            position_size: Base position size (default: 1.0)
            atr_period: ATR calculation period (default: 14)
            stop_loss_atr_multiplier: Stop loss distance in ATR units (default: 2.0)
            use_ma_filter: Use MA filter to confirm trend (default: True)
        """
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_signal = macd_signal
        self.ma_short = ma_short
        self.ma_long = ma_long
        self.position_size = position_size
        self.atr_period = atr_period
        self.stop_loss_atr_multiplier = stop_loss_atr_multiplier
        self.use_ma_filter = use_ma_filter

        # Trade history
        self.trade_history = []

    def calculate_position_size(
        self,
        base_size: float,
        atr: float,
        price: float
    ) -> float:
        """
        Calculate position size based on ATR (volatility).

        Formula: position_size = base_size / (atr / price)

        This ensures consistent risk across different volatility regimes:
        - High volatility → Smaller position size
        - Low volatility → Larger position size

        Args:
            base_size: Base position size
            atr: Current ATR value
            price: Current price

        Returns:
            Adjusted position size
        """
        # Volatility ratio (ATR as percentage of price)
        volatility_ratio = atr / price

        # Prevent division by zero
        if volatility_ratio < 0.001:
            volatility_ratio = 0.001

        # Inverse volatility sizing
        adjusted_size = base_size / volatility_ratio

        # Cap maximum position size at 3x base
        max_size = base_size * 3.0
        return min(adjusted_size, max_size)

    def generate_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> Dict:
        """
        Generate trading signal based on trend following logic.

        Signal Logic:
        - Buy: MACD crosses above Signal (and optionally SMA50 > SMA200)
        - Sell: MACD crosses below Signal (or SMA50 < SMA200)
        - Hold: Otherwise

        Args:
            data: Historical OHLCV data
            current_date: Current date for signal generation

        Returns:
            Signal dictionary:
                {
                    'date': pd.Timestamp,
                    'action': 'buy' | 'sell' | 'hold',
                    'confidence': float (0-1),
                    'position_size': float,
                    'price': float,
                    'stop_loss': float,
                    'indicators': Dict,
                    'reason': str
                }
        """
        # Use data up to current date (avoid look-ahead bias)
        historical_data = data[data.index <= current_date]

        min_required = max(self.macd_slow, self.ma_long, self.atr_period) + 10
        if len(historical_data) < min_required:
            return self._hold_signal(current_date, 0, "Insufficient data")

        # Calculate indicators
        indicators = TechnicalIndicators(historical_data)

        macd_result = indicators.calculate_macd(
            fast=self.macd_fast,
            slow=self.macd_slow,
            signal=self.macd_signal
        )
        atr_result = indicators.calculate_atr(period=self.atr_period)

        # Extract MACD values
        macd_line = macd_result['macd']
        signal_line = macd_result['signal_line']
        histogram = macd_result['histogram']
        current_atr = atr_result['atr']

        # Get current price
        current_price = historical_data['close'].iloc[-1]

        # Calculate previous histogram for crossover detection
        if len(historical_data) >= 2:
            prev_indicators = TechnicalIndicators(historical_data.iloc[:-1])
            prev_macd_result = prev_indicators.calculate_macd(
                fast=self.macd_fast,
                slow=self.macd_slow,
                signal=self.macd_signal
            )
            prev_histogram = prev_macd_result['histogram']
        else:
            prev_histogram = 0

        # Optional MA filter for trend confirmation
        ma_trend = None
        if self.use_ma_filter:
            ma_result = indicators.calculate_sma(periods=[self.ma_short, self.ma_long])
            sma_short = ma_result['sma50']
            sma_long = ma_result['sma200']

            if sma_short > sma_long:
                ma_trend = 'bullish'
            elif sma_short < sma_long:
                ma_trend = 'bearish'
            else:
                ma_trend = 'neutral'
        else:
            ma_result = None
            sma_short = None
            sma_long = None

        # Calculate position size
        position_size = self.calculate_position_size(
            self.position_size,
            current_atr,
            current_price
        )

        # Detect MACD crossover
        macd_cross_up = prev_histogram <= 0 and histogram > 0
        macd_cross_down = prev_histogram >= 0 and histogram < 0

        # Trend following logic
        # Buy signal: MACD crosses above signal line (bullish crossover)
        if macd_cross_up or (histogram > 0 and macd_line > signal_line):
            # Check MA filter if enabled
            if self.use_ma_filter and ma_trend != 'bullish':
                return self._hold_signal(
                    current_date,
                    current_price,
                    f"MACD bullish but MA trend is {ma_trend}"
                )

            # Calculate confidence based on histogram strength
            confidence = self._calculate_confidence(
                histogram,
                macd_line,
                signal_line,
                'buy'
            )

            # Stop loss below recent low (using ATR)
            stop_loss = current_price - (current_atr * self.stop_loss_atr_multiplier)

            indicators_dict = {
                'macd': float(macd_line),
                'signal_line': float(signal_line),
                'histogram': float(histogram),
                'atr': float(current_atr)
            }

            if self.use_ma_filter and ma_result:
                indicators_dict.update({
                    'sma_short': float(sma_short),
                    'sma_long': float(sma_long)
                })

            return {
                'date': current_date,
                'action': 'buy',
                'confidence': float(confidence),
                'position_size': float(position_size),
                'price': float(current_price),
                'stop_loss': float(stop_loss),
                'indicators': indicators_dict,
                'reason': f"Bullish MACD crossover: histogram={histogram:.2f}, MA trend={ma_trend}"
            }

        # Sell signal: MACD crosses below signal line (bearish crossover)
        elif macd_cross_down or (histogram < 0 and macd_line < signal_line):
            # Calculate confidence based on histogram strength
            confidence = self._calculate_confidence(
                histogram,
                macd_line,
                signal_line,
                'sell'
            )

            # Stop loss above recent high (using ATR)
            stop_loss = current_price + (current_atr * self.stop_loss_atr_multiplier)

            indicators_dict = {
                'macd': float(macd_line),
                'signal_line': float(signal_line),
                'histogram': float(histogram),
                'atr': float(current_atr)
            }

            if self.use_ma_filter and ma_result:
                indicators_dict.update({
                    'sma_short': float(sma_short),
                    'sma_long': float(sma_long)
                })

            return {
                'date': current_date,
                'action': 'sell',
                'confidence': float(confidence),
                'position_size': float(position_size),
                'price': float(current_price),
                'stop_loss': float(stop_loss),
                'indicators': indicators_dict,
                'reason': f"Bearish MACD crossover: histogram={histogram:.2f}, MA trend={ma_trend}"
            }

        # Hold signal: No clear trend signal
        else:
            return self._hold_signal(
                current_date,
                current_price,
                f"No MACD crossover: histogram={histogram:.2f}, MA trend={ma_trend}"
            )

    def _calculate_confidence(
        self,
        histogram: float,
        macd_line: float,
        signal_line: float,
        signal_type: str
    ) -> float:
        """
        Calculate signal confidence based on MACD strength.

        Args:
            histogram: MACD histogram value
            macd_line: MACD line value
            signal_line: Signal line value
            signal_type: 'buy' or 'sell'

        Returns:
            Confidence score (0-1)
        """
        # Histogram strength (normalized)
        histogram_strength = abs(histogram) / (abs(macd_line) + 0.01)  # Avoid division by zero

        # MACD-Signal divergence
        divergence = abs(macd_line - signal_line) / (abs(signal_line) + 0.01)

        # Combined confidence
        confidence = (histogram_strength + divergence) / 2

        # Normalize to [0.5, 1.0] range (minimum 0.5 for valid signals)
        normalized_confidence = 0.5 + (confidence * 0.5)

        return max(0.5, min(1.0, normalized_confidence))

    def _hold_signal(
        self,
        current_date: pd.Timestamp,
        price: float,
        reason: str
    ) -> Dict:
        """
        Generate hold signal.

        Args:
            current_date: Current date
            price: Current price
            reason: Reason for holding

        Returns:
            Hold signal dictionary
        """
        return {
            'date': current_date,
            'action': 'hold',
            'confidence': 0.5,
            'position_size': 0.0,
            'price': float(price),
            'stop_loss': None,
            'indicators': {},
            'reason': reason
        }

    def get_parameters(self) -> Dict:
        """
        Get strategy parameters.

        Returns:
            Dict with all strategy parameters
        """
        return {
            'strategy_name': 'TrendFollowing',
            'macd_fast': self.macd_fast,
            'macd_slow': self.macd_slow,
            'macd_signal': self.macd_signal,
            'ma_short': self.ma_short,
            'ma_long': self.ma_long,
            'position_size': self.position_size,
            'atr_period': self.atr_period,
            'stop_loss_atr_multiplier': self.stop_loss_atr_multiplier,
            'use_ma_filter': self.use_ma_filter
        }


if __name__ == "__main__":
    print("Trend Following Strategy - Test Run")
    print("=" * 60)

    # Sample data
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
    np.random.seed(42)

    # Generate trending market data (upward trend with noise)
    base_price = 35000
    trend = np.arange(len(dates)) * 5  # Upward trend
    noise = np.random.randn(len(dates)) * 500

    sample_data = pd.DataFrame({
        'date': dates,
        'open': base_price + trend + noise,
        'high': base_price + trend + noise + np.abs(np.random.randn(len(dates)) * 300),
        'low': base_price + trend + noise - np.abs(np.random.randn(len(dates)) * 300),
        'close': base_price + trend + noise,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    sample_data['date'] = pd.to_datetime(sample_data['date'])
    sample_data = sample_data.set_index('date')

    # Initialize strategy
    strategy = TrendFollowingStrategy(
        macd_fast=12,
        macd_slow=26,
        macd_signal=9,
        ma_short=50,
        ma_long=200,
        use_ma_filter=True
    )

    print("\n1. Strategy Parameters:")
    params = strategy.get_parameters()
    for key, value in params.items():
        print(f"   {key}: {value}")

    # Generate signals for last 30 days
    print("\n2. Generating signals for last 30 days...")
    test_dates = sample_data.index[-30:]

    buy_signals = 0
    sell_signals = 0
    hold_signals = 0

    for date in test_dates:
        signal = strategy.generate_signal(sample_data, date)

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

    print("\n" + "=" * 60)
    print("Test completed")
