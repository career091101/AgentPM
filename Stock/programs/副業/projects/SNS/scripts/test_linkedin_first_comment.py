#!/usr/bin/env python3
"""
Late API LinkedIn First Comment テスト
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from late_api_post import (
    load_config,
    get_headers,
    handle_late_api_response,
    get_account_id,
    LateAPIError
)
import requests


# テスト用本文（案3）
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


# First Comment
FIRST_COMMENT = """**【詳報・出典】**

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

あなたは、「かしこさ」を手放す勇気がありますか？"""


def test_linkedin_with_first_comment():
    """LinkedIn投稿 + First Commentのテスト"""
    print("=" * 70)
    print("LinkedIn First Comment テスト")
    print("=" * 70)
    print()

    config = load_config()
    api_key = config["api_key"]
    base_url = config["base_url"]

    try:
        linkedin_account_id = get_account_id("linkedin")
        print(f"✅ LinkedInアカウントID: {linkedin_account_id}")
        print()
    except Exception as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return

    # パターン1: platformSpecificData.firstComment
    print("パターン1: platformSpecificData.firstComment を試行")
    print()

    request_body_1 = {
        "content": LINKEDIN_POST,
        "platforms": [
            {
                "platform": "linkedin",
                "accountId": linkedin_account_id,
                "platformSpecificData": {
                    "firstComment": FIRST_COMMENT
                }
            }
        ],
        "scheduledFor": "2026-01-07T08:00:00+09:00",
        "timezone": "Asia/Tokyo"
    }

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body_1,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:300]}")
        print()

        if response.status_code == 200 or response.status_code == 201:
            result = response.json()
            print("   ✅ パターン1成功！")
            print(f"   投稿ID: {result.get('_id', 'N/A')}")
            print()
            print("   Late APIはFirst Commentをサポートしています")
            print("   platformSpecificData.firstComment を使用してください")
            return True
        else:
            print("   ❌ パターン1失敗")

    except Exception as e:
        print(f"   ❌ パターン1エラー: {e}")

    print()

    # パターン2: comment フィールド（トップレベル）
    print("パターン2: トップレベル comment を試行")
    print()

    request_body_2 = {
        "content": LINKEDIN_POST,
        "comment": FIRST_COMMENT,
        "platforms": [
            {
                "platform": "linkedin",
                "accountId": linkedin_account_id
            }
        ],
        "scheduledFor": "2026-01-07T08:00:00+09:00",
        "timezone": "Asia/Tokyo"
    }

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers=get_headers(api_key),
            json=request_body_2,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:300]}")
        print()

        if response.status_code == 200 or response.status_code == 201:
            result = response.json()
            print("   ✅ パターン2成功！")
            print(f"   投稿ID: {result.get('_id', 'N/A')}")
            print()
            print("   Late APIはFirst Commentをサポートしています")
            print("   トップレベル comment を使用してください")
            return True
        else:
            print("   ❌ パターン2失敗")

    except Exception as e:
        print(f"   ❌ パターン2エラー: {e}")

    print()
    print("=" * 70)
    print("結論")
    print("=" * 70)
    print()
    print("❌ Late APIはLinkedIn First Commentの自動投稿をサポートしていません")
    print()
    print("対処法:")
    print("1. LinkedInの本文は案3のまま（1,150字）で予約")
    print("2. First Comment内容は準備済み（450字）")
    print("3. 1月7日（火）08:00の投稿直後、30秒以内に手動でコピペ")
    print()
    print("First Comment内容は以下のファイルに保存済みです:")
    print("   /Users/yuichi/AIPM/Flow/202601/2026-01-03/linkedin_first_comment_null2.md")
    print()

    return False


if __name__ == "__main__":
    test_linkedin_with_first_comment()
