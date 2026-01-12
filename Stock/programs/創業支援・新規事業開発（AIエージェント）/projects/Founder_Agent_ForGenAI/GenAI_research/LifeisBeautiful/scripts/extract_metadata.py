#!/usr/bin/env python3
"""
LifeisBeautifulフォルダの全.mdファイルからYAML frontmatterメタデータを抽出してindex.yamlを生成
"""

import os
import yaml
import re
from pathlib import Path
from datetime import datetime
from collections import Counter

def extract_frontmatter(file_path):
    """ファイルからYAML frontmatterを抽出"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # YAML frontmatterを抽出（---で囲まれた部分）
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            metadata = yaml.safe_load(yaml_content)

            # 日付を文字列に統一
            if 'date' in metadata and metadata['date']:
                if isinstance(metadata['date'], datetime):
                    metadata['date'] = metadata['date'].strftime('%Y-%m-%d')
                elif not isinstance(metadata['date'], str):
                    metadata['date'] = str(metadata['date'])

            return metadata
        return None
    except Exception as e:
        print(f"⚠️  パースエラー: {file_path.name}")
        # エラー詳細は省略
        return None

def main():
    # 対象ディレクトリ
    target_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/LifeisBeautiful")

    # 除外ファイル
    exclude_files = {'_index.md', 'README.md', 'index.yaml'}

    # 全.mdファイルを取得
    md_files = [f for f in target_dir.glob('*.md') if f.name not in exclude_files]

    print(f"対象ファイル数: {len(md_files)}")

    # メタデータ収集
    files_data = []
    all_tags = []
    all_categories = set()

    for md_file in md_files:
        metadata = extract_frontmatter(md_file)
        if metadata:
            file_info = {
                'file': md_file.name,
                'title': metadata.get('title', ''),
                'date': metadata.get('date', ''),
                'author': metadata.get('author', ''),
                'newsletter_number': metadata.get('newsletter_number', ''),
                'tags': metadata.get('tags', []),
                'summary': metadata.get('summary', ''),
                'key_points': metadata.get('key_points', []),
                'topics': metadata.get('topics', [])
            }
            files_data.append(file_info)

            # タグとカテゴリを収集
            if metadata.get('tags'):
                all_tags.extend(metadata['tags'])

            # カテゴリ推定（タグから）
            for tag in metadata.get('tags', []):
                if any(keyword in tag for keyword in ['AI', 'LLM', 'DeepSeek', 'ChatGPT', 'Claude']):
                    all_categories.add('AI技術')
                elif any(keyword in tag for keyword in ['ビジネス', 'スタートアップ', '投資', 'Tesla', 'NVIDIA']):
                    all_categories.add('ビジネス戦略')
                elif any(keyword in tag for keyword in ['政策', '社会', '規制', '輸出管理']):
                    all_categories.add('社会・政策')
                elif any(keyword in tag for keyword in ['チップ', 'GPU', 'ハードウェア']):
                    all_categories.add('ハードウェア')
        else:
            print(f"メタデータなし: {md_file.name}")

    # 日付でソート
    files_data.sort(key=lambda x: x['date'] if isinstance(x['date'], str) else str(x['date']))

    # タグの集計
    tag_counts = Counter(all_tags)

    # 日付範囲を取得
    dates = [f['date'] for f in files_data if f['date']]
    date_range = f"{min(dates)} - {max(dates)}" if dates else "不明"

    # index.yamlの構造を作成
    index_data = {
        'collection': '週刊Life is beautiful Newsletter',
        'description': '中島聡氏による週刊ニュースレターのアーカイブ',
        'total_files': len(files_data),
        'date_range': date_range,
        'categories': sorted(list(all_categories)),
        'tags': dict(tag_counts.most_common(20)),  # 上位20タグ
        'files': files_data
    }

    # index.yamlを生成
    output_path = target_dir / 'index.yaml'
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(index_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"\n✅ index.yaml を生成しました: {output_path}")
    print(f"   総ファイル数: {len(files_data)}")
    print(f"   日付範囲: {date_range}")
    print(f"   カテゴリ数: {len(all_categories)}")
    print(f"   ユニークタグ数: {len(tag_counts)}")

if __name__ == '__main__':
    main()
