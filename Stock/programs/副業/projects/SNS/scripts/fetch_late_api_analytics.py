#!/usr/bin/env python3
"""
Late API Analytics データ収集スクリプト

Analytics APIを使用して2026年1月1日～10日の実際のインプレッション数とエンゲージメント率を取得
"""

import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# .env読み込み
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")


class LateAPIAnalyticsClient:
    """Late API Analytics クライアント"""

    def __init__(self):
        self.api_key = os.getenv("LATE_API_KEY")
        if not self.api_key:
            raise ValueError("LATE_API_KEY not found in .env file")

        self.base_url = "https://getlate.dev/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_posts_list(self, platform: str = None) -> list:
        """
        投稿一覧を取得（/posts エンドポイント）

        Args:
            platform: プラットフォーム指定（x, threads, linkedin）

        Returns:
            list: 投稿データリスト
        """
        endpoint = f"{self.base_url}/posts"

        params = {"limit": 100, "sortBy": "date", "order": "desc"}

        if platform:
            params["platform"] = platform

        print(f"📋 投稿一覧取得: {endpoint}")
        print(f"   パラメータ: {params}")

        response = requests.get(endpoint, headers=self.headers, params=params)

        if response.status_code != 200:
            error_msg = (
                f"Late API Error: {response.status_code} - {response.text}"
            )
            raise Exception(error_msg)

        data = response.json()
        posts = data.get("posts", []) if isinstance(data, dict) else data

        print(f"✅ {len(posts)}件の投稿を取得")
        return posts

    def get_analytics(self, from_date: str, to_date: str, platform: str) -> dict:
        """
        Analytics APIからエンゲージメントデータを取得

        Args:
            from_date: 開始日 (YYYY-MM-DD)
            to_date: 終了日 (YYYY-MM-DD)
            platform: プラットフォーム

        Returns:
            dict: Analyticsデータ
        """
        endpoint = f"{self.base_url}/analytics"

        params = {
            "fromDate": from_date,
            "toDate": to_date,
            "platform": platform,
            "sortBy": "date",
            "order": "desc",
            "limit": 100,
        }

        print(f"📊 Analytics API呼び出し: {endpoint}")
        print(f"   パラメータ: {params}")

        response = requests.get(endpoint, headers=self.headers, params=params)

        if response.status_code == 402:
            print("⚠️  Analytics Addonが有効化されていません（$10/月）")
            print(
                "   Late Dashboard (https://app.getlate.dev/settings/billing) で有効化してください"
            )
            return {}

        if response.status_code != 200:
            error_msg = (
                f"Analytics API Error: {response.status_code} - {response.text}"
            )
            raise Exception(error_msg)

        data = response.json()
        print(f"✅ Analyticsデータ取得成功")

        return data

    def fetch_all_platforms(self, start_date: str, end_date: str) -> dict:
        """
        全プラットフォームのデータを取得

        Args:
            start_date: 開始日
            end_date: 終了日

        Returns:
            dict: プラットフォーム別データ
        """
        platforms = ["x", "threads", "linkedin"]
        all_data = []
        platform_stats = {}

        for platform in platforms:
            print(f"\n🔍 {platform.upper()} のデータ取得中...")

            try:
                # Step 1: 投稿一覧取得
                posts = self.get_posts_list(platform=platform)

                # 期間内の投稿をフィルタ
                start_dt = datetime.fromisoformat(start_date + "T00:00:00Z")
                end_dt = datetime.fromisoformat(end_date + "T23:59:59Z")

                filtered_posts = []
                for post in posts:
                    published_at_str = post.get("publishedAt") or post.get(
                        "published_at"
                    )
                    if published_at_str:
                        published_at = datetime.fromisoformat(
                            published_at_str.replace("Z", "+00:00")
                        )
                        if start_dt <= published_at <= end_dt:
                            filtered_posts.append(post)

                print(
                    f"   📅 期間内の投稿: {len(filtered_posts)}件（全{len(posts)}件中）"
                )

                # Step 2: Analytics データ取得
                analytics_data = self.get_analytics(
                    start_date, end_date, platform
                )

                # Analyticsデータを投稿IDでマッピング
                analytics_map = {}
                if "analytics" in analytics_data:
                    for item in analytics_data.get("analytics", []):
                        post_id = item.get("postId") or item.get("post_id")
                        if post_id:
                            analytics_map[post_id] = item

                # Step 3: 投稿データとAnalyticsデータを結合
                total_impressions = 0
                total_engagement = 0

                for post in filtered_posts:
                    post_id = post.get("_id") or post.get("id")

                    # Analyticsデータを結合
                    if post_id in analytics_map:
                        post["analytics"] = analytics_map[post_id]

                    # 標準化データ作成
                    normalized = self._normalize_post_data(post, platform)
                    all_data.append(normalized)

                    total_impressions += normalized["impressions"]
                    total_engagement += (
                        normalized["likes"]
                        + normalized["comments"]
                        + normalized["shares"]
                    )

                platform_stats[platform] = {
                    "total_posts": len(filtered_posts),
                    "impressions": total_impressions,
                    "total_engagement": total_engagement,
                }

                print(
                    f"   ✅ {len(filtered_posts)}件取得 | インプレッション: {total_impressions:,}"
                )

            except Exception as e:
                print(f"   ❌ エラー: {e}")
                platform_stats[platform] = {
                    "total_posts": 0,
                    "impressions": 0,
                    "total_engagement": 0,
                    "error": str(e),
                }

        return {
            "metadata": {
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "period_start": start_date,
                "period_end": end_date,
                "platforms": platforms,
                "total_posts": len(all_data),
                "platform_stats": platform_stats,
            },
            "data": all_data,
        }

    def _normalize_post_data(self, post: dict, platform: str) -> dict:
        """
        投稿データを標準化

        Args:
            post: Late APIレスポンス
            platform: プラットフォーム名

        Returns:
            dict: 標準化された投稿データ
        """
        # Late APIのフィールドマッピング
        post_id = post.get("_id") or post.get("id")
        published_at = post.get("publishedAt") or post.get("published_at")
        text = post.get("post") or post.get("text") or post.get("content", "")

        # Analytics データ（analytics オブジェクトまたはトップレベル）
        analytics = post.get("analytics", {})

        impressions = (
            analytics.get("impressions")
            or post.get("impressions")
            or post.get("views")
            or 0
        )

        likes = (
            analytics.get("likes")
            or post.get("likes")
            or post.get("reactions")
            or 0
        )

        comments = (
            analytics.get("comments")
            or post.get("comments")
            or post.get("replies")
            or 0
        )

        shares = (
            analytics.get("shares")
            or post.get("shares")
            or post.get("reposts")
            or 0
        )

        # エンゲージメント率計算
        total_engagement = likes + comments + shares
        engagement_rate = (
            (total_engagement / impressions * 100) if impressions > 0 else 0
        )

        # メディアタイプ判定
        media = post.get("media", [])
        media_type = "image" if media else "text"

        return {
            "post_id": post_id,
            "platform": platform,
            "published_at": published_at,
            "text": text[:200] + "..." if len(text) > 200 else text,
            "impressions": impressions,
            "engagement_rate": round(engagement_rate, 2),
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "media_type": media_type,
            "raw_data": post,  # デバッグ用に元データも保存
        }


