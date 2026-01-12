# Late API予約投稿 - 注意点・制約事項・ベストプラクティス

Late API統合時に必ず確認すべき制限事項と実装上の注意点。

---

## 1. API制限事項

### 1.1 レート制限

| プラン | リクエスト数 | 期間 |
|--------|------------|------|
| **Proプラン**（推奨） | 300 | 1分間 |
| **Basicプラン** | 30 | 1分間 |

**実装時の対応**:

```python
# 複数投稿時は最低1秒間隔を空ける
import time

for variant in variants:
    post_to_late_api(variant)
    time.sleep(1)  # 安全のため1秒待機
```

### 1.2 タイムアウト設定

- **接続タイムアウト**: 30秒
- **読み取りタイムアウト**: 30秒
- **推奨**: `timeout=30` を明示的に指定

```python
response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=30  # 必須
)
```

### 1.3 リクエストサイズ制限

- **最大コンテンツ長**: プラットフォーム依存
  - LinkedIn: 3,000文字
  - X（Twitter）: 140文字/ツイート
  - Threads: 500文字/投稿
  - Facebook: 63,206文字

---

## 2. 日時・タイムゾーン制約

### 2.1 タイムゾーン形式

| 形式 | 例 | 状態 |
|------|-----|------|
| `+09:00` | `2026-01-07T08:00:00+09:00` | ✅ 正しい |
| `+0900` | `2026-01-07T08:00:00+0900` | ❌ 不正 |
| `JST` | `2026-01-07T08:00:00JST` | ❌ 不正 |
| `Z` | `2026-01-07T08:00:00Z` | ⚠️ UTC（+09:00を使用） |

**修正コード**:

```python
# 間違い
dt_str = "2026-01-07T08:00:00+0900"

# 正しい
dt_str = "2026-01-07T08:00:00+09:00"
```

### 2.2 予約可能な日時範囲

- **最小**: 現在時刻より1時間以上先
- **最大**: 制限なし（ただし1年以上先はテスト不十分）
- **推奨**: 1-365日以内

```python
from datetime import datetime, timedelta, timezone

jst = timezone(timedelta(hours=9))
now = datetime.now(jst)

# NG: 1時間以内
scheduled_too_soon = now + timedelta(minutes=30)

# OK: 1時間以上先
scheduled_ok = now + timedelta(hours=1)

# OK: 数日先
scheduled_better = now + timedelta(days=1)
```

### 2.3 日付変更線を越える投稿

UTCと JST の日付ずれに注意：

```python
from datetime import datetime, timezone, timedelta

jst = timezone(timedelta(hours=9))

# 2026-01-07 08:00 JST = 2026-01-06 23:00 UTC
dt_jst = datetime(2026, 1, 7, 8, 0, 0, tzinfo=jst)
dt_utc = dt_jst.astimezone(timezone.utc)

print(f"JST: {dt_jst}")  # 2026-01-07 08:00:00+09:00
print(f"UTC: {dt_utc}")  # 2026-01-06 23:00:00+00:00
```

---

## 3. プラットフォーム別制約

### 3.1 LinkedIn

**制限**:
- 最大3,000文字/投稿
- スレッド機能なし（単一投稿のみ）
- 予約投稿の最大数: 無制限

**実装時の注意**:

```python
# OK
payload = {
    "content": "投稿内容（3,000文字以内）",
    "platforms": [{"platform": "linkedin", "accountId": "..."}]
}

# NG: threadItems は LinkedIn では使用不可
payload = {
    "content": "",
    "platforms": [{
        "platform": "linkedin",
        "platformSpecificData": {"threadItems": [...]}  # 無効
    }]
}
```

### 3.2 X（Twitter）

**制限**:
- 最大140文字/ツイート
- スレッド最大数: 制限なし
- 同一内容の連続投稿: 1時間に複数投稿不可

**実装時の注意**:

