#!/usr/bin/env python3
"""
Quality Checker for Founder Research Case Studies

ケーススタディの品質チェックスクリプト。
100点満点で品質スコアを算出し、PASS/WARN/FAILを判定。
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class QualityChecker:
    """ケーススタディ品質チェック"""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.documents_path = self.base_path / "documents"

    def check_file(self, file_path: Path) -> Dict:
        """1ファイルの品質チェック"""
        result = {
            'file': file_path.name,
            'scores': {},
            'total_score': 0,
            'grade': 'FAIL',
            'issues': []
        }

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # YAML Front Matter抽出
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                result['issues'].append('YAML Front Matterが見つかりません')
                return result

            yaml_content = match.group(1)
            metadata = yaml.safe_load(yaml_content)

            # 各項目をチェック
            result['scores']['yaml_syntax'] = self._check_yaml_syntax(yaml_content)
            result['scores']['required_fields'] = self._check_required_fields(metadata)
            result['scores']['sources_count'] = self._check_sources_count(metadata, content)
            result['scores']['cpf_data'] = self._check_cpf_data(metadata)
            result['scores']['psf_data'] = self._check_psf_data(metadata)
            result['scores']['fact_check'] = self._check_fact_check(metadata)

            # 総合スコア計算
            result['total_score'] = sum(result['scores'].values())

            # グレード判定
            if result['total_score'] >= 80:
                result['grade'] = 'PASS'
            elif result['total_score'] >= 60:
                result['grade'] = 'WARN'
            else:
                result['grade'] = 'FAIL'

        except Exception as e:
            result['issues'].append(f'エラー: {str(e)}')

        return result

    def _check_yaml_syntax(self, yaml_content: str) -> int:
        """YAML構文チェック（10点）"""
        try:
            yaml.safe_load(yaml_content)
            return 10
        except:
            return 0

    def _check_required_fields(self, metadata: Dict) -> int:
        """必須フィールドチェック（20点）"""
        required_fields = [
            'id',
            'title',
            'tier',
            ('founder', 'name'),
            ('company', 'name'),
            ('company', 'founded_year'),
            ('company', 'industry'),
            ('funding', 'total_raised'),
            ('validation_data', 'cpf'),
            ('validation_data', 'psf')
        ]

        score = 0
        for field in required_fields:
            if isinstance(field, tuple):
                # ネストフィールド
                value = metadata
                for key in field:
                    value = value.get(key, {}) if isinstance(value, dict) else None
                    if value is None:
                        break
                if value:
                    score += 2
            else:
                # トップレベルフィールド
                if metadata.get(field):
                    score += 2

        return min(score, 20)

    def _check_sources_count(self, metadata: Dict, content: str) -> int:
        """ソース数チェック（20点）"""
        sources_count = metadata.get('quality', {}).get('sources_count', 0)

        # 参照ソースセクションからもカウント
        source_section = re.search(r'## 参照ソース\s+(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if source_section:
            source_lines = [line for line in source_section.group(1).split('\n') if line.strip().startswith(('1.', '2.', '3.', '4.', '5.'))]
            actual_sources = len(source_lines)
            sources_count = max(sources_count, actual_sources)

        if sources_count >= 5:
            return 20
        elif sources_count >= 2:
            return 10
        elif sources_count == 1:
            return 5
        else:
            return 0

    def _check_cpf_data(self, metadata: Dict) -> int:
        """CPFデータ完全性チェック（20点）"""
        cpf_data = metadata.get('validation_data', {}).get('cpf', {})

        score = 0

        # interview_count（5点）
        if cpf_data.get('interview_count') is not None:
            score += 5

        # problem_commonality（5点）
        if cpf_data.get('problem_commonality') is not None:
            score += 5

        # wtp_confirmed（5点）
        if cpf_data.get('wtp_confirmed') is not None:
            score += 5

        # urgency_score（5点）
        if cpf_data.get('urgency_score') is not None:
            score += 5

        return score

    def _check_psf_data(self, metadata: Dict) -> int:
        """PSFデータ完全性チェック（20点）"""
        psf_data = metadata.get('validation_data', {}).get('psf', {})

        score = 0

        # ten_x_axes（10点）
        ten_x_axes = psf_data.get('ten_x_axes', [])
        if len(ten_x_axes) >= 2:
            score += 10
        elif len(ten_x_axes) == 1:
            score += 5

        # mvp_type（5点）
        if psf_data.get('mvp_type'):
            score += 5

        # initial_cvr（5点）
        if psf_data.get('initial_cvr') is not None:
            score += 5

        return score

    def _check_fact_check(self, metadata: Dict) -> int:
        """ファクトチェックステータス（10点）"""
        fact_check = metadata.get('quality', {}).get('fact_check', '')

        if fact_check == 'pass':
            return 10
        elif fact_check == 'warn':
            return 5
        else:
            return 0

    def check_all_files(self) -> Tuple[List[Dict], Dict]:
        """全ファイルの品質チェック"""
        results = []
        summary = {
            'total': 0,
            'pass': 0,
            'warn': 0,
            'fail': 0,
            'avg_score': 0
        }

        print("\n" + "="*60)
        print("🔍 品質チェック開始")
        print("="*60 + "\n")

        for category_dir in self.documents_path.iterdir():
            if not category_dir.is_dir():
                continue

            print(f"📁 {category_dir.name}")

            for md_file in category_dir.glob("FOUNDER_*.md"):
                result = self.check_file(md_file)
                results.append(result)

                # サマリー更新
                summary['total'] += 1
                if result['grade'] == 'PASS':
                    summary['pass'] += 1
                    icon = '✅'
                elif result['grade'] == 'WARN':
                    summary['warn'] += 1
                    icon = '⚠️ '
                else:
                    summary['fail'] += 1
                    icon = '❌'

                print(f"  {icon} {result['file']}: {result['total_score']}点 ({result['grade']})")

                # 問題がある場合は表示
                if result['issues']:
                    for issue in result['issues']:
                        print(f"     - {issue}")

        # 平均スコア計算
        if summary['total'] > 0:
            summary['avg_score'] = sum(r['total_score'] for r in results) / summary['total']

        print("\n" + "="*60)
        print("📊 品質チェックサマリー")
        print("="*60)
        print(f"総件数: {summary['total']}件")
        print(f"✅ PASS (80点以上): {summary['pass']}件 ({summary['pass']/summary['total']*100:.1f}%)")
        print(f"⚠️  WARN (60-79点): {summary['warn']}件 ({summary['warn']/summary['total']*100:.1f}%)")
        print(f"❌ FAIL (60点未満): {summary['fail']}件 ({summary['fail']/summary['total']*100:.1f}%)")
        print(f"平均スコア: {summary['avg_score']:.1f}点")
        print("="*60 + "\n")

        return results, summary

    def generate_quality_report(self, results: List[Dict], summary: Dict) -> str:
        """品質レポートMarkdown生成"""
        md = "# ケーススタディ品質レポート\n\n"

        from datetime import datetime
        md += f"**作成日**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

        md += "## サマリー\n\n"
        md += "| 指標 | 実績 |\n"
        md += "|------|:----:|\n"
        md += f"| 総件数 | {summary['total']}件 |\n"
        md += f"| ✅ PASS (80点以上) | {summary['pass']}件 ({summary['pass']/summary['total']*100:.1f}%) |\n"
        md += f"| ⚠️  WARN (60-79点) | {summary['warn']}件 ({summary['warn']/summary['total']*100:.1f}%) |\n"
        md += f"| ❌ FAIL (60点未満) | {summary['fail']}件 ({summary['fail']/summary['total']*100:.1f}%) |\n"
        md += f"| 平均スコア | {summary['avg_score']:.1f}点 |\n\n"

        # FAIL/WARNリスト
        md += "## 要改善ファイル\n\n"

        fail_files = [r for r in results if r['grade'] == 'FAIL']
        if fail_files:
            md += "### ❌ FAIL（60点未満）\n\n"
            md += "| ファイル | スコア | 問題点 |\n"
            md += "|---------|:------:|-------|\n"
            for r in sorted(fail_files, key=lambda x: x['total_score']):
                issues = ', '.join(r['issues']) if r['issues'] else 'データ不足'
                md += f"| {r['file']} | {r['total_score']}点 | {issues} |\n"
            md += "\n"

        warn_files = [r for r in results if r['grade'] == 'WARN']
        if warn_files:
            md += "### ⚠️  WARN（60-79点）\n\n"
            md += "| ファイル | スコア | 改善推奨 |\n"
            md += "|---------|:------:|----------|\n"
            for r in sorted(warn_files, key=lambda x: x['total_score']):
                # 低スコア項目を特定
                low_scores = [k for k, v in r['scores'].items() if v < 10]
                improvements = ', '.join(low_scores) if low_scores else '軽微改善'
                md += f"| {r['file']} | {r['total_score']}点 | {improvements} |\n"
            md += "\n"

        # 高品質ファイル
        pass_files = [r for r in results if r['grade'] == 'PASS']
        if pass_files:
            md += "## ✅ 高品質ファイル（80点以上）\n\n"
            md += "| ファイル | スコア |\n"
            md += "|---------|:------:|\n"
            for r in sorted(pass_files, key=lambda x: x['total_score'], reverse=True)[:20]:
                md += f"| {r['file']} | {r['total_score']}点 |\n"
            md += "\n"

        return md


if __name__ == "__main__":
    # 実行
    base_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research"

    checker = QualityChecker(base_path)
    results, summary = checker.check_all_files()

    # レポート生成
    report_md = checker.generate_quality_report(results, summary)

    # ファイル保存
    report_path = Path(base_path) / "quality_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_md)

    print(f"📄 品質レポート保存: {report_path}")
