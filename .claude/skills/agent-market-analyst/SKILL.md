---
name: agent-market-analyst
description: |
  日経平均先物のテクニカル分析を実行する自律型エージェント。
  8つのテクニカル指標（SMA50/200、MACD、RSI、ボリンジャーバンド、ATR、VWMA等）を
  WebSearch/WebFetchで収集・分析し、1週間の価格動向を予測。

  使用タイミング：
  - 日経平均先物のトレード戦略立案開始時
  - テクニカル分析の最新データが必要な時

  所要時間：20-30分（自動実行）
  出力：market_analysis.md

trigger_keywords:
  - "マーケット分析"
  - "テクニカル分析"
  - "市場分析"
  - "日経先物分析"

dependencies: []  # Phase 1は独立実行

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/market_analysis.md

execution_time: 20-30分（自動実行）

stage: Phase1 - Market Analysis

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P0

framework_compliance: 100%
---

# Market Analyst Skill

日経平均先物のテクニカル分析を実行する自律型エージェント。

---

## このSkillでできること

1. **テクニカル指標収集**: WebSearch/WebFetchで8指標の最新データを収集
2. **トレンド分析**: 移動平均線（SMA50/200、EMA10）によるトレンド判定
3. **モメンタム分析**: MACD、RSIによる買われすぎ/売られすぎ判定
4. **ボラティリティ分析**: ATR、ボリンジャーバンドによるリスク評価
5. **総合判定**: 8指標の統合による強気/弱気/中立判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（現在日時と対象銘柄は自動設定） |
| **対象** | 日経平均先物（日経225） |
| **期間** | 今後1週間（5営業日） |
| **出力** | `Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/market_analysis.md` |
| **次のSkill** | `/trading-phase1-analysts` または独立使用可能 |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 20-30分

### 自動実行フロー（ReActループ）

#### 準備: 前提条件確認

1. 今日の日付取得（例: 2025-12-29）
2. 対象確認: 日経平均先物（日経225）
3. 分析期間: 今後1週間（5営業日）
4. 出力ディレクトリ確認・作成

---

#### Iteration 1: 現在値とトレンド把握

**Thought（思考）**:
- 日経平均先物の現在値と前日比を確認する必要がある
- 市場の基本的な状況を把握することが最初のステップ

**Action（行動）**:
```
WebSearch: "日経平均先物 2025年12月29日 現在値 前日比"
```

**Observation（観察）**:
- 検索結果から以下を抽出:
  - 現在値: XX,XXX円
  - 前日比: +/-XXX円（+/-X.X%）
  - 取引時間: 日中/夜間
  - データソース: [URL]

**Result（結果）**:
- 現在値=XX,XXX円、前日比=+XXX円を確認
- 基本的な市場状況: [上昇/下降/横ばい]
- データソース記録: [URL1]

---

#### Iteration 2: 移動平均線の状態確認

**Thought（思考）**:
- トレンド判定にはMA50/200のゴールデンクロス/デッドクロスが重要
- 長期・中期・短期トレンドの整合性を確認

**Action（行動）**:
```
WebFetch: "https://www.tradingview.com/symbols/TVC-NI225/"
または
WebSearch: "日経225先物 移動平均線 SMA50 SMA200 2025年12月"
```

**Observation（観察）**:
- TradingViewチャートまたは検索結果から抽出:
  - 200日SMA: XX,XXX円
  - 50日SMA: XX,XXX円
  - 10日EMA: XX,XXX円
  - クロス状態: [ゴールデンクロス/デッドクロス/中立]

**Result（結果）**:
- MA50=XX,XXX円、MA200=XX,XXX円 → [ゴールデンクロス（強気）/デッドクロス（弱気）]
- トレンド方向: [上昇/下降/横ばい]
- データソース記録: [URL2]

---

#### Iteration 3: RSI・MACDでモメンタム確認

**Thought（思考）**:
- 短期的な買われすぎ/売られすぎを判定
- MACDのシグナル線との関係でトレンドの強さを測定

**Action（行動）**:
```
WebSearch: "日経平均 RSI MACD 最新 2025年12月"
WebSearch: "Nikkei 225 futures RSI MACD December 2025"
```

**Observation（観察）**:
- 検索結果から以下を抽出:
  - RSI: XX（0-100）
  - MACD: +/-XXX
  - MACDシグナル線: +/-XXX
  - クロス状態: [ゴールデンクロス/デッドクロス]

**Result（結果）**:
- RSI=68（買われすぎ接近）
- MACDゴールデンクロス → 強気継続
- データソース記録: [URL3, URL4]

---

#### Iteration 4: サポート・レジスタンス特定

**Thought（思考）**:
- エントリー・イグジットレベルの設定に必要
- 重要な価格帯を特定してリスク管理に活用

**Action（行動）**:
```
WebSearch: "日経平均 サポートライン レジスタンスライン 2025年12月"
WebSearch: "site:tradingview.com Nikkei 225 support resistance"
```

