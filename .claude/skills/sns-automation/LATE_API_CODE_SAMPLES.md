# Late API予約投稿 - コード実装サンプル集

実装時に即座に参照できるコードスニペット集。

---

## 1. 基本的な単一投稿（即時）

```python
#!/usr/bin/env python3
"""Late API基本投稿サンプル"""

import requests
from datetime import datetime, timezone, timedelta

# 設定
API_KEY = "sk_..."  # .envから取得推奨
ACCOUNT_ID = "ln_abc123xyz"

def post_immediately(content: str):
    """即時投稿"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": content,
        "platforms": [{
            "platform": "linkedin",
            "accountId": ACCOUNT_ID
        }],
        "publishNow": True
    }

    response = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    return response.json()


# 実行例
if __name__ == "__main__":
    result = post_immediately("テスト投稿内容")
    print(f"✅ Post ID: {result.get('post', {}).get('_id')}")
```

---

## 2. 予約投稿（日時指定）

```python
#!/usr/bin/env python3
"""Late API予約投稿サンプル"""

import requests
from datetime import datetime, timezone, timedelta

API_KEY = "sk_..."
ACCOUNT_ID = "ln_abc123xyz"

def post_scheduled(content: str, scheduled_datetime: datetime):
    """指定日時に予約投稿"""

    # タイムゾーン情報がない場合は JST を付与
    if scheduled_datetime.tzinfo is None:
        jst = timezone(timedelta(hours=9))
        scheduled_datetime = scheduled_datetime.replace(tzinfo=jst)

    # ISO8601形式に変換（+09:00 付き）
    iso_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(iso_str) >= 5:
        iso_str = iso_str[:-2] + ':' + iso_str[-2:]  # +0900 → +09:00

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": content,
        "platforms": [{
            "platform": "linkedin",
            "accountId": ACCOUNT_ID
        }],
        "scheduledFor": iso_str,
        "timezone": "Asia/Tokyo"
    }

    response = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code in [200, 201]:
        print(f"✅ 予約投稿成功: {iso_str}")
        return response.json()
    else:
        print(f"❌ エラー: {response.status_code} - {response.text}")
        return None


# 実行例
if __name__ == "__main__":
    # 明日の朝8時に予約
    jst = timezone(timedelta(hours=9))
    tomorrow_8am = (datetime.now(jst) + timedelta(days=1)).replace(
        hour=8, minute=0, second=0, microsecond=0
    )

    result = post_scheduled("明日の朝8時に投稿", tomorrow_8am)
```

---

## 3. 複数案の個別投稿

```python
#!/usr/bin/env python3
"""複数案を個別に投稿するサンプル"""

import requests
from datetime import datetime, timezone, timedelta

API_KEY = "sk_..."
ACCOUNT_ID = "ln_abc123xyz"

def post_variants(variants: list, base_datetime: datetime, interval_days: int = 1):
    """
    複数案を個別に投稿

    Args:
        variants: [{"title": "案1", "content": "..."}, ...]
        base_datetime: 最初の投稿日時
        interval_days: 投稿間隔（日数）
    """
    jst = timezone(timedelta(hours=9))
    if base_datetime.tzinfo is None:
        base_datetime = base_datetime.replace(tzinfo=jst)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    results = []

    for i, variant in enumerate(variants):
        # 各案を異なる日時に投稿
        scheduled_datetime = base_datetime + timedelta(days=i * interval_days)

        # ISO8601形式に変換
        iso_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
        if len(iso_str) >= 5:
            iso_str = iso_str[:-2] + ':' + iso_str[-2:]

        payload = {
            "content": variant["content"],
            "platforms": [{
                "platform": "linkedin",
                "accountId": ACCOUNT_ID
            }],
            "scheduledFor": iso_str,
            "timezone": "Asia/Tokyo"
        }

        try:
            response = requests.post(
                "https://getlate.dev/api/v1/posts",
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code in [200, 201]:
                post_id = response.json().get("post", {}).get("_id")
                results.append({
                    "variant": variant.get("title", f"案{i+1}"),
                    "status": "success",
                    "post_id": post_id,
                    "scheduled_for": iso_str
                })
                print(f"✅ {variant.get('title', f'案{i+1}')}: {iso_str}")
            else:
                results.append({
                    "variant": variant.get("title", f"案{i+1}"),
                    "status": "error",
                    "error": response.text
                })
                print(f"❌ {variant.get('title', f'案{i+1}')}: {response.status_code}")

        except Exception as e:
            results.append({
                "variant": variant.get("title", f"案{i+1}"),
                "status": "error",
                "error": str(e)
            })
            print(f"❌ {variant.get('title', f'案{i+1}')}: {e}")

    return results


# 実行例
if __name__ == "__main__":
    variants = [
        {"title": "案1", "content": "案1の投稿内容"},
        {"title": "案2", "content": "案2の投稿内容"},
        {"title": "案3", "content": "案3の投稿内容"}
    ]

    jst = timezone(timedelta(hours=9))
    tomorrow_8am = (datetime.now(jst) + timedelta(days=1)).replace(
        hour=8, minute=0, second=0, microsecond=0
    )

    results = post_variants(variants, tomorrow_8am, interval_days=1)
```

