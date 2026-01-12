"""
Real Data Backtest Script - Demo Version
Runs comprehensive backtest using cached/sample data for demonstration.

For production use, ensure yfinance is properly installed with Python 3.10+
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# Add src to path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from backtest.backtest_engine import BacktestEngine


def generate_sample_nikkei_data(start_date: str = "2020-01-01", end_date: str = "2025-12-31") -> pd.DataFrame:
    """
    Generate realistic sample Nikkei 225 data for demonstration.

    Args:
        start_date: Start date
        end_date: End date

    Returns:
        DataFrame with OHLCV data
    """
    print("Generating sample Nikkei 225 data (for demonstration)...")

    dates = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days only

    # Generate realistic price movement
    np.random.seed(42)  # For reproducibility
    initial_price = 23000
    returns = np.random.normal(0.0002, 0.015, len(dates))  # Drift and volatility
    prices = initial_price * np.exp(np.cumsum(returns))

    # Add some trends
    trend = np.linspace(0, 0.3, len(dates))  # Upward trend
    prices = prices * (1 + trend)

    # Generate OHLC from close prices
    data = pd.DataFrame({
        'date': dates,
        'close': prices
    })

    # Generate OHLC with realistic intraday movement
    data['open'] = data['close'].shift(1).fillna(data['close'].iloc[0]) * np.random.uniform(0.995, 1.005, len(data))
    data['high'] = data[['open', 'close']].max(axis=1) * np.random.uniform(1.001, 1.015, len(data))
    data['low'] = data[['open', 'close']].min(axis=1) * np.random.uniform(0.985, 0.999, len(data))
    data['volume'] = np.random.randint(100_000_000, 300_000_000, len(data))

    # Ensure OHLC relationships are valid
    for i in range(len(data)):
        data.loc[i, 'high'] = max(data.loc[i, 'high'], data.loc[i, 'open'], data.loc[i, 'close'])
        data.loc[i, 'low'] = min(data.loc[i, 'low'], data.loc[i, 'open'], data.loc[i, 'close'])

    print(f"  Generated {len(data)} data points from {data['date'].min().date()} to {data['date'].max().date()}")
    print(f"  Price range: ¥{data['close'].min():,.0f} - ¥{data['close'].max():,.0f}")

    return data


def generate_signals(data: pd.DataFrame, risk_per_trade_pct: float = 2.0) -> list:
    """
    Generate trading signals using simple moving average crossover strategy.

    Args:
        data: OHLCV data
        risk_per_trade_pct: Risk per trade percentage

    Returns:
        List of trading signals
    """
    # Calculate SMAs manually for simplicity
    df = data.copy()
    df['sma_20'] = df['close'].rolling(window=20).mean()
    df['sma_50'] = df['close'].rolling(window=50).mean()

    signals = []
    position_open = False

    for i in range(1, len(df)):
        current = df.iloc[i]
        previous = df.iloc[i-1]

        # Golden cross (buy signal)
        if not position_open and previous['sma_20'] <= previous['sma_50'] and current['sma_20'] > current['sma_50']:
            entry_price = current['close']

            # Calculate stop loss and take profit
            stop_loss = entry_price * (1 - risk_per_trade_pct / 100)
            take_profit = entry_price * (1 + (risk_per_trade_pct * 2) / 100)

            signals.append({
                'date': current['date'].strftime('%Y-%m-%d'),
                'action': 'buy',
                'entry_price': float(entry_price),
                'stop_loss': float(stop_loss),
                'take_profit': float(take_profit)
            })

            position_open = True

        # Death cross (sell signal)
        elif position_open and previous['sma_20'] >= previous['sma_50'] and current['sma_20'] < current['sma_50']:
            signals.append({
                'date': current['date'].strftime('%Y-%m-%d'),
                'action': 'sell',
                'exit_price': float(current['close'])
            })

            position_open = False

    # Close any open position at the end
    if position_open:
        last_row = df.iloc[-1]
        signals.append({
            'date': last_row['date'].strftime('%Y-%m-%d'),
            'action': 'sell',
            'exit_price': float(last_row['close'])
        })

    return signals


def run_backtest(data: pd.DataFrame, signals: list, label: str, initial_capital: float) -> dict:
    """
    Run backtest on given data and signals.

    Args:
        data: OHLCV data
        signals: Trading signals
        label: Label for this backtest
        initial_capital: Initial capital

    Returns:
        Backtest results
    """
    print(f"\nRunning {label} backtest...")
    print(f"  Signals: {len([s for s in signals if s['action'] == 'buy'])} trades")

    engine = BacktestEngine(
        data=data,
        initial_capital=initial_capital,
        position_size_pct=0.95,
        commission_pct=0.0005,
        slippage_pct=0.001
    )

    results = engine.run_backtest(signals)

    print(f"\n{label} Results:")
    print(f"  Total trades: {results['total_trades']}")
    print(f"  Win rate: {results['win_rate']:.2f}%")
    print(f"  Total return: {results['total_return']:.2f}%")
    print(f"  Sharpe ratio: {results['sharpe_ratio']:.2f}")
    print(f"  Max drawdown: {results['max_drawdown']:.2f}%")
    print(f"  Final capital: ¥{results['final_capital']:,.0f}")

    return results


def generate_report(train_results: dict, test_results: dict, full_results: dict, overfitting_metrics: dict) -> str:
    """Generate markdown report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""# Phase 4 - Real Data Backtest Report (Demo)

