#!/usr/bin/env python3
"""
Late API Scheduler - 予約投稿スケジューリング

このモジュールは、Late API経由での予約投稿スケジューリングを管理します。
- 既存予約投稿の取得
- 空き日検索（14日先まで）
- 20:00 JST予約日時生成
- リトライ付き投稿
"""

import os
import time
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Dict, List, Optional, Set
from pathlib import Path

# 既存のユーティリティをインポート
from late_api_utils import load_env_vars


class SchedulingError(Exception):
    """スケジューリングエラー基底クラス"""
    pass


class NoAvailableSlotError(SchedulingError):
    """空き日なしエラー"""
    pass


class LateAPIError(Exception):
    """Late APIエラー基底クラス"""
    pass


class AuthenticationError(LateAPIError):
    """認証エラー（401）"""
    pass


class RateLimitError(LateAPIError):
    """レート制限エラー（429）"""
    pass


class BadRequestError(LateAPIError):
    """リクエスト不正エラー（400）"""
    pass


class NetworkTimeoutError(LateAPIError):
    """ネットワークタイムアウト"""
    pass


class LateAPIScheduler:
    """Late API予約投稿スケジューラー"""

    def __init__(self, config_path: str = None, env_path: str = None):
        """
        Args:
            config_path: Late API設定ファイルパス（オプション）
            env_path: .envファイルパス（オプション）
        """
        # 環境変数読み込み
        if env_path:
            self.env_vars = load_env_vars(env_path)
        else:
            # デフォルト: Stock/programs/副業/projects/SNS/.env
            default_env = Path(__file__).parent.parent / ".env"
            if default_env.exists():
                self.env_vars = load_env_vars(str(default_env))
            else:
                self.env_vars = {}

        # Late API設定
        self.api_key = self.env_vars.get('LATE_API_KEY') or os.environ.get('LATE_API_KEY')
        if not self.api_key:
            raise ValueError("LATE_API_KEY not found in environment variables")

        self.base_url = "https://getlate.dev/api/v1"
        self.jst = ZoneInfo('Asia/Tokyo')

        # アカウント情報（config_pathから読み込み、またはenv_varsから）
        if config_path:
            self._load_config(config_path)
        else:
            self.accounts = {
                'twitter': self.env_vars.get('LATE_TWITTER_ACCOUNT_ID') or os.environ.get('LATE_TWITTER_ACCOUNT_ID'),
                'threads': self.env_vars.get('LATE_THREADS_ACCOUNT_ID') or os.environ.get('LATE_THREADS_ACCOUNT_ID')
            }

    def _load_config(self, config_path: str):
        """設定ファイルからアカウント情報を読み込み"""
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        self.accounts = {
            platform: info['accountId']
            for platform, info in config.get('accounts', {}).items()
        }

    def get_existing_reservations(
        self,
        target_hour: int = 20,
        target_minute: int = 0
    ) -> Set[datetime.date]:
        """
        Late APIから既存予約投稿を取得し、指定時刻の予約済み日付を抽出

        Args:
            target_hour: 対象時刻（時）
            target_minute: 対象時刻（分）

        Returns:
            予約済み日付のセット

        Raises:
            LateAPIError: API呼び出しエラー
        """
        try:
            response = requests.get(
                f"{self.base_url}/posts",
                headers={'Authorization': f'Bearer {self.api_key}'},
                params={'status': 'scheduled'},
                timeout=30
            )
            self._handle_response(response)

            posts_data = response.json()
            reserved_dates = set()

            for post in posts_data.get('posts', []):
                scheduled_for = post.get('scheduledFor')
                if not scheduled_for:
                    continue

                # ISO 8601形式をパース
                dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
                dt_jst = dt.astimezone(self.jst)

                # 指定時刻の予約をチェック
                if dt_jst.hour == target_hour and dt_jst.minute == target_minute:
                    reserved_dates.add(dt_jst.date())

            return reserved_dates

        except requests.exceptions.Timeout:
            raise NetworkTimeoutError("既存予約の取得がタイムアウトしました")
        except requests.exceptions.RequestException as e:
            raise LateAPIError(f"既存予約の取得に失敗: {e}")

    def find_available_slot(
        self,
        days_ahead: int = 14,
        target_hour: int = 20,
        target_minute: int = 0,
        specified_date: Optional[str] = None
    ) -> datetime:
        """
        空き日を検索し、予約日時を返す

        Args:
            days_ahead: 検索範囲（日数）
            target_hour: 予約時刻（時）
            target_minute: 予約時刻（分）
            specified_date: ユーザー指定日（YYYY-MM-DD形式、オプション）

        Returns:
            予約日時（JSTタイムゾーン付き）

        Raises:
            NoAvailableSlotError: 空き日が見つからない
            ValueError: 指定日が既に予約済み
        """
        # 既存予約を取得
        reserved_dates = self.get_existing_reservations(target_hour, target_minute)

        # ユーザー指定日がある場合
        if specified_date:
            specified_dt = datetime.strptime(specified_date, "%Y-%m-%d").date()

            # 競合チェック
            if specified_dt in reserved_dates:
                raise ValueError(
                    f"{specified_date}は既に{target_hour:02d}:{target_minute:02d}に予約投稿があります"
                )

            # 予約日時を作成
            scheduled_dt = datetime.combine(
                specified_dt,
                datetime.min.time().replace(hour=target_hour, minute=target_minute),
                tzinfo=self.jst
            )
            return scheduled_dt

        # 自動検索: 翌日から検索開始
        current_date = (datetime.now(self.jst) + timedelta(days=1)).date()
        end_date = current_date + timedelta(days=days_ahead)

        while current_date <= end_date:
            if current_date not in reserved_dates:
                # 空き日発見
                scheduled_dt = datetime.combine(
                    current_date,
                    datetime.min.time().replace(hour=target_hour, minute=target_minute),
                    tzinfo=self.jst
                )
                return scheduled_dt

            current_date += timedelta(days=1)

        # 空き日が見つからない
        raise NoAvailableSlotError(
            f"{days_ahead}日先まで{target_hour:02d}:{target_minute:02d}の空き日がありません"
        )

    def schedule_post(
        self,
        content: str,
        platform: str,
        scheduled_dt: datetime,
        image_path: Optional[str] = None,
        platform_specific_data: Optional[Dict] = None,
        max_retries: int = 3
    ) -> Dict:
        """
        Late API経由で予約投稿（リトライ付き）

        Args:
            content: 投稿内容
            platform: プラットフォーム名（'twitter', 'threads'）
            scheduled_dt: 予約日時（JSTタイムゾーン付き）
            image_path: 画像ファイルパス（オプション）
            platform_specific_data: プラットフォーム固有データ（オプション）
            max_retries: 最大リトライ回数

        Returns:
            Late APIレスポンス

        Raises:
            LateAPIError: API呼び出しエラー
        """
        account_id = self.accounts.get(platform)
        if not account_id:
            raise ValueError(f"アカウントID not found for platform: {platform}")

        # ISO 8601形式に変換（+09:00付き）
        iso_str = scheduled_dt.strftime("%Y-%m-%dT%H:%M:%S%z")
        iso_str = iso_str[:-2] + ':' + iso_str[-2:]  # +0900 → +09:00

        # リクエストボディ作成
        payload = {
            'content': content,
            'scheduledFor': iso_str,
            'timezone': 'Asia/Tokyo',
            'platforms': [{
                'platform': platform,
                'accountId': account_id
            }],
            'publishNow': False,
            'crosspostingEnabled': False
        }

        # プラットフォーム固有データ追加
        if platform_specific_data:
            payload['platforms'][0]['platformSpecificData'] = platform_specific_data

        # 画像添付
        if image_path:
            uploaded_image_url = self._upload_image(image_path)
            payload['media'] = [{'url': uploaded_image_url}]

        # リトライ付き投稿
        return self._post_with_retry(payload, max_retries)

    def _post_with_retry(self, payload: Dict, max_retries: int) -> Dict:
        """リトライ付きでLate APIに投稿"""
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f"{self.base_url}/posts",
                    headers={
                        'Authorization': f'Bearer {self.api_key}',
                        'Content-Type': 'application/json'
                    },
                    json=payload,
                    timeout=30
                )

                self._handle_response(response)
                return response.json()

            except RateLimitError as e:
                if attempt < max_retries - 1:
                    wait_time = 3600  # 1時間
                    print(f"⚠️  Rate Limit検出、{wait_time}秒待機中... (試行 {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    raise

            except NetworkTimeoutError as e:
                if attempt < max_retries - 1:
                    wait_time = 10 * (2 ** attempt)  # 指数バックオフ
                    print(f"⚠️  Timeout検出、{wait_time}秒待機中... (試行 {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    raise

            except AuthenticationError:
                # 401は即時停止
                print("❌ 認証エラー: Late API設定を確認してください")
                raise

            except BadRequestError as e:
                # 400は即時停止
                print(f"❌ リクエスト不正エラー: {e}")
                raise

        # ここには到達しないはずだが、念のため
        raise LateAPIError(f"{max_retries}回のリトライ後も失敗しました")

    def _handle_response(self, response: requests.Response):
        """Late APIレスポンスのエラーハンドリング"""
        if response.status_code == 200 or response.status_code == 201:
            return

        # エラーハンドリング
        if response.status_code == 401:
            raise AuthenticationError("Late API認証失敗: APIキーを確認してください")

        if response.status_code == 429:
            raise RateLimitError("Late APIレート制限超過")

        if response.status_code == 400:
            error_detail = response.json().get('message', 'Unknown error')
            raise BadRequestError(f"リクエスト不正: {error_detail}")

        if response.status_code >= 500:
            raise LateAPIError(f"Late APIサーバーエラー: {response.status_code}")

        # その他のエラー
        raise LateAPIError(f"Late APIエラー: {response.status_code} - {response.text}")

    def _upload_image(self, image_path: str) -> str:
        """
        Late APIに画像をアップロードし、URLを取得

        Args:
            image_path: ローカル画像ファイルパス

        Returns:
            アップロードされた画像のURL

        Raises:
            FileNotFoundError: 画像ファイルが見つからない
            LateAPIError: アップロード失敗
        """
        image_path_obj = Path(image_path)
        if not image_path_obj.exists():
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")

        # Late API画像アップロードエンドポイント
        # POST /media にmultipart/form-data形式でアップロード
        try:
            with open(image_path, 'rb') as f:
                files = {'file': (image_path_obj.name, f, 'image/png')}
                response = requests.post(
                    f"{self.base_url}/media",
                    headers={'Authorization': f'Bearer {self.api_key}'},
                    files=files,
                    timeout=60
                )

            self._handle_response(response)
            result = response.json()

            # Late APIは {'url': 'https://...'} 形式でURLを返す
            if 'url' not in result:
                raise LateAPIError("画像アップロード応答にURLが含まれていません")

            return result['url']

        except requests.exceptions.Timeout:
            raise NetworkTimeoutError("画像アップロードがタイムアウトしました")
        except requests.exceptions.RequestException as e:
            raise LateAPIError(f"画像アップロードエラー: {e}")


def find_available_slot_simple(
    days_ahead: int = 14,
    target_hour: int = 20,
    specified_date: Optional[str] = None
) -> datetime:
    """
    空き日検索の簡易インターフェース

    Args:
        days_ahead: 検索範囲（日数）
        target_hour: 予約時刻（時）
        specified_date: ユーザー指定日（YYYY-MM-DD形式、オプション）

    Returns:
        予約日時（JSTタイムゾーン付き）

    Example:
        >>> scheduled_dt = find_available_slot_simple(days_ahead=14, target_hour=20)
        >>> print(scheduled_dt)
        2026-01-08 20:00:00+09:00
    """
    scheduler = LateAPIScheduler()
    return scheduler.find_available_slot(
        days_ahead=days_ahead,
        target_hour=target_hour,
        specified_date=specified_date
    )


def schedule_post_simple(
    content: str,
    platform: str,
    scheduled_dt: datetime,
    image_path: Optional[str] = None
) -> Dict:
    """
    予約投稿の簡易インターフェース

    Args:
        content: 投稿内容
        platform: プラットフォーム名（'twitter', 'threads'）
        scheduled_dt: 予約日時（JSTタイムゾーン付き）
        image_path: 画像ファイルパス（オプション）

    Returns:
        Late APIレスポンス

    Example:
        >>> from datetime import datetime
        >>> from zoneinfo import ZoneInfo
        >>> jst = ZoneInfo('Asia/Tokyo')
        >>> scheduled_dt = datetime(2026, 1, 8, 20, 0, 0, tzinfo=jst)
        >>> result = schedule_post_simple("テスト投稿", "twitter", scheduled_dt)
        >>> print(result['post_id'])
    """
    scheduler = LateAPIScheduler()
    return scheduler.schedule_post(content, platform, scheduled_dt, image_path)


if __name__ == "__main__":
    # テスト実行
    print("=" * 50)
    print("Late API Scheduler テスト")
    print("=" * 50)

    try:
        # STEP 1: 既存予約を取得
        scheduler = LateAPIScheduler()
        reserved = scheduler.get_existing_reservations(target_hour=20)
        print(f"\n✅ 既存予約（20:00 JST）: {len(reserved)}件")
        for date in sorted(reserved):
            print(f"  - {date}")

        # STEP 2: 空き日を検索
        available_slot = scheduler.find_available_slot(days_ahead=14, target_hour=20)
        print(f"\n✅ 次の空き日: {available_slot.strftime('%Y-%m-%d %H:%M:%S %Z')}")

        # STEP 3: テスト投稿（実際には実行しない、コメントアウト）
        # result = scheduler.schedule_post(
        #     content="テスト投稿",
        #     platform="twitter",
        #     scheduled_dt=available_slot
        # )
        # print(f"\n✅ 投稿成功: Post ID = {result.get('post_id')}")

        print("\n" + "=" * 50)
        print("✅ すべてのテストが成功しました")
        print("=" * 50)

    except NoAvailableSlotError as e:
        print(f"\n⚠️  空き日なし: {e}")
    except AuthenticationError as e:
        print(f"\n❌ 認証エラー: {e}")
    except LateAPIError as e:
        print(f"\n❌ Late APIエラー: {e}")
    except Exception as e:
        print(f"\n❌ 実行エラー: {e}")
        import traceback
        traceback.print_exc()
