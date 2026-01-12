# Late API予約投稿実装ガイド

日本時間（JST）タイムゾーン対応の Late API 予約投稿機能の完全実装ガイド。

---

## 1. 予約投稿の基本概念

### エンドポイント

```
POST https://getlate.dev/api/v1/posts
```

### 必須フィールド

| フィールド | 説明 | 形式 | 例 |
|-----------|------|------|-----|
| `content` | 投稿内容 | String | `"投稿本文"` |
| `platforms` | 対象プラットフォーム | Array | `[{"platform": "linkedin", "accountId": "..."}]` |
| `scheduledFor` | 予約日時 | ISO8601 | `"2026-01-07T08:00:00+09:00"` |
| `timezone` | タイムゾーン | String | `"Asia/Tokyo"` |

### 即時投稿時の変更

即時投稿の場合、`scheduledFor` と `timezone` の代わりに以下を使用：

```json
{
  "content": "投稿内容",
  "platforms": [...],
  "publishNow": true
}
```

---

## 2. リクエスト形式（完全サンプル）

### 2.1 LinkedIn単一投稿（予約）

```python
import requests
from datetime import datetime, timezone, timedelta

# 予約日時の設定（JST）
jst = timezone(timedelta(hours=9))
scheduled_time = datetime(2026, 1, 7, 8, 0, 0, tzinfo=jst)

# ISO8601形式に変換
scheduled_datetime_str = scheduled_time.isoformat()
# 出力例: "2026-01-07T08:00:00+09:00"

# リクエストボディ
payload = {
    "content": "投稿内容テキスト",
    "platforms": [
        {
            "platform": "linkedin",
            "accountId": "ln_abc123xyz"  # Late API設定から取得
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
    "https://getlate.dev/api/v1/posts",
    headers=headers,
    json=payload,
    timeout=30
)

if response.status_code in [200, 201]:
    print("✅ 予約投稿成功")
    post_id = response.json().get("post", {}).get("_id") or response.json().get("id")
    print(f"Post ID: {post_id}")
else:
    print(f"❌ エラー: {response.status_code} - {response.text}")
```

### 2.2 X（Twitter）スレッド投稿（予約）

```python
# X スレッド投稿（最大140文字×N投稿）
thread_items = [
    {"content": "(1/3)\n\n最初のツイート"},
    {"content": "(2/3)\n\n2番目のツイート"},
    {"content": "(3/3)\n\n最後のツイート"}
]

payload = {
    "content": "",  # threadItems使用時は空
    "platforms": [
        {
            "platform": "twitter",
            "accountId": "tw_abc123xyz",
            "platformSpecificData": {
                "threadItems": thread_items
            }
        }
    ],
    "scheduledFor": "2026-01-07T12:00:00+09:00",
    "timezone": "Asia/Tokyo"
}
```

### 2.3 Threads スレッド投稿（予約）

```python
# Threads スレッド投稿（最大500文字×N投稿）
thread_items = [
    {"content": "1投目（500文字以内）..."},
    {"content": "2投目（500文字以内）..."},
    {"content": "3投目（500文字以内）..."}
]

payload = {
    "content": "",  # threadItems使用時は空
    "platforms": [
        {
            "platform": "threads",
            "accountId": "th_abc123xyz",
            "platformSpecificData": {
                "threadItems": thread_items
            }
        }
    ],
    "scheduledFor": "2026-01-07T20:00:00+09:00",
    "timezone": "Asia/Tokyo"
}
```

### 2.4 複数プラットフォーム同時投稿

```python
# LinkedIn + X + Threads に同時投稿（同じ内容）
payload = {
    "content": "各プラットフォーム共通の投稿内容",
    "platforms": [
        {
            "platform": "linkedin",
            "accountId": "ln_abc123xyz"
        },
        {
            "platform": "twitter",
            "accountId": "tw_abc123xyz"
        },
        {
            "platform": "threads",
            "accountId": "th_abc123xyz"
        }
    ],
    "scheduledFor": "2026-01-07T18:00:00+09:00",
    "timezone": "Asia/Tokyo"
}
```

