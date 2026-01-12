#!/usr/bin/env python3
"""
Whisper APIを使用したYouTube文字起こし取得スクリプト

使用方法:
1. OpenAI APIキーを環境変数に設定: export OPENAI_API_KEY="your-key-here"
2. 実行: python whisper_transcriber.py

または、無料のローカルWhisperを使用する場合:
- requirements.txtにwhisperを追加してインストール
- USE_LOCAL_WHISPER = True に設定
"""

import os
import json
import time
import subprocess
from pathlib import Path

# 設定
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
TEMP_DIR = OUTPUT_DIR / "temp_audio"
USE_LOCAL_WHISPER = True  # True: ローカルWhisper使用, False: OpenAI API使用

# OpenAI APIを使う場合
if not USE_LOCAL_WHISPER:
    try:
        import openai
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            print("⚠️ OPENAI_API_KEYが設定されていません")
            print("export OPENAI_API_KEY='your-key-here' を実行してください")
            USE_LOCAL_WHISPER = True
            print("→ ローカルWhisperモードに切り替えます")
    except ImportError:
        print("openaiパッケージがインストールされていません")
        print("pip install openai でインストールしてください")
        USE_LOCAL_WHISPER = True
        print("→ ローカルWhisperモードに切り替えます")

# ローカルWhisperを使う場合
if USE_LOCAL_WHISPER:
    try:
        import whisper
    except ImportError:
        print("whisperパッケージがインストールされていません")
        print("pip install openai-whisper でインストールしてください")
        exit(1)


def download_audio(youtube_url, output_path):
    """YouTube動画から音声をダウンロード"""
    try:
        # yt-dlpを使用して音声のみダウンロード
        command = [
            'yt-dlp',
            '-x',  # 音声のみ抽出
            '--audio-format', 'mp3',
            '--audio-quality', '0',  # 最高品質
            '-o', str(output_path),
            youtube_url
        ]

        subprocess.run(command, check=True, capture_output=True)
        return True

    except subprocess.CalledProcessError as e:
        print(f"  ✗ 音声ダウンロードエラー: {e}")
        return False
    except FileNotFoundError:
        print("  ✗ yt-dlpがインストールされていません")
        print("    brew install yt-dlp または pip install yt-dlp")
        return False


def transcribe_with_openai_api(audio_file):
    """OpenAI Whisper APIで文字起こし"""
    # ファイルサイズチェック(OpenAI APIは25MB制限)
    file_size = audio_file.stat().st_size
    if file_size > 25 * 1024 * 1024:  # 25MB
        print(f"  ⚠️ ファイルサイズ超過({file_size / 1024 / 1024:.1f}MB > 25MB)")
        print(f"  → ローカルWhisperで処理します")
        return transcribe_with_local_whisper(audio_file)

    try:
        with open(audio_file, 'rb') as f:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                language="ja",
                response_format="verbose_json"
            )

        # タイムスタンプ付きテキストを生成
        formatted = []
        plain_text = []

        for segment in transcript.segments:
            timestamp = format_timestamp(segment.start)
            text = segment.text.strip()
            formatted.append(f"[{timestamp}] {text}")
            plain_text.append(text)

        return {
            'formatted': '\n'.join(formatted),
            'plain': '\n'.join(plain_text),
            'duration': transcript.duration
        }

    except Exception as e:
        print(f"  ✗ Whisper APIエラー: {e}")
        return None


def transcribe_with_local_whisper(audio_file, model_size="base"):
    """ローカルWhisperで文字起こし"""
    try:
        print(f"  ローカルWhisperモデル読み込み中... (model: {model_size})")
        model = whisper.load_model(model_size)

        print(f"  文字起こし実行中...")
        result = model.transcribe(str(audio_file), language="ja", verbose=False)

        # タイムスタンプ付きテキストを生成
        formatted = []
        plain_text = []

        for segment in result['segments']:
            timestamp = format_timestamp(segment['start'])
            text = segment['text'].strip()
            formatted.append(f"[{timestamp}] {text}")
            plain_text.append(text)

        return {
            'formatted': '\n'.join(formatted),
            'plain': '\n'.join(plain_text),
            'duration': result.get('duration', 0)
        }

    except Exception as e:
        print(f"  ✗ ローカルWhisperエラー: {e}")
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


