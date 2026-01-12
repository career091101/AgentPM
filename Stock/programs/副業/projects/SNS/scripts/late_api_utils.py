#!/usr/bin/env python3
"""
Late API共通ユーティリティ関数

再発防止のため、以下の問題に対処：
1. 環境変数のインラインコメント処理
2. 正しいAPIエンドポイント（https://getlate.dev/api/v1）
3. 正しいリクエストボディ形式（platforms配列）

Usage:
    from late_api_utils import load_env_vars, post_to_late_api
"""

import os
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Dict, Optional
import requests


def load_env_vars(env_file_path: str = None) -> Dict[str, str]:
    """
    .envファイルから環境変数を読み込み（インラインコメント対応）

    Args:
        env_file_path: .envファイルパス（デフォルト: プロジェクトルート/.env）

    Returns:
        dict: 環境変数の辞書

    注意:
        - インラインコメント（例: VAR="value"  # comment）を正しく処理
        - クォート内の # はコメントとして扱わない
    """
    if env_file_path is None:
        project_root = Path(__file__).parent.parent
        env_file_path = project_root / ".env"
    else:
        env_file_path = Path(env_file_path)

    env_vars = {}

    if not env_file_path.exists():
        raise FileNotFoundError(f".env file not found: {env_file_path}")

    with open(env_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)

            # インラインコメント除去（クォート外の # 以降を削除）
            if "#" in value:
                in_quote = False
                quote_char = None
                clean_value = []

                for ch in value:
                    if ch in ['"', "'"]:
                        if not in_quote:
                            in_quote = True
                            quote_char = ch
                        elif ch == quote_char:
                            in_quote = False
                            quote_char = None
                    elif ch == "#" and not in_quote:
                        # クォート外の # 以降は切り捨て
                        break
                    clean_value.append(ch)

                value = "".join(clean_value)

            # クォート除去
            value = value.strip().strip('"').strip("'")
            env_vars[key.strip()] = value

    return env_vars


def get_late_api_config(env_vars: Dict[str, str] = None) -> Dict[str, str]:
    """
    Late API設定を取得

    Args:
        env_vars: 環境変数辞書（省略時は自動読み込み）

    Returns:
        dict: {
            "api_key": str,
            "base_url": str,  # https://getlate.dev/api/v1
            "linkedin_account_id": str,
            "twitter_account_id": str,
            "threads_account_id": str
        }

    Raises:
        ValueError: 必須の環境変数が見つからない場合
    """
    if env_vars is None:
        env_vars = load_env_vars()

    api_key = env_vars.get("LATE_API_KEY")
    if not api_key:
        raise ValueError("LATE_API_KEY not found in .env file")

    # 正しいエンドポイント（2026-01-05確認済み）
    base_url = "https://getlate.dev/api/v1"

    return {
        "api_key": api_key,
        "base_url": base_url,
        "linkedin_account_id": env_vars.get("LATE_LINKEDIN_ACCOUNT_ID", ""),
        "twitter_account_id": env_vars.get("LATE_TWITTER_ACCOUNT_ID", ""),
        "threads_account_id": env_vars.get("LATE_THREADS_ACCOUNT_ID", "")
    }


def format_datetime_for_late_api(dt: datetime) -> str:
    """
    datetimeをLate API形式に変換

    Args:
        dt: datetime（タイムゾーン付き）

    Returns:
        str: ISO8601形式（例: "2026-01-07T08:00:00+09:00"）

    注意:
        - Late APIは "+09:00" 形式を要求（"+0900" ではない）
    """
    # JSTタイムゾーン確認
    JST = timezone(timedelta(hours=9))

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=JST)

    # ISO8601形式に変換
    dt_str = dt.strftime("%Y-%m-%dT%H:%M:%S%z")

    # %z は +0900 形式なので、コロン挿入して +09:00 にする
    if len(dt_str) >= 5:
        dt_str = dt_str[:-2] + ':' + dt_str[-2:]

    return dt_str


