#!/usr/bin/env python3
"""
X (Twitter) Bookmark Scraper (Full Text Version)

「さらに表示」ボタンを展開して全文を取得するバージョン

必要な環境変数:
- X_USERNAME: Xのユーザー名またはメールアドレス
- X_PASSWORD: Xのパスワード

使用方法:
1. .envファイルに認証情報を設定
2. python3 x_bookmark_scraper_fulltext.py を実行
"""

import asyncio
import os
import json
import logging
import re
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# Configuration
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0")
SCRIPTS_DIR = BASE_DIR / "scripts"
OUTPUT_DIR = BASE_DIR / "Flow" / "202512" / "2025-12-31"
USER_DATA_DIR = SCRIPTS_DIR / "x_scraper_user_data"
LOG_FILE = SCRIPTS_DIR / "x_bookmark_scraper_fulltext.log"
OUTPUT_FILE = OUTPUT_DIR / "x_bookmarks_fulltext.json"

BOOKMARKS_URL = "https://x.com/i/bookmarks"
SCROLL_PAUSE_TIME = 2.0  # スクロール間隔（少し長めに）
MAX_SCROLL_ATTEMPTS = 100
BATCH_SAVE_INTERVAL = 50

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def expand_show_more_buttons(article_elem):
    """
    article要素内の「さらに表示」ボタンを全て展開

    Args:
        article_elem: Playwright article element

    Returns:
        bool: 展開した場合True
    """
    try:
        # 「さらに表示」「Show more」ボタンを検出
        # data-testid="tweet-text-show-more-link" が使われることが多い
        show_more_buttons = await article_elem.query_selector_all('[data-testid="tweet-text-show-more-link"]')

        if not show_more_buttons:
            # 代替: テキストで検出
            show_more_buttons = await article_elem.query_selector_all('span:has-text("さらに表示")')

        if not show_more_buttons:
            show_more_buttons = await article_elem.query_selector_all('span:has-text("Show more")')

        if show_more_buttons:
            for button in show_more_buttons:
                try:
                    await button.click(timeout=1000)
                    await asyncio.sleep(0.3)  # 展開を待機
                    logger.debug("「さらに表示」ボタンを展開しました")
                except Exception as e:
                    logger.debug(f"ボタンクリック失敗（スキップ）: {e}")
                    continue
            return True

        return False

    except Exception as e:
        logger.debug(f"さらに表示ボタン展開エラー: {e}")
        return False

def extract_tweet_data(article_soup):
    """
    article要素から投稿データを抽出

    Args:
        article_soup: BeautifulSoup article element

    Returns:
        dict: 投稿データ
    """
    try:
        # 投稿URL抽出
        link_elem = article_soup.find('a', href=re.compile(r'/status/\d+'))
        if not link_elem:
            return None

        tweet_url = link_elem.get('href', '')
        if not tweet_url.startswith('http'):
            tweet_url = f"https://x.com{tweet_url}"

        # Status ID抽出
        status_id_match = re.search(r'/status/(\d+)', tweet_url)
        status_id = status_id_match.group(1) if status_id_match else None

        if not status_id:
            return None

        # 投稿テキスト抽出
        tweet_text_elem = article_soup.find('div', {'data-testid': 'tweetText'})
        tweet_text = tweet_text_elem.get_text(strip=True) if tweet_text_elem else ""

        # 投稿者情報抽出
        author_name_elem = article_soup.find('div', {'data-testid': 'User-Name'})
        author_name = ""
        author_username = ""

        if author_name_elem:
            full_text = author_name_elem.get_text(strip=True)
            parts = full_text.split('@')
            if len(parts) >= 2:
                author_name = parts[0].strip()
                username_part = parts[1].split('·')[0].strip() if '·' in parts[1] else parts[1].strip()
                author_username = f"@{username_part}"

        # 日時抽出
        time_elem = article_soup.find('time')
        tweet_date = time_elem.get('datetime', '') if time_elem else ""

        # エンゲージメント抽出
        engagement = {
            'likes': 0,
            'retweets': 0,
            'replies': 0,
            'views': 0
        }

        # いいね数
        like_elem = article_soup.find('button', {'data-testid': 'like'})
        if like_elem:
            like_text = like_elem.get_text(strip=True)
            like_match = re.search(r'(\d+(?:,\d+)*)', like_text)
            if like_match:
                engagement['likes'] = int(like_match.group(1).replace(',', ''))

        # リツイート数
        retweet_elem = article_soup.find('button', {'data-testid': 'retweet'})
        if retweet_elem:
            retweet_text = retweet_elem.get_text(strip=True)
            retweet_match = re.search(r'(\d+(?:,\d+)*)', retweet_text)
            if retweet_match:
                engagement['retweets'] = int(retweet_match.group(1).replace(',', ''))

        return {
            'id': status_id,
            'url': tweet_url,
            'text': tweet_text,
            'author_name': author_name,
            'author_username': author_username,
            'date': tweet_date,
            'engagement': engagement
        }

    except Exception as e:
        logger.debug(f"投稿データ抽出エラー: {e}")
        return None

