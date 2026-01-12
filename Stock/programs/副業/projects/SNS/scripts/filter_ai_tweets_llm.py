#!/usr/bin/env python3
"""
AI関連度フィルタリング - LLM判定版
LLM判定用の中間ファイルを生成し、Claude Code LLMによる判定を待機
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any


def prepare_llm_judgment_data(tweets: List[Dict[str, Any]], output_file: Path) -> None:
    """
    LLM判定用の中間データを生成

    Args:
        tweets: ツイートリスト
        output_file: 出力ファイルパス
    """
    print(f"\n📝 Preparing LLM judgment data...")

    # LLM判定用のプロンプトテンプレート
    judgment_template = {
        "instruction": """以下の10件のツイートについて、AI・機械学習・データサイエンス関連かどうか、各ツイートを0-3点で評価してください。

【評価基準】
- 3点: LLM, ChatGPT, Claude, GPT, Gemini, transformer, RAG, プロンプトエンジニアリング等の明示的なAI技術キーワードが含まれる
- 2点: OpenAI, Anthropic, DeepMind等のAI企業名が明記され、技術的な詳細がある
- 1点: 機械学習、データサイエンス、予測モデル、自動化が主題
- 0点: 上記いずれにも該当しない（一般ビジネス、政治、株式投資、マーケティング、エンタメ等）

【重要な注意】
- Elon Muskの政治資金援助、成功要因等の自己啓発は0点
- 株式投資、企業の大株主情報は0点
- YouTubeチャンネル収益化、マーケティング手法は0点
- キーボード、ガジェット、製品紹介は0点
- 目標達成システム、自己啓発は0点
- 投資一般、株価見通しは0点
- ロボット（Optimus等）のみでAI技術言及なしは1点（AI周辺技術）

