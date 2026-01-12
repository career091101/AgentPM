#!/usr/bin/env python3
"""
Scrape Tweet Details Skill Implementation (Playwright Version)
ツイート詳細ページからリンク・リプライを抽出
外国人ツイートを日本語に翻訳
"""

import json
import sys
import time
import random
import requests
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    print("❌ Error: Playwright not installed")
    print("   Install with: pip install playwright && playwright install chromium")
    sys.exit(1)


def classify_link(url: str) -> str:
    """
    URLを記事/YouTube/PDFに分類

    Args:
        url: 分類対象のURL

    Returns:
        "youtube", "pdf", "article", "other"
    """
    url_lower = url.lower()

    # YouTube
    if 'youtube.com' in url_lower or 'youtu.be' in url_lower:
        return 'youtube'

    # PDF（拡張子チェック）
    if url_lower.endswith('.pdf'):
        return 'pdf'

    # 記事サイト
    article_domains = [
        'medium.com', 'note.com', 'zenn.dev', 'qiita.com',
        'hatena.ne.jp', 'hatenablog.com', 'techcrunch.com',
        'theverge.com', 'wired.com', 'arstechnica.com',
        'bloomberg.com', 'reuters.com', 'wsj.com',
        'nikkei.com', 'ascii.jp', 'itmedia.co.jp',
        'github.com', 'arxiv.org', 'news.ycombinator.com'
    ]

    if any(domain in url_lower for domain in article_domains):
        return 'article'

    # Content-TypeでPDF判定
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('Content-Type', '').lower()

        if 'application/pdf' in content_type:
            return 'pdf'
        elif 'text/html' in content_type:
            return 'article'
    except Exception:
        pass

    return 'other'


def expand_shortened_url(url: str) -> str:
    """短縮URLを実URLに展開"""
    shorteners = ['t.co', 'bit.ly', 'tinyurl.com', 'goo.gl', 'ow.ly']

    if any(s in url.lower() for s in shorteners):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.url
        except Exception:
            return url

    return url