---

## 3. 日時指定のフォーマット（JSTタイムゾーン処理）

### 3.1 正しい形式

```python
from datetime import datetime, timezone, timedelta

# 方法1: zoneinfo（推奨、Python 3.9+）
from zoneinfo import ZoneInfo

jst = ZoneInfo('Asia/Tokyo')
dt = datetime(2026, 1, 7, 8, 0, 0, tzinfo=jst)
iso_str = dt.isoformat()  # "2026-01-07T08:00:00+09:00"
```

```python
# 方法2: timezone + timedelta（Python 3.6+互換）
jst = timezone(timedelta(hours=9))
dt = datetime(2026, 1, 7, 8, 0, 0, tzinfo=jst)

# ISO8601形式に変換
iso_str = dt.strftime("%Y-%m-%dT%H:%M:%S%z")  # "2026-01-07T08:00:00+0900"

# Late APIは "+09:00" 形式を要求（+0900ではない）
# コロンを挿入して修正
if len(iso_str) >= 5:
    iso_str = iso_str[:-2] + ':' + iso_str[-2:]  # "2026-01-07T08:00:00+09:00"
```

### 3.2 よくあるエラーと修正

| エラー | 原因 | 修正 |
|--------|------|------|
| `+0900` | `%z` フォーマットの出力 | コロン挿入: `+09:00` |
| `2026-01-07T08:00:00Z` | UTC 形式 | JST に変換: `+09:00` を使用 |
| `2026-01-07T08:00:00` | タイムゾーン情報なし | `+09:00` を付与 |
| `08:00 PM` | 12時間形式 | 24時間形式に変換 |

### 3.3 現在時刻からの相対指定

```python
from datetime import datetime, timedelta, timezone

jst = timezone(timedelta(hours=9))

# 明日の朝8時に予約
tomorrow_8am = (datetime.now(jst) + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
scheduled_for = tomorrow_8am.isoformat()

# 3日後の夜20時に予約
three_days_later_8pm = (datetime.now(jst) + timedelta(days=3)).replace(hour=20, minute=0, second=0, microsecond=0)
scheduled_for = three_days_later_8pm.isoformat()
```

---

## 4. 既存予約投稿の取得方法

### 4.1 全ステータスの予約を取得

```python
import requests

api_key = "sk_..."  # Late API Key
base_url = "https://getlate.dev/api/v1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 予約済み投稿を取得
response = requests.get(
    f"{base_url}/posts",
    headers=headers,
    params={"status": "scheduled"},
    timeout=30
)

if response.status_code == 200:
    posts = response.json().get("posts", [])
    for post in posts:
        print(f"Post ID: {post.get('_id')}")
        print(f"Scheduled For: {post.get('scheduledFor')}")
        print(f"Platform: {post.get('platform')}")
        print()
else:
    print(f"❌ エラー: {response.status_code} - {response.text}")
```

### 4.2 特定プラットフォームの予約を取得

```python
# LinkedIn の予約投稿のみ取得
response = requests.get(
    f"{base_url}/posts",
    headers=headers,
    params={
        "status": "scheduled",
        "platform": "linkedin"
    },
    timeout=30
)
```

### 4.3 8:00 AM JST の予約済み日付を抽出（競合回避）

```python
from datetime import datetime
from zoneinfo import ZoneInfo

jst = ZoneInfo('Asia/Tokyo')
reserved_8am_dates = set()

for post in posts:
    scheduled_for = post.get('scheduledFor')
    if scheduled_for:
        # ISO8601形式をパース
        dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
        dt_jst = dt.astimezone(jst)

        # 8:00 AM JST のみフィルタ
        if dt_jst.hour == 8 and dt_jst.minute == 0:
            reserved_8am_dates.add(dt_jst.date())

print(f"8:00 AM JST の予約済み日付: {sorted(reserved_8am_dates)}")
```

### 4.4 利用可能な日付を検索（競合回避）

