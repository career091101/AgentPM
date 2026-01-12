#!/usr/bin/env python3
"""
YouTube文字起こし取得スクリプト

metadata.jsonからYouTube URLを読み取り、文字起こしを取得して保存
"""

import json
import time
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
DELAY = 0.5  # API呼び出し間隔（秒）


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


def process_transcripts():
    """メタデータからYouTube動画を処理"""
    print("=" * 60)
    print("YouTube文字起こし取得開始")
    print("=" * 60)

    metadata_file = OUTPUT_DIR / 'metadata.json'
    if not metadata_file.exists():
        print("✗ metadata.jsonが見つかりません")
        return

    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    stats = {'success': 0, 'failed': 0, 'skipped': 0}

    # 対談動画
    print("\n=== 対談動画の文字起こし ===")
    for item in metadata.get('interviews', []):
        video_id = item.get('youtube_id')
        if not video_id:
            stats['skipped'] += 1
            continue

        print(f"\n処理中: {item['title']}")
        print(f"  Video ID: {video_id}")

        transcript = get_transcript(video_id)
        time.sleep(DELAY)

        if transcript:
            # ファイルパスを取得
            filepath = Path(item['filepath'])
            base_dir = filepath.parent

            # タイムスタンプ付き文字起こし
            formatted_file = base_dir / 'transcript_formatted.md'
            with open(formatted_file, 'w', encoding='utf-8') as f:
                f.write(f"# {item['title']} - 文字起こし\n\n")
                f.write(f"**YouTube**: {item['youtube_url']}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**長さ**: {format_timestamp(transcript['duration'])}\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーンテキスト版
            plain_file = base_dir / 'transcript.md'
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {item['title']} - 文字起こし\n\n")
                f.write(f"**YouTube**: {item['youtube_url']}\n")
                f.write(f"**Video ID**: {video_id}\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file}")
            stats['success'] += 1
        else:
            stats['failed'] += 1

    # 動画教材
    print("\n=== 動画教材の文字起こし ===")
    for item in metadata.get('videos', []):
        video_id = item.get('youtube_id')
        if not video_id:
            stats['skipped'] += 1
            continue

        print(f"\n処理中: {item['title']}")
        print(f"  Video ID: {video_id}")

        transcript = get_transcript(video_id)
        time.sleep(DELAY)

        if transcript:
            # 既存のMarkdownファイルに追記
            filepath = Path(item['filepath'])
            if filepath.exists():
                with open(filepath, 'a', encoding='utf-8') as f:
                    f.write("\n\n---\n\n")
                    f.write("## 文字起こし\n\n")
                    f.write(transcript['plain'])
                print(f"  ✓ 追記完了: {filepath}")
                stats['success'] += 1
            else:
                stats['failed'] += 1
        else:
            stats['failed'] += 1

    # ZOOMコンサル
    print("\n=== ZOOMコンサルの文字起こし ===")
    for item in metadata.get('zoom', []):
        video_id = item.get('youtube_id')
        if not video_id:
            stats['skipped'] += 1
            continue

        print(f"\n処理中: {item['title']}")
        print(f"  Video ID: {video_id}")

        transcript = get_transcript(video_id)
        time.sleep(DELAY)

        if transcript:
            filepath = Path(item['filepath'])
            filepath.parent.mkdir(parents=True, exist_ok=True)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {item['title']}\n\n")
                f.write(f"**YouTube**: {item['youtube_url']}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**長さ**: {format_timestamp(transcript['duration'])}\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {filepath}")
            stats['success'] += 1
        else:
            stats['failed'] += 1

    print("\n" + "=" * 60)
    print("文字起こし取得完了")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"スキップ: {stats['skipped']}件")
    print("=" * 60)


if __name__ == "__main__":
    process_transcripts()
