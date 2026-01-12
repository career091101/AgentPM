"""
Mean Reversion Trading Strategy
Implements contrarian trading based on RSI and Bollinger Bands.

Designed for sideways (range-bound) markets.
Uses mean reversion principle: Buy oversold, Sell overbought.
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


class MeanReversionStrategy:
    """
    Mean reversion strategy for sideways markets.

    Features:
    - RSI-based contrarian signals: Buy RSI<30, Sell RSI>70
    - Bollinger Bands mean reversion: Buy at lower band, Sell at upper band
    - Position sizing: Fixed 1.0 or volatility-adjusted
    - Risk management: Stop loss based on ATR

    Example usage:
        strategy = MeanReversionStrategy(
            rsi_period=14,
            rsi_oversold=30,
            rsi_overbought=70,
            bb_period=20,
            bb_std=2.0,
            position_size=1.0,
            use_volatility_sizing=True
        )

        signal = strategy.generate_signal(data, current_date)
    """

    def __init__(
        self,
        rsi_period: int = 14,
        rsi_oversold: float = 30,
        rsi_overbought: float = 70,
        bb_period: int = 20,
        bb_std: float = 2.0,
        position_size: float = 1.0,
        use_volatility_sizing: bool = True,
        atr_period: int = 14,
        stop_loss_atr_multiplier: float = 2.0
    ):
        """
        Initialize mean reversion strategy.

        Args:
            rsi_period: RSI calculation period (default: 14)
            rsi_oversold: RSI oversold threshold (default: 30)
            rsi_overbought: RSI overbought threshold (default: 70)
            bb_period: Bollinger Bands period (default: 20)
            bb_std: Bollinger Bands standard deviation multiplier (default: 2.0)
            position_size: Base position size (default: 1.0)
            use_volatility_sizing: Use ATR-based position sizing (default: True)
            atr_period: ATR calculation period (default: 14)
            stop_loss_atr_multiplier: Stop loss distance in ATR units (default: 2.0)
        """
        self.rsi_period = rsi_period
        self.rsi_oversold = rsi_oversold
        self.rsi_overbought = rsi_overbought
        self.bb_period = bb_period
        self.bb_std = bb_std
        self.position_size = position_size
        self.use_volatility_sizing = use_volatility_sizing
        self.atr_period = atr_period
        self.stop_loss_atr_multiplier = stop_loss_atr_multiplier

        # Trade history
        self.trade_history = []

    def calculate_position_size(
        self,
        base_size: float,
        atr: float,
        price: float
    ) -> float:
        """
        Calculate position size based on volatility.

        Formula: position_size = base_size / (atr / price)

        Args:
            base_size: Base position size
            atr: Current ATR value
            price: Current price

        Returns:
            Adjusted position size
        """
        if not self.use_volatility_sizing:
            return base_size

        # Volatility ratio (ATR as percentage of price)
        volatility_ratio = atr / price

        # Inverse volatility sizing: Lower position size in high volatility
        # Prevent division by zero
        if volatility_ratio < 0.001:
            volatility_ratio = 0.001

        adjusted_size = base_size / volatility_ratio

        # Cap maximum position size
        max_size = base_size * 3.0
        return min(adjusted_size, max_size)

    def generate_signal(
        self,
        data: pd.DataFrame,
        current_date: pd.Timestamp
    ) -> Dict:
        """
        Generate trading signal based on mean reversion logic.

        Signal Logic:
        - Buy: (RSI < oversold AND price <= BB lower band)
        - Sell: (RSI > overbought AND price >= BB upper band)
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

        if len(historical_data) < max(self.rsi_period, self.bb_period, self.atr_period) + 10:
            return self._hold_signal(current_date, 0, "Insufficient data")

        # Calculate indicators
        indicators = TechnicalIndicators(historical_data)

        rsi_result = indicators.calculate_rsi(period=self.rsi_period)
        bb_result = indicators.calculate_bollinger_bands(
            period=self.bb_period,
            num_std=self.bb_std
        )
        atr_result = indicators.calculate_atr(period=self.atr_period)

        # Extract values
        current_rsi = rsi_result['rsi']
        current_price = bb_result['current_price']
        bb_upper = bb_result['upper']
        bb_middle = bb_result['middle']
        bb_lower = bb_result['lower']
        current_atr = atr_result['atr']

        # Calculate position size
        position_size = self.calculate_position_size(
            self.position_size,
            current_atr,
            current_price
        )

        # Mean reversion logic
        # Buy signal: Oversold conditions
        if current_rsi < self.rsi_oversold and current_price <= bb_lower:
            # Strong buy: Both RSI and BB indicate oversold
            confidence = self._calculate_confidence(
                current_rsi,
                self.rsi_oversold,
                current_price,
                bb_lower,
                bb_middle,
                'buy'
            )

            # Stop loss below recent low
            stop_loss = current_price - (current_atr * self.stop_loss_atr_multiplier)

            return {
                'date': current_date,
                'action': 'buy',
                'confidence': float(confidence),
                'position_size': float(position_size),
                'price': float(current_price),
                'stop_loss': float(stop_loss),
                'indicators': {
                    'rsi': float(current_rsi),
                    'bb_upper': float(bb_upper),
                    'bb_middle': float(bb_middle),
                    'bb_lower': float(bb_lower),
                    'atr': float(current_atr)
                },
                'reason': f"Oversold: RSI={current_rsi:.1f} < {self.rsi_oversold}, Price at BB lower"
            }

        # Sell signal: Overbought conditions
        elif current_rsi > self.rsi_overbought and current_price >= bb_upper:
            # Strong sell: Both RSI and BB indicate overbought
            confidence = self._calculate_confidence(
                current_rsi,
                self.rsi_overbought,
                current_price,
                bb_upper,
                bb_middle,
                'sell'
            )

            # Stop loss above recent high
            stop_loss = current_price + (current_atr * self.stop_loss_atr_multiplier)

            return {
                'date': current_date,
                'action': 'sell',
                'confidence': float(confidence),
                'position_size': float(position_size),
                'price': float(current_price),
                'stop_loss': float(stop_loss),
                'indicators': {
                    'rsi': float(current_rsi),
                    'bb_upper': float(bb_upper),
                    'bb_middle': float(bb_middle),
                    'bb_lower': float(bb_lower),
                    'atr': float(current_atr)
                },
                'reason': f"Overbought: RSI={current_rsi:.1f} > {self.rsi_overbought}, Price at BB upper"
            }

        # Hold signal: No strong mean reversion signal
        else:
            return self._hold_signal(
                current_date,
                current_price,
                f"No mean reversion signal: RSI={current_rsi:.1f}, Price in range"
            )

    def _calculate_confidence(
        self,
        rsi: float,
        rsi_threshold: float,
        price: float,
        bb_band: float,
        bb_middle: float,
        signal_type: str
    ) -> float:
        """
        Calculate signal confidence based on indicator strength.

        Args:
            rsi: Current RSI value
            rsi_threshold: RSI threshold (oversold/overbought)
            price: Current price
            bb_band: Bollinger Band (upper/lower)
            bb_middle: Bollinger Band middle
            signal_type: 'buy' or 'sell'

        Returns:
            Confidence score (0-1)
        """
        # RSI distance from threshold
        if signal_type == 'buy':
            rsi_distance = (rsi_threshold - rsi) / rsi_threshold  # Larger when more oversold
        else:  # sell
            rsi_distance = (rsi - rsi_threshold) / (100 - rsi_threshold)  # Larger when more overbought

        # Price distance from BB band
        band_width = abs(bb_band - bb_middle)
        if band_width > 0:
            price_distance = abs(price - bb_band) / band_width
        else:
            price_distance = 0

        # Combined confidence (average of both indicators)
        confidence = (rsi_distance + price_distance) / 2

        # Clamp to [0.5, 1.0] range (minimum 0.5 for valid signals)
        return max(0.5, min(1.0, 0.5 + confidence))

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
            'strategy_name': 'MeanReversion',
            'rsi_period': self.rsi_period,
            'rsi_oversold': self.rsi_oversold,
            'rsi_overbought': self.rsi_overbought,
            'bb_period': self.bb_period,
            'bb_std': self.bb_std,
            'position_size': self.position_size,
            'use_volatility_sizing': self.use_volatility_sizing,
            'atr_period': self.atr_period,
            'stop_loss_atr_multiplier': self.stop_loss_atr_multiplier
        }


if __name__ == "__main__":
    print("Mean Reversion Strategy - Test Run")
    print("=" * 60)

    # Sample data
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
    np.random.seed(42)

    # Generate sideways market data (range-bound with noise)
    base_price = 40000
    noise = np.random.randn(len(dates)) * 500
    trend = np.sin(np.arange(len(dates)) / 30) * 2000  # Oscillating pattern

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
    strategy = MeanReversionStrategy(
        rsi_oversold=30,
        rsi_overbought=70,
        bb_period=20,
        bb_std=2.0,
        use_volatility_sizing=True
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
