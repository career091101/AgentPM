# Phase 4: Late API予約投稿

## 概要

Phase 3で生成したリポスト投稿（4-6件）をLate API経由で最適な時間帯に予約投稿するフェーズ。

**所要時間**: 10-15分
**並列化**: 不可（API直列実行）
**推奨モデル**: haiku（シンプルなAPI操作）

---

## 目的

1. Late API経由で4-6投稿を予約投稿
2. URL埋め込み方式でX投稿を生成（Xがリンクカード自動生成）
3. エラーハンドリング（指数バックオフリトライ: 5秒→15秒→30秒）
4. 投稿結果レポート生成

---

## 入力ファイル

### `repost_drafts_{date}.json`

Phase 3で生成したリポスト投稿案（4-6件）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/repost_drafts_{date}.json`

**使用データ**:
```json
{
  "drafts": [
    {
      "tweet_url": "https://x.com/username/status/123456789",
      "tweet_rank": 1,
      "quality_score": 85,
      "scheduled_time": "2026-01-13T07:30:00+09:00",
      "post_json": {
        "content": "[takano式解説文]\n\n🔗 元の投稿: https://x.com/username/status/123456789",
        "platforms": [
          {
            "platform": "twitter",
            "accountId": "LATE_TWITTER_ACCOUNT_ID"
          }
        ],
        "scheduledFor": "2026-01-13T07:30:00+09:00",
        "timezone": "Asia/Tokyo"
      }
    },
    ...
  ]
}
```

---

## 処理フロー

### STEP 1: 環境変数読み込み

Late API認証情報とX Proアカウント情報を環境変数から取得。

```python
import os
import json

# Late API認証
LATE_API_KEY = os.getenv('LATE_API_KEY')
LATE_API_URL = 'https://api.late.so/v1/posts'

# X Proアカウント
LATE_TWITTER_ACCOUNT_ID = os.getenv('LATE_TWITTER_ACCOUNT_ID')

if not LATE_API_KEY or not LATE_TWITTER_ACCOUNT_ID:
    raise ValueError("環境変数 LATE_API_KEY, LATE_TWITTER_ACCOUNT_ID が設定されていません")

print(f"Late API URL: {LATE_API_URL}")
print(f"X Account ID: {LATE_TWITTER_ACCOUNT_ID}")
```

### STEP 2: 投稿JSON準備

Phase 3の `post_json` を読み込み、アカウントIDを環境変数の値に置換。

```python
# repost_drafts_{date}.json 読み込み
with open('Flow/{date_path}/repost_drafts_{date}.json', 'r') as f:
    repost_data = json.load(f)

drafts = repost_data['drafts']

# アカウントID置換
for draft in drafts:
    draft['post_json']['platforms'][0]['accountId'] = LATE_TWITTER_ACCOUNT_ID

print(f"投稿準備完了: {len(drafts)}件")
```

### STEP 3: Late API投稿実行

指数バックオフリトライ（5秒→15秒→30秒）で各投稿を実行。

```python
import requests
import time

