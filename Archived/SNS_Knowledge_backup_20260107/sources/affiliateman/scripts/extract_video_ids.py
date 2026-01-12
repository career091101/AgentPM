#!/usr/bin/env python3
"""
YouTube ID不明のページから動画ソースを抽出するスクリプト
"""

import requests
import re

# 対象URL
URLS = {
    'kanagawagurume': 'https://affiliateman.site/kanagawagurume/',
    'note_ryu': 'https://affiliateman.site/note_ryu/'
}

PASSWORD = "snshack"

def login_and_get_page(url):
    """ページにログインして取得"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })

    # パスワード認証
    print(f"ログイン中: {url}")
    response = session.get(url, allow_redirects=True)

    login_data = {
        'password_protected_pwd': PASSWORD,
        'password_protected_rememberme': '1',
        'Submit': 'ログイン'
    }

    response = session.post(response.url, data=login_data, allow_redirects=True)

    auth_cookies = ['wp-postpass', 'password_protected_auth']
    is_authenticated = any(cookie_name in str(session.cookies) for cookie_name in auth_cookies)

    if not is_authenticated:
        print("✗ ログイン失敗")
        return None

    print("✓ ログイン成功")

    # ページ取得
    response = session.get(url)
    response.encoding = 'utf-8'

    return response.text

def extract_video_sources(html):
    """HTMLから動画ソースを抽出"""
    if not html:
        return None

    # YouTube ID抽出パターン
    youtube_patterns = [
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
        r'youtu\.be/([a-zA-Z0-9_-]{11})',
        r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        r'youtube-nocookie\.com/embed/([a-zA-Z0-9_-]{11})'
    ]

    # Loom URL抽出
    loom_pattern = r'loom\.com/share/([a-f0-9]+)'

    # Vimeo ID抽出
    vimeo_pattern = r'vimeo\.com/video/(\d+)|player\.vimeo\.com/video/(\d+)'

    results = {
        'youtube': set(),
        'loom': set(),
        'vimeo': set()
    }

    # YouTube検索
    for pattern in youtube_patterns:
        matches = re.findall(pattern, html)
        results['youtube'].update(matches)

    # Loom検索
    loom_matches = re.findall(loom_pattern, html)
    results['loom'].update(loom_matches)

    # Vimeo検索
    vimeo_matches = re.findall(vimeo_pattern, html)
    for match in vimeo_matches:
        vid = match[0] or match[1]
        if vid:
            results['vimeo'].add(vid)

    return results

def main():
    print("=" * 60)
    print("動画ソース抽出")
    print("=" * 60)

    all_results = {}

    for key, url in URLS.items():
        print(f"\n[{key}]")
        html = login_and_get_page(url)

        if html:
            sources = extract_video_sources(html)
            all_results[key] = sources

            print(f"YouTube ID: {list(sources['youtube']) if sources['youtube'] else 'なし'}")
            print(f"Loom ID: {list(sources['loom']) if sources['loom'] else 'なし'}")
            print(f"Vimeo ID: {list(sources['vimeo']) if sources['vimeo'] else 'なし'}")
        else:
            print("✗ ページ取得失敗")
            all_results[key] = None

    print("\n" + "=" * 60)
    print("抽出結果サマリー")
    print("=" * 60)

    for key, sources in all_results.items():
        if sources:
            print(f"\n{key}:")
            if sources['youtube']:
                for vid in sources['youtube']:
                    print(f"  YouTube: https://www.youtube.com/watch?v={vid}")
            if sources['loom']:
                for vid in sources['loom']:
                    print(f"  Loom: https://www.loom.com/share/{vid}")
            if sources['vimeo']:
                for vid in sources['vimeo']:
                    print(f"  Vimeo: https://vimeo.com/{vid}")

if __name__ == "__main__":
    main()
