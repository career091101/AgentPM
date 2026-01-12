# Corporate Product Research Quality Scoring Criteria

**Version**: 1.0
**Last Updated**: 2025-12-30
**Total Points**: 100点満点

---

## Overview

本スコアリングシステムは、Corporate Product Researchの品質を定量的に評価し、継続的な改善を促進するために設計されています。Founder Researchの品質基準を基に、企業製品リサーチ特有の要件を反映しています。

---

## Scoring Categories (6カテゴリ)

### Category 1: YAML Frontmatter完全性（20点）

#### 1.1 必須フィールド記載（10点）
- **40フィールド必須**: 1フィールド欠損ごとに-0.25点
- 推定値（"~"接頭辞付き）は記載とみなす
- null/空白は欠損扱い

**採点式**: `10 - (欠損数 × 0.25)`

**必須40フィールドリスト**:
```yaml
# Basic Info (8)
company_name, product_name, product_url, tagline, description, category, subcategory, founded_date

# Business Model (10)
business_model, revenue_model, pricing_model, unit_economics_cac, unit_economics_ltv, unit_economics_cac_ltv_ratio, revenue_streams, primary_customer_segment, geographic_focus, market_position

# Market & Traction (12)
funding_stage, total_funding, latest_valuation, employee_count, mrr_arr, growth_rate_mom, growth_rate_yoy, user_count, paying_customer_count, retention_rate, churn_rate, nps_score

# CPF/PMF Validation (10)
user_research_count, market_need_percentage, wtp_confirmed, competitive_advantage_axes, problem_solution_fit_score, market_pull_evidence, repeat_usage_rate, referral_rate, market_share_percentage, strategic_moats
```

#### 1.2 オプションフィールド記載（5点）
- **15フィールド**: 記載率に応じて配点
- 記載率 = (記載フィールド数 / 15) × 100%

**採点式**: `5 × (記載率 / 100)`

**オプション15フィールドリスト**:
```yaml
key_investors, key_partners, exit_events, acquisition_offers, international_expansion, regulatory_approvals, patents_filed, awards_recognition, media_mentions, leadership_team, board_members, advisory_board, technology_stack, data_sources, last_updated
```

#### 1.3 データ品質（5点）
- 推定値比率に基づく評価
- 推定値比率 = (推定値フィールド数 / 記載フィールド数) × 100%

**採点基準**:
- 推定値 < 30%: 5点（高品質）
- 推定値 30-50%: 3点（標準品質）
- 推定値 > 50%: 0点（要改善）

---

### Category 2: CPF/PMF検証データ（25点）

#### 2.1 user_research_count記載（5点）
- **数値あり**: 5点（例: `user_research_count: 45`）
- **推定値**: 3点（例: `user_research_count: ~30`）
- **ゼロ**: 1点（例: `user_research_count: 0`）
- **null/欠損**: 0点

#### 2.2 market_need_percentage記載（5点）
- **統計データ**: 5点（例: `market_need_percentage: 78%`）
- **推定値**: 3点（例: `market_need_percentage: ~60%`）
- **null/欠損**: 0点

#### 2.3 wtp_confirmed記載（5点）
- **true/false明記**: 5点
- **null/欠損**: 0点

#### 2.4 competitive_advantage_axes（10点）
- **3軸以上**: 10点
- **2軸**: 7点
- **1軸**: 3点
- **0軸/null**: 0点

**例**:
```yaml
competitive_advantage_axes:
  - "AI-powered personalization engine"
  - "Enterprise-grade security compliance"
  - "Proprietary dataset of 10M+ records"
```

---

### Category 3: ビジネス分析深度（20点）

#### 3.1 Unit Economics分析（5点）
- **詳細分析**: 5点（CAC, LTV, Ratio, Payback Period, Cohort分析を含む）
- **基本分析**: 3点（CAC, LTV, Ratioのみ）
- **なし**: 0点

