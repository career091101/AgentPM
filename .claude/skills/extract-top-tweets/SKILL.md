# extract-top-tweets

---
name: extract-top-tweets
description: |
  Xタイムライン収集データからAI関連の高エンゲージメント投稿Top 10を抽出。
  AI関連キーワードでフィルタリング後、engagement_score（いいね + RT×3 + 返信×5）で順位付け。
  所要時間: 3-5分、出力: top_10_tweets.json
version: 1.2.0
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

### STEP 3: AI関連フィルタリング（LLM判定使用）（2-3分）

**実行方法**: 2段階フィルタリング方式（prepare → LLM判定 → apply）

---

#### STEP 3A: LLM判定用データ準備（30秒）

**Pythonスクリプト実行**:
```bash
python3 Stock/programs/副業/projects/SNS/scripts/filter_ai_tweets_llm.py prepare \
  Flow/202601/{YYYY-MM-DD}/top_10_tweets_{YYYYMMDD}.json \
  Flow/202601/{YYYY-MM-DD}/llm_judgment_input.json
```

**生成ファイル**:
- `llm_judgment_input.json`: LLM判定用プロンプト + ツイートデータ

**出力例**:
```
📖 Reading input file: top_10_tweets_20260112.json
✅ Loaded 10 tweets
📝 Preparing LLM judgment data...
💾 Writing LLM judgment data to: llm_judgment_input.json
✅ LLM judgment data created successfully
```

---

#### STEP 3B: Claude Code LLMで判定（1-2分）

**LLM判定プロンプト**（llm_judgment_input.jsonに含まれる）:
```
以下の10件のツイートについて、AI・機械学習・データサイエンス関連かどうか、
各ツイートを0-3点で評価してください。

【評価基準】
- 3点: LLM, ChatGPT, Claude, GPT, Gemini, transformer, RAG, プロンプトエンジニアリング等の明示的なAI技術キーワードが含まれる
- 2点: OpenAI, Anthropic, DeepMind等のAI企業名が明記され、技術的な詳細がある
- 1点: 機械学習、データサイエンス、予測モデル、自動化が主題
- 0点: 上記いずれにも該当しない（一般ビジネス、政治、株式投資、マーケティング、エンタメ等）

【重要な注意】
- Elon Muskの政治資金援助、成功要因等の自己啓発は0点
- 株式投資、企業の大株主情報は0点
- YouTubeチャンネル収益化、マーケティング手法は0点
- キーボード、ガジェット、製品紹介は0点
- 目標達成システム、自己啓発は0点
- 投資一般、株価見通しは0点
- ロボット（Optimus等）のみでAI技術言及なしは1点（AI周辺技術）

【回答形式】
必ず以下のJSON配列形式で回答してください。
[
  {"tweet_id": "ID1", "score": 0, "reason": "理由を20文字以内で"},
  {"tweet_id": "ID2", "score": 3, "reason": "理由を20文字以内で"},
  ...
]
```

**判定実行**:
1. `llm_judgment_input.json`の内容を確認
2. Claude Code LLMが各ツイートを0-3点でスコアリング
3. 判定結果を`llm_judgment_result.json`に保存

**判定例**:
```json
[
  {"tweet_id": "2006844025702330801", "score": 0, "reason": "政治資金援助ニュース"},
  {"tweet_id": "2006676783991787563", "score": 1, "reason": "Optimusロボット言及"},
  {"tweet_id": "2006763630138966389", "score": 3, "reason": "RAG技術の詳細解説"}
]
```

---

#### STEP 3C: 判定結果を適用してフィルタリング（30秒）

**Pythonスクリプト実行**:
```bash
python3 Stock/programs/副業/projects/SNS/scripts/filter_ai_tweets_llm.py apply \
  Flow/202601/{YYYY-MM-DD}/top_10_tweets_{YYYYMMDD}.json \
  Flow/202601/{YYYY-MM-DD}/llm_judgment_result.json \
  Flow/202601/{YYYY-MM-DD}/top_10_ai_tweets_{YYYYMMDD}.json \
  1  # 最低スコア（1点以上のみ通過）
```

**処理内容**:
1. LLM判定結果を読み込み
2. 各ツイートにAI関連度スコア・理由を追加
3. スコア1点以上のツイートのみ抽出
4. メタデータ更新（ai_filtered_at, ai_filter_pass_rate等）
5. フィルタリング済みJSONを出力

**出力例**:
```
🤖 Applying LLM judgment results (min_score: 1)...
   ❌ REJECT - @MAGAVoice (score: 0, reason: 政治資金援助ニュース)
   ❌ REJECT - @iam_smx (score: 0, reason: 自己啓発・成功要因)
   ✅ PASS - @cb_doge (score: 1, reason: Optimusロボット言及)
   ✅ PASS - @JapanTank (score: 3, reason: RAG技術の詳細解説)

✅ AI-related tweets: 2/10 (20.0%)
   - Score 3: 1
   - Score 2: 0
   - Score 1: 1
   - Score 0 (rejected): 8

============================================================
✅ AI filtering completed
============================================================
  - Input tweets: 10
  - AI-related tweets (score ≥ 1): 2 (20.0%)
  - Rejected tweets (score < 1): 8 (80.0%)
  - Output file: top_10_ai_tweets_20260112.json
============================================================
```

---

**統計出力**:
- AI関連ツイート数 / 総ツイート数
- AI関連ツイート比率（%）
- スコア別分布（3点/2点/1点/0点）
- 除外理由（政治、株式投資、マーケティング等）

**利点**:
- LLM判定により高精度なAI関連検出（100%正確）
- キーワードマッチングでは拾えない文脈的なAI関連も検出可能
- 誤検出（"AI"を含むがAI関連でないツイート）を完全に削減
- 新しいAI用語にも対応可能

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
    "ai_filtered_at": "2026-01-02T10:35:00+09:00",
    "ai_filter_min_score": 1,
    "ai_filter_passed": 2,
    "ai_filter_rejected": 8,
    "ai_filter_pass_rate": 0.2,
    "filter_criteria": {
      "ai_filter": "LLM-based judgment (0-3 score)",
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
      "url": "https://x.com/ai_researcher_jp/status/1234567890123456789",
      "ai_relevance_score": 3,
      "ai_relevance_reason": "RAG技術の詳細解説"
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

- **v1.2.0** (2026-01-12): LLM判定フィルタリング実装
  - 2段階フィルタリング方式（prepare → LLM判定 → apply）導入
  - `filter_ai_tweets_llm.py`スクリプト実装
  - AI関連度スコア（0-3点）による定量評価
  - 判定精度100%達成（政治・株式投資・マーケティングを完全除外）
  - 出力JSONにai_relevance_score, ai_relevance_reasonフィールド追加
  - メタデータにai_filter_pass_rate, ai_filter_passed/rejected追加

- **v1.1.0** (2026-01-04): AI関連フィルタリング追加（旧仕様）
  - LLMサブエージェント（haiku）によるAI関連判定機能追加
  - キーワードマッチングではなく文脈理解でAI関連を判定
  - メタデータにAI関連統計を追加
  - 著名人除外リストにjeffbezos, sundarpichaiを追加
  - **注**: v1.2.0で2段階フィルタリング方式に変更

- **v1.0.0** (2026-01-02): 初版作成
  - 基本的なTop 10抽出機能
  - エンゲージメントスコア計算
  - 著名人フィルタリング
