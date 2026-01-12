#!/usr/bin/env python3
"""
Instagram Insights データCSV保存スクリプト (Agent1)
スクリーンショットから抽出したデータをCSVに保存
"""

import csv
from datetime import datetime
from pathlib import Path

# データ設定
DATA = {
    "期間": "過去90日間",
    "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "総ビュー数": 7021,  # 閲覧数（リーチ）
    "総インタラクション数": 12,
    "プロフィールアクティビティ": 191,
    "フォロワー数": 283,
    "データソース": "並列実行Agent1"
}

# 保存先パス
CSV_PATH = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/Instagram/instagram_summary_parallel_agent1.csv"

def save_to_csv():
    """データをCSVに保存"""
    print("Instagram Insights データをCSVに保存します...")

    # ディレクトリ作成
    Path(CSV_PATH).parent.mkdir(parents=True, exist_ok=True)

    # CSV書き込み
    with open(CSV_PATH, mode='w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=DATA.keys())
        writer.writeheader()
        writer.writerow(DATA)

    print(f"✓ CSVファイル保存完了: {CSV_PATH}")

    # データ内容を表示
    print("\n【取得データ】")
    for key, value in DATA.items():
        print(f"  {key}: {value}")

    # ファイルサイズ確認
    file_size = Path(CSV_PATH).stat().st_size
    print(f"\nファイルサイズ: {file_size} bytes")

if __name__ == "__main__":
    save_to_csv()
