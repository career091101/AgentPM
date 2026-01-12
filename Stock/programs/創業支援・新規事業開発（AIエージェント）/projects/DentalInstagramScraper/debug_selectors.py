#!/usr/bin/env python3
"""
Debug script to investigate Instagram's current HTML structure
Based on research findings from 2024-2025 best practices
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import json

def load_cookies_for_browser():
    """Load cookies from Netscape format"""
    cookies = []
    cookie_file = Path("instagram_cookies.txt")

    with open(cookie_file, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue

            parts = line.strip().split('\t')
            if len(parts) >= 7:
                cookies.append({
                    'name': parts[5],
                    'value': parts[6],
                    'domain': parts[0],
                    'path': parts[2],
                    'expires': int(parts[4]) if parts[4] != '0' else -1,
                    'httpOnly': False,
                    'secure': parts[3] == 'TRUE'
                })

    return cookies

def debug_instagram_structure():
    """
    Investigate Instagram's HTML structure to find working selectors
    Based on 2024-2025 research findings
    """
    print("🔍 Debugging Instagram HTML Structure\n")
    print("Based on research:")
    print("- Instagram uses React (wait for full JS load)")
    print("- Class names change frequently")
    print("- Structure-based selectors are more stable\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )

        cookies = load_cookies_for_browser()
        context.add_cookies(cookies)
        page = context.new_page()

        # Step 1: Get a post URL from hashtag page
        print("Step 1: Visiting hashtag page to get a post URL...")
        hashtag = "歯科"
        page.goto(f"https://www.instagram.com/explore/tags/{hashtag}/",
                 wait_until='domcontentloaded', timeout=60000)
        time.sleep(5)

        # Find first post
        first_post_link = page.locator('a[href*="/p/"]').first
        post_url = first_post_link.get_attribute('href')
        post_url = f"https://www.instagram.com{post_url}"
        print(f"   ✅ Found post: {post_url}\n")

        # Step 2: Visit post page and analyze structure
        print("Step 2: Visiting post page and analyzing structure...")
        page.goto(post_url, wait_until='domcontentloaded', timeout=60000)
        time.sleep(5)

        print("   Taking screenshot...")
        page.screenshot(path="debug_post_page.png", full_page=True)
        print("   ✅ Screenshot saved: debug_post_page.png\n")

        # Step 3: Try multiple selector strategies
        print("Step 3: Testing selector strategies...\n")

        # Strategy 1: Header-based selectors (most stable)
        print("   Strategy 1: Header-based selectors")
        header_selectors = [
            'header h2',                              # Username in header h2
            'header a[role="link"]',                   # Links in header
            'header section a',                        # Section links
            'article header a',                        # Article header links
        ]

        for selector in header_selectors:
            try:
                elements = page.locator(selector).all()
                if elements:
                    print(f"      ✅ {selector}: Found {len(elements)} elements")
                    for i, el in enumerate(elements[:3]):  # Show first 3
                        href = el.get_attribute('href')
                        text = el.inner_text() if el.is_visible() else '[hidden]'
                        print(f"         [{i+1}] href={href}, text={text}")
            except Exception as e:
                print(f"      ❌ {selector}: {e}")

        print()

        # Strategy 2: Role-based selectors
        print("   Strategy 2: Role-based selectors")
        role_selectors = [
            'a[role="link"]',
            'header a[role="link"]',
            '[role="link"][href^="/"]',
        ]

        for selector in role_selectors:
            try:
                elements = page.locator(selector).all()
                if elements:
                    print(f"      ✅ {selector}: Found {len(elements)} elements")
                    # Find username-like hrefs
                    for el in elements[:5]:
                        href = el.get_attribute('href')
                        if href and href.startswith('/') and not any(x in href for x in ['/p/', '/reel/', '/explore/']):
                            print(f"         Potential username: {href}")
            except Exception as e:
                print(f"      ❌ {selector}: {e}")

        print()

        # Strategy 3: Text content-based
        print("   Strategy 3: Text content & structure-based")
        text_selectors = [
            'header span',
            'header div span',
            'article header span',
        ]

        for selector in text_selectors:
            try:
                elements = page.locator(selector).all()
                if elements:
                    print(f"      ✅ {selector}: Found {len(elements)} elements")
                    for i, el in enumerate(elements[:3]):
                        text = el.inner_text() if el.is_visible() else '[hidden]'
                        if text and len(text) < 50:  # Likely username or short text
                            print(f"         [{i+1}] text={text}")
            except Exception as e:
                print(f"      ❌ {selector}: {e}")

        print()

        # Strategy 4: Dump HTML structure for manual inspection
        print("   Strategy 4: Dumping HTML for manual inspection...")

        # Get header HTML
        try:
            header = page.locator('header').first
            header_html = header.evaluate('el => el.outerHTML')

            with open('debug_header_structure.html', 'w', encoding='utf-8') as f:
                f.write(header_html)

            print("      ✅ Header HTML saved: debug_header_structure.html")
        except Exception as e:
            print(f"      ❌ Failed to dump header: {e}")

        # Get article HTML
        try:
            article = page.locator('article').first
            article_html = article.evaluate('el => el.outerHTML')

            with open('debug_article_structure.html', 'w', encoding='utf-8') as f:
                f.write(article_html)

            print("      ✅ Article HTML saved: debug_article_structure.html")
        except Exception as e:
            print(f"      ❌ Failed to dump article: {e}")

        print()

        # Strategy 5: Extract from URL directly
        print("   Strategy 5: Alternative - Extract from network requests")
        print("      💡 Tip: Instagram posts contain username in:")
        print("         - Post URL structure")
        print("         - GraphQL responses")
        print("         - Window.__additionalDataLoaded data")

        # Try to get username from page context
        try:
            username_from_js = page.evaluate('''() => {
                // Try to find username in page data
                const scripts = Array.from(document.querySelectorAll('script'));
                for (const script of scripts) {
                    if (script.textContent.includes('username')) {
                        const match = script.textContent.match(/"username":"([^"]+)"/);
                        if (match) return match[1];
                    }
                }
                return null;
            }''')

            if username_from_js:
                print(f"      ✅ Username from JS: @{username_from_js}")
        except Exception as e:
            print(f"      ❌ JS extraction failed: {e}")

        print("\n⏸️  Browser will stay open for 15 seconds...")
        print("    Inspect the page manually to identify the correct selector")
        time.sleep(15)

        browser.close()

        print("\n" + "="*60)
        print("📋 Summary")
        print("="*60)
        print("\nFiles created:")
        print("  - debug_post_page.png (Full page screenshot)")
        print("  - debug_header_structure.html (Header HTML)")
        print("  - debug_article_structure.html (Article HTML)")
        print("\nNext steps:")
        print("  1. Open debug_header_structure.html in browser")
        print("  2. Find the <a> tag containing the username")
        print("  3. Note its parent structure and attributes")
        print("  4. Update the selector in browser_collector.py")

if __name__ == "__main__":
    debug_instagram_structure()
