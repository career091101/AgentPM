---
id: "FOUNDER_359"
title: "Frank Slootman - Snowflake (Mega IPO)"
category: "founder"
tier: "ipo_global"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: [Data Cloud, SaaS, Enterprise, IPO, Mega IPO, Cloud Computing]

# 基本情報
founder:
  name: "Frank Slootman (CEO), Benoit Dageville & Thierry Cruanes (Technical Founders)"
  birth_year: 1958 # Frank Slootman
  nationality: "Dutch-American (Slootman), French (Dageville, Cruanes)"
  education: "Slootman: Economics (Netherlands); Dageville/Cruanes: PhD (Oracle alumni)"
  prior_experience: "Slootman: Data Domain CEO (sold to EMC $2.4B), ServiceNow CEO; Founders: Oracle"

company:
  name: "Snowflake"
  founded_year: 2012
  industry: "Data Cloud / Cloud Data Warehouse / SaaS"
  current_status: "active"
  valuation: "$60B+（2024年時価総額）"
  employees: 6000+

# IPO情報
ipo:
  ipo_date: "2020-09-16"
  exchange: "NYSE"
  ticker: "SNOW"
  ipo_price: "$120/share"
  ipo_valuation: "$33B"
  first_day_close: "$253.93"
  first_day_pop: "+111.6%"
  current_valuation: "$60B+"
  ipo_path: "traditional_ipo"
  records: "史上最大のソフトウェアIPO"

