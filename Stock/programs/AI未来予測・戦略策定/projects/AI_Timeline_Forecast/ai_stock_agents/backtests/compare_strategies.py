"""
Strategy Comparison Script

等ウェイト戦略 vs 改良版マルチファクター戦略の比較
"""

from datetime import datetime
from pathlib import Path
import pandas as pd

import sys
sys.path.append(str(Path(__file__).parent))

from data_loader.data_preparer import prepare_backtest_data
from engine.backtest_engine import BacktestEngine, BacktestConfig
from strategies.ai_agent_strategy import create_ai_agent_strategy
from strategies.enhanced_strategy import create_enhanced_strategy


def run_backtest(strategy, strategy_name, data_manager, universe_manager, cost_model, regime_detector):
    """バックテスト実行"""
    print(f"\n{'='*80}")
    print(f"Running: {strategy_name}")
    print(f"{'='*80}\n")

    config = BacktestConfig(
        start_date=datetime(2020, 1, 1),
        end_date=datetime(2024, 12, 31),
        initial_capital=1000000,
        rebalance_frequency="weekly",
        rebalance_day="Monday",
        max_position_size=0.15,  # 改良版は15%まで許可
        max_category_size=0.30,
        min_trade_threshold=0.001,
        enable_trading_costs=True,
        benchmark_ticker="SPY",
        enable_regime_detection=False,
    )

    engine = BacktestEngine(
        config=config,
        data_manager=data_manager,
        universe_manager=universe_manager,
        cost_model=cost_model,
        regime_detector=regime_detector,
    )

    result = engine.run(strategy)

    return result


def main():
    print("="*80)
    print("STRATEGY COMPARISON: Equal-Weight vs Enhanced Multi-Factor")
    print("="*80)
    print()

    # データ準備
    cache_dir = Path(__file__).parent / "cache"
    master_data = Path(__file__).parent / "data" / "ai_stocks_master.json"

    print("📊 Preparing data...")
    data_manager, universe_manager, cost_model, regime_detector = prepare_backtest_data(
        start_date=datetime(2020, 1, 1),
        end_date=datetime(2024, 12, 31),
        master_data_path=master_data,
        cache_dir=cache_dir,
    )

    # 1. 等ウェイト戦略
    equal_weight_strategy = create_ai_agent_strategy(enable_agents=False)
    result_equal = run_backtest(
        equal_weight_strategy,
        "Equal-Weight Strategy",
        data_manager, universe_manager, cost_model, regime_detector
    )

    # 2. 改良版マルチファクター戦略
    enhanced_strategy = create_enhanced_strategy(
        data_manager=data_manager,
        lookback_weeks=12,
    )
    result_enhanced = run_backtest(
        enhanced_strategy,
        "Enhanced Multi-Factor Strategy",
        data_manager, universe_manager, cost_model, regime_detector
    )

    # 比較表示
    print("\n" + "="*80)
    print("COMPARISON SUMMARY")
    print("="*80)
    print()

    comparison_data = {
        "Metric": [
            "Total Return",
            "Annualized Return",
            "Sharpe Ratio",
            "Sortino Ratio",
            "Calmar Ratio",
            "Max Drawdown",
            "Volatility (Ann.)",
            "Win Rate",
            "Final Value",
            "Total Trading Cost",
        ],
        "Equal-Weight": [
            f"{result_equal.metrics.total_return:.2%}",
            f"{result_equal.metrics.annualized_return:.2%}",
            f"{result_equal.metrics.sharpe_ratio:.2f}",
            f"{result_equal.metrics.sortino_ratio:.2f}",
            f"{result_equal.metrics.calmar_ratio:.2f}",
            f"{result_equal.metrics.max_drawdown:.2%}",
            f"{result_equal.metrics.annualized_volatility:.2%}",
            f"{result_equal.metrics.win_rate:.2%}",
            f"${result_equal.summary['final_value']:,.0f}",
            f"${result_equal.metrics.total_trading_cost:,.2f}",
        ],
        "Enhanced Multi-Factor": [
            f"{result_enhanced.metrics.total_return:.2%}",
            f"{result_enhanced.metrics.annualized_return:.2%}",
            f"{result_enhanced.metrics.sharpe_ratio:.2f}",
            f"{result_enhanced.metrics.sortino_ratio:.2f}",
            f"{result_enhanced.metrics.calmar_ratio:.2f}",
            f"{result_enhanced.metrics.max_drawdown:.2%}",
            f"{result_enhanced.metrics.annualized_volatility:.2%}",
            f"{result_enhanced.metrics.win_rate:.2%}",
            f"${result_enhanced.summary['final_value']:,.0f}",
            f"${result_enhanced.metrics.total_trading_cost:,.2f}",
        ],
    }

    df = pd.DataFrame(comparison_data)
    print(df.to_string(index=False))
    print()

    # 改善度計算
    print("="*80)
    print("IMPROVEMENT ANALYSIS")
    print("="*80)
    print()

    improvements = {
        "Return": (result_enhanced.metrics.total_return - result_equal.metrics.total_return) / result_equal.metrics.total_return * 100,
        "Sharpe": (result_enhanced.metrics.sharpe_ratio - result_equal.metrics.sharpe_ratio) / result_equal.metrics.sharpe_ratio * 100,
        "Max DD": (result_enhanced.metrics.max_drawdown - result_equal.metrics.max_drawdown) / abs(result_equal.metrics.max_drawdown) * 100,
    }

    for metric, improvement in improvements.items():
        sign = "📈" if improvement > 0 else "📉" if improvement < 0 else "➡️ "
        print(f"  {metric:12s}: {sign} {improvement:+.1f}%")

    print()

    # 結果保存
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)

    # CSV保存
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_equal.weekly_returns['strategy'] = 'equal_weight'
    result_enhanced.weekly_returns['strategy'] = 'enhanced'

    combined_returns = pd.concat([
        result_equal.weekly_returns,
        result_enhanced.weekly_returns
    ], ignore_index=True)

    csv_file = output_dir / f"strategy_comparison_{timestamp}.csv"
    combined_returns.to_csv(csv_file, index=False)

    print(f"✅ Results saved to: {csv_file}")
    print()


if __name__ == "__main__":
    main()
