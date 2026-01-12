#!/usr/bin/env python3
"""
既存ブログ記事の画像取得スクリプト

metadata.jsonから記事URLリストを取得し、画像付きで再スクレイピング
"""

import json
from pathlib import Path
from scraper import AffiliateManScraper

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

def rescrape_blog_images():
    """既存ブログ記事の画像を再取得"""
    print("=" * 60)
    print("ブログ記事画像再スクレイピング")
    print("=" * 60)

    # スクレイパー初期化
    scraper = AffiliateManScraper()
    if not scraper.login():
        print("✗ ログイン失敗")
        return

    # metadata.jsonから記事リスト取得
    metadata_file = OUTPUT_DIR / 'metadata.json'
    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    blog_articles = metadata.get('blog', [])
    print(f"\n対象記事: {len(blog_articles)}件\n")

    # 進捗管理
    updated_articles = []
    success_count = 0
    error_count = 0
    total_images = 0

    for i, article in enumerate(blog_articles, 1):
        print(f"[{i}/{len(blog_articles)}] {article['title']}")
        print(f"  URL: {article['url']}")

        try:
            # 再スクレイピング（画像含む）
            result = scraper.scrape_blog_post(article['url'], article['category'])

            if result:
                updated_articles.append(result)
                success_count += 1
                if result.get('images', 0) > 0:
                    total_images += result['images']
                print(f"  ✓ 完了")
            else:
                error_count += 1
                updated_articles.append(article)  # 元データ保持
                print(f"  ✗ 取得失敗")

        except Exception as e:
            print(f"  ✗ エラー: {e}")
            error_count += 1
            updated_articles.append(article)  # 元データ保持

    # metadata.json更新
    metadata['blog'] = updated_articles
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    # 画像情報を別ファイルに保存（Claude Codeが画像説明を追加する用）
    image_inventory = []
    for article in updated_articles:
        if article.get('image_metadata'):
            for img in article['image_metadata']:
                image_inventory.append({
                    'article_title': article['title'],
                    'article_url': article['url'],
                    'article_filepath': article['filepath'],
                    'category': article['category'],
                    'image_path': img['local_path'],
                    'original_url': img['original_url'],
                    'alt': img['alt'],
                    'filename': img['filename'],
                    'description': None  # Claude Codeが後で埋める
                })

    with open(OUTPUT_DIR / 'image_inventory.json', 'w', encoding='utf-8') as f:
        json.dump(image_inventory, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"再スクレイピング完了")
    print("=" * 60)
    print(f"成功: {success_count}件 / エラー: {error_count}件")
    print(f"画像ダウンロード: {total_images}枚")
    print(f"✓ metadata.json更新")
    print(f"✓ image_inventory.json生成 ({len(image_inventory)}件)")
    print("=" * 60)

if __name__ == "__main__":
    rescrape_blog_images()
