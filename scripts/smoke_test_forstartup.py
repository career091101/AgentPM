#!/usr/bin/env python3
"""
ForStartup Edition Smoke Test
全26スキルの基本動作確認
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# 定義されたスキルリスト
TIER_1_SKILLS = [
    'discover-demand',
    'research-problem',
    'research-competitors',
    'create-persona',
    'simulate-interview',
    'validate-cpf',
    'validate-psf',
    'validate-pmf',
    'validate-10x',
    'create-mvv',
    'build-pitch-deck',
    'prepare-vc-meeting',
]

TIER_2_SKILLS = [
    'design-pricing',
    'analyze-aarrr',
    'build-flywheel',
    'build-lp',
    'build-synergy-map',
    'inventory-internal-resources',
    'validate-market-timing',
    'design-exit-strategy',
    'analyze-competitive-moat',
    'validate-ring-criteria',
    'orchestrate-review-loop',
    'discover-demand-vc-focus',
    'build-approval-deck',
    'validate-unit-economics-strict',
]

ALL_SKILLS = TIER_1_SKILLS + TIER_2_SKILLS

BASE_PATH = Path('/Users/yuichi/AIPM/aipm_v0')
SKILLS_PATH = BASE_PATH / '.claude' / 'skills' / 'for_startup'
COMMANDS_PATH = BASE_PATH / '.claude' / 'commands'

# テスト結果の格納
results = {
    'file_integrity': {},
    'path_references': {},
    'command_consistency': {},
    'markdown_syntax': {},
    'summary': {
        'file_integrity': {'pass': 0, 'warning': 0, 'fail': 0},
        'path_references': {'pass': 0, 'warning': 0, 'fail': 0},
        'command_consistency': {'pass': 0, 'warning': 0, 'fail': 0},
        'markdown_syntax': {'pass': 0, 'warning': 0, 'fail': 0},
    }
}

def check_file_integrity(skill_name: str) -> Tuple[str, List[str]]:
    """ファイル整合性チェック"""
    issues = []
    skill_dir = SKILLS_PATH / skill_name

    # スキルディレクトリの存在確認
    if not skill_dir.exists():
        return 'fail', [f"スキルディレクトリが存在しません: {skill_dir}"]

    # SKILL.mdの存在確認
    skill_md = skill_dir / 'SKILL.md'
    if not skill_md.exists():
        issues.append(f"SKILL.mdが存在しません")
        return 'fail', issues

    # ファイルサイズチェック
    if skill_md.stat().st_size == 0:
        issues.append(f"SKILL.mdが空です (0 bytes)")
        return 'fail', issues

    # コマンドファイルの存在確認
    cmd_name = f'for-startup-{skill_name}.md'
    cmd_file = COMMANDS_PATH / cmd_name
    if not cmd_file.exists():
        issues.append(f"コマンドファイルが存在しません: {cmd_name}")
        return 'fail', issues

    if cmd_file.stat().st_size == 0:
        issues.append(f"コマンドファイルが空です: {cmd_name}")
        return 'fail', issues

    return 'pass', issues

def check_path_references(skill_name: str) -> Tuple[str, List[str]]:
    """参照パス存在確認"""
    issues = []
    skill_dir = SKILLS_PATH / skill_name
    skill_md = skill_dir / 'SKILL.md'

    if not skill_md.exists():
        return 'fail', ["SKILL.mdが存在しません"]

    try:
        content = skill_md.read_text(encoding='utf-8')
    except Exception as e:
        return 'fail', [f"ファイル読み込みエラー: {str(e)}"]

    # 参照パターンを抽出
    # @で始まるパスを検出
    ref_pattern = r'@([^\s\]]+)'
    references = re.findall(ref_pattern, content)

    missing_refs = []
    for ref in set(references):
        # 相対パスを絶対パスに変換
        if ref.startswith('.claude/'):
            check_path = BASE_PATH / ref
        elif ref.startswith('Founder'):
            # Stock/programs/...下の参照
            check_path = BASE_PATH / 'Stock' / 'programs' / '創業支援・新規事業開発（AIエージェント）' / 'projects' / ref
        else:
            check_path = BASE_PATH / ref

        if not check_path.exists():
            missing_refs.append(f"参照パスが見つかりません: @{ref}")

    if missing_refs:
        return 'warning' if len(missing_refs) <= 2 else 'fail', missing_refs

    return 'pass', issues

def check_command_consistency(skill_name: str) -> Tuple[str, List[str]]:
    """コマンド-スキル整合性確認"""
    issues = []

    cmd_name = f'for-startup-{skill_name}.md'
    cmd_file = COMMANDS_PATH / cmd_name

    if not cmd_file.exists():
        return 'fail', [f"コマンドファイルが存在しません: {cmd_name}"]

    try:
        content = cmd_file.read_text(encoding='utf-8')
    except Exception as e:
        return 'fail', [f"ファイル読み込みエラー: {str(e)}"]

    # YAMLフロントマター抽出
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        issues.append("YAMLフロントマターが見つかりません")
        return 'warning', issues

    yaml_content = yaml_match.group(1)

    # スキル名の一致確認
    if f"skill: '{skill_name}'" not in yaml_content and f'skill: "{skill_name}"' not in yaml_content:
        issues.append(f"YAMLのスキル名が一致していません (期待: {skill_name})")

    # Output pathの確認
    if 'output_path:' in yaml_content:
        output_match = re.search(r'output_path:\s*(.+)', yaml_content)
        if output_match and 'null2' not in output_match.group(1):
            pass  # パスが設定されている

    return 'pass' if not issues else 'warning', issues

def check_markdown_syntax(skill_name: str) -> Tuple[str, List[str]]:
    """Markdown構文チェック"""
    issues = []
    skill_dir = SKILLS_PATH / skill_name
    skill_md = skill_dir / 'SKILL.md'

    if not skill_md.exists():
        return 'fail', ["SKILL.mdが存在しません"]

    try:
        content = skill_md.read_text(encoding='utf-8')
    except Exception as e:
        return 'fail', [f"ファイル読み込みエラー: {str(e)}"]

    # YAMLフロントマターチェック
    if not re.match(r'^---\n', content):
        issues.append("YAMLフロントマターが見つかりません")

    # 見出しの階層チェック
    lines = content.split('\n')
    prev_level = 0
    for i, line in enumerate(lines, 1):
        if line.startswith('#'):
            match = re.match(r'^(#+)\s', line)
            if match:
                level = len(match.group(1))
                # 階層が2段階以上飛ばないかチェック
                if level > prev_level + 1 and prev_level > 0:
                    issues.append(f"行{i}: 見出しの階層が不正です (#{prev_level}から#{level}へジャンプ)")
                prev_level = level

    # リンク構文チェック
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for i, line in enumerate(lines, 1):
        # リンク形式が正しいか確認
        if '[' in line and ']' in line and '(' in line:
            matches = re.findall(r'\[([^\]]*)\]\(', line)
            for match in matches:
                if not match:
                    issues.append(f"行{i}: 空のリンクテキストがあります")

    return 'pass' if not issues else 'warning' if len(issues) <= 2 else 'fail', issues

def run_smoke_tests():
    """全スキルのスモークテスト実行"""
    print("ForStartup Edition Smoke Test 実行中...\n")

    for skill_name in ALL_SKILLS:
        # ファイル整合性チェック
        status, issues = check_file_integrity(skill_name)
        results['file_integrity'][skill_name] = {'status': status, 'issues': issues}
        results['summary']['file_integrity'][status] += 1

        # 参照パス存在確認
        status, issues = check_path_references(skill_name)
        results['path_references'][skill_name] = {'status': status, 'issues': issues}
        results['summary']['path_references'][status] += 1

        # コマンド-スキル整合性確認
        status, issues = check_command_consistency(skill_name)
        results['command_consistency'][skill_name] = {'status': status, 'issues': issues}
        results['summary']['command_consistency'][status] += 1

        # Markdown構文チェック
        status, issues = check_markdown_syntax(skill_name)
        results['markdown_syntax'][skill_name] = {'status': status, 'issues': issues}
        results['summary']['markdown_syntax'][status] += 1

    return results

def generate_report(results: Dict) -> str:
    """レポート生成"""
    report = """# ForStartup Edition Smoke Test Report

