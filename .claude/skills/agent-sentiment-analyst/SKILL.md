---
name: agent-sentiment-analyst
description: |
  市場センチメントを4指標で分析するエージェント。Fear & Greed Index（CNN）、Put/Call比率（JPX）、VIX指数（日経VI）、ニュースセンチメント（Google News）を統合し、投資家心理と市場過熱度を評価。逆張り解釈（極度の恐怖=買いシグナル、極度の強欲=売りシグナル）を採用。

  使用タイミング：
  - データ収集完了後の並列分析フェーズ（STEP 2-4）
  - テクニカル分析、エリオット波動分析と同時実行
  - 市場心理の定量化が必要な時

  所要時間：20-30分
  出力：sentiment_analysis.md（総合センチメント + 4指標詳細 + トレード推奨）
trigger_keywords:
  - "センチメント分析"
  - "市場心理"
  - "Fear and Greed"
stage: Sentiment Analysis
dependencies:
  - agent-data-collector
output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/sentiment_analysis.md
execution_time: 20-30分
framework_reference: Stock/programs/資産運用/projects/TradingAgents/knowledge/technical_indicators.md
priority: P0
framework_compliance: 100%
---

# Agent Sentiment Analyst Skill

市場センチメントを4つの指標で多面的に分析し、投資家心理と市場過熱度を定量化するエージェント。

---

## 役割

テクニカル指標やエリオット波動分析では捉えきれない「市場参加者の感情」を定量化し、トレード判断に活用します。特に、極端な心理状態（パニック売り、FOMO買い）は逆張りシグナルとして有効です。

---

## 分析対象の4指標

### 1. Fear & Greed Index（恐怖と強欲指数）

**データソース**: CNN Business Fear & Greed Index
**URL**: `https://edition.cnn.com/markets/fear-and-greed`

**取得方法**:
```javascript
// Claude in Chrome MCP使用
1. navigate("https://edition.cnn.com/markets/fear-and-greed")
2. wait(duration=3)
3. read_page() でDOM取得
4. find("Fear & Greed Index") で指数検出
5. javascript_tool で数値抽出
```

**指標範囲**: 0-100
- **0-25**: 極度の恐怖（Extreme Fear）→ 買いシグナル
- **25-45**: 恐怖（Fear）→ やや買い
- **45-55**: 中立（Neutral）→ 観望
- **55-75**: 強欲（Greed）→ やや売り
- **75-100**: 極度の強欲（Extreme Greed）→ 売りシグナル

**重み**: 1.5（最重要、市場全体の心理を反映）

**判定ロジック**:
```python
if index <= 25:
    signal = "強気"（逆張り買い）
    confidence = 80%
elif index <= 45:
    signal = "やや強気"
    confidence = 60%
elif index <= 55:
    signal = "中立"
    confidence = 40%
elif index <= 75:
    signal = "やや弱気"
    confidence = 60%
else:
    signal = "弱気"（逆張り売り）
    confidence = 80%
```

---

### 2. Put/Call比率（プット・コール・レシオ）

**データソース**: 日本取引所グループ（JPX）デリバティブ市場統計
**URL**: `https://www.jpx.co.jp/markets/statistics-derivatives/daily/index.html`

**取得方法**:
```javascript
// WebFetch使用
WebFetch(
    url="https://www.jpx.co.jp/markets/statistics-derivatives/daily/index.html",
    prompt="日経225オプションのPut出来高とCall出来高を抽出し、Put/Call比率を計算してください"
)
```

**計算式**:
```
Put/Call比率 = Put出来高 / Call出来高
```

**判定基準**:
- **> 1.2**: プット買い優勢 → 悲観的 → 買いシグナル（逆張り）
- **0.8-1.2**: 均衡 → 中立
- **< 0.8**: コール買い優勢 → 楽観的 → 売りシグナル（逆張り）

**重み**: 1.3（日本市場固有の指標として重要）

---

### 3. VIX指数（日経VI）

