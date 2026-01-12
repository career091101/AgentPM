#!/usr/bin/env python3
"""
Period Analysis Script
Analyzes articles by time periods and generates period-specific reports
"""

import yaml
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import re

# Paths
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30")
TIMELINE_DATA_PATH = OUTPUT_DIR / "timeline_data.yaml"
ARTICLES_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/full_run/articles")
ANALYSIS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/Analysis/Pattern_B_Timeline")

# Period definitions
PERIODS = {
    'Period_1_2019-2020': {
        'name': '初期探索期（2019-2020）',
        'years': [2019, 2020],
        'description': 'note開始初期、コンピュテーショナル・フィールドの探索と表現実験'
    },
    'Period_2_2021-2023': {
        'name': '展開深化期（2021-2023）',
        'years': [2021, 2022, 2023],
        'description': 'デジタルネイチャー概念の展開とパンデミック期の思索'
    },
    'Period_3_2024-2025': {
        'name': '統合実装期（2024-2025）',
        'years': [2024, 2025],
        'description': 'null²プロジェクトと大阪万博に向けた統合的実践'
    }
}

def load_timeline_data():
    """Load timeline data"""
    with open(TIMELINE_DATA_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def classify_by_period(timeline_data):
    """Classify articles by period"""
    period_articles = {period_id: [] for period_id in PERIODS.keys()}

    for article in timeline_data['articles']:
        year = article['year']
        for period_id, period_info in PERIODS.items():
            if year in period_info['years']:
                period_articles[period_id].append(article)
                break

    return period_articles

def extract_keywords_from_title(title):
    """Extract keywords from title (simple word extraction)"""
    # Remove common patterns
    title = re.sub(r'[｜\|]落合陽一.*$', '', title)
    title = re.sub(r'[\(\（].*?[\)\）]', '', title)
    title = re.sub(r'[【】「」『』\[\]#]', ' ', title)

    # Split and filter
    words = title.split()
    keywords = [w.strip() for w in words if len(w.strip()) > 1]

    return keywords

def analyze_period(period_id, articles):
    """Analyze a specific period"""

    # Theme distribution
    theme_counter = Counter()
    for article in articles:
        for theme in article.get('themes', []):
            theme_counter[theme] += 1

    # Tag analysis
    tag_counter = Counter()
    for article in articles:
        for tag in article.get('tags', []):
            tag_counter[tag] += 1

    # Keyword extraction from titles
    keyword_counter = Counter()
    for article in articles:
        keywords = extract_keywords_from_title(article['title'])
        keyword_counter.update(keywords)

    # Monthly distribution
    monthly_dist = Counter()
    for article in articles:
        monthly_dist[f"{article['year']}-{article['month']:02d}"] += 1

    return {
        'total_articles': len(articles),
        'theme_distribution': dict(theme_counter.most_common(10)),
        'top_tags': dict(tag_counter.most_common(20)),
        'top_keywords': dict(keyword_counter.most_common(30)),
        'monthly_distribution': dict(sorted(monthly_dist.items())),
        'articles': articles
    }

def get_representative_articles(articles, n=5):
    """Get representative articles from the period"""
    # Get articles with most tags or longest titles (as proxy for substantial content)
    scored_articles = []
    for article in articles:
        score = len(article.get('tags', [])) + len(article.get('themes', []))
        scored_articles.append((score, article))

    scored_articles.sort(key=lambda x: x[0], reverse=True)
    return [article for score, article in scored_articles[:n]]

def read_article_content(file_path):
    """Read article markdown content"""
    md_path = ARTICLES_DIR.parent / file_path.replace('.json', '.md')
    if md_path.exists():
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract first few paragraphs
                lines = content.split('\n')
                paragraphs = []
                current_para = []
                for line in lines:
                    if line.strip():
                        current_para.append(line)
                    elif current_para:
                        paragraphs.append('\n'.join(current_para))
                        current_para = []
                        if len(paragraphs) >= 3:
                            break
                return '\n\n'.join(paragraphs[:3])
        except:
            pass
    return ""

def create_period_readme(period_id, period_info, analysis):
    """Create README.md for each period"""

    content = f"""# {period_info['name']}

## 期間概要

**対象期間**: {', '.join(map(str, period_info['years']))}

{period_info['description']}

## 基本統計

- **総記事数**: {analysis['total_articles']}件
- **月平均**: {analysis['total_articles'] / (len(period_info['years']) * 12):.1f}件

## 月別分布

"""

    for month, count in analysis['monthly_distribution'].items():
        content += f"- {month}: {count}件\n"

    content += f"""

## テーマ分布（上位10位）

"""

    for theme, count in analysis['theme_distribution'].items():
        percentage = (count / analysis['total_articles']) * 100
        content += f"- **{theme}**: {count}件 ({percentage:.1f}%)\n"

    content += f"""

## 頻出タグ（上位20位）

"""

    for tag, count in list(analysis['top_tags'].items())[:20]:
        content += f"- {tag}: {count}件\n"

    content += f"""

## 頻出キーワード（タイトルから抽出、上位30位）

"""

    for keyword, count in list(analysis['top_keywords'].items())[:30]:
        if count >= 3:  # 3回以上出現したもののみ
            content += f"- {keyword}: {count}回\n"

    content += """

## 期間の特徴

"""

    # Analyze characteristics based on themes and keywords
    top_themes = list(analysis['theme_distribution'].keys())[:3]
    content += f"この期間は、主に「{top_themes[0]}」「{top_themes[1] if len(top_themes) > 1 else ''}」を中心としたコンテンツが展開されました。\n\n"

    content += "詳細なトレンド分析は、別途作成される期間別トレンドレポートを参照してください。\n"

    return content

def create_article_list(period_id, articles):
    """Create article_list.md for each period"""

    content = f"""# {PERIODS[period_id]['name']} - 記事一覧

総記事数: {len(articles)}件

## 記事リスト

"""

    for article in articles:
        content += f"""### {article['title']}

- **公開日**: {article['published_date']}
- **テーマ**: {', '.join(article['themes'])}
- **タグ**: {', '.join(article.get('tags', []))}
- **URL**: {article['url']}

---

"""

    return content

def main():
    """Main execution"""

    print("Loading timeline data...")
    timeline_data = load_timeline_data()

    print("Classifying articles by period...")
    period_articles = classify_by_period(timeline_data)

    # Analyze each period
    period_analyses = {}
    for period_id, articles in period_articles.items():
        print(f"Analyzing {period_id}: {len(articles)} articles...")
        period_analyses[period_id] = analyze_period(period_id, articles)

    # Create README and article list for each period
    for period_id, analysis in period_analyses.items():
        period_dir = ANALYSIS_DIR / period_id

        # Create README
        readme_content = create_period_readme(period_id, PERIODS[period_id], analysis)
        readme_path = period_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"Created {readme_path}")

        # Create article list
        article_list_content = create_article_list(period_id, analysis['articles'])
        article_list_path = period_dir / "article_list.md"
        with open(article_list_path, 'w', encoding='utf-8') as f:
            f.write(article_list_content)
        print(f"Created {article_list_path}")

    # Save detailed analysis data
    analysis_data_path = OUTPUT_DIR / "period_analysis_data.yaml"
    with open(analysis_data_path, 'w', encoding='utf-8') as f:
        yaml.dump(period_analyses, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"Saved detailed analysis to {analysis_data_path}")

    print("\nPeriod analysis complete!")

if __name__ == "__main__":
    main()
