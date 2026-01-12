# AUTONOMOUS CASE STUDY GENERATION - BATCH6_5

## CRITICAL: FULL AUTOMATION MODE
- **NO human input required**
- **NO questions or confirmations**
- Use best judgment and available online sources
- Complete all 5 cases in this batch
- Work autonomously from start to finish

## VC FOCUS: Founders Fund & Benchmark
Emphasize Founders Fund & Benchmark's investment perspective, board participation, and value-add throughout all case studies.

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
  top_tier_vcs: ["Founders Fund & Benchmark", "Other Top VCs"]

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
   - **4.5 資金調達履歴** (**Founders Fund & Benchmarkの役割を詳述**)

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
- **Founders Fund & Benchmark Role**: 投資判断の背景、ボード参加、戦略的支援内容
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

## ASSIGNED CASES FOR BATCH6_5

1. **FOUNDER_196**: SpaceX
   - Founders: Elon Musk
   - Founded: 2002
   - Valuation: $180B+
   - VC Angle: Founders Fund視点 (既存FOUNDER_361とは別角度)
   - Estimated Interview Count: 80
   - Estimated Problem Commonality: 50%
   - Research Notes: Founders Fund Peter Thiel視点、宇宙産業への挑戦、再利用ロケット


2. **FOUNDER_197**: Palantir
   - Founders: Peter Thiel, Alex Karp, Nathan Gettings, Joe Lonsdale, Stephen Cohen
   - Founded: 2003
   - Valuation: IPO $20B+
   - VC Angle: Founders Fund視点 (既存FOUNDER_159を補完)
   - Estimated Interview Count: 60
   - Estimated Problem Commonality: 40%
   - Research Notes: Founders Fund創業者企業、ビッグデータ分析プラットフォーム


3. **FOUNDER_198**: Uber
   - Founders: Travis Kalanick & Garrett Camp
   - Founded: 2009
   - Valuation: IPO $82B
   - VC Angle: Benchmark視点、Series A $11M投資の伝説
   - Estimated Interview Count: 120
   - Estimated Problem Commonality: 80%
   - Research Notes: Benchmark Series A、Bill Gurleyの支援、ライドシェア市場創出


4. **FOUNDER_199**: Twitter
   - Founders: Jack Dorsey, Evan Williams, Biz Stone, Noah Glass
   - Founded: 2006
   - Valuation: $44B (Musk買収)
   - VC Angle: Benchmark視点、Series A投資
   - Estimated Interview Count: 100
   - Estimated Problem Commonality: 75%
   - Research Notes: Benchmark Series A投資、リアルタイム情報ネットワーク


5. **FOUNDER_200**: eBay
   - Founders: Pierre Omidyar
   - Founded: 1995
   - Valuation: IPO $1.5B → 現在$25B+
   - VC Angle: Benchmark視点、初期投資の成功
   - Estimated Interview Count: 80
   - Estimated Problem Commonality: 85%
   - Research Notes: Benchmark初期投資、オンラインオークション市場創出、C2Cマーケットプレイスのパイオニア


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
- [ ] All emphasize Founders Fund & Benchmark investment perspective

## BEGIN EXECUTION NOW
Start with FOUNDER_196 (SpaceX) and proceed through all 5 cases.
