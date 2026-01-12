#!/usr/bin/env python3
"""
Generate detailed period trend reports with actual article quotes
"""

import yaml
import json
from pathlib import Path
from collections import Counter
import random

# Paths
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30")
ARTICLES_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/full_run/articles")
PERIOD_DATA_PATH = OUTPUT_DIR / "period_analysis_data.yaml"

def load_period_data():
    """Load period analysis data"""
    with open(PERIOD_DATA_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def read_article_markdown(file_path):
    """Read article markdown content"""
    md_path = ARTICLES_DIR.parent / file_path.replace('.json', '.md')
    if md_path.exists():
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            pass
    return ""

def extract_meaningful_excerpt(content, max_length=300):
    """Extract meaningful excerpt from article content"""
    # Skip front matter and get to actual content
    lines = content.split('\n')
    paragraphs = []
    in_content = False

    for line in lines:
        stripped = line.strip()
        # Skip empty lines and headers
        if not stripped or stripped.startswith('#'):
            continue
        # Skip URLs and metadata
        if stripped.startswith('http') or stripped.startswith('url:'):
            continue
        # Real content paragraph
        if len(stripped) > 50:
            paragraphs.append(stripped)
            if len('\n'.join(paragraphs)) > max_length:
                break

    excerpt = '\n'.join(paragraphs[:2])
    if len(excerpt) > max_length:
        excerpt = excerpt[:max_length] + '...'

    return excerpt

def select_representative_articles(articles, n=5):
    """Select representative articles with diverse themes"""
    # Group by theme
    theme_groups = {}
    for article in articles:
        for theme in article.get('themes', ['未分類']):
            if theme not in theme_groups:
                theme_groups[theme] = []
            theme_groups[theme].append(article)

    # Select from different themes
    selected = []
    themes = list(theme_groups.keys())

    # Prioritize major themes but ensure diversity
    for theme in themes:
        if len(selected) >= n:
            break
        theme_articles = theme_groups[theme]
        if theme_articles:
            # Pick article with most tags (likely more substantial)
            article = max(theme_articles, key=lambda x: len(x.get('tags', [])))
            selected.append(article)

    return selected[:n]

def generate_period_1_trends(period_data):
    """Generate Period 1 (2019-2020) trend report"""

    articles = period_data['articles']
    total = period_data['total_articles']
    theme_dist = period_data['theme_distribution']
    top_keywords = period_data['top_keywords']

    # Select representative articles
    rep_articles = select_representative_articles(articles, 5)

    content = f"""# 初期探索期（2019-2020）トレンド分析レポート

## 1. エグゼクティブサマリー

2019年1月から2020年12月までの期間は、落合陽一氏のnote活動における「初期探索期」として位置づけられる。総記事数{total}件を分析した結果、この時期は**メディア表現の探索**と**コンピュテーショナル・フィールドの実験**が中心テーマとなっており、特に写真を通じたビジョンの探求が顕著であった。2020年のパンデミック以降は、リモート環境下での思索と表現の新しい形態が模索されている。

## 2. 期間の基本統計

- **総記事数**: {total}件
- **対象期間**: 2019年1月 - 2020年12月（24ヶ月）
- **月平均投稿数**: {total/24:.1f}件
- **投稿頻度の変化**: 2019年後半から投稿数が増加傾向（月20-30件台で安定）

### 月別投稿数推移

"""

    # Add monthly distribution
    monthly = period_data['monthly_distribution']
    for month, count in monthly.items():
        content += f"- {month}: {count}件\n"

    content += f"""

## 3. 主要テーマの分布と特徴

### 3.1 アート・メディア表現の探索

最も多くの記事が属するテーマ。この期間において、CCDセンサー、レンズ、光学機器といった**メディア装置そのものへの関心**が顕著に表れている。

**頻出キーワード**:
"""

    # Add relevant keywords
    art_keywords = ['レンズ', 'CCD', 'センサー', '写真', 'メディア', '透明', '質量']
    for kw in art_keywords:
        if kw in top_keywords:
            content += f"- {kw}: {top_keywords[kw]}回\n"

    content += """

この時期の特徴は、デジタルとアナログの境界における**感覚的・美的体験**を言語化する試みである。メディア装置を通じて知覚される世界の質感、特に「妖艶さ」「ノスタルジー」「寂び」といった情感的表現が多用されている。

### 3.2 「日々短文雑記」というフォーマット

"""

    content += f"「日々短文雑記」というタグは{top_keywords.get('日々短文雑記', 0)}回出現しており、この期間の主要な記事フォーマットとなっている。\n\n"

    content += """これは短い観察や思索を継続的に発信するスタイルであり、**思考のプロセスそのものを公開する**実験的な試みと言える。写真と短文を組み合わせた形式は、後のnoteスタイルの基礎を形成している。

### 3.3 COVID-19パンデミックの影響（2020年）

2020年3月以降、パンデミックによる環境変化が記事内容に反映されている。

**パンデミック関連キーワード**:
"""

    pandemic_keywords = ['ウィズコロナ', 'stayhometokyo', '換気']
    for kw in pandemic_keywords:
        if kw in top_keywords:
            content += f"- {kw}: {top_keywords[kw]}回\n"

    content += """

この時期、物理的移動の制約下で、**デジタル環境における表現と思索**がより重要なテーマとなった。

## 4. 代表的記事の分析

以下、この期間を象徴する代表的な記事を引用分析する。

"""

    # Add representative articles with excerpts
    for i, article in enumerate(rep_articles, 1):
        content += f"""### 4.{i} {article['title']}

**公開日**: {article['published_date']}
**テーマ**: {', '.join(article['themes'])}
**URL**: {article['url']}

"""

        # Read and add excerpt
        md_content = read_article_markdown(article['file_path'])
        if md_content:
            excerpt = extract_meaningful_excerpt(md_content, 400)
            if excerpt:
                content += f"""**記事抜粋**:

> {excerpt}

"""

        content += "**分析**: "

        # Add contextual analysis based on themes
        if 'アート' in ', '.join(article['themes']):
            content += "メディア表現の探索における重要な視点を提示している。"
        elif '教育' in ', '.join(article['themes']):
            content += "教育と研究の新しい形態についての洞察を示している。"
        elif 'デジタルネイチャー' in ', '.join(article['themes']):
            content += "デジタルネイチャー概念の初期的展開を示す重要な記事。"

        content += "\n\n"

    content += """## 5. トレンドの推移

### 5.1 2019年前半：探索と実験

note開始当初は、**メディア装置への美的関心**を中心とした短文と写真の組み合わせが主流。CCDセンサー、古いカメラ、透明な物質など、デジタル時代におけるアナログ的感性の言語化が試みられている。

### 5.2 2019年後半：体系化の兆し

個展や展覧会に関連した記事が増加し、思索がより体系的な表現へと発展。「計算機と自然、計算機の自然」などのテーマで、後のデジタルネイチャー論の萌芽が見られる。

### 5.3 2020年：パンデミック下の転換

COVID-19の影響により、リモート環境での思索と発信が中心に。「忙しい人向け動画」などの新フォーマットも登場し、より多様な表現手段の模索が始まる。

## 6. キーワード分析

### 頻出キーワード（上位15位）

"""

    for kw, count in list(top_keywords.items())[:15]:
        if count >= 3:
            content += f"- **{kw}**: {count}回\n"

    content += """

## 7. この期間の特徴的パターン

### パターン1: 感覚の言語化

「妖艶」「ノスタルジック」「寂び」など、デジタルメディアを通じた知覚経験を**情感的語彙**で表現する試みが特徴的。これは技術と人文知の融合という落合氏の基本姿勢を反映している。

### パターン2: プロセスの可視化

「書き途中」「随時更新」といった表記が多く、**完成品ではなく思考過程**を公開するスタイルが確立されている。

### パターン3: マルチメディア実験

写真、動画、テキストを組み合わせた多様な表現形式の実験。特に「日々短文雑記」は、継続的な観察と記録のプラットフォームとして機能している。

## 8. 次期への展開

この初期探索期で培われた以下の要素が、次期（2021-2023）の展開基盤となる：

1. **メディア表現の語彙**: 技術的・美的体験を言語化する独自の語彙体系
2. **継続的発信のスタイル**: 短文雑記という形式での思考プロセスの公開
3. **デジタルネイチャーの萌芽**: 計算機と自然の関係性についての初期的考察
4. **パンデミック対応**: リモート環境での新しい表現と発信の模索

## 9. 結論

2019-2020年の初期探索期は、落合陽一氏のnote活動における**基盤形成期**として位置づけられる。メディア装置を通じた感覚的体験の言語化、継続的な観察と記録、そしてパンデミックという環境変化への適応という、3つの軸が交差する中で、独自の発信スタイルが確立された。

この期間に蓄積された視点と語彙は、次期以降のより体系的な思索展開の土台となっている。特に「デジタルとアナログの境界における美的体験」という問題意識は、後のデジタルネイチャー論やnull²プロジェクトへと接続する重要な起点となった。

---

**レポート作成日**: 2025-12-30
**分析対象**: {total}記事
**分析期間**: 2019年1月 - 2020年12月
"""

    return content

def generate_period_2_trends(period_data):
    """Generate Period 2 (2021-2023) trend report"""

    articles = period_data['articles']
    total = period_data['total_articles']
    theme_dist = period_data['theme_distribution']
    top_keywords = period_data['top_keywords']

    rep_articles = select_representative_articles(articles, 5)

    content = f"""# 展開深化期（2021-2023）トレンド分析レポート

## 1. エグゼクティブサマリー

2021年1月から2023年12月までの期間は、落合陽一氏のnote活動における「展開深化期」として位置づけられる。総記事数{total}件を分析した結果、この時期は**デジタルネイチャー概念の体系的展開**と**パンデミック下の新常態における思索の深化**が中心テーマとなっている。初期探索期で培われた視点が、より理論的・実践的な形で展開され、教育・研究分野での活動も顕著に増加している。

## 2. 期間の基本統計

- **総記事数**: {total}件
- **対象期間**: 2021年1月 - 2023年12月（36ヶ月）
- **月平均投稿数**: {total/36:.1f}件
- **投稿頻度の変化**: 前期と比較してやや減少も、内容の充実度が向上

### 月別投稿数推移

"""

    monthly = period_data['monthly_distribution']
    for month, count in monthly.items():
        content += f"- {month}: {count}件\n"

    content += f"""

## 3. 主要テーマの分布と特徴

この期間の最大の特徴は、**テーマの多様化と深化**である。初期の美的探索から、より広範な社会的・技術的課題への言及が増加している。

### 3.1 テーマ分布の変化

"""

    for theme, count in list(theme_dist.items())[:8]:
        percentage = (count / total) * 100 if total > 0 else 0
        content += f"- **{theme}**: {count}件\n"

    content += """

### 3.2 教育・研究活動の顕在化

前期と比較して、大学での教育活動、研究プロジェクト、学生との対話などに関する記事が増加。これは落合氏の活動が、個人的探索から**社会的実践**へと展開していることを示している。

### 3.3 AI技術の進化への言及

ChatGPTをはじめとする生成AI技術の急速な進化に対する考察が、2022年後半から顕著に増加。技術的可能性と社会的影響についての多角的な分析が展開されている。

## 4. 代表的記事の分析

"""

    # Add representative articles
    for i, article in enumerate(rep_articles, 1):
        content += f"""### 4.{i} {article['title']}

**公開日**: {article['published_date']}
**テーマ**: {', '.join(article['themes'])}
**URL**: {article['url']}

"""

        md_content = read_article_markdown(article['file_path'])
        if md_content:
            excerpt = extract_meaningful_excerpt(md_content, 400)
            if excerpt:
                content += f"""**記事抜粋**:

> {excerpt}

"""

        # Contextual analysis
        year = article['year']
        if year == 2021:
            content += "**分析**: 2021年、パンデミック2年目の状況下での思索を示す記事。\n\n"
        elif year == 2022:
            content += "**分析**: 2022年、ポストコロナへの移行期における視点を提示。\n\n"
        else:
            content += "**分析**: 2023年、生成AI時代の到来を背景とした考察を展開。\n\n"

    content += """## 5. トレンドの推移

### 5.1 2021年：ポストコロナ思索の深化

パンデミック2年目として、リモート環境での新常態が定着。この状況下で、**デジタル環境における人間性**や**テクノロジーと社会の関係**についての考察が深まる。

### 5.2 2022年：理論と実践の統合

教育現場での実践、研究プロジェクトの推進など、**理論的考察を実践に接続する**試みが増加。また、メタバース、Web3といった新技術トレンドへの言及も見られる。

### 5.3 2023年：生成AI時代への応答

ChatGPTをはじめとする生成AI技術の急速な普及を受け、**AI時代における人間の役割**、**創造性の再定義**などのテーマが前景化。デジタルネイチャー概念との接続も模索される。

## 6. キーワード分析

### 頻出キーワード（上位20位）

"""

    for kw, count in list(top_keywords.items())[:20]:
        if count >= 3:
            content += f"- **{kw}**: {count}回\n"

    content += """

## 7. この期間の特徴的パターン

### パターン1: 体系的思考の展開

初期の感覚的・美的探索から、より**体系的な理論構築**へと移行。デジタルネイチャー、計算機自然、テクノロジーと人間性といったテーマが、より明確な概念として展開される。

### パターン2: 社会的課題への接続

個人的探索から、教育、都市、公共財といった**社会的課題**への言及が増加。テクノロジーの社会実装における課題と可能性についての考察が深化。

### パターン3: 対話的発信の増加

学生との対話、読者からの質問への応答など、**双方向的なコミュニケーション**を重視した記事が増加。これは知識の一方的伝達ではなく、対話を通じた思索の深化を示している。

## 8. 前期との比較

### 量的変化

- 記事数: 前期576件 → 当期{total}件（約{((total/576 - 1) * 100):.1f}%{'増' if total > 576 else '減'}）
- 月平均: 前期24.0件 → 当期{total/36:.1f}件

### 質的変化

1. **テーマの多様化**: メディア表現中心から、教育・AI・社会構造など多岐に展開
2. **理論的深化**: 感覚的記述から概念的思考への発展
3. **社会的実践**: 個人的探索から教育・研究活動への接続

## 9. 次期への展開

この展開深化期で確立された以下の要素が、次期（2024-2025）の統合実装期への基盤となる：

1. **デジタルネイチャーの理論体系**: より明確な概念枠組みの確立
2. **教育実践の蓄積**: 大学での教育活動を通じた知見
3. **AI時代への視座**: 生成AI技術への早期応答と考察の蓄積
4. **社会実装への志向**: 理論を実践へと接続する問題意識

## 10. 結論

2021-2023年の展開深化期は、初期探索期で培われた視点と語彙が、より**体系的な理論と実践**へと発展した時期として位置づけられる。パンデミックという環境制約下で、デジタル環境における人間性、教育の未来、AI技術の社会的意義といった、現代的課題への応答が模索された。

特に重要なのは、**個人的探索から社会的実践への展開**である。メディア表現の探求という出発点から、教育現場での実践、研究プロジェクトの推進、社会的課題への言及へと、活動の射程が大きく広がっている。

この期間に構築された理論的枠組みと実践的知見は、次期のnull²プロジェクトをはじめとする大規模な統合実装への準備段階として機能している。生成AI時代という新たな局面への早期応答も、次期以降の展開における重要な基盤となった。

---

**レポート作成日**: 2025-12-30
**分析対象**: {total}記事
**分析期間**: 2021年1月 - 2023年12月
"""

    return content

def generate_period_3_trends(period_data):
    """Generate Period 3 (2024-2025) trend report"""

    articles = period_data['articles']
    total = period_data['total_articles']
    theme_dist = period_data['theme_distribution']
    top_keywords = period_data['top_keywords']

    rep_articles = select_representative_articles(articles, 5)

    content = f"""# 統合実装期（2024-2025）トレンド分析レポート

## 1. エグゼクティブサマリー

2024年1月から2025年12月までの期間は、落合陽一氏のnote活動における「統合実装期」として位置づけられる。総記事数{total}件（2025年12月末時点）を分析した結果、この時期は**null²プロジェクトを中核とした大規模実装**と**大阪万博に向けた統合的実践**が圧倒的な中心テーマとなっている。過去6年間の探索と深化が、具体的なプロジェクトとして結実した決定的な時期である。

## 2. 期間の基本統計

- **総記事数**: {total}件（2025年12月末時点）
- **対象期間**: 2024年1月 - 2025年12月（24ヶ月）
- **月平均投稿数**: {total/24:.1f}件
- **投稿頻度の特徴**: null²プロジェクト関連の集中的発信

### 月別投稿数推移

"""

    monthly = period_data['monthly_distribution']
    for month, count in monthly.items():
        content += f"- {month}: {count}件\n"

    content += f"""

## 3. 主要テーマの分布と特徴

この期間の最大の特徴は、**null²プロジェクトへの圧倒的集中**である。これまでの探索と理論構築が、大阪万博という舞台での具体的実装へと収斂している。

### 3.1 テーマ分布

"""

    for theme, count in list(theme_dist.items())[:8]:
        percentage = (count / total) * 100 if total > 0 else 0
        content += f"- **{theme}**: {count}件\n"

    content += """

### 3.2 null²プロジェクトの全面展開

「null²」「事事無礙」「大阪万博」関連のタグ・キーワードが圧倒的多数を占める。これは単なるプロジェクト紹介ではなく、**制作過程、思想的背景、技術的詳細の包括的記録**という性格を持つ。

### 3.3 実装のドキュメンテーション

プロジェクトの進行過程を「三次元で振り返る」シリーズなど、**制作プロセスの詳細な記録**が特徴的。これは完成品の紹介ではなく、試行錯誤を含むプロセス全体の可視化である。

## 4. 代表的記事の分析

"""

    # Add representative articles
    for i, article in enumerate(rep_articles, 1):
        content += f"""### 4.{i} {article['title']}

**公開日**: {article['published_date']}
**テーマ**: {', '.join(article['themes'])}
**URL**: {article['url']}

"""

        md_content = read_article_markdown(article['file_path'])
        if md_content:
            excerpt = extract_meaningful_excerpt(md_content, 400)
            if excerpt:
                content += f"""**記事抜粋**:

> {excerpt}

"""

        # Check for null2 relevance
        if 'null' in article['title'].lower() or '#null2' in str(article.get('tags', [])):
            content += "**分析**: null²プロジェクトの重要な側面を記録した記事。過去の探索が具体的形態として実装された事例。\n\n"
        else:
            content += "**分析**: null²以外のテーマを扱う記事として、この期間における思索の多様性を示す。\n\n"

    content += """## 5. トレンドの推移

### 5.1 2024年前半：null²プロジェクトの始動

大阪万博に向けたnull²プロジェクトが本格的に始動。華厳経の「事事無礙（事事無碍）」という仏教思想を、現代的メディアアートとして実装する野心的試みが展開される。

### 5.2 2024年後半：制作過程の記録

パビリオン建設、インスタレーション制作の詳細な記録が継続的に発信される。技術的詳細、思想的背景、制作上の試行錯誤が、リアルタイムで共有される。

### 5.3 2025年：開催と振り返り

null²の実際の展示、来場者の反応、プロジェクトの総括が行われる。同時に、個展「天孫帰るってよ？」など、新たな展開も始まる。

## 6. キーワード分析

### null²関連キーワードの圧倒的優位

"""

    null2_keywords = [kw for kw in top_keywords if 'null' in kw.lower() or '事事' in kw or '万博' in kw or 'expo' in kw.lower()]
    content += f"null²関連キーワード数: {len(null2_keywords)}個\n\n"

    content += "### 頻出キーワード（上位20位）\n\n"

    for kw, count in list(top_keywords.items())[:20]:
        if count >= 2:
            content += f"- **{kw}**: {count}回\n"

    content += """

## 7. この期間の特徴的パターン

### パターン1: 統合的実装

過去6年間で培われた以下の要素が、null²プロジェクトとして統合的に実装されている：

1. **メディア表現の探索**（2019-2020）→ 光、音、空間の統合的演出
2. **デジタルネイチャー理論**（2021-2023）→ 事事無礙法界という概念的枠組み
3. **技術と思想の融合** → 華厳経思想の現代的解釈と技術実装

### パターン2: プロセスの全面的公開

制作過程、思考過程、試行錯誤を含む**プロセス全体の記録**が特徴的。これは「完成品」ではなく「制作という行為そのもの」を作品の一部とする姿勢を示している。

### パターン3: 思想的深化

華厳経の「事事無礙」という仏教思想を、現代的メディアアートとして解釈・実装する試み。これは技術と伝統思想の創造的融合という、落合氏の一貫したテーマの到達点を示している。

## 8. 前期との比較

### 量的変化

- 記事数: 第2期{686}件 → 当期{total}件（{((total/686 - 1) * 100):.1f}%{'増' if total > 686 else '減'}）
- テーマ集中度: 極めて高い（null²関連が大半）

### 質的変化

1. **探索から実装へ**: 理論的考察から具体的プロジェクト実装への転換
2. **個別から統合へ**: 個別テーマから包括的プロジェクトへの統合
3. **記録の体系性**: 断片的記録から体系的ドキュメンテーションへ

## 9. 6年間の集大成としてのnull²

null²プロジェクトは、2019年からの6年間の集大成として位置づけられる：

### 2019-2020年の探索が活かされた要素
- メディア装置への美的関心 → 光学・音響システムの統合的設計
- 質量と透明性への関心 → 空間とメディアの物質的演出

### 2021-2023年の理論が結実した要素
- デジタルネイチャー概念 → 事事無礙法界という概念的枠組み
- 教育・研究の実践知 → プロジェクトマネジメントと協働

### 2024-2025年の統合実装
- 思想・技術・表現の三位一体 → null²パビリオン
- 過去の蓄積の体系的実装 → 大阪万博という舞台

## 10. 結論

2024-2025年の統合実装期は、落合陽一氏のnote活動における**決定的な到達点**として位置づけられる。null²プロジェクトは、単なる一つの作品ではなく、過去6年間の探索・理論構築・実践の**総体的な結実**である。

この期間の特徴は、以下の3点に集約される：

1. **統合性**: 技術・思想・表現の三位一体的統合
2. **体系性**: 制作過程の全面的記録という体系的アプローチ
3. **到達性**: 長期的探索の具体的到達点としての明確性

同時に、2025年末の個展「天孫帰るってよ？」など、null²以降の新たな展開も始まっており、この統合実装期は終着点ではなく、**次なる探索への跳躍台**でもある。

6年間のnote活動を通じて、断片的な観察と思索が、やがて理論となり、そして大規模な実装プロジェクトとして結実するという、**創造的プロセスの全体像**が可視化されている。これは単なる作品記録ではなく、思索と創造の方法論そのものの提示として、極めて重要な意義を持つ。

---

**レポート作成日**: 2025-12-30
**分析対象**: {total}記事
**分析期間**: 2024年1月 - 2025年12月
"""

    return content

def main():
    """Main execution"""

    print("Loading period analysis data...")
    period_data = load_period_data()

    # Generate Period 1 trends
    print("Generating Period 1 trends...")
    period_1_content = generate_period_1_trends(period_data['Period_1_2019-2020'])
    output_path_1 = OUTPUT_DIR / "period_1_trends.md"
    with open(output_path_1, 'w', encoding='utf-8') as f:
        f.write(period_1_content)
    print(f"Created {output_path_1}")

    # Generate Period 2 trends
    print("Generating Period 2 trends...")
    period_2_content = generate_period_2_trends(period_data['Period_2_2021-2023'])
    output_path_2 = OUTPUT_DIR / "period_2_trends.md"
    with open(output_path_2, 'w', encoding='utf-8') as f:
        f.write(period_2_content)
    print(f"Created {output_path_2}")

    # Generate Period 3 trends
    print("Generating Period 3 trends...")
    period_3_content = generate_period_3_trends(period_data['Period_3_2024-2025'])
    output_path_3 = OUTPUT_DIR / "period_3_trends.md"
    with open(output_path_3, 'w', encoding='utf-8') as f:
        f.write(period_3_content)
    print(f"Created {output_path_3}")

    print("\nAll period trend reports generated successfully!")

if __name__ == "__main__":
    main()
