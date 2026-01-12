#!/usr/bin/env python3
"""
Late API アナリティクス取得スクリプト
Facebookを含む全プラットフォームのアナリティクスデータを取得
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import pandas as pd


# Late API設定読み込み
def load_config(config_path: str = None) -> dict:
    """Late API設定をロード"""
    if config_path is None:
        config_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/config/late_api_config.json"

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_headers(api_key: str) -> dict:
    """APIリクエストヘッダー"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


def get_analytics(
    platform: Optional[str] = None,
    profile_id: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    post_id: Optional[str] = None,
    limit: int = 50,
    page: int = 1,
    sort_by: str = "date",
    config_path: str = None
) -> Dict:
    """
    Late API経由でアナリティクスデータを取得

    Args:
        platform: プラットフォーム名（facebook, linkedin, twitter, threads, instagram）
        profile_id: プロフィールID
        from_date: 開始日（YYYY-MM-DD）
        to_date: 終了日（YYYY-MM-DD）
        post_id: 特定の投稿ID
        limit: 取得件数（デフォルト: 50）
        page: ページ番号（デフォルト: 1）
        sort_by: ソート順（"date" または "engagement"）
        config_path: 設定ファイルパス

    Returns:
        dict: アナリティクスデータ
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    # パラメータ構築
    params = {
        "limit": limit,
        "page": page,
        "sortBy": sort_by
    }

    if platform:
        params["platform"] = platform
    if profile_id:
        params["profileId"] = profile_id
    if from_date:
        params["fromDate"] = from_date
    if to_date:
        params["toDate"] = to_date
    if post_id:
        params["postId"] = post_id

    # API呼び出し
    try:
        response = requests.get(
            f"{base_url}/analytics",
            headers=get_headers(api_key),
            params=params,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"Response: {response.text}")
            return {"error": response.text, "status_code": response.status_code}

    except Exception as e:
        print(f"❌ API呼び出しエラー: {e}")
        return {"error": str(e)}


def get_facebook_analytics(
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    limit: int = 50,
    sort_by: str = "engagement",
    config_path: str = None
) -> Dict:
    """
    Facebook専用アナリティクス取得

    Args:
        from_date: 開始日（YYYY-MM-DD）デフォルト: 7日前
        to_date: 終了日（YYYY-MM-DD）デフォルト: 今日
        limit: 取得件数
        sort_by: ソート順（"date" または "engagement"）
        config_path: 設定ファイルパス

    Returns:
        dict: Facebookアナリティクスデータ
    """
    # デフォルト日付設定（過去7日間）
    if from_date is None:
        from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    if to_date is None:
        to_date = datetime.now().strftime("%Y-%m-%d")

    return get_analytics(
        platform="facebook",
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        sort_by=sort_by,
        config_path=config_path
    )


def get_follower_stats(
    account_id: str,
    granularity: str = "daily",
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    config_path: str = None
) -> Dict:
    """
    フォロワー統計データを取得

    Args:
        account_id: アカウントID
        granularity: 粒度（"daily", "weekly", "monthly"）
        from_date: 開始日（YYYY-MM-DD）
        to_date: 終了日（YYYY-MM-DD）
        config_path: 設定ファイルパス

    Returns:
        dict: フォロワー統計データ
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    params = {
        "granularity": granularity
    }

    if from_date:
        params["fromDate"] = from_date
    if to_date:
        params["toDate"] = to_date

    try:
        response = requests.get(
            f"{base_url}/accounts/{account_id}/follower-stats",
            headers=get_headers(api_key),
            params=params,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"Response: {response.text}")
            return {"error": response.text, "status_code": response.status_code}

    except Exception as e:
        print(f"❌ API呼び出しエラー: {e}")
        return {"error": str(e)}


