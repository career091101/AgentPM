---
name: agent-bull-researcher
description: |
  Phase1アナリスト結果を基に強気シナリオを構築する自律型エージェント。
  上昇トレンド継続の前提条件、目標価格、確率、根拠を明確化し、
  1週間の強気シナリオを詳細に設計（15-25分）。

  使用タイミング：
  - Phase1完了後、シナリオ分析を開始する時
  - 強気シナリオの詳細構築が必要な時

  所要時間：15-25分（自動実行）
  出力：bull_scenario.md

trigger_keywords:
  - "強気シナリオ"
  - "Bull Scenario"
  - "上昇シナリオ"

dependencies:
  - trading-phase1-analysts

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bull_scenario.md

execution_time: 15-25分（自動実行）

stage: Phase2 - Research Team (Bull Scenario)

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P1

framework_compliance: 100%
---

# Bull Researcher Skill

Phase1アナリスト結果を基に強気シナリオを構築する自律型エージェント。

---

## このSkillでできること

1. **強気シナリオ構築**: Phase1結果から上昇要因を抽出・強化
2. **目標価格設定**: 1週間の目標価格（上昇率）を設定
3. **確率評価**: 強気シナリオ実現確率を定量評価
4. **根拠明確化**: WebSearchで追加リサーチ、根拠を強化
5. **リスク要因特定**: 強気シナリオを阻害する要因も明記

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `analysts_summary.md`（Phase1結果） |
| **出力** | `bull_scenario.md` |
| **次のSkill** | agent-bear-researcher → agent-research-manager |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 15-25分

### 前提条件確認

#### ステップ1: Phase1結果読み込み

```markdown
Read: `Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md`

抽出項目:
1. 総合判定: [強気/弱気/中立]
2. コンセンサススコア: +X/4
3. Market Analyst 判定: [強気/弱気/中立]
4. Fundamentals 判定: [追い風/逆風/中立]
5. News 判定: [ポジティブ/ネガティブ/中立]
6. Sentiment 判定: [楽観/恐怖/中立]
```

### シナリオ構築フロー（ReActループ）

#### Iteration 1: 強気要因抽出

**Thought**: Phase1で強気判定した要因を抽出し、優先順位付け

**Action**:
```markdown
1. Market Analyst結果から:
   - 強気シグナルの指標リスト（例: MA50 > MA200、MACDゴールデンクロス）
   - エントリー候補価格
   - サポートライン

2. Fundamentals結果から:
   - Tailwinds（追い風）リスト
   - 主要ポジティブファクター

3. News結果から:
   - ポジティブニュース件数・主要テーマ

4. Sentiment結果から:
   - 逆張りシグナル（恐怖時の買いシグナル等）
```

**Observation**: [強気要因リスト作成]

**Result**: 強気要因を重要度順にランク付け

---

#### Iteration 2: 追加リサーチ（強気根拠強化）

**Thought**: 強気シナリオを支持する追加データをWebSearchで収集

**Action**:
```
WebSearch: "日経平均先物 上昇要因 2025年12月"
WebSearch: "日本株 強気見通し 2025年"
WebSearch: "Nikkei 225 bullish outlook December 2025"
WebSearch: "日経平均 テクニカル 買いシグナル"
```

**Observation**: [追加データ収集]

**Result**: 強気根拠を補強する外部データ取得

---

#### Iteration 3: 目標価格設定

**Thought**: テクニカル・ファンダメンタルズから1週間の目標価格を設定

**Action**:
```python
# 目標価格算出ロジック
current_price = XX,XXX  # 現在値

# テクニカル目標
technical_target = current_price + ATR * 3  # ATR 3倍

# レジスタンスライン
resistance = XX,XXX

# ファンダメンタルズ目標（PER・EPS等から算出）
fundamental_target = XX,XXX

# 最終目標価格（保守的に設定）
target_price = min(technical_target, resistance, fundamental_target)
target_return = (target_price - current_price) / current_price * 100
```

**Observation**: [目標価格算出]

**Result**:
- 目標価格: XX,XXX円
- 期待リターン: +X.X%

---

#### Iteration 4: 確率評価

**Thought**: 過去の類似パターン、統計データから実現確率を評価

**Action**:
```python
# 確率評価ロジック
probability_factors = {
    "technical_strength": 0.8 if 6/8指標が強気 else 0.6,
    "fundamentals_support": 0.7 if Tailwinds優勢 else 0.5,
    "news_sentiment": 0.6 if ポジティブ優勢 else 0.4,
    "market_sentiment": 0.5 if センチメント中立〜楽観 else 0.3
}

# 総合確率（保守的に最小値を重視）
weights = [0.3, 0.3, 0.2, 0.2]
bull_probability = sum([p * w for p, w in zip(probability_factors.values(), weights)])
```

