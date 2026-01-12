#!/usr/bin/env python3
"""
X Bookmark Media & Replies Enricher

Phase 3で取得した全文データに、メディア情報とリプライ情報を追加するスクリプト。
Phase 3.5として動作。

使い方:
  python3 x_bookmark_media_replies_enricher.py [--test 10]  # テスト: 最初の10件のみ
  python3 x_bookmark_media_replies_enricher.py              # 本番: 全件実行
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
        logging.FileHandler('enricher_execution.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# 定数
USER_DATA_DIR = Path(__file__).parent / "x_scraper_user_data"
INPUT_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_fulltext_v2.json"
OUTPUT_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_enriched.json"


def parse_engagement_count(text):
    """
    エンゲージメント数（いいね数等）をパース

    Args:
        text: エンゲージメント数のテキスト（例: "1.2万", "345", "1.5K"）

    Returns:
        int: パースされた数値

    Examples:
        >>> parse_engagement_count("1.2万")
        12000
        >>> parse_engagement_count("345")
        345
        >>> parse_engagement_count("1.5K")
        1500
    """
    if not text:
        return 0

    text = text.strip()

    # "万"の処理
    if '万' in text:
        try:
            num = float(text.replace('万', '').replace(',', ''))
            return int(num * 10000)
        except:
            return 0

    # "K"の処理
    if 'K' in text.upper():
        try:
            num = float(text.upper().replace('K', '').replace(',', ''))
            return int(num * 1000)
        except:
            return 0

    # 数字のみ
    try:
        return int(text.replace(',', ''))
    except:
        return 0


async def extract_all_media(page, post_url):
    """
    投稿のメディア情報（画像/動画）を抽出

    Args:
        page: Playwright page object
        post_url: 投稿URL

    Returns:
        dict | None: {
            "images": [{"url", "alt", "width", "height"}],
            "videos": [{"poster", "aria_label", "duration"}],
            "extracted_at": ISO8601 timestamp
        }
    """
    logger.info(f"メディア抽出: {post_url}")

    try:
        await page.goto(post_url, wait_until="domcontentloaded", timeout=90000)
        await asyncio.sleep(8)  # 待機時間（初期読み込み）

        # 投稿要素待機
        try:
            await page.wait_for_selector('article[data-testid="tweet"]', timeout=10000)
        except:
            logger.warning(f"投稿要素が見つかりません（タイムアウト）: {post_url}")
            return None

            # 全文展開処理 ("Show more" / "さらに表示")
        was_expanded = False
        try:
            article = await page.query_selector('article[data-testid="tweet"]')
            if article:
                # 「さらに表示」ボタンを探す
                show_more = await article.query_selector('[data-testid="tweet-text-show-more-link"]')
                if not show_more:
                    show_more = await article.query_selector('span:has-text("さらに表示")')
                if not show_more:
                    show_more = await article.query_selector('span:has-text("Show more")')
                
                if show_more:
                    logger.info("  全文を展開します...")
                    await show_more.click()
                    await asyncio.sleep(2)  # 展開待機
                    was_expanded = True
        except Exception as e:
            logger.debug(f"全文展開エラー（無視）: {e}")

        # 再取得（展開後）
        article = await page.query_selector('article[data-testid="tweet"]')
        if not article:
            logger.warning(f"投稿要素が見つかりません: {post_url}")
            return None

        # 画像抽出（拡張版）
        images = []
        img_elements = await article.query_selector_all('img[alt]')
        for img in img_elements:
            alt = await img.get_attribute('alt')
            src = await img.get_attribute('src')

            # プロフィール画像を除外
            if src and 'profile' not in src.lower():
                # 画像サイズ取得（可能な場合）
                try:
                    bounding_box = await img.bounding_box()
                    width = int(bounding_box['width']) if bounding_box else None
                    height = int(bounding_box['height']) if bounding_box else None
                except:
                    width = None
                    height = None

                images.append({
                    "url": src,
                    "alt": alt or "",
                    "width": width,
                    "height": height
                })

        # 動画抽出（拡張版）
        videos = []
        video_elements = await article.query_selector_all('video')
        for video in video_elements:
            poster = await video.get_attribute('poster')
            aria_label = await video.get_attribute('aria-label')

            # 動画時間取得（可能な場合）
            try:
                # aria-labelから時間を抽出（例: "Embedded video · 0:45"）
                duration = None
                if aria_label and '·' in aria_label:
                    parts = aria_label.split('·')
                    for part in parts:
                        if ':' in part:
                            duration = part.strip()
                            break
            except:
                duration = None

            videos.append({
                "poster": poster or "",
                "aria_label": aria_label or "",
                "duration": duration
            })

        logger.info(f"✅ メディア抽出成功: 画像{len(images)}件、動画{len(videos)}件")

        return {
            "images": images,
            "videos": videos,
            "extracted_at": datetime.now().isoformat(),
            "was_expanded": was_expanded
        }

    except Exception as e:
        logger.error(f"❌ メディア抽出エラー（{post_url}）: {e}")
        return None


async def extract_replies_info(page, post_url, max_replies=10):
    """
    リプライ欄の情報を抽出

    Args:
        page: Playwright page object
        post_url: 投稿URL
        max_replies: 取得するリプライの最大数（デフォルト10件）

    Returns:
        dict | None: {
            "count": リプライ総数,
            "top_replies": [リプライデータ],
            "has_source_urls": bool,
            "source_urls": [URL一覧],
            "extracted_at": ISO8601 timestamp
        }
    """
    logger.info(f"リプライ抽出: {post_url}")

    try:
        # ページはすでに読み込み済み（extract_all_media後）

        # リプライセクションまでスクロール
        await page.evaluate("window.scrollBy(0, 800)")
        await asyncio.sleep(3)

        # リプライ要素を取得（最初の投稿を除外）
        reply_articles = await page.query_selector_all('article[data-testid="tweet"]')

        if len(reply_articles) <= 1:
            logger.info("リプライが見つかりません")
            return {
                "count": 0,
                "top_replies": [],
                "has_source_urls": False,
                "source_urls": [],
                "extracted_at": datetime.now().isoformat()
            }

        # 最初の投稿を除外（元投稿）
        reply_articles = reply_articles[1:]

        top_replies = []
        all_urls = []

        for i, reply_article in enumerate(reply_articles[:max_replies]):
            try:
                # リプライ著者
                author_elem = await reply_article.query_selector('div[data-testid="User-Name"] a')
                author = await author_elem.get_attribute('href') if author_elem else "unknown"
                author = author.replace('/', '') if author else "unknown"

                # リプライテキスト
                text_elem = await reply_article.query_selector('div[data-testid="tweetText"]')
                text = await text_elem.inner_text() if text_elem else ""

                # いいね数
                like_elem = await reply_article.query_selector('div[data-testid="like"] span')
                likes_text = await like_elem.inner_text() if like_elem else "0"
                likes = parse_engagement_count(likes_text)

                # 投稿日時
                time_elem = await reply_article.query_selector('time')
                posted_at = await time_elem.get_attribute('datetime') if time_elem else None

                # URL抽出 (強化版)
                urls = []
                
                # 1. テキストからの正規表現抽出
                text_urls = re.findall(r'https?://[^\s]+', text)
                urls.extend(text_urls)
                
                # 2. リンク要素(a tag)からの抽出
                try:
                    links = await text_elem.query_selector_all('a')
                    for link in links:
                        href = await link.get_attribute('href')
                        if href and not href.startswith('/') and 't.co' in href: # 外部リンクのみ対象（内部リンク除外）
                             urls.append(href)
                        elif href and href.startswith('http'):
                             urls.append(href)
                except Exception as e_url:
                     logger.debug(f"  URLタグ抽出エラー: {e_url}")

                all_urls.extend(urls)

                top_replies.append({
                    "author": author,
                    "text": text,
                    "likes": likes,
                    "posted_at": posted_at,
                    "urls": urls
                })

                logger.debug(f"  リプライ{i+1}: @{author} - {len(text)}文字 - いいね{likes}件")

            except Exception as e:
                logger.warning(f"  リプライ{i+1}の抽出に失敗: {e}")
                continue

        # 重複URL削除
        unique_urls = list(set(all_urls))

        logger.info(f"✅ リプライ抽出成功: {len(top_replies)}件、URL {len(unique_urls)}件")

        return {
            "count": len(reply_articles),
            "top_replies": top_replies,
            "has_source_urls": len(unique_urls) > 0,
            "source_urls": unique_urls,
            "extracted_at": datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"❌ リプライ抽出エラー（{post_url}）: {e}")
        return None


async def main(test_limit=None, input_path=None):
    """
    メイン処理

    Args:
        test_limit: テストモード時の処理件数制限（Noneの場合は全件）
        input_path: 入力ファイルパス（Noneの場合はデフォルト）
    """
    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("X Bookmark Media & Replies Enricher 起動")
    logger.info("=" * 60)

    # 入力ファイル設定
    target_input_file = Path(input_path) if input_path else INPUT_FILE

    # Phase 3完了データ読み込み
    if not target_input_file.exists():
        logger.error(f"データファイルが見つかりません: {target_input_file}")
        return

    with open(target_input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    bookmarks = data["bookmarks"]
    logger.info(f"総ブックマーク数: {len(bookmarks)}件")

    # テストモード
    if test_limit:
        bookmarks_to_process = bookmarks[:test_limit]
        logger.info(f"⚠️  テストモード: 最初の{test_limit}件のみ処理")
    else:
        bookmarks_to_process = bookmarks

    logger.info(f"処理対象: {len(bookmarks_to_process)}件\n")

    # Playwright起動
    async with async_playwright() as p:
        logger.info("ブラウザを起動中...")

        browser = await p.chromium.launch_persistent_context(
            str(USER_DATA_DIR),
            headless=True,
            channel="chrome",
            slow_mo=500,
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
        media_extracted_count = 0
        replies_extracted_count = 0

        for i, bookmark in enumerate(bookmarks_to_process, 1):
            logger.info(f"\n[{i}/{len(bookmarks_to_process)}] 処理中...")

            url = bookmark.get("url")
            if not url:
                logger.warning(f"URLが見つかりません（スキップ）")
                failed_count += 1
                continue

            media_success = False
            replies_success = False

            # メディア情報抽出
            media_info = await extract_all_media(page, url)
            if media_info:
                bookmark["media"] = media_info
                media_success = True
                media_extracted_count += 1

            # リプライ情報抽出（同じページで続けて実行）
            replies_info = await extract_replies_info(page, url, max_replies=10)
            if replies_info:
                bookmark["replies"] = replies_info
                replies_success = True
                replies_extracted_count += 1

            # 全文テキストの更新処理
            try:
                article_elem = await page.query_selector('article[data-testid="tweet"] div[data-testid="tweetText"]')
                if article_elem:
                    full_text = await article_elem.inner_text()
                    # 展開した場合は無条件更新、そうでない場合は長さチェック
                    if media_info.get("was_expanded") or (full_text and len(full_text) > len(bookmark.get("text", ""))):
                        logger.info(f"  全文更新: {len(bookmark.get('text', ''))}文字 -> {len(full_text)}文字 (Expanded: {media_info.get('was_expanded')})")
                        bookmark["text"] = full_text
            except Exception as e:
                logger.warning(f"全文テキスト更新失敗: {e}")

            if media_success or replies_success:
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
                            "enriched_at": datetime.now().isoformat(),
                            "enriched_count": success_count,
                            "failed_count": failed_count,
                            "media_extracted_count": media_extracted_count,
                            "replies_extracted_count": replies_extracted_count
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
                "enriched_at": datetime.now().isoformat(),
                "enriched_count": success_count,
                "failed_count": failed_count,
                "total_processed": len(bookmarks_to_process),
                "media_extracted_count": media_extracted_count,
                "replies_extracted_count": replies_extracted_count
            },
            "bookmarks": bookmarks
        }, f, ensure_ascii=False, indent=2)

    # 統計表示
    elapsed = (datetime.now() - start_time).total_seconds()

    logger.info("=" * 60)
    logger.info("処理完了！")
    logger.info("=" * 60)
    logger.info(f"処理対象: {len(bookmarks_to_process)}件")
    logger.info(f"成功: {success_count}件")
    logger.info(f"失敗: {failed_count}件")
    logger.info(f"メディア抽出: {media_extracted_count}件")
    logger.info(f"リプライ抽出: {replies_extracted_count}件")
    logger.info(f"実行時間: {elapsed:.1f}秒（{elapsed/60:.1f}分）")
    logger.info(f"平均処理時間: {elapsed/len(bookmarks_to_process):.1f}秒/件")
    logger.info(f"保存先: {OUTPUT_FILE}")
    logger.info("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="X Bookmark Media & Replies Enricher")
    parser.add_argument(
        "--test",
        type=int,
        metavar="N",
        help="テストモード: 最初のN件のみ処理（例: --test 10）"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="入力ファイルパス（指定がない場合はデフォルト）"
    )

    args = parser.parse_args()

    asyncio.run(main(test_limit=args.test, input_path=args.input))