**詳細分析の例**:
```
CAC: $450
LTV: $2,700
CAC:LTV Ratio: 1:6
Payback Period: 8 months
Cohort Retention (12M): 85%
```

#### 3.2 TAM/SAM/SOM算出（5点）
- **3つすべて算出**: 5点
- **2つ**: 3点
- **1つ以下**: 0点

**算出根拠の明記が必須**

#### 3.3 収益モデル分析（5点）
- **詳細分析**: 5点（複数収益源、成長戦略、Unit Economics連携）
- **基本分析**: 3点（主要収益源のみ）
- **なし**: 0点

#### 3.4 競合分析（5点）
- **3社以上比較**: 5点（比較表、差別化ポイント明記）
- **1-2社**: 3点
- **なし**: 0点

**比較項目例**: 機能、価格、市場シェア、強み/弱み、差別化要因

---

### Category 4: リクルート資産分析（10点）

#### 4.1 活用資産の特定（5点）
- **3つ以上**: 5点
- **1-2つ**: 3点
- **なし**: 0点

**資産例**: 求人DB、企業ネットワーク、マッチングアルゴリズム、ブランド力、顧客基盤

#### 4.2 シナジー効果の定量化（5点）
- **定量化あり**: 5点（数値、KPI改善率、ROI等）
- **定性のみ**: 2点（方向性のみ）
- **なし**: 0点

**定量化の例**:
```
リクルートDB活用により:
- 候補者マッチング精度: 35% → 67% (+32pt)
- 採用コスト削減: $1,200 → $680 (43%削減)
- Time-to-hire短縮: 45日 → 22日 (51%短縮)
```

---

### Category 5: ソースの質と量（15点）

#### 5.1 ソース総数（5点）
- **15ソース以上**: 5点
- **10-14ソース**: 4点
- **7-9ソース**: 2点
- **7ソース未満**: 0点

#### 5.2 Tier分布（5点）
- Tier 1+2の比率に基づく評価
- 比率 = (Tier1数 + Tier2数) / 総ソース数 × 100%

**採点基準**:
- **50%以上**: 5点
- **30-49%**: 3点
- **30%未満**: 1点

**Tier定義**:
- **Tier 1**: 公式サイト、IR資料、プレスリリース、公式ブログ
- **Tier 2**: 信頼性の高いメディア（TechCrunch, Forbes等）、業界レポート
- **Tier 3**: 一般ニュース、SNS、ブログ

#### 5.3 ファクトチェックPASS率（5点）
- PASS率 = (PASSソース数 / 総ソース数) × 100%

**採点基準**:
- **90%以上**: 5点
- **80-89%**: 3点
- **80%未満**: 0点

---

### Category 6: 文書の完全性（10点）

#### 6.1 全セクション記載（5点）
- **13セクション必須**:
  1. Executive Summary
  2. Product Overview
  3. Business Model Analysis
  4. Market Analysis
  5. CPF/PMF Validation
  6. Competitive Landscape
  7. Recruit Asset Integration
  8. Growth Strategy
  9. Risk Assessment
  10. Financial Analysis
  11. Technology & Innovation
  12. Team & Leadership
  13. Conclusion & Recommendations

**採点基準**:
- **13/13セクション**: 5点
- **10-12セクション**: 3点
- **10セクション未満**: 0点

#### 6.2 文書長（3点）
- **400行以上**: 3点
- **200-399行**: 2点
- **200行未満**: 0点

#### 6.3 可読性（2点）
- **構造明確・誤字脱字なし**: 2点
- **一部不明瞭**: 1点
- **問題あり**: 0点

**評価基準**:
- 見出し階層の適切性
- 箇条書き・表の活用
- 誤字脱字の有無
- データの可読性

---

## Quality Tier定義

### Tier S (90-100点)
**Excellence Level** - Founder Research同等の品質

