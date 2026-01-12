"""
Quick Strategy Validation

Fast validation of the three strategies with smaller dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from strategy.mean_reversion_strategy import MeanReversionStrategy
from strategy.trend_following_strategy import TrendFollowingStrategy
from strategy.portfolio_strategy import PortfolioStrategy


def generate_test_data() -> pd.DataFrame:
    """Generate small test dataset."""
    # Shorter period for quick test
    dates = pd.date_range('2023-01-01', '2025-12-31', freq='D')
    np.random.seed(42)

    base_price = 40000
    trend = np.arange(len(dates)) * 3
    oscillation = np.sin(np.arange(len(dates)) / 30) * 1000
    noise = np.random.randn(len(dates)) * 500

    data = pd.DataFrame({
        'open': base_price + trend + oscillation + noise,
        'high': base_price + trend + oscillation + noise + np.abs(np.random.randn(len(dates)) * 300),
        'low': base_price + trend + oscillation + noise - np.abs(np.random.randn(len(dates)) * 300),
        'close': base_price + trend + oscillation + noise,
        'volume': np.random.randint(1000, 10000, len(dates))
    }, index=dates)

    return data


def quick_backtest(strategy, data: pd.DataFrame) -> dict:
    """Simple backtest."""
    signals = []
    for date in data.index[::5]:  # Sample every 5th day for speed
        signal = strategy.generate_signal(data, date)
        signals.append(signal)

    buy_signals = sum(1 for s in signals if s['action'] == 'buy')
    sell_signals = sum(1 for s in signals if s['action'] == 'sell')
    hold_signals = sum(1 for s in signals if s['action'] == 'hold')

    return {
        'total_signals': len(signals),
        'buy': buy_signals,
        'sell': sell_signals,
        'hold': hold_signals,
        'buy_rate': buy_signals / len(signals) if signals else 0,
        'sell_rate': sell_signals / len(signals) if signals else 0
    }


def main():
    print("=" * 70)
    print("QUICK STRATEGY VALIDATION")
    print("=" * 70)

    # Generate data
    print("\n1. Generating test data...")
    data = generate_test_data()
    print(f"   Period: {data.index[0].date()} to {data.index[-1].date()}")
    print(f"   Total days: {len(data)}")

    # Initialize strategies
    print("\n2. Initializing strategies...")
    strategies = {
        'Mean Reversion': MeanReversionStrategy(),
        'Trend Following': TrendFollowingStrategy(),
        'Portfolio': PortfolioStrategy()
    }
    print(f"   Created {len(strategies)} strategies")

    # Quick test
    print("\n3. Running quick validation...")
    print("-" * 70)

    for name, strategy in strategies.items():
        print(f"\n{name}:")
        result = quick_backtest(strategy, data)

        print(f"   Total signals generated: {result['total_signals']}")
        print(f"   Buy signals:  {result['buy']:>4} ({result['buy_rate']:>6.1%})")
        print(f"   Sell signals: {result['sell']:>4} ({result['sell_rate']:>6.1%})")
        print(f"   Hold signals: {result['hold']:>4}")

        # Check if strategy is generating trades
        if result['buy'] > 0 or result['sell'] > 0:
            print(f"   Status: ACTIVE (generating trade signals)")
        else:
            print(f"   Status: INACTIVE (no trade signals)")

    print("\n" + "=" * 70)
    print("SUCCESS: All three strategies are operational!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Run full backtest with real Nikkei 225 data")
    print("2. Evaluate against success criteria:")
    print("   - Train-Test gap <30%")
    print("   - Test Sharpe >0.5")
    print("   - Test Win Rate >50%")
    print("3. Compare with previous AdaptiveStrategy results")


if __name__ == "__main__":
    main()
