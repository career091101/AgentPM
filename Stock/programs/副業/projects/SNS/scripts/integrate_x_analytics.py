#!/usr/bin/env python3
"""
X Analytics統合スクリプト（Late API + Bearer Token）

Late APIから投稿一覧を取得し、X API Bearer TokenでPublic Metricsを取得してマージします。

Usage:
    python3 scripts/integrate_x_analytics.py --from-date 2026-01-05 --to-date 2026-01-06
"""

import requests
import json
import argparse
import re
from datetime import datetime
from pathlib import Path
import time

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

LATE_API_KEY = env_vars.get("LATE_API_KEY")
LATE_BASE_URL = env_vars.get("LATE_BASE_URL", "https://getlate.dev/api/v1")
X_BEARER_TOKEN = env_vars.get("X_BEARER_TOKEN")


def extract_tweet_id(platform_url):
    """
    Platform URLからツイートIDを抽出

    例:
    - https://twitter.com/i/web/status/2007770258292043823
    - https://x.com/yuichisatoeco/status/2007770258292043823
    """
    if not platform_url:
        return None

    # パターン1: /status/{tweet_id}
    match = re.search(r'/status/(\d+)', platform_url)
    if match:
        return match.group(1)

    return None


def fetch_late_posts(from_date, to_date):
    """Late APIからX/Twitter投稿を取得"""
    headers = {
        "Authorization": f"Bearer {LATE_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "platform": "twitter",
        "sortBy": "date",
        "order": "desc",
        "limit": 100
    }

    # 日付フィルタは指定された場合のみ追加
    if from_date:
        params["fromDate"] = from_date
    if to_date:
        params["toDate"] = to_date

    try:
        response = requests.get(
            f"{LATE_BASE_URL}/analytics",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("posts", [])
    except Exception as e:
        print(f"❌ Late API投稿取得エラー: {str(e)}")
        return []


def fetch_public_metrics_bearer(tweet_id):
    """
    Bearer TokenでX APIからPublic Metricsを取得

    Returns:
        dict: public_metrics or None
    """
    headers = {
        "Authorization": f"Bearer {X_BEARER_TOKEN}"
    }

    params = {
        "tweet.fields": "created_at,public_metrics"
    }

    try:
        response = requests.get(
            f"https://api.twitter.com/2/tweets/{tweet_id}",
            headers=headers,
            params=params,
            timeout=30
        )

        # レート制限チェック
        if response.status_code == 429:
            print(f"   ⚠️  レート制限（ツイートID: {tweet_id}）")
            return None

        response.raise_for_status()
        data = response.json()

        tweet = data.get("data", {})
        return tweet.get("public_metrics", {})

    except requests.exceptions.HTTPError as e:
        print(f"   ❌ HTTPエラー: {e.response.status_code}（ツイートID: {tweet_id}）")
        return None
    except Exception as e:
        print(f"   ❌ エラー: {str(e)}（ツイートID: {tweet_id}）")
        return None


def calculate_engagement_rate(metrics):
    """
    Engagement Rate計算

    ER = (Likes + Retweets×2 + Replies×3) / Impressions × 100
    """
    impressions = metrics.get("impression_count", 0)
    if impressions == 0:
        return 0.0

    likes = metrics.get("like_count", 0)
    retweets = metrics.get("retweet_count", 0)
    replies = metrics.get("reply_count", 0)

    er = ((likes + retweets * 2 + replies * 3) / impressions) * 100
    return round(er, 2)


def main():
    parser = argparse.ArgumentParser(description="X Analytics統合（Late API + Bearer Token）")
    parser.add_argument("--from-date", required=False, help="開始日（YYYY-MM-DD）")
    parser.add_argument("--to-date", required=False, help="終了日（YYYY-MM-DD）")
    args = parser.parse_args()

    print("=" * 60)
    print("X Analytics統合（Late API + Bearer Token）")
    print("=" * 60)
    print(f"期間: {args.from_date} ~ {args.to_date}")
    print()

    # STEP 1: Late APIから投稿取得
    print("📋 STEP 1: Late APIから投稿取得")
    print("-" * 60)

    late_posts = fetch_late_posts(args.from_date, args.to_date)
    print(f"✅ Late API投稿数: {len(late_posts)}")
    print()

    if not late_posts:
        print("⚠️  投稿が見つかりません")
        return

    # STEP 2: 各投稿からツイートIDを抽出
    print("📋 STEP 2: ツイートID抽出")
    print("-" * 60)

    integrated_posts = []
    success_count = 0
    failed_count = 0

    for i, post in enumerate(late_posts, 1):
        post_id = post.get("_id")
        platform_url = post.get("platformPostUrl")
        content = post.get("content", "")[:60]

        print(f"\n{i}. Post ID: {post_id}")
        print(f"   URL: {platform_url}")
        print(f"   Content: {content}...")

        # ツイートID抽出
        tweet_id = extract_tweet_id(platform_url)
        if not tweet_id:
            print(f"   ⚠️  ツイートIDを抽出できませんでした")
            failed_count += 1

            # Late APIデータをそのまま使用
            integrated_posts.append({
                "late_post_id": post_id,
                "tweet_id": None,
                "text": post.get("content", ""),
                "published_at": post.get("publishedAt"),
                "platform_url": platform_url,
                "analytics": {
                    "source": "Late API（Bearer Token取得失敗）",
                    "impressions": post.get("analytics", {}).get("impressions", 0),
                    "likes": post.get("analytics", {}).get("likes", 0),
                    "shares": post.get("analytics", {}).get("shares", 0),
                    "comments": post.get("analytics", {}).get("comments", 0),
                    "engagement_rate": 0.0
                }
            })
            continue

        print(f"   ✅ ツイートID: {tweet_id}")

        # STEP 3: Bearer TokenでPublic Metrics取得
        print(f"   🔄 Public Metrics取得中...")
        public_metrics = fetch_public_metrics_bearer(tweet_id)

        if not public_metrics:
            failed_count += 1

            # Late APIデータをそのまま使用
            integrated_posts.append({
                "late_post_id": post_id,
                "tweet_id": tweet_id,
                "text": post.get("content", ""),
                "published_at": post.get("publishedAt"),
                "platform_url": platform_url,
                "analytics": {
                    "source": "Late API（Bearer Token取得失敗）",
                    "impressions": post.get("analytics", {}).get("impressions", 0),
                    "likes": post.get("analytics", {}).get("likes", 0),
                    "shares": post.get("analytics", {}).get("shares", 0),
                    "comments": post.get("analytics", {}).get("comments", 0),
                    "engagement_rate": 0.0
                }
            })
            continue

        # 成功: Bearer Tokenデータを使用
        success_count += 1
        impressions = public_metrics.get("impression_count", 0)
        likes = public_metrics.get("like_count", 0)
        retweets = public_metrics.get("retweet_count", 0)
        replies = public_metrics.get("reply_count", 0)
        quotes = public_metrics.get("quote_count", 0)
        bookmarks = public_metrics.get("bookmark_count", 0)

        er = calculate_engagement_rate(public_metrics)

        print(f"   ✅ Impressions: {impressions:,}")
        print(f"   ✅ Likes: {likes:,}")
        print(f"   ✅ Retweets: {retweets:,}")
        print(f"   ✅ ER: {er:.2f}%")

        integrated_posts.append({
            "late_post_id": post_id,
            "tweet_id": tweet_id,
            "text": post.get("content", ""),
            "published_at": post.get("publishedAt"),
            "platform_url": platform_url,
            "analytics": {
                "source": "X API Bearer Token",
                "impressions": impressions,
                "likes": likes,
                "retweets": retweets,
                "replies": replies,
                "quotes": quotes,
                "bookmarks": bookmarks,
                "engagement_rate": er
            }
        })

        # レート制限回避（3秒待機）
        if i < len(late_posts):
            time.sleep(3)

    # STEP 4: 結果サマリー
    print("\n" + "=" * 60)
    print("📊 結果サマリー")
    print("=" * 60)
    print(f"総投稿数: {len(late_posts)}")
    print(f"✅ Bearer Token成功: {success_count}")
    print(f"❌ Bearer Token失敗: {failed_count}")
    print(f"成功率: {(success_count / len(late_posts) * 100):.1f}%")
    print()

    # STEP 5: 統合データ保存
    output_file = project_root / "data" / f"x_analytics_integrated_{datetime.now().strftime('%Y%m%d')}.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    output_data = {
        "generated_at": datetime.now().isoformat(),
        "period": {
            "from": args.from_date,
            "to": args.to_date
        },
        "summary": {
            "total_posts": len(late_posts),
            "bearer_token_success": success_count,
            "bearer_token_failed": failed_count,
            "success_rate": round((success_count / len(late_posts) * 100), 1)
        },
        "posts": integrated_posts
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"💾 出力: {output_file}")
    print(f"   サイズ: {output_file.stat().st_size:,} bytes")
    print()

    # STEP 6: トップ投稿表示
    if success_count > 0:
        print("🏆 Top 3 高エンゲージメント投稿:")
        print("-" * 60)

        # Impressions降順でソート
        sorted_posts = sorted(
            [p for p in integrated_posts if p["analytics"]["source"] == "X API Bearer Token"],
            key=lambda x: x["analytics"]["impressions"],
            reverse=True
        )

        for i, post in enumerate(sorted_posts[:3], 1):
            print(f"\n{i}. {post['text'][:60]}...")
            print(f"   Impressions: {post['analytics']['impressions']:,}")
            print(f"   Likes: {post['analytics']['likes']:,}")
            print(f"   ER: {post['analytics']['engagement_rate']:.2f}%")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
