"""
バックテスト実行エンジン

AI株式投資エージェントの週次リバランス戦略をバックテスト。
ルックアヘッドバイアス、サバイバーシップバイアスを厳格に排除。
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable
from pathlib import Path
import pandas as pd
import numpy as np
import json

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from core.timestamped_data import TimeSeriesDataManager, get_monday_timestamp, get_previous_friday
from core.universe_manager import UniverseManager
from core.market_regime import MarketRegimeDetector, MarketRegime
from metrics.performance_metrics import BacktestMetrics, calculate_performance_metrics
from engine.cost_model import TradingCostModel, RebalanceCost


@dataclass
class BacktestConfig:
    """バックテスト設定"""

    # 期間
    start_date: datetime
    end_date: datetime

    # 初期資本
    initial_capital: float = 1000000  # $1M

    # リバランス頻度
    rebalance_frequency: str = "weekly"  # "weekly", "monthly"
    rebalance_day: str = "Monday"  # 週次の場合

    # ポートフォリオ制約
    max_position_size: float = 0.10  # 10%/銘柄
    max_category_size: float = 0.30  # 30%/カテゴリ
    min_trade_threshold: float = 0.001  # 0.1%未満の変動は無視

    # コスト設定
    enable_trading_costs: bool = True
    commission_per_trade: float = 0.0  # IBKR無料

    # データソース
    data_dir: Optional[Path] = None
    benchmark_ticker: str = "SPY"  # S&P500

    # レジーム検出
    enable_regime_detection: bool = True


@dataclass
class BacktestResult:
    """バックテスト結果"""

    config: BacktestConfig
    metrics: BacktestMetrics

    # 週次履歴
    weekly_returns: pd.DataFrame  # date, return, portfolio_value
    weekly_positions: List[Dict[str, Any]]  # 各週のポジション

    # レジーム別パフォーマンス
    regime_performance: Dict[MarketRegime, Dict[str, Any]]

    # コスト詳細
    cost_history: List[Dict[str, Any]]

    # サマリー
    summary: Dict[str, Any]

    def save_to_json(self, output_path: Path) -> None:
        """結果をJSON保存"""
        output = {
            "config": {
                "start_date": self.config.start_date.isoformat(),
                "end_date": self.config.end_date.isoformat(),
                "initial_capital": self.config.initial_capital,
                "rebalance_frequency": self.config.rebalance_frequency,
            },
            "metrics": self.metrics.to_dict(),
            "regime_performance": {
                regime.value: perf for regime, perf in self.regime_performance.items()
            },
            "summary": self.summary,
        }

        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)

        print(f"✅ Results saved to {output_path}")

    def save_to_csv(self, output_dir: Path) -> None:
        """CSV形式で詳細データを保存"""
        output_dir.mkdir(parents=True, exist_ok=True)

        # Weekly returns
        csv_path = output_dir / f"weekly_returns_{self.config.start_date.date()}_{self.config.end_date.date()}.csv"
        self.weekly_returns.to_csv(csv_path, index=False)
        print(f"✅ Weekly returns CSV saved: {csv_path}")

        # Cost history
        cost_df = pd.DataFrame(self.cost_history)
        cost_csv = output_dir / f"cost_history_{self.config.start_date.date()}_{self.config.end_date.date()}.csv"
        cost_df.to_csv(cost_csv, index=False)
        print(f"✅ Cost history CSV saved: {cost_csv}")


class BacktestEngine:
    """
    バックテスト実行エンジン

    週次リバランス戦略をシミュレート。
    """

    def __init__(
        self,
        config: BacktestConfig,
        data_manager: TimeSeriesDataManager,
        universe_manager: UniverseManager,
        cost_model: TradingCostModel,
        regime_detector: Optional[MarketRegimeDetector] = None,
    ):
        self.config = config
        self.data_manager = data_manager
        self.universe_manager = universe_manager
        self.cost_model = cost_model
        self.regime_detector = regime_detector

        # 履歴記録
        self.portfolio_history: List[Dict[str, Any]] = []
        self.return_history: List[Dict[str, Any]] = []
        self.cost_history: List[Dict[str, Any]] = []

    def run(
        self,
        strategy_func: Callable[[datetime, List[str]], Dict[str, float]],
    ) -> BacktestResult:
        """
        バックテスト実行

        Args:
            strategy_func: 戦略関数
                引数: (decision_date, available_tickers)
                戻り値: {ticker: weight} の辞書

        Returns:
            BacktestResult
        """
        print(f"🚀 Starting Backtest: {self.config.start_date.date()} to {self.config.end_date.date()}")
        print(f"   Initial Capital: ${self.config.initial_capital:,.0f}")
        print(f"   Rebalance: {self.config.rebalance_frequency} ({self.config.rebalance_day})")
        print()

        # 初期化
        current_date = get_monday_timestamp(self.config.start_date)
        end_date = self.config.end_date
        portfolio_value = self.config.initial_capital
        current_portfolio: Dict[str, float] = {}  # ticker -> weight

        week_count = 0

        # 週次ループ
        while current_date <= end_date:
            week_count += 1

            # 1. 判断可能日（前週金曜終値まで）
            decision_cutoff = get_previous_friday(current_date)

            # 2. 投資可能ユニバース取得（サバイバーシップバイアス防止）
            available_tickers = self.universe_manager.get_available_tickers(
                as_of_date=decision_cutoff
            )

            if len(available_tickers) == 0:
                print(f"⚠️  Week {week_count}: No available tickers on {current_date.date()}")
                current_date += timedelta(days=7)
                continue

            # 3. 戦略実行（decision_cutoff時点のデータのみ使用）
            try:
                target_portfolio = strategy_func(decision_cutoff, available_tickers)
            except Exception as e:
                print(f"❌ Strategy failed on {current_date.date()}: {e}")
                current_date += timedelta(days=7)
                continue

            # 4. リバランスコスト計算
            if self.config.enable_trading_costs:
                rebalance_costs = self.cost_model.calculate_rebalance_cost(
                    current_portfolio,
                    target_portfolio,
                    portfolio_value,
                    self.config.min_trade_threshold,
                )
                total_cost = self.cost_model.calculate_total_cost(rebalance_costs)
            else:
                rebalance_costs = {}
                total_cost = 0.0

            # コスト適用
            portfolio_value -= total_cost

            # 5. ポートフォリオ更新
            current_portfolio = target_portfolio.copy()

            # 6. 週次リターン計算（月曜始値 → 金曜終値）
            week_return = self._calculate_weekly_return(
                current_date, current_portfolio
            )

            portfolio_value *= 1 + week_return

            # 7. レジーム検出
            if self.regime_detector and self.config.enable_regime_detection:
                # TODO: 実装時にSPYデータを渡す
                regime = None
            else:
                regime = None

            # 8. 履歴記録
            self.return_history.append({
                "date": current_date,
                "return": week_return,
                "portfolio_value": portfolio_value,
                "regime": regime.value if regime else None,
            })

            self.portfolio_history.append({
                "date": current_date,
                "portfolio": current_portfolio.copy(),
                "num_positions": len([w for w in current_portfolio.values() if w > 0.001]),
            })

            self.cost_history.append({
                "date": current_date,
                "total_cost": total_cost,
                "cost_percentage": total_cost / portfolio_value if portfolio_value > 0 else 0.0,
            })

            # 進捗表示
            if week_count % 13 == 0:  # 四半期ごと
                print(f"Week {week_count:3d} | {current_date.date()} | "
                      f"Value: ${portfolio_value:,.0f} | "
                      f"Return: {week_return:+.2%} | "
                      f"Positions: {len([w for w in current_portfolio.values() if w > 0.001])}")

            # 次の週へ
            current_date += timedelta(days=7)

        print()
        print(f"✅ Backtest Complete: {week_count} weeks simulated")

        # 結果集計
        return self._compile_results()

    def _calculate_weekly_return(
        self,
        monday: datetime,
        portfolio: Dict[str, float],
    ) -> float:
        """
        週次リターン計算（月曜始値 → 金曜終値）

        Args:
            monday: 月曜日
            portfolio: ポートフォリオウェイト

        Returns:
            週次リターン
        """
        friday = monday + timedelta(days=4)

        total_return = 0.0

        for ticker, weight in portfolio.items():
            if weight < 0.001:
                continue

            # 月曜始値
            monday_price = self._get_price(ticker, monday, "open")

            # 金曜終値
            friday_price = self._get_price(ticker, friday, "close")

            if monday_price and friday_price and monday_price > 0:
                ticker_return = (friday_price / monday_price) - 1
                total_return += weight * ticker_return

        return total_return

    def _get_price(
        self,
        ticker: str,
        date: datetime,
        price_type: str = "close",
    ) -> Optional[float]:
        """
        指定日の株価取得

        Args:
            ticker: ティッカー
            date: 日付
            price_type: "open", "close"

        Returns:
            株価（取得失敗時はNone）
        """
        from core.timestamped_data import DataType

        # data_managerから株価データを取得
        price_data = self.data_manager.get_latest_value(ticker, date, DataType.PRICE)

        if price_data and isinstance(price_data, dict):
            return price_data.get(price_type)

        return None

    def _compile_results(self) -> BacktestResult:
        """結果集計"""
        # DataFrames作成
        returns_df = pd.DataFrame(self.return_history)

        # ベンチマーク（TODO: 実装時にSPYデータ取得）
        benchmark_returns_df = returns_df.copy()
        benchmark_returns_df["return"] = 0.0  # 仮データ

        # メトリクス計算
        trading_costs = [c["total_cost"] for c in self.cost_history]

        metrics = calculate_performance_metrics(
            returns_df[["date", "return"]],
            benchmark_returns_df[["date", "return"]],
            trading_costs,
            self.config.initial_capital,
        )

        # レジーム別パフォーマンス（TODO: 実装）
        regime_performance = {}

        # サマリー
        summary = {
            "total_weeks": len(self.return_history),
            "final_value": self.return_history[-1]["portfolio_value"] if self.return_history else 0,
            "total_return": metrics.total_return,
            "sharpe_ratio": metrics.sharpe_ratio,
            "max_drawdown": metrics.max_drawdown,
            "total_trading_cost": metrics.total_trading_cost,
        }

        return BacktestResult(
            config=self.config,
            metrics=metrics,
            weekly_returns=returns_df,
            weekly_positions=self.portfolio_history,
            regime_performance=regime_performance,
            cost_history=self.cost_history,
            summary=summary,
        )


# ヘルパー関数


def create_simple_strategy() -> Callable:
    """
    シンプルな等ウェイト戦略（テスト用）

    Returns:
        戦略関数
    """
    def strategy(decision_date: datetime, available_tickers: List[str]) -> Dict[str, float]:
        """等ウェイト配分"""
        n = len(available_tickers)
        if n == 0:
            return {}

        weight = 1.0 / n
        return {ticker: weight for ticker in available_tickers}

    return strategy
