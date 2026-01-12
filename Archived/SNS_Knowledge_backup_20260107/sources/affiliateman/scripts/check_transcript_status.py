#!/usr/bin/env python3
"""
文字起こし状況確認スクリプト

video_urls_complete.jsonと既存の文字起こしファイルを比較し、
未取得動画をリスト化。YouTube Transcript API利用可否も判定。
"""

import json
import re
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"

def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None

def check_youtube_api_availability(video_id):
    """YouTube Transcript APIで字幕取得可能かチェック"""
    try:
        YouTubeTranscriptApi.get_transcript(video_id, languages=['ja', 'ja-JP'])
        return True, "ja"
    except:
        try:
            YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            return True, "en"
        except:
            return False, None

def sanitize_filename(title):
    """ファイル名として使える文字列に変換"""
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = title
    for char in invalid_chars:
        sanitized = sanitized.replace(char, '_')
    if len(sanitized) > 200:
        sanitized = sanitized[:200]
    return sanitized

def main():
    print("=" * 60)
    print("文字起こし状況確認開始")
    print("=" * 60)

    # video_urls_complete.json読み込み
    with open(VIDEO_URLS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 既存の文字起こしファイルをスキャン
    existing_files = set()
    if OUTPUT_BASE_DIR.exists():
        for file in OUTPUT_BASE_DIR.rglob("*.md"):
            # _formatted版は除外
            if not file.name.endswith("_formatted.md"):
                existing_files.add(file.stem)

    print(f"既存文字起こしファイル: {len(existing_files)}件\n")

    # 各カテゴリの動画を処理
    results = {
        "already_transcribed": [],
        "youtube_api_available": [],
        "whisper_required": [],
        "skipped": [],
        "total_count": 0
    }

    categories = data.get('categories', {})

    for category_name, videos in categories.items():
        print(f"\n処理中: {category_name} ({len(videos)}件)")

        for video in videos:
            title = video.get('title', '')
            url = video.get('url', '')
            video_id = extract_youtube_id(url)

            results["total_count"] += 1

            # Loom動画やプレイリストはスキップ
            if 'loom.com' in url:
                results["skipped"].append({
                    "title": title,
                    "url": url,
                    "category": category_name,
                    "reason": "Loom動画"
                })
                print(f"  [SKIP] {title[:50]} - Loom動画")
                continue

            if category_name == 'playlists' or ('list=' in url and 'watch?v=' not in url):
                results["skipped"].append({
                    "title": title,
                    "url": url,
                    "category": category_name,
                    "reason": "プレイリスト"
                })
                print(f"  [SKIP] {title[:50]} - プレイリスト")
                continue

            # 既存ファイルチェック
            sanitized_title = sanitize_filename(title)
            if sanitized_title in existing_files:
                results["already_transcribed"].append({
                    "title": title,
                    "url": url,
                    "category": category_name
                })
                print(f"  [DONE] {title[:50]}")
                continue

            # YouTube API利用可否チェック
            if video_id:
                available, lang = check_youtube_api_availability(video_id)
                if available:
                    results["youtube_api_available"].append({
                        "title": title,
                        "url": url,
                        "video_id": video_id,
                        "category": category_name,
                        "language": lang
                    })
                    print(f"  [YT-API] {title[:50]} ({lang})")
                else:
                    results["whisper_required"].append({
                        "title": title,
                        "url": url,
                        "video_id": video_id,
                        "category": category_name
                    })
                    print(f"  [WHISPER] {title[:50]}")
            else:
                results["whisper_required"].append({
                    "title": title,
                    "url": url,
                    "video_id": video_id,
                    "category": category_name
                })
                print(f"  [WHISPER] {title[:50]} - ID抽出失敗")

    # JSONファイルに保存
    output_file = PROJECT_ROOT / "scripts" / "transcript_status_report.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # サマリー表示
    print(f"\n{'='*60}")
    print("処理結果サマリー")
    print(f"{'='*60}")
    print(f"既存文字起こし: {len(results['already_transcribed'])}件")
    print(f"YouTube API取得可能: {len(results['youtube_api_available'])}件")
    print(f"Whisper API必要: {len(results['whisper_required'])}件")
    print(f"スキップ（Loom/プレイリスト）: {len(results['skipped'])}件")
    print(f"総動画数: {results['total_count']}件")
    print(f"{'='*60}")
    print(f"\nレポート保存: {output_file}")

    # カテゴリ別内訳
    if results['youtube_api_available']:
        print(f"\n【YouTube API取得可能動画】")
        for video in results['youtube_api_available']:
            print(f"  - [{video['category']}] {video['title'][:60]}")

    if results['whisper_required']:
        print(f"\n【Whisper API必要動画】")
        for video in results['whisper_required']:
            print(f"  - [{video['category']}] {video['title'][:60]}")

if __name__ == "__main__":
    main()
