#!/usr/bin/env python3
"""
画像をBase64に変換してMarkdownファイルに埋め込むスクリプト

使用方法:
    python convert_images_to_base64.py

機能:
    - 各Markdownファイルから画像URLを検出
    - 画像をダウンロード（オリジナル解像度維持）
    - Base64にエンコード
    - Markdownに埋め込み（data:image/...;base64,...形式）
"""

import os
import re
import base64
import requests
from pathlib import Path
from typing import List, Tuple
import mimetypes

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
BLOG_DIR = PROJECT_ROOT / "blog"

def extract_image_urls_from_markdown(md_content: str) -> List[Tuple[str, str]]:
    """
    Markdownから画像URLを抽出

    Args:
        md_content: Markdownの内容

    Returns:
        [(alt_text, url), ...] のリスト
    """
    # Markdown画像パターン: ![alt](url)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, md_content)

    # http/httpsで始まるURLのみフィルタ
    image_urls = [(alt, url) for alt, url in matches if url.startswith(('http://', 'https://'))]

    return image_urls

def download_image(url: str) -> bytes:
    """
    画像をダウンロード

    Args:
        url: 画像URL

    Returns:
        画像のバイナリデータ
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"  ⚠️ 画像ダウンロード失敗: {url}")
        print(f"     エラー: {e}")
        return None

def image_to_base64(image_data: bytes, url: str) -> str:
    """
    画像をBase64にエンコード

    Args:
        image_data: 画像のバイナリデータ
        url: 画像URL（MIME type判定用）

    Returns:
        data:image/...;base64,... 形式の文字列
    """
    # MIME typeを推定
    mime_type, _ = mimetypes.guess_type(url)
    if not mime_type or not mime_type.startswith('image/'):
        # 拡張子から判定できない場合、デフォルトをpngに
        mime_type = 'image/png'

    # Base64エンコード
    base64_data = base64.b64encode(image_data).decode('utf-8')

    return f"data:{mime_type};base64,{base64_data}"

def replace_images_with_base64(md_content: str, md_file_path: Path) -> str:
    """
    Markdown内の画像URLをBase64に置換

    Args:
        md_content: Markdownの内容
        md_file_path: Markdownファイルのパス

    Returns:
        Base64埋め込み済みのMarkdown
    """
    image_urls = extract_image_urls_from_markdown(md_content)

    if not image_urls:
        print(f"  画像なし")
        return md_content

    print(f"  画像数: {len(image_urls)}")

    modified_content = md_content
    success_count = 0

    for i, (alt_text, url) in enumerate(image_urls, 1):
        print(f"  [{i}/{len(image_urls)}] ダウンロード中: {url[:60]}...")

        # 画像ダウンロード
        image_data = download_image(url)
        if image_data is None:
            continue

        # Base64変換
        base64_url = image_to_base64(image_data, url)

        # 置換
        old_pattern = f"![{re.escape(alt_text)}]({re.escape(url)})"
        new_pattern = f"![{alt_text}]({base64_url})"
        modified_content = modified_content.replace(old_pattern, new_pattern)

        success_count += 1
        print(f"  ✓ 変換完了 ({len(image_data)} bytes -> {len(base64_url)} chars)")

    print(f"  結果: {success_count}/{len(image_urls)} 件成功")

    return modified_content

def process_markdown_file(md_file_path: Path):
    """
    1つのMarkdownファイルを処理

    Args:
        md_file_path: Markdownファイルのパス
    """
    print(f"\n処理中: {md_file_path.relative_to(PROJECT_ROOT)}")

    # ファイル読み込み
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"  ✗ 読み込み失敗: {e}")
        return

    # 画像をBase64に変換
    modified_content = replace_images_with_base64(original_content, md_file_path)

    # ファイル保存
    if modified_content != original_content:
        try:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"  ✓ 保存完了")
        except Exception as e:
            print(f"  ✗ 保存失敗: {e}")
    else:
        print(f"  変更なし")

def main():
    """メイン処理"""
    print("=" * 60)
    print("画像Base64変換スクリプト")
    print("=" * 60)

    # 対象ディレクトリ
    categories = ["instagram", "twitter", "tiktok"]

    total_files = 0
    for category in categories:
        category_dir = BLOG_DIR / category
        if not category_dir.exists():
            print(f"\n⚠️ ディレクトリが存在しません: {category_dir}")
            continue

        # Markdownファイル一覧
        md_files = list(category_dir.glob("*.md"))
        print(f"\n{'=' * 60}")
        print(f"カテゴリ: {category} ({len(md_files)} files)")
        print(f"{'=' * 60}")

        for md_file in md_files:
            process_markdown_file(md_file)
            total_files += 1

    print(f"\n{'=' * 60}")
    print(f"完了: {total_files} ファイル処理")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
