#!/usr/bin/env python3
"""
Late API投稿の共通関数ライブラリ

Phase 1-5で使用する関数を提供：
- 基本的なLate API投稿
- スレッド分割（X: 140文字、Threads: 500文字）
- スケジュール計算
- エラーハンドリング
"""

import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from zoneinfo import ZoneInfo


# ===========================
# 設定とエラークラス
# ===========================

def load_config(config_path: str = None) -> dict:
    """Late API設定をロード"""
    if config_path is None:
        config_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/config/late_api_config.json"

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_account_id(platform: str, config_path: str = None) -> str:
    """
    プラットフォーム名からアカウントIDを取得

    Args:
        platform: プラットフォーム名（linkedin, twitter, threads, instagram）
        config_path: 設定ファイルパス

    Returns:
        str: アカウントID

    Raises:
        ValueError: 指定されたプラットフォームのアカウントが見つからない場合
    """
    config = load_config(config_path)
    accounts = config.get("accounts", {})

    if platform not in accounts:
        available_platforms = list(accounts.keys())
        raise ValueError(
            f"プラットフォーム '{platform}' のアカウントが見つかりません。\n"
            f"利用可能なプラットフォーム: {available_platforms}"
        )

    return accounts[platform]["accountId"]


class LateAPIError(Exception):
    """Late API基本エラー"""
    pass


class RateLimitError(LateAPIError):
    """レート制限エラー（429）"""
    pass


class AuthenticationError(LateAPIError):
    """認証エラー（401）"""
    pass


# ===========================
# Phase 1: 基本的なLate API投稿
# ===========================

def get_headers(api_key: str) -> dict:
    """Late APIリクエストヘッダー"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


def handle_late_api_response(response: requests.Response) -> dict:
    """
    Late APIレスポンスのエラーハンドリング

    Returns:
        dict: 成功時のレスポンスJSON

    Raises:
        AuthenticationError: 401エラー
        RateLimitError: 429エラー
        LateAPIError: その他のエラー
    """
    if response.status_code == 200 or response.status_code == 201:
        return response.json()

    elif response.status_code == 401:
        raise AuthenticationError(
            f"認証失敗: APIキーが無効または期限切れです。\n"
            f"Response: {response.text}"
        )

    elif response.status_code == 429:
        raise RateLimitError(
            f"レート制限超過: 1時間後に再試行してください。\n"
            f"Response: {response.text}"
        )

    elif response.status_code == 400:
        raise LateAPIError(
            f"リクエストエラー (400): パラメータが不正です。\n"
            f"Response: {response.text}"
        )

    elif response.status_code >= 500:
        raise LateAPIError(
            f"サーバーエラー ({response.status_code}): Late APIサーバーに問題があります。\n"
            f"Response: {response.text}"
        )

    else:
        raise LateAPIError(
            f"不明なエラー ({response.status_code}): {response.text}"
        )


def post_to_late_api(
    content: str,
    platform: str,
    account_id: str,
    scheduled_for: Optional[str] = None,
    timezone: str = "Asia/Tokyo",
    platform_specific_data: Optional[dict] = None,
    config_path: str = None
) -> dict:
    """
    Late API経由で投稿（基本関数）

    Args:
        content: 投稿内容
        platform: プラットフォーム名（linkedin, facebook, twitter, threads）
        account_id: アカウントID
        scheduled_for: 予約投稿時刻（ISO8601形式、例: "2026-01-02T08:00:00+09:00"）
        timezone: タイムゾーン（デフォルト: "Asia/Tokyo"）
        platform_specific_data: プラットフォーム固有データ（threadItems等）
        config_path: 設定ファイルパス

    Returns:
        dict: Late APIレスポンス

    Raises:
        LateAPIError: API呼び出しエラー
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    # リクエストボディ構築
    platform_data = {
        "platform": platform,
        "accountId": account_id
    }

    if platform_specific_data:
        platform_data["platformSpecificData"] = platform_specific_data

    request_body = {
        "platforms": [platform_data]
    }

    # contentはthreadItemsがない場合のみ設定
    if not platform_specific_data or "threadItems" not in platform_specific_data:
        request_body["content"] = content

    # スケジューリング設定
    if scheduled_for:
        request_body["scheduledFor"] = scheduled_for
        request_body["timezone"] = timezone
    else:
        request_body["publishNow"] = True

    # API呼び出し
    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body,
            timeout=30
        )

        return handle_late_api_response(response)

    except requests.exceptions.Timeout:
        raise LateAPIError("タイムアウト: Late APIへの接続がタイムアウトしました")

    except requests.exceptions.ConnectionError:
        raise LateAPIError("接続エラー: Late APIに接続できませんでした")


