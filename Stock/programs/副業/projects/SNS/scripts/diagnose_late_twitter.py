#!/usr/bin/env python3
"""
Late API X/Twitter連携診断スクリプト

このスクリプトは以下を実行します:
1. Late APIからX/Twitterアカウント情報を取得
2. X/Twitter投稿のステータスを確認
3. Analytics同期状況を診断
4. 再同期トリガーを実行（可能な場合）

Usage:
    python3 scripts/diagnose_late_twitter.py
"""

import requests
import json
import os
from datetime import datetime, timezone
from pathlib import Path

# プロジェクトルート
project_root = Path(__file__).parent.parent

# Late API設定読み込み
env_file = project_root / ".env"
env_vars = {}

if env_file.exists():
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

LATE_API_KEY = env_vars.get("LATE_API_KEY")
LATE_BASE_URL = env_vars.get("LATE_BASE_URL", "https://getlate.dev/api/v1")
LATE_TWITTER_ACCOUNT_ID = env_vars.get("LATE_TWITTER_ACCOUNT_ID", "").strip('"')

print("=" * 60)
print("Late API X/Twitter連携診断")
print("=" * 60)
print(f"実行日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Late Base URL: {LATE_BASE_URL}")
print(f"Twitter Account ID: {LATE_TWITTER_ACCOUNT_ID}")
print()

# HTTPヘッダー
headers = {
    "Authorization": f"Bearer {LATE_API_KEY}",
    "Content-Type": "application/json"
}

# ========================================
# STEP 1: アカウント情報取得
# ========================================
print("📋 STEP 1: アカウント情報取得")
print("-" * 60)

