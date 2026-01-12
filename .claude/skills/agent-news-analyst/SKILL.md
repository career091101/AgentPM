---
name: agent-news-analyst
description: |
  過去7日間の日経平均先物関連ニュースを収集・分類する自律型エージェント。
  WebSearchで金融ニュースサイトから最新情報を収集し、重要度・センチメント
  （ポジティブ/ネガティブ/中立）で分類、今後1週間への影響を評価（10-15分）。

  使用タイミング：
  - トレード戦略立案時のニュース分析
  - 市場イベント前の情報収集
  - センチメント変化の検出

  所要時間：10-15分（自動実行）
  出力：news_analysis.md

trigger_keywords:
  - "ニュース分析"
  - "市場ニュース"
  - "ニュース影響分析"

dependencies: []  # Phase 1は独立実行

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/news_analysis.md

execution_time: 10-15分（自動実行）

stage: Phase1 - News Analysis

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P0
---

# News Analyst Skill

過去7日間の日経平均先物関連ニュースを収集・分類する自律型エージェント。

---

## このSkillでできること

1. **ニュース収集**: 過去7日間の日経関連ニュースを主要サイトから収集
2. **重要度分類**: 各ニュースを重要度（高/中/低）で分類
3. **センチメント分析**: ポジティブ/ネガティブ/中立に分類
4. **市場テーマ抽出**: 主要な市場テーマを特定
5. **影響度評価**: 今後1週間への影響を評価

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 10-15分

### 自動実行フロー（ReActループ）

#### Iteration 1: 日本語ニュース収集

**Thought**: 日経新聞、Bloomberg Japan、Reuters Japan から最新7日間のニュースを収集

**Action**:
```
WebSearch: "日経平均 ニュース site:nikkei.com 過去7日間"
WebSearch: "日本株式市場 最新 site:bloomberg.co.jp"
WebSearch: "日経225 ニュース site:jp.reuters.com"
```

**Result**: 20-30件のニュースヘッドライン収集

---

#### Iteration 2: 英語ニュース収集

**Thought**: Bloomberg、Reuters、Financial Times から国際的視点のニュースを収集

**Action**:
```
WebSearch: "Nikkei 225 news site:bloomberg.com past week"
WebSearch: "Japan stock market site:reuters.com"
WebSearch: "Nikkei index site:ft.com"
```

**Result**: 10-20件のニュースヘッドライン収集

---

#### Iteration 3: ニュース分類とスコアリング

**Thought**: 収集したニュースを重要度・センチメントで分類

**Action**:
```python
for news in collected_news:
    # 重要度判定
    if "日銀" in news or "FRB" in news or "決算" in news:
        importance = "高"
    elif "見通し" in news or "予想" in news:
        importance = "中"
    else:
        importance = "低"

    # センチメント判定
    positive_words = ["上昇", "好調", "増加", "プラス", "買い"]
    negative_words = ["下落", "懸念", "減少", "マイナス", "売り"]

    if any(w in news for w in positive_words):
        sentiment = "ポジティブ"
    elif any(w in news for w in negative_words):
        sentiment = "ネガティブ"
    else:
        sentiment = "中立"
```

**Result**: 全ニュースを分類完了

---

#### Final Output: news_analysis.md生成

**Content**:
```markdown
---
agent: agent-news-analyst
phase: phase1
timestamp: 2025-12-29 11:30:00
status: completed
target: 日経平均先物（日経225）
period: 過去7日間のニュース分析
---

# News Analyst ニュース影響分析レポート

## エグゼクティブサマリー

**総ニュース件数**: XX件
**ポジティブ**: XX件（XX%）
**ネガティブ**: XX件（XX%）
**中立**: XX件（XX%）
**総合センチメント**: [ポジティブ優勢/ネガティブ優勢/中立]

---

## 1. 重要ニュースサマリー

### 重要度【高】のニュース

| 日付 | ヘッドライン | センチメント | 影響度 | ソース |
|------|-------------|-------------|--------|--------|
| 12/28 | [ヘッドライン1] | [ポジ/ネガ/中立] | [高/中/低] | [URL] |
| 12/27 | [ヘッドライン2] | [ポジ/ネガ/中立] | [高/中/低] | [URL] |

---

## 2. 市場テーマ分析

### 主要テーマ

| テーマ | 関連ニュース数 | センチメント | 今後の影響 |
|--------|---------------|-------------|-----------|
| 金融政策 | X件 | [ポジ/ネガ/中立] | [詳細] |
| 企業業績 | X件 | [ポジ/ネガ/中立] | [詳細] |
| 地政学 | X件 | [ポジ/ネガ/中立] | [詳細] |
| セクター動向 | X件 | [ポジ/ネガ/中立] | [詳細] |

---

## 3. センチメント総合評価

**ポジティブ要因**:
- [要因1]（ニュース数: X件）
- [要因2]（ニュース数: X件）

**ネガティブ要因**:
- [要因1]（ニュース数: X件）
- [要因2]（ニュース数: X件）

**総合判定**: [ポジティブ優勢/ネガティブ優勢/中立]

---

## 4. 今後1週間への影響予測

**予測**: [ポジティブ/ネガティブ/中立]

**根拠**:
- [根拠1]
- [根拠2]

**注視すべきニュース**:
- [項目1]
- [項目2]

---

## メタデータ

- **実行時間**: XX分
- **WebSearchクエリ数**: 6
- **収集ニュース数**: XX件
- **データソース数**: X
```

---

## 使用例

```
User: /agent-news-analyst

Skill:
# News Analyst 自律実行開始

収集期間: 過去7日間

[自動実行中...]

## Iteration 1: 日本語ニュース収集 ✅
- 日経新聞: 15件
- Bloomberg Japan: 10件
- Reuters Japan: 8件

## Iteration 2: 英語ニュース収集 ✅
- Bloomberg: 12件
- Reuters: 7件
- FT: 5件

## Iteration 3: 分類・スコアリング ✅
- 重要度【高】: 8件
- ポジティブ: 25件（43%）
- ネガティブ: 20件（34%）
- 中立: 13件（22%）

完了時間: 12分
総合センチメント: ポジティブ優勢
```
