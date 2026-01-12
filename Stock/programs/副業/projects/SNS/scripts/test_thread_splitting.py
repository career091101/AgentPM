#!/usr/bin/env python3
"""
スレッド分割機能テスト
"""

import sys
from pathlib import Path

# late_api_postモジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
from late_api_post import split_for_twitter, split_for_threads

# テスト用長文コンテンツ（約1000字）
TEST_CONTENT = """AIエージェント技術の進化が加速しています。

特に注目すべきは、Elon MuskのxAI社が開発した「Grok 2」モデルです。このモデルは、リアルタイムでX（旧Twitter）のデータにアクセスし、最新のトレンドやニュースを即座に分析できる能力を持っています。

━━━

従来のAIモデルとの最大の違いは、情報の鮮度です。ChatGPTやClaude等の既存モデルは、学習データのカットオフ日が存在するため、最新情報への対応に制約がありました。しかし、Grokはリアルタイム検索機能を統合することで、この問題を解決しています。

また、Meta社も「Llama 3」シリーズでマルチモーダル機能を強化し、画像認識と自然言語処理を高度に融合させた新世代のAIエージェントを開発中です。これにより、ユーザーは画像をアップロードするだけで、その内容を詳細に解析し、関連情報を自動的に収集できるようになります。

━━━

企業における活用事例も急速に増加しています。特にカスタマーサポート領域では、AIエージェントが24時間365日対応可能なヘルプデスクとして機能し、人間のオペレーターの負荷を大幅に軽減しています。

さらに、開発者向けには「GitHub Copilot」のようなコーディング支援AIが普及し、プログラミングの生産性が飛躍的に向上しています。これらの技術は、今後さらに洗練され、私たちの働き方を根本から変える可能性を秘めています。

#AIエージェント #技術トレンド #自動化"""


def test_twitter_splitting():
    """X（Twitter）スレッド分割テスト"""
    print("=" * 70)
    print("X（Twitter）スレッド分割テスト")
    print("=" * 70)

    tweets = split_for_twitter(TEST_CONTENT, max_length=140)

    print(f"\n✅ 分割結果: {len(tweets)}ツイート\n")

    for i, tweet in enumerate(tweets):
        char_count = len(tweet)
        # 番号を除いた本文のみの文字数も計算
        content_only = tweet.split('\n\n', 1)[1] if '\n\n' in tweet else tweet
        content_char_count = len(content_only)

        print(f"--- ツイート {i+1} ---")
        print(f"文字数: {char_count}文字（番号込み）/ {content_char_count}文字（本文のみ）")
        print(f"内容:\n{tweet}\n")

        # 検証
        if char_count > 140:
            print(f"❌ エラー: 140文字を超えています！")
            return False

    # 5ツイート以上の確認
    if len(tweets) < 5:
        print(f"⚠️  警告: {len(tweets)}ツイートのみ（推奨: 5ツイート以上）")
    else:
        print(f"✅ 5ツイート以上: {len(tweets)}ツイート")

    return True


def test_threads_splitting():
    """Threadsスレッド分割テスト"""
    print("\n" + "=" * 70)
    print("Threadsスレッド分割テスト")
    print("=" * 70)

    posts = split_for_threads(TEST_CONTENT, max_length=500)

    print(f"\n✅ 分割結果: {len(posts)}投稿\n")

    for i, post in enumerate(posts):
        char_count = len(post)

        print(f"--- 投稿 {i+1} ---")
        print(f"文字数: {char_count}文字")
        print(f"内容:\n{post}\n")

        # 検証
        if char_count > 500:
            print(f"❌ エラー: 500文字を超えています！")
            return False

    # 3投稿の確認
    if len(posts) != 3:
        print(f"⚠️  警告: {len(posts)}投稿（推奨: 3投稿）")
    else:
        print(f"✅ 3投稿に調整済み")

    return True


if __name__ == "__main__":
    twitter_success = test_twitter_splitting()
    threads_success = test_threads_splitting()

    print("\n" + "=" * 70)
    print("総合結果")
    print("=" * 70)
    print(f"X（Twitter）分割: {'✅ 成功' if twitter_success else '❌ 失敗'}")
    print(f"Threads分割: {'✅ 成功' if threads_success else '❌ 失敗'}")

    sys.exit(0 if (twitter_success and threads_success) else 1)
