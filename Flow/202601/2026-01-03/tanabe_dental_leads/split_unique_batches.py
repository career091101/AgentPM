#!/usr/bin/env python3
"""
ユニーク医院データのバッチ分割

1,615件を500件ずつ分割（4バッチ）
"""

import csv
from pathlib import Path

# 入力ファイル
input_csv = Path("tanabe_dental_leads_unique_20260104_132935.csv")

# 出力ディレクトリ
output_dir = Path("scoring_batches_unique")
output_dir.mkdir(exist_ok=True)

# バッチサイズ
batch_size = 500

print(f"📊 バッチ分割処理開始")
print(f"   入力: {input_csv}")
print(f"   出力ディレクトリ: {output_dir}/")
print(f"   バッチサイズ: {batch_size}件")

# CSV読み込み
with open(input_csv, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    clinics = list(reader)

print(f"\n✓ 読み込み完了: {len(clinics)}件")

# 500件ずつ分割
for i in range(0, len(clinics), batch_size):
    batch = clinics[i:i+batch_size]
    batch_num = i // batch_size + 1

    output_file = output_dir / f'batch_{batch_num:03d}_to_score.csv'

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f_out:
        if batch:
            writer = csv.DictWriter(f_out, fieldnames=batch[0].keys())
            writer.writeheader()
            writer.writerows(batch)

    print(f"✓ バッチ{batch_num:03d}: {len(batch)}件 → {output_file}")

print(f"\n✓ 分割完了: {len(clinics)}件 → {batch_num}バッチ")
print(f"\n📊 バッチ構成:")
print(f"   バッチ001-{(batch_num-1):03d}: 各500件")
print(f"   バッチ{batch_num:03d}: {len(clinics) - (batch_num-1)*batch_size}件")
