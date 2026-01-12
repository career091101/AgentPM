import json
from pathlib import Path
from collections import Counter
import re

# 全JSONファイルを読み込む
base_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note")

articles = []

print("Reading JSON files...")
for json_file in base_path.rglob("*.json"):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            articles.append(data)
    except Exception as e:
        print(f"Error reading {json_file}: {e}")

print(f"\nTotal articles loaded: {len(articles)}")

# タイトルのキーワード分析
keyword_patterns = {
    'AI技術の進化': [
        'AI', 'LLM', 'GPT', 'DeepSeek', '生成AI', '機械学習',
        'オープンソース', 'Llama', 'Claude', 'ChatGPT', 'Gemini',
        'AIバブル', '大規模言語モデル', 'OpenAI', '言語モデル'
    ],
    'アート・メディア表現': [
        '質量', 'アート', '写真', '表現', '美', 'エモ', 'センサー',
        '映像', 'メディア', '芸術', 'カメラ', 'CCD', 'レンズ',
        '画像', '視覚', '光', '色', '撮影', 'フィルム'
    ],
    '教育・研究の未来': [
        '教育', '学校', '研究', '学習', '大学', '学生',
        '授業', '知識', 'ラボ', '講義', '教室'
    ],
    '都市・空間デザイン': [
        '都市', '空間', 'セミパブリック', '風景', '建築', '場所',
        'まちづくり', '環境', 'ランドスケープ', '街', '景観'
    ],
    '未来予測・技術革新': [
        '未来', '予測', 'トレンド', '2030', '2035', 'シンギュラリティ',
        'カルロタ・ペレス', '技術革命', '金融資本', 'イノベーション'
    ],
    '社会構造・公共財': [
        '社会', '資本主義', '公共財', 'インフラ', '革命', 'バブル',
        'コモディティ', '鉄道', '運河', '産業革命', '資本', '経済'
    ],
    'デジタルネイチャー': [
        'デジタルネイチャー', '計算機自然', 'デジタルツイン',
        'メタバース', 'VR', 'AR', 'XR', '空間コンピューティング',
        'バーチャル', '仮想空間'
    ],
    '身体性・物質性': [
        '裸性', '身体性', '物質', '質量', 'フィジカル',
        '肉体', '身体', '触覚', 'マテリアル'
    ]
}

theme_counts = {theme: 0 for theme in keyword_patterns}
theme_articles = {theme: [] for theme in keyword_patterns}

for article in articles:
    title = article.get('title', '')
    for theme, keywords in keyword_patterns.items():
        if any(kw in title for kw in keywords):
            theme_counts[theme] += 1
            if len(theme_articles[theme]) < 5:
                theme_articles[theme].append(article)

print("\n=== THEME DISTRIBUTION ===\n")
for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{theme}: {count} articles")

# 日付分析
all_dates = [a.get('publishedAt', '') for a in articles if a.get('publishedAt')]
if all_dates:
    print(f"\n=== DATE RANGE ===")
    print(f"Earliest: {min(all_dates)}")
    print(f"Latest: {max(all_dates)}")

    year_counter = Counter()
    for date in all_dates:
        if date and len(date) >= 4:
            year = date[:4]
            year_counter[year] += 1

    print(f"\n=== ARTICLES BY YEAR ===")
    for year, count in sorted(year_counter.items()):
        print(f"{year}: {count}")

# 各テーマのサンプル記事を保存
print("\n=== SAVING SAMPLE ARTICLES ===")
for theme, articles_list in theme_articles.items():
    if articles_list:
        filename = f"/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/theme_samples_{theme.replace('/', '_').replace('・', '_')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== {theme} ===\n\n")
            for i, article in enumerate(articles_list[:5]):
                f.write(f"Article {i+1}:\n")
                f.write(f"Title: {article.get('title', 'N/A')}\n")
                f.write(f"Date: {article.get('publishedAt', 'N/A')}\n")
                f.write(f"Tags: {', '.join(article.get('tags', []))}\n")
                f.write(f"\n{'='*80}\n\n")
        print(f"Saved: {filename}")

print("\nAnalysis complete!")