**データソース**: 日本取引所グループ 日経平均VI（ボラティリティ・インデックス）
**URL**: `https://www.jpx.co.jp/markets/statistics-derivatives/misc/03.html`

**取得方法**:
```javascript
// WebFetch使用
WebFetch(
    url="https://www.jpx.co.jp/markets/statistics-derivatives/misc/03.html",
    prompt="最新の日経平均VIの値を抽出してください"
)
```

**判定基準**:
- **> 30**: 高ボラティリティ、恐怖 → 買いシグナル（逆張り）
- **20-30**: やや高め → やや買い
- **15-20**: 通常レベル → 中立
- **< 15**: 低ボラティリティ、過信 → やや売り

**重み**: 1.2（ボラティリティは市場心理の直接指標）

---

### 4. ニュースセンチメント

**データソース**: Google News検索「日経平均」
**URL**: `https://news.google.com/search?q=日経平均&hl=ja&gl=JP&ceid=JP:ja`

**取得方法**:
```javascript
// WebFetch使用
WebFetch(
    url="https://news.google.com/search?q=日経平均&hl=ja&gl=JP&ceid=JP:ja",
    prompt="日経平均関連の最新ニュース20件の見出しから、ポジティブ/ネガティブ/中立を判定し、スコア化してください"
)
```

**スコア化**:
```python
# 各ニュース見出しをLLMで判定
positive_count = ポジティブニュース数
negative_count = ネガティブニュース数
neutral_count = 中立ニュース数

sentiment_score = (positive_count - negative_count) / 20 × 100
# 範囲: -100（完全ネガティブ）~ +100（完全ポジティブ）
```

**判定基準**:
- **< -50**: 極度にネガティブ → 買いシグナル（逆張り）
- **-50 ~ -20**: ネガティブ → やや買い
- **-20 ~ +20**: 中立 → 観望
- **+20 ~ +50**: ポジティブ → やや売り
- **> +50**: 極度にポジティブ → 売りシグナル（逆張り）

**重み**: 1.0（補助的指標、ノイズが多い）

---

## 統合判定ロジック

### 重み付けスコア計算

```python
WEIGHTS = {
    'fear_greed': 1.5,
    'put_call': 1.3,
    'vix': 1.2,
    'news': 1.0
}

# 各指標を-100（強気）~ +100（弱気）に正規化
normalized_scores = {
    'fear_greed': (index - 50) * 2,  # 0-100 → -100 ~ +100
    'put_call': (ratio - 1.0) * 100,  # 0.8-1.2 → -20 ~ +20（拡大）
    'vix': (vi - 22.5) * 4,  # 15-30 → -30 ~ +30（拡大）
    'news': sentiment_score  # 既に-100 ~ +100
}

# 重み付け総合スコア
total_score = sum(
    normalized_scores[key] * WEIGHTS[key]
    for key in WEIGHTS
) / sum(WEIGHTS.values())

# 範囲: -100（強気）~ +100（弱気）
```

### 総合判定

```python
if total_score < -40:
    overall_sentiment = "強気"
    signal = "買い"
    confidence = min(80, abs(total_score) * 0.8)
elif total_score < -15:
    overall_sentiment = "やや強気"
    signal = "やや買い"
    confidence = 60
elif total_score < 15:
    overall_sentiment = "中立"
    signal = "観望"
    confidence = 40
elif total_score < 40:
    overall_sentiment = "やや弱気"
    signal = "やや売り"
    confidence = 60
else:
    overall_sentiment = "弱気"
    signal = "売り"
    confidence = min(80, abs(total_score) * 0.8)
```

---

## 出力フォーマット

**ファイル名**: `Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/sentiment_analysis.md`

**内容**:

