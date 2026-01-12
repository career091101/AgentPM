#!/usr/bin/env python3
"""
Late API 日次アナリティクス収集スクリプト
毎日AM 9:00に前日のデータを自動取得し、SQLiteに保存
"""

import requests
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import os
from typing import Dict, List


# ベースパス設定
BASE_DIR = Path(__file__).parent.parent
CONFIG_PATH = BASE_DIR / "config" / "late_api_config.json"
DB_PATH = BASE_DIR / "data" / "analytics.db"
BACKUP_DIR = BASE_DIR / "data" / "analytics_backup"


def load_config() -> dict:
    """Late API設定をロード"""
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 環境変数からAPI Keyを取得
    api_key = os.environ.get("LATE_API_KEY")
    if api_key:
        config["api_key"] = api_key

    return config


def get_headers(api_key: str) -> dict:
    """APIリクエストヘッダー"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


def init_database():
    """データベース初期化（テーブル作成）"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # analytics テーブル
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id TEXT UNIQUE NOT NULL,
            platform TEXT NOT NULL,
            published_at TEXT NOT NULL,
            impressions INTEGER DEFAULT 0,
            reach INTEGER DEFAULT 0,
            likes INTEGER DEFAULT 0,
            comments INTEGER DEFAULT 0,
            shares INTEGER DEFAULT 0,
            clicks INTEGER DEFAULT 0,
            views INTEGER DEFAULT 0,
            engagement_rate REAL DEFAULT 0.0,
            collected_at TEXT NOT NULL,
            raw_data TEXT
        )
    """)

    # daily_summary テーブル
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL,
            platform TEXT NOT NULL,
            total_posts INTEGER DEFAULT 0,
            total_impressions INTEGER DEFAULT 0,
            total_engagement INTEGER DEFAULT 0,
            avg_engagement_rate REAL DEFAULT 0.0,
            top_post_id TEXT,
            top_post_impressions INTEGER DEFAULT 0,
            collected_at TEXT NOT NULL
        )
    """)

    # インデックス作成
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_platform ON analytics(platform)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_published_at ON analytics(published_at)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_impressions ON analytics(impressions DESC)")

    conn.commit()
    conn.close()

    print("✅ データベース初期化完了")


