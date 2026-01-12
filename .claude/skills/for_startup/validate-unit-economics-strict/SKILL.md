---
skill: validate-unit-economics-strict
description: |
  ユニットエコノミクス厳格検証スキル（ForStartup版）。

  **VC投資基準に準拠した厳格な検証**：
  - LTV/CAC 5.0以上（業界平均3.0の1.7倍）
  - CAC回収期間 12ヶ月以内（業界平均18ヶ月より6ヶ月短縮）
  - Gross Margin 70%以上（SaaS業界標準）
  - Net Revenue Retention 100%以上（理想は120%以上）
  - Magic Number 0.75以上（効率的な成長）

  使用タイミング：
  - Series A調達準備時
  - ピッチデッキ作成前
  - VC Meeting前の最終検証

  所要時間：30-45分（自動実行）
  出力：unit_economics_strict.md
trigger_keywords:
  - "ユニットエコノミクス検証"
  - "LTV/CAC検証"
  - "unit economics"
  - "validate unit economics"
stage: planning
dependencies:
  - validate-pmf (PMF達成確認)
  - analyze-aarrr (AARRR分析完了)
  - cohort分析データ
  - 財務データ（CAC、ARPU、Churn Rate等）
output_file: documents/3_planning/unit_economics_strict.md
execution_time: 30-45分
framework_reference: |
  - a16z: Unit Economics Framework
  - SaaS Capital: SaaS Metrics
  - Bessemer Venture Partners: Cloud 100 Metrics
  - Founder_Research VC投資成功事例
priority: P0
framework_compliance: 100%
version: 1.0-ForStartup
created_at: 2026-01-03
domain: ForStartup
---

# Validate Unit Economics Strict Skill (ForStartup Edition)

ユニットエコノミクス厳格検証スキル（VC調達基準）。

---

## このSkillでできること

1. **LTV/CAC検証**: 5.0以上の基準でスケールability評価
2. **CAC回収期間検証**: 12ヶ月以内の資金効率確認
3. **Gross Margin検証**: 70%以上のSaaS標準達成確認
4. **NRR検証**: 100%以上（理想120%以上）の顧客成長確認
5. **Magic Number検証**: 0.75以上の成長効率確認
6. **セグメント別分析**: SMB/Mid-Market/Enterpriseの経済性比較
7. **ベンチマーク比較**: Shopify, Atlassian, Zoom, Slackとの比較

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 財務データ（CAC、ARPU、Churn Rate、Gross Margin等）、コホート分析データ、`pmf_validation.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/unit_economics_strict.md` |
| **次のSkill** | `/for-startup-build-pitch-deck`（ピッチデッキ作成）、`/for-startup-prepare-vc-meeting`（VC Meeting準備） |
| **ステージ** | Series A調達準備 |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

### 理論基盤
- @for_startup/knowledge_base/knowledge_base.md（ユニットエコノミクス基準）
- @for_startup/knowledge_base/case_reference_for_startup.md（成功事例）

### 評価基準・フレームワーク
- NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）

### ベンチマーク事例（成功企業）

| 企業 | LTV/CAC | CAC回収期間 | Gross Margin | NRR | 特徴 |
|------|:-------:|:----------:|:------------:|:---:|------|
| **Shopify** | 7.5 | 5ヶ月 | 55% | 120%+ | 低CAC、高リテンション |
| **Atlassian** | 9.0 | 3ヶ月 | 85% | 110%+ | プロダクト主導成長（PLG） |
| **Zoom** | 6.8 | 4ヶ月 | 81% | 125%+ | バイラル成長 |
| **Slack** | 8.2 | 6ヶ月 | 89% | 143%+ | ネットワーク効果 |
| **Snowflake** | 10.0+ | 2ヶ月 | 70% | 168%+ | 使用量ベース課金 |
| **Datadog** | 9.5 | 3ヶ月 | 78% | 130%+ | プラットフォーム効果 |

**平均**: LTV/CAC 8.5、CAC回収期間 3.8ヶ月、Gross Margin 76%、NRR 134%

**Series A基準**: LTV/CAC 5.0以上、CAC回収期間 12ヶ月以内、Gross Margin 70%以上、NRR 100%以上

---

## Domain-Specific Knowledge (from Research)

