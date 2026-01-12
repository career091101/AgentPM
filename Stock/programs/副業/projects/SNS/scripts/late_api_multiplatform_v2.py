#!/usr/bin/env python3
"""
Late API v2 - マルチプラットフォーム予約投稿スクリプト

v2仕様:
- LinkedIn: 3日分散投稿（Late API空き日自動検出）
- X/Threads: 同時刻投稿（各Top記事を同じ時間帯に配信）

修正履歴:
- 2026-01-12: LinkedIn案3抽出失敗による重複投稿問題を修正（Fix 7, 8）
  - Fix 1-2 (P0): X/Threads threadItems構造修正（"text" → "content"）
  - Fix 3-5 (P1): post_id_late_api抽出パス修正（3箇所）
  - Fix 6 (P2): Markdown除去機能追加（remove_markdown関数）
  - Fix 7: 案3抽出ロジック書き直し（セクション見出し直接検索）
  - Fix 8: 投稿数と日数の不一致チェック追加
  - 詳細: docs/LINKEDIN_EXTRACTION_BEST_PRACTICES.md 参照
"""

import requests
import json
from datetime import datetime, timedelta
import sys
from pathlib import Path
import pytz

# プロジェクトルート追加
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

# Late API共通ライブラリをインポート
from late_api_post import post_to_late_api, load_config, get_account_id, get_headers, handle_late_api_response

# 設定ファイル読み込み
CONFIG_PATH = PROJECT_ROOT / "config" / "late_api_config.json"
config = load_config(str(CONFIG_PATH))

API_KEY = config["api_key"]
BASE_URL = config["base_url"]
ACCOUNTS = config["accounts"]
JST = pytz.timezone("Asia/Tokyo")

# Phase 3生成ファイルパス
LINKEDIN_FILE = PROJECT_ROOT / "data" / "posts_generated_takano_20260112_v2.md"
X_THREADS_FILE = PROJECT_ROOT / "data" / "x_threads_20260112.json"
THREADS_POSTS_FILE = PROJECT_ROOT / "data" / "threads_posts_20260112.json"

# 出力ファイルパス
OUTPUT_FILE = PROJECT_ROOT / "data" / "late_api_v2_20260112.json"


def get_existing_posts(platform, days_past=7, days_future=7):
    """
    Late APIから既存の予約投稿をスキャン

    Args:
        platform: プラットフォーム名（linkedin, twitter, threads）
        days_past: 過去何日分をスキャンするか
        days_future: 未来何日分をスキャンするか

    Returns:
        既存投稿のリスト
    """
    account_id = ACCOUNTS[platform]["accountId"]

    # 日付範囲計算
    now = datetime.now(JST)
    start_date = (now - timedelta(days=days_past)).strftime("%Y-%m-%d")
    end_date = (now + timedelta(days=days_future)).strftime("%Y-%m-%d")

    # Late API GET /posts エンドポイント
    url = f"{BASE_URL}/posts"
    params = {
        "accountId": account_id,
        "start_date": start_date,
        "end_date": end_date
    }

    try:
        response = requests.get(url, headers=get_headers(API_KEY), params=params)
        response.raise_for_status()
        posts = response.json().get("posts", [])
        print(f"✅ {platform}: 既存予約投稿 {len(posts)}件を取得")
        return posts
    except requests.exceptions.RequestException as e:
        print(f"❌ {platform}: 既存予約投稿取得失敗 - {e}")
        return []


