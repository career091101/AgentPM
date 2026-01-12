#!/usr/bin/env python3
"""
Add ForRecruit Knowledge Base Reference sections to all 18 skills.
Handles multiple section patterns.
"""

from pathlib import Path
import re

# Skill-specific reference mappings
SKILL_REFERENCES = {
    "discover-demand": {
        "specific_case": "Airレジ需要発見: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md",
        "skill_mapping": "skill-mapping-discover-demand"
    },
    "research-problem": {
        "specific_case": "Geppo課題検証事例: @Recruit_Product_Research/documents/SUCCESS/CORP_M001_geppo.md",
        "skill_mapping": "skill-mapping-research-problem"
    },
    "inventory-internal-resources": {
        "specific_case": "Air統合分析: @Recruit_Product_Research/analysis/integrated_analysis_report.md",
        "skill_mapping": "skill-mapping-inventory-resources"
    },
    "build-approval-deck": {
        "specific_case": "Airレジ承認プロセス: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md",
        "skill_mapping": "skill-mapping-approval-deck"
    },
    "validate-ring-criteria": {
        "specific_case": "達成期間ベンチマーク: @.claude/skills/_shared/knowledge_base.md#forrecruit-ring-benchmarks",
        "skill_mapping": "skill-mapping-ring-criteria"
    },
    "validate-cpf": {
        "specific_case": "Geppo CPF 80%事例: @Recruit_Product_Research/documents/SUCCESS/CORP_M001_geppo.md",
        "skill_mapping": "skill-mapping-validate-cpf"
    },
    "simulate-interview": {
        "specific_case": "Airペイ100回ヒアリング: @Recruit_Product_Research/documents/SUCCESS/CORP_S001_airペイ.md",
        "skill_mapping": "skill-mapping-simulate-interview"
    },
    "validate-psf": {
        "specific_case": "Airレジ PSF成功: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md",
        "skill_mapping": "skill-mapping-validate-psf"
    },
    "research-competitors": {
        "specific_case": "競合分析事例（Airシリーズ）: @Recruit_Product_Research/analysis/integrated_analysis_report.md",
        "skill_mapping": "skill-mapping-research-competitors"
    },
    "validate-10x": {
        "specific_case": "10倍優位性事例Top 5: @.claude/skills/_shared/case_reference_for_recruit.md#10x-success-top5",
        "skill_mapping": "skill-mapping-validate-10x"
    },
    "validate-pmf": {
        "specific_case": "Airレジ PMF 9.2事例: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md",
        "skill_mapping": "skill-mapping-validate-pmf"
    },
    "build-flywheel": {
        "specific_case": "Airシリーズエコシステム: @Recruit_Product_Research/analysis/integrated_analysis_report.md",
        "skill_mapping": "skill-mapping-build-flywheel"
    },
    "create-mvv": {
        "specific_case": "リクルート6つの価値観: @.claude/skills/_shared/recruit_specific_frameworks.md#recruit-values",
        "skill_mapping": "skill-mapping-create-mvv"
    },
    "analyze-aarrr": {
        "specific_case": "AARRR指標ベンチマーク: @.claude/skills/_shared/knowledge_base.md#forrecruit-aarrr-benchmarks",
        "skill_mapping": "skill-mapping-analyze-aarrr"
    },
    "startup-scorecard": {
        "specific_case": "総合80点満点評価: @.claude/skills/_shared/recruit_specific_frameworks.md#scorecard-criteria",
        "skill_mapping": "skill-mapping-startup-scorecard"
    },
    "build-lp": {
        "specific_case": "2段階CTA事例: @.claude/skills/_shared/case_reference_for_recruit.md#lp-success-patterns",
        "skill_mapping": "skill-mapping-build-lp"
    },
    "design-pricing": {
        "specific_case": "基本無料モデル（Airレジ）: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md",
        "skill_mapping": "skill-mapping-design-pricing"
    },
    "orchestrate-phase1-recruit": {
        "specific_case": "18スキル統合フロー: @.claude/skills/_shared/knowledge_base.md#forrecruit-orchestration",
        "skill_mapping": "skill-mapping-orchestrate"
    }
}

