#!/usr/bin/env python3
"""
RAG用チャンク分割スクリプト

Markdownファイルをセマンティックチャンキング（見出し単位）で分割し、
JSONL形式で出力
"""

import json
import re
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")


def chunk_markdown(content, source_metadata):
    """
    Markdownコンテンツをセマンティックチャンキング

    見出し（## 以下）単位で分割し、各チャンクにメタデータを付与
    """
    chunks = []
    lines = content.split('\n')

    current_chunk = []
    current_heading = ""
    current_level = 0

    for line in lines:
        # 見出しを検出（## 以下）
        heading_match = re.match(r'^(#{2,6})\s+(.+)$', line)

        if heading_match:
            # 前のチャンクを保存
            if current_chunk:
                chunk_text = '\n'.join(current_chunk).strip()
                if chunk_text:
                    chunks.append({
                        "content": chunk_text,
                        "heading": current_heading,
                        "heading_level": current_level,
                        **source_metadata
                    })

            # 新しいチャンク開始
            level = len(heading_match.group(1))
            heading = heading_match.group(2).strip()

            current_heading = heading
            current_level = level
            current_chunk = [line]
        else:
            # 画像を検出してalt textをチャンクに含める
            image_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', line.strip())
            if image_match:
                alt_text = image_match.group(1).strip()
                if alt_text and alt_text != 'image' and not alt_text.startswith('PLACEHOLDER:'):
                    # 画像説明をチャンクに含める
                    current_chunk.append(f"[画像: {alt_text}]")
                else:
                    # alt textがない場合は元の行をそのまま含める
                    current_chunk.append(line)
            else:
                current_chunk.append(line)

    # 最後のチャンクを保存
    if current_chunk:
        chunk_text = '\n'.join(current_chunk).strip()
        if chunk_text:
            chunks.append({
                "content": chunk_text,
                "heading": current_heading,
                "heading_level": current_level,
                **source_metadata
            })

    return chunks


def process_directory(directory, category):
    """ディレクトリ内のMarkdownファイルを処理"""
    chunks = []

    for md_file in directory.rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # タイトルを抽出（最初の# 見出し）
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem

            # URLを抽出
            url_match = re.search(r'\*\*URL\*\*:\s*(.+)$', content, re.MULTILINE)
            url = url_match.group(1).strip() if url_match else ""

            # メタデータ
            source_metadata = {
                "source_file": str(md_file.relative_to(OUTPUT_DIR)),
                "title": title,
                "url": url,
                "category": category
            }

            # チャンク分割
            file_chunks = chunk_markdown(content, source_metadata)
            chunks.extend(file_chunks)

            print(f"  処理: {md_file.name} ({len(file_chunks)}チャンク)")

        except Exception as e:
            print(f"  ✗ エラー: {md_file.name} - {e}")

    return chunks


def create_chunks():
    """全コンテンツをチャンク分割"""
    print("=" * 60)
    print("RAG用チャンク分割開始")
    print("=" * 60)

    all_chunks = []

    # ブログ記事
    print("\n=== ブログ記事 ===")
    blog_dir = OUTPUT_DIR / 'blog'
    if blog_dir.exists():
        blog_chunks = process_directory(blog_dir, 'blog')
        all_chunks.extend(blog_chunks)
        print(f"ブログチャンク: {len(blog_chunks)}件")

    # 動画教材
    print("\n=== 動画教材 ===")
    video_dir = OUTPUT_DIR / 'video_tutorials'
    if video_dir.exists():
        video_chunks = process_directory(video_dir, 'video_tutorials')
        all_chunks.extend(video_chunks)
        print(f"動画教材チャンク: {len(video_chunks)}件")

    # 対談動画
    print("\n=== 対談動画 ===")
    interview_dir = OUTPUT_DIR / 'interviews'
    if interview_dir.exists():
        interview_chunks = process_directory(interview_dir, 'interviews')
        all_chunks.extend(interview_chunks)
        print(f"対談動画チャンク: {len(interview_chunks)}件")

    # ZOOMコンサル
    print("\n=== ZOOMコンサル ===")
    zoom_dir = OUTPUT_DIR / 'zoom_consult'
    if zoom_dir.exists():
        zoom_chunks = process_directory(zoom_dir, 'zoom_consult')
        all_chunks.extend(zoom_chunks)
        print(f"ZOOMコンサルチャンク: {len(zoom_chunks)}件")

    # 動画文字起こし
    print("\n=== 動画文字起こし ===")
    video_transcripts_dir = OUTPUT_DIR / 'video_transcripts'
    if video_transcripts_dir.exists():
        video_transcripts_chunks = process_directory(video_transcripts_dir, 'video_transcripts')
        all_chunks.extend(video_transcripts_chunks)
        print(f"動画文字起こしチャンク: {len(video_transcripts_chunks)}件")

    # JSONL形式で保存
    chunks_dir = OUTPUT_DIR / 'chunks'
    chunks_dir.mkdir(exist_ok=True)

    output_file = chunks_dir / 'all_chunks.jsonl'
    with open(output_file, 'w', encoding='utf-8') as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + '\n')

    print("\n" + "=" * 60)
    print("チャンク分割完了")
    print(f"総チャンク数: {len(all_chunks)}件")
    print(f"出力ファイル: {output_file}")
    print("=" * 60)

    # 統計情報を生成
    category_stats = {}
    for chunk in all_chunks:
        cat = chunk['category']
        category_stats[cat] = category_stats.get(cat, 0) + 1

    print("\nカテゴリ別統計:")
    for cat, count in sorted(category_stats.items()):
        print(f"  {cat}: {count}チャンク")


if __name__ == "__main__":
    create_chunks()
