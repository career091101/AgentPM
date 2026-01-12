---
name: analyze-replies
description: |
  ツイート詳細データからリプライを分析し、反響ポイント（共感・批判・質問・追加情報）を抽出するスキル。
  ClaudeCode LLMが直接リプライテキストを読み込み、意味的に分析してインサイトを生成します。

  使用タイミング：
  - SNS投稿作成時に反響を事前予測したい時
  - リプライから追加情報を収集したい時
  - 批判的視点を把握したい時

  所要時間：10-15分
  出力：reply_insights_ai_{YYYYMMDD}.json
trigger_keywords:
  - "リプライ分析"
  - "反響分析"
  - "analyze replies"
  - "リアクション分析"
stage: Phase 2 - Reply Analysis
dependencies: ["scrape-tweet-details"]
output_file: Stock/programs/副業/projects/SNS/data/reply_insights_ai_{YYYYMMDD}.json
execution_time: 10-15分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P1
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
thinking: true
---

# Analyze Replies Skill

ツイート詳細からリプライを分析し、反響ポイントを抽出するスキル。

---

## このSkillでできること

1. **反響タイプ分類**: 共感・期待、批判・懸念、追加情報・洞察、質問に自動分類
2. **インサイト抽出**: 各リプライから投稿作成に有用な洞察を日本語で要約
3. **エンゲージメント重視**: いいね数が多いリプライを優先的に分析
4. **複数ツイート一括処理**: Top 10ツイート全てのリプライを自動分析
5. **日本語・英語両対応**: リプライ言語に関わらず日本語で要約

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | tweet_details_ai_{YYYYMMDD}.json（ツイート詳細+リプライ） |
| **出力** | reply_insights_ai_{YYYYMMDD}.json（反響ポイント） |
| **次のアクション** | research-topic（Web調査）、generate-sns-posts（投稿生成） |

---

## Instructions

**実行モード**: ClaudeCode LLM自律実行（思考モード有効）
**推定所要時間**: 10-15分

### STEP 1: 入力ファイル読み込み（30秒）

**Readツール使用**:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/tweet_details_ai_{最新日付}.json
```

**確認項目**:
- ファイル存在確認
- `tweet_details` 配列の読み込み
- 各ツイートの `replies` 配列を抽出
- リプライ総数をカウント

**フォールバック**:
- 最新日付ファイルが見つからない場合、`tweet_details_*.json` の最新ファイルを検索

---

### STEP 2: 分析対象ツイート選定（1分）

**優先順位**:
1. **Top 5ツイート**: エンゲージメントスコアTop 5を優先分析
2. **リプライ数**: リプライ数が多いツイートを優先
3. **AI関連**: AI関連ツイートを優先

**選定基準**:
```python
# 疑似コード
tweets_with_replies = [t for t in tweet_details if len(t['replies']) > 0]

# エンゲージメントスコアでソート
sorted_tweets = sorted(
    tweets_with_replies,
    key=lambda t: t.get('engagement_score', t['likes'] + t['retweets']*3 + len(t['replies'])*5),
    reverse=True
)

# Top 5を選定
top_tweets = sorted_tweets[:5]
```

**ユーザーに報告**:
```
📊 リプライ分析対象
- 対象ツイート数: 5件
- 総リプライ数: 40件
- 平均リプライ数/ツイート: 8件

分析を開始します...
```

---

### STEP 3: リプライ意味分析（8-12分）

**各ツイートのリプライを分析**:

#### 3A. リプライ読み込み

**各ツイートに対して**:
```python
# 疑似コード
for tweet in top_tweets:
    tweet_text = tweet['text']
    replies = tweet['replies']  # 最大10件のリプライ

    # リプライテキストを結合
    all_replies_text = "\n---\n".join([
        f"Reply {i+1} (likes: {r['likes']}): {r['text']}"
        for i, r in enumerate(replies)
    ])
```

#### 3B. LLM分析実行

**分析プロンプト**（ClaudeCode LLM内部で実行）:
```
以下はツイート本文とそのリプライです。各リプライを分析し、以下の情報を抽出してください：

【ツイート本文】
{tweet_text}

【リプライ一覧】
{all_replies_text}

【抽出指示】
1. 各リプライを以下のタイプに分類:
   - 共感・期待: ツイート内容に賛同・期待を示すもの
   - 批判・懸念: 批判的視点、懸念点を指摘するもの
   - 追加情報・洞察: 新しい情報、洞察、データを追加するもの
   - 質問: 疑問・質問を投げかけるもの

2. 各リプライから投稿作成に役立つインサイトを日本語で要約（1-2文）

3. 元のリプライテキスト（原文）を保持

4. いいね数を記録（エンゲージメント指標）

