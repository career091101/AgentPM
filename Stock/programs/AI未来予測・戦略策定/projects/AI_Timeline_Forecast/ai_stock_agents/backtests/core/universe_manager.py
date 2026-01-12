"""
投資ユニバース管理（サバイバーシップバイアス防止）

IPO、上場廃止、M&A等のイベントを管理し、各時点で「実際に投資可能だった
銘柄のみ」を返すことでサバイバーシップバイアスを防止。
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Set
from enum import Enum
import json
from pathlib import Path


class DelistingReason(Enum):
    """上場廃止理由"""

    BANKRUPTCY = "bankruptcy"  # 倒産
    MERGER = "merger"  # 合併
    ACQUISITION = "acquisition"  # 買収
    GOING_PRIVATE = "going_private"  # 非公開化
    VOLUNTARY = "voluntary"  # 自主的上場廃止
    REGULATORY = "regulatory"  # 規制違反
    OTHER = "other"


@dataclass
class IPOInfo:
    """IPO情報"""

    ticker: str
    ipo_date: datetime
    initial_price: float
    exchange: str  # "NASDAQ", "NYSE"
    category: str  # "Compute", "Frontier Labs", etc.
    metadata: Dict[str, any] = field(default_factory=dict)


@dataclass
class DelistingInfo:
    """上場廃止情報"""

    ticker: str
    delisting_date: datetime
    reason: DelistingReason
    final_price: float  # 最終取引価格（損失計算用）
    acquirer: Optional[str] = None  # 買収企業（M&Aの場合）
    metadata: Dict[str, any] = field(default_factory=dict)


class UniverseManager:
    """
    投資ユニバース管理

    時系列でのユニバース構成変化を管理し、サバイバーシップバイアスを防止。
    """

    def __init__(self, data_dir: Optional[Path] = None):
        """
        Args:
            data_dir: データディレクトリ（JSONファイル保存先）
        """
        self.data_dir = data_dir

        # IPO情報: ticker -> IPOInfo
        self._ipo_info: Dict[str, IPOInfo] = {}

        # 上場廃止情報: ticker -> DelistingInfo
        self._delisting_info: Dict[str, DelistingInfo] = {}

        # カテゴリ別ティッカー
        self._categories: Dict[str, Set[str]] = {}

    def add_ipo(self, ipo_info: IPOInfo) -> None:
        """IPO情報を追加"""
        self._ipo_info[ipo_info.ticker] = ipo_info

        # カテゴリ別管理
        if ipo_info.category not in self._categories:
            self._categories[ipo_info.category] = set()
        self._categories[ipo_info.category].add(ipo_info.ticker)

    def add_delisting(self, delisting_info: DelistingInfo) -> None:
        """上場廃止情報を追加"""
        self._delisting_info[delisting_info.ticker] = delisting_info

    def is_available(self, ticker: str, as_of_date: datetime) -> bool:
        """
        指定日時点で投資可能か判定

        Args:
            ticker: ティッカーシンボル
            as_of_date: 判定日

        Returns:
            True if 投資可能（上場済み かつ 未廃止）
        """
        # IPO前は不可
        if ticker in self._ipo_info:
            if as_of_date < self._ipo_info[ticker].ipo_date:
                return False
        else:
            # IPO情報がない場合は常に利用可能と仮定（データ欠損対策）
            pass

        # 上場廃止後は不可
        if ticker in self._delisting_info:
            if as_of_date >= self._delisting_info[ticker].delisting_date:
                return False

        return True

    def get_available_tickers(
        self,
        as_of_date: datetime,
        category: Optional[str] = None,
    ) -> List[str]:
        """
        指定日時点で投資可能な銘柄リストを取得

        Args:
            as_of_date: 判定日
            category: カテゴリフィルタ（省略時は全カテゴリ）

        Returns:
            投資可能なティッカーリスト
        """
        # カテゴリフィルタ
        if category:
            candidates = self._categories.get(category, set())
        else:
            # 全ティッカー
            candidates = set(self._ipo_info.keys())

        # 利用可能性チェック
        available = [ticker for ticker in candidates if self.is_available(ticker, as_of_date)]

        return sorted(available)

    def get_ipo_date(self, ticker: str) -> Optional[datetime]:
        """IPO日を取得"""
        if ticker in self._ipo_info:
            return self._ipo_info[ticker].ipo_date
        return None

    def get_delisting_info(self, ticker: str) -> Optional[DelistingInfo]:
        """上場廃止情報を取得"""
        return self._delisting_info.get(ticker)

    def get_categories(self) -> List[str]:
        """全カテゴリリストを取得"""
        return sorted(self._categories.keys())

    def get_category(self, ticker: str) -> Optional[str]:
        """ティッカーのカテゴリを取得"""
        if ticker in self._ipo_info:
            return self._ipo_info[ticker].category
        return None

    def save_to_json(self) -> None:
        """データをJSONファイルに保存"""
        if self.data_dir is None:
            raise ValueError("data_dir not specified")

        self.data_dir.mkdir(parents=True, exist_ok=True)

        # IPO情報保存
        ipo_data = {
            ticker: {
                "ipo_date": info.ipo_date.isoformat(),
                "initial_price": info.initial_price,
                "exchange": info.exchange,
                "category": info.category,
                "metadata": info.metadata,
            }
            for ticker, info in self._ipo_info.items()
        }

        with open(self.data_dir / "ipo_info.json", "w") as f:
            json.dump(ipo_data, f, indent=2)

        # 上場廃止情報保存
        delisting_data = {
            ticker: {
                "delisting_date": info.delisting_date.isoformat(),
                "reason": info.reason.value,
                "final_price": info.final_price,
                "acquirer": info.acquirer,
                "metadata": info.metadata,
            }
            for ticker, info in self._delisting_info.items()
        }

        with open(self.data_dir / "delisting_info.json", "w") as f:
            json.dump(delisting_data, f, indent=2)

    def load_from_json(self) -> None:
        """JSONファイルからデータを読み込み"""
        if self.data_dir is None:
            raise ValueError("data_dir not specified")

        # IPO情報読み込み
        ipo_file = self.data_dir / "ipo_info.json"
        if ipo_file.exists():
            with open(ipo_file) as f:
                ipo_data = json.load(f)

            for ticker, data in ipo_data.items():
                self.add_ipo(
                    IPOInfo(
                        ticker=ticker,
                        ipo_date=datetime.fromisoformat(data["ipo_date"]),
                        initial_price=data["initial_price"],
                        exchange=data["exchange"],
                        category=data["category"],
                        metadata=data.get("metadata", {}),
                    )
                )

        # 上場廃止情報読み込み
        delisting_file = self.data_dir / "delisting_info.json"
        if delisting_file.exists():
            with open(delisting_file) as f:
                delisting_data = json.load(f)

            for ticker, data in delisting_data.items():
                self.add_delisting(
                    DelistingInfo(
                        ticker=ticker,
                        delisting_date=datetime.fromisoformat(data["delisting_date"]),
                        reason=DelistingReason(data["reason"]),
                        final_price=data["final_price"],
                        acquirer=data.get("acquirer"),
                        metadata=data.get("metadata", {}),
                    )
                )


# ヘルパー関数


def create_ai_stock_universe() -> UniverseManager:
    """
    AI株式46社のユニバースを作成

    AI Timeline Forecastプロジェクトで管理する46社の
    IPO情報を設定。
    """
    manager = UniverseManager()

    # AI株式46社（主要企業のみ例示、実際は全46社登録）
    ai_stocks = [
        # Compute (半導体・ハードウェア)
        {"ticker": "NVDA", "ipo_date": "1999-01-22", "price": 12.0, "exchange": "NASDAQ", "category": "Compute"},
        {"ticker": "AMD", "ipo_date": "1979-09-19", "price": 18.0, "exchange": "NASDAQ", "category": "Compute"},
        {"ticker": "AVGO", "ipo_date": "2009-08-06", "price": 21.0, "exchange": "NASDAQ", "category": "Compute"},
        # Frontier Labs
        {"ticker": "GOOGL", "ipo_date": "2004-08-19", "price": 85.0, "exchange": "NASDAQ", "category": "Frontier Labs"},
        {"ticker": "MSFT", "ipo_date": "1986-03-13", "price": 21.0, "exchange": "NASDAQ", "category": "Frontier Labs"},
        {"ticker": "META", "ipo_date": "2012-05-18", "price": 38.0, "exchange": "NASDAQ", "category": "Frontier Labs"},
        # Cloud Infrastructure
        {"ticker": "AMZN", "ipo_date": "1997-05-15", "price": 18.0, "exchange": "NASDAQ", "category": "Cloud"},
        {"ticker": "CRM", "ipo_date": "2004-06-23", "price": 11.0, "exchange": "NYSE", "category": "Cloud"},
        # AI Applications
        {"ticker": "ORCL", "ipo_date": "1986-03-12", "price": 15.0, "exchange": "NYSE", "category": "Enterprise AI"},
        {"ticker": "ADBE", "ipo_date": "1986-08-20", "price": 3.5, "exchange": "NASDAQ", "category": "Creative AI"},
        # Emerging AI (IPO近年)
        {"ticker": "PLTR", "ipo_date": "2020-09-30", "price": 10.0, "exchange": "NYSE", "category": "Enterprise AI"},
        {"ticker": "SNOW", "ipo_date": "2020-09-16", "price": 120.0, "exchange": "NYSE", "category": "Data Platform"},
        # ... 残り34社も同様に追加
    ]

    for stock in ai_stocks:
        manager.add_ipo(
            IPOInfo(
                ticker=stock["ticker"],
                ipo_date=datetime.fromisoformat(stock["ipo_date"]),
                initial_price=stock["price"],
                exchange=stock["exchange"],
                category=stock["category"],
            )
        )

    return manager


def add_example_delistings(manager: UniverseManager) -> None:
    """
    上場廃止例を追加（テスト用）

    実際のAI関連企業で2020-2024期間に上場廃止は少ないが、
    将来的な対応のための実装例。
    """
    # 例: 架空のAI企業が2023年に買収された
    manager.add_delisting(
        DelistingInfo(
            ticker="FICTIVE",
            delisting_date=datetime(2023, 6, 15),
            reason=DelistingReason.ACQUISITION,
            final_price=85.5,
            acquirer="GOOGL",
            metadata={"acquisition_premium": 1.35},  # 35%プレミアム
        )
    )
