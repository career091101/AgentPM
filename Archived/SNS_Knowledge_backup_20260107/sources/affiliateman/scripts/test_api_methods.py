#!/usr/bin/env python3
"""
youtube-transcript-apiの正しい使い方を確認
"""

from youtube_transcript_api import YouTubeTranscriptApi

test_video_id = "Q2kuqnzSFjg"

print(f"テスト動画ID: {test_video_id}")
print("=" * 60)

# fetchメソッドを試す
print("\nfetchメソッドを試します...")
try:
    result = YouTubeTranscriptApi.fetch(test_video_id)
    print(f"✓ fetch成功")
    print(f"結果の型: {type(result)}")
    print(f"結果: {str(result)[:200]}...")
except Exception as e:
    print(f"✗ fetchエラー: {type(e).__name__}: {e}")

# listメソッドを試す
print("\n\nlistメソッドを試します...")
try:
    result = YouTubeTranscriptApi.list(test_video_id)
    print(f"✓ list成功")
    print(f"結果の型: {type(result)}")
    print(f"結果: {str(result)[:200]}...")
except Exception as e:
    print(f"✗ listエラー: {type(e).__name__}: {e}")

print("\n" + "=" * 60)
