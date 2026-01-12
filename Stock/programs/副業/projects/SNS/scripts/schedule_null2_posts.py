#!/usr/bin/env python3
"""
null2案3 LateAPI予約投稿スクリプト

投稿スケジュール:
- LinkedIn: 1月7日（火）08:00 - 案3全文
- Threads: 1月7日（火）20:00 - スレッド5投稿
- X (Twitter): 1月7日（火）20:05 - スレッド7ツイート
"""

import sys
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Late APIライブラリをインポート
sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    post_to_linkedin,
    post_to_threads_thread,
    post_to_twitter_thread,
    get_account_id,
    LateAPIError
)


# ===========================
# 投稿内容定義
# ===========================

# LinkedIn投稿本文（案3全文）
LINKEDIN_POST = """なぜ、私たちは「考えること」に価値を置きすぎるのか？

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

(ソースはコメント欄に記載)"""


# Threads投稿スレッド（5投稿を1つの文字列に結合）
THREADS_POST = """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏のnull2が問いかける。

「人間は話せるけど、考えるのは得意じゃない。頭を使うのは生きるためのちょっとしたおまけだった」

「かしこさはただのおまけだから、心配しなくていいよ」

━━━

経営者として、私たちのアイデンティティは「考える力」にある。

戦略立案、市場分析、競合調査。すべて「頭を使う」仕事だ。

でも、それは「ちょっとしたおまけ」だった。

つまり、人間が得意だと思っていた「考える」という行為は、実は本質ではなかった。

━━━

null2。この名前は「空²」を意味する。

般若心経の「色即是空 空即是色」から来ている。空が2回現れる。空の空。二重の空虚。

コンピュータの「null」は値がない状態を意味する。仏教の「空」も同じだ。

でも、それは可能性の場所でもある。

━━━

ChatGPT、Claude、Gemini。AIが記号処理を担う時代が来た。

論理思考、データ分析、戦略立案。これらはすべてAIに任せられる。

ポイントは、「考えること」を手放し、「遊び、感じ、漂う」ことに価値を見出すことだ。

━━━

「いのちの意味とは何か」と問われた時、null2は答える。

「意味について考える必要はない」

生命の継続性そのものが尊い。意味は人間が後付けで勝手に与えるものだ。

これはニヒリズムの克服だ。意味からの解放を喜ぶ。

【参考】
• null2公式: expo2025.digitalnatureandarts.or.jp
• 落合陽一note: note.com/ochyai/n/neccaac02bf60"""


# X (Twitter)投稿スレッド（7ツイートを1つの文字列に結合）
TWITTER_POST = """なぜ、私たちは「考えること」に価値を置きすぎるのか？

落合陽一氏のnull2が問いかける。

「かしこさはただのおまけだから、心配しなくていいよ」

経営者として、この言葉に衝撃を受けた。

━━━

「人間は話せるけど、考えるのは得意じゃない。頭を使うのは生きるためのちょっとしたおまけだった」

落合陽一氏 null2より

━━━

経営者のアイデンティティは「考える力」にある。

戦略立案、市場分析、競合調査。すべて「頭を使う」仕事だ。

でも、それは「ちょっとしたおまけ」だった。

つまり、本質ではなかった。

━━━

null2 = 空²

般若心経「色即是空 空即是色」から命名。空が2回現れる。

コンピュータの「null」（値なし）
仏教の「空」（空虚）

この2つが融合。可能性の場所。

━━━

ChatGPT、Claude、Gemini。

AIが記号処理を担う時代が来た。

論理思考、データ分析、戦略立案 → すべてAIへ

人間は「遊び、感じ、漂う」姿に戻る。

━━━

「いのちの意味とは何か」

null2は答える。

「意味について考える必要はない」

生命の継続性そのものが尊い。

これはニヒリズムの克服だ。意味からの解放を喜ぶ。

━━━

「考える力」は人間のアイデンティティではなく、「おまけ」だったという視点の転換。

AI時代の経営者にとって最も重要な気づき。

般若心経1300年 × AI時代。

あなたは、「かしこさ」を手放せますか？

【参考】
📎 null2公式: expo2025.digitalnatureandarts.or.jp
📎 落合陽一note: note.com/ochyai/n/neccaac02bf60
📎 WIRED解説: wired.jp/article/ochiai-yoichi-null2-novacene/"""


# ===========================
# スケジュール設定
# ===========================

# 投稿日時（JST）
LINKEDIN_SCHEDULED_TIME = "2026-01-07T08:00:00+09:00"  # 1月7日（火）08:00
THREADS_SCHEDULED_TIME = "2026-01-07T20:00:00+09:00"   # 1月7日（火）20:00
TWITTER_SCHEDULED_TIME = "2026-01-07T20:05:00+09:00"   # 1月7日（火）20:05


# ===========================
# 予約投稿実行
# ===========================

