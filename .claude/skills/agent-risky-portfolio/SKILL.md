---
name: agent-risky-portfolio
description: |
  積極的なリスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。
  レバレッジ2倍、ストップロス-5%、目標+10%の高リスク高リターン戦略（5-10分）。

  使用タイミング：
  - Phase2完了後、リスク管理フェーズで積極的戦略が必要な時
  - 高リスク許容度のトレーダー向け

  所要時間：5-10分（自動実行）
  出力：risky_portfolio.md

trigger_keywords:
  - "積極的ポートフォリオ"
  - "Risky Portfolio"
  - "ハイリスク戦略"

dependencies:
  - trading-phase2-research

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risky_portfolio.md

execution_time: 5-10分（自動実行）

stage: Phase3 - Risk Management Team (Risky Portfolio)

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P1

framework_compliance: 100%
---

# Risky Portfolio Skill

積極的なリスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。

---

## このSkillでできること

1. **高リスク高リターン戦略**: レバレッジ2倍、目標+10%
2. **積極的なポジションサイジング**: フルポジション推奨
3. **広いストップロス**: -5%（大きな値動きに耐える）
4. **VaR計算**: 95%信頼区間でのリスク評価
5. **ストレステスト**: 最悪シナリオでの損失評価

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `research_consensus.md`（Phase2結果） |
| **出力** | `risky_portfolio.md` |
| **次のSkill** | agent-risk-manager（3ポートフォリオ統合判断） |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 5-10分

### ポートフォリオ設計パラメータ

```yaml
Risk Profile: Risky（積極的）
Leverage: 2倍
Target Return: +10%
Stop Loss: -5%
Position Size: フル（100%）
Risk Tolerance: 高
```

### ポートフォリオ設計フロー

#### ステップ1: Phase2結果読み込み

```markdown
Read: `research_consensus.md`

抽出項目:
- 最終推奨: [ロング/ショート/中立/見送り]
- 期待リターン: +X.XX%
- Risk/Reward比率: X.XX
- 推奨エントリー価格: XX,XXX - XX,XXX円
- 利益確定目標: XX,XXX円
- ストップロス推奨: XX,XXX円
```

#### ステップ2: リスキー戦略設計

```python
# リスキーポートフォリオ設計
leverage = 2.0  # レバレッジ2倍
position_size = 1.0  # フルポジション
stop_loss_pct = -5.0  # ストップロス-5%
target_return_pct = +10.0  # 目標+10%

# エントリー価格（推奨範囲の上限）
entry_price = research_consensus["entry_price_upper"]  # 積極的エントリー

# 利益確定目標（Phase2目標の2倍）
profit_target = entry_price * (1 + target_return_pct / 100)

# ストップロス
stop_loss = entry_price * (1 + stop_loss_pct / 100)

# レバレッジ考慮の実質リターン
leveraged_return = target_return_pct * leverage
leveraged_loss = stop_loss_pct * leverage
```

#### ステップ3: VaR計算

```python
# VaR（Value at Risk）計算（95%信頼区間）
import math

volatility = 0.02  # 日次ボラティリティ2%（過去データから推定）
time_horizon = 5  # 5営業日（1週間）

# パラメトリックVaR
daily_var_95 = 1.65 * volatility  # 95%信頼区間のz値
period_var_95 = daily_var_95 * math.sqrt(time_horizon)

# レバレッジ考慮
leveraged_var_95 = period_var_95 * leverage

VaR_95 = leveraged_var_95 * 100  # パーセント表示
```

#### ステップ4: ストレステスト

```python
# ストレステスト（最悪シナリオ）
stress_scenarios = {
    "通常の下落": -3.0,  # -3%
    "大幅下落": -7.0,  # -7%
    "暴落": -15.0  # -15%
}

# レバレッジ考慮の損失
stressed_losses = {
    scenario: loss * leverage
    for scenario, loss in stress_scenarios.items()
}
```

---

## 最終成果物: risky_portfolio.md

```markdown
---
agent: agent-risky-portfolio
phase: phase3
timestamp: 2025-12-29 14:00:00
status: completed
profile: Risky（積極的）
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Risky Portfolio 積極的戦略レポート

## エグゼクティブサマリー

**リスクプロファイル**: Risky（積極的）
**レバレッジ**: 2倍
**目標リターン**: +10%（レバレッジ考慮）
**ストップロス**: -5%（レバレッジ考慮で実質-10%）
**ポジションサイズ**: フル（100%）
**VaR（95%信頼区間）**: -X.X%

---

## 1. ポートフォリオ設計パラメータ

### 1.1 基本パラメータ

| パラメータ | 値 | 説明 |
|----------|-----|------|
| リスクプロファイル | Risky | 積極的 |
| レバレッジ | 2倍 | 資金の2倍のポジション |
| ポジションサイズ | 100% | フルポジション |
| 目標リターン | +10% | レバレッジ考慮後 |
| ストップロス | -5% | レバレッジ考慮後 |
| Risk/Reward | 2.0 | 目標+10% / リスク-5% |

### 1.2 Phase2推奨との比較

| 項目 | Phase2推奨 | Risky Portfolio | 差分 |
|------|-----------|----------------|------|
| 推奨方向 | [ロング/ショート] | 同じ | - |
| 目標リターン | +X.XX% | +10% | より積極的 |
| ストップロス | -X.X% | -5% | より広い |
| レバレッジ | 1倍 | 2倍 | 2倍 |

---

## 2. エントリー・イグジット戦略

### 2.1 エントリー戦略

**エントリー価格**: XX,XXX円（Phase2推奨範囲の上限）
**エントリータイミング**: [詳細]
**ポジション構築**:
- 初回: 50%（XX,XXX円で）
- 追加: 50%（XX,XXX円で）

### 2.2 利益確定戦略

**第1目標**: XX,XXX円（+5%）- 50%利益確定
**第2目標**: XX,XXX円（+10%）- 残り50%利益確定
**最大目標**: XX,XXX円（+15%）- 追加機会あれば

### 2.3 損切り戦略

**ストップロス**: XX,XXX円（-5%）
**実質損失**: -10%（レバレッジ2倍考慮）
**強制ロスカット**: -10%で全ポジション決済

---

## 3. リスク分析

### 3.1 VaR（Value at Risk）

**計算方法**: パラメトリックVaR（95%信頼区間）

```
ボラティリティ: 2%/日
期間: 5営業日
レバレッジ: 2倍

