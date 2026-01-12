#!/usr/bin/env python3
"""
Research Topic Skill Implementation
Web調査でトピックの最新ニュース、ファクトチェック、反対意見、専門家見解を収集
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

# WebSearch機能はClaudeCode LLMで実行（このスクリプトはデータ準備のみ）


def extract_research_topics(top_tweets_file: Path) -> List[Dict[str, Any]]:
    """
    Top 10ツイートから調査すべきトピックを抽出

    Args:
        top_tweets_file: Top 10ツイートJSONファイル

    Returns:
        調査トピックのリスト
    """
    print(f"📖 Reading top tweets from: {top_tweets_file}")

    try:
        with open(top_tweets_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {top_tweets_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format: {e}")
        sys.exit(1)

    top_tweets = data.get('top_tweets', [])
    print(f"✅ Loaded {len(top_tweets)} top tweets")

    # トピック抽出（ClaudeCode LLMで判断）
    topics = []
    for i, tweet in enumerate(top_tweets, 1):
        topic = {
            'tweet_id': tweet['tweet_id'],
            'username': tweet['username'],
            'text': tweet['text'][:200],  # 最初の200文字
            'rank': i,
            'engagement_score': tweet.get('engagement_score', 0),
            'research_priority': 'high' if i <= 3 else 'medium' if i <= 6 else 'low'
        }
        topics.append(topic)

    return topics


def prepare_research_output(topics: List[Dict[str, Any]], output_file: Path) -> Dict[str, Any]:
    """
    調査結果の出力ファイルを準備

    Args:
        topics: 調査トピックリスト
        output_file: 出力JSONファイル

    Returns:
        出力データ構造
    """
    output_data = {
        'metadata': {
            'researched_at': datetime.now().isoformat(),
            'research_method': 'ClaudeCode WebSearch + LLM analysis',
            'total_topics': len(topics),
            'high_priority_count': len([t for t in topics if t['research_priority'] == 'high']),
            'research_categories': [
                'latest_news',
                'fact_check',
                'opposing_views',
                'expert_opinions'
            ]
        },
        'research_findings': {}
    }

    print(f"\n📊 Research topics prepared:")
    print(f"  - Total topics: {output_data['metadata']['total_topics']}")
    print(f"  - High priority: {output_data['metadata']['high_priority_count']}")
    print(f"  - Research categories: {len(output_data['metadata']['research_categories'])}")

    return output_data, topics


def display_topics(topics: List[Dict[str, Any]]):
    """調査トピック一覧を表示"""
    print("\n" + "="*70)
    print("📝 Topics to research")
    print("="*70)

    for topic in topics:
        priority_icon = "🔥" if topic['research_priority'] == 'high' else "⚡" if topic['research_priority'] == 'medium' else "💡"
        print(f"\n{priority_icon} Rank {topic['rank']} ({topic['research_priority']} priority)")
        print(f"  @{topic['username']} (engagement: {topic['engagement_score']})")
        print(f"  {topic['text'][:100]}...")

    print("\n" + "="*70)


def main():
    """メイン処理"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"

    # 最新のtop_10_ai_tweets_ファイルを検索
    top_tweets_files = sorted(
        data_dir.glob("top_10_ai_tweets_*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    if not top_tweets_files:
        print("❌ Error: No top_10_ai_tweets file found")
        print("   Please run extract_top_tweets.py first")
        sys.exit(1)

    input_file = top_tweets_files[0]

    # 出力ファイル名生成
    date_str = input_file.stem.replace('top_10_ai_tweets_', '')
    output_file = data_dir / f"research_findings_ai_{date_str}.json"

    print("\n" + "="*70)
    print("🔍 Research Topic Skill")
    print("="*70)
    print(f"\n📂 Input file: {input_file.name}")
    print(f"📂 Output file: {output_file.name}")

    # STEP 1: トピック抽出
    topics = extract_research_topics(input_file)

    # STEP 2: トピック表示
    display_topics(topics)

    # STEP 3: 調査実行の準備
    output_data, topics = prepare_research_output(topics, output_file)

    # STEP 4: 出力ファイル生成（調査結果はClaudeCode LLMで追記）
    print(f"\n💾 Writing prepared structure to: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # トピック情報を含めて保存
    output_data['topics'] = topics

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("✅ Research preparation completed")
    print("\n📌 Next: ClaudeCode LLM will execute WebSearch and fill research_findings")
    print(f"   Total topics to research: {len(topics)}")
    print(f"   High priority topics: {len([t for t in topics if t['research_priority'] == 'high'])}")

    return output_data, topics


if __name__ == "__main__":
    main()
