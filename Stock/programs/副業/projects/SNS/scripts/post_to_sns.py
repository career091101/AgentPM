#!/usr/bin/env python3
"""
post_to_sns.py - SNS手動投稿スクリプト

approved_post_*.json を読み取り、指定されたプラットフォームに投稿を実行します。
Phase A（手動投稿）とPhase B（自動スケジューリング）の両方で使用されます。

使用方法:
    # 最新のapproved_post_*.jsonを使用
    python post_to_sns.py

    # 特定のファイルを指定
    python post_to_sns.py --file approved_post_20260104_120000.json

    # 特定のプラットフォームのみ投稿
    python post_to_sns.py --platforms LinkedIn X

    # スケジューラーから呼び出し（内部使用）
    python post_to_sns.py --scheduled-post-id <post_id>
"""

import os
import sys
import json
import glob
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import logging

# .envファイル読み込み
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ロギング設定
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / 'post_to_sns.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# データディレクトリ
SNS_DATA_DIR = Path(__file__).parent.parent / "data"

# 環境変数（今後実装）
LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")


def load_approved_post(file_path=None):
    """
    approved_post_*.json を読み込み

    Args:
        file_path (str, optional): 指定ファイルパス。Noneの場合は最新ファイルを自動取得

    Returns:
        dict: 承認済み投稿データ
    """
    if file_path:
        approved_file = SNS_DATA_DIR / file_path
        if not approved_file.exists():
            raise FileNotFoundError(f"File not found: {approved_file}")
    else:
        # 最新ファイルを自動検索
        files = list(SNS_DATA_DIR.glob("approved_post_*.json"))
        if not files:
            raise FileNotFoundError("No approved_post_*.json files found")

        approved_file = max(files, key=lambda f: f.stat().st_ctime)

    logger.info(f"Loading approved post: {approved_file}")

    with open(approved_file, "r", encoding="utf-8") as f:
        return json.load(f)


def post_to_linkedin(content):
    """
    LinkedIn に投稿

    Args:
        content (str): 投稿内容

    Returns:
        dict: {success: bool, platform: str, post_id: str, message: str}
    """
    # TODO: LinkedIn API統合（Phase B実装時）
    logger.info(f"[STUB] LinkedIn投稿: {len(content)}文字")

    # スタブ実装（Phase A）
    return {
        "success": True,
        "platform": "LinkedIn",
        "post_id": "stub_linkedin_" + datetime.now().strftime('%Y%m%d%H%M%S'),
        "message": "LinkedIn投稿スタブ実行（Phase A）",
        "content_preview": content[:50] + "..."
    }


def post_to_x(content):
    """
    X (Twitter) に投稿

    Args:
        content (str): 投稿内容

    Returns:
        dict: {success: bool, platform: str, post_id: str, message: str}
    """
    # TODO: X API統合（Phase B実装時）
    logger.info(f"[STUB] X投稿: {len(content)}文字")

    # スタブ実装（Phase A）
    return {
        "success": True,
        "platform": "X",
        "post_id": "stub_x_" + datetime.now().strftime('%Y%m%d%H%M%S'),
        "message": "X投稿スタブ実行（Phase A）",
        "content_preview": content[:50] + "..."
    }


def post_to_facebook(content):
    """
    Facebook に投稿

    Args:
        content (str): 投稿内容

    Returns:
        dict: {success: bool, platform: str, post_id: str, message: str}
    """
    # TODO: Facebook API統合（Phase B実装時）
    logger.info(f"[STUB] Facebook投稿: {len(content)}文字")

    # スタブ実装（Phase A）
    return {
        "success": True,
        "platform": "Facebook",
        "post_id": "stub_facebook_" + datetime.now().strftime('%Y%m%d%H%M%S'),
        "message": "Facebook投稿スタブ実行（Phase A）",
        "content_preview": content[:50] + "..."
    }


def post_to_threads(content):
    """
    Threads に投稿

    Args:
        content (str): 投稿内容

    Returns:
        dict: {success: bool, platform: str, post_id: str, message: str}
    """
    # TODO: Threads API統合（Phase B実装時）
    logger.info(f"[STUB] Threads投稿: {len(content)}文字")

    # スタブ実装（Phase A）
    return {
        "success": True,
        "platform": "Threads",
        "post_id": "stub_threads_" + datetime.now().strftime('%Y%m%d%H%M%S'),
        "message": "Threads投稿スタブ実行（Phase A）",
        "content_preview": content[:50] + "..."
    }


def main():
    parser = argparse.ArgumentParser(description="SNS手動投稿スクリプト")
    parser.add_argument("--file", help="approved_post_*.json ファイルパス")
    parser.add_argument("--platforms", nargs="+", default=["LinkedIn", "X", "Facebook", "Threads"],
                        help="投稿先プラットフォーム（デフォルト: 全プラットフォーム）")
    parser.add_argument("--scheduled-post-id", help="スケジューラーから呼び出し時のpost_id（内部使用）")

    args = parser.parse_args()

    print("=" * 60)
    print("SNS手動投稿スクリプト")
    print("=" * 60)

    # 承認済み投稿データを読み込み
    try:
        approved_post = load_approved_post(args.file)
        print(f"✅ 承認済み投稿を読み込みました")
        print(f"   承認日時: {approved_post.get('approved_at')}")
        print(f"   承認案: {approved_post.get('approved_variant')}")
        print(f"   承認者: {approved_post.get('user_name')}")
    except FileNotFoundError as e:
        print(f"❌ エラー: {e}")
        sys.exit(1)

    # 投稿内容取得（修正版が存在する場合は修正版を使用）
    content = approved_post.get("refined_content") or approved_post.get("content")

    if not content:
        print("❌ エラー: 投稿内容が見つかりません")
        sys.exit(1)

    print(f"\n📝 投稿内容（{len(content)}文字）:")
    print("─" * 60)
    print(content[:200] + ("..." if len(content) > 200 else ""))
    print("─" * 60)

    # 各プラットフォームに投稿
    results = []

    print(f"\n🚀 投稿実行中...")

    for platform in args.platforms:
        if platform == "LinkedIn":
            result = post_to_linkedin(content)
        elif platform == "X":
            result = post_to_x(content)
        elif platform == "Facebook":
            result = post_to_facebook(content)
        elif platform == "Threads":
            result = post_to_threads(content)
        else:
            print(f"⚠️  未対応のプラットフォーム: {platform}")
            continue

        results.append(result)

        if result["success"]:
            print(f"   ✅ {platform}: {result['message']}")
        else:
            print(f"   ❌ {platform}: {result.get('message', 'Unknown error')}")

    # 投稿結果を保存
    result_file = SNS_DATA_DIR / f"post_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    result_data = {
        "executed_at": datetime.now().isoformat(),
        "approved_variant": approved_post.get("approved_variant"),
        "content": content,
        "platforms": args.platforms,
        "results": results,
        "scheduled_post_id": args.scheduled_post_id
    }

    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 投稿完了")
    print(f"   結果ファイル: {result_file.name}")
    print("=" * 60)

    # 成功数をカウント
    success_count = sum(1 for r in results if r["success"])

    if success_count == len(results):
        logger.info(f"All platforms posted successfully: {args.platforms}")
        sys.exit(0)
    elif success_count > 0:
        logger.warning(f"Partial success: {success_count}/{len(results)} platforms posted")
        sys.exit(1)
    else:
        logger.error(f"All platforms failed to post")
        sys.exit(2)


if __name__ == "__main__":
    main()