**基準**:
- すべてのカテゴリで80%以上の得点
- YAML必須フィールド: 40/40記載
- CPF/PMF検証データ: 完全記載
- ソース総数: 15以上、Tier1+2比率60%以上
- ファクトチェックPASS率: 95%以上
- 文書長: 500行以上

**使用ケース**: ベストプラクティスとして社内共有、新規リサーチのテンプレート化

---

### Tier A (80-89点)
**High Quality** - 高品質、一部カテゴリで改善余地あり

**基準**:
- 4カテゴリ以上で80%以上の得点
- YAML必須フィールド: 38/40以上記載
- CPF/PMF検証データ: 主要項目記載
- ソース総数: 12以上、Tier1+2比率50%以上
- ファクトチェックPASS率: 90%以上
- 文書長: 400行以上

**使用ケース**: そのまま意思決定に使用可能、軽微な改善を推奨

---

### Tier B (70-79点)
**Acceptable** - 合格レベル、基本要件を満たす

**基準**:
- 3カテゴリ以上で70%以上の得点
- YAML必須フィールド: 35/40以上記載
- CPF/PMF検証データ: 一部記載
- ソース総数: 10以上、Tier1+2比率40%以上
- ファクトチェックPASS率: 85%以上
- 文書長: 300行以上

**使用ケース**: 基本的な意思決定に使用可能、追加調査を推奨

---

### Tier C (60-69点)
**Needs Improvement** - 要改善、複数カテゴリで課題あり

**基準**:
- 2カテゴリ以上で60%以上の得点
- YAML必須フィールド: 30/40以上記載
- CPF/PMF検証データ: 不完全
- ソース総数: 7以上
- ファクトチェックPASS率: 80%以上
- 文書長: 200行以上

**使用ケース**: 参考情報として使用、大幅な追加調査が必要

---

### Tier D (0-59点)
**Unacceptable** - 不合格、大幅な再調査が必要

**基準**:
- 複数カテゴリで60%未満の得点
- YAML必須フィールド: 30/40未満
- CPF/PMFデータ: 大部分欠損
- ソース総数: 7未満
- ファクトチェックPASS率: 80%未満

**使用ケース**: 再調査必須、現状では使用不可

---

## 最低閾値設定

**すべての製品が満たすべき最低基準**:

| 項目 | 最低基準 | 理由 |
|-----|---------|------|
| YAML必須フィールド | 40/40記載（推定値可） | 基本情報の完全性 |
| ソース総数 | 10ソース以上 | 情報の信頼性担保 |
| Tier 1ソース | 3ソース以上 | 公式情報の裏付け |
| competitive_advantage_axes | 2軸以上 | 差別化の明確化 |
| ファクトチェックPASS率 | 80%以上 | 情報精度の保証 |
| 文書長 | 300行以上 | 分析深度の担保 |
| 全セクション記載 | 10/13以上 | 構造の完全性 |

**閾値未達の場合**: Tier D判定、即座に再調査実施

---

## 自動採点ルール

### Category 1: YAML Frontmatter
```python
# 必須フィールド採点
required_fields = 40
missing_count = count_missing_required_fields(yaml_data)
score_1_1 = max(0, 10 - (missing_count * 0.25))

# オプションフィールド採点
optional_fields = 15
optional_filled = count_filled_optional_fields(yaml_data)
score_1_2 = 5 * (optional_filled / optional_fields)

# データ品質採点
total_filled = count_all_filled_fields(yaml_data)
estimated_count = count_estimated_fields(yaml_data)
estimated_ratio = (estimated_count / total_filled) * 100

if estimated_ratio < 30:
    score_1_3 = 5
elif estimated_ratio <= 50:
    score_1_3 = 3
else:
    score_1_3 = 0

category_1_score = score_1_1 + score_1_2 + score_1_3
```

