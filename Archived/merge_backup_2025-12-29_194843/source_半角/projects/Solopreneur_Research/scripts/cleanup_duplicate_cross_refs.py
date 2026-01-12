#!/usr/bin/env python3
"""
Cleanup duplicate cross-reference sections
Consolidates old "Related Strategies" sections with new YAML blocks
"""

import re
from pathlib import Path

def cleanup_file(file_path: Path) -> bool:
    """Clean up duplicate cross-reference sections in a file"""
    content = file_path.read_text()

    # Check if there are duplicate cross-reference sections
    # Pattern 1: Old style without YAML
    old_pattern = r'##\s+\d+\.\s+cross_reference\s*\n+###\s+Related\s+(Strategies|Case Studies)\s*\n+(.*?)(?=---\n## Cross Reference|$)'
    # Pattern 2: New style with YAML at the end
    new_pattern = r'---\n## Cross Reference\s*\n+```yaml\s*\ncross_reference:\s*\n(.*?)```'

    old_match = re.search(old_pattern, content, re.DOTALL)
    new_match = re.search(new_pattern, content, re.DOTALL)

    if old_match and new_match:
        # Extract YAML data from new section
        yaml_content = new_match.group(0)

        # Remove the old section
        content = re.sub(old_pattern, '', content, flags=re.DOTALL)

        # Ensure the new YAML section stays (it should already be there)
        # Clean up any extra whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)

        # Write back
        file_path.write_text(content)
        return True

    return False

def main():
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Solopreneur_Research")

    batch3_files = [
        "documents/03_SNS/case_studies/catnose99/sns_analysis.md",
        "documents/03_SNS/case_studies/chase_jarvis/sns_analysis.md",
        "documents/03_SNS/case_studies/chris_do/sns_analysis.md",
        "documents/03_SNS/case_studies/chris_williamson/sns_analysis.md",
        "documents/03_SNS/case_studies/codie_sanchez/sns_analysis.md",
        "documents/03_SNS/case_studies/connor/sns_analysis.md",
        "documents/03_SNS/case_studies/courtland_allen/sns_analysis.md",
        "documents/03_SNS/case_studies/dagobert_renouf/sns_analysis.md",
        "documents/03_SNS/case_studies/damon_chen/sns_analysis.md",
        "documents/03_SNS/case_studies/dan_koe/sns_analysis.md",
        "documents/03_SNS/case_studies/daniel_bitton/sns_analysis.md",
        "documents/03_SNS/case_studies/daniel_nguyen/sns_analysis.md",
        "documents/03_SNS/case_studies/daniel_vassallo/sns_analysis.md",
        "documents/03_SNS/case_studies/danny_postma/sns_analysis.md",
    ]

    cleaned_count = 0
    for file_path_str in batch3_files:
        file_path = base_dir / file_path_str
        if file_path.exists():
            if cleanup_file(file_path):
                cleaned_count += 1
                print(f"Cleaned: {file_path.parent.name}")

    print(f"\nTotal files cleaned: {cleaned_count}")

if __name__ == "__main__":
    main()
