#!/usr/bin/env python3
"""
Markdownファイルから data URI 形式の画像参照を削除するスクリプト
"""
import re
from pathlib import Path

def clean_markdown_images(md_path):
    """Markdownファイルから data URI 形式の画像参照を削除"""
    content = md_path.read_text(encoding='utf-8')

    # data URI形式の画像参照を削除
    # パターン1: ![alt](data:image/...)
    content = re.sub(r'!\[([^\]]*)\]\(data:image/[^)]+\)', '', content)

    # パターン2: [![alt](data:image/...)](link)
    content = re.sub(r'\[!\[([^\]]*)\]\(data:image/[^)]+\)\]\([^)]+\)', '', content)

    # 連続する空行を1つにまとめる
    content = re.sub(r'\n{3,}', '\n\n', content)

    md_path.write_text(content, encoding='utf-8')
    return True

def main():
    articles_dir = Path("../data/d_1d2d_articles/articles")

    md_files = list(articles_dir.glob("*.md"))
    print(f"Processing {len(md_files)} Markdown files...")

    fixed_count = 0
    for md_file in md_files:
        try:
            clean_markdown_images(md_file)
            fixed_count += 1
            if fixed_count % 10 == 0:
                print(f"  Processed {fixed_count}/{len(md_files)} files...")
        except Exception as e:
            print(f"  Error processing {md_file.name}: {e}")

    print(f"\n✅ Complete! Fixed {fixed_count} Markdown files.")
    print(f"   Removed data URI image references from all files.")

if __name__ == "__main__":
    main()
