#!/usr/bin/env python3
"""
自動生成された説明を持つ画像を検出
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

def is_auto_generated(description):
    """説明が自動生成されたものかチェック"""
    if not description:
        return True

    # 自動生成パターン
    auto_patterns = [
        "運用に関する説明画像または投稿サムネイル。記事",
        "運用に関する説明画像または図解。",
        "記事のバナー画像またはメインビジュアル。",
        "関連コンテンツ。"
    ]

    for pattern in auto_patterns:
        if pattern in description:
            return True

    return False

def find_auto_generated_images():
    """自動生成説明の画像を検出"""

    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    auto_generated = []
    manually_described = []

    for idx, img in enumerate(inventory):
        desc = img.get('description', '')
        if is_auto_generated(desc):
            auto_generated.append((idx, img))
        else:
            manually_described.append((idx, img))

    total = len(inventory)
    auto_count = len(auto_generated)
    manual_count = len(manually_described)

    print("=" * 60)
    print("画像説明の状況")
    print("=" * 60)
    print(f"総画像数: {total}")
    print(f"詳細説明済み: {manual_count} ({manual_count/total*100:.1f}%)")
    print(f"自動生成説明: {auto_count} ({auto_count/total*100:.1f}%)")
    print("=" * 60)

    return auto_generated

if __name__ == "__main__":
    auto_gen = find_auto_generated_images()

    if auto_gen:
        print(f"\n自動生成説明の画像: {len(auto_gen)}件")
        print("\n最初の5件:")
        for idx, img in auto_gen[:5]:
            print(f"[{idx}] {img['filename']}: {img['description'][:60]}...")
