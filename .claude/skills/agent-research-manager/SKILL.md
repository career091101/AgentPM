---
name: agent-research-manager
description: |
  Bull/Bearシナリオを統合判断する自律型エージェント。
  両シナリオの確率・期待リターンを分析し、期待値計算で最終推奨を決定。
  リスク・リワード比率、確信度を評価し、Phase3への引き継ぎ事項を明確化（10-20分）。

  使用タイミング：
  - Bull/Bearシナリオ完成後、統合判断が必要な時
  - Phase2の最終判断を行う時

  所要時間：10-20分（自動実行）
  出力：research_consensus.md

trigger_keywords:
  - "シナリオ統合"
  - "Research Manager"
  - "Bull Bear統合"

dependencies:
  - agent-bull-researcher
  - agent-bear-researcher

input_files:
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bull_scenario.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bear_scenario.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

execution_time: 10-20分（自動実行）

stage: Phase2 - Research Team (Consensus)

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P1

framework_compliance: 100%
---

# Research Manager Skill

Bull/Bearシナリオを統合判断する自律型エージェント。

---

## このSkillでできること

1. **シナリオ比較**: Bull/Bearシナリオの詳細比較
2. **期待リターン計算**: 確率加重期待値の算出
3. **リスク・リワード分析**: リスク対リターンの評価
4. **最終推奨**: ロング/ショート/中立/見送りの判断
5. **Phase3引き継ぎ**: リスク管理チームへの指示明確化

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `bull_scenario.md`, `bear_scenario.md` |
| **出力** | `research_consensus.md` |
| **次のSkill** | trading-phase3-risk（リスク管理チーム） |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 10-20分

### 前提条件確認

#### ステップ1: Bull/Bearシナリオ読み込み

```markdown
Read: `bull_scenario.md`
抽出項目:
- 実現確率: XX%
- 目標価格: XX,XXX円
- 期待リターン: +X.X%
- 主要根拠: [リスト]
- リスク要因: [リスト]

Read: `bear_scenario.md`
抽出項目:
- 実現確率: XX%
- 目標価格: XX,XXX円
- 期待リターン: -X.X%
- 主要根拠: [リスト]
- リスク要因: [リスト]
```

### 統合判断フロー（ReActループ）

#### Iteration 1: シナリオ比較

**Thought**: Bull/Bearシナリオの確率・リターン・根拠を比較

**Action**:
```python
# シナリオ比較テーブル作成
comparison = {
    "Bull": {
        "probability": 0.XX,
        "return": +X.XX,
        "confidence": "高/中/低"
    },
    "Bear": {
        "probability": 0.XX,
        "return": -X.XX,
        "confidence": "高/中/低"
    }
}
```

**Observation**: [比較テーブル作成]

**Result**: 両シナリオの定量比較完了

---

#### Iteration 2: 期待リターン計算

**Thought**: 確率加重期待値を算出し、統計的優位性を判定

**Action**:
```python
# 期待リターン計算
P_bull = 0.XX  # Bull確率
R_bull = +X.XX  # Bullリターン（%）
P_bear = 0.XX  # Bear確率
R_bear = -X.XX  # Bearリターン（%）

# 期待値
E_return = (P_bull * R_bull) + (P_bear * R_bear)

# 確率正規化チェック
if abs((P_bull + P_bear) - 1.0) > 0.05:
    # 確率合計が100%でない場合は正規化
    total_prob = P_bull + P_bear
    P_bull_normalized = P_bull / total_prob
    P_bear_normalized = P_bear / total_prob
    E_return = (P_bull_normalized * R_bull) + (P_bear_normalized * R_bear)
```

**Observation**: [期待リターン算出]

**Result**:
- 期待リターン: +X.XX% or -X.XX%
- 判定: [ポジティブ/ネガティブ/中立]

---

#### Iteration 3: リスク・リワード分析

**Thought**: リスクとリターンのバランスを評価

**Action**:
```python
# リスク・リワード比率
# リスク = 最大損失（Bearシナリオリターン）
# リワード = 最大利益（Bullシナリオリターン）

risk = abs(R_bear)  # Bearシナリオの下落幅
reward = abs(R_bull)  # Bullシナリオの上昇幅

risk_reward_ratio = reward / risk if risk > 0 else float('inf')

# 判定
if risk_reward_ratio >= 2.0:
    rr_judgment = "優秀（リワード2倍以上）"
elif risk_reward_ratio >= 1.5:
    rr_judgment = "良好（リワード1.5倍以上）"
elif risk_reward_ratio >= 1.0:
    rr_judgment = "許容範囲（リワード≥リスク）"
else:
    rr_judgment = "不適切（リスク＞リワード）"
```

**Observation**: [リスク・リワード比率算出]

**Result**:
- Risk/Reward比率: X.XX
- 判定: [優秀/良好/許容範囲/不適切]

---

