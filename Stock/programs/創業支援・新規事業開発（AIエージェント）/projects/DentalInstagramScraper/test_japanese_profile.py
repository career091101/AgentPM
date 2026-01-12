#!/usr/bin/env python3
"""
Test Japanese dental clinic profile fetch
"""
import instaloader
import http.cookiejar
from pathlib import Path
import time

def test_japanese_profiles():
    """Test with Japanese dental clinic profiles"""
    print("🔍 Testing Japanese dental clinic profiles...\n")

    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        save_metadata=False
    )

    try:
        # Load and inject cookies
        cookie_file = Path("instagram_cookies.txt")
        cj = http.cookiejar.MozillaCookieJar(str(cookie_file))
        cj.load(ignore_discard=True, ignore_expires=True)
        loader.context._session.cookies = cj

        print(f"✅ Loaded {len(cj)} cookies\n")

        # Test with some known Japanese dental clinic accounts
        # These are examples - we'll need to build a real list
        test_profiles = [
            "shikaiin_tokyo",      # Example - may not exist
            "dentalclinic_jp",     # Example - may not exist
            "dentaltown",          # We know this works
        ]

        successful_profiles = []

        for username in test_profiles:
            try:
                print(f"📥 Fetching @{username}...")
                profile = instaloader.Profile.from_username(loader.context, username)

                print(f"   ✅ Success!")
                print(f"      Name: {profile.full_name}")
                print(f"      Followers: {profile.followers:,}")
                print(f"      Business: {profile.is_business_account}")

                bio_preview = profile.biography[:100] if profile.biography else "No bio"
                print(f"      Bio: {bio_preview}...")

                # Check for dental keywords
                bio_lower = profile.biography.lower() if profile.biography else ""
                dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic', '矯正']
                is_dental = any(keyword in bio_lower for keyword in dental_keywords)

                print(f"      🦷 Dental clinic: {'Yes' if is_dental else 'No'}")

                if is_dental:
                    successful_profiles.append(username)

                print()
                time.sleep(3)

            except Exception as e:
                print(f"   ❌ Failed: {e}\n")

        print(f"\n✅ Successfully found {len(successful_profiles)} dental profiles:")
        for username in successful_profiles:
            print(f"   - @{username}")

        return successful_profiles

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return []

if __name__ == "__main__":
    test_japanese_profiles()