def scrape_tweet_details_playwright(top_tweets_file: Path, output_file: Path) -> Dict[str, Any]:
    """
    ツイート詳細を抽出（Playwright実装版）
    """
    print("🌐 Running in PLAYWRIGHT mode (real browser)")

    # STEP 1: 入力データ読み込み
    print(f"\n📖 Reading top tweets from: {top_tweets_file}")

    try:
        with open(top_tweets_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {top_tweets_file}")
        sys.exit(1)

    top_tweets = data.get('top_tweets', [])
    print(f"✅ Loaded {len(top_tweets)} tweets")

    # STEP 2: Cookie認証準備
    cookie_file = top_tweets_file.parent / "x_cookies.json"
    print(f"\n🔐 Loading cookies from: {cookie_file}")

    try:
        with open(cookie_file, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        print(f"✅ Loaded {len(cookies)} cookies")
    except FileNotFoundError:
        print(f"❌ Error: Cookie file not found: {cookie_file}")
        print("   Please create x_cookies.json with auth_token and ct0")
        sys.exit(1)

    # Cookie有効期限チェック
    auth_cookie = next((c for c in cookies if c['name'] == 'auth_token'), None)
    if auth_cookie:
        expires = auth_cookie.get('expires', 0)
        if expires > 0:
            expires_date = datetime.fromtimestamp(expires)
            days_left = (expires_date - datetime.now()).days
            if days_left < 0:
                print(f"⚠️  Warning: auth_token has expired")
            elif days_left < 7:
                print(f"⚠️  Warning: auth_token will expire in {days_left} days")
            else:
                print(f"✅ auth_token valid for {days_left} days")

    tweet_details = []
    errors = []
    success_count = 0

    # STEP 3: Playwright起動
    print(f"\n🚀 Launching Playwright browser...")

    with sync_playwright() as p:
        # ブラウザ起動（ヘッドレスモード）
        browser = p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )

        # コンテキスト作成（User-Agent設定）
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            viewport={'width': 1280, 'height': 720},
            locale='ja-JP',
            timezone_id='Asia/Tokyo'
        )

        # Cookie追加
        context.add_cookies(cookies)

        page = context.new_page()

        print(f"✅ Browser launched successfully")

        # STEP 4-6: ツイート詳細ページ巡回
        print(f"\n🔍 Extracting tweet details from {len(top_tweets)} tweets...")

        for i, tweet in enumerate(top_tweets, start=1):
            tweet_id = tweet['tweet_id']
            username = tweet['username']
            url = f"https://x.com/{username}/status/{tweet_id}"

            print(f"\n  [{i}/{len(top_tweets)}] Processing @{username} (ID: {tweet_id})")

            try:
                # ページ遷移（domcontentloadedで十分）
                print(f"    → Navigating to: {url}")
                page.goto(url, wait_until='domcontentloaded', timeout=60000)

                # 動的コンテンツ読み込み待機（より長めに設定）
                time.sleep(3)  # 3秒待機してJavaScript実行を待つ

                # ツイート要素の待機
                try:
                    page.wait_for_selector('article[data-testid="tweet"]', timeout=15000)
                except PlaywrightTimeout:
                    print(f"    ⚠️  Tweet article not found, trying alternative selector...")
                    # フォールバック: 任意のarticle要素
                    try:
                        page.wait_for_selector('article', timeout=10000)
                    except PlaywrightTimeout:
                        print(f"    ⚠️  No article found, continuing anyway...")
                        pass

                # スクロールしてリプライ読み込み
                page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)  # 2秒待機

                # STEP 4: リンク抽出
                links = []
                try:
                    # ツイート本文内のリンク要素を取得
                    link_elements = page.query_selector_all('article[data-testid="tweet"] a[href^="http"]')

                    for link_elem in link_elements:
                        link_url = link_elem.get_attribute('href')
                        if not link_url:
                            continue

                        # x.com内部リンクをスキップ（ユーザーページ、ステータスページ等）
                        if 'x.com/' in link_url or 'twitter.com/' in link_url:
                            # 写真・動画リンクは除外
                            if '/photo/' in link_url or '/video/' in link_url or '/status/' in link_url:
                                continue

                        # 短縮URL展開
                        expanded_url = expand_shortened_url(link_url)

                        # 分類
                        link_type = classify_link(expanded_url)

                        # タイトル取得試行（link_elemのテキスト）
                        title = link_elem.inner_text().strip() if link_elem.inner_text() else None
                        if not title or len(title) < 3:
                            domain = urlparse(expanded_url).netloc
                            title = f"Content from {domain}"

                        links.append({
                            'url': expanded_url,
                            'type': link_type,
                            'title': title,
                            'domain': urlparse(expanded_url).netloc
                        })

                    # 重複除去
                    seen_urls = set()
                    unique_links = []
                    for link in links:
                        if link['url'] not in seen_urls:
                            seen_urls.add(link['url'])
                            unique_links.append(link)
                    links = unique_links

                    print(f"    ✅ Extracted {len(links)} unique links")

                except Exception as e:
                    print(f"    ⚠️  Link extraction failed: {e}")
                    links = []

                # STEP 5: リプライ抽出
                replies = []
                try:
                    # リプライツイートのDOM要素を取得
                    reply_elements = page.query_selector_all('article[data-testid="tweet"]')

                    # 最初の1件は元ツイート自身なので除外
                    if len(reply_elements) > 1:
                        reply_elements = reply_elements[1:6]  # 上位5件のみ

                    for reply_elem in reply_elements:
                        try:
                            # ユーザー名
                            user_elem = reply_elem.query_selector('[data-testid="User-Name"] a')
                            reply_username = user_elem.inner_text().split('\n')[0].replace('@', '') if user_elem else 'unknown'

                            # リプライテキスト
                            text_elem = reply_elem.query_selector('[data-testid="tweetText"]')
                            reply_text = text_elem.inner_text() if text_elem else ''

                            # いいね数
                            like_elem = reply_elem.query_selector('[data-testid="like"]')
                            likes_text = like_elem.get_attribute('aria-label') if like_elem else '0'
                            # aria-labelから数値抽出（例: "123 Likes" → 123）
                            likes = 0
                            if likes_text:
                                import re
                                match = re.search(r'(\d+)', likes_text)
                                if match:
                                    likes = int(match.group(1))

                            # タイムスタンプ
                            time_elem = reply_elem.query_selector('time')
                            created_at = time_elem.get_attribute('datetime') if time_elem else datetime.now().isoformat()

                            replies.append({
                                'username': reply_username,
                                'text': reply_text,
                                'likes': likes,
                                'created_at': created_at
                            })

                        except Exception as e:
                            print(f"    ⚠️  Failed to parse reply: {e}")
                            continue

                    print(f"    ✅ Extracted {len(replies)} replies")

                except Exception as e:
                    print(f"    ⚠️  Reply extraction failed: {e}")
                    replies = []

                # STEP 6: メタデータ取得
                metadata = {
                    'has_media': False,
                    'media_count': 0,
                    'has_video': False,
                    'view_count': None,
                    'is_thread': False
                }

                try:
                    # メディア要素チェック
                    photo_elems = page.query_selector_all('[data-testid="tweetPhoto"]')
                    metadata['has_media'] = len(photo_elems) > 0
                    metadata['media_count'] = len(photo_elems)

                    # 動画チェック
                    video_elem = page.query_selector('video')
                    metadata['has_video'] = video_elem is not None

                    # ビュー数
                    view_elem = page.query_selector('[data-testid="app-text-transition-container"]')
                    if view_elem:
                        metadata['view_count'] = view_elem.inner_text()

                except Exception as e:
                    print(f"    ⚠️  Metadata extraction failed: {e}")

                # データ統合
                tweet_detail = {
                    'tweet_id': tweet_id,
                    'username': username,
                    'url': url,
                    'engagement_score': tweet.get('engagement_score', 0),
                    'is_japanese': tweet.get('is_japanese', True),  # 日本人判定フラグを引き継ぎ
                    'links': links,
                    'replies': replies,
                    'metadata': metadata
                }

                tweet_details.append(tweet_detail)
                success_count += 1

                print(f"    ✅ Successfully extracted details")

                # レート制限回避（ランダム待機）
                if i < len(top_tweets):
                    wait_time = random.uniform(3, 5)
                    print(f"    ⏳ Waiting {wait_time:.1f}s before next tweet...")
                    time.sleep(wait_time)

            except PlaywrightTimeout as e:
                error_msg = f"Timeout loading page: {str(e)}"
                print(f"    ❌ {error_msg}")
                errors.append({
                    'tweet_id': tweet_id,
                    'error_type': 'PlaywrightTimeout',
                    'error_message': error_msg,
                    'url': url
                })
                continue

            except Exception as e:
                error_msg = str(e)
                print(f"    ❌ Error: {error_msg}")
                errors.append({
                    'tweet_id': tweet_id,
                    'error_type': type(e).__name__,
                    'error_message': error_msg,
                    'url': url
                })
                continue

        # ブラウザクローズ
        browser.close()
        print(f"\n✅ Browser closed")

    # STEP 7: データ統合・出力
    output_data = {
        'metadata': {
            'processed_at': datetime.now().isoformat(),
            'source_file': top_tweets_file.name,
            'total_tweets_processed': len(top_tweets),
            'success_count': success_count,
            'error_count': len(errors),
            'mode': 'Playwright (real browser)'
        },
        'tweet_details': tweet_details,
        'errors': errors
    }

    print(f"\n💾 Writing output to: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("✅ Output file created successfully")

    # STEP 8: 品質検証
    print("\n✅ Quality validation:")
    print(f"  - Total tweets processed: {success_count}/{len(top_tweets)}")
    if len(top_tweets) > 0:
        success_rate = success_count / len(top_tweets) * 100
        print(f"  - Success rate: {success_rate:.1f}%")

    link_count = sum(len(td['links']) for td in tweet_details)
    print(f"  - Total links extracted: {link_count}")

    reply_count = sum(len(td['replies']) for td in tweet_details)
    print(f"  - Total replies extracted: {reply_count}")

    if errors:
        print(f"  - Errors: {len(errors)}")
        for err in errors[:3]:
            print(f"    - {err['tweet_id']}: {err['error_type']}")

    print("\nℹ️  Translation will be performed by ClaudeCode LLM (not by API)")

    return output_data


def display_summary(output_data: Dict[str, Any]):
    """処理結果のサマリーを表示"""
    metadata = output_data['metadata']
    tweet_details = output_data['tweet_details']

    print("\n" + "="*60)
    print("✅ Tweet details extracted successfully")
    print("="*60)

    print(f"\n📊 Summary:")
    print(f"  - Total tweets processed: {metadata['success_count']}/{metadata['total_tweets_processed']}")
    if metadata['total_tweets_processed'] > 0:
        success_rate = metadata['success_count'] / metadata['total_tweets_processed'] * 100
        print(f"  - Success rate: {success_rate:.1f}%")
    print(f"  - Mode: {metadata.get('mode', 'Unknown')}")

    # リンク統計
    all_links = []
    for td in tweet_details:
        all_links.extend(td['links'])

    if all_links:
        link_types = {}
        for link in all_links:
            link_type = link['type']
            link_types[link_type] = link_types.get(link_type, 0) + 1

        print(f"  - Total links extracted: {len(all_links)}")
        for link_type, count in sorted(link_types.items(), key=lambda x: x[1], reverse=True):
            percentage = count / len(all_links) * 100
            print(f"    - {link_type.capitalize()}: {count} ({percentage:.1f}%)")

    # リプライ統計
    all_replies = []
    for td in tweet_details:
        all_replies.extend(td['replies'])

    if all_replies:
        print(f"  - Total replies extracted: {len(all_replies)} (avg {len(all_replies)/max(len(tweet_details),1):.1f}/tweet)")

        if all_replies:
            avg_likes = sum(r['likes'] for r in all_replies) / len(all_replies)
            print(f"  - Average likes per reply: {avg_likes:.1f}")

    # エラー
    if metadata.get('error_count', 0) > 0:
        print(f"  - Errors: {metadata['error_count']}")

    print(f"  - Output file: {metadata['source_file'].replace('top_10_tweets', 'tweet_details')}")

    # Link Breakdown by Tweet
    if tweet_details:
        print(f"\n🔗 Link Breakdown by Tweet:")
        for i, td in enumerate(tweet_details[:5], start=1):
            link_count = len(td['links'])
            link_types_str = ', '.join([f"{l['type']}" for l in td['links']])
            print(f"  - Tweet {i} (@{td['username']}): {link_count} link(s) ({link_types_str if link_types_str else 'none'})")

    print("\n" + "="*60)


def main():
    """メイン処理"""
    # デフォルトパス設定
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"

    # 最新のtop_10_tweetsファイルを検索
    top_tweets_files = sorted(data_dir.glob("top_10_tweets_*.json"), key=lambda f: f.stat().st_mtime, reverse=True)

    if not top_tweets_files:
        print("❌ Error: No top_10_tweets file found")
        print("   Please run extract_top_tweets.py first")
        sys.exit(1)

    input_file = top_tweets_files[0]

    # 出力ファイル名生成
    date_str = input_file.stem.replace('top_10_tweets_', '')
    output_file = data_dir / f"tweet_details_{date_str}.json"

    # Playwright実装版実行
    output_data = scrape_tweet_details_playwright(input_file, output_file)

    # サマリー表示
    display_summary(output_data)


if __name__ == "__main__":
    main()
