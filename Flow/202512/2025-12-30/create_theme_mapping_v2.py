#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
落合ノート記事のテーマ別グルーピング (T008-3) - 改善版
全1,669記事を8つのテーマごとにグルーピングし、theme_mapping.yaml を作成する
"""

import json
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import unicodedata

# 拡張テーマ定義とキーワード（themes_list.mdより + タグベース）
THEME_KEYWORDS = {
    'アート・メディア表現': {
        'keywords': [
            'アート', '写真', '表現', 'CCD', 'センサー', '美', 'エモ', '質量',
            '風景', 'カメラ', 'レンズ', '画像', '視覚', '光', '色', '撮影',
            'フィルム', '映像', 'メディア', '芸術', 'ボケ', '妖艶', 'メディアアート',
            '個展', '展覧会', 'null²', 'ヌルヌル', '彫刻', '絵画', 'ビジュアル',
            '作品', '展示', 'アート展', '美術', '創作', '表現者', '芸術家',
            '美術館', 'ギャラリー', '茶道', '民藝', '縄文', '万博'
        ],
        'tags': [
            '#写真', '#メディアアート', '#アート', '#美', '#映像', '#表現',
            '#null2', '#expo2025'
        ]
    },
    '身体性・物質性': {
        'keywords': [
            '身体', '物質', '質量', '触覚', '視覚', '五感', 'メディア装置',
            '裸性', 'フィジカル', '肉体', 'マテリアル', '憧憬', '身体性',
            '物質性', '感覚'
        ],
        'tags': [
            '#裸性と身体性', '#質量', '#触覚', '#身体'
        ]
    },
    'デジタルネイチャー': {
        'keywords': [
            'デジタルネイチャー', '計算機自然', '自然', '人工', '融合',
            'メタバース', 'VR', 'AR', 'XR', '空間コンピューティング',
            'バーチャル', '仮想空間', 'デジタルツイン', 'マタギドライヴ',
            '計算機', 'デジタル', 'ネイチャー', 'ポストデジタル'
        ],
        'tags': [
            '#デジタルネイチャー', '#計算機自然', '#ポストデジタル',
            '#メタバース', '#VR', '#AR'
        ]
    },
    '都市・空間デザイン': {
        'keywords': [
            '都市', '空間', 'セミパブリック', '建築', '場所', '風景',
            'まちづくり', '環境', 'ランドスケープ', '街', '景観',
            '教室', '学校', '学び舎', '公共空間', '都市計画'
        ],
        'tags': [
            '#都市', '#空間', '#セミパブリック', '#建築', '#風景'
        ]
    },
    'AI技術の進化': {
        'keywords': [
            'AI', 'LLM', 'GPT', 'DeepSeek', 'Llama', 'オープンソース',
            '生成AI', '機械学習', 'ChatGPT', 'Claude', 'Gemini',
            'AIバブル', '大規模言語モデル', 'OpenAI', '言語モデル',
            '人工知能', 'ディープラーニング', 'ニューラルネット',
            'トランスフォーマー', 'AI時代'
        ],
        'tags': [
            '#AI', '#LLM', '#GPT', '#生成AI', '#機械学習', '#ChatGPT',
            '#DeepSeek', '#オープンソース'
        ]
    },
    '教育・研究の未来': {
        'keywords': [
            '教育', '学校', '研究', '大学', '学習', '知識',
            '学生', '授業', 'ラボ', '講義', '教室', '研究室',
            '筑波大', '東大', '教授', '博士', '論文', '学問',
            '学び', '教える', '研究者'
        ],
        'tags': [
            '#教育', '#研究', '#大学', '#学習', '#授業', '#ラボ'
        ]
    },
    '未来予測・技術革新': {
        'keywords': [
            '未来', '予測', 'トレンド', '2030', '2035', 'シンギュラリティ',
            'カルロタ・ペレス', 'ペレス', '技術革命', '金融資本', 'イノベーション',
            '未来予測', '技術トレンド', 'フォアキャスト', '将来'
        ],
        'tags': [
            '#未来', '#予測', '#2030', '#シンギュラリティ', '#イノベーション'
        ]
    },
    '社会構造・公共財': {
        'keywords': [
            '社会', '資本主義', '公共財', 'インフラ', '革命', 'バブル',
            'コモディティ', '鉄道', '運河', '産業革命', '資本', '経済',
            'コモンズ', '公共', '社会構造', '資本破壊', '債務', '人類学',
            '喫煙', 'タバコ', 'シーシャ', '外交', '歴史', '文化'
        ],
        'tags': [
            '#社会', '#資本主義', '#公共財', '#経済', '#インフラ', '#革命'
        ]
    }
}

def normalize_text(text):
    """Unicode正規化（NFC形式）"""
    return unicodedata.normalize('NFC', text)

def match_theme(title, tags):
    """タイトルとタグからテーマを判定（優先度順にマッチング）"""
    # タイトルとタグを結合して検索対象テキストを作成
    search_text = title.lower()
    tags_text = ' '.join(tags).lower() if tags else ''

    # 各テーマについてスコアリング
    theme_scores = {}

    for theme, config in THEME_KEYWORDS.items():
        score = 0

        # キーワードマッチング
        for keyword in config['keywords']:
            if keyword.lower() in search_text:
                score += 10  # タイトルマッチは高得点

        # タグマッチング
        for tag in config['tags']:
            if tag.lower() in tags_text:
                score += 5  # タグマッチは中得点

        theme_scores[theme] = score

    # 最高スコアのテーマを返す
    if max(theme_scores.values()) > 0:
        return max(theme_scores, key=theme_scores.get)

    return 'uncategorized'

def extract_date_from_filename(filename):
    """ファイル名から日付を抽出"""
    # ファイル名形式: 2019-01-06_タイトル.json
    parts = filename.split('_')
    if parts and len(parts[0]) == 10:  # YYYY-MM-DD
        return parts[0]
    return 'unknown'

def process_articles(base_path):
    """全記事を読み込んでテーマ別にグルーピング"""
    base_path = Path(base_path)

    # 複数のarticlesディレクトリをチェック
    articles_dirs = [
        base_path / "full_run" / "articles",
        base_path / "articles",  # ルートのarticlesもチェック
    ]

    # テーマ別の記事リスト
    theme_mapping = defaultdict(list)

    # 統計情報
    total_count = 0
    error_count = 0
    processed_files = set()  # 重複チェック用

    # 全JSONファイルを処理
    for articles_dir in articles_dirs:
        if not articles_dir.exists():
            continue

        for json_file in sorted(articles_dir.glob("*.json")):
            # 重複チェック（ファイル名ベース）
            if json_file.name in processed_files:
                continue

            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    title = normalize_text(data.get('title', ''))
                    published_at = data.get('published_at', '')
                    url = data.get('url', '')
                    tags = data.get('tags', [])

                    # 日付を取得（published_atまたはファイル名から）
                    if published_at:
                        date = published_at[:10]
                    else:
                        date = extract_date_from_filename(json_file.name)

                    # テーマを判定
                    theme = match_theme(title, tags)

                    # 記事情報を追加
                    article_info = {
                        'title': title,
                        'date': date,
                        'url': url,
                        'file_path': str(json_file.relative_to(base_path)),
                        'tags': tags[:5] if tags else []  # 最初の5タグのみ保存
                    }

                    theme_mapping[theme].append(article_info)
                    total_count += 1
                    processed_files.add(json_file.name)

            except Exception as e:
                error_count += 1
                print(f"エラー: {json_file.name} - {e}")

    return dict(theme_mapping), total_count, error_count

def create_theme_mapping_yaml(theme_mapping, total_count, output_path):
    """theme_mapping.yaml を作成"""

    # メタデータ
    metadata = {
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_articles': total_count,
        'themes': len(THEME_KEYWORDS),
        'description': '落合陽一note記事のテーマ別分類（改善版）',
        'version': '2.0'
    }

    # テーマごとの記事数を含む構造を作成
    themes_output = {}
    for theme in THEME_KEYWORDS.keys():
        articles = theme_mapping.get(theme, [])
        themes_output[theme] = {
            'article_count': len(articles),
            'articles': sorted(articles, key=lambda x: x['date'], reverse=True)
        }

    # uncategorizedも追加
    uncategorized = theme_mapping.get('uncategorized', [])
    themes_output['uncategorized'] = {
        'article_count': len(uncategorized),
        'articles': sorted(uncategorized, key=lambda x: x['date'], reverse=True)
    }

    # 最終出力
    output = {
        'metadata': metadata,
        'themes': themes_output
    }

    # YAMLファイルとして保存
    output_path = Path(output_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(output, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    return output_path

def print_statistics(theme_mapping, total_count):
    """統計情報を表示"""
    print("\n" + "="*80)
    print("テーマ別グルーピング結果 (改善版)")
    print("="*80)
    print(f"\n総記事数: {total_count}")
    print(f"\nテーマ別記事数:\n")

    for theme in THEME_KEYWORDS.keys():
        count = len(theme_mapping.get(theme, []))
        percentage = (count / total_count * 100) if total_count > 0 else 0
        print(f"  {theme:<20} : {count:>4}記事 ({percentage:>5.1f}%)")

    uncategorized_count = len(theme_mapping.get('uncategorized', []))
    uncategorized_percentage = (uncategorized_count / total_count * 100) if total_count > 0 else 0
    print(f"  {'uncategorized':<20} : {uncategorized_count:>4}記事 ({uncategorized_percentage:>5.1f}%)")

    # カバレッジ
    categorized_count = total_count - uncategorized_count
    coverage = (categorized_count / total_count * 100) if total_count > 0 else 0
    print(f"\nカバレッジ: {coverage:.1f}% ({categorized_count}/{total_count}記事)")

    print("\n" + "="*80)

def main():
    """メイン処理"""
    # パス設定
    base_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note")
    output_path = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/theme_mapping.yaml")

    print("落合ノート記事のテーマ別グルーピング（改善版）を開始します...")
    print(f"対象ディレクトリ: {base_path}")

    # 記事を処理
    theme_mapping, total_count, error_count = process_articles(base_path)

    # YAML作成
    output_file = create_theme_mapping_yaml(theme_mapping, total_count, output_path)

    # 統計表示
    print_statistics(theme_mapping, total_count)

    if error_count > 0:
        print(f"\n警告: {error_count}件のエラーが発生しました")

    print(f"\n出力ファイル: {output_file}")
    print("\n完了しました。")

if __name__ == "__main__":
    main()
