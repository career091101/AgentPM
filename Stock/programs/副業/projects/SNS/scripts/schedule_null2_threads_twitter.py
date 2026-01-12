#!/usr/bin/env python3
"""
null2案3 Threads & Twitter 手動スレッド予約投稿

ThreadsとTwitterは、Late APIのスレッド機能が不安定なため、
各投稿を個別に予約します。
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    post_to_late_api,
    get_account_id,
    LateAPIError
)


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

THREADS_BASE_TIME = "2026-01-07T20:00:00+09:00"  # 1月7日（火）20:00
TWITTER_BASE_TIME = "2026-01-07T20:05:00+09:00"  # 1月7日（火）20:05


# ===========================
# 予約投稿実行
# ===========================

def schedule_threads_posts():
    """Threads 5投稿を個別に予約"""

    print("=" * 70)
    print("Threads投稿予約（1月7日 20:00-20:04）- 5投稿")
    print("=" * 70)
    print()

    try:
        threads_account_id = get_account_id("threads")
        print(f"✅ Threadsアカウ��トID: {threads_account_id}")
        print()
    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return

    results = []

    for i, post_content in enumerate(THREADS_POSTS, 1):
        print(f"投稿{i}/5 を予約中...")

        # 1分間隔でスケジューリング
        from datetime import datetime, timedelta
        from zoneinfo import ZoneInfo

        base_dt = datetime.fromisoformat(THREADS_BASE_TIME.replace('+09:00', ''))
        base_dt = base_dt.replace(tzinfo=ZoneInfo('Asia/Tokyo'))
        scheduled_dt = base_dt + timedelta(minutes=i-1)
        scheduled_time = scheduled_dt.isoformat()

        try:
            result = post_to_late_api(
                content=post_content,
                platform="threads",
                account_id=threads_account_id,
                scheduled_for=scheduled_time
            )

            results.append(result)
            print(f"   ✅ 成功 - {scheduled_time}")
            print(f"   文字数: {len(post_content)}字")
            print()

        except LateAPIError as e:
            print(f"   ❌ 失敗: {e}")
            print()

    print("=" * 70)
    print(f"Threads投稿予約完了: {len(results)}/5件成功")
    print("=" * 70)
    print()

    return results


def schedule_twitter_posts():
    """Twitter 7投稿を個別に予約"""

    print("=" * 70)
    print("X (Twitter)投稿予約（1月7日 20:05-20:11）- 7ツイート")
    print("=" * 70)
    print()

    try:
        twitter_account_id = get_account_id("twitter")
        print(f"✅ TwitterアカウントID: {twitter_account_id}")
        print()
    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return

    results = []

    for i, post_content in enumerate(TWITTER_POSTS, 1):
        print(f"ツイート{i}/7 を予約中...")

        # 1分間隔でスケジューリング
        from datetime import datetime, timedelta
        from zoneinfo import ZoneInfo

        base_dt = datetime.fromisoformat(TWITTER_BASE_TIME.replace('+09:00', ''))
        base_dt = base_dt.replace(tzinfo=ZoneInfo('Asia/Tokyo'))
        scheduled_dt = base_dt + timedelta(minutes=i-1)
        scheduled_time = scheduled_dt.isoformat()

        try:
            result = post_to_late_api(
                content=post_content,
                platform="twitter",
                account_id=twitter_account_id,
                scheduled_for=scheduled_time
            )

            results.append(result)
            print(f"   ✅ 成功 - {scheduled_time}")
            print(f"   文字数: {len(post_content)}字")
            print()

        except LateAPIError as e:
            print(f"   ❌ 失敗: {e}")
            print()

    print("=" * 70)
    print(f"X (Twitter)投稿予約完了: {len(results)}/7件成功")
    print("=" * 70)
    print()

    return results


if __name__ == "__main__":
    # Threads投稿予約
    threads_results = schedule_threads_posts()

    # Twitter投稿予約
    twitter_results = schedule_twitter_posts()

    # 最終サマリー
    print()
    print("=" * 70)
    print("最終サマリー")
    print("=" * 70)
    print(f"Threads: {len(threads_results) if threads_results else 0}/5件成功")
    print(f"Twitter: {len(twitter_results) if twitter_results else 0}/7件成功")
    print()