def post_to_late_api(
    content: str,
    platform: str,
    account_id: str,
    scheduled_datetime: datetime,
    config: Dict[str, str] = None
) -> Dict:
    """
    Late APIに投稿（正しいスキーマ版）

    Args:
        content: 投稿本文
        platform: プラットフォーム名（linkedin, twitter, threads）
        account_id: アカウントID
        scheduled_datetime: 予約日時（JST）
        config: Late API設定（省略時は自動取得）

    Returns:
        dict: Late APIレスポンス

    Raises:
        Exception: API呼び出し失敗時

    注意:
        - リクエストボディは platforms配列形式
        - scheduledFor は ISO8601形式（+09:00付き）
    """
    if config is None:
        config = get_late_api_config()

    api_key = config["api_key"]
    base_url = config["base_url"]

    # ISO8601形式に変換
    scheduled_datetime_str = format_datetime_for_late_api(scheduled_datetime)

    # リクエストボディ（正しいスキーマ）
    payload = {
        "content": content,
        "platforms": [
            {
                "platform": platform,
                "accountId": account_id
            }
        ],
        "scheduledFor": scheduled_datetime_str,
        "timezone": "Asia/Tokyo"
    }

    # API呼び出し
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{base_url}/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    # エラーハンドリング
    if response.status_code not in [200, 201]:
        error_msg = f"Late API Error: {response.status_code} - {response.text}"
        raise Exception(error_msg)

    return response.json()


def post_multiple_variants_to_late_api(
    variants: list,
    platform: str,
    account_id: str,
    base_datetime: datetime,
    interval_days: int = 1,
    config: Dict[str, str] = None
) -> list:
    """
    複数バリアントを個別に投稿

    Args:
        variants: バリアントリスト（各要素は {"content": str, "title": str}）
        platform: プラットフォーム名
        account_id: アカウントID
        base_datetime: 基準日時（最初の投稿日時）
        interval_days: 投稿間隔（日数）
        config: Late API設定

    Returns:
        list: 投稿結果リスト（各要素は {"status": "success"|"error", "post_id": str, ...}）

    注意:
        - 各バリアントは確実に個別POSTリクエストで送信
    """
    if config is None:
        config = get_late_api_config()

    results = []

    for i, variant in enumerate(variants):
        scheduled_datetime = base_datetime + timedelta(days=i * interval_days)
        content = variant["content"]

        try:
            result = post_to_late_api(
                content=content,
                platform=platform,
                account_id=account_id,
                scheduled_datetime=scheduled_datetime,
                config=config
            )

            post_id = result.get("post", {}).get("_id") or result.get("id")

            results.append({
                "variant": f"案{i+1}",
                "status": "success",
                "post_id": post_id,
                "scheduled_for": scheduled_datetime.isoformat(),
                "platform": platform,
                "title": variant.get("title", "")
            })

        except Exception as e:
            results.append({
                "variant": f"案{i+1}",
                "status": "error",
                "error_message": str(e),
                "scheduled_for": scheduled_datetime.isoformat(),
                "platform": platform
            })

    return results


if __name__ == "__main__":
    # テスト実行
    print("=" * 60)
    print("Late API共通ユーティリティ - テスト実行")
    print("=" * 60)
    print()

    # 1. 環境変数読み込みテスト
    print("1. 環境変数読み込みテスト")
    try:
        env_vars = load_env_vars()
        print(f"   ✅ 成功: {len(env_vars)} 件の環境変数を読み込みました")
        print(f"   LATE_API_KEY: {env_vars.get('LATE_API_KEY', 'NOT FOUND')[:20]}...")
        print(f"   LATE_LINKEDIN_ACCOUNT_ID: {env_vars.get('LATE_LINKEDIN_ACCOUNT_ID', 'NOT FOUND')}")
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
    print()

    # 2. Late API設定取得テスト
    print("2. Late API設定取得テスト")
    try:
        config = get_late_api_config()
        print(f"   ✅ 成功")
        print(f"   base_url: {config['base_url']}")
        print(f"   linkedin_account_id: {config['linkedin_account_id']}")
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
    print()

    # 3. 日時フォーマットテスト
    print("3. 日時フォーマットテスト")
    JST = timezone(timedelta(hours=9))
    test_datetime = datetime(2026, 1, 7, 8, 0, 0, tzinfo=JST)
    formatted = format_datetime_for_late_api(test_datetime)
    print(f"   入力: {test_datetime}")
    print(f"   出力: {formatted}")
    print(f"   期待値: 2026-01-07T08:00:00+09:00")
    if formatted == "2026-01-07T08:00:00+09:00":
        print("   ✅ 正しくフォーマットされました")
    else:
        print("   ❌ フォーマットが異なります")

    print()
    print("=" * 60)
