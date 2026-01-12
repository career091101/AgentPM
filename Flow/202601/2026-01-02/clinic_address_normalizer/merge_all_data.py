#!/usr/bin/env python3
"""
全データ統合（既存75件 + 新規98件 + 残り地域）
"""

import csv
from datetime import datetime
from collections import Counter

# 既存ファイル
existing_file = "pediatric_filtered_output.csv"  # 東京・大阪・愛知75件
remaining_file = "pediatric_dental_remaining_20260102_221959.csv"  # 愛媛〜鹿児島98件

# 統合
all_data = []
seen_place_ids = set()

print("=" * 60)
print("全データ統合")
print("=" * 60)

# 既存データ読み込み
print(f"\n既存データ読み込み: {existing_file}")
with open(existing_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # place_id がない場合は医院名+住所でユニーク化
        unique_key = f"{row['医院名']}_{row['住所']}"
        if unique_key not in seen_place_ids:
            seen_place_ids.add(unique_key)
            # 診療科目と都道府県を追加（既存データにはない場合）
            if '診療科目' not in row:
                row['診療科目'] = row.get('検索クエリ', '').split()[0] if '検索クエリ' in row else ''
            if '都道府県' not in row:
                # 住所から都道府県を抽出
                address = row['住所']
                for pref in ['東京都', '大阪府', '愛知県']:
                    if pref in address:
                        row['都道府県'] = pref
                        break
            all_data.append(row)

print(f"  読み込み: {len(all_data)}件")

# 新規データ読み込み
print(f"\n新規データ読み込み: {remaining_file}")
initial_count = len(all_data)
with open(remaining_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        unique_key = f"{row['医院名']}_{row['住所']}"
        if unique_key not in seen_place_ids:
            seen_place_ids.add(unique_key)
            all_data.append(row)

print(f"  読み込み: {len(all_data) - initial_count}件")

# 重複削除確認
print(f"\n統合後: {len(all_data)}件（重複なし）")

# 統計
print(f"\n{'=' * 60}")
print("📊 統計サマリー")
print(f"{'=' * 60}")

total = len(all_data)
avg_rating = sum(float(r["評価"]) for r in all_data if r["評価"]) / len([r for r in all_data if r["評価"]])
avg_reviews = sum(int(r["口コミ件数"]) for r in all_data) / len(all_data)
has_website = sum(1 for r in all_data if r.get("公式ウェブサイト"))

print(f"総件数: {total}件")
print(f"平均評価: ⭐{avg_rating:.2f}")
print(f"平均口コミ件数: {avg_reviews:.0f}件")
print(f"公式ウェブサイトあり: {has_website}/{total} ({has_website/total*100:.1f}%)")

# 都道府県別内訳
prefecture_counts = Counter(r.get("都道府県", "不明") for r in all_data)
print(f"\n都道府県別内訳:")
for pref, count in sorted(prefecture_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {pref}: {count}件")

# 診療科目別内訳
specialty_counts = Counter(r.get("診療科目", "不明") for r in all_data)
print(f"\n診療科目別内訳:")
for spec, count in sorted(specialty_counts.items()):
    print(f"  {spec}: {count}件")

# 最終CSV出力
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"nationwide_pediatric_dental_final_{timestamp}.csv"

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
