---
name: agent-bear-researcher
description: |
  Phase1アナリスト結果を基に弱気シナリオを構築する自律型エージェント。
  下落トレンド発生の前提条件、目標価格、確率、根拠を明確化し、
  1週間の弱気シナリオを詳細に設計（15-25分）。

  使用タイミング：
  - Phase1完了後、シナリオ分析を開始する時
  - 弱気シナリオの詳細構築が必要な時

  所要時間：15-25分（自動実行）
  出力：bear_scenario.md

trigger_keywords:
  - "弱気シナリオ"
  - "Bear Scenario"
  - "下落シナリオ"

dependencies:
  - trading-phase1-analysts

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bear_scenario.md

execution_time: 15-25分（自動実行）

stage: Phase2 - Research Team (Bear Scenario)

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P1

framework_compliance: 100%
---

# Bear Researcher Skill

Phase1アナリスト結果を基に弱気シナリオを構築する自律型エージェント。

---

## このSkillでできること

1. **弱気シナリオ構築**: Phase1結果から下落要因を抽出・強化
2. **目標価格設定**: 1週間の目標価格（下落率）を設定
3. **確率評価**: 弱気シナリオ実現確率を定量評価
4. **根拠明確化**: WebSearchで追加リサーチ、根拠を強化
5. **リスク要因特定**: 弱気シナリオを阻害する要因（予想外の強気転換）も明記

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `analysts_summary.md`（Phase1結果） |
| **出力** | `bear_scenario.md` |
| **次のSkill** | agent-research-manager（Bull/Bear統合判断） |

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
2. コンセンサススコア: +X/4 or -X/4
3. Market Analyst 判定: [強気/弱気/中立]
4. Fundamentals 判定: [追い風/逆風/中立]
5. News 判定: [ポジティブ/ネガティブ/中立]
6. Sentiment 判定: [楽観/恐怖/中立]
```

### シナリオ構築フロー（ReActループ）

#### Iteration 1: 弱気要因抽出

**Thought**: Phase1で弱気判定した要因、またはリスク要因を抽出し、優先順位付け

**Action**:
```markdown
1. Market Analyst結果から:
   - 弱気シグナルの指標リスト（例: RSI買われすぎ、レジスタンス接近）
   - ショート候補価格
   - レジスタンスライン

2. Fundamentals結果から:
   - Headwinds（逆風）リスト
   - 主要ネガティブファクター

3. News結果から:
   - ネガティブニュース件数・主要テーマ

4. Sentiment結果から:
   - 逆張りシグナル（楽観時の売りシグナル等）
   - 過度な楽観指標
```

**Observation**: [弱気要因リスト作成]

**Result**: 弱気要因を重要度順にランク付け

---

#### Iteration 2: 追加リサーチ（弱気根拠強化）

**Thought**: 弱気シナリオを支持する追加データをWebSearchで収集

**Action**:
```
WebSearch: "日経平均先物 下落リスク 2025年12月"
WebSearch: "日本株 弱気見通し 2025年"
WebSearch: "Nikkei 225 bearish outlook December 2025"
WebSearch: "日経平均 テクニカル 売りシグナル"
```

**Observation**: [追加データ収集]

**Result**: 弱気根拠を補強する外部データ取得

---

#### Iteration 3: 目標価格設定（下落目標）

**Thought**: テクニカル・ファンダメンタルズから1週間の下落目標価格を設定

**Action**:
```python
# 下落目標価格算出ロジック
current_price = XX,XXX  # 現在値

# テクニカル目標
technical_target = current_price - ATR * 3  # ATR 3倍下落

# サポートライン
support = XX,XXX

# ファンダメンタルズ目標
fundamental_target = XX,XXX

# 最終目標価格（保守的に設定 = 下落幅を控えめに）
target_price = max(technical_target, support, fundamental_target)
target_return = (target_price - current_price) / current_price * 100  # マイナス値
```

**Observation**: [下落目標価格算出]

**Result**:
- 目標価格: XX,XXX円
- 期待リターン: -X.X%

---

#### Iteration 4: 確率評価

**Thought**: 過去の類似パターン、統計データから弱気シナリオ実現確率を評価

**Action**:
```python
# 確率評価ロジック
probability_factors = {
    "technical_weakness": 0.8 if 6/8指標が弱気 else 0.6,
    "fundamentals_headwind": 0.7 if Headwinds優勢 else 0.5,
    "news_sentiment": 0.6 if ネガティブ優勢 else 0.4,
    "market_sentiment": 0.5 if センチメント極端な楽観 else 0.3
}

