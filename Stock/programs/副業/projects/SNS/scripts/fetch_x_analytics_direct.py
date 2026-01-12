#!/usr/bin/env python3
"""
X Analytics直接取得スクリプト（OAuth 1.0a使用）

tweepyを使用してX API v2から直接analyticsデータを取得します。
Late APIをバイパスして、X API Free/Basic Tierを判定します。

Usage:
    python3 scripts/fetch_x_analytics_direct.py
"""

import tweepy
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
                # 引用符を除去
                value = value.strip().strip('"').strip("'")
                env_vars[key.strip()] = value

# X API認証情報
X_API_KEY = env_vars.get("X_API_KEY")
X_API_SECRET = env_vars.get("X_API_SECRET")
X_ACCESS_TOKEN = env_vars.get("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = env_vars.get("X_ACCESS_TOKEN_SECRET")

print("=" * 60)
print("X Analytics直接取得（OAuth 1.0a）")
print("=" * 60)
print()

# OAuth 1.0a認証
try:
    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )

    print("✅ OAuth 1.0a認証成功")
    print()

except Exception as e:
    print(f"❌ 認証失敗: {str(e)}")
    exit(1)

# ========================================
# STEP 1: 自分のユーザー情報取得
# ========================================
print("📋 STEP 1: 自分のユーザー情報取得")
print("-" * 60)

try:
    me = client.get_me(user_fields=["public_metrics", "created_at"])
    user = me.data

    print("✅ ユーザー情報取得成功")
    print(f"   User ID: {user.id}")
    print(f"   Username: @{user.username}")
    print(f"   Name: {user.name}")
    print(f"   Followers: {user.public_metrics['followers_count']:,}")
    print(f"   Following: {user.public_metrics['following_count']:,}")
    print()

    USER_ID = user.id

except tweepy.TweepyException as e:
    print(f"❌ Tweepyエラー: {str(e)}")
    exit(1)
except Exception as e:
    print(f"❌ エラー: {str(e)}")
    exit(1)

# ========================================
# STEP 2: 自分のツイート取得
# ========================================
print("📋 STEP 2: 自分のツイート取得（最新10件）")
print("-" * 60)

try:
    tweets = client.get_users_tweets(
        id=USER_ID,
        max_results=10,
        tweet_fields=["created_at", "public_metrics"],
        exclude=["retweets", "replies"]
    )

    if tweets.data:
        print(f"✅ ツイート取得成功: {len(tweets.data)}件")
        print()

        print("📝 ツイート一覧（Analytics付き）:")
        for i, tweet in enumerate(tweets.data, 1):
            print(f"\n   {i}. Tweet ID: {tweet.id}")
            print(f"      Text: {tweet.text[:60]}...")
            print(f"      Created: {tweet.created_at}")

            # Public Metrics（Free Tierでもアクセス可能）
            metrics = tweet.public_metrics
            print(f"      Public Metrics:")
            print(f"         Impressions: {metrics.get('impression_count', 'N/A')}")
            print(f"         Likes: {metrics.get('like_count', 0)}")
            print(f"         Retweets: {metrics.get('retweet_count', 0)}")
            print(f"         Replies: {metrics.get('reply_count', 0)}")
            print(f"         Quote Tweets: {metrics.get('quote_count', 0)}")

        LATEST_TWEET_ID = tweets.data[0].id
    else:
        print("⚠️  ツイートが見つかりません")
        LATEST_TWEET_ID = None

except tweepy.TweepyException as e:
    print(f"❌ Tweepyエラー: {str(e)}")
    LATEST_TWEET_ID = None
except Exception as e:
    print(f"❌ エラー: {str(e)}")
    LATEST_TWEET_ID = None

# ========================================
# STEP 3: 特定ツイートの詳細Analytics取得
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 3: 詳細Analytics取得（Basic Tier判定）")
print("=" * 60)

if LATEST_TWEET_ID is None:
    print("⚠️  ツイートIDが取得できなかったためスキップ")