def find_linkedin_available_days(existing_posts, target_hour=8, target_count=3):
    """
    LinkedInの空き日を自動検出

    Args:
        existing_posts: 既存投稿リスト
        target_hour: 目標投稿時刻（デフォルト8:00）
        target_count: 必要な空き日数（デフォルト3日）

    Returns:
        空き日のリスト（ISO 8601形式）
    """
    # 既存投稿の日時を抽出
    existing_dates = set()
    for post in existing_posts:
        scheduled_at = post.get("scheduled_at")
        if scheduled_at:
            dt = datetime.fromisoformat(scheduled_at.replace("Z", "+00:00"))
            dt_jst = dt.astimezone(JST)
            # 8:00前後1時間以内に投稿があればその日は埋まっている
            if abs(dt_jst.hour - target_hour) <= 1:
                existing_dates.add(dt_jst.date())

    # 今日から+1日〜+7日をスキャン
    now = datetime.now(JST)
    available_days = []

    for i in range(1, 8):  # +1〜+7日
        candidate_date = (now + timedelta(days=i)).date()
        if candidate_date not in existing_dates:
            # ISO 8601形式で保存
            scheduled_dt = datetime.combine(candidate_date, datetime.min.time()).replace(hour=target_hour, minute=0, second=0, tzinfo=JST)
            available_days.append(scheduled_dt.isoformat())

            if len(available_days) >= target_count:
                break

    if len(available_days) < target_count:
        print(f"⚠️ LinkedIn: 空き日が不足しています（{len(available_days)}/{target_count}日）")

    return available_days


def remove_markdown(text: str) -> str:
    """Markdown装飾を除去"""
    import re
    # **太字** → 太字
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # _イタリック_ → イタリック
    text = re.sub(r'_(.+?)_', r'\1', text)
    # `コード` → コード
    text = re.sub(r'`(.+?)`', r'\1', text)
    # - 箇条書き → 箇条書き（行頭のマーカー除去）
    text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
    # 1. 番号リスト → 番号リスト（行頭のマーカー除去）
    text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
    # --- 区切り線を末尾から除去（Fix 9: 2026-01-12追加）
    text = re.sub(r'\n*---\s*$', '', text)
    return text


