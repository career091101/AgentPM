"""
取引コストモデル（Trading Cost Model）

手数料、スプレッド、スリッページを考慮したリアリスティックなコスト計算
"""

from dataclasses import dataclass
from typing import Dict
from enum import Enum


class TickerCategory(Enum):
    """銘柄カテゴリ（流動性分類）"""

    LARGE_CAP = "large_cap"  # 大型株（NVDA, GOOGL等）
    MID_CAP = "mid_cap"  # 中型株（PLTR等）
    SMALL_CAP = "small_cap"  # 小型株


@dataclass
class RebalanceCost:
    """リバランスコスト詳細"""

    ticker: str
    trade_value: float  # 取引金額（ドル）
    commission: float  # 手数料
    spread_cost: float  # スプレッドコスト
    slippage_cost: float  # スリッページコスト
    total_cost: float  # 総コスト

    def to_dict(self) -> Dict[str, float]:
        return {
            "ticker": self.ticker,
            "trade_value": self.trade_value,
            "commission": self.commission,
            "spread_cost": self.spread_cost,
            "slippage_cost": self.slippage_cost,
            "total_cost": self.total_cost,
        }


class TradingCostModel:
    """
    取引コストモデル

    米国株取引の現実的なコストを計算。
    """

    def __init__(
        self,
        commission_per_trade: float = 0.0,  # Interactive Brokers等は無料
        spread_bps: Dict[TickerCategory, float] = None,
        slippage_bps: Dict[str, float] = None,  # オーダーサイズ別
    ):
        """
        Args:
            commission_per_trade: 1取引あたり手数料（ドル）
            spread_bps: ビッド・アスクスプレッド（ベーシスポイント）
            slippage_bps: スリッページ（ベーシスポイント）
        """
        self.commission_per_trade = commission_per_trade

        # デフォルトスプレッド（bps）
        self.spread_bps = spread_bps or {
            TickerCategory.LARGE_CAP: 2.0,  # 0.02%
            TickerCategory.MID_CAP: 5.0,  # 0.05%
            TickerCategory.SMALL_CAP: 10.0,  # 0.10%
        }

        # デフォルトスリッページ（bps）
        self.slippage_bps = slippage_bps or {
            "small_order": 1.0,  # $10K未満 (0.01%)
            "medium_order": 3.0,  # $10K-$100K (0.03%)
            "large_order": 8.0,  # $100K以上 (0.08%)
        }

        # ティッカー別カテゴリ（実際は外部データで管理）
        self._ticker_categories: Dict[str, TickerCategory] = {}

    def set_ticker_category(self, ticker: str, category: TickerCategory) -> None:
        """ティッカーのカテゴリを設定"""
        self._ticker_categories[ticker] = category

    def get_ticker_category(self, ticker: str) -> TickerCategory:
        """ティッカーのカテゴリを取得（デフォルトはLARGE_CAP）"""
        return self._ticker_categories.get(ticker, TickerCategory.LARGE_CAP)

    def calculate_rebalance_cost(
        self,
        current_portfolio: Dict[str, float],  # ticker -> weight
        target_portfolio: Dict[str, float],  # ticker -> weight
        portfolio_value: float,  # ポートフォリオ総額（ドル）
        min_trade_threshold: float = 0.001,  # 最小取引閾値（0.1%）
    ) -> Dict[str, RebalanceCost]:
        """
        リバランスコスト計算

        Args:
            current_portfolio: 現在のポートフォリオウェイト
            target_portfolio: 目標ポートフォリオウェイト
            portfolio_value: ポートフォリオ総額
            min_trade_threshold: 最小取引閾値（これ以下のウェイト変動は無視）

        Returns:
            ticker -> RebalanceCost の辞書
        """
        costs = {}

        # 全ティッカー（現在 + 目標）
        all_tickers = set(current_portfolio.keys()) | set(target_portfolio.keys())

        for ticker in all_tickers:
            current_weight = current_portfolio.get(ticker, 0.0)
            target_weight = target_portfolio.get(ticker, 0.0)

            # ウェイト変動量
            weight_change = abs(target_weight - current_weight)

            # 最小閾値以下は取引しない
            if weight_change < min_trade_threshold:
                continue

            # 取引金額
            trade_value = weight_change * portfolio_value

            # 手数料
            commission = self.commission_per_trade if trade_value > 0 else 0.0

            # スプレッドコスト
            category = self.get_ticker_category(ticker)
            spread_bps = self.spread_bps[category]
            spread_cost = trade_value * (spread_bps / 10000)

            # スリッページコスト
            slippage_bps = self._get_slippage_bps(trade_value)
            slippage_cost = trade_value * (slippage_bps / 10000)

            # 総コスト
            total_cost = commission + spread_cost + slippage_cost

            costs[ticker] = RebalanceCost(
                ticker=ticker,
                trade_value=trade_value,
                commission=commission,
                spread_cost=spread_cost,
                slippage_cost=slippage_cost,
                total_cost=total_cost,
            )

        return costs

    def _get_slippage_bps(self, trade_value: float) -> float:
        """取引金額に応じたスリッページ計算"""
        if trade_value < 10000:
            return self.slippage_bps["small_order"]
        elif trade_value < 100000:
            return self.slippage_bps["medium_order"]
        else:
            return self.slippage_bps["large_order"]

    def calculate_total_cost(
        self,
        costs: Dict[str, RebalanceCost],
    ) -> float:
        """総リバランスコスト計算"""
        return sum(cost.total_cost for cost in costs.values())

    def calculate_cost_as_percentage(
        self,
        costs: Dict[str, RebalanceCost],
        portfolio_value: float,
    ) -> float:
        """
        コストをポートフォリオ価値の割合として計算

        Returns:
            コスト割合（例: 0.0015 = 0.15%）
        """
        total_cost = self.calculate_total_cost(costs)
        return total_cost / portfolio_value if portfolio_value > 0 else 0.0


# ヘルパー関数


def create_ai_stock_cost_model() -> TradingCostModel:
    """
    AI株式46社用のコストモデル作成

    Returns:
        TradingCostModel（ティッカーカテゴリ設定済み）
    """
    model = TradingCostModel()

    # 大型株（流動性高）
    large_caps = [
        "NVDA", "AMD", "AVGO", "GOOGL", "MSFT", "META", "AMZN",
        "CRM", "ORCL", "ADBE", "INTC", "QCOM", "TXN", "AMAT",
        "ASML", "TSM", "MU", "NXPI"
    ]

    for ticker in large_caps:
        model.set_ticker_category(ticker, TickerCategory.LARGE_CAP)

    # 中型株
    mid_caps = [
        "PLTR", "SNOW", "NOW", "DDOG", "NET", "TEAM", "ZS",
        "CRWD", "PANW", "FTNT", "MNDY", "PATH", "AI"
    ]

    for ticker in mid_caps:
        model.set_ticker_category(ticker, TickerCategory.MID_CAP)

    # 小型株（流動性低）
    small_caps = [
        "SOUN", "BBAI", "BABA", "C3.AI", "SMCI"
    ]

    for ticker in small_caps:
        model.set_ticker_category(ticker, TickerCategory.SMALL_CAP)

    return model
