#!/usr/bin/env python3
"""
X Bookmark Full Text Expander

切り捨てられた投稿の全文を個別に取得するスクリプト。
2段階スクレイピングのPhase 2として動作。

使い方:
  python3 x_bookmark_expander.py [--test 10]  # テスト: 最初の10件のみ
  python3 x_bookmark_expander.py              # 本番: 全件実行
"""

import asyncio
import json
import logging
import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# .envファイルから環境変数を読み込む（オプショナル）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenvがない場合はスキップ

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('expander_execution.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# 定数
USER_DATA_DIR = Path(__file__).parent / "x_scraper_user_data"
DATA_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_fulltext.json"
OUTPUT_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_fulltext_v2.json"


def check_sentence_completeness(text):
    """
    文章が完結しているかをヒューリスティックに判定

    Args:
        text: チェック対象のテキスト

    Returns:
        bool: 文章が完結していればTrue、不完全ならFalse
    """
    if not text:
        return False

    last_char = text[-1]
    # 文末記号で終わっている場合は完結とみなす
    if last_char in ['。', '！', '？', '!', '?', '.', '」', ')', '）', '>']:
        return True

    return False


def identify_truncated_posts(bookmarks):
    """
    切り捨てられている可能性がある投稿を特定（全範囲対応版）

    判定基準:
    - 空投稿（画像/動画のみ）
    - 280文字ちょうど
    - 本文末尾に省略記号（URL部分は除外）
    - 270-279文字で文章が不完全
    - 250-269文字で文章が不完全
    - 200-249文字で文章が不完全
    - 200文字未満で文章が不完全
    """
    truncated = []

    for idx, bookmark in enumerate(bookmarks):
        text = bookmark.get("text", "")
        url = bookmark.get("url", "")

        if not url:
            continue

        # 空投稿チェック
        if not text.strip():
            truncated.append({
                "index": idx,
                "url": url,
                "type": "empty",
                "reason": "空投稿（画像/動画のみ）",
                "original_text": "",
                "original_length": 0,
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # 280文字ちょうど
        if len(text) == 280:
            truncated.append({
                "index": idx,
                "url": url,
                "type": "length_limit",
                "reason": "280文字ちょうど",
                "original_text": text,
                "original_length": 280,
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # URLを除外したテキスト
        text_without_urls = re.sub(r'https?://[^\s]+', '', text)

        # 本文末尾の省略記号（URLを除外した後）
        if re.search(r'(\.\.\.|\…)\s*$', text_without_urls.strip()):
            truncated.append({
                "index": idx,
                "url": url,
                "type": "ellipsis",
                "reason": "本文末尾に省略記号",
                "original_text": text,
                "original_length": len(text),
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # 270-279文字で文章が不完全
        if 270 <= len(text) <= 279 and not check_sentence_completeness(text):
            truncated.append({
                "index": idx,
                "url": url,
                "type": "270_279_incomplete",
                "reason": "270-279文字（文章不完全）",
                "original_text": text,
                "original_length": len(text),
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # 250-269文字で文章が不完全
        if 250 <= len(text) <= 269 and not check_sentence_completeness(text):
            truncated.append({
                "index": idx,
                "url": url,
                "type": "250_269_incomplete",
                "reason": "250-269文字（文章不完全）",
                "original_text": text,
                "original_length": len(text),
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # 200-249文字で文章が不完全
        if 200 <= len(text) <= 249 and not check_sentence_completeness(text):
            truncated.append({
                "index": idx,
                "url": url,
                "type": "200_249_incomplete",
                "reason": "200-249文字（文章不完全）",
                "original_text": text,
                "original_length": len(text),
                "author": bookmark.get("author_username", "unknown")
            })
            continue

        # 200文字未満で文章が不完全
        if len(text) < 200 and not check_sentence_completeness(text):
            truncated.append({
                "index": idx,
                "url": url,
                "type": "below_200_incomplete",
                "reason": "200文字未満（文章不完全）",
                "original_text": text,
                "original_length": len(text),
                "author": bookmark.get("author_username", "unknown")
            })

    return truncated


async def extract_media_metadata(page, post_info):
    """
    空投稿（画像/動画のみ）からメタデータを抽出

    Args:
        page: Playwright page object
        post_info: 投稿情報（url等）

    Returns:
        dict | None: {
            "images": [{"url": "...", "alt": "..."}],
            "videos": [{"poster": "...", "aria_label": "..."}]
        }
    """
    url = post_info["url"]
    logger.info(f"メタデータ抽出: {url}")

    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await asyncio.sleep(3)

        article = await page.query_selector('article[data-testid="tweet"]')
        if not article:
            logger.warning(f"投稿要素が見つかりません: {url}")
            return None

        # 画像抽出
        images = []
        img_elements = await article.query_selector_all('img[alt]')
        for img in img_elements:
            alt = await img.get_attribute('alt')
            src = await img.get_attribute('src')
            # プロフィール画像を除外
            if src and 'profile' not in src.lower():
                images.append({"url": src, "alt": alt or ""})

        # 動画抽出
        videos = []
        video_elements = await article.query_selector_all('video')
        for video in video_elements:
            poster = await video.get_attribute('poster')
            aria_label = await video.get_attribute('aria-label')
            videos.append({
                "poster": poster or "",
                "aria_label": aria_label or ""
            })

        logger.debug(f"  画像: {len(images)}件、動画: {len(videos)}件")
        return {
            "images": images,
            "videos": videos
        }
    except Exception as e:
        logger.error(f"❌ メタデータ抽出エラー（{url}）: {e}")
        return None


async def expand_single_post(page, post_info, max_expand_attempts=5):
    """
    単一の投稿URLにアクセスして全文を取得

    Args:
        page: Playwright page object
        post_info: 投稿情報（url, original_text等）
        max_expand_attempts: 「さらに表示」ボタンのクリック最大試行回数

    Returns:
        展開後の全文テキスト（失敗時はNone）
    """
    url = post_info["url"]
    logger.info(f"個別ページにアクセス: {url}")

    try:
        # URLにアクセス（DOMContentLoaded待機に変更）
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await asyncio.sleep(3)  # ページ読み込み完了を待つ（2秒 → 3秒に延長）

        # 投稿要素を取得
        article = await page.query_selector('article[data-testid="tweet"]')
        if not article:
            logger.warning(f"投稿要素が見つかりません: {url}")
            return None

        # 「さらに表示」ボタンを繰り返しクリック
        previous_length = 0
        current_text = ""

        for attempt in range(max_expand_attempts):
            # 現在のテキストを取得
            current_text = await article.inner_text()
            current_length = len(current_text)

            logger.debug(f"  試行{attempt+1}: テキスト長 = {current_length}文字")

            # テキスト長が変化しなくなったら終了
            if attempt > 0 and current_length == previous_length:
                logger.debug(f"  テキスト長が変化しないため展開完了")
                break

            previous_length = current_length

            # 「さらに表示」ボタンを探す
            show_more_selectors = [
                'div[role="button"]:has-text("さらに表示")',
                'div[role="button"]:has-text("Show more")',
                'span:has-text("さらに表示")',
                'span:has-text("Show more")'
            ]

            button_found = False
            for selector in show_more_selectors:
                try:
                    buttons = await article.query_selector_all(selector)
                    if buttons:
                        # 最初のボタンをクリック
                        await buttons[0].click()
                        logger.debug(f"  「さらに表示」ボタンをクリック（セレクタ: {selector}）")
                        button_found = True

                        # DOM更新を待つ
                        await asyncio.sleep(1.0)
                        break
                except Exception as e:
                    logger.debug(f"  セレクタ {selector} でエラー: {e}")
                    continue

            if not button_found:
                logger.debug(f"  「さらに表示」ボタンが見つからない（展開完了）")
                break

        # 最終的なテキストを取得
        final_text = await article.inner_text()
        final_length = len(final_text)

        original_length = post_info["original_length"]
        if final_length > original_length:
            logger.info(f"✅ 展開成功: {original_length}文字 → {final_length}文字 (+{final_length - original_length})")
            return final_text
        else:
            logger.warning(f"⚠️  展開されませんでした: {original_length}文字 → {final_length}文字")
            return None

    except Exception as e:
        logger.error(f"❌ エラー発生（{url}）: {e}")
        return None


async def main(test_limit=None, rerun=False, incomplete_only=False):
    """
    メイン処理

    Args:
        test_limit: テストモード時の処理件数制限（Noneの場合は全件）
        rerun: 再実行モード（既に展開済みの投稿も再処理）
        incomplete_only: 未完了投稿のみを処理
    """
    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("X Bookmark Full Text Expander 起動")
    logger.info("=" * 60)

    # データファイル読み込み
    if not DATA_FILE.exists():
        logger.error(f"データファイルが見つかりません: {DATA_FILE}")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    bookmarks = data["bookmarks"]
    logger.info(f"総ブックマーク数: {len(bookmarks)}件")

    # 切り捨て投稿を特定
    truncated_posts = identify_truncated_posts(bookmarks)
    logger.info(f"切り捨て対象投稿: {len(truncated_posts)}件")

    if not truncated_posts:
        logger.info("切り捨て投稿がありません。処理終了。")
        return

    # テストモード
    if test_limit:
        truncated_posts = truncated_posts[:test_limit]
        logger.info(f"⚠️  テストモード: 最初の{test_limit}件のみ処理")

    # 処理対象を表示
    logger.info("\n処理対象一覧:")
    for i, post in enumerate(truncated_posts, 1):
        logger.info(f"  {i}. @{post['author']} - {post['original_length']}文字 - {post['reason']}")
        logger.info(f"     URL: {post['url']}")

    logger.info("")

    # Playwright起動
    async with async_playwright() as p:
        logger.info("ブラウザを起動中...")

        # Cookie保存済みのユーザーデータディレクトリを使用
        browser = await p.chromium.launch_persistent_context(
            str(USER_DATA_DIR),
            headless=False,  # デバッグのため表示
            slow_mo=500,     # 動作をゆっくり（視認性向上）
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )

        page = browser.pages[0]

        # 各投稿を処理
        success_count = 0
        failed_count = 0

        for i, post_info in enumerate(truncated_posts, 1):
            logger.info(f"\n[{i}/{len(truncated_posts)}] 処理中...")

            idx = post_info["index"]

            if post_info.get("type") == "empty":
                # 空投稿 → メタデータ抽出
                media_metadata = await extract_media_metadata(page, post_info)

                if media_metadata:
                    bookmarks[idx]["media_metadata"] = media_metadata
                    bookmarks[idx]["media_extracted"] = True
                    bookmarks[idx]["extracted_at"] = datetime.now().isoformat()
                    success_count += 1
                    logger.info(f"✅ メタデータ取得成功: 画像{len(media_metadata['images'])}件、動画{len(media_metadata['videos'])}件")
                else:
                    failed_count += 1
            else:
                # テキスト展開（既存処理）
                expanded_text = await expand_single_post(page, post_info)

                if expanded_text:
                    bookmarks[idx]["text"] = expanded_text
                    bookmarks[idx]["expanded"] = True
                    bookmarks[idx]["expanded_at"] = datetime.now().isoformat()
                    success_count += 1
                else:
                    failed_count += 1

            # 進捗保存（10件ごと）
            if i % 10 == 0:
                logger.info(f"中間保存実行（{i}件処理完了）")
                with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                    json.dump({
                        "metadata": {
                            **data["metadata"],
                            "expanded_at": datetime.now().isoformat(),
                            "expanded_count": success_count,
                            "failed_count": failed_count
                        },
                        "bookmarks": bookmarks
                    }, f, ensure_ascii=False, indent=2)

        await browser.close()

    # 最終保存
    logger.info("\n最終データを保存中...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "metadata": {
                **data["metadata"],
                "expanded_at": datetime.now().isoformat(),
                "expanded_count": success_count,
                "failed_count": failed_count,
                "total_processed": len(truncated_posts)
            },
            "bookmarks": bookmarks
        }, f, ensure_ascii=False, indent=2)

    # 統計表示
    elapsed = (datetime.now() - start_time).total_seconds()

    logger.info("=" * 60)
    logger.info("処理完了！")
    logger.info("=" * 60)
    logger.info(f"処理対象: {len(truncated_posts)}件")
    logger.info(f"成功: {success_count}件")
    logger.info(f"失敗: {failed_count}件")
    logger.info(f"実行時間: {elapsed:.1f}秒（{elapsed/60:.1f}分）")
    logger.info(f"保存先: {OUTPUT_FILE}")
    logger.info("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="X Bookmark Full Text Expander")
    parser.add_argument(
        "--test",
        type=int,
        metavar="N",
        help="テストモード: 最初のN件のみ処理（例: --test 10）"
    )
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="再実行モード: 改善された判定ロジックで再処理"
    )
    parser.add_argument(
        "--incomplete-only",
        action="store_true",
        help="未完了投稿のみを処理（全範囲の文章不完全投稿、空投稿）"
    )

    args = parser.parse_args()

    asyncio.run(main(test_limit=args.test, rerun=args.rerun, incomplete_only=args.incomplete_only))
