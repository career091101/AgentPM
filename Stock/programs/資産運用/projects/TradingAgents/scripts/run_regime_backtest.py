"""
Regime-Specific Backtest Runner
Compares fixed vs regime-specific vs adaptive strategies.

Usage:
    python scripts/run_regime_backtest.py
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / 'src'))

from utils.market_regime import MarketRegimeDetector, RegimeType
from utils.technical_indicators import TechnicalIndicators
from strategy.regime_specific_optimizer import RegimeSpecificOptimizer, DEFAULT_PARAM_GRIDS
from strategy.adaptive_strategy import AdaptiveStrategy
from backtest.backtest_engine import BacktestEngine
from data.real_data_loader import RealDataLoader


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


def create_simple_backtest_function(data: pd.DataFrame):
    """
    Create a simplified backtest function for parameter optimization.

    Args:
        data: Historical OHLCV data

    Returns:
        Backtest function that accepts parameters
    """
    def backtest_with_params(**params):
        """
        Simple MA crossover backtest with configurable parameters.

        Parameters can include:
        - ma_short, ma_long: MA periods
        - rsi_period, rsi_oversold, rsi_overbought: RSI settings
        - bb_period, bb_std: Bollinger Band settings
        - position_size_pct: Position sizing
        - stop_loss_pct: Stop loss percentage
        """
        ma_short = params.get('ma_short', 20)
        ma_long = params.get('ma_long', 50)
        position_size_pct = params.get('position_size_pct', 0.95)
        stop_loss_pct = params.get('stop_loss_pct', 0.02)

        # Calculate indicators
        indicators = TechnicalIndicators(data)
        ma_result = indicators.calculate_sma(periods=[ma_short, ma_long])

        close = data['close']
        sma_short_series = close.rolling(window=ma_short).mean()
        sma_long_series = close.rolling(window=ma_long).mean()

        # Generate signals
        signals = []
        position = None

        for i in range(max(ma_short, ma_long), len(data)):
            date = data.index[i]
            price = close.iloc[i]

            if position is None:
                # Look for buy signal
                if sma_short_series.iloc[i] > sma_long_series.iloc[i] and sma_short_series.iloc[i-1] <= sma_long_series.iloc[i-1]:
                    # Buy signal
                    stop_loss_price = price * (1 - stop_loss_pct)
                    take_profit_price = price * (1 + stop_loss_pct * 2)  # 2:1 R:R

                    signals.append({
                        'date': date,
                        'action': 'buy',
                        'entry_price': price,
                        'stop_loss': stop_loss_price,
                        'take_profit': take_profit_price
                    })
                    position = 'long'

            else:
                # Look for sell signal
                if sma_short_series.iloc[i] < sma_long_series.iloc[i]:
                    signals.append({
                        'date': date,
                        'action': 'sell',
                        'entry_price': price
                    })
                    position = None

        # Run backtest
        if not signals:
            return {
                'sharpe_ratio': 0,
                'total_return': 0,
                'win_rate': 0,
                'max_drawdown': 0
            }

        engine = BacktestEngine(
            data=data,
            initial_capital=1000000,
            position_size_pct=position_size_pct
        )

        results = engine.run_backtest(signals)
        return results

    return backtest_with_params


def run_fixed_strategy_backtest(data: pd.DataFrame, params: dict) -> dict:
    """Run backtest with fixed parameters across all periods."""
    print("\n" + "=" * 60)
    print("1. FIXED STRATEGY BACKTEST")
    print("=" * 60)
    print(f"Parameters: {params}")

    backtest_fn = create_simple_backtest_function(data)
    results = backtest_fn(**params)

    print(f"\n✅ Fixed Strategy Results:")
    print(f"   Sharpe Ratio: {results.get('sharpe_ratio', 0):.3f}")
    print(f"   Total Return: {results.get('total_return', 0):.2f}%")
    print(f"   Win Rate: {results.get('win_rate', 0):.2f}%")
    print(f"   Max Drawdown: {results.get('max_drawdown', 0):.2f}%")

    return results


def run_regime_optimization(data: pd.DataFrame) -> dict:
    """Optimize parameters for each regime separately."""
    print("\n" + "=" * 60)
    print("2. REGIME-SPECIFIC OPTIMIZATION")
    print("=" * 60)

    # Create detector and optimizer
    detector = MarketRegimeDetector(data)
    backtest_fn = create_simple_backtest_function(data)

    optimizer = RegimeSpecificOptimizer(
        data=data,
        regime_detector=detector,
        backtest_function=backtest_fn
    )

    # Optimize for each regime
    print("\nOptimizing parameters for each regime...")
    results = optimizer.optimize_all_regimes(
        param_grids=DEFAULT_PARAM_GRIDS,
        metric='sharpe_ratio'
    )

    print("\n✅ Regime-Specific Optimization Complete:")
    regime_params = {}
    for regime, result in results.items():
        if 'error' not in result:
            print(f"\n{regime.upper()}:")
            print(f"   Best Sharpe: {result['best_score']:.3f}")
            print(f"   Parameters: {result['best_params']}")
            regime_params[regime] = result['best_params']

    return {
        'optimization_results': results,
        'regime_params': regime_params
    }


def run_adaptive_strategy_backtest(
    data: pd.DataFrame,
    regime_params: dict
) -> dict:
    """Run backtest with adaptive regime-switching strategy."""
    print("\n" + "=" * 60)
    print("3. ADAPTIVE STRATEGY BACKTEST")
    print("=" * 60)

    # Create detector and adaptive strategy
    detector = MarketRegimeDetector(data)
    strategy = AdaptiveStrategy(
        regime_detector=detector,
        regime_params=regime_params,
        stability_days=5
    )

    # Generate signals for entire period
    print("\nGenerating adaptive signals...")
    signals = []
    position = None

    for date in data.index[200:]:  # Start after warmup period
        signal = strategy.generate_signal(data, date)

        if signal['regime_switched']:
            print(f"   🔄 Regime switched to {signal['regime']} on {date.date()}")

        # Convert to backtest signals
        if position is None and signal['action'] == 'buy':
            params = signal['parameters']
            stop_loss_pct = params.get('stop_loss_pct', 0.02)

            signals.append({
                'date': date,
                'action': 'buy',
                'entry_price': signal['price'],
                'stop_loss': signal['price'] * (1 - stop_loss_pct),
                'take_profit': signal['price'] * (1 + stop_loss_pct * 2)
            })
            position = 'long'

        elif position == 'long' and signal['action'] == 'sell':
            signals.append({
                'date': date,
                'action': 'sell',
                'entry_price': signal['price']
            })
            position = None

    print(f"\n✅ Generated {len(signals)} signals")

    # Run backtest
    if not signals:
        print("⚠️  No signals generated")
        return {
            'sharpe_ratio': 0,
            'total_return': 0,
            'win_rate': 0,
            'max_drawdown': 0
        }

    engine = BacktestEngine(
        data=data,
        initial_capital=1000000,
        position_size_pct=0.95
    )

    results = engine.run_backtest(signals)

    print(f"\n✅ Adaptive Strategy Results:")
    print(f"   Sharpe Ratio: {results.get('sharpe_ratio', 0):.3f}")
    print(f"   Total Return: {results.get('total_return', 0):.2f}%")
    print(f"   Win Rate: {results.get('win_rate', 0):.2f}%")
    print(f"   Max Drawdown: {results.get('max_drawdown', 0):.2f}%")

    # Add regime statistics
    regime_stats = strategy.get_regime_statistics()
    results['regime_statistics'] = regime_stats

    print(f"\n   Regime Switches: {regime_stats.get('regime_switches', 0)}")
    print(f"   Regime Distribution: {regime_stats.get('regime_distribution', {})}")

    return results


def compare_strategies(
    fixed_results: dict,
    adaptive_results: dict
) -> dict:
    """Compare fixed vs adaptive strategy performance."""
    print("\n" + "=" * 60)
    print("4. STRATEGY COMPARISON")
    print("=" * 60)

    metrics = ['sharpe_ratio', 'total_return', 'win_rate', 'max_drawdown']
    comparison = {}

    for metric in metrics:
        fixed_value = fixed_results.get(metric, 0)
        adaptive_value = adaptive_results.get(metric, 0)

        if fixed_value != 0:
            improvement_pct = ((adaptive_value - fixed_value) / abs(fixed_value)) * 100
        else:
            improvement_pct = 0

        comparison[metric] = {
            'fixed': fixed_value,
            'adaptive': adaptive_value,
            'improvement_pct': improvement_pct
        }

        print(f"\n{metric.replace('_', ' ').title()}:")
        print(f"   Fixed: {fixed_value:.3f}")
        print(f"   Adaptive: {adaptive_value:.3f}")
        print(f"   Improvement: {improvement_pct:+.2f}%")

    return comparison


def save_results_to_report(
    fixed_results: dict,
    optimization_results: dict,
    adaptive_results: dict,
    comparison: dict,
    data: pd.DataFrame
):
    """Save all results to markdown report."""
    report_path = project_root / 'data' / 'results' / 'phase4_regime_optimization_report.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Phase 4 - レジーム別戦略最適化レポート\n\n")
        f.write(f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Executive Summary
        f.write("## エグゼクティブサマリー\n\n")
        f.write(f"- データ期間: {data.index.min().date()} ~ {data.index.max().date()}\n")
        f.write(f"- データポイント: {len(data)} 日\n")
        f.write(f"- 戦略比較: 固定パラメータ vs レジーム適応\n\n")

        # Regime-specific parameters
        f.write("## レジーム別最適パラメータ\n\n")
        regime_params = optimization_results.get('regime_params', {})
        for regime, params in regime_params.items():
            f.write(f"### {regime.upper()} Market\n\n")
            f.write("| パラメータ | 値 |\n")
            f.write("|-----------|----|\n")
            for key, value in params.items():
                f.write(f"| {key} | {value} |\n")
            f.write("\n")

        # Fixed strategy results
        f.write("## 固定戦略パフォーマンス\n\n")
        f.write("| メトリクス | 値 |\n")
        f.write("|-----------|----|\n")
        for key, value in fixed_results.items():
            if isinstance(value, (int, float)):
                f.write(f"| {key} | {value:.3f} |\n")
        f.write("\n")

        # Adaptive strategy results
        f.write("## 適応戦略パフォーマンス\n\n")
        f.write("| メトリクス | 値 |\n")
        f.write("|-----------|----|\n")
        for key, value in adaptive_results.items():
            if isinstance(value, (int, float)):
                f.write(f"| {key} | {value:.3f} |\n")
        f.write("\n")

        # Comparison
        f.write("## 戦略比較\n\n")
        f.write("| メトリクス | 固定 | 適応 | 改善率 |\n")
        f.write("|-----------|------|------|--------|\n")
        for metric, values in comparison.items():
            f.write(f"| {metric} | {values['fixed']:.3f} | {values['adaptive']:.3f} | {values['improvement_pct']:+.2f}% |\n")
        f.write("\n")

        # Regime statistics
        regime_stats = adaptive_results.get('regime_statistics', {})
        if regime_stats:
            f.write("## レジーム統計\n\n")
            f.write(f"- 総日数: {regime_stats.get('total_days', 0)} 日\n")
            f.write(f"- レジーム切り替え回数: {regime_stats.get('regime_switches', 0)} 回\n")
            f.write(f"- レジーム分布: {regime_stats.get('regime_distribution', {})}\n\n")

        # Conclusion
        f.write("## 結論\n\n")
        sharpe_improvement = comparison.get('sharpe_ratio', {}).get('improvement_pct', 0)

        if sharpe_improvement > 20:
            f.write(f"✅ **成功**: 適応戦略はSharpe Ratioを{sharpe_improvement:+.2f}%改善し、目標の+20%を達成しました。\n\n")
        else:
            f.write(f"⚠️  **要改善**: 適応戦略のSharpe Ratio改善は{sharpe_improvement:+.2f}%で、目標の+20%に未達です。\n\n")

        f.write("## 次のアクション\n\n")
        f.write("1. Phase 4 Agent 1（実データバックテスト）との統合\n")
        f.write("2. Phase 4 Agent 3（KPI再評価）との統合\n")
        f.write("3. Phase 4最終検証の実施\n")

    print(f"\n✅ Report saved to: {report_path}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("PHASE 4 - REGIME-SPECIFIC OPTIMIZATION")
    print("=" * 60)

    # Load data
    print("\nLoading historical data...")

    # Try to fetch real data, fallback to sample data if yfinance fails (Python 3.9)
    try:
        loader = RealDataLoader(ticker="^N225", start_date='2020-01-01', end_date='2025-12-31')
        data = loader.fetch_data(use_cache=True)
    except (ImportError, TypeError) as e:
        print(f"⚠️  Real data fetch failed (Python 3.9 compatibility issue)")
        print("Using sample data for demonstration...")
        data = generate_sample_nikkei_data('2020-01-01', '2025-12-31')
        # Set index to date for consistency with RealDataLoader
        data.set_index('date', inplace=True)

    if data is None or len(data) == 0:
        print("❌ Failed to load data")
        return

    print(f"✅ Loaded {len(data)} days of data ({data.index.min().date()} to {data.index.max().date()})")

    # 1. Fixed strategy baseline
    fixed_params = {
        'ma_short': 20,
        'ma_long': 50,
        'position_size_pct': 0.95,
        'stop_loss_pct': 0.02
    }
    fixed_results = run_fixed_strategy_backtest(data, fixed_params)

    # 2. Regime-specific optimization
    optimization_output = run_regime_optimization(data)
    regime_params = optimization_output['regime_params']

    # 3. Adaptive strategy backtest
    adaptive_results = run_adaptive_strategy_backtest(data, regime_params)

    # 4. Compare strategies
    comparison = compare_strategies(fixed_results, adaptive_results)

    # 5. Save report
    save_results_to_report(
        fixed_results=fixed_results,
        optimization_results=optimization_output,
        adaptive_results=adaptive_results,
        comparison=comparison,
        data=data
    )

    print("\n" + "=" * 60)
    print("✅ PHASE 4 - REGIME OPTIMIZATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
