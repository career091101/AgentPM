#!/usr/bin/env python3
"""
ForStartup Skills Validation Script

このスクリプトは以下の検証を行います:
1. YAML フロントマター必須フィールドの検証
2. ForRecruit残骸の検出
3. ファイル構造の検証
4. Markdown基本構文の検証
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ValidationError:
    """検証エラー情報"""
    file: str
    message: str
    severity: str = "error"  # "error" or "warning"


@dataclass
class ValidationReport:
    """検証レポート"""
    timestamp: str
    errors: List[Dict]
    warnings: List[Dict]
    summary: Dict


class SkillValidator:
    """ForStartup Skillsの検証クラス"""

    # 必須フロントマターフィールド
    REQUIRED_FIELDS = [
        'trigger_keywords',
        'stage',
        'output_file',
        'dependencies'
    ]

    # 必須フィールドの型
    FIELD_TYPES = {
        'trigger_keywords': (list,),
        'stage': (str,),
        'output_file': (str,),
        'dependencies': (list,),
        'name': (str,),
        'description': (str,),
    }

    def __init__(self, base_dir: str = '.'):
        self.base_dir = Path(base_dir)
        self.skills_dir = self.base_dir / '.claude' / 'skills' / 'for_startup'
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def validate_all(self) -> bool:
        """全スキルファイルの検証を実行"""
        print(f"Validating ForStartup Skills in: {self.skills_dir}")

        if not self.skills_dir.exists():
            print(f"⚠️  Skills directory not found: {self.skills_dir}")
            return True  # ディレクトリがなければスキップ

        # SKILL.md ファイルを探す
        skill_files = list(self.skills_dir.glob('**/SKILL.md'))

        if not skill_files:
            print("⚠️  No SKILL.md files found")
            return True

        print(f"Found {len(skill_files)} SKILL.md files\n")

        for skill_file in skill_files:
            print(f"Validating: {skill_file.relative_to(self.base_dir)}")
            self._validate_skill_file(skill_file)

        # ForRecruit残骸をチェック
        print("\nChecking for ForRecruit remnants...")
        self._check_for_recruit_remnants()

        # レポート出力
        self._generate_report()

        return len(self.errors) == 0

    def _validate_skill_file(self, file_path: Path) -> None:
        """個別スキルファイルの検証"""
        try:
            content = file_path.read_text(encoding='utf-8')

            # フロントマターを抽出
            frontmatter, body = self._extract_frontmatter(content)

            if frontmatter is None:
                self.errors.append(ValidationError(
                    str(file_path.relative_to(self.base_dir)),
                    "YAML frontmatter not found or invalid",
                    "error"
                ))
                return

            # 必須フィールドを検証
            self._validate_required_fields(file_path, frontmatter)

            # フィールドの型を検証
            self._validate_field_types(file_path, frontmatter)

            # フロントマターの内容を検証
            self._validate_field_content(file_path, frontmatter)

            # ファイル構造を検証
            self._validate_file_structure(file_path, content)

            print(f"  ✅ {file_path.name} is valid")

        except Exception as e:
            self.errors.append(ValidationError(
                str(file_path.relative_to(self.base_dir)),
                f"Error during validation: {str(e)}",
                "error"
            ))

    def _extract_frontmatter(self, content: str) -> Tuple[Optional[Dict], str]:
        """YAML フロントマターを抽出"""
        # フロントマターは ---で囲まれた最初のセクション
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return None, content

        yaml_text = match.group(1)
        body = content[match.end():]

        try:
            frontmatter = yaml.safe_load(yaml_text)
            return frontmatter, body
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML frontmatter: {str(e)}")

    def _validate_required_fields(self, file_path: Path, frontmatter: Dict) -> None:
        """必須フィールドの存在を検証"""
        missing_fields = [
            field for field in self.REQUIRED_FIELDS
            if field not in frontmatter
        ]

        if missing_fields:
            self.errors.append(ValidationError(
                str(file_path.relative_to(self.base_dir)),
                f"Missing required fields: {', '.join(missing_fields)}",
                "error"
            ))

    def _validate_field_types(self, file_path: Path, frontmatter: Dict) -> None:
        """フィールドの型を検証"""
        for field, expected_types in self.FIELD_TYPES.items():
            if field in frontmatter:
                value = frontmatter[field]
                if not isinstance(value, expected_types):
                    self.errors.append(ValidationError(
                        str(file_path.relative_to(self.base_dir)),
                        f"Field '{field}' has invalid type. "
                        f"Expected {expected_types}, got {type(value).__name__}",
                        "error"
                    ))

    def _validate_field_content(self, file_path: Path, frontmatter: Dict) -> None:
        """フロントマター内容の検証"""
        # trigger_keywords が空でないか確認
        if 'trigger_keywords' in frontmatter:
            keywords = frontmatter['trigger_keywords']
            if isinstance(keywords, list):
                if len(keywords) == 0:
                    self.warnings.append(ValidationError(
                        str(file_path.relative_to(self.base_dir)),
                        "trigger_keywords is empty (should contain at least one keyword)",
                        "warning"
                    ))
                else:
                    # 各キーワードが文字列か確認
                    for i, kw in enumerate(keywords):
                        if not isinstance(kw, str):
                            self.errors.append(ValidationError(
                                str(file_path.relative_to(self.base_dir)),
                                f"trigger_keywords[{i}] is not a string: {kw}",
                                "error"
                            ))

        # stage が有効な値か確認
        if 'stage' in frontmatter:
            stage = frontmatter['stage']
            valid_stages = [
                'Phase1', 'Phase2', 'Phase3', 'Phase4',
                'planning', 'discovery', 'research',
                'Phase1（需要発見）', 'Phase2（CPF検証）',
                'Phase3（PSF検証）', 'Phase4（実装）'
            ]
            if stage not in valid_stages:
                self.warnings.append(ValidationError(
                    str(file_path.relative_to(self.base_dir)),
                    f"stage '{stage}' may not be in standard format. "
                    f"Common values: {', '.join(valid_stages)}",
                    "warning"
                ))

        # output_file パスの検証
        if 'output_file' in frontmatter:
            output_file = frontmatter['output_file']
            # 全角括弧を使用しているか確認
            if '(AIエージェント)' in output_file:
                self.errors.append(ValidationError(
                    str(file_path.relative_to(self.base_dir)),
                    "output_file contains half-width parentheses. "
                    "Use full-width: （AIエージェント）",
                    "error"
                ))

        # dependencies が有効か確認
        if 'dependencies' in frontmatter:
            deps = frontmatter['dependencies']
            if isinstance(deps, list):
                for i, dep in enumerate(deps):
                    if not isinstance(dep, str):
                        self.errors.append(ValidationError(
                            str(file_path.relative_to(self.base_dir)),
                            f"dependencies[{i}] is not a string: {dep}",
                            "error"
                        ))

    def _validate_file_structure(self, file_path: Path, content: str) -> None:
        """ファイル構造を検証"""
        # Markdown見出しの確認
        has_title = re.search(r'^#\s+', content, re.MULTILINE)
        if not has_title:
            self.warnings.append(ValidationError(
                str(file_path.relative_to(self.base_dir)),
                "No H1 heading (# Title) found in content",
                "warning"
            ))

        # コード例や説明の有無を確認
        has_content = len(content.strip()) > 100
        if not has_content:
            self.warnings.append(ValidationError(
                str(file_path.relative_to(self.base_dir)),
                "Content is very short (< 100 characters)",
                "warning"
            ))

    def _check_for_recruit_remnants(self) -> None:
        """ForRecruit残骸をチェック"""
        pattern = re.compile(r'ForRecruit', re.IGNORECASE)

        for md_file in self.skills_dir.glob('**/*.md'):
            content = md_file.read_text(encoding='utf-8')
            matches = pattern.finditer(content)

            for match in matches:
                # スキルファイル内の場合は警告
                if '_analysis' not in str(md_file) and 'PHASE' not in str(md_file):
                    self.warnings.append(ValidationError(
                        str(md_file.relative_to(self.base_dir)),
                        f"ForRecruit reference found: {match.group()}",
                        "warning"
                    ))

    def _generate_report(self) -> None:
        """検証レポートを生成"""
        summary = {
            'total_files': len(list(self.skills_dir.glob('**/SKILL.md'))),
            'valid_files': len(list(self.skills_dir.glob('**/SKILL.md'))) - len(self.errors),
            'invalid_files': len(self.errors),
            'total_issues': len(self.errors) + len(self.warnings),
        }

        report = {
            'timestamp': datetime.now().isoformat(),
            'errors': [asdict(e) for e in self.errors],
            'warnings': [asdict(w) for w in self.warnings],
            'summary': summary,
        }

        # JSON レポートを出力
        with open('validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        # コンソール出力
        print("\n" + "=" * 80)
        print("VALIDATION REPORT")
        print("=" * 80)

        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in self.errors:
                print(f"  {error.file}")
                print(f"    → {error.message}")

        if self.warnings:
            print(f"\n⚠️  Warnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  {warning.file}")
                print(f"    → {warning.message}")

        print(f"\n📊 Summary:")
        print(f"  Total files: {summary['total_files']}")
        print(f"  Valid files: {summary['valid_files']}")
        print(f"  Invalid files: {summary['invalid_files']}")
        print(f"  Total issues: {summary['total_issues']}")

        if not self.errors:
            print("\n✅ All validations passed!")
        else:
            print("\n❌ Validation failed!")

        print("=" * 80)


def main():
    """メイン関数"""
    validator = SkillValidator(base_dir='.')
    success = validator.validate_all()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
