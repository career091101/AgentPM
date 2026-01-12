#!/usr/bin/env python3
"""
エラーロギングモジュール

X & Threads同時投稿スキルのエラーログを管理します。
- 詳細なエラーログ出力
- エラー統計の集計
- ログファイルのローテーション
"""

import os
import json
import traceback
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, Any
from zoneinfo import ZoneInfo


class ErrorLogger:
    """エラーログ管理クラス"""

    def __init__(self, log_dir: str = None):
        """
        Args:
            log_dir: ログディレクトリパス（デフォルト: Stock/programs/副業/projects/SNS/logs）
        """
        if log_dir is None:
            log_dir = Path(__file__).parent.parent / "logs"

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.jst = ZoneInfo('Asia/Tokyo')

    def log_error(
        self,
        error_type: str,
        error_message: str,
        context: Dict[str, Any] = None,
        platform: str = None,
        retry_count: int = 0,
        traceback_str: str = None
    ) -> str:
        """
        エラーログを記録

        Args:
            error_type: エラー種別（"AuthenticationError", "RateLimitError"等）
            error_message: エラーメッセージ
            context: コンテキスト情報（入力パラメータ等）
            platform: プラットフォーム名（"twitter", "threads"）
            retry_count: リトライ回数
            traceback_str: トレースバック文字列

        Returns:
            ログファイルパス
        """
        timestamp = datetime.now(self.jst)
        log_entry = {
            "timestamp": timestamp.isoformat(),
            "error_type": error_type,
            "error_message": error_message,
            "platform": platform,
            "retry_count": retry_count,
            "context": context or {},
            "traceback": traceback_str
        }

        # ログファイル名（日付別）
        log_filename = f"error_log_{timestamp.strftime('%Y%m%d')}.jsonl"
        log_path = self.log_dir / log_filename

        # JSONLINESフォーマットで追記
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

        # コンソール出力
        self._print_error(log_entry)

        return str(log_path)

    def _print_error(self, log_entry: Dict):
        """コンソールにエラーを出力"""
        timestamp = log_entry['timestamp']
        error_type = log_entry['error_type']
        message = log_entry['error_message']
        platform = log_entry.get('platform', 'unknown')
        retry_count = log_entry.get('retry_count', 0)

        print(f"\n{'='*60}")
        print(f"❌ エラー発生: {error_type}")
        print(f"{'='*60}")
        print(f"日時: {timestamp}")
        print(f"プラットフォーム: {platform}")
        print(f"リトライ回数: {retry_count}")
        print(f"メッセージ: {message}")

        if log_entry.get('context'):
            print(f"\nコンテキスト:")
            for key, value in log_entry['context'].items():
                print(f"  - {key}: {value}")

        if log_entry.get('traceback'):
            print(f"\nトレースバック:")
            print(log_entry['traceback'])

        print(f"{'='*60}\n")

    def log_success(
        self,
        platform: str,
        post_id: str,
        scheduled_datetime: str,
        content_preview: str = None,
        retry_count: int = 0
    ) -> str:
        """
        成功ログを記録

        Args:
            platform: プラットフォーム名
            post_id: Late API Post ID
            scheduled_datetime: 予約日時
            content_preview: コンテンツプレビュー（最初の100文字）
            retry_count: リトライ回数

        Returns:
            ログファイルパス
        """
        timestamp = datetime.now(self.jst)
        log_entry = {
            "timestamp": timestamp.isoformat(),
            "status": "success",
            "platform": platform,
            "post_id": post_id,
            "scheduled_datetime": scheduled_datetime,
            "content_preview": content_preview[:100] if content_preview else None,
            "retry_count": retry_count
        }

        # 成功ログファイル名（日付別）
        log_filename = f"success_log_{timestamp.strftime('%Y%m%d')}.jsonl"
        log_path = self.log_dir / log_filename

        # JSONLINESフォーマットで追記
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

        # コンソール出力
        print(f"\n✅ {platform}投稿成功: Post ID = {post_id}")
        if retry_count > 0:
            print(f"   リトライ回数: {retry_count}")
        print(f"   予約日時: {scheduled_datetime}")

        return str(log_path)

    def get_error_statistics(self, days: int = 30) -> Dict:
        """
        過去N日間のエラー統計を取得

        Args:
            days: 集計対象日数

        Returns:
            エラー統計
        """
        error_counts = {}
        platform_errors = {"twitter": 0, "threads": 0, "unknown": 0}
        retry_stats = []

        # 過去N日分のログファイルを読み込み
        for i in range(days):
            date = datetime.now(self.jst) - timedelta(days=i)
            log_filename = f"error_log_{date.strftime('%Y%m%d')}.jsonl"
            log_path = self.log_dir / log_filename

            if not log_path.exists():
                continue

            with open(log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    entry = json.loads(line)
                    error_type = entry.get('error_type', 'Unknown')
                    platform = entry.get('platform', 'unknown')
                    retry_count = entry.get('retry_count', 0)

                    # エラー種別ごとのカウント
                    error_counts[error_type] = error_counts.get(error_type, 0) + 1

                    # プラットフォーム別のカウント
                    if platform in platform_errors:
                        platform_errors[platform] += 1
                    else:
                        platform_errors['unknown'] += 1

                    # リトライ統計
                    retry_stats.append(retry_count)

        # 統計サマリー
        total_errors = sum(error_counts.values())
        avg_retry = sum(retry_stats) / len(retry_stats) if retry_stats else 0

        return {
            "total_errors": total_errors,
            "error_counts": dict(sorted(error_counts.items(), key=lambda x: -x[1])),
            "platform_errors": platform_errors,
            "average_retry_count": round(avg_retry, 2),
            "max_retry_count": max(retry_stats) if retry_stats else 0
        }

    def get_success_rate(self, days: int = 30) -> Dict:
        """
        過去N日間の投稿成功率を取得

        Args:
            days: 集計対象日数

        Returns:
            成功率統計
        """
        from datetime import timedelta

        success_counts = {"twitter": 0, "threads": 0}
        error_counts = {"twitter": 0, "threads": 0}

        # エラーログから失敗数を集計
        for i in range(days):
            date = datetime.now(self.jst) - timedelta(days=i)
            log_filename = f"error_log_{date.strftime('%Y%m%d')}.jsonl"
            log_path = self.log_dir / log_filename

            if log_path.exists():
                with open(log_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        entry = json.loads(line)
                        platform = entry.get('platform')
                        if platform in error_counts:
                            error_counts[platform] += 1

        # 成功ログから成功数を集計
        for i in range(days):
            date = datetime.now(self.jst) - timedelta(days=i)
            log_filename = f"success_log_{date.strftime('%Y%m%d')}.jsonl"
            log_path = self.log_dir / log_filename

            if log_path.exists():
                with open(log_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        entry = json.loads(line)
                        platform = entry.get('platform')
                        if platform in success_counts:
                            success_counts[platform] += 1

        # 成功率計算
        twitter_total = success_counts['twitter'] + error_counts['twitter']
        threads_total = success_counts['threads'] + error_counts['threads']

        twitter_rate = (success_counts['twitter'] / twitter_total * 100) if twitter_total > 0 else 0
        threads_rate = (success_counts['threads'] / threads_total * 100) if threads_total > 0 else 0
        overall_rate = ((success_counts['twitter'] + success_counts['threads']) /
                       (twitter_total + threads_total) * 100) if (twitter_total + threads_total) > 0 else 0

        return {
            "period_days": days,
            "twitter": {
                "success": success_counts['twitter'],
                "failure": error_counts['twitter'],
                "success_rate": round(twitter_rate, 1)
            },
            "threads": {
                "success": success_counts['threads'],
                "failure": error_counts['threads'],
                "success_rate": round(threads_rate, 1)
            },
            "overall": {
                "success": success_counts['twitter'] + success_counts['threads'],
                "failure": error_counts['twitter'] + error_counts['threads'],
                "success_rate": round(overall_rate, 1)
            }
        }


def log_error_simple(
    error_type: str,
    error_message: str,
    platform: str = None,
    **kwargs
) -> str:
    """
    エラーログの簡易インターフェース

    Args:
        error_type: エラー種別
        error_message: エラーメッセージ
        platform: プラットフォーム名
        **kwargs: その他のパラメータ

    Returns:
        ログファイルパス

    Example:
        >>> log_error_simple(
        ...     "RateLimitError",
        ...     "Late APIレート制限超過",
        ...     platform="twitter",
        ...     retry_count=1
        ... )
    """
    logger = ErrorLogger()
    return logger.log_error(error_type, error_message, platform=platform, **kwargs)


def log_success_simple(
    platform: str,
    post_id: str,
    scheduled_datetime: str,
    **kwargs
) -> str:
    """
    成功ログの簡易インターフェース

    Example:
        >>> log_success_simple(
        ...     "twitter",
        ...     "695ceb1e8247cf816ba753b6",
        ...     "2026-01-08T20:00:00+09:00"
        ... )
    """
    logger = ErrorLogger()
    return logger.log_success(platform, post_id, scheduled_datetime, **kwargs)


if __name__ == "__main__":
    # テスト実行
    print("=" * 60)
    print("Error Logger テスト")
    print("=" * 60)

    logger = ErrorLogger()

    # テスト1: エラーログ
    print("\n[テスト1] エラーログ記録")
    logger.log_error(
        error_type="RateLimitError",
        error_message="Late APIレート制限超過",
        platform="twitter",
        retry_count=1,
        context={"input_type": "topic", "input_value": "AIの最新動向"}
    )

    # テスト2: 成功ログ
    print("\n[テスト2] 成功ログ記録")
    logger.log_success(
        platform="twitter",
        post_id="695ceb1e8247cf816ba753b6",
        scheduled_datetime="2026-01-08T20:00:00+09:00",
        content_preview="OpenAIのGPT-5.2プロンプトガイド...",
        retry_count=0
    )

    # テスト3: エラー統計
    print("\n[テスト3] エラー統計（過去30日）")
    stats = logger.get_error_statistics(days=30)
    print(json.dumps(stats, indent=2, ensure_ascii=False))

    # テスト4: 成功率
    print("\n[テスト4] 投稿成功率（過去30日）")
    success_rate = logger.get_success_rate(days=30)
    print(json.dumps(success_rate, indent=2, ensure_ascii=False))

    print("\n" + "=" * 60)
    print("✅ すべてのテストが完了しました")
    print("=" * 60)
