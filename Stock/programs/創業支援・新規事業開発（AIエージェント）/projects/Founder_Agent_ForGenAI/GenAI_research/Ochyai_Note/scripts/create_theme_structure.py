#!/usr/bin/env python3
"""
落合ノート テーマ別フォルダ構造作成スクリプト (T008-4)

目的:
- Analysis/Pattern_A_Themes/ 配下にテーマ別フォルダを作成
- 各テーマのREADME.mdとarticle_list.mdを生成
"""

from pathlib import Path
from datetime import datetime
import json
import re
from typing import Dict, List, Tuple
from collections import defaultdict

# ベースパス
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note")
ARTICLES_DIR = BASE_DIR / "full_run" / "articles"
ANALYSIS_DIR = BASE_DIR / "Analysis" / "Pattern_A_Themes"

# テーマ定義（8テーマ）
THEMES = {
    'Art_Media_Expression': {
        'ja': 'アート・メディア表現',
        'en': 'Art, Media & Expression',
        'description': 'アート、メディアアート、映像表現、視覚文化に関する考察',
        'keywords': ['アート', 'メディアアート', '映像', '表現', 'ビジュアル', 'インスタレーション', '展示', '作品', '美術', 'ギャラリー', '映画', '写真', 'カメラ', 'センサー']
    },
    'Digital_Nature': {
        'ja': 'デジタルネイチャー',
        'en': 'Digital Nature',
        'description': '計算機自然、デジタルと物理の融合、自然とテクノロジーの共存',
        'keywords': ['デジタルネイチャー', '計算機自然', 'コンピューテーショナル', 'シミュレーション', '拡張現実', 'AR', 'VR', 'メタバース', 'バーチャル']
    },
    'Physicality_Materiality': {
        'ja': '身体性・物質性',
        'en': 'Physicality & Materiality',
        'description': '身体感覚、触覚、物理的マテリアル、素材への関心',
        'keywords': ['身体', '触覚', '物質', 'マテリアル', '質量', '素材', '手触り', '感覚', '体験', 'ハプティック', 'インタラクション']
    },
    'Urban_Space_Design': {
        'ja': '都市・空間デザイン',
        'en': 'Urban & Space Design',
        'description': '都市計画、建築、空間設計、環境デザインに関する思考',
        'keywords': ['都市', '建築', '空間', 'デザイン', '街', '環境', '場所', 'ランドスケープ', '公共空間']
    },
    'AI_Technology': {
        'ja': 'AI技術の進化',
        'en': 'AI Technology Evolution',
        'description': '人工知能、機械学習、生成AI、技術的ブレークスルー',
        'keywords': ['AI', '人工知能', '機械学習', 'ディープラーニング', 'ChatGPT', 'GPT', 'LLM', '生成AI', 'アルゴリズム', 'ニューラル']
    },
    'Education_Research': {
        'ja': '教育・研究の未来',
        'en': 'Future of Education & Research',
        'description': '大学教育、研究環境、学びの未来、アカデミアの変革',
        'keywords': ['教育', '大学', '研究', 'アカデミア', '学生', '授業', 'ゼミ', '論文', '学会', '博士', '筑波', '学び']
    },
    'Future_Prediction': {
        'ja': '未来予測・技術革新',
        'en': 'Future Prediction & Innovation',
        'description': '未来予測、技術トレンド、イノベーション、パラダイムシフト',
        'keywords': ['未来', '予測', '10年後', '20年後', 'イノベーション', '革新', 'トレンド', '技術革命', 'パラダイム', '変革']
    },
    'Social_Structure': {
        'ja': '社会構造・公共財',
        'en': 'Social Structure & Public Goods',
        'description': '社会システム、公共財、政策、社会課題への提言',
        'keywords': ['社会', '公共', '政策', 'システム', '制度', '課題', '問題', '提言', 'インフラ', '公共財', '民主主義']
    }
}


def extract_date_from_filename(filename: str) -> str:
    """ファイル名から日付を抽出"""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else '不明'


def classify_article(article_path: Path) -> List[str]:
    """記事を読み込みテーマ分類（キーワードマッチング）"""
    try:
        content = article_path.read_text(encoding='utf-8')
        title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        title = title_match.group(1) if title_match else article_path.stem

        # 全テキストを対象にキーワードマッチング
        full_text = f"{title}\n{content}".lower()

        matched_themes = []
        for theme_id, theme_info in THEMES.items():
            # キーワードマッチングスコアを計算
            score = sum(1 for keyword in theme_info['keywords'] if keyword.lower() in full_text)
            if score >= 2:  # 2つ以上のキーワードがマッチしたらテーマに分類
                matched_themes.append(theme_id)

        # マッチしなかった場合のフォールバック
        if not matched_themes:
            # タイトルだけでも再チェック
            for theme_id, theme_info in THEMES.items():
                if any(keyword.lower() in title.lower() for keyword in theme_info['keywords'][:3]):
                    matched_themes.append(theme_id)
                    break

        return matched_themes if matched_themes else ['Art_Media_Expression']  # デフォルトはアート

    except Exception as e:
        print(f"⚠️  Error processing {article_path}: {e}")
        return ['Art_Media_Expression']