---

## 4. X（Twitter）スレッド投稿

```python
#!/usr/bin/env python3
"""X（Twitter）スレッド投稿サンプル"""

import requests
from datetime import datetime, timezone, timedelta

API_KEY = "sk_..."
TWITTER_ACCOUNT_ID = "tw_abc123xyz"

def post_twitter_thread(thread_items: list, scheduled_datetime: datetime):
    """
    Xスレッド投稿（最大140文字×N投稿）

    Args:
        thread_items: [
            {"content": "(1/3)\\n\\n1ツイート目..."},
            {"content": "(2/3)\\n\\n2ツイート目..."},
            {"content": "(3/3)\\n\\n3ツイート目..."}
        ]
        scheduled_datetime: 予約日時
    """
    jst = timezone(timedelta(hours=9))
    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=jst)

    iso_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(iso_str) >= 5:
        iso_str = iso_str[:-2] + ':' + iso_str[-2:]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": "",  # threadItems使用時は空
        "platforms": [{
            "platform": "twitter",
            "accountId": TWITTER_ACCOUNT_ID,
            "platformSpecificData": {
                "threadItems": thread_items
            }
        }],
        "scheduledFor": iso_str,
        "timezone": "Asia/Tokyo"
    }

    response = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    return response.json() if response.status_code in [200, 201] else None


# 実行例
if __name__ == "__main__":
    thread = [
        {"content": "(1/3)\n\n最初のツイート内容..."},
        {"content": "(2/3)\n\n2番目のツイート内容..."},
        {"content": "(3/3)\n\n最後のツイート内容..."}
    ]

    jst = timezone(timedelta(hours=9))
    tomorrow_12pm = (datetime.now(jst) + timedelta(days=1)).replace(
        hour=12, minute=0, second=0, microsecond=0
    )

    result = post_twitter_thread(thread, tomorrow_12pm)
    print(f"✅ Xスレッド投稿: {result}")
```

---

## 5. Threads スレッド投稿

```python
#!/usr/bin/env python3
"""Threads スレッド投稿サンプル"""

import requests
from datetime import datetime, timezone, timedelta

API_KEY = "sk_..."
THREADS_ACCOUNT_ID = "th_abc123xyz"

def post_threads_thread(thread_items: list, scheduled_datetime: datetime):
    """
    Threadsスレッド投稿（最大500文字×N投稿）

    Args:
        thread_items: [
            {"content": "1投目（500文字以内）..."},
            {"content": "2投目（500文字以内）..."},
            {"content": "3投目（500文字以内）..."}
        ]
        scheduled_datetime: 予約日時
    """
    jst = timezone(timedelta(hours=9))
    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=jst)

    iso_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(iso_str) >= 5:
        iso_str = iso_str[:-2] + ':' + iso_str[-2:]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": "",  # threadItems使用時は空
        "platforms": [{
            "platform": "threads",
            "accountId": THREADS_ACCOUNT_ID,
            "platformSpecificData": {
                "threadItems": thread_items
            }
        }],
        "scheduledFor": iso_str,
        "timezone": "Asia/Tokyo"
    }

    response = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    return response.json() if response.status_code in [200, 201] else None


# 実行例
if __name__ == "__main__":
    thread = [
        {"content": "1投目: Threadsでのシェア内容..."},
        {"content": "2投目: 続きの内容..."},
        {"content": "3投目: 最後のまとめ..."}
    ]

    jst = timezone(timedelta(hours=9))
    tomorrow_8pm = (datetime.now(jst) + timedelta(days=1)).replace(
        hour=20, minute=0, second=0, microsecond=0
    )

    result = post_threads_thread(thread, tomorrow_8pm)
    print(f"✅ Threadsスレッド投稿: {result}")
```

---

## 6. 既存予約投稿の取得と競合回避

