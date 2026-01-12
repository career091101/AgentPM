"""
Enhanced Multi-Factor Strategy

等ウェイトを改善したマルチファクター戦略
- モメンタムファクター
- ボラティリティ調整
- バリューエーション考慮（簡易版）
"""

from datetime import datetime, timedelta
from typing import Dict, List
import numpy as np

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from core.timestamped_data import TimeSeriesDataManager, DataType


class EnhancedMultiFactorStrategy:
    """
    マルチファクター戦略

    複数のファクターを組み合わせて最適なポートフォリオを構築
    """

    def __init__(
        self,
        data_manager: TimeSeriesDataManager,
        lookback_weeks: int = 12,  # モメンタム計算期間
        min_position: float = 0.01,  # 最小ポジション
        max_position: float = 0.15,  # 最大ポジション
    ):
        self.data_manager = data_manager
        self.lookback_weeks = lookback_weeks
        self.min_position = min_position
        self.max_position = max_position

    def __call__(
        self,
        decision_date: datetime,
        available_tickers: List[str],
    ) -> Dict[str, float]:
        """
        戦略実行

        Args:
            decision_date: 判断日
            available_tickers: 投資可能銘柄

        Returns:
            {ticker: weight}
        """
        if not available_tickers:
            return {}

        # 各銘柄のスコア計算
        scores = {}

        for ticker in available_tickers:
            score = self._calculate_ticker_score(ticker, decision_date)
            if score is not None:
                scores[ticker] = score

        if not scores:
            # スコア計算失敗時は等ウェイト
            return self._equal_weight(available_tickers)

        # スコアに基づいてウェイト配分
        return self._allocate_weights(scores)

    def _calculate_ticker_score(
        self,
        ticker: str,
        decision_date: datetime
    ) -> float:
        """
        銘柄スコア計算

        Returns:
            総合スコア（高いほど優良）
        """
        # 1. モメンタムスコア（過去リターン）
        momentum_score = self._calculate_momentum(ticker, decision_date)

        # 2. ボラティリティスコア（低ボラ = 高スコア）
        volatility_score = self._calculate_volatility_score(ticker, decision_date)

        # 3. トレンドスコア（上昇トレンド = 高スコア）
        trend_score = self._calculate_trend_score(ticker, decision_date)

        if momentum_score is None or volatility_score is None or trend_score is None:
            return None

        # 重み付け合成
        total_score = (
            0.4 * momentum_score +     # モメンタム40%
            0.3 * volatility_score +   # ボラティリティ30%
            0.3 * trend_score          # トレンド30%
        )

        return total_score

    def _calculate_momentum(
        self,
        ticker: str,
        decision_date: datetime
    ) -> float:
        """モメンタムスコア計算（過去N週リターン）"""
        start_date = decision_date - timedelta(weeks=self.lookback_weeks)

        # 開始価格
        start_price = self._get_price(ticker, start_date, "close")
        # 終了価格
        end_price = self._get_price(ticker, decision_date, "close")

        if start_price is None or end_price is None or start_price <= 0:
            return None

        # リターン計算
        returns = (end_price / start_price) - 1

        # 正規化（-1 to 1の範囲に）
        # 仮定: ±50%で±1とする
        normalized = np.tanh(returns * 2)

        return normalized

    def _calculate_volatility_score(
        self,
        ticker: str,
        decision_date: datetime
    ) -> float:
        """ボラティリティスコア（低ボラ = 高スコア）"""
        # 過去N週の週次リターンを取得
        returns = []

        for i in range(self.lookback_weeks):
            week_start = decision_date - timedelta(weeks=i+1)
            week_end = decision_date - timedelta(weeks=i)

            start_price = self._get_price(ticker, week_start, "close")
            end_price = self._get_price(ticker, week_end, "close")

            if start_price and end_price and start_price > 0:
                ret = (end_price / start_price) - 1
                returns.append(ret)

        if len(returns) < 4:  # 最低4週必要
            return None

        # ボラティリティ = 標準偏差
        volatility = np.std(returns)

        # 低ボラティリティ = 高スコア
        # 仮定: vol=0.05 (5%) で中間スコア
        normalized = 1.0 / (1.0 + volatility * 10)

        return normalized

    def _calculate_trend_score(
        self,
        ticker: str,
        decision_date: datetime
    ) -> float:
        """トレンドスコア（短期MA > 長期MA = 上昇トレンド）"""
        # 短期MA（4週）
        short_prices = []
        for i in range(4):
            date = decision_date - timedelta(weeks=i)
            price = self._get_price(ticker, date, "close")
            if price:
                short_prices.append(price)

        # 長期MA（12週）
        long_prices = []
        for i in range(12):
            date = decision_date - timedelta(weeks=i)
            price = self._get_price(ticker, date, "close")
            if price:
                long_prices.append(price)

        if len(short_prices) < 3 or len(long_prices) < 8:
            return None

        short_ma = np.mean(short_prices)
        long_ma = np.mean(long_prices)

        # 短期MA / 長期MA - 1
        trend_ratio = (short_ma / long_ma) - 1

        # 正規化
        normalized = np.tanh(trend_ratio * 5)

        return normalized

    def _get_price(
        self,
        ticker: str,
        date: datetime,
        price_type: str = "close",
    ) -> float:
        """指定日の株価取得"""
        price_data = self.data_manager.get_latest_value(ticker, date, DataType.PRICE)

        if price_data and isinstance(price_data, dict):
            return price_data.get(price_type)

        return None

    def _allocate_weights(self, scores: Dict[str, float]) -> Dict[str, float]:
        """
        スコアに基づいてウェイト配分

        - 上位銘柄に高ウェイト
        - 下位銘柄は除外または低ウェイト
        """
        # スコアでソート（降順）
        sorted_tickers = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # 上位70%のみ投資
        cutoff_index = int(len(sorted_tickers) * 0.7)
        selected_tickers = sorted_tickers[:max(cutoff_index, 10)]  # 最低10銘柄

        # スコアを0-1に正規化（最低スコアが0、最高スコアが1）
        min_score = min(s for _, s in selected_tickers)
        max_score = max(s for _, s in selected_tickers)

        if max_score - min_score < 0.01:
            # スコア差が小さい場合は等ウェイト
            return self._equal_weight([t for t, _ in selected_tickers])

        # 正規化スコアに基づくウェイト
        normalized_scores = {}
        for ticker, score in selected_tickers:
            norm_score = (score - min_score) / (max_score - min_score)
            # 最低0.5、最高1.5の範囲に変換（スコアが低くても完全に0にはしない）
            normalized_scores[ticker] = 0.5 + norm_score

        # ウェイト総和を1に正規化
        total_weight = sum(normalized_scores.values())
        weights = {
            ticker: weight / total_weight
            for ticker, weight in normalized_scores.items()
        }

        # 最大・最小制約適用
        weights = self._apply_constraints(weights)

        return weights

    def _apply_constraints(self, weights: Dict[str, float]) -> Dict[str, float]:
        """最大・最小ポジション制約適用"""
        # 最大制約
        for ticker in weights:
            if weights[ticker] > self.max_position:
                weights[ticker] = self.max_position

        # 最小制約（小さすぎるポジションは除外）
        weights = {
            ticker: weight
            for ticker, weight in weights.items()
            if weight >= self.min_position
        }

        # 再正規化
        total_weight = sum(weights.values())
        if total_weight > 0:
            weights = {
                ticker: weight / total_weight
                for ticker, weight in weights.items()
            }

        return weights

    def _equal_weight(self, tickers: List[str]) -> Dict[str, float]:
        """等ウェイト（フォールバック）"""
        if not tickers:
            return {}

        weight = 1.0 / len(tickers)
        return {ticker: weight for ticker in tickers}


# ファクトリー関数

def create_enhanced_strategy(
    data_manager: TimeSeriesDataManager,
    lookback_weeks: int = 12,
) -> EnhancedMultiFactorStrategy:
    """
    Enhanced Multi-Factor Strategy作成

    Args:
        data_manager: TimeSeriesDataManager
        lookback_weeks: モメンタム計算期間

    Returns:
        EnhancedMultiFactorStrategy callable
    """
    return EnhancedMultiFactorStrategy(
        data_manager=data_manager,
        lookback_weeks=lookback_weeks,
    )
