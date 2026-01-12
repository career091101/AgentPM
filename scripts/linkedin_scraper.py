#!/usr/bin/env python3
"""
LinkedIn投稿スクレイパー（検出回避実装）

Usage:
    source venv_linkedin/bin/activate
    python linkedin_scraper.py --profile-url https://www.linkedin.com/in/hidetoshitakano/ --target-count 50
"""

import asyncio
import os
import json
import logging
import re
import random
from datetime import datetime
from urllib.parse import urlparse
from playwright.async_api import async_playwright, Page
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = "/Users/yuichi/AIPM/aipm_v0"
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
OUTPUT_DIR = os.path.join(BASE_DIR, "Flow/202512/2025-12-31")
USER_DATA_DIR = os.path.join(SCRIPTS_DIR, "linkedin_user_data")

# LinkedIn Selectors (2025年想定)
POST_SELECTORS = {
    'container': 'div[data-id*="urn:li:activity"]',
    'text': 'div.feed-shared-update-v2__description, div.update-components-text',
    'timestamp': 'time.update-components-actor__sub-description, span.update-components-actor__sub-description time',
    'reactions': 'span.social-details-social-counts__reactions-count',
    'comments': 'button.social-details-social-counts__comments span',
    'shares': 'button.social-details-social-counts__shares-count',
    'author': 'span.update-components-actor__name'
}

