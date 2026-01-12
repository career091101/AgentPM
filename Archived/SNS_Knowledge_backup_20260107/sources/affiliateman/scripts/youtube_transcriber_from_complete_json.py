#!/usr/bin/env python3
"""
YouTube文字起こし取得スクリプト（video_urls_complete.json用）

video_urls_complete.jsonから全52件の動画を読み取り、文字起こしを取得
"""

import json
import time
import re
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
DELAY = 0.5  # API呼び出し間隔（秒）


def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    # 通常のYouTube URL
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    if match:
        return match.group(1)

    # Loom URLの場合はNone
    if 'loom.com' in url:
        return None

    return None


def get_transcript(video_id):
    """YouTube動画の文字起こしを取得"""
    if not video_id:
        return None

    try:
        # 日本語字幕を試す
        try:
            entries = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja', 'ja-JP'])
        except:
            # 英語字幕を試す
            try:
                entries = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            except:
                return None

        if not entries:
            return None

        # タイムスタンプ付きフォーマット
        formatted = []
        for entry in entries:
            timestamp = format_timestamp(entry['start'])
            text = entry['text'].strip()
            formatted.append(f"[{timestamp}] {text}")

        # プレーンテキスト版も作成
        plain_text = '\n'.join([entry['text'].strip() for entry in entries])

        return {
            'formatted': '\n'.join(formatted),
            'plain': plain_text,
            'duration': entries[-1]['start'] + entries[-1]['duration'] if entries else 0
        }

    except TranscriptsDisabled:
        print(f"  ⚠ 字幕が無効: {video_id}")
    except NoTranscriptFound:
        print(f"  ⚠ 字幕が見つかりません: {video_id}")
    except Exception as e:
        print(f"  ✗ エラー: {video_id} - {e}")

    return None


def format_timestamp(seconds):
    """秒数をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def sanitize_filename(title):
    """ファイル名として使える文字列に変換"""
    # 使えない文字を置換
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = title
    for char in invalid_chars:
        sanitized = sanitized.replace(char, '_')

    # 長すぎる場合は切り詰め
    if len(sanitized) > 200:
        sanitized = sanitized[:200]

    return sanitized


def process_transcripts():
    """video_urls_complete.jsonから全動画を処理"""
    print("=" * 60)
    print("YouTube文字起こし取得開始")
    print(f"入力ファイル: {VIDEO_URLS_FILE}")
    print("=" * 60)

    if not VIDEO_URLS_FILE.exists():
        print(f"✗ {VIDEO_URLS_FILE} が見つかりません")
        return

    with open(VIDEO_URLS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = data.get('categories', {})
    stats = {
        'success': 0,
        'failed': 0,
        'skipped': 0
    }

    # カテゴリ別に処理
    for category_name, videos in categories.items():
        print(f"\n{'=' * 60}")
        print(f"カテゴリ: {category_name} ({len(videos)}件)")
        print(f"{'=' * 60}")

        # カテゴリ別ディレクトリ作成
        category_dir = OUTPUT_BASE_DIR / category_name
        category_dir.mkdir(parents=True, exist_ok=True)

        for i, video in enumerate(videos, 1):
            title = video.get('title', 'Untitled')
            url = video.get('url', '')
            note = video.get('note', '')

            print(f"\n[{i}/{len(videos)}] {title}")
            print(f"  URL: {url[:60]}...")

            # Loom動画はスキップ
            if 'loom.com' in url:
                print(f"  ⚠ Loom動画のため、手動処理が必要です")
                stats['skipped'] += 1
                continue

            # プレイリストURLの場合もスキップ（個別動画として処理すべき）
            if 'list=' in url and 'watch?v=' not in url:
                print(f"  ⚠ プレイリストのため、個別動画として処理してください")
                stats['skipped'] += 1
                continue

            # YouTube IDを抽出
            video_id = extract_youtube_id(url)
            if not video_id:
                print(f"  ✗ YouTube IDの抽出に失敗")
                stats['failed'] += 1
                continue

            print(f"  Video ID: {video_id}")

            # 文字起こし取得
            transcript = get_transcript(video_id)
            time.sleep(DELAY)

            if transcript:
                # ファイル名をサニタイズ
                safe_filename = sanitize_filename(title)

                # タイムスタンプ付き文字起こし
                formatted_file = category_dir / f"{safe_filename}_formatted.md"
                with open(formatted_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"**YouTube**: {url}\n")
                    f.write(f"**Video ID**: {video_id}\n")
                    f.write(f"**カテゴリ**: {category_name}\n")
                    f.write(f"**長さ**: {format_timestamp(transcript['duration'])}\n\n")
                    f.write("---\n\n")
                    f.write(transcript['formatted'])

                # プレーンテキスト版
                plain_file = category_dir / f"{safe_filename}.md"
                with open(plain_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"**YouTube**: {url}\n")
                    f.write(f"**Video ID**: {video_id}\n")
                    f.write(f"**カテゴリ**: {category_name}\n\n")
                    f.write("---\n\n")
                    f.write(transcript['plain'])

                print(f"  ✓ 保存完了: {plain_file.name}")
                stats['success'] += 1
            else:
                stats['failed'] += 1

    print("\n" + "=" * 60)
    print("文字起こし取得完了")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"スキップ: {stats['skipped']}件")
    print(f"出力ディレクトリ: {OUTPUT_BASE_DIR}")
    print("=" * 60)

    # 失敗した動画のリスト作成
    if stats['failed'] > 0 or stats['skipped'] > 0:
        print("\n注意: 失敗またはスキップされた動画があります")
        print("ログを確認して、必要に応じてWhisper APIで処理してください")


if __name__ == "__main__":
    process_transcripts()
