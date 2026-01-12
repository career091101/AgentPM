#!/usr/bin/env python3
"""
Task Orchestrator for Wave6 VC-Backed Case Study Generation
============================================================

このスクリプトは5つの並列Taskエージェントを起動し、
FOUNDER_176-200の25件のVC-Backedケーススタディを完全自動生成します。

使用方法:
    python3 task_orchestrator.py

機能:
    - company_assignments.jsonから企業データ読み込み
    - 5バッチ分のプロンプト生成
    - Claude Code Task toolで5エージェント並列起動
    - 完了レポート生成
"""

import json
import os
from pathlib import Path
from datetime import datetime

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DOCS_DIR = PROJECT_ROOT / "documents" / "03_VC_Backed"

# 設定ファイル
COMPANY_ASSIGNMENTS_FILE = SCRIPTS_DIR / "company_assignments.json"
WAVE_DEFINITIONS_FILE = SCRIPTS_DIR / "wave_definitions.json"
TEMPLATE_FILE = DOCS_DIR / "FOUNDER_151_airbnb.md"

def load_json(filepath):
    """JSONファイルを読み込む"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_batch_prompt(batch_data, assignments):
    """
    バッチ専用プロンプトを生成

    Args:
        batch_data: wave_definitionsからのバッチ情報
        assignments: company_assignmentsからの企業詳細データ

    Returns:
        str: 完全なTaskエージェントプロンプト
    """
    batch_id = batch_data['batch_id']
    vc_focus = batch_data['vc_focus']

    # assignmentsから該当バッチの企業データ取得
    batch_assignments = None
    for batch in assignments['wave6']['batches']:
        if batch['batch_id'] == batch_id:
            batch_assignments = batch
            break

    if not batch_assignments:
        raise ValueError(f"Batch {batch_id} not found in company_assignments.json")

    # 企業リストを整形
    cases_list = []
    for idx, case in enumerate(batch_assignments['cases'], 1):
        case_text = f"""
{idx}. **{case['id']}**: {case['company']}
   - Founders: {case['founders']}
   - Founded: {case['founded_year']}
   - Valuation: {case['current_valuation']}
   - VC Angle: {case['vc_angle']}
   - Estimated Interview Count: {case['estimated_interview_count']}
   - Estimated Problem Commonality: {case['estimated_problem_commonality']}%
   - Research Notes: {case['research_notes']}
"""
        cases_list.append(case_text)

    cases_text = "\n".join(cases_list)

    # プロンプトテンプレート
    prompt = f"""# AUTONOMOUS CASE STUDY GENERATION - {batch_id.upper()}

## CRITICAL: FULL AUTOMATION MODE
- **NO human input required**
- **NO questions or confirmations**
- Use best judgment and available online sources
- Complete all 5 cases in this batch
- Work autonomously from start to finish

## VC FOCUS: {vc_focus}
Emphasize {vc_focus}'s investment perspective, board participation, and value-add throughout all case studies.

## TEMPLATE STRUCTURE (MANDATORY)
Follow FOUNDER_151_airbnb.md format EXACTLY:

### YAML Front Matter (必須フィールド):
```yaml
---
id: "FOUNDER_XXX"
title: "{{Founder Name}} - {{Company}}"
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
  top_tier_vcs: ["{vc_focus}", "Other Top VCs"]

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
   - **4.5 資金調達履歴** (**{vc_focus}の役割を詳述**)

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
- **{vc_focus} Role**: 投資判断の背景、ボード参加、戦略的支援内容
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
/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_XXX_{{company_slug}}.md
```

File naming: `FOUNDER_176_stripe.md`, `FOUNDER_177_reddit.md`, etc.

## ASSIGNED CASES FOR {batch_id.upper()}
{cases_text}

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
- [ ] All emphasize {vc_focus} investment perspective

## BEGIN EXECUTION NOW
Start with {batch_assignments['cases'][0]['id']} ({batch_assignments['cases'][0]['company']}) and proceed through all 5 cases.
"""

    return prompt

def generate_all_prompts():
    """全バッチのプロンプトを生成"""
    print("📖 Loading configuration files...")
    assignments = load_json(COMPANY_ASSIGNMENTS_FILE)
    wave_defs = load_json(WAVE_DEFINITIONS_FILE)

    wave6 = wave_defs['waves'][0]
    print(f"\n✅ Loaded Wave6: {wave6['name']}")
    print(f"   Total batches: {len(wave6['batches'])}")
    print(f"   Total cases: {wave6['count']}\n")

    prompts = {}
    for batch in wave6['batches']:
        batch_id = batch['batch_id']
        print(f"🔨 Generating prompt for {batch_id} ({batch['vc_focus']})...")
        prompt = generate_batch_prompt(batch, assignments)
        prompts[batch_id] = {
            'vc_focus': batch['vc_focus'],
            'prompt': prompt
        }

    return prompts

def save_prompts_for_manual_execution(prompts):
    """プロンプトをファイルに保存 (手動実行用)"""
    output_dir = SCRIPTS_DIR / "generated_prompts"
    output_dir.mkdir(exist_ok=True)

    for batch_id, data in prompts.items():
        output_file = output_dir / f"{batch_id}_prompt.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(data['prompt'])
        print(f"   💾 Saved: {output_file}")

    print(f"\n✅ All prompts saved to: {output_dir}\n")

def print_task_tool_instructions(prompts):
    """Task tool実行手順を出力"""
    print("\n" + "="*80)
    print("🚀 TASK TOOL PARALLEL EXECUTION INSTRUCTIONS")
    print("="*80)
    print("\nClaude Code UIで以下のTask toolコマンドを5つ並列実行してください:\n")

    for idx, (batch_id, data) in enumerate(prompts.items(), 1):
        print(f"\n--- Task {idx}: {batch_id} ({data['vc_focus']}) ---")
        print(f"```")
        print(f"Use Task tool with:")
        print(f"  subagent_type: general-purpose")
        print(f"  description: Generate {batch_id} VC-backed cases")
        print(f"  prompt: <paste from scripts/generated_prompts/{batch_id}_prompt.md>")
        print(f"```")

    print("\n" + "="*80)
    print("⏱️  Expected completion time: 35-45 minutes")
    print("📊 Total cases to generate: 25")
    print("="*80 + "\n")

def main():
    """メイン処理"""
    print("\n" + "="*80)
    print("🎯 WAVE6 VC-BACKED CASE STUDY ORCHESTRATOR")
    print("="*80 + "\n")

    # プロンプト生成
    prompts = generate_all_prompts()

    # プロンプトをファイル保存
    print("\n💾 Saving prompts to files...")
    save_prompts_for_manual_execution(prompts)

    # Task tool実行手順を表示
    print_task_tool_instructions(prompts)

    print("✅ Orchestrator setup complete!")
    print("\n次のステップ:")
    print("1. Claude Code UIを開く")
    print("2. 上記の5つのTaskツールコマンドを1つのメッセージで同時実行")
    print("3. 35-45分待機")
    print("4. validate_wave6.py実行で品質検証\n")

if __name__ == "__main__":
    main()