### Success Patterns（成功パターン）

#### パターン1: PLG（Product-Led Growth）による低CAC

**事例**: Atlassian, Slack, Zoom

- **戦略**: フリーミアムモデル → ボトムアップ採用 → エンタープライズアップセル
- **CAC**: $100-500（業界平均$1,000-3,000の1/3-1/10）
- **LTV/CAC**: 8.0-10.0（極めて高効率）
- **CAC回収期間**: 3-6ヶ月（業界平均18ヶ月の1/3-1/6）

**学び**:
- セルフサービスオンボーディングでCAC削減
- リファラルプログラムでバイラル成長
- プロダクト内アップセルで営業コスト最小化

#### パターン2: 使用量ベース課金（Usage-Based Pricing）

**事例**: Snowflake, Datadog, Twilio

- **戦略**: 使うほど支払う仕組み → 顧客成長と連動
- **NRR**: 120-170%（顧客の拡大が自動的に売上増加）
- **Churn Rate**: 2-5%/年（低い離脱率）
- **LTV**: 長期契約で極めて高い

**学び**:
- 顧客の成功 = 自社の成功の構造
- アップセル営業不要（使用量が自然増加）
- 初期導入ハードル低減（スモールスタート可能）

#### パターン3: ネットワーク効果による高リテンション

**事例**: Slack, Notion, Figma

- **戦略**: チーム内での利用拡大 → 切り替えコスト増大
- **NRR**: 120-150%（チーム規模拡大で自然増収）
- **Churn Rate**: 1-3%/年（極めて低い）
- **LTV/CAC**: 7.0-9.0

**学び**:
- コラボレーション機能でロックイン
- チーム全員が使うツールは切り替えが困難
- 部門間拡大（横展開）で売上増加

### Common Pitfalls（失敗パターン）

**失敗パターン1: 過大評価されたLTV**

- **問題**: Churn Rateを楽観的に見積もり、LTVを過大評価
- **教訓**: コホート分析で実際のChurn Rateを測定し、保守的に計算
- **VC視点**: LTVの根拠が薄弱だと信頼を失う

**失敗パターン2: セグメント別分析の欠如**

- **問題**: 全体平均でLTV/CAC 5.0だが、SMBはLTV/CAC 2.0、EnterpriseはLTV/CAC 10.0
- **教訓**: セグメント別に分析し、どこに注力すべきか明確化
- **VC視点**: セグメント別分析がないと戦略性を疑われる

**失敗パターン3: CAC回収期間の誤算**

- **問題**: Gross Marginを考慮せずCAC回収期間を計算
- **教訓**: CAC回収期間 = CAC ÷ (ARPU × Gross Margin × 12)で正確に計算
- **VC視点**: Gross Margin無視はキャッシュフロー理解不足と判断される

**失敗パターン4: NRR 100%未満**

- **問題**: Churn RateがExpansion Revenueを上回り、NRR 100%未満
- **教訓**: NRR 100%未満は顧客基盤が縮小中 → Series A調達困難
- **VC視点**: NRR 100%未満は投資見送りの重大理由

### Quantitative Benchmarks（定量的ベンチマーク）

#### VC投資基準（Series A）

| 指標 | 最低基準 | 理想基準 | 優秀企業平均 | 出典 |
|------|---------|---------|------------|------|
| **LTV/CAC** | 5.0以上 | 7.0以上 | 8.5 | a16z SaaS Metrics |
| **CAC回収期間** | 12ヶ月以内 | 6ヶ月以内 | 3.8ヶ月 | SaaS Capital Survey |
| **Gross Margin** | 70%以上 | 80%以上 | 76% | Bessemer Cloud 100 |
| **NRR** | 100%以上 | 120%以上 | 134% | a16z SaaS Metrics |
| **Magic Number** | 0.75以上 | 1.0以上 | 1.2 | SaaS Capital |
| **Churn Rate** | 5%/年以下 | 2%/年以下 | 3%/年 | SaaS Capital |

#### セグメント別ベンチマーク

