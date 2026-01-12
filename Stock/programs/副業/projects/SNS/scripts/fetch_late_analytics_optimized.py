#!/usr/bin/env python3
"""
Late API Analytics 最適化版データ取得スクリプト

Issue Report (2026-01-10) で特定された課題を修正:
- Critical Issue #1: パラメータ名修正 (dateFrom/dateTo)
- High Issue #2: N+1クエリ問題解決 (/v1/analytics直接使用)
- High Issue #3: ページネーション実装
- High Issue #4: Dual ID System対応

Usage:
    python3 fetch_late_analytics_optimized.py --from-date 2026-01-01 --to-date 2026-01-10
"""

import requests
import json
import argparse
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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


def check_analytics_addon(base_url: str, api_key: str) -> bool:
    """
    Analytics Addon契約確認
    
    Issue #10 対応: 事前に402エラーを検出
    """
    try:
        response = requests.get(
            f"{base_url}/analytics",
            headers=get_headers(api_key),
            params={"postId": "dummy_check"},
            timeout=10
        )
        
        if response.status_code == 402:
            logger.error("❌ Analytics Addon契約が必要です")
            logger.error("   https://app.getlate.dev/settings/billing で契約してください")
            return False
        
        return True
    except Exception as e:
        logger.warning(f"Analytics Addon確認中にエラー: {e}")
        return True  # エラー時は続行を許可