**Observation（観察）**:
- テクニカルレポートから抽出:
  - 主要サポート: XX,XXX円（50日SMA付近）
  - 主要レジスタンス: XX,XXX円（ボリンジャーバンド上限）
  - 次のサポート: XX,XXX円
  - 次のレジスタンス: XX,XXX円

**Result（結果）**:
- サポート=32,500円、レジスタンス=33,800円
- 想定価格レンジ: 32,500-34,500円
- データソース記録: [URL5]

---

#### Iteration 5: ボラティリティとATR確認

**Thought（思考）**:
- ストップロス幅の設定にATRが必要
- ボラティリティの状態でリスク管理パラメータを調整

**Action（行動）**:
```
WebSearch: "日経平均 ATR ボリンジャーバンド 2025年12月"
WebFetch: "https://www.investing.com/indices/japan-ni225-technical"
```

**Observation（観察）**:
- ボラティリティ指標を収集:
  - ATR (14日): XXX円
  - ボリンジャーバンド幅: XXX円
  - ボリンジャーバンド上限: XX,XXX円
  - ボリンジャーバンド下限: XX,XXX円
  - 価格位置: [上限接近/中央/下限接近]

**Result（結果）**:
- ATR=450円 → ストップロスは450円幅（ATR 1倍）を推奨
- ボリンジャーバンド幅=1,200円 → 中程度のボラティリティ
- データソース記録: [URL6]

---

#### Iteration 6: 出来高分析

**Thought（思考）**:
- 機関投資家の動向を出来高加重移動平均（VWMA）で確認
- 価格変動の信頼性を出来高で検証

**Action（行動）**:
```
WebSearch: "日経平均先物 出来高 VWMA 2025年12月"
```

**Observation（観察）**:
- 出来高データを収集:
  - VWMA: XX,XXX円
  - 現在の出来高: [増加/減少/平均並み]
  - 出来高トレンド: [上昇/下降/横ばい]

**Result（結果）**:
- VWMA=33,000円 → 価格を下支え、機関投資家買い優勢
- 出来高状況: [強気/弱気/中立]
- データソース記録: [URL7]

---

#### Final Output: market_analysis.md生成

**Action（行動）**:
1. 出力ディレクトリ確認・作成
   ```
   Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/2025-12-29/
   ```

2. 収集した8指標データを統合

3. 総合判定を実施:
   - 強気シグナル数: X/8
   - 弱気シグナル数: Y/8
   - 中立シグナル数: Z/8
   - 総合判定: [強気/弱気/中立]

4. Writeツールで `market_analysis.md` 作成

**Content（内容）**:
```markdown
---
agent: agent-market-analyst
phase: phase1
timestamp: 2025-12-29 10:30:15
status: completed
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Market Analyst テクニカル分析レポート

## エグゼクティブサマリー

**総合判定**: [強気/弱気/中立]（X/8指標が[強気/弱気]シグナル）
**推奨方向**: [ロング/ショート/様子見]
**目標リターン**: +X.X%
**想定リスク**: -X.X%

---

## 1. 選択指標と根拠

**選択した8つの指標**:
1. close_200_sma (200日SMA) - 長期トレンド判定
2. close_50_sma (50日SMA) - 中期トレンド判定
3. close_10_ema (10日EMA) - 短期トレンド判定
4. macd (MACD) - モメンタム判定
5. rsi (RSI) - 買われすぎ/売られすぎ判定
6. boll_ub/boll_lb (ボリンジャーバンド) - 価格レンジ判定
7. atr (ATR) - ボラティリティ判定
8. vwma (出来高加重平均) - 機関投資家動向判定

**選択理由**: スイングトレード戦略に最適化され、トレンド・モメンタム・ボラティリティ・出来高の4要素を網羅

---

## 2. 各指標の詳細分析

### トレンド系指標

| 指標 | 現在値 | シグナル | 強度 | 1週間見通し |
|------|--------|----------|------|-------------|
| 200日SMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| 50日SMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| 10日EMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |

**分析**: [詳細な分析]

---

### モメンタム系指標

| 指標 | 現在値 | シグナル | 強度 | 1週間見通し |
|------|--------|----------|------|-------------|
| MACD | [値] | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| RSI | [値] | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |

**分析**: [詳細な分析]

---

### ボラティリティ系指標

| 指標 | 現在値 | シグナル | 強度 | 1週間見通し |
|------|--------|----------|------|-------------|
| ボリンジャーバンド | 上限[値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| ATR | [値]円 | - | - | [高/中/低]ボラティリティ |

**分析**: [詳細な分析]

---

### 出来高系指標

| 指標 | 現在値 | シグナル | 強度 | 1週間見通し |
|------|--------|----------|------|-------------|
| VWMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |

**分析**: [詳細な分析]

---

## 3. 総合的テクニカル見解

**判定**: [強気（Bull）/弱気（Bear）/中立（Neutral）]

**根拠**:
- 8つの指標のうちX個が強気シグナル（XX%）
- 主要なサポートレベル: XX,XXX円
- 主要なレジスタンスレベル: XX,XXX円
- 想定される価格レンジ: XX,XXX-XX,XXX円

**エントリー候補**:
- **ロング**: XX,XXX-XX,XXX円（[根拠]）
- **ショート**: XX,XXX-XX,XXX円（[根拠]）

---

## 4. テクニカル指標サマリー

| 指標 | 現在値 | シグナル | 強度 | 1週間見通し |
|------|--------|----------|------|-------------|
| 200日SMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| 50日SMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| 10日EMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| MACD | [値] | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| RSI | [値] | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| ボリンジャー | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |
| ATR | [値]円 | - | - | [高/中/低] |
| VWMA | [値]円 | [強気/弱気/中立] | [高/中/低] | [上昇/下降/横ばい] |

**総合スコア**: X/8（XX%の強気シグナル）

---

## 5. データソース（監査ログ）

### WebSearch実行履歴
1. [タイトル1](URL1) - アクセス日時: YYYY-MM-DD HH:MM
2. [タイトル2](URL2) - アクセス日時: YYYY-MM-DD HH:MM
3. [タイトル3](URL3) - アクセス日時: YYYY-MM-DD HH:MM
4. [タイトル4](URL4) - アクセス日時: YYYY-MM-DD HH:MM
5. [タイトル5](URL5) - アクセス日時: YYYY-MM-DD HH:MM
6. [タイトル6](URL6) - アクセス日時: YYYY-MM-DD HH:MM
7. [タイトル7](URL7) - アクセス日時: YYYY-MM-DD HH:MM

### 収集データ検証
- 複数ソースでの数値確認: ✅ 完了（X ソース）
- 異常値検出: ✅ なし / ⚠️ [異常値の詳細]
- データ整合性: ✅ 確認済み

---

## 6. リスク・注意事項

### 短期リスク
1. **[リスク要因1]**: [詳細]（確率XX%）
2. **[リスク要因2]**: [詳細]

### 推奨アクション
- エントリー: XX,XXX-XX,XXX円で[押し目買い/戻り売り]
- ストップロス: XX,XXX円（ATR X倍 = -X.X%）
- 利益確定目標: XX,XXX円（+X.X%）

---

## メタデータ

- **実行時間**: XX分
- **WebSearchクエリ数**: X
- **WebFetch URL数**: X
- **ReActイテレーション数**: 6
```

