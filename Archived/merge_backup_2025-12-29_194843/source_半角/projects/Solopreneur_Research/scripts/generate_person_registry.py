#!/usr/bin/env python3
"""
Person Registry Generator

全カテゴリ（App/Newsletter/SNS）のケーススタディから人物情報を抽出し、
統合Person Registryを生成します。

Usage:
    python3 scripts/generate_person_registry.py

Output:
    - documents/_registry/person_registry.md
    - analysis/quality_scores/person_registry_stats.csv
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime

# ディレクトリパス
BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "documents"
APP_DIR = DOCS_DIR / "01_App" / "case_studies"
NEWSLETTER_DIR = DOCS_DIR / "02_Newsletter" / "case_studies"
SNS_DIR = DOCS_DIR / "03_SNS"
REGISTRY_DIR = DOCS_DIR / "_registry"
ANALYSIS_DIR = BASE_DIR / "analysis" / "quality_scores"

def extract_yaml_frontmatter(filepath):
    """YAMLフロントマターを抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                return yaml.safe_load(match.group(1))
    except Exception as e:
        print(f"Warning: Failed to parse YAML in {filepath}: {e}")
    return None

def extract_sns_info_from_text(filepath):
    """SNS analysisファイルからテキスト情報を抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

            # 基本情報テーブルから抽出
            name_match = re.search(r'\|\s*\*\*人物名\*\*\s*\|\s*([^|]+?)\s*\|', content)
            handle_match = re.search(r'\|\s*\*\*ハンドル\*\*\s*\|\s*(@\w+)', content)

            name = name_match.group(1).strip() if name_match else None
            handle = handle_match.group(1).strip() if handle_match else None

            return {'name': name, 'twitter_handle': handle}
    except Exception as e:
        print(f"Warning: Failed to extract SNS info from {filepath}: {e}")
    return None

def normalize_twitter_handle(handle):
    """Twitter handleを正規化"""
    if not handle:
        return None
    handle = str(handle).strip().lower()
    handle = re.sub(r'^@', '', handle)
    handle = re.sub(r'[^a-z0-9_]', '', handle)
    return handle if handle and len(handle) > 0 else None

def scan_app_cases():
    """App case studiesをスキャン"""
    persons = defaultdict(lambda: {
        'names': set(),
        'twitter_handles': set(),
        'app_ids': [],
        'newsletter_ids': [],
        'sns_ids': [],
        'metadata': {}
    })

    print(f"Scanning App case studies in {APP_DIR}...")
    if not APP_DIR.exists():
        print(f"Warning: {APP_DIR} does not exist")
        return persons

    for file in APP_DIR.glob("*.md"):
        data = extract_yaml_frontmatter(file)
        if data and 'subject' in data:
            subject = data['subject']
            name = subject.get('name')
            twitter = normalize_twitter_handle(subject.get('twitter_handle'))

            if twitter:
                key = f"@{twitter}"
                persons[key]['names'].add(name)
                persons[key]['twitter_handles'].add(twitter)
                persons[key]['app_ids'].append({
                    'id': data.get('id'),
                    'role': 'founder',
                    'product': data.get('main_product', {}).get('name')
                })
                if 'nationality' in subject:
                    persons[key]['metadata']['nationality'] = subject['nationality']
                if 'japan_score' in data:
                    persons[key]['metadata']['japan_relevance'] = data['japan_score'].get('total')

    print(f"Found {len(persons)} unique persons from App")
    return persons

def scan_newsletter_cases(persons):
    """Newsletter case studiesをスキャン"""
    print(f"Scanning Newsletter case studies in {NEWSLETTER_DIR}...")
    if not NEWSLETTER_DIR.exists():
        print(f"Warning: {NEWSLETTER_DIR} does not exist")
        return persons

    for file in NEWSLETTER_DIR.glob("*.md"):
        data = extract_yaml_frontmatter(file)
        if data:
            name = data.get('founder_name')
            twitter = normalize_twitter_handle(data.get('founder_twitter'))

            if twitter:
                key = f"@{twitter}"
                if name:
                    persons[key]['names'].add(name)
                persons[key]['twitter_handles'].add(twitter)
                persons[key]['newsletter_ids'].append({
                    'id': data.get('id'),
                    'role': 'founder',
                    'newsletter': data.get('newsletter_name')
                })
                if data.get('japan_market_score'):
                    persons[key]['metadata']['japan_relevance'] = data['japan_market_score'].get('overall')

    print(f"Total unique persons after Newsletter: {len(persons)}")
    return persons

def scan_sns_cases(persons):
    """SNS case studiesをスキャン"""
    print(f"Scanning SNS case studies in {SNS_DIR}...")
    if not SNS_DIR.exists():
        print(f"Warning: {SNS_DIR} does not exist")
        return persons

    for sns_file in SNS_DIR.rglob("sns_analysis.md"):
        sns_info = extract_sns_info_from_text(sns_file)
        if sns_info and sns_info['twitter_handle']:
            name = sns_info['name']
            twitter = normalize_twitter_handle(sns_info['twitter_handle'])

            if twitter:
                key = f"@{twitter}"
                if name:
                    persons[key]['names'].add(name)
                persons[key]['twitter_handles'].add(twitter)

                # ディレクトリ名からIDを生成
                parent_dir = sns_file.parent.name
                sns_id = f"SNS_{parent_dir}"
                persons[key]['sns_ids'].append({
                    'id': sns_id,
                    'platform': 'twitter'
                })

    print(f"Total unique persons after SNS: {len(persons)}")
    return persons

def generate_registry(persons, top_n=50):
    """Person Registry YAMLを生成"""
    # Presence順にソート
    ranked_persons = []
    for key, data in persons.items():
        total_presence = len(data['app_ids']) + len(data['newsletter_ids']) + len(data['sns_ids'])
        if total_presence > 0:
            ranked_persons.append((key, data, total_presence))

    ranked_persons.sort(key=lambda x: x[2], reverse=True)
    top_persons = ranked_persons[:top_n]

    # Registry YAMLファイル生成
    REGISTRY_DIR.mkdir(exist_ok=True)
    registry_file = REGISTRY_DIR / "person_registry.md"

    with open(registry_file, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write("registry_version: \"1.0\"\n")
        f.write(f"last_updated: \"{datetime.now().strftime('%Y-%m-%d')}\"\n")
        f.write(f"total_persons: {len(top_persons)}\n")
        f.write("\npersons:\n")

        for key, data, total_presence in top_persons:
            twitter_handle = list(data['twitter_handles'])[0]
            person_id = f"PERSON_{twitter_handle.upper()}"
            primary_name = list(data['names'])[0] if data['names'] else "Unknown"

            f.write(f"  - id: \"{person_id}\"\n")
            f.write(f"    name: \"{primary_name}\"\n")
            f.write(f"    name_ja: \"\"\n")
            f.write(f"    twitter_handle: \"@{twitter_handle}\"\n")
            f.write(f"    \n")
            f.write(f"    presence:\n")

            if data['app_ids']:
                f.write(f"      app:\n")
                for app in data['app_ids'][:3]:  # 最大3件
                    f.write(f"        - id: \"{app['id']}\"\n")
                    f.write(f"          role: \"{app['role']}\"\n")
                    if app.get('product'):
                        f.write(f"          product: \"{app['product']}\"\n")

            if data['newsletter_ids']:
                f.write(f"      newsletter:\n")
                for nl in data['newsletter_ids'][:3]:  # 最大3件
                    f.write(f"        - id: \"{nl['id']}\"\n")
                    f.write(f"          role: \"{nl['role']}\"\n")
                    if nl.get('newsletter'):
                        f.write(f"          newsletter: \"{nl['newsletter']}\"\n")

            if data['sns_ids']:
                f.write(f"      sns:\n")
                for sns in data['sns_ids'][:3]:  # 最大3件
                    f.write(f"        - id: \"{sns['id']}\"\n")
                    f.write(f"          platform: \"{sns['platform']}\"\n")

            f.write(f"    \n")
            f.write(f"    metadata:\n")
            if data['metadata'].get('nationality'):
                f.write(f"      nationality: \"{data['metadata']['nationality']}\"\n")
            f.write(f"      known_for: []\n")
            if data['metadata'].get('japan_relevance'):
                f.write(f"      japan_relevance: {data['metadata']['japan_relevance']}\n")
            else:
                f.write(f"      japan_relevance: null\n")
            f.write(f"    \n")

    print(f"\n✅ Person Registry created: {registry_file}")
    return top_persons

def generate_csv_stats(top_persons):
    """CSV統計ファイルを生成"""
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    csv_file = ANALYSIS_DIR / "person_registry_stats.csv"

    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("person_id,name,twitter_handle,app_count,newsletter_count,sns_count,total_presence,japan_relevance\n")

        for key, data, total_presence in top_persons:
            twitter_handle = list(data['twitter_handles'])[0]
            person_id = f"PERSON_{twitter_handle.upper()}"
            primary_name = list(data['names'])[0] if data['names'] else "Unknown"
            # CSVでカンマを含む名前をエスケープ
            primary_name = f'"{primary_name}"' if ',' in primary_name else primary_name
            app_count = len(data['app_ids'])
            newsletter_count = len(data['newsletter_ids'])
            sns_count = len(data['sns_ids'])
            japan_rel = data['metadata'].get('japan_relevance', '')

            f.write(f"{person_id},{primary_name},@{twitter_handle},{app_count},{newsletter_count},{sns_count},{total_presence},{japan_rel}\n")

    print(f"✅ CSV stats created: {csv_file}")

def print_statistics(top_persons):
    """統計情報を表示"""
    stats = {'3軸統合': 0, '2軸統合': 0, '単一カテゴリ': 0}
    japan_scores = []

    for key, data, total in top_persons:
        presence_types = sum([
            1 if data['app_ids'] else 0,
            1 if data['newsletter_ids'] else 0,
            1 if data['sns_ids'] else 0
        ])

        if presence_types == 3:
            stats['3軸統合'] += 1
        elif presence_types == 2:
            stats['2軸統合'] += 1
        else:
            stats['単一カテゴリ'] += 1

        if data['metadata'].get('japan_relevance'):
            japan_scores.append(float(data['metadata']['japan_relevance']))

    avg_japan_score = sum(japan_scores) / len(japan_scores) if japan_scores else 0

    print(f"\n=== Statistics ===")
    print(f"総登録人数: {len(top_persons)}名")
    print(f"3軸統合（App+Newsletter+SNS）: {stats['3軸統合']}名")
    print(f"2軸統合: {stats['2軸統合']}名")
    print(f"単一カテゴリのみ: {stats['単一カテゴリ']}名")
    print(f"Japan relevance平均: {avg_japan_score:.2f}点 ({len(japan_scores)}名から算出)")

def main():
    """メイン処理"""
    print("=== Person Registry Generator ===\n")

    # データ収集
    persons = scan_app_cases()
    persons = scan_newsletter_cases(persons)
    persons = scan_sns_cases(persons)

    # Registry生成
    top_persons = generate_registry(persons, top_n=50)

    # CSV生成
    generate_csv_stats(top_persons)

    # 統計表示
    print_statistics(top_persons)

    print("\n✅ Person Registry generation completed!")

if __name__ == "__main__":
    main()
