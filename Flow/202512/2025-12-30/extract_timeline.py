#!/usr/bin/env python3
"""
Timeline Data Extraction Script
Extracts published_at dates from all JSON files and creates timeline_data.yaml
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Input directory
ARTICLES_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/full_run/articles")
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30")
THEME_MAPPING_PATH = OUTPUT_DIR / "theme_mapping.yaml"

def load_theme_mapping():
    """Load existing theme mapping to get theme assignments"""
    with open(THEME_MAPPING_PATH, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Create article_id to themes mapping
    article_themes = {}
    for theme_name, theme_data in data['themes'].items():
        for article in theme_data['articles']:
            # Extract article ID from file_path
            file_path = article.get('file_path', '')
            if file_path:
                article_id = Path(file_path).stem.split('_', 3)[-1] if '_' in Path(file_path).stem else ''
                if article_id not in article_themes:
                    article_themes[article_id] = []
                article_themes[article_id].append(theme_name)

    return article_themes

def extract_timeline_data():
    """Extract timeline data from all JSON files"""

    # Load theme mapping
    print("Loading theme mapping...")
    article_themes = load_theme_mapping()

    timeline_data = []
    json_files = list(ARTICLES_DIR.glob("*.json"))

    print(f"Processing {len(json_files)} JSON files...")

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extract date information
            published_at = data.get('published_at')
            if not published_at:
                continue

            # Parse date
            dt = datetime.fromisoformat(published_at.replace('+09:00', ''))

            # Get themes for this article
            article_id = json_file.stem.split('_', 3)[-1] if '_' in json_file.stem else ''
            themes = article_themes.get(article_id, ['未分類'])

            timeline_data.append({
                'id': data.get('id'),
                'title': data.get('title'),
                'published_date': dt.strftime('%Y-%m-%d'),
                'published_datetime': published_at,
                'year': dt.year,
                'month': dt.month,
                'day': dt.day,
                'themes': themes,
                'tags': data.get('tags', []),
                'url': data.get('url'),
                'file_path': str(json_file.relative_to(ARTICLES_DIR.parent.parent))
            })

        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")
            continue

    # Sort by date
    timeline_data.sort(key=lambda x: x['published_datetime'])

    return timeline_data

def create_period_stats(timeline_data):
    """Create statistics for period analysis"""

    # Count by year
    year_counts = defaultdict(int)
    year_month_counts = defaultdict(lambda: defaultdict(int))

    for article in timeline_data:
        year_counts[article['year']] += 1
        year_month_counts[article['year']][article['month']] += 1

    return {
        'year_counts': dict(year_counts),
        'year_month_counts': {year: dict(months) for year, months in year_month_counts.items()}
    }

def main():
    """Main execution"""

    print("Starting timeline data extraction...")

    # Extract data
    timeline_data = extract_timeline_data()

    print(f"Extracted {len(timeline_data)} articles")

    # Create period statistics
    stats = create_period_stats(timeline_data)

    # Prepare output
    output = {
        'metadata': {
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_articles': len(timeline_data),
            'date_range': {
                'start': timeline_data[0]['published_date'] if timeline_data else None,
                'end': timeline_data[-1]['published_date'] if timeline_data else None
            },
            'year_distribution': stats['year_counts']
        },
        'articles': timeline_data
    }

    # Write output
    output_path = OUTPUT_DIR / "timeline_data.yaml"
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(output, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"Timeline data saved to: {output_path}")
    print(f"\nYear distribution:")
    for year in sorted(stats['year_counts'].keys()):
        print(f"  {year}: {stats['year_counts'][year]} articles")

if __name__ == "__main__":
    main()
