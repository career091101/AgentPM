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
        {'time': '08:00', 'type': 'main', 'topic': 'top1', 'date_offset': 'auto'},
        {'time': '08:00', 'type': 'main', 'topic': 'top2', 'date_offset': 'auto'},
        {'time': '08:00', 'type': 'main', 'topic': 'top3', 'date_offset': 'auto'}
    ],
    'twitter': [
        {'time': '07:30', 'type': 'thread', 'topic': 'top1'},
        {'time': '12:00', 'type': 'thread', 'topic': 'top2'},
        {'time': '20:00', 'type': 'thread', 'topic': 'top3'}
    ],
    'threads': [
        {'time': '07:30', 'type': 'new', 'topic': 'top1'},
        {'time': '12:00', 'type': 'new', 'topic': 'top2'},
        {'time': '20:00', 'type': 'new', 'topic': 'top3'}
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

    **v2対応**: variant_numberを1-3で指定可能
    v2.1: 「最初のコメント（firstComment）」セクションも抽出

    Args:
        markdown: Phase 3生成されたMarkdownファイルの内容
        variant_number: バリアント番号（1-3、デフォルト: 案2が最推奨）

    Returns:
        dict: {"title": str, "body": str, "full_content": str, "first_comment": str}
    """
    # 新フォーマット: ## LinkedIn案1（パターンX「名称」、...）
    pattern = rf'## LinkedIn案{variant_number}（.*?\）\n\n(.*?)(?=\n## |\Z)'
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
            "full_content": f"{title}\n\n{body}",
            "first_comment": None  # 旧フォーマットではfirstComment未対応
        }

    # 新フォーマットの場合
    full_section = match.group(1).strip()

    # v2形式では「#### 最初のコメント」セクションがないため、本文全体を抽出
    body = remove_markdown(full_section)

    # タイトルは本文の最初の行を使用
    lines = body.split('\n', 1)
    title = lines[0] if lines else ""

    first_comment = None  # v2形式ではfirstCommentなし

    return {
        "title": title,
        "body": body,
        "full_content": body,
        "first_comment": first_comment
    }


def extract_x_thread_content(markdown: str, thread_number: int) -> Optional[List[str]]:
    """
    Xスレッド投稿のコンテンツを抽出（5-7ツイート深掘り型）

    **v2対応**: thread_number を 1-3 に拡張（従来は1-2のみ）

    Args:
        markdown: Markdownファイルの内容
        thread_number: スレッド番号（1=Top1, 2=Top2, 3=Top3）

    Returns:
        List[str]: 各ツイートのコンテンツ（5-7件）
    """
    # v2フォーマット: ## Xスレッド1（Top 1トピック: XXX、深掘り型）
    pattern = rf'## Xスレッド{thread_number}（.*?\）\n\n(.*?)(?=\n## |\Z)'
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


def extract_threads_post_with_char_control(markdown: str, post_number: int) -> Optional[dict]:
    """
    Threads投稿を抽出（文字数制御対応版）

    ≤500文字: 単一投稿
    >500文字: 2-3投稿スレッド

    Args:
        post_number: 投稿番号（1-3）

    Returns:
        dict: {"type": "single", "content": str} or
              {"type": "thread", "posts": [...], "total_posts": int}
    """
    # v2フォーマット: ## Threads投稿1（Top 1トピック: XXX）
    pattern = rf'## Threads投稿{post_number}（.*?\）\n\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    content = remove_markdown(match.group(1).strip())
    char_count = len(content)

    if char_count <= 500:
        return {"type": "single", "content": content, "char_count": char_count}
    else:
        # セマンティック分割: 段落単位で500文字以内に分割
        paragraphs = content.split('\n\n')
        posts = []
        current_post = ""

        for para in paragraphs:
            if len(current_post) + len(para) + 2 <= 500:
                current_post += para + "\n\n"
            else:
                if current_post:
                    posts.append({"content": current_post.strip(), "char_count": len(current_post.strip())})
                current_post = para + "\n\n"

        if current_post:
            posts.append({"content": current_post.strip(), "char_count": len(current_post.strip())})

        return {"type": "thread", "posts": posts, "total_posts": len(posts)}


# ========================================
# Late API投稿関数
# ========================================

def post_to_late_api(
    content: str,
    platform: str,
    account_id: str,
    scheduled_datetime: datetime,
    api_key: str,
    thread_items: Optional[List[str]] = None,
    first_comment: Optional[str] = None
) -> dict:
    """
    Late APIに1件の投稿を送信

    v2.1: LinkedIn firstComment対応追加

    Args:
        content: 投稿本文（スレッド時は最初の投稿）
        platform: プラットフォーム（linkedin, twitter, threads）
        account_id: プラットフォーム固有のアカウントID
        scheduled_datetime: 予約日時（JST）
        api_key: Late API キー
        thread_items: Xスレッド投稿時の各ツイートリスト
        first_comment: LinkedIn firstComment（LinkedInのみ対応）

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

    # LinkedIn firstComment対応
    if first_comment and platform == "linkedin":
        platform_config["platformSpecificData"] = {
            "firstComment": first_comment
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


def find_available_dates_for_linkedin(
    reserved_by_hour: dict,
    target_hour: int = 8,
    days_needed: int = 3,
    max_search_days: int = 14
) -> List[datetime.date]:
    """
    LinkedIn用に複数の空き日を検索

    Args:
        reserved_by_hour: 時間帯別の予約済み日付
        target_hour: 投稿時刻（デフォルト8時）
        days_needed: 必要な日数（デフォルト3日）
        max_search_days: 最大検索日数（デフォルト14日）

    Returns:
        List[datetime.date]: 利用可能な日付のリスト（最大3日）

    Raises:
        Exception: 必要な日数が見つからない場合
    """
    current_date = datetime.now(JST).date() + timedelta(days=1)
    available_dates = []

    for day_offset in range(max_search_days):
        check_date = current_date + timedelta(days=day_offset)

        if check_date not in reserved_by_hour.get(target_hour, set()):
            available_dates.append(check_date)

        if len(available_dates) == days_needed:
            break

    if len(available_dates) < days_needed:
        raise Exception(
            f"LinkedIn空き日が{len(available_dates)}日しか見つかりませんでした。"
            f"14日以内に{days_needed}日の空きが必要です。"
        )

    return available_dates


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

        # LinkedIn（案1-3を使用）
        for i in range(1, 4):
            linkedin_content = extract_linkedin_content(markdown_content, i)
            if linkedin_content:
                contents[f'linkedin{i}'] = linkedin_content
                print(f"  ✅ LinkedIn案{i}: {len(linkedin_content['full_content'])}文字")
            else:
                print(f"  ⚠️  LinkedIn案{i}: 抽出失敗")

        # Xスレッド1-3（Top 1-3トピック）
        for i in range(1, 4):
            x_thread = extract_x_thread_content(markdown_content, i)
            if x_thread:
                contents[f'x_thread{i}'] = x_thread
                print(f"  ✅ Xスレッド{i}: {len(x_thread)}ツイート")
            else:
                print(f"  ⚠️  Xスレッド{i}: 抽出失敗")

        # Threads投稿1-3（Top 1-3トピック、文字数制御）
        for i in range(1, 4):
            threads_post = extract_threads_post_with_char_control(markdown_content, i)
            if threads_post:
                contents[f'threads_post{i}'] = threads_post
                type_label = "単一" if threads_post['type'] == 'single' else f"スレッド{threads_post['total_posts']}投稿"
                print(f"  ✅ Threads投稿{i}: {type_label}")
            else:
                print(f"  ⚠️  Threads投稿{i}: 抽出失敗")

        # 4. 既存予約取得と日付決定
        print()
        print("🔍 既存予約投稿をチェック中...")
        existing = get_existing_scheduled_posts(api_key)
        print(f"   既存予約投稿: {len(existing['posts'])}件")

        # LinkedIn用の空き日を3日検出
        try:
            linkedin_dates = find_available_dates_for_linkedin(
                reserved_by_hour=existing['reserved_by_hour'],
                target_hour=8,
                days_needed=3,
                max_search_days=7
            )
            print(f"✅ LinkedIn空き日: {len(linkedin_dates)}日検出")
            for i, date in enumerate(linkedin_dates, 1):
                print(f"   {i}日目: {date}")
        except Exception as e:
            print(f"⚠️  7日以内に空き日不足。14日に延長して再試行...")
            linkedin_dates = find_available_dates_for_linkedin(
                reserved_by_hour=existing['reserved_by_hour'],
                target_hour=8,
                days_needed=3,
                max_search_days=14
            )
            print(f"✅ LinkedIn空き日: {len(linkedin_dates)}日検出（14日スキャン）")
            for i, date in enumerate(linkedin_dates, 1):
                print(f"   {i}日目: {date}")

        # X/Threads用の投稿日を検索（7:30, 12:00, 20:00が全て空いている日）
        target_date = find_available_date(existing['reserved_by_hour'], [7, 12, 20])
        print(f"✅ X/Threads投稿日: {target_date}")

        # 5. 投稿計画を作成
        posting_plan = []

        # LinkedIn（8:00、3投稿を3日分散）
        if linkedin_account_id:
            for i in range(1, 4):
                linkedin_key = f'linkedin{i}'
                if linkedin_key in contents:
                    posting_plan.append({
                        'platform': 'linkedin',
                        'type': 'main',
                        'time': '08:00',
                        'date': linkedin_dates[i-1],  # 空き日を個別指定
                        'content': contents[linkedin_key]['full_content'],
                        'account_id': linkedin_account_id,
                        'title': f'LinkedIn案{i}（Top {i}）',
                        'thread_items': None,
                        'first_comment': contents[linkedin_key].get('first_comment')
                    })

        # Xスレッド1-3（7:30, 12:00, 20:00）
        if twitter_account_id:
            for i in range(1, 4):
                x_thread_key = f'x_thread{i}'
                if x_thread_key in contents:
                    posting_plan.append({
                        'platform': 'twitter',
                        'type': 'thread',
                        'time': ['07:30', '12:00', '20:00'][i-1],
                        'content': contents[x_thread_key][0] if contents[x_thread_key] else '',
                        'account_id': twitter_account_id,
                        'title': f'Xスレッド{i}（Top {i}、{len(contents[x_thread_key])}ツイート）',
                        'thread_items': contents[x_thread_key]
                    })

        # Threads投稿1-3（7:30, 12:00, 20:00）
        if threads_account_id:
            for i in range(1, 4):
                threads_key = f'threads_post{i}'
                if threads_key in contents:
                    threads_data = contents[threads_key]
                    if threads_data['type'] == 'single':
                        # 単一投稿
                        posting_plan.append({
                            'platform': 'threads',
                            'type': 'new',
                            'time': ['07:30', '12:00', '20:00'][i-1],
                            'content': threads_data['content'],
                            'account_id': threads_account_id,
                            'title': f'Threads投稿{i}（Top {i}）',
                            'thread_items': None
                        })
                    else:
                        # スレッド投稿
                        posting_plan.append({
                            'platform': 'threads',
                            'type': 'new',
                            'time': ['07:30', '12:00', '20:00'][i-1],
                            'content': threads_data['posts'][0]['content'],
                            'account_id': threads_account_id,
                            'title': f'Threads投稿{i}（Top {i}、スレッド{threads_data["total_posts"]}投稿）',
                            'thread_items': [post['content'] for post in threads_data['posts']]
                        })

        # 6. 投稿計画を表示
        print()
        print("=" * 60)
        print("投稿計画（競合回避済み）")
        print("=" * 60)

        for plan in posting_plan:
            platform_emoji = {'linkedin': '💼', 'twitter': '🐦', 'threads': '🧵'}.get(plan['platform'], '📱')
            post_date = plan.get('date', target_date)  # LinkedInは個別日付
            print(f"{platform_emoji} {post_date} {plan['time']} JST - {plan['platform'].upper()}")
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
            # プラットフォーム別日付（LinkedInは個別日付）
            post_date = plan.get('date', target_date)
            scheduled_datetime = datetime.combine(
                post_date,
                datetime.min.time()
            ).replace(hour=hour, minute=minute, tzinfo=JST)

            platform_emoji = {'linkedin': '💼', 'twitter': '🐦', 'threads': '🧵'}.get(plan['platform'], '📱')
            print(f"{platform_emoji} {plan['platform'].upper()} ({plan['time']}, {post_date}) を投稿中...")
            print(f"   タイプ: {plan['type']}")

            # 指数バックオフリトライ
            retry_delays = [5, 15, 30]  # 秒
            success = False

            for retry_attempt, delay in enumerate(retry_delays + [None], 1):
                try:
                    result = post_to_late_api(
                        content=plan['content'],
                        platform=plan['platform'],
                        account_id=plan['account_id'],
                        scheduled_datetime=scheduled_datetime,
                        api_key=api_key,
                        thread_items=plan['thread_items'],
                        first_comment=plan.get('first_comment')
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
                    success = True
                    break  # 成功したらループ終了

                except Exception as e:
                    if delay is not None:
                        print(f"   ⚠️  リトライ {retry_attempt}/{len(retry_delays)}（{delay}秒後）...")
                        import time
                        time.sleep(delay)
                    else:
                        # 3回失敗→Markdownフォールバック
                        print(f"   ❌ 最終失敗: {e}")
                        data_dir = Path(__file__).parent.parent / "data"
                        fallback_file = data_dir / f"manual_posts/{plan['platform']}_{plan['type']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                        fallback_file.parent.mkdir(parents=True, exist_ok=True)
                        with open(fallback_file, 'w', encoding='utf-8') as f:
                            f.write(f"# 手動投稿用ファイル\n\n")
                            f.write(f"**プラットフォーム**: {plan['platform']}\n")
                            f.write(f"**予約日時**: {scheduled_datetime.isoformat()}\n\n")
                            f.write(f"## 投稿内容\n\n{plan['content']}\n")
                        print(f"   📄 手動投稿用ファイル生成: {fallback_file.name}")
                        print()

                        results.append({
                            "platform": plan['platform'],
                            "type": plan['type'],
                            "status": "error",
                            "error_message": str(e),
                            "scheduled_for": scheduled_datetime.isoformat(),
                            "fallback_file": str(fallback_file)
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
