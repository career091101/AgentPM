"""
Walk-Forward Analysis Runner
Performs walk-forward analysis with rolling train/test splits.

Usage:
    python scripts/run_walk_forward_analysis.py
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / 'src'))

from backtest.walk_forward_analyzer import WalkForwardAnalyzer
from utils.technical_indicators import TechnicalIndicators


def generate_sample_nikkei_data(start_date: str = "2020-01-01", end_date: str = "2025-12-31") -> pd.DataFrame:
    """Generate realistic sample Nikkei 225 data (Python 3.9 fallback)."""
    print("Generating sample Nikkei 225 data (for demonstration)...")
    dates = pd.date_range(start=start_date, end=end_date, freq='B')
    np.random.seed(42)
    initial_price = 23000
    returns = np.random.normal(0.0002, 0.015, len(dates))
    prices = initial_price * np.exp(np.cumsum(returns))
    trend = np.linspace(0, 0.3, len(dates))
    prices = prices * (1 + trend)

    data = pd.DataFrame({'date': dates, 'close': prices})
    data['open'] = data['close'].shift(1).fillna(data['close'].iloc[0]) * np.random.uniform(0.995, 1.005, len(data))
    data['high'] = data[['open', 'close']].max(axis=1) * np.random.uniform(1.001, 1.015, len(data))
    data['low'] = data[['open', 'close']].min(axis=1) * np.random.uniform(0.985, 0.999, len(data))
    data['volume'] = np.random.randint(100_000_000, 300_000_000, len(data))

    for i in range(len(data)):
        data.loc[i, 'high'] = max(data.loc[i, 'high'], data.loc[i, 'open'], data.loc[i, 'close'])
        data.loc[i, 'low'] = min(data.loc[i, 'low'], data.loc[i, 'open'], data.loc[i, 'close'])

    print(f"  Generated {len(data)} data points from {data['date'].min().date()} to {data['date'].max().date()}")
    return data


def simple_ma_strategy(data: pd.DataFrame, **params):
    """
    Simple MA crossover backtest function.

    Parameters:
    - ma_short: Short MA period
    - ma_long: Long MA period
    - position_size_pct: Position size as % of capital
    - stop_loss_pct: Stop loss percentage
    """
    ma_short = params.get('ma_short', 20)
    ma_long = params.get('ma_long', 50)
    position_size_pct = params.get('position_size_pct', 0.95)
    stop_loss_pct = params.get('stop_loss_pct', 0.02)

    # Calculate MAs
    df = data.copy()
    df['sma_short'] = df['close'].rolling(window=ma_short).mean()
    df['sma_long'] = df['close'].rolling(window=ma_long).mean()

    # Generate signals
    signals = []
    capital = 10_000_000
    position_open = False

    for i in range(1, len(df)):
        if pd.isna(df['sma_short'].iloc[i]) or pd.isna(df['sma_long'].iloc[i]):
            continue

        current = df.iloc[i]
        previous = df.iloc[i-1]

        # Buy signal: golden cross
        if not position_open and previous['sma_short'] <= previous['sma_long'] and current['sma_short'] > current['sma_long']:
            entry_price = current['close']
            position_size = capital * position_size_pct
            shares = int(position_size / entry_price)

            signals.append({
                'entry_date': current['date'] if 'date' in df.columns else df.index[i],
                'entry_price': entry_price,
                'shares': shares,
                'stop_loss': entry_price * (1 - stop_loss_pct),
                'take_profit': entry_price * 1.04,
                'exit_date': None,
                'exit_price': None,
                'pnl': None,
                'pnl_pct': None
            })
            position_open = True

        # Exit conditions
        elif position_open:
            signal = signals[-1]

            # Stop loss
            if current['low'] <= signal['stop_loss']:
                signal['exit_date'] = current['date'] if 'date' in df.columns else df.index[i]
                signal['exit_price'] = signal['stop_loss']
                signal['pnl'] = (signal['exit_price'] - signal['entry_price']) * signal['shares']
                signal['pnl_pct'] = (signal['exit_price'] / signal['entry_price'] - 1) * 100
                capital += signal['shares'] * signal['exit_price']
                position_open = False

            # Take profit
            elif current['high'] >= signal['take_profit']:
                signal['exit_date'] = current['date'] if 'date' in df.columns else df.index[i]
                signal['exit_price'] = signal['take_profit']
                signal['pnl'] = (signal['exit_price'] - signal['entry_price']) * signal['shares']
                signal['pnl_pct'] = (signal['exit_price'] / signal['entry_price'] - 1) * 100
                capital += signal['shares'] * signal['exit_price']
                position_open = False

            # Death cross exit
            elif previous['sma_short'] >= previous['sma_long'] and current['sma_short'] < current['sma_long']:
                signal['exit_date'] = current['date'] if 'date' in df.columns else df.index[i]
                signal['exit_price'] = current['close']
                signal['pnl'] = (signal['exit_price'] - signal['entry_price']) * signal['shares']
                signal['pnl_pct'] = (signal['exit_price'] / signal['entry_price'] - 1) * 100
                capital += signal['shares'] * signal['exit_price']
                position_open = False

    # Calculate KPIs
    closed_trades = [s for s in signals if s['exit_date'] is not None]

    if len(closed_trades) == 0:
        return {
            'sharpe_ratio': 0.0,
            'total_return': 0.0,
            'win_rate': 0.0,
            'max_drawdown': 0.0,
            'total_trades': 0
        }

    returns = [t['pnl_pct'] for t in closed_trades]
    wins = sum(1 for r in returns if r > 0)

    sharpe_ratio = np.mean(returns) / (np.std(returns) + 1e-10)
    total_return = sum(returns)
    win_rate = (wins / len(closed_trades)) * 100
    max_drawdown = abs(min(returns))

    return {
        'sharpe_ratio': sharpe_ratio,
        'total_return': total_return,
        'win_rate': win_rate,
        'max_drawdown': max_drawdown,
        'total_trades': len(closed_trades)
    }


def main():
    print("=" * 60)
    print("WALK-FORWARD ANALYSIS")
    print("=" * 60)

    # Load data
    print("\n[1/3] Loading historical data...")
    try:
        from data.real_data_loader import RealDataLoader
        loader = RealDataLoader(ticker="^N225", start_date='2020-01-01', end_date='2025-12-31')
        data = loader.fetch_data(use_cache=True)
    except (ImportError, TypeError) as e:
        print(f"⚠️  Real data fetch failed (Python 3.9 compatibility issue)")
        print("Using sample data for demonstration...")
        data = generate_sample_nikkei_data('2020-01-01', '2025-12-31')
        data.set_index('date', inplace=True)

    print(f"✅ Loaded {len(data)} days of data ({data.index.min().date()} to {data.index.max().date()})")

    # Set up walk-forward analyzer
    print("\n[2/3] Running walk-forward analysis...")

    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=12,  # 1 year
        test_months=3,    # 3 months
        step_months=1     # 1 month step
    )

    param_grid = {
        'ma_short': [10, 20, 30],
        'ma_long': [30, 50, 100],
        'position_size_pct': [0.7, 0.8, 0.9],
        'stop_loss_pct': [0.01, 0.02, 0.03]
    }

    results = analyzer.run_analysis(simple_ma_strategy, param_grid)

    print(f"\n✅ Walk-forward analysis completed!")
    print(f"   Windows analyzed: {results['num_windows']}")
    print(f"   Median test Sharpe: {results['statistics']['sharpe_ratio']['median']:.3f}")
    print(f"   Positive return rate: {results['positive_return_rate']:.1f}%")

    # Save results
    print("\n[3/3] Saving results...")

    # Save to CSV
    results_dir = project_root / 'data' / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)

    csv_path = results_dir / 'walk_forward_results.csv'

    windows_data = []
    for window in results['windows']:
        row = {
            'window_id': window['window_id'],
            'test_sharpe': window['test_metrics']['sharpe_ratio'],
            'test_return': window['test_metrics']['total_return'],
            'test_win_rate': window['test_metrics']['win_rate'],
            'test_max_drawdown': window['test_metrics']['max_drawdown'],
            'test_trades': window['test_metrics']['total_trades'],
            'degradation_pct': window['degradation_pct']
        }
        windows_data.append(row)

    pd.DataFrame(windows_data).to_csv(csv_path, index=False)
    print(f"✅ Results saved to: {csv_path}")

    print("\n" + "=" * 60)
    print("✅ WALK-FORWARD ANALYSIS COMPLETE")
    print("=" * 60)
    print("\nNext step: Run KPI statistics analysis")
    print("  python scripts/analyze_kpi_statistics.py")


if __name__ == "__main__":
    main()