def post_to_linkedin(
    content: str,
    account_id: str,
    scheduled_for: Optional[str] = None,
    config_path: str = None
) -> dict:
    """LinkedIn投稿"""
    return post_to_late_api(
        content=content,
        platform="linkedin",
        account_id=account_id,
        scheduled_for=scheduled_for,
        config_path=config_path
    )


def post_to_facebook(
    content: str,
    account_id: str,
    scheduled_for: Optional[str] = None,
    config_path: str = None
) -> dict:
    """Facebook投稿"""
    return post_to_late_api(
        content=content,
        platform="facebook",
        account_id=account_id,
        scheduled_for=scheduled_for,
        config_path=config_path
    )


# ===========================
# Phase 3: スレッド分割機能（骨組み）
# ===========================

def split_for_twitter(content: str, max_length: int = 140) -> List[str]:
    """
    X（Twitter）用スレッド分割

    優先順位:
    1. 段落分割（\\n\\n）
    2. 句点分割（。）
    3. 読点分割（、）※柔軟基準
    4. 強制分割（最終手段）

    Args:
        content: 長文コンテンツ（700-1500字）
        max_length: 最大文字数（デフォルト: 140）

    Returns:
        List[str]: 番号付きツイート配列（"(1/N)" 形式）
    """
    # 番号表記用のマージン（"(N/N)\n\n" の最大長）
    number_margin = 10

    # 段落分割
    paragraphs = content.split('\n\n')
    tweets = []
    current_tweet = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # 段落が制限内に収まる場合
        if len(para) <= max_length - number_margin:
            # 現在のツイートに追加できるか確認
            if current_tweet and len(current_tweet) + len(para) + 2 <= max_length - number_margin:
                current_tweet += "\n\n" + para
            else:
                # 現在のツイートを確定し、新しいツイート開始
                if current_tweet:
                    tweets.append(current_tweet.strip())
                current_tweet = para
        else:
            # 段落が長すぎる場合は句点で分割
            if current_tweet:
                tweets.append(current_tweet.strip())
                current_tweet = ""

            sentences = para.split('。')
            for sentence in sentences:
                if not sentence.strip():
                    continue

                sentence_with_period = sentence.strip() + '。'

                # 句点付き文が制限内に収まる場合
                if len(sentence_with_period) <= max_length - number_margin:
                    if current_tweet and len(current_tweet) + len(sentence_with_period) <= max_length - number_margin:
                        current_tweet += sentence_with_period
                    else:
                        if current_tweet:
                            tweets.append(current_tweet.strip())
                        current_tweet = sentence_with_period
                else:
                    # 文が長すぎる場合は読点で分割
                    if current_tweet:
                        tweets.append(current_tweet.strip())
                        current_tweet = ""

                    clauses = sentence_with_period.split('、')
                    for clause in clauses:
                        clause = clause.strip()
                        if not clause:
                            continue

                        # 読点を復元（最後の句以外）
                        if clause != clauses[-1].strip():
                            clause += '、'

                        if len(clause) <= max_length - number_margin:
                            if current_tweet and len(current_tweet) + len(clause) <= max_length - number_margin:
                                current_tweet += clause
                            else:
                                if current_tweet:
                                    tweets.append(current_tweet.strip())
                                current_tweet = clause
                        else:
                            # 強制分割（最終手段）
                            if current_tweet:
                                tweets.append(current_tweet.strip())
                                current_tweet = ""

                            while len(clause) > max_length - number_margin:
                                tweets.append(clause[:max_length - number_margin].strip())
                                clause = clause[max_length - number_margin:]

                            if clause:
                                current_tweet = clause

    # 残りのツイートを追加
    if current_tweet:
        tweets.append(current_tweet.strip())

    # 5ツイート未満の場合は最長ツイートを分割
    while len(tweets) < 5 and tweets:
        # 最長ツイートを見つける
        longest_idx = max(range(len(tweets)), key=lambda i: len(tweets[i]))
        longest_tweet = tweets[longest_idx]

        # 60文字以下の場合は分割できないのでbreak
        if len(longest_tweet) <= 60:
            break

        # 半分で分割
        mid_point = len(longest_tweet) // 2
        # 句点か読点で分割点を探す
        split_point = mid_point
        for offset in range(20):  # 前後20文字以内で探す
            if mid_point + offset < len(longest_tweet) and longest_tweet[mid_point + offset] in ['。', '、']:
                split_point = mid_point + offset + 1
                break
            if mid_point - offset >= 0 and longest_tweet[mid_point - offset] in ['。', '、']:
                split_point = mid_point - offset + 1
                break

        tweets[longest_idx] = longest_tweet[:split_point].strip()
        tweets.insert(longest_idx + 1, longest_tweet[split_point:].strip())

    # 番号付与 "(1/N)" 形式
    total = len(tweets)
    numbered_tweets = [f"({i+1}/{total})\n\n{tweet}" for i, tweet in enumerate(tweets)]

    return numbered_tweets