| セグメント | ARPU | CAC | LTV/CAC | CAC回収期間 | Churn Rate |
|-----------|------|-----|:-------:|:----------:|:----------:|
| **SMB** | $100-500/月 | $500-1,000 | 3.0-4.0 | 12-18ヶ月 | 10-15%/年 |
| **Mid-Market** | $1,000-5,000/月 | $3,000-10,000 | 5.0-7.0 | 8-12ヶ月 | 5-8%/年 |
| **Enterprise** | $10,000+/月 | $30,000-100,000 | 8.0-12.0 | 6-10ヶ月 | 2-5%/年 |

**学び**: Mid-Market以上に注力するとLTV/CAC、CAC回収期間、Churn Rateが改善

### Best Practices

1. **保守的なLTV計算**: Churn Rateは実績ベース、将来改善を見込まない
2. **セグメント別分析**: SMB/Mid-Market/Enterpriseで経済性を分離評価
3. **Gross Margin考慮**: CAC回収期間計算時にGross Marginを必ず適用
4. **NRR 120%目標**: Expansion Revenueでネット成長を実現
5. **Magic Number 0.75以上**: 効率的な成長を証明（Sales & Marketing費用対効果）

### Reference

- 詳細: @for_startup/knowledge_base/knowledge_base.md#ユニットエコノミクス基準
- VC投資成功事例: @for_startup/knowledge_base/case_reference_for_startup.md

---

## 実行ステップ

### STEP 1: データ収集（5分）

**必須データ**:

| データ項目 | 説明 | 取得元 |
|----------|------|--------|
| **CAC** | 顧客獲得コスト | Sales & Marketing費用 ÷ 新規顧客数 |
| **ARPU** | 顧客あたり月次平均収益 | MRR ÷ 顧客数 |
| **Churn Rate** | 月次解約率 | 解約顧客数 ÷ 全顧客数 |
| **Gross Margin** | 粗利率 | (Revenue - COGS) / Revenue |
| **NRR** | Net Revenue Retention | (期末MRR - Churn + Expansion) / 期初MRR |
| **Sales & Marketing費用** | 営業・マーケ費用 | 財務データ |
| **コホート分析** | 月別顧客リテンション | 顧客データベース |

**データ検証**:
- Churn Rateは実績ベース（最低6ヶ月分）
- ARPUはセグメント別に分離
- Gross MarginはCOGSを正確に計上

### STEP 2: LTV計算（5分）

**計算式**:
```
LTV = ARPU × Gross Margin ÷ Churn Rate
```

**例**:
- ARPU: $1,000/月
- Gross Margin: 75%
- Churn Rate: 2%/月

```
LTV = $1,000 × 0.75 ÷ 0.02 = $37,500
```

**セグメント別LTV**:

| セグメント | ARPU | Gross Margin | Churn Rate | LTV |
|-----------|------|:------------:|:----------:|----:|
| SMB | $200 | 70% | 5%/月 | $2,800 |
| Mid-Market | $2,000 | 75% | 2%/月 | $75,000 |
| Enterprise | $15,000 | 80% | 1%/月 | $1,200,000 |

### STEP 3: CAC計算（5分）

**計算式**:
```
CAC = (Sales費用 + Marketing費用) ÷ 新規顧客数
```

**例**:
- Sales費用: $100,000/月
- Marketing費用: $50,000/月
- 新規顧客数: 50/月

```
CAC = ($100,000 + $50,000) ÷ 50 = $3,000
```

**セグメント別CAC**:

| セグメント | Sales費用 | Marketing費用 | 新規顧客数 | CAC |
|-----------|---------|-------------|----------|----:|
| SMB | $20,000 | $30,000 | 100 | $500 |
| Mid-Market | $60,000 | $15,000 | 25 | $3,000 |
| Enterprise | $20,000 | $5,000 | 2 | $12,500 |

### STEP 4: LTV/CAC計算（2分）

**計算式**:
```
LTV/CAC = LTV ÷ CAC
```

**全体平均**:
```
LTV/CAC = $37,500 ÷ $3,000 = 12.5
```

**セグメント別LTV/CAC**:

| セグメント | LTV | CAC | LTV/CAC | 判定 |
|-----------|----:|----:|:-------:|:----:|
| SMB | $2,800 | $500 | 5.6 | ✅ 合格 |
| Mid-Market | $75,000 | $3,000 | 25.0 | 🏆 優秀 |
| Enterprise | $1,200,000 | $12,500 | 96.0 | 🏆 優秀 |

