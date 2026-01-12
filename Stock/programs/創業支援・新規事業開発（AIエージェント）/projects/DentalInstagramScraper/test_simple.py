#!/usr/bin/env python3
"""
Simple test with known dental accounts
"""
import instaloader
import http.cookiejar
from pathlib import Path
import time

def test_simple():
    """Test with direct profile access"""
    print("🔍 Simple Instagram test with cookies...\n")

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

        # Test English hashtag
        print("🔍 Testing English hashtag: #dental...")
        try:
            hashtag = instaloader.Hashtag.from_name(loader.context, "dental")
            print(f"✅ Hashtag found: #{hashtag.name}")

            print("\n📥 Fetching 3 recent posts...")
            for i, post in enumerate(hashtag.get_posts()):
                if i >= 3:
                    break
                print(f"   {i+1}. @{post.owner_username} - {post.likes} likes")
                time.sleep(2)

        except Exception as e:
            print(f"❌ Hashtag search failed: {e}")

        # Test direct profile access
        print("\n👤 Testing direct profile access...")
        test_profiles = ["dentistryworld", "dentaltown"]

        for username in test_profiles:
            try:
                print(f"\n   Fetching @{username}...")
                profile = instaloader.Profile.from_username(loader.context, username)

                print(f"   ✅ Profile found!")
                print(f"      Full name: {profile.full_name}")
                print(f"      Followers: {profile.followers:,}")
                print(f"      Posts: {profile.mediacount}")
                print(f"      Is business: {profile.is_business_account}")
                print(f"      Bio: {(profile.biography[:80] + '...') if profile.biography else 'No bio'}")

                time.sleep(3)

            except Exception as e:
                print(f"   ❌ Failed to fetch @{username}: {e}")

        print("\n🎉 Test complete!")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_simple()
