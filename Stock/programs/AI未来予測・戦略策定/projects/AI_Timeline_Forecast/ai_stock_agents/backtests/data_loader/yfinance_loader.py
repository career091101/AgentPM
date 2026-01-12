"""
YFinance データローダー

yfinanceから株価データを取得し、TimeSeriesDataManagerに格納
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
import yfinance as yf
from pathlib import Path
import pickle
from tqdm import tqdm

import sys
sys.path.append(str(Path(__file__).parent.parent))

from core.timestamped_data import (
    TimeSeriesDataManager,
    DataType,
    create_price_data,
)


class YFinanceLoader:
    """
    YFinance データローダー

    株価データを取得し、キャッシュ機能も提供
    """

    def __init__(self, cache_dir: Optional[Path] = None):
        """
        Args:
            cache_dir: キャッシュディレクトリ（None = キャッシュ無効）
        """
        self.cache_dir = cache_dir
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)

    def load_stock_data(
        self,
        ticker: str,
        start_date: datetime,
        end_date: datetime,
        use_cache: bool = True,
    ) -> pd.DataFrame:
        """
        株価データ取得

        Args:
            ticker: ティッカーシンボル
            start_date: 開始日
            end_date: 終了日
            use_cache: キャッシュ使用

        Returns:
            DataFrame (date, open, high, low, close, volume)
        """
        # キャッシュチェック
        if use_cache and self.cache_dir:
            cache_file = self._get_cache_path(ticker, start_date, end_date)
            if cache_file.exists():
                with open(cache_file, "rb") as f:
                    return pickle.load(f)

        # yfinanceから取得
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(
                start=start_date.strftime("%Y-%m-%d"),
                end=(end_date + timedelta(days=1)).strftime("%Y-%m-%d"),  # 終了日含む
                interval="1d",
            )

            if df.empty:
                print(f"⚠️  No data for {ticker}")
                return pd.DataFrame()

            # カラム名を小文字化
            df = df.reset_index()
            df.columns = [col.lower() for col in df.columns]

            # タイムゾーンを除去（offset-aware → offset-naive）
            if 'date' in df.columns and hasattr(df['date'].dtype, 'tz') and df['date'].dtype.tz is not None:
                df['date'] = df['date'].dt.tz_localize(None)

            # 必要なカラムのみ抽出
            df = df[["date", "open", "high", "low", "close", "volume"]]

            # キャッシュ保存
            if use_cache and self.cache_dir:
                with open(cache_file, "wb") as f:
                    pickle.dump(df, f)

            return df

        except Exception as e:
            print(f"❌ Error loading {ticker}: {e}")
            return pd.DataFrame()

    def load_multiple_stocks(
        self,
        tickers: List[str],
        start_date: datetime,
        end_date: datetime,
        use_cache: bool = True,
    ) -> Dict[str, pd.DataFrame]:
        """
        複数銘柄の株価データ取得

        Args:
            tickers: ティッカーリスト
            start_date: 開始日
            end_date: 終了日
            use_cache: キャッシュ使用

        Returns:
            {ticker: DataFrame} の辞書
        """
        data = {}

        for ticker in tqdm(tickers, desc="Loading stock data"):
            df = self.load_stock_data(ticker, start_date, end_date, use_cache)
            if not df.empty:
                data[ticker] = df

        return data

    def populate_data_manager(
        self,
        data_manager: TimeSeriesDataManager,
        tickers: List[str],
        start_date: datetime,
        end_date: datetime,
        use_cache: bool = True,
    ) -> None:
        """
        TimeSeriesDataManagerにデータを投入

        Args:
            data_manager: TimeSeriesDataManager
            tickers: ティッカーリスト
            start_date: 開始日
            end_date: 終了日
            use_cache: キャッシュ使用
        """
        stock_data = self.load_multiple_stocks(tickers, start_date, end_date, use_cache)

        total_records = 0

        for ticker, df in stock_data.items():
            for _, row in df.iterrows():
                # タイムゾーンを除去してdatetimeに変換
                date_val = row["date"]
                if hasattr(date_val, 'tz_localize'):
                    date_val = date_val.tz_localize(None) if date_val.tz is not None else date_val
                date_dt = date_val.to_pydatetime() if hasattr(date_val, 'to_pydatetime') else date_val

                # 株価は即日利用可能（effective_date = as_of_date）
                data_manager.add_data(
                    ticker=ticker,
                    effective_date=date_dt,
                    value={
                        "open": row["open"],
                        "high": row["high"],
                        "low": row["low"],
                        "close": row["close"],
                        "volume": row["volume"],
                    },
                    data_type=DataType.PRICE,
                    as_of_date=date_dt,
                    metadata={"ticker": ticker},
                )
                total_records += 1

        print(f"✅ Loaded {total_records:,} price records for {len(stock_data)} stocks")

    def _get_cache_path(
        self, ticker: str, start_date: datetime, end_date: datetime
    ) -> Path:
        """キャッシュファイルパス生成"""
        filename = f"{ticker}_{start_date.date()}_{end_date.date()}.pkl"
        return self.cache_dir / filename


# ヘルパー関数


def load_stock_data(
    ticker: str,
    start_date: datetime,
    end_date: datetime,
    cache_dir: Optional[Path] = None,
) -> pd.DataFrame:
    """
    株価データ取得（シンプル版）

    Args:
        ticker: ティッカーシンボル
        start_date: 開始日
        end_date: 終了日
        cache_dir: キャッシュディレクトリ

    Returns:
        DataFrame
    """
    loader = YFinanceLoader(cache_dir)
    return loader.load_stock_data(ticker, start_date, end_date)


def load_benchmark_data(
    benchmark: str,
    start_date: datetime,
    end_date: datetime,
    cache_dir: Optional[Path] = None,
) -> pd.DataFrame:
    """
    ベンチマーク（SPY等）データ取得

    Args:
        benchmark: ベンチマークティッカー（"SPY", "QQQ"等）
        start_date: 開始日
        end_date: 終了日
        cache_dir: キャッシュディレクトリ

    Returns:
        DataFrame (date, open, high, low, close, volume)
    """
    return load_stock_data(benchmark, start_date, end_date, cache_dir)


def calculate_benchmark_returns(
    benchmark_data: pd.DataFrame, frequency: str = "weekly"
) -> pd.DataFrame:
    """
    ベンチマークリターン計算

    Args:
        benchmark_data: ベンチマークデータ（DataFrame: date, close）
        frequency: 頻度（"daily", "weekly", "monthly"）

    Returns:
        DataFrame (date, return)
    """
    df = benchmark_data.copy()
    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)

    # リサンプル
    if frequency == "weekly":
        # 週次（月曜始値→金曜終値）
        df_resampled = df["close"].resample("W-FRI").last()
    elif frequency == "monthly":
        df_resampled = df["close"].resample("M").last()
    else:  # daily
        df_resampled = df["close"]

    # リターン計算
    returns = df_resampled.pct_change().dropna()

    return pd.DataFrame({"date": returns.index, "return": returns.values})
