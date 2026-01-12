# create-viral-x-thread Skill

海外のバズX投稿を収集し、技術解説スレッド＆画像を生成してSlack承認経由でLate APIに予約投稿するスキル。

## Metadata

```yaml
name: create-viral-x-thread
version: 0.1.0-alpha (Phase 1のみ実装)
description: 海外バズX投稿からエンゲージメント最適化したスレッドを自動生成・予約投稿
triggers:
  - "バズ投稿からスレッド作成"
  - "AIトレンド投稿生成"
  - "/create-viral-x-thread"
automation_level: full_auto
execution_frequency: daily (20:00 JST投稿予定)
status: Phase 1実装中
```

## 実装ステータス

| Phase | 機能 | ステータス | 実行時間目安 |
|-------|------|-----------|-------------|
| Phase 1 | バズ投稿収集 | ✅ 実装完了 | 5-7分 |
| Phase 2 | スレッド生成 | ✅ 実装完了 | 10-15分 |
| Phase 3 | 画像生成 | ✅ 実装中 | 5-10分 |
| Phase 4 | Slack承認 | 🔜 未実装 | 待機 |
| Phase 5 | Late API予約 | 🔜 未実装 | 5分 |

---

## Phase 1: バズ投稿収集（実装済み）

### 目的
Claude in Chromeを使って、海外のAI関連バズ投稿を自動収集。

### 収集条件
- **対象**: 過去24時間のX投稿
- **検索クエリ**: `(Claude OR GPT OR Gemini OR AI) min_retweets:100 lang:en`
- **収集件数**: 10-20件
- **フィルタ**: RT 100以上、AI/Claude/GPT/Gemini関連

### 実行方法

#### オプション1: Skillコマンドとして実行
```bash
/create-viral-x-thread --phase 1
```

#### オプション2: 直接プロンプト実行
```
「バズ投稿からスレッド作成」を実行してください。Phase 1（収集）のみ実行。
```

### 実行フロー

```mermaid
graph LR
    A[スキル起動] --> B[Claude in Chrome起動]
    B --> C[X.com検索]
    C --> D[投稿収集]
    D --> E[JSON保存]
    E --> F[完了通知]
```

### 出力ファイル

**保存先**: `Stock/programs/副業/projects/SNS/data/viral_posts_YYYYMMDD.json`

**フォーマット**:
```json
{
  "collected_at": "2026-01-03T10:00:00+09:00",
  "search_query": "(Claude OR GPT OR Gemini OR AI) min_retweets:100 lang:en",
  "total_collected": 12,
  "posts": [
    {
      "rank": 1,
      "url": "https://x.com/bcherry/status/2007296114656194730",
      "author": "@bcherry",
      "author_name": "Boris Cherny",
      "content": "1/ I run 5 Claudes in parallel in my terminal...",
      "engagement": {
        "retweets": 150,
        "likes": 500,
        "replies": 30,
        "views": 12000
      },
      "posted_at": "2026-01-02T18:30:00Z",
      "topic_detected": "Claude Code Tips",
      "is_thread": true,
      "thread_length": 13
    }
  ]
}
```

---

## 実装詳細（Phase 1）

### Task実行パターン

