"""
Full Backtest Execution Script

Run complete 2020-2024 backtest with comprehensive analysis
"""

from datetime import datetime
from pathlib import Path
import argparse

import sys
sys.path.append(str(Path(__file__).parent))

from data_loader.data_preparer import prepare_backtest_data
from engine.backtest_engine import BacktestEngine, BacktestConfig
from strategies.ai_agent_strategy import create_ai_agent_strategy


def main():
    parser = argparse.ArgumentParser(description="Run full AI stock backtest")
    parser.add_argument("--start", type=str, default="2020-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2024-12-31", help="End date (YYYY-MM-DD)")
    parser.add_argument("--capital", type=float, default=1000000, help="Initial capital")
    parser.add_argument("--no-cache", action="store_true", help="Disable yfinance cache")
    args = parser.parse_args()

    # Parse dates
    start_date = datetime.strptime(args.start, "%Y-%m-%d")
    end_date = datetime.strptime(args.end, "%Y-%m-%d")

    print("=" * 80)
    print("AI STOCK AGENTS - FULL BACKTEST")
    print("=" * 80)
    print()
    print(f"Period: {start_date.date()} to {end_date.date()}")
    print(f"Initial Capital: ${args.capital:,.0f}")
    print()

    # データ準備
    cache_dir = Path(__file__).parent / "cache"
    master_data = Path(__file__).parent / "data" / "ai_stocks_master.json"

    data_manager, universe_manager, cost_model, regime_detector = prepare_backtest_data(
        start_date=start_date,
        end_date=end_date,
        master_data_path=master_data,
        cache_dir=cache_dir if not args.no_cache else None,
    )

    # バックテスト設定
    config = BacktestConfig(
        start_date=start_date,
        end_date=end_date,
        initial_capital=args.capital,
        rebalance_frequency="weekly",
        rebalance_day="Monday",
        max_position_size=0.10,
        max_category_size=0.30,
        min_trade_threshold=0.001,
        enable_trading_costs=True,
        benchmark_ticker="SPY",
        enable_regime_detection=True,
    )

    # エンジン初期化
    engine = BacktestEngine(
        config=config,
        data_manager=data_manager,
        universe_manager=universe_manager,
        cost_model=cost_model,
        regime_detector=regime_detector,
    )

    # 戦略作成
    strategy = create_ai_agent_strategy(
        enable_agents=False,  # 現在は等ウェイト
        use_simple_fallback=True,
    )

    # バックテスト実行
    result = engine.run(strategy)

    # 結果保存
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = output_dir / f"backtest_result_{timestamp}.json"
    result.save_to_json(result_file)

    # CSV保存
    result.save_to_csv(output_dir)

    # サマリー表示
    print()
    print("=" * 80)
    print("BACKTEST RESULTS SUMMARY")
    print("=" * 80)
    print()
    print(f"Period: {start_date.date()} to {end_date.date()}")
    print(f"Total Weeks: {result.summary['total_weeks']}")
    print()
    print("PERFORMANCE METRICS:")
    print(f"  Total Return:       {result.metrics.total_return:>8.2%}")
    print(f"  Annualized Return:  {result.metrics.annualized_return:>8.2%}")
    print(f"  Sharpe Ratio:       {result.metrics.sharpe_ratio:>8.2f}")
    print(f"  Sortino Ratio:      {result.metrics.sortino_ratio:>8.2f}")
    print(f"  Calmar Ratio:       {result.metrics.calmar_ratio:>8.2f}")
    print()
    print("RISK METRICS:")
    print(f"  Max Drawdown:       {result.metrics.max_drawdown:>8.2%}")
    print(f"  Volatility (Ann.):  {result.metrics.annualized_volatility:>8.2%}")
    print(f"  Max DD Duration:    {result.metrics.max_drawdown_duration:>8} days")
    print()
    print("TRADING METRICS:")
    print(f"  Win Rate:           {result.metrics.win_rate:>8.2%}")
    print(f"  Total Trading Cost: ${result.metrics.total_trading_cost:>,.2f}")
    print(f"  Cost % of Capital:  {result.metrics.total_trading_cost / args.capital:>8.2%}")
    print()
    print("PORTFOLIO:")
    print(f"  Final Value:        ${result.summary['final_value']:>,.2f}")
    print(f"  Initial Capital:    ${args.capital:>,.2f}")
    print(f"  Profit:             ${result.summary['final_value'] - args.capital:>,.2f}")
    print()
    print("=" * 80)
    print(f"✅ Results saved to: {result_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()
