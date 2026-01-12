#!/usr/bin/env python3
"""
Late API Analytics 正しいデータ取得スクリプト

Analytics Addon契約済みの環境で/v1/analyticsエンドポイントを使用して
実際のインプレッション数、エンゲージメント率などを取得します。

Usage:
    python3 fetch_late_analytics_corrected.py --from-date 2026-01-01 --to-date 2026-01-10
"""

import requests
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def load_config(config_path: Optional[str] = None) -> Dict:
    """Late API設定をロード"""
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config/late_api_config.json"

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_headers(api_key: str) -> Dict:
    """APIリクエストヘッダー"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


def get_published_posts(
    base_url: str,
    api_key: str,
    from_date: str,
    to_date: str,
    platform: Optional[str] = None
) -> List[Dict]:
    """
    公開済み投稿を取得

    Args:
        base_url: Late API Base URL
        api_key: API Key
        from_date: 開始日 (YYYY-MM-DD)
        to_date: 終了日 (YYYY-MM-DD)
        platform: プラットフォーム名 (x, threads, linkedin, facebook)

    Returns:
        公開済み投稿のリスト
    """
    params = {
        "status": "published",  # 重要: 公開済みのみ
        "limit": 100
    }

    if from_date:
        params["fromDate"] = from_date
    if to_date:
        params["toDate"] = to_date
    if platform:
        params["platform"] = platform

    response = requests.get(
        f"{base_url}/posts",
        headers=get_headers(api_key),
        params=params,
        timeout=30
    )

    if response.status_code != 200:
        print(f"❌ エラー: /posts endpoint - {response.status_code}")
        print(f"Response: {response.text}")
        return []

    data = response.json()
    posts = data.get("posts", [])

    print(f"✅ 公開済み投稿取得: {len(posts)}件")
    return posts


def get_analytics_for_post(
    base_url: str,
    api_key: str,
    post_id: str
) -> Optional[Dict]:
    """
    特定投稿のアナリティクスを取得

    Args:
        base_url: Late API Base URL
        api_key: API Key
        post_id: 投稿ID

    Returns:
        アナリティクスデータ（取得失敗時はNone）
    """
    response = requests.get(
        f"{base_url}/analytics",
        headers=get_headers(api_key),
        params={"postId": post_id},
        timeout=30
    )

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 202:
        # 202 Accepted: データ処理中（まだアナリティクスが利用できない）
        print(f"⏳  Post {post_id[:12]}... - アナリティクスデータ処理中 (202)")
        return None
    elif response.status_code == 402:
        print(f"❌ エラー: Analytics Addonが契約されていません")
        print(f"   Late Dashboard (https://app.getlate.dev/settings/billing) で確認してください")
        return None
    else:
        print(f"⚠️  警告: Post {post_id[:12]}... のアナリティクス取得失敗 - {response.status_code}")
        return None


def fetch_all_analytics(
    from_date: str,
    to_date: str,
    platform: Optional[str] = None,
    config_path: Optional[str] = None
) -> Dict:
    """
    全投稿のアナリティクスを取得

    Args:
        from_date: 開始日 (YYYY-MM-DD)
        to_date: 終了日 (YYYY-MM-DD)
        platform: プラットフォーム名 (x, threads, linkedin, facebook)
        config_path: 設定ファイルパス

    Returns:
        アナリティクスデータ（メタデータ含む）
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    print(f"\n🚀 Late API Analytics データ取得開始")
    print(f"   期間: {from_date} ～ {to_date}")
    if platform:
        print(f"   プラットフォーム: {platform}")
    print()

    # STEP 1: 公開済み投稿を取得
    posts = get_published_posts(base_url, api_key, from_date, to_date, platform)

    if not posts:
        print("⚠️  公開済み投稿が0件です")
        print("   - 期間内に投稿が公開されていない可能性があります")
        print("   - または全ての投稿が 'scheduled' ステータスのままです")
        return {
            "metadata": {
                "fetched_at": datetime.now().isoformat(),
                "period_start": from_date,
                "period_end": to_date,
                "total_posts": 0,
                "platform_stats": {}
            },
            "data": []
        }

    # STEP 2: 各投稿のアナリティクスを取得
    analytics_data = []
    failed_count = 0

    for i, post in enumerate(posts, 1):
        post_id = post.get("_id")
        post_platform = post.get("platform")

        print(f"   [{i}/{len(posts)}] Post ID: {post_id[:12]}... ({post_platform})")

        analytics = get_analytics_for_post(base_url, api_key, post_id)

        if analytics:
            # analytics データの構造: {"postId": "...", "analytics": {...}, "platformAnalytics": [...]}
            analytics_obj = analytics.get("analytics", {})
            platform_analytics = analytics.get("platformAnalytics", [])

            # platform情報を取得
            detected_platform = post_platform
            if not detected_platform and platform_analytics:
                detected_platform = platform_analytics[0].get("platform")

            analytics_data.append({
                "post_id": post_id,
                "platform": detected_platform,
                "published_at": analytics.get("publishedAt"),
                "text": analytics.get("content", "")[:100],  # 最初100文字のみ
                "impressions": analytics_obj.get("impressions", 0),
                "engagement_rate": (
                    platform_analytics[0].get("analytics", {}).get("engagementRate", 0)
                    if platform_analytics else 0
                ),
                "likes": analytics_obj.get("likes", 0),
                "comments": analytics_obj.get("comments", 0),
                "shares": analytics_obj.get("shares", 0),
                "reach": analytics_obj.get("reach", 0),
                "clicks": analytics_obj.get("clicks", 0),
                "views": analytics_obj.get("views", 0),
                "raw_analytics": analytics  # 全データを保存
            })
        else:
            failed_count += 1

    # STEP 3: プラットフォーム別統計
    platform_stats = {}
    for item in analytics_data:
        p = item["platform"]
        if p not in platform_stats:
            platform_stats[p] = {
                "total_posts": 0,
                "impressions": 0,
                "total_engagement": 0
            }
        platform_stats[p]["total_posts"] += 1
        platform_stats[p]["impressions"] += item.get("impressions", 0)
        platform_stats[p]["total_engagement"] += (
            item.get("likes", 0) +
            item.get("comments", 0) +
            item.get("shares", 0)
        )

    # STEP 4: 結果サマリー
    result = {
        "metadata": {
            "fetched_at": datetime.now().isoformat(),
            "period_start": from_date,
            "period_end": to_date,
            "total_posts": len(analytics_data),
            "total_impressions": sum(item.get("impressions", 0) for item in analytics_data),
            "total_engagement": sum(
                item.get("likes", 0) + item.get("comments", 0) + item.get("shares", 0)
                for item in analytics_data
            ),
            "failed_count": failed_count,
            "platform_stats": platform_stats
        },
        "data": analytics_data
    }

    return result


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description="Late API Analytics データ取得（Analytics Addon契約済み環境）"
    )
    parser.add_argument(
        "--from-date",
        type=str,
        required=True,
        help="開始日 (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--to-date",
        type=str,
        required=True,
        help="終了日 (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--platform",
        type=str,
        choices=["x", "threads", "linkedin", "facebook"],
        help="プラットフォーム指定（省略時は全プラットフォーム）"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="出力ファイルパス（省略時は自動生成）"
    )

    args = parser.parse_args()

    # データ取得
    result = fetch_all_analytics(
        from_date=args.from_date,
        to_date=args.to_date,
        platform=args.platform
    )

    # 出力ファイルパス決定
    if args.output:
        output_path = Path(args.output)
    else:
        from_date_str = args.from_date.replace("-", "")
        to_date_str = args.to_date.replace("-", "")
        filename = f"late_api_analytics_{from_date_str}-{to_date_str}.json"
        output_path = Path(__file__).parent.parent / "data" / filename

    # データ保存
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # サマリー表示
    print("\n" + "="*80)
    print("📊 データ取得完了")
    print("="*80)
    print(f"保存先: {output_path}")
    print(f"期間: {args.from_date} ～ {args.to_date}")
    print(f"\n総投稿数: {result['metadata']['total_posts']}件")
    print(f"総インプレッション数: {result['metadata']['total_impressions']:,}")
    print(f"総エンゲージメント数: {result['metadata']['total_engagement']:,}")

    if result['metadata']['failed_count'] > 0:
        print(f"\n⚠️  取得失敗: {result['metadata']['failed_count']}件")

    print("\nプラットフォーム別統計:")
    for platform, stats in result['metadata']['platform_stats'].items():
        platform_name = platform if platform else "不明"
        print(f"  {platform_name:10s}: {stats['total_posts']:3d}件 | "
              f"Impressions: {stats['impressions']:,} | "
              f"Engagement: {stats['total_engagement']:,}")

    print("\n✅ 完了")


if __name__ == "__main__":
    main()
