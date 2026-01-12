#!/usr/bin/env python3
"""
LinkedIn投稿分析スクリプト

Usage:
    python linkedin_analyzer.py --input takano_linkedin_posts.json
"""

import json
import re
from collections import Counter
from pathlib import Path
import statistics
from janome.tokenizer import Tokenizer


class LinkedInAnalyzer:
    """LinkedIn投稿テキスト分析"""

    # 構成パターン（7種類）
    PATTERNS = {
        'question_first': r'^[？?]|^(何|どう|なぜ|どの|いつ|誰)',
        'conclusion_last': r'(です|ます|でした|ました|だ|である)$',
        'bullet_points': r'[・•◦\-\*]\s',
        'numbered_list': r'^\d+[\.\)、]\s',
        'story_opening': r'^(先日|最近|今日|昨日|先週|去年)',
        'call_to_action': r'(ください|しましょう|いかがでしょうか|どう思|考えてみて)',
        'emoji_usage': r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
    }

    # ストップワード（除外する一般的な単語）
    STOPWORDS = {
        'する', 'ある', 'いる', 'なる', 'れる', 'られる', 'ない', 'せる',
        'させる', 'くれる', 'やる', 'くる', 'いく', 'もらう', 'こと', 'もの',
        'の', 'に', 'は', 'を', 'た', 'が', 'で', 'て', 'と', 'し', 'れ',
        'さ', 'ある', 'いる', 'も', 'する', 'から', 'な', 'こと', 'として',
        'い', 'や', 'れる', 'など', 'なっ', 'ない', 'この', 'ため', 'その',
        'あっ', 'よう', 'また', 'もの', 'という', 'あり', 'まで', 'られ',
        'なる', 'へ', 'か', 'だ', 'これ', 'によって', 'により', 'おり',
        'より', 'による', 'ず', 'なり', 'られる', 'において', 'ば', 'なかっ',
        'なく', 'しかし', 'について', 'せ', 'だっ', 'その後', 'できる',
        'それ', 'う', 'ので', 'なお', 'のみ', 'でき', 'き', 'つ', 'における',
        'および', 'いう', 'さらに', 'でも', 'ら', 'たり', 'その他', 'に関する',
        'たち', 'ます', 'ん', 'なら', 'に対して', '及び', 'これら', 'とも', 'ところ',
        'ここ'
    }

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.data = self._load_data()
        self.posts = self.data['posts']
        self.tokenizer = Tokenizer()

    def _load_data(self) -> dict:
        """JSONデータをロード"""
        with open(self.json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def analyze_statistics(self) -> dict:
        """文字数統計分析"""
        char_counts = [p['char_count'] for p in self.posts]

        # 分布作成（0-500, 501-1000, 1001-1500, 1501+）
        distribution = {
            '0-500': sum(1 for c in char_counts if c <= 500),
            '501-1000': sum(1 for c in char_counts if 501 <= c <= 1000),
            '1001-1500': sum(1 for c in char_counts if 1001 <= c <= 1500),
            '1501+': sum(1 for c in char_counts if c > 1500)
        }

        return {
            'char_count': {
                'mean': round(statistics.mean(char_counts), 1),
                'median': round(statistics.median(char_counts), 1),
                'min': min(char_counts),
                'max': max(char_counts),
                'std': round(statistics.stdev(char_counts), 1) if len(char_counts) > 1 else 0
            },
            'distribution': distribution,
            'total_posts': len(self.posts)
        }

    def classify_patterns(self) -> dict:
        """構成パターン分類（7パターン）"""
        results = {pattern: [] for pattern in self.PATTERNS.keys()}

        for i, post in enumerate(self.posts, 1):
            text = post['text']

            for pattern_name, pattern_regex in self.PATTERNS.items():
                if re.search(pattern_regex, text, re.MULTILINE):
                    results[pattern_name].append({
                        'post_index': i,
                        'post_id': post['post_id'],
                        'char_count': post['char_count'],
                        'preview': text[:100] + '...' if len(text) > 100 else text
                    })

        # 統計サマリー
        summary = {
            pattern: {
                'count': len(matches),
                'percentage': round(len(matches) / len(self.posts) * 100, 1),
                'avg_char_count': round(statistics.mean([m['char_count'] for m in matches]), 1) if matches else 0
            }
            for pattern, matches in results.items()
        }

        return {
            'matches': results,
            'summary': summary
        }

    def extract_keywords(self, top_n: int = 50) -> list:
        """頻出キーワード抽出（Janome形態素解析）"""
        all_words = []

        for post in self.posts:
            text = post['text']
            tokens = self.tokenizer.tokenize(text)

            for token in tokens:
                # 品詞情報を取得
                parts = str(token).split('\t')
                if len(parts) < 2:
                    continue

                word = parts[0]
                features = parts[1].split(',')
                pos = features[0]  # 品詞

                # 名詞、動詞、形容詞のみ抽出
                if pos in ['名詞', '動詞', '形容詞']:
                    base_form = features[6] if len(features) > 6 and features[6] != '*' else word

                    # ストップワード除外
                    if base_form not in self.STOPWORDS and len(base_form) > 1:
                        all_words.append(base_form)

        # 頻出上位N個
        counter = Counter(all_words)
        top_keywords = [
            {'word': word, 'count': count, 'pos': 'keyword'}
            for word, count in counter.most_common(top_n)
        ]

        return top_keywords

    def analyze_engagement(self) -> dict:
        """エンゲージメント相関分析（データ制限版）"""
        # エンゲージメントデータがないため、文字数ベースの分析
        sorted_posts = sorted(self.posts, key=lambda p: p['char_count'], reverse=True)
        top_20_percent = sorted_posts[:len(sorted_posts) // 5]

        # トップ20%の特徴分析
        top_patterns = {pattern: 0 for pattern in self.PATTERNS.keys()}

        for post in top_20_percent:
            text = post['text']
            for pattern_name, pattern_regex in self.PATTERNS.items():
                if re.search(pattern_regex, text, re.MULTILINE):
                    top_patterns[pattern_name] += 1

        return {
            'note': 'エンゲージメントデータ未取得のため、文字数トップ20%の投稿を分析',
            'top_performing_count': len(top_20_percent),
            'avg_char_count_top20': round(statistics.mean([p['char_count'] for p in top_20_percent]), 1),
            'pattern_frequency_top20': top_patterns,
            'top_posts': [
                {
                    'post_id': p['post_id'],
                    'char_count': p['char_count'],
                    'preview': p['text'][:150] + '...' if len(p['text']) > 150 else p['text']
                }
                for p in top_20_percent[:10]
            ]
        }

    def generate_report(self, output_path: str):
        """分析レポート生成（JSON形式）"""
        report = {
            'statistics': self.analyze_statistics(),
            'patterns': self.classify_patterns(),
            'keywords': self.extract_keywords(50),
            'engagement': self.analyze_engagement()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"✅ Analysis report saved: {output_path}")
        return report

    def print_summary(self):
        """サマリーをコンソール出力"""
        stats = self.analyze_statistics()
        patterns = self.classify_patterns()
        keywords = self.extract_keywords(20)

        print("=" * 60)
        print("LinkedIn投稿分析サマリー")
        print("=" * 60)
        print(f"\n📊 基本統計:")
        print(f"  総投稿数: {stats['total_posts']}件")
        print(f"  平均文字数: {stats['char_count']['mean']}字")
        print(f"  中央値: {stats['char_count']['median']}字")
        print(f"  最小-最大: {stats['char_count']['min']}-{stats['char_count']['max']}字")
        print(f"  標準偏差: {stats['char_count']['std']}")

        print(f"\n📈 文字数分布:")
        for range_label, count in stats['distribution'].items():
            print(f"  {range_label}字: {count}件")

        print(f"\n🎨 構成パターン:")
        for pattern, data in patterns['summary'].items():
            print(f"  {pattern}: {data['count']}件 ({data['percentage']}%)")

        print(f"\n🔑 頻出キーワード（Top 20）:")
        for i, kw in enumerate(keywords, 1):
            print(f"  {i}. {kw['word']} ({kw['count']}回)")

        print("=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="LinkedIn投稿分析")
    parser.add_argument('--input', required=True, help='入力JSONファイル')
    parser.add_argument('--output', default=None, help='出力JSONファイル（デフォルト: analysis_report.json）')

    args = parser.parse_args()

    # 出力パス決定
    if args.output is None:
        input_path = Path(args.input)
        output_path = input_path.parent / 'analysis_report.json'
    else:
        output_path = args.output

    # 分析実行
    analyzer = LinkedInAnalyzer(args.input)
    analyzer.print_summary()
    analyzer.generate_report(str(output_path))


if __name__ == "__main__":
    main()
