#!/usr/bin/env python3
"""
ForStartup Edition Final Quality Evaluation Script
Comprehensive assessment across all 30 skills
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

SKILLS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup")
COMMANDS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/.claude/commands")
FOUNDER_RESEARCH = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research")

# Expected 30 skills
EXPECTED_SKILLS = [
    "analyze-aarrr", "analyze-competitive-moat", "build-approval-deck",
    "build-flywheel", "build-lp", "build-pitch-deck", "build-synergy-map",
    "create-fundraising-plan", "create-mvv", "create-persona",
    "design-exit-strategy", "design-pricing", "discover-demand",
    "inventory-internal-resources", "measure-aarrr", "monitor-burn-rate",
    "orchestrate-review-loop", "prepare-vc-meeting", "research-competitors",
    "research-problem", "simulate-interview", "startup-scorecard",
    "validate-10x", "validate-cpf", "validate-market-timing",
    "validate-pmf", "validate-psf", "validate-ring-criteria",
    "validate-unit-economics", "validate-unit-economics-strict"
]

# YAML frontmatter required fields
REQUIRED_YAML_FIELDS = ["name", "description", "trigger_keywords", "output_file", "stage", "dependencies"]

# Category A: Inappropriate ForRecruit references (should be 0)
CAT_A_PATTERNS = [
    r'Ring制度',
    r'リング制度',
    r'ForRecruit\s+Edition',
    r'for-recruit-edition',
    r'ForRecruitプロジェクト',
    r'リクルート社内',
    r'社内リソース活用',
    r'ForRecruitカスタマイズ',
]

# Category C: Brand bias patterns (should be genericized)
CAT_C_PATTERNS = [
    r'リクルート(?!グループ出身|出身者|OB)',  # Recruit without "出身" context
    r'Indeed',
    r'Glassdoor',
    r'(?<!事例: )(?<!参考: )リクルート社',  # Recruit company without case study context
]

# VC Criteria patterns
VC_CRITERIA_PATTERNS = [
    r'NRR\s*≥?\s*120%',
    r'年間成長率\s*≥?\s*300%',
    r'CPF\s*≥?\s*70%',
    r'PSF\s*≥?\s*70%',
    r'PMF\s*≥?\s*70%',
    r'TAM\s*≥?\s*\$?1B|\$1,000M',
]

class EvaluationReport:
    def __init__(self):
        self.scores = {
            "file_integrity": 0,
            "metadata_completeness": 0,
            "forrecruit_remnant": 0,
            "path_accuracy": 0,
            "vc_criteria": 0
        }
        self.findings = defaultdict(list)
        self.issues = {"P0": [], "P1": [], "P2": []}

    def add_finding(self, category, message):
        self.findings[category].append(message)

    def add_issue(self, priority, skill, message):
        self.issues[priority].append(f"{skill}: {message}")

    def calculate_total(self):
        return sum(self.scores.values())

def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return None

    yaml_content = yaml_match.group(1)
    yaml_dict = {}
    for line in yaml_content.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            yaml_dict[key.strip()] = value.strip()
    return yaml_dict

def check_file_integrity(report):
    """Criterion 1: File Integrity (30 points)"""
    print("\n=== Checking File Integrity ===")

    # Check SKILL.md files
    skill_files = []
    missing_skills = []
    for skill in EXPECTED_SKILLS:
        skill_path = SKILLS_DIR / skill / "SKILL.md"
        if skill_path.exists():
            skill_files.append(skill)
        else:
            missing_skills.append(skill)
            report.add_issue("P0", skill, "SKILL.md missing")

    # Check command files
    command_files = []
    missing_commands = []
    for skill in EXPECTED_SKILLS:
        cmd_path = COMMANDS_DIR / f"for-startup-{skill}.md"
        if cmd_path.exists():
            command_files.append(skill)
        else:
            missing_commands.append(skill)
            report.add_issue("P1", skill, "Command file missing")

    # Calculate score
    skill_score = (len(skill_files) / 30) * 15
    command_score = (len(command_files) / 30) * 10
    structure_score = 5 if not missing_skills else 0

    report.scores["file_integrity"] = skill_score + command_score + structure_score
    report.add_finding("file_integrity", f"✓ SKILL.md files: {len(skill_files)}/30")
    report.add_finding("file_integrity", f"✓ Command files: {len(command_files)}/30")
    if missing_skills:
        report.add_finding("file_integrity", f"✗ Missing SKILLs: {', '.join(missing_skills)}")
    if missing_commands:
        report.add_finding("file_integrity", f"✗ Missing commands: {', '.join(missing_commands)}")

    return skill_files

def check_metadata_completeness(report, skills):
    """Criterion 2: Metadata Completeness (20 points)"""
    print("\n=== Checking Metadata Completeness ===")

    skills_with_yaml = 0
    complete_yaml = 0

    for skill in skills:
        skill_path = SKILLS_DIR / skill / "SKILL.md"
        content = skill_path.read_text()
        yaml_data = parse_yaml_frontmatter(content)

        if yaml_data:
            skills_with_yaml += 1
            missing_fields = [f for f in REQUIRED_YAML_FIELDS if f not in yaml_data]
            if not missing_fields:
                complete_yaml += 1
            else:
                report.add_issue("P1", skill, f"Missing YAML fields: {', '.join(missing_fields)}")
        else:
            report.add_issue("P0", skill, "No YAML frontmatter found")

    # Calculate score
    yaml_presence = (skills_with_yaml / len(skills)) * 10
    yaml_quality = (complete_yaml / len(skills)) * 10

    report.scores["metadata_completeness"] = yaml_presence + yaml_quality
    report.add_finding("metadata_completeness", f"✓ Skills with YAML: {skills_with_yaml}/{len(skills)}")
    report.add_finding("metadata_completeness", f"✓ Complete YAML: {complete_yaml}/{len(skills)}")

def check_forrecruit_remnants(report, skills):
    """Criterion 3: ForRecruit Remnant Removal (20 points)"""
    print("\n=== Checking ForRecruit Remnants ===")

    cat_a_total = 0
    cat_c_total = 0

    for skill in skills:
        skill_path = SKILLS_DIR / skill / "SKILL.md"
        content = skill_path.read_text()

        # Check Category A (inappropriate references)
        for pattern in CAT_A_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                cat_a_total += len(matches)
                report.add_issue("P0", skill, f"Category A remnant found: {pattern} ({len(matches)} occurrences)")

        # Check Category C (brand bias)
        for pattern in CAT_C_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                cat_c_total += len(matches)
                report.add_issue("P2", skill, f"Category C brand bias: {pattern} ({len(matches)} occurrences)")

    # Calculate score (20 points max)
    # Cat A: should be 0 (15 points if clean)
    # Cat C: should be minimal (5 points if < 10 total)
    cat_a_score = 15 if cat_a_total == 0 else max(0, 15 - cat_a_total)
    cat_c_score = 5 if cat_c_total < 10 else max(0, 5 - (cat_c_total - 10) * 0.5)

    report.scores["forrecruit_remnant"] = cat_a_score + cat_c_score
    report.add_finding("forrecruit_remnant", f"Category A (inappropriate): {cat_a_total} instances")
    report.add_finding("forrecruit_remnant", f"Category C (brand bias): {cat_c_total} instances")

def check_path_accuracy(report, skills):
    """Criterion 4: Path Reference Accuracy (20 points)"""
    print("\n=== Checking Path Accuracy ===")

    valid_paths = 0
    broken_paths = 0
    total_refs = 0

    for skill in skills:
        skill_path = SKILLS_DIR / skill / "SKILL.md"
        content = skill_path.read_text()

        # Find all @ references
        refs = re.findall(r'@([^\s\n]+)', content)
        total_refs += len(refs)

        for ref in refs:
            # Check if path exists (convert to absolute path)
            if ref.startswith('Stock/'):
                abs_path = Path(f"/Users/yuichi/AIPM/aipm_v0/{ref}")
            elif ref.startswith('aipm_v0/'):
                abs_path = Path(f"/Users/yuichi/AIPM/{ref}")
            else:
                abs_path = Path(ref)

            if abs_path.exists():
                valid_paths += 1
            else:
                broken_paths += 1
                report.add_issue("P1", skill, f"Broken path reference: {ref}")

    # Calculate score
    if total_refs > 0:
        accuracy_rate = valid_paths / total_refs
        report.scores["path_accuracy"] = accuracy_rate * 20
    else:
        report.scores["path_accuracy"] = 20  # No refs = no broken refs

    report.add_finding("path_accuracy", f"Valid path references: {valid_paths}/{total_refs}")
    report.add_finding("path_accuracy", f"Broken path references: {broken_paths}")

def check_vc_criteria(report, skills):
    """Criterion 5: VC Criteria Reflection (10 points)"""
    print("\n=== Checking VC Criteria ===")

    skills_with_vc_criteria = 0

    for skill in skills:
        skill_path = SKILLS_DIR / skill / "SKILL.md"
        content = skill_path.read_text()

        # Check if at least 2 VC criteria patterns are present
        criteria_found = []
        for pattern in VC_CRITERIA_PATTERNS:
            if re.search(pattern, content):
                criteria_found.append(pattern)

        if len(criteria_found) >= 2:
            skills_with_vc_criteria += 1
        else:
            report.add_issue("P2", skill, f"Insufficient VC criteria (found {len(criteria_found)}/2+)")

    # Calculate score
    report.scores["vc_criteria"] = (skills_with_vc_criteria / len(skills)) * 10
    report.add_finding("vc_criteria", f"Skills with VC criteria: {skills_with_vc_criteria}/{len(skills)}")

def generate_report(report):
    """Generate markdown report"""
    total_score = report.calculate_total()
    initial_score = 16.4
    improvement = total_score - initial_score

    output = f"""# ForStartup Edition Final Quality Evaluation Report

