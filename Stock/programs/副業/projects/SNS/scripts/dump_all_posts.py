#!/usr/bin/env python3
"""
Late API全投稿をダンプして確認
"""

import sys
import os
import json
from datetime import datetime

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    load_config,
    get_headers,
    handle_late_api_response
)
import requests


def dump_all_posts():
    """全投稿を取得して表示"""
    config = load_config()
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        response = requests.get(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            timeout=30
        )

        result = handle_late_api_response(response)
        posts = result.get("posts", [])

        print("=" * 70)
        print(f"Late API全投稿一覧（{len(posts)}件）")
        print("=" * 70)
        print()

        for i, post in enumerate(posts, 1):
            post_id = post.get("_id", "N/A")
            content = post.get("content", "")
            scheduled_for = post.get("scheduledFor", "N/A")
            platforms = post.get("platforms", [])

            print(f"投稿 {i}:")
            print(f"   ID: {post_id}")
            print(f"   スケジュール: {scheduled_for}")
            print(f"   文字数: {len(content)}字")
            print(f"   本文（先頭100字）: {content[:100]}...")
            print()

            if platforms:
                for platform_data in platforms:
                    platform = platform_data.get("platform", "N/A")
                    account_id = platform_data.get("accountId", "N/A")
                    platform_specific = platform_data.get("platformSpecificData", {})

                    print(f"   プラットフォーム: {platform}")
                    print(f"   アカウントID: {account_id}")

                    if platform_specific:
                        print(f"   platformSpecificData:")
                        if "threadItems" in platform_specific:
                            thread_items = platform_specific["threadItems"]
                            print(f"      - threadItems: {len(thread_items)}件")
                        else:
                            print(f"      - Keys: {list(platform_specific.keys())}")

                    print()

            print("-" * 70)
            print()

        # 2026-01-07の投稿のみフィルタ
        print()
        print("=" * 70)
        print("2026-01-07の投稿のみ")
        print("=" * 70)
        print()

        jan7_posts = [p for p in posts if p.get("scheduledFor", "").startswith("2026-01-07")]

        for i, post in enumerate(jan7_posts, 1):
            scheduled_for = post.get("scheduledFor", "N/A")
            platforms = post.get("platforms", [])
            platform = platforms[0].get("platform", "N/A") if platforms else "N/A"
            platform_specific = platforms[0].get("platformSpecificData", {}) if platforms else {}
            has_thread = "threadItems" in platform_specific

            print(f"{i}. {scheduled_for} - {platform} - スレッド: {has_thread}")

        print()

    except Exception as e:
        print(f"❌ エラー: {e}")


if __name__ == "__main__":
    dump_all_posts()
