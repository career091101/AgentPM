# AUTONOMOUS CASE STUDY GENERATION - BATCH6_2

## CRITICAL: FULL AUTOMATION MODE
- **NO human input required**
- **NO questions or confirmations**
- Use best judgment and available online sources
- Complete all 5 cases in this batch
- Work autonomously from start to finish

## VC FOCUS: Sequoia Capital
Emphasize Sequoia Capital's investment perspective, board participation, and value-add throughout all case studies.

## TEMPLATE STRUCTURE (MANDATORY)
Follow FOUNDER_151_airbnb.md format EXACTLY:

### YAML Front Matter (必須フィールド):
```yaml
---
id: "FOUNDER_XXX"
title: "{Founder Name} - {Company}"
category: "founder"
tier: "vc_backed"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: [relevant tags including VC name, industry, exit type]

# 基本情報
founder:
  name: "Full Name (Role)"
  birth_year: YYYY
  nationality: "Country"
  education: "University/Degree"
  prior_experience: "Previous roles/companies"

company:
  name: "Company Name"
  founded_year: YYYY
  industry: "Primary Industry / Sector"
  current_status: "ipo|acquired|active|shutdown"
  valuation: "$XXB (description)"
  employees: XXXX

# VC投資情報 (CRITICAL - 詳細必須)
funding:
  total_raised: "$XXB"
  funding_rounds:
    - round: "seed|series_a|series_b|series_c|..."
      date: "YYYY-MM-DD"
      amount: "$XXM"
      valuation_post: "$XXM|$XXB"
      lead_investors: ["VC Name"]
      other_investors: ["Investor 1", "Investor 2"]
  top_tier_vcs: ["Sequoia Capital", "Other Top VCs"]

# 成功/失敗/Pivot分類
outcome:
  category: "success|failure|pivot"
  subcategory: "exit_success|growth_success|..."
  failure_pattern: ""
  pivot_details:
    count: 0
    major_pivots: []

# orchestrate-phase1対応 (CPF/PSF検証データ)
validation_data:
  cpf:
    interview_count: XX-XXX (research or estimate)
    problem_commonality: XX (percentage 0-100)
    wtp_confirmed: true|false
    urgency_score: X (1-10)
    validation_method: "方法の説明"
  psf:
    ten_x_axes:
      - axis: "軸の名前 (例: コスト削減)"
        multiplier: X (3, 5, 10, 20, 50, 100)
      - axis: "別の軸"
        multiplier: Y
    mvp_type: "concierge|wizard_of_oz|landing_page|prototype|..."
    initial_cvr: null or percentage
    uvp_clarity: X (1-10)
    competitive_advantage: "Main differentiator"

# 品質保証
quality:
  fact_check: "pass"
  sources_count: XX (minimum 12)
  last_verified: "2025-12-29"
  primary_sources: []
---
```

### Markdown本文 (12セクション必須):

1. **基本情報**
   - 創業者・企業概要テーブル

2. **創業ストーリー**
   - 2.1 課題発見 (Demand Discovery)
   - 2.2 CPF検証 (Customer Problem Fit validation)
   - 2.3 PSF検証 (Problem Solution Fit with 10x axes table)

3. **ピボット/失敗経験**
   - 初期の試行錯誤やピボット

4. **成長戦略**
   - 4.1 初期トラクション
   - 4.2 Flywheel/成長ループ
   - 4.3 スケーリング戦略
   - 4.4 バリューチェーン
   - **4.5 資金調達履歴** (**Sequoia Capitalの役割を詳述**)

5. **使用ツール・サービス**
   - 技術スタック、インフラ

6. **成功要因分析**
   - KSF、タイミング、差別化

7. **日本市場適用性**
   - 5段階スコアリング (Cultural Fit, Regulatory, Market Size, Competition, Localization)

8. **orchestrate-phase1への示唆**
   - CPF/PSF検証フレームワークへの学び

9. **事業アイデア候補**
   - このケースから着想する3つのビジネスアイデア

10. **ファクトチェック結果**
    - データ検証テーブル (PASS/WARN/FAIL)

11. **参照ソース**
    - 12+の検証済みソース (URLs, 記事, 書籍)

## RESEARCH REQUIREMENTS