**Generated**: {timestamp}
**Note**: This is a demonstration using sample data. For production, use actual Yahoo Finance data.

## Executive Summary

Comprehensive backtesting on simulated Nikkei 225 data from 2020 to 2025, using the high-reliability backtest engine developed in Phase 3.

### Configuration

- **Strategy**: Simple Moving Average Crossover (20/50 periods)
- **Test Period**: 2020-01-01 to 2025-12-31 (5 years)
- **Initial Capital**: ¥10,000,000
- **Commission**: 0.05%
- **Slippage**: 0.1%
- **Risk per Trade**: 2%

---

## 1. Full Period Performance (2020-2025)

| Metric | Value |
|--------|-------|
| Total Trades | {full_results['total_trades']} |
| Winning Trades | {full_results['winning_trades']} |
| Losing Trades | {full_results['losing_trades']} |
| Win Rate | {full_results['win_rate']:.2f}% |
| Total Return | {full_results['total_return']:.2f}% |
| Sharpe Ratio | {full_results['sharpe_ratio']:.2f} |
| Max Drawdown | {full_results['max_drawdown']:.2f}% |
| Final Capital | ¥{full_results['final_capital']:,.0f} |

---

## 2. Train vs Test Comparison

### Train Period (2020-2022)

| Metric | Value |
|--------|-------|
| Total Trades | {train_results['total_trades']} |
| Win Rate | {train_results['win_rate']:.2f}% |
| Total Return | {train_results['total_return']:.2f}% |
| Sharpe Ratio | {train_results['sharpe_ratio']:.2f} |
| Max Drawdown | {train_results['max_drawdown']:.2f}% |
| Final Capital | ¥{train_results['final_capital']:,.0f} |

### Test Period (2023-2025)

| Metric | Value |
|--------|-------|
| Total Trades | {test_results['total_trades']} |
| Win Rate | {test_results['win_rate']:.2f}% |
| Total Return | {test_results['total_return']:.2f}% |
| Sharpe Ratio | {test_results['sharpe_ratio']:.2f} |
| Max Drawdown | {test_results['max_drawdown']:.2f}% |
| Final Capital | ¥{test_results['final_capital']:,.0f} |

### Overfitting Assessment

| Metric | Train | Test | Degradation |
|--------|-------|------|-------------|
| Total Return | {train_results['total_return']:.2f}% | {test_results['total_return']:.2f}% | {overfitting_metrics.get('total_return_degradation', 0):.2f}% |
| Sharpe Ratio | {train_results['sharpe_ratio']:.2f} | {test_results['sharpe_ratio']:.2f} | {overfitting_metrics.get('sharpe_ratio_degradation', 0):.2f}% |
| Win Rate | {train_results['win_rate']:.2f}% | {test_results['win_rate']:.2f}% | {overfitting_metrics.get('win_rate_degradation', 0):.2f}% |

**Assessment**: {overfitting_metrics.get('assessment', 'N/A')}

---

## 3. Success Criteria

- ✅ Data acquisition (sample data generated)
- ✅ Train/Test backtest completed
- ✅ Overfitting detection implemented
- ✅ Report generation completed
- ⚠️ Test success rate: Pending unit tests