def analyze_articles() -> Dict[str, List[Dict]]:
    """全記事を分析してテーマ別に分類"""
    theme_articles = defaultdict(list)

    print(f"📂 Analyzing articles in {ARTICLES_DIR}...")

    article_files = sorted(ARTICLES_DIR.glob("*.md"))
    total = len(article_files)

    for idx, article_path in enumerate(article_files, 1):
        if idx % 100 == 0:
            print(f"   Progress: {idx}/{total}")

        date = extract_date_from_filename(article_path.name)
        themes = classify_article(article_path)

        article_info = {
            'filename': article_path.name,
            'date': date,
            'path': article_path,
            'relative_path': f"../../full_run/articles/{article_path.name}"
        }

        for theme in themes:
            theme_articles[theme].append(article_info)

    print(f"✅ Analyzed {total} articles")
    return theme_articles


def create_theme_folders():
    """テーマフォルダを作成"""
    print(f"\n📁 Creating theme folders in {ANALYSIS_DIR}...")

    for theme_id, theme_info in THEMES.items():
        folder_path = ANALYSIS_DIR / theme_id
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {theme_id}/")

    print("✅ Theme folders created")


def create_article_list(theme_id: str, articles: List[Dict]) -> str:
    """article_list.mdのコンテンツを生成"""
    theme_info = THEMES[theme_id]

    # 年別にグループ化
    by_year = defaultdict(list)
    for article in articles:
        year = article['date'][:4] if article['date'] != '不明' else '不明'
        by_year[year].append(article)

    content = f"""# {theme_info['ja']} - 関連記事一覧

**総記事数**: {len(articles)}件
**最終更新**: {datetime.now().strftime('%Y-%m-%d')}

## 記事リスト（日付降順）

"""

    # 年ごとにソートして出力
    for year in sorted(by_year.keys(), reverse=True):
        year_articles = sorted(by_year[year], key=lambda x: x['date'], reverse=True)
        content += f"\n### {year}年（{len(year_articles)}件）\n\n"

        for article in year_articles:
            # ファイル名からタイトル抽出
            title = article['filename'].replace('.md', '').split('_', 1)[1] if '_' in article['filename'] else article['filename']
            content += f"#### {article['date']}: {title}\n"
            content += f"- **ファイルパス**: `{article['relative_path']}`\n"
            content += f"- **ファイル名**: `{article['filename']}`\n\n"

    return content


def create_theme_readme(theme_id: str, articles: List[Dict]) -> str:
    """各テーマのREADME.mdのコンテンツを生成"""
    theme_info = THEMES[theme_id]

    # 統計情報
    total_articles = len(articles)
    dates = [a['date'] for a in articles if a['date'] != '不明']
    date_range = f"{min(dates)} ～ {max(dates)}" if dates else "不明"

    # 年別集計
    by_year = defaultdict(int)
    for article in articles:
        year = article['date'][:4] if article['date'] != '不明' else '不明'
        by_year[year] += 1

    # 代表記事（最新5件）
    top_articles = sorted(articles, key=lambda x: x['date'], reverse=True)[:5]

    content = f"""# {theme_info['ja']} - {theme_info['en']}

## 概要

{theme_info['description']}

## 統計

- **記事数**: {total_articles}件
- **期間**: {date_range}
- **全体比率**: 計算中

## 主要コンセプト

{theme_info['ja']}に関連する以下のような概念を扱っています：

"""

    # キーワードを3つずつ表示
    for i in range(0, min(9, len(theme_info['keywords'])), 3):
        keywords_chunk = theme_info['keywords'][i:i+3]
        content += f"- **{'・'.join(keywords_chunk)}**\n"

    content += f"""
## 代表記事（最新5件）

"""

    for idx, article in enumerate(top_articles, 1):
        title = article['filename'].replace('.md', '').split('_', 1)[1] if '_' in article['filename'] else article['filename']
        content += f"""### {idx}. {title}
- **日付**: {article['date']}
- **ファイル**: `{article['filename']}`

"""

    content += f"""## 関連記事リスト

全{total_articles}記事のリストは [article_list.md](./article_list.md) を参照。

## 時系列トレンド

"""

    for year in sorted(by_year.keys(), reverse=True):
        count = by_year[year]
        content += f"- **{year}年**: {count}件\n"

    content += f"""
## キーワード

"""

    for keyword in theme_info['keywords'][:15]:
        content += f"- {keyword}\n"

    content += """
## 分析メモ

このテーマに関する詳細な分析は今後追加予定です。

"""

    return content