【回答形式】
必ず以下のJSON配列形式で回答してください。
[
  {"tweet_id": "ID1", "score": 0, "reason": "理由を20文字以内で"},
  {"tweet_id": "ID2", "score": 3, "reason": "理由を20文字以内で"},
  ...
]
""",
        "tweets": []
    }

    # ツイートデータを簡略化して追加
    for tweet in tweets:
        judgment_template["tweets"].append({
            "tweet_id": tweet.get('tweet_id'),
            "username": tweet.get('username'),
            "text": tweet.get('text'),
            "rank": tweet.get('rank'),
            "engagement_score": tweet.get('engagement_score')
        })

    # ファイル出力
    print(f"💾 Writing LLM judgment data to: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(judgment_template, f, ensure_ascii=False, indent=2)

    print("✅ LLM judgment data created successfully")
    print(f"\n📌 Next step:")
    print(f"   Run Claude Code to judge AI relevance:")
    print(f"   cat {output_file} | claude --model haiku")


def apply_llm_judgment(
    original_tweets: List[Dict[str, Any]],
    judgment_results: List[Dict[str, Any]],
    min_score: int = 1
) -> List[Dict[str, Any]]:
    """
    LLM判定結果を適用してフィルタリング

    Args:
        original_tweets: 元のツイートリスト
        judgment_results: LLM判定結果リスト
        min_score: 最低スコア

    Returns:
        フィルタリング済みツイートリスト
    """
    print(f"\n🤖 Applying LLM judgment results (min_score: {min_score})...")

    # tweet_id -> 判定結果のマッピング作成
    judgment_map = {
        result['tweet_id']: result
        for result in judgment_results
    }

    ai_tweets = []
    non_ai_tweets = []

    for tweet in original_tweets:
        tweet_id = tweet.get('tweet_id')
        judgment = judgment_map.get(tweet_id)

        if not judgment:
            print(f"⚠️  Warning: No judgment found for tweet {tweet_id}")
            tweet['ai_relevance_score'] = 0
            tweet['ai_relevance_reason'] = "判定なし"
            non_ai_tweets.append(tweet)
            continue

        score = judgment.get('score', 0)
        reason = judgment.get('reason', '')

        # ツイートにAI関連度情報を追加
        tweet['ai_relevance_score'] = score
        tweet['ai_relevance_reason'] = reason

        if score >= min_score:
            ai_tweets.append(tweet)
            print(f"   ✅ PASS - @{tweet.get('username')} (score: {score}, reason: {reason})")
        else:
            non_ai_tweets.append(tweet)
            print(f"   ❌ REJECT - @{tweet.get('username')} (score: {score}, reason: {reason})")

    print(f"\n✅ AI-related tweets: {len(ai_tweets)}/{len(original_tweets)} ({len(ai_tweets)/len(original_tweets)*100:.1f}%)")
    print(f"   - Score 3: {len([t for t in ai_tweets if t['ai_relevance_score'] == 3])}")
    print(f"   - Score 2: {len([t for t in ai_tweets if t['ai_relevance_score'] == 2])}")
    print(f"   - Score 1: {len([t for t in ai_tweets if t['ai_relevance_score'] == 1])}")
    print(f"   - Score 0 (rejected): {len(non_ai_tweets)}")

    return ai_tweets


def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Step 1 (Prepare): python filter_ai_tweets_llm.py prepare <input_json> <judgment_file>")
        print("  Step 2 (Apply):   python filter_ai_tweets_llm.py apply <input_json> <judgment_result_json> <output_json> [min_score]")
        print("\nExample:")
        print("  python filter_ai_tweets_llm.py prepare top_10_tweets.json llm_judgment_input.json")
        print("  # Then run: cat llm_judgment_input.json | claude --model haiku > llm_judgment_result.json")
        print("  python filter_ai_tweets_llm.py apply top_10_tweets.json llm_judgment_result.json top_10_ai_tweets.json 1")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "prepare":
        # Step 1: LLM判定用データ準備
        if len(sys.argv) < 4:
            print("Error: Missing arguments for prepare mode")
            print("Usage: python filter_ai_tweets_llm.py prepare <input_json> <judgment_file>")
            sys.exit(1)

        input_file = Path(sys.argv[2])
        judgment_file = Path(sys.argv[3])

        # 入力ファイル読み込み
        print(f"📖 Reading input file: {input_file}")

        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"❌ Error: File not found: {input_file}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON format: {e}")
            sys.exit(1)

        tweets = data.get('top_tweets', [])

        if not tweets:
            print("⚠️  Warning: No tweets found in the data")
            sys.exit(1)

        print(f"✅ Loaded {len(tweets)} tweets")

        # LLM判定用データ生成
        prepare_llm_judgment_data(tweets, judgment_file)

    elif mode == "apply":
        # Step 2: LLM判定結果適用
        if len(sys.argv) < 5:
            print("Error: Missing arguments for apply mode")
            print("Usage: python filter_ai_tweets_llm.py apply <input_json> <judgment_result_json> <output_json> [min_score]")
            sys.exit(1)

        input_file = Path(sys.argv[2])
        judgment_result_file = Path(sys.argv[3])
        output_file = Path(sys.argv[4])
        min_score = int(sys.argv[5]) if len(sys.argv) > 5 else 1

        # 入力ファイル読み込み
        print(f"📖 Reading input file: {input_file}")

        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"❌ Error: File not found: {input_file}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON format: {e}")
            sys.exit(1)

        tweets = data.get('top_tweets', [])

        if not tweets:
            print("⚠️  Warning: No tweets found in the data")
            sys.exit(1)

        print(f"✅ Loaded {len(tweets)} tweets")

        # LLM判定結果読み込み
        print(f"\n📖 Reading LLM judgment results: {judgment_result_file}")

        try:
            with open(judgment_result_file, 'r', encoding='utf-8') as f:
                judgment_results = json.load(f)
        except FileNotFoundError:
            print(f"❌ Error: File not found: {judgment_result_file}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON format: {e}")
            sys.exit(1)

        if not isinstance(judgment_results, list):
            print(f"❌ Error: Judgment results must be a JSON array")
            sys.exit(1)

        print(f"✅ Loaded {len(judgment_results)} judgment results")

        # LLM判定結果を適用してフィルタリング
        ai_tweets = apply_llm_judgment(tweets, judgment_results, min_score=min_score)

        # メタデータ更新
        metadata = data.get('metadata', {})
        metadata['ai_filtered_at'] = datetime.now().isoformat()
        metadata['ai_filter_min_score'] = min_score
        metadata['ai_filter_passed'] = len(ai_tweets)
        metadata['ai_filter_rejected'] = len(tweets) - len(ai_tweets)
        metadata['ai_filter_pass_rate'] = len(ai_tweets) / len(tweets) if tweets else 0

        # 出力データ構造
        output_data = {
            "metadata": metadata,
            "top_tweets": ai_tweets
        }

        # ファイル出力
        print(f"\n💾 Writing output to: {output_file}")
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print("✅ Output file created successfully")

        # サマリー表示
        print("\n" + "="*60)
        print("✅ AI filtering completed")
        print("="*60)
        print(f"  - Input tweets: {len(tweets)}")
        print(f"  - AI-related tweets (score ≥ {min_score}): {len(ai_tweets)} ({len(ai_tweets)/len(tweets)*100:.1f}%)")
        print(f"  - Rejected tweets (score < {min_score}): {len(tweets) - len(ai_tweets)} ({(len(tweets) - len(ai_tweets))/len(tweets)*100:.1f}%)")
        print(f"  - Output file: {output_file}")
        print("="*60)

    else:
        print(f"❌ Error: Unknown mode '{mode}'")
        print("Valid modes: prepare, apply")
        sys.exit(1)


if __name__ == "__main__":
    main()