else:
    try:
        # non_public_metrics, organic_metricsを要求
        tweet_detail = client.get_tweet(
            id=LATEST_TWEET_ID,
            tweet_fields=["created_at", "public_metrics", "non_public_metrics", "organic_metrics", "promoted_metrics"]
        )

        tweet = tweet_detail.data
        print(f"✅ ツイート詳細取得成功")
        print(f"   Tweet ID: {tweet.id}")
        print()

        # Public Metrics
        print("Public Metrics（Free Tierでアクセス可能）:")
        public_metrics = tweet.public_metrics
        print(f"   Impressions: {public_metrics.get('impression_count', 'N/A')}")
        print(f"   Likes: {public_metrics.get('like_count', 0)}")
        print(f"   Retweets: {public_metrics.get('retweet_count', 0)}")
        print(f"   Replies: {public_metrics.get('reply_count', 0)}")
        print()

        # Non-Public Metrics（Basic Tier以上が必要）
        if hasattr(tweet, 'non_public_metrics') and tweet.non_public_metrics:
            print("✅ Non-Public Metrics取得成功（Basic Tier以上確定）:")
            non_public = tweet.non_public_metrics
            print(f"   URL Link Clicks: {non_public.get('url_link_clicks', 0)}")
            print(f"   User Profile Clicks: {non_public.get('user_profile_clicks', 0)}")
            print()
            API_TIER = "Basic Tier以上"
            HAS_ANALYTICS = True
        else:
            print("❌ Non-Public Metricsアクセス不可（Free Tier確定）")
            print()
            API_TIER = "Free Tier"
            HAS_ANALYTICS = False

        # Organic Metrics（Basic Tier以上が必要）
        if hasattr(tweet, 'organic_metrics') and tweet.organic_metrics:
            print("✅ Organic Metrics取得成功（Basic Tier以上確定）:")
            organic = tweet.organic_metrics
            print(f"   Impressions: {organic.get('impression_count', 0)}")
            print(f"   Likes: {organic.get('like_count', 0)}")
            print(f"   Retweets: {organic.get('retweet_count', 0)}")
            print()
            HAS_ANALYTICS = True
        else:
            print("❌ Organic Metricsアクセス不可（Free Tier確定）")
            print()

    except tweepy.Forbidden as e:
        print("❌ 403 Forbidden: Analytics APIアクセス不可")
        print("   → Free Tier確定")
        print()
        API_TIER = "Free Tier"
        HAS_ANALYTICS = False
    except tweepy.TweepyException as e:
        print(f"❌ Tweepyエラー: {str(e)}")
        API_TIER = "不明"
        HAS_ANALYTICS = False
    except Exception as e:
        print(f"❌ エラー: {str(e)}")
        API_TIER = "不明"
        HAS_ANALYTICS = False

# ========================================
# STEP 4: Late API対象投稿の確認
# ========================================
print("\n" + "=" * 60)
print("📋 STEP 4: Late API対象投稿の確認")
print("=" * 60)

# Late APIで問題のあった投稿のURL
# https://twitter.com/i/web/status/2007770258292043823
TARGET_TWEET_ID = "2007770258292043823"

print(f"Late APIで問題のあった投稿ID: {TARGET_TWEET_ID}")
print(f"URL: https://twitter.com/i/web/status/{TARGET_TWEET_ID}")
print()

try:
    target_tweet = client.get_tweet(
        id=TARGET_TWEET_ID,
        tweet_fields=["created_at", "public_metrics", "non_public_metrics", "organic_metrics"]
    )

    if target_tweet.data:
        tweet = target_tweet.data
        print("✅ 対象ツイート取得成功")
        print(f"   Text: {tweet.text[:80]}...")
        print(f"   Created: {tweet.created_at}")
        print()

        # Public Metrics
        print("Public Metrics:")
        metrics = tweet.public_metrics
        impressions = metrics.get('impression_count', 0)
        likes = metrics.get('like_count', 0)
        retweets = metrics.get('retweet_count', 0)
        replies = metrics.get('reply_count', 0)

        print(f"   Impressions: {impressions:,}")
        print(f"   Likes: {likes:,}")
        print(f"   Retweets: {retweets:,}")
        print(f"   Replies: {replies:,}")
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
        result = {
            "tweet_id": TARGET_TWEET_ID,
            "url": f"https://twitter.com/i/web/status/{TARGET_TWEET_ID}",
            "text": tweet.text,
            "created_at": str(tweet.created_at),
            "public_metrics": {
                "impressions": impressions,
                "likes": likes,
                "retweets": retweets,
                "replies": replies,
                "quotes": metrics.get('quote_count', 0)
            },
            "engagement_rate": round(er, 2),
            "api_tier": API_TIER,
            "fetched_at": datetime.now().isoformat()
        }

        # JSON保存
        output_file = project_root / "data" / f"x_analytics_direct_{datetime.now().strftime('%Y%m%d')}.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"✅ 結果を保存: {output_file}")
        print()

    else:
        print("❌ 対象ツイートが見つかりません")
        print("   このツイートは削除されたか、アクセス権限がありません")
        print()

except tweepy.TweepyException as e:
    print(f"❌ Tweepyエラー: {str(e)}")
except Exception as e:
    print(f"❌ エラー: {str(e)}")

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
    print("❌ Free TierではAnalytics API（non_public_metrics, organic_metrics）にアクセスできません")
    print()
    print("しかし、Public Metrics（Impressions, Likes, Retweets, Replies）は取得できます！")
    print()
    print("Late APIの問題:")
    print("   Late APIはX API v2のnon_public_metricsに依存している可能性があります。")
    print("   Free Tierではこれにアクセスできないため、Late APIが0を返しています。")
    print()
    print("解決策:")
    print("   Option A: X API Basic Tier購入（$100/month）→ Late API再認証")
    print("   Option B: このスクリプトを定期実行してPublic Metricsを取得")
    print("   Option C: X Analytics Dashboardで手動確認（無料）")
    print()
elif API_TIER == "Basic Tier以上":
    print("✅ Basic Tier以上でAnalytics APIアクセス可能")
    print()
    print("Late APIでデータ取得できない場合:")
    print("   1. Late Dashboard → X/Twitter → Disconnect → Reconnect")
    print("   2. Late APIサポートに問い合わせ（X API Basicプラン契約済みを伝える）")
    print()
else:
    print("⚠️  API Tierが判定できませんでした")
    print()

print("=" * 60)
