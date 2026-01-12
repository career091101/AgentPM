#!/usr/bin/env python3
"""
Late API投稿一覧取得テスト
"""

import sys
import os
import json

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    load_config,
    get_headers,
    LateAPIError
)
import requests


def test_list_posts():
    """Late API投稿一覧を取得してレスポンスを確認"""
    config = load_config()
    api_key = config["api_key"]
    base_url = config["base_url"]

    print("=" * 70)
    print("Late API投稿一覧取得テスト")
    print("=" * 70)
    print()
    print(f"Base URL: {base_url}")
    print()

    try:
        # GET /posts を試す
        print("1. GET /posts を試行...")
        response = requests.get(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            timeout=30
        )

        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:500]}")
        print()

        if response.status_code == 200:
            data = response.json()
            print("   レスポンス構造:")
            print(f"   - Keys: {list(data.keys())}")

            if "data" in data:
                posts = data["data"]
                print(f"   - 投稿数: {len(posts)}件")

                if posts:
                    print()
                    print("   最初の投稿:")
                    print(json.dumps(posts[0], indent=2, ensure_ascii=False))
            elif isinstance(data, list):
                print(f"   - 投稿数: {len(data)}件")

                if data:
                    print()
                    print("   最初の投稿:")
                    print(json.dumps(data[0], indent=2, ensure_ascii=False))
        else:
            print(f"   ❌ エラー: {response.status_code}")

    except Exception as e:
        print(f"   ❌ 例外: {e}")

    print()

    # GET /queue を試す（Late APIによっては別エンドポイント）
    try:
        print("2. GET /queue を試行...")
        response = requests.get(
            f"{base_url}/queue",
            headers=get_headers(api_key),
            timeout=30
        )

        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:500]}")
        print()

    except Exception as e:
        print(f"   ❌ 例外: {e}")

    print()


if __name__ == "__main__":
    test_list_posts()
