---
name: generate-x-threads-posts
description: |
  X（Twitter）とThreadsに同時投稿するスキル。
  各プラットフォームに最適化したコンテンツを生成し、Late API経由で予約投稿。
  - X: スレッド形式（7ツイート最適）、バズ構文84パターン
  - Threads: 500字以内、絵文字多用、カジュアルトーン
trigger_keywords:
  - "X&Threads投稿"
  - "同時投稿"
  - "XとThreads投稿"
stage: Development
dependencies:
  - generate-x-posts
  - sns-automation
priority: P0
model: claude-opus-4-5-20251101  # Opus 4.5 (2026年1月時点の最新モデル)
thinking: true
context_optimization:
  external_files:
    - threads_patterns_config.json
    - x_patterns_detailed.md (generate-x-posts)
  estimated_reduction: 70%
---

# X & Threads 同時投稿スキル

## 概要

このスキルは、X（Twitter）とThreadsの両方に最適化された投稿を生成し、Late API経由で予約投稿します。

### 主要機能

1. **プラットフォーム別最適化**
   - X版: `generate-x-posts`スキル（v0.4.6）のロジックを流用
   - Threads版: X版をベースに500字以内、絵文字・口語体を増強

2. **予約投稿スケジューリング**
   - Late API経由で既存予約を取得
   - 14日先までの空き日を自動検索
   - 20:00 JST に予約投稿（デフォルト）
   - 1日1投稿のみ（競合回避）

3. **エラーハンドリング・リトライ**
   - Rate Limit: 1時間待機後リトライ
   - Network Timeout: 指数バックオフ（10秒→20秒→40秒）
   - 片方失敗でも他方は継続（部分成功許容）

4. **画像添付**
   - 同一画像をX・Threads両方に添付（オプション）

---

## 入力仕様

### 必須パラメータ

| パラメータ | 型 | 説明 | 例 |
|-----------|---|------|---|
| `input_type` | string | 入力タイプ | `"topic"`, `"article_url"`, `"keyword"` |
| `input_value` | string | 入力値 | トピック文、URL、キーワード |

### オプションパラメータ

| パラメータ | 型 | デフォルト | 説明 |
|-----------|---|----------|------|
| `scheduled_date` | string | `null` | 予約日付（YYYY-MM-DD形式、未指定時は自動検索） |
| `scheduled_time` | string | `"20:00"` | 予約時刻（HH:MM形式） |
| `image_path` | string | `null` | 画像ファイルパス |
| `days_ahead` | int | `14` | 空き日検索範囲（日数） |

---

## 処理フロー

### STEP 1: 入力検証・準備（1分）

**処理内容**:
- 入力パラメータのバリデーション
- 画像ファイル存在確認（指定時）
- Late API設定ロード

**使用ツール**:
- `Read`: 設定ファイル読み込み
- Bash: ファイル存在確認（画像指定時）

### STEP 2: X版コンテンツ生成（2-3分）

**処理内容**:
- `generate-x-posts`スキル（v0.4.6）のロジックを流用
- スレッド生成（7ツイート想定）
- バズ構文選択（84パターンから最適選択）
- エンゲージメント予測

**実装方法**:
```markdown
`generate-x-posts`スキルのSTEP 1-4を実行:

1. **コンテンツ準備**
   - topic型: LLM直接推論
   - URL型: WebFetch tool + LLM要約
   - keyword型: WebSearch + Top 3統合

2. **スレッド生成**
   - バズ構文選択（x_patterns_detailed.mdから3パターン）
   - セマンティック分割（LLM自然言語理解）
   - 280文字/ツイート制限検証

3. **エンゲージメント予測**
   - X公式アルゴリズムスコア計算
   - Recency Factor適用
   - Premium優遇・時間帯補正
```

**出力**:
```json
{
  "format": "thread",
  "thread_tweets": [
    {
      "tweet_number": "1/7",
      "content": "🚨 OpenAIが「ひっそり公開」した...",
      "character_count": {"total": 134}
    },
    ...
  ],
  "engagement_prediction": {
    "predicted_likes": 120,
    "x_algorithm_score": 173.0
  }
}
```

