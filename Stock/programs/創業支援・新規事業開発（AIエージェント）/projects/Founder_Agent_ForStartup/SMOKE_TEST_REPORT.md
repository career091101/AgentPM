# ForStartup Edition Smoke Test Report

## テスト実行日時

2026-01-03 14:42:56

## テスト結果サマリー

| テスト項目 | 合格 | 警告 | 不合格 | 合計 |
|-----------|------|------|--------|------|
| file_integrity | 24/26 | 0/26 | 2/26 | 26/26 |
| path_references | 0/26 | 0/26 | 26/26 | 26/26 |
| command_consistency | 0/26 | 25/26 | 1/26 | 26/26 |
| markdown_syntax | 14/26 | 8/26 | 4/26 | 26/26 |
| **総合** | **38/104** | **33/104** | **33/104** | **104/104** |

## Tier別詳細結果

### Tier 1スキル (12)

#### discover-demand

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/3u_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/persona_creation.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/documents/03_VC_Backed/**
  - 参照パスが見つかりません: @startup_science/03_tactics/founder_issue_fit/fif_overview.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - YAMLフロントマターが見つかりません

#### research-problem

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/3u_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/persona_creation.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/customer_interview.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @Founder_Research/analysis/cpf_patterns/**
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md**
  - YAMLフロントマターが見つかりません

#### research-competitors

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @startup_science/01_stages/psf/uvp_canvas.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-research-competitors
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @startup_science/01_stages/psf/10x_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/psf/psf_overview.md
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md**
  - 参照パスが見つかりません: @Founder_Research/analysis/psf_patterns/**
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### create-persona

- ファイル整合性: ❌
- 参照パス: ❌
- コマンド整合性: ❌
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - コマンドファイルが存在しません: for-startup-create-persona.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/3u_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/persona_creation.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/12_uber_two_sided_marketplace.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/01_airbnb_marketplace_personas.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/06_dropbox_freemium_strategy.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/08_stripe_developer_personas.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/07_slack_team_adoption.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/03_canva_freemium_personas.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/02_freshworks_b2b_saas_personas.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/05_amazon_customer_obsession.md
  - 参照パスが見つかりません: @Founder_Research/documents/pitch_decks/
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/10_linkedin_network_effects.md
  - 参照パスが見つかりません: @for_startup/_analysis/domain_requirements.md
  - 参照パスが見つかりません: @domain_requirements.md
  - 参照パスが見つかりません: @research_knowledge.md（Airbnb事例）
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/04_stitch_fix_personalization_personas.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/11_instagram_growth_hacking.md
  - 参照パスが見つかりません: @research/case_studies/tier2/create-persona/09_shopify_smb_personas.md
  - 参照パスが見つかりません: @research_knowledge.md（Freshworks事例）
  - 参照パスが見つかりません: @for_startup/_analysis/research_knowledge.md
  - コマンドファイルが存在しません: for-startup-create-persona.md

#### simulate-interview

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/3u_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/persona_creation.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @startup_science/01_stages/psf/uvp_canvas.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S001_airペイ.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-simulate-interview
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @Founder_Research/analysis/cpf_patterns/**
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md**
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### validate-cpf

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/3u_validation.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/persona_creation.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/customer_interview.md
  - 参照パスが見つかりません: @.claude/skills/for_startup/knowledge_base/case_reference.md#skill-mapping-validate-cpf
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/failure_patterns.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/for_startup/knowledge_base/knowledge_base.md#forstartup-edition
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md**
  - 参照パスが見つかりません: @Founder_Research/documents/WITHDRAWN/
  - 参照パスが見つかりません: @.claude/skills/for_startup/knowledge_base/knowledge_base.md#seed-stage-gates
  - 参照パスが見つかりません: @.claude/skills/for_startup/knowledge_base/knowledge_base.md#pivot-criteria
  - YAMLフロントマターが見つかりません

#### validate-psf

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @startup_science/01_stages/psf/uvp_canvas.md
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_airレジ.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-validate-psf
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @startup_science/01_stages/psf/10x_validation.md
  - 参照パスが見つかりません: @startup_science/01_stages/psf/psf_overview.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_recruit.md#failure-patterns
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md**
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_recruit.md#success-patterns
  - 参照パスが見つかりません: @Founder_Research/documents/WITHDRAWN/
  - 参照パスが見つかりません: @startup_science/01_stages/psf/mvp_types.md
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### validate-pmf

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ❌
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-validate-pmf
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_airレジ.md
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません
  - 行284: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行364: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行414: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行502: 見出しの階層が不正です (#2から#4へジャンプ)

#### validate-10x

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-validate-10x
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#10x-success-top5
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません
  - 行205: 見出しの階層が不正です (#2から#4へジャンプ)

#### create-mvv

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @startup_science/02_frameworks/lean_canvas/lean_canvas_overview.md`
  - 参照パスが見つかりません: @startup_science/02_frameworks/mvv/mvv_overview.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/recruit_specific_frameworks.md#recruit-values
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-create-mvv
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/CORP_M001_geppo.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません
  - 行217: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行238: 見出しの階層が不正です (#2から#4へジャンプ)

#### build-pitch-deck

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @startup_science/03_stages/pmf/pmf_overview.md
  - 参照パスが見つかりません: @startup_science/01_stages/cpf/cpf_overview.md
  - 参照パスが見つかりません: @for_startup/_analysis/domain_requirements.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @for_startup/_analysis/domain_requirements.md（VC投資基準）
  - 参照パスが見つかりません: @domain_requirements.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @research_knowledge.md
  - 参照パスが見つかりません: @for_startup/_analysis/research_knowledge.md
  - 参照パスが見つかりません: @for_startup/_analysis/research_knowledge.md（VC投資成功事例）
  - 参照パスが見つかりません: @startup_science/02_stages/psf/psf_overview.md
  - YAMLフロントマターが見つかりません

#### prepare-vc-meeting

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/research/case_studies/tier2/prepare-vc-meeting/_integration_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/research/case_studies/tier2/prepare-vc-meeting/case_*.md`
  - 参照パスが見つかりません: @for_startup/_analysis/research_knowledge.md（VC投資基準、ピッチ成功パターン）
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @Founder_Research/documents/01_Legendary/FOUNDER_006_brian_chesky.md（Airbnb事例）
  - 参照パスが見つかりません: @Founder_Research/documents/02_Unicorn/FOUNDER_060_girish_mathrubootham.md（Freshworks事例）
  - 参照パスが見つかりません: @Founder_Research/documents/02_Unicorn/FOUNDER_061_aaron_levie.md（Box事例）
  - YAMLフロントマターが見つかりません


### Tier 2スキル (14)

#### design-pricing

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_airレジ.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_Stripe.md,
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-design-pricing
  - 参照パスが見つかりません: @Founder_Research/documents/WITHDRAWN/CORP_W003_Coursera個別指導.md,
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### analyze-aarrr

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-analyze-aarrr
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @startup_science/05_scale/growth_hacking.md`
  - 参照パスが見つかりません: @startup_science/04_pmf/unit_economics.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-aarrr-benchmarks
  - 参照パスが見つかりません: @startup_science/05_scale/aarrr_framework.md`（未作成の場合はWebSearchで補完）
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### build-flywheel

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/CORP_S001_airpay.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
  - 参照パスが見つかりません: @startup_science/02_frameworks/lean_canvas/lean_canvas_overview.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @startup_science/03_tactics/flywheel/flywheel_design.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/WITHDRAWN/`
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-build-flywheel
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### build-lp

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#lp-success-patterns
  - 参照パスが見つかりません: @Founder_Research/documents/WITHDRAWN/CORP_W001_エリクラ.md,
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-build-lp
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_Stripe.md,
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - YAMLフロントマターが見つかりません

#### build-synergy-map

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/official_Figma_v3.md`
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER5_NEW_BUSINESS/CORP_S062_recruit_agent.md
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S043_airpay_qr.md
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/official_Slack_v3.md`
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/official_Notion_v3.md`
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/withdrawn_CODE.SCORE_v3.md`
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S012_airpay.md
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/official_Coursera_v3.md`
  - 参照パスが見つかりません: @Founder_Research/analysis/research_notes_v3/withdrawn_エリクラ_v3.md`
  - YAMLフロントマターが見つかりません
  - YAMLフロントマターが見つかりません
  - 行282: 見出しの階層が不正です (#1から#4へジャンプ)

#### inventory-internal-resources

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/FAILURE/`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - YAMLフロントマターが見つかりません
  - YAMLフロントマターが見つかりません

#### validate-market-timing

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/official_Stripe_v3.md`
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Sratup_Research/documents/03_VC_Backed/FOUNDER_172_segway.md（早すぎる
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Sratup_Research/documents/06_Pivot_Success/PIVOT_044_groupon.md（完璧なタイミング）
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md（早すぎる失敗）
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_008_jawbone.md（早すぎる
  - 参照パスが見つかりません: @/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/official_Coursera_v3.md`
  - 参照パスが見つかりません: @Founder_Agent_ForStartup/research/case_studies/tier2/prepare-vc-meeting/case_006_stripe_founder_market_fit.md（適切なタイミング）
  - 参照パスが見つかりません: @/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/withdrawn_エリクラ_v3.md`
  - 参照パスが見つかりません: @/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - YAMLフロントマターが見つかりません
  - YAMLフロントマターが見つかりません

#### design-exit-strategy

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/withdrawn_*.md
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/withdrawal_analysis/recruit_withdrawal_criteria.md
  - YAMLフロントマターが見つかりません
  - YAMLフロントマターが見つかりません

#### analyze-competitive-moat

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ❌
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/official_Stripe_v3.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/withdrawn_CODE.SCORE_v3.md`
  - YAMLフロントマターが見つかりません
  - 行227: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行283: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行347: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行397: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行467: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行527: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行619: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行729: 見出しの階層が不正です (#1から#3へジャンプ)

#### validate-ring-criteria

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/FAILURE/`
  - 参照パスが見つかりません: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/README.md`
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - YAMLフロントマターが見つかりません
  - YAMLフロントマターが見つかりません

#### orchestrate-review-loop

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ❌
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/agents/review-agent.md（Review
  - 参照パスが見つかりません: @startup_science/01_frameworks/cpf_validation.md
  - 参照パスが見つかりません: @.claude/agents/review-agent.md参照）
  - 参照パスが見つかりません: @.claude/skills/_shared/review_criteria.md参照）
  - 参照パスが見つかりません: @.claude/skills/_shared/review_criteria.md（品質基準）
  - 参照パスが見つかりません: @startup_science/02_tools/lean_canvas_template.md
  - YAMLフロントマターが見つかりません
  - 行219: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行437: 見出しの階層が不正です (#1から#3へジャンプ)
  - 行675: 見出しの階層が不正です (#1から#4へジャンプ)

#### discover-demand-vc-focus

- ファイル整合性: ❌
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ❌
- **総合判定**: FAIL
- **問題**: 
  - スキルディレクトリが存在しません: /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/discover-demand-vc-focus
  - SKILL.mdが存在しません
  - YAMLフロントマターが見つかりません
  - SKILL.mdが存在しません

#### build-approval-deck

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ⚠️
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria
  - 参照パスが見つかりません: @Founder_Research/documents/SUCCESS/CORP_S009_airレジ.md
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#success-patterns
  - 参照パスが見つかりません: @Founder_Research/analysis/approval_deck_templates.md（将来作成予定）
  - 参照パスが見つかりません: @Founder_Research/documents/pitch_decks/（創業者向け、参考用）
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - 参照パスが見つかりません: @Founder_Research/analysis/integrated_analysis_report.md
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-approval-deck
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
  - 参照パスが見つかりません: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
  - 参照パスが見つかりません: @.claude/skills/_shared/recruit_specific_frameworks.md#ring制度（将来作成予定）
  - 参照パスが見つかりません: @.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
  - 参照パスが見つかりません: @Founder_Research/documents/pitch_decks/（創業者ピッチデッキ事例）
  - YAMLフロントマターが見つかりません
  - 行1014: 見出しの階層が不正です (#2から#4へジャンプ)
  - 行1055: 見出しの階層が不正です (#1から#4へジャンプ)

#### validate-unit-economics-strict

- ファイル整合性: ✅
- 参照パス: ❌
- コマンド整合性: ⚠️
- Markdown構文: ✅
- **総合判定**: FAIL
- **問題**: 
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
  - 参照パスが見つかりません: @for_startup/knowledge_base/knowledge_base.md（ユニットエコノミクス基準）
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
  - 参照パスが見つかりません: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式
  - 参照パスが見つかりません: @for_startup/knowledge_base/case_reference_for_startup.md（成功事例）
  - 参照パスが見つかりません: @for_startup/knowledge_base/knowledge_base.md#ユニットエコノミクス基準
  - 参照パスが見つかりません: @for_startup/knowledge_base/case_reference_for_startup.md
  - YAMLフロントマターが見つかりません


## 重大な問題

1. create-persona: ファイル整合性エラー - コマンドファイルが存在しません: for-startup-create-persona.md
2. create-persona: コマンド整合性エラー
3. discover-demand-vc-focus: ファイル整合性エラー - スキルディレクトリが存在しません: /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/discover-demand-vc-focus

## 推奨修正

1. 26個のスキルで参照パスに問題があります。参照パスを修正してください。
2. 4個のスキルでMarkdown構文エラーが見つかりました。

## E2Eテスト準備状況

- ❌ 基本動作確認に失敗
- ❌ 大規模修正必要