```python
from task import Task
import os
from datetime import datetime

# 環境変数
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
today = datetime.now().strftime("%Y%m%d")

# Phase 1: バズ投稿収集（general-purposeサブエージェント）
task_result = Task(
    description="海外バズX投稿を収集",
    subagent_type="general-purpose",
    model="haiku",  # 軽量タスクなのでhaiku
    prompt=f"""
    あなたはX（Twitter）のバズ投稿収集エージェントです。
    Claude in Chromeを使って、以下の手順でAI関連のバズ投稿を収集してください。

    ## 実行手順

    ### 1. ブラウザ準備
    - `tabs_context_mcp(createIfEmpty=true)` でタブ取得
    - `tabs_create_mcp()` で新規タブ作成（既存タブがある場合）

    ### 2. X.com検索
    - `navigate(url="https://x.com/search?q=(Claude%20OR%20GPT%20OR%20Gemini%20OR%20AI)%20min_retweets:100%20lang:en&src=typed_query&f=live")`
    - 「最新」タブに切り替え（既にURLに`f=live`が含まれているので不要かも）
    - 3秒待機（`computer(action="wait", duration=3)`）

    ### 3. 投稿収集
    - `read_page(tabId=xxx, filter="all")` でページ全体を解析
    - または `find(query="tweet with high engagement")` で投稿要素を特定
    - 上位10-20件の投稿から以下を抽出:
      - URL（投稿リンク）
      - 著者（@username）
      - 著者名（表示名）
      - 投稿内容（全文）
      - RT数、いいね数、返信数
      - 投稿日時
      - スレッドかどうか（「このスレッドを表示」があるか）
      - スレッド長（推定）

    ### 4. トピック検出
    - 各投稿の内容から主要トピックを推測:
      - "Claude Code Tips"
      - "GPT-5 News"
      - "Gemini Updates"
      - "AI Development"
      - "Prompt Engineering"
      - など

    ### 5. JSON出力
    - 収集したデータを以下の形式でJSON保存:

    ```json
    {{
      "collected_at": "2026-01-03T10:00:00+09:00",
      "search_query": "(Claude OR GPT OR Gemini OR AI) min_retweets:100 lang:en",
      "total_collected": 12,
      "posts": [
        {{
          "rank": 1,
          "url": "...",
          "author": "...",
          "author_name": "...",
          "content": "...",
          "engagement": {{
            "retweets": 150,
            "likes": 500,
            "replies": 30,
            "views": 12000
          }},
          "posted_at": "...",
          "topic_detected": "...",
          "is_thread": true,
          "thread_length": 13
        }}
      ]
    }}
    ```

    - **保存先**: `{SNS_DATA_DIR}/viral_posts_{today}.json`

    ## 注意事項
    - ログイン不要（公開情報のみ収集）
    - RT数が100未満の投稿は除外
    - スクリーンショットは不要（データのみ収集）
    - エラー時は部分的な結果でも保存すること
    - タイムアウト: 20分

    ## 完了条件
    - 10件以上の投稿を収集
    - JSON形式で正しく保存
    - メインセッションに「Phase 1完了、X件収集」と報告

    実行してください。
    """,
    timeout=1200000  # 20分 = 1,200,000ミリ秒
)

print(f"✅ Phase 1完了: {task_result}")
```

---

## エラーハンドリング

### ケース1: X.comアクセス失敗
- **対処**: 3回リトライ、それでも失敗なら前日の収集データを再利用

### ケース2: 投稿が10件未満
- **対処**: RT閾値を50に下げて再検索

### ケース3: タイムアウト（20分超過）
- **対処**: 部分的な結果でも保存し、次回実行時に不足分を補完

---

## 次のPhaseへの接続

Phase 1完了後、以下のファイルがPhase 2（スレッド生成）の入力となります:
- `viral_posts_{today}.json`

Phase 2では、このJSONから最もエンゲージメントが高い投稿を選択し、スレッド生成を行います。

---

## テスト実行ログ（サンプル）

```
[2026-01-03 10:00:00] Phase 1開始
[2026-01-03 10:00:05] タブ作成完了 (tabId: 1816160803)
[2026-01-03 10:00:08] X.com検索ページ表示
[2026-01-03 10:02:15] 投稿収集中... (5/10)
[2026-01-03 10:05:30] 投稿収集中... (10/10)
[2026-01-03 10:07:00] JSON保存完了: viral_posts_20260103.json
[2026-01-03 10:07:01] Phase 1完了 ✅
```

---

## 環境変数（Phase 1不要）

Phase 1はClaude in Chromeのみ使用するため、API Keyは不要です。