def post_to_late_api(post_json, retries=3):
    """Late APIに投稿（指数バックオフリトライ）"""
    headers = {
        'Authorization': f'Bearer {LATE_API_KEY}',
        'Content-Type': 'application/json'
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(
                LATE_API_URL,
                headers=headers,
                json=post_json,
                timeout=30
            )

            if response.status_code == 201:
                # 成功
                return {
                    'status': 'success',
                    'response': response.json(),
                    'attempt': attempt
                }
            elif response.status_code == 429:
                # レート制限
                if attempt < retries:
                    wait_time = [5, 15, 30][attempt - 1]
                    print(f"  レート制限検出、{wait_time}秒待機...")
                    time.sleep(wait_time)
                    continue
                else:
                    return {
                        'status': 'rate_limit_exceeded',
                        'error': 'Max retries exceeded',
                        'attempt': attempt
                    }
            else:
                # その他エラー
                return {
                    'status': 'error',
                    'error': response.text,
                    'status_code': response.status_code,
                    'attempt': attempt
                }

        except requests.exceptions.Timeout:
            if attempt < retries:
                wait_time = [5, 15, 30][attempt - 1]
                print(f"  タイムアウト、{wait_time}秒待機後リトライ...")
                time.sleep(wait_time)
                continue
            else:
                return {
                    'status': 'timeout',
                    'error': 'Request timeout after max retries',
                    'attempt': attempt
                }

        except Exception as e:
            return {
                'status': 'exception',
                'error': str(e),
                'attempt': attempt
            }

    return {
        'status': 'unknown_error',
        'error': 'Unexpected error',
        'attempt': retries
    }


# 投稿実行
post_results = []

for i, draft in enumerate(drafts, 1):
    print(f"\n投稿 {i}/{len(drafts)}: Rank {draft['tweet_rank']}")
    print(f"  予定時刻: {draft['scheduled_time']}")

    result = post_to_late_api(draft['post_json'])

    post_results.append({
        'tweet_rank': draft['tweet_rank'],
        'tweet_url': draft['tweet_url'],
        'scheduled_time': draft['scheduled_time'],
        'quality_score': draft['quality_score'],
        'result': result
    })

    if result['status'] == 'success':
        print(f"  ✓ 投稿成功（試行{result['attempt']}回目）")
    else:
        print(f"  ✗ 投稿失敗: {result['status']} - {result.get('error', 'Unknown')}")

    # API負荷軽減のため、投稿間に1秒待機
    if i < len(drafts):
        time.sleep(1)

# 成功・失敗の集計
success_count = sum(1 for r in post_results if r['result']['status'] == 'success')
failed_count = len(post_results) - success_count

print(f"\n投稿結果: 成功 {success_count}件 / 失敗 {failed_count}件")
```

### STEP 4: フォールバック処理（3回失敗後）

3回のリトライ後も失敗した投稿は、手動投稿用Markdownファイルを生成。

```python
# repost_config.json からフォールバック設定読み込み
with open('.claude/skills/x-deck-repost-automation/repost_config.json', 'r') as f:
    config = json.load(f)

fallback_enabled = config['late_api']['fallback_enabled']

if fallback_enabled and failed_count > 0:
    fallback_posts = []

    for result in post_results:
        if result['result']['status'] != 'success':
            # 失敗した投稿の詳細を取得
            failed_draft = next(d for d in drafts if d['tweet_rank'] == result['tweet_rank'])

            fallback_posts.append({
                'rank': result['tweet_rank'],
                'scheduled_time': result['scheduled_time'],
                'content': failed_draft['post_json']['content'],
                'error': result['result'].get('error', 'Unknown')
            })

    # 手動投稿用Markdownファイル生成
    fallback_md = f"""# 手動投稿が必要な投稿一覧

Late API投稿に失敗したため、以下の投稿を手動で投稿してください。

生成日時: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

"""

    for post in fallback_posts:
        fallback_md += f"""
## 投稿 {post['rank']}

**予定時刻**: {post['scheduled_time']}
**エラー**: {post['error']}

**投稿内容**:
```
{post['content']}
```

---

"""

    # ファイル保存
    fallback_path = f"Flow/{date_path}/late_api_fallback_{date}.md"
    with open(fallback_path, 'w', encoding='utf-8') as f:
        f.write(fallback_md)

    print(f"\nフォールバックファイル生成: {fallback_path}")
```

---

## 出力ファイル

### `late_api_repost_{date}.json`

Late API投稿結果。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/late_api_repost_{date}.json`

**データ構造**:
```json
{
  "posted_at": "2026-01-12T15:00:00+09:00",
  "total_posts": 6,
  "success_count": 5,
  "failed_count": 1,
  "results": [
    {
      "tweet_rank": 1,
      "tweet_url": "https://x.com/username/status/123456789",
      "scheduled_time": "2026-01-13T07:30:00+09:00",
      "quality_score": 85,
      "result": {
        "status": "success",
        "response": {
          "id": "late_post_abc123",
          "scheduledFor": "2026-01-13T07:30:00+09:00",
          "status": "scheduled"
        },
        "attempt": 1
      }
    },
    {
      "tweet_rank": 2,
      "tweet_url": "https://x.com/username/status/987654321",
      "scheduled_time": "2026-01-13T08:30:00+09:00",
      "quality_score": 82,
      "result": {
        "status": "success",
        "response": {
          "id": "late_post_def456",
          "scheduledFor": "2026-01-13T08:30:00+09:00",
          "status": "scheduled"
        },
        "attempt": 2
      }
    },
    {
      "tweet_rank": 6,
      "tweet_url": "https://x.com/username/status/111222333",
      "scheduled_time": "2026-01-13T21:00:00+09:00",
      "quality_score": 78,
      "result": {
        "status": "timeout",
        "error": "Request timeout after max retries",
        "attempt": 3
      }
    }
  ]
}
```

### `repost_summary_{date}.md`

投稿サマリーレポート（Markdown形式）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/repost_summary_{date}.md`

**データ構造**:
```markdown
# X Pro Deck リポスト投稿サマリー

**実行日**: 2026-01-12
**投稿総数**: 6件
**成功**: 5件
**失敗**: 1件

---

## 成功投稿一覧

### 1. Rank 1 - OpenAI投資ラウンド評価額

- **予定時刻**: 2026-01-13 07:30 JST
- **品質スコア**: 85点
- **Late Post ID**: late_post_abc123
- **元ツイート**: https://x.com/username/status/123456789

### 2. Rank 2 - GoogleのAI投資戦略

- **予定時刻**: 2026-01-13 08:30 JST
- **品質スコア**: 82点
- **Late Post ID**: late_post_def456
- **元ツイート**: https://x.com/username/status/987654321

...

---

## 失敗投稿

### 1. Rank 6 - MicrosoftのAI人材採用

- **予定時刻**: 2026-01-13 21:00 JST
- **品質スコア**: 78点
- **エラー**: Request timeout after max retries
- **元ツイート**: https://x.com/username/status/111222333

**対策**: 手動投稿が必要です。詳細は `late_api_fallback_2026-01-12.md` を参照してください。

---

## 統計

| 指標 | 値 |
|------|-----|
| 平均品質スコア | 82.5点 |
| 成功率 | 83% (5/6) |
| 平均試行回数 | 1.4回 |
| 最高品質スコア | 85点（Rank 1） |
| 最低品質スコア | 78点（Rank 6） |

---

**次回実行**: 2026-01-13 06:00 JST
```

### `late_api_fallback_{date}.md`（失敗時のみ）

手動投稿用Markdownファイル。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/late_api_fallback_{date}.md`

---

## エラーハンドリング

### エラー1: 認証エラー（401 Unauthorized）

**エラー**: Late API認証失敗

```python
# 対策: 環境変数の確認
if response.status_code == 401:
    print("認証エラー: LATE_API_KEYを確認してください")
    print(f"現在の設定: {LATE_API_KEY[:10]}... (先頭10文字)")
    raise ValueError("Late API認証に失敗しました")
```

### エラー2: レート制限（429 Too Many Requests）

**エラー**: Late APIのレート制限に引っかかる

```python
# 対策: 指数バックオフリトライ（実装済み）
# 5秒 → 15秒 → 30秒で自動リトライ
```

### エラー3: タイムアウト（Timeout）

**エラー**: Late APIリクエストがタイムアウト

```python
# 対策: リトライ + タイムアウト延長
try:
    response = requests.post(..., timeout=30)
except requests.exceptions.Timeout:
    # 60秒に延長してリトライ
    response = requests.post(..., timeout=60)
```

### エラー4: アカウントID不正（400 Bad Request）

**エラー**: X ProアカウントIDが無効

```python
# 対策: アカウントID検証
if response.status_code == 400:
    error_msg = response.json().get('message', '')
    if 'accountId' in error_msg:
        print(f"アカウントID不正: {LATE_TWITTER_ACCOUNT_ID}")
        print("Late.soダッシュボードでアカウントIDを確認してください")
```

---

## 並列化の不可理由

Late APIは**直列実行のみ推奨**（並列実行は非推奨）。

理由:
1. **レート制限**: 短時間に大量リクエストを送るとレート制限に引っかかる
2. **投稿順序**: 予約時刻の順番で投稿する必要がある
3. **エラーハンドリング**: 直列実行で各投稿のエラーを確実に処理

---

## パフォーマンス最適化

### 最適化1: 投稿間隔の最適化

Late APIのレート制限を考慮し、投稿間に1秒待機。

```python
# 投稿間に1秒待機
for i, draft in enumerate(drafts):
    result = post_to_late_api(draft['post_json'])
    post_results.append(result)

    if i < len(drafts) - 1:  # 最後の投稿以外
        time.sleep(1)
```

### 最適化2: タイムアウト設定の最適化

Late APIレスポンスが遅い場合、タイムアウトを30秒→60秒に延長。

```python
# タイムアウト設定
TIMEOUT_DEFAULT = 30
TIMEOUT_EXTENDED = 60

# 初回タイムアウトで失敗したら延長
try:
    response = requests.post(..., timeout=TIMEOUT_DEFAULT)
except requests.exceptions.Timeout:
    response = requests.post(..., timeout=TIMEOUT_EXTENDED)
```

### 最適化3: 事前検証

Late API投稿前に、投稿内容の形式を検証。

```python
def validate_post_json(post_json):
    """投稿JSONの形式検証"""
    required_fields = ['content', 'platforms', 'scheduledFor', 'timezone']

    for field in required_fields:
        if field not in post_json:
            raise ValueError(f"必須フィールド '{field}' が不足しています")

    # 文字数チェック（X投稿の上限: 25,000字）
    if len(post_json['content']) > 25000:
        raise ValueError(f"投稿文字数が上限（25,000字）を超えています: {len(post_json['content'])}字")

    return True

# 投稿前に検証
for draft in drafts:
    validate_post_json(draft['post_json'])
```

---

## 検証項目

Phase 4完了時に以下を確認:

- [ ] Late API経由で4-6投稿を予約投稿できたか
- [ ] URL埋め込み方式でX投稿が生成されたか（Xがリンクカード自動生成）
- [ ] 予約時刻が正しく設定されたか（朝7-9時、昼12-13時、夜20-22時、JST）
- [ ] エラー時の指数バックオフリトライが機能したか（5秒→15秒→30秒）
- [ ] 3回失敗後のフォールバック機能が動作したか（手動投稿用MD生成）
- [ ] 出力ファイル（`late_api_repost_{date}.json`, `repost_summary_{date}.md`）が生成されたか
- [ ] 失敗投稿のフォールバックファイル（`late_api_fallback_{date}.md`）が生成されたか（失敗時）

---

## Late API仕様詳細

### エンドポイント

```
POST https://api.late.so/v1/posts
```

### リクエストヘッダー

```http
Authorization: Bearer {LATE_API_KEY}
Content-Type: application/json
```

### リクエストボディ

```json
{
  "content": "[takano式解説文]\n\n🔗 元の投稿: https://x.com/username/status/123456789",
  "platforms": [
    {
      "platform": "twitter",
      "accountId": "LATE_TWITTER_ACCOUNT_ID"
    }
  ],
  "scheduledFor": "2026-01-13T07:30:00+09:00",
  "timezone": "Asia/Tokyo"
}
```

**重要フィールド**:
- `content`: 投稿本文（最大25,000字、X長文投稿対応）
- `platforms[0].platform`: "twitter"（固定）
- `platforms[0].accountId`: Late.soダッシュボードで確認
- `scheduledFor`: ISO 8601形式（`YYYY-MM-DDTHH:MM:SS+09:00`）
- `timezone`: "Asia/Tokyo"（固定）

### レスポンス（成功時）

```json
{
  "id": "late_post_abc123",
  "content": "[投稿本文]",
  "platforms": [
    {
      "platform": "twitter",
      "accountId": "LATE_TWITTER_ACCOUNT_ID",
      "status": "scheduled"
    }
  ],
  "scheduledFor": "2026-01-13T07:30:00+09:00",
  "status": "scheduled",
  "createdAt": "2026-01-12T15:00:00Z"
}
```

### レスポンス（失敗時）

```json
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "statusCode": 429
}
```

---

## トラブルシューティング

### 問題1: 投稿が予約されない

**症状**: Late APIから200応答があるが、Late.soダッシュボードに投稿が表示されない

```python
# 解決策
1. Late.soダッシュボードでアカウント接続を確認
2. X Proアカウントの認証状態を確認
3. accountIdが正しいか確認（Late.soダッシュボードで取得）
```

### 問題2: リンクカードが生成されない

**症状**: URL埋め込みしたが、Xでリンクカードが表示されない

```python
# 解決策
1. URLが正しい形式か確認（https://x.com/username/status/123456789）
2. URLの前後に改行があるか確認（\n\n🔗 元の投稿: {url}）
3. X投稿後24時間以内にリンクカードが生成されることを確認（遅延の可能性）
```

### 問題3: 投稿が送信されない

**症状**: 予約時刻になっても投稿が送信されない

```python
# 解決策
1. Late.soダッシュボードで投稿ステータスを確認
2. X Proアカウントの権限を確認（投稿権限が有効か）
3. Late.soのサービスステータスを確認（障害発生の可能性）
```

---

## 次のステップ

Phase 4完了後、次回実行まで待機。

### 定期実行設定

```bash
# cronで毎日朝6時に全Phaseを自動実行
0 6 * * * cd /Users/yuichi/agentpm && claude-code --skill x-deck-repost-automation --auto
```

### モニタリング

- Late.soダッシュボードで予約投稿を確認
- X Proタイムラインで投稿を確認
- エンゲージメント統計を定期的に収集

---

## 参照

- **メインSkill定義**: `../SKILL.md`
- **設定ファイル**: `../repost_config.json`
- **Late API実装**: `Stock/programs/副業/projects/SNS/scripts/late_api_multi_post_v2.py`
- **Late API仕様**: `Flow/202601/2026-01-12/late-api-openapi.yaml`
- **Late API公式ドキュメント**: https://late.so/api
- **実装プラン**: `~/.claude/plans/serene-painting-pumpkin.md`