```markdown
# センチメント分析レポート

分析日時: 2025-12-29 14:00:00

---

## 総合センチメント判定

- **総合センチメント**: やや強気
- **シグナル**: やや買い
- **信頼度**: 60%
- **総合スコア**: -22.5（-100が最強気、+100が最弱気）

---

## 指標別詳細

### 1. Fear & Greed Index

- **現在値**: 42
- **判定**: 恐怖（Fear）
- **正規化スコア**: -16（恐怖 = 買いシグナル）
- **重み**: 1.5
- **解釈**: 市場参加者が警戒的。過度な悲観は買い場の可能性。

### 2. Put/Call比率

- **Put出来高**: 1,250,000
- **Call出来高**: 1,100,000
- **比率**: 1.14
- **判定**: プット優勢（悲観的）
- **正規化スコア**: +14（プット買い = 買いシグナル）
- **重み**: 1.3
- **解釈**: オプション市場で下落への備えが目立つ。逆張りで買い検討。

### 3. 日経VI（VIX）

- **現在値**: 24.5
- **判定**: やや高め
- **正規化スコア**: +8（ボラ高 = やや買いシグナル）
- **重み**: 1.2
- **解釈**: 通常よりやや高いボラティリティ。市場の不安定さ示唆。

### 4. ニュースセンチメント

- **分析ニュース数**: 20件
- **ポジティブ**: 6件
- **ネガティブ**: 10件
- **中立**: 4件
- **センチメントスコア**: -20
- **判定**: ネガティブ寄り
- **正規化スコア**: -20（ネガティブ = やや買いシグナル）
- **重み**: 1.0
- **解釈**: ニュース報道は慎重トーン。過度な悲観は買い場。

---

## 統合判定の根拠

**重み付け計算**:
```
総合スコア = (
    Fear & Greed: -16 × 1.5 +
    Put/Call: +14 × 1.3 +
    VIX: +8 × 1.2 +
    News: -20 × 1.0
) / (1.5 + 1.3 + 1.2 + 1.0)
= (-24.0 + 18.2 + 9.6 - 20.0) / 5.0
= -16.2 / 5.0
= -22.5
```

**解釈**:
- スコア-22.5は「やや強気」ゾーン（-15 ~ -40）
- Fear & Greedとニュースセンチメントが悲観的 → 逆張り買い支持
- Put/Call比率も悲観的バイアス → 買い支持
- VIXのみやや警戒（ボラティリティ高）

---

## トレード推奨

### センチメント観点からの推奨

- **取引方向**: 買い
- **推奨エントリー価格**: 33,000円前後（押し目待ち）
- **信頼度**: 60%
- **根拠**: 市場が過度に悲観的。Fear & Greedが恐怖ゾーン、ニュースもネガティブ寄り。逆張りで買い場。

### 注意点

1. **ボラティリティ高**: VIX 24.5はやや高め。ポジションサイズ縮小推奨。
2. **Put/Call比率**: 下落への備えが多い = 下落リスク存在。ストップロス厳守。
3. **ニュースノイズ**: ニュースセンチメントは短期的に変動しやすい。重視しすぎない。

---

## データソース

- Fear & Greed Index: CNN Business
- Put/Call比率: JPX日経225オプション統計
- 日経VI: JPXボラティリティ・インデックス
- ニュースセンチメント: Google News「日経平均」検索

---

## 次のアクション

このセンチメント分析結果は、テクニカル分析・エリオット波動分析と統合され、最終的な戦略判定に使用されます。
```

---

## エラーハンドリング

### データ取得失敗時

```python
if fear_greed_index is None:
    # CNN代替ソース: Alternative.me Crypto Fear & Greed（参考値）
    fallback_url = "https://alternative.me/crypto/fear-and-greed-index/"

if put_call_ratio is None:
    # 前日値を使用、または中立値1.0を仮定
    put_call_ratio = 1.0

if vix is None:
    # 過去平均値22.5を仮定
    vix = 22.5

if news_sentiment is None:
    # 中立値0を仮定
    news_sentiment = 0
```

### 部分データでの継続

- 4指標中 **3指標以上**取得できれば分析継続
- 2指標以下の場合は「データ不足、センチメント分析スキップ」と報告

---

## 参考文献

- Sentiment Analysis in Financial Markets - Richard L. Peterson
- Behavioral Finance - Robert J. Shiller
- The Psychology of Risk - Ari Kiev

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
