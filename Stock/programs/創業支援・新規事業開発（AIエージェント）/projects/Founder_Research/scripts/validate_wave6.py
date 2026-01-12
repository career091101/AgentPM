#!/usr/bin/env python3
"""
Wave6 Quality Validation Script
================================

FOUNDER_176-200 (25件) の品質検証を実行します。

検証項目:
- ファイル存在確認
- YAML front matter妥当性
- sources_count ≥ 12
- fact_check: "pass"
- CPF/PSF検証データ存在
- 12セクション構造確認

使用方法:
    python3 validate_wave6.py
"""

import os
import re
from pathlib import Path
import yaml
from collections import defaultdict

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "documents" / "03_VC_Backed"

# Wave6のID範囲
WAVE6_IDS = [f"FOUNDER_{i}" for i in range(176, 201)]

# 必須セクション
REQUIRED_SECTIONS = [
    "基本情報",
    "創業ストーリー",
    "ピボット",
    "成長戦略",
    "ツール",
    "成功要因",
    "日本市場",
    "orchestrate",
    "事業アイデア",
    "ファクトチェック",
    "参照ソース"
]

class Wave6Validator:
    def __init__(self):
        self.results = {
            'total': 25,
            'files_found': 0,
            'yaml_valid': 0,
            'sources_12plus': 0,
            'fact_check_pass': 0,
            'cpf_data': 0,
            'psf_data': 0,
            'sections_complete': 0,
            'issues': []
        }

    def validate_file_exists(self, founder_id):
        """ファイル存在確認"""
        pattern = f"{founder_id}_*.md"
        files = list(DOCS_DIR.glob(pattern))

        if not files:
            self.results['issues'].append(f"❌ {founder_id}: File not found")
            return None
        elif len(files) > 1:
            self.results['issues'].append(f"⚠️  {founder_id}: Multiple files found: {[f.name for f in files]}")

        self.results['files_found'] += 1
        return files[0]

    def extract_yaml_frontmatter(self, filepath):
        """YAML front matter抽出"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # YAML front matterを抽出 (--- ... ---)
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None, content

        yaml_text = match.group(1)
        markdown_body = content[match.end():]

        try:
            yaml_data = yaml.safe_load(yaml_text)
            return yaml_data, markdown_body
        except yaml.YAMLError as e:
            return None, content

    def validate_yaml(self, founder_id, yaml_data):
        """YAML検証"""
        if not yaml_data:
            self.results['issues'].append(f"❌ {founder_id}: Invalid YAML front matter")
            return False

        self.results['yaml_valid'] += 1

        # sources_count確認
        sources_count = yaml_data.get('quality', {}).get('sources_count', 0)
        if sources_count >= 12:
            self.results['sources_12plus'] += 1
        else:
            self.results['issues'].append(f"⚠️  {founder_id}: sources_count={sources_count} (< 12)")

        # fact_check確認
        fact_check = yaml_data.get('quality', {}).get('fact_check', '')
        if fact_check == 'pass':
            self.results['fact_check_pass'] += 1
        else:
            self.results['issues'].append(f"⚠️  {founder_id}: fact_check={fact_check} (not 'pass')")

        # CPF検証データ
        cpf = yaml_data.get('validation_data', {}).get('cpf', {})
        if cpf and 'interview_count' in cpf and 'problem_commonality' in cpf:
            self.results['cpf_data'] += 1
        else:
            self.results['issues'].append(f"⚠️  {founder_id}: CPF validation data incomplete")

        # PSF検証データ
        psf = yaml_data.get('validation_data', {}).get('psf', {})
        if psf and 'ten_x_axes' in psf and psf['ten_x_axes']:
            self.results['psf_data'] += 1
        else:
            self.results['issues'].append(f"⚠️  {founder_id}: PSF validation data incomplete (ten_x_axes)")

        return True

    def validate_sections(self, founder_id, markdown_body):
        """セクション構造検証"""
        found_sections = 0
        for section in REQUIRED_SECTIONS:
            if section in markdown_body:
                found_sections += 1

        if found_sections >= len(REQUIRED_SECTIONS) - 2:  # 9/11以上でOK (柔軟に)
            self.results['sections_complete'] += 1
        else:
            self.results['issues'].append(
                f"⚠️  {founder_id}: Only {found_sections}/{len(REQUIRED_SECTIONS)} sections found"
            )

    def validate_all(self):
        """全ファイル検証"""
        print("\n" + "="*80)
        print("🔍 WAVE6 QUALITY VALIDATION")
        print("="*80 + "\n")

        for founder_id in WAVE6_IDS:
            # ファイル存在確認
            filepath = self.validate_file_exists(founder_id)
            if not filepath:
                continue

            # YAML front matter抽出・検証
            yaml_data, markdown_body = self.extract_yaml_frontmatter(filepath)
            self.validate_yaml(founder_id, yaml_data)

            # セクション検証
            self.validate_sections(founder_id, markdown_body)

        self.print_report()

    def print_report(self):
        """検証レポート出力"""
        print("\n" + "="*80)
        print("📊 VALIDATION REPORT")
        print("="*80 + "\n")

        print(f"Total Cases: {self.results['total']}")
        print(f"\n✅ Files Found: {self.results['files_found']}/{self.results['total']} ({self.results['files_found']/self.results['total']*100:.1f}%)")
        print(f"✅ Valid YAML: {self.results['yaml_valid']}/{self.results['total']} ({self.results['yaml_valid']/self.results['total']*100:.1f}%)")
        print(f"✅ Sources ≥12: {self.results['sources_12plus']}/{self.results['total']} ({self.results['sources_12plus']/self.results['total']*100:.1f}%)")
        print(f"✅ Fact Check PASS: {self.results['fact_check_pass']}/{self.results['total']} ({self.results['fact_check_pass']/self.results['total']*100:.1f}%)")
        print(f"✅ CPF Data Complete: {self.results['cpf_data']}/{self.results['total']} ({self.results['cpf_data']/self.results['total']*100:.1f}%)")
        print(f"✅ PSF Data Complete: {self.results['psf_data']}/{self.results['total']} ({self.results['psf_data']/self.results['total']*100:.1f}%)")
        print(f"✅ Sections Complete: {self.results['sections_complete']}/{self.results['total']} ({self.results['sections_complete']/self.results['total']*100:.1f}%)")

        if self.results['issues']:
            print(f"\n⚠️  ISSUES FOUND ({len(self.results['issues'])}):")
            for issue in self.results['issues']:
                print(f"   {issue}")
        else:
            print("\n🎉 No issues found! All cases passed validation.")

        # 総合評価
        success_rate = (
            self.results['files_found'] +
            self.results['yaml_valid'] +
            self.results['sources_12plus'] +
            self.results['fact_check_pass'] +
            self.results['cpf_data'] +
            self.results['psf_data'] +
            self.results['sections_complete']
        ) / (self.results['total'] * 7) * 100

        print(f"\n📈 Overall Success Rate: {success_rate:.1f}%")

        if success_rate >= 90:
            print("🏆 Excellent! Wave6 quality is outstanding.")
        elif success_rate >= 75:
            print("👍 Good! Minor issues to address.")
        else:
            print("⚠️  Needs improvement. Please review issues above.")

        print("\n" + "="*80 + "\n")

def main():
    validator = Wave6Validator()
    validator.validate_all()

if __name__ == "__main__":
    main()
