#!/usr/bin/env python3
"""
Whisper API バッチ処理スクリプト（進捗保存・再開機能付き）

transcript_status_report.jsonからWhisper必要動画を読み込み、
バッチ処理で文字起こしを取得。進捗を保存し、中断再開が可能。
"""

import json
import subprocess
import re
import os
import argparse
from pathlib import Path
from openai import OpenAI

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
STATUS_REPORT_FILE = SCRIPTS_DIR / "transcript_status_report.json"
PROGRESS_FILE = SCRIPTS_DIR / "whisper_progress.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
TEMP_DIR = Path("/tmp/whisper_transcripts")

# .envファイルから読み込み
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    with open(env_file, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# OpenAI APIキー（タイムアウト10分）
client = None
if os.environ.get("OPENAI_API_KEY"):
    client = OpenAI(timeout=600.0)  # 10分のタイムアウト


def load_progress():
    """進捗状態をロード"""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "completed_videos": [],
        "failed_videos": [],
        "total_processed": 0,
        "total_cost": 0.0,
        "remaining_videos": []
    }


def save_progress(progress):
    """進捗状態を保存"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None


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


def compress_audio_if_needed(audio_file):
    """ファイルが25MBより大きい場合、圧縮する"""
    MAX_SIZE_MB = 15  # Whisper API制限25MBに対して安全マージン（20→15に変更）
    file_size_mb = audio_file.stat().st_size / 1024 / 1024

    compressed_file = audio_file.parent / f"{audio_file.stem}_compressed.mp3"

    # 既に圧縮済みかチェック
    if compressed_file.exists():
        compressed_size_mb = compressed_file.stat().st_size / 1024 / 1024
        if compressed_size_mb <= MAX_SIZE_MB:
            print(f"  圧縮ファイルを使用: {compressed_size_mb:.1f}MB")
            audio_file.unlink(missing_ok=True)
            return compressed_file
        else:
            compressed_file.unlink()
            print(f"  圧縮ファイルが大きすぎるため再圧縮: {compressed_size_mb:.1f}MB")

    if file_size_mb <= MAX_SIZE_MB:
        print(f"  ファイルサイズOK: {file_size_mb:.1f}MB")
        return audio_file

    print(f"  ファイルサイズ大: {file_size_mb:.1f}MB → 圧縮が必要")

    try:
        # より正確な動画長推定（1MB ≈ 30-40秒の音声）
        duration_seconds = file_size_mb * 35
        target_size_mb = MAX_SIZE_MB * 0.90  # 90%に設定してさらに安全マージン
        target_bitrate_kbps = int((target_size_mb * 1024 * 8) / duration_seconds)
        bitrate = max(12, min(20, target_bitrate_kbps))  # 12-20kbpsに制限（16-24から変更）

        cmd = [
            'ffmpeg',
            '-i', str(audio_file),
            '-vn',
            '-ac', '1',
            '-ar', '16000',
            '-ab', f'{bitrate}k',
            '-y',
            str(compressed_file)
        ]

        print(f"  音声圧縮中（モノラル {bitrate}kbps）...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        if result.returncode != 0:
            print(f"  ✗ 圧縮エラー: {result.stderr[:200]}")
            return audio_file

        if not compressed_file.exists():
            print(f"  ✗ 圧縮ファイルが作成されませんでした")
            return audio_file

        compressed_size_mb = compressed_file.stat().st_size / 1024 / 1024
        print(f"  ✓ 圧縮完了: {compressed_size_mb:.1f}MB ({file_size_mb/compressed_size_mb:.1f}x削減)")

        # 圧縮後も大きすぎる場合は警告
        if compressed_size_mb > 24:
            print(f"  ⚠ 警告: 圧縮後も24MB超過、API制限に近い")

        audio_file.unlink()
        print(f"  ✓ 元ファイル削除")

        return compressed_file

    except subprocess.TimeoutExpired:
        print(f"  ✗ 圧縮タイムアウト")
    except Exception as e:
        print(f"  ✗ 圧縮エラー: {type(e).__name__}: {e}")

    return audio_file


def transcribe_with_whisper(audio_file):
    """Whisper APIで文字起こし"""
    if not client:
        print(f"  ✗ OpenAI APIクライアントが初期化されていません")
        return None

    try:
        print(f"  Whisper API文字起こし中...")

        with open(audio_file, 'rb') as f:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                language="ja",
                response_format="verbose_json",
                timeout=600.0  # 10分のタイムアウト
            )

        if not transcript.text:
            print(f"  ✗ 文字起こしが空です")
            return None

        # テキストのみの場合
        if not hasattr(transcript, 'segments') or not transcript.segments:
            return {
                'plain': transcript.text,
                'formatted': transcript.text
            }

        # タイムスタンプ付き
        formatted_lines = []
        for segment in transcript.segments:
            timestamp = format_timestamp(segment.start)
            text = segment.text.strip()
            formatted_lines.append(f"[{timestamp}] {text}")

        return {
            'plain': transcript.text,
            'formatted': '\n'.join(formatted_lines)
        }

    except Exception as e:
        print(f"  ✗ Whisper APIエラー: {type(e).__name__}: {e}")
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
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = title
    for char in invalid_chars:
        sanitized = sanitized.replace(char, '_')

    if len(sanitized) > 200:
        sanitized = sanitized[:200]

    return sanitized


def main():
    parser = argparse.ArgumentParser(description='Whisper APIバッチ処理スクリプト')
    parser.add_argument('--resume', action='store_true', help='前回の続きから実行')
    parser.add_argument('--batch-size', type=int, default=0, help='一度に処理する動画数（0=全件）')
    parser.add_argument('--max-cost', type=float, default=5.0, help='累積コスト上限（USD）')
    parser.add_argument('--reset', action='store_true', help='進捗ファイルをリセット')
    args = parser.parse_args()

    print("=" * 60)
    print("Whisper API バッチ処理開始")
    print("=" * 60)

    # APIキーチェック
    if not client:
        print("\n✗ OPENAI_API_KEYが設定されていません")
        print("export OPENAI_API_KEY='your-api-key' を実行してください")
        return

    # ステータスレポート読み込み
    if not STATUS_REPORT_FILE.exists():
        print(f"✗ {STATUS_REPORT_FILE} が見つかりません")
        print("先にcheck_transcript_status.pyを実行してください")
        return

    with open(STATUS_REPORT_FILE, 'r', encoding='utf-8') as f:
        status = json.load(f)

    # 進捗読み込み
    if args.reset and PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
        print("進捗ファイルをリセットしました\n")

    progress = load_progress()
    completed_ids = set(v.get('video_id') for v in progress['completed_videos'] if v.get('video_id'))

    # 処理対象動画リスト
    whisper_videos = status.get('whisper_required', [])

    # video_idがある動画のみフィルタ
    whisper_videos = [v for v in whisper_videos if v.get('video_id')]

    # 再開モードの場合、未完了のみ
    if args.resume:
        whisper_videos = [v for v in whisper_videos if v.get('video_id') not in completed_ids]
        print(f"再開モード: 残り{len(whisper_videos)}件を処理")

    # バッチサイズ制御
    if args.batch_size > 0:
        whisper_videos = whisper_videos[:args.batch_size]

    print(f"処理対象: {len(whisper_videos)}件")
    print(f"累積コスト: ${progress['total_cost']:.2f} / 上限: ${args.max_cost}")
    print("=" * 60)

    stats = {'success': 0, 'failed': 0, 'cost_limit_reached': False}

    for i, video in enumerate(whisper_videos, 1):
        # コスト上限チェック
        if progress['total_cost'] >= args.max_cost:
            print(f"\n⚠ コスト上限に達しました: ${progress['total_cost']:.2f}")
            stats['cost_limit_reached'] = True
            break

        title = video.get('title', '')
        url = video.get('url', '')
        video_id = video.get('video_id')
        category = video.get('category', '')

        print(f"\n[{i}/{len(whisper_videos)}] {title}")
        print(f"  Category: {category}")
        if video_id:
            print(f"  Video ID: {video_id}")

        # video_idがない場合（サイト内ページ）はスキップ
        if not video_id:
            print(f"  ⚠ YouTube IDが取得できません - スキップ")
            progress['failed_videos'].append(video)
            stats['failed'] += 1
            save_progress(progress)
            continue

        # 既に文字起こし済みかチェック
        category_dir = OUTPUT_BASE_DIR / category
        safe_filename = sanitize_filename(title)
        plain_file = category_dir / f"{safe_filename}.md"

        if plain_file.exists():
            print(f"  ✓ 既に文字起こし済み")
            progress['completed_videos'].append(video)
            save_progress(progress)
            continue

        # 音声ダウンロード
        audio_file = download_audio(video_id)
        if not audio_file:
            progress['failed_videos'].append(video)
            stats['failed'] += 1
            save_progress(progress)
            continue

        # 圧縮（必要な場合）
        audio_file = compress_audio_if_needed(audio_file)

        # コスト見積もり
        file_size_mb = audio_file.stat().st_size / 1024 / 1024
        estimated_minutes = file_size_mb / 1.0
        estimated_cost = estimated_minutes * 0.006
        print(f"  推定コスト: ${estimated_cost:.3f} ({estimated_minutes:.1f}分相当)")

        # コスト上限チェック（事前）
        if progress['total_cost'] + estimated_cost > args.max_cost:
            print(f"  ⚠ この動画を処理するとコスト上限を超えます")
            print(f"  現在: ${progress['total_cost']:.2f}, 推定追加: ${estimated_cost:.3f}, 上限: ${args.max_cost}")
            stats['cost_limit_reached'] = True
            break

        # Whisper API文字起こし
        transcript = transcribe_with_whisper(audio_file)

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
                f.write(f"**文字起こし方法**: Whisper API\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーン版
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {url}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: Whisper API\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file.name}")

            # 音声ファイル削除
            audio_file.unlink()
            print(f"  ✓ 音声ファイル削除")

            # 進捗更新
            progress['completed_videos'].append(video)
            progress['total_processed'] += 1
            progress['total_cost'] += estimated_cost
            stats['success'] += 1
            save_progress(progress)

        else:
            progress['failed_videos'].append(video)
            stats['failed'] += 1
            save_progress(progress)

    # 最終レポート
    print(f"\n{'='*60}")
    print("処理完了")
    print(f"{'='*60}")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"累積処理数: {progress['total_processed']}件")
    print(f"累積コスト: ${progress['total_cost']:.2f}")
    if stats['cost_limit_reached']:
        print(f"⚠ コスト上限に達したため処理を中断しました")
        print(f"続きを実行するには: python {Path(__file__).name} --resume")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
