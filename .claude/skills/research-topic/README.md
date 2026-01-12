# Research Topic Skill

Top 10ツイートのトピックをWeb調査し、最新ニュース、ファクトチェック、批判的視点、専門家意見を収集するClaude Code Skill。

---

## 概要

**ClaudeCode WebSearch実行型**により、3トピックから30ソース、7ファクトチェック、13批判的視点を収集。4カテゴリ構造化（最新ニュース、ファクトチェック、批判的視点、専門家意見）で投稿作成に必要な情報を網羅的に提供します。

---

## クイックスタート

### 1. 前提条件

`top_10_ai_tweets_{YYYYMMDD}.json` が存在すること（`extract-top-tweets` スキル実行後）

### 2. スキル実行

```bash
# Claude Codeで実行
トピック調査
```

または

```bash
/research-topic
```

### 3. 出力確認

```bash
# 出力ファイル
Stock/programs/副業/projects/SNS/data/research_findings_ai_YYYYMMDD.json

# 内容確認
cat Stock/programs/副業/projects/SNS/data/research_findings_ai_20260102.json | jq '.metadata'
```

---

## 実行パラメータ

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| **入力ファイル** | 最新の `top_10_ai_tweets_*.json` | AI関連Top 10ツイート |
| **調査対象** | High priority（Top 3） | エンゲージメントTop 3を詳細調査 |
| **model** | sonnet | ClaudeCode実行モデル |
| **thinking** | true | 思考モード有効 |

---

## 出力フォーマット

```json
{
  "metadata": {
    "researched_at": "2026-01-02T12:51:35",
    "research_method": "ClaudeCode WebSearch + LLM analysis",
    "total_topics": 10,
    "topics_researched": 3,
    "research_summary": {
      "total_sources_found": 30,
      "fact_checks_performed": 7,
      "criticisms_identified": 13,
      "expert_opinions_collected": 9
    }
  },
  "research_findings": {
    "2006676783991787563": {
      "tweet_username": "cb_doge",
      "topic": "Tesla Optimus × NVIDIA Jensen Huang",
      "latest_news": {...},
      "fact_check": {...},
      "opposing_views": {...},
      "expert_opinions": {...}
    }
  }
}
```

---

## パフォーマンス

| 指標 | 実績（2026-01-02） |
|------|------------------|
| **調査トピック数** | 3 (High priority) |
| **総ソース数** | 30 |
| **ファクトチェック数** | 7 |
| **批判的視点数** | 13 |
| **専門家意見数** | 9 |
| **実行時間** | 約18分 |

---

## 調査カテゴリ

### 最新ニュース（latest_news）
トピックの最新動向を把握（2026年または2025年後半の情報）

### ファクトチェック（fact_check）
数値・主張・予測の信頼性を検証（高/中/低で評価）

### 批判的視点（opposing_views）
リスク・限界点・技術的課題を事前に把握

### 専門家意見（expert_opinions）
支持派・懐疑派の両論を収集（専門性・実績で信頼性評価）

---

## トラブルシューティング

### WebSearch結果が0件の場合

**症状**: 特定クエリで検索結果なし

**対処法**: 自動的にクエリを変更して再検索（最大2回）

### ソース情報が不十分な場合

**症状**: 一部カテゴリの情報が少ない

**対処法**: `status: "partial"` で記録され、得られた情報のみ出力

---

## 次のアクション

調査完了後、以下のアクションを実行できます：

1. **generate-sns-posts**: 調査結果を反映した投稿文生成
2. **ファクトチェック済み投稿**: 数値・主張の信頼性を明記
3. **両論併記型投稿**: 支持派・懐疑派の両方を紹介

---

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## 更新履歴

- 2026-01-02: 初版作成（ClaudeCode WebSearch実行型）
- 実績: 3トピック調査、30ソース、7ファクトチェック、13批判的視点
