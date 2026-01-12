#!/usr/bin/env python3
"""
RAGチャンク再生成スクリプト

文字起こしファイルを5分（300秒）ごとにチャンク分割し、
既存のall_chunks.jsonlに追加
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
METADATA_FILE = PROJECT_ROOT / "metadata.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
CHUNKS_DIR = PROJECT_ROOT / "chunks"
CHUNKS_FILE = CHUNKS_DIR / "all_chunks.jsonl"


def parse_timestamp_to_seconds(timestamp_str):
    """タイムスタンプ文字列を秒数に変換 ([HH:MM:SS] or [MM:SS])"""
    timestamp_str = timestamp_str.strip('[]')
    parts = timestamp_str.split(':')

    if len(parts) == 3:  # HH:MM:SS
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:  # MM:SS
        return int(parts[0]) * 60 + int(parts[1])

    return 0


def format_seconds_to_timestamp(seconds):
    """秒数をタイムスタンプ文字列に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def chunk_video_transcript(transcript_file, video_metadata):
    """動画文字起こしをチャンク分割（5分ごと）"""
    chunks = []

    file_path = PROJECT_ROOT / transcript_file

    # formatted版を優先
    formatted_path = file_path.parent / f"{file_path.stem}_formatted.md"
    if formatted_path.exists():
        file_path = formatted_path

    if not file_path.exists():
        return chunks

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # タイムスタンプ付き行を抽出
    lines = content.split('\n')
    current_chunk_lines = []
    current_start_time = None
    chunk_start_line_idx = 0

    for i, line in enumerate(lines):
        # タイムスタンプ抽出 [HH:MM:SS] or [MM:SS]
        timestamp_match = re.match(r'\[(\d{1,2}:\d{2}:?\d{0,2})\]', line)

        if timestamp_match:
            timestamp = timestamp_match.group(1)
            seconds = parse_timestamp_to_seconds(timestamp)

            # 最初のタイムスタンプ
            if current_start_time is None:
                current_start_time = seconds
                chunk_start_line_idx = i

            # 5分（300秒）ごとに区切る
            elif seconds - current_start_time >= 300:
                # チャンク保存
                chunk_content = '\n'.join(current_chunk_lines).strip()
                if chunk_content:
                    chunks.append({
                        "content": chunk_content,
                        "source_type": "video",
                        "source_file": str(transcript_file),
                        "title": video_metadata['title'],
                        "url": video_metadata['url'],
                        "category": video_metadata['category'],
                        "timestamp_start": format_seconds_to_timestamp(current_start_time),
                        "timestamp_end": format_seconds_to_timestamp(seconds),
                        "chunk_index": len(chunks)
                    })

                # リセット
                current_chunk_lines = []
                current_start_time = seconds
                chunk_start_line_idx = i

        current_chunk_lines.append(line)

    # 最後のチャンク
    if current_chunk_lines:
        chunk_content = '\n'.join(current_chunk_lines).strip()
        if chunk_content:
            # 最後のタイムスタンプを探す
            last_timestamp = None
            for line in reversed(current_chunk_lines):
                match = re.match(r'\[(\d{1,2}:\d{2}:?\d{0,2})\]', line)
                if match:
                    last_timestamp = match.group(1)
                    break

            end_time_str = format_seconds_to_timestamp(parse_timestamp_to_seconds(last_timestamp)) if last_timestamp else "END"

            chunks.append({
                "content": chunk_content,
                "source_type": "video",
                "source_file": str(transcript_file),
                "title": video_metadata['title'],
                "url": video_metadata['url'],
                "category": video_metadata['category'],
                "timestamp_start": format_seconds_to_timestamp(current_start_time) if current_start_time else "00:00",
                "timestamp_end": end_time_str,
                "chunk_index": len(chunks)
            })

    return chunks


def main():
    print("=" * 60)
    print("RAGチャンク再生成開始")
    print("=" * 60)

    # metadata.json読み込み
    if not METADATA_FILE.exists():
        print(f"✗ {METADATA_FILE} が見つかりません")
        print("先にintegrate_video_metadata.pyを実行してください")
        return

    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # 既存のブログチャンクを保持
    existing_blog_chunks = []
    if CHUNKS_FILE.exists():
        print(f"\n既存のチャンクファイルを読み込み中...")
        with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    chunk = json.loads(line)
                    # ブログチャンクのみ保持（動画チャンクは再生成）
                    if chunk.get('source_type') != 'video':
                        existing_blog_chunks.append(chunk)

        print(f"  保持するブログチャンク: {len(existing_blog_chunks)}件")

    # 動画チャンクを生成
    video_chunks = []
    videos = metadata.get('videos', [])

    print(f"\n動画チャンク生成中...")

    for video in videos:
        if not video.get('has_transcript'):
            continue

        transcript_file = video.get('transcript_file')
        if not transcript_file:
            continue

        print(f"  処理中: {video['title'][:50]}")

        chunks = chunk_video_transcript(transcript_file, video)
        video_chunks.extend(chunks)

        print(f"    → {len(chunks)}チャンク生成")

    # チャンクを結合（ブログ + 動画）
    all_chunks = existing_blog_chunks + video_chunks

    # チャンクファイルに保存
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

    with open(CHUNKS_FILE, 'w', encoding='utf-8') as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + '\n')

    # 統計
    print(f"\n{'='*60}")
    print("RAGチャンク再生成完了")
    print(f"{'='*60}")
    print(f"ブログチャンク: {len(existing_blog_chunks)}件")
    print(f"動画チャンク: {len(video_chunks)}件")
    print(f"総チャンク数: {len(all_chunks)}件")
    print(f"\n✓ チャンクファイル保存: {CHUNKS_FILE}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
