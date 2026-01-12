#!/usr/bin/env python3
"""
Extract Content Skill Implementation
記事・YouTube・PDFからコンテンツを抽出
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from urllib.parse import urlparse

# Webスクレイピングライブラリ
try:
    import requests
    from bs4 import BeautifulSoup
    REQUESTS_AVAILABLE = True
except ImportError:
    print("⚠️  Warning: requests or beautifulsoup4 not installed")
    print("   Install with: pip install requests beautifulsoup4")
    REQUESTS_AVAILABLE = False


def extract_article_content(url: str) -> Optional[Dict[str, Any]]:
    """
    記事URLからコンテンツを抽出

    Args:
        url: 記事URL

    Returns:
        抽出結果の辞書、失敗時はNone
    """
    if not REQUESTS_AVAILABLE:
        return None

    try:
        print(f"  → Fetching: {url[:60]}...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # タイトル抽出
        title = None
        if soup.find('title'):
            title = soup.find('title').text.strip()
        elif soup.find('h1'):
            title = soup.find('h1').text.strip()

        # 本文抽出（一般的なパターン）
        content_text = ""

        # パターン1: article タグ
        article = soup.find('article')
        if article:
            paragraphs = article.find_all('p')
            content_text = '\n\n'.join([p.text.strip() for p in paragraphs if p.text.strip()])

        # パターン2: main タグ
        if not content_text:
            main = soup.find('main')
            if main:
                paragraphs = main.find_all('p')
                content_text = '\n\n'.join([p.text.strip() for p in paragraphs if p.text.strip()])

        # パターン3: 全てのp タグ（フォールバック）
        if not content_text:
            paragraphs = soup.find_all('p')
            # 長いパラグラフのみ抽出（広告・ナビ除外）
            paragraphs = [p for p in paragraphs if len(p.text.strip()) > 50]
            content_text = '\n\n'.join([p.text.strip() for p in paragraphs[:20]])  # 最初の20段落

        # メタ情報抽出
        meta_description = None
        meta_tag = soup.find('meta', attrs={'name': 'description'})
        if meta_tag and meta_tag.get('content'):
            meta_description = meta_tag['content']

        result = {
            'url': url,
            'type': 'article',
            'title': title,
            'content': content_text,
            'meta_description': meta_description,
            'word_count': len(content_text.split()) if content_text else 0,
            'extracted_at': datetime.now().isoformat(),
            'status': 'success'
        }

        print(f"  ✅ Extracted: {len(content_text)} chars, {result['word_count']} words")
        return result

    except requests.exceptions.Timeout:
        print(f"  ❌ Timeout: {url[:60]}")
        return {'url': url, 'type': 'article', 'status': 'timeout', 'error': 'Request timeout'}
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error: {str(e)[:60]}")
        return {'url': url, 'type': 'article', 'status': 'error', 'error': str(e)}
    except Exception as e:
        print(f"  ❌ Unexpected error: {str(e)[:60]}")
        return {'url': url, 'type': 'article', 'status': 'error', 'error': str(e)}


def extract_youtube_content(url: str) -> Optional[Dict[str, Any]]:
    """
    YouTube URLから字幕・メタデータを抽出

    Note: 今回は実装スキップ（youtube-transcript-api未インストール）
    """
    print(f"  ⚠️  YouTube extraction not implemented yet: {url[:60]}")
    return {
        'url': url,
        'type': 'youtube',
        'status': 'not_implemented',
        'error': 'YouTube extraction requires youtube-transcript-api'
    }


def extract_pdf_content(url: str) -> Optional[Dict[str, Any]]:
    """
    PDF URLからテキストを抽出

    Note: 今回は実装スキップ（pdfplumber未インストール）
    """
    print(f"  ⚠️  PDF extraction not implemented yet: {url[:60]}")
    return {
        'url': url,
        'type': 'pdf',
        'status': 'not_implemented',
        'error': 'PDF extraction requires pdfplumber'
    }


def extract_content(tweet_details_file: Path, output_file: Path) -> Dict[str, Any]:
    """
    ツイート詳細からリンクのコンテンツを抽出

    Args:
        tweet_details_file: ツイート詳細JSONファイル
        output_file: 出力JSONファイル

    Returns:
        処理結果のメタデータ
    """
    # STEP 1: ツイート詳細データ読み込み
    print(f"📖 Reading tweet details from: {tweet_details_file}")

    try:
        with open(tweet_details_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {tweet_details_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format: {e}")
        sys.exit(1)

    tweet_details = data.get('tweet_details', [])
    print(f"✅ Loaded {len(tweet_details)} tweet details")

    # STEP 2: 全リンクを収集
    all_links = []
    for detail in tweet_details:
        links = detail.get('links', [])
        for link in links:
            link['tweet_id'] = detail['tweet_id']
            link['username'] = detail['username']
            all_links.append(link)

    print(f"\n🔗 Total links to extract: {len(all_links)}")

    if len(all_links) == 0:
        print("⚠️  No links found in tweet details")
        sys.exit(0)

    # リンクタイプ別集計
    link_types = {}
    for link in all_links:
        link_type = link['type']
        link_types[link_type] = link_types.get(link_type, 0) + 1

    print(f"Link types:")
    for link_type, count in sorted(link_types.items()):
        print(f"  - {link_type}: {count}")

    # STEP 3: コンテンツ抽出
    print(f"\n📝 Extracting content from {len(all_links)} links...")

    extracted_contents = []
    success_count = 0
    error_count = 0

    for i, link in enumerate(all_links, 1):
        print(f"\n[{i}/{len(all_links)}] Processing {link['type']}: {link['domain']}")

        link_type = link['type']
        url = link['url']

        # タイプ別に抽出関数を選択
        if link_type == 'article':
            content = extract_article_content(url)
        elif link_type == 'youtube':
            content = extract_youtube_content(url)
        elif link_type == 'pdf':
            content = extract_pdf_content(url)
        else:
            content = {
                'url': url,
                'type': link_type,
                'status': 'unsupported',
                'error': f'Unsupported link type: {link_type}'
            }

        if content:
            content['tweet_id'] = link['tweet_id']
            content['username'] = link['username']
            content['domain'] = link['domain']
            extracted_contents.append(content)

            if content.get('status') == 'success':
                success_count += 1
            else:
                error_count += 1

        # レート制限対策（待機）
        if i < len(all_links):
            wait_time = 2  # 2秒待機
            time.sleep(wait_time)

    # STEP 4: 結果集計
    print(f"\n✅ Content extraction completed")
    print(f"  - Success: {success_count}/{len(all_links)}")
    print(f"  - Errors: {error_count}/{len(all_links)}")

    # STEP 5: 出力ファイル生成
    output_data = {
        'metadata': {
            'processed_at': datetime.now().isoformat(),
            'source_file': tweet_details_file.name,
            'total_links': len(all_links),
            'success_count': success_count,
            'error_count': error_count,
            'link_types': link_types
        },
        'extracted_contents': extracted_contents
    }

    print(f"\n💾 Writing output to: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("✅ Output file created successfully")

    return output_data


def display_summary(output_data: Dict[str, Any]):
    """処理結果のサマリーを表示"""
    metadata = output_data['metadata']
    extracted_contents = output_data['extracted_contents']

    print("\n" + "="*70)
    print("✅ Content extraction completed")
    print("="*70)

    print(f"\n📊 Summary:")
    print(f"  - Total links processed: {metadata['total_links']}")
    print(f"  - Success: {metadata['success_count']}")
    print(f"  - Errors: {metadata['error_count']}")

    if metadata['success_count'] > 0:
        success_rate = metadata['success_count'] / metadata['total_links'] * 100
        print(f"  - Success rate: {success_rate:.1f}%")

    # 成功したコンテンツの統計
    successful_contents = [c for c in extracted_contents if c.get('status') == 'success']

    if successful_contents:
        total_words = sum(c.get('word_count', 0) for c in successful_contents)
        avg_words = total_words / len(successful_contents) if successful_contents else 0

        print(f"\n📝 Content statistics:")
        print(f"  - Total words extracted: {total_words:,}")
        print(f"  - Average words per article: {avg_words:.0f}")

        print(f"\n🏆 Top 3 longest articles:")
        sorted_contents = sorted(successful_contents, key=lambda c: c.get('word_count', 0), reverse=True)
        for i, content in enumerate(sorted_contents[:3], 1):
            title = content.get('title', 'No title')[:50]
            word_count = content.get('word_count', 0)
            print(f"  {i}. {title}... ({word_count} words)")

    print("\n" + "="*70)


def main():
    """メイン処理"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"

    # 最新のtweet_details_ai_ファイルを検索
    tweet_details_files = sorted(
        data_dir.glob("tweet_details_ai_*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    if not tweet_details_files:
        # フォールバック: tweet_details_*.json
        tweet_details_files = sorted(
            data_dir.glob("tweet_details_*.json"),
            key=lambda f: f.stat().st_mtime,
            reverse=True
        )

    if not tweet_details_files:
        print("❌ Error: No tweet_details file found")
        print("   Please run scrape_tweet_details.py first")
        sys.exit(1)

    input_file = tweet_details_files[0]

    # 出力ファイル名生成
    date_str = input_file.stem.replace('tweet_details_', '').replace('tweet_details_ai_', '')
    output_file = data_dir / f"extracted_contents_{date_str}.json"

    # コンテンツ抽出実行
    output_data = extract_content(input_file, output_file)

    # サマリー表示
    display_summary(output_data)


if __name__ == "__main__":
    main()
