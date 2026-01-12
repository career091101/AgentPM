#!/usr/bin/env python3
"""
Extract Top Tweets Skill Implementation
エンゲージメントスコアに基づいてTop 10ツイートを抽出
日本人7割、外国人3割の比率で抽出
"""

import json
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

# 世界的著名人の除外リスト
EXCLUDED_USERNAMES = [
    'elonmusk',
    'billgates',
    'barackobama',
    'tim_cook',
    'realdonaldtrump',
    'jeffbezos',
    'sundarPichai',
    'satyanadella'
]

# AI関連判定はClaudeCode LLMで実行
# このスクリプトはツイートデータを準備するのみ

def calculate_engagement_score(tweet: Dict[str, Any]) -> int:
    """
    エンゲージメントスコアを計算
    engagement_score = likes + (retweets × 3) + (replies × 5)
    """
    likes = tweet.get('likes', 0)
    retweets = tweet.get('retweets', 0)
    replies = tweet.get('replies', 0)

    # 負の値を0として扱う（異常データ）
    likes = max(0, likes)
    retweets = max(0, retweets)
    replies = max(0, replies)

    return likes + (retweets * 3) + (replies * 5)


def filter_famous_accounts(tweets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """世界的著名人のツイートを除外"""
    excluded_lower = [u.lower() for u in EXCLUDED_USERNAMES]
    filtered = [
        tweet for tweet in tweets
        if tweet.get('username', '').lower() not in excluded_lower
    ]
    return filtered


def is_japanese_tweet(tweet: Dict[str, Any]) -> bool:
    """
    ツイートが日本語かどうかを判定

    判定基準:
    - ツイート本文に日本語文字（ひらがな、カタカナ、漢字）が含まれる
    - 日本語文字が全体の20%以上を占める

    Args:
        tweet: ツイートデータ

    Returns:
        日本語ツイートの場合True
    """
    text = tweet.get('text', '')

    if not text:
        return False

    # 日本語文字のパターン（ひらがな、カタカナ、漢字）
    japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')

    # 日本語文字を抽出
    japanese_chars = japanese_pattern.findall(text)
    japanese_count = len(japanese_chars)
    total_chars = len(text.replace(' ', '').replace('\n', ''))  # 空白・改行を除く

    if total_chars == 0:
        return False

    # 日本語文字が20%以上含まれていればJapaese判定
    japanese_ratio = japanese_count / total_chars
    return japanese_ratio >= 0.2


def split_japanese_foreign_tweets(tweets: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    ツイートを日本人と外国人に分類

    Args:
        tweets: ツイートリスト

    Returns:
        (日本人ツイート, 外国人ツイート)のタプル
    """
    japanese_tweets = []
    foreign_tweets = []

    for tweet in tweets:
        if is_japanese_tweet(tweet):
            tweet['is_japanese'] = True
            japanese_tweets.append(tweet)
        else:
            tweet['is_japanese'] = False
            foreign_tweets.append(tweet)

    return japanese_tweets, foreign_tweets


def extract_top_tweets(input_file: Path, output_file: Path, top_n: int = 10) -> Dict[str, Any]:
    """
    タイムラインデータからTop Nツイートを抽出

    Args:
        input_file: 入力JSONファイルパス
        output_file: 出力JSONファイルパス
        top_n: 抽出件数（デフォルト: 10）

    Returns:
        処理結果のメタデータ
    """
    # STEP 1: タイムラインデータ読み込み
    print(f"📖 Reading timeline data from: {input_file}")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format: {e}")
        sys.exit(1)

    tweets = data.get('tweets', [])
    total_tweets = len(tweets)

    if total_tweets == 0:
        print("⚠️  Warning: No tweets found in the data")
        sys.exit(1)

    print(f"✅ Loaded {total_tweets} tweets")

    # STEP 2: エンゲージメントスコア計算
    print("\n🔢 Calculating engagement scores...")
    for tweet in tweets:
        tweet['engagement_score'] = calculate_engagement_score(tweet)

    # STEP 3: フィルタリング（世界的著名人除外）
    print("\n🔍 Filtering famous accounts...")
    initial_count = len(tweets)
    filtered_tweets = filter_famous_accounts(tweets)
    filtered_count = len(filtered_tweets)
    excluded_count = initial_count - filtered_count

    print(f"✅ Filtered: {filtered_count} tweets (excluded {excluded_count} famous accounts)")

    # STEP 4: 日本人・外国人の分類
    print(f"\n🌏 Classifying Japanese/Foreign tweets...")
    japanese_tweets, foreign_tweets = split_japanese_foreign_tweets(filtered_tweets)

    print(f"✅ Japanese tweets: {len(japanese_tweets)}")
    print(f"✅ Foreign tweets: {len(foreign_tweets)}")

    # STEP 5: 各カテゴリ内でソート（エンゲージメントスコア降順）
    japanese_sorted = sorted(
        japanese_tweets,
        key=lambda t: (t['engagement_score'], t.get('timestamp_text', '')),
        reverse=True
    )

    foreign_sorted = sorted(
        foreign_tweets,
        key=lambda t: (t['engagement_score'], t.get('timestamp_text', '')),
        reverse=True
    )

    # STEP 6: 7:3比率で抽出（日本人7件、外国人3件）
    print(f"\n🏆 Extracting top {top_n} tweets (7 Japanese, 3 Foreign)...")

    japanese_count = int(top_n * 0.7)  # 7件
    foreign_count = top_n - japanese_count  # 3件

    top_japanese = japanese_sorted[:japanese_count]
    top_foreign = foreign_sorted[:foreign_count]

    # 不足分の調整（日本人または外国人が足りない場合）
    if len(top_japanese) < japanese_count:
        shortage = japanese_count - len(top_japanese)
        print(f"⚠️  Warning: Only {len(top_japanese)} Japanese tweets available (need {japanese_count})")
        # 外国人から不足分を補充
        top_foreign = foreign_sorted[:foreign_count + shortage]

    if len(top_foreign) < foreign_count:
        shortage = foreign_count - len(top_foreign)
        print(f"⚠️  Warning: Only {len(top_foreign)} Foreign tweets available (need {foreign_count})")
        # 日本人から不足分を補充
        top_japanese = japanese_sorted[:japanese_count + shortage]

    # 合計Top 10ツイート
    top_tweets = top_japanese + top_foreign

    # エンゲージメントスコア順に再ソート（ランキング用）
    top_tweets = sorted(
        top_tweets,
        key=lambda t: (t['engagement_score'], t.get('timestamp_text', '')),
        reverse=True
    )

    actual_count = len(top_tweets)
    actual_japanese_count = len([t for t in top_tweets if t.get('is_japanese')])
    actual_foreign_count = actual_count - actual_japanese_count

    print(f"✅ Extracted {actual_count} tweets ({actual_japanese_count} Japanese, {actual_foreign_count} Foreign)")

    if actual_count < top_n:
        print(f"⚠️  Warning: Only {actual_count} tweets available (less than {top_n})")

    # STEP 7: メタデータ付与
    print("\n📝 Adding metadata...")

    # Top tweetsにランキングとURLを付与
    for rank, tweet in enumerate(top_tweets, start=1):
        tweet['rank'] = rank
        username = tweet.get('username', '')
        tweet_id = tweet.get('tweet_id', '')
        tweet['url'] = f"https://x.com/{username}/status/{tweet_id}"

    # 出力データ構造
    output_data = {
        "metadata": {
            "processed_at": datetime.now().isoformat(),
            "source_file": input_file.name,
            "total_tweets": total_tweets,
            "filtered_tweets": filtered_count,
            "top_tweets_count": actual_count,
            "japanese_tweets_count": actual_japanese_count,
            "foreign_tweets_count": actual_foreign_count,
            "japanese_ratio": actual_japanese_count / actual_count if actual_count > 0 else 0,
            "filter_criteria": {
                "excluded_usernames": EXCLUDED_USERNAMES,
                "target_japanese_ratio": 0.7,
                "min_engagement_score": top_tweets[-1]['engagement_score'] if top_tweets else 0
            }
        },
        "top_tweets": top_tweets
    }

    # STEP 6: ファイル出力
    print(f"\n💾 Writing output to: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("✅ Output file created successfully")

    # STEP 8: 品質検証
    print("\n✅ Quality validation:")

    # エンゲージメントスコア妥当性
    all_scores_valid = all(t['engagement_score'] >= 0 for t in top_tweets)
    print(f"  - All engagement scores valid: {all_scores_valid}")

    # スコアが降順に並んでいる
    scores = [t['engagement_score'] for t in top_tweets]
    is_sorted = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
    print(f"  - Scores are sorted: {is_sorted}")

    # 重複チェック
    tweet_ids = [t['tweet_id'] for t in top_tweets]
    no_duplicates = len(tweet_ids) == len(set(tweet_ids))
    print(f"  - No duplicate tweet IDs: {no_duplicates}")

    # 著名人除外確認
    usernames_lower = [t.get('username', '').lower() for t in top_tweets]
    excluded_lower = [u.lower() for u in EXCLUDED_USERNAMES]
    no_famous = not any(u in excluded_lower for u in usernames_lower)
    print(f"  - No famous accounts included: {no_famous}")

    # URL形式確認
    all_urls_valid = all(t['url'].startswith('https://x.com/') for t in top_tweets)
    print(f"  - All URLs valid: {all_urls_valid}")

    # 日本人/外国人比率確認
    japanese_ratio_check = actual_japanese_count >= int(top_n * 0.6)  # 60%以上ならOK（許容範囲）
    print(f"  - Japanese ratio acceptable (≥60%): {japanese_ratio_check} ({actual_japanese_count}/{actual_count} = {actual_japanese_count/actual_count*100:.1f}%)")

    return output_data


def display_summary(output_data: Dict[str, Any]):
    """処理結果のサマリーを表示"""
    metadata = output_data['metadata']
    top_tweets = output_data['top_tweets']

    print("\n" + "="*60)
    print("✅ Top 10 tweets extracted successfully (7:3 ratio)")
    print("="*60)

    print("\n📊 Summary:")
    print(f"  - Total tweets processed: {metadata['total_tweets']}")
    print(f"  - Filtered tweets: {metadata['filtered_tweets']} (excluded {metadata['total_tweets'] - metadata['filtered_tweets']} famous accounts)")
    print(f"  - Japanese tweets: {metadata['japanese_tweets_count']}/{metadata['top_tweets_count']} ({metadata['japanese_ratio']*100:.1f}%)")
    print(f"  - Foreign tweets: {metadata['foreign_tweets_count']}/{metadata['top_tweets_count']} ({(1-metadata['japanese_ratio'])*100:.1f}%)")

    scores = [t['engagement_score'] for t in top_tweets]
    print(f"  - Top {len(top_tweets)} engagement scores: {', '.join(map(str, scores))}")

    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"  - Average engagement score (Top {len(top_tweets)}): {avg_score:.1f}")

    print(f"  - Output file: {metadata['source_file'].replace('x_timeline_', 'top_10_tweets_')}")

    print("\n🏆 Top 3 Preview:")
    for i, tweet in enumerate(top_tweets[:3], start=1):
        username = tweet.get('username', 'unknown')
        score = tweet['engagement_score']
        is_japanese = tweet.get('is_japanese', False)
        lang_flag = "🇯🇵" if is_japanese else "🌏"
        text = tweet.get('text', '')[:50] + "..." if len(tweet.get('text', '')) > 50 else tweet.get('text', '')
        print(f"{i}. {lang_flag} @{username} ({score} pts) - \"{text}\"")

    print("\n" + "="*60)


def main():
    """メイン処理"""
    # デフォルトパス設定
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"

    # 最新のタイムラインファイルを検索（日付形式YYYYMMDDで始まるもの優先）
    timeline_files = list(data_dir.glob("x_timeline_202*.json"))

    if not timeline_files:
        print("⚠️  No timeline files with date format found, trying all timeline files...")
        timeline_files = list(data_dir.glob("x_timeline_*.json"))

    if not timeline_files:
        print("❌ Error: No timeline data found")
        sys.exit(1)

    # ファイルの更新日時でソート（最新のものを使用）
    timeline_files = sorted(timeline_files, key=lambda f: f.stat().st_mtime, reverse=True)

    input_file = timeline_files[0]

    # 出力ファイル名生成（x_timeline_YYYYMMDD.json → top_10_tweets_YYYYMMDD.json）
    date_str = input_file.stem.replace('x_timeline_', '')
    # YYYYMMDD_HHMMSS形式の場合、_HHMMSSを削除
    if '_' in date_str:
        date_str = date_str.split('_')[0]

    output_file = data_dir / f"top_10_tweets_{date_str}.json"

    # 処理実行
    output_data = extract_top_tweets(input_file, output_file)

    # サマリー表示
    display_summary(output_data)


if __name__ == "__main__":
    main()
