#!/usr/bin/env python3
"""
メタデータ統合スクリプト

video_urls_complete.jsonと文字起こしファイルをマッピングし、
metadata.jsonのvideosセクションを更新
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
METADATA_FILE = PROJECT_ROOT / "metadata.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"


def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None


def sanitize_filename(title):
    """ファイル名として使える文字列に変換"""
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = title
    for char in invalid_chars:
        sanitized = sanitized.replace(char, '_')
    if len(sanitized) > 200:
        sanitized = sanitized[:200]
    return sanitized


def get_transcript_file(category, title):
    """文字起こしファイルパスを取得"""
    category_dir = OUTPUT_BASE_DIR / category
    sanitized_title = sanitize_filename(title)

    possible_files = [
        category_dir / f"{sanitized_title}.md",
        category_dir / f"{title}.md"
    ]

    for file in possible_files:
        if file.exists():
            return str(file.relative_to(PROJECT_ROOT))

    return None


def get_duration_from_transcript(transcript_file):
    """文字起こしファイルから動画長を推定"""
    if not transcript_file:
        return 0

    file_path = PROJECT_ROOT / transcript_file
    if not file_path.exists():
        return 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 最後のタイムスタンプを探す（formatted版があれば優先）
        formatted_file = file_path.parent / f"{file_path.stem}_formatted.md"
        if formatted_file.exists():
            with open(formatted_file, 'r', encoding='utf-8') as f:
                content = f.read()

        # タイムスタンプパターン: [HH:MM:SS] または [MM:SS]
        timestamps = re.findall(r'\[(\d{1,2}):(\d{2}):?(\d{2})?\]', content)

        if timestamps:
            last_timestamp = timestamps[-1]
            if len(last_timestamp) == 3 and last_timestamp[2]:  # HH:MM:SS
                hours = int(last_timestamp[0])
                minutes = int(last_timestamp[1])
                seconds = int(last_timestamp[2])
            else:  # MM:SS
                hours = 0
                minutes = int(last_timestamp[0])
                seconds = int(last_timestamp[1])

            return hours * 3600 + minutes * 60 + seconds

    except Exception as e:
        print(f"  ⚠ 動画長取得エラー: {transcript_file}: {e}")

    return 0


def format_duration(seconds):
    """秒数をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def main():
    print("=" * 60)
    print("メタデータ統合開始")
    print("=" * 60)

    # video_urls_complete.json読み込み
    if not VIDEO_URLS_FILE.exists():
        print(f"✗ {VIDEO_URLS_FILE} が見つかりません")
        return

    with open(VIDEO_URLS_FILE, 'r', encoding='utf-8') as f:
        video_data = json.load(f)

    # 既存metadata.json読み込み
    if not METADATA_FILE.exists():
        print(f"✗ {METADATA_FILE} が見つかりません")
        return

    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # videosセクションを生成
    videos = []
    stats = {
        'total': 0,
        'with_transcript': 0,
        'without_transcript': 0,
        'skipped': 0
    }

    print("\n動画情報を統合中...")

    for category_name, video_list in video_data.get('categories', {}).items():
        # プレイリスト/Loomはスキップ
        if category_name in ['playlists', 'other_platforms']:
            stats['skipped'] += len(video_list)
            print(f"  [SKIP] {category_name}: {len(video_list)}件")
            continue

        for video in video_list:
            title = video.get('title', '')
            url = video.get('url', '')
            video_id = extract_youtube_id(url)

            stats['total'] += 1

            # 文字起こしファイル検索
            transcript_file = get_transcript_file(category_name, title)

            if transcript_file:
                stats['with_transcript'] += 1
                status_icon = "✓"
            else:
                stats['without_transcript'] += 1
                status_icon = "✗"

            # 動画長を取得
            duration = get_duration_from_transcript(transcript_file)

            # 取得方法を判定
            method = "unknown"
            if transcript_file:
                if "zoom_consultations" in category_name or "interview_videos" in category_name:
                    method = "whisper"
                else:
                    method = "youtube_api"

            video_entry = {
                "title": title,
                "url": url,
                "youtube_id": video_id,
                "category": category_name,
                "transcript_file": transcript_file,
                "duration": duration,
                "duration_formatted": format_duration(duration) if duration > 0 else "00:00",
                "method": method,
                "has_transcript": transcript_file is not None
            }

            videos.append(video_entry)

            print(f"  [{status_icon}] {category_name}/{title[:50]}")

    # metadata.jsonのvideosセクションを更新
    metadata['videos'] = videos
    metadata['video_stats'] = {
        'total_videos': stats['total'],
        'with_transcript': stats['with_transcript'],
        'without_transcript': stats['without_transcript'],
        'skipped': stats['skipped'],
        'completion_rate': f"{stats['with_transcript'] / stats['total'] * 100:.1f}%" if stats['total'] > 0 else "0%"
    }

    # 保存
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print("メタデータ統合完了")
    print(f"{'='*60}")
    print(f"総動画数: {stats['total']}件")
    print(f"文字起こしあり: {stats['with_transcript']}件")
    print(f"文字起こしなし: {stats['without_transcript']}件")
    print(f"スキップ: {stats['skipped']}件")
    print(f"完了率: {metadata['video_stats']['completion_rate']}")
    print(f"\n✓ metadata.json更新完了: {METADATA_FILE}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
