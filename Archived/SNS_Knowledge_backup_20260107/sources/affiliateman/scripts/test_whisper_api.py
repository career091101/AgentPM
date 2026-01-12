#!/usr/bin/env python3
"""
Whisper API直接テスト
"""

import os
from pathlib import Path
from openai import OpenAI

# .envファイルから読み込み
env_file = Path(__file__).parent.parent / ".env"
if env_file.exists():
    with open(env_file, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# APIキー
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("✗ OPENAI_API_KEYが設定されていません")
    exit(1)

client = OpenAI(api_key=api_key)

# テスト用音声ファイル（2月ZOOMコンサル - 17MB）
audio_file = Path("/tmp/whisper_transcripts/UJw-d0vOMHw_compressed.mp3")

if not audio_file.exists():
    print(f"✗ 音声ファイルが見つかりません: {audio_file}")
    exit(1)

print(f"音声ファイル: {audio_file}")
print(f"ファイルサイズ: {audio_file.stat().st_size / 1024 / 1024:.1f}MB")
print("\nWhisper API呼び出し中...")

try:
    with open(audio_file, 'rb') as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="ja",
            response_format="verbose_json"
        )

    print("✓ 成功！")
    print(f"テキスト長: {len(transcript.text)}文字")
    print(f"最初の100文字: {transcript.text[:100]}")

    if hasattr(transcript, 'segments') and transcript.segments:
        print(f"セグメント数: {len(transcript.segments)}")
        print(f"最初のセグメント: {transcript.segments[0]}")

except Exception as e:
    print(f"✗ エラー: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
