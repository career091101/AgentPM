#!/usr/bin/env python3
"""
Newsletter Quality Re-evaluation Script v2.0
ネスト構造YAML対応版
"""

import os
import re
import csv
import yaml
from datetime import datetime, timedelta
from pathlib import Path

def extract_yaml_frontmatter(content):
    """YAML Front Matterを抽出してパース"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        try:
            return yaml.safe_load(yaml_content)
        except:
            # YAMLパース失敗時は手動パース
            return manual_parse_yaml(yaml_content)
    return {}

def manual_parse_yaml(yaml_text):
    """手動YAMLパース（フォールバック）"""
    data = {}
    current_key = None
    for line in yaml_text.split('\n'):
        if ':' in line and not line.strip().startswith('-'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if not value or value == '':
                current_key = key
                data[key] = {}
            else:
                if current_key and line.startswith('  '):
                    nested_key = key
                    data[current_key][nested_key] = value
                else:
                    data[key] = value
                    current_key = None
    return data

def get_nested_value(data, *keys):
    """ネストされた値を安全に取得"""
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, '')
        else:
            return ''
    return str(current) if current else ''

def count_sources(content):
    """ソース数をカウント"""
    sources_match = re.search(r'## Sources?\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if sources_match:
        sources_text = sources_match.group(1)
        urls = re.findall(r'https?://[^\s\)]+', sources_text)
        numbered = re.findall(r'^\d+\.', sources_text, re.MULTILINE)
        bullets = re.findall(r'^[-*]', sources_text, re.MULTILINE)
        return max(len(urls), len(numbered), len(bullets))
    return 0

def calculate_universal_score(metadata, content):
    """ユニバーサルメトリクス評価（50点満点）"""
    score = 0
    details = {}

    # 1. fact_check (30点) - qualityフィールドから取得
    fact_check = get_nested_value(metadata, 'quality', 'fact_check').strip('"\'')
    if fact_check.lower() == 'pass':
        score += 30
        details['fact_check'] = 30
    else:
        details['fact_check'] = 0

    # 2. sources_count (15点) - quality.sources_countまたはcontentから取得
    sources_in_metadata = get_nested_value(metadata, 'quality', 'sources_count')
    try:
        sources = int(sources_in_metadata) if sources_in_metadata else count_sources(content)
    except:
        sources = count_sources(content)

    if sources >= 8:
        score += 15
        details['sources_count'] = 15
    elif sources >= 5:
        score += 10
        details['sources_count'] = 10
    elif sources >= 3:
        score += 5
        details['sources_count'] = 5
    else:
        details['sources_count'] = 0

    # 3. last_verified (5点)
    last_verified = get_nested_value(metadata, 'quality', 'last_verified').strip('"\'')
    if last_verified:
        try:
            verified_date = datetime.strptime(last_verified, '%Y-%m-%d')
            days_ago = (datetime.now() - verified_date).days
            if days_ago <= 90:
                score += 5
                details['last_verified'] = 5
            else:
                details['last_verified'] = 0
        except:
            details['last_verified'] = 0
    else:
        details['last_verified'] = 0

    return score, details

def calculate_newsletter_score(metadata, content):
    """Newsletter固有メトリクス評価（50点満点）"""
    score = 0
    details = {}

    # 1. subscriber_data (15点)
    subscribers_total = get_nested_value(metadata, 'subscribers', 'total').strip('"\'')
    try:
        # "1000000" or "100000" などの文字列を数値に変換
        subs = int(str(subscribers_total).replace(',', '').replace('k', '000').replace('+', ''))
        if subs >= 1000:
            score += 15
            details['subscriber_data'] = 15
        elif subs >= 500:
            score += 10
            details['subscriber_data'] = 10
        elif subs >= 100:
            score += 5
            details['subscriber_data'] = 5
        else:
            details['subscriber_data'] = 0
    except:
        details['subscriber_data'] = 0

    # 2. metrics_complete (10点)
    engagement_rate = get_nested_value(metadata, 'metrics', 'engagement_rate').strip('"\'')
    growth_rate = get_nested_value(metadata, 'metrics', 'growth_rate_monthly').strip('"\'')
    if engagement_rate and growth_rate:
        score += 10
        details['metrics_complete'] = 10
    elif engagement_rate or growth_rate:
        score += 5
        details['metrics_complete'] = 5
    else:
        details['metrics_complete'] = 0

    # 3. growth_stage (10点)
    current = get_nested_value(metadata, 'growth_stage', 'current').strip('"\'')
    trust_score = get_nested_value(metadata, 'growth_stage', 'trust_score')
    authority_score = get_nested_value(metadata, 'growth_stage', 'authority_score')

    growth_stage_scores = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        'ideation': 1, 'validation': 2, 'early_growth': 3,
        'scaling': 4, 'mature': 5, 'influence': 5
    }
    current_score = growth_stage_scores.get(current.lower(), 0)

    # trust + authorityの合計スコアも評価
    try:
        combined_score = int(trust_score) + int(authority_score)
        if combined_score >= 8 or current_score >= 4:
            score += 10
            details['growth_stage'] = 10
        elif combined_score >= 5 or current_score >= 3:
            score += 5
            details['growth_stage'] = 5
        else:
            details['growth_stage'] = 0
    except:
        if current_score >= 3:
            score += 10
            details['growth_stage'] = 10
        else:
            details['growth_stage'] = 0

    # 4. cross_reference (10点)
    app_id = get_nested_value(metadata, 'cross_reference', 'app_id').strip('"\'')
    newsletter_id = metadata.get('id', '').strip('"\'')
    person_id = get_nested_value(metadata, 'cross_reference', 'person_registry_id').strip('"\'')

    has_reference = (
        (app_id and app_id.lower() != 'n/a') or
        newsletter_id or
        (person_id and person_id.lower() != 'n/a')
    )

    if has_reference:
        score += 10
        details['cross_reference'] = 10
    else:
        details['cross_reference'] = 0

    # 5. monetization_tags (5点)
    # monetizationフィールドをチェック
    monetization = metadata.get('monetization', [])
    if isinstance(monetization, list) and len(monetization) > 0:
        score += 5
        details['monetization_tags'] = 5
    else:
        details['monetization_tags'] = 0

    return score, details

def assign_grade(total_score):
    """グレード判定"""
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'

def evaluate_file(filepath):
    """1ファイルを評価"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = extract_yaml_frontmatter(content)

        # ユニバーサルスコア
        universal_score, universal_details = calculate_universal_score(metadata, content)

        # Newsletter固有スコア
        newsletter_score, newsletter_details = calculate_newsletter_score(metadata, content)

        # 合計スコア
        total_score = universal_score + newsletter_score
        grade = assign_grade(total_score)

        # 改善度（仮定: 改善前は11.9点平均）
        improvement = total_score - 11.9

        return {
            'filename': os.path.basename(filepath),
            'fact_check': universal_details['fact_check'],
            'sources_count': universal_details['sources_count'],
            'last_verified': universal_details['last_verified'],
            'subscriber_data': newsletter_details['subscriber_data'],
            'metrics_complete': newsletter_details['metrics_complete'],
            'growth_stage': newsletter_details['growth_stage'],
            'cross_reference': newsletter_details['cross_reference'],
            'monetization_tags': newsletter_details['monetization_tags'],
            'total': total_score,
            'rank': grade,
            'improvement': round(improvement, 1)
        }
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def main():
    # ファイル検索
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/02_Newsletter/case_studies')
    files = sorted(base_path.glob('NL_CASE_*.md'))

    print(f"Found {len(files)} Newsletter files")

    results = []
    for filepath in files:
        result = evaluate_file(filepath)
        if result:
            results.append(result)
            print(f"✓ {result['filename']}: {result['total']}点 ({result['rank']})")

    # CSV出力
    output_dir = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/analysis/quality_scores')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 're_evaluation_newsletter.csv'

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['filename', 'fact_check', 'sources_count', 'last_verified',
                     'subscriber_data', 'metrics_complete', 'growth_stage',
                     'cross_reference', 'monetization_tags', 'total', 'rank', 'improvement']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # サマリー統計
    total_scores = [r['total'] for r in results]
    avg_score = sum(total_scores) / len(total_scores)
    a_grade_count = sum(1 for r in results if r['rank'] == 'A')
    a_grade_rate = (a_grade_count / len(results)) * 100

    improvement_avg = avg_score - 11.9

    print(f"\n{'='*60}")
    print(f"Newsletter Quality Re-evaluation Summary")
    print(f"{'='*60}")
    print(f"Total files evaluated: {len(results)}")
    print(f"Average score BEFORE: 11.9点")
    print(f"Average score AFTER:  {avg_score:.1f}点")
    print(f"Score improvement:    +{improvement_avg:.1f}点")
    print(f"A-grade rate:         {a_grade_rate:.1f}% ({a_grade_count}/{len(results)})")
    print(f"{'='*60}")
    print(f"CSV output: {output_file}")

    # グレード分布
    grade_counts = {}
    for r in results:
        grade_counts[r['rank']] = grade_counts.get(r['rank'], 0) + 1

    print(f"\nGrade Distribution:")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = grade_counts.get(grade, 0)
        print(f"  {grade}: {count} ({count/len(results)*100:.1f}%)")

    # Top 10スコア
    print(f"\nTop 10 Scores:")
    sorted_results = sorted(results, key=lambda x: x['total'], reverse=True)
    for i, r in enumerate(sorted_results[:10], 1):
        print(f"  {i}. {r['filename']}: {r['total']}点 ({r['rank']})")

if __name__ == '__main__':
    main()