## テスト実行日時

"""
    import datetime
    report += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

    # サマリー表
    report += """## テスト結果サマリー

| テスト項目 | 合格 | 警告 | 不合格 | 合計 |
|-----------|------|------|--------|------|
"""

    for test_type in ['file_integrity', 'path_references', 'command_consistency', 'markdown_syntax']:
        summary = results['summary'][test_type]
        total = summary['pass'] + summary['warning'] + summary['fail']
        report += f"| {test_type} | {summary['pass']}/26 | {summary['warning']}/26 | {summary['fail']}/26 | {total}/26 |\n"

    # 総合判定
    total_pass = sum(results['summary'][t]['pass'] for t in results['summary'])
    total_warning = sum(results['summary'][t]['warning'] for t in results['summary'])
    total_fail = sum(results['summary'][t]['fail'] for t in results['summary'])
    total_all = total_pass + total_warning + total_fail

    report += f"| **総合** | **{total_pass}/104** | **{total_warning}/104** | **{total_fail}/104** | **{total_all}/104** |\n\n"

    # Tier別結果
    report += "## Tier別詳細結果\n\n"

    # Tier 1
    report += "### Tier 1スキル (12)\n\n"
    for skill_name in TIER_1_SKILLS:
        report += generate_skill_report(skill_name, results)

    # Tier 2
    report += "\n### Tier 2スキル (14)\n\n"
    for skill_name in TIER_2_SKILLS:
        report += generate_skill_report(skill_name, results)

    # 重大な問題
    critical_issues = find_critical_issues(results)
    if critical_issues:
        report += "\n## 重大な問題\n\n"
        for i, issue in enumerate(critical_issues, 1):
            report += f"{i}. {issue}\n"
    else:
        report += "\n## 重大な問題\n\nなし\n"

    # 推奨修正
    recommendations = generate_recommendations(results)
    if recommendations:
        report += "\n## 推奨修正\n\n"
        for i, rec in enumerate(recommendations, 1):
            report += f"{i}. {rec}\n"
    else:
        report += "\n## 推奨修正\n\nなし\n"

    # E2Eテスト準備状況
    report += "\n## E2Eテスト準備状況\n\n"
    if total_fail == 0 and total_warning <= 5:
        report += "- ✅ 基本動作確認完了\n"
        report += "- ✅ 参照パス整合性確認完了\n"
        report += "- ✅ 実ユーザーテスト準備完了\n"
    elif total_fail == 0:
        report += "- ✅ 基本動作確認完了\n"
        report += "- ⚠️ 参照パス整合性確認完了 (軽微な警告あり)\n"
        report += "- ⚠️ 一部修正後、実ユーザーテスト準備可能\n"
    else:
        report += "- ❌ 基本動作確認に失敗\n"
        report += "- ❌ 大規模修正必要\n"

    return report

def generate_skill_report(skill_name: str, results: Dict) -> str:
    """スキル別レポート生成"""
    fi_status = results['file_integrity'][skill_name]['status']
    pr_status = results['path_references'][skill_name]['status']
    cc_status = results['command_consistency'][skill_name]['status']
    ms_status = results['markdown_syntax'][skill_name]['status']

    # ステータスアイコン
    def icon(status):
        return '✅' if status == 'pass' else '⚠️' if status == 'warning' else '❌'

    # 総合判定
    statuses = [fi_status, pr_status, cc_status, ms_status]
    if 'fail' in statuses:
        overall = 'FAIL'
    elif 'warning' in statuses:
        overall = 'WARNING'
    else:
        overall = 'PASS'

    report = f"#### {skill_name}\n\n"
    report += f"- ファイル整合性: {icon(fi_status)}\n"
    report += f"- 参照パス: {icon(pr_status)}\n"
    report += f"- コマンド整合性: {icon(cc_status)}\n"
    report += f"- Markdown構文: {icon(ms_status)}\n"
    report += f"- **総合判定**: {overall}\n"

    # 問題がある場合は列挙
    issues = []
    if fi_status != 'pass':
        issues.extend(results['file_integrity'][skill_name]['issues'])
    if pr_status != 'pass':
        issues.extend(results['path_references'][skill_name]['issues'])
    if cc_status != 'pass':
        issues.extend(results['command_consistency'][skill_name]['issues'])
    if ms_status != 'pass':
        issues.extend(results['markdown_syntax'][skill_name]['issues'])

    if issues:
        report += f"- **問題**: \n"
        for issue in issues:
            report += f"  - {issue}\n"

    report += "\n"
    return report

def find_critical_issues(results: Dict) -> List[str]:
    """重大な問題を抽出"""
    critical = []

    for skill_name in ALL_SKILLS:
        # FAILステータスのチェック
        if results['file_integrity'][skill_name]['status'] == 'fail':
            critical.append(f"{skill_name}: ファイル整合性エラー - " +
                          " / ".join(results['file_integrity'][skill_name]['issues']))

        if results['command_consistency'][skill_name]['status'] == 'fail':
            critical.append(f"{skill_name}: コマンド整合性エラー")

    return critical

def generate_recommendations(results: Dict) -> List[str]:
    """修正推奨事項を生成"""
    recommendations = []

    # 参照パスエラーの集計
    path_issues_count = sum(1 for s in ALL_SKILLS
                           if results['path_references'][s]['status'] != 'pass')
    if path_issues_count > 0:
        recommendations.append(f"{path_issues_count}個のスキルで参照パスに問題があります。参照パスを修正してください。")

    # Markdown構文エラーの集計
    md_issues_count = sum(1 for s in ALL_SKILLS
                         if results['markdown_syntax'][s]['status'] == 'fail')
    if md_issues_count > 0:
        recommendations.append(f"{md_issues_count}個のスキルでMarkdown構文エラーが見つかりました。")

    return recommendations

if __name__ == '__main__':
    results = run_smoke_tests()
    report = generate_report(results)

    # レポートを出力
    output_path = BASE_PATH / 'Stock' / 'programs' / '創業支援・新規事業開発（AIエージェント）' / 'projects' / 'Founder_Agent_ForStartup' / 'SMOKE_TEST_REPORT.md'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print("レポートを生成しました:")
    print(f"  {output_path}")
    print("\n" + "="*80 + "\n")
    print(report)

    # JSON形式でも保存
    json_path = output_path.parent / 'smoke_test_results.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nJSON結果を保存しました: {json_path}")