def split_for_threads(content: str, max_length: int = 500) -> List[str]:
    """
    Threads用スレッド分割

    要件: 500文字×3投稿
    分割: セクション→段落の順

    Args:
        content: 長文コンテンツ（700-1500字）
        max_length: 最大文字数（デフォルト: 500）

    Returns:
        List[str]: 3投稿の配列
    """
    # セクション区切り（━━━）で分割
    sections = content.split('━━━')
    posts = []
    current_post = ""

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # セクションが制限内に収まる場合
        if len(section) <= max_length:
            if current_post and len(current_post) + len(section) + 2 <= max_length:
                current_post += "\n\n" + section
            else:
                if current_post:
                    posts.append(current_post.strip())
                current_post = section
        else:
            # セクションが長すぎる場合は段落で分割
            if current_post:
                posts.append(current_post.strip())
                current_post = ""

            paragraphs = section.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue

                if len(para) <= max_length:
                    if current_post and len(current_post) + len(para) + 2 <= max_length:
                        current_post += "\n\n" + para
                    else:
                        if current_post:
                            posts.append(current_post.strip())
                        current_post = para
                else:
                    # 段落が長すぎる場合は句点で分割
                    if current_post:
                        posts.append(current_post.strip())
                        current_post = ""

                    sentences = para.split('。')
                    for sentence in sentences:
                        if not sentence.strip():
                            continue

                        sentence_with_period = sentence.strip() + '。'

                        if len(sentence_with_period) <= max_length:
                            if current_post and len(current_post) + len(sentence_with_period) <= max_length:
                                current_post += sentence_with_period
                            else:
                                if current_post:
                                    posts.append(current_post.strip())
                                current_post = sentence_with_period
                        else:
                            # 文が長すぎる場合は強制分割
                            if current_post:
                                posts.append(current_post.strip())
                                current_post = ""

                            while len(sentence_with_period) > max_length:
                                posts.append(sentence_with_period[:max_length].strip())
                                sentence_with_period = sentence_with_period[max_length:]

                            if sentence_with_period:
                                current_post = sentence_with_period

    # 残りの投稿を追加
    if current_post:
        posts.append(current_post.strip())

    # 3投稿に調整
    while len(posts) < 3:
        # 最長投稿を分割
        if not posts:
            # コンテンツが空の場合
            return ["", "", ""]

        longest_idx = max(range(len(posts)), key=lambda i: len(posts[i]))
        longest_post = posts[longest_idx]

        # 100文字以下の場合は分割できないのでbreak
        if len(longest_post) <= 100:
            break

        # 半分で分割
        mid_point = len(longest_post) // 2

        # 段落、句点、読点で分割点を探す
        split_point = mid_point
        for offset in range(50):  # 前後50文字以内で探す
            if mid_point + offset < len(longest_post):
                if longest_post[mid_point + offset:mid_point + offset + 2] == '\n\n':
                    split_point = mid_point + offset + 2
                    break
                elif longest_post[mid_point + offset] in ['。', '、']:
                    split_point = mid_point + offset + 1
                    break
            if mid_point - offset >= 0:
                if mid_point - offset >= 2 and longest_post[mid_point - offset - 2:mid_point - offset] == '\n\n':
                    split_point = mid_point - offset
                    break
                elif longest_post[mid_point - offset] in ['。', '、']:
                    split_point = mid_point - offset + 1
                    break

        posts[longest_idx] = longest_post[:split_point].strip()
        posts.insert(longest_idx + 1, longest_post[split_point:].strip())

    while len(posts) > 3:
        # 最短の連続2投稿を統合
        shortest_pair_idx = 0
        shortest_pair_len = len(posts[0]) + len(posts[1]) if len(posts) > 1 else float('inf')

        for i in range(len(posts) - 1):
            pair_len = len(posts[i]) + len(posts[i + 1])
            if pair_len < shortest_pair_len and pair_len <= max_length:
                shortest_pair_idx = i
                shortest_pair_len = pair_len

        # 統合
        posts[shortest_pair_idx] = posts[shortest_pair_idx] + "\n\n" + posts[shortest_pair_idx + 1]
        posts.pop(shortest_pair_idx + 1)

    return posts