### STEP 3: Threads版コンテンツ生成（1-2分）

**処理内容**:
- X版スレッドをThreads向けに変換
- 文字数調整（700-1500字 → 300-500字）
- 段落構成（4-8段落 → 2-4段落）
- 絵文字追加（0-2個 → 3-5個）
- 口語体増強（2回 → 3-5回）

**実行方法**: ClaudeCode CLI内でLLM推論により直接変換を実行

**LLM推論プロンプト**:
```
以下のX投稿スレッドをThreads向けに最適化してください。

**要件**:
- 文字数: 300-500字（厳守）
- 段落: 2-4段落（空白2行禁止）
- 絵文字: 3-5個（Hook、Insight、CTA位置）
- 口語体: 3-5回使用（「マジで」「ヤバい」「〜の件」等）
- ハッシュタグ: 一切使用しない（SNS横断での重複コンテンツ回避のため）
- 問いかけ終結: 必須

**調整ポイント**:
- データポイントは3-5個に絞る
- 断定型表現を維持（「つまり」「ポイントは」）
- カジュアルなトーン（20-40代若年層向け）

**禁止事項**:
- 空白2行以上の改行（自動ツリー化）
- ハッシュタグの使用（一切使用しない）
- 絵文字過多（10個以上）

**元のX投稿**:
{X版スレッド全文}

**出力形式**: Threads投稿本文のみ（JSON不要、プレーンテキストで出力）
```

**実行後の検証**:
生成されたThreads投稿を`threads_adapter.py`の検証機能でチェック：

```bash
cd Stock/programs/副業/projects/SNS/scripts
python3 -c "
from threads_adapter import ThreadsAdapter

adapter = ThreadsAdapter()

# LLM推論で生成されたThreads投稿本文
threads_content = '''[生成されたThreads投稿本文]'''

# 検証のみ実行（メトリクス抽出）
result = adapter._validate_and_extract_metrics(
    content=threads_content,
    target_length=(300, 500),
    emoji_count_range=(3, 5),
    informal_count_range=(3, 5)
)

print(f'✅ 検証成功')
print(f'文字数: {result[\"character_count\"]}字')
print(f'絵文字: {result[\"emoji_count\"]}個')
print(f'段落: {result[\"paragraph_count\"]}段落')
print(f'口語体: {result[\"informal_count\"]}回')
"
```

**出力例**:
```
✅ 検証成功
文字数: 480字
絵文字: 3個
段落: 3段落
口語体: 3回
```

### STEP 4: 予約投稿スケジューリング（30秒）

**処理内容**:
- Late API経由で既存予約を取得
- 指定日または自動検索で空き日を決定

**使用スクリプト**:
```bash
cd Stock/programs/副業/projects/SNS/scripts
python3 -c "
from late_api_scheduler import LateAPIScheduler

scheduler = LateAPIScheduler()

# 既存予約を取得
reserved = scheduler.get_existing_reservations(target_hour=20)
print(f'既存予約: {len(reserved)}件')

# 空き日を検索
available_slot = scheduler.find_available_slot(
    days_ahead=14,
    target_hour=20,
    specified_date='2026-01-08'  # ユーザー指定日（オプション）
)
print(f'次の空き日: {available_slot}')
"
```

**ロジック**:
1. Late API `GET /posts?status=scheduled` で既存予約を取得
2. 20:00 JST予約済み日付を抽出
3. 翌日から14日先まで検索
4. 競合しない最初の日付を選択

**出力**:
```
scheduled_datetime: 2026-01-08T20:00:00+09:00
```

### STEP 5: Late API予約投稿（1-2分）

**処理内容**:
- X版をスレッド形式で投稿
- Threads版を単一投稿
- リトライ付き実行

