#!/usr/bin/env python3
"""
ForStartup Skills Customization Script
Applies systematic replacements to convert ForRecruit skills to ForStartup

Usage:
    python scripts/customize_forstartup_skills.py
"""

import re
from pathlib import Path
from typing import Dict, Tuple

# Systematic replacements mapping
REPLACEMENTS = {
    "ForRecruit": "ForStartup",
    "for-recruit": "for-startup",
    "for_recruit": "for_startup",
    "Ring制度": "Seed調達",
    "Ring 1": "Seed Stage",
    "Ring 2": "Series A Stage",
    "Ring 3": "Series B Stage",
    "Recruit_Product_Research": "Founder_Research",
    "社内承認": "VC承認",
    "社内ベータテスター": "早期ユーザー（early adopters）",
    "社内実績": "トラクション実績",
    "社内顧客": "早期顧客",
    "社内リソース": "スタートアップリソース",
    "社内人材": "創業チーム",
    "社内公募": "共同創業者募集",
    "営業網": "セールスチャネル",
    "既存顧客基盤": "コミュニティ基盤",
    "ホットペッパー": "プロダクト主導成長",
    "リクルートブランド": "創業者ブランド",
    "Ring 1承認": "Seed調達承認",
    "Ring 2承認": "Series A調達承認",
    "Ring 3承認": "Series B調達承認",
    # Numeric criteria (critical for VC standards)
    "CPF 50%": "CPF 70%",
    "TAM 50億円": "TAM $1B",
    "TAM $100M": "TAM $1B",
    "成長率 5%/年": "成長率 20%/月",
    "月次10%": "月次20%",
    "10倍優位性 2軸": "10倍優位性 3軸",
    "LTV/CAC 3.0": "LTV/CAC 5.0",
    "CAC回収期間 18ヶ月": "CAC回収期間 12ヶ月",
    # Project paths
    "Founder_Agent_ForRecruit": "Founder_Agent_ForStartup",
    "programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit": "programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup",
    # Example companies (contextual - may need manual review)
    "Airレジ": "Stripe",
    "Geppo": "Notion",
    "Airペイ": "Figma",
    "Airキャッシュ": "Slack",
    "SUUMO": "Airbnb",
    "じゃらん": "Booking.com",
    "ホットペッパービューティー": "Calendly",
    "スタディサプリ": "Coursera",
}

SKILLS_DIR = Path(__file__).parent.parent / ".claude" / "skills" / "for_startup"
TARGET_SKILLS = [
    "design-pricing",
    "analyze-aarrr",
    "build-flywheel",
    "build-lp",
    "build-synergy-map",
    "inventory-internal-resources",
    "validate-market-timing",
    "design-exit-strategy",
    "analyze-competitive-moat",
    "validate-ring-criteria",
    "orchestrate-review-loop",
    "build-approval-deck",
]


def apply_replacements(file_path: Path) -> Tuple[int, Dict[str, int]]:
    """
    Apply systematic replacements to a file

    Returns:
        Tuple of (total_count, replacement_breakdown)
    """
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    replacement_counts = {}

    for old, new in REPLACEMENTS.items():
        if old in content:
            occurrences = content.count(old)
            content = content.replace(old, new)
            replacement_counts[old] = occurrences

    if content != original_content:
        # Create backup before writing
        backup_path = file_path.with_suffix('.md.backup')
        backup_path.write_text(original_content, encoding='utf-8')

        # Write updated content
        file_path.write_text(content, encoding='utf-8')

    total_count = sum(replacement_counts.values())
    return total_count, replacement_counts


def validate_replacements(file_path: Path) -> list:
    """
    Validate that no ForRecruit remnants remain

    Returns:
        List of validation issues
    """
    content = file_path.read_text(encoding='utf-8')
    issues = []

    # Check for ForRecruit patterns
    if re.search(r'\bForRecruit\b', content):
        issues.append("Found remaining 'ForRecruit' references")

    if re.search(r'\bfor-recruit\b', content):
        issues.append("Found remaining 'for-recruit' references")

    if re.search(r'\bRing制度\b', content):
        issues.append("Found remaining 'Ring制度' references")

    if re.search(r'\bRecruit_Product_Research\b', content):
        issues.append("Found remaining 'Recruit_Product_Research' references")

    # Check numeric criteria updated
    if 'CPF 50%' in content:
        issues.append("CPF threshold still at 50% (should be 70%)")

    if 'LTV/CAC 3.0' in content:
        issues.append("LTV/CAC threshold still at 3.0 (should be 5.0)")

    return issues


def main():
    print("=" * 80)
    print("ForStartup Skills Customization - Phase 1: Automated Replacements")
    print("=" * 80)
    print()

    if not SKILLS_DIR.exists():
        print(f"❌ ERROR: Skills directory not found: {SKILLS_DIR}")
        return

    total_replacements = 0
    skill_reports = []

    for skill in TARGET_SKILLS:
        skill_file = SKILLS_DIR / skill / "SKILL.md"

        if not skill_file.exists():
            print(f"⚠️  {skill}: File not found - skipping")
            continue

        # Apply replacements
        count, breakdown = apply_replacements(skill_file)
        total_replacements += count

        # Validate
        issues = validate_replacements(skill_file)

        # Report
        status = "✅" if not issues else "⚠️ "
        print(f"{status} {skill:30s} | {count:3d} replacements")

        if breakdown:
            print(f"   Top replacements:")
            top_5 = sorted(breakdown.items(), key=lambda x: x[1], reverse=True)[:5]
            for old, cnt in top_5:
                print(f"     - {old:30s} → {cnt:2d}x")

        if issues:
            print(f"   ⚠️  Validation issues:")
            for issue in issues:
                print(f"     - {issue}")

        skill_reports.append({
            "skill": skill,
            "count": count,
            "issues": issues,
            "breakdown": breakdown
        })
        print()

    print("=" * 80)
    print(f"🎉 Phase 1 Complete: {total_replacements} total replacements across {len(skill_reports)} skills")
    print("=" * 80)
    print()

    # Summary report
    print("Summary:")
    print(f"  - Skills processed: {len(skill_reports)}")
    print(f"  - Total replacements: {total_replacements}")
    print(f"  - Skills with issues: {sum(1 for r in skill_reports if r['issues'])}")
    print()

    if any(r['issues'] for r in skill_reports):
        print("⚠️  Next Steps:")
        print("   1. Review validation issues above")
        print("   2. Manually fix remaining issues")
        print("   3. Proceed to Phase 2: Manual content customization")
    else:
        print("✅ All automated replacements completed successfully!")
        print("   → Proceed to Phase 2: Manual content customization")

    print()
    print("Backup files created: {skill}/SKILL.md.backup")


if __name__ == "__main__":
    main()
