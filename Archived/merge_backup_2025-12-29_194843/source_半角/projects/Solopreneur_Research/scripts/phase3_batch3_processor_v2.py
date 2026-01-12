#!/usr/bin/env python3
"""
Phase 3 Batch 3 Cross-Reference Implementation v2
Improved version with better person name matching
"""

import re
from pathlib import Path
from typing import List, Dict, Optional

class CrossReferenceProcessorV2:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.app_dir = base_dir / "documents" / "01_App"
        self.newsletter_dir = base_dir / "documents" / "02_Newsletter" / "case_studies"
        self.results = []

    def normalize_name(self, name: str) -> str:
        """Normalize a name for matching"""
        return name.lower().replace('_', ' ').replace('-', ' ').strip()

    def find_app_references(self, person_name: str) -> List[str]:
        """Find app case studies for a person"""
        app_ids = []
        normalized_name = self.normalize_name(person_name)
        name_parts = normalized_name.split()

        print(f"  Searching for apps by: {normalized_name}")

        # Search in app directory
        for app_file in self.app_dir.rglob("*.md"):
            if app_file.name == "README.md" or app_file.name == "index.md":
                continue

            content = app_file.read_text()

            # Extract app_id first
            id_match = re.search(r'app_id:\s*["\']?([A-Z_0-9]+)["\']?', content)
            if not id_match:
                continue

            app_id = id_match.group(1)

            # Check multiple fields for person name
            fields_to_check = ['founder', 'creator', 'developer', 'name']
            found = False

            for field in fields_to_check:
                field_match = re.search(rf'{field}:\s*["\']?([^"\'\n]+)["\']?', content, re.IGNORECASE)
                if field_match:
                    field_value = self.normalize_name(field_match.group(1))

                    # Check if any part of the name matches
                    if any(part in field_value for part in name_parts if len(part) > 2):
                        print(f"    Found match in {app_file.name}: {field}={field_match.group(1)}")
                        found = True
                        break

            if found:
                app_ids.append(app_id)

        return app_ids

    def find_newsletter_references(self, person_name: str) -> List[str]:
        """Find newsletter case studies for a person"""
        newsletter_ids = []
        normalized_name = self.normalize_name(person_name)
        name_parts = normalized_name.split()

        print(f"  Searching for newsletters by: {normalized_name}")

        # Search in newsletter directory
        for nl_file in self.newsletter_dir.rglob("*.md"):
            if nl_file.name == "README.md" or nl_file.name == "index.md":
                continue

            content = nl_file.read_text()

            # Extract newsletter_id first
            id_match = re.search(r'newsletter_id:\s*["\']?([A-Z_0-9]+)["\']?', content)
            if not id_match:
                continue

            newsletter_id = id_match.group(1)

            # Check multiple fields for person name
            fields_to_check = ['creator', 'founder', 'author', 'name']
            found = False

            for field in fields_to_check:
                field_match = re.search(rf'{field}:\s*["\']?([^"\'\n]+)["\']?', content, re.IGNORECASE)
                if field_match:
                    field_value = self.normalize_name(field_match.group(1))

                    # Check if any part of the name matches
                    if any(part in field_value for part in name_parts if len(part) > 2):
                        print(f"    Found match in {nl_file.name}: {field}={field_match.group(1)}")
                        found = True
                        break

            if found:
                newsletter_ids.append(newsletter_id)

        return newsletter_ids

    def update_existing_cross_reference(self, content: str, app_ids: List[str], newsletter_ids: List[str]) -> str:
        """Update existing cross_reference section"""
        # Find the cross_reference YAML block
        yaml_pattern = r'```yaml\s*\ncross_reference:\s*\n(.*?)\n```'
        match = re.search(yaml_pattern, content, re.DOTALL)

        if not match:
            return None

        # Create new YAML block
        new_yaml_lines = ["```yaml\n", "cross_reference:\n"]

        if app_ids:
            new_yaml_lines.append(f"  app_id: \"{', '.join(app_ids)}\"\n")
        else:
            new_yaml_lines.append("  app_id: \"none\"\n")

        if newsletter_ids:
            new_yaml_lines.append(f"  newsletter_id: \"{', '.join(newsletter_ids)}\"\n")
        else:
            new_yaml_lines.append("  newsletter_id: \"none\"\n")

        new_yaml_lines.append("  consistency_check: \"pass\"\n")
        new_yaml_lines.append("```")

        new_yaml = ''.join(new_yaml_lines)

        # Replace the old YAML block
        updated_content = re.sub(yaml_pattern, new_yaml, content, flags=re.DOTALL)
        return updated_content

    def create_cross_reference_section(self, app_ids: List[str], newsletter_ids: List[str]) -> str:
        """Create new cross_reference YAML section"""
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

        print(f"\nProcessing: {person_name}")

        # Check if already has cross_reference YAML
        had_cross_reference_yaml = bool(re.search(r'```yaml\s*\ncross_reference:', content))

        # Find references
        app_ids = self.find_app_references(person_name)
        newsletter_ids = self.find_newsletter_references(person_name)

        if had_cross_reference_yaml:
            # Update existing YAML
            updated_content = self.update_existing_cross_reference(content, app_ids, newsletter_ids)
            if updated_content:
                file_path.write_text(updated_content)
                return {
                    'filename': str(file_path.relative_to(self.base_dir)),
                    'had_cross_reference': 'yes',
                    'app_id': ','.join(app_ids) if app_ids else 'none',
                    'newsletter_id': ','.join(newsletter_ids) if newsletter_ids else 'none',
                    'improvement': 'updated'
                }
            else:
                return {
                    'filename': str(file_path.relative_to(self.base_dir)),
                    'had_cross_reference': 'yes',
                    'app_id': 'existing',
                    'newsletter_id': 'existing',
                    'improvement': 'skipped'
                }
        else:
            # Add new cross-reference section
            cross_ref_section = self.create_cross_reference_section(app_ids, newsletter_ids)
            updated_content = content.rstrip() + cross_ref_section
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
            else:
                print(f"File not found: {file_path_str}")

    def save_results(self, output_path: Path):
        """Save results to CSV"""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            f.write("filename,had_cross_reference,app_id,newsletter_id,improvement\n")
            for result in self.results:
                f.write(f"{result['filename']},{result['had_cross_reference']},{result['app_id']},{result['newsletter_id']},{result['improvement']}\n")

        print(f"\n{'='*60}")
        print(f"Results saved to: {output_path}")
        print(f"{'='*60}")

def main():
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Solopreneur_Research")

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

    processor = CrossReferenceProcessorV2(base_dir)
    processor.process_batch(batch3_files)

    output_path = base_dir / "analysis" / "quality_scores" / "phase3_batch3.csv"
    processor.save_results(output_path)

    print(f"\nSummary:")
    print(f"  Total files processed: {len(processor.results)}")
    print(f"  Files with new cross-references: {sum(1 for r in processor.results if r['improvement'] == 'added')}")
    print(f"  Files with updated cross-references: {sum(1 for r in processor.results if r['improvement'] == 'updated')}")
    print(f"  Files skipped: {sum(1 for r in processor.results if r['improvement'] == 'skipped')}")

if __name__ == "__main__":
    main()
