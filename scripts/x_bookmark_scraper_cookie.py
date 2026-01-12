#!/usr/bin/env python3
"""
X (Twitter) Bookmark Scraper using Cookie File

このスクリプトはcookieファイルを使用してX(Twitter)のブックマークを取得し、テキスト形式で保存します。

使用方法:
1. x_cookies.txtにcookieファイルを配置
2. python3 x_bookmark_scraper_cookie.py を実行
3. x_bookmarks_sample.txtにテキスト形式で保存
"""

import requests
import json
import logging
import re
from pathlib import Path
from datetime import datetime
import http.cookiejar
import time

# Configuration
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0")
SCRIPTS_DIR = BASE_DIR / "scripts"
OUTPUT_DIR = BASE_DIR / "Flow" / "202512" / "2025-12-31"
COOKIE_FILE = SCRIPTS_DIR / "x_cookies.txt"
OUTPUT_FILE = OUTPUT_DIR / "x_bookmarks_sample.txt"
JSON_OUTPUT_FILE = OUTPUT_DIR / "x_bookmarks_data.json"
LOG_FILE = SCRIPTS_DIR / "x_bookmark_scraper_cookie.log"

BOOKMARKS_URL = "https://x.com/i/api/graphql/JlLLvsgDPY_xqGksAL4Dtw/Bookmarks"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
MAX_REQUESTS = 5  # 最大リクエスト数（ページネーション）
REQUEST_DELAY = 2  # リクエスト間隔（秒）

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