## Overall Score: {total_score:.1f}/100

## Detailed Breakdown

### 1. File Integrity: {report.scores['file_integrity']:.1f}/30
"""
    for finding in report.findings['file_integrity']:
        output += f"- {finding}\n"

    output += f"""
### 2. Metadata Completeness: {report.scores['metadata_completeness']:.1f}/20
"""
    for finding in report.findings['metadata_completeness']:
        output += f"- {finding}\n"

    output += f"""
### 3. ForRecruit Remnant Removal: {report.scores['forrecruit_remnant']:.1f}/20
"""
    for finding in report.findings['forrecruit_remnant']:
        output += f"- {finding}\n"

    output += f"""
### 4. Path Reference Accuracy: {report.scores['path_accuracy']:.1f}/20
"""
    for finding in report.findings['path_accuracy']:
        output += f"- {finding}\n"

    output += f"""
### 5. VC Criteria Reflection: {report.scores['vc_criteria']:.1f}/10
"""
    for finding in report.findings['vc_criteria']:
        output += f"- {finding}\n"

    output += f"""
## Improvement Summary
- Initial score (post bug fix): {initial_score}/100
- Final score: {total_score:.1f}/100
- Improvement: +{improvement:.1f} points ({(improvement/initial_score)*100:.1f}% increase)