```python
# 正しいスレッド形式
thread_items = [
    {"content": "(1/5)\n\nツイート1（140文字以内）"},
    {"content": "(2/5)\n\nツイート2（140文字以内）"}
]

payload = {
    "content": "",  # threadItems使用時は空
    "platforms": [{
        "platform": "twitter",
        "accountId": "tw_...",
        "platformSpecificData": {"threadItems": thread_items}
    }]
}
```

### 3.3 Threads

**制限**:
- 最大500文字/投稿
- スレッド最大数: 推奨3投稿（分割アルゴリズムで自動調整）
- Instagram との連携が必須

**実装時の注意**:

```python
# 正しいスレッド形式（3投稿推奨）
thread_items = [
    {"content": "1投目（500文字以内）..."},
    {"content": "2投目（500文字以内）..."},
    {"content": "3投目（500文字以内）..."}
]

payload = {
    "content": "",  # threadItems使用時は空
    "platforms": [{
        "platform": "threads",
        "accountId": "th_...",
        "platformSpecificData": {"threadItems": thread_items}
    }]
}
```

### 3.4 Facebook

**制限**:
- 最大63,206文字/投稿
- スレッド機能なし
- ページアカウント必須（個人アカウント不可）

---

## 4. リクエスト形式の制約

### 4.1 contentとthreadItemsの排他性

Late API では以下のルールが厳密に適用される：

```python
# パターン1: 単一投稿（content のみ）
payload = {
    "content": "投稿内容",
    "platforms": [...]
}

# パターン2: スレッド投稿（threadItems のみ）
payload = {
    "content": "",  # 空にする（重要）
    "platforms": [{
        "platformSpecificData": {
            "threadItems": [{"content": "..."}, ...]
        }
    }]
}

# NG: 両方を指定
payload = {
    "content": "投稿内容",  # 不正
    "platforms": [{
        "platformSpecificData": {
            "threadItems": [...]  # 不正
        }
    }]
}
```

**エラーが発生する場合**:

```
400 Bad Request
"error": "Either content or threadItems must be provided, not both"
```

### 4.2 platformsは配列必須

```python
# OK: platforms は配列
payload = {
    "content": "内容",
    "platforms": [
        {"platform": "linkedin", "accountId": "..."},
        {"platform": "twitter", "accountId": "..."}
    ]
}

# NG: platforms が文字列
payload = {
    "content": "内容",
    "platforms": "linkedin"  # エラー
}

# NG: platform（単数） を使用
payload = {
    "content": "内容",
    "platform": "linkedin"  # エラー
}
```

### 4.3 accountId は必須

```python
# OK
payload = {
    "platforms": [{
        "platform": "linkedin",
        "accountId": "ln_abc123xyz"  # 必須
    }]
}

# NG: accountId なし
payload = {
    "platforms": [{
        "platform": "linkedin"
        # accountId が不足 → 400 Error
    }]
}
```

---

## 5. .env管理の制約

### 5.1 インラインコメント禁止

Late APIのアカウントID解析エラーの主要原因：

```bash
# ❌ 禁止: インラインコメント
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"  # 優一 佐藤

# ✅ 推奨: コメントは別行
# LinkedIn: 優一 佐藤
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"
```

**発生するエラー**:

```
500 Internal Server Error
{
  "error": "Invalid account ID format"
}
```

### 5.2 クォートの統一

```bash
# OK: ダブルクォート
LATE_API_KEY="sk_abc123..."

# OK: シングルクォート
LATE_API_KEY='sk_abc123...'

# OK: クォートなし（スペース含まない場合）
LATE_API_KEY=sk_abc123...

# NG: 混在
LATE_API_KEY="sk_abc123...'
```

### 5.3 特殊文字のエスケープ

```bash
# OK: クォート内の特殊文字
CONTENT="投稿内容 (1/3)"

# NG: クォートなしの特殊文字
CONTENT=投稿内容 (1/3)  # エラー

# OK: バックスラッシュでエスケープ
CONTENT=投稿内容\ \(1/3\)
```

---