def main():
    """メイン実行関数"""
    # パラメータ
    start_date = "2026-01-01"
    end_date = "2026-01-10"

    print("=" * 60)
    print("Late API Analytics データ収集")
    print("=" * 60)
    print(f"期間: {start_date} ～ {end_date}")
    print(f"プラットフォーム: X, Threads, LinkedIn")
    print()

    try:
        # クライアント初期化
        client = LateAPIAnalyticsClient()

        # データ取得
        result = client.fetch_all_platforms(start_date, end_date)

        # 出力ファイル
        output_dir = project_root / "data"
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / "late_api_analytics_20260101-0110.json"

        # JSON保存
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print("\n" + "=" * 60)
        print("📊 データ収集完了")
        print("=" * 60)
        print(f"総投稿数: {result['metadata']['total_posts']}")
        print(
            f"総インプレッション: {sum(p['impressions'] for p in result['data']):,}"
        )
        print(f"保存先: {output_file}")
        print()

        # プラットフォーム別サマリー
        print("プラットフォーム別統計:")
        for platform, stats in result["metadata"]["platform_stats"].items():
            print(
                f"  {platform.upper()}: {stats['total_posts']}件 | インプレッション: {stats['impressions']:,}"
            )

        # データ検証
        zero_impressions = [
            p for p in result["data"] if p["impressions"] == 0
        ]
        if zero_impressions:
            print(
                f"\n⚠️  警告: {len(zero_impressions)}件の投稿のインプレッション数が0です"
            )
            print("   → Late APIがAnalyticsデータを返していない可能性があります")
        else:
            print("\n✅ 全投稿で有効なインプレッション数を取得しました")

    except Exception as e:
        print(f"\n❌ エラー発生: {e}")
        import traceback

        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()