#### Iteration 4: 最終推奨決定

**Thought**: 期待リターン、確率、リスク・リワード比率から最終推奨を決定

**Action**:
```python
# 最終推奨ロジック
if E_return > 2.0 and P_bull > 0.6 and risk_reward_ratio >= 1.5:
    recommendation = "ロング（強気）"
    confidence = "高"
elif E_return > 1.0 and P_bull > 0.5 and risk_reward_ratio >= 1.2:
    recommendation = "ロング（慎重）"
    confidence = "中"
elif E_return < -2.0 and P_bear > 0.6 and risk_reward_ratio >= 1.5:
    recommendation = "ショート（強気）"
    confidence = "高"
elif E_return < -1.0 and P_bear > 0.5 and risk_reward_ratio >= 1.2:
    recommendation = "ショート（慎重）"
    confidence = "中"
elif abs(E_return) < 1.0:
    recommendation = "中立（様子見）"
    confidence = "低"
else:
    recommendation = "見送り（不明確）"
    confidence = "非常に低"
```

**Observation**: [最終推奨決定]

**Result**:
- 推奨: [ロング/ショート/中立/見送り]
- 確信度: [高/中/低/非常に低]

---

#### Iteration 5: Phase3引き継ぎ事項作成

**Thought**: リスク管理チーム（Phase3）への指示を明確化

**Action**:
```markdown
Phase3への指示:
1. 推奨方向: [ロング/ショート/中立]
2. 目標リターン: +X.XX% または -X.XX%
3. 許容リスク: X.XX%
4. 重点検証事項: [Bull/Bear シナリオの主要前提条件]
5. ストップロス推奨: XX,XXX円（-X.X%）
```

**Observation**: [Phase3引き継ぎ事項作成]

**Result**: リスク管理チームへの明確な指示完成

---

### 最終成果物: research_consensus.md

```markdown
---
agent: agent-research-manager
phase: phase2
timestamp: 2025-12-29 13:40:00
status: completed
recommendation: [ロング/ショート/中立/見送り]
confidence: [高/中/低]
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Research Manager シナリオ統合分析レポート

## エグゼクティブサマリー

**最終推奨**: [ロング（強気）/ロング（慎重）/ショート（強気）/ショート（慎重）/中立（様子見）/見送り]
**確信度**: [高/中/低/非常に低]
**期待リターン**: +X.XX% または -X.XX%
**Risk/Reward比率**: X.XX
**推奨ポジション**: [ロング/ショート/中立]

**判断根拠サマリー**:
- Bullシナリオ確率: XX%、目標+X.X%
- Bearシナリオ確率: XX%、目標-X.X%
- 期待リターン: (XX% × +X.X%) + (XX% × -X.X%) = +X.XX%

---

## 1. シナリオ比較分析

### 1.1 Bull vs Bear 比較テーブル

| 項目 | Bullシナリオ | Bearシナリオ | 優位 |
|------|-------------|-------------|------|
| 実現確率 | XX% | XX% | [Bull/Bear/同等] |
| 目標価格 | XX,XXX円 | XX,XXX円 | - |
| 期待リターン | +X.X% | -X.X% | - |
| 確信度 | [高/中/低] | [高/中/低] | [Bull/Bear/同等] |
| 根拠の強さ | [強/中/弱] | [強/中/弱] | [Bull/Bear/同等] |

### 1.2 主要根拠の比較

#### Bullシナリオ主要根拠（Top 3）
1. [根拠1]
2. [根拠2]
3. [根拠3]

#### Bearシナリオ主要根拠（Top 3）
1. [根拠1]
2. [根拠2]
3. [根拠3]

### 1.3 総合評価

**優位シナリオ**: [Bull/Bear/同等]

**理由**:
- [理由1]
- [理由2]
- [理由3]

---

## 2. 期待リターン分析

### 2.1 期待値計算

```
Bullシナリオ:
  確率: XX%
  リターン: +X.X%
  期待値寄与: (0.XX × +X.X%) = +X.XX%

Bearシナリオ:
  確率: XX%
  リターン: -X.X%
  期待値寄与: (0.XX × -X.X%) = -X.XX%

期待リターン = +X.XX% + (-X.XX%) = +X.XX%
```

**判定**: [ポジティブ/ネガティブ/中立]

### 2.2 確率正規化

```python
# 確率合計チェック
P_bull + P_bear = XX% + XX% = XX%

# 正規化（100%に調整）
P_bull_normalized = XX% / XX% = XX%
P_bear_normalized = XX% / XX% = XX%

# 正規化後の期待リターン
E_return_normalized = +X.XX%
```

---

## 3. リスク・リワード分析

### 3.1 Risk/Reward比率

```
最大リワード（Bullシナリオ）: +X.X%
最大リスク（Bearシナリオ）: -X.X%（絶対値: X.X%）

