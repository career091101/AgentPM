#!/usr/bin/env python3
"""
YouTube トランスクリプトファイルにMETADATA_GUIDE.md準拠のYAML frontmatterを適用するスクリプト

処理対象: sources/Founder_Agent_Videos/ 配下の.mdファイル (1-94番目)
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# ベースディレクトリ
BASE_DIR = Path(__file__).parent.parent
VIDEOS_DIR = BASE_DIR / "sources" / "Founder_Agent_Videos"


def extract_video_info(content: str, video_id: str) -> Dict[str, any]:
    """トランスクリプト内容から動画情報を抽出"""

    # タイトル推定（トランスクリプトの最初の数行から）
    lines = content.split('\n')
    transcript_lines = [l for l in lines if l.startswith('- [')]

    title = f"YouTube Video: {video_id}"
    speaker = "Unknown"
    channel = "Unknown"
    date = ""

    # トランスクリプトの最初の100行から推定
    first_text = ' '.join([l.split(']')[1].strip() if ']' in l else ''
                           for l in transcript_lines[:100]])

    # 話者名の推定（自己紹介パターン）
    speaker_patterns = [
        r"(?:I'm|I am|My name is|This is)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)",
        r"こんにちは[。、]([^。、]{2,10})です",
    ]

    for pattern in speaker_patterns:
        match = re.search(pattern, first_text)
        if match:
            speaker = match.group(1)
            break

    # トピック抽出
    topics = []
    topic_keywords = {
        "AI Agent": ["agent", "エージェント", "autonomous"],
        "Startup": ["startup", "起業", "founder", "business"],
        "LLM": ["GPT", "Claude", "LLM", "language model", "生成AI"],
        "Technical": ["code", "programming", "Python", "API"],
        "Business Strategy": ["strategy", "revenue", "profit", "market"],
        "Tutorial": ["tutorial", "how to", "build", "作り方"],
    }

    for topic, keywords in topic_keywords.items():
        if any(kw.lower() in first_text.lower() for kw in keywords):
            topics.append(topic)

    # タグ生成
    tags = ["YouTube", "Transcript"]
    if topics:
        tags.extend(topics[:5])

    # 要約生成（最初の200文字）
    summary_text = first_text[:300].strip()
    if len(summary_text) > 200:
        summary_text = summary_text[:200] + "..."

    # 主要ポイント抽出（トランスクリプトから重要そうな部分）
    key_points = []
    for line in transcript_lines[:50]:
        if any(marker in line.lower() for marker in ["first", "second", "key", "important", "まず", "次に", "重要"]):
            text = line.split(']')[1].strip() if ']' in line else ''
            if len(text) > 20:
                key_points.append(text[:100])
        if len(key_points) >= 5:
            break

    return {
        "title": title,
        "speaker": speaker,
        "channel": channel,
        "date": date,
        "tags": tags,
        "topics": topics[:5],
        "summary": summary_text,
        "key_points": key_points[:7] if key_points else ["動画トランスクリプトの内容を参照"],
    }


def create_enhanced_frontmatter(video_id: str, content: str) -> str:
    """METADATA_GUIDE.md準拠の強化版YAML frontmatterを生成"""

    info = extract_video_info(content, video_id)

    # タグをフォーマット
    tags_yaml = "\n".join([f'  - "{tag}"' for tag in info["tags"]])

    # トピックをフォーマット
    topics_yaml = "\n".join([f'  - "{topic}"' for topic in info["topics"]]) if info["topics"] else '  - "General"'

    # キーポイントをフォーマット
    key_points_yaml = "\n".join([f'  - "{point}"' for point in info["key_points"]])

    # カテゴリ推定
    category = "Tutorial" if "Tutorial" in info["topics"] else \
               "Business" if "Business Strategy" in info["topics"] else \
               "AI Technical" if "Technical" in info["topics"] else \
               "General"

    frontmatter = f"""---
title: "{info['title']}"
video_id: "{video_id}"
video_url: "https://www.youtube.com/watch?v={video_id}"
speaker: "{info['speaker']}"
channel: "{info['channel']}"
date: "{info['date']}"
duration: ""
tags:
{tags_yaml}
topics:
{topics_yaml}
summary: |
  {info['summary']}
key_points:
{key_points_yaml}
category: "{category}"
confidence_level: "medium"
transcript_type: "YouTube Auto-generated"
language: "en-ja-mixed"
source: "Founder_Agent_Videos"
---
"""

    return frontmatter


def process_file(file_path: Path) -> bool:
    """1ファイルを処理してメタデータを適用"""

    try:
        # ファイル読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # video_idを取得（ファイル名から）
        video_id = file_path.stem

        # 既存のfrontmatterを削除
        if content.startswith('---'):
            # 2つ目の---を見つける
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()

        # 新しいfrontmatterを生成
        new_frontmatter = create_enhanced_frontmatter(video_id, content)

        # 新しいコンテンツを作成
        new_content = new_frontmatter + "\n\n" + content

        # ファイルに書き込み
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False


def main():
    """メイン処理"""

    # 全.mdファイルを取得してソート
    all_files = sorted(VIDEOS_DIR.glob("*.md"))

    # 最初の94ファイル
    target_files = all_files[:94]

    print(f"処理対象ファイル数: {len(target_files)}")
    print("=" * 60)

    success_count = 0
    failed_files = []

    for i, file_path in enumerate(target_files, 1):
        print(f"Processing ({i}/{len(target_files)}): {file_path.name}")

        if process_file(file_path):
            success_count += 1
        else:
            failed_files.append(file_path.name)

    print("=" * 60)
    print(f"処理完了: {success_count}/{len(target_files)} ファイル成功")

    if failed_files:
        print(f"\n失敗したファイル ({len(failed_files)}):")
        for fname in failed_files:
            print(f"  - {fname}")

    # 代表例を表示
    if success_count > 0:
        print("\n代表例（最初の処理ファイル）:")
        first_file = target_files[0]
        with open(first_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # frontmatter部分のみ表示
            for i, line in enumerate(lines):
                print(line.rstrip())
                if i > 0 and line.strip() == '---':
                    break


if __name__ == "__main__":
    main()