【出力形式】
JSONフォーマット:
{
  "insights": [
    {
      "type": "共感・期待",
      "content": "日本語要約（1-2文）",
      "supporting_reply": "元のリプライテキスト",
      "likes": 17
    }
  ]
}
```

#### 3C. インサイト抽出例

**実際の抽出結果**:
```json
{
  "tweet_id": "2006676783991787563",
  "tweet_username": "cb_doge",
  "topic": "Optimusヒューマノイドロボット × NVIDIA Jensen Huang",
  "insights": [
    {
      "type": "共感・期待",
      "content": "NVIDIA CEOからの「extraordinary engineer」という評価は究極の検証。$3T企業トップの言葉は重みが違う",
      "supporting_reply": "When the CEO of a $3T company calls you an 'extraordinary engineer', that is the ultimate validation",
      "likes": 17
    },
    {
      "type": "批判・懸念",
      "content": "ロボットが看護師を置き換える可能性を指摘したら職を失った。雇用への影響は現実的な懸念",
      "supporting_reply": "I was forced out of a job teaching nurses about robots... one day robots may replace nurses",
      "likes": 5
    },
    {
      "type": "追加情報・洞察",
      "content": "重要なのは「収束」。AI、ハードウェア、エネルギー、製造が大規模で交差する今、ロボットはデモから生産性を変えるインフラへ",
      "supporting_reply": "convergence: AI, hardware, energy, and manufacturing finally meeting at scale... robots stop being demos and start becoming infrastructure",
      "likes": 15
    }
  ]
}
```

---

### STEP 4: 結果集計（1分）

**統計情報計算**:
```python
# 疑似コード
total_insights = sum([len(tweet['insights']) for tweet in analyzed_tweets])
type_distribution = {
    '共感・期待': count_by_type('共感・期待'),
    '批判・懸念': count_by_type('批判・懸念'),
    '追加情報・洞察': count_by_type('追加情報・洞察'),
    '質問': count_by_type('質問')
}

avg_insights_per_tweet = total_insights / len(analyzed_tweets)
```

---

### STEP 5: 出力ファイル生成（30秒）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "analyzed_at": "2026-01-02T12:41:28",
    "analysis_method": "ClaudeCode LLM direct analysis",
    "total_tweets_analyzed": 5,
    "total_insights_extracted": 24
  },
  "reply_insights": {
    "2006676783991787563": {
      "tweet_username": "cb_doge",
      "topic": "Optimusヒューマノイドロボット × NVIDIA Jensen Huang",
      "insights": [...]
    },
    "2006763630138966389": {
      "tweet_username": "JapanTank",
      "topic": "RAGの本質的問題 - 組織・インセンティブ",
      "insights": [...]
    }
  }
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/reply_insights_ai_{YYYYMMDD}.json`

---

### STEP 6: サマリーレポート生成（30秒）

**ユーザーへの報告**:
```
✅ リプライ分析完了

📊 Summary:
  - Total tweets analyzed: 5
  - Total replies processed: 40
  - Total insights extracted: 24

📈 Insight distribution:
  - 共感・期待: 10件 (41.7%)
  - 批判・懸念: 5件 (20.8%)
  - 追加情報・洞察: 8件 (33.3%)
  - 質問: 1件 (4.2%)

🏆 Top insights by engagement:
  1. NVIDIA CEOからの評価が究極の検証 (17 likes)
  2. AI・ハードウェア・製造の収束がインフラ化を促進 (15 likes)
  3. Claude Codeは上手い人のやり方を試して我流化 (3155 likes)

💾 Output: reply_insights_ai_20260102.json (10KB)

📌 Next: research-topic（Web調査）、generate-sns-posts（投稿生成）
```

---

## 分析カテゴリ詳細

### 共感・期待
**定義**: ツイート内容に賛同、期待、ポジティブな反応を示すリプライ
**例**:
- "This is game-changing!"
- "期待しかない"
- "素晴らしい取り組みですね"

### 批判・懸念
**定義**: 批判的視点、懸念点、ネガティブな反応を示すリプライ
**例**:
- "雇用への影響が心配"
- "過剰な賞賛は控えてほしい"
- "実現可能性に疑問"

### 追加情報・洞察
**定義**: 新しい情報、データ、洞察、専門知識を追加するリプライ
**例**:
- "関連する研究によれば..."
- "テンバガー株の実証研究では、FCF利回りが最も効く"
- "LLMの凄さは報酬システムにある"

### 質問
**定義**: 疑問、質問、詳細説明を求めるリプライ
**例**:
- "具体的にどう使うのか？"
- "技術的な詳細を教えてください"
- "いつリリースされますか？"

---

## エラーハンドリング

### リプライ数が0の場合
- **対応**: そのツイートをスキップ、次へ進む
- **ログ**: `status: "no_replies"` で記録

### リプライテキストが空の場合
- **対応**: そのリプライをスキップ、次へ進む
- **ログ**: `status: "empty_text"` で記録

### LLM分析失敗
- **原因**: リプライが短すぎる、意味が不明
- **対応**: `type: "その他"`, `content: "分析不可"` で記録
- **ログ**: `status: "analysis_failed"` で記録

---

## データ品質保証

| 品質指標 | 目標 | 実績（2026-01-02） |
|---------|------|------------------|
| **分析ツイート数** | ≥3 | 5 |
| **抽出インサイト数** | ≥10 | 24 |
| **平均インサイト数/ツイート** | ≥3 | 4.8 |

---

## 使用例

### 基本的な使用

```
User: リプライ分析
```

システムが自動的に：
1. 最新の `tweet_details_ai_*.json` を読み込み
2. Top 5ツイートを選定
3. ClaudeCode LLMで各リプライを意味分析
4. インサイトを4カテゴリに分類
5. JSON出力生成
6. サマリーレポート表示

---

## 依存ツール

**必須**:
- `Read`: 入力ファイル読み込み
- `Write`: 出力ファイル保存
- ClaudeCode LLM内部処理（思考モード有効）

---

## 次のアクション提案

分析完了後、以下のアクションを提案します：

1. **research-topic**: インサイトを深掘りするWeb調査
2. **generate-sns-posts**: 反響ポイントを反映した投稿文生成
3. **投稿戦略調整**: 批判的視点を事前に対処する論点設計

---

## 更新履歴

- 2026-01-02: 初版作成（ClaudeCode LLM直接分析型）
- 実績: 5ツイート、40リプライ → 24インサイト抽出