```python
#!/usr/bin/env python3
"""既存予約投稿を取得して競合を回避するサンプル"""

import requests
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

API_KEY = "sk_..."

def get_scheduled_posts():
    """既存の予約投稿を取得"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        "https://getlate.dev/api/v1/posts",
        headers=headers,
        params={"status": "scheduled"},
        timeout=30
    )

    return response.json().get("posts", [])


def extract_8am_reserved_dates(posts: list):
    """8:00 AM JST の予約済み日付を抽出"""
    jst = ZoneInfo('Asia/Tokyo')
    reserved_dates = set()

    for post in posts:
        scheduled_for = post.get('scheduledFor')
        if not scheduled_for:
            continue

        try:
            # ISO8601形式をパース
            dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
            dt_jst = dt.astimezone(jst)

            # 8:00 AM JST のみフィルタ
            if dt_jst.hour == 8 and dt_jst.minute == 0:
                reserved_dates.add(dt_jst.date())
        except:
            pass

    return sorted(list(reserved_dates))


def find_available_dates(count: int = 3, reserved_dates: list = None):
    """利用可能な日付を検索"""
    if reserved_dates is None:
        posts = get_scheduled_posts()
        reserved_dates = extract_8am_reserved_dates(posts)

    jst = ZoneInfo('Asia/Tokyo')
    available_dates = []
    current_date = (datetime.now(jst) + timedelta(days=1)).date()

    while len(available_dates) < count:
        if current_date not in reserved_dates:
            available_dates.append(current_date)
        current_date += timedelta(days=1)

    return available_dates


# 実行例
if __name__ == "__main__":
    print("🔍 既存予約投稿を確認中...")
    posts = get_scheduled_posts()
    print(f"   総投稿数: {len(posts)}")

    reserved_dates = extract_8am_reserved_dates(posts)
    print(f"   8:00 AM JST予約済み日付: {reserved_dates}")

    available_dates = find_available_dates(count=3, reserved_dates=reserved_dates)
    print(f"   利用可能日付: {available_dates}")
```

---

## 7. エラーハンドリング付き投稿

```python
#!/usr/bin/env python3
"""エラーハンドリング付き投稿サンプル"""

import requests
import time
from datetime import datetime, timezone, timedelta
from typing import Optional

API_KEY = "sk_..."
ACCOUNT_ID = "ln_abc123xyz"

def post_with_error_handling(
    content: str,
    scheduled_datetime: datetime,
    max_retries: int = 3
) -> Optional[dict]:
    """
    エラーハンドリング付き投稿

    Returns:
        成功時: {"post_id": str, "status": "success"}
        失敗時: {"status": "error", "error": str}
    """
    jst = timezone(timedelta(hours=9))
    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=jst)

    iso_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(iso_str) >= 5:
        iso_str = iso_str[:-2] + ':' + iso_str[-2:]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": content,
        "platforms": [{
            "platform": "linkedin",
            "accountId": ACCOUNT_ID
        }],
        "scheduledFor": iso_str,
        "timezone": "Asia/Tokyo"
    }

    for attempt in range(max_retries):
        try:
            print(f"📤 投稿試行 ({attempt + 1}/{max_retries})...")

            response = requests.post(
                "https://getlate.dev/api/v1/posts",
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code in [200, 201]:
                post_id = response.json().get("post", {}).get("_id")
                print(f"✅ 投稿成功: {post_id}")
                return {"post_id": post_id, "status": "success"}

            elif response.status_code == 401:
                # 認証エラー：リトライなし
                print("❌ 認証エラー (401)")
                print("   API Keyを確認してください")
                return {"status": "error", "error": "Authentication failed"}

            elif response.status_code == 429:
                # レート制限：1時間待機
                print("⏳ レート制限超過 (429)")
                print("   1時間待機します...")
                time.sleep(3600)
                continue

            elif response.status_code == 400:
                # リクエストエラー：リトライなし
                print(f"❌ リクエストエラー (400)")
                print(f"   詳細: {response.text}")
                return {"status": "error", "error": response.text}

            elif response.status_code >= 500:
                # サーバーエラー：指数バックオフでリトライ
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # 1, 2, 4秒
                    print(f"⏳ サーバーエラー ({response.status_code})")
                    print(f"   {wait_time}秒後に再試行...")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"❌ サーバーエラー (最大リトライ回数に達成)")
                    return {"status": "error", "error": f"Server error {response.status_code}"}

        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"⏳ タイムアウト - {wait_time}秒後に再試行...")
                time.sleep(wait_time)
            else:
                print("❌ タイムアウト (最大リトライ回数に達成)")
                return {"status": "error", "error": "Timeout"}

        except requests.exceptions.ConnectionError:
            print("❌ 接続エラー")
            return {"status": "error", "error": "Connection error"}

        except Exception as e:
            print(f"❌ 予期しないエラー: {e}")
            return {"status": "error", "error": str(e)}

    return {"status": "error", "error": "Max retries exceeded"}


# 実行例
if __name__ == "__main__":
    jst = timezone(timedelta(hours=9))
    tomorrow_8am = (datetime.now(jst) + timedelta(days=1)).replace(
        hour=8, minute=0, second=0, microsecond=0
    )

    result = post_with_error_handling("テスト投稿", tomorrow_8am)
    print(result)
```

