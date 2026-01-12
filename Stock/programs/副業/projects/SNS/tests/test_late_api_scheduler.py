#!/usr/bin/env python3
"""
Late API Scheduler ユニットテスト
"""

import sys
import pytest
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
from unittest.mock import Mock, patch

# プロジェクトルートをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from late_api_scheduler import (
    LateAPIScheduler,
    NoAvailableSlotError,
    AuthenticationError,
    RateLimitError,
    find_available_slot_simple
)


class TestLateAPIScheduler:
    """LateAPISchedulerクラスのテスト"""

    @pytest.fixture
    def mock_env_vars(self, monkeypatch):
        """環境変数のモック"""
        monkeypatch.setenv('LATE_API_KEY', 'sk_test_key_12345')
        monkeypatch.setenv('LATE_TWITTER_ACCOUNT_ID', 'twitter_account_123')
        monkeypatch.setenv('LATE_THREADS_ACCOUNT_ID', 'threads_account_456')

    @pytest.fixture
    def scheduler(self, mock_env_vars):
        """テスト用スケジューラーインスタンス"""
        return LateAPIScheduler()

    @pytest.fixture
    def mock_existing_reservations(self):
        """既存予約のモックデータ"""
        jst = ZoneInfo('Asia/Tokyo')
        return {
            'posts': [
                {
                    'scheduledFor': datetime(2026, 1, 7, 20, 0, 0, tzinfo=jst).isoformat()
                },
                {
                    'scheduledFor': datetime(2026, 1, 9, 20, 0, 0, tzinfo=jst).isoformat()
                },
                {
                    'scheduledFor': datetime(2026, 1, 10, 21, 0, 0, tzinfo=jst).isoformat()  # 21時（対象外）
                }
            ]
        }

    def test_initialization_with_env_vars(self, mock_env_vars):
        """環境変数からの初期化テスト"""
        scheduler = LateAPIScheduler()

        assert scheduler.api_key == 'sk_test_key_12345'
        assert scheduler.accounts['twitter'] == 'twitter_account_123'
        assert scheduler.accounts['threads'] == 'threads_account_456'

    def test_initialization_without_api_key(self, monkeypatch):
        """APIキー未設定時のエラーテスト"""
        monkeypatch.delenv('LATE_API_KEY', raising=False)

        with pytest.raises(ValueError, match="LATE_API_KEY not found"):
            LateAPIScheduler()

    @patch('requests.get')
    def test_get_existing_reservations_success(self, mock_get, scheduler, mock_existing_reservations):
        """既存予約取得の成功テスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_existing_reservations
        mock_get.return_value = mock_response

        # 実行
        reserved_dates = scheduler.get_existing_reservations(target_hour=20)

        # 検証
        assert datetime(2026, 1, 7).date() in reserved_dates
        assert datetime(2026, 1, 9).date() in reserved_dates
        assert datetime(2026, 1, 10).date() not in reserved_dates  # 21時なので含まれない

        # API呼び出し確認
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert 'status=scheduled' in str(call_args)

    @patch('requests.get')
    def test_find_available_slot_success(self, mock_get, scheduler, mock_existing_reservations):
        """空き日検索の成功テスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_existing_reservations
        mock_get.return_value = mock_response

        # 実行
        available_slot = scheduler.find_available_slot(days_ahead=14, target_hour=20)

        # 検証
        assert available_slot is not None
        assert available_slot.hour == 20
        assert available_slot.minute == 0

        # 予約済み日付でないことを確認
        assert available_slot.date() != datetime(2026, 1, 7).date()
        assert available_slot.date() != datetime(2026, 1, 9).date()

    @patch('requests.get')
    def test_find_available_slot_specified_date(self, mock_get, scheduler, mock_existing_reservations):
        """ユーザー指定日での空き日検索テスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_existing_reservations
        mock_get.return_value = mock_response

        # 実行: 2026-01-08を指定（空き）
        available_slot = scheduler.find_available_slot(
            days_ahead=14,
            target_hour=20,
            specified_date="2026-01-08"
        )

        # 検証
        assert available_slot.date() == datetime(2026, 1, 8).date()
        assert available_slot.hour == 20

    @patch('requests.get')
    def test_find_available_slot_specified_date_conflict(self, mock_get, scheduler, mock_existing_reservations):
        """ユーザー指定日が既に予約済みの場合のエラーテスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_existing_reservations
        mock_get.return_value = mock_response

        # 実行: 2026-01-07を指定（既に予約済み）
        with pytest.raises(ValueError, match="既に.*予約投稿があります"):
            scheduler.find_available_slot(
                days_ahead=14,
                target_hour=20,
                specified_date="2026-01-07"
            )

    @patch('requests.get')
    def test_find_available_slot_no_slots(self, mock_get, scheduler):
        """空き日がない場合のエラーテスト"""
        # 全日予約済みのモック（14日先まで）
        jst = ZoneInfo('Asia/Tokyo')
        all_reserved = {
            'posts': [
                {'scheduledFor': (datetime.now(jst) + timedelta(days=i)).replace(hour=20, minute=0).isoformat()}
                for i in range(1, 15)
            ]
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = all_reserved
        mock_get.return_value = mock_response

        # 実行
        with pytest.raises(NoAvailableSlotError, match="空き日がありません"):
            scheduler.find_available_slot(days_ahead=14, target_hour=20)

    @patch('requests.get')
    def test_handle_response_401(self, mock_get, scheduler):
        """401認証エラーのテスト"""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        with pytest.raises(AuthenticationError, match="Late API認証失敗"):
            scheduler.get_existing_reservations()

    @patch('requests.get')
    def test_handle_response_429(self, mock_get, scheduler):
        """429レート制限エラーのテスト"""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response

        with pytest.raises(RateLimitError, match="Late APIレート制限超過"):
            scheduler.get_existing_reservations()

    @patch('requests.post')
    def test_schedule_post_success(self, mock_post, scheduler):
        """予約投稿成功のテスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            'post_id': '695ceb1e8247cf816ba753b6',
            'status': 'scheduled'
        }
        mock_post.return_value = mock_response

        # 実行
        jst = ZoneInfo('Asia/Tokyo')
        scheduled_dt = datetime(2026, 1, 8, 20, 0, 0, tzinfo=jst)

        result = scheduler.schedule_post(
            content="テスト投稿",
            platform="twitter",
            scheduled_dt=scheduled_dt,
            max_retries=1  # テストではリトライ1回に制限
        )

        # 検証
        assert result['post_id'] == '695ceb1e8247cf816ba753b6'

        # API呼び出し確認
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args.kwargs
        assert call_kwargs['json']['content'] == "テスト投稿"
        assert call_kwargs['json']['platforms'][0]['platform'] == "twitter"

    @patch('requests.post')
    def test_schedule_post_retry_on_timeout(self, mock_post, scheduler):
        """タイムアウト時のリトライテスト"""
        # 1回目: Timeout、2回目: 成功
        mock_response_error = Mock()
        mock_response_error.status_code = 500  # タイムアウトをサーバーエラーとして模擬

        mock_response_success = Mock()
        mock_response_success.status_code = 201
        mock_response_success.json.return_value = {'post_id': 'success_after_retry'}

        mock_post.side_effect = [mock_response_error, mock_response_success]

        # 実行
        jst = ZoneInfo('Asia/Tokyo')
        scheduled_dt = datetime(2026, 1, 8, 20, 0, 0, tzinfo=jst)

        result = scheduler.schedule_post(
            content="テスト投稿",
            platform="twitter",
            scheduled_dt=scheduled_dt,
            max_retries=3
        )

        # 検証: 2回目で成功
        assert result['post_id'] == 'success_after_retry'
        assert mock_post.call_count == 2


class TestSimpleInterface:
    """簡易インターフェースのテスト"""

    @patch('requests.get')
    def test_find_available_slot_simple(self, mock_get, mock_env_vars):
        """find_available_slot_simple関数のテスト"""
        # モックレスポンス
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'posts': []}
        mock_get.return_value = mock_response

        # 実行
        result = find_available_slot_simple(days_ahead=14, target_hour=20)

        # 検証
        assert result is not None
        assert result.hour == 20


if __name__ == "__main__":
    # pytest実行
    pytest.main([__file__, "-v", "--tb=short"])