### STEP 5: CAC回収期間計算（5分）

**計算式**:
```
CAC回収期間（月） = CAC ÷ (ARPU × Gross Margin)
```

**例**:
- CAC: $3,000
- ARPU: $1,000/月
- Gross Margin: 75%

```
CAC回収期間 = $3,000 ÷ ($1,000 × 0.75) = 4ヶ月
```

**セグメント別CAC回収期間**:

| セグメント | CAC | ARPU | Gross Margin | CAC回収期間 | 判定 |
|-----------|----:|-----:|:------------:|:----------:|:----:|
| SMB | $500 | $200 | 70% | 3.6ヶ月 | 🏆 優秀 |
| Mid-Market | $3,000 | $2,000 | 75% | 2.0ヶ月 | 🏆 優秀 |
| Enterprise | $12,500 | $15,000 | 80% | 1.0ヶ月 | 🏆 優秀 |

### STEP 6: NRR計算（5分）

**計算式**:
```
NRR = (期末MRR - Churned MRR + Expansion MRR) ÷ 期初MRR × 100%
```

**例**:
- 期初MRR: $100,000
- Churned MRR: $5,000（5%離脱）
- Expansion MRR: $25,000（アップセル・クロスセル）
- 期末MRR: $120,000

```
NRR = ($120,000 - $5,000 + $25,000) ÷ $100,000 × 100% = 140%
```

**NRR判定基準**:

| NRR範囲 | 判定 | VC評価 |
|:-------:|:----:|--------|
| **120%以上** | 🏆 優秀 | Series A確実 |
| **100-119%** | ✅ 合格 | Series A可能性高い |
| **90-99%** | ⚠️ 要改善 | Expansion強化必要 |
| **90%未満** | ❌ 不合格 | 顧客基盤縮小中 |

### STEP 7: Magic Number計算（5分）

**計算式**:
```
Magic Number = Net New ARR ÷ Sales & Marketing費用（前四半期）
```

**例**:
- Net New ARR（今四半期）: $300,000
- Sales & Marketing費用（前四半期）: $250,000

```
Magic Number = $300,000 ÷ $250,000 = 1.2
```

**Magic Number判定基準**:

| Magic Number | 判定 | 意味 |
|:------------:|:----:|------|
| **1.0以上** | 🏆 優秀 | $1の投資で$1以上のARR創出 |
| **0.75-0.99** | ✅ 合格 | 効率的な成長 |
| **0.5-0.74** | ⚠️ 要改善 | 成長効率が低い |
| **0.5未満** | ❌ 不合格 | 投資効率が悪い |

### STEP 8: ベンチマーク比較（5分）

**ベンチマーク企業との比較**:

| 指標 | 自社 | Shopify | Atlassian | Zoom | Slack | 平均 | 判定 |
|------|:----:|:-------:|:---------:|:----:|:-----:|:----:|:----:|
| **LTV/CAC** | 12.5 | 7.5 | 9.0 | 6.8 | 8.2 | 8.5 | 🏆 |
| **CAC回収期間** | 4ヶ月 | 5ヶ月 | 3ヶ月 | 4ヶ月 | 6ヶ月 | 3.8ヶ月 | ✅ |
| **Gross Margin** | 75% | 55% | 85% | 81% | 89% | 76% | ✅ |
| **NRR** | 140% | 120% | 110% | 125% | 143% | 134% | 🏆 |
| **Magic Number** | 1.2 | 1.1 | 1.3 | 1.0 | 1.4 | 1.2 | ✅ |

### STEP 9: 総合評価（5分）

**総合スコア（100点満点）**:

| 評価項目 | 配点 | スコア | 評価基準 |
|---------|:----:|:-----:|---------|
| **LTV/CAC** | 30点 | [X]点 | 5.0+ (15点)、7.0+ (25点)、10.0+ (30点) |
| **CAC回収期間** | 25点 | [X]点 | 12ヶ月以内 (15点)、6ヶ月以内 (25点) |
| **Gross Margin** | 15点 | [X]点 | 70%+ (10点)、80%+ (15点) |
| **NRR** | 20点 | [X]点 | 100%+ (10点)、120%+ (20点) |
| **Magic Number** | 10点 | [X]点 | 0.75+ (5点)、1.0+ (10点) |

