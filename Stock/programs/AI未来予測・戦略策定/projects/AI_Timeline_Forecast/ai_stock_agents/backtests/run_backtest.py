#!/usr/bin/env python3
"""
バックテスト実行スクリプト

Usage:
    python backtests/run_backtest.py --start 2020-01-01 --end 2024-12-31
"""

import argparse
from datetime import datetime
from pathlib import Path
import sys

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backtests.core.timestamped_data import TimeSeriesDataManager
from backtests.core.universe_manager import UniverseManager, create_ai_stock_universe
from backtests.core.market_regime import MarketRegimeDetector
from backtests.engine.backtest_engine import BacktestEngine, BacktestConfig, create_simple_strategy
from backtests.engine.cost_model import TradingCostModel, create_ai_stock_cost_model


def main():
    parser = argparse.ArgumentParser(description="AI Stock Agent Backtest")
    parser.add_argument("--start", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--capital", type=float, default=1000000, help="Initial capital (default: $1M)")
    parser.add_argument("--output", type=str, default="backtest_results", help="Output directory")
    parser.add_argument("--no-costs", action="store_true", help="Disable trading costs")

    args = parser.parse_args()

    # 日付パース
    start_date = datetime.strptime(args.start, "%Y-%m-%d")
    end_date = datetime.strptime(args.end, "%Y-%m-%d")

    print("=" * 80)
    print("AI STOCK AGENT BACKTEST")
    print("=" * 80)
    print()

    # 1. 設定
    config = BacktestConfig(
        start_date=start_date,
        end_date=end_date,
        initial_capital=args.capital,
        enable_trading_costs=not args.no_costs,
    )

    # 2. データマネージャー初期化
    data_manager = TimeSeriesDataManager()
    print("✅ TimeSeriesDataManager initialized")

    # 3. ユニバースマネージャー初期化
    universe_manager = create_ai_stock_universe()
    print(f"✅ UniverseManager initialized ({len(universe_manager.get_categories())} categories)")

    # 4. コストモデル初期化
    cost_model = create_ai_stock_cost_model()
    print("✅ TradingCostModel initialized")

    # 5. レジーム検出器初期化（オプション）
    regime_detector = None
    if config.enable_regime_detection:
        regime_detector = MarketRegimeDetector()
        print("✅ MarketRegimeDetector initialized")

    # 6. バックテストエンジン初期化
    engine = BacktestEngine(
        config=config,
        data_manager=data_manager,
        universe_manager=universe_manager,
        cost_model=cost_model,
        regime_detector=regime_detector,
    )
    print("✅ BacktestEngine initialized")
    print()

    # 7. 戦略定義（テスト用: 等ウェイト）
    strategy = create_simple_strategy()
    print("📊 Strategy: Equal Weight")
    print()

    # 8. バックテスト実行
    print("🚀 Running backtest...")
    print()

    result = engine.run(strategy)

    # 9. 結果出力
    print()
    print("=" * 80)
    print("BACKTEST RESULTS")
    print("=" * 80)
    print()
    print(f"Total Return:        {result.metrics.total_return:+.2%}")
    print(f"Annualized Return:   {result.metrics.annualized_return:+.2%}")
    print(f"Sharpe Ratio:        {result.metrics.sharpe_ratio:.2f}")
    print(f"Max Drawdown:        {result.metrics.max_drawdown:.2%}")
    print(f"Win Rate:            {result.metrics.win_rate:.2%}")
    print()
    print(f"Total Trading Cost:  ${result.metrics.total_trading_cost:,.2f}")
    print(f"Cost Drag:           {(result.metrics.gross_return - result.metrics.net_return):.2%}")
    print()

    # 10. 結果保存
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    result_file = output_dir / f"backtest_{start_date.date()}_{end_date.date()}.json"
    result.save_to_json(result_file)

    print(f"📁 Full results saved to: {result_file}")
    print()


if __name__ == "__main__":
    main()
