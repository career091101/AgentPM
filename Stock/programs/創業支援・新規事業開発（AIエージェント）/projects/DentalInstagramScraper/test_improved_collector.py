#!/usr/bin/env python3
"""
Test the improved browser collector with username extraction
Based on 2024-2025 research findings
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import re

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

def extract_username_from_post(page):
    """Extract username using improved methods"""
    # Strategy 1: JavaScript extraction
    try:
        username = page.evaluate('''() => {
            const scripts = Array.from(document.querySelectorAll('script'));
            for (const script of scripts) {
                if (script.textContent.includes('username')) {
                    const match = script.textContent.match(/"username":"([^"]+)"/);
                    if (match) return match[1];
                }
            }
            return null;
        }''')

        if username:
            print(f"      ✅ Extracted via JS: @{username}")
            return username
    except Exception as e:
        print(f"      ⚠️  JS extraction failed: {e}")

    # Strategy 2: Role-based selector
    try:
        links = page.locator('a[role="link"]').all()
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('/') and href.endswith('/'):
                if not any(x in href for x in ['/p/', '/reel/', '/explore/', '/stories/']):
                    username = href.strip('/')
                    if username:
                        print(f"      ✅ Extracted via selector: @{username}")
                        return username
    except Exception as e:
        print(f"      ⚠️  Selector extraction failed: {e}")

    return None

def extract_postal_code(text):
    """Extract Japanese postal code"""
    if not text:
        return ''
    pattern = r'〒?\s*(\d{3})-?(\d{4})'
    match = re.search(pattern, text)
    if match:
        return f"{match.group(1)}-{match.group(2)}"
    return ''

def extract_address(text):
    """Extract Japanese address"""
    if not text:
        return ''
    pattern = r'((?:北海道|東京都|大阪府|京都府|.{2,3}県)[^\n]{0,80}?(?:市|区|町|村|丁目|番地|号|ビル|F))'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return ''

def test_improved_collection():
    """Test the improved collection workflow"""
    print("🦷 Testing Improved Instagram Collector\n")
    print("Based on 2024-2025 research:")
    print("  - JavaScript extraction for usernames")
    print("  - Role-based selectors as fallback")
    print("  - Optimized wait strategies for React\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )

        cookies = load_cookies_for_browser()
        context.add_cookies(cookies)
        page = context.new_page()

        # Step 1: Visit hashtag page
        hashtag = "歯科"
        print(f"Step 1: Visiting #{hashtag} hashtag page...")
        page.goto(f"https://www.instagram.com/explore/tags/{hashtag}/",
                 wait_until='domcontentloaded', timeout=60000)
        time.sleep(5)  # Wait for React
        print("   ✅ Page loaded\n")

        # Step 2: Collect post URLs
        print("Step 2: Collecting post URLs...")
        post_links = page.locator('a[href*="/p/"]').all()
        posts = []
        for link in post_links[:3]:  # Test with 3 posts
            href = link.get_attribute('href')
            if href:
                posts.append(f"https://www.instagram.com{href}")

        print(f"   ✅ Found {len(posts)} posts to check\n")

        # Step 3: Extract usernames from posts
        print("Step 3: Extracting usernames from posts...")
        dental_profiles = []

        for i, post_url in enumerate(posts, 1):
            print(f"\n   [{i}/{len(posts)}] Post: {post_url}")
            page.goto(post_url, wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)

            username = extract_username_from_post(page)

            if username:
                print(f"      ✅ Username: @{username}")

                # Visit profile
                print(f"      📥 Visiting profile...")
                page.goto(f"https://www.instagram.com/{username}/",
                         wait_until='domcontentloaded', timeout=60000)
                time.sleep(5)

                # Extract bio
                try:
                    bio = page.locator('header section h1 + div').first.inner_text()
                    print(f"      Bio: {bio[:80]}...")

                    # Check for dental keywords
                    dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic']
                    is_dental = any(kw in bio.lower() for kw in dental_keywords)

                    if is_dental:
                        print(f"      🦷 This is a dental clinic!")

                        # Extract data
                        postal_code = extract_postal_code(bio)
                        address = extract_address(bio)

                        dental_profiles.append({
                            'username': username,
                            'bio': bio,
                            'postal_code': postal_code,
                            'address': address
                        })

                        print(f"      📮 Postal code: {postal_code or '❌ Not found'}")
                        print(f"      🏠 Address: {address[:50] if address else '❌ Not found'}...")

                    else:
                        print(f"      ⚠️  Not a dental clinic")

                except Exception as e:
                    print(f"      ❌ Failed to extract bio: {e}")

            else:
                print(f"      ❌ Could not extract username")

        print(f"\n{'='*60}")
        print(f"✅ Test Complete!")
        print(f"{'='*60}")
        print(f"Posts checked: {len(posts)}")
        print(f"Dental clinics found: {len(dental_profiles)}")

        if dental_profiles:
            print(f"\n📋 Found dental clinics:")
            for profile in dental_profiles:
                print(f"   - @{profile['username']}")
                if profile['postal_code']:
                    print(f"     📮 {profile['postal_code']}")
                if profile['address']:
                    print(f"     🏠 {profile['address'][:50]}...")

        print("\n⏸️  Browser will close in 10 seconds...")
        time.sleep(10)

        browser.close()

if __name__ == "__main__":
    test_improved_collection()