---

## Knowledge Base参照

### プロジェクト要件
- **テクニカル指標リスト**: `Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`
- **KPI定義**: 同上（シャープレシオ、最大DD等）

### 既存skillsパターン
- **WebSearch活用**: `.claude/skills/research-problem/SKILL.md`
- **自律実行フロー**: `.claude/skills/discover-demand/SKILL.md`
- **オーケストレーション**: `.claude/skills/orchestrate-phase1/SKILL.md`

---

## エラーハンドリング

### WebSearch/Fetch失敗時
1. リトライ（最大3回）
2. 代替クエリで再検索
3. 失敗継続 → 警告表示して続行（利用可能なデータのみで分析）

### データ不足時
- 最低5ソース以上のデータ収集を目指す
- 3ソース未満の場合は警告を出力
- ハルシネーション防止: 推測は「推測:」ラベルで明示

---

## 使用例

```
User: /agent-market-analyst

Skill:
# Market Analyst 自律実行開始

対象: 日経平均先物（日経225）
分析期間: 今後1週間（5営業日）

[自動実行中...]

## Iteration 1: 現在値とトレンド把握 ✅
- Thought: 現在値と前日比を確認
- Action: WebSearch実行
- Result: 現在値=33,200円、前日比=+150円

## Iteration 2: 移動平均線の状態確認 ✅
- Thought: MA50/200でトレンド判定
- Action: WebFetch TradingView
- Result: ゴールデンクロス（強気）

## Iteration 3: RSI・MACDでモメンタム確認 ✅
- Thought: 買われすぎ/売られすぎ判定
- Action: WebSearch実行
- Result: RSI=68、MACDゴールデンクロス

## Iteration 4: サポート・レジスタンス特定 ✅
- Thought: エントリー/イグジットレベル設定
- Action: WebSearch実行
- Result: サポート=32,500円、レジスタンス=33,800円

## Iteration 5: ボラティリティとATR確認 ✅
- Thought: ストップロス幅の設定
- Action: WebSearch + WebFetch
- Result: ATR=450円、ボラティリティ中程度

## Iteration 6: 出来高分析 ✅
- Thought: 機関投資家動向確認
- Action: WebSearch実行
- Result: VWMA=33,000円、買い優勢

## Final Output: market_analysis.md生成 ✅
- 総合判定: 強気（6/8指標が強気シグナル）
- 推奨方向: ロング
- 目標リターン: +5.2%

完了時間: 22分
出力ファイル: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/2025-12-29/market_analysis.md

推奨: `/trading-phase1-analysts` で他のアナリストと統合分析へ
```
