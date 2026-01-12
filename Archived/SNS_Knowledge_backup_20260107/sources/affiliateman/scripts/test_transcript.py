#!/usr/bin/env python3
"""
YouTube文字起こしテスト - 1件の動画で詳細確認
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import traceback

# テスト用動画ID
test_video_id = "Q2kuqnzSFjg"  # 2025年最新版Xで毎月複数アカで300~800万円稼ぐ裏側公開

print(f"テスト動画ID: {test_video_id}")
print(f"URL: https://www.youtube.com/watch?v={test_video_id}")
print("=" * 60)

# 日本語字幕を取得
print("\n日本語字幕を取得中...")
try:
    entries = YouTubeTranscriptApi.get_transcript(test_video_id, languages=['ja'])
    print(f"\n✓ 日本語字幕取得成功 ({len(entries)}エントリ)")
    print(f"\n最初の5エントリ:")
    for i, entry in enumerate(entries[:5]):
        print(f"  [{i+1}] {entry['start']:.2f}秒: {entry['text']}")
except TranscriptsDisabled as e:
    print(f"\n✗ 字幕が無効: {e}")
    print("\n詳細:")
    traceback.print_exc()
except NoTranscriptFound as e:
    print(f"\n✗ 字幕が見つかりません: {e}")
    print("\n詳細:")
    traceback.print_exc()
except Exception as e:
    print(f"\n✗ エラー発生: {type(e).__name__}: {e}")
    print("\n詳細:")
    traceback.print_exc()

# 言語指定なしで試す
print("\n\n言語指定なしで試す...")
try:
    entries = YouTubeTranscriptApi.get_transcript(test_video_id)
    print(f"\n✓ 字幕取得成功 ({len(entries)}エントリ)")
    print(f"\n最初の3エントリ:")
    for i, entry in enumerate(entries[:3]):
        print(f"  [{i+1}] {entry['start']:.2f}秒: {entry['text']}")
except Exception as e:
    print(f"\n✗ エラー: {type(e).__name__}: {e}")
    print("\n詳細:")
    traceback.print_exc()

print("\n" + "=" * 60)
