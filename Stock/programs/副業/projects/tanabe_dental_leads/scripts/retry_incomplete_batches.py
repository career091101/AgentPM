#!/usr/bin/env python3
"""
不完全バッチの再実行スクリプト

対象バッチ: 002, 003, 005, 006, 007, 008, 009, 010, 012, 013, 018, 022, 026, 032, 035
合計15バッチを再実行
"""

import json
from pathlib import Path

# 不完全バッチリスト（件数が500件未満のバッチ）
INCOMPLETE_BATCHES = [2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 18, 22, 26, 32, 35]

# 各バッチの期待件数
EXPECTED_COUNTS = {
    i: 500 for i in range(1, 36)
}
EXPECTED_COUNTS[36] = 452  # バッチ36のみ452件

def check_batch_completeness():
    """各バッチの完全性をチェック"""
    print("=" * 60)
    print("バッチ完全性チェック")
    print("=" * 60)

    incomplete = []

    for batch_num in range(1, 37):
        expected = EXPECTED_COUNTS.get(batch_num, 500)

        # 既存のスコアリング結果を検索
        result_files = list(Path('.').glob(f'**/scoring_results_batch_{batch_num:03d}*.json'))

        if not result_files:
            incomplete.append(batch_num)
            print(f"✗ バッチ {batch_num:03d}: ファイルなし")
            continue

        # 最新ファイルを確認
        latest_file = max(result_files, key=lambda p: p.stat().st_mtime)

        try:
            with open(latest_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 件数カウント
            count = 0
            if 'results' in data:
                if isinstance(data['results'], list):
                    count = len(data['results'])
                elif isinstance(data['results'], dict):
                    count = len(data['results'])

            if count >= expected:
                print(f"✓ バッチ {batch_num:03d}: {count}/{expected}件（完全）")
            else:
                incomplete.append(batch_num)
                print(f"⚠ バッチ {batch_num:03d}: {count}/{expected}件（不完全）")

        except Exception as e:
            incomplete.append(batch_num)
            print(f"✗ バッチ {batch_num:03d}: エラー - {e}")

    print("\n" + "=" * 60)
    print(f"不完全バッチ: {len(incomplete)}個")
    print(f"対象: {incomplete}")
    print("=" * 60)

    return incomplete

if __name__ == '__main__':
    incomplete = check_batch_completeness()

    print(f"\n再実行対象バッチリスト:")
    print(f"INCOMPLETE_BATCHES = {incomplete}")
