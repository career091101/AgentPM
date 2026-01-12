#!/usr/bin/env python3
"""
X Analytics取得（Bearer Token版）

OAuth 1.0aが401エラーの場合の代替手段。
Bearer Tokenでpublic_metricsを取得します。

Usage:
    python3 scripts/fetch_x_analytics_bearer.py
"""

import requests
import json
import os
from datetime import datetime
from pathlib import Path

# プロジェクトルート
project_root = Path(__file__).parent.parent

# .env読み込み
env_file = project_root / ".env"
env_vars = {}

if env_file.exists():
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                value = value.strip().strip('"').strip("'")
                env_vars[key.strip()] = value

X_BEARER_TOKEN = env_vars.get("X_BEARER_TOKEN")

print("=" * 60)
print("X Analytics取得（Bearer Token版）")
print("=" * 60)
print()

# ========================================
# STEP 1: Late API対象ツイートのAnalytics取得
# ========================================
print("📋 STEP 1: Late API対象ツイートのAnalytics取得")
print("-" * 60)

# Late APIで問題のあった投稿ID
TARGET_TWEET_IDS = [
    "2007770258292043823"  # Late APIで0だった投稿
]

headers = {
    "Authorization": f"Bearer {X_BEARER_TOKEN}"
}

all_analytics = []

for tweet_id in TARGET_TWEET_IDS:
    try:
        response = requests.get(
            f"https://api.twitter.com/2/tweets/{tweet_id}",
            headers=headers,
            params={
                "tweet.fields": "created_at,public_metrics"
            },
            timeout=30
        )
        response.raise_for_status()
        tweet_data = response.json()

        tweet = tweet_data.get("data", {})
        print(f"\n✅ ツイート取得成功: {tweet_id}")
        print(f"   Text: {tweet.get('text', '')[:60]}...")
        print(f"   Created: {tweet.get('created_at')}")
        print()

        # Public Metrics
        public_metrics = tweet.get("public_metrics", {})
        impressions = public_metrics.get("impression_count", 0)
        likes = public_metrics.get("like_count", 0)
        retweets = public_metrics.get("retweet_count", 0)
        replies = public_metrics.get("reply_count", 0)
        quotes = public_metrics.get("quote_count", 0)
        bookmarks = public_metrics.get("bookmark_count", 0)

        print("Public Metrics:")
        print(f"   Impressions: {impressions:,}")
        print(f"   Likes: {likes:,}")
        print(f"   Retweets: {retweets:,}")
        print(f"   Replies: {replies:,}")
        print(f"   Quotes: {quotes:,}")
        print(f"   Bookmarks: {bookmarks:,}")
        print()

        # Engagement Rate計算
        if impressions > 0:
            er = ((likes + retweets*2 + replies*3) / impressions) * 100
            print(f"   Engagement Rate: {er:.2f}%")
        else:
            er = 0
            print(f"   Engagement Rate: N/A（Impressions=0）")
        print()

        # 結果を保存
        analytics_record = {
            "tweet_id": tweet_id,
            "url": f"https://twitter.com/i/web/status/{tweet_id}",
            "text": tweet.get("text", ""),
            "created_at": tweet.get("created_at"),
            "public_metrics": {
                "impressions": impressions,
                "likes": likes,
                "retweets": retweets,
                "replies": replies,
                "quotes": quotes,
                "bookmarks": bookmarks
            },
            "engagement_rate": round(er, 2),
            "fetched_at": datetime.now().isoformat(),
            "api_method": "Bearer Token (X API v2)"
        }

        all_analytics.append(analytics_record)

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTPエラー: {e.response.status_code}")
        print(f"   レスポンス: {e.response.text}")
    except Exception as e:
        print(f"❌ エラー: {str(e)}")

# ========================================
# STEP 2: 結果をJSON保存
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 2: 結果をJSON保存")
print("=" * 60)

output_file = project_root / "data" / f"x_analytics_bearer_{datetime.now().strftime('%Y%m%d')}.json"
output_file.parent.mkdir(parents=True, exist_ok=True)

output_data = {
    "fetched_at": datetime.now().isoformat(),
    "api_method": "Bearer Token (X API v2)",
    "total_tweets": len(all_analytics),
    "analytics": all_analytics
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\n✅ 結果を保存: {output_file}")
print(f"   総ツイート数: {len(all_analytics)}")
print()

# ========================================
# STEP 3: Late APIとの比較
# ========================================
print("=" * 60)
print("📋 STEP 3: Late APIとの比較")
print("=" * 60)
print()

print("Late API結果（2026-01-05取得）:")
print("   Impressions: 0")
print("   Likes: 0")
print("   Last Updated: null")
print()

if all_analytics:
    print(f"Bearer Token結果（本スクリプト）:")
    for record in all_analytics:
        print(f"   Impressions: {record['public_metrics']['impressions']:,}")
        print(f"   Likes: {record['public_metrics']['likes']:,}")
        print(f"   Engagement Rate: {record['engagement_rate']:.2f}%")
        print()

    print("✅ Bearer Tokenを使用することで、X Analyticsを取得できました！")
    print()
    print("次のステップ:")
    print("1. X Developer Portal → Access Token再生成")
    print("2. Late Dashboard → X/Twitter再認証")
    print("3. 24時間後にLate APIで再確認")

print()
print("=" * 60)
