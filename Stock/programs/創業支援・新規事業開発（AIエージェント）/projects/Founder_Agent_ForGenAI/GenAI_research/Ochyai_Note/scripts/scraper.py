import asyncio
import os
import json
import logging
from datetime import datetime
from urllib.parse import urlparse
import aiohttp
import aiofiles
from playwright.async_api import async_playwright, Page
from bs4 import BeautifulSoup
import markdownify

# Configuration
BASE_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Ochyai_Note"
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
METADATA_DIR = os.path.join(BASE_DIR, "metadata")
USER_DATA_DIR = os.path.join(BASE_DIR, "user_data")
MAGAZINE_URL = "https://note.com/ochyai/m/m41f58d360230/archive"
YEARS = range(2019, 2026)  # 2019 to 2025
CONCURRENCY = 5

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(BASE_DIR, "scraper.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def download_image(session, url, save_path):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                async with aiofiles.open(save_path, 'wb') as f:
                    await f.write(await response.read())
                return True
    except Exception as e:
        logger.error(f"Failed to download image {url}: {e}")
    return False

async def process_article(context, article_url, session, sem):
    async with sem:
        page = await context.new_page()
        try:
            # Check if processed
            article_id = article_url.split("/n/")[1]
            # ID might have query params
            if "?" in article_id:
                article_id = article_id.split("?")[0]
            
            logger.info(f"Processing article: {article_id}")

            await page.goto(article_url, wait_until="domcontentloaded")
            await asyncio.sleep(2) # Wait for dynamic content

            # Check for paywall or login requirement (simplified)
            # If we are logged in, we should see the content.
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Metadata Extraction
            title_tag = soup.find('h1')
            title = title_tag.get_text(strip=True) if title_tag else "No Title"
            
            date_tag = soup.find('time')
            pub_date = date_tag.get('datetime') if date_tag else datetime.now().isoformat()
            
            # Like count (approximated from DOM if possible, or skip)
            # Tag extraction
            tags = [tag.get_text(strip=True).replace('#', '') for tag in soup.select('.m-articleTags__tag text') if tag]

            # Content Extraction and Image Handling
            article_body = soup.select_one('.m-noteArticle__body') or soup.find('body')
            
            images = []
            if article_body:
                # Find all images
                img_tags = article_body.find_all('img')
                for i, img in enumerate(img_tags):
                    src = img.get('data-src') or img.get('src')
                    if not src:
                        continue
                    
                    # Clean URL
                    if "?" in src:
                        clean_src = src.split("?")[0]
                    else:
                        clean_src = src
                    
                    # Generate local path
                    parsed_date = datetime.fromisoformat(pub_date.replace('Z', '+00:00')) if pub_date else datetime.now()
                    year = str(parsed_date.year)
                    month = f"{parsed_date.month:02d}"
                    ext = os.path.splitext(clean_src)[1] or ".jpg"
                    if not ext or len(ext) > 5: ext = ".jpg"
                    
                    image_filename = f"{article_id}_{i+1:03d}{ext}"
                    local_rel_path = f"{year}/{month}/{image_filename}"
                    local_abs_path = os.path.join(IMAGES_DIR, local_rel_path)
                    
                    # Download
                    success = await download_image(session, src, local_abs_path)
                    
                    if success:
                        images.append({"original": src, "local": local_rel_path})
                        # Replace src in soup for Markdown conversion
                        # Calculate relative path from article MD file to image
                        # Article: articles/YYYY/MM/ID.md
                        # Image: images/YYYY/MM/ID_xxx.jpg
                        # Rel: ../../../images/YYYY/MM/ID_xxx.jpg
                        rel_path_from_md = f"../../../images/{local_rel_path}"
                        img['src'] = rel_path_from_md
                        img['data-src'] = rel_path_from_md
                        if img.parent.name == 'figure':
                             # Sometimes markdownify drops figure, ensure img is kept
                             pass

            # Convert to Markdown
            markdown_content = markdownify.markdownify(str(article_body), heading_style="ATX")
            
            # Create Frontmatter
            frontmatter = f"""---
title: "{title}"
date: "{pub_date}"
url: "{article_url}"
article_id: "{article_id}"
tags: {json.dumps(tags, ensure_ascii=False)}
---

"""
            full_markdown = frontmatter + markdown_content

            # Save Markdown
            parsed_date = datetime.fromisoformat(pub_date.replace('Z', '+00:00')) if pub_date else datetime.now()
            year = str(parsed_date.year)
            month = f"{parsed_date.month:02d}"
            
            article_rel_path = f"{year}/{month}/{article_id}.md"
            article_abs_path = os.path.join(ARTICLES_DIR, article_rel_path)
            
            os.makedirs(os.path.dirname(article_abs_path), exist_ok=True)
            async with aiofiles.open(article_abs_path, 'w') as f:
                await f.write(full_markdown)

            logger.info(f"Saved article: {article_abs_path}")
            
            return {
                "article_id": article_id,
                "title": title,
                "path": article_rel_path,
                "processed": True
            }

        except Exception as e:
            logger.error(f"Error processing {article_url}: {e}")
            return {"article_url": article_url, "error": str(e), "processed": False}
        finally:
            await page.close()

async def get_article_urls_for_month(page, year, month):
    url = f"{MAGAZINE_URL}/{year}-{month:02d}"
    logger.info(f"Navigating to archive: {url}")
    await page.goto(url)
    
    # Scroll to bottom to ensure all articles load
    last_height = await page.evaluate("document.body.scrollHeight")
    while True:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1)
        new_height = await page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Extract URLs
    # Selectors might need adjustment based on site verification
    # Usually note articles are <a> tags with href containing '/n/'
    # Since we are in a magazine, urls might be /ochyai/n/...
    urls = await page.evaluate("""() => {
        const anchors = Array.from(document.querySelectorAll('a'));
        return anchors
            .map(a => a.href)
            .filter(href => href.includes('/n/') && href.includes('note.com/ochyai'))
            .filter((value, index, self) => self.indexOf(value) === index); // Unique
    }""")
    
    logger.info(f"Found {len(urls)} articles in {year}-{month:02d}")
    return urls

