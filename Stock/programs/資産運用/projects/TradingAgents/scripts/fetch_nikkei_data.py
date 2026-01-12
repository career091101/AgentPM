#!/usr/bin/env python3
"""
日経平均先物データ収集スクリプト
Yahoo Finance USから5年分のOHLCVデータを取得
"""

import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta

def fetch_nikkei_data():
    """日経平均（^N225）の5年分データを取得"""

    # 日経平均のティッカーシンボル
    ticker = "^N225"

    # 期間設定（5年前 ~ 今日）
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)

    print(f"📊 日経平均先物データ取得開始")
    print(f"   ティッカー: {ticker}")
    print(f"   期間: {start_date.date()} ~ {end_date.date()}")
    print()

    # データ取得
    try:
        nikkei = yf.Ticker(ticker)
        hist = nikkei.history(start=start_date, end=end_date, interval='1d')

        if hist.empty:
            print("❌ データ取得失敗: 空のデータフレーム")
            return None

        print(f"✅ データ取得成功: {len(hist)} データポイント")

        # データフレームをJSON形式に変換
        historical_data = []
        for date, row in hist.iterrows():
            historical_data.append({
                "date": date.strftime("%Y-%m-%d"),
                "open": round(float(row['Open']), 2),
                "high": round(float(row['High']), 2),
                "low": round(float(row['Low']), 2),
                "close": round(float(row['Close']), 2),
                "volume": int(row['Volume'])
            })

        # データ完全性チェック
        expected_points = 5 * 250  # 5年 × 約250営業日
        actual_points = len(historical_data)
        completeness = (actual_points / expected_points) * 100
        missing_points = expected_points - actual_points

        # 現在価格情報
        current_info = nikkei.info
        current_price = {
            "price": round(float(hist['Close'].iloc[-1]), 2),
            "high": round(float(hist['High'].iloc[-1]), 2),
            "low": round(float(hist['Low'].iloc[-1]), 2),
            "open": round(float(hist['Open'].iloc[-1]), 2),
            "volume": int(hist['Volume'].iloc[-1]),
            "timestamp": datetime.now().isoformat()
        }

        # 変動率計算
        if len(hist) >= 2:
            prev_close = float(hist['Close'].iloc[-2])
            curr_close = float(hist['Close'].iloc[-1])
            change_pct = round(((curr_close - prev_close) / prev_close) * 100, 2)
            current_price["change_pct"] = change_pct
        else:
            current_price["change_pct"] = 0.0

        # 最終JSON構造
        result = {
            "collection_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "success" if completeness >= 95 else ("warning" if completeness >= 90 else "failure"),
            "current_price": current_price,
            "historical_data": historical_data,
            "data_quality": {
                "completeness": round(completeness, 2),
                "expected_points": expected_points,
                "actual_points": actual_points,
                "missing_points": missing_points,
                "date_range": {
                    "start": historical_data[0]["date"],
                    "end": historical_data[-1]["date"]
                }
            },
            "data_sources": {
                "current_price": "Yahoo Finance US (yfinance)",
                "historical_data": "Yahoo Finance US (yfinance)"
            }
        }

        # データ品質レポート
        print()
        print("📈 データ品質レポート")
        print(f"   データ完全性: {completeness:.2f}%")
        print(f"   期待ポイント数: {expected_points}")
        print(f"   実際のポイント数: {actual_points}")
        print(f"   欠損ポイント数: {missing_points}")
        print(f"   日付範囲: {historical_data[0]['date']} ~ {historical_data[-1]['date']}")
        print(f"   ステータス: {result['status']}")
        print()

        # 現在価格サマリー
        print("💹 現在価格情報")
        print(f"   終値: {current_price['price']:,.2f}円")
        print(f"   変動率: {current_price['change_pct']:+.2f}%")
        print(f"   高値: {current_price['high']:,.2f}円")
        print(f"   安値: {current_price['low']:,.2f}円")
        print(f"   出来高: {current_price['volume']:,}")
        print()

        return result

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        return None

if __name__ == "__main__":
    # データ取得実行
    data = fetch_nikkei_data()

    if data:
        # JSONファイルとして保存
        output_dir = "data/sources/2026-01-02"
        import os
        os.makedirs(output_dir, exist_ok=True)

        output_file = f"{output_dir}/market_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ データ保存完了: {output_file}")
        print(f"   ファイルサイズ: {os.path.getsize(output_file):,} bytes")
    else:
        print("❌ データ取得失敗")
        exit(1)
