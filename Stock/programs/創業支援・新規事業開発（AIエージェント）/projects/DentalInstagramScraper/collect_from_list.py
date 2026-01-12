#!/usr/bin/env python3
"""
Collect dental clinic data from a list of Instagram handles
This is the working alternative since hashtag search returns 404
"""
import instaloader
import http.cookiejar
from pathlib import Path
import time
import json
import csv
from datetime import datetime
import re

def extract_postal_code(text):
    """Extract Japanese postal code from text"""
    if not text:
        return None
    pattern = r'〒?\s*(\d{3})-?(\d{4})'
    match = re.search(pattern, text)
    if match:
        return f"{match.group(1)}-{match.group(2)}"
    return None

def extract_address(text):
    """Extract Japanese address from text"""
    if not text:
        return None

    # Pattern for Japanese addresses
    pattern = r'((?:北海道|東京都|大阪府|京都府|.{2,3}県)[^\n]{0,80}?(?:市|区|町|村|丁目|番地|号|ビル|F))'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def extract_phone(text):
    """Extract phone number from text"""
    if not text:
        return None
    pattern = r'0\d{1,4}[-\s]?\d{1,4}[-\s]?\d{4}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None

def collect_dental_data(handles_list):
    """
    Collect data from a list of Instagram handles

    Args:
        handles_list: List of Instagram usernames (without @)
    """
    print(f"🔍 Collecting data from {len(handles_list)} Instagram profiles...\n")

    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        save_metadata=False
    )

    # Load cookies
    cookie_file = Path("instagram_cookies.txt")
    if not cookie_file.exists():
        print("❌ Cookie file not found!")
        return []

    cj = http.cookiejar.MozillaCookieJar(str(cookie_file))
    cj.load(ignore_discard=True, ignore_expires=True)
    loader.context._session.cookies = cj

    print(f"✅ Loaded {len(cj)} cookies\n")

    collected_data = []
    dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic', '矯正', '小児歯科']

    for i, username in enumerate(handles_list, 1):
        print(f"[{i}/{len(handles_list)}] 📥 Fetching @{username}...")

        try:
            profile = instaloader.Profile.from_username(loader.context, username)

            # Check if it's a dental clinic
            bio_lower = profile.biography.lower() if profile.biography else ""
            is_dental = any(kw in bio_lower for kw in dental_keywords)

            if not is_dental:
                print(f"   ⚠️  Not a dental clinic, skipping\n")
                time.sleep(2)
                continue

            print(f"   ✅ Found dental clinic!")

            # Extract data
            postal_code = extract_postal_code(profile.biography)
            address = extract_address(profile.biography)
            phone = extract_phone(profile.biography)

            # Combine external URL if available
            if profile.external_url and not (postal_code or address):
                print(f"      ℹ️  No address in bio, external URL: {profile.external_url}")

            data = {
                'instagram_handle': profile.username,
                'clinic_name': profile.full_name,
                'postal_code': postal_code or '',
                'address': address or '',
                'phone_number': phone or '',
                'external_link_url': profile.external_url or '',
                'follower_count': profile.followers,
                'bio_text': profile.biography or '',
                'is_business_account': profile.is_business_account,
                'posts_count': profile.mediacount,
                'needs_manual_review': not (postal_code or address),
                'collected_at': datetime.now().isoformat()
            }

            collected_data.append(data)

            print(f"      Name: {profile.full_name}")
            print(f"      Followers: {profile.followers:,}")
            print(f"      Postal code: {postal_code or '❌ Not found'}")
            print(f"      Address: {(address[:50] + '...') if address else '❌ Not found'}")
            print(f"      ✅ Data collected ({len(collected_data)} total)\n")

            # Rate limiting
            time.sleep(5)

        except Exception as e:
            print(f"   ❌ Error: {e}\n")
            time.sleep(3)

    return collected_data

def save_to_csv(data, output_file=None):
    """Save collected data to CSV"""
    if not data:
        print("⚠️  No data to save")
        return None

    if not output_file:
        output_file = f"dental_instagram_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    headers = [
        'instagram_handle', 'clinic_name', 'postal_code', 'address',
        'phone_number', 'external_link_url', 'follower_count',
        'bio_text', 'is_business_account', 'posts_count',
        'needs_manual_review', 'collected_at'
    ]

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ CSV saved: {output_file}")
    return output_file

def main():
    """Main execution"""
    # Sample seed list - replace with real handles
    # You can find real handles by:
    # 1. Running find_dental_handles.py
    # 2. Manually searching Instagram
    # 3. Using Google: "歯科医院 Instagram site:instagram.com"

    seed_handles = [
        "dentaltown",  # Known working profile
        # Add more real dental clinic handles here
        # Example format:
        # "example_dental_clinic",
        # "tokyo_dental_2024",
        # etc.
    ]

    print("🦷 Dental Instagram Scraper")
    print("=" * 50)
    print(f"\nStarting collection from {len(seed_handles)} handles...\n")

    # Collect data
    data = collect_dental_data(seed_handles)

    # Save results
    if data:
        csv_file = save_to_csv(data)

        # Summary
        print(f"\n📊 Collection Summary:")
        print(f"   Total profiles checked: {len(seed_handles)}")
        print(f"   Dental clinics found: {len(data)}")
        print(f"   With postal code: {sum(1 for d in data if d['postal_code'])}")
        print(f"   With address: {sum(1 for d in data if d['address'])}")
        print(f"   Needs manual review: {sum(1 for d in data if d['needs_manual_review'])}")

        print(f"\n✅ Collection complete!")
        print(f"   Output file: {csv_file}")

    else:
        print("\n⚠️  No dental clinic data collected")
        print("\n💡 Tips:")
        print("   1. Add real dental clinic Instagram handles to the seed_handles list")
        print("   2. Run find_dental_handles.py to discover handles")
        print("   3. Search Google: '歯科医院 Instagram site:instagram.com'")

if __name__ == "__main__":
    main()