async def main():
    async with async_playwright() as p:
        # Launch persistent context to keep login session
        if not os.path.exists(USER_DATA_DIR):
            os.makedirs(USER_DATA_DIR)
            
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False, # Headless=False to allow manual login if needed
            slow_mo=50
        )
        
        page = await browser.new_page()
        
        # 1. Login Check
        logger.info("Checking login status...")
        await page.goto("https://note.com/ochyai/m/m41f58d360230")
        
        # 1. Login Check & Auto-start
        logger.info("Checking login status...")
        await page.goto("https://note.com/ochyai/m/m41f58d360230")
        
        print("ブラウザが起動しました。")
        print("X (Twitter) でログインしてください。")
        print("「購読中」ステータスを検知すると自動的に抽出を開始します...")

        # Loop until logged in (check for '購読中' or similar indicator)
        max_retries = 60 # 5 minutes
        logged_in = False
        for i in range(max_retries):
            content = await page.content()
            # "購読中" comes from the button or badge. 
            # Or check if we can see paid content.
            # Simplified check: Look for the specific subscription badge text if known, 
            # Or just check if we validly loaded the page and it's not the generic guest view.
            # The browser subagent saw "購読中".
            if "購読中" in content or "購読内容を確認" in content:
                print("ログイン（購読権限）を確認しました！ 抽出を開始します。")
                logged_in = True
                break
            
            print(f"ログイン待機中... ({i+1}/{max_retries})")
            await asyncio.sleep(5)
        
        if not logged_in:
            print("タイムアウト：ログインが確認できませんでした。")
            await browser.close()
            return
        
        logger.info("Starting extraction...")
        
        all_articles_metadata = []
        
        async with aiohttp.ClientSession() as session:
            sem = asyncio.Semaphore(CONCURRENCY)
            
            for year in YEARS:
                for month in range(1, 13):
                    if year == 2025 and month > 12: continue # Future check
                    if year == 2019 and month < 1: continue
                    
                    try:
                        urls = await get_article_urls_for_month(page, year, month)
                        
                        tasks = []
                        for url in urls:
                            tasks.append(process_article(browser, url, session, sem))
                        
                        results = await asyncio.gather(*tasks)
                        all_articles_metadata.extend([r for r in results if r.get('processed')])
                        
                    except Exception as e:
                        logger.error(f"Error in {year}-{month}: {e}")

        # Save Metadata
        with open(os.path.join(METADATA_DIR, "all_articles.json"), "w", encoding='utf-8') as f:
            json.dump({
                "extracted_at": datetime.now().isoformat(),
                "total_count": len(all_articles_metadata),
                "articles": all_articles_metadata
            }, f, indent=2, ensure_ascii=False)
            
        logger.info("Extraction completed!")
        await browser.close()

if __name__ == "__main__":
    if not os.path.exists(ARTICLES_DIR): os.makedirs(ARTICLES_DIR)
    if not os.path.exists(IMAGES_DIR): os.makedirs(IMAGES_DIR)
    if not os.path.exists(METADATA_DIR): os.makedirs(METADATA_DIR)
    asyncio.run(main())
