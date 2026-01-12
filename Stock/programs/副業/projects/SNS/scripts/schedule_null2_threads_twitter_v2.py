#!/usr/bin/env python3
"""
null2案3 Threads & Twitter スレッド予約投稿（修正版）

ThreadsとTwitterをスレッドとして投稿します。
contentフィールドも含めることでLate APIのエラーを回避します。
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    get_account_id,
    load_config,
    get_headers,
    handle_late_api_response,
    LateAPIError
)
import requests


# ===========================
# Threads投稿スレッド（5投稿）
# ===========================

THREADS_POSTS = [
    # 投稿1
    """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏のnull2が問いかける。

「人間は話せるけど、考えるのは得意じゃない。頭を使うのは生きるためのちょっとしたおまけだった」

「かしこさはただのおまけだから、心配しなくていいよ」""",

    # 投稿2
    """経営者として、私たちのアイデンティティは「考える力」にある。

戦略立案、市場分析、競合調査。すべて「頭を使う」仕事だ。

でも、それは「ちょっとしたおまけ」だった。

つまり、人間が得意だと思っていた「考える」という行為は、実は本質ではなかった。""",

    # 投稿3
    """null2。この名前は「空²」を意味する。

般若心経の「色即是空 空即是色」から来ている。空が2回現れる。空の空。二重の空虚。

コンピュータの「null」は値がない状態を意味する。仏教の「空」も同じだ。

でも、それは可能性の場所でもある。""",

    # 投稿4
    """ChatGPT、Claude、Gemini。AIが記号処理を担う時代が来た。

論理思考、データ分析、戦略立案。これらはすべてAIに任せられる。

ポイントは、「考えること」を手放し、「遊び、感じ、漂う」ことに価値を見出すことだ。""",

    # 投稿5
    """「いのちの意味とは何か」と問われた時、null2は答える。

「意味について考える必要はない」

生命の継続性そのものが尊い。意味は人間が後付けで勝手に与えるものだ。

これはニヒリズムの克服だ。意味からの解放を喜ぶ。

【参考】
• null2公式: expo2025.digitalnatureandarts.or.jp
• 落合陽一note: note.com/ochyai/n/neccaac02bf60"""
]


# ===========================
# X (Twitter)投稿スレッド（7ツイート）
# ===========================

TWITTER_POSTS = [
    # ツイート1
    """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏のnull2が問いかける。

「かしこさはただのおまけだから、心配しなくていいよ」

経営者として、この言葉に衝撃を受けた。""",

    # ツイート2
    """「人間は話せるけど、考えるのは得意じゃない。頭を使うのは生きるためのちょっとしたおまけだった」

落合陽一氏 null2より""",

    # ツイート3
    """経営者のアイデンティティは「考える力」にある。

戦略立案、市場分析、競合調査。すべて「頭を使う」仕事だ。

でも、それは「ちょっとしたおまけ」だった。

つまり、本質ではなかった。""",

    # ツイート4
    """null2 = 空²

般若心経「色即是空 空即是色」から命名。空が2回現れる。

コンピュータの「null」（値なし）
仏教の「空」（空虚）

この2つが融合。可能性の場所。""",

    # ツイート5
    """ChatGPT、Claude、Gemini。

AIが記号処理を担う時代が来た。

論理思考、データ分析、戦略立案 → すべてAIへ

人間は「遊び、感じ、漂う」姿に戻る。""",

    # ツイート6
    """「いのちの意味とは何か」

null2は答える。

「意味について考える必要はない」

生命の継続性そのものが尊い。

これはニヒリズムの克服だ。意味からの解放を喜ぶ。""",

    # ツイート7
    """「考える力」は人間のアイデンティティではなく、「おまけ」だったという視点の転換。

AI時代の経営者にとって最も重要な気づき。

般若心経1300年 × AI時代。

あなたは、「かしこさ」を手放せますか？

