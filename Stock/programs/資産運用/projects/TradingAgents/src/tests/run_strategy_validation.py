"""
Strategy Validation Script

Validates the three new strategies against success criteria:
1. Train-Test gap <30%
2. Test Sharpe >0.5
3. Test Win Rate >50%

Runs comprehensive backtests and generates performance report.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
from typing import Dict, List
from datetime import datetime

# Add parent to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from strategy.mean_reversion_strategy import MeanReversionStrategy
from strategy.trend_following_strategy import TrendFollowingStrategy
from strategy.portfolio_strategy import PortfolioStrategy


def generate_test_data(data_type: str = 'mixed') -> pd.DataFrame:
    """
    Generate synthetic test data.

    Args:
        data_type: 'sideways', 'trending', or 'mixed'

    Returns:
        DataFrame with OHLCV data
    """
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
    np.random.seed(42)

    base_price = 40000
    noise = np.random.randn(len(dates)) * 500

    if data_type == 'sideways':
        # Oscillating pattern
        pattern = np.sin(np.arange(len(dates)) / 30) * 2000
    elif data_type == 'trending':
        # Upward trend
        pattern = np.arange(len(dates)) * 5
    else:  # mixed
        # Trend + oscillation
        pattern = np.arange(len(dates)) * 3 + np.sin(np.arange(len(dates)) / 30) * 1000

    data = pd.DataFrame({
        'date': dates,
        'open': base_price + pattern + noise,
        'high': base_price + pattern + noise + np.abs(np.random.randn(len(dates)) * 300),
        'low': base_price + pattern + noise - np.abs(np.random.randn(len(dates)) * 300),
        'close': base_price + pattern + noise,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index('date')
    return data


def run_backtest(
    strategy,
    data: pd.DataFrame,
    initial_capital: float = 10000000
) -> Dict:
    """Run backtest for a strategy."""
    capital = initial_capital
    position = 0
    position_price = 0
    trades = []
    equity_curve = []

    for date in data.index:
        signal = strategy.generate_signal(data, date)
        current_price = signal['price']

        # Execute trades
        if signal['action'] == 'buy' and position == 0:
            position_size = signal['position_size']
            shares = int((capital * min(position_size, 1.0)) / current_price)

            if shares > 0:
                position = shares
                position_price = current_price
                capital -= shares * current_price

                trades.append({
                    'date': date,
                    'action': 'buy',
                    'price': current_price,
                    'shares': shares,
                    'capital': capital
                })

        elif signal['action'] == 'sell' and position > 0:
            sell_value = position * current_price
            profit = sell_value - (position * position_price)
            capital += sell_value

            trades.append({
                'date': date,
                'action': 'sell',
                'price': current_price,
                'shares': position,
                'capital': capital,
                'profit': profit,
                'return': (profit / (position * position_price)) if position * position_price > 0 else 0
            })

            position = 0
            position_price = 0

        # Track equity
        total_equity = capital + (position * current_price if position > 0 else 0)
        equity_curve.append({
            'date': date,
            'equity': total_equity,
            'capital': capital,
            'position': position
        })

    # Final equity
    final_equity = capital + (position * data['close'].iloc[-1] if position > 0 else 0)

    return {
        'trades': trades,
        'equity_curve': equity_curve,
        'initial_capital': initial_capital,
        'final_capital': final_equity,
        'total_return': (final_equity - initial_capital) / initial_capital
    }


def calculate_metrics(backtest_results: Dict) -> Dict:
    """Calculate performance metrics."""
    trades = backtest_results['trades']
    equity_curve = pd.DataFrame(backtest_results['equity_curve'])

    # Calculate returns
    equity_curve['returns'] = equity_curve['equity'].pct_change()

    # Total return
    total_return = backtest_results['total_return']

    # Win rate
    completed_trades = [t for t in trades if 'profit' in t]
    profitable_trades = [t for t in completed_trades if t['profit'] > 0]
    total_trades = len(completed_trades)
    win_rate = len(profitable_trades) / total_trades if total_trades > 0 else 0

    # Sharpe ratio (annualized)
    returns = equity_curve['returns'].dropna()
    if len(returns) > 0 and returns.std() > 0:
        sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)
    else:
        sharpe_ratio = 0

    # Max drawdown
    equity = equity_curve['equity']
    cummax = equity.expanding().max()
    drawdown = (equity - cummax) / cummax
    max_drawdown = drawdown.min()

    # Average trade return
    if completed_trades:
        avg_trade_return = np.mean([t['return'] for t in completed_trades])
    else:
        avg_trade_return = 0

    return {
        'total_return': float(total_return),
        'win_rate': float(win_rate),
        'sharpe_ratio': float(sharpe_ratio),
        'max_drawdown': float(max_drawdown),
        'total_trades': total_trades,
        'profitable_trades': len(profitable_trades),
        'avg_trade_return': float(avg_trade_return)
    }


def calculate_train_test_gap(train_metrics: Dict, test_metrics: Dict) -> float:
    """Calculate train-test gap percentage."""
    train_return = train_metrics['total_return']
    test_return = test_metrics['total_return']

    if train_return == 0:
        return 0

    gap = ((test_return - train_return) / abs(train_return)) * 100
    return gap


def print_separator(char='=', length=80):
    """Print separator line."""
    print(char * length)


def main():
    """Main validation function."""
    print_separator()
    print("STRATEGY VALIDATION - PHASE 6")
    print_separator()
    print()

    # Generate test data
    print("1. Generating test data...")
    mixed_data = generate_test_data('mixed')
    print(f"   Data period: {mixed_data.index[0].date()} to {mixed_data.index[-1].date()}")
    print(f"   Total days: {len(mixed_data)}")
    print()

    # Split data: 80% train, 20% test
    split_idx = int(len(mixed_data) * 0.8)
    train_data = mixed_data.iloc[:split_idx]
    test_data = mixed_data.iloc[split_idx:]

    print(f"   Train period: {train_data.index[0].date()} to {train_data.index[-1].date()} ({len(train_data)} days)")
    print(f"   Test period: {test_data.index[0].date()} to {test_data.index[-1].date()} ({len(test_data)} days)")
    print()

    # Initialize strategies
    print("2. Initializing strategies...")
    strategies = {
        'Mean Reversion': MeanReversionStrategy(
            rsi_oversold=30,
            rsi_overbought=70,
            use_volatility_sizing=True
        ),
        'Trend Following': TrendFollowingStrategy(
            macd_fast=12,
            macd_slow=26,
            use_ma_filter=True
        ),
        'Portfolio': PortfolioStrategy(
            mean_reversion_weight=0.4,
            trend_following_weight=0.6,
            use_dynamic_weights=True,
            use_regime_filter=True
        )
    }
    print(f"   Initialized {len(strategies)} strategies")
    print()

    # Run backtests
    print("3. Running backtests...")
    print_separator('-')

    all_results = {}

    for name, strategy in strategies.items():
        print(f"\n{name} Strategy:")
        print("-" * 40)

        # Train backtest
        print("   Running train backtest...")
        train_results = run_backtest(strategy, train_data)
        train_metrics = calculate_metrics(train_results)

        # Test backtest
        print("   Running test backtest...")
        test_results = run_backtest(strategy, test_data)
        test_metrics = calculate_metrics(test_results)

        # Calculate gap
        gap = calculate_train_test_gap(train_metrics, test_metrics)

        all_results[name] = {
            'train': train_metrics,
            'test': test_metrics,
            'gap': gap
        }

        # Print results
        print("\n   Train Metrics:")
        print(f"      Total Return:     {train_metrics['total_return']:>10.2%}")
        print(f"      Sharpe Ratio:     {train_metrics['sharpe_ratio']:>10.2f}")
        print(f"      Win Rate:         {train_metrics['win_rate']:>10.2%}")
        print(f"      Max Drawdown:     {train_metrics['max_drawdown']:>10.2%}")
        print(f"      Total Trades:     {train_metrics['total_trades']:>10d}")

        print("\n   Test Metrics:")
        print(f"      Total Return:     {test_metrics['total_return']:>10.2%}")
        print(f"      Sharpe Ratio:     {test_metrics['sharpe_ratio']:>10.2f}")
        print(f"      Win Rate:         {test_metrics['win_rate']:>10.2%}")
        print(f"      Max Drawdown:     {test_metrics['max_drawdown']:>10.2%}")
        print(f"      Total Trades:     {test_metrics['total_trades']:>10d}")

        print(f"\n   Train-Test Gap:   {gap:>10.1f}%")
        print()

    # Summary comparison
    print_separator()
    print("\n4. STRATEGY COMPARISON SUMMARY")
    print_separator()
    print()

    print(f"{'Strategy':<20} {'Train Ret':<12} {'Test Ret':<12} {'Gap':<10} {'Test Sharpe':<12} {'Test WR':<10}")
    print_separator('-')

    for name, results in all_results.items():
        train_ret = results['train']['total_return']
        test_ret = results['test']['total_return']
        gap = results['gap']
        sharpe = results['test']['sharpe_ratio']
        win_rate = results['test']['win_rate']

        print(f"{name:<20} {train_ret:>10.2%}  {test_ret:>10.2%}  {gap:>8.1f}%  {sharpe:>10.2f}  {win_rate:>8.2%}")

    print()

    # Success criteria evaluation
    print_separator()
    print("\n5. SUCCESS CRITERIA EVALUATION")
    print_separator()
    print()

    success_criteria = {
        'Train-Test Gap < 30%': lambda r: abs(r['gap']) < 30,
        'Test Sharpe > 0.5': lambda r: r['test']['sharpe_ratio'] > 0.5,
        'Test Win Rate > 50%': lambda r: r['test']['win_rate'] > 0.5
    }

    for name, results in all_results.items():
        print(f"{name}:")

        criteria_met = 0
        total_criteria = len(success_criteria)

        for criterion_name, check_func in success_criteria.items():
            met = check_func(results)
            status = "PASS" if met else "FAIL"
            print(f"   [{status}] {criterion_name}")

            if met:
                criteria_met += 1

        success_rate = (criteria_met / total_criteria) * 100
        print(f"   Success Rate: {criteria_met}/{total_criteria} ({success_rate:.0f}%)")
        print()

    # Final summary
    print_separator()
    print("\n6. FINAL SUMMARY")
    print_separator()
    print()

    # Identify best strategy
    best_sharpe = max(all_results.items(), key=lambda x: x[1]['test']['sharpe_ratio'])
    best_return = max(all_results.items(), key=lambda x: x[1]['test']['total_return'])
    best_gap = min(all_results.items(), key=lambda x: abs(x[1]['gap']))

    print(f"Best Test Sharpe:  {best_sharpe[0]} ({best_sharpe[1]['test']['sharpe_ratio']:.2f})")
    print(f"Best Test Return:  {best_return[0]} ({best_return[1]['test']['total_return']:.2%})")
    print(f"Best Train-Test Gap: {best_gap[0]} ({best_gap[1]['gap']:.1f}%)")
    print()

    # Overall assessment
    print("Overall Assessment:")
    portfolio_results = all_results.get('Portfolio', {})

    if portfolio_results:
        gap_ok = abs(portfolio_results['gap']) < 30
        sharpe_ok = portfolio_results['test']['sharpe_ratio'] > 0.5
        win_rate_ok = portfolio_results['test']['win_rate'] > 0.5

        if gap_ok and sharpe_ok and win_rate_ok:
            print("   STATUS: ALL SUCCESS CRITERIA MET")
        elif gap_ok and (sharpe_ok or win_rate_ok):
            print("   STATUS: PARTIAL SUCCESS - Overfitting reduced, performance needs improvement")
        else:
            print("   STATUS: NEEDS IMPROVEMENT - Further tuning required")
    else:
        print("   STATUS: INCOMPLETE - Portfolio strategy not tested")

    print()
    print_separator()
    print("Validation complete!")
    print_separator()


if __name__ == "__main__":
    main()
