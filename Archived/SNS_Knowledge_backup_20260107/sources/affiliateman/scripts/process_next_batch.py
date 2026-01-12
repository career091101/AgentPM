#!/usr/bin/env python3
"""
次のバッチの画像パスを取得して表示
"""

import json
from pathlib import Path
import sys

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

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

def get_next_batch(batch_size=20):
    """次に処理すべき画像のバッチを取得"""

    # 進捗ファイルを読み込み
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    if progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
    else:
        with open(OUTPUT_DIR / 'image_inventory.json', 'r', encoding='utf-8') as f:
            inventory = json.load(f)

    # 未処理の画像を検索（自動生成説明も未処理として扱う）
    unprocessed = [
        (idx, img) for idx, img in enumerate(inventory)
        if is_auto_generated(img.get('description', ''))
    ]

    if not unprocessed:
        print("✓ 全ての画像の説明が完了しました！")
        return [], 0, len(inventory)

    # 次のバッチを取得
    batch = unprocessed[:batch_size]
    start_idx = batch[0][0]
    end_idx = batch[-1][0]

    total = len(inventory)
    completed = total - len(unprocessed)
    remaining = len(unprocessed)

    print(f"=== バッチ情報 ===")
    print(f"総画像数: {total}")
    print(f"完了: {completed} ({completed/total*100:.1f}%)")
    print(f"残り: {remaining}")
    print(f"次のバッチ: {start_idx} - {end_idx} ({len(batch)}件)")
    print()

    # 記事ごとにグループ化して表示
    articles = {}
    for idx, img in batch:
        article_title = img['article_title']
        if article_title not in articles:
            articles[article_title] = []
        articles[article_title].append((idx, img))

    print("=== 記事ごとの内訳 ===")
    for article, images in articles.items():
        print(f"{article} ({len(images)}枚)")

    print()
    print("=== 画像パス一覧 ===")
    for idx, img in batch:
        full_path = OUTPUT_DIR / img['image_path']
        print(f"[{idx}] {full_path}")

    return batch, completed, total

if __name__ == "__main__":
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    get_next_batch(batch_size)
