#!/usr/bin/env python3
"""
重複投稿を削除して最終調整
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    load_config,
    get_headers,
)
import requests


# ===========================
# 削除対象ID
# ===========================

DELETE_IDS = [
    # Threads個別投稿（3件）
    "695864aa38609c72a1d86dd1",  # 投稿2: 11:02
    "695864a838609c72a1d86db8",  # 投稿3: 11:01
    "695864a638609c72a1d86d9f",  # 投稿6: 11:00（個別）

    # Threadsスレッド重複（1件削除、1件残す）
    "695865b1042b180bc998bf83",  # 投稿5: 11:00（重複）削除
    # "6958679e7eb2560d2ac78800",  # 投稿4: 11:00（正）残す

    # LinkedIn重複（古い3件を削除、最新1件を残す）
    "69586404d3ea5a7fc9a7c5de",  # 投稿10: 764字（古い）
    "695866f47eb2560d2ac783e5",  # 投稿9: 1544字
    "695867187eb2560d2ac7850e",  # 投稿8: 1544字
    # "695867a07eb2560d2ac78815",  # 投稿7: 1544字（最新）残す
]


def delete_post(post_id: str) -> bool:
    """Late API投稿を削除"""
    config = load_config()
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        response = requests.delete(
            f"{base_url}/posts/{post_id}",
            headers=get_headers(api_key),
            timeout=30
        )

        if response.status_code == 200 or response.status_code == 204:
            return True
        else:
            return False

    except Exception as e:
        return False


def main():
    print("=" * 70)
    print("重複投稿削除")
    print("=" * 70)
    print()
    print(f"削除対象: {len(DELETE_IDS)}件")
    print()

    deleted_count = 0
    for post_id in DELETE_IDS:
        print(f"削除中: {post_id}")
        if delete_post(post_id):
            print("   ✅ 削除成功")
            deleted_count += 1
        else:
            print("   ❌ 削除失敗")

    print()
    print(f"削除完了: {deleted_count}/{len(DELETE_IDS)}件")
    print()
    print("=" * 70)
    print("最終スケジュール（予定）")
    print("=" * 70)
    print()
    print("2026-01-07T11:00:00.000Z (JST 20:00) - Threadsスレッド（5投稿）")
    print("2026-01-07T11:05:00.000Z (JST 20:05) - Twitterスレッド（7ツイート）")
    print("2026-01-06T23:00:00.000Z (JST 08:00) - LinkedIn（本文+First Comment）")
    print()


if __name__ == "__main__":
    main()
