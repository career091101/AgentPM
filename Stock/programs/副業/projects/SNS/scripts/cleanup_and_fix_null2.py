#!/usr/bin/env python3
"""
null2投稿のクリーンアップと修正

1. 個別投稿のThreads/Twitter（12件）を削除
2. LinkedInの既存投稿を削除
3. LinkedIn（本文+First Comment統合版）を再予約
"""

import sys
import os
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    load_config,
    get_headers,
    handle_late_api_response,
    post_to_linkedin,
    get_account_id,
    LateAPIError
)
import requests


# ===========================
# 投稿一覧取得
# ===========================

def get_scheduled_posts(config_path: str = None) -> list:
    """Late APIからスケジュール済み投稿を取得"""
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        response = requests.get(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            timeout=30
        )

        result = handle_late_api_response(response)
        return result.get("posts", [])

    except Exception as e:
        print(f"❌ 投稿一覧取得エラー: {e}")
        return []


def filter_null2_posts(posts: list) -> dict:
    """
    null2関連の投稿を抽出

    Returns:
        dict: {
            "linkedin": [post],
            "threads_individual": [post1, post2, ...],
            "twitter_individual": [post1, post2, ...],
            "threads_thread": [post],
            "twitter_thread": [post]
        }
    """
    result = {
        "linkedin": [],
        "threads_individual": [],
        "twitter_individual": [],
        "threads_thread": [],
        "twitter_thread": []
    }

    for post in posts:
        # スケジュール日時が2026-01-07かチェック
        scheduled_for = post.get("scheduledFor", "")
        if not scheduled_for.startswith("2026-01-07"):
            continue

        # プラットフォーム確認
        platforms = post.get("platforms", [])
        if not platforms:
            continue

        platform = platforms[0].get("platform", "")
        platform_data = platforms[0].get("platformSpecificData", {})

        # LinkedIn（8:00）
        if platform == "linkedin" and "08:00" in scheduled_for:
            result["linkedin"].append(post)

        # Threads個別投稿（20:00-20:04）
        elif platform == "threads" and not platform_data.get("threadItems"):
            if "20:00" in scheduled_for or "20:01" in scheduled_for or "20:02" in scheduled_for or "20:03" in scheduled_for or "20:04" in scheduled_for:
                result["threads_individual"].append(post)

        # Threadsスレッド投稿（20:00）
        elif platform == "threads" and platform_data.get("threadItems"):
            result["threads_thread"].append(post)

        # Twitter個別投稿（20:05-20:11）
        elif platform == "twitter" and not platform_data.get("threadItems"):
            if "20:0" in scheduled_for or "20:1" in scheduled_for:
                result["twitter_individual"].append(post)

        # Twitterスレッド投稿（20:05）
        elif platform == "twitter" and platform_data.get("threadItems"):
            result["twitter_thread"].append(post)

    return result


# ===========================
# 投稿削除
# ===========================