def process_video(video_info, category):
    """動画を処理して文字起こしを取得"""
    video_id = video_info['youtube_id']
    title = video_info['title']
    youtube_url = video_info['youtube_url']

    print(f"\n処理中: {title}")
    print(f"  Video ID: {video_id}")

    # 既存ファイルチェック
    filepath = Path(video_info['filepath'])
    if category == 'interviews':
        existing_transcript = filepath.parent / 'transcript.md'
    else:
        existing_transcript = filepath

    if existing_transcript.exists():
        # ファイルサイズをチェック（空または小さいファイルは再処理）
        file_size = existing_transcript.stat().st_size
        if file_size > 1000:  # 1KB以上なら文字起こし済みと判断
            print(f"  ⏭ スキップ: 文字起こし済み")
            return 'skipped'

    # 音声ファイルパス
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    audio_file = TEMP_DIR / f"{video_id}.mp3"

    # 音声ダウンロード
    if not audio_file.exists():
        print(f"  音声ダウンロード中...")
        if not download_audio(youtube_url, audio_file.with_suffix('')):
            return False

    # 実際のファイル名を確認（yt-dlpが拡張子を追加する）
    actual_audio = list(TEMP_DIR.glob(f"{video_id}.*"))
    if not actual_audio:
        print(f"  ✗ 音声ファイルが見つかりません")
        return False

    audio_file = actual_audio[0]
    print(f"  音声ファイル: {audio_file.name}")

    # 文字起こし
    if USE_LOCAL_WHISPER:
        print(f"  文字起こし中（ローカルWhisper）...")
        transcript = transcribe_with_local_whisper(audio_file)
    else:
        print(f"  文字起こし中（OpenAI API）...")
        transcript = transcribe_with_openai_api(audio_file)

    if not transcript:
        return False

    # 文字起こしを保存
    filepath = Path(video_info['filepath'])

    if category == 'interviews':
        # 対談動画: 専用ディレクトリに保存
        base_dir = filepath.parent
        formatted_file = base_dir / 'transcript_formatted.md'
        plain_file = base_dir / 'transcript.md'
    else:
        # ZOOMコンサル: ファイル自体を上書き
        formatted_file = filepath.parent / f"{filepath.stem}_formatted.md"
        plain_file = filepath

    # タイムスタンプ付き文字起こし
    with open(formatted_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title} - 文字起こし\n\n")
        f.write(f"**YouTube**: {youtube_url}\n")
        f.write(f"**Video ID**: {video_id}\n")
        f.write(f"**長さ**: {format_timestamp(transcript['duration'])}\n\n")
        f.write("---\n\n")
        f.write(transcript['formatted'])

    # プレーンテキスト版
    with open(plain_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**YouTube**: {youtube_url}\n")
        f.write(f"**Video ID**: {video_id}\n\n")
        f.write("---\n\n")
        f.write(transcript['plain'])

    print(f"  ✓ 保存完了: {plain_file}")

    # 音声ファイルを削除（ディスク容量節約）
    audio_file.unlink()

    return True


def main():
    """メイン処理"""
    print("=" * 60)
    print("YouTube文字起こし取得（Whisper使用）")
    print(f"モード: {'ローカルWhisper' if USE_LOCAL_WHISPER else 'OpenAI API'}")
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
        if not item.get('youtube_id'):
            stats['skipped'] += 1
            continue

        result = process_video(item, 'interviews')
        if result == 'skipped':
            stats['skipped'] += 1
        elif result:
            stats['success'] += 1
        else:
            stats['failed'] += 1

        time.sleep(1)  # レート制限対策

    # ZOOMコンサル
    print("\n=== ZOOMコンサルの文字起こし ===")
    for item in metadata.get('zoom', []):
        if not item.get('youtube_id'):
            stats['skipped'] += 1
            continue

        result = process_video(item, 'zoom')
        if result == 'skipped':
            stats['skipped'] += 1
        elif result:
            stats['success'] += 1
        else:
            stats['failed'] += 1

        time.sleep(1)

    print("\n" + "=" * 60)
    print("文字起こし取得完了")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"スキップ: {stats['skipped']}件")
    print("=" * 60)

    # 一時ファイルディレクトリを削除
    if TEMP_DIR.exists():
        import shutil
        shutil.rmtree(TEMP_DIR)
        print("\n一時ファイルを削除しました")


if __name__ == "__main__":
    main()
