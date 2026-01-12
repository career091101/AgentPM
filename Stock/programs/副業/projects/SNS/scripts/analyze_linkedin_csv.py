#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn CSV完全分析スクリプト
取得したlinkedin-2026-01-01.csvから正確な文字数・パターン分析
"""

import pandas as pd
import json
from pathlib import Path
import re

def analyze_linkedin_csv(csv_path: str) -> dict:
    """LinkedIn CSVから完全な文字数・パターン分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # 投稿本文は 'media-description' 列
    content_col = 'media-description'

    if content_col not in df.columns:
        return {'error': f'media-description列が見つかりません。利用可能な列: {df.columns.tolist()}'}

    # 文字数分析
    char_counts = []
    posts_data = []

    for idx, row in df.iterrows():
        text = str(row[content_col])
        if pd.notna(text) and text != 'nan' and len(text) > 10:  # 短すぎる投稿を除外
            char_count = len(text)
            char_counts.append(char_count)

            posts_data.append({
                'date': str(row['created-date']),
                'char_count': char_count,
                'text': text
            })

    # パターン分類
    def classify_pattern(text: str) -> str:
        # Pattern 3: ニュース引用（「〇〇氏は」「〇〇によると」「報道によると」）
        if re.search(r'(氏は|氏が|氏によれば|によると|報道によると|発表|述べた|明らかにした|断言した|提唱する|指摘する)', text[:150]):
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

    # 問いかけ終結チェック
    def check_question_ending(text: str) -> bool:
        # 最後の100文字を確認（長文対応）
        ending = text[-100:]

        question_patterns = [
            r'か？',
            r'でしょうか',
            r'ますか',
            r'ませんか',
            r'のでは',
            r'だろうか',
            r'はいかが',
            r'どう思いますか',
            r'いかがでしょうか',
            r'ではないか',
            r'のではないか'
        ]

        return any(re.search(pattern, ending) for pattern in question_patterns)

    # 企業名引用数カウント
    def count_company_mentions(text: str) -> int:
        company_patterns = [
            r'OpenAI',
            r'Google|グーグル',
            r'Microsoft|マイクロソフト',
            r'Tesla|テスラ',
            r'Anthropic|アンソロッピック',
            r'Meta',
            r'Apple',
            r'Amazon',
            r'NVIDIA|エヌビディア',
            r'Alibaba|アリババ',
            r'DeepSeek|ディープシーク',
            r'Gemini',
            r'ChatGPT',
            r'Claude',
            r'セコイア',
            r'ゴールドマン',
            r'a16z|A16z',
            r'ソフトバンク',
            r'Walmart|ウォルマート',
            r'エポックAI|Epoch AI',
            r'スペースX|SpaceX',
            r'LayerX|レイヤーエックス',
            r'トランスコスモス',
            r'DeepMind|ディープマインド',
            r'バクラク'
        ]

        count = 0
        for pattern in company_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)

        return count

    # 各投稿を分析
    patterns = {}
    question_endings = 0
    company_mentions_list = []

    for post in posts_data:
        text = post['text']

        # パターン分類
        pattern = classify_pattern(text)
        patterns[pattern] = patterns.get(pattern, 0) + 1
        post['pattern'] = pattern

        # 問いかけ終結
        has_question = check_question_ending(text)
        if has_question:
            question_endings += 1
        post['has_question_ending'] = has_question

        # 企業名引用
        companies = count_company_mentions(text)
        company_mentions_list.append(companies)
        post['company_mentions'] = companies

    # 結果集計
    return {
        'total_posts_analyzed': len(char_counts),
        'char_count_analysis': {
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
        },
        'pattern_classification': patterns,
        'question_ending': {
            'count': question_endings,
            'rate': question_endings / len(posts_data) * 100 if posts_data else 0,
            'benchmark_takano': '問いかけ終結 ほぼ必須（推定80%以上）'
        },
        'company_mentions': {
            'average': sum(company_mentions_list) / len(company_mentions_list) if company_mentions_list else 0,
            'total': sum(company_mentions_list),
            'benchmark_takano': 1.58,
            'gap': (sum(company_mentions_list) / len(company_mentions_list) - 1.58) if company_mentions_list else 0
        },
        'posts_data': posts_data
    }

if __name__ == '__main__':
    csv_path = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/X/linkedin-2026-01-01.csv'

    result = analyze_linkedin_csv(csv_path)

    # 結果を表示
    print("=" * 80)
    print("LinkedIn CSV完全分析レポート（データ制約なし）")
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

        # JSON出力（posts_dataは除外、サイズが大きすぎるため）
        output_data = {k: v for k, v in result.items() if k != 'posts_data'}
        output_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_csv_complete_analysis.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"詳細結果をJSONで保存: {output_path}")