## 6. エラーハンドリングの制約

### 6.1 リトライ可能なエラー

| コード | エラー | リトライ | 待機時間 |
|--------|--------|---------|---------|
| **401** | Unauthorized | ❌ | - |
| **429** | Rate Limit | ✅ | 1時間 |
| **500+** | Server Error | ✅ | 指数バックオフ |
| **Timeout** | Connection Timeout | ✅ | 指数バックオフ |

### 6.2 リトライしてはいけないエラー

```python
# 401: API Key不正
if status_code == 401:
    print("❌ API設定を確認してください")
    # リトライしない → スキップ

# 400: リクエスト不正
if status_code == 400:
    print("❌ パラメータを確認してください")
    # リトライしない → スキップ
```

### 6.3 リトライロジックの実装上限

```python
# 推奨: 最大3回リトライ
max_retries = 3

# 避けるべき: 無限リトライ
while True:  # NG: 無限ループ
    result = post_to_api()
    if result:
        break
```

---

## 7. 並列処理の制約

### 7.1 同時リクエスト数の制限

Late APIはレート制限を持つため、大量の並列リクエストは避けるべき：

```python
# OK: 逐次処理（安全）
for variant in variants:
    post_to_late_api(variant)
    time.sleep(1)

# 慎重: 最大5並列（テスト必須）
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(post_to_late_api, v) for v in variants]

# NG: 無制限並列
import threading

for variant in variants:
    thread = threading.Thread(target=post_to_late_api, args=(variant,))
    thread.start()  # 危険: レート制限に引っかかる可能性
```

### 7.2 依存性がある場合は逐次処理

```python
# OK: 逐次処理（前の結果を使用）
for i, variant in enumerate(variants):
    scheduled_date = available_dates[i]
    result = post_to_late_api(variant, scheduled_date)

    if result["status"] == "error":
        # エラー処理
        pass

# NG: 並列処理（日付が確定していない）
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(post_to_late_api, v, available_dates[i])
        for i, v in enumerate(variants)
    ]
```

---

## 8. データ型の制約

### 8.1 文字列フィールド

```python
# OK: 文字列
payload = {"content": "投稿内容"}

# NG: 数値（自動変換されない）
payload = {"content": 12345}  # TypeError

# NG: バイト列
payload = {"content": b"投稿内容"}  # TypeError
```

### 8.2 日時フィールド

```python
# OK: ISO8601形式（文字列）
payload = {"scheduledFor": "2026-01-07T08:00:00+09:00"}

# NG: datetime オブジェクト（文字列化が必須）
import datetime
payload = {"scheduledFor": datetime.datetime.now()}  # TypeError

# NG: Unixタイムスタンプ（文字列化が必須）
payload = {"scheduledFor": 1672977600}  # 型が違う
```

### 8.3 配列フィールド

```python
# OK: 配列
payload = {"platforms": [{"platform": "linkedin", "accountId": "..."}]}

# NG: 文字列
payload = {"platforms": "linkedin"}  # TypeError

# NG: 単一オブジェクト
payload = {"platforms": {"platform": "linkedin", "accountId": "..."}}  # TypeError
```

---

## 9. 既知の制限事項

### 9.1 複数プラットフォーム投稿時の挙動

```python
# 複数プラットフォームに同時投稿
payload = {
    "content": "内容",
    "platforms": [
        {"platform": "linkedin", "accountId": "ln_..."},
        {"platform": "twitter", "accountId": "tw_..."}
    ]
}

# 実際の動作:
# ✅ LinkedInに投稿される
# ✅ Xに投稿される
# ⚠️ 両方が同じPost IDで管理される（個別追跡不可）
```

### 9.2 スレッド投稿時の順序保証

```python
thread_items = [
    {"content": "(1/3)..."},
    {"content": "(2/3)..."},
    {"content": "(3/3)..."}
]

# ✅ 投稿順序は保証される（(1/3) → (2/3) → (3/3)）
# ⚠️ ただし、投稿に失敗した場合は部分的に投稿される可能性
```

