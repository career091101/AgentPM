#!/usr/bin/env python3
"""
統合テストスクリプト

バックテストシステムの全コンポーネントを統合してテスト実行

Usage:
    python backtests/integration_test.py
"""

from datetime import datetime
from pathlib import Path
import sys

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backtests.data_loader.data_preparer import prepare_backtest_data
from backtests.engine.backtest_engine import BacktestEngine, BacktestConfig
from backtests.strategies.ai_agent_strategy import create_ai_agent_strategy


def main():
    print("=" * 80)
    print("AI STOCK AGENT BACKTEST - INTEGRATION TEST")
    print("=" * 80)
    print()

    # テスト期間（短期テスト: 2023年1月-6月）
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 6, 30)

    print(f"📅 Test Period: {start_date.date()} to {end_date.date()}")
    print()

    # ステップ1: データ準備
    print("=" * 80)
    print("STEP 1: Data Preparation")
    print("=" * 80)
    print()

    cache_dir = Path(__file__).parent / "cache"
    cache_dir.mkdir(exist_ok=True)

    try:
        data_manager, universe_manager, cost_model, regime_detector = prepare_backtest_data(
            start_date=start_date,
            end_date=end_date,
            cache_dir=cache_dir,
        )
    except Exception as e:
        print(f"❌ Data preparation failed: {e}")
        print()
        print("Possible causes:")
        print("- yfinance connection failure (check internet connection)")
        print("- Missing ai_stocks_master.json (check data/ directory)")
        print("- Invalid date range")
        return 1

    # ステップ2: バックテスト設定
    print("=" * 80)
    print("STEP 2: Backtest Configuration")
    print("=" * 80)
    print()

    config = BacktestConfig(
        start_date=start_date,
        end_date=end_date,
        initial_capital=1000000,  # $1M
        enable_trading_costs=True,
        enable_regime_detection=False,  # 短期テストでは無効化
    )

    print(f"   Initial Capital: ${config.initial_capital:,.0f}")
    print(f"   Trading Costs: {'Enabled' if config.enable_trading_costs else 'Disabled'}")
    print(f"   Regime Detection: {'Enabled' if config.enable_regime_detection else 'Disabled'}")
    print()

    # ステップ3: 戦略準備
    print("=" * 80)
    print("STEP 3: Strategy Setup")
    print("=" * 80)
    print()

    # テスト用: 等ウェイト戦略（AgentSkillsは後で統合）
    strategy = create_ai_agent_strategy(
        enable_agents=False,  # AgentSkills無効（等ウェイト戦略）
        use_simple_fallback=True,
    )

    print("   Strategy: Equal Weight (AgentSkills disabled for testing)")
    print()

    # ステップ4: バックテストエンジン初期化
    print("=" * 80)
    print("STEP 4: Backtest Engine Initialization")
    print("=" * 80)
    print()

    engine = BacktestEngine(
        config=config,
        data_manager=data_manager,
        universe_manager=universe_manager,
        cost_model=cost_model,
        regime_detector=regime_detector if config.enable_regime_detection else None,
    )

    print("   ✅ BacktestEngine ready")
    print()

    # ステップ5: バックテスト実行
    print("=" * 80)
    print("STEP 5: Running Backtest")
    print("=" * 80)
    print()

    try:
        result = engine.run(strategy)
    except Exception as e:
        print(f"❌ Backtest execution failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # ステップ6: 結果表示
    print("=" * 80)
    print("STEP 6: Results")
    print("=" * 80)
    print()

    print("📊 Performance Metrics:")
    print(f"   Total Return:        {result.metrics.total_return:+.2%}")
    print(f"   Annualized Return:   {result.metrics.annualized_return:+.2%}")
    print(f"   Sharpe Ratio:        {result.metrics.sharpe_ratio:.2f}")
    print(f"   Max Drawdown:        {result.metrics.max_drawdown:.2%}")
    print(f"   Win Rate:            {result.metrics.win_rate:.2%}")
    print()

    print("💰 Cost Analysis:")
    print(f"   Gross Return:        {result.metrics.gross_return:+.2%}")
    print(f"   Net Return:          {result.metrics.net_return:+.2%}")
    print(f"   Total Trading Cost:  ${result.metrics.total_trading_cost:,.2f}")
    print(f"   Cost Drag:           {(result.metrics.gross_return - result.metrics.net_return):.2%}")
    print()

    # ステップ7: 結果保存
    print("=" * 80)
    print("STEP 7: Saving Results")
    print("=" * 80)
    print()

    output_dir = Path(__file__).parent / "test_results"
    output_dir.mkdir(exist_ok=True)

    result_file = output_dir / f"integration_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    result.save_to_json(result_file)

    print(f"   📁 Results saved: {result_file}")
    print()

    # ステップ8: テスト評価
    print("=" * 80)
    print("STEP 8: Test Evaluation")
    print("=" * 80)
    print()

    # 基本的な健全性チェック
    checks_passed = 0
    total_checks = 5

    # チェック1: リターンがNaNでない
    if not (result.metrics.total_return != result.metrics.total_return):  # NaNチェック
        print("   ✅ Return calculation valid")
        checks_passed += 1
    else:
        print("   ❌ Return calculation failed (NaN)")

    # チェック2: ウェイトの合計が1.0付近
    if result.weekly_positions:
        avg_sum = sum(
            sum(pos["portfolio"].values())
            for pos in result.weekly_positions
        ) / len(result.weekly_positions)
        if 0.99 <= avg_sum <= 1.01:
            print(f"   ✅ Portfolio weights valid (avg sum: {avg_sum:.4f})")
            checks_passed += 1
        else:
            print(f"   ❌ Portfolio weights invalid (avg sum: {avg_sum:.4f})")

    # チェック3: コストが正の値
    if result.metrics.total_trading_cost >= 0:
        print("   ✅ Trading costs non-negative")
        checks_passed += 1
    else:
        print("   ❌ Trading costs negative")

    # チェック4: 週次データ数が妥当
    expected_weeks = (end_date - start_date).days // 7
    actual_weeks = len(result.weekly_returns)
    if abs(actual_weeks - expected_weeks) <= 2:  # ±2週許容
        print(f"   ✅ Weekly data count reasonable ({actual_weeks} weeks)")
        checks_passed += 1
    else:
        print(f"   ⚠️  Weekly data count unexpected ({actual_weeks} vs expected ~{expected_weeks})")

    # チェック5: 最終ポートフォリオ価値が正
    final_value = result.summary["final_value"]
    if final_value > 0:
        print(f"   ✅ Final portfolio value positive (${final_value:,.2f})")
        checks_passed += 1
    else:
        print(f"   ❌ Final portfolio value invalid (${final_value:,.2f})")

    print()
    print(f"   Test Score: {checks_passed}/{total_checks} checks passed")
    print()

    if checks_passed == total_checks:
        print("=" * 80)
        print("✅ INTEGRATION TEST PASSED")
        print("=" * 80)
        print()
        print("Next Steps:")
        print("1. Run full backtest with 2020-2024 data")
        print("2. Enable AgentSkills strategy integration")
        print("3. Implement visualization (equity curve, drawdown chart)")
        print("4. Run walk-forward analysis")
        return 0
    else:
        print("=" * 80)
        print("⚠️  INTEGRATION TEST COMPLETED WITH WARNINGS")
        print("=" * 80)
        print()
        print("Review the failed checks above and fix issues before full backtest.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
