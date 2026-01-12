#!/usr/bin/env python3
"""
最終検証スクリプト

文字起こしプロジェクトの完全性、品質を検証
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
VIDEO_URLS_FILE = PROJECT_ROOT / "video_urls_complete.json"
METADATA_FILE = PROJECT_ROOT / "metadata.json"
OUTPUT_BASE_DIR = PROJECT_ROOT / "video_transcripts"
CHUNKS_FILE = PROJECT_ROOT / "chunks" / "all_chunks.jsonl"


def check_file_quality(file_path):
    """ファイル品質をチェック"""
    if not file_path.exists():
        return {"exists": False}

    file_size = file_path.stat().st_size

    if file_size == 0:
        return {"exists": True, "size": 0, "empty": True}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 文字数
        char_count = len(content)

        # 日本語文字数（ひらがな、カタカナ、漢字）
        japanese_count = len(re.findall(r'[ぁ-んァ-ヶー一-龯]', content))
        japanese_ratio = japanese_count / char_count if char_count > 0 else 0

        # 行数
        line_count = len(content.split('\n'))

        return {
            "exists": True,
            "size": file_size,
            "empty": False,
            "char_count": char_count,
            "japanese_count": japanese_count,
            "japanese_ratio": japanese_ratio,
            "line_count": line_count
        }

    except Exception as e:
        return {"exists": True, "size": file_size, "error": str(e)}


def main():
    print("=" * 60)
    print("最終検証開始")
    print("=" * 60)

    # ファイル存在チェック
    if not VIDEO_URLS_FILE.exists():
        print(f"✗ {VIDEO_URLS_FILE} が見つかりません")
        return

    if not METADATA_FILE.exists():
        print(f"✗ {METADATA_FILE} が見つかりません")
        return

    # データ読み込み
    with open(VIDEO_URLS_FILE, 'r', encoding='utf-8') as f:
        video_data = json.load(f)

    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # 検証結果
    results = {
        "completeness": {},
        "quality": {},
        "metadata": {},
        "chunks": {}
    }

    # 1. 完全性チェック
    print("\n" + "=" * 60)
    print("1. 完全性チェック")
    print("=" * 60)

    total_videos = 0
    for category_name, videos in video_data.get('categories', {}).items():
        if category_name in ['playlists', 'other_platforms']:
            continue
        total_videos += len(videos)

    videos_in_metadata = len([v for v in metadata.get('videos', []) if v.get('has_transcript')])

    print(f"総動画数（video_urls_complete.json）: {total_videos}件")
    print(f"文字起こしあり（metadata.json）: {videos_in_metadata}件")
    print(f"文字起こしなし: {total_videos - videos_in_metadata}件")
    print(f"完了率: {videos_in_metadata / total_videos * 100:.1f}%")

    results["completeness"] = {
        "total_videos": total_videos,
        "transcribed": videos_in_metadata,
        "missing": total_videos - videos_in_metadata,
        "completion_rate": f"{videos_in_metadata / total_videos * 100:.1f}%"
    }

    # 2. ファイル品質チェック
    print("\n" + "=" * 60)
    print("2. ファイル品質チェック")
    print("=" * 60)

    quality_issues = []
    total_chars = 0
    total_japanese_chars = 0

    for video in metadata.get('videos', []):
        if not video.get('has_transcript'):
            continue

        transcript_file = video.get('transcript_file')
        if not transcript_file:
            continue

        file_path = PROJECT_ROOT / transcript_file
        quality = check_file_quality(file_path)

        if not quality.get('exists'):
            quality_issues.append(f"✗ ファイルが存在しません: {transcript_file}")
        elif quality.get('empty'):
            quality_issues.append(f"✗ ファイルが空です: {transcript_file}")
        elif quality.get('char_count', 0) < 100:
            quality_issues.append(f"⚠ 文字数が少ない ({quality['char_count']}文字): {transcript_file}")
        elif quality.get('japanese_ratio', 0) < 0.3:
            quality_issues.append(f"⚠ 日本語率が低い ({quality['japanese_ratio']*100:.1f}%): {transcript_file}")

        if 'char_count' in quality:
            total_chars += quality['char_count']
        if 'japanese_count' in quality:
            total_japanese_chars += quality['japanese_count']

    if quality_issues:
        print(f"\n品質問題: {len(quality_issues)}件")
        for issue in quality_issues[:10]:  # 最初の10件のみ表示
            print(f"  {issue}")
        if len(quality_issues) > 10:
            print(f"  ... 他 {len(quality_issues) - 10}件")
    else:
        print("✓ 品質問題なし")

    print(f"\n総文字数: {total_chars:,}文字")
    print(f"日本語文字数: {total_japanese_chars:,}文字")
    print(f"平均日本語率: {total_japanese_chars / total_chars * 100:.1f}%" if total_chars > 0 else "N/A")

    results["quality"] = {
        "total_chars": total_chars,
        "japanese_chars": total_japanese_chars,
        "issues_count": len(quality_issues),
        "issues": quality_issues[:20]  # 上位20件のみ保存
    }

    # 3. メタデータ整合性チェック
    print("\n" + "=" * 60)
    print("3. メタデータ整合性チェック")
    print("=" * 60)

    metadata_issues = []

    for video in metadata.get('videos', []):
        if video.get('has_transcript') and not video.get('transcript_file'):
            metadata_issues.append(f"✗ 文字起こしファイルパスが未設定: {video['title']}")

        if video.get('transcript_file'):
            file_path = PROJECT_ROOT / video['transcript_file']
            if not file_path.exists():
                metadata_issues.append(f"✗ ファイルが存在しません: {video['transcript_file']}")

    if metadata_issues:
        print(f"メタデータ問題: {len(metadata_issues)}件")
        for issue in metadata_issues[:10]:
            print(f"  {issue}")
        if len(metadata_issues) > 10:
            print(f"  ... 他 {len(metadata_issues) - 10}件")
    else:
        print("✓ メタデータ整合性OK")

    results["metadata"] = {
        "issues_count": len(metadata_issues),
        "issues": metadata_issues[:20]
    }

    # 4. チャンクファイル検証
    print("\n" + "=" * 60)
    print("4. チャンクファイル検証")
    print("=" * 60)

    if CHUNKS_FILE.exists():
        chunk_count = 0
        blog_chunks = 0
        video_chunks = 0
        invalid_chunks = 0

        with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        chunk = json.loads(line)
                        chunk_count += 1

                        if chunk.get('source_type') == 'video':
                            video_chunks += 1
                        else:
                            blog_chunks += 1

                    except json.JSONDecodeError:
                        invalid_chunks += 1

        print(f"総チャンク数: {chunk_count}件")
        print(f"  ブログチャンク: {blog_chunks}件")
        print(f"  動画チャンク: {video_chunks}件")
        if invalid_chunks > 0:
            print(f"  ⚠ 無効なチャンク: {invalid_chunks}件")

        results["chunks"] = {
            "total": chunk_count,
            "blog": blog_chunks,
            "video": video_chunks,
            "invalid": invalid_chunks
        }
    else:
        print("✗ チャンクファイルが存在しません")
        results["chunks"] = {"error": "チャンクファイルが存在しません"}

    # 最終サマリー
    print("\n" + "=" * 60)
    print("最終検証サマリー")
    print("=" * 60)
    print(f"✓ 完了率: {results['completeness']['completion_rate']}")
    print(f"✓ 総文字数: {results['quality']['total_chars']:,}文字")
    print(f"✓ 総チャンク数: {results['chunks'].get('total', 0)}件")

    if results['quality']['issues_count'] > 0:
        print(f"⚠ 品質問題: {results['quality']['issues_count']}件")
    if results['metadata']['issues_count'] > 0:
        print(f"⚠ メタデータ問題: {results['metadata']['issues_count']}件")
    if results['chunks'].get('invalid', 0) > 0:
        print(f"⚠ 無効チャンク: {results['chunks']['invalid']}件")

    print("=" * 60)

    # JSONレポート出力
    report_file = PROJECT_ROOT / "FINAL_VALIDATION_REPORT.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 詳細レポート保存: {report_file}")


if __name__ == "__main__":
    main()
