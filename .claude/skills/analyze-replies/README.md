# Analyze Replies Skill

ツイート詳細データからリプライを分析し、反響ポイント（共感・批判・質問・追加情報）を抽出するClaude Code Skill。

---

## 概要

**ClaudeCode LLM意味分析型**により、40リプライから24インサイトを抽出。4カテゴリ（共感・期待、批判・懸念、追加情報・洞察、質問）に自動分類し、投稿作成に直接反映できる形式で日本語要約します。

---

## クイックスタート

### 1. 前提条件

`tweet_details_ai_{YYYYMMDD}.json` が存在すること（`scrape-tweet-details` スキル実行後）

### 2. スキル実行

```bash
# Claude Codeで実行
リプライ分析
```

または

```bash
/analyze-replies
```

### 3. 出力確認

```bash
# 出力ファイル
Stock/programs/副業/projects/SNS/data/reply_insights_ai_YYYYMMDD.json

# 内容確認
cat Stock/programs/副業/projects/SNS/data/reply_insights_ai_20260102.json | jq '.metadata'
```

---

## 実行パラメータ

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| **入力ファイル** | 最新の `tweet_details_ai_*.json` | ツイート詳細+リプライ |
| **分析対象** | Top 5ツイート | エンゲージメントTop 5を優先分析 |
| **model** | sonnet | ClaudeCode実行モデル |
| **thinking** | true | 思考モード有効 |

---

## 出力フォーマット

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
      "insights": [
        {
          "type": "共感・期待",
          "content": "NVIDIA CEOからの「extraordinary engineer」という評価は究極の検証",
          "supporting_reply": "When the CEO of a $3T company calls you...",
          "likes": 17
        }
      ]
    }
  }
}
```

---

## パフォーマンス

| 指標 | 実績（2026-01-02） |
|------|------------------|
| **分析ツイート数** | 5 |
| **抽出インサイト数** | 24 |
| **平均インサイト数/ツイート** | 4.8 |
| **実行時間** | 約12分 |

---

## 分析カテゴリ

### 共感・期待
ツイート内容に賛同、期待、ポジティブな反応を示すリプライ

### 批判・懸念
批判的視点、懸念点、ネガティブな反応を示すリプライ

### 追加情報・洞察
新しい情報、データ、洞察、専門知識を追加するリプライ

### 質問
疑問、質問、詳細説明を求めるリプライ

---

## トラブルシューティング

### リプライ数が0の場合

**症状**: ツイートにリプライがない

**対処法**: 正常動作です。そのツイートをスキップし、次へ進みます。

### LLM分析失敗

**症状**: インサイト抽出ができない

**対処法**: リプライが短すぎる場合は `type: "その他"` で記録されます。

---

## 次のアクション

分析完了後、以下のアクションを実行できます：

1. **research-topic**: インサイトを深掘りするWeb調査
2. **generate-sns-posts**: 反響ポイントを反映した投稿文生成
3. **投稿戦略調整**: 批判的視点を事前に対処する論点設計

---

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## 更新履歴

- 2026-01-02: 初版作成（ClaudeCode LLM直接分析型）
- 実績: 5ツイート、40リプライ → 24インサイト抽出
