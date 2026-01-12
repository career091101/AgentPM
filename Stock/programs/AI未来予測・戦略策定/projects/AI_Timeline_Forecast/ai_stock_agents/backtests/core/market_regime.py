"""
マーケットレジーム検出（Market Regime Detection）

相場環境を「上昇トレンド」「レンジ」「暴落・下降」に分類し、
レジーム別のパフォーマンス測定を可能にする。
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum
import pandas as pd
import numpy as np


class MarketRegime(Enum):
    """マーケットレジーム分類"""

    BULL_TREND = "bull_trend"  # 上昇トレンド相場
    SIDEWAYS = "sideways"  # レンジ相場
    BEAR_CRASH = "bear_crash"  # 暴落・下降相場


@dataclass
class RegimeMetrics:
    """レジーム判定用メトリクス"""

    date: datetime
    sma_200: float  # 200日移動平均
    sma_200_slope: float  # 200日MA年率変化率
    vix: float  # VIX指数
    drawdown_3m: float  # 過去3ヶ月最大ドローダウン
    regime: MarketRegime


class MarketRegimeDetector:
    """
    マーケットレジーム検出器

    S&P500（SPY）とVIXを使用して相場環境を判定。
    """

    def __init__(
        self,
        bull_trend_threshold: float = 0.05,  # 5%以上の年率上昇
        vix_low_threshold: float = 20.0,  # VIX < 20で低ボラティリティ
        vix_high_threshold: float = 30.0,  # VIX > 30で高ボラティリティ
        crash_drawdown_threshold: float = -0.15,  # 3ヶ月で15%以上下落
    ):
        """
        Args:
            bull_trend_threshold: 上昇トレンド判定の年率変化率閾値
            vix_low_threshold: 低VIX閾値
            vix_high_threshold: 高VIX閾値（暴落判定）
            crash_drawdown_threshold: 暴落判定のドローダウン閾値
        """
        self.bull_trend_threshold = bull_trend_threshold
        self.vix_low_threshold = vix_low_threshold
        self.vix_high_threshold = vix_high_threshold
        self.crash_drawdown_threshold = crash_drawdown_threshold

        # レジーム履歴（キャッシュ）
        self._regime_history: Dict[datetime, RegimeMetrics] = {}

    def detect_regime(
        self,
        date: datetime,
        spy_data: pd.DataFrame,
        vix_data: pd.DataFrame,
    ) -> MarketRegime:
        """
        指定日のマーケットレジームを判定

        Args:
            date: 判定日
            spy_data: S&P500（SPY）の株価データ（DataFrame: date, close）
            vix_data: VIX指数データ（DataFrame: date, close）

        Returns:
            MarketRegime
        """
        # キャッシュチェック
        if date in self._regime_history:
            return self._regime_history[date].regime

        # データ準備
        spy_data = spy_data.copy()
        spy_data.set_index("date", inplace=True)
        spy_data.sort_index(inplace=True)

        vix_data = vix_data.copy()
        vix_data.set_index("date", inplace=True)
        vix_data.sort_index(inplace=True)

        # 指定日までのデータに制限
        spy_data = spy_data[spy_data.index <= date]
        vix_data = vix_data[vix_data.index <= date]

        if len(spy_data) < 252:  # 最低1年分のデータ必要
            raise ValueError(f"Insufficient data for {date}. Need at least 252 trading days.")

        # メトリクス計算
        metrics = self._calculate_metrics(date, spy_data, vix_data)

        # レジーム判定
        regime = self._classify_regime(metrics)
        metrics.regime = regime

        # キャッシュ保存
        self._regime_history[date] = metrics

        return regime

    def _calculate_metrics(
        self,
        date: datetime,
        spy_data: pd.DataFrame,
        vix_data: pd.DataFrame,
    ) -> RegimeMetrics:
        """メトリクス計算"""
        # 200日移動平均
        sma_200 = spy_data["close"].rolling(window=200).mean()
        current_sma_200 = sma_200.iloc[-1]

        # 200日MA年率変化率（1年前との比較）
        if len(sma_200) >= 252:
            sma_200_1y_ago = sma_200.iloc[-252]
            sma_200_slope = (current_sma_200 / sma_200_1y_ago) - 1.0
        else:
            sma_200_slope = 0.0

        # VIX（現在値）
        if date in vix_data.index:
            vix_current = vix_data.loc[date, "close"]
        else:
            # 直近のVIX値を使用
            vix_current = vix_data["close"].iloc[-1]

        # 過去3ヶ月（63営業日）の最大ドローダウン
        window_3m = min(63, len(spy_data))
        recent_spy = spy_data["close"].iloc[-window_3m:]
        cummax = recent_spy.cummax()
        drawdown = (recent_spy / cummax) - 1.0
        max_drawdown_3m = drawdown.min()

        return RegimeMetrics(
            date=date,
            sma_200=current_sma_200,
            sma_200_slope=sma_200_slope,
            vix=vix_current,
            drawdown_3m=max_drawdown_3m,
            regime=MarketRegime.SIDEWAYS,  # 仮置き
        )

    def _classify_regime(self, metrics: RegimeMetrics) -> MarketRegime:
        """
        レジーム分類ロジック

        優先順位:
        1. 暴落判定（VIX高 or 急落）
        2. 上昇トレンド判定（MA上昇 and VIX低）
        3. それ以外はレンジ
        """
        # 1. 暴落・下降相場判定
        if metrics.vix > self.vix_high_threshold or metrics.drawdown_3m < self.crash_drawdown_threshold:
            return MarketRegime.BEAR_CRASH

        # 2. 上昇トレンド判定
        if metrics.sma_200_slope > self.bull_trend_threshold and metrics.vix < self.vix_low_threshold:
            return MarketRegime.BULL_TREND

        # 3. レンジ相場
        return MarketRegime.SIDEWAYS

    def get_regime_metrics(self, date: datetime) -> Optional[RegimeMetrics]:
        """指定日のレジームメトリクスを取得"""
        return self._regime_history.get(date)

    def get_regime_history(
        self, start_date: datetime, end_date: datetime
    ) -> List[RegimeMetrics]:
        """期間内のレジーム履歴を取得"""
        history = [
            metrics
            for date, metrics in self._regime_history.items()
            if start_date <= date <= end_date
        ]
        history.sort(key=lambda x: x.date)
        return history

    def get_regime_statistics(
        self, start_date: datetime, end_date: datetime
    ) -> Dict[MarketRegime, Dict[str, any]]:
        """
        レジーム別の統計情報

        Returns:
            {
                MarketRegime.BULL_TREND: {
                    "days": 520,
                    "percentage": 0.51,
                    "avg_vix": 15.2,
                },
                ...
            }
        """
        history = self.get_regime_history(start_date, end_date)

        if not history:
            return {}

        total_days = len(history)
        stats = {}

        for regime in MarketRegime:
            regime_data = [m for m in history if m.regime == regime]
            regime_days = len(regime_data)

            if regime_days > 0:
                stats[regime] = {
                    "days": regime_days,
                    "percentage": regime_days / total_days,
                    "avg_vix": np.mean([m.vix for m in regime_data]),
                    "avg_drawdown_3m": np.mean([m.drawdown_3m for m in regime_data]),
                    "avg_sma_slope": np.mean([m.sma_200_slope for m in regime_data]),
                }
            else:
                stats[regime] = {
                    "days": 0,
                    "percentage": 0.0,
                    "avg_vix": 0.0,
                    "avg_drawdown_3m": 0.0,
                    "avg_sma_slope": 0.0,
                }

        return stats


@dataclass
class RegimePerformance:
    """レジーム別パフォーマンス"""

    regime: MarketRegime
    total_days: int
    total_return: float
    annualized_return: float
    annualized_volatility: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float  # 週次リターン > 0の割合


class RegimePerformanceAnalyzer:
    """レジーム別パフォーマンス分析"""

    def __init__(self, regime_detector: MarketRegimeDetector):
        self.regime_detector = regime_detector

    def analyze_performance(
        self,
        portfolio_returns: pd.DataFrame,  # date, return
        start_date: datetime,
        end_date: datetime,
        risk_free_rate: float = 0.04,  # 4%
    ) -> Dict[MarketRegime, RegimePerformance]:
        """
        レジーム別のパフォーマンスを分析

        Args:
            portfolio_returns: ポートフォリオリターン（DataFrame: date, return）
            start_date: 分析開始日
            end_date: 分析終了日
            risk_free_rate: 無リスク金利（年率）

        Returns:
            レジーム別パフォーマンス辞書
        """
        portfolio_returns = portfolio_returns.copy()
        portfolio_returns.set_index("date", inplace=True)
        portfolio_returns.sort_index(inplace=True)

        # レジーム履歴取得
        regime_history = self.regime_detector.get_regime_history(start_date, end_date)

        # レジーム別に分類
        regime_returns: Dict[MarketRegime, List[float]] = {regime: [] for regime in MarketRegime}

        for metrics in regime_history:
            if metrics.date in portfolio_returns.index:
                ret = portfolio_returns.loc[metrics.date, "return"]
                regime_returns[metrics.regime].append(ret)

        # パフォーマンス計算
        performance = {}

        for regime, returns in regime_returns.items():
            if not returns:
                continue

            returns_arr = np.array(returns)

            # 総リターン（複利）
            total_return = np.prod(1 + returns_arr) - 1

            # 年率リターン（週次データ想定、52週/年）
            weeks = len(returns)
            years = weeks / 52.0
            if years > 0:
                annualized_return = (1 + total_return) ** (1 / years) - 1
            else:
                annualized_return = 0.0

            # 年率ボラティリティ
            annualized_volatility = np.std(returns_arr) * np.sqrt(52)

            # シャープレシオ
            if annualized_volatility > 0:
                sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
            else:
                sharpe_ratio = 0.0

            # 最大ドローダウン
            cumulative = np.cumprod(1 + returns_arr)
            cummax = np.maximum.accumulate(cumulative)
            drawdown = (cumulative / cummax) - 1
            max_drawdown = np.min(drawdown)

            # 勝率
            win_rate = np.sum(returns_arr > 0) / len(returns_arr)

            performance[regime] = RegimePerformance(
                regime=regime,
                total_days=len(returns),
                total_return=total_return,
                annualized_return=annualized_return,
                annualized_volatility=annualized_volatility,
                sharpe_ratio=sharpe_ratio,
                max_drawdown=max_drawdown,
                win_rate=win_rate,
            )

        return performance
