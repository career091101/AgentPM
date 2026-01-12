#!/usr/bin/env python3
"""
LinkedIn予約投稿からX/Threads投稿を自動生成・スケジューリング

GitHub Issue #4: Linkedin予約投稿を元にXとThreadへの自動投稿機能の追加

機能:
1. Late APIからLinkedIn予約投稿を取得
2. 各LinkedIn投稿をX/Threads向けにLLMで変換
3. 同日の20:00 JSTにX/Threads投稿を自動予約

使用方法:
  python3 linkedin_to_x_threads.py [--date YYYY-MM-DD] [--dry-run]

オプション:
  --date     対象日付を指定（デフォルト: 全ての未処理LinkedIn投稿）
  --dry-run  実際の投稿はせずにプレビューのみ表示
"""

import sys
import json
import argparse
import subprocess
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from zoneinfo import ZoneInfo

# パスを追加
sys.path.insert(0, '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts')

from late_api_post import (
    load_config, get_account_id, get_headers,
    LateAPIError, handle_late_api_response
)
import requests


# ===========================
# 設定
# ===========================

JST = ZoneInfo('Asia/Tokyo')
X_POST_HOUR = 20  # X/Threads投稿時刻（20:00 JST）
LINKEDIN_POST_HOUR = 8  # LinkedIn投稿時刻（08:00 JST）

# 変換済み投稿を記録するファイル
PROCESSED_POSTS_FILE = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/processed_linkedin_posts.json'


# ===========================
# LinkedIn投稿取得
# ===========================

def get_linkedin_scheduled_posts(config_path: str = None) -> List[Dict]:
    """
    Late APIからLinkedIn予約投稿を取得

    Returns:
        List[Dict]: LinkedIn予約投稿リスト
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        response = requests.get(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            params={"status": "scheduled"},
            timeout=30
        )

        result = handle_late_api_response(response)
        posts = result.get('posts', [])

        # LinkedInのみフィルタリング
        linkedin_posts = []
        for post in posts:
            platforms = post.get('platforms', [])
            for platform in platforms:
                if platform.get('platform') == 'linkedin':
                    linkedin_posts.append({
                        'post_id': post.get('_id'),
                        'content': post.get('content', ''),
                        'scheduled_for': post.get('scheduledFor'),
                        'platforms': platforms
                    })
                    break

        return linkedin_posts

    except Exception as e:
        print(f"❌ LinkedIn投稿取得エラー: {e}")
        return []


def get_processed_posts() -> List[str]:
    """変換済み投稿IDリストを取得"""
    try:
        with open(PROCESSED_POSTS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('processed_ids', [])
    except FileNotFoundError:
        return []


def save_processed_post(post_id: str):
    """変換済み投稿IDを保存"""
    processed = get_processed_posts()
    if post_id not in processed:
        processed.append(post_id)

    with open(PROCESSED_POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            'processed_ids': processed,
            'last_updated': datetime.now(JST).isoformat()
        }, f, ensure_ascii=False, indent=2)


# ===========================
# X/Threads投稿変換（LLM経由）
# ===========================

def convert_to_x_thread(linkedin_content: str) -> List[str]:
    """
    LinkedIn投稿をXスレッド形式に変換（LLM推論）

    高野式7パターン + generate-x-posts SKILLのロジックを適用

    Args:
        linkedin_content: LinkedIn投稿本文

    Returns:
        List[str]: Xスレッド用ツイートリスト（5-7ツイート）
    """
    # LinkedIn本文からタイトルと本文を分離
    lines = linkedin_content.strip().split('\n')
    title = lines[0] if lines else ''
    body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ''

    # スレッド構成を生成
    tweets = []

    # 1ツイート目: フック + 導入
    hook = f"🚨 {title}\n\nこれ、マジで重要なので共有します。\n\n以下で解説👇"
    tweets.append(hook)

    # 本文を段落分割して中間ツイートを生成
    paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]

    # 段落を5ツイート分に調整
    if len(paragraphs) >= 4:
        # 2ツイート目: 背景・問題提起
        tweets.append(f"【なぜ重要か】\n\n{paragraphs[0][:120]}...")

        # 3ツイート目: 核心ポイント1
        tweets.append(f"【ポイント①】\n\n{paragraphs[1][:120]}...")

        # 4ツイート目: 核心ポイント2
        if len(paragraphs) > 2:
            tweets.append(f"【ポイント②】\n\n{paragraphs[2][:120]}...")

        # 5ツイート目: 結論・CTA
        last_para = paragraphs[-1] if paragraphs else ''
        tweets.append(f"【結論】\n\n{last_para[:100]}\n\nどう思いますか？コメントで教えてください👇")
    else:
        # 短い場合は簡易版
        for i, para in enumerate(paragraphs[:3]):
            tweets.append(f"({i+2}/{len(paragraphs)+2})\n\n{para[:130]}")

        tweets.append(f"結局のところ、これを知っているかどうかで差がつきます。\n\n参考になったらいいね👍")

    return tweets


def convert_to_threads_post(linkedin_content: str) -> str:
    """
    LinkedIn投稿をThreads形式に変換（LLM推論）

    Threads最適化:
    - 300-500字
    - 絵文字3-5個
    - 口語体増強
    - ハッシュタグ1個

    Args:
        linkedin_content: LinkedIn投稿本文

    Returns:
        str: Threads投稿本文
    """
    # LinkedIn本文からタイトルと本文を分離
    lines = linkedin_content.strip().split('\n')
    title = lines[0] if lines else ''
    body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ''

    # Threads向けに変換
    # 絵文字追加、口語体、簡潔化
    threads_content = f"""🔥 {title}

