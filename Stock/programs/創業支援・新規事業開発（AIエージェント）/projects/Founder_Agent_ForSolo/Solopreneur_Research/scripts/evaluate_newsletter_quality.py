#!/usr/bin/env python3
"""
Newsletter Quality Re-evaluation Script
100点満点スコアリング基準で全Newsletterファイルを再評価
"""

import os
import re
import csv
from datetime import datetime, timedelta
from pathlib import Path

def extract_yaml_frontmatter(content):
    """YAML Front Matterを抽出"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        metadata = {}
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        return metadata
    return {}

def count_sources(content):
    """ソース数をカウント"""
    sources_match = re.search(r'## Sources?\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if sources_match:
        sources_text = sources_match.group(1)
        # URLまたは番号付きリストをカウント
        urls = re.findall(r'https?://[^\s\)]+', sources_text)
        numbered = re.findall(r'^\d+\.', sources_text, re.MULTILINE)
        bullets = re.findall(r'^[-*]', sources_text, re.MULTILINE)
        return max(len(urls), len(numbered), len(bullets))
    return 0

def calculate_universal_score(metadata, content):
    """ユニバーサルメトリクス評価（50点満点）"""
    score = 0
    details = {}

    # 1. fact_check (30点)
    fact_check = metadata.get('fact_check', '').strip('"\'')
    if fact_check.lower() == 'pass':
        score += 30
        details['fact_check'] = 30
    else:
        details['fact_check'] = 0

    # 2. sources_count (15点)
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
    last_verified = metadata.get('last_verified', '').strip('"\'')
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
    subscribers_total = metadata.get('subscribers_total', '0').strip('"\'')
    try:
        subs = int(subscribers_total.replace(',', '').replace('k', '000').replace('+', ''))
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
    engagement_rate = metadata.get('engagement_rate', '').strip('"\'')
    growth_rate = metadata.get('growth_rate_monthly', '').strip('"\'')
    if engagement_rate and growth_rate:
        score += 10
        details['metrics_complete'] = 10
    elif engagement_rate or growth_rate:
        score += 5
        details['metrics_complete'] = 5
    else:
        details['metrics_complete'] = 0

    # 3. growth_stage (10点)
    current = metadata.get('current', '0').strip('"\'')
    growth_stage_scores = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        'ideation': 1, 'validation': 2, 'early_growth': 3,
        'scaling': 4, 'mature': 5
    }
    current_score = growth_stage_scores.get(current.lower(), 0)

    if current_score >= 3:
        score += 10
        details['growth_stage'] = 10
    elif current_score >= 2:
        score += 5
        details['growth_stage'] = 5
    else:
        details['growth_stage'] = 0

    # 4. cross_reference (10点)
    app_id = metadata.get('app_id', '').strip('"\'')
    newsletter_id = metadata.get('newsletter_id', '').strip('"\'')
    person_id = metadata.get('person_registry_id', '').strip('"\'')

    if app_id or newsletter_id or person_id:
        score += 10
        details['cross_reference'] = 10
    else:
        details['cross_reference'] = 0

    # 5. monetization_tags (5点)
    tags = metadata.get('tags', '').strip('"\'')
    monetization_keywords = ['sponsorship', 'subscription', 'ads', 'affiliate',
                            'product', 'consulting', 'premium', 'paid']
    has_monetization = any(kw in tags.lower() for kw in monetization_keywords)

    if has_monetization:
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

if __name__ == '__main__':
    main()
