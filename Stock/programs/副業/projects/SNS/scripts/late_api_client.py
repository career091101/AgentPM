#!/usr/bin/env python3
"""
Late API Client - LinkedIn予約投稿クライアント

Usage:
    from late_api_client import LateAPIClient
    client = LateAPIClient()
    result = client.schedule_linkedin_post(content, schedule_at)
"""

import os
import requests
from datetime import datetime, timezone
import pytz
from pathlib import Path
from dotenv import load_dotenv

# .env読み込み
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")


class LateAPIClient:
    """Late API クライアント（LinkedIn特化）"""

    def __init__(self):
        self.api_key = os.getenv("LATE_API_KEY")
        self.linkedin_account_id = os.getenv("LATE_LINKEDIN_ACCOUNT_ID")

        if not self.api_key:
            raise ValueError("LATE_API_KEY not found in .env file")

        if not self.linkedin_account_id:
            raise ValueError("LATE_LINKEDIN_ACCOUNT_ID not found in .env file")

        self.base_url = "https://api.getlate.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def schedule_linkedin_post(
        self, content: str, schedule_at: datetime
    ) -> dict:
        """
        LinkedIn予約投稿を作成

        Args:
            content: 投稿本文
            schedule_at: 予約日時（JSTまたはUTC）

        Returns:
            dict: Late APIレスポンス
                {
                    "post": {
                        "_id": "post_abc123"
                    }
                }

        Raises:
            Exception: Late APIエラー時
        """
        # UTCに変換（JST→UTCの場合）
        if schedule_at.tzinfo is None:
            # タイムゾーン未指定の場合はJSTと仮定
            jst = pytz.timezone("Asia/Tokyo")
            schedule_at = jst.localize(schedule_at)

        schedule_at_utc = schedule_at.astimezone(timezone.utc)

        # ISO 8601形式（UTC）に変換
        schedule_at_str = schedule_at_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

        # リクエストボディ
        payload = {
            "post": content,
            "profile_ids": [self.linkedin_account_id],
            "schedule_at": schedule_at_str,
        }

        # API呼び出し
        response = requests.post(
            f"{self.base_url}/posts", headers=self.headers, json=payload
        )

        # エラーハンドリング
        if response.status_code != 200:
            error_msg = f"Late API Error: {response.status_code} - {response.text}"
            raise Exception(error_msg)

        return response.json()

    def get_scheduled_posts(self) -> list:
        """
        予約投稿一覧を取得（Late APIには専用エンドポイントがないため、ローカルログから取得を推奨）

        Returns:
            list: 予約投稿リスト（Late APIの仕様により空リストを返す）
        """
        # Late APIには予約投稿一覧取得エンドポイントが存在しないため、
        # ローカルログファイルから取得することを推奨
        return []


if __name__ == "__main__":
    # テスト実行
    from datetime import timedelta

    client = LateAPIClient()

    # テスト: 1時間後にLinkedIn投稿予約
    test_content = "【テスト投稿】Late API経由のLinkedIn予約投稿テスト\n\n#AI #テスト"
    test_schedule = datetime.now() + timedelta(hours=1)

    print(f"📅 予約日時: {test_schedule.strftime('%Y-%m-%d %H:%M:%S')} JST")
    print(f"📝 投稿内容:\n{test_content}\n")

    try:
        result = client.schedule_linkedin_post(test_content, test_schedule)
        print(f"✅ 予約投稿成功!")
        print(f"   Post ID: {result['post']['_id']}")
    except Exception as e:
        print(f"❌ エラー: {e}")
