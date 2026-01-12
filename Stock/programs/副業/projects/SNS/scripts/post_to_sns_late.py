#!/usr/bin/env python3
"""
Late API経由でSNS投稿をスケジュール予約するスクリプト

Usage:
    python3 post_to_sns_late.py --file approved_post_20260104_001.json --platforms LinkedIn X --scheduled-time "2026-01-04T13:30:00"
"""

import os
import json
import argparse
import requests
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# Late API設定
LATE_API_BASE_URL = "https://getlate.dev/api/v1"
LATE_API_KEY = os.getenv("LATE_API_KEY")

# Late APIアカウントID（各プラットフォーム）
LATE_ACCOUNT_IDS = {
    "LinkedIn": os.getenv("LATE_LINKEDIN_ACCOUNT_ID"),
    "X": os.getenv("LATE_TWITTER_ACCOUNT_ID"),
    "Facebook": os.getenv("LATE_FACEBOOK_ACCOUNT_ID"),
    "Threads": os.getenv("LATE_THREADS_ACCOUNT_ID")
}

# プラットフォーム名マッピング（Late API仕様）
PLATFORM_MAPPING = {
    "LinkedIn": "linkedin",
    "X": "twitter",
    "Facebook": "facebook",
    "Threads": "threads"
}


def load_approved_post(file_path: str) -> dict:
    """
    approved_post_*.jsonファイルを読み込み
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def schedule_post_to_late(
    content: str,
    platforms: list[str],
    scheduled_time: str,
    thread_posts: list[str] = None,
    recommended_format: str = "single"
) -> dict:
    """
    Late API経由で投稿をスケジュール予約（スレッド対応）

    Args:
        content: 投稿内容（single投稿 or スレッド1投稿目）
        platforms: 投稿先プラットフォームリスト（例: ["LinkedIn", "X"]）
        scheduled_time: スケジュール時刻（ISO 8601形式: "2026-01-04T13:30:00"）
        thread_posts: スレッド投稿リスト（オプション）
        recommended_format: "single" or "thread"

    Returns:
        Late APIのレスポンス
    """
    if not LATE_API_KEY:
        raise ValueError("LATE_API_KEY environment variable not set")

    # プラットフォーム設定を作成
    platform_configs = []
    for platform in platforms:
        account_id = LATE_ACCOUNT_IDS.get(platform)
        if not account_id:
            print(f"⚠️  Warning: {platform} account ID not configured, skipping...")
            continue

        platform_name = PLATFORM_MAPPING.get(platform, platform.lower())

        # プラットフォーム固有データ設定
        platform_config = {
            "platform": platform_name,
            "accountId": account_id
        }

        # スレッド投稿の場合、platformSpecificDataを追加
        if recommended_format == "thread" and thread_posts:
            platform_config["platformSpecificData"] = {
                "threadItems": [{"content": post} for post in thread_posts]
            }

        platform_configs.append(platform_config)

    if not platform_configs:
        raise ValueError("No valid platforms configured")

    # ISO 8601形式に変換（UTCで送信）
    # フロントエンドからはJSTで送られてくるので、UTCに変換
    dt = datetime.fromisoformat(scheduled_time.replace('Z', '+00:00'))
    scheduled_time_utc = dt.isoformat()

    # Late APIリクエスト
    url = f"{LATE_API_BASE_URL}/posts"
    headers = {
        "Authorization": f"Bearer {LATE_API_KEY}",
        "Content-Type": "application/json"
    }

    # スレッド投稿の場合、最初の投稿内容を設定（Late API要件）
    if recommended_format == "thread" and thread_posts:
        content = thread_posts[0]

    payload = {
        "content": content,  # 必須フィールド
        "scheduledFor": scheduled_time_utc,
        "timezone": "Asia/Tokyo",  # JSTタイムゾーン
        "platforms": platform_configs,
        "publishNow": False,  # スケジュール予約（即時投稿ではない）
        "crosspostingEnabled": True
    }

    print(f"📤 Scheduling post to Late API...")
    print(f"   Content: {content[:50]}...")
    print(f"   Format: {recommended_format}")
    if recommended_format == "thread" and thread_posts:
        print(f"   Thread posts: {len(thread_posts)} items")
    print(f"   Platforms: {', '.join(platforms)}")
    print(f"   Scheduled for: {scheduled_time_utc}")

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    result = response.json()
    print(f"✅ Post scheduled successfully!")
    print(f"   Post ID: {result.get('post', {}).get('_id', 'N/A')}")
    print(f"   Status: {result.get('post', {}).get('status', 'N/A')}")

    return result


def save_result(result: dict, scheduled_post_id: str):
    """
    投稿結果をJSONファイルに保存
    """
    data_dir = Path(__file__).parent.parent / "data"
    result_file = data_dir / f"post_result_{scheduled_post_id}.json"

    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"📁 Result saved to: {result_file}")


def main():
    parser = argparse.ArgumentParser(description="Schedule SNS posts via Late API")
    parser.add_argument("--file", required=True, help="approved_post_*.json file name")
    parser.add_argument("--platforms", nargs="+", required=True, choices=["LinkedIn", "X", "Facebook", "Threads"],
                        help="Target platforms")
    parser.add_argument("--scheduled-time", required=True, help="Scheduled time (ISO 8601 format)")
    parser.add_argument("--scheduled-post-id", required=True, help="Scheduled post ID for result file")
    parser.add_argument("--optimized-content", help="Optimized content (overrides file content)")
    parser.add_argument("--thread-posts", help="Thread posts JSON string (for X/Threads thread mode)")
    parser.add_argument("--recommended-format", default="single", choices=["single", "thread"],
                        help="Posting format: single or thread")
    args = parser.parse_args()

    # approved_post_*.jsonファイルのパス
    data_dir = Path(__file__).parent.parent / "data"
    approved_file = data_dir / args.file

    if not approved_file.exists():
        print(f"❌ Error: {approved_file} not found")
        return

    # 承認済み投稿データ読み込み
    approved_data = load_approved_post(approved_file)

    # 最適化コンテンツが指定されている場合はそれを使用、なければファイルから読み込み
    if args.optimized_content:
        content = args.optimized_content
    else:
        content = approved_data.get("refined_content") or approved_data.get("content")

    # スレッド投稿リストの解析
    thread_posts = None
    if args.thread_posts:
        try:
            thread_posts = json.loads(args.thread_posts)
        except json.JSONDecodeError as e:
            print(f"⚠️  Warning: Failed to parse thread_posts JSON: {e}")
            print(f"   Using single post mode")

    # Late API経由でスケジュール予約
    try:
        result = schedule_post_to_late(
            content,
            args.platforms,
            args.scheduled_time,
            thread_posts=thread_posts,
            recommended_format=args.recommended_format
        )
        save_result(result, args.scheduled_post_id)
        print("\n🎉 Scheduling complete!")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Late API Error: {e}")
        print(f"   Response: {e.response.text}")
        raise
    except Exception as e:
        print(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
