"""
Technical Indicators Calculator
Implements 8 technical indicators for Nikkei 225 futures trading analysis.

Uses numpy and pandas for calculations (no pandas-ta dependency).
Based on knowledge/technical_indicators.md specifications.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional


class TechnicalIndicators:
    """
    Technical indicators calculator for stock market analysis.

    Implements 8 indicators with weighted voting system:
    - MA (Moving Average): Weight 2.0
    - MACD: Weight 1.8
    - RSI: Weight 1.6
    - Bollinger Bands: Weight 1.4
    - ATR: Weight 1.2
    - Volume Ratio: Weight 1.0
    - VWMA: Weight 1.5
    - Stochastic: Weight 1.4
    """

    # Signal weights for weighted voting
    WEIGHTS = {
        'ma': 2.0,
        'macd': 1.8,
        'rsi': 1.6,
        'bollinger': 1.4,
        'atr': 1.2,
        'volume': 1.0,
        'vwma': 1.5,
        'stochastic': 1.4
    }

    def __init__(self, data: pd.DataFrame):
        """
        Initialize with OHLCV data.

        Args:
            data: DataFrame with columns ['date', 'open', 'high', 'low', 'close', 'volume']
        """
        self.data = data.copy()
        self._validate_data()

    def _validate_data(self):
        """Validate input data has required columns."""
        required_columns = {'open', 'high', 'low', 'close', 'volume'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Data must contain columns: {required_columns}")

    def calculate_sma(self, periods: List[int] = [50, 200]) -> Dict:
        """
        Calculate Simple Moving Average (SMA).

        Formula: SMA = Sum(close, n) / n

        Signal logic:
        - Buy: Price > SMA50 AND SMA50 > SMA200 (Golden Cross)
        - Sell: Price < SMA50 AND SMA50 < SMA200 (Death Cross)
        - Neutral: Otherwise

        Args:
            periods: List of periods [short, long]. Default [50, 200]

        Returns:
            Dict with 'sma50', 'sma200', 'signal', 'strength', 'weight'
        """
        close = self.data['close']
        short_period, long_period = periods

        sma_short = close.rolling(window=short_period).mean()
        sma_long = close.rolling(window=long_period).mean()

        current_price = close.iloc[-1]
        current_sma_short = sma_short.iloc[-1]
        current_sma_long = sma_long.iloc[-1]

        # Signal determination
        if current_price > current_sma_short and current_sma_short > current_sma_long:
            signal = 'buy'
            strength = min(100, ((current_price - current_sma_long) / current_sma_long) * 100)
        elif current_price < current_sma_short and current_sma_short < current_sma_long:
            signal = 'sell'
            strength = min(100, ((current_sma_long - current_price) / current_sma_long) * 100)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'sma50': float(current_sma_short),
            'sma200': float(current_sma_long),
            'current_price': float(current_price),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['ma']
        }

    def calculate_macd(self, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict:
        """
        Calculate MACD (Moving Average Convergence Divergence).

        Formula:
        - MACD Line = EMA12 - EMA26
        - Signal Line = EMA(MACD, 9)
        - Histogram = MACD - Signal

        Signal logic:
        - Buy: MACD crosses above Signal (histogram > 0 and increasing)
        - Sell: MACD crosses below Signal (histogram < 0 and decreasing)
        - Neutral: Otherwise

        Args:
            fast: Fast EMA period (default 12)
            slow: Slow EMA period (default 26)
            signal: Signal line period (default 9)

        Returns:
            Dict with 'macd', 'signal_line', 'histogram', 'signal', 'strength', 'weight'
        """
        close = self.data['close']

        # Calculate EMAs
        ema_fast = close.ewm(span=fast, adjust=False).mean()
        ema_slow = close.ewm(span=slow, adjust=False).mean()

        # MACD line
        macd_line = ema_fast - ema_slow

        # Signal line
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()

        # Histogram
        histogram = macd_line - signal_line

        current_macd = macd_line.iloc[-1]
        current_signal = signal_line.iloc[-1]
        current_histogram = histogram.iloc[-1]
        previous_histogram = histogram.iloc[-2]

        # Signal determination
        if current_histogram > 0 and current_histogram > previous_histogram:
            signal_result = 'buy'
            strength = min(100, abs(current_histogram) * 10)
        elif current_histogram < 0 and current_histogram < previous_histogram:
            signal_result = 'sell'
            strength = min(100, abs(current_histogram) * 10)
        else:
            signal_result = 'neutral'
            strength = 0

        return {
            'macd': float(current_macd),
            'signal_line': float(current_signal),
            'histogram': float(current_histogram),
            'signal': signal_result,
            'strength': float(strength),
            'weight': self.WEIGHTS['macd']
        }

    def calculate_rsi(self, period: int = 14) -> Dict:
        """
        Calculate RSI (Relative Strength Index).

        Formula:
        - RS = Average Gain / Average Loss (over period)
        - RSI = 100 - (100 / (1 + RS))

        Signal logic:
        - Buy: RSI < 30 (oversold)
        - Sell: RSI > 70 (overbought)
        - Neutral: 30 <= RSI <= 70

        Args:
            period: Calculation period (default 14)

        Returns:
            Dict with 'rsi', 'signal', 'strength', 'weight'
        """
        close = self.data['close']

        # Calculate price changes
        delta = close.diff()

        # Separate gains and losses
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        # Calculate average gain and loss
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        # Calculate RS and RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        current_rsi = rsi.iloc[-1]

        # Signal determination
        if current_rsi < 30:
            signal = 'buy'
            strength = float(30 - current_rsi)
        elif current_rsi > 70:
            signal = 'sell'
            strength = float(current_rsi - 70)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'rsi': float(current_rsi),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['rsi']
        }

    def calculate_bollinger_bands(self, period: int = 20, num_std: float = 2.0) -> Dict:
        """
        Calculate Bollinger Bands.

        Formula:
        - Middle Band = SMA(close, 20)
        - Upper Band = Middle + (2 × σ)
        - Lower Band = Middle - (2 × σ)

        Signal logic:
        - Buy: Price touches or crosses below lower band
        - Sell: Price touches or crosses above upper band
        - Neutral: Price within bands

        Args:
            period: Period for SMA and std dev (default 20)
            num_std: Number of standard deviations (default 2.0)

        Returns:
            Dict with 'upper', 'middle', 'lower', 'signal', 'strength', 'weight'
        """
        close = self.data['close']

        # Calculate middle band (SMA)
        middle = close.rolling(window=period).mean()

        # Calculate standard deviation
        std = close.rolling(window=period).std()

        # Calculate upper and lower bands
        upper = middle + (num_std * std)
        lower = middle - (num_std * std)

        current_price = close.iloc[-1]
        current_upper = upper.iloc[-1]
        current_middle = middle.iloc[-1]
        current_lower = lower.iloc[-1]

        # Band width for strength calculation
        band_width = current_upper - current_lower

        # Signal determination
        if current_price <= current_lower:
            signal = 'buy'
            strength = min(100, ((current_lower - current_price) / band_width) * 200)
        elif current_price >= current_upper:
            signal = 'sell'
            strength = min(100, ((current_price - current_upper) / band_width) * 200)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'upper': float(current_upper),
            'middle': float(current_middle),
            'lower': float(current_lower),
            'current_price': float(current_price),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['bollinger']
        }

    def calculate_atr(self, period: int = 14) -> Dict:
        """
        Calculate ATR (Average True Range) for volatility measurement.

        Formula:
        - True Range = max(high - low, abs(high - prev_close), abs(low - prev_close))
        - ATR = EMA(True Range, 14)

        Signal logic:
        - High volatility: ATR > 1.5 × average ATR (reduce position size)
        - Normal volatility: ATR ≤ 1.5 × average ATR (normal position)

        Args:
            period: Period for ATR calculation (default 14)

        Returns:
            Dict with 'atr', 'atr_percent', 'volatility', 'weight'
        """
        high = self.data['high']
        low = self.data['low']
        close = self.data['close']

        # Calculate True Range
        prev_close = close.shift(1)
        tr1 = high - low
        tr2 = abs(high - prev_close)
        tr3 = abs(low - prev_close)

        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

        # Calculate ATR (EMA of True Range)
        atr = true_range.ewm(span=period, adjust=False).mean()

        current_atr = atr.iloc[-1]
        current_price = close.iloc[-1]
        atr_percent = (current_atr / current_price) * 100

        # Calculate average ATR for volatility comparison
        avg_atr = atr.rolling(window=50).mean().iloc[-1]

        # Volatility determination
        if current_atr > 1.5 * avg_atr:
            volatility = 'high'
        else:
            volatility = 'normal'

        return {
            'atr': float(current_atr),
            'atr_percent': float(atr_percent),
            'volatility': volatility,
            'avg_atr': float(avg_atr),
            'weight': self.WEIGHTS['atr']
        }

    def calculate_volume_ratio(self, period: int = 20) -> Dict:
        """
        Calculate Volume Ratio.

        Formula:
        - Volume Ratio = Current Volume / SMA(Volume, 20)

        Signal logic:
        - Strong buy: Ratio > 2.0 with price increase
        - Strong sell: Ratio > 2.0 with price decrease
        - Neutral: Ratio <= 2.0

        Args:
            period: Period for volume SMA (default 20)

        Returns:
            Dict with 'volume_ratio', 'signal', 'strength', 'weight'
        """
        volume = self.data['volume']
        close = self.data['close']

        # Calculate average volume
        avg_volume = volume.rolling(window=period).mean()

        current_volume = volume.iloc[-1]
        current_avg_volume = avg_volume.iloc[-1]
        volume_ratio = current_volume / current_avg_volume

        # Price change
        price_change = close.iloc[-1] - close.iloc[-2]

        # Signal determination
        if volume_ratio > 2.0 and price_change > 0:
            signal = 'buy'
            strength = min(100, (volume_ratio - 1) * 30)
        elif volume_ratio > 2.0 and price_change < 0:
            signal = 'sell'
            strength = min(100, (volume_ratio - 1) * 30)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'volume_ratio': float(volume_ratio),
            'current_volume': int(current_volume),
            'avg_volume': float(current_avg_volume),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['volume']
        }

    def calculate_vwma(self, period: int = 20) -> Dict:
        """
        Calculate VWMA (Volume Weighted Moving Average).

        Formula:
        - VWMA = Σ(price × volume) / Σ(volume)

        Signal logic:
        - Buy: Price > VWMA (volume-weighted uptrend)
        - Sell: Price < VWMA (volume-weighted downtrend)
        - Neutral: Price ≈ VWMA

        Args:
            period: Period for VWMA calculation (default 20)

        Returns:
            Dict with 'vwma', 'signal', 'strength', 'weight'
        """
        close = self.data['close']
        volume = self.data['volume']

        # Calculate VWMA
        pv = close * volume
        vwma = pv.rolling(window=period).sum() / volume.rolling(window=period).sum()

        current_price = close.iloc[-1]
        current_vwma = vwma.iloc[-1]

        # Calculate percentage difference
        diff_percent = ((current_price - current_vwma) / current_vwma) * 100

        # Signal determination
        if diff_percent > 1.0:
            signal = 'buy'
            strength = min(100, abs(diff_percent) * 10)
        elif diff_percent < -1.0:
            signal = 'sell'
            strength = min(100, abs(diff_percent) * 10)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'vwma': float(current_vwma),
            'current_price': float(current_price),
            'diff_percent': float(diff_percent),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['vwma']
        }

    def calculate_stochastic(self, k_period: int = 14, d_period: int = 3) -> Dict:
        """
        Calculate Stochastic Oscillator.

        Formula:
        - %K = ((Close - Low14) / (High14 - Low14)) × 100
        - %D = SMA(%K, 3)

        Signal logic:
        - Buy: %K < 20 (oversold) and %K crosses above %D
        - Sell: %K > 80 (overbought) and %K crosses below %D
        - Neutral: Otherwise

        Args:
            k_period: Period for %K calculation (default 14)
            d_period: Period for %D calculation (default 3)

        Returns:
            Dict with 'k', 'd', 'signal', 'strength', 'weight'
        """
        close = self.data['close']
        high = self.data['high']
        low = self.data['low']

        # Calculate %K
        lowest_low = low.rolling(window=k_period).min()
        highest_high = high.rolling(window=k_period).max()

        k = ((close - lowest_low) / (highest_high - lowest_low)) * 100

        # Calculate %D (SMA of %K)
        d = k.rolling(window=d_period).mean()

        current_k = k.iloc[-1]
        current_d = d.iloc[-1]
        previous_k = k.iloc[-2]
        previous_d = d.iloc[-2]

        # Signal determination
        if current_k < 20 and current_k > current_d and previous_k <= previous_d:
            signal = 'buy'
            strength = float(20 - current_k)
        elif current_k > 80 and current_k < current_d and previous_k >= previous_d:
            signal = 'sell'
            strength = float(current_k - 80)
        else:
            signal = 'neutral'
            strength = 0

        return {
            'k': float(current_k),
            'd': float(current_d),
            'signal': signal,
            'strength': float(strength),
            'weight': self.WEIGHTS['stochastic']
        }

    def calculate_all(self) -> Dict:
        """
        Calculate all 8 technical indicators and perform weighted voting.

        Returns:
            Dict with all indicators, individual signals, and final weighted signal
        """
        results = {
            'ma': self.calculate_sma(),
            'macd': self.calculate_macd(),
            'rsi': self.calculate_rsi(),
            'bollinger': self.calculate_bollinger_bands(),
            'atr': self.calculate_atr(),
            'volume': self.calculate_volume_ratio(),
            'vwma': self.calculate_vwma(),
            'stochastic': self.calculate_stochastic()
        }

        # Weighted voting
        buy_score = 0
        sell_score = 0
        total_weight = 0

        for indicator, data in results.items():
            if 'signal' in data:
                weight = data['weight']
                signal = data['signal']

                if signal == 'buy':
                    buy_score += weight
                elif signal == 'sell':
                    sell_score += weight

                total_weight += weight

        # Determine final signal
        if buy_score > sell_score and (buy_score / total_weight) > 0.5:
            final_signal = 'buy'
            confidence = (buy_score / total_weight) * 100
        elif sell_score > buy_score and (sell_score / total_weight) > 0.5:
            final_signal = 'sell'
            confidence = (sell_score / total_weight) * 100
        else:
            final_signal = 'neutral'
            confidence = 50

        return {
            'indicators': results,
            'weighted_voting': {
                'buy_score': float(buy_score),
                'sell_score': float(sell_score),
                'total_weight': float(total_weight),
                'final_signal': final_signal,
                'confidence': float(confidence)
            }
        }


# Convenience function for quick analysis
def analyze_market_data(data: pd.DataFrame) -> Dict:
    """
    Convenience function to analyze market data with all indicators.

    Args:
        data: DataFrame with OHLCV data

    Returns:
        Dict with all indicator results and weighted voting
    """
    indicators = TechnicalIndicators(data)
    return indicators.calculate_all()
