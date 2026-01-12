#!/usr/bin/env python3
"""
Late API Analytics取得スクリプト

Usage:
    python3 scripts/fetch_late_analytics.py --from-date 2026-01-04 --to-date 2026-01-05
    python3 scripts/fetch_late_analytics.py --post-id 695a540ef497177b163fd7be
"""

import requests
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse

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

def fetch_analytics(from_date=None, to_date=None, post_id=None, platform="linkedin"):
    """
    Late API /v1/analytics からエンゲージメントデータを取得

    Args:
        from_date (str): 開始日 (YYYY-MM-DD)
        to_date (str): 終了日 (YYYY-MM-DD)
        post_id (str): 特定投稿ID
        platform (str): プラットフォーム（デフォルト: linkedin）

    Returns:
        dict: Analyticsデータ
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {}

    if post_id:
        # 単一投稿のAnalytics取得
        params["postId"] = post_id
    else:
        # 日付範囲でフィルタ
        if from_date:
            params["fromDate"] = from_date
        if to_date:
            params["toDate"] = to_date

        params["platform"] = platform
        params["sortBy"] = "date"
        params["order"] = "desc"
        params["limit"] = 100

    try:
        response = requests.get(
            f"{LATE_BASE_URL}/analytics",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()

        analytics_data = response.json()

        # レスポンスヘッダからレート制限情報を取得
        rate_limit_info = {
            "limit": response.headers.get("X-RateLimit-Limit"),
            "remaining": response.headers.get("X-RateLimit-Remaining"),
            "reset": response.headers.get("X-RateLimit-Reset")
        }

        return {
            "success": True,
            "data": analytics_data,
            "rate_limit": rate_limit_info
        }

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 402:
            return {
                "success": False,
                "error": "Analytics Addon not enabled. Please add $10/month Analytics Addon in Late Dashboard.",
                "error_code": 402
            }
        elif e.response.status_code == 429:
            return {
                "success": False,
                "error": "Rate limit exceeded (150 requests/hour). Please wait.",
                "error_code": 429,
                "reset": e.response.headers.get("X-RateLimit-Reset")
            }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {e.response.status_code} - {e.response.text}",
                "error_code": e.response.status_code
            }

    except Exception as e:
        return {
            "success": False,
            "error": f"Request failed: {str(e)}"
        }

def calculate_engagement_rate(analytics):
    """
    エンゲージメント率を計算（Late APIが提供しない場合）

    ER = (Likes + Comments×2 + Shares×3) / Impressions × 100
    """
    impressions = analytics.get("impressions", 0)
    if impressions == 0:
        return 0.0

    likes = analytics.get("likes", 0)
    comments = analytics.get("comments", 0)
    shares = analytics.get("shares", 0)

    engagement = likes + (comments * 2) + (shares * 3)
    er = (engagement / impressions) * 100

    return round(er, 2)

def main():
    parser = argparse.ArgumentParser(description="Late API Analytics取得")
    parser.add_argument("--from-date", help="開始日 (YYYY-MM-DD)")
    parser.add_argument("--to-date", help="終了日 (YYYY-MM-DD)")
    parser.add_argument("--post-id", help="特定投稿ID")
    parser.add_argument("--platform", default="linkedin", help="プラットフォーム（デフォルト: linkedin）")
    parser.add_argument("--output", help="出力ファイルパス（デフォルト: data/late_analytics_{date}.json）")

    args = parser.parse_args()

    # デフォルト値設定
    if not args.from_date and not args.post_id:
        # デフォルト: 過去7日間
        jst = timezone(timedelta(hours=9))
        today = datetime.now(jst).date()
        args.from_date = str(today - timedelta(days=7))
        args.to_date = str(today)

    print("=" * 60)
    print("Late API Analytics取得")
    print("=" * 60)

    if args.post_id:
        print(f"Post ID: {args.post_id}")
    else:
        print(f"期間: {args.from_date} ~ {args.to_date}")
        print(f"プラットフォーム: {args.platform}")
    print()

    # Analytics取得
    result = fetch_analytics(
        from_date=args.from_date,
        to_date=args.to_date,
        post_id=args.post_id,
        platform=args.platform
    )

    if not result["success"]:
        print(f"❌ エラー: {result['error']}")
        if result.get("error_code") == 402:
            print("\n💡 解決方法:")
            print("   1. Late Dashboard (https://app.getlate.dev) にログイン")
            print("   2. Settings → Billing へ移動")
            print("   3. Analytics Addon ($10/月) を追加購入")
        return

    # 結果表示
    data = result["data"]

    if args.post_id:
        # 単一投稿
        print(f"✅ 投稿Analytics取得成功")
        print(f"\n📊 エンゲージメントデータ:")
        analytics = data.get("analytics", {})
        print(f"   Impressions: {analytics.get('impressions', 0):,}")
        print(f"   Reach: {analytics.get('reach', 0):,}")
        print(f"   Likes: {analytics.get('likes', 0):,}")
        print(f"   Comments: {analytics.get('comments', 0):,}")
        print(f"   Shares: {analytics.get('shares', 0):,}")
        print(f"   Clicks: {analytics.get('clicks', 0):,}")
        print(f"   Views: {analytics.get('views', 0):,}")

        # エンゲージメント率計算
        if "engagementRate" in analytics:
            print(f"   ER: {analytics['engagementRate']}%")
        else:
            er = calculate_engagement_rate(analytics)
            print(f"   ER (計算): {er}%")

        print(f"\n⏱️  最終更新: {analytics.get('lastUpdated', 'N/A')}")
    else:
        # 複数投稿
        posts = data.get("posts", [])
        print(f"✅ Analytics取得成功: {len(posts)}件")

        if posts:
            print(f"\n📊 投稿一覧:")
            for i, post in enumerate(posts, 1):
                analytics = post.get("analytics", {})
                print(f"\n{i}. {post.get('content', '')[:50]}...")
                print(f"   Published: {post.get('publishedAt', 'N/A')}")
                print(f"   Impressions: {analytics.get('impressions', 0):,}")
                print(f"   Likes: {analytics.get('likes', 0):,}")
                print(f"   Comments: {analytics.get('comments', 0):,}")
                print(f"   Shares: {analytics.get('shares', 0):,}")

                # エンゲージメント率
                if "engagementRate" in analytics:
                    print(f"   ER: {analytics['engagementRate']}%")
                else:
                    er = calculate_engagement_rate(analytics)
                    print(f"   ER (計算): {er}%")

    # レート制限情報
    rate_limit = result["rate_limit"]
    print(f"\n🔄 レート制限:")
    print(f"   上限: {rate_limit['limit']}/時間")
    print(f"   残り: {rate_limit['remaining']}/時間")
    print(f"   リセット: {rate_limit['reset']}")

    # ファイル保存
    if args.output:
        output_path = Path(args.output)
    else:
        jst = timezone(timedelta(hours=9))
        today = datetime.now(jst).strftime("%Y%m%d")
        output_path = project_root / "data" / f"late_analytics_{today}.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n💾 出力: {output_path}")
    print(f"   サイズ: {output_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    main()