**Observation**: [確率算出]

**Result**:
- 強気シナリオ実現確率: XX%

---

#### Iteration 5: リスク要因特定

**Thought**: 強気シナリオを阻害する要因を明記（偏りを防ぐ）

**Action**:
```markdown
リスク要因特定:
1. テクニカルリスク:
   - RSI買われすぎ（70超）
   - レジスタンス突破失敗の可能性

2. ファンダメンタルズリスク:
   - 日銀利上げ観測
   - 米国株調整の波及

3. ニュースリスク:
   - 地政学リスク
   - 企業業績下方修正

4. センチメントリスク:
   - 楽観的すぎる市場心理の反転
```

**Observation**: [リスク要因リスト作成]

**Result**: 強気シナリオのリスク要因を明確化

---

### 最終成果物: bull_scenario.md

```markdown
---
agent: agent-bull-researcher
phase: phase2
timestamp: 2025-12-29 13:00:00
status: completed
scenario: Bull (強気)
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Bull Researcher 強気シナリオ分析レポート

## エグゼクティブサマリー

**シナリオ**: 強気（Bull）
**実現確率**: XX%
**目標価格**: XX,XXX円（現在値: XX,XXX円）
**期待リターン**: +X.X%
**想定期間**: 1週間（5営業日）

**シナリオ概要**:
[1-2文で強気シナリオの核心を説明]

---

## 1. 強気シナリオの前提条件

### 1.1 主要な前提

1. **テクニカル前提**:
   - [前提1]（例: 200日SMAサポート継続）
   - [前提2]（例: MACDゴールデンクロス維持）

2. **ファンダメンタルズ前提**:
   - [前提1]（例: 日銀金融緩和継続）
   - [前提2]（例: 米国株高継続）

3. **ニュース・イベント前提**:
   - [前提1]（例: ポジティブ決算発表継続）
   - [前提2]（例: 地政学リスク顕在化せず）

4. **センチメント前提**:
   - [前提1]（例: リスクオン継続）
   - [前提2]（例: 恐怖指数低位安定）

---

## 2. 強気シナリオの根拠

### 2.1 Phase1アナリスト結果からの根拠

#### Market Analyst（テクニカル分析）

**総合判定**: [強気/弱気/中立]

**強気根拠**:
- [根拠1]: 8指標中X個が強気シグナル
- [根拠2]: ゴールデンクロス形成（MA50 > MA200）
- [根拠3]: サポートライン XX,XXX円で堅調

**詳細**: `market_analysis.md` 参照

---

#### Fundamentals Analyst（マクロ経済分析）

**総合判定**: [追い風/逆風/中立]

**強気根拠**:
- [根拠1]: Tailwinds XX点 > Headwinds XX点
- [根拠2]: 日銀金融緩和継続見込み
- [根拠3]: USD/JPY安定推移

**詳細**: `fundamentals_analysis.md` 参照

---

#### News Analyst（ニュース分析）

**総合センチメント**: [ポジティブ優勢/ネガティブ優勢/中立]

**強気根拠**:
- [根拠1]: ポジティブニュース XX件（XX%）
- [根拠2]: 主要テーマ「[テーマ名]」がポジティブ
- [根拠3]: ネガティブ要因は限定的

**詳細**: `news_analysis.md` 参照

---

#### Sentiment Analyst（市場心理分析）

**総合センチメント**: [恐怖/中立/楽観]

**強気根拠**:
- [根拠1]: VIX指数低位（XX）
- [根拠2]: Fear & Greed Index XX/100（[判定]）
- [根拠3]: 逆張りシグナル「[買い/売り/なし]」

**詳細**: `sentiment_analysis.md` 参照

---

### 2.2 追加リサーチからの根拠

**WebSearch結果**:

1. **[ソース1]**: [URL]
   - [強気根拠の要約]

2. **[ソース2]**: [URL]
   - [強気根拠の要約]

3. **[ソース3]**: [URL]
   - [強気根拠の要約]

---

## 3. 目標価格と期待リターン

### 3.1 目標価格設定

**算出方法**:

| 手法 | 目標価格 | 根拠 |
|------|---------|------|
| テクニカル（ATR 3倍） | XX,XXX円 | 現在値 + ATR×3 |
| レジスタンス突破 | XX,XXX円 | 過去レジスタンスライン |
| ファンダメンタルズ | XX,XXX円 | PER・EPS分析 |

**最終目標価格**: XX,XXX円（保守的に最小値を採用）

### 3.2 期待リターン

```
現在値: XX,XXX円
目標価格: XX,XXX円
期待リターン: +X.X%
想定期間: 1週間（5営業日）
```

### 3.3 エントリー・イグジット戦略

**推奨エントリー価格**: XX,XXX - XX,XXX円
**利益確定目標**: XX,XXX円（+X.X%）
**ストップロス**: XX,XXX円（-X.X%）

---

## 4. 実現確率評価

### 4.1 確率算出ロジック

```python
probability_factors = {
    "technical_strength": 0.XX,  # テクニカル強度
    "fundamentals_support": 0.XX,  # ファンダメンタルズ支持度
    "news_sentiment": 0.XX,  # ニュースセンチメント
    "market_sentiment": 0.XX  # 市場心理
}

