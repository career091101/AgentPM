#!/usr/bin/env python3
"""
Test script for Instagram collection using cookies
"""
import instaloader
from pathlib import Path
import json

def test_cookie_login():
    """Test Instaloader login with cookies"""
    print("🔍 Testing Instagram cookie authentication...\n")

    # Create Instaloader instance
    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False
    )

    try:
        # Import cookies
        cookie_file = Path("instagram_cookies.txt")
        if not cookie_file.exists():
            print("❌ Cookie file not found!")
            return False

        print("📂 Loading cookies from instagram_cookies.txt...")
        loader.load_session_from_file("74979810942", filename="instagram_cookies.txt")
        print("✅ Cookies loaded successfully!")

        # Test by getting a hashtag
        print("\n🔍 Testing hashtag search: #歯科...")
        hashtag = instaloader.Hashtag.from_name(loader.context, "歯科")

        print(f"✅ Hashtag found!")
        print(f"   Name: {hashtag.name}")

        # Get first 3 posts
        print("\n📥 Fetching first 3 posts...")
        posts = []
        for i, post in enumerate(hashtag.get_posts()):
            if i >= 3:
                break
            posts.append({
                'shortcode': post.shortcode,
                'owner': post.owner_username,
                'caption': post.caption[:50] if post.caption else None,
                'likes': post.likes
            })
            print(f"   {i+1}. @{post.owner_username} - {post.likes} likes")

        print(f"\n✅ Successfully fetched {len(posts)} posts!")

        # Get first profile
        if posts:
            print(f"\n👤 Testing profile fetch: @{posts[0]['owner']}...")
            profile = instaloader.Profile.from_username(loader.context, posts[0]['owner'])
            print(f"✅ Profile fetched!")
            print(f"   Username: {profile.username}")
            print(f"   Full name: {profile.full_name}")
            print(f"   Followers: {profile.followers}")
            print(f"   Is business: {profile.is_business_account}")
            print(f"   Biography: {profile.biography[:100]}...")

        print("\n🎉 All tests passed! Instagram collection is working.")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_cookie_login()