# Detection Avoidance Settings
MIN_SCROLL_DELAY = 2.0  # seconds
MAX_SCROLL_DELAY = 4.5  # seconds
WARNING_SLEEP = 60  # seconds when rate limit detected

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(SCRIPTS_DIR, "linkedin_scraper.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class LoginTimeoutError(Exception):
    """ログインタイムアウトエラー"""
    pass


class LinkedInScraper:
    """LinkedIn投稿スクレイパー（検出回避実装）"""

    def __init__(self, profile_url: str, target_count: int = 50):
        self.profile_url = profile_url
        self.target_count = target_count
        self.posts_data = []
        self.user_data_dir = USER_DATA_DIR
        os.makedirs(self.user_data_dir, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    async def initialize_browser(self):
        """Persistent Context起動（認証セッション再利用）"""
        p = await async_playwright().start()
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            headless=False,  # LinkedIn検出回避
            slow_mo=100,     # 人間らしい操作
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            locale='ja-JP',
            timezone_id='Asia/Tokyo'
        )
        return p, browser

    async def wait_for_login(self, page: Page, max_wait: int = 300) -> bool:
        """ユーザー手動ログイン待機（最大5分）"""
        logger.info("=" * 60)
        logger.info("ブラウザが起動しました。LinkedInにログインしてください。")
        logger.info("ログイン完了後、プロフィールページが表示されると自動的に抽出を開始します...")
        logger.info("=" * 60)

        for i in range(max_wait // 5):
            try:
                # Wait for page to be in stable state
                await page.wait_for_load_state("domcontentloaded", timeout=3000)
                content = await page.content()
                # ログイン検出：Feed, アクティビティ等の要素が表示されているか確認
                if any(keyword in content for keyword in ["Feed", "アクティビティ", "activity", "feed-shared"]):
                    logger.info("✅ ログイン確認！抽出を開始します。")
                    return True
            except Exception as e:
                # Navigation in progress is expected during login
                logger.debug(f"Login check (navigation in progress): {type(e).__name__}")
                pass

            if i % 6 == 0:  # 30秒ごとにメッセージ
                logger.info(f"ログイン待機中... ({(i * 5) // 60}分{(i * 5) % 60}秒経過)")

            await asyncio.sleep(5)

        raise LoginTimeoutError(f"Timeout: ログインが検出されませんでした（{max_wait}秒経過）")

    async def human_scroll(self, page: Page):
        """人間らしいスクロール動作"""
        scroll_count = random.randint(5, 10)
        for _ in range(scroll_count):
            scroll_amount = random.uniform(0.6, 0.8)
            await page.evaluate(f"window.scrollBy(0, window.innerHeight * {scroll_amount})")
            delay = random.uniform(MIN_SCROLL_DELAY, MAX_SCROLL_DELAY)
            logger.debug(f"Scrolling... (delay: {delay:.2f}s)")
            await asyncio.sleep(delay)

    async def detect_warning(self, page: Page) -> bool:
        """レート制限警告検出"""
        content = await page.content()
        warning_keywords = [
            "You're visiting too many pages",
            "アクティビティが検出されました",
            "多数のページを訪問",
            "rate-limit"
        ]

        for keyword in warning_keywords:
            if keyword.lower() in content.lower():
                logger.warning(f"⚠️  Rate limit detected: '{keyword}'! Sleeping {WARNING_SLEEP} seconds...")
                await asyncio.sleep(WARNING_SLEEP)
                return True
        return False

    async def scrape_posts(self, page: Page):
        """投稿データ取得（30-50件）"""
        # プロフィールのactivityページに移動
        activity_url = f"{self.profile_url}/recent-activity/all/"
        logger.info(f"Navigating to: {activity_url}")
        await page.goto(activity_url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        posts_loaded = 0
        scroll_attempts = 0
        max_scrolls = 20
        previous_count = 0
        stagnant_count = 0

        while posts_loaded < self.target_count and scroll_attempts < max_scrolls:
            # 人間らしいスクロール
            await self.human_scroll(page)

            # レート制限警告を検出
            if await self.detect_warning(page):
                break

            # 投稿要素を取得
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')

            # 複数のセレクタを試行
            post_elements = (
                soup.select(POST_SELECTORS['container']) or
                soup.select('div[data-urn*="activity"]') or
                soup.select('div.feed-shared-update-v2')
            )

            posts_loaded = len(post_elements)
            logger.info(f"Loaded {posts_loaded} posts (target: {self.target_count}, scroll: {scroll_attempts})")

            # 進捗が停滞している場合は終了
            if posts_loaded == previous_count:
                stagnant_count += 1
                if stagnant_count >= 3:
                    logger.warning(f"投稿数が3回連続で変化なし。現在{posts_loaded}件で終了します。")
                    break
            else:
                stagnant_count = 0
                previous_count = posts_loaded

            scroll_attempts += 1

        logger.info(f"スクロール完了。{posts_loaded}件の投稿要素を抽出します。")

        # 投稿データ抽出
        return await self._extract_all_posts(post_elements[:self.target_count])

    async def _extract_all_posts(self, post_elements):
        """全投稿データを抽出"""
        posts = []

        for i, post_element in enumerate(post_elements, 1):
            try:
                post_data = self._extract_post_data(post_element, i)
                if post_data:
                    posts.append(post_data)
                    logger.debug(f"Extracted post {i}/{len(post_elements)}: {post_data['char_count']} chars")
            except Exception as e:
                logger.error(f"Failed to extract post {i}: {e}")

        logger.info(f"✅ {len(posts)}件の投稿データを抽出しました。")
        return posts

    def _extract_post_data(self, post_element, index: int) -> dict:
        """個別投稿データ抽出"""
        # post_id
        post_id = post_element.get('data-id') or post_element.get('data-urn') or f"unknown_{index}"

        # テキスト抽出
        text_elem = (
            post_element.select_one(POST_SELECTORS['text']) or
            post_element.select_one('div[dir="ltr"]') or
            post_element.find('div', class_=re.compile(r'.*update.*text.*'))
        )
        text = text_elem.get_text(strip=True) if text_elem else ""

        # タイムスタンプ
        timestamp_elem = (
            post_element.select_one(POST_SELECTORS['timestamp']) or
            post_element.find('time')
        )
        timestamp = timestamp_elem.get('datetime') if timestamp_elem and timestamp_elem.has_attr('datetime') else None
        if not timestamp and timestamp_elem:
            timestamp = timestamp_elem.get_text(strip=True)

        # エンゲージメント抽出
        reactions = self._extract_count(post_element, POST_SELECTORS['reactions'])
        comments = self._extract_count(post_element, POST_SELECTORS['comments'])
        shares = self._extract_count(post_element, POST_SELECTORS['shares'])

        # ハッシュタグ抽出
        hashtags = self._extract_hashtags(text)

        # URL（推測）
        url = f"https://www.linkedin.com/feed/update/{post_id}" if post_id.startswith('urn:') else None

        return {
            "post_id": post_id,
            "author": "Hidetoshi Takano",
            "published_at": timestamp,
            "text": text,
            "char_count": len(text),
            "reactions": reactions,
            "comments": comments,
            "shares": shares,
            "hashtags": hashtags,
            "url": url
        }

    def _extract_count(self, element, selector: str) -> int:
        """エンゲージメント数値抽出"""
        try:
            count_elem = element.select_one(selector)
            if not count_elem:
                return 0

            text = count_elem.get_text(strip=True)
            # "45", "1,234", "1K" などの形式に対応
            text = text.replace(',', '').replace('K', '000').replace('k', '000')
            match = re.search(r'\d+', text)
            return int(match.group()) if match else 0
        except Exception as e:
            logger.debug(f"Count extraction failed for selector '{selector}': {e}")
            return 0

    def _extract_hashtags(self, text: str) -> list:
        """ハッシュタグ抽出"""
        return re.findall(r'#[\w\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+', text)

    def save_to_json(self, posts: list, output_path: str):
        """JSON保存（メタデータ付き）"""
        data = {
            "posts": posts,
            "metadata": {
                "profile_url": self.profile_url,
                "scraped_at": datetime.now().isoformat(),
                "total_posts": len(posts),
                "scraper_version": "1.0.0"
            }
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info(f"💾 JSON saved: {output_path}")

    async def run(self):
        """メイン実行"""
        logger.info("=" * 60)
        logger.info("LinkedIn投稿スクレイパー起動")
        logger.info(f"Profile: {self.profile_url}")
        logger.info(f"Target: {self.target_count} posts")
        logger.info("=" * 60)

        p, browser = await self.initialize_browser()
        page = await browser.new_page()

        try:
            # LinkedIn開く
            await page.goto("https://www.linkedin.com")
            await asyncio.sleep(2)

            # ログイン待機
            await self.wait_for_login(page)

            # 投稿スクレイピング
            posts = await self.scrape_posts(page)
            self.posts_data = posts

            # JSON保存
            output_path = os.path.join(OUTPUT_DIR, "takano_linkedin_posts.json")
            self.save_to_json(posts, output_path)

            logger.info("=" * 60)
            logger.info(f"✅ Complete! {len(posts)} posts scraped.")
            logger.info(f"Output: {output_path}")
            logger.info("=" * 60)

        except Exception as e:
            logger.error(f"❌ Error: {e}", exc_info=True)
            raise
        finally:
            await browser.close()
            await p.stop()


async def main():
    """エントリーポイント"""
    import argparse

    parser = argparse.ArgumentParser(description="LinkedIn投稿スクレイパー")
    parser.add_argument('--profile-url', required=True, help='LinkedInプロフィールURL')
    parser.add_argument('--target-count', type=int, default=50, help='取得する投稿数（デフォルト: 50）')

    args = parser.parse_args()

    scraper = LinkedInScraper(
        profile_url=args.profile_url,
        target_count=args.target_count
    )

    await scraper.run()


if __name__ == "__main__":
    asyncio.run(main())