def post_to_twitter_thread(
    content: str,
    account_id: str,
    scheduled_for: Optional[str] = None,
    config_path: str = None
) -> dict:
    """
    X（Twitter）スレッド投稿

    Args:
        content: 長文コンテンツ（自動的にスレッド分割）
        account_id: XアカウントID
        scheduled_for: 予約投稿時刻（オプション）
        config_path: 設定ファイルパス

    Returns:
        dict: Late APIレスポンス
    """
    # スレッド分割
    thread_items = split_for_twitter(content)

    # threadItems形式に変換
    thread_items_data = [{"content": tweet} for tweet in thread_items]

    # Late API投稿
    return post_to_late_api(
        content="",  # threadItems使用時は空
        platform="twitter",
        account_id=account_id,
        scheduled_for=scheduled_for,
        platform_specific_data={"threadItems": thread_items_data},
        config_path=config_path
    )


def post_to_threads_thread(
    content: str,
    account_id: str,
    scheduled_for: Optional[str] = None,
    config_path: str = None
) -> dict:
    """
    Threadsスレッド投稿

    Args:
        content: 長文コンテンツ（自動的にスレッド分割）
        account_id: ThreadsアカウントID
        scheduled_for: 予約投稿時刻（オプション）
        config_path: 設定ファイルパス

    Returns:
        dict: Late APIレスポンス
    """
    # スレッド分割
    thread_posts = split_for_threads(content)

    # threadItems形式に変換
    thread_items_data = [{"content": post} for post in thread_posts]

    # Late API投稿
    return post_to_late_api(
        content="",  # threadItems使用時は空
        platform="threads",
        account_id=account_id,
        scheduled_for=scheduled_for,
        platform_specific_data={"threadItems": thread_items_data},
        config_path=config_path
    )


# ===========================
# Phase 4: スケジュール計算
# ===========================

