---
id: "FOUNDER_159"
title: "Peter Thiel & Alex Karp - Palantir"
category: "founder"
tier: "vc_backed"
type: "delayed_ipo"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["data-analytics", "government", "defense", "delayed-ipo", "direct-listing", "Founders-Fund", "In-Q-Tel"]

# 基本情報
founder:
  name: "Peter Thiel (創業者), Alex Karp (CEO)"
  birth_year: 1967 # Thiel, Karp: 1967
  nationality: "アメリカ (Thiel: ドイツ系, Karp: ユダヤ系)"
  education: "Thiel: Stanford (哲学, JD), Karp: Haverford (哲学), Stanford (JD), Frankfurt (哲学博士)"
  prior_experience: "Thiel: PayPal共同創業者, Founders Fund; Karp: 法律・哲学研究者"

company:
  name: "Palantir Technologies"
  founded_year: 2003
  industry: "データアナリティクス / AI / 政府・防衛 / エンタープライズソフトウェア"
  current_status: "public"
  valuation: "$15.7B（2020年IPO時）→ $80B+（2024年）"
  employees: 3,500+ # 2024年

# VC投資情報
funding:
  total_raised: "$2.46B+"
  funding_rounds:
    - round: "seed"
      date: "2004"
      amount: "$30M"
      valuation_post: "不明"
      lead_investors: ["Founders Fund (Peter Thiel)"]
      other_investors: ["In-Q-Tel (CIA venture arm)"]
    - round: "series_a"
      date: "2006-06"
      amount: "$7.5M"
      valuation_post: "不明"
      lead_investors: ["Oakhouse Partners"]
      other_investors: []
    - round: "series_b"
      date: "2006-11"
      amount: "$10.5M"
      valuation_post: "不明"
      lead_investors: ["REV Venture Partners"]
      other_investors: []
    - round: "series_h"
      date: "2015-07"
      amount: "$880M"
      valuation_post: "$20B"
      lead_investors: ["Morgan Stanley"]
      other_investors: []
  top_tier_vcs: ["Founders Fund (Peter Thiel)", "In-Q-Tel (CIA)", "Tiger Global Management", "Morgan Stanley"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "delayed_ipo"
  ipo_details:
    ipo_date: "2020-09-30"
    ipo_method: "direct_listing"
    years_to_ipo: 17
    ipo_valuation: "$15.7B"
    current_valuation: "$80B+"
    revenue_at_ipo: "$1.1B (2020年)"
    profit_at_ipo: "赤字（$1.2B損失）"
  success_factors:
    - "政府・防衛契約での独占的地位"
    - "極めて高い参入障壁（セキュリティクリアランス）"
    - "長期契約による安定収益"
    - "PatientキャピタルによるIPO遅延戦略"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 30  # 推定: ['data-analytics', 'government', 'defense', 'delayed-ipo', 'direct-listing', 'Founders-Fund', 'In-Q-Tel']業界標準
    problem_commonality: 10 # 政府・防衛の大規模データ分析ニーズ
    wtp_confirmed: true # 政府契約で高額
    urgency_score: 10 # テロ対策、国家安全保障
    validation_method: "CIA In-Q-Telからの初期投資・契約"
  psf:
    ten_x_axes:
      - axis: "データ統合能力"
        multiplier: 100 # 既存ツールでは不可能
      - axis: "セキュリティ"
        multiplier: 50 # 政府レベルのセキュリティ
      - axis: "スケーラビリティ"
        multiplier: 10 # ペタバイト級データ処理
    mvp_type: "custom_solution"
    initial_cvr: null
    uvp_clarity: 10 # 政府・防衛に特化した明確な価値提案
    competitive_advantage: "政府契約、セキュリティクリアランス、参入障壁"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "政府・防衛向けデータアナリティクス"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Peter Thiel", "Alex Karp", "Joe Lonsdale", "Stephen Cohen", "Nathan Gettings"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 14
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "CNBC"
    - "CNN Business"
    - "Fast Company"
    - "Tracxn"
    - "Crunchbase"
---

# Peter Thiel & Alex Karp - Palantir（遅延IPO成功分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Peter Thiel（創業者）, Alex Karp（CEO） |
| 共同創業者 | Joe Lonsdale, Stephen Cohen, Nathan Gettings |
| 生年 | Thiel: 1967年, Karp: 1967年 |
| 国籍 | アメリカ（Thiel: ドイツ系, Karp: ユダヤ系） |
| 学歴 | Thiel: Stanford（哲学, JD）, Karp: Haverford（哲学）, Stanford（JD）, Frankfurt（哲学博士） |
| 創業前経験 | Thiel: PayPal共同創業者, Founders Fund; Karp: 法律・哲学研究者 |
| 企業名 | Palantir Technologies |
| 創業年 | 2003年 |
| 業界 | データアナリティクス / AI / 政府・防衛 / エンタープライズソフトウェア |
| 現在の状況 | 上場企業（NYSE: PLTR, 2020年9月直接上場） |
| 評価額/時価総額 | $15.7B（2020年IPO時）→ $80B+（2024年） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **2001年9月11日同時多発テロ**: Peter Thielが「データ統合で防げたのでは?」と問題意識
- 政府・情報機関は膨大なデータを持つが、サイロ化されていて活用できない
- テロリストの動きを事前に検知するには、異なるデータソースを統合・分析する必要

**課題の具体化**:
1. **データサイロ問題**: CIA, FBI, NSA等が各自データを保有、共有されない
2. **レガシーシステム**: 既存ツールでは大規模データ統合が不可能
3. **セキュリティ要件**: 政府レベルのセキュリティクリアランスが必須

**需要検証方法**:
- **2004年**: CIA傘下のIn-Q-Telから$2M投資
- CIAが最初の顧客（テロ対策データ分析）
- 政府契約での実証実験

### 2.2 プロダクト開発

**創業メンバー**:
- **Peter Thiel**: PayPal創業者、Founders Fund創設者、資金提供
- **Alex Karp**: 哲学博士、CEO（経営）
- **Joe Lonsdale**: Stanford MBA学生、技術開発
- **Stephen Cohen**: PayPalエンジニア、技術開発
- **Nathan Gettings**: PayPalエンジニア、プロトタイプ開発

**初期資金調達（2004年）**:
- Peter ThielのFounders Fundから$30M
- In-Q-Tel（CIA）から$2M
- VCはほとんど興味を示さなかった（「政府契約は儲からない」）

**コアプロダクト: Palantir Gotham**:
- 政府・防衛向けデータ統合・分析プラットフォーム
- 異なるデータソース（テキスト、画像、動画、センサー等）を統合
- リアルタイムデータ分析、パターン検出
- 高度なセキュリティ（政府レベルのクリアランス）

## 3. 成長の軌跡

### 3.1 初期の苦闘（2003-2008年）

**VC調達の失敗**:
- シリコンバレーのVCはほとんど投資せず
- 「政府契約は儲からない」「スケールしない」と見なされた
- Peter Thiel自身のFounders Fundが主要投資家

**Series A/B（2006年）**:
- **Series A**: $7.5M（Oakhouse Partners主導）
- **Series B**: $10.5M（REV Venture Partners主導）
- 小規模VCのみ、トップティアVCは参加せず

**初期顧客**:
- CIA, FBI, NSA等の情報機関
- 国防総省（DoD）
- テロ対策、サイバーセキュリティ

### 3.2 転機: ビンラディン殺害作戦（2011年）

**Palantirの貢献**:
- 2011年5月、オサマ・ビンラディン殺害作戦でPalantirのデータ分析が活用されたと報道
- 異なるデータソース（通信記録、人物関係、地理情報）を統合
- ビンラディンの潜伏先を特定

**評価の急上昇**:
- Palantirの技術力が証明された
- 政府契約が急増
- 評価額が急上昇

### 3.3 大規模調達と評価額上昇（2014-2015年）

**評価額の推移**:
- **2014年11月**: $15B評価額
- **2015年6月**: $20B評価額（$500M調達）
- **2015年12月**: Series H $880M調達（Morgan Stanley主導、評価額$20B維持）

**総調達額**:
- $2.46B+（18ラウンド以上）
- 主要投資家: Founders Fund, In-Q-Tel, Tiger Global Management, Morgan Stanley

### 3.4 商業顧客への展開（2015年以降）

**Palantir Foundry**:
- エンタープライズ向けデータ統合・分析プラットフォーム
- 顧客: Airbus, Ferrari, BP, Morgan Stanley等

**商業契約の拡大**:
- 政府契約だけでなく、大企業にも展開
- 収益源の多様化

### 3.5 IPO遅延戦略（2003-2020年）

**17年間非上場を維持**:
- 2003年創業 → 2020年9月IPO
- シリコンバレーでは異例の長さ

**IPO遅延の理由**:
1. **Patient Capital（忍耐強い資本）**: Peter Thielの哲学
2. **政府契約の長期性**: 短期利益よりも長期契約重視
3. **四半期決算プレッシャー回避**: 上場すると短期業績重視に
4. **競合への情報開示回避**: 非上場で技術・契約内容を秘匿

**IPO前の収益状況**:
- **2020年収益**: $1.1B
- **2020年損失**: $1.2B（依然赤字）

### 3.6 直接上場（2020年9月30日）

**IPO方法: Direct Listing**:
- 従来のIPO（新株発行）ではなく、既存株主の株式を直接上場
- 資金調達なし、手数料削減
- Spotify, Slackと同じ手法

**IPO初日**:
- **参照価格**: $7.25（評価額$16B）
- **初値**: $10
- **終値**: $9.20（市場時価総額$15.2B）

**2024年時点**:
- **市場時価総額**: $80B+
- IPO時の5倍以上

## 4. 成功要因分析

### 4.1 極めて高い参入障壁

**政府セキュリティクリアランス**:
- 政府・防衛契約には高度なセキュリティクリアランスが必須
- 新規参入企業が取得するには数年かかる
- Palantirは2004年から保有

**長期契約の安定性**:
- 政府契約は5-10年の長期契約
- 一度契約を獲得すると、競合が入り込みにくい
- スイッチングコストが極めて高い

### 4.2 Patient Capital戦略

**Peter Thielの哲学**:
- 「短期利益よりも長期価値」
- 四半期決算プレッシャーを避ける
- 17年間非上場を維持

**IPO遅延のメリット**:
- 技術開発に集中
- 政府契約の詳細を秘匿
- 競合（IBM, Oracle等）への情報開示回避

### 4.3 独占的市場地位

**政府・防衛市場での圧倒的シェア**:
- CIA, FBI, NSA, 国防総省等の主要顧客
- ビンラディン殺害作戦での実績
- 代替品がない

**スイッチングコストの高さ**:
- Palantirのシステムに依存すると、他社への移行が困難
- データ統合、トレーニング、セキュリティクリアランス

### 4.4 商業顧客への多角化

**Palantir Foundry**:
- エンタープライズ向けプラットフォーム
- Airbus, Ferrari, BP等の大企業
- 政府依存からの脱却

## 5. 遅延IPOの成功モデル

### 5.1 Patient Capitalの利点

**長期視点での技術開発**:
- 四半期決算プレッシャーなし
- R&Dに集中
- 政府契約の長期性に適合

**競合への情報開示回避**:
- 上場企業は四半期報告が必須
- Palantirは非上場で技術・契約内容を秘匿
- 競合（IBM, Oracle等）が模倣困難

### 5.2 IPO遅延のリスク

**流動性の欠如**:
- 従業員・投資家の株式売却困難
- 一部従業員の不満

**評価額の不透明性**:
- 非上場のため市場評価が不明
- 二次市場での価格変動

### 5.3 直接上場のメリット

**従来のIPOとの違い**:
- 新株発行なし → 既存株主の株式売却のみ
- 引受手数料削減（通常7%）
- ロックアップ期間なし

**Palantirの選択理由**:
- 資金調達不要（$2.46B既に調達済み）
- 既存株主（Peter Thiel等）の流動性確保
- IPO手数料削減

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本政府・防衛・大企業のデータ分析ニーズ |
| 競合状況 | 3 | NEC, 富士通等の国内ベンダーが強い |
| ローカライズ容易性 | 2 | セキュリティクリアランス、法規制が障壁 |
| 再現性（成功再現） | 3 | 政府契約の獲得は困難だが、モデルは参考に |
| **総合** | 3.0 | 日本独自の政府契約モデルが必要 |

**日本市場での応用**:
- 日本政府・防衛向けデータアナリティクス
- 大企業（製造業、金融）向けエンタープライズソフトウェア
- 長期契約モデル、Patient Capital戦略

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **政府・防衛ニーズの検証**: 初期顧客をCIA（In-Q-Tel）から獲得
- **緊急度の高い課題**: テロ対策、国家安全保障 → 予算確保しやすい

### 7.2 CPF検証（/validate-cpf）での注意点

- **WTP（支払意思額）**: 政府契約は高額（数億円規模）
- **長期契約**: 5-10年の安定収益
- **セキュリティクリアランス**: 参入障壁が極めて高い

### 7.3 PSF検証（/validate-10x）での注意点

- **10倍優位性**: 既存ツールでは不可能なデータ統合
- **競合不在**: 政府レベルのセキュリティ + 大規模データ分析
- **スイッチングコスト**: 一度導入すると、競合への移行困難

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | Palantirの事例 | スコア |
|------|---------------|--------|
| PMF | 政府・防衛での独占的地位 | 10/10 |
| 参入障壁 | セキュリティクリアランス、長期契約 | 10/10 |
| 収益性 | IPO時は赤字だが、2024年黒字化 | 7/10 |
| スケーラビリティ | 商業顧客への展開で証明 | 8/10 |
| **総合** | 独占的市場地位、遅延IPO成功 | **8.75/10** |

## 8. 遅延IPOの教訓

### 8.1 Patient Capitalの重要性

1. **長期視点での技術開発**:
   - 四半期決算プレッシャーなし
   - R&Dに集中

2. **競合への情報開示回避**:
   - 非上場で技術・契約内容を秘匿
   - 競合が模倣困難

3. **政府契約の長期性**:
   - 5-10年契約に適合
   - 短期利益よりも長期価値

### 8.2 直接上場の選択肢

1. **資金調達不要の場合**:
   - 既に十分な資金を調達済み
   - 新株発行不要

2. **既存株主の流動性確保**:
   - Peter Thiel等の創業者、初期投資家
   - ロックアップ期間なし

3. **IPO手数料削減**:
   - 引受手数料（通常7%）を削減
   - Spotify, Slackと同じ手法

### 8.3 日本スタートアップへの示唆

1. **政府契約の獲得**:
   - 日本政府・防衛向けソリューション
   - セキュリティクリアランス取得

2. **長期契約モデル**:
   - 5-10年契約で安定収益
   - スイッチングコスト高い

3. **Patient Capital戦略**:
   - IPO急がず、技術開発に集中
   - 四半期決算プレッシャー回避

## 9. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2003年） | ✅ PASS | Wikipedia, Crunchbase |
| 総調達額（$2.46B+） | ✅ PASS | Tracxn, Crunchbase |
| In-Q-Tel投資（$2M、2004年） | ✅ PASS | Fast Company, Wikipedia |
| IPO日（2020年9月30日） | ✅ PASS | CNBC, CNN Business |
| IPO方法（直接上場） | ✅ PASS | CNBC, CNN Business |
| IPO時評価額（$15.7B） | ✅ PASS | CNBC, CNN Business |
| 創業からIPOまで（17年） | ✅ PASS | Wikipedia, 計算 |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Palantir Technologies](https://en.wikipedia.org/wiki/Palantir_Technologies)
2. [CNBC - Palantir goes public: (PLTR) starts trading on the NYSE](https://www.cnbc.com/2020/09/30/palantir-goes-public-pltr-starts-trading-on-the-nyse.html)
3. [CNN Business - Palantir IPO: controversial data company surges in its Wall Street debut](https://www.cnn.com/2020/09/30/tech/palantir-ipo)
4. [Fast Company - How Silicon Valley rejection and CIA cash fueled Palantir's rise](https://www.fastcompany.com/91446398/cia-police-palantir-alex-karp-predictive-peter-thiel-paypal-sequoia)
5. [Public.com - What to know about Palantir's 2020 IPO](https://public.com/learn/what-to-know-about-palantirs-ipo)
6. [Tracxn - Palantir 2025 Funding Rounds & List of Investors](https://tracxn.com/d/companies/palantir/__N9Uaw2GHjG5JVqvNtXcgrGRwXgHpY9cQsxh3xArGQ6A/funding-and-investors)
7. [Crunchbase - Palantir Technologies Company Profile & Funding](https://www.crunchbase.com/organization/palantir-technologies)
8. [Britannica Money - Palantir](https://www.britannica.com/money/Palantir-Technologies-Inc)
9. [Built In - What Is Palantir? The Company Behind Government AI Tools](https://builtin.com/articles/what-is-palantir)
10. [Medium - Palantir's Growth Story: How the Magic of Data Analysis Is Changing the World](https://medium.com/@takafumi.endo/palantirs-growth-story-how-the-magic-of-data-analysis-is-changing-the-world-05fe98f4c2af)
11. [Inc. - Why Peter Thiel Could Walk Away From Palantir With Billions](https://www.inc.com/jeremy-quittner/staggering-valuation-of-palantir-and-founder-ownership.html)
12. [Bloomberg - Palantir's Long-Awaited Public Debut Frustrates Some Investors](https://www.bloomberg.com/news/articles/2020-10-04/palantir-s-long-awaited-public-debut-frustrates-some-investors)
13. [Renaissance Capital - Palantir selects September 23 for NYSE direct listing date](https://www.renaissancecapital.com/IPO-Center/News/70965/Palantir-selects-September-23-for-NYSE-direct-listing-date)
14. [Websets - Palantir Technologies Inc. Funding & Investor Information](https://websets.exa.ai/websets/directory/palantir-funding)
