#!/usr/bin/env python3
"""
Browser-based Instagram collector using Playwright
This bypasses API limitations by automating the actual Instagram web interface
"""
from playwright.sync_api import sync_playwright
import json
import time
from datetime import datetime
from pathlib import Path
import re

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

def collect_from_hashtag(hashtag, max_posts=20, headless=False):
    """
    Collect dental clinic profiles from a hashtag using browser automation

    Args:
        hashtag: Hashtag to search (without #)
        max_posts: Maximum number of posts to collect
        headless: Run browser in headless mode (False to see browser for debugging)
    """
    print(f"🌐 Starting browser-based collection for #{hashtag}...")
    print(f"   Target: {max_posts} posts\n")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=headless)
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

        # Navigate to hashtag page
        url = f"https://www.instagram.com/explore/tags/{hashtag}/"
        print(f"🔗 Navigating to {url}...")
        page.goto(url, wait_until='domcontentloaded', timeout=60000)

        # Wait for React to render (based on research findings)
        time.sleep(5)

        # Check if we're logged in
        if "login" in page.url:
            print("❌ Not logged in! Cookies may be expired.")
            browser.close()
            return []

        print("✅ Successfully loaded hashtag page\n")

        # Collect post links
        print(f"📥 Collecting posts from #{hashtag}...")
        collected_posts = []
        collected_profiles = set()

        # Try to find posts - use flexible selector based on test results
        selector = 'a[href*="/p/"]'  # This worked in our tests (found 18 posts)

        # Initial collection
        post_links = page.locator(selector).all()
        print(f"   Initial scan: Found {len(post_links)} post links")

        for link in post_links[:max_posts]:
            href = link.get_attribute('href')
            if href:
                full_url = f"https://www.instagram.com{href}" if href.startswith('/') else href
                if full_url not in [p['url'] for p in collected_posts]:
                    collected_posts.append({'url': full_url})
                    print(f"   Added post {len(collected_posts)}/{max_posts}")

        # If we need more, scroll and collect
        scroll_count = 0
        max_scrolls = 3

        while len(collected_posts) < max_posts and scroll_count < max_scrolls:
            print(f"   Scrolling for more posts... (scroll {scroll_count + 1}/{max_scrolls})")
            page.evaluate("window.scrollBy(0, 1000)")
            time.sleep(3)

            # Find new post links
            post_links = page.locator(selector).all()
            for link in post_links:
                if len(collected_posts) >= max_posts:
                    break

                href = link.get_attribute('href')
                if href:
                    full_url = f"https://www.instagram.com{href}" if href.startswith('/') else href
                    if full_url not in [p['url'] for p in collected_posts]:
                        collected_posts.append({'url': full_url})
                        print(f"   Added post {len(collected_posts)}/{max_posts}")

            scroll_count += 1

        print(f"\n✅ Collected {len(collected_posts)} posts\n")

        # Visit each post and extract profile information
        print("👤 Extracting profile information...\n")
        profiles_data = []

        for i, post in enumerate(collected_posts[:max_posts], 1):
            try:
                print(f"[{i}/{len(collected_posts)}] 🔍 Visiting post...")
                page.goto(post['url'], wait_until='domcontentloaded', timeout=60000)
                time.sleep(3)

                # Extract username using our improved extraction method
                username = extract_username_from_post(page)

                if not username:
                    print(f"   ⚠️  Failed to extract username from post")
                    continue

                if username:
                    if username in collected_profiles:
                        print(f"   ⏭️  Skipping @{username} (already processed)")
                        continue

                    print(f"   Found profile: @{username}")
                    collected_profiles.add(username)

                    # Visit profile page
                    profile_url = f"https://www.instagram.com/{username}/"
                    page.goto(profile_url, wait_until='domcontentloaded', timeout=60000)
                    time.sleep(5)  # Wait for React to render

                    # Extract profile data
                    profile_data = extract_profile_data(page, username)

                    if profile_data:
                        # Debug: Show extracted data
                        print(f"      📊 Extracted data:")
                        print(f"         Name: {profile_data.get('full_name', 'N/A')}")
                        print(f"         Followers: {profile_data.get('followers', 0):,}")
                        bio = profile_data.get('biography', '')
                        print(f"         Bio: {bio[:100] if bio else 'No bio'}...")

                        # Check if it's a dental clinic
                        bio_lower = bio.lower()
                        dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic', '矯正', '小児歯科']

                        matching_keywords = [kw for kw in dental_keywords if kw in bio_lower]
                        if matching_keywords:
                            print(f"      🦷 Dental clinic found! (matched: {', '.join(matching_keywords)})")
                            print(f"         Postal code: {profile_data.get('postal_code') or '❌'}")
                            print(f"         Address: {(profile_data.get('address', '')[:50] + '...') if profile_data.get('address') else '❌'}")
                            profiles_data.append(profile_data)
                        else:
                            print(f"      ⚠️  Not a dental clinic (no keywords found)")

                    print()

            except Exception as e:
                print(f"   ❌ Error: {e}\n")
                continue

        browser.close()

        print(f"\n✅ Collection complete!")
        print(f"   Posts checked: {len(collected_posts)}")
        print(f"   Dental clinics found: {len(profiles_data)}")

        return profiles_data

