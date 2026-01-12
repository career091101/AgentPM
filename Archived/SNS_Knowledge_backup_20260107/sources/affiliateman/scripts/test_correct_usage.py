#!/usr/bin/env python3
"""
youtube-transcript-apiの正しい使い方を確認（ドキュメント参照）
"""

from youtube_transcript_api import YouTubeTranscriptApi

test_video_id = "Q2kuqnzSFjg"

print(f"テスト動画ID: {test_video_id}")
print("=" * 60)

# インスタンス作成を試す
print("\nYouTubeTranscriptApiのインスタンス化を試します...")
try:
    api = YouTubeTranscriptApi()
    print(f"✓ インスタンス作成成功: {type(api)}")

    # fetchメソッド
    print("\nfetchメソッドを試します...")
    result = api.fetch(test_video_id)
    print(f"✓ fetch成功")
    print(f"結果の型: {type(result)}")
    if isinstance(result, list) and len(result) > 0:
        print(f"最初のエントリ: {result[0]}")
except Exception as e:
    print(f"✗ エラー: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