**使用スクリプト**:
```bash
cd Stock/programs/副業/projects/SNS/scripts
python3 -c "
from late_api_scheduler import LateAPIScheduler
from datetime import datetime
from zoneinfo import ZoneInfo

scheduler = LateAPIScheduler()
jst = ZoneInfo('Asia/Tokyo')
scheduled_dt = datetime(2026, 1, 8, 20, 0, 0, tzinfo=jst)

# X投稿（スレッド）
x_tweets = [...]  # STEP 2の出力
x_result = scheduler.schedule_post(
    content=x_tweets[0],  # 1ツイート目
    platform='twitter',
    scheduled_dt=scheduled_dt,
    platform_specific_data={
        'threadItems': [{'content': tweet} for tweet in x_tweets[1:]]
    }
)

# Threads投稿
threads_content = ...  # STEP 3の出力
threads_result = scheduler.schedule_post(
    content=threads_content,
    platform='threads',
    scheduled_dt=scheduled_dt
)

print(f'X Post ID: {x_result[\"post_id\"]}')
print(f'Threads Post ID: {threads_result[\"post_id\"]}')
"
```

**画像添付ありの場合**:
```bash
# 画像パスを指定して投稿
image_path = '/path/to/image.png'

# X投稿（スレッド + 画像）
x_result = scheduler.schedule_post(
    content=x_tweets[0],
    platform='twitter',
    scheduled_dt=scheduled_dt,
    image_path=image_path,
    platform_specific_data={
        'threadItems': [{'content': tweet} for tweet in x_tweets[1:]]
    }
)

# Threads投稿（同一画像）
threads_result = scheduler.schedule_post(
    content=threads_content,
    platform='threads',
    scheduled_dt=scheduled_dt,
    image_path=image_path
)
```

**画像アップロードの処理フロー**:
1. `scheduler._upload_image(image_path)` でLate API `/media` エンドポイントに画像をアップロード
2. アップロード成功時、Late APIから画像URLを取得
3. 投稿ペイロードに `payload['media'] = [{'url': uploaded_url}]` を追加
4. X・Threads両方に同一画像が添付される

**リトライロジック**:
- Rate Limit（429）: 1時間待機後リトライ（1回）
- Network Timeout: 10秒→20秒→40秒の指数バックオフ（3回）
- Authentication（401）: 即時停止
- Bad Request（400）: 即時停止

**エラー時の挙動**:
- X投稿失敗 → Threads投稿は継続
- Threads投稿失敗 → X投稿は継続
- 両方失敗 → エラー通知（部分成功でもOK）

### STEP 6: 結果サマリー出力（10秒）

**処理内容**:
- JSON形式で結果を保存
- Markdown形式でレポート生成

**出力先**:
```
Flow/202601/2026-01-06/post_result_20260106_153000.json
Flow/202601/2026-01-06/post_result_20260106_153000.md
```

**JSON形式**:
```json
{
  "execution_timestamp": "2026-01-06T15:30:00+09:00",
  "scheduled_datetime": "2026-01-08T20:00:00+09:00",
  "results": {
    "x": {
      "status": "success",
      "post_id": "695ceb1e8247cf816ba753b6",
      "tweet_count": 7,
      "engagement_prediction": {
        "predicted_likes": 120,
        "x_algorithm_score": 173.0
      }
    },
    "threads": {
      "status": "success",
      "post_id": "695ceb1e8247cf816ba753b7",
      "character_count": 480,
      "emoji_count": 3
    }
  },
  "image_attached": false,
  "retry_count": {
    "x": 0,
    "threads": 1
  }
}
```

**Markdown形式**:
```markdown
# X & Threads 同時投稿結果

**実行日時**: 2026-01-06 15:30:00 JST
**予約日時**: 2026-01-08 20:00:00 JST

## X投稿

### ステータス
✅ 成功（Post ID: 695ceb1e8247cf816ba753b6）

### コンテンツ（スレッド7ツイート）
1/7: 🚨 OpenAIが「ひっそり公開」した...
2/7: つまり、プロンプトエンジニアリングの...
...

### エンゲージメント予測
- いいね: 120件
- Xアルゴリズムスコア: 173.0

---

## Threads投稿

### ステータス
✅ 成功（Post ID: 695ceb1e8247cf816ba753b7）

### コンテンツ
🚨 OpenAIがひっそり公開した最新のプロンプトガイドがヤバい。

プロンプトエンジニアリングの常識が3つ変わる件について。

どう思う？

### メトリクス
- 文字数: 480字
- 絵文字: 3個
- 口語体: 3回

---

## リトライ履歴
- X: 0回
- Threads: 1回（Network Timeout → 成功）
```