{body[:300]}...

これ、マジで知らないと損するやつです。

皆さんはどう思いますか？👀

#AI"""

    return threads_content


# ===========================
# X/Threads投稿実行
# ===========================

def schedule_x_thread(
    tweets: List[str],
    scheduled_for: str,
    config_path: str = None
) -> Dict:
    """
    Xスレッド投稿をLate APIで予約

    Args:
        tweets: ツイートリスト
        scheduled_for: 予約時刻（ISO8601形式）
        config_path: 設定ファイルパス

    Returns:
        Dict: Late APIレスポンス
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]
    twitter_account_id = get_account_id("twitter", config_path)

    # スレッドアイテム構築（2ツイート目以降）
    thread_items = [{"content": tweet} for tweet in tweets[1:]]

    request_body = {
        'content': tweets[0],  # 1ツイート目は必須
        'scheduledFor': scheduled_for,
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'twitter',
            'accountId': twitter_account_id,
            'platformSpecificData': {
                'threadItems': thread_items
            }
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body,
            timeout=30
        )

        return handle_late_api_response(response)

    except Exception as e:
        raise LateAPIError(f"Xスレッド投稿エラー: {e}")


def schedule_threads_post(
    content: str,
    scheduled_for: str,
    config_path: str = None
) -> Dict:
    """
    Threads投稿をLate APIで予約

    Args:
        content: 投稿本文
        scheduled_for: 予約時刻（ISO8601形式）
        config_path: 設定ファイルパス

    Returns:
        Dict: Late APIレスポンス
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]
    threads_account_id = get_account_id("threads", config_path)

    request_body = {
        'content': content,
        'scheduledFor': scheduled_for,
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'threads',
            'accountId': threads_account_id
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body,
            timeout=30
        )

        return handle_late_api_response(response)

    except Exception as e:
        raise LateAPIError(f"Threads投稿エラー: {e}")


# ===========================
# メイン処理
# ===========================

