"""
ウォークフォワード分析（Walk-Forward Analysis）

過剰最適化（Overfitting）を防ぐため、In-Sample/Out-of-Sampleを
ローリングウィンドウで繰り返し検証。
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Callable
import pandas as pd
import numpy as np


@dataclass
class WalkForwardConfig:
    """ウォークフォワード分析設定"""

    # 全体期間
    start_date: datetime
    end_date: datetime

    # In-Sample期間（訓練期間）
    train_period_months: int = 24  # 2年

    # Out-of-Sample期間（テスト期間）
    test_period_months: int = 6  # 6ヶ月

    # アンカー型 vs ローリング型
    anchored: bool = True  # True: Anchored (開始点固定), False: Rolling (全期間移動)

    # ステップサイズ（次のウィンドウまでの移動月数）
    step_months: int = 6

    # 最小データポイント数
    min_data_points: int = 100


@dataclass
class WindowResult:
    """各ウィンドウの結果"""

    window_id: int
    train_start: datetime
    train_end: datetime
    test_start: datetime
    test_end: datetime

    # In-Sample結果
    train_return: float
    train_sharpe: float
    train_max_drawdown: float

    # Out-of-Sample結果
    test_return: float
    test_sharpe: float
    test_max_drawdown: float

    # パフォーマンス劣化度
    degradation: float  # (train_sharpe - test_sharpe) / train_sharpe

    # メタデータ
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WalkForwardResult:
    """ウォークフォワード分析結果"""

    config: WalkForwardConfig
    windows: List[WindowResult]

    # 全体統計
    avg_train_sharpe: float
    avg_test_sharpe: float
    avg_degradation: float

    # 安定性メトリクス
    test_sharpe_std: float  # テスト期間シャープレシオの標準偏差
    positive_test_windows: int  # テスト期間で利益が出たウィンドウ数
    total_windows: int

    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "config": {
                "start_date": self.config.start_date.isoformat(),
                "end_date": self.config.end_date.isoformat(),
                "train_period_months": self.config.train_period_months,
                "test_period_months": self.config.test_period_months,
                "anchored": self.config.anchored,
            },
            "summary": {
                "total_windows": self.total_windows,
                "avg_train_sharpe": self.avg_train_sharpe,
                "avg_test_sharpe": self.avg_test_sharpe,
                "avg_degradation": self.avg_degradation,
                "test_sharpe_std": self.test_sharpe_std,
                "positive_test_windows": self.positive_test_windows,
                "win_rate": self.positive_test_windows / self.total_windows if self.total_windows > 0 else 0,
            },
            "windows": [
                {
                    "window_id": w.window_id,
                    "train_period": f"{w.train_start.date()} to {w.train_end.date()}",
                    "test_period": f"{w.test_start.date()} to {w.test_end.date()}",
                    "train_sharpe": w.train_sharpe,
                    "test_sharpe": w.test_sharpe,
                    "degradation": w.degradation,
                }
                for w in self.windows
            ],
        }


class WalkForwardAnalyzer:
    """
    ウォークフォワード分析器

    戦略の堅牢性を検証するため、ローリングウィンドウで
    In-Sample最適化とOut-of-Sample検証を繰り返す。
    """

    def __init__(self, config: WalkForwardConfig):
        self.config = config

    def run_analysis(
        self,
        strategy_func: Callable[[datetime, datetime], Dict[str, Any]],
        returns_data: pd.DataFrame,  # date, return
    ) -> WalkForwardResult:
        """
        ウォークフォワード分析実行

        Args:
            strategy_func: 戦略実行関数
                引数: (start_date, end_date)
                戻り値: {"returns": pd.DataFrame, "sharpe": float, ...}
            returns_data: 全期間のリターンデータ（date, return）

        Returns:
            WalkForwardResult
        """
        # ウィンドウ生成
        windows = self._generate_windows()

        # 各ウィンドウで分析
        window_results = []

        for i, (train_start, train_end, test_start, test_end) in enumerate(windows):
            print(f"Window {i+1}/{len(windows)}: Train {train_start.date()} to {train_end.date()}, "
                  f"Test {test_start.date()} to {test_end.date()}")

            # In-Sample（訓練）
            train_result = strategy_func(train_start, train_end)
            train_returns = returns_data[
                (returns_data["date"] >= train_start) & (returns_data["date"] <= train_end)
            ]

            train_metrics = self._calculate_metrics(train_returns)

            # Out-of-Sample（テスト）
            test_result = strategy_func(test_start, test_end)
            test_returns = returns_data[
                (returns_data["date"] >= test_start) & (returns_data["date"] <= test_end)
            ]

            test_metrics = self._calculate_metrics(test_returns)

            # 劣化度計算
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

        # 全体統計計算
        return self._compute_overall_statistics(window_results)

    def _generate_windows(self) -> List[tuple]:
        """
        ウィンドウ生成

        Returns:
            List of (train_start, train_end, test_start, test_end)
        """
        windows = []
        current_date = self.config.start_date

        while True:
            # Train期間
            if self.config.anchored:
                # Anchored: 開始点は固定
                train_start = self.config.start_date
            else:
                # Rolling: 開始点も移動
                train_start = current_date

            train_end = train_start + timedelta(days=self.config.train_period_months * 30)

            # Test期間
            test_start = train_end + timedelta(days=1)
            test_end = test_start + timedelta(days=self.config.test_period_months * 30)

            # 終了日を超えたら終了
            if test_end > self.config.end_date:
                break

            windows.append((train_start, train_end, test_start, test_end))

            # 次のウィンドウへ
            current_date = test_start

        return windows

    def _calculate_metrics(self, returns: pd.DataFrame) -> Dict[str, float]:
        """
        パフォーマンスメトリクス計算

        Args:
            returns: DataFrame with "return" column

        Returns:
            {"total_return": float, "sharpe": float, "max_drawdown": float}
        """
        if len(returns) == 0:
            return {"total_return": 0.0, "sharpe": 0.0, "max_drawdown": 0.0}

        returns_arr = returns["return"].values

        # 総リターン
        total_return = np.prod(1 + returns_arr) - 1

        # シャープレシオ（週次データ想定、年率化）
        mean_return = np.mean(returns_arr)
        std_return = np.std(returns_arr)

        annualized_return = mean_return * 52  # 週次 → 年率
        annualized_vol = std_return * np.sqrt(52)

        if annualized_vol > 0:
            sharpe = (annualized_return - 0.04) / annualized_vol  # 無リスク金利4%
        else:
            sharpe = 0.0

        # 最大ドローダウン
        cumulative = np.cumprod(1 + returns_arr)
        cummax = np.maximum.accumulate(cumulative)
        drawdown = (cumulative / cummax) - 1
        max_drawdown = np.min(drawdown)

        return {
            "total_return": total_return,
            "sharpe": sharpe,
            "max_drawdown": max_drawdown,
        }

    def _compute_overall_statistics(self, windows: List[WindowResult]) -> WalkForwardResult:
        """全体統計計算"""
        if not windows:
            return WalkForwardResult(
                config=self.config,
                windows=[],
                avg_train_sharpe=0.0,
                avg_test_sharpe=0.0,
                avg_degradation=0.0,
                test_sharpe_std=0.0,
                positive_test_windows=0,
                total_windows=0,
            )

        # 平均値計算
        avg_train_sharpe = np.mean([w.train_sharpe for w in windows])
        avg_test_sharpe = np.mean([w.test_sharpe for w in windows])
        avg_degradation = np.mean([w.degradation for w in windows])

        # テストシャープレシオの標準偏差（安定性指標）
        test_sharpe_std = np.std([w.test_sharpe for w in windows])

        # テスト期間で利益が出たウィンドウ数
        positive_test_windows = sum(1 for w in windows if w.test_return > 0)

        return WalkForwardResult(
            config=self.config,
            windows=windows,
            avg_train_sharpe=avg_train_sharpe,
            avg_test_sharpe=avg_test_sharpe,
            avg_degradation=avg_degradation,
            test_sharpe_std=test_sharpe_std,
            positive_test_windows=positive_test_windows,
            total_windows=len(windows),
        )


# ヘルパー関数


def evaluate_walk_forward_quality(result: WalkForwardResult) -> Dict[str, str]:
    """
    ウォークフォワード結果の品質評価

    Returns:
        {"overall": "excellent/good/poor", "reasons": [...]}
    """
    reasons = []
    score = 0

    # 1. テストシャープレシオ
    if result.avg_test_sharpe > 1.5:
        reasons.append("✅ Excellent Out-of-Sample Sharpe (>1.5)")
        score += 3
    elif result.avg_test_sharpe > 1.0:
        reasons.append("✅ Good Out-of-Sample Sharpe (>1.0)")
        score += 2
    elif result.avg_test_sharpe > 0.5:
        reasons.append("⚠️  Moderate Out-of-Sample Sharpe (>0.5)")
        score += 1
    else:
        reasons.append("❌ Poor Out-of-Sample Sharpe (<0.5)")

    # 2. 劣化度
    if result.avg_degradation < 0.2:
        reasons.append("✅ Low Performance Degradation (<20%)")
        score += 2
    elif result.avg_degradation < 0.4:
        reasons.append("⚠️  Moderate Performance Degradation (<40%)")
        score += 1
    else:
        reasons.append("❌ High Performance Degradation (>40%)")

    # 3. テスト勝率
    win_rate = result.positive_test_windows / result.total_windows
    if win_rate > 0.75:
        reasons.append(f"✅ High Test Win Rate ({win_rate:.1%})")
        score += 2
    elif win_rate > 0.5:
        reasons.append(f"✅ Positive Test Win Rate ({win_rate:.1%})")
        score += 1
    else:
        reasons.append(f"❌ Low Test Win Rate ({win_rate:.1%})")

    # 4. 安定性（標準偏差）
    if result.test_sharpe_std < 0.5:
        reasons.append("✅ Stable Performance (Low Sharpe StdDev)")
        score += 1
    else:
        reasons.append("⚠️  Unstable Performance (High Sharpe StdDev)")

    # 総合評価
    if score >= 6:
        overall = "excellent"
    elif score >= 4:
        overall = "good"
    else:
        overall = "poor"

    return {
        "overall": overall,
        "score": score,
        "max_score": 8,
        "reasons": reasons,
    }
