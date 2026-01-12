#!/usr/bin/env python3
"""
Xブックマークページのhtml構造をデバッグ
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SCRIPTS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/scripts")
USER_DATA_DIR = SCRIPTS_DIR / "x_scraper_user_data"
OUTPUT_FILE = SCRIPTS_DIR / "x_bookmarks_debug.html"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            slow_mo=50
        )

        page = await browser.new_page()
        await page.goto("https://x.com/i/bookmarks", wait_until='domcontentloaded')

        # 5秒待機してページ読み込み
        await asyncio.sleep(5)

        # HTMLを保存
        content = await page.content()

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"HTML保存完了: {OUTPUT_FILE}")
        print(f"サイズ: {len(content)} 文字")

        # article要素の確認
        articles = await page.query_selector_all('article')
        print(f"\narticle要素数: {len(articles)}")

        if articles:
            first_article = articles[0]
            article_html = await first_article.inner_html()
            print(f"\n最初のarticle要素（一部）:\n{article_html[:500]}...")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