def create_main_readme(theme_articles: Dict[str, List[Dict]]) -> str:
    """Pattern_A_Themes全体のREADME.mdを生成"""
    total_articles = sum(len(articles) for articles in theme_articles.values())

    # テーマ別記事数でソート
    sorted_themes = sorted(
        theme_articles.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    content = f"""# 落合ノート テーマ別分析（Pattern A）

**分析日**: {datetime.now().strftime('%Y-%m-%d')}
**総記事数**: {total_articles}件
**テーマ数**: {len(THEMES)}テーマ

## 分析概要

落合陽一氏のnote記事を8つの主要テーマに分類し、各テーマごとの特徴や時系列トレンドを分析しています。

## テーマ一覧

"""

    for idx, (theme_id, articles) in enumerate(sorted_themes, 1):
        theme_info = THEMES[theme_id]
        count = len(articles)
        percentage = (count / total_articles * 100) if total_articles > 0 else 0
        content += f"{idx}. [{theme_info['ja']}](./{theme_id}/) - {count}記事（{percentage:.1f}%）\n"

    content += f"""
## 使い方

各テーマフォルダに移動して、README.mdと article_list.md を参照してください。

### フォルダ構造

```
Pattern_A_Themes/
├── README.md                      # このファイル
├── Art_Media_Expression/          # アート・メディア表現
│   ├── README.md
│   └── article_list.md
├── Digital_Nature/                # デジタルネイチャー
│   ├── README.md
│   └── article_list.md
... (以下同様)
```

## テーマ定義

### 1. {THEMES['Art_Media_Expression']['ja']}
{THEMES['Art_Media_Expression']['description']}

### 2. {THEMES['Digital_Nature']['ja']}
{THEMES['Digital_Nature']['description']}

### 3. {THEMES['Physicality_Materiality']['ja']}
{THEMES['Physicality_Materiality']['description']}

### 4. {THEMES['Urban_Space_Design']['ja']}
{THEMES['Urban_Space_Design']['description']}

### 5. {THEMES['AI_Technology']['ja']}
{THEMES['AI_Technology']['description']}

### 6. {THEMES['Education_Research']['ja']}
{THEMES['Education_Research']['description']}

### 7. {THEMES['Future_Prediction']['ja']}
{THEMES['Future_Prediction']['description']}

### 8. {THEMES['Social_Structure']['ja']}
{THEMES['Social_Structure']['description']}

## 分析手法

記事内容のキーワードマッチングにより自動分類。1つの記事が複数のテーマに分類される場合があります。

## 次のステップ

- Pattern B: 時系列分析（過去・現在・未来）の実施
- テーマ間の関連性分析
- 主要概念の抽出と可視化

---

**生成日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**スクリプト**: create_theme_structure.py (T008-4)
"""

    return content


def main():
    """メイン処理"""
    print("=" * 60)
    print("  落合ノート テーマ別フォルダ構造作成")
    print("  Task: T008-4")
    print("=" * 60)

    # STEP 1: フォルダ作成
    create_theme_folders()

    # STEP 2: 記事分析
    theme_articles = analyze_articles()

    # STEP 3: 各テーマのREADMEとarticle_list作成
    print("\n📝 Creating theme documentation...")
    for theme_id, articles in theme_articles.items():
        theme_folder = ANALYSIS_DIR / theme_id

        # README.md作成
        readme_content = create_theme_readme(theme_id, articles)
        (theme_folder / "README.md").write_text(readme_content, encoding='utf-8')

        # article_list.md作成
        article_list_content = create_article_list(theme_id, articles)
        (theme_folder / "article_list.md").write_text(article_list_content, encoding='utf-8')

        print(f"   ✓ {theme_id}/ ({len(articles)} articles)")

    # STEP 4: 全体のREADME作成
    print("\n📝 Creating main README...")
    main_readme_content = create_main_readme(theme_articles)
    (ANALYSIS_DIR / "README.md").write_text(main_readme_content, encoding='utf-8')

    print("\n" + "=" * 60)
    print("✅ 完了！")
    print(f"📂 出力先: {ANALYSIS_DIR}")
    print("=" * 60)

    # サマリー出力
    print("\n📊 テーマ別記事数サマリー:")
    sorted_themes = sorted(
        theme_articles.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    for theme_id, articles in sorted_themes:
        theme_info = THEMES[theme_id]
        print(f"   {theme_info['ja']:20} : {len(articles):4}記事")


if __name__ == "__main__":
    main()
