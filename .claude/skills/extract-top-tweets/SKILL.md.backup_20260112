# extract-top-tweets

---
name: extract-top-tweets
description: |
  Xタイムライン収集データからAI関連の高エンゲージメント投稿Top 10を抽出。
  AI関連キーワードでフィルタリング後、engagement_score（いいね + RT×3 + 返信×5）で順位付け。
  所要時間: 3-5分、出力: top_10_tweets.json
version: 1.1.0
trigger_keywords:
  - "Top 10抽出"
  - "高エンゲージメント投稿"
  - "X投稿ランキング"
  - "AI関連ツイート抽出"
stage: Phase 1a - Data Processing
dependencies:
  - collect-x-timeline
output_file: "Stock/programs/副業/projects/SNS/data/top_10_tweets_{YYYYMMDD}.json"
execution_time: "3-5分"
priority: P0
model: claude-haiku-4-5-20251001  # Haiku 4.5 (2026年1月時点の最新モデル)
thinking: false
---

## Overview

Xタイムライン収集スキル（collect-x-timeline）が収集した200件のツイートデータから、**AI関連ツイートのみを抽出**し、エンゲージメントスコアに基づいて高パフォーマンス投稿Top 10を抽出します。

**AI関連フィルタリング**: ツイート本文にAI関連キーワードが含まれるもののみを対象とします。

**エンゲージメントスコア計算式**:
```
engagement_score = likes + (retweets × 3) + (replies × 5)
```

リプライを最重視（×5）、リツイートを中重視（×3）、いいねを基本値として扱います。

## Instructions

### STEP 1: タイムラインデータ読み込み（1分）

**入力ファイルの特定**:
- 優先順位1: ユーザー指定の日付（`YYYYMMDD`パラメータ）
- 優先順位2: 最新日付のファイルを自動検索

```bash
# 最新ファイル検索例
ls -t Stock/programs/副業/projects/SNS/data/x_timeline_*.json | head -1
```

**ファイル読み込み**:
- Read tool を使用してJSONファイル全体を読み込み
- JSONパース検証（invalid JSONの場合はエラー）

**エラーハンドリング**:
- ファイル未検出時: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- JSONパースエラー: エラーメッセージを表示し、処理中断
- データ件数0件: 警告表示 + 処理中断

---

### STEP 2: エンゲージメントスコア計算（1分）

**処理ロジック**:
```python
for tweet in tweets:
    tweet['engagement_score'] = (
        tweet.get('likes', 0) +
        tweet.get('retweets', 0) * 3 +
        tweet.get('replies', 0) * 5
    )
```

**データバリデーション**:
- 必須フィールドチェック: `likes`, `retweets`, `replies`
- 欠損値の処理: デフォルト値0で補完
- 負の値の処理: 0として扱う（異常データ）

---

### STEP 3: AI関連フィルタリング（LLMサブエージェント使用）（2-3分）

**実行方法**: Claude Code CLIのTask toolでサブエージェントを起動し、LLMの判断でAI関連ツイートを抽出。

**サブエージェント起動**:
```python
Task(
    subagent_type="general-purpose",
    model="haiku",  # コスト効率重視
    prompt=f"""
以下のツイートリストから、AI・機械学習・LLM関連のツイートのみを抽出してください。

**AI関連の判断基準**:
- AI技術（ChatGPT, Claude, Gemini, GPT, LLM, 機械学習, 深層学習など）
- AI企業（OpenAI, Anthropic, Google AI, Microsoft AIなど）
- AI応用（生成AI, 画像生成, プロンプト, エージェントなど）
- AI関連ニュース・議論

**重要**: 政治・経済・エンタメなど、AIと直接関係のないツイートは除外してください。

**入力ツイート**:
{tweets_json}

**出力形式**:
AI関連と判断したツイートのtweet_idのリストをJSON配列で出力してください。
例: ["1234567890", "2345678901", "3456789012"]

AI関連ツイートがない場合は空配列 [] を出力してください。
""",
    description="AI関連ツイートをフィルタリング"
)
```

**処理フロー**:
1. 全ツイートをサブエージェントに渡す
2. LLMがツイート内容を理解し、AI関連かどうかを判断
3. AI関連と判断されたtweet_idリストを取得
4. 該当ツイートのみを抽出

**利点**:
- キーワードマッチングでは拾えない文脈的なAI関連も検出可能
- 誤検出（"AI"を含むがAI関連でないツイート）を削減
- 新しいAI用語にも対応可能

**統計出力**:
- AI関連ツイート数 / 総ツイート数
- AI関連ツイート比率（%）
- LLM判定の信頼度（オプション）

---

### STEP 4: 著名人フィルタリング（30秒）

**世界的著名人の除外**:

以下のアカウントを除外リストとして管理:
- `elonmusk` - Elon Musk
- `BillGates` - Bill Gates
- `BarackObama` - Barack Obama
- `tim_cook` - Tim Cook
- `jeffbezos` - Jeff Bezos
- `sundarpichai` - Sundar Pichai
- その他フォロワー数10M以上のアカウント

**フィルタリングロジック**:
```python
excluded_usernames = ['elonmusk', 'BillGates', 'BarackObama', 'tim_cook', 'jeffbezos', 'sundarpichai']
filtered_tweets = [
    tweet for tweet in ai_tweets
    if tweet.get('username', '').lower() not in [u.lower() for u in excluded_usernames]
]
```

