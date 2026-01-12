#!/usr/bin/env python3
"""
重複医院データの削除スクリプト

元の17,952件から重複を削除し、ユニーク医院のみのCSVを作成
"""

import csv
from pathlib import Path
from datetime import datetime

# 入力ファイル
input_csv = Path("tanabe_dental_leads_all_batches_20260104_123142.csv")

# 出力ファイル
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_csv = Path(f"tanabe_dental_leads_unique_{timestamp}.csv")

print(f"📊 重複削除処理開始")
print(f"   入力: {input_csv}")
print(f"   出力: {output_csv}")

# CSV読み込み
with open(input_csv, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)

print(f"\n✓ 読み込み完了: {len(all_rows)}件")

# 医院名でユニーク化（最初に出現した行を保持）
seen_clinics = set()
unique_rows = []

for row in all_rows:
    clinic_name = row.get('医院名', '')

    if clinic_name and clinic_name not in seen_clinics:
        seen_clinics.add(clinic_name)
        unique_rows.append(row)

print(f"✓ 重複削除完了: {len(unique_rows)}件（重複削除: {len(all_rows) - len(unique_rows)}件）")

# ユニークデータを新しいCSVに書き出し
if unique_rows:
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=unique_rows[0].keys())
        writer.writeheader()
        writer.writerows(unique_rows)

print(f"\n✓ 出力完了: {output_csv}")
print(f"   ユニーク医院数: {len(unique_rows)}件")
print(f"   重複削除率: {(len(all_rows) - len(unique_rows)) / len(all_rows) * 100:.1f}%")

# 統計情報
print(f"\n📊 統計情報:")
print(f"   元データ: {len(all_rows)}件")
print(f"   ユニークデータ: {len(unique_rows)}件")
print(f"   削除された重複: {len(all_rows) - len(unique_rows)}件")
