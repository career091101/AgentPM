#!/usr/bin/env python3
"""
画像説明生成バッチ処理ヘルパー

image_inventory.jsonから指定範囲の画像情報を抽出し、
Claude Codeが処理しやすい形式で出力する
"""

import json
from pathlib import Path
import sys

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

def get_batch(start_idx=0, batch_size=15):
    """指定範囲の画像情報を取得"""
    with open(OUTPUT_DIR / 'image_inventory.json', 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    end_idx = min(start_idx + batch_size, len(inventory))
    batch = inventory[start_idx:end_idx]

    print(f"=== バッチ情報 ===")
    print(f"総画像数: {len(inventory)}")
    print(f"処理範囲: {start_idx} - {end_idx} ({len(batch)}件)")
    print(f"残り: {len(inventory) - end_idx}件")
    print()

    print("=== 画像リスト ===")
    for i, img in enumerate(batch, start_idx):
        print(f"[{i}] {img['article_title']}")
        print(f"    ファイル: {img['filename']}")
        print(f"    パス: {img['image_path']}")
        print()

    return batch

def save_batch_output(batch_data, output_file='batch_output.json'):
    """バッチ処理結果を保存"""
    with open(OUTPUT_DIR / output_file, 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)
    print(f"✓ 保存完了: {output_file}")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    batch = get_batch(start, size)

    # 処理用にパスリストを出力
    print("=== 画像パス一覧（Read用） ===")
    for img in batch:
        full_path = OUTPUT_DIR / img['image_path']
        print(full_path)
