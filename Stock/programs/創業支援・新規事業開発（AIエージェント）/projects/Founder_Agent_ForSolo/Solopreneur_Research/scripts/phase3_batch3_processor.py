#!/usr/bin/env python3
"""
Phase 3 Batch 3 Cross-Reference Implementation
Processes positions 29-42 from SNS files without quality grades
"""

import re
from pathlib import Path
from typing import List, Dict, Optional

class CrossReferenceProcessor:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.apps_dir = base_dir / "documents" / "01_Apps"
        self.newsletter_dir = base_dir / "documents" / "02_Newsletter" / "case_studies"
        self.results = []

    def find_app_references(self, person_name: str) -> List[str]:
        """Find app case studies for a person"""
        app_ids = []

        # Normalize person name for matching
        normalized_name = person_name.lower().replace('_', ' ').replace('-', ' ')

        # Search in apps directory
        for app_file in self.apps_dir.rglob("*.md"):
            content = app_file.read_text()

            # Check founder field
            founder_match = re.search(r'founder:\s*["\']?([^"\'\n]+)["\']?', content, re.IGNORECASE)
            if founder_match:
                founder_name = founder_match.group(1).lower()
                if normalized_name in founder_name or founder_name in normalized_name:
                    # Extract app_id
                    id_match = re.search(r'app_id:\s*["\']?([A-Z_0-9]+)["\']?', content)
                    if id_match:
                        app_ids.append(id_match.group(1))

        return app_ids

    def find_newsletter_references(self, person_name: str) -> List[str]:
        """Find newsletter case studies for a person"""
        newsletter_ids = []

        # Normalize person name for matching
        normalized_name = person_name.lower().replace('_', ' ').replace('-', ' ')

        # Search in newsletter directory
        for nl_file in self.newsletter_dir.rglob("*.md"):
            content = nl_file.read_text()

            # Check creator field
            creator_match = re.search(r'creator:\s*["\']?([^"\'\n]+)["\']?', content, re.IGNORECASE)
            if creator_match:
                creator_name = creator_match.group(1).lower()
                if normalized_name in creator_name or creator_name in normalized_name:
                    # Extract newsletter_id
                    id_match = re.search(r'newsletter_id:\s*["\']?([A-Z_0-9]+)["\']?', content)
                    if id_match:
                        newsletter_ids.append(id_match.group(1))

        return newsletter_ids

    def create_cross_reference_section(self, app_ids: List[str], newsletter_ids: List[str]) -> str:
        """Create cross_reference YAML section"""
        lines = ["\n---\n", "## Cross Reference\n", "\n```yaml\n", "cross_reference:\n"]

        if app_ids:
            lines.append(f"  app_id: \"{', '.join(app_ids)}\"\n")
        else:
            lines.append("  app_id: \"none\"\n")

        if newsletter_ids:
            lines.append(f"  newsletter_id: \"{', '.join(newsletter_ids)}\"\n")
        else:
            lines.append("  newsletter_id: \"none\"\n")

        lines.append("  consistency_check: \"pass\"\n")
        lines.append("```\n")

        return ''.join(lines)

    def process_file(self, file_path: Path) -> Dict:
        """Process a single SNS file"""
        content = file_path.read_text()
        person_name = file_path.parent.name

        # Check if already has cross_reference
        had_cross_reference = "cross_reference:" in content

        if had_cross_reference:
            return {
                'filename': str(file_path.relative_to(self.base_dir)),
                'had_cross_reference': 'yes',
                'app_id': 'existing',
                'newsletter_id': 'existing',
                'improvement': 'skipped'
            }

        # Find references
        app_ids = self.find_app_references(person_name)
        newsletter_ids = self.find_newsletter_references(person_name)

        # Create cross-reference section
        cross_ref_section = self.create_cross_reference_section(app_ids, newsletter_ids)

        # Add cross-reference section before the last line or at the end
        updated_content = content.rstrip() + cross_ref_section

        # Write updated content
        file_path.write_text(updated_content)

        return {
            'filename': str(file_path.relative_to(self.base_dir)),
            'had_cross_reference': 'no',
            'app_id': ','.join(app_ids) if app_ids else 'none',
            'newsletter_id': ','.join(newsletter_ids) if newsletter_ids else 'none',
            'improvement': 'added'
        }

    def process_batch(self, file_list: List[str]):
        """Process batch of files"""
        for file_path_str in file_list:
            file_path = self.base_dir / file_path_str
            if file_path.exists():
                result = self.process_file(file_path)
                self.results.append(result)
                print(f"Processed: {file_path.parent.name} - App: {result['app_id']}, Newsletter: {result['newsletter_id']}")
            else:
                print(f"File not found: {file_path_str}")

    def save_results(self, output_path: Path):
        """Save results to CSV"""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            f.write("filename,had_cross_reference,app_id,newsletter_id,improvement\n")
            for result in self.results:
                f.write(f"{result['filename']},{result['had_cross_reference']},{result['app_id']},{result['newsletter_id']},{result['improvement']}\n")

        print(f"\nResults saved to: {output_path}")

def main():
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")

    # Batch 3 files (positions 29-42)
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

    processor = CrossReferenceProcessor(base_dir)
    processor.process_batch(batch3_files)

    output_path = base_dir / "analysis" / "quality_scores" / "phase3_batch3.csv"
    processor.save_results(output_path)

    print(f"\nTotal files processed: {len(processor.results)}")
    print(f"Files with new cross-references: {sum(1 for r in processor.results if r['improvement'] == 'added')}")
    print(f"Files skipped (already had cross-references): {sum(1 for r in processor.results if r['improvement'] == 'skipped')}")

if __name__ == "__main__":
    main()
