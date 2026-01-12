#!/usr/bin/env python3
"""
X (Twitter) Bookmark Scraper

このスクリプトはPlaywrightを使用してX(Twitter)のブックマークを自動取得し、JSON形式で保存します。

必要な環境変数:
- X_USERNAME: Xのユーザー名またはメールアドレス
- X_PASSWORD: Xのパスワード

使用方法:
1. .envファイルに認証情報を設定
2. python3 x_bookmark_scraper.py を実行
3. 初回のみブラウザが起動するので、手動でログイン
4. ログイン成功後、自動的にブックマークを取得開始
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
LOG_FILE = SCRIPTS_DIR / "x_bookmark_scraper.log"
OUTPUT_FILE = OUTPUT_DIR / "x_bookmarks_data.json"

BOOKMARKS_URL = "https://x.com/i/bookmarks"
SCROLL_PAUSE_TIME = 1.5  # スクロール間隔（秒）
MAX_SCROLL_ATTEMPTS = 100  # 最大スクロール回数
BATCH_SAVE_INTERVAL = 50  # 50件ごとに中間保存

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

def extract_tweet_data(article_element):
    """
    article要素から投稿データを抽出

    Args:
        article_element: BeautifulSoup article element

    Returns:
        dict: 投稿データ（ID, テキスト, 投稿者, 日時, エンゲージメント）
    """
    try:
        # 投稿URL抽出（Status IDを含む）
        link_elem = article_element.find('a', href=re.compile(r'/status/\d+'))
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
        # Xの投稿テキストは通常 data-testid="tweetText" に含まれる
        tweet_text_elem = article_element.find('div', {'data-testid': 'tweetText'})
        tweet_text = tweet_text_elem.get_text(strip=True) if tweet_text_elem else ""

        # 投稿者情報抽出
        # ユーザー名（表示名）
        author_name_elem = article_element.find('div', {'data-testid': 'User-Name'})
        author_name = ""
        author_username = ""

        if author_name_elem:
            # 表示名とユーザー名（@xxx）を含むテキストから抽出
            full_text = author_name_elem.get_text(strip=True)
            # 通常のパターン: "Display Name@username·時間"
            parts = full_text.split('@')
            if len(parts) >= 2:
                author_name = parts[0].strip()
                username_part = parts[1].split('·')[0].strip() if '·' in parts[1] else parts[1].strip()
                author_username = username_part

        # 投稿日時抽出
        time_elem = article_element.find('time')
        posted_at = time_elem.get('datetime', '') if time_elem else ""

        # エンゲージメント指標抽出
        # Xの各指標は特定のaria-labelまたはdata-testidで識別される
        engagement = {
            "replies": 0,
            "retweets": 0,
            "likes": 0,
            "bookmarks": 0,
            "views": 0
        }

        # 返信数（Reply）
        reply_elem = article_element.find('button', {'data-testid': 'reply'})
        if reply_elem:
            aria_label = reply_elem.get('aria-label', '')
            match = re.search(r'(\d+)', aria_label)
            if match:
                engagement['replies'] = int(match.group(1))

        # リツイート数（Retweet）
        retweet_elem = article_element.find('button', {'data-testid': 'retweet'})
        if retweet_elem:
            aria_label = retweet_elem.get('aria-label', '')
            match = re.search(r'(\d+)', aria_label)
            if match:
                engagement['retweets'] = int(match.group(1))

        # いいね数（Like）
        like_elem = article_element.find('button', {'data-testid': 'like'})
        if like_elem:
            aria_label = like_elem.get('aria-label', '')
            match = re.search(r'(\d+)', aria_label)
            if match:
                engagement['likes'] = int(match.group(1))

        # ブックマーク数（通常は表示されないが、エクスポートデータには含まれる場合がある）
        bookmark_elem = article_element.find('button', {'data-testid': 'bookmark'})
        if bookmark_elem:
            aria_label = bookmark_elem.get('aria-label', '')
            match = re.search(r'(\d+)', aria_label)
            if match:
                engagement['bookmarks'] = int(match.group(1))

        # ビュー数（X Premiumユーザーは表示される）
        # ビュー数は通常、特定のspan要素に含まれる
        view_elems = article_element.find_all('span', string=re.compile(r'[\d,]+\s*ビュー'))
        if view_elems:
            for elem in view_elems:
                view_text = elem.get_text(strip=True)
                match = re.search(r'([\d,]+)', view_text)
                if match:
                    engagement['views'] = int(match.group(1).replace(',', ''))
                    break

        return {
            "id": status_id,
            "text": tweet_text,
            "author_name": author_name,
            "author_username": author_username,
            "author_url": f"https://x.com/{author_username}" if author_username else "",
            "posted_at": posted_at,
            "engagement": engagement,
            "url": tweet_url,
            "scraped_at": datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"Error extracting tweet data: {e}")
        return None

async def scroll_and_collect(page, max_scrolls=MAX_SCROLL_ATTEMPTS):
    """
    ページをスクロールしながらブックマークを収集

    Args:
        page: Playwright page object
        max_scrolls: 最大スクロール回数

    Returns:
        list: 収集した投稿データのリスト
    """
    bookmarks = []
    seen_ids = set()
    no_new_content_count = 0

    logger.info("ブックマークの収集を開始します...")

    # 初回は長めに待機（ページ読み込み完了を待つ）
    logger.info("ページの読み込みを待機中...")
    await asyncio.sleep(5)

    # article要素が表示されるまで待機（最大30秒）
    try:
        await page.wait_for_selector('article[data-testid="tweet"]', timeout=30000)
        logger.info("投稿要素を検出しました")
    except Exception as e:
        logger.warning(f"article要素の待機がタイムアウト: {e}")
        logger.info("代替セレクターを試します...")

        # 代替: JavaScriptで直接取得
        try:
            await page.wait_for_selector('article', timeout=10000)
            logger.info("article要素（汎用）を検出しました")
        except Exception as e2:
            logger.error(f"article要素が全く見つかりません: {e2}")

    for scroll_count in range(max_scrolls):
        # Playwrightの$$でarticle要素を直接取得
        article_elements = await page.query_selector_all('article')

        logger.info(f"スクロール {scroll_count + 1}: article要素数 = {len(article_elements)}")

        new_tweets_count = 0

        for article_elem in article_elements:
            try:
                # 「さらに表示」ボタンをクリックして全文展開（改善版）
                try:
                    # クリック前のテキスト長を記録
                    text_before = await article_elem.inner_text()
                    initial_length = len(text_before)

                    # 複数の「さらに表示」ボタンを順次クリック（最大3回）
                    for attempt in range(3):
                        show_more_button = await article_elem.query_selector('div[role="button"]:has-text("さらに表示"), div[role="button"]:has-text("Show more"), span:has-text("さらに表示"), span:has-text("Show more")')

                        if show_more_button:
                            # ボタンをクリック
                            await show_more_button.click()
                            logger.debug(f"「さらに表示」ボタンをクリック（試行{attempt+1}回目）")

                            # DOM更新とネットワークリクエストの完了を待つ
                            await asyncio.sleep(1.5)  # 0.5秒 → 1.5秒に延長

                            # テキスト長の変化を確認
                            text_after = await article_elem.inner_text()
                            new_length = len(text_after)

                            if new_length > initial_length:
                                logger.debug(f"テキスト展開成功: {initial_length}文字 → {new_length}文字 (+{new_length-initial_length})")
                                initial_length = new_length  # 次回のために更新
                            else:
                                # 変化がなければループ終了
                                break
                        else:
                            # ボタンが見つからなければ終了
                            break

                except Exception as e:
                    # ボタンがない場合は無視（全文表示されている）
                    logger.debug(f"さらに表示ボタンなし or クリック失敗（問題なし）: {e}")
                    pass

                # article要素のHTMLを取得（展開後）
                article_html = await article_elem.inner_html()
                soup = BeautifulSoup(article_html, 'html.parser')

                # ダミーのarticleタグで囲む（extract_tweet_data用）
                article_soup = BeautifulSoup(f'<article data-testid="tweet">{article_html}</article>', 'html.parser')
                article = article_soup.find('article')

                tweet_data = extract_tweet_data(article)
                if tweet_data and tweet_data['id'] not in seen_ids:
                    seen_ids.add(tweet_data['id'])
                    bookmarks.append(tweet_data)
                    new_tweets_count += 1

                    # デバッグ: 最初の投稿のテキストを表示
                    if len(bookmarks) == 1:
                        logger.info(f"  最初の投稿: {tweet_data['text'][:50]}...")

            except Exception as e:
                logger.debug(f"投稿抽出エラー（スキップ）: {e}")
                continue

        if new_tweets_count > 0:
            logger.info(f"スクロール {scroll_count + 1}: 新規 {new_tweets_count} 件取得（累計 {len(bookmarks)} 件）")
            no_new_content_count = 0

            # 中間保存
            if len(bookmarks) % BATCH_SAVE_INTERVAL == 0:
                save_bookmarks(bookmarks, partial=True)
        else:
            no_new_content_count += 1
            logger.info(f"スクロール {scroll_count + 1}: 新規取得なし（連続 {no_new_content_count} 回）")

            # 5回連続で新規取得がなければ終了
            if no_new_content_count >= 5:
                logger.info("新規コンテンツが見つからないため、スクロールを終了します")
                break

        # 下にスクロール
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(SCROLL_PAUSE_TIME)

        # ページの高さをチェック（変化がなければ終了）
        new_height = await page.evaluate("document.body.scrollHeight")
        if scroll_count > 0:
            prev_height = await page.evaluate("window.scrollY")
            if new_height == prev_height:
                logger.info("ページの最後に到達しました")
                break

    logger.info(f"ブックマーク収集完了: 合計 {len(bookmarks)} 件")
    return bookmarks

def save_bookmarks(bookmarks, partial=False):
    """
    ブックマークデータをJSON形式で保存

    Args:
        bookmarks: 投稿データのリスト
        partial: 中間保存フラグ
    """
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        output_data = {
            "metadata": {
                "scrape_date": datetime.now().isoformat(),
                "total_bookmarks": len(bookmarks),
                "scrape_duration_seconds": 0,  # メイン関数で更新
                "is_partial": partial
            },
            "bookmarks": bookmarks
        }

        filename = OUTPUT_FILE if not partial else OUTPUT_DIR / "x_bookmarks_data_partial.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        logger.info(f"{'中間' if partial else '最終'}保存完了: {filename} ({len(bookmarks)} 件)")

    except Exception as e:
        logger.error(f"保存エラー: {e}")

async def auto_login(page, username, password):
    """
    自動ログイン処理

    Args:
        page: Playwright page object
        username: ユーザー名
        password: パスワード

    Returns:
        bool: ログイン成功フラグ
    """
    try:
        logger.info("自動ログインを試みます...")

        # ログインページかどうか確認
        current_url = page.url
        if 'login' not in current_url.lower():
            logger.info("既にログイン済みです")
            return True

        # ユーザー名入力フィールドを待機
        await page.wait_for_selector('input[autocomplete="username"]', timeout=10000)
        logger.info("ユーザー名を入力中...")

        # ユーザー名入力
        await page.fill('input[autocomplete="username"]', username)
        await asyncio.sleep(1)

        # 次へボタンをクリック
        next_button = await page.query_selector('button:has-text("次へ"), button:has-text("Next")')
        if next_button:
            await next_button.click()
            logger.info("「次へ」をクリックしました")
            await asyncio.sleep(2)

        # パスワード入力フィールドを待機
        await page.wait_for_selector('input[name="password"], input[type="password"]', timeout=10000)
        logger.info("パスワードを入力中...")

        # パスワード入力
        await page.fill('input[name="password"], input[type="password"]', password)
        await asyncio.sleep(1)

        # ログインボタンをクリック
        login_button = await page.query_selector('button[data-testid="LoginForm_Login_Button"]')
        if not login_button:
            login_button = await page.query_selector('button:has-text("ログイン"), button:has-text("Log in")')

        if login_button:
            await login_button.click()
            logger.info("ログインボタンをクリックしました")
            await asyncio.sleep(5)

            # ログイン成功を確認
            current_url = page.url
            if 'home' in current_url or 'bookmarks' in current_url:
                logger.info("自動ログイン成功！")
                return True
            else:
                logger.warning(f"ログイン後のURL確認: {current_url}")
                return True  # 一旦成功とみなす

        else:
            logger.error("ログインボタンが見つかりません")
            return False

    except Exception as e:
        logger.error(f"自動ログインエラー: {e}")
        return False

async def wait_for_login(page, max_wait_minutes=5):
    """
    ログイン完了を待機

    Args:
        page: Playwright page object
        max_wait_minutes: 最大待機時間（分）

    Returns:
        bool: ログイン成功フラグ
    """
    max_retries = max_wait_minutes * 12  # 5秒ごとにチェック

    logger.info("ブラウザが起動しました")

    for i in range(max_retries):
        content = await page.content()

        # ブックマークページのインジケーター
        # 1. URLが正しい
        # 2. "ブックマーク" テキストが存在
        # 3. タイムライン要素が存在
        current_url = page.url

        if 'bookmarks' in current_url and ('ブックマーク' in content or 'Bookmarks' in content):
            logger.info("ログイン成功！ブックマークページを検出しました")
            return True

        if (i + 1) % 12 == 0:  # 1分ごとにメッセージ
            logger.info(f"ログイン待機中... ({(i + 1) // 12}/{max_wait_minutes}分経過)")

        await asyncio.sleep(5)

    logger.error(f"タイムアウト: {max_wait_minutes}分以内にログインが確認できませんでした")
    return False

async def main():
    """
    メイン処理
    """
    start_time = datetime.now()

    # 認証情報のチェック
    x_username = os.getenv('X_USERNAME')
    x_password = os.getenv('X_PASSWORD')

    if not x_username or not x_password:
        logger.warning(".envファイルにX_USERNAMEとX_PASSWORDが設定されていません")
        logger.info("手動ログインを使用します（Cookieは保存されます）")

    # ディレクトリ作成
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        # Persistent contextを使用してCookieを保存
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,  # 手動ログイン用にブラウザを表示
            slow_mo=50,
            args=[
                '--disable-blink-features=AutomationControlled',  # bot検出回避
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )

        page = await browser.new_page()

        # ブックマークページに遷移
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

        # ログイン待機
        logged_in = await wait_for_login(page, max_wait_minutes=5)

        if not logged_in:
            logger.error("ログインに失敗しました。スクリプトを終了します。")
            await browser.close()
            return

        # ブックマーク収集開始
        await asyncio.sleep(2)  # ページ読み込み待機

        bookmarks = await scroll_and_collect(page)

        # 最終保存
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        # メタデータ更新
        output_data = {
            "metadata": {
                "scrape_date": start_time.isoformat(),
                "total_bookmarks": len(bookmarks),
                "scrape_duration_seconds": int(duration),
                "script_version": "1.0.0"
            },
            "bookmarks": bookmarks
        }

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        logger.info("=" * 60)
        logger.info("ブックマークスクレイピング完了！")
        logger.info(f"保存先: {OUTPUT_FILE}")
        logger.info(f"取得件数: {len(bookmarks)} 件")
        logger.info(f"実行時間: {int(duration)} 秒（{duration / 60:.1f} 分）")
        logger.info("=" * 60)

        await browser.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("ユーザーによって中断されました")
    except Exception as e:
        logger.error(f"予期しないエラー: {e}", exc_info=True)