async def auto_login(page, username, password):
    """
    自動ログイン処理
    """
    try:
        logger.info("自動ログインを試みます...")

        # ユーザー名入力
        await page.wait_for_selector('input[autocomplete="username"]', timeout=10000)
        await page.fill('input[autocomplete="username"]', username)
        await asyncio.sleep(1)

        # 次へボタンクリック
        next_button = await page.query_selector('button:has-text("次へ"), button:has-text("Next")')
        if next_button:
            await next_button.click()
            await asyncio.sleep(2)

        # パスワード入力
        await page.wait_for_selector('input[name="password"], input[type="password"]', timeout=10000)
        await page.fill('input[name="password"], input[type="password"]', password)
        await asyncio.sleep(1)

        # ログインボタンクリック
        login_button = await page.query_selector('button[data-testid="LoginForm_Login_Button"]')
        if login_button:
            await login_button.click()
            await asyncio.sleep(5)
            return True

        return False

    except Exception as e:
        logger.error(f"自動ログイン失敗: {e}")
        return False

async def scroll_and_collect_fulltext(page, max_scrolls=MAX_SCROLL_ATTEMPTS):
    """
    スクロールしながらブックマークを収集（全文展開版）
    """
    bookmarks = []
    seen_ids = set()
    no_new_content_count = 0

    # 初回ページ読み込み待機
    logger.info("ページの読み込みを待機中...")
    await asyncio.sleep(5)

    # article要素が表示されるまで待機
    try:
        await page.wait_for_selector('article[data-testid="tweet"]', timeout=30000)
        logger.info("投稿要素を検出しました")
    except Exception as e:
        logger.warning(f"article要素の待機がタイムアウト: {e}")
        try:
            await page.wait_for_selector('article', timeout=10000)
            logger.info("article要素（汎用）を検出しました")
        except Exception as e2:
            logger.error(f"article要素が全く見つかりません: {e2}")

    for scroll_count in range(max_scrolls):
        # article要素を取得
        article_elements = await page.query_selector_all('article')

        logger.info(f"スクロール {scroll_count + 1}: article要素数 = {len(article_elements)}")

        new_tweets_count = 0
        expanded_count = 0

        for article_elem in article_elements:
            try:
                # ★ 重要: 「さらに表示」ボタンを展開
                was_expanded = await expand_show_more_buttons(article_elem)
                if was_expanded:
                    expanded_count += 1
                    await asyncio.sleep(0.2)  # 展開後の待機

                # 展開後のHTMLを取得
                article_html = await article_elem.inner_html()
                soup = BeautifulSoup(article_html, 'html.parser')

                # ダミーのarticleタグで囲む
                article_soup = BeautifulSoup(f'<article data-testid="tweet">{article_html}</article>', 'html.parser')
                article = article_soup.find('article')

                tweet_data = extract_tweet_data(article)
                if tweet_data and tweet_data['id'] not in seen_ids:
                    seen_ids.add(tweet_data['id'])
                    bookmarks.append(tweet_data)
                    new_tweets_count += 1

                    # デバッグ: 最初の投稿のテキストを表示
                    if len(bookmarks) == 1:
                        logger.info(f"  最初の投稿（{len(tweet_data['text'])}文字）: {tweet_data['text'][:80]}...")

            except Exception as e:
                logger.debug(f"投稿抽出エラー（スキップ）: {e}")
                continue

        if expanded_count > 0:
            logger.info(f"  → {expanded_count}件の投稿で「さらに表示」を展開しました")

        if new_tweets_count > 0:
            logger.info(f"スクロール {scroll_count + 1}: 新規 {new_tweets_count} 件取得（累計 {len(bookmarks)} 件）")
            no_new_content_count = 0

            # 中間保存
            if len(bookmarks) % BATCH_SAVE_INTERVAL == 0:
                save_bookmarks(bookmarks)
        else:
            no_new_content_count += 1
            logger.info(f"スクロール {scroll_count + 1}: 新規取得なし（連続 {no_new_content_count} 回）")

        # 連続5回新規コンテンツがない場合は終了
        if no_new_content_count >= 5:
            logger.info("新規コンテンツが見つからないため、スクロールを終了します")
            break

        # スクロール実行
        await page.evaluate("window.scrollBy(0, window.innerHeight)")
        await asyncio.sleep(SCROLL_PAUSE_TIME)

    logger.info(f"ブックマーク収集完了: 合計 {len(bookmarks)} 件")
    return bookmarks

