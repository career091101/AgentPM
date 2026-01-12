#!/usr/bin/env python3
"""
全バッチのCSVファイルを統合して最終営業リストを作成
"""

import csv
import glob
from datetime import datetime

def merge_all_batches():
    """全バッチCSVファイルを読み込み、統合してソート"""

    # 全CSVファイルを取得（batch_002_leads_final.csvと batch_*_leads_llm_*.csv）
    csv_files = []
    csv_files.extend(glob.glob('batch_002_leads_final.csv'))  # バッチ2（手動作成）
    csv_files.extend(glob.glob('batch_*_leads_llm_*.csv'))    # バッチ3-20（自動生成）

    print(f"📂 {len(csv_files)}個のCSVファイルを統合します")

    all_rows = []
    fieldnames = None

    for csv_file in sorted(csv_files):
        print(f"   読み込み中: {csv_file}")
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            if fieldnames is None:
                fieldnames = reader.fieldnames
            for row in reader:
                all_rows.append(row)

    print(f"✅ 総件数: {len(all_rows)}件のデータを統合")

    # スコア順にソート（降順）
    all_rows_sorted = sorted(all_rows, key=lambda x: int(x['スコア']), reverse=True)

    # 最終CSV出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"tanabe_dental_leads_all_batches_{timestamp}.csv"

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows_sorted)

    print(f"✅ 最終営業リスト作成完了: {output_file}")

    # 統計情報
    if all_rows_sorted:
        avg_score = sum(int(r['スコア']) for r in all_rows_sorted) / len(all_rows_sorted)
        print(f"\n--- 統計情報 ---")
        print(f"総件数: {len(all_rows_sorted)}件")
        print(f"平均スコア: {avg_score:.1f}点")
        print(f"最高スコア: {all_rows_sorted[0]['スコア']}点 - {all_rows_sorted[0]['医院名']}")
        print(f"最低スコア: {all_rows_sorted[-1]['スコア']}点 - {all_rows_sorted[-1]['医院名']}")

        # スコア帯別集計
        high_score = sum(1 for r in all_rows_sorted if int(r['スコア']) >= 70)
        mid_score = sum(1 for r in all_rows_sorted if 50 <= int(r['スコア']) < 70)
        low_score = sum(1 for r in all_rows_sorted if int(r['スコア']) < 50)

        print(f"\nスコア帯別:")
        print(f"  70点以上（優先アプローチ推奨）: {high_score}件")
        print(f"  50-69点（中優先度）: {mid_score}件")
        print(f"  50点未満（低優先度）: {low_score}件")

    return output_file

if __name__ == '__main__':
    merge_all_batches()
