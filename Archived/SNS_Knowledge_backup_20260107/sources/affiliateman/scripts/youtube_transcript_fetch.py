#!/usr/bin/env python3
"""
YouTube Transcript API を使用した文字起こし取得スクリプト

Whisper APIの代替として、YouTubeの自動生成字幕を取得
"""

import json
import re
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
STATUS_REPORT_FILE = SCRIPTS_DIR / "transcript_status_report.json"
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


def format_timestamp(seconds):
    """秒数をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def get_transcript(video_id):
    """YouTube字幕を取得"""
    try:
        # 日本語字幕を試行
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja', 'ja-JP'])
            print(f"  ✓ 日本語字幕を取得")
        except:
            # 英語字幕を試行
            try:
                transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
                print(f"  ✓ 英語字幕を取得（日本語翻訳なし）")
            except:
                print(f"  ✗ 字幕が見つかりません")
                return None

        if not transcript_data:
            print(f"  ✗ 字幕データが空です")
            return None

        # プレーンテキスト版
        plain_text = ' '.join([item['text'] for item in transcript_data])

        # タイムスタンプ付き版
        formatted_lines = []
        for item in transcript_data:
            timestamp = format_timestamp(item['start'])
            text = item['text'].strip()
            formatted_lines.append(f"[{timestamp}] {text}")

        return {
            'plain': plain_text,
            'formatted': '\n'.join(formatted_lines)
        }

    except TranscriptsDisabled:
        print(f"  ✗ 字幕が無効化されています")
        return None
    except NoTranscriptFound:
        print(f"  ✗ 字幕が見つかりません")
        return None
    except Exception as e:
        print(f"  ✗ エラー: {type(e).__name__}: {e}")
        return None


def main():
    print("=" * 60)
    print("YouTube Transcript API 文字起こし取得")
    print("=" * 60)

    # ステータスレポート読み込み
    if not STATUS_REPORT_FILE.exists():
        print(f"✗ {STATUS_REPORT_FILE} が見つかりません")
        return

    with open(STATUS_REPORT_FILE, 'r', encoding='utf-8') as f:
        status = json.load(f)

    # Whisper必要な動画のうち、video_idがあるもの
    whisper_videos = [v for v in status.get('whisper_required', []) if v.get('video_id')]

    print(f"処理対象: {len(whisper_videos)}件")
    print("=" * 60)

    stats = {'success': 0, 'failed': 0}

    for i, video in enumerate(whisper_videos, 1):
        title = video.get('title', '')
        url = video.get('url', '')
        video_id = video.get('video_id')
        category = video.get('category', '')

        print(f"\n[{i}/{len(whisper_videos)}] {title}")
        print(f"  Video ID: {video_id}")
        print(f"  Category: {category}")

        # 既に文字起こし済みかチェック
        category_dir = OUTPUT_BASE_DIR / category
        safe_filename = sanitize_filename(title)
        plain_file = category_dir / f"{safe_filename}.md"

        if plain_file.exists():
            print(f"  ✓ 既に文字起こし済み")
            stats['success'] += 1
            continue

        # 字幕取得
        transcript = get_transcript(video_id)

        if transcript:
            # ディレクトリ作成
            category_dir.mkdir(parents=True, exist_ok=True)

            # タイムスタンプ付き版
            formatted_file = category_dir / f"{safe_filename}_formatted.md"
            with open(formatted_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {url}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: YouTube Transcript API\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーン版
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {url}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: YouTube Transcript API\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file.name}")
            stats['success'] += 1
        else:
            stats['failed'] += 1

    # 最終レポート
    print(f"\n{'='*60}")
    print("処理完了")
    print(f"{'='*60}")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
