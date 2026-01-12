import json
import glob
from pathlib import Path
from collections import Counter
import re

# 全JSONファイルを読み込む
base_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note")

articles = []
all_titles = []
all_tags = []
all_dates = []

print("Reading JSON files...")
for json_file in base_path.rglob("*.json"):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            articles.append(data)
            all_titles.append(data.get('title', ''))
            all_tags.extend(data.get('tags', []))
            all_dates.append(data.get('publishedAt', ''))
    except Exception as e:
        print(f"Error reading {json_file}: {e}")

print(f"\nTotal articles: {len(articles)}")
print(f"Total tags collected: {len(all_tags)}")

# タグ集計
tag_counter = Counter(all_tags)
print(f"Unique tags: {len(tag_counter)}")
print(f"\nTop 30 tags:")
for tag, count in tag_counter.most_common(30):
    print(f"  {tag}: {count}")

# タイトルのキーワード分析（頻出パターン）
keyword_patterns = {
    'AI技術の進化': ['AI', 'LLM', 'GPT', 'DeepSeek', '生成AI', '機械学習', 'オープンソース', 'Llama', 'Claude', 'ChatGPT', 'Gemini', 'AIバブル', '大規模言語モデル'],
    'デジタルツイン/メタバース': ['デジタルツイン', 'メタバース', 'VR', 'AR', 'XR', '空間コンピューティング', 'バーチャル', '仮想空間', 'アバター'],
    '未来予測手法': ['未来', '予測', 'トレンド', '2030', '2035', 'シンギュラリティ', 'カルロタ・ペレス', '技術革命', '金融資本'],
    '社会構造の変化': ['社会', '資本主義', '公共財', 'インフラ', '革命', 'バブル', 'コモディティ', '鉄道', '運河', '産業革命'],
    'アート・メディア表現': ['質量', 'アート', '写真', '表現', '美', 'エモ', 'センサー', '映像', 'メディア', '芸術', 'カメラ'],
    '都市・空間デザイン': ['都市', '空間', 'セミパブリック', '風景', '建築', '場所', 'まちづくり', '環境', 'ランドスケープ'],
    '教育・研究の未来': ['教育', '学校', '研究', '学習', '大学', '学生', '授業', '知識'],
}

theme_counts = {theme: 0 for theme in keyword_patterns}
theme_articles = {theme: [] for theme in keyword_patterns}

for idx, title in enumerate(all_titles):
    for theme, keywords in keyword_patterns.items():
        if any(kw in title for kw in keywords):
            theme_counts[theme] += 1
            if len(theme_articles[theme]) < 10:  # 各テーマ最大10記事保存
                theme_articles[theme].append({
                    'title': title,
                    'date': all_dates[idx] if idx < len(all_dates) else '',
                    'tags': articles[idx].get('tags', []) if idx < len(articles) else []
                })

print("\n\n=== Theme Distribution ===")
for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"\n{theme}: {count} articles")
    print(f"  Sample titles:")
    for i, article in enumerate(theme_articles[theme][:3]):
        print(f"    {i+1}. {article['title'][:80]}")

# 日付分析（期間の確認）
valid_dates = [d for d in all_dates if d]
if valid_dates:
    print(f"\n\n=== Date Range ===")
    print(f"Earliest: {min(valid_dates)}")
    print(f"Latest: {max(valid_dates)}")

# 年ごとの分布
year_counter = Counter()
for date in valid_dates:
    if date:
        year = date[:4]
        year_counter[year] += 1

print(f"\n=== Articles by Year ===")
for year, count in sorted(year_counter.items()):
    print(f"  {year}: {count}")