---

---

## Phase 2: スレッド生成（実装中）

### 目的
Phase 1で収集したバズ投稿を分析し、日本語の技術解説スレッドを自動生成。エンゲージメント最適化を重視。

### 入力
- **ファイル**: `viral_posts_YYYYMMDD.json` (Phase 1の出力)
- **選択基準**: エンゲージメント最高の投稿を選択

### 処理フロー
1. **投稿選択**: RT数・いいね数・View数の総合スコアでランキング
2. **内容分析**: 投稿本文、トピック、スレッド構成を分析
3. **スレッド設計**: 10-15ツイートの構成を設計
4. **生成**: 各ツイート280字以内、技術解説スタイル
5. **最適化**: フック、数字、具体例を盛り込む

### 出力ファイル

**保存先**: `Stock/programs/副業/projects/SNS/data/thread_generated_YYYYMMDD.json`

**フォーマット**:
```json
{
  "generated_at": "2026-01-03T15:30:00+09:00",
  "source_post": {
    "url": "https://x.com/bcherry/status/2007296114656194730",
    "author": "@bcherry",
    "topic": "Claude Code Tips"
  },
  "thread": [
    {
      "tweet_num": 1,
      "content": "🚨Claude Code開発者が「自分の使い方」を公開\n\n驚いたのは「特別なカスタマイズなしでも十分使える」ということ\n\n1. 5〜15のClaude並列実行\n2. チームでCLAUDE.md共有\n3. Plan modeで計画→一発実装\n4. 検証手段を与えるのが最重要\n\nとのこと\n13のTipsを解説します👇",
      "character_count": 138,
      "image_required": true
    },
    {
      "tweet_num": 2,
      "content": "【Tip 1: 並列実行で効率最大化】\n\nBoris氏はターミナルで5-10のClaudeセッションを同時実行。\n\n各セッションに番号（1-5）を振り、システム通知で入力待ちを検知。\n\n独立したタスクを並列処理することで、待ち時間を大幅削減できます。",
      "character_count": 126,
      "image_required": false
    }
  ],
  "metadata": {
    "total_tweets": 13,
    "total_characters": 2847,
    "estimated_read_time": "3分",
    "topics_covered": [
      "並列実行",
      "CLAUDE.md共有",
      "Plan mode",
      "検証手段",
      "Opus 4.5活用"
    ]
  }
}
```

### 実装詳細