【参考】
📎 null2公式: expo2025.digitalnatureandarts.or.jp
📎 落合陽一note: note.com/ochyai/n/neccaac02bf60
📎 WIRED解説: wired.jp/article/ochiai-yoichi-null2-novacene/"""
]


# ===========================
# スケジュール設定
# ===========================

THREADS_SCHEDULED_TIME = "2026-01-07T20:00:00+09:00"  # 1月7日（火）20:00
TWITTER_SCHEDULED_TIME = "2026-01-07T20:05:00+09:00"  # 1月7日（火）20:05


# ===========================
# スレッド投稿関数（修正版）
# ===========================

def post_thread_with_content(
    posts: list,
    platform: str,
    account_id: str,
    scheduled_for: str,
    config_path: str = None
) -> dict:
    """
    スレッド投稿（contentフィールドも含める）

    Args:
        posts: 投稿リスト
        platform: プラットフォーム（twitter or threads）
        account_id: アカウントID
        scheduled_for: 予約時刻
        config_path: 設定ファイルパス

    Returns:
        dict: Late APIレスポンス
    """
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    # threadItems形式に変換
    thread_items_data = [{"content": post} for post in posts]

    # リクエストボディ構築
    request_body = {
        "content": posts[0],  # 最初の投稿をcontentに設定
        "platforms": [
            {
                "platform": platform,
                "accountId": account_id,
                "platformSpecificData": {
                    "threadItems": thread_items_data
                }
            }
        ],
        "scheduledFor": scheduled_for,
        "timezone": "Asia/Tokyo"
    }

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


# ===========================
# 予約投稿実行
# ===========================

def schedule_threads_thread():
    """Threads スレッド投稿を予約"""

    print("=" * 70)
    print("Threads スレッド投稿予約（1月7日 20:00）- 5投稿スレッド")
    print("=" * 70)
    print()

    try:
        threads_account_id = get_account_id("threads")
        print(f"✅ ThreadsアカウントID: {threads_account_id}")
        print()
    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return None

    try:
        result = post_thread_with_content(
            posts=THREADS_POSTS,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=THREADS_SCHEDULED_TIME
        )

        print("✅ Threadsスレッド投稿予約成功")
        print(f"   投稿ID: {result.get('_id', 'N/A')}")
        print(f"   スケジュール: {THREADS_SCHEDULED_TIME}")
        print(f"   スレッド数: 5投稿")
        print()

        return result

    except LateAPIError as e:
        print(f"❌ Threadsスレッド投稿予約エラー: {e}")
        print()
        return None


def schedule_twitter_thread():
    """X (Twitter) スレッド投稿を予約"""

    print("=" * 70)
    print("X (Twitter) スレッド投稿予約（1月7日 20:05）- 7ツイートスレッド")
    print("=" * 70)
    print()

    try:
        twitter_account_id = get_account_id("twitter")
        print(f"✅ TwitterアカウントID: {twitter_account_id}")
        print()
    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return None

    try:
        result = post_thread_with_content(
            posts=TWITTER_POSTS,
            platform="twitter",
            account_id=twitter_account_id,
            scheduled_for=TWITTER_SCHEDULED_TIME
        )

        print("✅ X (Twitter)スレッド投稿予約成功")
        print(f"   投稿ID: {result.get('_id', 'N/A')}")
        print(f"   スケジュール: {TWITTER_SCHEDULED_TIME}")
        print(f"   スレッド数: 7ツイート")
        print()

        return result

    except LateAPIError as e:
        print(f"❌ X (Twitter)スレッド投稿予約エラー: {e}")
        print()
        return None


if __name__ == "__main__":
    # Threads投稿予約
    threads_result = schedule_threads_thread()

    # Twitter投稿予約
    twitter_result = schedule_twitter_thread()

    # 最終サマリー
    print()
    print("=" * 70)
    print("最終サマリー")
    print("=" * 70)

    if threads_result:
        print("✅ Threads: スレッド投稿予約成功（5投稿）")
    else:
        print("❌ Threads: スレッド投稿予約失敗")

    if twitter_result:
        print("✅ X (Twitter): スレッド投稿予約成功（7ツイート）")
    else:
        print("❌ X (Twitter): スレッド投稿予約失敗")

    print()
