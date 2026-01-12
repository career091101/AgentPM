#!/usr/bin/env python3
"""
X API Tier確認スクリプト

X API v2を直接呼び出して、現在のAPI Tierを確認します。
Analytics APIへのアクセス可否を判定します。

Usage:
    python3 scripts/check_x_api_tier.py
"""

import requests
import json
import os
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
                # 引用符を除去
                value = value.strip().strip('"').strip("'")
                env_vars[key.strip()] = value

X_BEARER_TOKEN = env_vars.get("X_BEARER_TOKEN")

print("=" * 60)
print("X API Tier確認")
print("=" * 60)
print()

# ========================================
# STEP 1: 自分のユーザー情報取得（Free Tier OK）
# ========================================
print("📋 STEP 1: 自分のユーザー情報取得")
print("-" * 60)

headers = {
    "Authorization": f"Bearer {X_BEARER_TOKEN}"
}

try:
    response = requests.get(
        "https://api.twitter.com/2/users/me",
        headers=headers,
        params={
            "user.fields": "public_metrics,created_at"
        },
        timeout=30
    )
    response.raise_for_status()
    user_data = response.json()

    user = user_data.get("data", {})
    print("✅ ユーザー情報取得成功")
    print(f"   User ID: {user.get('id')}")
    print(f"   Username: @{user.get('username')}")
    print(f"   Name: {user.get('name')}")
    print(f"   Followers: {user.get('public_metrics', {}).get('followers_count', 0):,}")
    print(f"   Following: {user.get('public_metrics', {}).get('following_count', 0):,}")
    print(f"   Created At: {user.get('created_at')}")
    print()

    USER_ID = user.get('id')

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTPエラー: {e.response.status_code}")
    print(f"   レスポンス: {e.response.text}")
    print()
    print("原因:")
    print("   - Bearer Tokenが無効または期限切れ")
    print("   - .envファイルのX_BEARER_TOKENを確認してください")
    exit(1)
except Exception as e:
    print(f"❌ エラー: {str(e)}")
    exit(1)

# ========================================
# STEP 2: 自分のツイート取得（Free Tier OK）
# ========================================
print("📋 STEP 2: 自分のツイート取得")
print("-" * 60)

try:
    response = requests.get(
        f"https://api.twitter.com/2/users/{USER_ID}/tweets",
        headers=headers,
        params={
            "max_results": 10,
            "tweet.fields": "created_at,public_metrics"
        },
        timeout=30
    )
    response.raise_for_status()
    tweets_data = response.json()

    tweets = tweets_data.get("data", [])
    print(f"✅ ツイート取得成功: {len(tweets)}件")
    print()

    if len(tweets) > 0:
        print("📝 最新3件のツイート:")
        for i, tweet in enumerate(tweets[:3], 1):
            print(f"\n   {i}. Tweet ID: {tweet.get('id')}")
            print(f"      Text: {tweet.get('text', '')[:60]}...")
            print(f"      Created: {tweet.get('created_at')}")
            public_metrics = tweet.get('public_metrics', {})
            print(f"      Metrics:")
            print(f"         Impressions: {public_metrics.get('impression_count', 'N/A')}")
            print(f"         Likes: {public_metrics.get('like_count', 0)}")
            print(f"         Retweets: {public_metrics.get('retweet_count', 0)}")
            print(f"         Replies: {public_metrics.get('reply_count', 0)}")

        # LATEST_TWEET_IDを保存
        LATEST_TWEET_ID = tweets[0].get('id')
    else:
        print("⚠️  ツイートが見つかりません")
        LATEST_TWEET_ID = None

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTPエラー: {e.response.status_code}")
    print(f"   レスポンス: {e.response.text}")
    LATEST_TWEET_ID = None
except Exception as e:
    print(f"❌ エラー: {str(e)}")
    LATEST_TWEET_ID = None

# ========================================
# STEP 3: Analytics API確認（Basic Tier以上のみ）
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 3: Analytics API確認（重要）")
print("-" * 60)

if LATEST_TWEET_ID is None:
    print("⚠️  ツイートIDが取得できなかったためスキップ")
