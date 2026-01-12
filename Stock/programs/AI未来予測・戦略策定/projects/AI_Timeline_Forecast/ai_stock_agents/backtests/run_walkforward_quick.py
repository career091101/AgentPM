"""
Quick Walk-Forward Analysis

簡易版: 3つのウィンドウのみでテスト
"""

from datetime import datetime
from pathlib import Path
import json
import pandas as pd
import numpy as np

import sys
sys.path.append(str(Path(__file__).parent))

from data_loader.data_preparer import prepare_backtest_data
from engine.backtest_engine import BacktestEngine, BacktestConfig
from engine.walk_forward import WindowResult, WalkForwardResult, WalkForwardConfig, evaluate_walk_forward_quality
from strategies.ai_agent_strategy import create_ai_agent_strategy


def run_backtest_for_period(
    start_date: datetime,
    end_date: datetime,
    data_manager,
    universe_manager,
    cost_model,
    regime_detector,
):
    """指定期間のバックテスト実行"""
    config = BacktestConfig(
        start_date=start_date,
        end_date=end_date,
        initial_capital=1000000,
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

    strategy = create_ai_agent_strategy(enable_agents=False)
    result = engine.run(strategy)

    return result


def main():
    print("=" * 80)
    print("QUICK WALK-FORWARD ANALYSIS")
    print("=" * 80)
    print()

    # データ準備（全期間）
    full_start = datetime(2020, 1, 1)
    full_end = datetime(2024, 12, 31)

    cache_dir = Path(__file__).parent / "cache"
    master_data = Path(__file__).parent / "data" / "ai_stocks_master.json"

    print("📊 Loading dataset...")
    data_manager, universe_manager, cost_model, regime_detector = prepare_backtest_data(
        start_date=full_start,
        end_date=full_end,
        master_data_path=master_data,
        cache_dir=cache_dir,
    )

    # 簡易版ウィンドウ定義（手動）
    windows = [
        # Window 1: 2020-2021訓練, 2022前半テスト
        (datetime(2020, 1, 1), datetime(2021, 12, 31), datetime(2022, 1, 1), datetime(2022, 6, 30)),
        # Window 2: 2020-2022訓練, 2023前半テスト
        (datetime(2020, 1, 1), datetime(2022, 12, 31), datetime(2023, 1, 1), datetime(2023, 6, 30)),
        # Window 3: 2020-2023訓練, 2024前半テスト
        (datetime(2020, 1, 1), datetime(2023, 12, 31), datetime(2024, 1, 1), datetime(2024, 6, 30)),
    ]

    print(f"🔍 Running {len(windows)} windows (Anchored方式)")
    print()

    window_results = []

    for i, (train_start, train_end, test_start, test_end) in enumerate(windows):
        print("=" * 80)
        print(f"WINDOW {i+1}/{len(windows)}")
        print("=" * 80)
        print(f"Train: {train_start.date()} to {train_end.date()}")
        print(f"Test:  {test_start.date()} to {test_end.date()}")
        print()

        # Train
        print("🏋️  Training...")
        train_result = run_backtest_for_period(
            train_start, train_end,
            data_manager, universe_manager, cost_model, regime_detector
        )

        train_metrics = {
            "total_return": train_result.metrics.total_return,
            "sharpe": train_result.metrics.sharpe_ratio,
            "max_drawdown": train_result.metrics.max_drawdown,
        }

        # Test
        print("🧪 Testing...")
        test_result = run_backtest_for_period(
            test_start, test_end,
            data_manager, universe_manager, cost_model, regime_detector
        )

        test_metrics = {
            "total_return": test_result.metrics.total_return,
            "sharpe": test_result.metrics.sharpe_ratio,
            "max_drawdown": test_result.metrics.max_drawdown,
        }

        # 劣化度
        if train_metrics["sharpe"] > 0:
            degradation = (train_metrics["sharpe"] - test_metrics["sharpe"]) / train_metrics["sharpe"]
        else:
            degradation = 0.0

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

        print()
        print(f"📊 Window {i+1} Results:")
        print(f"   Train: Return={train_metrics['total_return']:>7.2%}, Sharpe={train_metrics['sharpe']:>5.2f}, MaxDD={train_metrics['max_drawdown']:>7.2%}")
        print(f"   Test:  Return={test_metrics['total_return']:>7.2%}, Sharpe={test_metrics['sharpe']:>5.2f}, MaxDD={test_metrics['max_drawdown']:>7.2%}")
        print(f"   Degradation: {degradation:>6.1%}")
        print()

    # 全体統計
    wf_config = WalkForwardConfig(
        start_date=full_start,
        end_date=full_end,
        train_period_months=24,
        test_period_months=6,
        anchored=True,
    )

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
    result_file = output_dir / f"walkforward_quick_{timestamp}.json"

    with open(result_file, "w") as f:
        json.dump(wf_result.to_dict(), f, indent=2)

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
    print(f"✅ Results saved to: {result_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()
