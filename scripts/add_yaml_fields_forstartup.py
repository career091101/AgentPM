#!/usr/bin/env python3
"""
Add missing YAML frontmatter fields to ForStartup Edition skills
"""
import re
from pathlib import Path

skills_dir = Path("/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup")

# Skill-specific metadata
SKILL_METADATA = {
    "validate-psf": {
        "trigger_keywords": ["PSF検証", "PSF達成判定", "Problem Solution Fit", "ソリューションフィット検証", "validate PSF"],
        "stage": "Phase3（PSF検証）",
        "dependencies": ["validate-cpf（CPF達成が前提）", "research-competitors（競合調査完了）", "validate-10x（10倍優位性検証完了）", "build-lp（LP作成完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/psf_validation.md"
    },
    "discover-demand": {
        "trigger_keywords": ["需要発見", "市場機会発見", "困りごと調査", "demand discovery", "discover demand"],
        "stage": "Phase1（Idea検証）",
        "dependencies": [],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/demand_discovery.md"
    },
    "create-persona": {
        "trigger_keywords": ["ペルソナ作成", "ターゲット顧客定義", "persona作成", "create persona"],
        "stage": "Phase2（CPF検証）",
        "dependencies": ["discover-demand（需要発見完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/persona.md"
    },
    "validate-10x": {
        "stage": "Phase3（PSF検証）",
        "dependencies": ["research-competitors（競合調査完了）", "inventory-internal-resources（リソース棚卸し完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/10x_validation.md"
    },
    "create-mvv": {
        "trigger_keywords": ["MVV作成", "ミッション策定", "ビジョン策定", "create MVV", "mission vision values"],
        "stage": "Phase1（Idea検証）",
        "dependencies": ["discover-demand（需要発見完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/mvv.md"
    },
    "research-problem": {
        "trigger_keywords": ["課題調査", "problem research", "3U検証", "課題裏付け"],
        "stage": "Phase2（CPF検証）",
        "dependencies": ["create-persona（ペルソナ作成完了）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/problem_research.md"
    },
    "research-competitors": {
        "trigger_keywords": ["競合調査", "competitor research", "競合分析", "市場分析"],
        "stage": "Phase2（Research）",
        "dependencies": ["validate-cpf（CPF達成後推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_research/competitor_research.md"
    },
    "simulate-interview": {
        "trigger_keywords": ["インタビュー実施", "ユーザーインタビュー", "simulate interview", "顧客インタビュー"],
        "stage": "Phase2（CPF検証）",
        "dependencies": ["create-persona（ペルソナ作成完了）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/interview_simulation.md"
    },
    "startup-scorecard": {
        "trigger_keywords": ["スコアカード作成", "健全性評価", "startup scorecard", "BSC評価"],
        "stage": "Phase5（Monitoring）",
        "dependencies": ["validate-pmf（PMF達成推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/5_monitoring/scorecard.md"
    },
    "validate-market-timing": {
        "trigger_keywords": ["市場タイミング検証", "参入時期評価", "market timing", "タイミング分析"],
        "stage": "Phase1（Idea検証）",
        "dependencies": ["discover-demand（需要発見完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/market_timing.md"
    },
    "validate-ring-criteria": {
        "trigger_keywords": ["Ring基準検証", "ステージゲート評価", "Ring criteria", "シード調達評価"],
        "stage": "Phase5（Monitoring）",
        "dependencies": ["startup-scorecard（スコアカード作成完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/5_monitoring/ring_criteria_diagnosis.md"
    },
    "build-flywheel": {
        "trigger_keywords": ["フライホイール設計", "成長戦略", "build flywheel", "グロースループ"],
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-cpf（CPF達成推奨）", "create-mvv（MVV策定完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/flywheel.md"
    },
    "build-lp": {
        "trigger_keywords": ["LP作成", "ランディングページ", "build landing page", "LP制作"],
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-10x（10倍優位性検証完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/lp/README.md"
    },
    "build-approval-deck": {
        "trigger_keywords": ["承認資料作成", "役員承認デッキ", "approval deck", "社内承認資料"],
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-ring-criteria（Ring基準達成確認）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/approval_deck.md"
    },
    "build-synergy-map": {
        "trigger_keywords": ["シナジーマップ作成", "既存事業連携", "synergy map", "事業シナジー分析"],
        "stage": "Phase1（Initiating）",
        "dependencies": ["inventory-internal-resources（リソース棚卸し完了推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/synergy_map.md"
    },
    "design-exit-strategy": {
        "trigger_keywords": ["出口戦略設計", "exit strategy", "IPO計画", "M&A戦略"],
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-pmf（PMF達成推奨）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/exit_strategy.md"
    },
    "design-pricing": {
        "trigger_keywords": ["価格設定", "pricing設計", "料金プラン", "プライシング戦略"],
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-cpf（CPF達成推奨）", "research-competitors（競合調査完了）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/pricing.md"
    },
    "inventory-internal-resources": {
        "trigger_keywords": ["リソース棚卸し", "社内資産評価", "internal resources", "スタートアップリソース活用"],
        "stage": "Phase1（Initiating）",
        "dependencies": [],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/internal_resources.md"
    },
    "prepare-vc-meeting": {
        "trigger_keywords": ["VC面談準備", "投資家ミーティング", "VC meeting", "資金調達準備"],
        "stage": "Phase4（Executing）",
        "dependencies": ["build-pitch-deck（ピッチデッキ作成完了）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/4_executing/vc_meeting_prep.md"
    },
    "analyze-competitive-moat": {
        "stage": "Phase3（Planning）",
        "dependencies": ["validate-10x（10倍優位性検証完了）", "research-competitors（競合調査完了）"],
        "output_file": "Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/competitive_moat.md"
    }
}

def add_yaml_fields(skill_name, skill_file):
    """Add missing YAML fields to a skill file"""
    content = skill_file.read_text()

    # Extract existing YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        print(f"  ⚠️  No YAML frontmatter found in {skill_name}")
        return False

    yaml_content = yaml_match.group(1)
    yaml_end_pos = yaml_match.end()

    # Check which fields are missing
    has_trigger = 'trigger_keywords:' in yaml_content
    has_stage = 'stage:' in yaml_content
    has_deps = 'dependencies:' in yaml_content
    has_output = 'output_file:' in yaml_content

    if all([has_trigger, has_stage, has_deps, has_output]):
        print(f"  ✅ {skill_name}: All fields present")
        return False

    # Get metadata for this skill
    if skill_name not in SKILL_METADATA:
        print(f"  ⚠️  {skill_name}: No metadata defined, skipping")
        return False

    metadata = SKILL_METADATA[skill_name]

    # Find insertion point (end of description field)
    desc_end = yaml_content.rfind('---')
    if desc_end == -1:
        # Find the last line before the closing ---
        lines = yaml_content.strip().split('\n')
        insertion_point = len('\n'.join(lines)) + 1  # Position after last line
    else:
        insertion_point = desc_end

    # Build new fields to insert
    new_fields = []

    if not has_trigger and 'trigger_keywords' in metadata:
        keywords = '\n  - "' + '"\n  - "'.join(metadata['trigger_keywords']) + '"'
        new_fields.append(f"trigger_keywords:{keywords}")

    if not has_stage and 'stage' in metadata:
        new_fields.append(f"stage: {metadata['stage']}")

    if not has_deps and 'dependencies' in metadata:
        if metadata['dependencies']:
            deps = '\n  - ' + '\n  - '.join(metadata['dependencies'])
            new_fields.append(f"dependencies:{deps}")
        else:
            new_fields.append("dependencies: []")

    if not has_output and 'output_file' in metadata:
        new_fields.append(f"output_file: {metadata['output_file']}")

    if not new_fields:
        return False

    # Insert new fields
    new_yaml = yaml_content[:insertion_point] + '\n' + '\n'.join(new_fields) + '\n' + yaml_content[insertion_point:]
    new_content = '---\n' + new_yaml + '---' + content[yaml_end_pos:]

    # Write back
    skill_file.write_text(new_content)
    print(f"  ✅ {skill_name}: Added {', '.join([f.split(':')[0] for f in new_fields])}")
    return True

# Process all skills
print("Adding missing YAML fields to ForStartup skills...")
print("=" * 60)

updated_count = 0
for skill_dir in sorted(skills_dir.iterdir()):
    if not skill_dir.is_dir():
        continue

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        continue

    if add_yaml_fields(skill_dir.name, skill_file):
        updated_count += 1

print("=" * 60)
print(f"\nUpdated {updated_count} skills")
