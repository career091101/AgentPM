#!/usr/bin/env python3
"""
Convert Netscape cookie file to Instaloader session format
"""
import http.cookiejar
import requests
import pickle
from pathlib import Path

def convert_netscape_to_session(cookie_file: str, username: str):
    """Convert Netscape cookie file to Instaloader session"""
    print(f"🔄 Converting cookies for user: {username}\n")

    # Create cookie jar
    cj = http.cookiejar.MozillaCookieJar(cookie_file)
    cj.load(ignore_discard=True, ignore_expires=True)

    print(f"✅ Loaded {len(cj)} cookies from {cookie_file}")

    # Create requests session
    session = requests.Session()
    session.cookies = cj

    # Save as pickle for Instaloader
    session_file = f"{username}_session"
    with open(session_file, 'wb') as f:
        pickle.dump(session.cookies, f)

    print(f"✅ Saved session to {session_file}")
    print(f"\n📝 Cookies converted:")
    for cookie in cj:
        print(f"   - {cookie.name}: {cookie.value[:20]}...")

    return session_file

if __name__ == "__main__":
    cookie_file = "instagram_cookies.txt"
    username = "74979810942"  # ds_user_id from cookies

    if not Path(cookie_file).exists():
        print(f"❌ Cookie file not found: {cookie_file}")
        exit(1)

    try:
        session_file = convert_netscape_to_session(cookie_file, username)
        print(f"\n🎉 Conversion complete!")
        print(f"   Session file: {session_file}")
        print(f"   You can now use this with Instaloader")
    except Exception as e:
        print(f"\n❌ Conversion failed: {e}")
        import traceback
        traceback.print_exc()