### 9.3 予約投稿のキャンセル

Late APIは予約投稿のキャンセル機能を提供していない：

```
DELETE /posts/{post_id}  # サポートなし（2026-01-06現在）
```

代替策：
- Late API ダッシュボードから手動キャンセル
- 自動投稿スクリプトで事前削除（ただしPost IDが必要）

---

## 10. ベストプラクティス

### 10.1 環境構築

```bash
# 推奨: 環境変数ファイルの管理
.env  # .gitignore に追加
│
├── LATE_API_KEY="sk_..."
├── LATE_LINKEDIN_ACCOUNT_ID="ln_..."
├── LATE_TWITTER_ACCOUNT_ID="tw_..."
└── LATE_THREADS_ACCOUNT_ID="th_..."

# 設定ファイルの管理
config/late_api_config.json  # Git管理（センシティブ情報なし）
```

### 10.2 エラーログ記録

```python
import json
from datetime import datetime

# エラーログを記録
error_log = {
    "timestamp": datetime.now().isoformat(),
    "endpoint": "https://getlate.dev/api/v1/posts",
    "status_code": 400,
    "error": response.text,
    "payload": payload  # デバッグ用（PII除去）
}

with open("late_api_errors.json", "a") as f:
    json.dump(error_log, f, ensure_ascii=False)
    f.write("\n")
```

### 10.3 インテグレーションテスト

```python
def test_late_api_integration():
    """本番前の統合テスト"""

    # テスト1: 接続確認
    assert late_api_connection_ok()

    # テスト2: 環境変数確認
    assert all([
        os.getenv("LATE_API_KEY"),
        os.getenv("LATE_LINKEDIN_ACCOUNT_ID")
    ])

    # テスト3: 小規模投稿テスト
    result = post_scheduled_test("テスト投稿", tomorrow_8am)
    assert result["status"] == "success"

    # テスト4: 予約取得テスト
    posts = get_existing_scheduled_posts()
    assert len(posts) >= 1
```

### 10.4 本番環境でのセーフティ

```python
# 投稿前に確認プロンプト
import sys

print("=" * 60)
print("Late API投稿計画")
print("=" * 60)
for plan in posting_plan:
    print(f"📅 {plan['date']} - {plan['title']}")

confirm = input("\n上記で実行しますか？ (yes/no): ")

if confirm.lower() != "yes":
    print("❌ キャンセルしました")
    sys.exit(0)

# 投稿実行
execute_posting_plan(posting_plan)
```

---

## 11. チェックリスト（デプロイ前確認）

Late API統合を本番環境にデプロイする前に確認：

### 基本設定
- [ ] API Keyは `.env` に保存（`.gitignore` 対象）
- [ ] アカウントIDは環境変数から取得
- [ ] エンドポイント: `https://getlate.dev/api/v1/posts`

### リクエスト形式
- [ ] `content` と `threadItems` は排他的
- [ ] `platforms` は配列形式
- [ ] `scheduledFor` はISO8601形式（`+09:00` 付き）
- [ ] `timezone` は `"Asia/Tokyo"`

### エラーハンドリング
- [ ] 401：リトライなし（API設定確認）
- [ ] 429：1時間待機後リトライ
- [ ] 5xx：指数バックオフで3回リトライ
- [ ] エラーログ記録を実装

### 並列処理
- [ ] 同時リクエスト数 ≤ 5
- [ ] リクエスト間隔 ≥ 1秒
- [ ] 依存性がある場合は逐次処理

### テスト
- [ ] 接続テスト成功
- [ ] 小規模投稿テスト成功
- [ ] 予約取得テスト成功
- [ ] エラーハンドリングテスト成功

### ドキュメント
- [ ] API仕様書を確認
- [ ] 制約事項を理解
- [ ] 本番手順書を作成

---

**最終更新**: 2026-01-06
**バージョン**: 1.0
**確認日**: 2026-01-06