VaR（95%）= 1.65 × 0.02 × √5 × 2 = X.X%
```

**解釈**: 95%の確率で、損失は-X.X%以内に収まる

### 3.2 ストレステスト

| シナリオ | 市場下落 | レバレッジなし損失 | レバレッジ2倍損失 |
|---------|---------|-----------------|----------------|
| 通常の下落 | -3% | -3% | -6% |
| 大幅下落 | -7% | -7% | -14% ⚠️ |
| 暴落 | -15% | -15% | -30% ❌ |

**評価**: 大幅下落時にストップロス突破リスク

---

## 4. リスク・リワード評価

### 4.1 期待値計算

```python
# Phase2からの確率・リターン
P_bull = 0.XX  # Bull確率
R_bull_risky = +10%  # Riskyポートフォリオ目標
P_bear = 0.XX  # Bear確率
R_bear_risky = -10%  # Riskyポートフォリオストップロス（レバレッジ考慮）

E_return_risky = (P_bull × +10%) + (P_bear × -10%)
               = +X.XX%
```

**判定**: [ポジティブ/ネガティブ]

### 4.2 シャープレシオ推定

```
期待リターン: +X.XX%
リスク（標準偏差）: X.X%
無リスク金利: 0.1%

シャープレシオ = (X.XX% - 0.1%) / X.X% = X.XX
```

**評価**: [優秀（>1.0）/良好（>0.5）/不適切（<0.5）]

---

## 5. 推奨投資家プロファイル

### 5.1 適合する投資家

**最適**:
- リスク許容度: 高
- 経験レベル: 上級者
- 資金余裕度: 十分（損失許容-10%）
- 投資期間: 短期（1週間）

**不適合**:
- リスク許容度: 低〜中
- 経験レベル: 初心者
- 資金余裕度: 限定的

### 5.2 リスク警告

⚠️ **警告**:
- レバレッジ2倍により損失も2倍
- ストップロス-5%＝実質-10%損失
- 大幅下落時はストップロス突破リスク
- 初心者には不適切

---

## 6. 実行プラン

### 6.1 実行チェックリスト

- [ ] 証拠金確認（レバレッジ2倍分）
- [ ] ストップロス注文設定（XX,XXX円）
- [ ] 利益確定注文設定（第1目標: XX,XXX円）
- [ ] リスク管理ルール確認
- [ ] 最大損失許容額確認（-10%）

### 6.2 モニタリング項目

**日次確認**:
- [ ] ポジション損益
- [ ] VaR更新
- [ ] Phase2前提条件の変化

**即時対応が必要な状況**:
- ストップロス接近（-4%以上）
- Phase2前提条件崩壊
- 重大ニュース発表

---

## メタデータ

- **実行時間**: X分
- **入力ファイル**: `research_consensus.md`
- **次のステップ**: agent-risk-manager（3ポートフォリオ統合判断）
```

---

## 成果物

```
TradingAgents/data/results/phase3/2025-12-29/
└── risky_portfolio.md ← このスキルが生成
```

---

## Knowledge Base参照

- Phase2結果: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /agent-risky-portfolio

Skill:
# Risky Portfolio 自律実行開始

入力: research_consensus.md
リスクプロファイル: Risky（積極的）
推定所要時間: 5-10分

[自動実行中...]

## ステップ1: Phase2結果読み込み ✅
- 推奨方向: ロング（慎重）
- 期待リターン: +1.29%
- エントリー: 32,600-32,800円

## ステップ2: リスキー戦略設計 ✅
- レバレッジ: 2倍
- 目標: +10%（34,500円）
- ストップロス: -5%（31,200円、実質-10%）

## ステップ3: VaR計算 ✅
- VaR（95%）: -7.4%

## ステップ4: ストレステスト ✅
- 通常下落: -6%
- 大幅下落: -14%（ストップロス突破リスク）

完了時間: 7分
推奨: 上級者向け、高リスク許容度必須

成果物: risky_portfolio.md 生成完了
```