### Data Collection (WebSearchツール必須使用):
- **Funding History**: 全ての資金調達ラウンド (amount, date, valuation, investors)
- **Sequoia Capital Role**: 投資判断の背景、ボード参加、戦略的支援内容
- **Founder Background**: 学歴、職歴、原体験
- **Customer Validation**: interview_count, problem_commonality (研究または推定)
- **Ten_x_axes**: 競合比較での10倍優位性 (2-5軸)
- **Sources**: 最低12の信頼できるソース (Crunchbase, TechCrunch, 公式ブログ, インタビュー記事)

### Estimation Guidelines (リサーチ不十分時):
- **interview_count**:
  - Seed段階: 40-80
  - Series A: 80-120
  - Series B+: 120-150+
- **problem_commonality**:
  - B2B SaaS: 60-80%
  - Consumer: 70-90%
  - Deep Tech: 40-60%
- 推定値は `(estimated)` フラグ付与

## OUTPUT LOCATION
Save each file to:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_XXX_{company_slug}.md
```

File naming: `FOUNDER_176_stripe.md`, `FOUNDER_177_reddit.md`, etc.

## ASSIGNED CASES FOR BATCH6_2

1. **FOUNDER_181**: Apple
   - Founders: Steve Jobs & Steve Wozniak
   - Founded: 1976
   - Valuation: $3T
   - VC Angle: Sequoia初期投資、Don Valentineの伝説的投資
   - Estimated Interview Count: 50
   - Estimated Problem Commonality: 60%
   - Research Notes: Sequoia VC視点でのApple投資ストーリー、Don Valentineの決断


2. **FOUNDER_182**: Google
   - Founders: Larry Page & Sergey Brin
   - Founded: 1998
   - Valuation: $1.7T
   - VC Angle: Sequoia・Kleinerの共同投資、検索エンジン市場制覇
   - Estimated Interview Count: 100
   - Estimated Problem Commonality: 90%
   - Research Notes: PageRank革命、Sequoia・Kleinerの共同リード投資、広告モデル構築


3. **FOUNDER_183**: LinkedIn
   - Founders: Reid Hoffman
   - Founded: 2003
   - Valuation: $26B (Microsoft買収)
   - VC Angle: Sequoia Series A投資、プロフェッショナルネットワーク
   - Estimated Interview Count: 120
   - Estimated Problem Commonality: 80%
   - Research Notes: B2Bソーシャルネットワーク、Sequoiaの早期支援


4. **FOUNDER_184**: YouTube
   - Founders: Chad Hurley, Steve Chen, Jawed Karim
   - Founded: 2005
   - Valuation: $1.65B (Google買収)
   - VC Angle: Sequoia Series A $3.5M、動画共有革命
   - Estimated Interview Count: 60
   - Estimated Problem Commonality: 85%
   - Research Notes: 動画共有プラットフォーム創出、Sequoia早期投資、18ヶ月でGoogle買収


5. **FOUNDER_185**: PayPal
   - Founders: Peter Thiel, Elon Musk (X.com合併)
   - Founded: 1998
   - Valuation: $1.5B (eBay買収)
   - VC Angle: Sequoia投資、オンライン決済のパイオニア
   - Estimated Interview Count: 110
   - Estimated Problem Commonality: 75%
   - Research Notes: Confinity + X.com合併、eBay買収、PayPal Mafia起点


## EXECUTION INSTRUCTIONS

1. **Start Immediately**: No confirmations, no delays
2. **Research Thoroughly**: Use WebSearch for each company extensively
3. **Generate Complete Files**: YAML + 12 markdown sections for all 5 cases
4. **Quality Assurance**: 12+ sources, fact_check: "pass", all CPF/PSF data populated
5. **Save Files**: Use Write tool to save to correct directory
6. **Report Completion**: After all 5 cases complete, report file paths

## SUCCESS CRITERIA
- [ ] 5 files created
- [ ] All follow FOUNDER_151 template
- [ ] All have 12+ sources
- [ ] All have fact_check: "pass"
- [ ] All have CPF/PSF data (research or estimated)
- [ ] All emphasize Sequoia Capital investment perspective

## BEGIN EXECUTION NOW
Start with FOUNDER_181 (Apple) and proceed through all 5 cases.
