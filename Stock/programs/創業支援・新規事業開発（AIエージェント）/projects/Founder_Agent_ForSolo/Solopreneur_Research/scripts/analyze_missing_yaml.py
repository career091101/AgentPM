#!/usr/bin/env python3
"""
Missing YAML Front Matter分析スクリプト
どのファイルにYAMLがないか、どのフィールドが不足しているかを特定
"""

import os
import re
import csv
import yaml
from pathlib import Path

def has_yaml_frontmatter(content):
    """YAML Front Matterの有無を確認"""
    return bool(re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL))

def extract_yaml_frontmatter(content):
    """YAML Front Matterを抽出"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        try:
            return yaml.safe_load(yaml_content)
        except:
            return {}
    return {}

def check_required_fields(metadata):
    """必須フィールドの有無をチェック"""
    checks = {
        'has_id': bool(metadata.get('id')),
        'has_quality': bool(metadata.get('quality')),
        'has_fact_check': bool(metadata.get('quality', {}).get('fact_check')) if isinstance(metadata.get('quality'), dict) else False,
        'has_last_verified': bool(metadata.get('quality', {}).get('last_verified')) if isinstance(metadata.get('quality'), dict) else False,
        'has_sources_count': bool(metadata.get('quality', {}).get('sources_count')) if isinstance(metadata.get('quality'), dict) else False,
        'has_subscribers': bool(metadata.get('subscribers')),
        'has_metrics': bool(metadata.get('metrics')),
        'has_growth_stage': bool(metadata.get('growth_stage')),
        'has_cross_reference': bool(metadata.get('cross_reference')),
        'has_monetization': bool(metadata.get('monetization'))
    }
    return checks

def analyze_file(filepath):
    """1ファイルを分析"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        has_yaml = has_yaml_frontmatter(content)

        result = {
            'filename': os.path.basename(filepath),
            'has_yaml': has_yaml,
        }

        if has_yaml:
            metadata = extract_yaml_frontmatter(content)
            checks = check_required_fields(metadata)
            result.update(checks)

            # 完全性スコア（10フィールド中何個持っているか）
            completeness = sum(checks.values())
            result['completeness'] = completeness
            result['status'] = 'COMPLETE' if completeness == 10 else f'PARTIAL ({completeness}/10)'
        else:
            result.update({
                'has_id': False,
                'has_quality': False,
                'has_fact_check': False,
                'has_last_verified': False,
                'has_sources_count': False,
                'has_subscribers': False,
                'has_metrics': False,
                'has_growth_stage': False,
                'has_cross_reference': False,
                'has_monetization': False,
                'completeness': 0,
                'status': 'NO_YAML'
            })

        return result

    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        return None

def main():
    # ファイル検索
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/02_Newsletter/case_studies')
    files = sorted(base_path.glob('NL_CASE_*.md'))

    print(f"Analyzing {len(files)} Newsletter files...")

    results = []
    for filepath in files:
        result = analyze_file(filepath)
        if result:
            results.append(result)

    # CSV出力
    output_dir = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/analysis/quality_scores')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'missing_yaml_analysis.csv'

    fieldnames = ['filename', 'has_yaml', 'completeness', 'status',
                 'has_id', 'has_quality', 'has_fact_check', 'has_last_verified',
                 'has_sources_count', 'has_subscribers', 'has_metrics',
                 'has_growth_stage', 'has_cross_reference', 'has_monetization']

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # 統計サマリー
    no_yaml = [r for r in results if not r['has_yaml']]
    partial = [r for r in results if r['has_yaml'] and r['completeness'] < 10]
    complete = [r for r in results if r['has_yaml'] and r['completeness'] == 10]

    print(f"\n{'='*60}")
    print(f"YAML Front Matter Analysis Summary")
    print(f"{'='*60}")
    print(f"Total files:         {len(results)}")
    print(f"NO YAML:             {len(no_yaml)} ({len(no_yaml)/len(results)*100:.1f}%)")
    print(f"PARTIAL YAML:        {len(partial)} ({len(partial)/len(results)*100:.1f}%)")
    print(f"COMPLETE YAML:       {len(complete)} ({len(complete)/len(results)*100:.1f}%)")
    print(f"{'='*60}")

    # NO YAMLファイルリスト
    if no_yaml:
        print(f"\nNO YAML Files ({len(no_yaml)}):")
        for r in no_yaml:
            print(f"  - {r['filename']}")

    # PARTIAL YAMLファイルリスト
    if partial:
        print(f"\nPARTIAL YAML Files ({len(partial)}):")
        for r in sorted(partial, key=lambda x: x['completeness']):
            print(f"  - {r['filename']}: {r['completeness']}/10 fields")

    # フィールド別欠損統計
    print(f"\nMissing Field Statistics:")
    field_stats = {
        'id': sum(1 for r in results if not r['has_id']),
        'quality': sum(1 for r in results if not r['has_quality']),
        'fact_check': sum(1 for r in results if not r['has_fact_check']),
        'last_verified': sum(1 for r in results if not r['has_last_verified']),
        'sources_count': sum(1 for r in results if not r['has_sources_count']),
        'subscribers': sum(1 for r in results if not r['has_subscribers']),
        'metrics': sum(1 for r in results if not r['has_metrics']),
        'growth_stage': sum(1 for r in results if not r['has_growth_stage']),
        'cross_reference': sum(1 for r in results if not r['has_cross_reference']),
        'monetization': sum(1 for r in results if not r['has_monetization'])
    }

    for field, count in sorted(field_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {field}: {count} files missing ({count/len(results)*100:.1f}%)")

    print(f"\nCSV output: {output_file}")

if __name__ == '__main__':
    main()