```python
from datetime import datetime, timedelta

jst = ZoneInfo('Asia/Tokyo')
available_dates = []
current_date = (datetime.now(jst) + timedelta(days=1)).date()

# 予約なしの3日分を検索
while len(available_dates) < 3:
    if current_date not in reserved_8am_dates:
        available_dates.append(current_date)
    current_date += timedelta(days=1)

print(f"利用可能日付: {available_dates}")
# 出力例: [datetime.date(2026, 1, 7), datetime.date(2026, 1, 8), datetime.date(2026, 1, 9)]
```

---

## 5. X・Threads両方への予約投稿

### 5.1 異なるコンテンツで投稿

```python
# X: 140文字制限、スレッド形式
x_payload = {
    "content": "",
    "platforms": [{
        "platform": "twitter",
        "accountId": "tw_abc123xyz",
        "platformSpecificData": {
            "threadItems": [
                {"content": "(1/5)\n\nツイート内容..."},
                {"content": "(2/5)\n\n..."}
            ]
        }
    }],
    "scheduledFor": "2026-01-07T12:00:00+09:00",
    "timezone": "Asia/Tokyo"
}

# Threads: 500文字制限、スレッド形式
threads_payload = {
    "content": "",
    "platforms": [{
        "platform": "threads",
        "accountId": "th_abc123xyz",
        "platformSpecificData": {
            "threadItems": [
                {"content": "Threads投稿1（500文字以内）..."},
                {"content": "Threads投稿2..."}
            ]
        }
    }],
    "scheduledFor": "2026-01-07T20:00:00+09:00",
    "timezone": "Asia/Tokyo"
}

# 2つの別々のリクエストで投稿
requests.post(f"{base_url}/posts", headers=headers, json=x_payload)
requests.post(f"{base_url}/posts", headers=headers, json=threads_payload)
```

### 5.2 同じコンテンツで複数プラットフォーム投稿

```python
# 同じ内容を複数プラットフォームに投稿
payload = {
    "content": "共通の投稿内容",
    "platforms": [
        {
            "platform": "twitter",
            "accountId": "tw_abc123xyz"
        },
        {
            "platform": "threads",
            "accountId": "th_abc123xyz"
        }
    ],
    "scheduledFor": "2026-01-07T18:00:00+09:00",
    "timezone": "Asia/Tokyo"
}

response = requests.post(f"{base_url}/posts", headers=headers, json=payload)
```

---

## 6. エラーハンドリング・リトライ実装例

### 6.1 エラーコード別の対応

```python
def handle_late_api_error(status_code, response_text):
    """Late APIエラーを処理"""

    if status_code == 401:
        # 認証エラー
        print("❌ 401 Unauthorized")
        print("   原因: API Keyが無効または期限切れ")
        print("   対応: Late APIダッシュボードで確認")
        return "SKIP"  # リトライなし

    elif status_code == 429:
        # レート制限超過
        print("❌ 429 Rate Limit Exceeded")
        print("   原因: リクエスト数超過（Proプラン: 300リクエスト/分）")
        print("   対応: 1時間待機後に1回リトライ")
        return "RETRY_AFTER_1HOUR"

    elif status_code == 400:
        # リクエストエラー
        print("❌ 400 Bad Request")
        print(f"   原因: パラメータ不正")
        print(f"   詳細: {response_text}")
        return "SKIP"  # リトライなし

    elif status_code >= 500:
        # サーバーエラー
        print(f"❌ {status_code} Server Error")
        print("   原因: Late APIサーバーに問題")
        print("   対応: 3回リトライ")
        return "RETRY_3TIMES"

    else:
        # その他のエラー
        print(f"❌ {status_code} Unknown Error")
        return "SKIP"
```

### 6.2 リトライロジック

