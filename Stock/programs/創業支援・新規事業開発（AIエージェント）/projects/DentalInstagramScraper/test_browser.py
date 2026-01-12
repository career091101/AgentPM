#!/usr/bin/env python3
"""
Test browser-based Instagram collection with a single hashtag
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time

def load_cookies_for_browser():
    """Load cookies from Netscape format and convert to browser format"""
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

def test_browser_collection():
    """Test browser-based hashtag search"""
    print("🌐 Testing browser-based Instagram collection...\n")

    with sync_playwright() as p:
        # Launch browser (visible for debugging)
        print("🚀 Launching browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )

        # Load cookies
        print("🍪 Loading cookies...")
        cookies = load_cookies_for_browser()
        context.add_cookies(cookies)
        print(f"   ✅ Loaded {len(cookies)} cookies\n")

        page = context.new_page()

        # Test 1: Navigate to Instagram
        print("📱 Test 1: Navigate to Instagram homepage...")
        page.goto("https://www.instagram.com/", wait_until='domcontentloaded', timeout=60000)
        time.sleep(5)

        if "login" in page.url:
            print("   ❌ Not logged in! Redirected to login page.")
            browser.close()
            return False
        else:
            print("   ✅ Successfully logged in!\n")

        # Test 2: Navigate to hashtag page
        hashtag = "歯科"
        url = f"https://www.instagram.com/explore/tags/{hashtag}/"
        print(f"📱 Test 2: Navigate to #{hashtag} page...")
        print(f"   URL: {url}")

        try:
            page.goto(url, wait_until='domcontentloaded', timeout=60000)
            time.sleep(5)

            # Check if page loaded successfully
            if "Page Not Found" in page.content() or page.url.endswith("/404/"):
                print("   ❌ Page not found (404)")
            else:
                print("   ✅ Hashtag page loaded successfully!\n")

                # Test 3: Find posts
                print("📱 Test 3: Find posts on hashtag page...")

                # Try multiple selectors for posts
                selectors_to_try = [
                    'a[href*="/p/"]',           # Any post link
                    'article a[href*="/p/"]',   # Post link in article
                    'div a[href*="/p/"]',       # Post link in div
                ]

                post_links_count = 0
                working_selector = None

                for selector in selectors_to_try:
                    try:
                        count = page.locator(selector).count()
                        if count > 0:
                            post_links_count = count
                            working_selector = selector
                            print(f"   ✅ Found {count} posts using selector: {selector}")
                            break
                    except:
                        continue

                if post_links_count == 0:
                    print("   ⚠️  Could not find posts with any selector")
                    print("   Taking screenshot for debugging...")
                    page.screenshot(path="debug_hashtag_page.png")
                    print("   Saved screenshot: debug_hashtag_page.png")

                if post_links_count > 0:
                    print(f"   ✅ Successfully found posts!\n")

                    # Test 4: Click on first post
                    print("📱 Test 4: Open first post...")
                    first_link = page.locator(working_selector).first
                    first_href = first_link.get_attribute('href')
                    print(f"   Post URL: https://www.instagram.com{first_href}")

                    page.goto(f"https://www.instagram.com{first_href}", wait_until='domcontentloaded', timeout=60000)
                    time.sleep(5)

                    # Find username
                    username_link = page.locator('header a[href^="/"][href$="/"]').first
                    if username_link:
                        href = username_link.get_attribute('href')
                        username = href.strip('/') if href else None
                        print(f"   Post author: @{username}")
                        print(f"   ✅ Successfully extracted username!\n")

                        # Test 5: Visit profile
                        print("📱 Test 5: Visit profile page...")
                        profile_url = f"https://www.instagram.com/{username}/"
                        page.goto(profile_url, wait_until='domcontentloaded', timeout=60000)
                        time.sleep(5)

                        # Extract profile name
                        try:
                            full_name = page.locator('header section h2').inner_text()
                            print(f"   Profile name: {full_name}")

                            # Extract bio
                            bio = page.locator('header section h1 + div').inner_text()
                            print(f"   Bio preview: {bio[:100]}...")

                            print(f"   ✅ Successfully extracted profile data!\n")

                        except Exception as e:
                            print(f"   ⚠️  Could not extract profile data: {e}\n")

                else:
                    print("   ❌ No posts found\n")

        except Exception as e:
            print(f"   ❌ Error: {e}\n")

        print("⏸️  Browser will stay open for 10 seconds for you to inspect...")
        print("    You can manually check if the page loaded correctly.")
        time.sleep(10)

        browser.close()
        print("\n✅ Test complete!")
        return True

if __name__ == "__main__":
    test_browser_collection()