else:
    # X API v2のAnalytics APIエンドポイント（存在しない可能性あり）
    # 注: X API v2には明示的な "Analytics API" がない
    # public_metricsにimpression_countが含まれているかで判定

    try:
        # 個別ツイートの詳細取得
        response = requests.get(
            f"https://api.twitter.com/2/tweets/{LATEST_TWEET_ID}",
            headers=headers,
            params={
                "tweet.fields": "created_at,public_metrics,non_public_metrics,organic_metrics,promoted_metrics"
            },
            timeout=30
        )
        response.raise_for_status()
        tweet_detail = response.json()

        tweet = tweet_detail.get("data", {})
        print("✅ ツイート詳細取得成功")
        print(f"   Tweet ID: {tweet.get('id')}")
        print()

        # Public Metrics（Free Tierでもアクセス可能）
        public_metrics = tweet.get('public_metrics', {})
        print("Public Metrics（Free Tierでアクセス可能）:")
        print(f"   Impressions: {public_metrics.get('impression_count', 'N/A')}")
        print(f"   Likes: {public_metrics.get('like_count', 0)}")
        print(f"   Retweets: {public_metrics.get('retweet_count', 0)}")
        print(f"   Replies: {public_metrics.get('reply_count', 0)}")
        print()

        # Non-Public Metrics（Basic Tier以上が必要）
        non_public_metrics = tweet.get('non_public_metrics')
        if non_public_metrics:
            print("✅ Non-Public Metrics取得成功（Basic Tier以上確定）:")
            print(f"   URL Link Clicks: {non_public_metrics.get('url_link_clicks', 0)}")
            print(f"   User Profile Clicks: {non_public_metrics.get('user_profile_clicks', 0)}")
            print()
            API_TIER = "Basic Tier以上"
        else:
            print("❌ Non-Public Metricsアクセス不可（Free Tier確定）")
            print()
            API_TIER = "Free Tier"

        # Organic Metrics（Basic Tier以上が必要）
        organic_metrics = tweet.get('organic_metrics')
        if organic_metrics:
            print("✅ Organic Metrics取得成功（Basic Tier以上確定）:")
            print(f"   Impressions: {organic_metrics.get('impression_count', 0)}")
            print(f"   Likes: {organic_metrics.get('like_count', 0)}")
            print()
        else:
            print("❌ Organic Metricsアクセス不可（Free Tier確定）")
            print()

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print("❌ 403 Forbidden: Analytics APIアクセス不可")
            print("   → Free Tier確定")
            print()
            print("   Basic Tier以上へのアップグレードが必要です:")
            print("   - Free Tier: $0/month（Analytics不可）")
            print("   - Basic Tier: $100/month（Analytics可能）")
            print("   - Pro Tier: $5,000/month（高度なAnalytics）")
            print()
            API_TIER = "Free Tier"
        else:
            print(f"❌ HTTPエラー: {e.response.status_code}")
            print(f"   レスポンス: {e.response.text}")
            API_TIER = "不明"
    except Exception as e:
        print(f"❌ エラー: {str(e)}")
        API_TIER = "不明"

# ========================================
# 最終判定
# ========================================
print("\n" + "=" * 60)
print("🎯 最終判定")
print("=" * 60)
print()
print(f"あなたのX API Tier: **{API_TIER}**")
print()

if API_TIER == "Free Tier":
    print("❌ Free TierではAnalytics APIにアクセスできません")
    print()
    print("Late APIでX/Twitter analyticsを取得するには:")
    print("   1. X Developer Portal → Products → Basic Tier購入（$100/month）")
    print("      URL: https://developer.twitter.com/en/portal/products")
    print("   2. Late APIで再認証（新しいスコープ取得）")
    print()
    print("代替案:")
    print("   - X Analytics Dashboardで手動確認（無料）")
    print("     URL: https://analytics.x.com")
    print("   - Late APIのX投稿を一時停止し、LinkedIn/Threads/Instagramに集中")
elif API_TIER == "Basic Tier以上":
    print("✅ Basic Tier以上でAnalytics APIアクセス可能")
    print()
    print("Late APIでデータ取得できない場合:")
    print("   1. Late Dashboard → X/Twitter → Disconnect → Reconnect")
    print("   2. Late APIサポートに問い合わせ（X API Basicプラン契約済みを伝える）")
else:
    print("⚠️  API Tierが判定できませんでした")
    print()
    print("手動確認:")
    print("   1. X Developer Portal → Dashboard → Usage")
    print("      URL: https://developer.twitter.com/en/portal/dashboard")
    print("   2. Current Planを確認")

print()
print("=" * 60)
