#!/usr/bin/env python3
"""
Facebook個人アカウント アナリティクス取得（Meta Graph API使用）

個人アカウントの自分の投稿データを取得します。
ビジネスページのような詳細なInsightsは取得できませんが、基本的なエンゲージメントデータは取得可能です。

セットアップ手順:
1. https://developers.facebook.com/apps にアクセス
2. 「アプリを作成」をクリック
3. 「その他」→「次へ」→「Consumer」を選択
4. アプリ名を入力（例: "My Personal Analytics"）
5. アプリダッシュボード → ツール → Graph APIエクスプローラー
6. アクセストークンを生成（以下の権限を追加）:
   - user_posts
   - user_photos
   - user_videos
7. 生成されたトークンを ACCESS_TOKEN に設定

注意:
- 個人アカウントでは詳細なInsightsは取得不可
- 取得できるのは: いいね数、コメント数、シェア数、投稿日時
- Reach、Impressions等は取得不可（ビジネスページのみ）
"""

import requests
import json
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd


# ===========================
# 設定
# ===========================

# Facebook Graph API設定
ACCESS_TOKEN = "EAAUPVwUe6s8BQWQGdfBtoIIzMpzshxw5rmfUZCWl6BejluNqZCrDpoZAbaVf1LOdZBdDSshZCkZBpXZAOT7JaFAG9FsES8zDGd8pKpkvnblmUAItZBp6NaI0U3EFL86y2fvJybpIw0EfCJ83wrx1eJV3tRuJWNGQ6ZAjhB6Cvu65XIKTu6itXZCKzhaJNmY2z8ADdnu8ZCWiXRI0T8uNf9fdycgmnijJlVFa5eAyZAFiZCD6r8eKmYHRyj9jR89gyrcL3FZA6N2ZAUaeaaBcChUIyqZAA4avhQZB7YklWGZAhUnjcgyv9RsDhDSRf987JapsIaOpURrmSTJopNNom5p30gRwTJIpDMqsvB8QZDZD"  # Graph APIエクスプローラーで生成したトークンを設定
API_VERSION = "v19.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


# ===========================
# データ取得関数
# ===========================

def get_user_posts(
    limit: int = 100,
    since: Optional[str] = None,
    until: Optional[str] = None
) -> List[Dict]:
    """
    個人アカウントの投稿一覧を取得

    Args:
        limit: 取得件数（最大100）
        since: 開始日（YYYY-MM-DD）
        until: 終了日（YYYY-MM-DD）

    Returns:
        List[Dict]: 投稿データリスト
    """
    print("📊 Facebook個人投稿データ取得中...")

    # パラメータ構築
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "id,message,created_time,likes.summary(true),comments.summary(true),shares",
        "limit": min(limit, 100)
    }

    if since:
        params["since"] = since
    if until:
        params["until"] = until

    # API呼び出し
    try:
        # 自分の投稿を取得（/me/feed - より広範なデータを取得）
        response = requests.get(
            f"{BASE_URL}/me/feed",
            params=params,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", [])
            print(f"✅ {len(posts)}件の投稿を取得しました")
            return posts
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"Response: {response.text}")
            return []

    except Exception as e:
        print(f"❌ API呼び出しエラー: {e}")
        return []


def get_post_details(post_id: str) -> Dict:
    """
    特定の投稿の詳細データを取得

    Args:
        post_id: 投稿ID

    Returns:
        Dict: 投稿詳細データ
    """
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "id,message,created_time,story,type,likes.summary(true),comments.summary(true),shares,reactions.summary(true)"
    }

    try:
        response = requests.get(
            f"{BASE_URL}/{post_id}",
            params=params,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ 投稿詳細取得エラー: {response.status_code}")
            return {}

    except Exception as e:
        print(f"❌ エラー: {e}")
        return {}


def get_user_info() -> Dict:
    """
    自分のユーザー情報を取得（接続テスト）

    Returns:
        Dict: ユーザー情報
    """
    print("🔍 ユーザー情報取得中...")

    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "id,name,email"
    }

    try:
        response = requests.get(
            f"{BASE_URL}/me",
            params=params,
            timeout=30
        )

        if response.status_code == 200:
            user = response.json()
            print(f"✅ ユーザー: {user.get('name', 'N/A')}")
            return user
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"Response: {response.text}")
            return {}

    except Exception as e:
        print(f"❌ エラー: {e}")
        return {}


# ===========================
# データ処理関数
# ===========================