# 総合確率（保守的に最小値を重視）
weights = [0.3, 0.3, 0.2, 0.2]
bear_probability = sum([p * w for p, w in zip(probability_factors.values(), weights)])
```

**Observation**: [確率算出]

**Result**:
- 弱気シナリオ実現確率: XX%

---

#### Iteration 5: リスク要因特定（予想外の強気転換）

**Thought**: 弱気シナリオを阻害する要因を明記（偏りを防ぐ）

**Action**:
```markdown
リスク要因特定（予想外の強気転換）:
1. テクニカルリスク:
   - サポートライン堅守による反発
   - 底値買い殺到

2. ファンダメンタルズリスク:
   - 日銀追加緩和サプライズ
   - 米国株予想外の上昇

3. ニュースリスク:
   - ポジティブサプライズ決算
   - 政策発表

4. センチメントリスク:
   - 過度な恐怖による逆張り買い
```

**Observation**: [リスク要因リスト作成]

**Result**: 弱気シナリオのリスク要因を明確化

---

### 最終成果物: bear_scenario.md

```markdown
---
agent: agent-bear-researcher
phase: phase2
timestamp: 2025-12-29 13:20:00
status: completed
scenario: Bear (弱気)
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Bear Researcher 弱気シナリオ分析レポート

## エグゼクティブサマリー

**シナリオ**: 弱気（Bear）
**実現確率**: XX%
**目標価格**: XX,XXX円（現在値: XX,XXX円）
**期待リターン**: -X.X%
**想定期間**: 1週間（5営業日）

**シナリオ概要**:
[1-2文で弱気シナリオの核心を説明]

---

## 1. 弱気シナリオの前提条件

### 1.1 主要な前提

1. **テクニカル前提**:
   - [前提1]（例: レジスタンス突破失敗）
   - [前提2]（例: MACDデッドクロス形成）

2. **ファンダメンタルズ前提**:
   - [前提1]（例: 日銀利上げ観測強まる）
   - [前提2]（例: 米国株調整）

3. **ニュース・イベント前提**:
   - [前提1]（例: ネガティブ決算発表）
   - [前提2]（例: 地政学リスク顕在化）

4. **センチメント前提**:
   - [前提1]（例: リスクオフ継続）
   - [前提2]（例: 恐怖指数上昇）

---

## 2. 弱気シナリオの根拠

### 2.1 Phase1アナリスト結果からの根拠

#### Market Analyst（テクニカル分析）

**総合判定**: [強気/弱気/中立]

**弱気根拠**:
- [根拠1]: 8指標中X個が弱気シグナル
- [根拠2]: デッドクロス形成（MA50 < MA200）
- [根拠3]: レジスタンスライン XX,XXX円で頭打ち

**詳細**: `market_analysis.md` 参照

---

#### Fundamentals Analyst（マクロ経済分析）

**総合判定**: [追い風/逆風/中立]

**弱気根拠**:
- [根拠1]: Headwinds XX点 > Tailwinds XX点
- [根拠2]: 日銀利上げ観測
- [根拠3]: USD/JPY 円高圧力

**詳細**: `fundamentals_analysis.md` 参照

---

#### News Analyst（ニュース分析）

**総合センチメント**: [ポジティブ優勢/ネガティブ優勢/中立]

**弱気根拠**:
- [根拠1]: ネガティブニュース XX件（XX%）
- [根拠2]: 主要テーマ「[テーマ名]」がネガティブ
- [根拠3]: ポジティブ要因は限定的

**詳細**: `news_analysis.md` 参照

---

#### Sentiment Analyst（市場心理分析）

**総合センチメント**: [恐怖/中立/楽観]

**弱気根拠**:
- [根拠1]: VIX指数高位（XX）
- [根拠2]: Fear & Greed Index XX/100（[Extreme Fear/Fear]）
- [根拠3]: 逆張りシグナル「[売り]」

**詳細**: `sentiment_analysis.md` 参照

---

### 2.2 追加リサーチからの根拠

**WebSearch結果**:

1. **[ソース1]**: [URL]
   - [弱気根拠の要約]

