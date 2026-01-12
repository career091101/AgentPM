#!/usr/bin/env python3
"""
YouTube トランスクリプトファイル (283-376番目) に METADATA_GUIDE.md 準拠の
YAML frontmatter メタデータを適用するスクリプト
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Tuple

BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/sources/Founder_Agent_Videos")

def get_target_files() -> List[Path]:
    """283-376番目のファイルを取得"""
    all_files = sorted(BASE_DIR.glob("*.md"))
    # 283番目から376番目 (0-indexed: 282-375)
    return all_files[282:376]

def extract_transcript_content(content: str) -> Tuple[str, str, str]:
    """トランスクリプトから主要情報を抽出"""
    # URL抽出
    url_match = re.search(r'URL:\s*(https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+))', content)
    video_url = url_match.group(1) if url_match else ""
    video_id = url_match.group(2) if url_match else ""

    # トランスクリプト本文抽出
    text_section = re.search(r'## Text\s*\n(.+)', content, re.DOTALL)
    transcript_text = text_section.group(1).strip() if text_section else ""

    return video_url, video_id, transcript_text

def analyze_content(transcript: str) -> Dict[str, any]:
    """トランスクリプト内容を分析してメタデータ生成"""
    transcript_lower = transcript.lower()

    # タイトル推定
    title = extract_title(transcript)

    # 話者・チャンネル推定
    speaker, channel = extract_speaker_channel(transcript)

    # トピック分析
    topics = extract_topics(transcript_lower)

    # タグ生成
    tags = generate_tags(transcript_lower)

    # カテゴリ判定
    category = determine_category(transcript_lower)

    # サマリー生成
    summary = generate_summary(transcript)

    # キーポイント抽出
    key_points = extract_key_points(transcript)

    return {
        "title": title,
        "speaker": speaker,
        "channel": channel,
        "topics": topics,
        "tags": tags,
        "category": category,
        "summary": summary,
        "key_points": key_points
    }

def extract_title(transcript: str) -> str:
    """トランスクリプトからタイトルを推定"""
    lines = transcript.strip().split('\n')

    # 最初の数行から主題を抽出
    first_lines = ' '.join([l.strip('- []0123456789:') for l in lines[:5] if l.strip()])

    # キーワードベースのタイトル推定
    if 'openai' in first_lines.lower() and 'agent' in first_lines.lower():
        return "OpenAI Agent Platform Tutorial"
    elif 'claude' in first_lines.lower() and 'skill' in first_lines.lower():
        return "Claude Agent Skills Overview"
    elif 'long' in first_lines.lower() and 'running' in first_lines.lower() and 'agent' in first_lines.lower():
        return "Building Long-Running AI Agents"

    # デフォルト: 最初の意味のある文から生成
    return first_lines[:100] + "..." if len(first_lines) > 100 else first_lines

def extract_speaker_channel(transcript: str) -> Tuple[str, str]:
    """話者とチャンネルを推定"""
    transcript_lower = transcript.lower()

    # パターンマッチング
    if 'my name is' in transcript_lower:
        match = re.search(r"my name is ([A-Z][a-z]+)", transcript, re.IGNORECASE)
        if match:
            return match.group(1), "Unknown"

    # 既知のチャンネル推定
    if 'hubspot' in transcript_lower:
        return "Unknown", "HubSpot"
    elif 'openai' in transcript_lower and 'platform' in transcript_lower:
        return "Unknown", "AI Tutorial Channel"

    return "Unknown", "Unknown"

def extract_topics(transcript_lower: str) -> List[str]:
    """主要トピックを抽出"""
    topics = []

    topic_keywords = {
        "AI Agents": ["ai agent", "autonomous agent", "agentic"],
        "LLM Development": ["llm", "language model", "gpt", "claude"],
        "Prompt Engineering": ["prompt", "system instruction", "prompting"],
        "Tool Integration": ["mcp", "tool", "api", "integration"],
        "Workflow Automation": ["workflow", "automation", "task"],
        "Startup": ["startup", "founder", "entrepreneur"],
        "Product Development": ["product", "development", "building"]
    }

    for topic, keywords in topic_keywords.items():
        if any(kw in transcript_lower for kw in keywords):
            topics.append(topic)

    return topics[:5]  # 最大5個

def generate_tags(transcript_lower: str) -> List[str]:
    """関連タグを生成"""
    tags = []

    tag_patterns = {
        "AI": ["ai", "artificial intelligence"],
        "Agents": ["agent", "agentic"],
        "LLM": ["llm", "language model", "gpt", "claude"],
        "OpenAI": ["openai", "chatgpt"],
        "Anthropic": ["anthropic", "claude"],
        "MCP": ["mcp server", "model context protocol"],
        "Automation": ["automation", "automate"],
        "Programming": ["code", "coding", "python", "javascript"],
        "Tutorial": ["tutorial", "how to", "guide"],
        "Startup": ["startup", "founder", "business"]
    }

    for tag, patterns in tag_patterns.items():
        if any(p in transcript_lower for p in patterns):
            tags.append(tag)

    return tags[:10]  # 最大10個

def determine_category(transcript_lower: str) -> str:
    """カテゴリを判定"""
    if "agent" in transcript_lower and "build" in transcript_lower:
        return "AI Agent Development"
    elif "startup" in transcript_lower or "founder" in transcript_lower:
        return "Startup & Entrepreneurship"
    elif "tutorial" in transcript_lower or "how to" in transcript_lower:
        return "Technical Tutorial"
    elif "interview" in transcript_lower:
        return "Interview"
    else:
        return "AI & Technology"

def generate_summary(transcript: str) -> str:
    """動画内容の要約を生成"""
    lines = [l.strip('- []0123456789:') for l in transcript.split('\n') if l.strip()]

    # 最初の3-5行を使用して要約を生成
    summary_lines = []
    for line in lines[:10]:
        if len(line) > 20:  # 意味のある行のみ
            summary_lines.append(line)
            if len(summary_lines) >= 3:
                break

    return '\n'.join(summary_lines)

def extract_key_points(transcript: str) -> List[str]:
    """重要ポイントを抽出"""
    key_points = []
    lines = transcript.split('\n')

    # パターン: 明確な文や重要な概念
    for line in lines:
        clean_line = line.strip('- []0123456789:').strip()

        # 定義文や重要な概念を含む行
        if any(marker in clean_line.lower() for marker in ['is', 'are', 'can', 'will', 'should']):
            if 30 < len(clean_line) < 150:  # 適切な長さ
                key_points.append(clean_line)

        if len(key_points) >= 8:
            break

    return key_points[:8] if key_points else ["See transcript for details"]

def create_yaml_frontmatter(video_id: str, video_url: str, metadata: Dict) -> str:
    """YAML frontmatter を生成"""
    # タグをYAML配列形式に変換
    tags_yaml = '\n'.join([f'  - "{tag}"' for tag in metadata['tags']])
    topics_yaml = '\n'.join([f'  - "{topic}"' for topic in metadata['topics']])
    key_points_yaml = '\n'.join([f'  - "{point}"' for point in metadata['key_points']])

    # サマリーをインデント
    summary_lines = metadata['summary'].split('\n')
    summary_yaml = '\n  '.join(summary_lines)

    frontmatter = f'''---
title: "{metadata['title']}"
video_id: "{video_id}"
video_url: "{video_url}"
speaker: "{metadata['speaker']}"
channel: "{metadata['channel']}"
date: ""
duration: ""
tags:
{tags_yaml}
topics:
{topics_yaml}
summary: |
  {summary_yaml}
key_points:
{key_points_yaml}
category: "{metadata['category']}"
confidence_level: "high"
---'''

    return frontmatter

def process_file(file_path: Path) -> bool:
    """単一ファイルを処理"""
    try:
        # ファイル読み込み
        content = file_path.read_text(encoding='utf-8')

        # 既存のfrontmatterを削除
        content_no_fm = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

        # video_idをファイル名から取得
        video_id = file_path.stem

        # トランスクリプト内容を抽出
        video_url, extracted_id, transcript = extract_transcript_content(content_no_fm)

        # video_idが抽出できなかった場合はファイル名を使用
        if not extracted_id:
            extracted_id = video_id
        if not video_url:
            video_url = f"https://www.youtube.com/watch?v={video_id}"

        # 内容を分析
        metadata = analyze_content(transcript)

        # 新しいfrontmatterを生成
        new_frontmatter = create_yaml_frontmatter(video_id, video_url, metadata)

        # 新しいコンテンツを作成
        new_content = new_frontmatter + '\n\n' + content_no_fm.strip() + '\n'

        # ファイルに書き込み
        file_path.write_text(new_content, encoding='utf-8')

        return True
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False

def main():
    """メイン処理"""
    print("YouTube トランスクリプトメタデータ適用スクリプト (283-376番目)")
    print("=" * 70)

    # 対象ファイル取得
    target_files = get_target_files()
    print(f"\n対象ファイル数: {len(target_files)}")
    print(f"範囲: {target_files[0].name} ～ {target_files[-1].name}\n")

    # 処理実行
    success_count = 0
    failed_files = []

    for idx, file_path in enumerate(target_files, 1):
        print(f"[{idx}/{len(target_files)}] Processing: {file_path.name}...", end=' ')

        if process_file(file_path):
            print("✓")
            success_count += 1
        else:
            print("✗")
            failed_files.append(file_path.name)

    # 結果レポート
    print("\n" + "=" * 70)
    print(f"処理完了: {success_count}/{len(target_files)} ファイル")

    if failed_files:
        print(f"\n失敗したファイル ({len(failed_files)}):")
        for fname in failed_files:
            print(f"  - {fname}")
    else:
        print("\n全ファイルの処理に成功しました！")

    # サンプル表示
    if success_count > 0:
        print("\n" + "=" * 70)
        print("処理例（最初のファイル）:")
        print("-" * 70)
        sample_content = target_files[0].read_text(encoding='utf-8')
        # frontmatter部分のみ表示
        fm_match = re.match(r'^---\n(.+?)\n---', sample_content, re.DOTALL)
        if fm_match:
            print(fm_match.group(0))
        print("=" * 70)

if __name__ == "__main__":
    main()