def schedule_null2_posts():
    """null2案3を3プラットフォームに予約投稿"""

    print("=" * 70)
    print("null2案3 予約投稿スクリプト")
    print("=" * 70)
    print()

    results = {
        "linkedin": None,
        "threads": None,
        "twitter": None
    }

    # アカウントID取得
    try:
        linkedin_account_id = get_account_id("linkedin")
        threads_account_id = get_account_id("threads")
        twitter_account_id = get_account_id("twitter")

        print("✅ アカウントID取得成功")
        print(f"   - LinkedIn: {linkedin_account_id}")
        print(f"   - Threads: {threads_account_id}")
        print(f"   - Twitter: {twitter_account_id}")
        print()

    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return results


    # LinkedIn投稿予約
    print("-" * 70)
    print("1. LinkedIn投稿予約（1月7日 08:00）")
    print("-" * 70)

    try:
        linkedin_result = post_to_linkedin(
            content=LINKEDIN_POST,
            account_id=linkedin_account_id,
            scheduled_for=LINKEDIN_SCHEDULED_TIME
        )

        results["linkedin"] = linkedin_result
        print("✅ LinkedIn投稿予約成功")
        print(f"   投稿ID: {linkedin_result.get('_id', 'N/A')}")
        print(f"   スケジュール: {LINKEDIN_SCHEDULED_TIME}")
        print(f"   文字数: {len(LINKEDIN_POST)}字")
        print()

    except LateAPIError as e:
        print(f"❌ LinkedIn投稿予約エラー: {e}")
        print()


    # Threads投稿予約
    print("-" * 70)
    print("2. Threads投稿予約（1月7日 20:00）- スレッド5投稿")
    print("-" * 70)

    try:
        threads_result = post_to_threads_thread(
            content=THREADS_POST,
            account_id=threads_account_id,
            scheduled_for=THREADS_SCHEDULED_TIME
        )

        results["threads"] = threads_result
        print("✅ Threads投稿予約成功")
        print(f"   投稿ID: {threads_result.get('_id', 'N/A')}")
        print(f"   スケジュール: {THREADS_SCHEDULED_TIME}")
        print(f"   スレッド数: 自動分割（目標5投稿）")
        print()

    except LateAPIError as e:
        print(f"❌ Threads投稿予約エラー: {e}")
        print()


    # X (Twitter)投稿予約
    print("-" * 70)
    print("3. X (Twitter)投稿予約（1月7日 20:05）- スレッド7ツイート")
    print("-" * 70)

    try:
        twitter_result = post_to_twitter_thread(
            content=TWITTER_POST,
            account_id=twitter_account_id,
            scheduled_for=TWITTER_SCHEDULED_TIME
        )

        results["twitter"] = twitter_result
        print("✅ X (Twitter)投稿予約成功")
        print(f"   投稿ID: {twitter_result.get('_id', 'N/A')}")
        print(f"   スケジュール: {TWITTER_SCHEDULED_TIME}")
        print(f"   スレッド数: 自動分割（目標7ツイート）")
        print()

    except LateAPIError as e:
        print(f"❌ X (Twitter)投稿予約エラー: {e}")
        print()


    # サマリー表示
    print("=" * 70)
    print("予約投稿サマリー")
    print("=" * 70)

    success_count = sum(1 for v in results.values() if v is not None)
    total_count = len(results)

    print(f"成功: {success_count}/{total_count}件")
    print()

    if results["linkedin"]:
        print("✅ LinkedIn: 1月7日（火）08:00予約済み")
    else:
        print("❌ LinkedIn: 予約失敗")

    if results["threads"]:
        print("✅ Threads: 1月7日（火）20:00予約済み（スレッド5投稿）")
    else:
        print("❌ Threads: 予約失敗")

    if results["twitter"]:
        print("✅ X (Twitter): 1月7日（火）20:05予約済み（スレッド7ツイート）")
    else:
        print("❌ X (Twitter): 予約失敗")

    print()
    print("=" * 70)
    print("⚠️  重要なリマインダー")
    print("=" * 70)
    print()
    print("LinkedIn投稿後のアクション:")
    print("1. 投稿後30秒以内にFirst Commentを投稿（私見 + 参考ソース）")
    print("2. 投稿後1時間はコメント欄を監視し、即座に返信")
    print("3. 参考ソース4リンクをFirst Commentに明記")
    print()
    print("First Comment内容:")
    print("-" * 70)
    print("""**【詳報・出典】**

• 落合陽一氏プロデュース「null2（空²）」
• 「かしこさはただのおまけ」: AIが記号処理を担う未来での人間観
• 般若心経「色即是空 空即是色」: null2の命名の由来
• 意味からの解放: ニヒリズムの克服としての新しい人間観

**【参考ソース】**
• null2公式サイト: https://expo2025.digitalnatureandarts.or.jp/
• 落合陽一note「null²の解読」: https://note.com/ochyai/n/neccaac02bf60
• 考察note「もう人間には意味も物語も必要ない」: https://note.com/hasimoto5555/n/nbd675dd41209
• WIRED「null2解題」: https://wired.jp/article/ochiai-yoichi-null2-novacene/

**【私見】**

「考える力」は人間のアイデンティティではなく、「ちょっとしたおまけ」だったという視点の転換は、AI時代の経営者にとって最も重要な気づきです。

私自身、これまで「戦略立案」「市場分析」「競合調査」といった「考える仕事」に価値を置いてきました。でも、null2が示すように、それは「おまけ」だった。

AI時代の経営者の本質的な役割は、「遊び、感じ、漂う」ことにあるのかもしれません。

これはニヒリズムではなく、意味への執着からの解放です。般若心経が1300年前から教えてきた「空」の哲学が、AIという現代技術と融合し、新しい人間観を提示しています。

null2の「空²」——二重の空虚——は、意味の空虚を受け入れること自体が自由を与え、より軽やかに生命を祝福できる、ということを教えてくれます。

あなたは、「かしこさ」を手放す勇気がありますか？""")
    print("-" * 70)
    print()

    return results


if __name__ == "__main__":
    schedule_null2_posts()