```python
from task import Task
from datetime import datetime
import json

SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
today = datetime.now().strftime("%Y%m%d")

# Phase 1の出力を読み込み
with open(f"{SNS_DATA_DIR}/viral_posts_{today}.json", "r") as f:
    viral_posts = json.load(f)

# Phase 2: スレッド生成（Sonnetエージェント）
task_result = Task(
    description="技術解説スレッドを生成",
    subagent_type="general-purpose",
    model="sonnet",  # 高品質生成のためSonnet
    prompt=f'''
    あなたは日本語技術解説スレッド生成エージェントです。

    ## 入力データ
    {json.dumps(viral_posts, ensure_ascii=False, indent=2)}

    ## タスク
    上記のバズ投稿から**最もエンゲージメントが高い投稿**（通常はrank 1）を選択し、
    日本語の技術解説スレッドを生成してください。

    ## スレッド生成ルール

    ### 1. フックツイート（1ツイート目）
    - 🚨などの注目絵文字で開始
    - 「〜が公開」「驚いたのは〜」など驚きを表現
    - 要約を3-4項目で箇条書き
    - 「Nのポイントを解説👇」で締める
    - 画像必須（image_required: true）
    - 280字以内

    ### 2. 詳細解説ツイート（2-N ツイート目）
    - 各ポイントを1ツイート1トピックで解説
    - 【Tip X: タイトル】形式で開始
    - 具体例、数字、引用を含める
    - 技術的正確性を維持
    - 絵文字は控えめ（タイトルのみ）
    - 各280字以内

    ### 3. スレッド長
    - 元投稿がスレッドの場合: 同程度の長さ（10-15ツイート）
    - 元投稿が単発の場合: 5-7ツイート

    ### 4. トーン
    - 技術解説スタイル（落ち着いた、専門的）
    - エンゲージメント優先（具体例、数字、引用）
    - ですます調

    ## 出力形式

    以下のJSON形式で出力してください:

    ```json
    {{
      "generated_at": "2026-01-03T15:30:00+09:00",
      "source_post": {{
        "url": "...",
        "author": "...",
        "topic": "..."
      }},
      "thread": [
        {{
          "tweet_num": 1,
          "content": "...",
          "character_count": 138,
          "image_required": true
        }},
        {{
          "tweet_num": 2,
          "content": "...",
          "character_count": 126,
          "image_required": false
        }}
      ],
      "metadata": {{
        "total_tweets": 13,
        "total_characters": 2847,
        "estimated_read_time": "3分",
        "topics_covered": ["...", "..."]
      }}
    }}
    ```

    - **保存先**: `{SNS_DATA_DIR}/thread_generated_{today}.json`

    ## 注意事項
    - 各ツイートは必ず280字以内
    - 技術的正確性を最優先
    - エンゲージメント要素（フック、数字、具体例）を必ず含める
    - 元投稿の内容を正確に理解した上で、より分かりやすく解説

    実行してください。
    ''',
    timeout=900000  # 15分
)

print(f"✅ Phase 2完了: {{task_result}}")
```

### 品質基準

| 項目 | 基準 |
|------|------|
| **各ツイート文字数** | 180-280字（280字厳守） |
| **スレッド長** | 10-15ツイート |
| **フック強度** | 絵文字+驚き+要約 |
| **具体性** | 数字・引用を各ツイートに1つ以上 |
| **技術正確性** | 元投稿の内容と矛盾なし |

---

## Phase 3: 画像生成（実装中）

### 目的
NannoBanana API（Gemini）を使って、フックツイート用の視覚的に魅力的な画像を生成。

### 入力
- **ファイル**: `thread_generated_YYYYMMDD.json` (Phase 2の出力)
- **対象**: 1ツイート目（image_required: true）

### API情報

**NannoBanana API (Gemini 2.0 Flash)**
- **エンドポイント**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent`
- **API Key**: `AIzaSyCg1OWV0kETK3OocmDgtf4J5dU-NpfpzGs`
- **モデル**: `gemini-2.0-flash-exp`

### 画像生成フロー

1. **プロンプト設計**: スレッド内容から視覚的要素を抽出
2. **API呼び出し**: Gemini APIでテキストから画像生成
3. **画像保存**: PNG形式で保存
4. **メタデータ更新**: thread_generated.jsonに画像パスを追加

### 出力ファイル

**保存先**: `Stock/programs/副業/projects/SNS/data/thread_image_YYYYMMDD.png`

### 実装詳細

```python
from task import Task
from datetime import datetime
import json
import base64

SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
today = datetime.now().strftime("%Y%m%d")
API_KEY = "AIzaSyCg1OWV0kETK3OocmDgtf4J5dU-NpfpzGs"

# Phase 2の出力を読み込み
with open(f"{SNS_DATA_DIR}/thread_generated_{today}.json", "r") as f:
    thread_data = json.load(f)

first_tweet = thread_data["thread"][0]["content"]
topic = thread_data["source_post"]["topic"]

