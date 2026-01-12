#!/usr/bin/env python3
"""
Test Instagram collection with direct cookie injection
"""
import instaloader
import http.cookiejar
from pathlib import Path

def test_with_cookies():
    """Test Instaloader with direct cookie injection"""
    print("🔍 Testing Instagram collection with cookies...\n")

    # Create Instaloader instance
    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False
    )

    try:
        # Load cookies from Netscape format
        cookie_file = Path("instagram_cookies.txt")
        if not cookie_file.exists():
            print("❌ Cookie file not found!")
            return False

        print("📂 Loading cookies from instagram_cookies.txt...")
        cj = http.cookiejar.MozillaCookieJar(str(cookie_file))
        cj.load(ignore_discard=True, ignore_expires=True)

        # Inject cookies into Instaloader session
        loader.context._session.cookies = cj

        print(f"✅ Injected {len(cj)} cookies into Instaloader session")
        for cookie in cj:
            print(f"   - {cookie.name[:20]}: {str(cookie.value)[:30]}...")

        # Test by getting a hashtag
        print("\n🔍 Testing hashtag search: #歯科...")
        hashtag = instaloader.Hashtag.from_name(loader.context, "歯科")

        print(f"✅ Hashtag found: #{hashtag.name}")

        # Get first 5 posts
        print("\n📥 Fetching first 5 posts...")
        profiles_found = []

        for i, post in enumerate(hashtag.get_posts()):
            if i >= 5:
                break

            owner = post.owner_username
            caption_preview = (post.caption[:50] + "...") if post.caption else "No caption"

            print(f"\n   Post {i+1}:")
            print(f"      Owner: @{owner}")
            print(f"      Likes: {post.likes}")
            print(f"      Caption: {caption_preview}")

            profiles_found.append(owner)

        print(f"\n✅ Successfully fetched {len(profiles_found)} posts!")

        # Test profile fetch
        if profiles_found:
            username = profiles_found[0]
            print(f"\n👤 Testing profile fetch: @{username}...")

            profile = instaloader.Profile.from_username(loader.context, username)

            print(f"✅ Profile fetched successfully!")
            print(f"   Username: {profile.username}")
            print(f"   Full name: {profile.full_name}")
            print(f"   Followers: {profile.followers:,}")
            print(f"   Is business account: {profile.is_business_account}")
            print(f"   Biography preview: {(profile.biography[:100] + '...') if profile.biography else 'No bio'}")

            # Check if it's a dental clinic
            bio_lower = profile.biography.lower() if profile.biography else ""
            dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic']
            is_dental = any(keyword in bio_lower for keyword in dental_keywords)

            print(f"   🦷 Likely dental clinic: {'Yes' if is_dental else 'No'}")

        print("\n🎉 All tests passed! Instagram collection is working with cookies.")
        return True

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_with_cookies()
    exit(0 if success else 1)
