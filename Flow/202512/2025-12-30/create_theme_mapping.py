#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
落合ノート記事のテーマ別グルーピング (T008-3)
全1,669記事を8つのテーマごとにグルーピングし、theme_mapping.yaml を作成する
"""

import json
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import unicodedata

# テーマ定義とキーワード（themes_list.mdより）
THEME_KEYWORDS = {
    'アート・メディア表現': [
        'アート', '写真', '表現', 'CCD', 'センサー', '美', 'エモ', '質量',
        '風景', 'カメラ', 'レンズ', '画像', '視覚', '光', '色', '撮影',
        'フィルム', '映像', 'メディア', '芸術', 'ボケ', '妖艶'
    ],
    '身体性・物質性': [
        '身体', '物質', '質量', '触覚', '視覚', '五感', 'メディア装置',
        '裸性', 'フィジカル', '肉体', 'マテリアル', '憧憬'
    ],
    'デジタルネイチャー': [
        'デジタルネイチャー', '計算機自然', '自然', '人工', '融合',
        'メタバース', 'VR', 'AR', 'XR', '空間コンピューティング',
        'バーチャル', '仮想空間', 'デジタルツイン', 'マタギドライヴ'
    ],
    '都市・空間デザイン': [
        '都市', '空間', 'セミパブリック', '建築', '場所', '風景',
        'まちづくり', '環境', 'ランドスケープ', '街', '景観',
        '教室', '学校'
    ],
    'AI技術の進化': [
        'AI', 'LLM', 'GPT', 'DeepSeek', 'Llama', 'オープンソース',
        '生成AI', '機械学習', 'ChatGPT', 'Claude', 'Gemini',
        'AIバブル', '大規模言語モデル', 'OpenAI', '言語モデル'
    ],
    '教育・研究の未来': [
        '教育', '学校', '研究', '大学', '学習', '知識',
        '学生', '授業', 'ラボ', '講義', '教室', '研究室'
    ],
    '未来予測・技術革新': [
        '未来', '予測', 'トレンド', '2030', '2035', 'シンギュラリティ',
        'カルロタ・ペレス', 'ペレス', '技術革命', '金融資本', 'イノベーション'
    ],
    '社会構造・公共財': [
        '社会', '資本主義', '公共財', 'インフラ', '革命', 'バブル',
        'コモディティ', '鉄道', '運河', '産業革命', '資本', '経済',
        'コモンズ', '公共'
    ]
}

def normalize_text(text):
    """Unicode正規化（NFC形式）"""
    return unicodedata.normalize('NFC', text)

def match_theme(title, tags):
    """タイトルとタグからテーマを判定（最初にマッチしたテーマを返す）"""
    # タイトルとタグを結合して検索対象テキストを作成
    search_text = title
    if tags:
        search_text += ' ' + ' '.join(tags)

    # 各テーマのキーワードでマッチング
    for theme, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            if keyword in search_text:
                return theme

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
    articles_dir = base_path / "full_run" / "articles"

    # テーマ別の記事リスト
    theme_mapping = defaultdict(list)

    # 統計情報
    total_count = 0
    error_count = 0

    # 全JSONファイルを処理
    for json_file in sorted(articles_dir.glob("*.json")):
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
                    'file_path': str(json_file.relative_to(base_path))
                }

                theme_mapping[theme].append(article_info)
                total_count += 1

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
        'description': '落合陽一note記事のテーマ別分類'
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
    print("テーマ別グルーピング結果")
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

    print("\n" + "="*80)

def main():
    """メイン処理"""
    # パス設定
    base_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note")
    output_path = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/theme_mapping.yaml")

    print("落合ノート記事のテーマ別グルーピングを開始します...")
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