def get_analytics(
    config: dict,
    from_date: str,
    to_date: str,
    platform: str = None,
    limit: int = 1000
) -> List[Dict]:
    """Late API経由でアナリティクスデータを取得"""
    api_key = config["api_key"]
    base_url = config["base_url"]

    params = {
        "fromDate": from_date,
        "toDate": to_date,
        "limit": limit,
        "sortBy": "date"
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
            data = response.json()
            # データ構造によって分岐
            if isinstance(data, dict) and "data" in data:
                return data["data"]
            elif isinstance(data, list):
                return data
            else:
                return [data]
        else:
            print(f"❌ API エラー: {response.status_code}")
            print(f"Response: {response.text}")
            return []

    except Exception as e:
        print(f"❌ API呼び出しエラー: {e}")
        return []


def save_to_database(analytics_data: List[Dict]):
    """アナリティクスデータをSQLiteに保存"""
    if not analytics_data:
        print("⚠️  保存するデータがありません")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    collected_at = datetime.now().isoformat()

    saved_count = 0
    updated_count = 0

    for item in analytics_data:
        try:
            # データ抽出（フィールド名は実際のAPIレスポンスに合わせて調整）
            post_id = item.get("postId") or item.get("id")
            platform = item.get("platform", "unknown")
            published_at = item.get("publishedAt") or item.get("createdAt")
            impressions = item.get("impressions", 0)
            reach = item.get("reach", 0)
            likes = item.get("likes", 0)
            comments = item.get("comments", 0)
            shares = item.get("shares", 0)
            clicks = item.get("clicks", 0)
            views = item.get("views", 0)
            engagement_rate = item.get("engagementRate", 0.0)

            # INSERT OR REPLACE（既存データは更新）
            cursor.execute("""
                INSERT OR REPLACE INTO analytics (
                    post_id, platform, published_at, impressions, reach,
                    likes, comments, shares, clicks, views, engagement_rate,
                    collected_at, raw_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                post_id, platform, published_at, impressions, reach,
                likes, comments, shares, clicks, views, engagement_rate,
                collected_at, json.dumps(item)
            ))

            if cursor.rowcount > 0:
                if cursor.lastrowid > 0:
                    saved_count += 1
                else:
                    updated_count += 1

        except Exception as e:
            print(f"⚠️  データ保存エラー: {e}")
            print(f"問題のデータ: {item}")

    conn.commit()
    conn.close()

    print(f"✅ データベース保存完了: {saved_count}件新規, {updated_count}件更新")


def save_daily_summary(date: str, platform: str):
    """日次サマリーを計算・保存"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 日次集計
    cursor.execute("""
        SELECT
            COUNT(*) as total_posts,
            SUM(impressions) as total_impressions,
            SUM(likes + comments + shares) as total_engagement,
            AVG(engagement_rate) as avg_engagement_rate,
            MAX(impressions) as max_impressions
        FROM analytics
        WHERE DATE(published_at) = ? AND platform = ?
    """, (date, platform))

    result = cursor.fetchone()

    if result and result[0] > 0:
        # トップ投稿取得
        cursor.execute("""
            SELECT post_id, impressions
            FROM analytics
            WHERE DATE(published_at) = ? AND platform = ?
            ORDER BY impressions DESC
            LIMIT 1
        """, (date, platform))

        top_post = cursor.fetchone()
        top_post_id = top_post[0] if top_post else None
        top_post_impressions = top_post[1] if top_post else 0

        # サマリー保存
        cursor.execute("""
            INSERT OR REPLACE INTO daily_summary (
                date, platform, total_posts, total_impressions, total_engagement,
                avg_engagement_rate, top_post_id, top_post_impressions, collected_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            date, platform, result[0], result[1] or 0, result[2] or 0,
            result[3] or 0.0, top_post_id, top_post_impressions,
            datetime.now().isoformat()
        ))

    conn.commit()
    conn.close()


def export_csv_backup(analytics_data: List[Dict], date: str):
    """CSVバックアップ出力"""
    import csv

    # バックアップディレクトリ作成
    BACKUP_DIR.mkdir(exist_ok=True)

    csv_path = BACKUP_DIR / f"analytics_{date}.csv"

    if not analytics_data:
        print("⚠️  CSVに出力するデータがありません")
        return

    # フィールド名取得
    fieldnames = list(analytics_data[0].keys())

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(analytics_data)

    print(f"✅ CSVバックアップ保存: {csv_path}")


def main():
    """メイン処理"""
    print("\n" + "=" * 80)
    print("🚀 Late API 日次アナリティクス収集開始")
    print("=" * 80)
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 設定読み込み
    config = load_config()

    # データベース初期化
    init_database()

    # 前日の日付
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    print(f"📅 収集対象日: {yesterday}\n")

    # 全プラットフォームのデータ取得
    platforms = ["facebook", "linkedin", "twitter", "threads"]
    all_data = []

    for platform in platforms:
        print(f"📊 {platform.upper()} データ取得中...")

        data = get_analytics(
            config=config,
            from_date=yesterday,
            to_date=yesterday,
            platform=platform,
            limit=1000
        )

        if data:
            print(f"   取得件数: {len(data)}件")
            all_data.extend(data)

            # プラットフォーム別サマリー保存
            save_daily_summary(yesterday, platform)
        else:
            print(f"   ⚠️  データなし")

    print()

    # データベース保存
    if all_data:
        save_to_database(all_data)

        # CSVバックアップ
        export_csv_backup(all_data, yesterday)

        print(f"\n📈 サマリー:")
        print(f"   総取得件数: {len(all_data)}件")
        print(f"   対象日: {yesterday}")
        print(f"   プラットフォーム数: {len(platforms)}")
    else:
        print("⚠️  取得データが0件でした")

    print("\n" + "=" * 80)
    print("✅ 日次アナリティクス収集完了")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