---

## 実行例

### 例1: トピック型（画像なし）

**入力**:
```json
{
  "input_type": "topic",
  "input_value": "OpenAIのGPT-5.2プロンプトガイドが公開され、プロンプトエンジニアリングの常識が変わりつつある"
}
```

**実行**:
```markdown
1. X版スレッド生成（7ツイート）
2. Threads版生成（480字）
3. 空き日検索 → 2026-01-08 20:00
4. Late API投稿（X + Threads）
5. 結果保存
```

**出力**:
```
✅ X投稿成功: Post ID = 695ceb1e...
✅ Threads投稿成功: Post ID = 695ceb1e...
📅 予約日時: 2026-01-08 20:00:00 JST
```

### 例2: URL型（画像あり）

**入力**:
```json
{
  "input_type": "article_url",
  "input_value": "https://example.com/ai-news",
  "image_path": "/path/to/image.png"
}
```

**実行**:
```markdown
1. WebFetch tool で記事取得
2. LLM要約（120字以内）
3. X版スレッド生成
4. Threads版生成
5. 画像アップロード → Late API
6. 予約投稿
```

---

## エラーハンドリング

### エラー種別と対応

| エラー | 対応 | リトライ | 通知 |
|--------|------|---------|------|
| **Rate Limit（429）** | 1時間待機後リトライ | 1回 | ⚠️  |
| **Network Timeout** | 指数バックオフ | 3回 | ⚠️  |
| **Authentication（401）** | 即時停止 | 0回 | ❌ |
| **Bad Request（400）** | 即時停止 | 0回 | ❌ |
| **空き日なし** | エラー通知 | - | ❌ |

### 部分成功の許容

- X投稿成功 + Threads投稿失敗 → **成功扱い**（Threads分はMarkdown保存）
- X投稿失敗 + Threads投稿成功 → **成功扱い**（X分はMarkdown保存）
- 両方失敗 → **失敗扱い**（両方Markdown保存）

---

## 設定ファイル

### Late API設定

**パス**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`

```json
{
  "api_key": "sk_...",
  "base_url": "https://getlate.dev/api/v1",
  "accounts": {
    "twitter": {"accountId": "...", "platform": "twitter"},
    "threads": {"accountId": "...", "platform": "threads"}
  },
  "scheduling": {
    "default_time": "20:00",
    "search_days_ahead": 14,
    "timezone": "Asia/Tokyo"
  },
  "retry": {
    "max_retries": 3,
    "rate_limit_wait": 3600,
    "timeout_backoff_base": 10
  }
}
```

### Threads設定

**パス**: `.claude/skills/generate-x-threads-posts/threads_patterns_config.json`

詳細は`threads_patterns_config.json`を参照。

---

## 制約事項

### X投稿
- 文字数: 280半角文字（日本語140文字）厳格
- スレッド最適: 5-10ツイート（最適7）
- ハッシュタグ: 一切使用しない（Xアルゴリズムで不要、かつSNS横断使用を避けるため）

### Threads投稿
- 文字数: 300-500字（厳守）
- 段落数: 2-4段落（空白2行禁止）
- 絵文字: 3-5個
- 口語体: 3-5回
- ハッシュタグ: 一切使用しない（SNS横断での重複コンテンツ回避のため）

### Late API
- レート制限: 300リクエスト/分
- タイムアウト: 30秒
- 予約投稿キャンセル: ダッシュボード手動削除のみ

---

## 参照

- `generate-x-posts/SKILL.md` (v0.4.6) - X投稿スキル
- `threads_patterns_config.json` - Threads最適化設定
- `Stock/programs/副業/projects/SNS/scripts/threads_adapter.py` - Threads Adapter
- `Stock/programs/副業/projects/SNS/scripts/late_api_scheduler.py` - Late API Scheduler
- `Flow/202601/2026-01-06/x_threads_simultaneous_posting_design.md` - 詳細設計書

---

**バージョン**: v1.0
**作成日**: 2026-01-06
**最終更新**: 2026-01-06
