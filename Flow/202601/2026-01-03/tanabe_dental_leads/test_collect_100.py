#!/usr/bin/env python3
"""
100件テスト収集スクリプト
collect_with_dedup.py を利用した重複排除付き収集
"""
import googlemaps
import sys
import os
from pathlib import Path
from datetime import datetime

# collect_with_dedup モジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
from collect_with_dedup import DedupCollector

# Google Maps API初期化
API_KEY = "AIzaSyASqcmLzyXnzrK6jcKzl7PVZ_3CmSv4rxc"
gmaps = googlemaps.Client(key=API_KEY)

# 重複排除コレクター初期化
collector = DedupCollector(output_dir=".")

# 東京都の中心座標
TOKYO_CENTER = (35.6812, 139.7671)

# 検索キーワード
keywords = ["小児歯科", "矯正歯科", "こども歯科"]

# 検索実行（既存履歴を読み込み、重複スキップ）
all_unique_clinics = []

print("=" * 60)
print("Phase 0: 100件テスト収集開始")
print("=" * 60)
print(f"検索地域: 東京都")
print(f"検索キーワード: {', '.join(keywords)}")
print(f"目標件数: 100件（新規ユニーク）")
print("=" * 60)

for keyword in keywords:
    print(f"\n🔍 検索: {keyword}")

    try:
        results = gmaps.places_nearby(
            location=TOKYO_CENTER,
            keyword=keyword,
            radius=50000,  # 50km
            type="dentist",
            language="ja"
        )

        # 重複排除して収集
        unique_results = collector.collect_from_search_results(results['results'])
        all_unique_clinics.extend(unique_results)

        print(f"   新規ユニーク: {len(unique_results)}件")
        print(f"   累計ユニーク: {len(all_unique_clinics)}件")

        # 100件到達で終了
        if len(all_unique_clinics) >= 100:
            print(f"\n✅ 目標達成: {len(all_unique_clinics)}件")
            break

    except Exception as e:
        print(f"   ❌ エラー: {e}")
        continue

# CSV保存
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"test_100_clinics_{timestamp}.csv"
collector.save_to_csv(all_unique_clinics, output_file)

# 統計表示
collector.print_statistics()

print("\n" + "=" * 60)
print("Phase 0: テスト収集完了")
print("=" * 60)
print(f"✅ 出力ファイル: {output_file}")
print(f"✅ 新規収集件数: {len(all_unique_clinics)}件")
print("\n次のステップ:")
print(f"  python3 validate_data_quality.py {output_file}")
print("=" * 60)
