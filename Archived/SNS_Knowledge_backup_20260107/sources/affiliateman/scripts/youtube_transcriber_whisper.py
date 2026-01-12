#!/usr/bin/env python3
"""
Whisper APIを使用したYouTube文字起こし取得スクリプト

字幕がない動画をWhisper APIで文字起こし
"""

import json
import subprocess
import re
import os
from pathlib import Path
from openai import OpenAI

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
TEMP_DIR = Path("/tmp/whisper_transcripts")

# 失敗した動画のIDリスト
FAILED_VIDEO_IDS = [
    # ZOOMコンサル（15件）
    "EifkWh4Pbw8",  # 3月のスペース
    "gZQ_ynYW-Ao",  # 8月ZOOMコンサル
    "FbvmCNSOGIs",  # 9月ZOOMコンサル
    "EETbSO_mtaU",  # 10月ZOOMコンサル
    "IxaIpmPXROs",  # 11月ZOOMコンサル
    "41TRGDhWyWk",  # 12月ZOOMコンサル
    "rQlQpSUpK9Q",  # 1月ZOOMコンサル
    "UJw-d0vOMHw",  # 2月ZOOMコンサル
    "7OavcPIOM3w",  # 3月ZOOMコンサル
    "ga-aPYaU_RU",  # 4月ZOOMコンサル
    "0bFmcFw2ZmQ",  # 5月ZOOMコンサル
    "QzDHpcgB9rA",  # 6月ZOOMコンサル
    "ucXvTChsZ3Q",  # 7月ZOOMコンサル
    "qm21QQ5EP1g",  # 8月ZOOMコンサル（2回目）
    "Eve641U4QXs",  # 9月ZOOMコンサル（2回目）
]

# OpenAI APIキーを環境変数から取得
client = None
if os.environ.get("OPENAI_API_KEY"):
    client = OpenAI()
else:
    print("⚠ OPENAI_API_KEYが設定されていません")
    print("export OPENAI_API_KEY='your-api-key' を実行してください")


def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    if match:
        return match.group(1)
    return None


