"""
時系列データ管理（ルックアヘッドバイアス防止）

二重タイムスタンプ管理により、T時点の判断でT-1までのデータのみを
使用することを保証する。
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
import pandas as pd
from enum import Enum


class DataType(Enum):
    """データタイプ分類"""

    PRICE = "price"  # 株価（OHLCV）
    FUNDAMENTAL = "fundamental"  # 財務データ
    NEWS = "news"  # ニュース
    INSIDER = "insider"  # インサイダー取引
    AI_MILESTONE = "ai_milestone"  # AIマイルストーン
    TECHNICAL = "technical"  # テクニカル指標


@dataclass
class TimestampedData:
    """
    タイムスタンプ管理用データクラス

    ルックアヘッドバイアスを防ぐため、2つの時刻を厳格に管理：
    - effective_date: データが「いつの期間」のものか
    - as_of_date: データが「いつ時点で入手可能」だったか

    Example:
        # 2024-Q4決算（2024-12-31期末）が2025-02-05に発表された場合
        data = TimestampedData(
            effective_date=datetime(2024, 12, 31),
            as_of_date=datetime(2025, 2, 5),
            value={"revenue": 1000000, "eps": 2.5},
            data_type=DataType.FUNDAMENTAL
        )

        # 2025-02-04時点では利用不可
        assert not data.is_available_at(datetime(2025, 2, 4))

        # 2025-02-05以降は利用可能
        assert data.is_available_at(datetime(2025, 2, 5))
    """

    # いつの期間のデータか（例: 決算期末日、ニュース発生日）
    effective_date: datetime

    # いつ時点で入手可能だったか（例: 決算発表日、ニュース公開日）
    as_of_date: datetime

    # 実際のデータ
    value: Any

    # データタイプ
    data_type: DataType

    # メタデータ（オプション）
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """検証: as_of_date >= effective_date"""
        if self.as_of_date < self.effective_date:
            # 例外: 株価データは即日利用可能（同日OK）
            if self.data_type != DataType.PRICE:
                raise ValueError(
                    f"as_of_date ({self.as_of_date}) must be >= effective_date ({self.effective_date}). "
                    f"Data cannot be available before it exists!"
                )

    def is_available_at(self, decision_date: datetime) -> bool:
        """
        指定日時点で利用可能か判定

        Args:
            decision_date: 判断を行う日時

        Returns:
            True if データが利用可能
        """
        return decision_date >= self.as_of_date

    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "effective_date": self.effective_date.isoformat(),
            "as_of_date": self.as_of_date.isoformat(),
            "value": self.value,
            "data_type": self.data_type.value,
            "metadata": self.metadata,
        }


class TimeSeriesDataManager:
    """
    時系列データの厳格な管理

    複数のTimestampedDataを管理し、任意の時点で「利用可能なデータのみ」を
    返すことでルックアヘッドバイアスを防止。
    """

    def __init__(self):
        # ticker -> List[TimestampedData]
        self._data: Dict[str, List[TimestampedData]] = {}

        # データソース別のデフォルト遅延時間
        self._default_delays: Dict[DataType, timedelta] = {
            DataType.PRICE: timedelta(days=0),  # 株価は即日利用可能
            DataType.TECHNICAL: timedelta(days=0),  # テクニカル指標も即日
            DataType.FUNDAMENTAL: timedelta(days=1),  # 決算は翌営業日
            DataType.NEWS: timedelta(hours=1),  # ニュースは1時間遅延
            DataType.INSIDER: timedelta(days=2),  # SEC Form 4は2営業日遅延
            DataType.AI_MILESTONE: timedelta(days=0),  # マイルストーンは計画ベース
        }

    def add_data(
        self,
        ticker: str,
        effective_date: datetime,
        value: Any,
        data_type: DataType,
        as_of_date: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        データを追加

        Args:
            ticker: ティッカーシンボル
            effective_date: データの期間
            value: データ値
            data_type: データタイプ
            as_of_date: 入手可能日（省略時はeffective_date + デフォルト遅延）
            metadata: メタデータ
        """
        # as_of_dateが未指定の場合、デフォルト遅延を適用
        if as_of_date is None:
            delay = self._default_delays.get(data_type, timedelta(days=0))
            as_of_date = effective_date + delay

        # TimestampedData作成
        timestamped_data = TimestampedData(
            effective_date=effective_date,
            as_of_date=as_of_date,
            value=value,
            data_type=data_type,
            metadata=metadata or {},
        )

        # 保存
        if ticker not in self._data:
            self._data[ticker] = []

        self._data[ticker].append(timestamped_data)

    def get_available_data(
        self,
        ticker: str,
        decision_date: datetime,
        data_type: Optional[DataType] = None,
        lookback_days: Optional[int] = None,
    ) -> List[TimestampedData]:
        """
        指定日時点で利用可能なデータを取得

        Args:
            ticker: ティッカーシンボル
            decision_date: 判断を行う日時
            data_type: データタイプでフィルタ（省略時は全タイプ）
            lookback_days: 何日前までのデータを取得するか（省略時は全期間）

        Returns:
            利用可能なTimestampedDataのリスト（effective_date昇順）
        """
        if ticker not in self._data:
            return []

        # フィルタリング
        available = [
            d
            for d in self._data[ticker]
            if d.is_available_at(decision_date)
            and (data_type is None or d.data_type == data_type)
        ]

        # lookback期間フィルタ
        if lookback_days is not None:
            cutoff_date = decision_date - timedelta(days=lookback_days)
            available = [d for d in available if d.effective_date >= cutoff_date]

        # effective_dateで昇順ソート
        available.sort(key=lambda x: x.effective_date)

        return available

    def get_latest_value(
        self,
        ticker: str,
        decision_date: datetime,
        data_type: DataType,
        default: Any = None,
    ) -> Any:
        """
        最新の利用可能データの値を取得

        Args:
            ticker: ティッカーシンボル
            decision_date: 判断を行う日時
            data_type: データタイプ
            default: データが存在しない場合のデフォルト値

        Returns:
            最新データの値、存在しない場合はdefault
        """
        available = self.get_available_data(ticker, decision_date, data_type)

        if not available:
            return default

        # 最新（最後）のデータの値を返す
        return available[-1].value

    def to_dataframe(
        self,
        ticker: str,
        decision_date: datetime,
        data_type: DataType,
    ) -> pd.DataFrame:
        """
        利用可能データをDataFrameに変換

        Args:
            ticker: ティッカーシンボル
            decision_date: 判断を行う日時
            data_type: データタイプ

        Returns:
            pandas DataFrame（effective_dateをインデックス）
        """
        available = self.get_available_data(ticker, decision_date, data_type)

        if not available:
            return pd.DataFrame()

        # effective_dateをインデックス、valueをカラムとするDataFrame作成
        records = []
        for d in available:
            record = {"effective_date": d.effective_date, "as_of_date": d.as_of_date}

            # valueが辞書の場合は展開
            if isinstance(d.value, dict):
                record.update(d.value)
            else:
                record["value"] = d.value

            records.append(record)

        df = pd.DataFrame(records)
        df.set_index("effective_date", inplace=True)

        return df

    def get_tickers(self) -> List[str]:
        """管理中の全ティッカーリストを取得"""
        return list(self._data.keys())

    def clear(self) -> None:
        """全データをクリア"""
        self._data.clear()