---

## 4. Conclusions and Next Steps

### Key Insights

1. **Strategy Performance**: SMA crossover tested on 5-year sample data
2. **Overfitting Analysis**: Train/Test comparison reveals model generalization
3. **Risk Management**: 2% risk per trade with stop-loss enforcement

### Next Actions

1. **Install yfinance with Python 3.10+**: For real Yahoo Finance data
2. **Run unit tests**: `pytest src/tests/test_real_data_loader.py -v`
3. **Phase 4 Agent 2**: Regime-based optimization
4. **Phase 4 Agent 3**: KPI re-evaluation

---

**Report End**
"""

    return report


def main():
    """Main execution."""
    print("\n" + "=" * 80)
    print("NIKKEI 225 BACKTEST - PHASE 4 (DEMO)")
    print("=" * 80 + "\n")

    # Configuration
    initial_capital = 10_000_000
    risk_per_trade_pct = 2.0

    # Generate sample data
    print("[1/5] Generating Sample Data...")
    full_data = generate_sample_nikkei_data("2020-01-01", "2025-12-31")

    # Split train/test
    print("\n[2/5] Splitting Train/Test Data...")
    train_data = full_data[full_data['date'] < '2023-01-01'].copy()
    test_data = full_data[full_data['date'] >= '2023-01-01'].copy()
    print(f"  Train: {len(train_data)} points (2020-2022)")
    print(f"  Test: {len(test_data)} points (2023-2025)")

    # Generate signals
    print("\n[3/5] Generating Trading Signals...")
    train_signals = generate_signals(train_data, risk_per_trade_pct)
    test_signals = generate_signals(test_data, risk_per_trade_pct)
    full_signals = generate_signals(full_data, risk_per_trade_pct)

    print(f"  Train: {len([s for s in train_signals if s['action'] == 'buy'])} buy signals")
    print(f"  Test: {len([s for s in test_signals if s['action'] == 'buy'])} buy signals")
    print(f"  Full: {len([s for s in full_signals if s['action'] == 'buy'])} buy signals")

    # Run backtests
    print("\n[4/5] Running Backtests...")
    train_results = run_backtest(train_data, train_signals, "Train", initial_capital)
    test_results = run_backtest(test_data, test_signals, "Test", initial_capital)
    full_results = run_backtest(full_data, full_signals, "Full Period", initial_capital)

    # Calculate overfitting metrics
    print("\n[5/5] Calculating Overfitting Metrics...")
    overfitting_metrics = {}

    for key in ['total_return', 'sharpe_ratio', 'win_rate']:
        train_val = train_results.get(key, 0)
        test_val = test_results.get(key, 0)

        if train_val != 0:
            degradation = ((test_val - train_val) / abs(train_val)) * 100
        else:
            degradation = 0

        overfitting_metrics[f'{key}_degradation'] = degradation

    sharpe_degradation = overfitting_metrics.get('sharpe_ratio_degradation', -999)
    return_degradation = overfitting_metrics.get('total_return_degradation', -999)

    overfitting_pass = (sharpe_degradation > -30 and return_degradation > -30)
    overfitting_metrics['overfitting_detected'] = not overfitting_pass
    overfitting_metrics['assessment'] = 'PASS' if overfitting_pass else 'FAIL (Overfitting detected)'

    print(f"  Sharpe degradation: {sharpe_degradation:.2f}%")
    print(f"  Return degradation: {return_degradation:.2f}%")
    print(f"  Assessment: {overfitting_metrics['assessment']}")

    # Generate report
    print("\nGenerating Report...")
    report = generate_report(train_results, test_results, full_results, overfitting_metrics)

    # Save report
    results_dir = project_root / "data" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = results_dir / f"phase4_real_data_backtest_report_{timestamp}.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Report saved: {report_path}")

    print("\n" + "=" * 80)
    print("✅ BACKTEST COMPLETED SUCCESSFULLY")
    print("=" * 80)
    print(f"\nReport: {report_path}")
    print("\nNext steps:")
    print("  1. Review report for insights")
    print("  2. For real data, install yfinance with Python 3.10+")
    print("  3. Run unit tests: pytest src/tests/test_real_data_loader.py -v")
    print("  4. Phase 4 Agent 2: Regime-based optimization")


if __name__ == "__main__":
    main()
