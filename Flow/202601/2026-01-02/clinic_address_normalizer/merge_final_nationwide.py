#!/usr/bin/env python3
"""
全45都府県データ統合（既存170件 + 新規4バッチ369件）
"""

import csv
from datetime import datetime
from collections import Counter
import glob

print("=" * 60)
print("全45都府県データ統合")
print("=" * 60)

# 統合対象ファイル
files_to_merge = [
    "nationwide_pediatric_dental_final_20260102_222039.csv",  # 既存170件（東京・大阪・愛知 + 9県）
    "batch1_pediatric_dental_20260102_230015.csv",  # 99件（青森〜埼玉）
    "batch2_pediatric_dental_20260102_232001.csv",  # 109件（千葉〜静岡）
    "batch3_pediatric_dental_20260102_232339.csv",  # 128件（三重〜広島）
    "batch4_pediatric_dental_20260102_232500.csv",  # 33件（山口・徳島・香川）
]

# 統合
all_data = []
seen_place_ids = set()
file_stats = {}

for filename in files_to_merge:
    print(f"\n読み込み: {filename}")
    initial_count = len(all_data)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # place_id または 医院名+住所でユニーク化
                if 'place_id' in row and row['place_id']:
                    unique_key = row['place_id']
                else:
                    unique_key = f"{row['医院名']}_{row['住所']}"

                if unique_key not in seen_place_ids:
                    seen_place_ids.add(unique_key)
                    all_data.append(row)

        added = len(all_data) - initial_count
        file_stats[filename] = added
        print(f"  追加: {added}件")
    except FileNotFoundError:
        print(f"  ⚠️  ファイルが見つかりません: {filename}")

# 統計
print(f"\n{'=' * 60}")
print("📊 統合結果サマリー")
print(f"{'=' * 60}")

total = len(all_data)
print(f"\n総件数: {total}件（重複なし）")

# ファイル別内訳
print(f"\nファイル別内訳:")
for filename, count in file_stats.items():
    print(f"  {filename}: {count}件")

# 品質指標
avg_rating = sum(float(r["評価"]) for r in all_data if r["評価"]) / len([r for r in all_data if r["評価"]])
avg_reviews = sum(int(r["口コミ件数"]) for r in all_data) / len(all_data)
has_website = sum(1 for r in all_data if r.get("公式ウェブサイト"))

print(f"\n品質指標:")
print(f"  平均評価: ⭐{avg_rating:.2f}")
print(f"  平均口コミ件数: {avg_reviews:.0f}件")
print(f"  公式ウェブサイトあり: {has_website}/{total} ({has_website/total*100:.1f}%)")

# 都道府県別内訳
prefecture_counts = Counter(r.get("都道府県", "不明") for r in all_data)
print(f"\n都道府県別内訳（45都府県）:")
for pref, count in sorted(prefecture_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {pref}: {count}件")

# 診療科目別内訳
specialty_counts = Counter(r.get("診療科目", "不明") for r in all_data)
print(f"\n診療科目別内訳:")
for spec, count in sorted(specialty_counts.items()):
    print(f"  {spec}: {count}件")

# 最終CSV出力
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"nationwide_45prefectures_pediatric_dental_final_{timestamp}.csv"

fieldnames = ["医院名", "住所", "郵便番号", "評価", "口コミ件数", "Google Maps URL", "公式ウェブサイト", "都道府県", "診療科目"]

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_data:
        # 必要なフィールドのみ出力
        output_row = {k: row.get(k, '') for k in fieldnames}
        writer.writerow(output_row)

print(f"\n✅ 最終CSV出力完了: {output_file}")
print(f"{'=' * 60}")