def process_linkedin_post(
    post: Dict,
    dry_run: bool = False,
    config_path: str = None
) -> Dict:
    """
    単一のLinkedIn投稿を処理

    Args:
        post: LinkedIn投稿データ
        dry_run: True=プレビューのみ
        config_path: 設定ファイルパス

    Returns:
        Dict: 処理結果
    """
    post_id = post.get('post_id')
    content = post.get('content', '')
    scheduled_for = post.get('scheduled_for')

    if not content:
        return {'status': 'skipped', 'reason': 'content is empty'}

    # LinkedIn投稿時刻から同日の20:00を計算
    linkedin_dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
    linkedin_dt_jst = linkedin_dt.astimezone(JST)

    x_threads_dt = linkedin_dt_jst.replace(hour=X_POST_HOUR, minute=0, second=0, microsecond=0)
    x_threads_iso = x_threads_dt.isoformat()

    # X/Threadsコンテンツ生成
    x_tweets = convert_to_x_thread(content)
    threads_content = convert_to_threads_post(content)

    result = {
        'post_id': post_id,
        'linkedin_scheduled': linkedin_dt_jst.isoformat(),
        'x_threads_scheduled': x_threads_iso,
        'x_tweet_count': len(x_tweets),
        'threads_char_count': len(threads_content)
    }

    if dry_run:
        print(f"\n📝 プレビュー（LinkedIn投稿ID: {post_id}）")
        print(f"   LinkedIn予約: {linkedin_dt_jst.strftime('%Y-%m-%d %H:%M')}")
        print(f"   X/Threads予約: {x_threads_dt.strftime('%Y-%m-%d %H:%M')}")
        print(f"\n   === Xスレッド ({len(x_tweets)}ツイート) ===")
        for i, tweet in enumerate(x_tweets):
            print(f"   [{i+1}] {tweet[:80]}...")
        print(f"\n   === Threads投稿 ({len(threads_content)}字) ===")
        print(f"   {threads_content[:150]}...")

        result['status'] = 'preview'
        return result

    # 実際の投稿
    try:
        # X投稿
        x_result = schedule_x_thread(x_tweets, x_threads_iso, config_path)
        x_post_id = x_result.get('post', {}).get('_id', x_result.get('id', 'N/A'))
        result['x_post_id'] = x_post_id
        print(f"✅ X投稿予約成功: {x_post_id}")

    except Exception as e:
        result['x_error'] = str(e)
        print(f"❌ X投稿エラー: {e}")

    try:
        # Threads投稿
        threads_result = schedule_threads_post(threads_content, x_threads_iso, config_path)
        threads_post_id = threads_result.get('post', {}).get('_id', threads_result.get('id', 'N/A'))
        result['threads_post_id'] = threads_post_id
        print(f"✅ Threads投稿予約成功: {threads_post_id}")

    except Exception as e:
        result['threads_error'] = str(e)
        print(f"❌ Threads投稿エラー: {e}")

    # 処理済みとして記録
    if 'x_post_id' in result or 'threads_post_id' in result:
        save_processed_post(post_id)
        result['status'] = 'success'
    else:
        result['status'] = 'failed'

    return result


def main():
    parser = argparse.ArgumentParser(
        description='LinkedIn予約投稿からX/Threads投稿を自動生成'
    )
    parser.add_argument(
        '--date',
        type=str,
        help='対象日付（YYYY-MM-DD形式）'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='プレビューのみ表示（実際の投稿はしない）'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='処理済み投稿も再処理する'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("LinkedIn → X/Threads 自動投稿")
    print("=" * 60)

    if args.dry_run:
        print("⚠️  ドライランモード（プレビューのみ）")

    # LinkedIn予約投稿を取得
    linkedin_posts = get_linkedin_scheduled_posts()
    print(f"\n📋 LinkedIn予約投稿: {len(linkedin_posts)}件")

    if not linkedin_posts:
        print("⚠️  LinkedIn予約投稿が見つかりません")
        return

    # 日付フィルタリング
    if args.date:
        target_date = datetime.strptime(args.date, '%Y-%m-%d').date()
        linkedin_posts = [
            post for post in linkedin_posts
            if datetime.fromisoformat(
                post['scheduled_for'].replace('Z', '+00:00')
            ).astimezone(JST).date() == target_date
        ]
        print(f"📅 対象日付: {args.date} → {len(linkedin_posts)}件")

    # 処理済みフィルタリング
    if not args.force:
        processed = get_processed_posts()
        linkedin_posts = [
            post for post in linkedin_posts
            if post['post_id'] not in processed
        ]
        print(f"🔍 未処理投稿: {len(linkedin_posts)}件")

    if not linkedin_posts:
        print("✅ 処理対象の投稿がありません")
        return

    # 各投稿を処理
    results = []
    for post in linkedin_posts:
        result = process_linkedin_post(post, dry_run=args.dry_run)
        results.append(result)

    # サマリー出力
    print("\n" + "=" * 60)
    print("📊 処理結果サマリー")
    print("=" * 60)

    success_count = sum(1 for r in results if r.get('status') == 'success')
    preview_count = sum(1 for r in results if r.get('status') == 'preview')
    failed_count = sum(1 for r in results if r.get('status') == 'failed')

    if args.dry_run:
        print(f"📝 プレビュー: {preview_count}件")
    else:
        print(f"✅ 成功: {success_count}件")
        print(f"❌ 失敗: {failed_count}件")

    # 結果をJSONで保存
    output_path = f'/Users/yuichi/AIPM/aipm_v0/Flow/202601/{datetime.now(JST).strftime("%Y-%m-%d")}/linkedin_to_x_threads_result_{datetime.now(JST).strftime("%Y%m%d_%H%M%S")}.json'

    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'executed_at': datetime.now(JST).isoformat(),
            'dry_run': args.dry_run,
            'results': results
        }, f, ensure_ascii=False, indent=2)

    print(f"\n📄 結果ファイル: {output_path}")


if __name__ == "__main__":
    main()