**理由**: 世界的著名人のツイートは参考にならず、ニッチなAI業界特化の示唆が得られない

---

### STEP 5: ソート・Top 10抽出（30秒）

**ソート処理**:
- `engagement_score` の降順でソート
- 同スコアの場合: `created_at`（新しい順）でサブソート

**Top 10抽出**:
```python
top_10_tweets = sorted_tweets[:10]
```

**10件未満の場合**:
- 警告メッセージ: "⚠️ 抽出件数が10件未満です（{N}件）。フィルタ条件を確認してください。"
- 処理継続（全件出力）

---

### STEP 6: メタデータ付与（30秒）

**出力JSON構造**:
```json
{
  "metadata": {
    "processed_at": "2026-01-02T10:30:00+09:00",
    "source_file": "x_timeline_20260102.json",
    "total_tweets": 200,
    "ai_related_tweets": 45,
    "ai_filter_ratio": "22.5%",
    "filtered_tweets": 42,
    "top_tweets_count": 10,
    "filter_criteria": {
      "ai_filter": "LLM-based (haiku model)",
      "excluded_usernames": ["elonmusk", "BillGates", "BarackObama", "tim_cook", "jeffbezos", "sundarpichai"],
      "engagement_formula": "likes + retweets*3 + replies*5"
    }
  },
  "top_tweets": [
    {
      "rank": 1,
      "tweet_id": "1234567890123456789",
      "username": "ai_researcher_jp",
      "text": "...",
      "likes": 150,
      "retweets": 45,
      "replies": 20,
      "engagement_score": 385,
      "created_at": "2026-01-02T08:15:00+09:00",
      "url": "https://x.com/ai_researcher_jp/status/1234567890123456789"
    },
    ...
  ]
}
```

---

### STEP 7: ファイル出力（30秒）

**出力先**:
- `Stock/programs/副業/projects/SNS/data/top_10_tweets_{YYYYMMDD}.json`
- `{YYYYMMDD}`: 処理日時（例: `20260102`）

**Write tool 使用**:
- JSON整形: インデント2スペース
- UTF-8エンコーディング

---

### STEP 8: 品質検証（1分）

**検証項目**:

1. **エンゲージメントスコア妥当性**:
   - [ ] Top 10全てのスコアが100以上
   - [ ] スコアが降順に並んでいる

2. **データ重複チェック**:
   - [ ] tweet_id に重複なし

3. **著名人除外確認**:
   - [ ] 除外リストのユーザーが含まれていない

4. **URL形式確認**:
   - [ ] 全ツイートのURLが `https://x.com/{username}/status/{tweet_id}` 形式

**検証失敗時**:
- エラーメッセージ表示
- 出力ファイルは生成するが、警告フラグを立てる

---

## Output Format

**成功時の表示例**:
```
✅ Top 10 AI-related tweets extracted successfully

📊 Summary:
- Total tweets processed: 200
- AI-related tweets: 45 (22.5%)
- After celebrity filter: 42
- Top 10 engagement scores: 385, 342, 298, 275, 263, 241, 230, 218, 205, 192
- Average engagement score (Top 10): 264.9
- Output file: Stock/programs/副業/projects/SNS/data/top_10_tweets_20260102.json

🤖 AI Filter Stats:
- Filter method: LLM-based (haiku model)
- AI detection rate: 22.5%

🏆 Top 3 Preview:
1. @ai_researcher_jp (385 pts) - "AIエージェントの未来について..."
2. @startup_founder (342 pts) - "ChatGPT APIの新機能を試してみた..."
3. @tech_writer_jp (298 pts) - "OpenAIの最新研究論文を読んで..."
```

---

## Error Handling

### エラーパターン1: ファイル未検出
- **参照**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **対応**: ユーザーに通知し、処理中断

### エラーパターン2: JSONパースエラー
- **対応**: エラー行を特定し、修正方法を提案

### エラーパターン3: データ不足（10件未満）
- **対応**: 警告表示 + 全件出力

### エラーパターン4: 全ツイートが著名人アカウント
- **対応**: フィルタ条件を緩和（フォロワー数閾値を上げる）

---

## Quality Checklist

実行完了時に以下を確認:

- [ ] Top 10件抽出成功
- [ ] engagement_score計算精度100%（手動で3件サンプル検証）
- [ ] 重複なし
- [ ] 著名人除外済み
- [ ] 出力JSONが正しい形式
- [ ] メタデータに処理統計が含まれている
- [ ] 出力ファイルが指定パスに作成済み

---

## Dependencies

**前提スキル**:
- `collect-x-timeline`: Xタイムラインデータ収集（200件）

**次フェーズスキル**:
- `scrape-tweet-details`: ツイート詳細ページからリンク・リプライ抽出

---

## Version History

- **v1.1.0** (2026-01-04): AI関連フィルタリング追加
  - LLMサブエージェント（haiku）によるAI関連判定機能追加
  - キーワードマッチングではなく文脈理解でAI関連を判定
  - メタデータにAI関連統計を追加
  - 著名人除外リストにjeffbezos, sundarpichaiを追加

- **v1.0.0** (2026-01-02): 初版作成
  - 基本的なTop 10抽出機能
  - エンゲージメントスコア計算
  - 著名人フィルタリング
