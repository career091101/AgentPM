#!/usr/bin/env python3
"""
全バッチのCSVファイルを統合（重複排除機能付き）

【改善点】
1. マージ時に医院名で重複チェック
2. 最初に出現した医院データを保持
3. 重複統計を出力
4. ユニークデータのみの統合CSV作成

【効果】
- 重複データの完全排除
- 統合CSVの品質向上
- 後続処理の効率化
"""

import csv
import glob
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set

def merge_all_batches_with_dedup():
    """全バッチCSVファイルを読み込み、重複排除して統合"""

    # 全CSVファイルを取得
    csv_files = []
    csv_files.extend(glob.glob('batch_002_leads_final.csv'))
    csv_files.extend(glob.glob('batch_*_leads_llm_*.csv'))

    print(f"📂 {len(csv_files)}個のCSVファイルを統合します")

    # 重複チェック用
    seen_clinics: Set[str] = set()
    unique_rows: List[Dict] = []
    duplicate_count = 0
    total_count = 0

    fieldnames = None

    for csv_file in sorted(csv_files):
        print(f"   読み込み中: {csv_file}")

        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)

            if fieldnames is None:
                fieldnames = reader.fieldnames

            for row in reader:
                total_count += 1
                clinic_name = row.get('医院名', '')

                # 重複チェック
                if clinic_name in seen_clinics:
                    duplicate_count += 1
                    print(f"      ⚠️  重複スキップ: {clinic_name}")
                    continue

                # 新規医院として記録
                seen_clinics.add(clinic_name)
                unique_rows.append(row)

    print(f"\n📊 統合結果:")
    print(f"   総読み込み件数: {total_count}件")
    print(f"   重複削除: {duplicate_count}件")
    print(f"   ユニーク医院数: {len(unique_rows)}件")
    print(f"   重複率: {duplicate_count / total_count * 100:.1f}%")

    # スコア順にソート（降順）
    unique_rows_sorted = sorted(unique_rows, key=lambda x: int(x['スコア']), reverse=True)

    # 最終CSV出力（ユニークデータのみ）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"tanabe_dental_leads_all_batches_UNIQUE_{timestamp}.csv"

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows_sorted)

    print(f"\n✅ 最終営業リスト作成完了: {output_file}")

    # 統計情報
    if unique_rows_sorted:
        avg_score = sum(int(r['スコア']) for r in unique_rows_sorted) / len(unique_rows_sorted)

        print(f"\n--- 統計情報 ---")
        print(f"総件数（ユニーク）: {len(unique_rows_sorted)}件")
        print(f"平均スコア: {avg_score:.1f}点")
        print(f"最高スコア: {unique_rows_sorted[0]['スコア']}点 - {unique_rows_sorted[0]['医院名']}")
        print(f"最低スコア: {unique_rows_sorted[-1]['スコア']}点 - {unique_rows_sorted[-1]['医院名']}")

        # スコア帯別集計
        high_score = sum(1 for r in unique_rows_sorted if int(r['スコア']) >= 70)
        mid_score = sum(1 for r in unique_rows_sorted if 50 <= int(r['スコア']) < 70)
        low_score = sum(1 for r in unique_rows_sorted if int(r['スコア']) < 50)

        print(f"\nスコア帯別:")
        print(f"  70点以上（優先アプローチ推奨）: {high_score}件")
        print(f"  50-69点（中優先度）: {mid_score}件")
        print(f"  50点未満（低優先度）: {low_score}件")

    return output_file

if __name__ == '__main__':
    merge_all_batches_with_dedup()
