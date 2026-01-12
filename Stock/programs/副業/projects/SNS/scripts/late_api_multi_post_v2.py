#!/usr/bin/env python3
"""
Late API マルチプラットフォーム投稿スクリプト v2（Option C対応版）

機能:
- LinkedIn 1案（8:00 JST）
- X 3投稿: 派生(7:30) + スレッド1(12:00) + スレッド2(20:00)
- Threads 2投稿: 派生(7:30) + 新規(20:00)

合計6投稿を個別にPOSTリクエスト

Usage:
    python3 scripts/late_api_multi_post_v2.py
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
import requests
from datetime import timezone
from typing import Optional, List, Dict, Any

# プロジェクトルート設定
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "scripts"))

# タイムゾーン設定
JST = timezone(timedelta(hours=9))

# ========================================
# 投稿スケジュール設定（Option C）
# ========================================
POSTING_SCHEDULE = {
    'linkedin': [
        {'time': '08:00', 'type': 'main', 'topic': 'top1'}
    ],
    'twitter': [
        {'time': '07:30', 'type': 'derived', 'topic': 'top1'},
        {'time': '12:00', 'type': 'thread', 'topic': 'top2'},
        {'time': '20:00', 'type': 'thread', 'topic': 'top3'}
    ],
    'threads': [
        {'time': '07:30', 'type': 'derived', 'topic': 'top1'},
        {'time': '20:00', 'type': 'new', 'topic': 'top2'}
    ]
}


def load_env_vars() -> dict:
    """
    .envファイルから環境変数を読み込む
    """
    env_file = project_root / ".env"
    env_vars = {}

    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    # インラインコメント除去
                    if "#" in value:
                        in_quote = False
                        quote_char = None
                        clean_value = []
                        for ch in value:
                            if ch in ['"', "'"]:
                                if not in_quote:
                                    in_quote = True
                                    quote_char = ch
                                elif ch == quote_char:
                                    in_quote = False
                                    quote_char = None
                            elif ch == "#" and not in_quote:
                                break
                            clean_value.append(ch)
                        value = "".join(clean_value)
                    value = value.strip().strip('"').strip("'")
                    env_vars[key.strip()] = value
    return env_vars


def remove_markdown(text: str) -> str:
    """Markdown装飾を除去"""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
    return text


# ========================================
# コンテンツ抽出関数
# ========================================

def extract_linkedin_content(markdown: str, variant_number: int = 2) -> Optional[dict]:
    """
    LinkedIn投稿（案N）のコンテンツを抽出

    Args:
        markdown: Phase 3生成されたMarkdownファイルの内容
        variant_number: バリアント番号（デフォルト: 案2が最推奨）

    Returns:
        dict: {"title": str, "body": str, "full_content": str}
    """
    # 新フォーマット: ## LinkedIn投稿案2（パターンX: 名称）
    pattern = rf'## LinkedIn投稿案{variant_number}（パターン\d+:.*?\）\n\n\*\*トピック\*\*:.*?\n\n---\n\n(.*?)(?=\n---\n|\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        # 旧フォーマット対応（フォールバック）
        pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\Z)'
        match = re.search(pattern, markdown, re.DOTALL)

        if not match:
            return None

        title = remove_markdown(match.group(1).strip())
        body = remove_markdown(match.group(2).strip())

        return {
            "title": title,
            "body": body,
            "full_content": f"{title}\n\n{body}"
        }

    # 新フォーマットの場合は全体をbodyとして扱う
    body = remove_markdown(match.group(1).strip())

    # タイトルは本文の最初の行を使用
    lines = body.split('\n', 1)
    title = lines[0] if lines else ""

    return {
        "title": title,
        "body": body,
        "full_content": body
    }


def extract_x_derived_content(markdown: str) -> Optional[dict]:
    """
    X派生投稿のコンテンツを抽出（フックのみ変更版）

    セクション: ## X派生投稿（Top 1トピック、フック変更）

    メタ情報（**元ネタ**:, ---, **文字数**:）を除外して本文のみを抽出
    """
    # **元ネタ**: ... と --- をスキップし、本文のみ抽出
    pattern = r'## X派生投稿（Top 1トピック、フック変更）.*?\n\n\*\*元ネタ\*\*:.*?\n\n---\n\n(.*?)(?=\n---\n|\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        # フォールバック: LinkedIn案2からフックを変更
        linkedin = extract_linkedin_content(markdown, 2)
        if linkedin:
            # 最初の3行をX用フックに変更（簡易版）
            lines = linkedin["full_content"].split("\n")
            if len(lines) > 3:
                # 最初の行をX向けに短縮
                hook = lines[0][:100] + "..." if len(lines[0]) > 100 else lines[0]
                rest = "\n".join(lines[1:])
                # 280文字に収める
                content = f"{hook}\n\n{rest}"[:280]
                return {"content": content, "type": "derived"}
        return None

    content = remove_markdown(match.group(1).strip())
    return {"content": content[:280], "type": "derived"}


def extract_x_thread_content(markdown: str, thread_number: int) -> Optional[List[str]]:
    """
    Xスレッド投稿のコンテンツを抽出（5-7ツイート深掘り型）

    Args:
        markdown: Markdownファイルの内容
        thread_number: スレッド番号（1=Top2トピック, 2=Top3トピック）

    Returns:
        List[str]: 各ツイートのコンテンツ（5-7件）
    """
    if thread_number == 1:
        section_name = "Xスレッド1（Top 2トピック、深掘り型）"
    else:
        section_name = "Xスレッド2（Top 3トピック、深掘り型）"

    pattern = rf'## {section_name}.*?\n\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    content = match.group(1).strip()

    # ツイートを分割（**N/M**, (N/M), ### ツイートN 形式）
    tweets = []

    # パターン1: **N/M** 形式（高野式生成フォーマット）
    tweet_sections = re.split(r'\n\*\*\d+/\d+\*\*\n', content)
    if len(tweet_sections) > 1:
        for section in tweet_sections[1:]:
            # ---で区切られたセクションを分離
            parts = section.split('\n---\n')
            if parts:
                tweet_text = remove_markdown(parts[0].strip())
                if tweet_text:
                    tweets.append(tweet_text[:280])

    # パターン2: ### ツイートN 形式
    if not tweets:
        tweet_sections = re.split(r'### ツイート\d+', content)
        if len(tweet_sections) > 1:
            for section in tweet_sections[1:]:
                tweet_text = remove_markdown(section.strip())
                if tweet_text:
                    tweets.append(tweet_text[:280])

    # パターン3: (N/M) 形式
    if not tweets:
        tweet_parts = re.split(r'\(\d+/\d+\)', content)
        for i, part in enumerate(tweet_parts):
            if part.strip():
                tweet_text = remove_markdown(part.strip())
                if tweet_text:
                    prefix = f"({i}/{len(tweet_parts)-1}) " if i > 0 else ""
                    tweets.append(f"{prefix}{tweet_text}"[:280])

    # フォールバック: コンテンツを7ツイートに自動分割
    if not tweets and content:
        content_clean = remove_markdown(content)
        # 段落で分割
        paragraphs = content_clean.split("\n\n")
        for p in paragraphs:
            if p.strip():
                tweets.append(p.strip()[:280])
        # 最大7ツイートに制限
        tweets = tweets[:7]

    return tweets if tweets else None


def extract_threads_derived_content(markdown: str) -> Optional[dict]:
    """
    Threads派生投稿のコンテンツを抽出（フックのみ変更版）

    セクション: ## Threads派生投稿（Top 1トピック、フック変更）

    メタ情報（**元ネタ**:, ---, **文字数**:）を除外して本文のみを抽出
    """
    # **元ネタ**: ... と --- をスキップし、本文のみ抽出
    pattern = r'## Threads派生投稿（Top 1トピック、フック変更）.*?\n\n\*\*元ネタ\*\*:.*?\n\n---\n\n(.*?)(?=\n---\n|\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        # フォールバック: LinkedIn案2から派生
        linkedin = extract_linkedin_content(markdown, 2)
        if linkedin:
            content = linkedin["full_content"][:500]
            return {"content": content, "type": "derived"}
        return None

    content = remove_markdown(match.group(1).strip())
    return {"content": content[:500], "type": "derived"}


def extract_threads_new_content(markdown: str) -> Optional[dict]:
    """
    Threads新規投稿のコンテンツを抽出（Top 2トピック、LinkedIn似表現）

    セクション: ## Threads新規投稿（Top 2トピック）

    メタ情報（**トピック**:, ---, **文字数**:）を除外して本文のみを抽出
    """
    # **トピック**: ... と --- をスキップし、本文のみ抽出
    pattern = r'## Threads新規投稿（Top 2トピック）.*?\n\n\*\*トピック\*\*:.*?\n\n---\n\n(.*?)(?=\n---\n|\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    content = remove_markdown(match.group(1).strip())
    return {"content": content[:500], "type": "new"}


# ========================================
# Late API投稿関数
# ========================================

def post_to_late_api(
    content: str,
    platform: str,
    account_id: str,
    scheduled_datetime: datetime,
    api_key: str,
    thread_items: Optional[List[str]] = None
) -> dict:
    """
    Late APIに1件の投稿を送信

    Args:
        content: 投稿本文（スレッド時は最初の投稿）
        platform: プラットフォーム（linkedin, twitter, threads）
        account_id: プラットフォーム固有のアカウントID
        scheduled_datetime: 予約日時（JST）
        api_key: Late API キー
        thread_items: Xスレッド投稿時の各ツイートリスト

    Returns:
        dict: Late APIレスポンス
    """
    base_url = "https://getlate.dev/api/v1"

    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=JST)

    scheduled_datetime_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(scheduled_datetime_str) >= 5:
        scheduled_datetime_str = scheduled_datetime_str[:-2] + ':' + scheduled_datetime_str[-2:]

    # プラットフォーム設定
    platform_config = {
        "platform": platform,
        "accountId": account_id
    }

    # Xスレッド投稿の場合
    if thread_items and platform == "twitter":
        platform_config["platformSpecificData"] = {
            "threadItems": [{"content": tweet} for tweet in thread_items]
        }

    payload = {
        "content": content,
        "platforms": [platform_config],
        "scheduledFor": scheduled_datetime_str,
        "timezone": "Asia/Tokyo"
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        f"{base_url}/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code not in [200, 201]:
        raise Exception(f"Late API Error: {response.status_code} - {response.text}")

    return response.json()


def get_existing_scheduled_posts(api_key: str) -> dict:
    """
    既存の予約投稿を取得し、時間帯別に分類

    Returns:
        dict: {
            'posts': [...],
            'reserved_by_hour': {7: set(), 8: set(), 12: set(), 20: set()}
        }
    """
    base_url = "https://getlate.dev/api/v1"

    try:
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        response = requests.get(f"{base_url}/posts", headers=headers, params={"status": "scheduled"}, timeout=30)
        response.raise_for_status()
        scheduled_posts = response.json()
    except Exception as e:
        print(f"⚠️  既存予約の取得に失敗: {e}")
        return {'posts': [], 'reserved_by_hour': {7: set(), 8: set(), 12: set(), 20: set()}}

    reserved_by_hour = {7: set(), 8: set(), 12: set(), 20: set()}

    for post in scheduled_posts.get("posts", []):
        scheduled_for = post.get("scheduledFor")
        if scheduled_for:
            try:
                dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
                dt_jst = dt.astimezone(JST)
                hour = dt_jst.hour
                if hour in reserved_by_hour:
                    reserved_by_hour[hour].add(dt_jst.date())
            except Exception:
                pass

    return {
        'posts': scheduled_posts.get('posts', []),
        'reserved_by_hour': reserved_by_hour
    }


def find_available_date(reserved_by_hour: dict, target_hours: List[int]) -> datetime:
    """
    指定した全時間帯で空いている最も近い日付を検索

    Args:
        reserved_by_hour: 時間帯別の予約済み日付
        target_hours: チェックする時間帯リスト [7, 8, 12, 20]

    Returns:
        datetime.date: 利用可能な日付
    """
    current_date = datetime.now(JST).date() + timedelta(days=1)
    max_search_days = 30

    for _ in range(max_search_days):
        is_available = True
        for hour in target_hours:
            if current_date in reserved_by_hour.get(hour, set()):
                is_available = False
                break

        if is_available:
            return current_date

        current_date += timedelta(days=1)

    # 30日後でも見つからない場合は翌日を返す
    return datetime.now(JST).date() + timedelta(days=1)


# ========================================
# メイン処理
# ========================================

def main():
    """メイン処理"""
    print("=" * 60)
    print("Late API マルチプラットフォーム投稿 v2（Option C対応版）")
    print("=" * 60)
    print()
    print("投稿計画:")
    print("  - LinkedIn: 1案（8:00）")
    print("  - X: 3投稿（派生7:30 + スレッド12:00 + スレッド20:00）")
    print("  - Threads: 2投稿（派生7:30 + 新規20:00）")
    print("  合計: 6投稿")
    print()

    try:
        # 1. 環境変数読み込み
        env_vars = load_env_vars()
        api_key = env_vars.get("LATE_API_KEY")
        linkedin_account_id = env_vars.get("LATE_LINKEDIN_ACCOUNT_ID")
        twitter_account_id = env_vars.get("LATE_TWITTER_ACCOUNT_ID")
        threads_account_id = env_vars.get("LATE_THREADS_ACCOUNT_ID")

        if not api_key:
            raise ValueError("LATE_API_KEY not found in .env file")

        # アカウントID確認
        available_platforms = []
        if linkedin_account_id:
            available_platforms.append("linkedin")
        if twitter_account_id:
            available_platforms.append("twitter")
        if threads_account_id:
            available_platforms.append("threads")

        print(f"📊 利用可能プラットフォーム: {', '.join(available_platforms)}")

        if not available_platforms:
            raise ValueError("No platform account IDs found in .env file")

        # 2. Markdownファイル読み込み
        data_dir = project_root / "data"
        markdown_files = list(data_dir.glob("posts_generated_takano_*.md"))

        if not markdown_files:
            print("❌ posts_generated_takano_*.md ファイルが見つかりません")
            sys.exit(1)

        latest_file = max(markdown_files, key=lambda f: f.stat().st_mtime)
        print(f"📄 入力ファイル: {latest_file.name}")
        markdown_content = latest_file.read_text(encoding="utf-8")

        # 3. コンテンツ抽出
        print()
        print("📝 コンテンツ抽出中...")

        contents = {}

        # LinkedIn（案2を使用）
        linkedin_content = extract_linkedin_content(markdown_content, 2)
        if linkedin_content:
            contents['linkedin'] = linkedin_content
            print(f"  ✅ LinkedIn: {len(linkedin_content['full_content'])}文字")
        else:
            print("  ⚠️  LinkedIn: 抽出失敗（案2が見つかりません）")

        # X派生
        x_derived = extract_x_derived_content(markdown_content)
        if x_derived:
            contents['x_derived'] = x_derived
            print(f"  ✅ X派生: {len(x_derived['content'])}文字")
        else:
            print("  ⚠️  X派生: 抽出失敗（LinkedIn案2からフォールバック生成）")

        # Xスレッド1（Top 2トピック）
        x_thread1 = extract_x_thread_content(markdown_content, 1)
        if x_thread1:
            contents['x_thread1'] = x_thread1
            print(f"  ✅ Xスレッド1: {len(x_thread1)}ツイート")
        else:
            print("  ⚠️  Xスレッド1: 抽出失敗")

        # Xスレッド2（Top 3トピック）
        x_thread2 = extract_x_thread_content(markdown_content, 2)
        if x_thread2:
            contents['x_thread2'] = x_thread2
            print(f"  ✅ Xスレッド2: {len(x_thread2)}ツイート")
        else:
            print("  ⚠️  Xスレッド2: 抽出失敗")

        # Threads派生
        threads_derived = extract_threads_derived_content(markdown_content)
        if threads_derived:
            contents['threads_derived'] = threads_derived
            print(f"  ✅ Threads派生: {len(threads_derived['content'])}文字")
        else:
            print("  ⚠️  Threads派生: 抽出失敗")

        # Threads新規
        threads_new = extract_threads_new_content(markdown_content)
        if threads_new:
            contents['threads_new'] = threads_new
            print(f"  ✅ Threads新規: {len(threads_new['content'])}文字")
        else:
            print("  ⚠️  Threads新規: 抽出失敗")

        # 4. 既存予約取得と日付決定
        print()
        print("🔍 既存予約投稿をチェック中...")
        existing = get_existing_scheduled_posts(api_key)
        print(f"   既存予約投稿: {len(existing['posts'])}件")

        # 全時間帯で空いている日付を検索
        target_date = find_available_date(existing['reserved_by_hour'], [7, 8, 12, 20])
        print(f"✅ 投稿日: {target_date}")

        # 5. 投稿計画を作成
        posting_plan = []

        # LinkedIn（8:00）
        if 'linkedin' in contents and linkedin_account_id:
            posting_plan.append({
                'platform': 'linkedin',
                'type': 'main',
                'time': '08:00',
                'content': contents['linkedin']['full_content'],
                'account_id': linkedin_account_id,
                'title': contents['linkedin']['title'][:50],
                'thread_items': None
            })

        # X派生（7:30）
        if 'x_derived' in contents and twitter_account_id:
            posting_plan.append({
                'platform': 'twitter',
                'type': 'derived',
                'time': '07:30',
                'content': contents['x_derived']['content'],
                'account_id': twitter_account_id,
                'title': 'X派生（Top1）',
                'thread_items': None
            })

        # Xスレッド1（12:00）
        if 'x_thread1' in contents and twitter_account_id:
            posting_plan.append({
                'platform': 'twitter',
                'type': 'thread',
                'time': '12:00',
                'content': contents['x_thread1'][0] if contents['x_thread1'] else '',
                'account_id': twitter_account_id,
                'title': f'Xスレッド1（Top2、{len(contents["x_thread1"])}ツイート）',
                'thread_items': contents['x_thread1']
            })

        # Xスレッド2（20:00）
        if 'x_thread2' in contents and twitter_account_id:
            posting_plan.append({
                'platform': 'twitter',
                'type': 'thread',
                'time': '20:00',
                'content': contents['x_thread2'][0] if contents['x_thread2'] else '',
                'account_id': twitter_account_id,
                'title': f'Xスレッド2（Top3、{len(contents["x_thread2"])}ツイート）',
                'thread_items': contents['x_thread2']
            })

        # Threads派生（7:30）
        if 'threads_derived' in contents and threads_account_id:
            posting_plan.append({
                'platform': 'threads',
                'type': 'derived',
                'time': '07:30',
                'content': contents['threads_derived']['content'],
                'account_id': threads_account_id,
                'title': 'Threads派生（Top1）',
                'thread_items': None
            })

        # Threads新規（20:00）
        if 'threads_new' in contents and threads_account_id:
            posting_plan.append({
                'platform': 'threads',
                'type': 'new',
                'time': '20:00',
                'content': contents['threads_new']['content'],
                'account_id': threads_account_id,
                'title': 'Threads新規（Top2）',
                'thread_items': None
            })

        # 6. 投稿計画を表示
        print()
        print("=" * 60)
        print("投稿計画（競合回避済み）")
        print("=" * 60)

        for plan in posting_plan:
            platform_emoji = {'linkedin': '💼', 'twitter': '🐦', 'threads': '🧵'}.get(plan['platform'], '📱')
            print(f"{platform_emoji} {target_date} {plan['time']} JST - {plan['platform'].upper()}")
            print(f"   タイプ: {plan['type']}")
            print(f"   内容: {plan['title']}...")
            if plan['thread_items']:
                print(f"   スレッド: {len(plan['thread_items'])}ツイート")
            print()

        print(f"合計: {len(posting_plan)}投稿")
        print()

        # 7. ユーザー確認（環境変数で自動承認可能）
        print("=" * 60)

        auto_confirm = env_vars.get("AUTO_CONFIRM_POSTING", "").lower() in ["true", "1", "yes"]

        if auto_confirm:
            print("✅ AUTO_CONFIRM_POSTING=true により自動実行します")
        else:
            confirm = input("上記の計画で投稿を実行しますか？ (y/n): ")
            if confirm.lower() != 'y':
                print("❌ 実行をキャンセルしました")
                sys.exit(0)

        # 8. 投稿実行
        print()
        print("=" * 60)
        print("Late API投稿実行中...")
        print("=" * 60)
        print()

        results = []

        for plan in posting_plan:
            # 時刻をパース
            hour, minute = map(int, plan['time'].split(':'))
            scheduled_datetime = datetime.combine(
                target_date,
                datetime.min.time()
            ).replace(hour=hour, minute=minute, tzinfo=JST)

            platform_emoji = {'linkedin': '💼', 'twitter': '🐦', 'threads': '🧵'}.get(plan['platform'], '📱')
            print(f"{platform_emoji} {plan['platform'].upper()} ({plan['time']}) を投稿中...")
            print(f"   タイプ: {plan['type']}")

            try:
                result = post_to_late_api(
                    content=plan['content'],
                    platform=plan['platform'],
                    account_id=plan['account_id'],
                    scheduled_datetime=scheduled_datetime,
                    api_key=api_key,
                    thread_items=plan['thread_items']
                )

                post_id = result.get("post", {}).get("_id") or result.get("id")
                print(f"   ✅ 成功! Post ID: {post_id}")
                print()

                results.append({
                    "platform": plan['platform'],
                    "type": plan['type'],
                    "status": "success",
                    "post_id": post_id,
                    "scheduled_for": scheduled_datetime.isoformat(),
                    "title": plan['title']
                })

            except Exception as e:
                print(f"   ❌ 失敗: {e}")
                print()

                results.append({
                    "platform": plan['platform'],
                    "type": plan['type'],
                    "status": "error",
                    "error_message": str(e),
                    "scheduled_for": scheduled_datetime.isoformat()
                })

        # 9. 結果保存
        result_file = data_dir / f"late_api_multiplatform_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(result_file, "w", encoding="utf-8") as f:
            json.dump({
                "executed_at": datetime.now(JST).isoformat(),
                "target_date": str(target_date),
                "posting_schedule": POSTING_SCHEDULE,
                "results": results
            }, f, indent=2, ensure_ascii=False)

        # 10. サマリー表示
        print("=" * 60)
        print("実行完了")
        print("=" * 60)
        print(f"💾 結果保存: {result_file.name}")
        print()

        success_count = sum(1 for r in results if r["status"] == "success")
        failed_count = len(results) - success_count

        print(f"✅ 成功: {success_count}/{len(posting_plan)}投稿")
        print(f"❌ 失敗: {failed_count}/{len(posting_plan)}投稿")

        # プラットフォーム別サマリー
        print()
        print("プラットフォーム別:")
        for platform in ['linkedin', 'twitter', 'threads']:
            platform_results = [r for r in results if r['platform'] == platform]
            if platform_results:
                success = sum(1 for r in platform_results if r['status'] == 'success')
                emoji = {'linkedin': '💼', 'twitter': '🐦', 'threads': '🧵'}.get(platform, '📱')
                print(f"  {emoji} {platform.upper()}: {success}/{len(platform_results)}")

        if success_count == len(posting_plan):
            print()
            print("🎉 全投稿が成功しました！")
            print("Late APIダッシュボードで確認してください:")
            print("https://getlate.dev/dashboard")
        elif success_count > 0:
            print()
            print("⚠️  一部の投稿が失敗しました")
            for r in results:
                if r["status"] == "error":
                    print(f"   - {r['platform']} ({r['type']}): {r.get('error_message', 'Unknown error')}")
        else:
            print()
            print("❌ 全ての投稿が失敗しました")
            print("エラーログを確認してください")

        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