def analytics_to_dataframe(analytics_data: Dict) -> pd.DataFrame:
    """
    アナリティクスデータをPandas DataFrameに変換

    Args:
        analytics_data: Late APIから取得したアナリティクスデータ

    Returns:
        pd.DataFrame: 分析用データフレーム
    """
    if "error" in analytics_data:
        print(f"❌ エラーデータのため変換できません: {analytics_data['error']}")
        return pd.DataFrame()

    # データがリストの場合（複数投稿）
    if isinstance(analytics_data, list):
        data = analytics_data
    # データが辞書の場合（単一投稿）
    elif isinstance(analytics_data, dict) and "data" in analytics_data:
        data = analytics_data["data"]
    else:
        data = [analytics_data]

    # DataFrame作成
    df = pd.DataFrame(data)

    # 日付列を変換
    if "publishedAt" in df.columns:
        df["publishedAt"] = pd.to_datetime(df["publishedAt"])

    return df


def export_analytics_report(
    analytics_data: Dict,
    output_path: str,
    format: str = "csv"
) -> None:
    """
    アナリティクスデータをファイル出力

    Args:
        analytics_data: Late APIから取得したアナリティクスデータ
        output_path: 出力ファイルパス
        format: 出力形式（"csv", "json", "excel"）
    """
    if format == "json":
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analytics_data, f, indent=2, ensure_ascii=False)
        print(f"✅ JSONファイルを保存しました: {output_path}")

    elif format == "csv":
        df = analytics_to_dataframe(analytics_data)
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"✅ CSVファイルを保存しました: {output_path}")

    elif format == "excel":
        df = analytics_to_dataframe(analytics_data)
        df.to_excel(output_path, index=False)
        print(f"✅ Excelファイルを保存しました: {output_path}")

    else:
        print(f"❌ 未対応のフォーマット: {format}")


def print_analytics_summary(analytics_data: Dict) -> None:
    """
    アナリティクスデータのサマリーを表示

    Args:
        analytics_data: Late APIから取得したアナリティクスデータ
    """
    if "error" in analytics_data:
        print(f"❌ エラー: {analytics_data['error']}")
        return

    df = analytics_to_dataframe(analytics_data)

    if df.empty:
        print("⚠️  データが空です")
        return

    print("\n" + "=" * 80)
    print("📊 アナリティクスサマリー")
    print("=" * 80)

    print(f"\n総投稿数: {len(df)}")

    # 数値列の統計
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 0:
        print("\n指標の合計値:")
        for col in numeric_cols:
            if col in ["impressions", "reach", "likes", "comments", "shares", "clicks", "views"]:
                print(f"  {col}: {df[col].sum():,.0f}")

        if "engagementRate" in df.columns:
            print(f"\n平均エンゲージメント率: {df['engagementRate'].mean():.2f}%")

    print("\n" + "=" * 80)


# ===========================
# メイン実行部
# ===========================

def main():
    """メイン処理"""
    print("\n🚀 Late API アナリティクス取得開始\n")

    # 1. Facebook アナリティクス取得（過去7日間）
    print("=" * 80)
    print("📊 Facebookアナリティクス取得（過去7日間）")
    print("=" * 80)

    fb_analytics = get_facebook_analytics(
        limit=50,
        sort_by="engagement"
    )

    # サマリー表示
    print_analytics_summary(fb_analytics)

    # CSV出力
    output_path = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/facebook_analytics_{datetime.now().strftime('%Y%m%d')}.csv"
    export_analytics_report(fb_analytics, output_path, format="csv")

    # JSON出力
    json_path = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/facebook_analytics_{datetime.now().strftime('%Y%m%d')}.json"
    export_analytics_report(fb_analytics, json_path, format="json")

    # 2. 全プラットフォームのアナリティクス取得（オプション）
    print("\n" + "=" * 80)
    print("📊 全プラットフォームアナリティクス取得")
    print("=" * 80)

    all_analytics = get_analytics(
        from_date=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        to_date=datetime.now().strftime("%Y-%m-%d"),
        limit=100,
        sort_by="engagement"
    )

    print_analytics_summary(all_analytics)

    print("\n✅ 完了")


if __name__ == "__main__":
    main()