def process_posts(posts: List[Dict]) -> pd.DataFrame:
    """
    投稿データをDataFrameに変換

    Args:
        posts: 投稿データリスト

    Returns:
        pd.DataFrame: 分析用データフレーム
    """
    processed = []

    for post in posts:
        # 基本データ抽出
        post_data = {
            "post_id": post.get("id", ""),
            "message": post.get("message", ""),
            "created_time": post.get("created_time", ""),
            "likes": post.get("likes", {}).get("summary", {}).get("total_count", 0),
            "comments": post.get("comments", {}).get("summary", {}).get("total_count", 0),
            "shares": post.get("shares", {}).get("count", 0)
        }

        # エンゲージメント合計
        post_data["total_engagement"] = (
            post_data["likes"] +
            post_data["comments"] +
            post_data["shares"]
        )

        processed.append(post_data)

    # DataFrame作成
    df = pd.DataFrame(processed)

    # 日付変換
    if "created_time" in df.columns:
        df["created_time"] = pd.to_datetime(df["created_time"])
        df["date"] = df["created_time"].dt.date

    return df


def export_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    DataFrameをCSVファイルに出力

    Args:
        df: データフレーム
        output_path: 出力ファイルパス
    """
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ CSVファイルを保存しました: {output_path}")


def export_to_json(posts: List[Dict], output_path: str) -> None:
    """
    投稿データをJSONファイルに出力

    Args:
        posts: 投稿データリスト
        output_path: 出力ファイルパス
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"✅ JSONファイルを保存しました: {output_path}")


def print_summary(df: pd.DataFrame) -> None:
    """
    データのサマリーを表示

    Args:
        df: データフレーム
    """
    if df.empty:
        print("⚠️  データが空です")
        return

    print("\n" + "=" * 80)
    print("📊 Facebookアナリティクスサマリー（個人アカウント）")
    print("=" * 80)

    print(f"\n総投稿数: {len(df)}")

    print(f"\n合計エンゲージメント:")
    print(f"  いいね: {df['likes'].sum():,.0f}")
    print(f"  コメント: {df['comments'].sum():,.0f}")
    print(f"  シェア: {df['shares'].sum():,.0f}")
    print(f"  合計: {df['total_engagement'].sum():,.0f}")

    print(f"\n平均エンゲージメント:")
    print(f"  いいね: {df['likes'].mean():.1f}")
    print(f"  コメント: {df['comments'].mean():.1f}")
    print(f"  シェア: {df['shares'].mean():.1f}")

    print(f"\nTop 5エンゲージメント投稿:")
    top_posts = df.nlargest(5, "total_engagement")[["created_time", "message", "total_engagement", "likes", "comments", "shares"]]
    for idx, row in top_posts.iterrows():
        message_preview = row["message"][:50] + "..." if len(row["message"]) > 50 else row["message"]
        print(f"\n  {row['created_time'].strftime('%Y-%m-%d %H:%M')}")
        print(f"  「{message_preview}」")
        print(f"  エンゲージメント: {row['total_engagement']:.0f} (👍{row['likes']:.0f} 💬{row['comments']:.0f} 🔄{row['shares']:.0f})")

    print("\n" + "=" * 80)


# ===========================
# メイン実行部
# ===========================

def main():
    """メイン処理"""
    print("\n🚀 Facebook個人アカウント アナリティクス取得開始\n")

    # アクセストークンチェック
    if ACCESS_TOKEN == "YOUR_ACCESS_TOKEN_HERE":
        print("=" * 80)
        print("⚠️  ACCESS_TOKENが設定されていません")
        print("=" * 80)
        print("\nセットアップ手順:")
        print("1. https://developers.facebook.com/apps にアクセス")
        print("2. アプリを作成")
        print("3. Graph APIエクスプローラーでトークンを生成")
        print("4. このスクリプトのACCESS_TOKENに設定")
        print("\n必要な権限: user_posts, user_photos, user_videos")
        print("=" * 80)
        return

    # 1. 接続テスト
    print("=" * 80)
    print("1. 接続テスト")
    print("=" * 80)
    user = get_user_info()

    if not user:
        print("\n❌ 接続失敗: トークンが無効です")
        return

    # 2. 投稿データ取得
    print("\n" + "=" * 80)
    print("2. 投稿データ取得")
    print("=" * 80)

    posts = get_user_posts(limit=100)

    if not posts:
        print("\n⚠️  投稿が見つかりませんでした")
        return

    # 3. データ処理
    print("\n" + "=" * 80)
    print("3. データ処理")
    print("=" * 80)

    df = process_posts(posts)

    # 4. サマリー表示
    print_summary(df)

    # 5. ファイル出力
    print("\n" + "=" * 80)
    print("4. ファイル出力")
    print("=" * 80)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"

    # CSV出力
    csv_path = f"{base_path}/facebook_personal_analytics_{timestamp}.csv"
    export_to_csv(df, csv_path)

    # JSON出力
    json_path = f"{base_path}/facebook_personal_analytics_{timestamp}.json"
    export_to_json(posts, json_path)

    print("\n✅ 完了")


if __name__ == "__main__":
    main()