REFERENCE_TEMPLATE = """
## ForRecruit Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/recruit_specific_frameworks.md#cpf-evaluation
- Ring制度詳細: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-system
- 社内リソース活用: @.claude/skills/_shared/recruit_specific_frameworks.md#resource-leverage
- ForRecruit評価基準: @.claude/skills/_shared/knowledge_base.md#forrecruit-evaluation

### 事例参照
- 成功パターン（Tier 1-4）: @.claude/skills/_shared/case_reference_for_recruit.md#success-patterns
- 失敗パターン: @.claude/skills/_shared/case_reference_for_recruit.md#failure-patterns
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#{skill_mapping}
- {specific_case}

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
"""

def add_reference_section(skill_path: Path, skill_name: str):
    """Add ForRecruit Knowledge Base Reference section to a skill file."""

    content = skill_path.read_text(encoding='utf-8')

    # Check if already has reference section
    if "## ForRecruit Knowledge Base Reference" in content:
        print(f"  ✓ {skill_name}: Already has reference section, skipping")
        return "skipped"

    # Get skill-specific references
    refs = SKILL_REFERENCES.get(skill_name, {
        "specific_case": "成功事例参照: @Recruit_Product_Research/analysis/integrated_analysis_report.md",
        "skill_mapping": f"skill-mapping-{skill_name}"
    })

    # Create reference section with skill-specific content
    reference_section = REFERENCE_TEMPLATE.format(
        skill_mapping=refs["skill_mapping"],
        specific_case=refs["specific_case"]
    )

    # Try multiple insertion patterns
    patterns = [
        (r'\n---\n\n## 使用例', 6),  # Before "## 使用例"
        (r'\n---\n\n## 注意事項', 6),  # Before "## 注意事項"
        (r'\n## 更新履歴', 0),  # Before "## 更新履歴"
        (r'\n## Knowledge Base参照', 0),  # Replace "## Knowledge Base参照"
    ]

    for pattern, skip_chars in patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.start()

            # Special handling for replacing existing Knowledge Base section
            if "## Knowledge Base参照" in pattern:
                # Find the end of this section (next ## or end of file)
                next_section = re.search(r'\n## ', content[match.end():])
                if next_section:
                    end_pos = match.start() + next_section.start()
                else:
                    end_pos = len(content)

                # Replace the entire section
                new_content = (
                    content[:insert_pos] +
                    "\n" +
                    reference_section +
                    content[end_pos:]
                )
            else:
                # Insert before the section
                new_content = (
                    content[:insert_pos] +
                    "\n---\n" +
                    reference_section +
                    content[insert_pos + skip_chars:]
                )

            # Write back
            skill_path.write_text(new_content, encoding='utf-8')
            print(f"  ✓ {skill_name}: Added reference section (pattern: {pattern})")
            return "added"

    print(f"  ✗ {skill_name}: Could not find insertion point")
    return "failed"

def main():
    skills_dir = Path("/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_recruit")

    print("Adding ForRecruit Knowledge Base Reference sections to skills...")
    print()

    added_count = 0
    skipped_count = 0
    failed_count = 0

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        skill_file = skill_dir / "SKILL.md"

        if not skill_file.exists():
            print(f"  ✗ {skill_name}: SKILL.md not found")
            failed_count += 1
            continue

        result = add_reference_section(skill_file, skill_name)
        if result == "added":
            added_count += 1
        elif result == "skipped":
            skipped_count += 1
        else:
            failed_count += 1

    print()
    print(f"Summary:")
    print(f"  Added: {added_count} skills")
    print(f"  Skipped: {skipped_count} skills")
    print(f"  Failed: {failed_count} skills")
    print(f"  Total: {added_count + skipped_count + failed_count} skills")
    print()

    if failed_count == 0:
        print("✅ All skills successfully processed!")
    else:
        print("⚠️  Some skills could not be processed. Manual review needed.")

if __name__ == "__main__":
    main()
