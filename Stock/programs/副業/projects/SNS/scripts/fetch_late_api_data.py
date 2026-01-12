#!/usr/bin/env python3
"""
Late API Data Fetcher - SNS投稿データ収集スクリプト

Usage:
    python fetch_late_api_data.py --start 2026-01-01 --end 2026-01-10 --platforms x threads linkedin

Description:
    Late APIから複数のソーシャルメディアプラットフォームの投稿データを取得します。
    X (Twitter), Threads, LinkedInをサポートしています。
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
import argparse
from typing import Dict, List, Optional

# .env読み込み
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")


class LateAPIDataFetcher:
    """Late APIからSNS投稿データを取得するクライアント"""

    def __init__(self):
        self.api_key = os.getenv("LATE_API_KEY")
        self.base_url = os.getenv("LATE_BASE_URL", "https://getlate.dev/api/v1")

        if not self.api_key:
            raise ValueError("LATE_API_KEY not found in .env file")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # アカウントID設定
        self.account_ids = {
            "x": os.getenv("LATE_TWITTER_ACCOUNT_ID"),
            "twitter": os.getenv("LATE_TWITTER_ACCOUNT_ID"),
            "threads": os.getenv("LATE_THREADS_ACCOUNT_ID"),
            "linkedin": os.getenv("LATE_LINKEDIN_ACCOUNT_ID"),
        }

    def fetch_posts(
        self,
        platform: str,
        start_date: datetime,
        end_date: datetime,
        limit: int = 100,
    ) -> List[Dict]:
        """
        Late APIから投稿データを取得

        Args:
            platform: プラットフォーム名 (x, threads, linkedin)
            start_date: 開始日時
            end_date: 終了日時
            limit: 取得件数の上限

        Returns:
            list: 投稿データリスト
        """
        account_id = self.account_ids.get(platform.lower())
        if not account_id:
            print(f"⚠️  Account ID not found for platform: {platform}")
            return []

        posts = []

        # 複数のエンドポイント候補を試す
        endpoints = [
            f"{self.base_url}/accounts/{account_id}/posts",
            f"{self.base_url}/posts",
            f"{self.base_url}/posts/list",
            f"{self.base_url}/{platform}/posts",
        ]

        params = {
            "account_id": account_id,
            "start": start_date.isoformat(),
            "end": end_date.isoformat(),
            "limit": limit,
        }

        try:
            print(f"📡 Fetching {platform} data from Late API...")
            print(f"   Account ID: {account_id}")
            print(f"   Period: {start_date} to {end_date}")

            # 最初のエンドポイントから試す
            for url in endpoints:
                try:
                    print(f"   Trying: {url}")
                    response = requests.get(
                        url, headers=self.headers, params=params, timeout=15
                    )

                    # ステータスコードチェック
                    if response.status_code == 200:
                        data = response.json()

                        # レスポンスフォーマットの確認（Late APIの仕様に応じて）
                        if isinstance(data, list):
                            posts = data
                        elif isinstance(data, dict):
                            # ネストされたレスポンスの場合
                            posts = data.get("posts", data.get("data", []))

                        if posts:
                            print(f"✅ Successfully fetched {len(posts)} posts from {platform}")
                            break
                        else:
                            print(f"   No data returned from this endpoint")

                    elif response.status_code == 403:
                        print(
                            f"   ⚠️  Access denied (403): {response.text[:100]}"
                        )
                    elif response.status_code == 404:
                        print(f"   Endpoint not found (404)")
                    else:
                        print(f"   Error ({response.status_code})")

                except requests.exceptions.Timeout:
                    print(f"   Timeout on this endpoint")
                except Exception as e:
                    print(f"   Error: {str(e)[:80]}")

            if not posts:
                print(f"⚠️  No posts retrieved for {platform} from any endpoint")

        except Exception as e:
            print(f"❌ Unexpected error for {platform}: {str(e)}")

        return posts

    def normalize_post_data(
        self, posts: List[Dict], platform: str
    ) -> List[Dict]:
        """
        投稿データを統一フォーマットに正規化

        Args:
            posts: 投稿データリスト
            platform: プラットフォーム名

        Returns:
            list: 正規化されたデータリスト
        """
        normalized = []

        for post in posts:
            try:
                # プラットフォームごとのマッピング（Late APIの実際のレスポンスに応じて調整）
                normalized_post = {
                    "post_id": post.get("id") or post.get("_id") or "",
                    "platform": platform,
                    "published_at": post.get(
                        "published_at"
                    ) or post.get("createdAt") or post.get("date") or "",
                    "text": post.get("content") or post.get("text") or "",
                    "impressions": post.get("impressions", 0),
                    "engagement_rate": post.get("engagement_rate", 0),
                    "likes": post.get("likes")
                    or post.get("like_count")
                    or post.get("favorites", 0),
                    "comments": post.get("comments")
                    or post.get("comment_count")
                    or post.get("replies", 0),
                    "shares": post.get("shares")
                    or post.get("retweets")
                    or post.get("share_count", 0),
                    "media_type": post.get("media_type") or "text",
                    "raw_data": post,  # オリジナルデータも保存
                }
                normalized.append(normalized_post)
            except Exception as e:
                print(f"⚠️  Error normalizing post: {str(e)}")
                continue

        return normalized


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description="Late API from SNS投稿データを取得"
    )
    parser.add_argument(
        "--start",
        type=str,
        default="2026-01-01",
        help="開始日 (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--end",
        type=str,
        default="2026-01-10",
        help="終了日 (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--platforms",
        type=str,
        nargs="+",
        default=["x", "threads", "linkedin"],
        help="対象プラットフォーム (x threads linkedin)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="出力ファイルパス (指定がない場合は自動生成)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="プラットフォームごとの取得件数上限",
    )

    args = parser.parse_args()

    # 日付の解析
    try:
        start_date = datetime.strptime(args.start, "%Y-%m-%d")
        end_date = datetime.strptime(args.end, "%Y-%m-%d")
        # 終了日を23:59:59に設定
        end_date = end_date.replace(hour=23, minute=59, second=59)
    except ValueError as e:
        print(f"❌ Date parsing error: {e}")
        return

    # フェッチャーの初期化
    try:
        fetcher = LateAPIDataFetcher()
    except ValueError as e:
        print(f"❌ Initialization error: {e}")
        return

    # 全プラットフォームからデータを取得
    all_posts = []
    platform_stats = {}

    print("\n" + "=" * 60)
    print("Late API Data Fetcher")
    print("=" * 60)
    print(f"Period: {args.start} to {args.end}")
    print(f"Platforms: {', '.join(args.platforms)}")
    print("=" * 60 + "\n")

    for platform in args.platforms:
        posts = fetcher.fetch_posts(platform, start_date, end_date, args.limit)
        normalized_posts = fetcher.normalize_post_data(posts, platform)

        platform_stats[platform] = {
            "total_posts": len(normalized_posts),
            "impressions": sum(p.get("impressions", 0) for p in normalized_posts),
            "total_engagement": sum(
                p.get("likes", 0) + p.get("comments", 0) + p.get("shares", 0)
                for p in normalized_posts
            ),
        }

        all_posts.extend(normalized_posts)
        print()

    # 出力ファイルパスの決定
    if args.output:
        output_path = Path(args.output)
    else:
        date_str = args.start.replace("-", "") + "-" + args.end.replace("-", "")
        output_filename = f"late_api_data_{date_str}.json"
        output_path = project_root / "data" / output_filename

    # データを保存
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "metadata": {
                        "fetched_at": datetime.now().isoformat(),
                        "period_start": args.start,
                        "period_end": args.end,
                        "platforms": args.platforms,
                        "total_posts": len(all_posts),
                        "platform_stats": platform_stats,
                    },
                    "data": all_posts,
                },
                f,
                ensure_ascii=False,
                indent=2,
            )
        print(f"\n✅ Data saved to: {output_path}")
    except Exception as e:
        print(f"\n❌ Error saving data: {e}")
        return

    # サマリー表示
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total posts collected: {len(all_posts)}")
    print(f"\nPlatform breakdown:")
    for platform, stats in platform_stats.items():
        print(f"  {platform.upper()}: {stats['total_posts']} posts")
        if stats["total_posts"] > 0:
            print(f"    Impressions: {stats['impressions']:,}")
            print(f"    Total engagement: {stats['total_engagement']:,}")

    # サンプルデータ表示
    if all_posts:
        print("\n" + "=" * 60)
        print("SAMPLE DATA (first 3 posts)")
        print("=" * 60)
        for i, post in enumerate(all_posts[:3], 1):
            print(f"\n[{i}] Platform: {post['platform']}")
            print(f"    ID: {post['post_id']}")
            print(f"    Published: {post['published_at']}")
            print(f"    Text: {post['text'][:100]}...")
            print(f"    Likes: {post['likes']}, Comments: {post['comments']}")


if __name__ == "__main__":
    main()
