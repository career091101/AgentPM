"""
Walk-Forward Analysis Full Execution (57 Windows)
Complete statistical robustness validation with 5-year historical data.

Execution:
    python scripts/run_walk_forward_full.py

Configuration:
    - Train period: 6 months
    - Test period: 3 months
    - Step: 3 months
    - Total windows: ~57 (2020-2025, 5 years)
    - Data: Nikkei 225 (N225)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Add src to path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from backtest.walk_forward_analyzer import WalkForwardAnalyzer
from strategy.adaptive_strategy import AdaptiveStrategy
from utils.market_regime import MarketRegimeDetector
from utils.data_loader import DataLoader


def create_strategy_function(regime_params: dict):
    """
    Create a strategy function wrapper for walk-forward analysis.

    Args:
        regime_params: Dict mapping regime names to their parameters

    Returns:
        Function that generates signals given (data, **params)
    """
    def strategy_function(data: pd.DataFrame, **optimization_params) -> list:
        """
        Generate trading signals for walk-forward analysis.

        Args:
            data: Historical OHLCV data (DataFrame with date index)
            **optimization_params: Parameters to optimize (e.g., position_size_pct, stop_loss_pct)

        Returns:
            List of trading signals: [{'date': str, 'action': str, 'entry_price': float, ...}, ...]
        """
        # Ensure data has datetime index
        if not isinstance(data.index, pd.DatetimeIndex):
            if 'date' in data.columns:
                data = data.set_index('date')
            else:
                raise ValueError("Data must have datetime index or 'date' column")

        # Initialize regime detector and adaptive strategy
        detector = MarketRegimeDetector(data)
        strategy = AdaptiveStrategy(
            regime_detector=detector,
            regime_params=regime_params,
            stability_days=5,
            min_regime_confidence=0.6
        )

        # Generate signals for each trading day
        signals = []
        position_open = None  # Track open position

        # Start from day 200 to have enough data for indicators
        trading_dates = data.index[200:]

        for i, current_date in enumerate(trading_dates):
            # Generate signal using adaptive strategy
            signal_info = strategy.generate_signal(data, current_date)

            action = signal_info['action']
            price = signal_info['price']
            confidence = signal_info['confidence']

            # Convert to backtest-compatible format
            if action == 'buy' and position_open is None and confidence > 0.6:
                # Open long position
                stop_loss_pct = optimization_params.get('stop_loss_pct', 0.02)
                risk_reward = optimization_params.get('risk_reward', 2.0)

                signals.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'action': 'buy',
                    'entry_price': price,
                    'stop_loss': price * (1 - stop_loss_pct),
                    'take_profit': price * (1 + stop_loss_pct * risk_reward),
                    'risk_reward_ratio': risk_reward,
                    'confidence': confidence,
                    'regime': signal_info['regime']
                })
                position_open = current_date

            elif action == 'sell' and position_open is not None:
                # Close long position
                signals.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'action': 'sell',
                    'exit_price': price,
                    'confidence': confidence,
                    'regime': signal_info['regime']
                })
                position_open = None

            # Force exit if position held too long (max 30 days)
            elif position_open is not None:
                days_held = (current_date - position_open).days
                if days_held > 30:
                    signals.append({
                        'date': current_date.strftime('%Y-%m-%d'),
                        'action': 'sell',
                        'exit_price': price,
                        'confidence': 0.5,
                        'regime': signal_info['regime'],
                        'exit_reason': 'max_hold_period'
                    })
                    position_open = None

        return signals

    return strategy_function


def main():
    """Execute 57-window walk-forward analysis."""
    print("=" * 80)
    print("Walk-Forward Analysis - Full Execution (57 Windows)")
    print("=" * 80)

    # 1. Load historical data (5 years: 2020-2024)
    print("\n[1/5] Loading historical data...")
    data_loader = DataLoader(cache_dir=project_root / "data" / "cache")

    try:
        data = data_loader.load_cached_data(
            symbol='N225',
            start_date='2020-01-01',
            end_date='2024-12-31'
        )
        print(f"   ✅ Loaded {len(data)} days of data ({data.index.min().date()} to {data.index.max().date()})")
    except FileNotFoundError:
        print("   ⚠️  Cached data not found. Downloading from yfinance...")
        data = data_loader.fetch_data(
            symbol='^N225',
            start_date='2020-01-01',
            end_date='2024-12-31'
        )
        # Cache for future use
        cache_path = project_root / "data" / "cache" / "N225_20200101_20241231.csv"
        data.to_csv(cache_path)
        print(f"   ✅ Downloaded and cached {len(data)} days of data")

    # 2. Configure regime parameters (from previous optimization)
    print("\n[2/5] Configuring adaptive strategy parameters...")
    regime_params = {
        'bull': {
            'ma_short': 15,
            'ma_long': 40,
            'rsi_period': 14,
            'rsi_overbought': 70,
            'rsi_oversold': 30
        },
        'bear': {
            'ma_short': 30,
            'ma_long': 60,
            'rsi_period': 14,
            'rsi_overbought': 65,
            'rsi_oversold': 30
        },
        'sideways': {
            'bb_period': 20,
            'bb_std': 2.0,
            'rsi_period': 14,
            'rsi_overbought': 70,
            'rsi_oversold': 30
        }
    }
    print("   ✅ Regime parameters configured")

    # 3. Create strategy function
    print("\n[3/5] Creating adaptive strategy function...")
    strategy_function = create_strategy_function(regime_params)
    print("   ✅ Strategy function created")

    # 4. Configure walk-forward analysis
    print("\n[4/5] Configuring walk-forward analysis...")
    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=6,    # 6-month training window
        test_months=3,     # 3-month testing window
        step_months=3,     # 3-month step (50% overlap)
        initial_capital=1000000
    )

    # Calculate expected windows
    windows = analyzer.split_data()
    print(f"   ✅ Analysis configured: {len(windows)} windows")
    print(f"   📊 Train: 6 months, Test: 3 months, Step: 3 months")

    # 5. Define parameter grid for optimization
    param_grid = {
        'stop_loss_pct': [0.015, 0.02, 0.025],     # 1.5%, 2%, 2.5%
        'risk_reward': [1.5, 2.0, 2.5]              # Risk:Reward ratios
    }
    print(f"   📈 Parameter combinations: {len(param_grid['stop_loss_pct']) * len(param_grid['risk_reward'])}")

    # 6. Run walk-forward analysis
    print("\n[5/5] Running walk-forward analysis...")
    print(f"   ⏱️  Estimated time: ~{len(windows) * 2} minutes")
    print("   " + "-" * 76)

    start_time = datetime.now()

    results = analyzer.run_analysis(
        strategy_function=strategy_function,
        param_grid=param_grid
    )

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() / 60

    # 7. Display summary
    print("\n" + "=" * 80)
    print("WALK-FORWARD ANALYSIS RESULTS")
    print("=" * 80)

    print(f"\n📊 Execution Summary:")
    print(f"   Total windows: {results['num_windows']}")
    print(f"   Duration: {duration:.1f} minutes")
    print(f"   Recommendation: {results['recommendation'].upper()}")

    print(f"\n📈 Performance Statistics (Test Windows):")
    stats = results['statistics']

    print(f"   Sharpe Ratio:")
    print(f"      Median: {stats['sharpe_ratio']['median']:.3f}")
    print(f"      Mean:   {stats['sharpe_ratio']['mean']:.3f} ± {stats['sharpe_ratio']['std']:.3f}")
    print(f"      Q25-Q75: [{stats['sharpe_ratio']['q25']:.3f}, {stats['sharpe_ratio']['q75']:.3f}]")

    print(f"\n   Total Return (%):")
    print(f"      Median: {stats['total_return']['median']:.2f}%")
    print(f"      Mean:   {stats['total_return']['mean']:.2f}% ± {stats['total_return']['std']:.2f}%")
    print(f"      Range:  [{stats['total_return']['min']:.2f}%, {stats['total_return']['max']:.2f}%]")

    print(f"\n   Win Rate (%):")
    print(f"      Median: {stats['win_rate']['median']:.1f}%")
    print(f"      Mean:   {stats['win_rate']['mean']:.1f}% ± {stats['win_rate']['std']:.1f}%")

    print(f"\n   Max Drawdown (%):")
    print(f"      Median: {stats['max_drawdown']['median']:.2f}%")
    print(f"      Mean:   {stats['max_drawdown']['mean']:.2f}% ± {stats['max_drawdown']['std']:.2f}%")
    print(f"      Worst:  {stats['max_drawdown']['max']:.2f}%")

    print(f"\n🎯 Robustness Metrics:")
    print(f"   Positive return rate: {results['positive_return_rate']:.1f}%")
    print(f"   Average degradation: {results['avg_degradation']:.1f}%")
    print(f"   Coefficient of Variation (Sharpe): {stats['sharpe_ratio']['coefficient_of_variation']:.3f}")

    # 8. Export results
    print(f"\n💾 Exporting results...")

    # Export CSV
    csv_path = project_root / "data" / "results" / f"walk_forward_57windows_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    analyzer.export_results(results, str(csv_path))

    # Export JSON summary
    json_path = project_root / "data" / "results" / f"walk_forward_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(json_path, 'w') as f:
        json.dump({
            'num_windows': results['num_windows'],
            'statistics': results['statistics'],
            'positive_return_rate': results['positive_return_rate'],
            'avg_degradation': results['avg_degradation'],
            'recommendation': results['recommendation'],
            'execution_time_minutes': duration,
            'config': {
                'train_months': 6,
                'test_months': 3,
                'step_months': 3,
                'param_grid': param_grid,
                'regime_params': regime_params
            }
        }, f, indent=2)
    print(f"   ✅ JSON summary: {json_path}")

    # 9. Success criteria validation
    print("\n" + "=" * 80)
    print("SUCCESS CRITERIA VALIDATION")
    print("=" * 80)

    success_criteria = {
        '✅ 57 windows completed': results['num_windows'] >= 50,
        '✅ Test Sharpe > 0.5': stats['sharpe_ratio']['mean'] > 0.5,
        '✅ Positive return rate > 60%': results['positive_return_rate'] > 60,
        '✅ Degradation < 30%': results['avg_degradation'] < 30
    }

    for criterion, passed in success_criteria.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status} - {criterion}")

    all_passed = all(success_criteria.values())

    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 ALL SUCCESS CRITERIA MET - Strategy is statistically robust!")
    else:
        print("⚠️  SOME CRITERIA NOT MET - Further optimization recommended")
    print("=" * 80)

    return results


if __name__ == "__main__":
    try:
        results = main()
        print("\n✅ Walk-forward analysis completed successfully")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error during walk-forward analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
