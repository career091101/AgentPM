# X & Threads 同時投稿スキル 詳細設計書

**作成日**: 2026-01-06
**バージョン**: v1.0
**対象スキル**: `generate-x-threads-posts`（新規作成）

---

## 目次

1. [要件定義](#1-要件定義)
2. [機能仕様](#2-機能仕様)
3. [技術設計](#3-技術設計)
4. [実装計画](#4-実装計画)
5. [テスト計画](#5-テスト計画)
6. [運用・保守](#6-運用保守)

---

## 1. 要件定義

### 1.1 ユーザー要件

| 項目 | 要件内容 | 優先度 |
|------|---------|--------|
| **投稿内容** | 各プラットフォーム最適化版を生成 | P0 |
| **画像・メディア** | 同一画像を両方に添付 | P0 |
| **エラーハンドリング** | リトライ機能付き（2-3回） | P0 |
| **投稿タイミング** | 予約投稿（14日先までの空き日の20時） | P0 |
| **投稿頻度制御** | 1日1投稿のみ（複数予約がある日はスキップ） | P0 |
| **トン＆マナー** | Xの既存スキル（generate-x-posts）を参照 | P0 |

### 1.2 機能要件

#### FR-1: プラットフォーム別コンテンツ生成

- **X版**:
  - 既存の`generate-x-posts`スキル（v0.4.6）のロジックを流用
  - スレッド形式（5-10ツイート、最適7ツイート）
  - 280文字/ツイート制限（半角140文字）
  - バズ構文84パターンから最適選択
  - ハッシュタグ2個

- **Threads版**:
  - X版をベースに500文字以内に最適化
  - 2-4段落構成（空白2行で自動ツリー化を回避）
  - ハッシュタグ1個（トピックタグのみ）
  - 絵文字3-5個（5-8%）
  - よりカジュアルなトーン（口語体3-5回）

#### FR-2: 予約投稿スケジューリング

- Late API経由で既存予約投稿を取得（`GET /posts?status=scheduled`）
- 翌日から14日先までの期間を検索
- 20:00（JST）に予約投稿が入っていない日を特定
- 1日1投稿のみ（複数予約がある日はスキップ）
- 検索範囲内に空き日がない場合はエラー通知

#### FR-3: エラーハンドリング・リトライ

| エラー種別 | リトライ回数 | 待機時間 | 対応 |
|-----------|------------|---------|------|
| **401 Unauthorized** | 0回 | - | 即時停止、API設定確認 |
| **429 Rate Limit** | 1回 | 1時間 | 1時間後に再実行 |
| **Network Timeout** | 3回 | 10秒 | 指数バックオフ（10秒→20秒→40秒） |
| **400 Bad Request** | 0回 | - | エラー詳細ログ、該当案スキップ |
| **500+ Server Error** | 3回 | 30秒 | 30秒待機後リトライ |

#### FR-4: 画像添付

- 同一画像ファイルをX・Threads両方に添付
- Late APIの`media`フィールドを使用
- 対応形式: PNG, JPEG, GIF（最大10MB）
- 画像なしの場合はテキストのみ投稿

### 1.3 非機能要件

| 項目 | 要件 |
|------|------|
| **パフォーマンス** | 総実行時間 5分以内（画像なし）、10分以内（画像あり） |
| **可用性** | エラー時の部分成功許容（X成功・Threads失敗でもOK） |
| **保守性** | 既存スキル（generate-x-posts）のコード再利用率70%以上 |
| **拡張性** | 将来的にInstagram、LinkedIn追加可能な設計 |

---

## 2. 機能仕様

### 2.1 処理フロー全体図

```
[STEP 1] 入力検証・準備（1分）
    ├── トピック/URL/キーワード判定
    ├── 画像ファイル存在確認
    └── Late API設定ロード
         ↓
[STEP 2] X版コンテンツ生成（2-3分）
    ├── generate-x-posts ロジック流用
    ├── スレッド生成（7ツイート想定）
    ├── バズ構文選択
    └── エンゲージメント予測
         ↓
[STEP 3] Threads版コンテンツ生成（1-2分）
    ├── X版を500文字に最適化
    ├── 段落構成調整（2-4段落）
    ├── 絵文字追加（3-5個）
    └── 口語体増強（3-5回）
         ↓
[STEP 4] 予約投稿スケジューリング（30秒）
    ├── Late API既存予約取得
    ├── 14日先までの空き日検索
    └── 20:00 JST予約日時決定
         ↓
[STEP 5] Late API予約投稿（1-2分）
    ├── X: スレッド投稿（threadItems使用）
    ├── Threads: 単一投稿
    └── エラーハンドリング・リトライ
         ↓
[STEP 6] 結果サマリー出力（10秒）
    ├── 投稿ID記録
    ├── スケジュール日時確認
    └── エンゲージメント予測表示
```

### 2.2 STEP別詳細仕様

#### STEP 1: 入力検証・準備

**入力パラメータ**:

```json
{
  "input_type": "topic|article_url|keyword",
  "input_value": "投稿内容/URL/キーワード",
  "image_path": "/path/to/image.png",  // オプション
  "scheduled_date": "2026-01-07",      // オプション（未指定時は自動検索）
  "x_account_id": "twitter_account_xxx",
  "threads_account_id": "threads_account_xxx"
}
```

**検証項目**:
- `input_type`が`topic`, `article_url`, `keyword`のいずれか
- `input_value`が空文字でない
- `image_path`が指定されている場合、ファイル存在確認
- Late API設定ファイル（`late_api_config.json`）の読み込み

#### STEP 2: X版コンテンツ生成

**流用元**: `generate-x-posts/SKILL.md` (v0.4.6)

**主要処理**:

1. **コンテンツ準備**（STEP 1と同様）
   - topic型: LLM直接推論
   - URL型: WebFetch + 要約
   - keyword型: WebSearch + Top 3統合

2. **スレッド生成**（STEP 2）
   - バズ構文選択（84パターンから3つ）
   - セマンティック分割（LLM自然言語理解）
   - 文字数検証（280カウント/ツイート）

3. **エンゲージメント予測**（STEP 4）
   - X公式アルゴリズムスコア計算
   - Recency Factor適用
   - Premium優遇・時間帯補正

**出力例**:

```json
{
  "format": "thread",
  "thread_tweets": [
    {
      "tweet_number": "1/7",
      "content": "🚨 OpenAIが「ひっそり公開」したGPT-5.2プロンプトガイド、これガチでヤバいです...",
      "character_count": {"total": 134, "japanese": 67}
    },
    ...
  ],
  "engagement_prediction": {
    "predicted_likes": 120,
    "predicted_retweets": 18,
    "predicted_replies": 10,
    "x_algorithm_score": 173.0,
    "estimated_reach": 1500
  }
}
```

#### STEP 3: Threads版コンテンツ生成

**ベース**: STEP 2のX版コンテンツ

**変換ロジック**:

```python
def convert_x_to_threads(x_thread: list[str]) -> str:
    """X版スレッドをThreads版に変換"""

    # 1. 全ツイートを結合
    full_text = "\n\n".join(x_thread)

    # 2. 500文字以内に要約（LLM使用）
    prompt = f"""
    以下のX投稿スレッドをThreads向けに最適化してください。

    **要件**:
    - 文字数: 300-500字（厳守）
    - 段落: 2-4段落（空白2行で区切らない）
    - 絵文字: 3-5個追加
    - 口語体: 3-5回使用（例: 「つまり」「ぶっちゃけ」「マジで」）
    - ハッシュタグ: 1個のみ（トピックタグ）

    **元のX投稿**:
    {full_text}
    """

    threads_content = llm_invoke(prompt)

    # 3. 検証
    assert 300 <= len(threads_content) <= 500, "文字数超過"
    assert threads_content.count("\n\n") <= 3, "段落過多"

    return threads_content
```

**調整ポイント**:

| 要素 | X版 | Threads版 | 調整理由 |
|------|-----|-----------|---------|
| **文字数** | 700-1500字 | 300-500字 | 500字制限対応 |
| **段落数** | 4-8段落 | 2-4段落 | 空白2行でツリー化回避 |
| **絵文字** | 0-2個 | 3-5個 | 若年層ユーザー層 |
| **口語体** | 2回 | 3-5回 | カジュアルトーン |
| **ハッシュタグ** | 2個 | 1個 | 過多は読みにくさ増 |

**出力例**:

```json
{
  "platform": "threads",
  "content": "🚨 OpenAIがひっそり公開したGPT-5.2プロンプトガイド、マジでヤバいです\n\n...\n\n#AIプロンプト",
  "character_count": 480,
  "emoji_count": 3,
  "informal_expressions": ["マジで", "つまり", "ぶっちゃけ"],
  "paragraph_count": 3
}
```

#### STEP 4: 予約投稿スケジューリング

**処理フロー**:

```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def find_available_slot(days_ahead: int = 14) -> datetime:
    """14日先までの空き日を検索"""

    jst = ZoneInfo('Asia/Tokyo')

    # 1. 既存予約を取得
    response = requests.get(
        f"{base_url}/posts",
        params={'status': 'scheduled'},
        headers={'Authorization': f'Bearer {api_key}'}
    )

    # 2. 20:00 JST予約済み日付を抽出
    reserved_dates = set()
    for post in response.json().get('posts', []):
        dt = datetime.fromisoformat(post['scheduledFor'].replace('Z', '+00:00'))
        dt_jst = dt.astimezone(jst)
        if dt_jst.hour == 20 and dt_jst.minute == 0:
            reserved_dates.add(dt_jst.date())

    # 3. 利用可能日を検索（翌日から14日先まで）
    current_date = (datetime.now(jst) + timedelta(days=1)).date()
    end_date = current_date + timedelta(days=days_ahead)

    while current_date <= end_date:
        if current_date not in reserved_dates:
            # 20:00 JST で予約日時を作成
            scheduled_dt = datetime.combine(
                current_date,
                datetime.min.time().replace(hour=20, minute=0),
                tzinfo=jst
            )
            return scheduled_dt
        current_date += timedelta(days=1)

    # 空き日が見つからない場合
    raise ValueError(f"14日先まで空き日がありません（検索範囲: {days_ahead}日）")
```

**ユーザー指定日の処理**:

```python
if scheduled_date:  # ユーザーが日付を指定した場合
    scheduled_dt = datetime.combine(
        datetime.strptime(scheduled_date, "%Y-%m-%d").date(),
        datetime.min.time().replace(hour=20, minute=0),
        tzinfo=ZoneInfo('Asia/Tokyo')
    )

    # 競合チェック
    if scheduled_dt.date() in reserved_dates:
        raise ValueError(f"{scheduled_date}は既に20:00に予約投稿があります")
else:
    scheduled_dt = find_available_slot(days_ahead=14)
```

#### STEP 5: Late API予約投稿

**X版（スレッド投稿）**:

```python
def post_x_thread(tweets: list[str], scheduled_dt: datetime) -> dict:
    """Xスレッド投稿"""

    # ISO8601形式に変換（+09:00付き）
    iso_str = scheduled_dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    iso_str = iso_str[:-2] + ':' + iso_str[-2:]  # +0900 → +09:00

    payload = {
        'content': tweets[0],  # 1ツイート目は必須
        'scheduledFor': iso_str,
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'twitter',
            'accountId': x_account_id,
            'platformSpecificData': {
                'threadItems': [{'content': tweet} for tweet in tweets[1:]]
            }
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    if image_path:
        payload['media'] = [{'url': upload_image_to_late(image_path)}]

    response = requests.post(
        f"{base_url}/posts",
        headers={'Authorization': f'Bearer {api_key}'},
        json=payload,
        timeout=30
    )

    return handle_response(response)
```

**Threads版（単一投稿）**:

```python
def post_threads(content: str, scheduled_dt: datetime) -> dict:
    """Threads投稿"""

    iso_str = scheduled_dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    iso_str = iso_str[:-2] + ':' + iso_str[-2:]

    payload = {
        'content': content,
        'scheduledFor': iso_str,
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'threads',
            'accountId': threads_account_id
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    if image_path:
        payload['media'] = [{'url': upload_image_to_late(image_path)}]

    response = requests.post(
        f"{base_url}/posts",
        headers={'Authorization': f'Bearer {api_key}'},
        json=payload,
        timeout=30
    )

    return handle_response(response)
```

**リトライロジック**:

```python
def post_with_retry(post_func, max_retries: int = 3) -> dict:
    """リトライ付き投稿"""

    for attempt in range(max_retries):
        try:
            return post_func()
        except RateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = 3600  # 1時間
                print(f"Rate Limit検出、{wait_time}秒待機中...")
                time.sleep(wait_time)
            else:
                raise
        except NetworkTimeoutError as e:
            if attempt < max_retries - 1:
                wait_time = 10 * (2 ** attempt)  # 指数バックオフ
                print(f"Timeout検出、{wait_time}秒待機中...")
                time.sleep(wait_time)
            else:
                raise
        except AuthenticationError:
            # 401は即時停止
            raise
        except BadRequestError as e:
            # 400は即時停止
            print(f"Bad Request: {e}")
            raise
```

#### STEP 6: 結果サマリー出力

**出力形式**（JSON + Markdown）:

```json
{
  "execution_timestamp": "2026-01-06T15:30:00+09:00",
  "scheduled_datetime": "2026-01-08T20:00:00+09:00",
  "results": {
    "x": {
      "status": "success",
      "post_id": "695ceb1e8247cf816ba753b6",
      "format": "thread",
      "tweet_count": 7,
      "engagement_prediction": {
        "predicted_likes": 120,
        "predicted_retweets": 18,
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
  "image_attached": true,
  "retry_count": {
    "x": 0,
    "threads": 1
  }
}
```

**Markdown出力**（`/Flow/202601/2026-01-06/post_result_YYYYMMDD_HHMMSS.md`）:

```markdown
# X & Threads 同時投稿結果

**実行日時**: 2026-01-06 15:30:00 JST
**予約日時**: 2026-01-08 20:00:00 JST

## X投稿

### ステータス
✅ 成功（Post ID: 695ceb1e8247cf816ba753b6）

### コンテンツ（スレッド7ツイート）
1/7: 🚨 OpenAIが「ひっそり公開」したGPT-5.2プロンプトガイド...
2/7: つまり、プロンプトエンジニアリングの「常識」が...
...

### エンゲージメント予測
- いいね: 120件
- リツイート: 18件
- リプライ: 10件
- Xアルゴリズムスコア: 173.0
- 推定リーチ: 1,500人

---

## Threads投稿

### ステータス
✅ 成功（Post ID: 695ceb1e8247cf816ba753b7）

### コンテンツ
🚨 OpenAIがひっそり公開したGPT-5.2プロンプトガイド、マジでヤバいです

[本文480文字]

#AIプロンプト

### メトリクス
- 文字数: 480文字
- 絵文字: 3個
- 口語体: 3回

---

## 画像
✅ 添付済み: `/path/to/image.png`

## リトライ履歴
- X: 0回
- Threads: 1回（Network Timeout → 成功）
```

---

## 3. 技術設計

### 3.1 アーキテクチャ設計

```
┌─────────────────────────────────────────────────────────┐
│  Claude Code Skill: generate-x-threads-posts            │
│  (新規作成)                                              │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
┌─────────────────┐                  ┌─────────────────┐
│ generate-x-posts│                  │ Late API        │
│ (v0.4.6)        │                  │ Integration     │
│                 │                  │                 │
│ - スレッド生成  │                  │ - 予約投稿      │
│ - バズ構文選択  │                  │ - 競合検出      │
│ - ER予測        │                  │ - リトライ      │
└─────────────────┘                  └─────────────────┘
        │                                     │
        │                                     │
        ▼                                     ▼
┌─────────────────┐                  ┌─────────────────┐
│ Threads Adapter │                  │ late_api_utils  │
│ (新規作成)      │                  │ (既存)          │
│                 │                  │                 │
│ - 文字数調整    │                  │ - 設定読込      │
│ - 絵文字追加    │                  │ - エラー処理    │
│ - 口語体増強    │                  │                 │
└─────────────────┘                  └─────────────────┘
```

### 3.2 コンポーネント設計

#### コンポーネント1: メインオーケストレーター

**ファイル**: `.claude/skills/generate-x-threads-posts/SKILL.md`

**責務**:
- 全体フロー制御（STEP 1-6）
- 入力検証
- 結果サマリー生成

**依存関係**:
- `generate-x-posts/SKILL.md` (v0.4.6)
- `late_api_utils.py`
- `threads_adapter.py` (新規)

#### コンポーネント2: Threads Adapter

**ファイル**: `Stock/programs/副業/projects/SNS/scripts/threads_adapter.py` (新規)

**責務**:
- X版コンテンツをThreads版に変換
- 文字数・段落・絵文字・口語体の調整

**主要関数**:

```python
def convert_x_to_threads(
    x_thread: list[str],
    target_length: tuple[int, int] = (300, 500),
    emoji_count: tuple[int, int] = (3, 5),
    informal_count: tuple[int, int] = (3, 5)
) -> dict:
    """X版スレッドをThreads版に変換

    Args:
        x_thread: Xスレッドの各ツイート
        target_length: 目標文字数範囲
        emoji_count: 絵文字数範囲
        informal_count: 口語体回数範囲

    Returns:
        {
            "content": str,
            "character_count": int,
            "emoji_count": int,
            "informal_expressions": list[str],
            "paragraph_count": int
        }
    """
```

#### コンポーネント3: Late API Scheduler

**ファイル**: `Stock/programs/副業/projects/SNS/scripts/late_api_scheduler.py` (新規)

**責務**:
- 既存予約投稿の取得
- 空き日検索（14日先まで）
- 20:00 JST予約日時生成

**主要関数**:

```python
def find_available_slot(
    days_ahead: int = 14,
    target_hour: int = 20,
    target_minute: int = 0,
    config_path: str = None
) -> datetime:
    """空き日検索"""

def get_existing_reservations(
    config_path: str = None
) -> set[datetime.date]:
    """既存予約日付を取得"""

def schedule_post(
    content: str,
    platform: str,
    account_id: str,
    scheduled_dt: datetime,
    image_path: str = None,
    config_path: str = None
) -> dict:
    """Late API予約投稿（リトライ付き）"""
```

### 3.3 データ設計

#### 設定ファイル

**パス**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`

**拡張項目**:

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

#### Threads設定ファイル

**パス**: `.claude/skills/generate-x-threads-posts/threads_patterns_config.json`

**内容**:

```json
{
  "character_limits": {
    "min": 300,
    "max": 500
  },
  "paragraph_limits": {
    "min": 2,
    "max": 4
  },
  "emoji_range": {
    "min": 3,
    "max": 5
  },
  "informal_expressions": {
    "target_count": {"min": 3, "max": 5},
    "patterns": [
      "マジで", "ぶっちゃけ", "つまり", "ポイントは",
      "実は", "正直", "これ", "めっちゃ"
    ]
  },
  "hashtag_limit": 1,
  "patterns": [
    {
      "id": 1,
      "name": "ニュース引用 → 深掘り",
      "description": "最新ニュースを引用し、独自の視点で深掘り",
      "priority": 5
    },
    ...
  ]
}
```

### 3.4 エラー設計

#### エラークラス階層

```python
class PostingError(Exception):
    """投稿エラー基底クラス"""

class ValidationError(PostingError):
    """入力検証エラー"""

class ContentGenerationError(PostingError):
    """コンテンツ生成エラー"""

class SchedulingError(PostingError):
    """スケジューリングエラー"""

class NoAvailableSlotError(SchedulingError):
    """空き日なしエラー"""

class LateAPIError(PostingError):
    """Late APIエラー基底クラス"""

class AuthenticationError(LateAPIError):
    """認証エラー（401）"""

class RateLimitError(LateAPIError):
    """レート制限エラー（429）"""

class BadRequestError(LateAPIError):
    """リクエスト不正エラー（400）"""

class NetworkTimeoutError(LateAPIError):
    """ネットワークタイムアウト"""
```

---

## 4. 実装計画

### 4.1 タスク分解

| タスクID | タスク名 | 所要時間 | 依存関係 | 優先度 |
|---------|---------|---------|---------|--------|
| **T1** | Threads Adapter実装 | 2時間 | - | P0 |
| **T2** | Late API Scheduler実装 | 2時間 | - | P0 |
| **T3** | メインスキル実装（SKILL.md） | 3時間 | T1, T2 | P0 |
| **T4** | エラーハンドリング強化 | 1時間 | T3 | P0 |
| **T5** | ユニットテスト作成 | 2時間 | T3 | P1 |
| **T6** | 統合テスト | 1時間 | T5 | P1 |
| **T7** | ドキュメント整備 | 1時間 | T6 | P2 |
| **合計** | - | **12時間** | - | - |

### 4.2 実装順序

#### フェーズ1: コア機能実装（6時間）

1. **Threads Adapter作成**（T1）
   - `threads_adapter.py`の実装
   - LLMプロンプト最適化
   - 文字数・絵文字・口語体調整ロジック

2. **Late API Scheduler作成**（T2）
   - `late_api_scheduler.py`の実装
   - 既存予約取得API呼び出し
   - 空き日検索アルゴリズム
   - リトライロジック

3. **メインスキル実装**（T3）
   - `SKILL.md`の作成
   - STEP 1-6の実装
   - `generate-x-posts`との統合

#### フェーズ2: 品質保証（4時間）

4. **エラーハンドリング強化**（T4）
   - エラークラス実装
   - リトライロジック精緻化
   - ログ出力強化

5. **ユニットテスト作成**（T5）
   - `test_threads_adapter.py`
   - `test_late_api_scheduler.py`
   - モックAPI使用

6. **統合テスト**（T6）
   - 実際のLate API呼び出し（Sandbox環境）
   - エンドツーエンドテスト

#### フェーズ3: 仕上げ（2時間）

7. **ドキュメント整備**（T7）
   - README.md作成
   - サンプルコード追加
   - トラブルシューティングガイド

### 4.3 ディレクトリ構造

```
aipm_v0/
├── .claude/
│   └── skills/
│       └── generate-x-threads-posts/        # 新規
│           ├── SKILL.md                     # メインスキル定義
│           ├── threads_patterns_config.json # Threads設定
│           ├── README.md                    # 使用方法
│           └── examples/                    # サンプル
│               ├── sample_input.json
│               └── sample_output.md
├── Stock/
│   └── programs/
│       └── 副業/
│           └── projects/
│               └── SNS/
│                   ├── scripts/
│                   │   ├── threads_adapter.py      # 新規
│                   │   ├── late_api_scheduler.py   # 新規
│                   │   ├── late_api_utils.py       # 既存（拡張）
│                   │   └── late_api_post.py        # 既存
│                   ├── config/
│                   │   └── late_api_config.json    # 既存（拡張）
│                   └── tests/                      # 新規
│                       ├── test_threads_adapter.py
│                       └── test_late_api_scheduler.py
└── Flow/
    └── 202601/
        └── 2026-01-06/
            ├── x_threads_simultaneous_posting_design.md  # 本ドキュメント
            ├── threads_optimization_analysis.md          # 調査レポート
            └── threads_patterns_config.json              # Threads設定（草案）
```

---

## 5. テスト計画

### 5.1 ユニットテスト

#### テストケース1: Threads Adapter

**ファイル**: `tests/test_threads_adapter.py`

```python
import pytest
from scripts.threads_adapter import convert_x_to_threads

def test_convert_basic():
    """基本的な変換テスト"""
    x_thread = [
        "1/3: これがテストです",
        "2/3: 詳細説明",
        "3/3: 結論"
    ]
    result = convert_x_to_threads(x_thread)

    assert 300 <= result['character_count'] <= 500
    assert 2 <= result['paragraph_count'] <= 4
    assert 3 <= result['emoji_count'] <= 5

def test_convert_long_thread():
    """長いスレッドの変換テスト"""
    x_thread = ["ツイート" + str(i) for i in range(10)]
    result = convert_x_to_threads(x_thread)

    assert result['character_count'] <= 500

def test_informal_expressions():
    """口語体追加テスト"""
    x_thread = ["これはテストです"]
    result = convert_x_to_threads(x_thread)

    assert len(result['informal_expressions']) >= 3
```

#### テストケース2: Late API Scheduler

**ファイル**: `tests/test_late_api_scheduler.py`

```python
import pytest
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from scripts.late_api_scheduler import find_available_slot, get_existing_reservations

@pytest.fixture
def mock_late_api(monkeypatch):
    """Late APIモック"""
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return {
                    'posts': [
                        {
                            'scheduledFor': '2026-01-07T20:00:00+09:00'
                        }
                    ]
                }
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)

def test_find_available_slot_success(mock_late_api):
    """空き日検索成功テスト"""
    result = find_available_slot(days_ahead=14)

    assert result is not None
    assert result.hour == 20
    assert result.minute == 0
    assert result.date() != datetime(2026, 1, 7).date()

def test_find_available_slot_no_slots(mock_late_api):
    """空き日なしエラーテスト"""
    # 全日予約済みのモックに変更
    with pytest.raises(ValueError, match="14日先まで空き日がありません"):
        find_available_slot(days_ahead=1)

def test_get_existing_reservations(mock_late_api):
    """既存予約取得テスト"""
    reserved = get_existing_reservations()

    assert datetime(2026, 1, 7).date() in reserved
```

### 5.2 統合テスト

#### テストケース3: エンドツーエンド

**ファイル**: `tests/test_integration.py`

```python
import pytest
from claude_skills import execute_skill

@pytest.mark.integration
def test_full_flow_with_sandbox():
    """Sandbox環境での完全フローテスト"""

    input_data = {
        "input_type": "topic",
        "input_value": "AIの最新動向",
        "x_account_id": "sandbox_twitter_xxx",
        "threads_account_id": "sandbox_threads_xxx"
    }

    result = execute_skill('generate-x-threads-posts', input_data)

    # X投稿成功確認
    assert result['results']['x']['status'] == 'success'
    assert 'post_id' in result['results']['x']

    # Threads投稿成功確認
    assert result['results']['threads']['status'] == 'success'
    assert 'post_id' in result['results']['threads']

    # スケジュール確認
    assert result['scheduled_datetime'] is not None

@pytest.mark.integration
def test_retry_on_network_error(monkeypatch):
    """ネットワークエラー時のリトライテスト"""

    call_count = 0

    def mock_post(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise NetworkTimeoutError("Timeout")
        return {'post_id': 'success_after_retry'}

    monkeypatch.setattr('requests.post', mock_post)

    # 2回リトライ後に成功するはず
    result = execute_skill('generate-x-threads-posts', {...})

    assert call_count == 3
    assert result['retry_count']['x'] == 2
```

### 5.3 テストデータ

#### サンプル入力1: トピック型

```json
{
  "input_type": "topic",
  "input_value": "OpenAIのGPT-5.2プロンプトガイドが公開され、プロンプトエンジニアリングの常識が変わりつつある",
  "x_account_id": "twitter_account_xxx",
  "threads_account_id": "threads_account_xxx"
}
```

#### サンプル入力2: URL型（画像あり）

```json
{
  "input_type": "article_url",
  "input_value": "https://example.com/ai-news",
  "image_path": "/path/to/image.png",
  "x_account_id": "twitter_account_xxx",
  "threads_account_id": "threads_account_xxx"
}
```

#### サンプル入力3: 日付指定

```json
{
  "input_type": "keyword",
  "input_value": "生成AI 最新動向",
  "scheduled_date": "2026-01-10",
  "x_account_id": "twitter_account_xxx",
  "threads_account_id": "threads_account_xxx"
}
```

---

## 6. 運用・保守

### 6.1 モニタリング

#### 投稿成功率の追跡

```python
# Stock/programs/副業/projects/SNS/monitoring/post_success_rate.py

def track_success_rate():
    """過去30日間の投稿成功率を集計"""

    results = load_results_from_last_30_days()

    total = len(results)
    x_success = sum(1 for r in results if r['x']['status'] == 'success')
    threads_success = sum(1 for r in results if r['threads']['status'] == 'success')

    print(f"X投稿成功率: {x_success / total * 100:.1f}%")
    print(f"Threads投稿成功率: {threads_success / total * 100:.1f}%")
    print(f"両方成功率: {sum(1 for r in results if r['x']['status'] == 'success' and r['threads']['status'] == 'success') / total * 100:.1f}%")
```

#### エラーログ分析

```python
# Stock/programs/副業/projects/SNS/monitoring/error_analysis.py

def analyze_errors():
    """エラー種別の統計を取得"""

    error_logs = load_error_logs()

    error_types = {}
    for log in error_logs:
        error_type = log.get('error_type', 'Unknown')
        error_types[error_type] = error_types.get(error_type, 0) + 1

    for error_type, count in sorted(error_types.items(), key=lambda x: -x[1]):
        print(f"{error_type}: {count}件")
```

### 6.2 保守タスク

#### 週次タスク

- [ ] 投稿成功率の確認（目標: 95%以上）
- [ ] エラーログの確認
- [ ] 予約投稿スケジュールの確認（競合なし）

#### 月次タスク

- [ ] Late API使用量の確認（レート制限に抵触していないか）
- [ ] エンゲージメント予測精度の検証
- [ ] Threads設定の見直し（文字数、絵文字、口語体の最適化）

#### 四半期タスク

- [ ] バズ構文パターンの更新（新しいトレンド反映）
- [ ] Threads最適化パターンの見直し
- [ ] A/Bテスト結果の分析

### 6.3 トラブルシューティング

#### 問題1: 予約投稿が14日先まで埋まっている

**原因**: 大量のスケジュール予約

**対応**:
1. `get_existing_reservations()`で既存予約を確認
2. 不要な予約をLate APIダッシュボードから削除
3. `days_ahead`パラメータを30に拡張（緊急時）

#### 問題2: Threads投稿が500文字を超過

**原因**: LLM生成時の文字数制御不良

**対応**:
1. `convert_x_to_threads()`のプロンプトを修正
2. `target_length=(280, 480)`に下方修正（安全マージン）
3. 生成後の文字数検証を強化

#### 問題3: X投稿がスレッド化されない

**原因**: `threadItems`の形式不正

**対応**:
1. `{"content": "..."}` 形式を使用（`{"text": "..."}`は不可）
2. 1ツイート目は`content`フィールドに配置
3. Late APIレスポンスのエラー詳細を確認

---

## 付録

### A. 参照ドキュメント

| ドキュメント | パス | 用途 |
|------------|------|------|
| **X投稿スキル** | `.claude/skills/generate-x-posts/SKILL.md` | スレッド生成ロジック流用 |
| **Late API設定ガイド** | `Stock/programs/副業/projects/SNS/config/LATE_API_SETUP_GUIDE.md` | Late API基本設定 |
| **Late API統合ガイド** | `.claude/skills/sns-automation/late_api_integration_guide.md` | エラーハンドリング |
| **Threads最適化分析** | `Flow/202601/2026-01-06/threads_optimization_analysis.md` | Threads特化設計 |
| **Late API予約投稿ガイド** | `.claude/skills/sns-automation/LATE_API_SCHEDULED_POSTING_GUIDE.md` | 予約投稿実装 |

### B. 用語集

| 用語 | 定義 |
|------|------|
| **バズ構文** | エンゲージメントを高めるための文章パターン（84種類） |
| **ER（Engagement Rate）** | エンゲージメント率（いいね+RT+リプライ / フォロワー数） |
| **JST** | 日本標準時（UTC+9） |
| **Late API** | SNS予約投稿サービスのAPI |
| **threadItems** | Late APIでスレッド投稿を行う際のフィールド |
| **スレッド分割** | 長文を複数ツイートに分割する処理 |
| **空き日検索** | 既存予約と競合しない日付を自動検索する処理 |

### C. 変更履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| **v1.0** | 2026-01-06 | 初版作成（詳細設計書完成） |

---

**作成者**: Claude Sonnet 4.5
**最終更新**: 2026-01-06
**ドキュメントステータス**: ✅ 完成（実装準備完了）
