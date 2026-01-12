"""
Walk-Forward Analysis Execution Script

Out-of-Sample検証により戦略の頑健性を評価
"""

from datetime import datetime
from pathlib import Path
import json
import pandas as pd

import sys
sys.path.append(str(Path(__file__).parent))

from data_loader.data_preparer import prepare_backtest_data
from engine.backtest_engine import BacktestEngine, BacktestConfig
from engine.walk_forward import WalkForwardAnalyzer, WalkForwardConfig, evaluate_walk_forward_quality
from strategies.ai_agent_strategy import create_ai_agent_strategy


def run_backtest_for_period(
    start_date: datetime,
    end_date: datetime,
    data_manager,
    universe_manager,
    cost_model,
    regime_detector,
    initial_capital: float = 1000000,
):
    """指定期間のバックテスト実行"""
    config = BacktestConfig(
        start_date=start_date,
        end_date=end_date,
        initial_capital=initial_capital,
        rebalance_frequency="weekly",
        rebalance_day="Monday",
        max_position_size=0.10,
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

    strategy = create_ai_agent_strategy(enable_agents=False, use_simple_fallback=True)
    result = engine.run(strategy)

    return result


def main():
    print("=" * 80)
    print("WALK-FORWARD ANALYSIS - AI STOCK AGENTS")
    print("=" * 80)
    print()

    # 全期間データ準備
    full_start = datetime(2020, 1, 1)
    full_end = datetime(2024, 12, 31)

    cache_dir = Path(__file__).parent / "cache"
    master_data = Path(__file__).parent / "data" / "ai_stocks_master.json"

    print("📊 Loading full dataset...")
    data_manager, universe_manager, cost_model, regime_detector = prepare_backtest_data(
        start_date=full_start,
        end_date=full_end,
        master_data_path=master_data,
        cache_dir=cache_dir,
    )

    # Walk-Forward設定
    wf_config = WalkForwardConfig(
        start_date=full_start,
        end_date=full_end,
        train_period_months=24,  # 2年訓練
        test_period_months=6,     # 6ヶ月テスト
        anchored=True,            # Anchored方式（開始点固定）
        step_months=6,
    )

    print()
    print("🔍 Walk-Forward Configuration:")
    print(f"   Train Period: {wf_config.train_period_months} months")
    print(f"   Test Period: {wf_config.test_period_months} months")
    print(f"   Method: {'Anchored' if wf_config.anchored else 'Rolling'}")
    print()

    # ウィンドウ生成
    analyzer = WalkForwardAnalyzer(wf_config)
    windows = analyzer._generate_windows()

    print(f"📈 Generated {len(windows)} windows")
    print()

    # 各ウィンドウでバックテスト実行
    window_results = []
    all_weekly_returns = []  # 全リターンを保存

    for i, (train_start, train_end, test_start, test_end) in enumerate(windows):
        print("=" * 80)
        print(f"WINDOW {i+1}/{len(windows)}")
        print("=" * 80)
        print(f"Train: {train_start.date()} to {train_end.date()}")
        print(f"Test:  {test_start.date()} to {test_end.date()}")
        print()

        # Train期間バックテスト
        print("🏋️  Training Phase...")
        train_result = run_backtest_for_period(
            train_start, train_end,
            data_manager, universe_manager, cost_model, regime_detector
        )

        train_metrics = {
            "total_return": train_result.metrics.total_return,
            "sharpe": train_result.metrics.sharpe_ratio,
            "max_drawdown": train_result.metrics.max_drawdown,
        }

        # Test期間バックテスト
        print("🧪 Testing Phase...")
        test_result = run_backtest_for_period(
            test_start, test_end,
            data_manager, universe_manager, cost_model, regime_detector
        )

        test_metrics = {
            "total_return": test_result.metrics.total_return,
            "sharpe": test_result.metrics.sharpe_ratio,
            "max_drawdown": test_result.metrics.max_drawdown,
        }

        # 劣化度計算
        if train_metrics["sharpe"] > 0:
            degradation = (train_metrics["sharpe"] - test_metrics["sharpe"]) / train_metrics["sharpe"]
        else:
            degradation = 0.0

        # 結果保存
        from engine.walk_forward import WindowResult
        window_result = WindowResult(
            window_id=i + 1,
            train_start=train_start,
            train_end=train_end,
            test_start=test_start,
            test_end=test_end,
            train_return=train_metrics["total_return"],
            train_sharpe=train_metrics["sharpe"],
            train_max_drawdown=train_metrics["max_drawdown"],
            test_return=test_metrics["total_return"],
            test_sharpe=test_metrics["sharpe"],
            test_max_drawdown=test_metrics["max_drawdown"],
            degradation=degradation,
        )

        window_results.append(window_result)

        # リターンデータ保存
        test_result.weekly_returns['window_id'] = i + 1
        test_result.weekly_returns['phase'] = 'test'
        all_weekly_returns.append(test_result.weekly_returns)

        # ウィンドウサマリー表示
        print()
        print(f"📊 Window {i+1} Results:")
        print(f"   Train Sharpe: {train_metrics['sharpe']:.2f}")
        print(f"   Test Sharpe:  {test_metrics['sharpe']:.2f}")
        print(f"   Degradation:  {degradation:.1%}")
        print()

    # 全体統計計算
    import numpy as np
    from engine.walk_forward import WalkForwardResult

    avg_train_sharpe = np.mean([w.train_sharpe for w in window_results])
    avg_test_sharpe = np.mean([w.test_sharpe for w in window_results])
    avg_degradation = np.mean([w.degradation for w in window_results])
    test_sharpe_std = np.std([w.test_sharpe for w in window_results])
    positive_test_windows = sum(1 for w in window_results if w.test_return > 0)

    wf_result = WalkForwardResult(
        config=wf_config,
        windows=window_results,
        avg_train_sharpe=avg_train_sharpe,
        avg_test_sharpe=avg_test_sharpe,
        avg_degradation=avg_degradation,
        test_sharpe_std=test_sharpe_std,
        positive_test_windows=positive_test_windows,
        total_windows=len(window_results),
    )

    # 品質評価
    quality = evaluate_walk_forward_quality(wf_result)

    # 結果保存
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = output_dir / f"walkforward_result_{timestamp}.json"

    with open(result_file, "w") as f:
        json.dump(wf_result.to_dict(), f, indent=2)

    # CSV保存
    all_returns_df = pd.concat(all_weekly_returns, ignore_index=True)
    csv_file = output_dir / f"walkforward_returns_{timestamp}.csv"
    all_returns_df.to_csv(csv_file, index=False)

    # 結果表示
    print()
    print("=" * 80)
    print("WALK-FORWARD ANALYSIS RESULTS")
    print("=" * 80)
    print()
    print(f"Total Windows: {wf_result.total_windows}")
    print()
    print("PERFORMANCE METRICS:")
    print(f"  Avg Train Sharpe:  {avg_train_sharpe:>8.2f}")
    print(f"  Avg Test Sharpe:   {avg_test_sharpe:>8.2f}")
    print(f"  Avg Degradation:   {avg_degradation:>8.1%}")
    print(f"  Test Sharpe Std:   {test_sharpe_std:>8.2f}")
    print()
    print("STABILITY METRICS:")
    print(f"  Test Win Rate:     {positive_test_windows}/{wf_result.total_windows} ({positive_test_windows/wf_result.total_windows:.1%})")
    print()
    print("QUALITY ASSESSMENT:")
    print(f"  Overall Rating:    {quality['overall'].upper()}")
    print(f"  Score:             {quality['score']}/{quality['max_score']}")
    print()
    print("  Evaluation:")
    for reason in quality['reasons']:
        print(f"    {reason}")
    print()
    print("=" * 80)
    print(f"✅ Results saved to:")
    print(f"   JSON: {result_file}")
    print(f"   CSV:  {csv_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()