Risk/Reward比率 = X.X% / X.X% = X.XX
```

**判定**: [優秀（≥2.0）/良好（≥1.5）/許容範囲（≥1.0）/不適切（<1.0）]

### 3.2 リスク・リワード解釈

**評価**: [詳細評価]

**推奨アクション**:
- [アクション1]
- [アクション2]

---

## 4. 最終推奨

### 4.1 推奨ポジション

**推奨**: [ロング（強気）/ロング（慎重）/ショート（強気）/ショート（慎重）/中立（様子見）/見送り]
**確信度**: [高/中/低/非常に低]

**根拠**:
```
期待リターン: +X.XX% [ポジティブ/ネガティブ]
Bull確率: XX% [高/中/低]
Risk/Reward比率: X.XX [優秀/良好/許容範囲/不適切]

判定ロジック: [詳細説明]
```

### 4.2 エントリー・イグジット戦略

**推奨エントリー価格**: XX,XXX - XX,XXX円
**利益確定目標**:
- 第1目標: XX,XXX円（+X.X%）
- 第2目標: XX,XXX円（+X.X%）

**ストップロス**: XX,XXX円（-X.X%）

**ポジションサイズ推奨**: [フル/ハーフ/ライト/見送り]

---

## 5. シナリオ別対応戦略

### 5.1 Bullシナリオ実現時の対応

**確率**: XX%

**対応戦略**:
1. エントリー: [詳細]
2. 利益確定: [詳細]
3. リスク管理: [詳細]

### 5.2 Bearシナリオ実現時の対応

**確率**: XX%

**対応戦略**:
1. ストップロス執行: [詳細]
2. ポジション調整: [詳細]
3. リスク管理: [詳細]

---

## 6. Phase3への引き継ぎ事項

### 6.1 リスク管理チームへの指示

**基本方針**:
- 推奨方向: [ロング/ショート/中立]
- 目標リターン: +X.XX%
- 許容リスク: X.XX%
- Risk/Reward目標: X.XX以上

**重点検証事項**:
1. [検証項目1]: [詳細]
2. [検証項目2]: [詳細]
3. [検証項目3]: [詳細]

**ポートフォリオ設計指示**:
- リスキー戦略: [指示]
- セーフ戦略: [指示]
- ニュートラル戦略: [指示]

### 6.2 監視すべき前提条件

**Bullシナリオ前提条件**:
1. [前提1]
2. [前提2]
3. [前提3]

**Bearシナリオ前提条件**:
1. [前提1]
2. [前提2]
3. [前提3]

**前提崩壊時の対応**:
- [対応策]

---

## 7. データソース（監査ログ）

### 入力ファイル
- `bull_scenario.md` - アクセス日時: YYYY-MM-DD HH:MM
- `bear_scenario.md` - アクセス日時: YYYY-MM-DD HH:MM

### 計算検証
- [ ] 期待リターン計算完了
- [ ] 確率正規化完了
- [ ] Risk/Reward比率算出完了
- [ ] 最終推奨ロジック明記

---

## メタデータ

- **実行時間**: XX分
- **ReActイテレーション数**: 5
- **入力ファイル**: `bull_scenario.md`, `bear_scenario.md`
- **次のステップ**: trading-phase3-risk（リスク管理チーム）
```

---

## 成果物

### 最終成果物

```
TradingAgents/data/results/phase2/2025-12-29/
├── bull_scenario.md         ← Bull Researcher作成
├── bear_scenario.md         ← Bear Researcher作成
└── research_consensus.md    ← このスキルが生成
```

---

## Knowledge Base参照

- Bull Scenario: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bull_scenario.md`
- Bear Scenario: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/bear_scenario.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /agent-research-manager

Skill:
# Research Manager 自律実行開始

入力: bull_scenario.md, bear_scenario.md
推定所要時間: 10-20分

[自動実行中...]

## Iteration 1: シナリオ比較 ✅
- Bull: 確率62%、目標+3.8%
- Bear: 確率38%、目標-2.8%

## Iteration 2: 期待リターン計算 ✅
- 期待リターン = (0.62 × +3.8%) + (0.38 × -2.8%)
- 期待リターン = +2.356% - 1.064% = +1.292%
- 判定: ポジティブ

## Iteration 3: リスク・リワード分析 ✅
- Risk: 2.8%
- Reward: 3.8%
- Risk/Reward比率 = 3.8 / 2.8 = 1.36
- 判定: 許容範囲（≥1.0）

## Iteration 4: 最終推奨決定 ✅
- 推奨: ロング（慎重）
- 確信度: 中
- 根拠: 期待リターン+1.29%、R/R比1.36

## Iteration 5: Phase3引き継ぎ ✅
- 推奨方向: ロング
- 目標リターン: +1.3%〜+3.8%
- 許容リスク: -2.8%

完了時間: 15分
最終推奨: ロング（慎重）、期待+1.29%

成果物: research_consensus.md 生成完了
```
