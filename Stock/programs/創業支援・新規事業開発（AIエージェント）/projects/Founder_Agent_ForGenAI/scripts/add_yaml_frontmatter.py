#!/usr/bin/env python3
"""
T005-4: トランスクリプトにYAML frontmatterを追加するスクリプト

Usage:
    python add_yaml_frontmatter.py
"""

import json
import yaml
from pathlib import Path

# パス設定
METADATA_FILE = Path("/tmp/youtube_metadata.json")
SOURCE_TRANSCRIPTS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/items")
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/sources/Founder_Agent_Videos")

def add_yaml_frontmatter(metadata_list):
    """各トランスクリプトにYAML frontmatterを追加"""

    # 出力ディレクトリ作成
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    processed_count = 0

    for metadata in metadata_list:
        video_id = metadata['video_id']
        source_file = SOURCE_TRANSCRIPTS_DIR / f"{video_id}.md"
        output_file = OUTPUT_DIR / f"{video_id}.md"

        if not source_file.exists():
            print(f"❌ Source file not found: {source_file}")
            continue

        # 元のトランスクリプトを読み込む
        with open(source_file, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # YAML frontmatterを作成
        frontmatter_data = {
            'video_url': f"https://www.youtube.com/watch?v={video_id}",
            'video_id': video_id,
            'title': metadata['title'],
            'speaker': metadata['speaker'],
            'channel': metadata.get('channel', ''),
            'date': metadata['date'],
            'topic_tags': metadata['topic_tags'],
            'summary': metadata['summary'],
            'key_points': metadata['key_points'],
            'technologies_mentioned': metadata['technologies_mentioned'],
            'use_cases': metadata['use_cases'],
            'language': metadata['language'],
            'source': 'Founder_Agent_Videos'
        }

        # YAML frontmatterを文字列化
        frontmatter_yaml = yaml.dump(frontmatter_data, allow_unicode=True, sort_keys=False)

        # 新しいファイルを作成（YAML frontmatter + 元のコンテンツ）
        new_content = f"""---
{frontmatter_yaml.strip()}
---

{original_content}
"""

        # 出力ファイルに書き込む
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        processed_count += 1
        print(f"✅ Processed: {video_id}.md")

    print(f"\n📊 Total processed: {processed_count} files")
    print(f"📁 Output directory: {OUTPUT_DIR}")

def main():
    # メタデータJSONを読み込む
    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata_list = json.load(f)

    print(f"📂 Processing {len(metadata_list)} transcripts...")
    print(f"📍 Source: {SOURCE_TRANSCRIPTS_DIR}")
    print(f"📍 Output: {OUTPUT_DIR}\n")

    add_yaml_frontmatter(metadata_list)

if __name__ == "__main__":
    main()