def download_audio(video_id):
    """yt-dlpを使用して音声をダウンロード"""
    TEMP_DIR.mkdir(exist_ok=True)

    audio_file = TEMP_DIR / f"{video_id}.m4a"

    # 既にダウンロード済みならスキップ
    if audio_file.exists():
        print(f"  音声ファイルが既に存在します: {audio_file.name}")
        return audio_file

    try:
        # 音声のみダウンロード
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
    MAX_SIZE_MB = 23  # 25MBより安全マージンを持って設定
    file_size_mb = audio_file.stat().st_size / 1024 / 1024

    # 圧縮ファイル名
    compressed_file = audio_file.parent / f"{audio_file.stem}_compressed.mp3"

    # 既に圧縮済みかチェック
    if compressed_file.exists():
        compressed_size_mb = compressed_file.stat().st_size / 1024 / 1024
        if compressed_size_mb <= MAX_SIZE_MB:
            print(f"  圧縮ファイルを使用: {compressed_size_mb:.1f}MB")
            audio_file.unlink(missing_ok=True)  # 元ファイル削除
            return compressed_file
        else:
            # 圧縮ファイルが大きすぎる場合は再圧縮
            compressed_file.unlink()
            print(f"  圧縮ファイルが大きすぎるため再圧縮: {compressed_size_mb:.1f}MB")

    if file_size_mb <= MAX_SIZE_MB:
        print(f"  ファイルサイズOK: {file_size_mb:.1f}MB")
        return audio_file

    print(f"  ファイルサイズ大: {file_size_mb:.1f}MB → 圧縮が必要")

    try:
        # ビットレートを動的に計算（23MB制限内に収める）
        duration_seconds = file_size_mb * 60  # 大まかな見積もり：1MB≈1分≈60秒
        target_size_mb = MAX_SIZE_MB * 0.95  # 安全マージン
        target_bitrate_kbps = int((target_size_mb * 1024 * 8) / duration_seconds)

        # 最小16kbps、最大24kbps
        bitrate = max(16, min(24, target_bitrate_kbps))

        # ffmpegで圧縮
        cmd = [
            'ffmpeg',
            '-i', str(audio_file),
            '-vn',  # 動画なし
            '-ac', '1',  # モノラル
            '-ar', '16000',  # サンプリングレート16kHz
            '-ab', f'{bitrate}k',  # 動的ビットレート
            '-y',  # 上書き
            str(compressed_file)
        ]

        print(f"  音声圧縮中（モノラル {bitrate}kbps）...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        if result.returncode != 0:
            print(f"  ✗ 圧縮エラー: {result.stderr[:200]}")
            return audio_file  # 元ファイルを返す

        if not compressed_file.exists():
            print(f"  ✗ 圧縮ファイルが作成されませんでした")
            return audio_file

        compressed_size_mb = compressed_file.stat().st_size / 1024 / 1024
        print(f"  ✓ 圧縮完了: {compressed_size_mb:.1f}MB ({file_size_mb/compressed_size_mb:.1f}x削減)")

        # 元ファイルを削除
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
                language="ja",  # 日本語を指定
                response_format="verbose_json"
            )

        if not transcript.text:
            print(f"  ✗ 文字起こしが空です")
            return None

        # テキストのみの場合
        if not hasattr(transcript, 'segments') or not transcript.segments:
            return {
                'plain': transcript.text,
                'formatted': transcript.text  # タイムスタンプなし
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


def process_with_whisper():
    """Whisper APIで失敗した動画を処理"""
    print("=" * 60)
    print("Whisper API文字起こし取得開始")
    print(f"対象動画数: {len(FAILED_VIDEO_IDS)}件")
    print("=" * 60)

    if not client:
        print("\n✗ OpenAI APIキーが設定されていません")
        print("以下のコマンドでAPIキーを設定してください:")
        print("export OPENAI_API_KEY='your-api-key'")
        return

    if not VIDEO_URLS_FILE.exists():
        print(f"✗ {VIDEO_URLS_FILE} が見つかりません")
        return

    with open(VIDEO_URLS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # video_idからタイトルとカテゴリを取得するマッピングを作成
    video_mapping = {}
    for category_name, videos in data.get('categories', {}).items():
        for video in videos:
            url = video.get('url', '')
            video_id = extract_youtube_id(url)
            if video_id:
                video_mapping[video_id] = {
                    'title': video.get('title', 'Untitled'),
                    'url': url,
                    'category': category_name
                }

    stats = {'success': 0, 'failed': 0, 'skipped': 0}
    total_cost_estimate = 0

    for i, video_id in enumerate(FAILED_VIDEO_IDS, 1):
        if video_id not in video_mapping:
            print(f"\n[{i}/{len(FAILED_VIDEO_IDS)}] {video_id}")
            print(f"  ✗ マッピング情報が見つかりません")
            stats['failed'] += 1
            continue

        info = video_mapping[video_id]
        title = info['title']
        category = info['category']

        print(f"\n[{i}/{len(FAILED_VIDEO_IDS)}] {title}")
        print(f"  Video ID: {video_id}")
        print(f"  カテゴリ: {category}")

        # 既に文字起こし済みかチェック
        category_dir = OUTPUT_BASE_DIR / category
        safe_filename = sanitize_filename(title)
        plain_file = category_dir / f"{safe_filename}.md"

        if plain_file.exists():
            print(f"  ✓ 既に文字起こし済み: {plain_file.name}")
            stats['skipped'] += 1
            continue

        # 音声ダウンロード
        audio_file = download_audio(video_id)
        if not audio_file:
            stats['failed'] += 1
            continue

        # 25MB制限のため圧縮（必要な場合）
        audio_file = compress_audio_if_needed(audio_file)
        if not audio_file:
            stats['failed'] += 1
            continue

        # ファイルサイズからコスト見積もり
        file_size_mb = audio_file.stat().st_size / 1024 / 1024
        estimated_minutes = file_size_mb / 1.0  # 大まかな見積もり: 1MB ≈ 1分
        estimated_cost = estimated_minutes * 0.006
        total_cost_estimate += estimated_cost
        print(f"  推定コスト: ${estimated_cost:.3f} ({estimated_minutes:.1f}分相当)")

        # Whisper APIで文字起こし
        transcript = transcribe_with_whisper(audio_file)

        if transcript:
            # カテゴリ別ディレクトリ
            category_dir = OUTPUT_BASE_DIR / category
            category_dir.mkdir(parents=True, exist_ok=True)

            # ファイル名をサニタイズ
            safe_filename = sanitize_filename(title)

            # タイムスタンプ付き文字起こし
            formatted_file = category_dir / f"{safe_filename}_formatted.md"
            with open(formatted_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {info['url']}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: Whisper API\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーンテキスト版
            plain_file = category_dir / f"{safe_filename}.md"
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {info['url']}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n")
                f.write(f"**文字起こし方法**: Whisper API\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file.name}")
            stats['success'] += 1

            # 音声ファイルを削除してディスク容量を節約
            audio_file.unlink()
            print(f"  ✓ 音声ファイル削除")
        else:
            stats['failed'] += 1

    print("\n" + "=" * 60)
    print("Whisper API文字起こし取得完了")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"スキップ: {stats['skipped']}件")
    print(f"推定総コスト: ${total_cost_estimate:.2f}")
    print(f"出力ディレクトリ: {OUTPUT_BASE_DIR}")
    print("=" * 60)

    if stats['success'] > 0:
        print(f"\n✓ {stats['success']}件の文字起こしを取得しました")
    if stats['failed'] > 0:
        print(f"\n注意: {stats['failed']}件の動画で文字起こしを取得できませんでした")


if __name__ == "__main__":
    process_with_whisper()
