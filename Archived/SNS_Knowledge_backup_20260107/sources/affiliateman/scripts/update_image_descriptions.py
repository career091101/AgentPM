#!/usr/bin/env python3
"""
画像説明をMarkdownに埋め込む

image_inventory_progress.jsonから画像説明を読み込み、
各Markdownファイルのプレースホルダーを説明に置き換える
"""

import json
import re
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

def update_markdown_descriptions():
    """Markdownファイルのプレースホルダーを画像説明に置き換え"""

    print("=" * 60)
    print("画像説明のMarkdown埋め込み処理開始")
    print("=" * 60)

    # 画像説明データを読み込み
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    # 記事ファイルパスごとに画像をグループ化
    articles_images = defaultdict(list)
    for img in inventory:
        filepath = OUTPUT_DIR / img['article_filepath']
        articles_images[filepath].append(img)

    print(f"\n対象記事: {len(articles_images)}件")
    print(f"対象画像: {len(inventory)}枚\n")

    # 統計
    updated_files = 0
    updated_images = 0
    skipped_images = 0

    # 各記事のMarkdownを更新
    for filepath, images in articles_images.items():
        if not filepath.exists():
            print(f"⚠ ファイル未検出（スキップ）: {filepath.name}")
            continue

        # Markdownファイルを読み込み
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        file_updated = False

        # 各画像のプレースホルダーを置換
        for img in images:
            filename = img['filename']
            description = img.get('description', '')

            if not description:
                skipped_images += 1
                continue

            # プレースホルダーパターン: ![PLACEHOLDER:image_XX.ext](path)
            placeholder_pattern = re.escape(f"PLACEHOLDER:{filename}")

            # 置換: ![PLACEHOLDER:filename](...) → ![description](...)
            pattern = rf'!\[{placeholder_pattern}\]'
            replacement = f'![{description}]'

            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                updated_images += 1
                file_updated = True

        # 変更があった場合のみファイルを更新
        if file_updated and content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files += 1
            print(f"✓ 更新: {filepath.name}")

    print("\n" + "=" * 60)
    print("画像説明の埋め込み完了")
    print("=" * 60)
    print(f"更新ファイル数: {updated_files}件")
    print(f"更新画像数: {updated_images}枚")
    print(f"スキップ画像数: {skipped_images}枚（説明なし）")
    print("=" * 60)

    # 次のステップの案内
    if updated_files > 0:
        print("\n✓ Markdownファイルの更新が完了しました！")
        print("\n次のステップ:")
        print("  Phase 6: chunker.pyを実行してRAG更新")
        print("  コマンド: python3 scripts/chunker.py")

if __name__ == "__main__":
    update_markdown_descriptions()
