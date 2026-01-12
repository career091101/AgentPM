#!/usr/bin/env python3
"""
yt-dlpを使用したYouTube文字起こし取得スクリプト

失敗した22件の動画を取得
"""

import json
import subprocess
import re
from pathlib import Path

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"

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
    # プレイリスト（2件）- 重複除外
    # "8Lhh0YxAn2Y",  # 動画一覧（すでに成功）
    # "QWP5cep1rIA",  # 対談動画一覧（すでに成功）
]


def extract_youtube_id(url):
    """URLからYouTube IDを抽出"""
    youtube_regex = r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    if match:
        return match.group(1)
    return None


def get_transcript_ytdlp(video_id):
    """yt-dlpを使用して文字起こしを取得"""
    if not video_id:
        return None

    try:
        # 字幕をダウンロード（日本語優先、なければ英語）
        # --write-auto-sub: 自動生成字幕をダウンロード
        # --sub-lang: 言語指定
        # --skip-download: 動画本体はダウンロードしない
        # --write-sub: 字幕をダウンロード
        cmd = [
            'yt-dlp',
            '--write-auto-sub',
            '--sub-lang', 'ja,en',
            '--skip-download',
            '--output', f'/tmp/yt_{video_id}.%(ext)s',
            f'https://www.youtube.com/watch?v={video_id}'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if result.returncode != 0:
            print(f"  ⚠ yt-dlpエラー: {result.stderr[:200]}")
            return None

        # ダウンロードされた字幕ファイルを探す
        subtitle_files = list(Path('/tmp').glob(f'yt_{video_id}.*.vtt'))

        if not subtitle_files:
            print(f"  ⚠ 字幕ファイルが見つかりません")
            return None

        # 最初の字幕ファイルを読み込む
        subtitle_file = subtitle_files[0]
        with open(subtitle_file, 'r', encoding='utf-8') as f:
            vtt_content = f.read()

        # VTTファイルをパース
        transcript_data = parse_vtt(vtt_content)

        # ファイルを削除
        for file in subtitle_files:
            file.unlink()

        return transcript_data

    except subprocess.TimeoutExpired:
        print(f"  ✗ タイムアウト")
    except Exception as e:
        print(f"  ✗ エラー: {type(e).__name__}: {e}")

    return None


def parse_vtt(vtt_content):
    """VTTファイルをパースしてテキストを抽出"""
    lines = vtt_content.split('\n')
    entries = []
    current_text = []
    current_timestamp = None

    for line in lines:
        line = line.strip()

        # タイムスタンプ行
        if '-->' in line:
            # 開始時刻を抽出
            timestamp_match = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3})', line)
            if timestamp_match:
                current_timestamp = timestamp_match.group(1)
            continue

        # 空行はエントリの区切り
        if not line or line == 'WEBVTT' or line.startswith('Kind:') or line.startswith('Language:'):
            if current_text and current_timestamp:
                text = ' '.join(current_text)
                # HTMLタグを除去
                text = re.sub(r'<[^>]+>', '', text)
                entries.append({
                    'timestamp': current_timestamp,
                    'text': text.strip()
                })
                current_text = []
                current_timestamp = None
            continue

        # 数字のみの行はスキップ（字幕番号）
        if line.isdigit():
            continue

        # テキスト行
        current_text.append(line)

    # 最後のエントリを追加
    if current_text and current_timestamp:
        text = ' '.join(current_text)
        text = re.sub(r'<[^>]+>', '', text)
        entries.append({
            'timestamp': current_timestamp,
            'text': text.strip()
        })

    if not entries:
        return None

    # フォーマット
    formatted = '\n'.join([f"[{e['timestamp']}] {e['text']}" for e in entries])
    plain = '\n'.join([e['text'] for e in entries])

    return {
        'formatted': formatted,
        'plain': plain
    }


def sanitize_filename(title):
    """ファイル名として使える文字列に変換"""
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = title
    for char in invalid_chars:
        sanitized = sanitized.replace(char, '_')

    if len(sanitized) > 200:
        sanitized = sanitized[:200]

    return sanitized


def process_failed_videos():
    """失敗した動画をyt-dlpで処理"""
    print("=" * 60)
    print("yt-dlpによる文字起こし取得開始")
    print(f"対象動画数: {len(FAILED_VIDEO_IDS)}件")
    print("=" * 60)

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

    stats = {'success': 0, 'failed': 0}

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

        # 文字起こし取得
        transcript = get_transcript_ytdlp(video_id)

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
                f.write(f"**カテゴリ**: {category}\n\n")
                f.write("---\n\n")
                f.write(transcript['formatted'])

            # プレーンテキスト版
            plain_file = category_dir / f"{safe_filename}.md"
            with open(plain_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**YouTube**: {info['url']}\n")
                f.write(f"**Video ID**: {video_id}\n")
                f.write(f"**カテゴリ**: {category}\n\n")
                f.write("---\n\n")
                f.write(transcript['plain'])

            print(f"  ✓ 保存完了: {plain_file.name}")
            stats['success'] += 1
        else:
            stats['failed'] += 1

    print("\n" + "=" * 60)
    print("yt-dlp文字起こし取得完了")
    print(f"成功: {stats['success']}件")
    print(f"失敗: {stats['failed']}件")
    print(f"出力ディレクトリ: {OUTPUT_BASE_DIR}")
    print("=" * 60)

    if stats['success'] > 0:
        print(f"\n✓ {stats['success']}件の文字起こしを取得しました")
    if stats['failed'] > 0:
        print(f"\n注意: {stats['failed']}件の動画で文字起こしを取得できませんでした")


if __name__ == "__main__":
    process_failed_videos()
