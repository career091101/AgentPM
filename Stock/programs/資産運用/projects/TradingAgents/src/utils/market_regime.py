"""
Market Regime Detection Module
Detects market regime (Bull, Bear, Sideways) for backtesting analysis.

Three regime detection methods:
1. Moving Average based (SMA 50 vs SMA 200)
2. Trend-based (linear regression slope)
3. Volatility-based (ATR/Price ratio)
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from enum import Enum


class RegimeType(Enum):
    """Market regime types"""
    BULL = "bull"      # Uptrend market
    BEAR = "bear"      # Downtrend market
    SIDEWAYS = "sideways"  # Range-bound market


class MarketRegimeDetector:
    """
    Detects market regime using multiple methods.

    Example:
        detector = MarketRegimeDetector(data)
        regimes = detector.detect_regime_periods()
        print(f"Bull periods: {regimes['bull']}")
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize with OHLCV data.

        Args:
            data: DataFrame with columns ['date', 'open', 'high', 'low', 'close', 'volume']
        """
        self.data = data.copy()

        # Ensure datetime index
        if 'date' in self.data.columns and not isinstance(self.data.index, pd.DatetimeIndex):
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data = self.data.set_index('date')

        self._validate_data()

    def _validate_data(self):
        """Validate input data has required columns."""
        required_columns = {'close', 'high', 'low'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Data must contain columns: {required_columns}")

    def detect_regime_ma_based(
        self,
        short_window: int = 50,
        long_window: int = 200
    ) -> pd.Series:
        """
        Detect regime using Moving Average crossover.

        Logic:
        - Bull: Price > SMA50 AND SMA50 > SMA200
        - Bear: Price < SMA50 AND SMA50 < SMA200
        - Sideways: Otherwise

        Args:
            short_window: Short MA period (default 50)
            long_window: Long MA period (default 200)

        Returns:
            Series with regime labels for each date
        """
        close = self.data['close']

        sma_short = close.rolling(window=short_window).mean()
        sma_long = close.rolling(window=long_window).mean()

        regime = pd.Series(index=self.data.index, dtype=str)

        # Bull market: Price > SMA50 > SMA200
        bull_condition = (close > sma_short) & (sma_short > sma_long)
        regime[bull_condition] = RegimeType.BULL.value

        # Bear market: Price < SMA50 < SMA200
        bear_condition = (close < sma_short) & (sma_short < sma_long)
        regime[bear_condition] = RegimeType.BEAR.value

        # Sideways: Everything else
        regime[~bull_condition & ~bear_condition] = RegimeType.SIDEWAYS.value

        return regime

    def detect_regime_trend_based(
        self,
        lookback: int = 60,
        bull_threshold: float = 0.0002,
        bear_threshold: float = -0.0002
    ) -> pd.Series:
        """
        Detect regime using linear regression slope.

        Logic:
        - Bull: Slope > bull_threshold (positive trend)
        - Bear: Slope < bear_threshold (negative trend)
        - Sideways: Slope between thresholds

        Args:
            lookback: Period for slope calculation (default 60)
            bull_threshold: Minimum slope for bull market (default 0.0002)
            bear_threshold: Maximum slope for bear market (default -0.0002)

        Returns:
            Series with regime labels for each date
        """
        close = self.data['close']
        regime = pd.Series(index=self.data.index, dtype=str)

        for i in range(lookback, len(close)):
            # Get lookback period
            y = close.iloc[i-lookback:i].values
            x = np.arange(lookback)

            # Linear regression
            slope, _ = np.polyfit(x, y, 1)

            # Normalize slope by price
            normalized_slope = slope / close.iloc[i]

            # Classify regime
            if normalized_slope > bull_threshold:
                regime.iloc[i] = RegimeType.BULL.value
            elif normalized_slope < bear_threshold:
                regime.iloc[i] = RegimeType.BEAR.value
            else:
                regime.iloc[i] = RegimeType.SIDEWAYS.value

        return regime

    def detect_regime_volatility_based(
        self,
        atr_period: int = 14,
        high_volatility_threshold: float = 0.02
    ) -> pd.Series:
        """
        Detect regime using volatility (ATR/Price ratio).

        High volatility often indicates trending markets.

        Args:
            atr_period: ATR calculation period (default 14)
            high_volatility_threshold: Threshold for high volatility (default 2%)

        Returns:
            Series with regime labels for each date
        """
        close = self.data['close']
        high = self.data['high']
        low = self.data['low']

        # Calculate ATR
        prev_close = close.shift(1)
        tr1 = high - low
        tr2 = abs(high - prev_close)
        tr3 = abs(low - prev_close)
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = true_range.ewm(span=atr_period, adjust=False).mean()

        # ATR as percentage of price
        atr_pct = atr / close

        # Use MA-based for direction, volatility for confirmation
        ma_regime = self.detect_regime_ma_based()

        regime = pd.Series(index=self.data.index, dtype=str)

        for i in range(len(self.data)):
            if atr_pct.iloc[i] > high_volatility_threshold:
                # High volatility: Use MA-based regime (trending)
                regime.iloc[i] = ma_regime.iloc[i]
            else:
                # Low volatility: Likely sideways
                regime.iloc[i] = RegimeType.SIDEWAYS.value

        return regime

    def detect_regime_combined(self) -> pd.Series:
        """
        Combined regime detection using voting from multiple methods.

        Returns:
            Series with regime labels based on majority voting
        """
        ma_regime = self.detect_regime_ma_based()
        trend_regime = self.detect_regime_trend_based()
        vol_regime = self.detect_regime_volatility_based()

        regime = pd.Series(index=self.data.index, dtype=str)

        for i in range(len(self.data)):
            votes = {
                RegimeType.BULL.value: 0,
                RegimeType.BEAR.value: 0,
                RegimeType.SIDEWAYS.value: 0
            }

            # Count votes
            if pd.notna(ma_regime.iloc[i]):
                votes[ma_regime.iloc[i]] += 1
            if pd.notna(trend_regime.iloc[i]):
                votes[trend_regime.iloc[i]] += 1
            if pd.notna(vol_regime.iloc[i]):
                votes[vol_regime.iloc[i]] += 1

            # Majority vote
            regime.iloc[i] = max(votes, key=votes.get)

        return regime

    def get_regime_periods(self, regime_series: pd.Series = None) -> Dict[str, List[Tuple]]:
        """
        Get start and end dates for each regime period.

        Args:
            regime_series: Series with regime labels (default: combined detection)

        Returns:
            Dict with regime types as keys and list of (start_date, end_date) tuples
        """
        if regime_series is None:
            regime_series = self.detect_regime_combined()

        periods = {
            RegimeType.BULL.value: [],
            RegimeType.BEAR.value: [],
            RegimeType.SIDEWAYS.value: []
        }

        current_regime = None
        start_date = None

        for date, regime in regime_series.items():
            if pd.isna(regime):
                continue

            if regime != current_regime:
                # Regime changed
                if current_regime is not None and start_date is not None:
                    periods[current_regime].append((start_date, self.data.index[self.data.index.get_loc(date) - 1]))

                current_regime = regime
                start_date = date

        # Add final period
        if current_regime is not None and start_date is not None:
            periods[current_regime].append((start_date, self.data.index[-1]))

        return periods

    def get_regime_statistics(self, regime_series: pd.Series = None) -> Dict:
        """
        Calculate statistics for each regime.

        Returns:
            Dict with regime statistics (count, percentage, avg duration)
        """
        if regime_series is None:
            regime_series = self.detect_regime_combined()

        total_days = len(regime_series)
        regime_counts = regime_series.value_counts()

        stats = {}
        for regime_type in [RegimeType.BULL.value, RegimeType.BEAR.value, RegimeType.SIDEWAYS.value]:
            count = regime_counts.get(regime_type, 0)
            stats[regime_type] = {
                'days': int(count),
                'percentage': float(count / total_days * 100) if total_days > 0 else 0
            }

        return stats


# Convenience function
def detect_market_regime(data: pd.DataFrame) -> pd.Series:
    """
    Quick regime detection using combined method.

    Args:
        data: OHLCV DataFrame

    Returns:
        Series with regime labels
    """
    detector = MarketRegimeDetector(data)
    return detector.detect_regime_combined()