def calculate_schedule(
    topic_index: int,
    base_date: datetime = None
) -> dict:
    """
    トピックインデックスに基づいてスケジュール計算

    Args:
        topic_index: トピックインデックス（0=今日、1=明日、2=明後日）
        base_date: 基準日時（デフォルト: 現在時刻）

    Returns:
        dict: {
            "linkedin": "2026-01-02T08:00:00+09:00",  // LinkedIn投稿時刻
            "others": "2026-01-02T20:00:00+09:00"     // その他投稿時刻
        }
    """
    if base_date is None:
        base_date = datetime.now(ZoneInfo('Asia/Tokyo'))

    # トピックインデックスに応じた日付オフセット
    target_date = base_date + timedelta(days=topic_index)

    # LinkedIn: 朝8時
    linkedin_time = target_date.replace(hour=8, minute=0, second=0, microsecond=0)

    # その他: 夜20時
    others_time = target_date.replace(hour=20, minute=0, second=0, microsecond=0)

    return {
        "linkedin": linkedin_time.isoformat(),
        "others": others_time.isoformat()
    }


def get_existing_scheduled_posts(config_path: str = None, target_hour: int = None) -> dict:
    """
    Late APIから既存の予約投稿を取得

    Args:
        config_path: 設定ファイルパス
        target_hour: フィルタリング対象の時刻（None=全時刻、8=8:00 AM、20=20:00）

    Returns:
        dict: {
            "posts": [...],  // 予約投稿リスト
            "reserved_8am_dates": [...],  // 8:00 JST予約済み日付リスト（互換性維持）
            "reserved_20pm_dates": [...],  // 20:00 JST予約済み日付リスト
            "reserved_dates_by_hour": {7: [...], 8: [...], 12: [...], 20: [...]}  // 時刻別予約済み日付
        }

    Raises:
        LateAPIError: API呼び出しエラー
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

        # 時刻別の予約済み日付を抽出
        jst = ZoneInfo('Asia/Tokyo')
        reserved_by_hour = {7: set(), 8: set(), 12: set(), 20: set()}

        for post in result.get('posts', []):
            scheduled_for = post.get('scheduledFor')
            if scheduled_for:
                # ISO8601形式をパース
                dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
                dt_jst = dt.astimezone(jst)

                # 各時刻をフィルタ
                hour = dt_jst.hour
                if hour in reserved_by_hour:
                    reserved_by_hour[hour].add(dt_jst.date())

        # 互換性維持のため8am/20pmも別途設定
        reserved_8am_dates = sorted(list(reserved_by_hour[8]))
        reserved_20pm_dates = sorted(list(reserved_by_hour[20]))

        return {
            "posts": result.get('posts', []),
            "reserved_8am_dates": reserved_8am_dates,
            "reserved_20pm_dates": reserved_20pm_dates,
            "reserved_dates_by_hour": {
                hour: sorted(list(dates)) for hour, dates in reserved_by_hour.items()
            }
        }

    except requests.exceptions.Timeout:
        raise LateAPIError("タイムアウト: Late APIへの接続がタイムアウトしました")

    except requests.exceptions.ConnectionError:
        raise LateAPIError("接続エラー: Late APIに接続できませんでした")


def find_available_dates(
    count: int = 3,
    reserved_dates: Optional[List] = None,
    config_path: str = None,
    target_hour: int = 8,
    target_hours: Optional[List[int]] = None
) -> dict:
    """
    競合回避型の利用可能日付を検索

    Args:
        count: 必要な日付数（デフォルト: 3）
        reserved_dates: 予約済み日付リスト（オプション、指定なしの場合はAPIから取得）
        config_path: 設定ファイルパス
        target_hour: 競合チェック対象の時刻（8=LinkedIn用8:00 AM、20=X/Threads用20:00）
                     ※target_hoursが指定された場合は無視される
        target_hours: 複数時刻の競合チェック（例: [7, 8, 12, 20]）
                      指定した場合、すべての時刻で空いている日付のみを返す

    Returns:
        dict: {
            "available_dates": [date1, date2, date3],  // 利用可能日付リスト
            "reserved_dates": [...],                   // 指定時刻の予約済み日付
            "reserved_8am_dates": [...],               // 8:00 JST予約済み日付（互換性維持）
            "reserved_20pm_dates": [...],              // 20:00 JST予約済み日付
            "reserved_dates_by_hour": {...},           // 時刻別予約済み日付
            "existing_scheduled_count": N              // 既存予約投稿数
        }
    """
    # 予約済み日付が指定されていない場合はAPIから取得
    existing_posts = get_existing_scheduled_posts(config_path)
    reserved_dates_by_hour = existing_posts.get('reserved_dates_by_hour', {})
    reserved_8am_dates = existing_posts['reserved_8am_dates']
    reserved_20pm_dates = existing_posts['reserved_20pm_dates']
    total_scheduled = len(existing_posts['posts'])

    # 複数時刻対応
    if target_hours is not None:
        # 複数時刻指定: すべての時刻で予約がない日付を検索
        all_reserved_dates = set()
        for hour in target_hours:
            hour_reserved = reserved_dates_by_hour.get(hour, [])
            all_reserved_dates.update(hour_reserved)
        reserved_dates = list(all_reserved_dates)
    elif reserved_dates is None:
        # 単一時刻: 従来互換
        if target_hour == 8:
            reserved_dates = reserved_8am_dates
        elif target_hour == 20:
            reserved_dates = reserved_20pm_dates
        else:
            # 指定時刻がサポート外の場合は8:00 AMをデフォルトに
            reserved_dates = reserved_8am_dates

    # 利用可能日付を検索
    jst = ZoneInfo('Asia/Tokyo')
    available_dates = []
    current_date = (datetime.now(jst) + timedelta(days=1)).date()

    while len(available_dates) < count:
        if current_date not in reserved_dates:
            available_dates.append(current_date)
        current_date += timedelta(days=1)

    return {
        "available_dates": available_dates,
        "reserved_dates": reserved_dates,
        "reserved_8am_dates": reserved_8am_dates,
        "reserved_20pm_dates": reserved_20pm_dates,
        "reserved_dates_by_hour": reserved_dates_by_hour,
        "existing_scheduled_count": total_scheduled
    }


def create_posting_plan(
    variants: List[dict],
    available_dates: Optional[List] = None,
    config_path: str = None
) -> dict:
    """
    スコアベースの投稿計画を作成

    Args:
        variants: 投稿バリアント [
            {"variant": "案1", "score": 92, "content": "..."},
            {"variant": "案2", "score": 95, "content": "..."},
            {"variant": "案3", "score": 88, "content": "..."}
        ]
        available_dates: 利用可能日付リスト（オプション、指定なしの場合は自動検索）
        config_path: 設定ファイルパス

    Returns:
        dict: {
            "posting_plan": [
                {"date": "2026-01-07", "time": "08:00", "variant": "案2（95点、最推奨）"},
                {"date": "2026-01-08", "time": "08:00", "variant": "案1（92点）"},
                {"date": "2026-01-09", "time": "08:00", "variant": "案3（88点）"}
            ],
            "available_dates": [...],
            "reserved_8am_dates": [...],
            "existing_scheduled_count": N
        }
    """
    # 利用可能日付が指定されていない場合は自動検索
    if available_dates is None:
        date_info = find_available_dates(count=len(variants), config_path=config_path)
        available_dates = date_info['available_dates']
        reserved_dates = date_info['reserved_8am_dates']
        total_scheduled = date_info['existing_scheduled_count']
    else:
        reserved_dates = []
        total_scheduled = 0

    # スコア降順でソート
    sorted_variants = sorted(variants, key=lambda x: x.get('score', 0), reverse=True)

    # 投稿計画作成
    posting_plan = []
    for i, variant in enumerate(sorted_variants):
        score = variant.get('score', 0)
        variant_name = variant.get('variant', f'案{i+1}')

        # スコア表記付きバリアント名
        if i == 0:
            variant_display = f"{variant_name}（{score}点、最推奨）"
        else:
            variant_display = f"{variant_name}（{score}点）"

        posting_plan.append({
            "date": str(available_dates[i]),
            "time": "08:00",
            "variant": variant_display
        })

    return {
        "posting_plan": posting_plan,
        "available_dates": available_dates,
        "reserved_8am_dates": reserved_dates,
        "existing_scheduled_count": total_scheduled
    }


# ===========================
# コンテンツ抽出関数
# ===========================

def extract_post_content(markdown: str, variant_number: int) -> Optional[str]:
    """
    案Nの本文を抽出（タイトル重複・装飾除去版）

    Args:
        markdown: Phase 3生成されたMarkdownファイルの内容
        variant_number: バリアント番号（1, 2, 3）

    Returns:
        str: 投稿本文（タイトル重複なし、Markdown装飾なし）
        None: 抽出失敗時
    """
    import re

    # Regexパターン: 案N → タイトル → 本文 を抽出（---区切りまで）
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\n## 案|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if match:
        title = match.group(1).strip()
        body = match.group(2).strip()

        # Markdown装飾を除去（**太字**を通常テキストに変換）
        title_clean = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
        body = re.sub(r'\*\*(.+?)\*\*', r'\1', body)

        # その他のMarkdown装飾も除去
        # - 箇条書き（- item → item）
        body = re.sub(r'^\- ', '', body, flags=re.MULTILINE)

        # - 番号付きリスト（1. item → item）
        body = re.sub(r'^\d+\. ', '', body, flags=re.MULTILINE)

        # 【修正】本文1行目がタイトルと同じ場合は除去（タイトル重複防止）
        body_lines = body.split('\n')
        if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
            # 1行目（タイトル重複）を除去
            body = '\n'.join(body_lines[1:]).strip()

        # タイトルと本文を結合
        full_content = f"{title_clean}\n\n{body}"

        return full_content

    return None


# ===========================
# Phase 5: キュー管理（骨組み）
# ===========================

def create_post_queue(
    topics: List[dict],
    base_date: datetime = None
) -> dict:
    """
    Top 3トピックから投稿キュー作成

    Args:
        topics: トピックリスト [
            {"topic_id": 1, "topic_summary": "...", "post_content": "..."},
            ...
        ]
        base_date: 基準日時

    Returns:
        dict: 投稿キュー {
            "queue": [
                {
                    "topic_id": 1,
                    "topic_summary": "...",
                    "post_content": "...",
                    "schedule_date_offset": 0  // 今日
                },
                ...
            ]
        }
    """
    queue = []

    for i, topic in enumerate(topics[:3]):  # Top 3のみ
        queue_item = {
            "topic_id": topic.get("topic_id", i + 1),
            "topic_summary": topic.get("topic_summary", ""),
            "post_content": topic.get("post_content", ""),
            "schedule_date_offset": i  # 0=今日、1=明日、2=明後日
        }
        queue.append(queue_item)

    return {"queue": queue}


# ===========================
# テスト関数
# ===========================

def test_late_api_connection(config_path: str = None) -> bool:
    """
    Late API接続テスト

    Returns:
        bool: 接続成功ならTrue
    """
    try:
        config = load_config(config_path)
        api_key = config["api_key"]
        base_url = config["base_url"]

        # プロフィール取得で接続テスト
        response = requests.get(
            f"{base_url}/profiles",
            headers=get_headers(api_key),
            timeout=10
        )

        if response.status_code == 200:
            print("✅ Late API接続成功")
            return True
        else:
            print(f"❌ Late API接続失敗: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Late API接続エラー: {e}")
        return False


if __name__ == "__main__":
    # テスト実行
    print("=" * 60)
    print("Late API投稿ライブラリ - 接続テスト")
    print("=" * 60)

    test_late_api_connection()
