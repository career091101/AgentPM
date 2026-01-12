"""
バックテスト用データ準備

マスターデータ読み込み、yfinanceデータ取得、TimeSeriesDataManagerへの投入を統合
"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import json

import sys
sys.path.append(str(Path(__file__).parent.parent))

from core.timestamped_data import TimeSeriesDataManager
from core.universe_manager import UniverseManager, IPOInfo
from core.market_regime import MarketRegimeDetector
from engine.cost_model import TradingCostModel, TickerCategory as CostTickerCategory
from .yfinance_loader import YFinanceLoader


class BacktestDataPreparer:
    """
    バックテスト用データ準備クラス

    マスターデータからユニバース設定、yfinanceデータ取得を一括実行
    """

    def __init__(
        self,
        master_data_path: Path,
        cache_dir: Optional[Path] = None,
    ):
        """
        Args:
            master_data_path: AI株式マスターデータ（JSON）
            cache_dir: yfinanceキャッシュディレクトリ
        """
        self.master_data_path = master_data_path
        self.cache_dir = cache_dir

        # マスターデータ読み込み
        with open(master_data_path) as f:
            self.master_data = json.load(f)

        self.stocks = self.master_data["stocks"]
        self.categories = self.master_data["categories"]

    def prepare_all(
        self,
        start_date: datetime,
        end_date: datetime,
        use_cache: bool = True,
    ) -> Tuple[TimeSeriesDataManager, UniverseManager, TradingCostModel, MarketRegimeDetector]:
        """
        バックテストに必要な全てのコンポーネントを準備

        Args:
            start_date: バックテスト開始日
            end_date: バックテスト終了日
            use_cache: yfinanceキャッシュ使用

        Returns:
            (data_manager, universe_manager, cost_model, regime_detector)
        """
        print("=" * 80)
        print("BACKTEST DATA PREPARATION")
        print("=" * 80)
        print()

        # 1. TimeSeriesDataManager初期化
        print("1️⃣  Initializing TimeSeriesDataManager...")
        data_manager = TimeSeriesDataManager()

        # 2. UniverseManager初期化
        print("2️⃣  Setting up UniverseManager...")
        universe_manager = self._setup_universe_manager()

        # 3. TradingCostModel初期化
        print("3️⃣  Configuring TradingCostModel...")
        cost_model = self._setup_cost_model()

        # 4. 株価データ取得
        print("4️⃣  Loading stock price data from yfinance...")
        tickers = [stock["ticker"] for stock in self.stocks]
        loader = YFinanceLoader(self.cache_dir)
        loader.populate_data_manager(
            data_manager, tickers, start_date, end_date, use_cache
        )

        # 5. MarketRegimeDetector初期化
        print("5️⃣  Initializing MarketRegimeDetector...")
        regime_detector = MarketRegimeDetector()

        print()
        print("✅ Data preparation complete!")
        print()
        print(f"   Stocks: {len(tickers)}")
        print(f"   Categories: {len(self.categories)}")
        print(f"   Period: {start_date.date()} to {end_date.date()}")
        print()

        return data_manager, universe_manager, cost_model, regime_detector

    def _setup_universe_manager(self) -> UniverseManager:
        """UniverseManager設定"""
        manager = UniverseManager()

        for stock in self.stocks:
            # IPO情報追加
            manager.add_ipo(
                IPOInfo(
                    ticker=stock["ticker"],
                    ipo_date=datetime.fromisoformat(stock["ipo_date"]),
                    initial_price=0.0,  # 価格は不要（データから取得）
                    exchange=stock["exchange"],
                    category=stock["category"],
                    metadata={
                        "name": stock["name"],
                        "ai_relevance": stock["ai_relevance"],
                        "weight_factor": stock["weight_factor"],
                    },
                )
            )

        print(f"   ✅ Configured {len(self.stocks)} stocks across {len(self.categories)} categories")

        return manager

    def _setup_cost_model(self) -> TradingCostModel:
        """TradingCostModel設定"""
        model = TradingCostModel()

        # 流動性分類に応じてカテゴリ設定
        for stock in self.stocks:
            ticker = stock["ticker"]
            liquidity = stock["liquidity"]

            if liquidity == "large_cap":
                model.set_ticker_category(ticker, CostTickerCategory.LARGE_CAP)
            elif liquidity == "mid_cap":
                model.set_ticker_category(ticker, CostTickerCategory.MID_CAP)
            else:  # small_cap
                model.set_ticker_category(ticker, CostTickerCategory.SMALL_CAP)

        print(f"   ✅ Configured trading costs for {len(self.stocks)} stocks")

        return model

    def get_tickers(self) -> List[str]:
        """全ティッカーリスト取得"""
        return [stock["ticker"] for stock in self.stocks]

    def get_category_tickers(self, category: str) -> List[str]:
        """カテゴリ別ティッカーリスト取得"""
        return [stock["ticker"] for stock in self.stocks if stock["category"] == category]

    def get_stock_info(self, ticker: str) -> Optional[Dict]:
        """銘柄情報取得"""
        for stock in self.stocks:
            if stock["ticker"] == ticker:
                return stock
        return None


# ヘルパー関数


def prepare_backtest_data(
    start_date: datetime,
    end_date: datetime,
    master_data_path: Optional[Path] = None,
    cache_dir: Optional[Path] = None,
) -> Tuple[TimeSeriesDataManager, UniverseManager, TradingCostModel, MarketRegimeDetector]:
    """
    バックテストデータ準備（シンプル版）

    Args:
        start_date: 開始日
        end_date: 終了日
        master_data_path: マスターデータパス（None = デフォルトパス使用）
        cache_dir: キャッシュディレクトリ

    Returns:
        (data_manager, universe_manager, cost_model, regime_detector)
    """
    # デフォルトマスターデータパス
    if master_data_path is None:
        master_data_path = Path(__file__).parent.parent / "data" / "ai_stocks_master.json"

    preparer = BacktestDataPreparer(master_data_path, cache_dir)
    return preparer.prepare_all(start_date, end_date)