def save_bookmarks(bookmarks):
    """
    ブックマークをJSON形式で保存
    """
    output_data = {
        'metadata': {
            'scrape_date': datetime.now().isoformat(),
            'total_bookmarks': len(bookmarks),
            'version': 'fulltext'
        },
        'bookmarks': bookmarks
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    logger.info(f"ブックマークを保存しました: {OUTPUT_FILE}")

async def main():
    """
    メイン処理
    """
    # 環境変数から認証情報取得
    x_username = os.getenv('X_USERNAME')
    x_password = os.getenv('X_PASSWORD')

    if not x_username or not x_password:
        logger.error("環境変数 X_USERNAME, X_PASSWORD が設定されていません")
        return

    logger.info("=== Xブックマークスクレイピング開始（全文版） ===")
    logger.info(f"出力ファイル: {OUTPUT_FILE}")

    async with async_playwright() as p:
        # 永続的なブラウザコンテキストを起動
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            slow_mo=50
        )

        page = await browser.new_page()

        # ブックマークページに移動
        logger.info(f"ブックマークページに移動: {BOOKMARKS_URL}")
        await page.goto(BOOKMARKS_URL, wait_until='domcontentloaded')
        await asyncio.sleep(3)

        # 自動ログイン試行
        if x_username and x_password:
            login_success = await auto_login(page, x_username, x_password)

            if login_success:
                # ブックマークページに再移動
                logger.info(f"ブックマークページに移動: {BOOKMARKS_URL}")
                await page.goto(BOOKMARKS_URL, wait_until='domcontentloaded')
                await asyncio.sleep(3)

        # ブックマーク収集（全文展開版）
        bookmarks = await scroll_and_collect_fulltext(page)

        # 最終保存
        save_bookmarks(bookmarks)

        # 統計情報表示
        logger.info("=== 収集統計 ===")
        logger.info(f"総ブックマーク数: {len(bookmarks)}")

        if bookmarks:
            lengths = [len(b['text']) for b in bookmarks]
            logger.info(f"平均文字数: {sum(lengths)/len(lengths):.1f}文字")
            logger.info(f"最長文字数: {max(lengths)}文字")
            logger.info(f"最短文字数: {min(lengths)}文字")

            # 280文字以上の投稿数をカウント
            long_tweets = [b for b in bookmarks if len(b['text']) > 280]
            logger.info(f"280文字超の投稿: {len(long_tweets)}件 ({len(long_tweets)/len(bookmarks)*100:.1f}%)")

        await browser.close()

        logger.info("=== スクレイピング完了 ===")

if __name__ == "__main__":
    asyncio.run(main())