```python
import time
from typing import Optional

def post_with_retry(
    payload: dict,
    api_key: str,
    max_retries: int = 3,
    timeout: int = 30
) -> Optional[dict]:
    """リトライ機能付きのLate API投稿"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    base_url = "https://getlate.dev/api/v1"

    for attempt in range(max_retries):
        try:
            print(f"📤 投稿試行 ({attempt + 1}/{max_retries})...")

            response = requests.post(
                f"{base_url}/posts",
                headers=headers,
                json=payload,
                timeout=timeout
            )

            if response.status_code in [200, 201]:
                print("✅ 投稿成功")
                return response.json()

            elif response.status_code == 401:
                # 認証エラーはリトライしない
                print("❌ 認証エラー - スキップ")
                return None

            elif response.status_code == 429:
                # レート制限は1時間待機
                print("⏳ レート制限超過 - 1時間待機")
                time.sleep(3600)  # 1時間
                continue

            elif response.status_code == 400:
                # リクエストエラーはリトライしない
                print(f"❌ リクエストエラー - {response.text}")
                return None

            elif response.status_code >= 500 and attempt < max_retries - 1:
                # サーバーエラーは指数バックオフでリトライ
                wait_time = 2 ** attempt  # 1秒、2秒、4秒
                print(f"⏳ サーバーエラー - {wait_time}秒後に再試行")
                time.sleep(wait_time)
                continue

            else:
                # その他のエラー
                print(f"❌ エラー: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                print(f"⏳ タイムアウト - {2 ** attempt}秒後に再試行")
                time.sleep(2 ** attempt)
            else:
                print("❌ タイムアウト - スキップ")
                return None

        except requests.exceptions.ConnectionError:
            print("❌ 接続エラー - スキップ")
            return None

        except Exception as e:
            print(f"❌ 予期しないエラー: {e}")
            return None

    print("❌ 最大リトライ回数に達しました")
    return None
```

---

## 7. スレッド投稿の実装例

### 7.1 X スレッド分割アルゴリズム

```python
def split_for_twitter(content: str, max_length: int = 140) -> list:
    """
    X（Twitter）用スレッド分割

    分割優先順位:
    1. 段落分割（\\n\\n）
    2. 句点分割（。）
    3. 読点分割（、）
    4. 強制分割（最終手段）

    返り値: 番号付きツイート配列 ["(1/N) ツイート1", "(2/N) ツイート2", ...]
    """
    # 実装詳細は late_api_utils.py の split_for_twitter() 参照
    pass
```

### 7.2 Threads スレッド分割アルゴリズム

```python
def split_for_threads(content: str, max_length: int = 500) -> list:
    """
    Threads用スレッド分割

    要件: 500文字×3投稿に自動調整
    分割優先順位:
    1. セクション区切り（━━━）
    2. 段落分割（\\n\\n）
    3. 句点分割（。）
    4. 強制分割（最終手段）

    返り値: 3投稿の配列 ["投稿1", "投稿2", "投稿3"]
    """
    # 実装詳細は late_api_utils.py の split_for_threads() 参照
    pass
```

---

## 8. 実装チェックリスト

Late API予約投稿を実装する際の確認項目：

### 基本設定
- [ ] Late API Key を `.env` に保存（インラインコメント禁止）
- [ ] アカウントID（LinkedIn, X, Threads等）を `.env` に保存
- [ ] `config/late_api_config.json` に accountId を設定
- [ ] エンドポイント: `https://getlate.dev/api/v1/posts`

### リクエスト形式
- [ ] `content` フィールドを指定（threadItems がない場合）
- [ ] `platforms` は配列形式（必須）
- [ ] `scheduledFor` はISO8601形式（`+09:00` 付き）
- [ ] `timezone` は `"Asia/Tokyo"` に統一
- [ ] スレッド投稿は `platformSpecificData` → `threadItems` で指定

### 日時処理
- [ ] タイムゾーン: `ZoneInfo('Asia/Tokyo')` または `timezone(timedelta(hours=9))`
- [ ] ISO8601フォーマット: `strftime("%Y-%m-%dT%H:%M:%S%z")` → コロン挿入
- [ ] タイムゾーン情報必須: `+09:00` 形式で送信

### エラーハンドリング
- [ ] 401 エラー: API設定を確認、リトライなし
- [ ] 429 エラー: 1時間待機、1回リトライ
- [ ] 400 エラー: パラメータ確認、リトライなし
- [ ] 5xx エラー: 指数バックオフで3回リトライ

