#!/usr/bin/env python3
"""
モックデータ生成スクリプト

yfinanceが使えない環境でのテスト用に、サンプルデータを生成します。
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

def generate_mock_nikkei_data(start_date: str, end_date: str, output_path: str):
    """
    模擬的な日経225データを生成

    Args:
        start_date: 開始日 (YYYY-MM-DD)
        end_date: 終了日 (YYYY-MM-DD)
        output_path: 出力ファイルパス
    """
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    # 営業日のみ生成
    dates = pd.date_range(start, end, freq='B')  # B = Business days

    # 基準価格: 40000円付近でランダムウォーク
    np.random.seed(42)  # 再現性のため
    base_price = 40000
    returns = np.random.randn(len(dates)) * 0.015  # 日次リターン1.5%標準偏差
    price_series = base_price * np.exp(returns.cumsum())

    # OHLCV データ生成
    data = []
    for i, date in enumerate(dates):
        close = price_series[i]
        open_price = close * (1 + np.random.randn() * 0.005)
        high = max(open_price, close) * (1 + abs(np.random.randn()) * 0.01)
        low = min(open_price, close) * (1 - abs(np.random.randn()) * 0.01)
        volume = int(np.random.uniform(100000, 500000))

        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'open': round(open_price, 2),
            'high': round(high, 2),
            'low': round(low, 2),
            'close': round(close, 2),
            'volume': volume
        })

    df = pd.DataFrame(data)

    # 保存
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)

    print(f"✅ モックデータ生成完了")
    print(f"  期間: {start_date} 〜 {end_date}")
    print(f"  データ数: {len(df)}日分")
    print(f"  保存先: {output_path}")

    return df


if __name__ == "__main__":
    # 2020年から2024年末までのデータ生成
    project_root = Path(__file__).parent.parent
    cache_dir = project_root / "data" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    output_path = cache_dir / "N225_20200101_20241231.csv"

    generate_mock_nikkei_data(
        start_date="2020-01-01",
        end_date="2024-12-31",
        output_path=str(output_path)
    )