### Category 2: CPF/PMF検証データ
```python
# user_research_count
if is_numeric(user_research_count) and not is_estimated(user_research_count):
    score_2_1 = 5
elif is_estimated(user_research_count):
    score_2_1 = 3
elif user_research_count == 0:
    score_2_1 = 1
else:
    score_2_1 = 0

# market_need_percentage
if is_numeric(market_need_percentage) and not is_estimated(market_need_percentage):
    score_2_2 = 5
elif is_estimated(market_need_percentage):
    score_2_2 = 3
else:
    score_2_2 = 0

# wtp_confirmed
if wtp_confirmed in [true, false]:
    score_2_3 = 5
else:
    score_2_3 = 0

# competitive_advantage_axes
axes_count = len(competitive_advantage_axes)
if axes_count >= 3:
    score_2_4 = 10
elif axes_count == 2:
    score_2_4 = 7
elif axes_count == 1:
    score_2_4 = 3
else:
    score_2_4 = 0

category_2_score = score_2_1 + score_2_2 + score_2_3 + score_2_4
```

### Category 3: ビジネス分析深度
```python
# Unit Economics分析
ue_keywords = ["CAC", "LTV", "Ratio", "Payback", "Cohort"]
ue_found = count_keywords_in_section(ue_keywords, "unit_economics_section")
if ue_found >= 4:
    score_3_1 = 5
elif ue_found >= 2:
    score_3_1 = 3
else:
    score_3_1 = 0

# TAM/SAM/SOM
market_metrics = count_metrics(["TAM", "SAM", "SOM"])
if market_metrics == 3:
    score_3_2 = 5
elif market_metrics == 2:
    score_3_2 = 3
else:
    score_3_2 = 0

# 収益モデル分析
revenue_section_lines = count_lines("revenue_model_section")
has_multiple_streams = check_multiple_revenue_streams()
if revenue_section_lines > 30 and has_multiple_streams:
    score_3_3 = 5
elif revenue_section_lines > 10:
    score_3_3 = 3
else:
    score_3_3 = 0

# 競合分析
competitor_count = count_competitors_analyzed()
if competitor_count >= 3:
    score_3_4 = 5
elif competitor_count >= 1:
    score_3_4 = 3
else:
    score_3_4 = 0

category_3_score = score_3_1 + score_3_2 + score_3_3 + score_3_4
```

### Category 5: ソースの質と量
```python
# ソース総数
source_count = len(sources)
if source_count >= 15:
    score_5_1 = 5
elif source_count >= 10:
    score_5_1 = 4
elif source_count >= 7:
    score_5_1 = 2
else:
    score_5_1 = 0

# Tier分布
tier1_count = count_sources_by_tier(sources, tier=1)
tier2_count = count_sources_by_tier(sources, tier=2)
tier_ratio = ((tier1_count + tier2_count) / source_count) * 100

if tier_ratio >= 50:
    score_5_2 = 5
elif tier_ratio >= 30:
    score_5_2 = 3
else:
    score_5_2 = 1

# ファクトチェックPASS率
pass_count = count_fact_check_pass(sources)
pass_rate = (pass_count / source_count) * 100

if pass_rate >= 90:
    score_5_3 = 5
elif pass_rate >= 80:
    score_5_3 = 3
else:
    score_5_3 = 0

category_5_score = score_5_1 + score_5_2 + score_5_3
```

---

## 採点例

### Example 1: Tier S (95点)

**製品**: AI-Powered Enterprise Analytics Platform

**スコア内訳**:
- Category 1 (YAML): 20/20点
  - 必須フィールド: 40/40記載（10点）
  - オプションフィールド: 14/15記載（4.7点）
  - 推定値比率: 15%（5点）

- Category 2 (CPF/PMF): 25/25点
  - user_research_count: 127（5点）
  - market_need_percentage: 82%（5点）
  - wtp_confirmed: true（5点）
  - competitive_advantage_axes: 4軸（10点）

- Category 3 (ビジネス分析): 19/20点
  - Unit Economics: 詳細分析（5点）
  - TAM/SAM/SOM: 3つ算出（5点）
  - 収益モデル: 詳細分析（5点）
  - 競合分析: 2社比較（4点）