# Phase 3: 画像生成（Haikuエージェント）
task_result = Task(
    description="NannoBanana APIで画像生成",
    subagent_type="general-purpose",
    model="haiku",  # API呼び出しのみなのでHaiku
    prompt=f'''
    あなたはNannoBanana API（Gemini）を使った画像生成エージェントです。

    ## タスク
    以下のスレッド内容に基づいて、視覚的に魅力的な画像を生成してください。

    ### スレッド情報
    - **トピック**: {topic}
    - **1ツイート目**: {first_tweet}

    ### 画像プロンプト設計ルール

    1. **視覚的要素**:
       - Claude Codeのロゴまたはターミナル画面
       - 並列実行を表す複数のウィンドウ・タブ
       - 技術的な雰囲気（コード、ダイアグラム）
       - 色: 青・紫・オレンジ（Claudeブランドカラー）

    2. **テキストオーバーレイ**:
       - "Claude Code開発者の13のTips"
       - "特別なカスタマイズ不要"
       - など、キーメッセージを含める

    3. **スタイル**:
       - モダン、プロフェッショナル
       - インフォグラフィック風
       - Twitter投稿に適したアスペクト比（16:9または1:1）

    ### API呼び出し

    以下のAPIを使用してください:

    **エンドポイント**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={API_KEY}`

    **リクエスト例**:
    ```json
    {{
      "contents": [
        {{
          "parts": [
            {{
              "text": "Create a modern infographic showing Claude Code parallel execution with 5-15 agents running simultaneously. Include terminal windows, code snippets, and the text 'Claude Code Developer's 13 Tips' in Japanese. Use blue and purple gradient background. Professional tech style."
            }}
          ]
        }}
      ],
      "generationConfig": {{
        "temperature": 0.7,
        "topK": 40,
        "topP": 0.95,
        "maxOutputTokens": 2048
      }}
    }}
    ```

    ### 画像保存

    1. APIレスポンスから画像データを取得（base64またはURL）
    2. PNG形式で保存: `{SNS_DATA_DIR}/thread_image_{today}.png`
    3. メタデータ更新: `thread_generated_{today}.json`に以下を追加:
       ```json
       "thread": [
         {{
           "tweet_num": 1,
           "content": "...",
           "image_required": true,
           "image_path": "{SNS_DATA_DIR}/thread_image_{today}.png"
         }}
       ]
       ```

    ### 注意事項
    - 画像サイズ: 1200x675px (Twitter推奨)
    - ファイル形式: PNG
    - 著作権: オリジナル生成のみ
    - エラー時: デフォルト画像またはスキップ

    実行してください。
    ''',
    timeout=600000  # 10分
)

print(f"✅ Phase 3完了: {{task_result}}")
```

### 画像プロンプトの例

```
Create a professional tech infographic for Twitter post about "Claude Code Developer's 13 Tips".

Visual elements:
- Multiple terminal windows showing parallel execution (5-15 agents)
- Claude Code logo in the corner
- Code snippets in the background
- Gradient background (blue #4A90E2 to purple #9B51E0)
- Clean, modern design

Text overlay (in Japanese):
- Main title: "Claude Code開発者の13のTips"
- Subtitle: "特別なカスタマイズなしでも十分使える"
- Key points:
  * 5〜15の並列実行
  * CLAUDE.md共有
  * Plan mode活用

Style: Professional tech infographic, suitable for Twitter, 16:9 aspect ratio
```

### エラーハンドリング

| エラー | 対処 |
|--------|------|
| **API呼び出し失敗** | 3回リトライ、失敗時はデフォルト画像使用 |
| **生成画像が不適切** | 再生成（プロンプト調整） |
| **タイムアウト** | デフォルト画像使用（Claude Codeロゴ） |
| **画像サイズ不適** | リサイズ処理実行 |

### デフォルト画像

API失敗時の代替案:
- Claude公式ロゴ
- テキストのみの画像（Canva風）
- 既存のClaude Code関連画像

---

## 参照

- @.claude/rules/execution_preference.md - LLM優先アプローチ
- @.claude/rules/parallel_execution.md - 並列エージェント実行
- @Stock/programs/副業/projects/SNS/scripts/approve_and_schedule.py - 既存Slack承認フロー（Phase 4で再利用）