# ヘルパー関数


def create_price_data(
    ticker: str,
    date: datetime,
    open_price: float,
    high: float,
    low: float,
    close: float,
    volume: int,
) -> TimestampedData:
    """
    株価データの作成ヘルパー

    株価は即日利用可能（effective_date = as_of_date）

    Args:
        ticker: ティッカーシンボル
        date: 日付
        open_price: 始値
        high: 高値
        low: 安値
        close: 終値
        volume: 出来高

    Returns:
        TimestampedData
    """
    return TimestampedData(
        effective_date=date,
        as_of_date=date,  # 株価は即日利用可能
        value={"open": open_price, "high": high, "low": low, "close": close, "volume": volume},
        data_type=DataType.PRICE,
        metadata={"ticker": ticker},
    )


def create_earnings_data(
    ticker: str,
    fiscal_period_end: datetime,
    announcement_date: datetime,
    earnings_data: Dict[str, Any],
) -> TimestampedData:
    """
    決算データの作成ヘルパー

    Args:
        ticker: ティッカーシンボル
        fiscal_period_end: 決算期末日
        announcement_date: 決算発表日
        earnings_data: 決算データ（revenue, eps等）

    Returns:
        TimestampedData
    """
    return TimestampedData(
        effective_date=fiscal_period_end,
        as_of_date=announcement_date,
        value=earnings_data,
        data_type=DataType.FUNDAMENTAL,
        metadata={"ticker": ticker, "fiscal_period": fiscal_period_end.strftime("%Y-Q%q")},
    )


def get_monday_timestamp(date: datetime) -> datetime:
    """
    指定日の週の月曜日を取得

    週次リバランス戦略で使用（月曜始値で判断）

    Args:
        date: 任意の日付

    Returns:
        その週の月曜日（00:00:00）
    """
    # 月曜日 = 0, 日曜日 = 6
    days_since_monday = date.weekday()
    monday = date - timedelta(days=days_since_monday)

    return monday.replace(hour=0, minute=0, second=0, microsecond=0)


def get_previous_friday(monday: datetime) -> datetime:
    """
    月曜日の前週金曜日を取得

    週次リバランス戦略で使用（金曜終値までのデータで判断）

    Args:
        monday: 月曜日

    Returns:
        前週金曜日（23:59:59）
    """
    # 月曜から3日戻ると金曜
    friday = monday - timedelta(days=3)

    return friday.replace(hour=23, minute=59, second=59, microsecond=0)
