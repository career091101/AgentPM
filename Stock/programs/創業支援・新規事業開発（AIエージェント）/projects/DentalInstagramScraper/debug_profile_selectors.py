#!/usr/bin/env python3
"""
Debug Instagram profile page selectors
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time

def load_cookies_for_browser():
    """Load cookies"""
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

def debug_profile_page():
    """Debug profile page structure"""
    print("🔍 Debugging Instagram Profile Page Structure\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )

        cookies = load_cookies_for_browser()
        context.add_cookies(cookies)
        page = context.new_page()

        # Visit a known dental clinic profile
        username = "dentaltown"  # Known working profile
        profile_url = f"https://www.instagram.com/{username}/"

        print(f"Visiting profile: {profile_url}")
        page.goto(profile_url, wait_until='domcontentloaded', timeout=60000)
        time.sleep(5)

        print("\n📸 Taking screenshot...")
        page.screenshot(path="debug_profile_page.png", full_page=True)
        print("   ✅ Saved: debug_profile_page.png\n")

        # Test bio selectors
        print("🔍 Testing bio selectors...\n")

        bio_selectors = [
            'header section h1 + div',          # Original
            'header section div:has-text("")',  # Any div with text
            'header section > div > div',       # Nested divs
            'header div[dir="auto"]',           # Auto-direction divs (often bio)
            'header span',                      # Spans in header
            'section span',                     # Spans in section
        ]

        for selector in bio_selectors:
            try:
                elements = page.locator(selector).all()
                if elements:
                    print(f"✅ {selector}")
                    print(f"   Found {len(elements)} elements")
                    for i, el in enumerate(elements[:3]):
                        try:
                            text = el.inner_text(timeout=2000)
                            if text and len(text) > 10:  # Likely bio
                                print(f"   [{i+1}] {text[:100]}...")
                        except:
                            pass
                    print()
            except Exception as e:
                print(f"❌ {selector}: {e}\n")

        # Test using JavaScript to extract bio
        print("🔍 Testing JavaScript extraction...\n")

        try:
            bio_from_js = page.evaluate('''() => {
                // Try to find bio in page data
                const scripts = Array.from(document.querySelectorAll('script'));
                for (const script of scripts) {
                    if (script.textContent.includes('biography')) {
                        const match = script.textContent.match(/"biography":"([^"]+)"/);
                        if (match) {
                            // Unescape the biography
                            return match[1].replace(/\\\\n/g, ' ').replace(/\\\\/g, '');
                        }
                    }
                }
                return null;
            }''')

            if bio_from_js:
                print(f"✅ Bio extracted via JavaScript:")
                print(f"   {bio_from_js}\n")
        except Exception as e:
            print(f"❌ JS extraction failed: {e}\n")

        # Test followers count
        print("🔍 Testing followers extraction...\n")

        followers_selectors = [
            'header section ul li',
            'header a[href*="/followers/"]',
            'a:-soup-contains("followers")',
        ]

        for selector in followers_selectors:
            try:
                elements = page.locator(selector).all()
                if elements:
                    print(f"✅ {selector}")
                    print(f"   Found {len(elements)} elements")
                    for i, el in enumerate(elements[:3]):
                        try:
                            text = el.inner_text(timeout=2000)
                            if 'follower' in text.lower():
                                print(f"   [{i+1}] {text}")
                        except:
                            pass
                    print()
            except Exception as e:
                print(f"❌ {selector}: {e}\n")

        # Dump full header HTML for manual inspection
        print("💾 Dumping header HTML...\n")

        try:
            header_html = page.evaluate('''() => {
                const header = document.querySelector('header');
                return header ? header.outerHTML : null;
            }''')

            if header_html:
                with open('debug_profile_header.html', 'w', encoding='utf-8') as f:
                    f.write(header_html)
                print("   ✅ Saved: debug_profile_header.html\n")
        except Exception as e:
            print(f"   ❌ Failed: {e}\n")

        print("⏸️  Browser will stay open for 15 seconds...")
        print("    Manually inspect the page to identify correct selectors")
        time.sleep(15)

        browser.close()

        print("\n" + "="*60)
        print("📋 Summary")
        print("="*60)
        print("\nFiles created:")
        print("  - debug_profile_page.png")
        print("  - debug_profile_header.html")
        print("\nNext: Update browser_collector.py with working selectors")

if __name__ == "__main__":
    debug_profile_page()