**総合判定**:

| スコア範囲 | 判定 | VC評価 | 次のアクション |
|:----------:|:----:|--------|---------------|
| **90-100点** | 🏆 優秀 | Series A確実 | ピッチデッキ作成、VC Meeting設定 |
| **70-89点** | ✅ 合格 | Series A可能性高い | 弱点項目を強化後に調達開始 |
| **50-69点** | ⚠️ 要改善 | 条件付き投資 | 3-6ヶ月改善後に再評価 |
| **50点未満** | ❌ 不合格 | 投資見送り | PMF再検証、Pivotまたは | 顧客セグメント変更 |

### STEP 10: 改善提案（5分）

**弱点項目への改善提案**:

#### LTV/CAC < 5.0の場合

**改善策**:
1. **CAC削減**: PLG導入、リファラルプログラム、コンテンツマーケティング
2. **LTV向上**: Churn Rate削減、アップセル強化、価格引き上げ
3. **セグメント最適化**: LTV/CAC高いセグメントに注力

#### CAC回収期間 > 12ヶ月の場合

**改善策**:
1. **ARPU向上**: 年次契約への誘導、上位プラン提案
2. **Gross Margin改善**: COGS削減、インフラコスト最適化
3. **CAC削減**: セルフサービスオンボーディング、営業効率化

#### NRR < 100%の場合

**改善策**:
1. **Churn Rate削減**: カスタマーサクセス強化、プロダクト改善
2. **Expansion Revenue増加**: アップセル施策、クロスセル提案
3. **顧客セグメント変更**: リテンション高いセグメントに注力

### STEP 11: 成果物出力

**出力先**: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/unit_economics_strict.md`

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## 使用例

```
User: /validate-unit-economics-strict

Skill:
# ユニットエコノミクス厳格検証 自律実行開始（ForStartup版）

データ収集中...
- CAC: $3,000 ✅
- ARPU: $1,000/月 ✅
- Churn Rate: 2%/月 ✅
- Gross Margin: 75% ✅
- NRR: 140% ✅
- コホート分析データ ✅

[自動計算中...]
- STEP 1: データ収集 ✅
- STEP 2: LTV計算 → $37,500 ✅
- STEP 3: CAC計算 → $3,000 ✅
- STEP 4: LTV/CAC計算 → 12.5 🏆
- STEP 5: CAC回収期間計算 → 4ヶ月 ✅
- STEP 6: NRR計算 → 140% 🏆
- STEP 7: Magic Number計算 → 1.2 ✅
- STEP 8: ベンチマーク比較 ✅
- STEP 9: 総合評価 ✅
- STEP 10: 改善提案 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: unit_economics_strict.md
総合スコア: **95/100点** 🏆 優秀

**主要指標**:
| 指標 | 値 | 判定 |
|------|:--:|:----:|
| LTV/CAC | 12.5 | 🏆 優秀（基準5.0の2.5倍） |
| CAC回収期間 | 4ヶ月 | ✅ 合格（基準12ヶ月の1/3） |
| Gross Margin | 75% | ✅ 合格（基準70%超過） |
| NRR | 140% | 🏆 優秀（基準120%超過） |
| Magic Number | 1.2 | ✅ 合格（基準1.0超過） |

**VC評価**: Series A確実、ピッチデッキ作成準備完了

**推奨次のステップ**:
- `/for-startup-build-pitch-deck` でピッチデッキ作成
- `/for-startup-prepare-vc-meeting` でVC Meeting準備
```

---

## 注意事項

1. **保守的なLTV計算**: Churn Rateは実績ベース、楽観的見積もりは避ける
2. **セグメント別分析必須**: 全体平均だけでなく、SMB/Mid-Market/Enterpriseで分離評価
3. **Gross Margin考慮**: CAC回収期間計算時にGross Marginを必ず適用
4. **NRR 100%以上必須**: NRR 100%未満はSeries A調達困難
5. **ベンチマーク比較**: Shopify, Atlassian, Zoom, Slackと比較し、優位性を確認

---

## 更新履歴

- 2026-01-03: ForStartup版として新規作成（VC投資基準、LTV/CAC 5.0以上、CAC回収期間12ヶ月以内）