def load_cookies_from_file(cookie_file):
    """
    Netscape形式のcookieファイルを読み込み、requests用のCookieJarに変換

    Args:
        cookie_file: cookieファイルのパス

    Returns:
        requests.cookies.RequestsCookieJar
    """
    try:
        requests_cookie_jar = requests.cookies.RequestsCookieJar()

        with open(cookie_file, 'r') as f:
            for line in f:
                line = line.strip()

                # コメント行やヘッダー行をスキップ
                if not line or line.startswith('#'):
                    continue

                # タブまたは複数スペースで分割
                parts = re.split(r'\s+', line)

                if len(parts) < 7:
                    continue

                domain, flag, path, secure, expires, name, value = parts[:7]

                # 値が複数パートに分かれている場合（引用符内のスペース等）
                if len(parts) > 7:
                    value = ' '.join(parts[6:])

                # 引用符を除去
                value = value.strip('"')

                # Cookieを追加
                requests_cookie_jar.set(
                    name=name,
                    value=value,
                    domain=domain,
                    path=path,
                    secure=(secure == 'TRUE'),
                    expires=int(expires) if expires.isdigit() else None
                )

        logger.info(f"Cookie読み込み成功: {len(requests_cookie_jar)} 件")

        # デバッグ: 読み込まれたCookie一覧を表示
        for cookie in requests_cookie_jar:
            logger.debug(f"  Cookie: {cookie.name} = {cookie.value[:20]}...")

        return requests_cookie_jar

    except Exception as e:
        logger.error(f"Cookie読み込みエラー: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return None

def extract_csrf_token(cookies):
    """
    cookieからCSRFトークン（ct0）を抽出

    Args:
        cookies: RequestsCookieJar

    Returns:
        str: CSRFトークン
    """
    return cookies.get('ct0', '')

def fetch_bookmarks(session, csrf_token, cursor=None):
    """
    X GraphQL APIを使用してブックマークを取得

    Args:
        session: requestsセッション
        csrf_token: CSRFトークン
        cursor: ページネーションカーソル

    Returns:
        dict: APIレスポンス
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": csrf_token,
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "ja",
        "Content-Type": "application/json",
        "Referer": "https://x.com/i/bookmarks",
        "Origin": "https://x.com",
    }

    # GraphQLクエリ変数
    variables = {
        "count": 100,  # 1回のリクエストで取得する件数
        "includePromotedContent": False
    }

    if cursor:
        variables["cursor"] = cursor

    features = {
        "graphql_timeline_v2_bookmark_timeline": True,
        "rweb_tipjar_consumption_enabled": True,
        "responsive_web_graphql_exclude_directive_enabled": True,
        "verified_phone_label_enabled": False,
        "creator_subscriptions_tweet_preview_api_enabled": True,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "communities_web_enable_tweet_community_results_fetch": True,
        "c9s_tweet_anatomy_moderator_badge_enabled": True,
        "articles_preview_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "responsive_web_twitter_article_tweet_consumption_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "creator_subscriptions_quote_tweet_preview_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
        "rweb_video_timestamps_enabled": True,
        "longform_notetweets_rich_text_read_enabled": True,
        "longform_notetweets_inline_media_enabled": True,
        "responsive_web_enhance_cards_enabled": False
    }

    params = {
        "variables": json.dumps(variables),
        "features": json.dumps(features)
    }

    try:
        response = session.get(BOOKMARKS_URL, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"APIリクエストエラー: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"レスポンス内容: {e.response.text[:500]}")
        return None

def extract_tweet_text(tweet_data):
    """
    ツイートデータからテキストを抽出

    Args:
        tweet_data: ツイートデータ（dict）

    Returns:
        str: ツイートテキスト
    """
    try:
        legacy = tweet_data.get('legacy', {})
        text = legacy.get('full_text', '')

        # RTを除外
        if text.startswith('RT @'):
            return None

        # URLを除去（オプション）
        # text = re.sub(r'https?://\S+', '', text)

        return text.strip()

    except Exception as e:
        logger.error(f"テキスト抽出エラー: {e}")
        return None

def parse_bookmarks_response(response):
    """
    APIレスポンスからブックマーク一覧とカーソルを抽出

    Args:
        response: APIレスポンス（dict）

    Returns:
        tuple: (ツイートリスト, 次のカーソル)
    """
    try:
        instructions = response['data']['bookmark_timeline_v2']['timeline']['instructions']

        tweets = []
        next_cursor = None

        for instruction in instructions:
            if instruction.get('type') == 'TimelineAddEntries':
                entries = instruction.get('entries', [])

                for entry in entries:
                    # ツイートエントリー
                    if entry['entryId'].startswith('tweet-'):
                        content = entry.get('content', {})
                        item_content = content.get('itemContent', {})
                        tweet_results = item_content.get('tweet_results', {})
                        result = tweet_results.get('result', {})

                        if result and result.get('__typename') == 'Tweet':
                            tweets.append(result)

                    # カーソルエントリー（次のページ用）
                    elif entry['entryId'].startswith('cursor-bottom-'):
                        content = entry.get('content', {})
                        next_cursor = content.get('value')

        return tweets, next_cursor

    except Exception as e:
        logger.error(f"レスポンス解析エラー: {e}")
        logger.error(f"レスポンス構造: {json.dumps(response, indent=2, ensure_ascii=False)[:1000]}")
        return [], None

def main():
    """
    メイン処理
    """
    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("X Bookmark Scraper (Cookie版) 開始")
    logger.info("=" * 60)

    # Cookieファイルの確認
    if not COOKIE_FILE.exists():
        logger.error(f"Cookieファイルが見つかりません: {COOKIE_FILE}")
        logger.error("x_cookies.txtを配置してください")
        return

    # Cookieの読み込み
    cookies = load_cookies_from_file(COOKIE_FILE)
    if not cookies:
        logger.error("Cookie読み込みに失敗しました")
        return

    # CSRFトークンの抽出
    csrf_token = extract_csrf_token(cookies)
    if not csrf_token:
        logger.error("CSRFトークン（ct0）が見つかりません")
        return

    logger.info(f"CSRFトークン: {csrf_token[:20]}...")

    # セッションの作成
    session = requests.Session()
    session.cookies = cookies

    # ブックマークの取得
    all_tweets = []
    cursor = None

    for page in range(MAX_REQUESTS):
        logger.info(f"\nページ {page + 1}/{MAX_REQUESTS} を取得中...")

        response = fetch_bookmarks(session, csrf_token, cursor)

        if not response:
            logger.error("APIリクエストに失敗しました")
            break

        tweets, next_cursor = parse_bookmarks_response(response)

        if not tweets:
            logger.info("これ以上ブックマークがありません")
            break

        all_tweets.extend(tweets)
        logger.info(f"  取得: {len(tweets)} 件（累計: {len(all_tweets)} 件）")

        if not next_cursor:
            logger.info("次のページがありません（全件取得完了）")
            break

        cursor = next_cursor

        # レート制限回避のための待機
        if page < MAX_REQUESTS - 1:
            logger.info(f"  {REQUEST_DELAY}秒待機...")
            time.sleep(REQUEST_DELAY)

    # テキスト抽出
    logger.info("\nテキスト抽出中...")
    tweet_texts = []

    for tweet in all_tweets:
        text = extract_tweet_text(tweet)
        if text:
            tweet_texts.append(text)

    logger.info(f"テキスト抽出完了: {len(tweet_texts)} 件")

    # 出力ディレクトリの作成
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # テキストファイルとして保存（T006用）
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for text in tweet_texts:
            # 1行1投稿形式
            cleaned_text = text.replace('\n', ' ')  # 改行を削除
            f.write(f"{cleaned_text}\n")

    logger.info(f"\nテキストファイル保存完了: {OUTPUT_FILE}")

    # JSON形式でも保存（バックアップ）
    output_data = {
        "metadata": {
            "scrape_date": start_time.isoformat(),
            "total_bookmarks": len(tweet_texts),
            "scrape_duration_seconds": int((datetime.now() - start_time).total_seconds())
        },
        "bookmarks": [{"text": text} for text in tweet_texts]
    }

    with open(JSON_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    logger.info(f"JSONファイル保存完了: {JSON_OUTPUT_FILE}")

    # 統計情報
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    logger.info("=" * 60)
    logger.info("ブックマークスクレイピング完了！")
    logger.info(f"テキストファイル: {OUTPUT_FILE}")
    logger.info(f"JSONファイル: {JSON_OUTPUT_FILE}")
    logger.info(f"取得件数: {len(tweet_texts)} 件")
    logger.info(f"実行時間: {int(duration)} 秒（{duration / 60:.1f} 分）")
    logger.info("=" * 60)

    # サンプル表示
    if tweet_texts:
        logger.info("\n【サンプル（最初の5件）】")
        for i, text in enumerate(tweet_texts[:5], 1):
            logger.info(f"{i}. {text[:100]}...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nユーザーによって中断されました")
    except Exception as e:
        logger.error(f"\n予期しないエラー: {e}", exc_info=True)
