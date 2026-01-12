#!/usr/bin/env python3
"""
Document Validation for IPO_Global Case Studies
Validates generated documents against quality standards
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Any, List, Tuple


class DocumentValidator:
    """Validate IPO_Global case study documents"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "documents" / "05_IPO_Global"

    def validate_document(self, file_path: Path) -> Tuple[bool, Dict[str, Any]]:
        """
        Validate a single document

        Args:
            file_path: Path to document

        Returns:
            Tuple of (is_valid, validation_results)
        """
        if not file_path.exists():
            return False, {'error': 'File does not exist'}

        content = file_path.read_text(encoding='utf-8')

        checks = {}

        # 1. YAML validation
        checks['yaml_valid'] = self._validate_yaml(content)

        # 2. CPF data validation
        checks['cpf_complete'] = self._validate_cpf(content)

        # 3. PSF data validation
        checks['psf_complete'] = self._validate_psf(content)

        # 4. Section validation
        checks['sections_complete'] = self._validate_sections(content)

        # 5. Source validation
        checks['sources_adequate'] = self._validate_sources(content)

        # 6. Fact check validation
        checks['fact_check_pass'] = self._validate_fact_check(content)

        # 7. File size validation
        checks['file_size_ok'] = file_path.stat().st_size >= 18000  # 18KB minimum

        # Overall validation
        is_valid = all(checks.values())

        return is_valid, checks

    def _validate_yaml(self, content: str) -> bool:
        """Validate YAML front matter"""
        try:
            # Extract YAML front matter
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False

            yaml_content = match.group(1)
            data = yaml.safe_load(yaml_content)

            # Check required fields
            required_fields = [
                'id', 'title', 'category', 'tier', 'type',
                'founder', 'company', 'funding', 'outcome',
                'validation_data', 'quality'
            ]

            for field in required_fields:
                if field not in data:
                    return False

            return True

        except Exception:
            return False

    def _validate_cpf(self, content: str) -> bool:
        """Validate CPF data completeness"""
        try:
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False

            data = yaml.safe_load(match.group(1))

            cpf = data.get('validation_data', {}).get('cpf', {})

            # Check interview_count >= 10 (or null)
            interview_count = cpf.get('interview_count')
            if interview_count is not None and interview_count < 10:
                return False

            # Check problem_commonality exists
            if 'problem_commonality' not in cpf:
                return False

            # Check wtp_confirmed exists
            if 'wtp_confirmed' not in cpf:
                return False

            # Check urgency_score exists
            if 'urgency_score' not in cpf:
                return False

            return True

        except Exception:
            return False

    def _validate_psf(self, content: str) -> bool:
        """Validate PSF data completeness"""
        try:
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False

            data = yaml.safe_load(match.group(1))

            psf = data.get('validation_data', {}).get('psf', {})

            # Check ten_x_axes has at least 2 axes
            ten_x_axes = psf.get('ten_x_axes', [])
            if len(ten_x_axes) < 2:
                return False

            # Check mvp_type exists
            if 'mvp_type' not in psf:
                return False

            # Check uvp_clarity exists
            if 'uvp_clarity' not in psf:
                return False

            return True

        except Exception:
            return False

    def _validate_sections(self, content: str) -> bool:
        """Validate document has all required sections"""
        required_sections = [
            '基本情報',
            '創業の経緯',
            'ソリューション',
            '市場環境',
            '成長プロセス',
            '資金調達',
            'IPO情報',
            '技術',
            'チーム',
            '課題',
            'データ・KPI',
            '追加情報'
        ]

        found_sections = 0
        for section in required_sections:
            if section in content:
                found_sections += 1

        # At least 10 out of 12 sections
        return found_sections >= 10

    def _validate_sources(self, content: str) -> bool:
        """Validate source count"""
        try:
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False

            data = yaml.safe_load(match.group(1))

            sources_count = data.get('quality', {}).get('sources_count', 0)

            return sources_count >= 12

        except Exception:
            return False

    def _validate_fact_check(self, content: str) -> bool:
        """Validate fact check status"""
        try:
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False

            data = yaml.safe_load(match.group(1))

            fact_check = data.get('quality', {}).get('fact_check', '')

            return fact_check == 'pass'

        except Exception:
            return False

    def validate_all(self) -> Dict[str, Any]:
        """
        Validate all documents in 05_IPO_Global

        Returns:
            Dictionary with validation results
        """
        results = {
            'total': 0,
            'valid': 0,
            'invalid': 0,
            'documents': {}
        }

        if not self.docs_dir.exists():
            return results

        for file_path in sorted(self.docs_dir.glob("FOUNDER_*.md")):
            is_valid, checks = self.validate_document(file_path)

            results['total'] += 1
            if is_valid:
                results['valid'] += 1
            else:
                results['invalid'] += 1

            results['documents'][file_path.name] = {
                'valid': is_valid,
                'checks': checks
            }

        return results

    def print_validation_report(self, results: Dict[str, Any]):
        """Print validation report"""
        print("\n" + "=" * 80)
        print("Document Validation Report")
        print("=" * 80)
        print(f"Total Documents: {results['total']}")
        print(f"Valid: {results['valid']} ({results['valid']/results['total']*100:.1f}%)")
        print(f"Invalid: {results['invalid']}")
        print()

        if results['invalid'] > 0:
            print("Invalid Documents:")
            for doc_name, doc_result in results['documents'].items():
                if not doc_result['valid']:
                    print(f"\n  {doc_name}:")
                    for check, passed in doc_result['checks'].items():
                        status = "✓" if passed else "✗"
                        print(f"    {status} {check}")

        print("=" * 80 + "\n")


if __name__ == '__main__':
    # Test validator
    project_root = Path(__file__).parent.parent
    validator = DocumentValidator(project_root)

    print("Testing DocumentValidator...")
    print()

    # Validate all
    results = validator.validate_all()
    validator.print_validation_report(results)

    print(f"\nValidation completed: {results['valid']}/{results['total']} documents valid")