weights = [0.3, 0.3, 0.2, 0.2]
bull_probability = sum([p * w for p, w in zip(probability_factors.values(), weights)])
```

**強気シナリオ実現確率**: XX%

### 4.2 確率評価の根拠

| 要因 | スコア | 重み | 加重スコア | 根拠 |
|------|--------|------|-----------|------|
| テクニカル強度 | 0.XX | 30% | 0.XX | [根拠] |
| ファンダメンタルズ | 0.XX | 30% | 0.XX | [根拠] |
| ニュースセンチメント | 0.XX | 20% | 0.XX | [根拠] |
| 市場心理 | 0.XX | 20% | 0.XX | [根拠] |

**合計**: XX%

---

## 5. リスク要因（強気シナリオ阻害要因）

### 5.1 テクニカルリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

**リスク2**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.2 ファンダメンタルズリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.3 ニュース・イベントリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.4 センチメントリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

---

## 6. シナリオ実現のタイムライン

### 1週間のシナリオ展開

**Day 1-2（月-火）**:
- [予想される展開]
- [注視すべきポイント]

**Day 3-4（水-木）**:
- [予想される展開]
- [注視すべきポイント]

**Day 5（金）**:
- [予想される展開]
- [利益確定タイミング]

---

## 7. データソース（監査ログ）

### Phase1入力データ
- `analysts_summary.md` - アクセス日時: YYYY-MM-DD HH:MM

### 追加WebSearch実行履歴
1. [ソース1](URL1) - アクセス日時: YYYY-MM-DD HH:MM
2. [ソース2](URL2) - アクセス日時: YYYY-MM-DD HH:MM
3. [ソース3](URL3) - アクセス日時: YYYY-MM-DD HH:MM

### データ検証
- [ ] Phase1結果読み込み完了
- [ ] 追加WebSearch 3件以上実施
- [ ] 確率算出ロジック明記
- [ ] リスク要因明記

---

## メタデータ

- **実行時間**: XX分
- **WebSearchクエリ数**: 4
- **ReActイテレーション数**: 5
- **入力ファイル**: `analysts_summary.md`
- **次のステップ**: agent-bear-researcher 実行
```

---

## 成果物

### 最終成果物

```
TradingAgents/data/results/phase2/2025-12-29/
└── bull_scenario.md ← このスキルが生成
```

---

## Knowledge Base参照

- Phase1結果: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /agent-bull-researcher

Skill:
# Bull Researcher 自律実行開始

入力: analysts_summary.md
推定所要時間: 15-25分

[自動実行中...]

## Iteration 1: 強気要因抽出 ✅
- Market: 6/8指標が強気
- Fundamentals: Tailwinds 15点 > Headwinds 8点
- News: ポジティブ43%
- Sentiment: 中立やや弱気（逆張り買いシグナル）

## Iteration 2: 追加リサーチ ✅
- WebSearch 4クエリ実行
- 追加根拠 3件取得

## Iteration 3: 目標価格設定 ✅
- テクニカル目標: 34,500円
- レジスタンス: 33,800円
- 最終目標: 34,200円（+3.8%）

## Iteration 4: 確率評価 ✅
- 実現確率: 62%

## Iteration 5: リスク要因特定 ✅
- テクニカルリスク: 2件
- ファンダメンタルズリスク: 2件
- ニュースリスク: 1件

完了時間: 18分
強気シナリオ: 実現確率62%、目標+3.8%

成果物: bull_scenario.md 生成完了
```
