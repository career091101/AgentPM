#!/usr/bin/env python3
"""
Gemini 2.0 Flash を使用した文字起こし取得スクリプト
"""

import json
import re
import subprocess
import os
import time
from pathlib import Path
import google.generativeai as genai

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
STATUS_REPORT_FILE = SCRIPTS_DIR / "transcript_status_report.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
TEMP_DIR = Path("/tmp/gemini_transcripts")

# Gemini APIキー
GEMINI_API_KEY = "AIzaSyDXzxCzKdWDKBD9IZFgUJR9-wtfM5rWI5c"
genai.configure(api_key=GEMINI_API_KEY)


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


def download_audio(video_id):
    """yt-dlpを使用して音声をダウンロード"""
    TEMP_DIR.mkdir(exist_ok=True)
    audio_file = TEMP_DIR / f"{video_id}.m4a"

    # 既にダウンロード済みならスキップ
    if audio_file.exists():
        print(f"  音声ファイルが既に存在: {audio_file.name}")
        return audio_file

    try:
        cmd = [
            'yt-dlp',
            '-f', 'bestaudio[ext=m4a]',
            '--output', str(audio_file),
            f'https://www.youtube.com/watch?v={video_id}'
        ]

        print(f"  音声ダウンロード中...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        if result.returncode != 0:
            print(f"  ✗ ダウンロードエラー: {result.stderr[:200]}")
            return None

        if not audio_file.exists():
            print(f"  ✗ 音声ファイルが作成されませんでした")
            return None

        print(f"  ✓ 音声ダウンロード完了: {audio_file.stat().st_size / 1024 / 1024:.1f}MB")
        return audio_file

    except subprocess.TimeoutExpired:
        print(f"  ✗ ダウンロードタイムアウト")
    except Exception as e:
        print(f"  ✗ ダウンロードエラー: {type(e).__name__}: {e}")

    return None


def transcribe_with_gemini(audio_file):
    """Gemini APIで文字起こし"""
    try:
        print(f"  Gemini API文字起こし中...")

        # モデル設定
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # 音声ファイルをアップロード
        print(f"  ファイルアップロード中...")
        audio_file_obj = genai.upload_file(path=str(audio_file))

        # アップロード完了を待機
        while audio_file_obj.state.name == "PROCESSING":
            print(f"  処理中...")
            time.sleep(2)
            audio_file_obj = genai.get_file(audio_file_obj.name)

        if audio_file_obj.state.name == "FAILED":
            print(f"  ✗ ファイル処理に失敗しました")
            return None

        # 文字起こしを要求
        prompt = """この音声ファイルを日本語で文字起こししてください。

以下のフォーマットで出力してください：
- タイムスタンプ付き（[HH:MM:SS]形式）
- 話者が変わる箇所で改行
- 可能な限り正確に
"""

        response = model.generate_content([prompt, audio_file_obj])

        # アップロードしたファイルを削除
        genai.delete_file(audio_file_obj.name)

        if not response.text:
            print(f"  ✗ 文字起こしが空です")
            return None

        print(f"  ✓ 文字起こし完了: {len(response.text)}文字")

        # タイムスタンプ付きと思われるテキストをそのまま使用
        return {
            'plain': response.text,
            'formatted': response.text  # Geminiが既にフォーマット済み
        }

    except Exception as e:
        print(f"  ✗ Gemini APIエラー: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    print("=" * 60)
    print("Gemini 2.0 Flash 文字起こし取得")
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

        # 音声ダウンロード
        audio_file = download_audio(video_id)
        if not audio_file:
            stats['failed'] += 1
            continue

        # Gemini API文字起こし
        transcript = transcribe_with_gemini(audio_file)

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
                f.write(f"**文字起こし方法**: Gemini 2.0 Flash\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーン版
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {url}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: Gemini 2.0 Flash\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file.name}")

            # 音声ファイル削除
            audio_file.unlink()
            print(f"  ✓ 音声ファイル削除")

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
