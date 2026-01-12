#!/usr/bin/env python3
"""
AI関連ツイート抽出スクリプト

入力: x_timeline_20260104.json
出力: ai_related_tweet_ids_v2_20260104.json
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Tuple

# AI関連キーワード（大文字小文字を区別しない）
AI_KEYWORDS = [
    # AI技術名
    r'\bAI\b', r'\bA\.I\.\b', r'\bChatGPT\b', r'\bClaude\b', r'\bGemini\b',
    r'\bGPT[-\s]?[0-9o]', r'\bLLM[s]?\b', r'\b機械学習\b', r'\b深層学習\b',
    r'\bGrok\b', r'\bCopilot\b', r'\bDALL[-\s]?E\b', r'\bMidjourney\b',
    r'\bStable\s+Diffusion\b', r'\bディープラーニング\b',

    # AI企業名
    r'\bOpenAI\b', r'\bAnthropic\b', r'\bDeepMind\b', r'\bMicrosoft\s+AI\b',
    r'\bMeta\s+AI\b', r'\bxAI\b', r'\bHugging\s+Face\b',

    # AI応用技術・概念
    r'\b生成AI\b', r'\b画像生成AI\b', r'\bプロンプト\s*エンジニアリング\b',
    r'\bAI\s*エージェント\b', r'\bAI\s*agent[s]?\b', r'\bRAG\b',
    r'\bファインチューニング\b', r'\bfine[-\s]?tuning\b',
    r'\btransformer[s]?\b', r'\bneural\s+network', r'\bニューラルネット\b',
    r'\b自然言語処理\b', r'\bNLP\b', r'\bコンピュータビジョン\b',
    r'\b強化学習\b', r'\breinforcement\s+learning\b',

    # AI開発・研究関連
    r'\bAI\s*安全性\b', r'\bAI\s*倫理\b', r'\bAI\s*規制\b', r'\bAI\s*ガバナンス\b',
    r'\bAGI\b', r'\bArtificial\s+General\s+Intelligence\b',
    r'\bプロンプト\b(?=.*AI|.*LLM|.*GPT|.*Claude|.*ChatGPT)',

    # 日本語特有の表現
    r'\bAI[をがにはも]', r'\b人工知能\b', r'\bAI活用\b', r'\bAI導入\b',
]

# 除外キーワード（政治・経済・エンタメ・地政学）
EXCLUDE_KEYWORDS = [
    # 政治
    r'\bマドゥロ\b', r'\bトランプ\b(?!.*AI)', r'\b選挙\b(?!.*AI)',
    r'\b政策\b(?!.*AI)', r'\b外交\b(?!.*AI)', r'\b軍事\b(?!.*AI)',

    # 軍事・地政学
    r'\bF[-\s]?22\b', r'\b戦闘機\b(?!.*AI)', r'\bロシア軍\b', r'\bウクライナ\b(?!.*AI)',
    r'\b制裁\b(?!.*AI)', r'\b紛争\b(?!.*AI)',

    # 仮想通貨（AIボット関連でない限り）
    r'\bPolymarket\b(?!.*AI)', r'\b仮想通貨\b(?!.*AI)', r'\bビットコイン\b(?!.*AI)',
]

def contains_ai_keywords(text: str) -> Tuple[bool, List[str]]:
    """AI関連キーワードが含まれているかチェック"""
    if not text:
        return False, []

    matched_keywords = []
    text_lower = text.lower()

    for pattern in AI_KEYWORDS:
        if re.search(pattern, text, re.IGNORECASE):
            matched_keywords.append(pattern)

    return len(matched_keywords) > 0, matched_keywords

def contains_exclude_keywords(text: str) -> Tuple[bool, List[str]]:
    """除外キーワードが含まれているかチェック"""
    if not text:
        return False, []

    matched_keywords = []

    for pattern in EXCLUDE_KEYWORDS:
        if re.search(pattern, text, re.IGNORECASE):
            matched_keywords.append(pattern)

    return len(matched_keywords) > 0, matched_keywords

def is_ai_related_tweet(tweet: Dict) -> Tuple[bool, str]:
    """
    ツイートがAI関連かどうかを判定

    Returns:
        (is_ai_related: bool, reason: str)
    """
    # ツイート本文を取得
    text = tweet.get('text', '')

    # 空のツイートは除外
    if not text.strip():
        return False, "Empty text"

    # 除外キーワードチェック
    has_exclude, exclude_keywords = contains_exclude_keywords(text)
    if has_exclude:
        return False, f"Contains exclude keywords: {exclude_keywords[:2]}"

    # AI関連キーワードチェック
    has_ai, ai_keywords = contains_ai_keywords(text)
    if has_ai:
        return True, f"Contains AI keywords: {ai_keywords[:2]}"

    return False, "No AI keywords found"

def extract_ai_tweets(input_file: Path, output_file: Path):
    """AI関連ツイートを抽出"""

    print(f"Reading tweets from: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tweets = data if isinstance(data, list) else data.get('tweets', [])
    print(f"Total tweets: {len(tweets)}")

    ai_tweet_ids = []
    excluded_examples = []
    included_examples = []

    for tweet in tweets:
        tweet_id = tweet.get('tweet_id') or tweet.get('id')
        is_ai, reason = is_ai_related_tweet(tweet)

        if is_ai:
            ai_tweet_ids.append(tweet_id)
            if len(included_examples) < 10:
                included_examples.append({
                    'tweet_id': tweet_id,
                    'text': tweet.get('text', '')[:200],
                    'reason': reason
                })
        else:
            if len(excluded_examples) < 10:
                excluded_examples.append({
                    'tweet_id': tweet_id,
                    'text': tweet.get('text', '')[:200],
                    'reason': reason
                })

    # 結果レポート
    print("\n" + "="*80)
    print("EXTRACTION REPORT")
    print("="*80)
    print(f"\nTotal tweets processed: {len(tweets)}")
    print(f"AI-related tweets: {len(ai_tweet_ids)}")
    print(f"Non-AI tweets: {len(tweets) - len(ai_tweet_ids)}")
    print(f"AI-related ratio: {len(ai_tweet_ids)/len(tweets)*100:.1f}%")

    print("\n" + "-"*80)
    print("EXCLUDED TWEET EXAMPLES (First 5)")
    print("-"*80)
    for i, example in enumerate(excluded_examples[:5], 1):
        print(f"\n{i}. Tweet ID: {example['tweet_id']}")
        print(f"   Text: {example['text']}")
        print(f"   Reason: {example['reason']}")

    print("\n" + "-"*80)
    print("INCLUDED TWEET EXAMPLES (First 5)")
    print("-"*80)
    for i, example in enumerate(included_examples[:5], 1):
        print(f"\n{i}. Tweet ID: {example['tweet_id']}")
        print(f"   Text: {example['text']}")
        print(f"   Reason: {example['reason']}")

    # 結果を保存
    result = {
        'metadata': {
            'total_tweets': len(tweets),
            'ai_related_count': len(ai_tweet_ids),
            'non_ai_count': len(tweets) - len(ai_tweet_ids),
            'ai_ratio': f"{len(ai_tweet_ids)/len(tweets)*100:.1f}%"
        },
        'ai_tweet_ids': ai_tweet_ids,
        'excluded_examples': excluded_examples[:10],
        'included_examples': included_examples[:10]
    }

    print(f"\n\nSaving results to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✓ Extraction complete!")
    print(f"✓ {len(ai_tweet_ids)} AI-related tweet IDs saved")

if __name__ == '__main__':
    input_file = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260104.json')
    output_file = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/ai_related_tweet_ids_v2_20260104.json')

    extract_ai_tweets(input_file, output_file)
