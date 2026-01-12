"""
Backtest Engine
Simulates trading strategy execution and calculates performance metrics.

Features:
- Trade simulation with entry/exit/stop-loss
- Performance metrics: Sharpe ratio, win rate, max drawdown, R:R ratio
- Walk-forward analysis support
- Risk management validation
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType


class BacktestEngine:
    """
    Backtesting engine for trading strategies.

    Example usage:
        engine = BacktestEngine(data=historical_data, initial_capital=1000000)
        trades = [
            {'date': '2025-01-01', 'action': 'buy', 'price': 40000, 'stop_loss': 39500, 'take_profit': 41000},
            {'date': '2025-01-05', 'action': 'sell', 'price': 40800}
        ]
        results = engine.run_backtest(trades)
        print(f"Sharpe Ratio: {results['sharpe_ratio']}")
    """

    def __init__(
        self,
        data: pd.DataFrame,
        initial_capital: float = 1000000,
        position_size_pct: float = 0.95,
        commission_pct: float = 0.001,
        slippage_pct: float = 0.001,
        max_volume_pct: float = 0.01
    ):
        """
        Initialize backtest engine.

        Args:
            data: DataFrame with OHLCV data (columns: date, open, high, low, close, volume)
            initial_capital: Starting capital in JPY (default: 1,000,000)
            position_size_pct: Position size as % of capital (default: 95%)
            commission_pct: Commission rate as % (default: 0.1%)
            slippage_pct: Slippage rate as % (default: 0.1%)
            max_volume_pct: Max position size as % of daily volume (default: 1%)
        """
        self.data = data.copy()
        self.initial_capital = initial_capital
        self.position_size_pct = position_size_pct
        self.commission_pct = commission_pct
        self.slippage_pct = slippage_pct
        self.max_volume_pct = max_volume_pct

        # Ensure date column is datetime
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data = self.data.set_index('date')

    def run_backtest(self, signals: List[Dict]) -> Dict:
        """
        Run backtest with trading signals.

        Args:
            signals: List of trading signals with format:
                [
                    {
                        'date': 'YYYY-MM-DD',
                        'action': 'buy' | 'sell',
                        'entry_price': float,
                        'stop_loss': float (optional),
                        'take_profit': float (optional),
                        'risk_reward_ratio': float (optional)
                    },
                    ...
                ]

        Returns:
            Dict with backtest results:
                {
                    'total_trades': int,
                    'winning_trades': int,
                    'losing_trades': int,
                    'win_rate': float (%),
                    'total_return': float (%),
                    'sharpe_ratio': float,
                    'max_drawdown': float (%),
                    'avg_rr_ratio': float,
                    'final_capital': float,
                    'trades': List[Dict]  # Detailed trade results
                }
        """
        capital = self.initial_capital
        trades_log = []
        equity_curve = [capital]
        current_position = None

        # Create signal lookup dictionary for faster access
        signal_dict = {}
        for signal in signals:
            signal_date = pd.to_datetime(signal['date'])
            if signal_date not in signal_dict:
                signal_dict[signal_date] = []
            signal_dict[signal_date].append(signal)

        # Process each day in the data (daily loop for stop-loss/take-profit checks)
        for current_date in self.data.index:
            price_data = self.data.loc[current_date]

            # Check stop-loss and take-profit if position is open
            if current_position is not None:
                high = price_data['high']
                low = price_data['low']

                # Check stop-loss hit (price went down)
                if current_position['stop_loss'] and low <= current_position['stop_loss']:
                    # Apply slippage - worse price for long positions (lower than stop loss)
                    exit_price = current_position['stop_loss'] * (1 - self.slippage_pct)
                    exit_value = current_position['size'] * exit_price
                    commission = exit_value * self.commission_pct

                    pnl = exit_value - (current_position['size'] * current_position['entry_price']) - current_position['commission_paid'] - commission
                    capital += exit_value - commission

                    trade_result = {
                        'entry_date': current_position['entry_date'].strftime('%Y-%m-%d'),
                        'exit_date': current_date.strftime('%Y-%m-%d'),
                        'entry_price': float(current_position['entry_price']),
                        'exit_price': float(exit_price),
                        'size': float(current_position['size']),
                        'pnl': float(pnl),
                        'return_pct': float((exit_price / current_position['entry_price'] - 1) * 100),
                        'exit_reason': 'stop_loss',
                        'commission_total': float(current_position['commission_paid'] + commission)
                    }
                    trades_log.append(trade_result)

                    current_position = None
                    equity_curve.append(capital)
                    continue  # Skip to next day

                # Check take-profit hit (price went up)
                elif current_position['take_profit'] and high >= current_position['take_profit']:
                    # Apply slippage - slightly worse price than take profit target
                    exit_price = current_position['take_profit'] * (1 - self.slippage_pct)
                    exit_value = current_position['size'] * exit_price
                    commission = exit_value * self.commission_pct

                    pnl = exit_value - (current_position['size'] * current_position['entry_price']) - current_position['commission_paid'] - commission
                    capital += exit_value - commission

                    trade_result = {
                        'entry_date': current_position['entry_date'].strftime('%Y-%m-%d'),
                        'exit_date': current_date.strftime('%Y-%m-%d'),
                        'entry_price': float(current_position['entry_price']),
                        'exit_price': float(exit_price),
                        'size': float(current_position['size']),
                        'pnl': float(pnl),
                        'return_pct': float((exit_price / current_position['entry_price'] - 1) * 100),
                        'exit_reason': 'take_profit',
                        'commission_total': float(current_position['commission_paid'] + commission)
                    }
                    trades_log.append(trade_result)

                    current_position = None
                    equity_curve.append(capital)
                    continue  # Skip to next day

            # Process signals for this date
            if current_date in signal_dict:
                for signal in signal_dict[current_date]:
                    action = signal['action'].lower()

                    if action == 'buy' and current_position is None:
                        # Open long position - Use NEXT day's open to avoid look-ahead bias
                        # Rationale: On current_date, we can only see closing price after market close.
                        # In reality, we cannot trade at that price - we must wait for next day's open.
                        signal_idx = self.data.index.get_loc(current_date)

                        # Check if there is a next trading day
                        if signal_idx + 1 >= len(self.data):
                            continue  # Skip if this is the last day

                        next_date = self.data.index[signal_idx + 1]
                        next_day_data = self.data.loc[next_date]

                        # Entry at next day's open price (no look-ahead bias)
                        entry_price = signal.get('entry_price', next_day_data['open'])
                        entry_date = next_date  # Actual entry is next day

                        # Calculate position size with liquidity constraint
                        max_shares_by_capital = (capital * self.position_size_pct) / entry_price
                        max_shares_by_volume = next_day_data['volume'] * self.max_volume_pct
                        position_size = min(max_shares_by_capital, max_shares_by_volume)

                        # Recalculate commission based on actual position size
                        position_value = position_size * entry_price
                        commission = position_value * self.commission_pct

                        current_position = {
                            'entry_date': entry_date,  # Use next day
                            'entry_price': entry_price,
                            'size': position_size,
                            'stop_loss': signal.get('stop_loss'),
                            'take_profit': signal.get('take_profit'),
                            'commission_paid': commission
                        }

                        # Deduct position value and commission from capital
                        position_value = position_size * entry_price
                        capital -= (position_value + commission)

                    elif action == 'sell' and current_position is not None:
                        # Close long position
                        exit_price = signal.get('exit_price', price_data['close'])

                        # Apply slippage - worse price for long position exit
                        exit_price = exit_price * (1 - self.slippage_pct)

                        exit_value = current_position['size'] * exit_price
                        commission = exit_value * self.commission_pct

                        pnl = exit_value - (current_position['size'] * current_position['entry_price']) - current_position['commission_paid'] - commission
                        capital += exit_value - commission

                        # Log trade
                        trade_result = {
                            'entry_date': current_position['entry_date'].strftime('%Y-%m-%d'),
                            'exit_date': current_date.strftime('%Y-%m-%d'),
                            'entry_price': float(current_position['entry_price']),
                            'exit_price': float(exit_price),
                            'size': float(current_position['size']),
                            'pnl': float(pnl),
                            'return_pct': float((exit_price / current_position['entry_price'] - 1) * 100),
                            'commission_total': float(current_position['commission_paid'] + commission)
                        }
                        trades_log.append(trade_result)

                        current_position = None
                        equity_curve.append(capital)

        # Calculate performance metrics
        metrics = self._calculate_metrics(trades_log, equity_curve, capital)

        return {
            **metrics,
            'trades': trades_log,
            'final_capital': float(capital),
            'equity_curve': [float(e) for e in equity_curve]
        }

    def _calculate_metrics(
        self,
        trades: List[Dict],
        equity_curve: List[float],
        final_capital: float
    ) -> Dict:
        """
        Calculate performance metrics from trades.

        Args:
            trades: List of completed trades
            equity_curve: Capital over time
            final_capital: Final capital after all trades

        Returns:
            Dict with performance metrics
        """
        if len(trades) == 0:
            return {
                'total_trades': 0,
                'winning_trades': 0,
                'losing_trades': 0,
                'win_rate': 0,
                'total_return': 0,
                'sharpe_ratio': 0,
                'max_drawdown': 0,
                'avg_rr_ratio': 0
            }

        # Basic trade statistics
        total_trades = len(trades)
        winning_trades = len([t for t in trades if t['pnl'] > 0])
        losing_trades = len([t for t in trades if t['pnl'] < 0])
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0

        # Total return
        total_return = ((final_capital / self.initial_capital) - 1) * 100

        # Sharpe ratio
        returns = pd.Series([t['return_pct'] for t in trades])
        sharpe_ratio = 0
        if len(returns) > 1 and returns.std() != 0:
            sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252 / len(returns))

        # Maximum drawdown
        max_drawdown = self._calculate_max_drawdown(equity_curve)

        # Average Risk:Reward ratio
        avg_rr_ratio = 0
        rr_trades = []
        for trade in trades:
            if trade['pnl'] > 0:  # Winning trade
                reward = abs(trade['return_pct'])
                # Estimate risk from entry to typical 2% stop
                risk = 2.0
                rr_trades.append(reward / risk)

        if rr_trades:
            avg_rr_ratio = np.mean(rr_trades)

        return {
            'total_trades': total_trades,
            'winning_trades': winning_trades,
            'losing_trades': losing_trades,
            'win_rate': float(win_rate),
            'total_return': float(total_return),
            'sharpe_ratio': float(sharpe_ratio),
            'max_drawdown': float(max_drawdown),
            'avg_rr_ratio': float(avg_rr_ratio)
        }

    def _calculate_max_drawdown(self, equity_curve: List[float]) -> float:
        """
        Calculate maximum drawdown from equity curve.

        Args:
            equity_curve: List of capital values over time

        Returns:
            Maximum drawdown as percentage
        """
        if len(equity_curve) < 2:
            return 0

        equity = pd.Series(equity_curve)
        running_max = equity.expanding().max()
        drawdown = (equity - running_max) / running_max * 100

        return abs(float(drawdown.min()))

    def walk_forward_analysis(
        self,
        signals: List[Dict],
        in_sample_ratio: float = 0.7,
        num_windows: int = 5
    ) -> Dict:
        """
        Perform walk-forward analysis.

        Args:
            signals: All trading signals
            in_sample_ratio: Ratio of in-sample period (default: 70%)
            num_windows: Number of walk-forward windows (default: 5)

        Returns:
            Dict with walk-forward results:
                {
                    'windows': List[Dict],  # Results for each window
                    'wf_efficiency': float,  # Walk-forward efficiency (%)
                    'avg_in_sample_sharpe': float,
                    'avg_out_sample_sharpe': float
                }
        """
        # Sort signals by date
        sorted_signals = sorted(signals, key=lambda x: pd.to_datetime(x['date']))

        window_size = len(sorted_signals) // num_windows
        in_sample_size = int(window_size * in_sample_ratio)
        out_sample_size = window_size - in_sample_size

        windows_results = []

        for i in range(num_windows):
            start_idx = i * window_size
            end_idx = start_idx + window_size

            if end_idx > len(sorted_signals):
                break

            # In-sample period
            in_sample_signals = sorted_signals[start_idx:start_idx + in_sample_size]
            in_sample_results = self.run_backtest(in_sample_signals)

            # Out-of-sample period
            out_sample_signals = sorted_signals[start_idx + in_sample_size:end_idx]
            out_sample_results = self.run_backtest(out_sample_signals)

            windows_results.append({
                'window': i + 1,
                'in_sample': {
                    'sharpe_ratio': in_sample_results['sharpe_ratio'],
                    'total_return': in_sample_results['total_return'],
                    'win_rate': in_sample_results['win_rate']
                },
                'out_sample': {
                    'sharpe_ratio': out_sample_results['sharpe_ratio'],
                    'total_return': out_sample_results['total_return'],
                    'win_rate': out_sample_results['win_rate']
                }
            })

        # Calculate walk-forward efficiency
        avg_in_sample_sharpe = np.mean([w['in_sample']['sharpe_ratio'] for w in windows_results])
        avg_out_sample_sharpe = np.mean([w['out_sample']['sharpe_ratio'] for w in windows_results])

        wf_efficiency = 0
        if avg_in_sample_sharpe != 0:
            wf_efficiency = (avg_out_sample_sharpe / avg_in_sample_sharpe) * 100

        return {
            'windows': windows_results,
            'wf_efficiency': float(wf_efficiency),
            'avg_in_sample_sharpe': float(avg_in_sample_sharpe),
            'avg_out_sample_sharpe': float(avg_out_sample_sharpe),
            'recommendation': 'pass' if wf_efficiency >= 50 else 'fail'
        }

    def analyze_by_regime(self, signals: List[Dict]) -> Dict:
        """
        Analyze backtest performance by market regime.

        Args:
            signals: Trading signals

        Returns:
            Dict with performance metrics for each regime:
                {
                    'regime_performance': {
                        'bull': {...},
                        'bear': {...},
                        'sideways': {...}
                    },
                    'regime_statistics': {
                        'bull': {'days': int, 'percentage': float},
                        'bear': {'days': int, 'percentage': float},
                        'sideways': {'days': int, 'percentage': float}
                    }
                }
        """
        # Detect regimes
        detector = MarketRegimeDetector(self.data)
        regime_series = detector.detect_regime_combined()

        # Run backtest for each regime
        regime_results = {}

        for regime_type in [RegimeType.BULL.value, RegimeType.BEAR.value, RegimeType.SIDEWAYS.value]:
            # Filter signals for this regime
            regime_signals = []
            for signal in signals:
                signal_date = pd.to_datetime(signal['date'])
                if signal_date in regime_series.index:
                    if regime_series.loc[signal_date] == regime_type:
                        regime_signals.append(signal)

            # Run backtest for this regime
            if len(regime_signals) > 0:
                results = self.run_backtest(regime_signals)
                regime_results[regime_type] = results
            else:
                regime_results[regime_type] = {
                    'total_trades': 0,
                    'winning_trades': 0,
                    'losing_trades': 0,
                    'win_rate': 0,
                    'total_return': 0,
                    'sharpe_ratio': 0,
                    'max_drawdown': 0,
                    'avg_rr_ratio': 0
                }

        # Calculate overall regime statistics
        regime_stats = detector.get_regime_statistics(regime_series)

        return {
            'regime_performance': regime_results,
            'regime_statistics': regime_stats,
            'regime_series': regime_series
        }


# Convenience function
def quick_backtest(data: pd.DataFrame, signals: List[Dict], initial_capital: float = 1000000) -> Dict:
    """
    Quick backtest wrapper.

    Args:
        data: OHLCV data
        signals: Trading signals
        initial_capital: Starting capital (default: 1,000,000 JPY)

    Returns:
        Backtest results

    Example:
        results = quick_backtest(data, signals)
        print(f"Win Rate: {results['win_rate']}%")
    """
    engine = BacktestEngine(data=data, initial_capital=initial_capital)
    return engine.run_backtest(signals)


# Example usage (for testing)
if __name__ == "__main__":
    print("Backtest Engine - Test Run")
    print("=" * 60)

    # Sample market data
    sample_data = pd.DataFrame({
        'date': pd.date_range('2025-01-01', periods=30, freq='D'),
        'open': np.random.randint(39000, 41000, 30),
        'high': np.random.randint(39500, 41500, 30),
        'low': np.random.randint(38500, 40500, 30),
        'close': np.random.randint(39000, 41000, 30),
        'volume': np.random.randint(100000, 200000, 30)
    })

    # Sample trading signals
    sample_signals = [
        {
            'date': '2025-01-02',
            'action': 'buy',
            'entry_price': 40000,
            'stop_loss': 39500,
            'take_profit': 41000
        },
        {
            'date': '2025-01-10',
            'action': 'sell',
            'exit_price': 40800
        },
        {
            'date': '2025-01-15',
            'action': 'buy',
            'entry_price': 39500,
            'stop_loss': 39000,
            'take_profit': 40500
        },
        {
            'date': '2025-01-20',
            'action': 'sell',
            'exit_price': 40200
        }
    ]

    print("\n1. Running backtest...")
    engine = BacktestEngine(data=sample_data, initial_capital=1000000)
    results = engine.run_backtest(sample_signals)

    print(f"✅ Backtest completed")
    print(f"\nPerformance Metrics:")
    print(f"  Total Trades: {results['total_trades']}")
    print(f"  Win Rate: {results['win_rate']:.2f}%")
    print(f"  Total Return: {results['total_return']:.2f}%")
    print(f"  Sharpe Ratio: {results['sharpe_ratio']:.2f}")
    print(f"  Max Drawdown: {results['max_drawdown']:.2f}%")
    print(f"  Final Capital: ¥{results['final_capital']:,.0f}")

    print(f"\nTrade Details:")
    for i, trade in enumerate(results['trades'], 1):
        print(f"  Trade {i}: {trade['entry_date']} → {trade['exit_date']}")
        print(f"    Entry: ¥{trade['entry_price']:,.0f}, Exit: ¥{trade['exit_price']:,.0f}")
        print(f"    P&L: ¥{trade['pnl']:,.0f} ({trade['return_pct']:.2f}%)")

    print("\n" + "=" * 60)
    print("✅ Test completed")
