#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn投稿詳細分析スクリプト

目的: LinkedIn過去90投稿の以下を分析
1. 文字数分布
2. パターン分類（高野氏7パターンとの照合）
3. 問いかけ終結率
4. 企業名引用数
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple
import json

def extract_posts_from_log(log_path: str) -> List[Dict]:
    """
    visual_extraction_log.mdから投稿テキストを抽出
    """
    posts = []

    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 投稿ごとに分割（### で始まる行で区切る）
    post_sections = re.split(r'\n### ', content)[1:]  # 最初のヘッダー部分をスキップ

    for section in post_sections:
        lines = section.split('\n')
        post_date = lines[0].strip()

        # Statsとテキストを抽出
        stats_match = re.search(r'\*\*Stats\*\*: (.+)', section)
        text_match = re.search(r'\*\*Text\*\*: (.+?)(?=\n- \*\*Link\*\*|$)', section, re.DOTALL)

        if text_match:
            text = text_match.group(1).strip()
            # "See full text in report" を含む場合はスキップ
            if "See full text in report" in text:
                continue

            # Stats解析
            impressions = 0
            reactions = 0
            comments = 0
            if stats_match:
                stats = stats_match.group(1)
                imp_match = re.search(r'(\d+,?\d*)\s*impressions?', stats)
                react_match = re.search(r'(\d+)\s*reactions?', stats)
                comment_match = re.search(r'(\d+)\s*comments?', stats)

                if imp_match:
                    impressions = int(imp_match.group(1).replace(',', ''))
                if react_match:
                    reactions = int(react_match.group(1))
                if comment_match:
                    comments = int(comment_match.group(1))

            posts.append({
                'date': post_date,
                'text': text,
                'impressions': impressions,
                'reactions': reactions,
                'comments': comments
            })

    return posts