def extract_linkedin_posts():
    """
    posts_generated_takano_20260112_v2.md から3投稿を抽出

    Returns:
        LinkedInの3投稿リスト（Markdown装飾除去済み）

    Notes:
        - 2026-01-12修正: 案3抽出失敗による重複投稿問題を解決
        - ベストプラクティス: docs/LINKEDIN_EXTRACTION_BEST_PRACTICES.md 参照
        - セクション見出し (### チェックリスト検証) を直接探すことで、
          固定区切り文字 (---) に依存しない堅牢な抽出を実現
    """
    with open(LINKEDIN_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    posts = []

    # 投稿案1を抽出
    if "## 投稿案1" in content:
        start_idx = content.find("## 投稿案1")
        end_idx = content.find("## 投稿案2")
        post1_section = content[start_idx:end_idx]

        # チェックリストより前を本文とする
        if "### チェックリスト検証" in post1_section:
            post1_text = post1_section[:post1_section.find("### チェックリスト検証")]
            # 見出し（## 投稿案1...）を除去
            post1_lines = post1_text.split("\n")[2:]  # 最初の2行（見出し+空行）をスキップ
            post1_clean = "\n".join(post1_lines).strip()
            # Markdown装飾を除去
            post1_clean = remove_markdown(post1_clean)
            posts.append(post1_clean)

    # 投稿案2を抽出
    if "## 投稿案2" in content:
        start_idx = content.find("## 投稿案2")
        end_idx = content.find("## 投稿案3")
        post2_section = content[start_idx:end_idx]

        if "### チェックリスト検証" in post2_section:
            post2_text = post2_section[:post2_section.find("### チェックリスト検証")]
            post2_lines = post2_text.split("\n")[2:]
            post2_clean = "\n".join(post2_lines).strip()
            # Markdown装飾を除去
            post2_clean = remove_markdown(post2_clean)
            posts.append(post2_clean)

    # 投稿案3を抽出
    # 重要: この実装は2026-01-12に修正されました（Fix 7）
    # 以前の実装では固定区切り文字 (---) に依存していたため、
    # 案3の途中で切断され、抽出失敗→重複投稿問題が発生していました
    if "## 投稿案3" in content:
        start_idx = content.find("## 投稿案3")

        # [修正ポイント1] セクション見出しを直接探す
        # 固定区切り文字 (---) は予測不可能な位置に出現するため、
        # 明確なセクション見出し (### チェックリスト検証) を探す方が安全
        checklist_idx = content.find("### チェックリスト検証", start_idx)
        if checklist_idx != -1:
            # チェックリスト検証が見つかった場合、その直前まで
            post3_text = content[start_idx:checklist_idx]
        else:
            # [修正ポイント2] 複数の終端候補から最短を選択
            # チェックリスト検証が見つからない場合の安全策として、
            # 次の区切り線、比較表セクション、ファイル末尾のいずれか最短を使用
            end_candidates = [
                content.find("---", start_idx + 100),
                content.find("## 比較表", start_idx),
                len(content)  # ファイル末尾
            ]
            # 有効なインデックス（-1以外）の中で最小値を取得
            end_idx = min([idx for idx in end_candidates if idx != -1])
            post3_text = content[start_idx:end_idx]

        # 見出し（## 投稿案3...）を除去
        post3_lines = post3_text.split("\n")[2:]  # 最初の2行（見出し+空行）をスキップ
        post3_clean = "\n".join(post3_lines).strip()

        # Markdown装飾を除去（Fix 6: remove_markdown関数追加）
        post3_clean = remove_markdown(post3_clean)

        # [修正ポイント3] 空チェックを追加
        # 抽出失敗時に空文字列を追加しないようにする
        if post3_clean:
            posts.append(post3_clean)

    print(f"✅ LinkedIn: {len(posts)}投稿を抽出（Markdown除去済み）")
    return posts


def extract_x_threads():
    """
    x_threads_20260112.json から3スレッドを抽出

    Returns:
        Xの3スレッドリスト
    """
    with open(X_THREADS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    threads = data.get("threads", [])
    print(f"✅ X: {len(threads)}スレッドを抽出")
    return threads[:3]  # Top 3のみ


def extract_threads_posts():
    """
    threads_posts_20260112.json から3投稿（各3パート）を抽出

    Returns:
        Threadsの3投稿リスト
    """
    with open(THREADS_POSTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    posts = data.get("posts", [])
    print(f"✅ Threads: {len(posts)}投稿を抽出")
    return posts[:3]  # Top 3のみ


def schedule_linkedin_post(content, scheduled_at, post_id):
    """
    LinkedIn投稿を予約

    Args:
        content: 投稿本文
        scheduled_at: 予約日時（ISO 8601形式）
        post_id: 投稿ID（top_1_linkedin等）

    Returns:
        APIレスポンス
    """
    account_id = ACCOUNTS["linkedin"]["accountId"]

    try:
        result = post_to_late_api(
            content=content,
            platform="linkedin",
            account_id=account_id,
            scheduled_for=scheduled_at,
            timezone="Asia/Tokyo",
            config_path=str(CONFIG_PATH)
        )

        print(f"✅ LinkedIn ({post_id}): 予約成功 - {scheduled_at}")
        post_data = result.get("post", {})
        return {
            "post_id": post_id,
            "platform": "linkedin",
            "type": "post",
            "scheduled_date": scheduled_at,
            "status": "scheduled",
            "post_id_late_api": post_data.get("_id"),
            "url": "N/A"  # scheduled時はURL未定
        }
    except Exception as e:
        print(f"❌ LinkedIn ({post_id}): 予約失敗 - {e}")
        return {
            "post_id": post_id,
            "platform": "linkedin",
            "type": "post",
            "scheduled_date": scheduled_at,
            "status": "failed",
            "error": str(e)
        }


def schedule_x_thread(thread_data, scheduled_at, post_id):
    """
    Xスレッドを予約

    Args:
        thread_data: スレッドデータ（tweets配列含む）
        scheduled_at: 予約日時（ISO 8601形式）
        post_id: 投稿ID（top_1_x等）

    Returns:
        APIレスポンス
    """
    account_id = ACCOUNTS["twitter"]["accountId"]

    # tweetsから本文を抽出
    tweets = thread_data.get("tweets", [])
    thread_texts = [tweet.get("text", "") for tweet in tweets]

    # X/Twitterスレッド用のplatform_specific_data
    platform_specific_data = {
        "threadItems": [{"content": text} for text in thread_texts]
    }

    try:
        result = post_to_late_api(
            content=thread_texts[0] if thread_texts else "",  # 最初のツイート
            platform="twitter",
            account_id=account_id,
            scheduled_for=scheduled_at,
            timezone="Asia/Tokyo",
            platform_specific_data=platform_specific_data,
            config_path=str(CONFIG_PATH)
        )

        print(f"✅ X ({post_id}): 予約成功 - {scheduled_at}")
        post_data = result.get("post", {})
        return {
            "post_id": post_id,
            "platform": "x",
            "type": "thread",
            "scheduled_date": scheduled_at,
            "status": "scheduled",
            "post_id_late_api": post_data.get("_id"),
            "url": "N/A"  # scheduled時はURL未定
        }
    except Exception as e:
        print(f"❌ X ({post_id}): 予約失敗 - {e}")
        return {
            "post_id": post_id,
            "platform": "x",
            "type": "thread",
            "scheduled_date": scheduled_at,
            "status": "failed",
            "error": str(e)
        }


def schedule_threads_post(post_data, scheduled_at, post_id):
    """
    Threads投稿を予約（マルチパート対応）

    Args:
        post_data: 投稿データ（parts配列含む）
        scheduled_at: 予約日時（ISO 8601形式）
        post_id: 投稿ID（top_1_threads等）

    Returns:
        APIレスポンス
    """
    account_id = ACCOUNTS["threads"]["accountId"]

    # partsから本文を抽出
    parts = post_data.get("parts", [])
    thread_texts = [part.get("text", "") for part in parts]

    # Threadsスレッド用のplatform_specific_data
    platform_specific_data = {
        "threadItems": [{"content": text} for text in thread_texts]
    }

    try:
        result = post_to_late_api(
            content=thread_texts[0] if thread_texts else "",  # 最初のパート
            platform="threads",
            account_id=account_id,
            scheduled_for=scheduled_at,
            timezone="Asia/Tokyo",
            platform_specific_data=platform_specific_data,
            config_path=str(CONFIG_PATH)
        )

        print(f"✅ Threads ({post_id}): 予約成功 - {scheduled_at}")
        post_data = result.get("post", {})
        return {
            "post_id": post_id,
            "platform": "threads",
            "type": "post_multipart",
            "scheduled_date": scheduled_at,
            "status": "scheduled",
            "post_id_late_api": post_data.get("_id"),
            "url": "N/A",  # scheduled時はURL未定
            "parts": len(parts)
        }
    except Exception as e:
        print(f"❌ Threads ({post_id}): 予約失敗 - {e}")
        return {
            "post_id": post_id,
            "platform": "threads",
            "type": "post_multipart",
            "scheduled_date": scheduled_at,
            "status": "failed",
            "error": str(e),
            "parts": len(parts)
        }


def main():
    print("=" * 80)
    print("Late API v2 - マルチプラットフォーム予約投稿")
    print("=" * 80)
    print()

    # STEP 1: 既存予約検出
    print("STEP 1: 既存予約検出")
    linkedin_existing = get_existing_posts("linkedin", days_past=7, days_future=7)
    x_existing = get_existing_posts("twitter", days_past=1, days_future=7)
    threads_existing = get_existing_posts("threads", days_past=1, days_future=7)
    print()

    # STEP 2: LinkedIn空き日検索
    print("STEP 2: LinkedIn空き日検索")
    linkedin_available_days = find_linkedin_available_days(linkedin_existing, target_hour=8, target_count=3)
    print(f"✅ LinkedIn空き日: {len(linkedin_available_days)}日")
    for day in linkedin_available_days:
        print(f"  - {day}")
    print()

    # STEP 3: 投稿コンテンツ抽出
    print("STEP 3: 投稿コンテンツ抽出")
    linkedin_posts = extract_linkedin_posts()
    x_threads = extract_x_threads()
    threads_posts = extract_threads_posts()
    print()

    # STEP 4: X/Threads同時刻スケジュール計算
    print("STEP 4: X/Threads同時刻スケジュール計算")
    now = datetime.now(JST)

    # 各時刻が過去の場合は翌日にスケジュール
    x_threads_schedule = []
    target_times = [(7, 30), (12, 0), (20, 0)]

    for hour, minute in target_times:
        target_dt = datetime.combine(now.date(), datetime.min.time()).replace(hour=hour, minute=minute, second=0, tzinfo=JST)

        # 過去の時刻の場合は翌日にスケジュール
        if target_dt < now:
            target_dt = target_dt + timedelta(days=1)

        x_threads_schedule.append(target_dt.isoformat())

    print("X/Threads同時刻投稿:")
    for i, scheduled_at in enumerate(x_threads_schedule, 1):
        print(f"  Top {i}: {scheduled_at}")
    print()

    # STEP 5: Late API予約投稿
    print("STEP 5: Late API予約投稿")
    results = []

    # LinkedIn 3日分散投稿
    print("LinkedIn 3日分散投稿:")

    # [Fix 8] 投稿数と利用可能日数の不一致チェック（2026-01-12追加）
    # 重要: この検証は重複投稿を防ぐために必須です
    # 理由: extract_linkedin_posts() が2件しか返さないのに、
    #       linkedin_available_days が3日分ある場合、zip() は2件しかループしません。
    #       しかし、過去のバグでは同じ投稿が3回送信される問題がありました。
    # 対策: 日数リストを投稿数に合わせて切り詰めることで、
    #       zip() の暗黙的な動作に依存せず、明示的に長さを一致させます。
    if len(linkedin_posts) != len(linkedin_available_days):
        print(f"⚠️  警告: LinkedIn投稿数({len(linkedin_posts)})と利用可能日数({len(linkedin_available_days)})が一致しません")
        print(f"  → 投稿数に合わせて日数を調整します")
        linkedin_available_days = linkedin_available_days[:len(linkedin_posts)]

    # ゼロ件エラー検出
    if len(linkedin_posts) == 0:
        print("⚠️  エラー: LinkedIn投稿が1件も抽出されていません")
        print("  → extract_linkedin_posts() の実装を確認してください")
    else:
        for i, (content, scheduled_at) in enumerate(zip(linkedin_posts, linkedin_available_days), 1):
            post_id = f"top_{i}_linkedin"
            result = schedule_linkedin_post(content, scheduled_at, post_id)
            results.append(result)
    print()

    # X/Threads同時刻投稿
    print("X/Threads同時刻投稿:")
    for i, (x_thread, threads_post, scheduled_at) in enumerate(zip(x_threads, threads_posts, x_threads_schedule), 1):
        # X投稿
        post_id_x = f"top_{i}_x"
        result_x = schedule_x_thread(x_thread, scheduled_at, post_id_x)
        results.append(result_x)

        # Threads投稿
        post_id_threads = f"top_{i}_threads"
        result_threads = schedule_threads_post(threads_post, scheduled_at, post_id_threads)
        results.append(result_threads)
    print()

    # STEP 6: 結果集計
    print("STEP 6: 結果集計")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    failed = sum(1 for r in results if r.get("status") == "failed")

    print(f"✅ 成功: {successful}投稿")
    print(f"❌ 失敗: {failed}投稿")
    print()

    # STEP 7: JSON出力
    print("STEP 7: JSON出力")
    output_data = {
        "metadata": {
            "scheduled_at": datetime.now(JST).isoformat(),
            "total_posts": len(results),
            "successful": successful,
            "failed": failed,
            "version": "v2_distributed_and_synchronized"
        },
        "schedule_summary": {
            "linkedin_distribution": {
                f"day{i+1}": day for i, day in enumerate(linkedin_available_days)
            },
            "x_threads_synchronized": {
                "top_1": x_threads_schedule[0],
                "top_2": x_threads_schedule[1],
                "top_3": x_threads_schedule[2]
            }
        },
        "posts": results
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✅ 出力完了: {OUTPUT_FILE}")
    print()

    # エラー発生時の処理
    if failed > 0:
        print("⚠️ 一部投稿が失敗しました。詳細は出力JSONを確認してください。")
        print()
        print("失敗した投稿:")
        for result in results:
            if result.get("status") == "failed":
                print(f"  - {result['post_id']}: {result.get('error', 'Unknown error')}")

    print("=" * 80)
    print("Phase 4完了")
    print("=" * 80)


if __name__ == "__main__":
    main()
