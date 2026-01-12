# AUTONOMOUS CASE STUDY GENERATION - BATCH6_3

## CRITICAL: FULL AUTOMATION MODE
- **NO human input required**
- **NO questions or confirmations**
- Use best judgment and available online sources
- Complete all 5 cases in this batch
- Work autonomously from start to finish

## VC FOCUS: Andreessen Horowitz
Emphasize Andreessen Horowitz's investment perspective, board participation, and value-add throughout all case studies.

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
  top_tier_vcs: ["Andreessen Horowitz", "Other Top VCs"]

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
   - **4.5 資金調達履歴** (**Andreessen Horowitzの役割を詳述**)

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
- **Andreessen Horowitz Role**: 投資判断の背景、ボード参加、戦略的支援内容
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
/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_XXX_{company_slug}.md
```

File naming: `FOUNDER_176_stripe.md`, `FOUNDER_177_reddit.md`, etc.

## ASSIGNED CASES FOR BATCH6_3

1. **FOUNDER_186**: Lyft
   - Founders: Logan Green & John Zimmer
   - Founded: 2012
   - Valuation: IPO $24B → 現在調整中
   - VC Angle: a16z Series B投資、ライドシェア市場での挑戦
   - Estimated Interview Count: 100
   - Estimated Problem Commonality: 80%
   - Research Notes: Uber競合としてのポジショニング、a16zの戦略的支援


2. **FOUNDER_187**: Oculus VR
   - Founders: Palmer Luckey
   - Founded: 2012
   - Valuation: $2B (Facebook買収)
   - VC Angle: a16z Series A投資、VR市場創出
   - Estimated Interview Count: 70
   - Estimated Problem Commonality: 60%
   - Research Notes: Kickstarterから始まったVR革命、a16z早期投資、Facebook買収


3. **FOUNDER_188**: Pinterest
   - Founders: Ben Silbermann, Evan Sharp, Paul Sciarra
   - Founded: 2010
   - Valuation: IPO $12B
   - VC Angle: a16z Series A投資、ビジュアル発見プラットフォーム
   - Estimated Interview Count: 80
   - Estimated Problem Commonality: 75%
   - Research Notes: ビジュアルブックマーク、女性ユーザー中心、a16zの成長支援


4. **FOUNDER_189**: Slack
   - Founders: Stewart Butterfield
   - Founded: 2013
   - Valuation: $27.7B (Salesforce買収)
   - VC Angle: a16z投資、エンタープライズコミュニケーション革命
   - Estimated Interview Count: 130
   - Estimated Problem Commonality: 85%
   - Research Notes: ゲーム開発から生まれたツール、a16zの支援、Salesforce買収


5. **FOUNDER_190**: Robinhood
   - Founders: Vlad Tenev & Baiju Bhatt
   - Founded: 2013
   - Valuation: IPO $32B
   - VC Angle: a16z投資、手数料無料取引革命
   - Estimated Interview Count: 90
   - Estimated Problem Commonality: 70%
   - Research Notes: 手数料無料取引アプリ、若年層投資家開拓、a16zの戦略的支援


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
- [ ] All emphasize Andreessen Horowitz investment perspective

## BEGIN EXECUTION NOW
Start with FOUNDER_186 (Lyft) and proceed through all 5 cases.