## Remaining Issues

"""

    if report.issues['P0']:
        output += "### P0 Issues (Critical)\n"
        for issue in report.issues['P0']:
            output += f"- {issue}\n"
        output += "\n"

    if report.issues['P1']:
        output += "### P1 Issues (High Priority)\n"
        for issue in report.issues['P1']:
            output += f"- {issue}\n"
        output += "\n"

    if report.issues['P2']:
        output += "### P2 Issues (Medium Priority)\n"
        for issue in report.issues['P2']:
            output += f"- {issue}\n"
        output += "\n"

    if not any(report.issues.values()):
        output += "**No remaining issues detected!**\n\n"

    output += """## Recommendations

"""

    if total_score >= 90:
        output += "**Excellent quality!** ForStartup Edition is production-ready.\n\n"
        output += "- Consider final user acceptance testing\n"
        output += "- Prepare deployment documentation\n"
    elif total_score >= 70:
        output += "**Good quality.** Address remaining P0/P1 issues before release.\n\n"
        output += "- Fix all P0 issues immediately\n"
        output += "- Plan P1 fixes for next sprint\n"
    else:
        output += "**Needs improvement.** Significant work required.\n\n"
        output += "- Prioritize P0 and P1 issues\n"
        output += "- Consider additional QA cycle\n"

    output += """
## Evaluation Methodology

This evaluation assessed all 30 ForStartup skills across 5 criteria:
1. **File Integrity** (30 pts): File existence, directory structure
2. **Metadata Completeness** (20 pts): YAML frontmatter quality
3. **ForRecruit Remnant Removal** (20 pts): Inappropriate references cleaned
4. **Path Reference Accuracy** (20 pts): Valid knowledge base references
5. **VC Criteria Reflection** (10 pts): Investment criteria presence

Total possible: 100 points

---
*Generated on: 2026-01-03*
*Evaluation script: evaluate_forstartup_final.py*
"""

    return output

def main():
    print("ForStartup Edition Final Quality Evaluation")
    print("=" * 60)

    report = EvaluationReport()

    # Run evaluations
    skills = check_file_integrity(report)
    check_metadata_completeness(report, skills)
    check_forrecruit_remnants(report, skills)
    check_path_accuracy(report, skills)
    check_vc_criteria(report, skills)

    # Generate report
    markdown_report = generate_report(report)

    # Save report
    output_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/FINAL_QUALITY_REPORT.md")
    output_path.write_text(markdown_report)

    print(f"\n{'=' * 60}")
    print(f"Final Score: {report.calculate_total():.1f}/100")
    print(f"Report saved to: {output_path}")
    print(f"{'=' * 60}\n")

    # Print summary
    print(markdown_report)

if __name__ == "__main__":
    main()