- Category 4 (リクルート資産): 10/10点
  - 活用資産: 5つ特定（5点）
  - シナジー定量化: 詳細ROI算出（5点）

- Category 5 (ソース): 14/15点
  - ソース総数: 18ソース（5点）
  - Tier分布: 67% Tier1+2（5点）
  - PASS率: 94%（4点）

- Category 6 (文書): 7/10点
  - 全セクション: 13/13（5点）
  - 文書長: 520行（3点）
  - 可読性: 優良（2点）

**総合評価**: Tier S（95点）- ベストプラクティス

---

### Example 2: Tier A (84点)

**製品**: SaaS Project Management Tool

**スコア内訳**:
- Category 1: 17/20点（推定値35%でやや多い）
- Category 2: 20/25点（wtp_confirmed未記載）
- Category 3: 17/20点（競合分析が2社のみ）
- Category 4: 7/10点（シナジー定性のみ）
- Category 5: 13/15点（PASS率87%）
- Category 6: 10/10点（完全）

**総合評価**: Tier A（84点）- 高品質、wtp検証の追加推奨

---

### Example 3: Tier B (73点)

**製品**: Mobile Fitness App

**スコア内訳**:
- Category 1: 14/20点（必須2フィールド欠損、推定値45%）
- Category 2: 17/25点（axes 2軸のみ）
- Category 3: 13/20点（TAM/SAMのみ算出）
- Category 4: 5/10点（資産2つ、定性のみ）
- Category 5: 12/15点（ソース12、Tier分布45%）
- Category 6: 7/10点（セクション11/13、350行）

**総合評価**: Tier B（73点）- 合格レベル、深掘り推奨

---

### Example 4: Tier D (52点)

**製品**: Early-Stage E-commerce Platform

**スコア内訳**:
- Category 1: 8/20点（必須8フィールド欠損、推定値60%）
- Category 2: 10/25点（多数null、axes 1軸のみ）
- Category 3: 8/20点（基本情報のみ）
- Category 4: 2/10点（資産1つ、定量化なし）
- Category 5: 6/15点（ソース6、PASS率75%）
- Category 6: 3/10点（セクション8/13、180行）

**総合評価**: Tier D（52点）- 再調査必須

---

## 改善アクションプラン

### Tier C → Tier B
1. YAML必須フィールドの完全記載（推定値でも可）
2. ソース追加（最低10ソース、Tier1を3つ以上）
3. competitive_advantage_axes 2軸以上明確化
4. 欠損セクションの補完（最低10セクション）

### Tier B → Tier A
1. 推定値の実測値化（推定値比率30%未満）
2. CPF/PMF検証データの完全記載（wtp含む）
3. 競合分析の拡充（3社以上）
4. ソースの質向上（Tier1+2比率50%以上）

### Tier A → Tier S
1. すべてのオプションフィールド記載
2. competitive_advantage_axes 3軸以上
3. Unit Economics詳細分析（Cohort含む）
4. リクルート資産シナジーの定量化
5. ファクトチェックPASS率95%以上達成

---

## 運用ガイドライン

### 採点タイミング
1. **初回リサーチ完了時**: ベースライン把握
2. **改善後**: 改善効果測定
3. **四半期レビュー**: 品質トレンド分析

### 品質管理プロセス
1. **自動採点**: スクリプトで初回スコア算出
2. **人的レビュー**: Tier C以下は必ずレビュー
3. **改善実施**: アクションプラン策定・実行
4. **再採点**: 改善後のスコア確認

### KPI設定
- **目標**: 全製品Tier B以上（70点以上）
- **stretch goal**: 50%以上がTier A以上（80点以上）
- **ベストプラクティス**: 年間5件以上のTier S達成

---

## Version History

- **v1.0 (2025-12-30)**: 初版リリース
  - Founder Research品質基準を参考に設計
  - 6カテゴリ100点満点システム確立
  - 自動採点ルール定義
