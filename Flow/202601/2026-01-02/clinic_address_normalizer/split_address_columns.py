#!/usr/bin/env python3
"""
住所列を「国名」「郵便番号」「住所」の3列に分割
"""

import csv
import re
from datetime import datetime

input_file = "nationwide_45prefectures_pediatric_dental_final_20260102_232546.csv"
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"nationwide_45prefectures_split_address_{timestamp}.csv"

print("=" * 60)
print("住所列の分割処理")
print("=" * 60)

def parse_address(full_address: str) -> tuple:
    """
    住所を国名、郵便番号、住所の3つに分割

    入力例: "日本、〒154-0022 東京都世田谷区梅丘１丁目１４−１８"
    出力: ("日本", "154-0022", "東京都世田谷区梅丘１丁目１４−１８")
    """
    # 国名抽出（カンマの前）
    country = ""
    if "、" in full_address or "," in full_address:
        parts = re.split('[、,]', full_address, 1)
        country = parts[0].strip()
        remaining = parts[1].strip() if len(parts) > 1 else ""
    else:
        remaining = full_address

    # 郵便番号抽出（〒123-4567 または 123-4567 の形式）
    postal_code = ""
    address = remaining

    postal_match = re.search(r'〒?(\d{3}-?\d{4})', remaining)
    if postal_match:
        postal_code = postal_match.group(1)
        # 郵便番号とその前後の記号を除去
        address = re.sub(r'〒?\d{3}-?\d{4}\s*', '', remaining).strip()

    return country, postal_code, address


# CSV読み込みと分割処理
all_data = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        full_address = row.get("住所", "")
        country, parsed_postal, parsed_address = parse_address(full_address)

        # 郵便番号列が既にある場合は既存のものを優先
        if row.get("郵便番号"):
            postal_code = row["郵便番号"]
        else:
            postal_code = parsed_postal

        new_row = {
            "医院名": row.get("医院名", ""),
            "国名": country,
            "郵便番号": postal_code,
            "住所": parsed_address,
            "評価": row.get("評価", ""),
            "口コミ件数": row.get("口コミ件数", ""),
            "Google Maps URL": row.get("Google Maps URL", ""),
            "公式ウェブサイト": row.get("公式ウェブサイト", ""),
            "都道府県": row.get("都道府県", ""),
            "診療科目": row.get("診療科目", "")
        }
        all_data.append(new_row)

print(f"\n読み込み: {len(all_data)}件")

# サンプル表示（最初の3件）
print(f"\n分割結果サンプル（最初の3件）:")
print("-" * 60)
for i, row in enumerate(all_data[:3], 1):
    print(f"\n{i}. {row['医院名']}")
    print(f"   国名: {row['国名']}")
    print(f"   郵便番号: {row['郵便番号']}")
    print(f"   住所: {row['住所']}")

# CSV出力
fieldnames = ["医院名", "国名", "郵便番号", "住所", "評価", "口コミ件数", "Google Maps URL", "公式ウェブサイト", "都道府県", "診療科目"]

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_data:
        writer.writerow(row)

print(f"\n✅ 分割完了: {output_file}")
print(f"{'=' * 60}")
