#!/usr/bin/env python3
"""
投稿生成後フック

投稿生成直後に自動レビューをトリガー
"""

import os
import sys
import subprocess
from pathlib import Path


def trigger_immediate_review(post_file_path: str):
    """投稿生成直後のレビューをトリガー"""

    # プロジェクトルート
    base_dir = Path(__file__).parent.parent.parent.parent.parent.parent

    # スケジューラースクリプト
    scheduler_script = base_dir / ".claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py"

    if not scheduler_script.exists():
        print(f"⚠️  スケジューラースクリプトが見つかりません: {scheduler_script}")
        return

    print(f"\n📋 投稿生成直後のレビューを実行します...")
    print(f"   対象ファイル: {post_file_path}")

    # スケジューラー実行
    try:
        result = subprocess.run(
            ["python3", str(scheduler_script), "immediate", "--post-file", post_file_path],
            cwd=str(base_dir),
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.returncode != 0:
            print(f"⚠️  レビュー実行エラー:")
            print(result.stderr)

    except Exception as e:
        print(f"❌ レビュー実行エラー: {str(e)}")


def main():
    """メイン実行"""

    if len(sys.argv) < 2:
        print("使用方法: python3 post_generation_hook.py <post_file_path>")
        sys.exit(1)

    post_file_path = sys.argv[1]

    if not os.path.exists(post_file_path):
        print(f"❌ ファイルが見つかりません: {post_file_path}")
        sys.exit(1)

    trigger_immediate_review(post_file_path)


if __name__ == '__main__':
    main()