### 競合回避（複数案投稿時）
- [ ] `get_existing_scheduled_posts()` で既存予約を取得
- [ ] 8:00 AM JST の予約済み日付を抽出
- [ ] `find_available_dates()` で利用可能日付を検索
- [ ] 各案を個別の POST リクエストで送信（1リクエスト1投稿）

---

## 9. 実装ファイルリファレンス

### 提供されている実装

| ファイル | 用途 | 関数 |
|---------|------|------|
| `scripts/late_api_utils.py` | 共通ユーティリティ | `load_env_vars()`, `post_to_late_api()`, `get_existing_scheduled_posts()`, `find_available_dates()` |
| `scripts/late_api_post.py` | 基本実装ライブラリ | `split_for_twitter()`, `split_for_threads()`, `post_to_twitter_thread()`, `post_to_threads_thread()`, `calculate_schedule()` |
| `scripts/late_api_multi_post_v2.py` | 複数案の個別投稿 | 3案の抽出→投稿→結果保存を自動実行 |

### 利用例

```python
# パターン1: 共通ユーティリティの使用
from late_api_utils import post_multiple_variants_to_late_api

variants = [
    {"content": "案1の内容", "title": "案1"},
    {"content": "案2の内容", "title": "案2"},
    {"content": "案3の内容", "title": "案3"}
]

results = post_multiple_variants_to_late_api(
    variants=variants,
    platform="linkedin",
    account_id="ln_abc123xyz",
    base_datetime=datetime.now(timezone(timedelta(hours=9)))
)
```

```python
# パターン2: 基本ライブラリの使用
from late_api_utils import post_to_late_api

post_to_late_api(
    content="単一投稿内容",
    platform="linkedin",
    account_id="ln_abc123xyz",
    scheduled_datetime=datetime(2026, 1, 7, 8, 0, 0, tzinfo=timezone(timedelta(hours=9)))
)
```

---

## 10. よくあるエラーと修正方法

### エラー: 500 Internal Server Error（アカウントID不正）

**原因**: `.env` ファイルのインラインコメント

```bash
# 誤り
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"  # 優一 佐藤
```

**修正**: コメントを別行に

```bash
# LinkedIn: 優一 佐藤
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"
```

### エラー: 400 Bad Request（スレッド投稿）

**原因**: `content` フィールドが設定されている

```python
# 誤り
payload = {
    "content": "投稿内容",  # threadItems と content の同時使用は禁止
    "platformSpecificData": {"threadItems": [...]}
}

# 修正
payload = {
    "content": "",  # threadItems 使用時は空
    "platformSpecificData": {"threadItems": [...]}
}
```

### エラー: タイムゾーン形式不正

**原因**: `+0900` 形式（コロンなし）

```python
# 誤り
"scheduledFor": "2026-01-07T08:00:00+0900"

# 修正
"scheduledFor": "2026-01-07T08:00:00+09:00"
```

---

## 11. パフォーマンス最適化

### バッチ投稿時の注意

```python
# 複数投稿を順序的に実行する場合
for variant in variants:
    result = post_to_late_api(variant["content"], ...)

    # Late APIのレート制限: 300リクエスト/分
    # 安全のため最低1秒間隔
    time.sleep(1)
```

### 並列投稿の推奨制限

- **同時リクエスト数**: 最大5並列
- **リクエスト間隔**: 最低1秒
- **1時間あたりの上限**: 300リクエスト（Proプラン）

---

## 12. 参考資料

### 関連ドキュメント

- Late API設定ガイド: `config/LATE_API_SETUP_GUIDE.md`
- 統合詳細ガイド: `.claude/skills/sns-automation/late_api_integration_guide.md`
- 修正記録: `docs/LATE_API_MULTI_POST_FIX.md`

### Late API公式リソース

- 公式ドキュメント: https://docs.getlate.dev/
- ダッシュボード: https://app.getlate.dev/
- APIリファレンス: https://docs.getlate.dev/api/posts

---

**最終更新**: 2026-01-06
**バージョン**: 1.0
**ステータス**: 実装検証済み