---

## 8. 環境変数の読み込みと設定

```python
#!/usr/bin/env python3
"""環境変数読み込みサンプル"""

import os
from pathlib import Path
from typing import Dict

def load_env_vars(env_file_path: str = None) -> Dict[str, str]:
    """
    .envファイルから環境変数を読み込み（インラインコメント対応）

    重要: インラインコメント（VAR="value"  # comment）に対応
    """
    if env_file_path is None:
        env_file_path = Path(__file__).parent.parent / ".env"
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
                        break
                    clean_value.append(ch)

                value = "".join(clean_value)

            # クォート除去
            value = value.strip().strip('"').strip("'")
            env_vars[key.strip()] = value

    return env_vars


# 実行例
if __name__ == "__main__":
    env_vars = load_env_vars()

    api_key = env_vars.get("LATE_API_KEY")
    linkedin_account_id = env_vars.get("LATE_LINKEDIN_ACCOUNT_ID")

    print(f"✅ 環境変数読み込み成功")
    print(f"   API Key: {api_key[:20]}...")
    print(f"   LinkedIn ID: {linkedin_account_id}")
```

---

## 9. JSON出力例

### 成功時のレスポンス

```json
{
  "post": {
    "_id": "6789abcd1234567890abcdef",
    "content": "投稿内容",
    "platform": "linkedin",
    "accountId": "ln_abc123xyz",
    "scheduledFor": "2026-01-07T08:00:00+09:00",
    "status": "scheduled"
  }
}
```

### 予約投稿リスト取得時のレスポンス

```json
{
  "posts": [
    {
      "_id": "post_id_1",
      "content": "案1の投稿内容",
      "platform": "linkedin",
      "scheduledFor": "2026-01-07T08:00:00+09:00",
      "status": "scheduled"
    },
    {
      "_id": "post_id_2",
      "content": "案2の投稿内容",
      "platform": "linkedin",
      "scheduledFor": "2026-01-08T08:00:00+09:00",
      "status": "scheduled"
    }
  ]
}
```

---

## 10. テストスクリプト

```python
#!/usr/bin/env python3
"""Late API統合テストスクリプト"""

import sys
from pathlib import Path

# パスを設定
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "scripts"))

from late_api_utils import (
    load_env_vars,
    get_late_api_config,
    format_datetime_for_late_api
)

def test_all():
    """全テストを実行"""
    print("=" * 60)
    print("Late API統合テスト")
    print("=" * 60)
    print()

    # テスト1: 環境変数読み込み
    print("1. 環境変数読み込みテスト")
    try:
        env_vars = load_env_vars()
        print(f"   ✅ 成功: {len(env_vars)} 件読み込み")
        print(f"   LATE_API_KEY: {env_vars.get('LATE_API_KEY', 'NOT FOUND')[:20]}...")
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
    print()

    # テスト2: Late API設定
    print("2. Late API設定取得テスト")
    try:
        config = get_late_api_config()
        print(f"   ✅ 成功")
        print(f"   base_url: {config['base_url']}")
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
    print()

    # テスト3: 日時フォーマット
    print("3. 日時フォーマットテスト")
    from datetime import datetime, timezone, timedelta
    jst = timezone(timedelta(hours=9))
    test_dt = datetime(2026, 1, 7, 8, 0, 0, tzinfo=jst)
    formatted = format_datetime_for_late_api(test_dt)
    expected = "2026-01-07T08:00:00+09:00"
    if formatted == expected:
        print(f"   ✅ 成功: {formatted}")
    else:
        print(f"   ❌ 失敗: 期待値={expected}, 実際={formatted}")
    print()

    print("=" * 60)
    print("テスト完了")
    print("=" * 60)


if __name__ == "__main__":
    test_all()
```

---

**最終更新**: 2026-01-06
**バージョン**: 1.0
