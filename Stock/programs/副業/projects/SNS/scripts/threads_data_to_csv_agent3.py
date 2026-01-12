#!/usr/bin/env python3
"""
Threads週間データをCSVに保存するスクリプト（Agent3）
"""

import csv
from datetime import datetime
import os

def save_to_csv():
    csv_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/Threads/threads_weekly_parallel_agent3.csv"

    # ディレクトリ作成
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # スクリーンショットから抽出したデータ
    data = {
        '取得日時': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'データソース': '並列実行Agent3',
        '投稿数': 3,
        '表示回数': 267,
        '新規フォロワー': 2,
        '返信数': 0
    }

    # CSVに保存
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] CSVファイル保存完了: {csv_path}")
    print(f"\n取得データ:")
    print(f"- 取得日時: {data['取得日時']}")
    print(f"- データソース: {data['データソース']}")
    print(f"- 投稿数: {data['投稿数']}")
    print(f"- 表示回数: {data['表示回数']}")
    print(f"- 新規フォロワー: {data['新規フォロワー']}")
    print(f"- 返信数: {data['返信数']}")

    return data

if __name__ == "__main__":
    save_to_csv()