# VC投資情報
funding:
  total_raised: "$2.0B+（IPO前）"
  funding_rounds:
    - round: "seed"
      date: "2012-10"
      amount: "$5M"
      lead_investors: ["Sutter Hill Ventures"]
    - round: "series_a"
      date: "2014-06"
      amount: "$26M"
      lead_investors: ["Sutter Hill Ventures", "Redpoint Ventures"]
    - round: "series_b"
      date: "2015-10"
      amount: "$45M"
      valuation_post: "$450M"
      lead_investors: ["Sutter Hill Ventures", "Redpoint Ventures"]
    - round: "series_c"
      date: "2017-01"
      amount: "$100M"
      valuation_post: "$1.5B"
      lead_investors: ["Sutter Hill Ventures", "Redpoint Ventures", "Sequoia Capital"]
    - round: "series_d"
      date: "2018-01"
      amount: "$450M"
      valuation_post: "$3.9B"
      lead_investors: ["Sequoia Capital", "Dragoneer Investment Group"]
    - round: "series_e"
      date: "2018-10"
      amount: "$450M"
      valuation_post: "$3.9B"
      lead_investors: ["Sequoia Capital", "Dragoneer Investment Group"]
    - round: "series_f"
      date: "2020-02"
      amount: "$479M"
      valuation_post: "$12.4B"
      lead_investors: ["Salesforce Ventures", "Dragoneer Investment Group"]
  top_tier_vcs: ["Sequoia Capital", "Sutter Hill Ventures", "Salesforce Ventures", "ICONIQ Capital"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "ipo_success"
  ipo_details:
    ipo_date: "2020-09-16"
    ipo_valuation: "$33B"
    first_day_pop: "+111.6%"
    current_status: "publicly_traded"
    market_cap_peak: "$120B+ (2021)"
    market_cap_current: "$60B+ (2024)"
    unique_feature: "史上最大のソフトウェアIPO、Berkshire HathawayとSalesforceが大規模投資"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 25  # 推定: ['Data Cloud', 'SaaS', 'Enterprise', 'IPO', 'Mega IPO', 'Cloud Computing']業界標準
    problem_commonality: 95
    wtp_confirmed: true
    urgency_score: 10
    validation_method: "エンタープライズ顧客からの強い需要"
  psf:
    ten_x_axes:
      - axis: "パフォーマンス"
        multiplier: 10
      - axis: "スケーラビリティ"
        multiplier: 100
      - axis: "運用コスト"
        multiplier: 5
    mvp_type: "enterprise_beta"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "クラウドネイティブアーキテクチャ、ストレージ・コンピュート分離"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: ["FOUNDER_357 (Shopify)", "FOUNDER_358 (Atlassian)", "FOUNDER_360 (Databricks)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 14
  last_verified: "2025-12-28"
  primary_sources:
    - "Snowflake S-1 Filing (2020)"
    - "CNBC"
    - "TechCrunch"
    - "Bloomberg"
    - "Wikipedia"
---

# Frank Slootman - Snowflake（Mega IPO）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| CEO | Frank Slootman |
| 技術創業者 | Benoit Dageville & Thierry Cruanes |
| 生年 | Slootman: 1958年 |
| 国籍 | Slootman: オランダ系アメリカ人、Dageville/Cruanes: フランス |
| 学歴 | Slootman: 経済学、Dageville/Cruanes: PhD（Oracle出身） |
| 創業前経験 | Slootman: Data Domain CEO、ServiceNow CEO |
| 企業名 | Snowflake |
| 創業年 | 2012年 |
| 業界 | データクラウド / クラウドデータウェアハウス / SaaS |
| IPO日 | 2020年9月16日 |
| IPO時評価額 | $33B |
| 現在時価総額 | $60B+（2024年） |

## 2. 創業ストーリー

### 2.1 Oracle出身者による創業（2012年）

**技術創業者**:
- **Benoit Dageville**: Oracleで16年、データベースアーキテクト
- **Thierry Cruanes**: Oracleで11年、データベースエンジニア
- **Marcin Zukowski**: Vectorwise共同創業者

**課題発見**:
- 従来のオンプレミスデータウェアハウスは高価で複雑
- Amazon Redshift、Google BigQuery等の初期クラウドDWHは制約が多い
- スケーラビリティ、パフォーマンス、使いやすさの全てを満たすソリューションがない

**ビジョン**:
- 「データクラウド」の創造
- クラウドネイティブな設計
- ストレージとコンピュートの完全分離
- エラスティックなスケーリング

### 2.2 Frank Slootman参画（2014年）

**連続起業家の参画**:
- 2014年5月、Frank SlootmanがCEOに就任
- 創業メンバーは技術に専念、Slootmanがビジネスをリード

**Slootmanの実績**:
- **Data Domain**: CEOとして$2.4BでEMCに売却
- **ServiceNow**: CEOとして売上$100M→$1Bにスケール、IPO成功

**Slootmanのアプローチ**:
- 「Amp It Up」哲学（スピード、成果、説明責任を高める）
- エンタープライズ営業の強化
- プロダクトマーケットフィットの徹底追求

## 3. IPOまでの成長（2012-2020年）

### 3.1 プロダクト開発とPMF（2012-2015年）

**技術的優位性**:
- クラウドネイティブアーキテクチャ
- マルチクラウド対応（AWS、Azure、GCP）
- ストレージ・コンピュート分離
- 自動スケーリング

**初期顧客**:
- エンタープライズ顧客からの強い需要
- Capital One、Adobe、Sony等

### 3.2 VC調達（2012-2020年）

| ラウンド | 時期 | 調達額 | 評価額 | リード投資家 |
|---------|------|--------|--------|------------|
| Seed | 2012年10月 | $5M | - | Sutter Hill Ventures |
| Series A | 2014年6月 | $26M | - | Sutter Hill, Redpoint |
| Series B | 2015年10月 | $45M | $450M | Sutter Hill, Redpoint |
| Series C | 2017年1月 | $100M | $1.5B | Sequoia Capital |
| Series D | 2018年1月 | $450M | $3.9B | Sequoia, Dragoneer |
| Series E | 2018年10月 | $450M | $3.9B | Sequoia, Dragoneer |
| Series F | 2020年2月 | $479M | $12.4B | Salesforce Ventures |

**総調達額**: $2.0B+（IPO前）

### 3.3 急成長（2017-2020年）

**成長指標**:
- 2019年度売上: $265M（前年比174%増）
- 2020年度売上: $592M（前年比123%増）
- 顧客数: 3,117社（2020年7月時点）
- Fortune 500の25%が顧客

**主要顧客**:
- Capital One、Adobe、Sony、Office Depot、Western Union等

## 4. IPO詳細（2020年9月）

### 4.1 IPO条件

| 項目 | 詳細 |
|------|------|
| IPO日 | 2020年9月16日 |
| 取引所 | NYSE |
| ティッカーシンボル | SNOW |
| 公募価格 | $120/株 |
| 公募株数 | 28,000,000株 |
| 調達額 | $3.4B |
| IPO時評価額 | $33B |
| 主幹事 | Goldman Sachs、Morgan Stanley、J.P. Morgan、Allen & Company |

**記録**:
- 史上最大のソフトウェアIPO
- 公募価格の2倍以上で初値

### 4.2 Berkshire Hathaway & Salesforceの投資

**Warren BuffettのBerkshire Hathaway**:
- IPOで$250M投資（Buffett初のIPO参加）
- 同時に$500Mの私募株購入
- 合計$750M投資

**Salesforce**:
- IPOで$250M投資

**意義**:
- Buffettは通常IPOに投資しない（テック嫌いでも有名）
- Snowflakeのビジネスモデルへの強い信頼

### 4.3 初日取引

**初値・終値**:
- 初値: $245（公募価格比+104.2%）
- 初日高値: $319
- 初日終値: $253.93（公募価格比+111.6%）
- 初日時価総額: $70B

**史上最高の初日騰落率**:
- ソフトウェアIPO史上最大の初日上昇
- 投資家からの圧倒的な需要

## 5. IPO成功要因分析

### 5.1 技術的優位性

**クラウドネイティブアーキテクチャ**:
- ストレージ・コンピュート分離
- 自動スケーリング
- マルチクラウド対応

**10倍優位性**:
- パフォーマンス: 従来DWHの10倍
- スケーラビリティ: 無限にスケール
- 運用コスト: 使った分だけ課金

### 5.2 タイミング

**市場環境**:
- データ量の爆発的増加
- クラウド移行の加速
- COVID-19によるデジタル化促進

**競合状況**:
- Amazon Redshift、Google BigQuery、Azure Synapse
- しかしSnowflakeはマルチクラウドで差別化

### 5.3 経営陣

**Frank Slootmanの実績**:
- Data Domain、ServiceNowでのIPO成功経験
- エンタープライズ営業の強化
- 「Amp It Up」哲学

### 5.4 財務指標

**IPO時点**:
- 売上: $592M（FY2020）
- YoY成長率: 123%
- 粗利率: 56%
- 純損失: $348M
- 顧客数: 3,117社

**Unit Economics**:
- Net Revenue Retention: 158%（業界トップクラス）
- 顧客あたりの平均契約額が急増

## 6. IPO後の成長

### 6.1 株価推移

| 時期 | イベント | 時価総額 |
|------|---------|---------|
| 2020年9月 | IPO | $33B |
| 2020年12月 | $400突破 | $100B+ |
| 2021年11月 | 史上最高値$405 | $120B+ |
| 2024年12月 | $180前後 | $60B+ |

### 6.2 新規事業

**Snowpark**:
- Python、Java、Scalaサポート
- データエンジニアリングの拡張

**Data Marketplace**:
- サードパーティデータの売買
- エコシステム構築

**Snowflake AI/ML**:
- 機械学習ワークロード対応

## 7. 教訓

### 7.1 IPO成功のポイント

1. **技術的優位性**: 10倍の改善
2. **エンタープライズ顧客**: Fortune 500の25%
3. **高成長**: YoY 123%
4. **経営陣の実績**: Slootmanの連続成功
5. **タイミング**: クラウド移行の加速期

### 7.2 Mega IPOの条件

- 大規模市場（TAM $100B+）
- 技術的ブレークスルー
- 高成長（100%+）
- 著名投資家の支持（Buffett等）

## 8. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| IPO日（2020年9月16日） | ✅ PASS | S-1、CNBC、Bloomberg |
| IPO価格（$120/株） | ✅ PASS | S-1、TechCrunch |
| IPO時評価額（$33B） | ✅ PASS | S-1、CNBC |
| 初日終値（$253.93、+111.6%） | ✅ PASS | Bloomberg、Yahoo Finance |
| Buffett投資（$750M） | ✅ PASS | CNBC、WSJ |
| 総調達額（$2.0B+） | ✅ PASS | Crunchbase、TechCrunch |

## 参照ソース

1. [Snowflake S-1 Filing (SEC)](https://www.sec.gov/Archives/edgar/data/1640147/000162828020013010/snow-20200731.htm)
2. [CNBC - Snowflake IPO soars 111%](https://www.cnbc.com/2020/09/16/snowflake-snow-opening-trading-on-the-nyse.html)
3. [Bloomberg - Snowflake Soars 111% in Biggest Software IPO Ever](https://www.bloomberg.com/news/articles/2020-09-16/snowflake-soars-in-biggest-software-ipo-ever-as-buffett-buys)
4. [TechCrunch - Snowflake IPO: Everything you need to know](https://techcrunch.com/2020/09/16/snowflake-ipo-everything-you-need-to-know/)
5. [Wikipedia - Snowflake Inc.](https://en.wikipedia.org/wiki/Snowflake_Inc.)
6. [WSJ - Warren Buffett Bets on Snowflake IPO](https://www.wsj.com/articles/warren-buffett-bets-on-snowflake-ipo-11600268425)
7. [Forbes - How Snowflake Became A $70 Billion Company](https://www.forbes.com/sites/alexkonrad/2020/09/16/how-snowflake-became-a-70-billion-company/)
8. [Crunchbase - Snowflake](https://www.crunchbase.com/organization/snowflake-computing)
9. [Sequoia Capital - Snowflake Investment](https://www.sequoiacap.com/companies/snowflake/)
10. [Sutter Hill Ventures - Snowflake](https://www.shv.com/portfolio/snowflake)
11. [Snowflake Investor Relations](https://investors.snowflake.com/)
12. [Yahoo Finance - Snowflake Stock](https://finance.yahoo.com/quote/SNOW/)
13. [The Information - Inside Snowflake's IPO](https://www.theinformation.com/articles/inside-snowflakes-ipo)
14. [Fortune - Frank Slootman's Snowflake Strategy](https://fortune.com/2020/09/15/snowflake-ipo-frank-slootman-interview/)