def delete_post(post_id: str, config_path: str = None) -> bool:
    """Late API投稿を削除"""
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        response = requests.delete(
            f"{base_url}/posts/{post_id}",
            headers=get_headers(api_key),
            timeout=30
        )

        if response.status_code == 200 or response.status_code == 204:
            return True
        else:
            print(f"   削除失敗: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"   削除エラー: {e}")
        return False


# ===========================
# LinkedIn統合版投稿
# ===========================

LINKEDIN_INTEGRATED_POST = """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏がプロデュースする「null2」。そのコンセプトが、今の経営者に問いかけている。

「AIによって文明ってのは多分すぐ変わっちゃうんですよ。夜寝て起きたら世界変わってるかもしんないです」

「それでも別に人生は続いちゃうじゃないですか。だから別に意味なんて探さなくても文明は変わっても人生は続くよ」

この言葉に、私は衝撃を受けた。

つまり、文明の変化に意味を求めすぎると、人生が見えなくなる。

AI導入を考えている経営者は多い。ChatGPT、Claude、Gemini。毎月のように新しいモデルがリリースされ、毎週のように新機能が追加される。

「AIが何をもたらすのか」「どんな意味があるのか」。こういう問いに答えを求め続ける。

この課題は、あなたの業界でも起きているはずだ。

GPT-4から半年でClaude 3。さらに3ヶ月でGemini 1.5 Pro。技術は進化し続ける。

でも、それでどうなるのか。何が変わるのか。意味を探し始めると、答えは見つからない。

ポイントは、「意味を探さない」という新しい生き方だ。

文明は急速に変わる。AIが仕事を奪う、AIが社会を変える、AIが世界を支配する。こういう議論は尽きない。

でも、人生は続く。毎朝起きて、仕事をして、家族と過ごす。この営みは変わらない。

落合陽一氏の「null2」が示すのは、文明と人生の分離だ。

文明は変わる。でも、人生は続く。この2つは別々に存在する。

3ヶ月に1度、AIの世界が変わる。文明は進化し続ける。

でも、私たちの人生も続く。

あなたの会社では、文明の変化に「意味」を求め続けますか？それとも、ただ人生を続けますか？

━━━

【詳報・出典】

• 落合陽一氏プロデュース「null2（空²）」
• 「かしこさはただのおまけ」: AIが記号処理を担う未来での人間観
• 般若心経「色即是空 空即是色」: null2の命名の由来
• 意味からの解放: ニヒリズムの克服としての新しい人間観

【参考ソース】
• null2公式サイト: https://expo2025.digitalnatureandarts.or.jp/
• 落合陽一note「null²の解読」: https://note.com/ochyai/n/neccaac02bf60
• 考察note「もう人間には意味も物語も必要ない」: https://note.com/hasimoto5555/n/nbd675dd41209
• WIRED「null2解題」: https://wired.jp/article/ochiai-yoichi-null2-novacene/

【私見】

「考える力」は人間のアイデンティティではなく、「ちょっとしたおまけ」だったという視点の転換は、AI時代の経営者にとって最も重要な気づきです。

私自身、これまで「戦略立案」「市場分析」「競合調査」といった「考える仕事」に価値を置いてきました。でも、null2が示すように、それは「おまけ」だった。

AI時代の経営者の本質的な役割は、「遊び、感じ、漂う」ことにあるのかもしれません。

これはニヒリズムではなく、意味への執着からの解放です。般若心経が1300年前から教えてきた「空」の哲学が、AIという現代技術と融合し、新しい人間観を提示しています。

null2の「空²」——二重の空虚——は、意味の空虚を受け入れること自体が自由を与え、より軽やかに生命を祝福できる、ということを教えてくれます。

あなたは、「かしこさ」を手放す勇気がありますか？"""


# ===========================
# メイン処理
# ===========================

def main():
    print("=" * 70)
    print("null2投稿のクリーンアップと修正")
    print("=" * 70)
    print()

    # 1. 現在の予約投稿を取得
    print("1. スケジュール済み投稿を取得中...")
    all_posts = get_scheduled_posts()
    null2_posts = filter_null2_posts(all_posts)

    print(f"   LinkedIn: {len(null2_posts['linkedin'])}件")
    print(f"   Threads個別: {len(null2_posts['threads_individual'])}件")
    print(f"   Threadsスレッド: {len(null2_posts['threads_thread'])}件")
    print(f"   Twitter個別: {len(null2_posts['twitter_individual'])}件")
    print(f"   Twitterスレッド: {len(null2_posts['twitter_thread'])}件")
    print()

    # 2. 削除対象を表示
    print("2. 削除対象の投稿:")
    print()

    delete_targets = []

    # LinkedIn既存投稿
    for post in null2_posts['linkedin']:
        post_id = post.get("_id")
        scheduled_for = post.get("scheduledFor", "")
        delete_targets.append(("LinkedIn", post_id, scheduled_for))
        print(f"   - LinkedIn: {scheduled_for} (ID: {post_id})")

    # Threads個別投稿
    for post in null2_posts['threads_individual']:
        post_id = post.get("_id")
        scheduled_for = post.get("scheduledFor", "")
        delete_targets.append(("Threads個別", post_id, scheduled_for))
        print(f"   - Threads個別: {scheduled_for} (ID: {post_id})")

    # Twitter個別投稿
    for post in null2_posts['twitter_individual']:
        post_id = post.get("_id")
        scheduled_for = post.get("scheduledFor", "")
        delete_targets.append(("Twitter個別", post_id, scheduled_for))
        print(f"   - Twitter個別: {scheduled_for} (ID: {post_id})")

    print()
    print(f"   合計: {len(delete_targets)}件")
    print()

    # 3. 削除実行
    if delete_targets:
        print("3. 削除実行中...")
        deleted_count = 0

        for platform, post_id, scheduled_for in delete_targets:
            print(f"   削除中: {platform} - {scheduled_for}")
            if delete_post(post_id):
                print(f"   ✅ 削除成功")
                deleted_count += 1
            else:
                print(f"   ❌ 削除失敗")

        print()
        print(f"   削除完了: {deleted_count}/{len(delete_targets)}件")
        print()
    else:
        print("3. 削除対象がありません")
        print()

    # 4. LinkedIn統合版を再予約
    print("4. LinkedIn統合版（本文+First Comment）を予約中...")
    print()

    try:
        linkedin_account_id = get_account_id("linkedin")
        result = post_to_linkedin(
            content=LINKEDIN_INTEGRATED_POST,
            account_id=linkedin_account_id,
            scheduled_for="2026-01-07T08:00:00+09:00"
        )

        print("✅ LinkedIn統合版予約成功")
        print(f"   投稿ID: {result.get('_id', 'N/A')}")
        print(f"   スケジュール: 2026-01-07T08:00:00+09:00")
        print(f"   文字数: {len(LINKEDIN_INTEGRATED_POST)}字")
        print()

    except LateAPIError as e:
        print(f"❌ LinkedIn統合版予約エラー: {e}")
        print()

    # 5. 最終確認
    print("=" * 70)
    print("最終確認")
    print("=" * 70)
    print()

    final_posts = get_scheduled_posts()
    final_null2_posts = filter_null2_posts(final_posts)

    print("現在のスケジュール:")
    print(f"   LinkedIn: {len(final_null2_posts['linkedin'])}件")
    print(f"   Threadsスレッド: {len(final_null2_posts['threads_thread'])}件")
    print(f"   Twitterスレッド: {len(final_null2_posts['twitter_thread'])}件")
    print(f"   Threads個別（削除対象）: {len(final_null2_posts['threads_individual'])}件")
    print(f"   Twitter個別（削除対象）: {len(final_null2_posts['twitter_individual'])}件")
    print()

    if (len(final_null2_posts['linkedin']) == 1 and
        len(final_null2_posts['threads_thread']) == 1 and
        len(final_null2_posts['twitter_thread']) == 1 and
        len(final_null2_posts['threads_individual']) == 0 and
        len(final_null2_posts['twitter_individual']) == 0):
        print("✅ すべて正常です！")
        print()
        print("最終スケジュール:")
        print("   08:00 - LinkedIn（本文+First Comment統合版）")
        print("   20:00 - Threadsスレッド（5投稿）")
        print("   20:05 - Twitterスレッド（7ツイート）")
    else:
        print("⚠️  スケジュールに問題がある可能性があります")
        print("   Late APIダッシュボードで確認してください")

    print()


if __name__ == "__main__":
    main()