def extract_username_from_post(page):
    """
    Extract username from Instagram post page
    Uses multiple strategies based on 2024-2025 research
    """
    # Strategy 1: JavaScript extraction (most reliable)
    try:
        username = page.evaluate('''() => {
            // Instagram embeds user data in script tags
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
            return username
    except Exception as e:
        print(f"      ⚠️  JS extraction failed: {e}")

    # Strategy 2: Role-based selector (fallback)
    try:
        links = page.locator('a[role="link"]').all()
        for link in links:
            href = link.get_attribute('href')
            # Username links: /username/ (exclude /p/, /reel/, /explore/)
            if href and href.startswith('/') and href.endswith('/'):
                if not any(x in href for x in ['/p/', '/reel/', '/explore/', '/stories/']):
                    username = href.strip('/')
                    if username:  # Not empty
                        return username
    except Exception as e:
        print(f"      ⚠️  Selector extraction failed: {e}")

    return None

def extract_profile_data(page, username):
    """
    Extract profile data from Instagram profile page
    Uses improved selectors based on 2024-2025 research
    """
    try:
        # Wait for profile to load (React rendering)
        time.sleep(3)

        # Extract data from page
        data = {
            'instagram_handle': username,
            'collected_at': datetime.now().isoformat()
        }

        # Strategy 1: Try JavaScript extraction (most reliable)
        try:
            js_data = page.evaluate('''() => {
                const scripts = Array.from(document.querySelectorAll('script'));
                let result = {};

                for (const script of scripts) {
                    const text = script.textContent;

                    // Extract full name
                    if (text.includes('full_name')) {
                        const match = text.match(/"full_name":"([^"]+)"/);
                        if (match) {
                            // Decode Unicode escapes
                            result.full_name = match[1]
                                .replace(/\\\\u([0-9a-f]{4})/gi, (m, code) =>
                                    String.fromCharCode(parseInt(code, 16))
                                );
                        }
                    }

                    // Extract biography
                    if (text.includes('biography')) {
                        const match = text.match(/"biography":"([^"]+)"/);
                        if (match) {
                            // Decode Unicode escapes
                            result.biography = match[1]
                                .replace(/\\\\u([0-9a-f]{4})/gi, (m, code) =>
                                    String.fromCharCode(parseInt(code, 16))
                                )
                                .replace(/\\\\n/g, ' ')
                                .replace(/\\\\/g, '');
                        }
                    }

                    // Extract followers count
                    if (text.includes('edge_followed_by')) {
                        const match = text.match(/"edge_followed_by":\\{"count":(\\d+)\\}/);
                        if (match) result.followers = parseInt(match[1]);
                    }

                    // Extract external URL
                    if (text.includes('external_url')) {
                        const match = text.match(/"external_url":"([^"]+)"/);
                        if (match) result.external_url = match[1].replace(/\\\//g, '/');
                    }

                    // Extract is_business_account
                    if (text.includes('is_business_account')) {
                        const match = text.match(/"is_business_account":(true|false)/);
                        if (match) result.is_business_account = match[1] === 'true';
                    }
                }

                return result;
            }''')

            # Merge JS data
            data.update(js_data)

        except Exception as e:
            print(f"         ⚠️  JS extraction failed: {e}")

        # Strategy 2: Fallback to selectors
        if 'full_name' not in data or not data.get('full_name'):
            try:
                full_name = page.locator('header section h2').first.inner_text(timeout=5000)
                data['full_name'] = full_name
            except:
                data['full_name'] = ''

        if 'biography' not in data or not data.get('biography'):
            try:
                # Use the working selector from debug
                bio = page.locator('header section h1 + div').first.inner_text(timeout=5000)
                data['biography'] = bio
            except:
                data['biography'] = ''

        # Followers count (if not extracted via JS)
        if 'followers' not in data or not data.get('followers'):
            try:
                stats_text = page.locator('header section ul').first.inner_text(timeout=5000)
                followers_match = re.search(r'([\d,\.]+[KM]?)\s*followers?', stats_text, re.IGNORECASE)
                if followers_match:
                    followers_str = followers_match.group(1)
                    if 'K' in followers_str.upper():
                        followers = int(float(followers_str.replace('K', '').replace(',', '')) * 1000)
                    elif 'M' in followers_str.upper():
                        followers = int(float(followers_str.replace('M', '').replace(',', '')) * 1000000)
                    else:
                        followers = int(followers_str.replace(',', ''))
                    data['followers'] = followers
            except:
                data['followers'] = 0

        # External URL (if not extracted via JS)
        if 'external_url' not in data or not data.get('external_url'):
            try:
                link = page.locator('header a[href^="http"]').first
                if link:
                    data['external_url'] = link.get_attribute('href', timeout=5000)
            except:
                data['external_url'] = ''

        # Business account (if not extracted via JS)
        if 'is_business_account' not in data:
            try:
                contact_button = page.locator('button:has-text("Contact")').first
                data['is_business_account'] = contact_button.count() > 0
            except:
                data['is_business_account'] = False

        # Extract postal code and address from bio
        data['postal_code'] = extract_postal_code(data['biography'])
        data['address'] = extract_address(data['biography'])
        data['phone_number'] = extract_phone(data['biography'])

        return data

    except Exception as e:
        print(f"      ⚠️  Failed to extract profile data: {e}")
        return None

def extract_postal_code(text):
    """Extract Japanese postal code from text"""
    if not text:
        return ''
    pattern = r'〒?\s*(\d{3})-?(\d{4})'
    match = re.search(pattern, text)
    if match:
        return f"{match.group(1)}-{match.group(2)}"
    return ''

def extract_address(text):
    """Extract Japanese address from text"""
    if not text:
        return ''
    pattern = r'((?:北海道|東京都|大阪府|京都府|.{2,3}県)[^\n]{0,80}?(?:市|区|町|村|丁目|番地|号|ビル|F))'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_phone(text):
    """Extract phone number from text"""
    if not text:
        return ''
    pattern = r'0\d{1,4}[-\s]?\d{1,4}[-\s]?\d{4}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return ''

def save_to_csv(data, hashtag):
    """Save collected data to CSV"""
    import csv

    if not data:
        print("⚠️  No data to save")
        return None

    output_file = f"dental_instagram_{hashtag}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    headers = [
        'instagram_handle', 'full_name', 'postal_code', 'address',
        'phone_number', 'external_url', 'followers',
        'biography', 'is_business_account', 'collected_at'
    ]

    # Normalize data
    normalized_data = []
    for profile in data:
        normalized_data.append({
            'instagram_handle': profile.get('instagram_handle', ''),
            'full_name': profile.get('full_name', ''),
            'postal_code': profile.get('postal_code', ''),
            'address': profile.get('address', ''),
            'phone_number': profile.get('phone_number', ''),
            'external_url': profile.get('external_url', ''),
            'followers': profile.get('followers', 0),
            'biography': profile.get('biography', '').replace('\n', ' '),
            'is_business_account': profile.get('is_business_account', False),
            'collected_at': profile.get('collected_at', '')
        })

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(normalized_data)

    print(f"✅ CSV saved: {output_file}")
    return output_file

def main():
    """Main execution"""
    print("🦷 Dental Instagram Scraper (Browser Mode)")
    print("=" * 60)
    print("\nThis tool uses browser automation to collect data from Instagram")
    print("You will see the browser window during collection (for debugging)\n")

    # Hashtags to search
    hashtags = ["歯科", "歯科医院", "歯医者", "小児歯科"]

    all_profiles = []

    for hashtag in hashtags:
        print(f"\n{'='*60}")
        print(f"Starting collection for #{hashtag}")
        print(f"{'='*60}\n")

        profiles = collect_from_hashtag(
            hashtag=hashtag,
            max_posts=20,  # Collect 20 posts per hashtag
            headless=False  # Show browser for debugging
        )

        all_profiles.extend(profiles)

        print(f"\n{'='*60}")
        print(f"Completed #{hashtag}: {len(profiles)} dental clinics found")
        print(f"{'='*60}\n")

        # Wait between hashtags to avoid rate limits
        if hashtag != hashtags[-1]:
            print("⏸️  Waiting 30 seconds before next hashtag...\n")
            time.sleep(30)

    # Remove duplicates
    seen = set()
    unique_profiles = []
    for profile in all_profiles:
        username = profile['instagram_handle']
        if username not in seen:
            seen.add(username)
            unique_profiles.append(profile)

    print(f"\n{'='*60}")
    print(f"FINAL RESULTS")
    print(f"{'='*60}")
    print(f"Total profiles collected: {len(all_profiles)}")
    print(f"Unique dental clinics: {len(unique_profiles)}")
    print(f"With postal code: {sum(1 for p in unique_profiles if p.get('postal_code'))}")
    print(f"With address: {sum(1 for p in unique_profiles if p.get('address'))}")

    # Save to CSV
    if unique_profiles:
        csv_file = save_to_csv(unique_profiles, 'all_hashtags')
        print(f"\n✅ Collection complete! Output: {csv_file}")
    else:
        print("\n⚠️  No dental clinic data collected")

if __name__ == "__main__":
    main()
