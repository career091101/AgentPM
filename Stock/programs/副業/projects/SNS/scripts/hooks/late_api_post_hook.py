#!/usr/bin/env python3
"""
Late API投稿後フック

Late APIで予約投稿した際に、公開日の1日後のレビューをスケジュール
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime, timedelta


def extract_publication_date_from_late_response(late_response: dict) -> str:
    """Late APIレスポンスから公開予定日を抽出"""

    # Late APIのレスポンス形式に応じて調整
    # 例: {"scheduled_time": "2026-01-10T09:00:00Z"}

    if "scheduled_time" in late_response:
        scheduled_time = late_response["scheduled_time"]
        # ISO 8601形式をパース
        dt = datetime.fromisoformat(scheduled_time.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d")

    # scheduledAtフィールドがある場合
    if "scheduledAt" in late_response:
        scheduled_time = late_response["scheduledAt"]
        dt = datetime.fromisoformat(scheduled_time.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d")

    # publishDateフィールドがある場合
    if "publishDate" in late_response:
        return late_response["publishDate"]

    # デフォルト: 30分後（Late APIのデフォルト設定）
    default_time = datetime.now() + timedelta(minutes=30)
    return default_time.strftime("%Y-%m-%d")


def trigger_post_publication_review(post_file_path: str, publication_date: str):
    """予約投稿の1日後のレビューをスケジュール"""

    # プロジェクトルート
    base_dir = Path(__file__).parent.parent.parent.parent.parent.parent

    # スケジューラースクリプト
    scheduler_script = base_dir / ".claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py"

    if not scheduler_script.exists():
        print(f"⚠️  スケジューラースクリプトが見つかりません: {scheduler_script}")
        return

    print(f"\n📅 予約投稿の1日後のレビューをスケジュールします...")
    print(f"   対象ファイル: {post_file_path}")
    print(f"   公開予定日: {publication_date}")

    # スケジューラー実行
    try:
        result = subprocess.run(
            [
                "python3", str(scheduler_script),
                "schedule",
                "--post-file", post_file_path,
                "--publication-date", publication_date
            ],
            cwd=str(base_dir),
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.returncode != 0:
            print(f"⚠️  スケジュール登録エラー:")
            print(result.stderr)

    except Exception as e:
        print(f"❌ スケジュール登録エラー: {str(e)}")


def main():
    """メイン実行"""

    if len(sys.argv) < 3:
        print("使用方法: python3 late_api_post_hook.py <post_file_path> <late_response_json>")
        print("")
        print("例:")
        print("  python3 late_api_post_hook.py posts.md '{\"scheduled_time\": \"2026-01-10T09:00:00Z\"}'")
        sys.exit(1)

    post_file_path = sys.argv[1]
    late_response_json = sys.argv[2]

    if not os.path.exists(post_file_path):
        print(f"❌ ファイルが見つかりません: {post_file_path}")
        sys.exit(1)

    # Late APIレスポンスをパース
    try:
        late_response = json.loads(late_response_json)
    except json.JSONDecodeError as e:
        print(f"❌ JSONパースエラー: {str(e)}")
        sys.exit(1)

    # 公開予定日を抽出
    publication_date = extract_publication_date_from_late_response(late_response)

    trigger_post_publication_review(post_file_path, publication_date)


if __name__ == '__main__':
    main()