def analyze_char_count(posts: List[Dict]) -> Dict:
    """文字数分析"""
    char_counts = [len(post['text']) for post in posts]

    return {
        'count': len(char_counts),
        'average': sum(char_counts) / len(char_counts) if char_counts else 0,
        'median': sorted(char_counts)[len(char_counts) // 2] if char_counts else 0,
        'min': min(char_counts) if char_counts else 0,
        'max': max(char_counts) if char_counts else 0,
        'optimal_range_500_1000': sum(1 for c in char_counts if 500 <= c <= 1000),
        'optimal_range_700_900': sum(1 for c in char_counts if 700 <= c <= 900),
        'distribution': {
            'under_500': sum(1 for c in char_counts if c < 500),
            '500_700': sum(1 for c in char_counts if 500 <= c < 700),
            '700_900': sum(1 for c in char_counts if 700 <= c < 900),
            '900_1000': sum(1 for c in char_counts if 900 <= c < 1000),
            'over_1000': sum(1 for c in char_counts if c >= 1000)
        }
    }

def classify_pattern(text: str) -> str:
    """
    高野氏7パターンとの照合

    1. 断定型主張 → データ展開 → 問いかけ
    2. 問題提起 → 反論 → 正論展開
    3. ニュース引用 → 深掘り → 示唆
    4. リスト型・衝撃ファクト連打
    5. イベント・体験レポート型
    6. サービス・人材紹介型
    7. 有料サロン・コミュニティ訴求型
    """

    # Pattern 3: ニュース引用（「〇〇氏は」「〇〇によると」「報道によると」）
    if re.search(r'(氏は|氏が|によると|報道によると|発表|述べた)', text[:100]):
        return 'Pattern 3: ニュース引用型'

    # Pattern 5: イベント告知（【告知】）
    if '【告知】' in text or 'イベント' in text[:50]:
        return 'Pattern 5: イベント型'

    # Pattern 1: 断定型（「〇〇である」「〇〇だ」で始まる）
    if re.search(r'(である|だ|でした)。', text[:200]):
        return 'Pattern 1: 断定型'

    # Pattern 4: リスト型・衝撃ファクト（複数の数値、「〇兆円」「〇倍」）
    num_count = len(re.findall(r'\d+,?\d*', text))
    if num_count >= 5:
        return 'Pattern 4: リスト型・衝撃ファクト'

    return 'その他'

def check_question_ending(text: str) -> bool:
    """問いかけで終わるかチェック"""
    # 最後の50文字を確認
    ending = text[-50:]

    # 問いかけパターン
    question_patterns = [
        r'か？',
        r'でしょうか',
        r'ますか',
        r'ませんか',
        r'のでは',
        r'だろうか',
        r'はいかが',
        r'どう思いますか',
        r'いかがでしょうか'
    ]

    return any(re.search(pattern, ending) for pattern in question_patterns)

def count_company_mentions(text: str) -> int:
    """企業名引用数をカウント"""
    # 高野氏ベンチマーク: 企業名79回/50投稿 = 平均1.58社/投稿

    company_patterns = [
        r'OpenAI',
        r'Google',
        r'Microsoft|マイクロソフト',
        r'Tesla|テスラ',
        r'Anthropic|アンソロッピック',
        r'Meta',
        r'Apple',
        r'Amazon',
        r'NVIDIA|エヌビディア',
        r'Alibaba|アリババ',
        r'DeepSeek',
        r'Gemini',
        r'ChatGPT',
        r'Claude',
        r'セコイア',
        r'ゴールドマン',
        r'a16z|A16z',
        r'ソフトバンク',
        r'Walmart|ウォルマート',
        r'エポックAI',
        r'スペースX'
    ]

    count = 0
    for pattern in company_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        count += len(matches)

    return count

def analyze_linkedin_posts(log_path: str) -> Dict:
    """総合分析"""

    posts = extract_posts_from_log(log_path)

    if not posts:
        return {'error': '投稿データが抽出できませんでした'}

    # 文字数分析
    char_analysis = analyze_char_count(posts)

    # パターン分類
    patterns = {}
    for post in posts:
        pattern = classify_pattern(post['text'])
        patterns[pattern] = patterns.get(pattern, 0) + 1

    # 問いかけ終結率
    question_endings = sum(1 for post in posts if check_question_ending(post['text']))
    question_ending_rate = question_endings / len(posts) * 100

    # 企業名引用数
    company_mentions = [count_company_mentions(post['text']) for post in posts]
    avg_company_mentions = sum(company_mentions) / len(company_mentions)

    # Top/Bottom分析
    posts_with_char = [(post, len(post['text'])) for post in posts if post['impressions'] > 0]
    sorted_by_imp = sorted(posts_with_char, key=lambda x: x[0]['impressions'], reverse=True)

    top_5 = sorted_by_imp[:5] if len(sorted_by_imp) >= 5 else sorted_by_imp
    bottom_5 = sorted_by_imp[-5:] if len(sorted_by_imp) >= 5 else sorted_by_imp

    return {
        'total_posts_analyzed': len(posts),
        'char_count_analysis': char_analysis,
        'pattern_classification': patterns,
        'question_ending': {
            'count': question_endings,
            'rate': question_ending_rate,
            'benchmark_takano': '問いかけ終結 ほぼ必須（推定80%以上）'
        },
        'company_mentions': {
            'average': avg_company_mentions,
            'total': sum(company_mentions),
            'benchmark_takano': 1.58,  # 企業名79回/50投稿
            'gap': avg_company_mentions - 1.58
        },
        'top_5_posts': [
            {
                'date': post[0]['date'],
                'impressions': post[0]['impressions'],
                'char_count': post[1],
                'pattern': classify_pattern(post[0]['text']),
                'has_question_ending': check_question_ending(post[0]['text']),
                'company_mentions': count_company_mentions(post[0]['text'])
            }
            for post in top_5
        ],
        'bottom_5_posts': [
            {
                'date': post[0]['date'],
                'impressions': post[0]['impressions'],
                'char_count': post[1],
                'pattern': classify_pattern(post[0]['text']),
                'has_question_ending': check_question_ending(post[0]['text']),
                'company_mentions': count_company_mentions(post[0]['text'])
            }
            for post in bottom_5
        ]
    }

if __name__ == '__main__':
    log_path = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedIn_visual_extraction_log.md'

    result = analyze_linkedin_posts(log_path)

    # 結果を整形して出力
    print("=" * 80)
    print("LinkedIn投稿詳細分析レポート")
    print("=" * 80)
    print()

    if 'error' in result:
        print(f"エラー: {result['error']}")
    else:
        print(f"分析対象投稿数: {result['total_posts_analyzed']}投稿")
        print()

        print("【1. 文字数分析】")
        print("-" * 80)
        ca = result['char_count_analysis']
        print(f"平均文字数: {ca['average']:.1f}字")
        print(f"中央値: {ca['median']}字")
        print(f"最小: {ca['min']}字")
        print(f"最大: {ca['max']}字")
        print(f"最適範囲(500-1000字): {ca['optimal_range_500_1000']}投稿 ({ca['optimal_range_500_1000']/ca['count']*100:.1f}%)")
        print(f"高野氏推奨範囲(700-900字): {ca['optimal_range_700_900']}投稿 ({ca['optimal_range_700_900']/ca['count']*100:.1f}%)")
        print()
        print("文字数分布:")
        for range_name, count in ca['distribution'].items():
            print(f"  {range_name}: {count}投稿 ({count/ca['count']*100:.1f}%)")
        print()
        print(f"高野氏ベンチマーク: 平均760.1字、500-1000字が56%")
        print()

        print("【2. パターン分類】")
        print("-" * 80)
        for pattern, count in sorted(result['pattern_classification'].items(), key=lambda x: x[1], reverse=True):
            print(f"{pattern}: {count}投稿 ({count/result['total_posts_analyzed']*100:.1f}%)")
        print()

        print("【3. 問いかけ終結率】")
        print("-" * 80)
        qe = result['question_ending']
        print(f"問いかけで終わる投稿: {qe['count']}投稿 ({qe['rate']:.1f}%)")
        print(f"高野氏ベンチマーク: {qe['benchmark_takano']}")
        print()

        print("【4. 企業名引用数】")
        print("-" * 80)
        cm = result['company_mentions']
        print(f"平均企業名引用数: {cm['average']:.2f}社/投稿")
        print(f"総企業名引用数: {cm['total']}回")
        print(f"高野氏ベンチマーク: {cm['benchmark_takano']}社/投稿")
        print(f"ギャップ: {cm['gap']:+.2f}社/投稿")
        print()

        print("【5. Top 5投稿分析】")
        print("-" * 80)
        for i, post in enumerate(result['top_5_posts'], 1):
            print(f"{i}. {post['date']} - {post['impressions']:,} imp")
            print(f"   文字数: {post['char_count']}字 | パターン: {post['pattern']}")
            print(f"   問いかけ終結: {'✓' if post['has_question_ending'] else '✗'} | 企業名: {post['company_mentions']}社")
            print()

        print("【6. Bottom 5投稿分析】")
        print("-" * 80)
        for i, post in enumerate(result['bottom_5_posts'], 1):
            print(f"{i}. {post['date']} - {post['impressions']:,} imp")
            print(f"   文字数: {post['char_count']}字 | パターン: {post['pattern']}")
            print(f"   問いかけ終結: {'✓' if post['has_question_ending'] else '✗'} | 企業名: {post['company_mentions']}社")
            print()

        # JSON出力
        output_path = Path(log_path).parent / 'linkedin_detailed_analysis.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"\n詳細結果をJSONで保存: {output_path}")