2. **[ソース2]**: [URL]
   - [弱気根拠の要約]

3. **[ソース3]**: [URL]
   - [弱気根拠の要約]

---

## 3. 目標価格と期待リターン

### 3.1 目標価格設定（下落目標）

**算出方法**:

| 手法 | 目標価格 | 根拠 |
|------|---------|------|
| テクニカル（ATR 3倍下落） | XX,XXX円 | 現在値 - ATR×3 |
| サポートライン割れ | XX,XXX円 | 過去サポートライン |
| ファンダメンタルズ | XX,XXX円 | PER・EPS下方修正 |

**最終目標価格**: XX,XXX円（保守的に最大値を採用 = 下落幅控えめ）

### 3.2 期待リターン

```
現在値: XX,XXX円
目標価格: XX,XXX円
期待リターン: -X.X%
想定期間: 1週間（5営業日）
```

### 3.3 エントリー・イグジット戦略

**推奨エントリー価格（ショート）**: XX,XXX - XX,XXX円
**利益確定目標**: XX,XXX円（-X.X%）
**ストップロス**: XX,XXX円（+X.X%）

---

## 4. 実現確率評価

### 4.1 確率算出ロジック

```python
probability_factors = {
    "technical_weakness": 0.XX,  # テクニカル弱気度
    "fundamentals_headwind": 0.XX,  # ファンダメンタルズ逆風度
    "news_sentiment": 0.XX,  # ニュースセンチメント
    "market_sentiment": 0.XX  # 市場心理
}

weights = [0.3, 0.3, 0.2, 0.2]
bear_probability = sum([p * w for p, w in zip(probability_factors.values(), weights)])
```

**弱気シナリオ実現確率**: XX%

### 4.2 確率評価の根拠

| 要因 | スコア | 重み | 加重スコア | 根拠 |
|------|--------|------|-----------|------|
| テクニカル弱気度 | 0.XX | 30% | 0.XX | [根拠] |
| ファンダメンタルズ逆風 | 0.XX | 30% | 0.XX | [根拠] |
| ニュースセンチメント | 0.XX | 20% | 0.XX | [根拠] |
| 市場心理 | 0.XX | 20% | 0.XX | [根拠] |

**合計**: XX%

---

## 5. リスク要因（弱気シナリオ阻害要因 = 予想外の強気転換）

### 5.1 テクニカルリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]（例: サポートライン堅守で反発）
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

**リスク2**: [リスク名]
- **詳細**: [詳細説明]
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.2 ファンダメンタルズリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]（例: 日銀追加緩和サプライズ）
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.3 ニュース・イベントリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]（例: ポジティブサプライズ決算）
- **発生確率**: [高/中/低]
- **影響度**: [大/中/小]

### 5.4 センチメントリスク

**リスク1**: [リスク名]
- **詳細**: [詳細説明]（例: 過度な恐怖による逆張り買い）
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
- **次のステップ**: agent-research-manager 実行（Bull/Bear統合）
```

---

## 成果物

### 最終成果物

```
TradingAgents/data/results/phase2/2025-12-29/
└── bear_scenario.md ← このスキルが生成
```

---

## Knowledge Base参照

- Phase1結果: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /agent-bear-researcher

Skill:
# Bear Researcher 自律実行開始

入力: analysts_summary.md
推定所要時間: 15-25分

[自動実行中...]

## Iteration 1: 弱気要因抽出 ✅
- Market: 2/8指標が弱気（RSI買われすぎ）
- Fundamentals: Headwinds 8点 < Tailwinds 15点
- News: ネガティブ34%
- Sentiment: 中立やや弱気

## Iteration 2: 追加リサーチ ✅
- WebSearch 4クエリ実行
- 追加根拠 3件取得

## Iteration 3: 目標価格設定 ✅
- テクニカル目標: 31,200円
- サポート: 32,000円
- 最終目標: 32,000円（-2.8%）

## Iteration 4: 確率評価 ✅
- 実現確率: 38%

## Iteration 5: リスク要因特定 ✅
- テクニカルリスク: 2件
- ファンダメンタルズリスク: 2件
- センチメントリスク: 1件

完了時間: 17分
弱気シナリオ: 実現確率38%、目標-2.8%

成果物: bear_scenario.md 生成完了
```