try:
    response = requests.get(
        f"{LATE_BASE_URL}/accounts",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    accounts_data = response.json()

    # X/Twitterアカウントを検索
    twitter_account = None
    for account in accounts_data.get("accounts", []):
        if account.get("platform") == "twitter":
            twitter_account = account
            break

    if twitter_account:
        print("✅ X/Twitterアカウント検出")
        print(f"   Account ID: {twitter_account.get('_id')}")
        print(f"   Username: @{twitter_account.get('username')}")
        print(f"   Display Name: {twitter_account.get('displayName')}")
        print(f"   Followers: {twitter_account.get('followersCount', 'N/A'):,}")
        print(f"   Profile ID: {twitter_account.get('profileId')}")
        print(f"   Status: {twitter_account.get('status', 'Unknown')}")
        print()
    else:
        print("❌ X/Twitterアカウントが見つかりません")
        print("   Late Dashboardで再接続が必要です: https://app.getlate.dev")
        print()
        exit(1)

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTPエラー: {e.response.status_code}")
    print(f"   {e.response.text}")
    exit(1)
except Exception as e:
    print(f"❌ エラー: {str(e)}")
    exit(1)

# ========================================
# STEP 2: X/Twitter投稿一覧取得
# ========================================
print("📋 STEP 2: X/Twitter投稿一覧取得")
print("-" * 60)

try:
    response = requests.get(
        f"{LATE_BASE_URL}/posts",
        headers=headers,
        params={
            "platform": "twitter",
            "limit": 100,
            "sortBy": "publishedAt",
            "order": "desc"
        },
        timeout=30
    )
    response.raise_for_status()
    posts_data = response.json()

    twitter_posts = posts_data.get("posts", [])
    print(f"✅ X/Twitter投稿数: {len(twitter_posts)}")
    print()

    if len(twitter_posts) == 0:
        print("⚠️  X/Twitter投稿が見つかりません")
        print("   Late API経由で投稿が行われていない可能性があります")
        print()
    else:
        print("📝 最新5件の投稿:")
        for i, post in enumerate(twitter_posts[:5], 1):
            print(f"\n   {i}. Post ID: {post.get('_id')}")
            print(f"      Content: {post.get('content', '')[:50]}...")
            print(f"      Published: {post.get('publishedAt', 'N/A')}")
            print(f"      Status: {post.get('status')}")
            print(f"      Platform URL: {post.get('platformPostUrl', 'N/A')}")

            # Analytics情報
            analytics = post.get("analytics", {})
            print(f"      Analytics:")
            print(f"         Impressions: {analytics.get('impressions', 0)}")
            print(f"         Likes: {analytics.get('likes', 0)}")
            print(f"         Retweets: {analytics.get('shares', 0)}")
            print(f"         Replies: {analytics.get('comments', 0)}")
            print(f"         Last Updated: {analytics.get('lastUpdated', 'Never')}")

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTPエラー: {e.response.status_code}")
    print(f"   {e.response.text}")
except Exception as e:
    print(f"❌ エラー: {str(e)}")

# ========================================
# STEP 3: Analytics API直接確認
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 3: Analytics API直接確認")
print("-" * 60)

try:
    response = requests.get(
        f"{LATE_BASE_URL}/analytics",
        headers=headers,
        params={
            "platform": "twitter",
            "limit": 10,
            "sortBy": "date",
            "order": "desc"
        },
        timeout=30
    )
    response.raise_for_status()
    analytics_data = response.json()

    analytics_posts = analytics_data.get("data", {}).get("posts", [])
    print(f"✅ Analytics API経由で取得した投稿数: {len(analytics_posts)}")
    print()

    if len(analytics_posts) == 0:
        print("⚠️  Analytics APIからデータを取得できません")
        print("\n考えられる原因:")
        print("   1. X API Free Tierの制限（Analytics APIアクセス不可）")
        print("   2. Late APIのX統合バグ")
        print("   3. アカウント再認証が必要")
        print()
        print("推奨アクション:")
        print("   1. Late Dashboard → Settings → Connected Accounts → X/Twitter")
        print("   2. API Planを確認（Free/Basic/Pro）")
        print("   3. Disconnect → Reconnect で再認証")
        print()
    else:
        print("📝 Analytics詳細（最新3件）:")
        for i, post in enumerate(analytics_posts[:3], 1):
            analytics = post.get("analytics", {})
            print(f"\n   {i}. Post ID: {post.get('_id')}")
            print(f"      Published: {post.get('publishedAt', 'N/A')}")
            print(f"      Impressions: {analytics.get('impressions', 0):,}")
            print(f"      Likes: {analytics.get('likes', 0):,}")
            print(f"      Shares: {analytics.get('shares', 0):,}")
            print(f"      Comments: {analytics.get('comments', 0):,}")
            print(f"      Views: {analytics.get('views', 0):,}")
            print(f"      ER: {analytics.get('engagementRate', 0):.2f}%")
            print(f"      Last Updated: {analytics.get('lastUpdated', 'Never')}")

except requests.exceptions.HTTPError as e:
    if e.response.status_code == 402:
        print("❌ Analytics Addon未契約")
        print("   Late Dashboardで$10/month Analytics Addonを有効化してください")
        print("   URL: https://app.getlate.dev/settings/billing")
    elif e.response.status_code == 429:
        print("❌ レート制限超過（150 requests/hour）")
        print(f"   Reset: {e.response.headers.get('X-RateLimit-Reset', 'Unknown')}")
    else:
        print(f"❌ HTTPエラー: {e.response.status_code}")
        print(f"   {e.response.text}")
except Exception as e:
    print(f"❌ エラー: {str(e)}")

# ========================================
# STEP 4: 問題のある投稿の詳細診断
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 4: 問題投稿の詳細診断")
print("-" * 60)

problem_post_id = "695a52fdf497177b163fd08d"  # Late APIデータから取得

try:
    response = requests.get(
        f"{LATE_BASE_URL}/posts/{problem_post_id}",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    post_detail = response.json()

    print(f"✅ 投稿詳細取得成功: {problem_post_id}")
    print()
    print(f"Content: {post_detail.get('content', '')[:100]}...")
    print(f"Published: {post_detail.get('publishedAt')}")
    print(f"Status: {post_detail.get('status')}")
    print(f"Platform: {post_detail.get('platform')}")
    print(f"Platform URL: {post_detail.get('platformPostUrl')}")
    print()

    # Analytics詳細
    analytics = post_detail.get("analytics", {})
    print("Analytics詳細:")
    print(f"   Impressions: {analytics.get('impressions', 0):,}")
    print(f"   Reach: {analytics.get('reach', 0):,}")
    print(f"   Likes: {analytics.get('likes', 0):,}")
    print(f"   Comments: {analytics.get('comments', 0):,}")
    print(f"   Shares: {analytics.get('shares', 0):,}")
    print(f"   Clicks: {analytics.get('clicks', 0):,}")
    print(f"   Views: {analytics.get('views', 0):,}")
    print(f"   Engagement Rate: {analytics.get('engagementRate', 0):.2f}%")
    print(f"   Last Updated: {analytics.get('lastUpdated', 'Never')}")
    print()

    # Platforms詳細
    platforms = post_detail.get("platforms", [])
    if platforms:
        print("Platform詳細:")
        for platform in platforms:
            print(f"   Platform: {platform.get('platform')}")
            print(f"   Status: {platform.get('status')}")
            platform_analytics = platform.get("analytics", {})
            print(f"   Analytics:")
            print(f"      Impressions: {platform_analytics.get('impressions', 0):,}")
            print(f"      Likes: {platform_analytics.get('likes', 0):,}")
            print(f"      Engagement Rate: {platform_analytics.get('engagementRate', 0):.2f}%")

    # 診断結果
    print("\n" + "-" * 60)
    print("🔍 診断結果:")
    print("-" * 60)

    if analytics.get('lastUpdated') is None:
        print("❌ 問題検出: lastUpdated = null")
        print("   → Late APIがX APIからデータを一度も取得していない")
        print()
        print("推奨アクション:")
        print("   1. Late Dashboard → X/Twitter → Disconnect → Reconnect")
        print("   2. Late APIサポートに問い合わせ（投稿ID: {})".format(problem_post_id))
        print("   3. X Analytics Dashboardで手動確認")
        print("      URL: https://analytics.x.com")
    elif all(analytics.get(k, 0) == 0 for k in ['impressions', 'likes', 'shares', 'comments', 'views']):
        print("⚠️  問題検出: すべてのanalytics指標が0")
        print("   → データ同期は実行されているが、X APIから0が返っている")
        print()
        print("推奨アクション:")
        print("   1. 投稿から24時間以上経過しているか確認")
        print("   2. X API Planを確認（Free TierではAnalytics API不可）")
        print("   3. Late APIサポートに問い合わせ")
    else:
        print("✅ Analytics正常")
        print(f"   Impressions: {analytics.get('impressions', 0):,}")
        print(f"   Engagement Rate: {analytics.get('engagementRate', 0):.2f}%")

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTPエラー: {e.response.status_code}")
    print(f"   投稿が存在しないか、アクセス権限がありません")
except Exception as e:
    print(f"❌ エラー: {str(e)}")

# ========================================
# STEP 5: 再同期トリガー（実験的）
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 5: Analytics再同期トリガー（実験的）")
print("-" * 60)
print("⚠️  この機能はLate APIドキュメントに記載されていない実験的機能です")
print("   実行しますか？ (y/n): ", end="")

user_input = input().strip().lower()

if user_input == "y":
    try:
        # POST /analytics/refresh エンドポイント（存在するか不明）
        response = requests.post(
            f"{LATE_BASE_URL}/analytics/refresh",
            headers=headers,
            json={
                "postId": problem_post_id
            },
            timeout=30
        )

        if response.status_code == 200:
            print("✅ 再同期トリガー送信成功")
            print("   60分後に再度確認してください")
        elif response.status_code == 404:
            print("⚠️  このエンドポイントは存在しません")
            print("   Late APIサポートに再同期方法を問い合わせてください")
        else:
            print(f"❌ ステータスコード: {response.status_code}")
            print(f"   レスポンス: {response.text}")

    except Exception as e:
        print(f"❌ エラー: {str(e)}")
        print("   Late APIサポートに問い合わせてください")
else:
    print("スキップしました")

# ========================================
# 最終レポート
# ========================================
print("\n" + "=" * 60)
print("📊 診断完了")
print("=" * 60)
print()
print("次のアクション:")
print("1. Late Dashboard → Settings → Connected Accounts → X/Twitter")
print("   URL: https://app.getlate.dev/settings/accounts")
print("2. API Planを確認（Free Tierの場合、Analytics API不可）")
print("3. Disconnect → Reconnect で再認証")
print("4. Late APIサポートに問い合わせ")
print("   Email: support@getlate.dev")
print("   Subject: X/Twitter Analytics Not Updating")
print("   Post ID: {}".format(problem_post_id))
print()
print("診断ログは以下に保存されています:")

# 診断ログを保存
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = project_root / "data" / f"late_twitter_diagnosis_{timestamp}.json"
log_file.parent.mkdir(parents=True, exist_ok=True)

log_data = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "twitter_account": twitter_account if twitter_account else None,
    "posts_count": len(twitter_posts) if 'twitter_posts' in locals() else 0,
    "analytics_posts_count": len(analytics_posts) if 'analytics_posts' in locals() else 0,
    "problem_post_id": problem_post_id,
    "problem_post_detail": post_detail if 'post_detail' in locals() else None
}

with open(log_file, "w", encoding="utf-8") as f:
    json.dump(log_data, f, indent=2, ensure_ascii=False)

print(f"   {log_file}")
print()
