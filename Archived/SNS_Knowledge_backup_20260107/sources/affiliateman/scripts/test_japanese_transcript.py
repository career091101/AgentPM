#!/usr/bin/env python3
"""
日本語字幕取得テスト
"""

from youtube_transcript_api import YouTubeTranscriptApi

test_video_id = "Q2kuqnzSFjg"

print(f"テスト動画ID: {test_video_id}")
print("=" * 60)

api = YouTubeTranscriptApi()

# 日本語字幕を取得
print("\n日本語字幕を取得中...")
try:
    # listで利用可能な字幕を取得
    transcript_list = api.list(test_video_id)

    # 日本語字幕を検索
    ja_transcript = transcript_list.find_transcript(['ja'])

    # 字幕データを取得
    transcript_data = ja_transcript.fetch()

    print(f"✓ 日本語字幕取得成功")
    print(f"エントリ数: {len(transcript_data)}")
    print(f"\n最初のエントリの型: {type(transcript_data[0])}")
    print(f"最初のエントリの属性: {dir(transcript_data[0])}")
    print(f"\n最初の5エントリ:")
    for i, entry in enumerate(transcript_data[:5]):
        print(f"  [{i+1}] {entry.start:.2f}秒: {entry.text}")

except Exception as e:
    print(f"✗ エラー: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