def fetch_analytics_page(
    base_url: str,
    api_key: str,
    from_date: str,
    to_date: str,
    platform: Optional[str] = None,
    page: int = 1,
    limit: int = 100,
    sort_by: str = "date",
    order: str = "desc"
) -> Dict:
    """
    /v1/analytics エンドポイントから1ページ分のデータを取得
    
    Issue #2 対応: /v1/analytics を直接使用（N+1問題解決）
    Issue #6 対応: sortBy/order パラメータ活用
    
    Args:
        base_url: Late API Base URL
        api_key: API Key
        from_date: 開始日 (YYYY-MM-DD)
        to_date: 終了日 (YYYY-MM-DD)
        platform: プラットフォーム名 (x, threads, linkedin, facebook)
        page: ページ番号（1から開始）
        limit: 1ページあたりの件数（1-100）
        sort_by: ソート基準 ("date" または "engagement")
        order: ソート順序 ("asc" または "desc")
    
    Returns:
        APIレスポンス（posts配列とメタデータ）
    """
    params = {
        "dateFrom": from_date,  # ✅ 修正: Late API OpenAPI仕様では dateFrom が正しい
        "dateTo": to_date,      # ✅ 修正: Late API OpenAPI仕様では dateTo が正しい
        "limit": limit,
        "page": page,
        "sortBy": sort_by,
        "order": order
    }
    
    if platform:
        params["platform"] = platform
    
    try:
        response = requests.get(
            f"{base_url}/analytics",
            headers=get_headers(api_key),
            params=params,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            logger.info(f"⏳ Page {page} - アナリティクスデータ処理中 (202)")
            return {"posts": [], "hasMore": False}
        elif response.status_code == 400:
            error_body = response.json()
            logger.error(f"❌ 無効なリクエスト (400): {error_body}")
            return {"posts": [], "hasMore": False}
        elif response.status_code == 402:
            logger.error(f"❌ Analytics Addon未契約 (402)")
            return {"posts": [], "hasMore": False}
        elif response.status_code == 404:
            logger.warning(f"⚠️  データが見つかりません (404)")
            return {"posts": [], "hasMore": False}
        elif response.status_code >= 500:
            logger.error(f"❌ サーバーエラー ({response.status_code})")
            return {"posts": [], "hasMore": False}
        else:
            logger.warning(f"⚠️  予期しないステータスコード: {response.status_code}")
            return {"posts": [], "hasMore": False}
    
    except requests.exceptions.Timeout:
        logger.error(f"❌ タイムアウト (Page {page})")
        return {"posts": [], "hasMore": False}
    except Exception as e:
        logger.error(f"❌ エラー発生 (Page {page}): {e}")
        return {"posts": [], "hasMore": False}


def fetch_all_analytics(
    from_date: str,
    to_date: str,
    platform: Optional[str] = None,
    config_path: Optional[str] = None,
    sort_by: str = "date",
    order: str = "desc"
) -> Dict:
    """
    全投稿のアナリティクスを取得（ページネーション対応）
    
    Issue #3 対応: ページネーション実装
    
    Args:
        from_date: 開始日 (YYYY-MM-DD)
        to_date: 終了日 (YYYY-MM-DD)
        platform: プラットフォーム名 (x, threads, linkedin, facebook)
        config_path: 設定ファイルパス
        sort_by: ソート基準 ("date" または "engagement")
        order: ソート順序 ("asc" または "desc")
    
    Returns:
        アナリティクスデータ（メタデータ含む）
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    logger.info(f"\n🚀 Late API Analytics 最適化版データ取得開始")
    logger.info(f"   期間: {from_date} ～ {to_date}")
    if platform:
        logger.info(f"   プラットフォーム: {platform}")
    logger.info(f"   ソート: {sort_by} ({order})")
    logger.info("")
    
    # Analytics Addon契約確認
    if not check_analytics_addon(base_url, api_key):
        return {
            "metadata": {
                "fetched_at": datetime.now().isoformat(),
                "period_start": from_date,
                "period_end": to_date,
                "total_posts": 0,
                "error": "Analytics Addon未契約"
            },
            "data": []
        }
    
    # ページネーションでデータ取得
    all_analytics_data = []
    page = 1
    total_posts_count = 0
    
    while True:
        logger.info(f"   📄 Page {page} を取得中...")
        
        page_data = fetch_analytics_page(
            base_url, api_key, from_date, to_date, platform,
            page=page, limit=100, sort_by=sort_by, order=order
        )
        
        posts = page_data.get("posts", [])
        
        if not posts:
            logger.info(f"   ✅ Page {page} - データなし（取得完了）")
            break
        
        total_posts_count += len(posts)
        logger.info(f"   ✅ Page {page} - {len(posts)}件取得（累計: {total_posts_count}件）")
        
        # 各投稿のデータを処理
        for post in posts:
            # Issue #4 対応: Dual ID System
            post_id = post.get("postId") or post.get("_id")
            is_external = post.get("isExternal", False)
            platform_post_url = post.get("platformPostUrl")
            
            analytics_obj = post.get("analytics", {})
            platform_analytics = post.get("platformAnalytics", [])
            
            # プラットフォーム情報を取得
            detected_platform = post.get("platform")
            if not detected_platform and platform_analytics:
                detected_platform = platform_analytics[0].get("platform")
            
            # エンゲージメント率の取得
            engagement_rate = 0
            if platform_analytics:
                engagement_rate = platform_analytics[0].get("analytics", {}).get("engagementRate", 0)
            
            # Issue #8 対応: lastUpdated を記録
            last_updated = analytics_obj.get("lastUpdated")
            
            # Issue #9 対応: 全文と要約の両方を保存
            content_full = post.get("content", "")
            
            all_analytics_data.append({
                "post_id": post_id,
                "is_external": is_external,  # ✅ Issue #4 対応
                "platform_post_url": platform_post_url,  # ✅ Issue #4 対応
                "platform": detected_platform,
                "published_at": post.get("publishedAt"),
                "scheduled_for": post.get("scheduledFor"),
                "status": post.get("status"),
                "text_full": content_full,  # ✅ Issue #9 対応
                "text_preview": content_full[:100],
                "impressions": analytics_obj.get("impressions", 0),
                "engagement_rate": engagement_rate,
                "likes": analytics_obj.get("likes", 0),
                "comments": analytics_obj.get("comments", 0),
                "shares": analytics_obj.get("shares", 0),
                "reach": analytics_obj.get("reach", 0),
                "clicks": analytics_obj.get("clicks", 0),
                "views": analytics_obj.get("views", 0),
                "last_updated": last_updated,  # ✅ Issue #8 対応
                "raw_analytics": post  # 全データを保存
            })
        
        # 次ページがあるかチェック
        # hasMore フィールドがあればそれを使用、なければ取得件数で判定
        has_more = page_data.get("hasMore")
        if has_more is not None:
            if not has_more:
                break
        else:
            # hasMore がない場合は取得件数で判定
            if len(posts) < 100:
                break
        
        page += 1
        
        # Rate Limit対策: 短い待機時間
        time.sleep(0.5)
    
    logger.info(f"\n   📊 合計 {total_posts_count} 件の投稿を取得")
    
    # プラットフォーム別統計
    platform_stats = {}
    for item in all_analytics_data:
        p = item["platform"]
        if p not in platform_stats:
            platform_stats[p] = {
                "total_posts": 0,
                "impressions": 0,
                "total_engagement": 0,
                "external_posts": 0,
                "late_posts": 0
            }
        platform_stats[p]["total_posts"] += 1
        platform_stats[p]["impressions"] += item.get("impressions", 0)
        platform_stats[p]["total_engagement"] += (
            item.get("likes", 0) +
            item.get("comments", 0) +
            item.get("shares", 0)
        )
        
        # Issue #4 対応: External/Late Post の分類
        if item.get("is_external"):
            platform_stats[p]["external_posts"] += 1
        else:
            platform_stats[p]["late_posts"] += 1
    
    # 結果サマリー
    result = {
        "metadata": {
            "fetched_at": datetime.now().isoformat(),
            "period_start": from_date,
            "period_end": to_date,
            "total_posts": len(all_analytics_data),
            "total_pages": page,
            "total_impressions": sum(item.get("impressions", 0) for item in all_analytics_data),
            "total_engagement": sum(
                item.get("likes", 0) + item.get("comments", 0) + item.get("shares", 0)
                for item in all_analytics_data
            ),
            "platform_stats": platform_stats,
            "optimization_info": {
                "api_calls": page,  # ✅ 大幅削減（従来は N+1 回）
                "script_version": "optimized_v1.0",
                "issues_fixed": ["#1_param_names", "#2_n+1_query", "#3_pagination", "#4_dual_id"]
            }
        },
        "data": all_analytics_data
    }

    return result


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description="Late API Analytics 最適化版データ取得（Issues #1-4 修正済み）"
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
        "--sort-by",
        type=str,
        choices=["date", "engagement"],
        default="date",
        help="ソート基準（デフォルト: date）"
    )
    parser.add_argument(
        "--order",
        type=str,
        choices=["asc", "desc"],
        default="desc",
        help="ソート順序（デフォルト: desc）"
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
        platform=args.platform,
        sort_by=args.sort_by,
        order=args.order
    )

    # 出力ファイルパス決定
    if args.output:
        output_path = Path(args.output)
    else:
        from_date_str = args.from_date.replace("-", "")
        to_date_str = args.to_date.replace("-", "")
        filename = f"late_api_analytics_optimized_{from_date_str}-{to_date_str}.json"
        output_path = Path(__file__).parent.parent / "data" / filename

    # データ保存
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # サマリー表示
    print("\n" + "="*80)
    print("📊 Late API Analytics 最適化版 - データ取得完了")
    print("="*80)
    print(f"保存先: {output_path}")
    print(f"期間: {args.from_date} ～ {args.to_date}")
    print(f"\n✅ 修正済みIssues: #1 (パラメータ名), #2 (N+1問題), #3 (ページネーション), #4 (Dual ID)")
    print(f"\n総投稿数: {result['metadata']['total_posts']}件")
    print(f"総ページ数: {result['metadata']['total_pages']}ページ")
    print(f"API呼び出し数: {result['metadata']['optimization_info']['api_calls']}回")
    print(f"総インプレッション数: {result['metadata']['total_impressions']:,}")
    print(f"総エンゲージメント数: {result['metadata']['total_engagement']:,}")

    print("\nプラットフォーム別統計:")
    for platform, stats in result['metadata']['platform_stats'].items():
        platform_name = platform if platform else "不明"
        print(f"  {platform_name:10s}: {stats['total_posts']:3d}件 | "
              f"Impressions: {stats['impressions']:,} | "
              f"Engagement: {stats['total_engagement']:,} | "
              f"External: {stats['external_posts']} / Late: {stats['late_posts']}")

    print("\n✅ 完了")


if __name__ == "__main__":
    main()
