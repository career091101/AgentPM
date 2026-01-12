#!/usr/bin/env python3
"""
null2投稿の最終修正

1. Twitter個別投稿（7件）を削除
2. Threads個別投稿（2件）を削除
3. Threadsスレッド投稿を追加
4. LinkedIn統合版を追加
"""

import sys
import os

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
# 削除対象ID（Late APIから取得した実際のID）
# ===========================

DELETE_IDS = [
    # Twitter個別投稿（7件）
    "695864bf38609c72a1d86f08",  # 投稿1
    "695864bd38609c72a1d86ef0",  # 投稿2
    "695864ba38609c72a1d86ed8",  # 投稿3
    "695864b838609c72a1d86ea9",  # 投稿4
    "695864b538609c72a1d86e7a",  # 投稿5
    "695864b338609c72a1d86e62",  # 投稿6
    "695864b138609c72a1d86e49",  # 投稿8（重複）
    # Threads個別投稿（2件）
    "695864af38609c72a1d86e29",  # 投稿9
    "695864ac38609c72a1d86df7",  # 投稿10
]


# ===========================
# Threads投稿スレッド（5投稿）
# ===========================

THREADS_POSTS = [
    """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏のnull2が問いかける。

「人間は話せるけど、考えるのは得意じゃない。頭を使うのは生きるためのちょっとしたおまけだった」

「かしこさはただのおまけだから、心配しなくていいよ」""",

    """経営者として、私たちのアイデンティティは「考える力」にある。

戦略立案、市場分析、競合調査。すべて「頭を使う」仕事だ。

でも、それは「ちょっとしたおまけ」だった。

つまり、人間が得意だと思っていた「考える」という行為は、実は本質ではなかった。""",

    """null2。この名前は「空²」を意味する。

般若心経の「色即是空 空即是色」から来ている。空が2回現れる。空の空。二重の空虚。

コンピュータの「null」は値がない状態を意味する。仏教の「空」も同じだ。

でも、それは可能性の場所でもある。""",

    """ChatGPT、Claude、Gemini。AIが記号処理を担う時代が来た。

論理思考、データ分析、戦略立案。これらはすべてAIに任せられる。

ポイントは、「考えること」を手放し、「遊び、感じ、漂う」ことに価値を見出すことだ。""",

    """「いのちの意味とは何か」と問われた時、null2は答える。

「意味について考える必要はない」

生命の継続性そのものが尊い。意味は人間が後付けで勝手に与えるものだ。

これはニヒリズムの克服だ。意味からの解放を喜ぶ。

【参考】
• null2公式: expo2025.digitalnatureandarts.or.jp
• 落合陽一note: note.com/ochyai/n/neccaac02bf60"""
]


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
            print(f"      ❌ 削除失敗: {response.status_code}")
            return False

    except Exception as e:
        print(f"      ❌ 削除エラー: {e}")
        return False


# ===========================
# スレッド投稿（修正版）
# ===========================

def post_thread_with_content(
    posts: list,
    platform: str,
    account_id: str,
    scheduled_for: str,
    config_path: str = None
) -> dict:
    """スレッド投稿"""
    config = load_config(config_path)
    api_key = config["api_key"]
    base_url = config["base_url"]

    thread_items_data = [{"content": post} for post in posts]

    request_body = {
        "content": posts[0],
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

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body,
            timeout=30
        )

        return handle_late_api_response(response)

    except Exception as e:
        raise LateAPIError(f"投稿エラー: {e}")


# ===========================
# メイン処理
# ===========================

def main():
    print("=" * 70)
    print("null2投稿の最終修正")
    print("=" * 70)
    print()

    # 1. 個別投稿を削除
    print("1. 個別投稿を削除中...")
    print(f"   削除対象: {len(DELETE_IDS)}件")
    print()

    deleted_count = 0
    for post_id in DELETE_IDS:
        print(f"   削除中: {post_id}")
        if delete_post(post_id):
            print(f"      ✅ 削除成功")
            deleted_count += 1

    print()
    print(f"   削除完了: {deleted_count}/{len(DELETE_IDS)}件")
    print()

    # 2. Threadsスレッド投稿を追加
    print("2. Threadsスレッド投稿を追加中...")
    print()

    try:
        threads_account_id = get_account_id("threads")
        result = post_thread_with_content(
            posts=THREADS_POSTS,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for="2026-01-07T20:00:00+09:00"
        )

        print("   ✅ Threadsスレッド投稿成功")
        print(f"      投稿ID: {result.get('_id', 'N/A')}")
        print(f"      スレッド数: 5投稿")
        print()

    except LateAPIError as e:
        print(f"   ❌ Threadsスレッド投稿エラー: {e}")
        print()

    # 3. LinkedIn統合版を追加
    print("3. LinkedIn統合版（本文+First Comment）を追加中...")
    print()

    try:
        linkedin_account_id = get_account_id("linkedin")
        result = post_to_linkedin(
            content=LINKEDIN_INTEGRATED_POST,
            account_id=linkedin_account_id,
            scheduled_for="2026-01-07T08:00:00+09:00"
        )

        print("   ✅ LinkedIn統合版投稿成功")
        print(f"      投稿ID: {result.get('_id', 'N/A')}")
        print(f"      文字数: {len(LINKEDIN_INTEGRATED_POST)}字")
        print()

    except LateAPIError as e:
        print(f"   ❌ LinkedIn統合版投稿エラー: {e}")
        print()

    # 4. 最終確認
    print("=" * 70)
    print("修正完了")
    print("=" * 70)
    print()
    print("最終スケジュール:")
    print("   08:00 JST - LinkedIn（本文+First Comment統合版）")
    print("   20:00 JST - Threadsスレッド（5投稿）")
    print("   20:05 JST - Twitterスレッド（7ツイート）")
    print()
    print("⚠️  Late APIダッシュボードで最終確認してください")
    print()


if __name__ == "__main__":
    main()
