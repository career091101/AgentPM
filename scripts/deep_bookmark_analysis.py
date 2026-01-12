#!/usr/bin/env python3
"""
Xブックマーク深掘り分析スクリプト

詳細分析項目：
1. 文体・表現パターン（語尾、トーン、レトリック）
2. セマンティック分析（トピッククラスタリング）
3. エンゲージメント相関分析（いいね・RT・返信の関係）
4. 投稿者プロファイリング（専門性、発信パターン）
5. 時系列トレンド分析（トピック変遷）
6. 情報の深さ・質的評価（一次情報 vs 二次情報）
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from datetime import datetime
import statistics

# パス設定
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0")
INPUT_FILE = BASE_DIR / "Flow/202512/2025-12-31/x_bookmarks_data_fulltext.json"
OUTPUT_DIR = BASE_DIR / "Flow/202512/2025-12-31"

def load_bookmarks():
    """ブックマークデータを読み込み"""
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['bookmarks'], data['metadata']

# ========================================
# 1. 文体・表現パターン分析
# ========================================

def analyze_writing_style(bookmarks):
    """文体・表現パターンの詳細分析"""
    print("\n=== 1. 文体・表現パターン分析 ===\n")

    # 語尾パターン
    sentence_endings = Counter()
    # トーン（感嘆符、疑問符、絵文字の頻度）
    tone_markers = {
        'exclamation': 0,  # ！
        'question': 0,      # ？
        'emoji': 0,         # 絵文字
        'ellipsis': 0       # ...
    }
    # レトリック手法
    rhetoric_patterns = {
        'question_form': 0,      # 問いかけ形式
        'comparison': 0,         # 比較（vs, より, 〜に比べて）
        'emphasis': 0,           # 強調（ヤバい, すごい, 最高）
        'negation': 0,           # 否定形からの肯定
        'imperative': 0,         # 命令形・推奨形
        'quotation': 0           # 引用符使用
    }

    # 文の長さ分布
    sentence_lengths = []

    for bm in bookmarks:
        text = bm.get('text', '')

        # 語尾パターン（文末の2文字）
        sentences = re.split(r'[。！？\n]', text)
        for sent in sentences:
            if len(sent) >= 2:
                ending = sent[-2:]
                sentence_endings[ending] += 1
                sentence_lengths.append(len(sent))

        # トーン分析
        tone_markers['exclamation'] += text.count('！') + text.count('!')
        tone_markers['question'] += text.count('？') + text.count('?')
        tone_markers['emoji'] += len(re.findall(r'[\U0001F300-\U0001F9FF]', text))
        tone_markers['ellipsis'] += text.count('...') + text.count('…')

        # レトリック手法
        if re.search(r'[？?]', text):
            rhetoric_patterns['question_form'] += 1
        if re.search(r'vs|より|に比べて|〜に対して', text, re.IGNORECASE):
            rhetoric_patterns['comparison'] += 1
        if re.search(r'ヤバい|すごい|最高|驚き|衝撃', text):
            rhetoric_patterns['emphasis'] += 1
        if re.search(r'ではない|じゃない.*実は|〜ではなく', text):
            rhetoric_patterns['negation'] += 1
        if re.search(r'べき|してください|おすすめ|試して|使って', text):
            rhetoric_patterns['imperative'] += 1
        if text.count('「') > 0 or text.count('"') > 0:
            rhetoric_patterns['quotation'] += 1

    # 結果
    result = {
        'sentence_endings_top20': sentence_endings.most_common(20),
        'tone_markers': tone_markers,
        'rhetoric_patterns': rhetoric_patterns,
        'sentence_length_stats': {
            'average': round(statistics.mean(sentence_lengths), 1) if sentence_lengths else 0,
            'median': round(statistics.median(sentence_lengths), 1) if sentence_lengths else 0,
            'max': max(sentence_lengths) if sentence_lengths else 0,
            'min': min(sentence_lengths) if sentence_lengths else 0
        }
    }

    print(f"【語尾パターン TOP 20】")
    for ending, count in result['sentence_endings_top20']:
        print(f"  '{ending}': {count}回")

    print(f"\n【トーンマーカー】")
    for marker, count in result['tone_markers'].items():
        print(f"  {marker}: {count}回")

    print(f"\n【レトリック手法】")
    for pattern, count in result['rhetoric_patterns'].items():
        print(f"  {pattern}: {count}件 ({round(count/len(bookmarks)*100, 1)}%)")

    print(f"\n【文の長さ統計】")
    print(f"  平均: {result['sentence_length_stats']['average']}文字")
    print(f"  中央値: {result['sentence_length_stats']['median']}文字")

    return result

# ========================================
# 2. エンゲージメント相関分析
# ========================================

def analyze_engagement_correlation(bookmarks):
    """エンゲージメント指標の詳細相関分析"""
    print("\n=== 2. エンゲージメント相関分析 ===\n")

    # データ収集
    likes = []
    retweets = []
    replies = []
    engagement_scores = []  # いいね + RT*3 + 返信*5

    # カテゴリ別エンゲージメント
    category_engagement = defaultdict(lambda: {'likes': [], 'retweets': [], 'replies': []})

    # 構造パターン別エンゲージメント
    structure_engagement = defaultdict(lambda: {'likes': [], 'count': 0})

    for bm in bookmarks:
        text = bm.get('text', '')
        like = bm['engagement'].get('likes', 0)
        rt = bm['engagement'].get('retweets', 0)
        reply = bm['engagement'].get('replies', 0)

        likes.append(like)
        retweets.append(rt)
        replies.append(reply)
        engagement_scores.append(like + rt*3 + reply*5)

        # カテゴリ判定
        if any(kw in text.lower() for kw in ['claude', 'chatgpt', 'gpt', 'ai', 'llm']):
            category = 'AI・生成AI'
        elif any(kw in text.lower() for kw in ['startup', 'pmf', 'saas', 'ビジネス']):
            category = 'ビジネス・起業'
        else:
            category = 'その他'

        category_engagement[category]['likes'].append(like)
        category_engagement[category]['retweets'].append(rt)
        category_engagement[category]['replies'].append(reply)

        # 構造パターン別
        if re.search(r'[①②③④⑤123456789]\s*[．.]', text):
            structure_engagement['リスト形式']['likes'].append(like)
            structure_engagement['リスト形式']['count'] += 1
        if re.search(r'\d+%|\d+倍', text):
            structure_engagement['数値データ']['likes'].append(like)
            structure_engagement['数値データ']['count'] += 1
        if '引用' in text or 'RT' in text.upper():
            structure_engagement['引用・RT']['likes'].append(like)
            structure_engagement['引用・RT']['count'] += 1

    # 相関係数計算（簡易版）
    def pearson_correlation(x, y):
        n = len(x)
        if n == 0:
            return 0
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n)) ** 0.5
        denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n)) ** 0.5
        if denominator_x == 0 or denominator_y == 0:
            return 0
        return numerator / (denominator_x * denominator_y)

    result = {
        'basic_stats': {
            'likes': {
                'mean': round(statistics.mean(likes), 1),
                'median': round(statistics.median(likes), 1),
                'stdev': round(statistics.stdev(likes), 1) if len(likes) > 1 else 0,
                'max': max(likes),
                'min': min(likes)
            },
            'retweets': {
                'mean': round(statistics.mean(retweets), 1),
                'median': round(statistics.median(retweets), 1),
                'max': max(retweets)
            },
            'replies': {
                'mean': round(statistics.mean(replies), 1),
                'median': round(statistics.median(replies), 1),
                'max': max(replies)
            }
        },
        'correlations': {
            'likes_vs_retweets': round(pearson_correlation(likes, retweets), 3),
            'likes_vs_replies': round(pearson_correlation(likes, replies), 3),
            'retweets_vs_replies': round(pearson_correlation(retweets, replies), 3)
        },
        'category_engagement': {
            cat: {
                'avg_likes': round(statistics.mean(data['likes']), 1) if data['likes'] else 0,
                'avg_retweets': round(statistics.mean(data['retweets']), 1) if data['retweets'] else 0,
                'avg_replies': round(statistics.mean(data['replies']), 1) if data['replies'] else 0,
                'count': len(data['likes'])
            }
            for cat, data in category_engagement.items()
        },
        'structure_engagement': {
            struct: {
                'avg_likes': round(statistics.mean(data['likes']), 1) if data['likes'] else 0,
                'count': data['count']
            }
            for struct, data in structure_engagement.items()
        }
    }

    print(f"【基本統計】")
    print(f"  いいね: 平均 {result['basic_stats']['likes']['mean']}, 中央値 {result['basic_stats']['likes']['median']}, 最大 {result['basic_stats']['likes']['max']}")
    print(f"  RT: 平均 {result['basic_stats']['retweets']['mean']}, 中央値 {result['basic_stats']['retweets']['median']}, 最大 {result['basic_stats']['retweets']['max']}")
    print(f"  返信: 平均 {result['basic_stats']['replies']['mean']}, 中央値 {result['basic_stats']['replies']['median']}, 最大 {result['basic_stats']['replies']['max']}")

    print(f"\n【相関係数】")
    print(f"  いいね vs RT: {result['correlations']['likes_vs_retweets']}")
    print(f"  いいね vs 返信: {result['correlations']['likes_vs_replies']}")
    print(f"  RT vs 返信: {result['correlations']['retweets_vs_replies']}")

    print(f"\n【カテゴリ別エンゲージメント】")
    for cat, data in result['category_engagement'].items():
        print(f"  {cat}: 平均いいね {data['avg_likes']}, 平均RT {data['avg_retweets']}, 件数 {data['count']}")

    print(f"\n【構造パターン別エンゲージメント】")
    for struct, data in result['structure_engagement'].items():
        print(f"  {struct}: 平均いいね {data['avg_likes']}, 件数 {data['count']}")

    return result

# ========================================
# 3. 投稿者プロファイリング
# ========================================

def analyze_author_profiling(bookmarks):
    """投稿者の詳細プロファイリング"""
    print("\n=== 3. 投稿者プロファイリング ===\n")

    author_profiles = defaultdict(lambda: {
        'post_count': 0,
        'total_likes': 0,
        'total_retweets': 0,
        'topics': Counter(),
        'avg_text_length': []
    })

    for bm in bookmarks:
        author = bm.get('author_username', 'unknown')
        text = bm.get('text', '')
        likes = bm['engagement'].get('likes', 0)
        retweets = bm['engagement'].get('retweets', 0)

        profile = author_profiles[author]
        profile['post_count'] += 1
        profile['total_likes'] += likes
        profile['total_retweets'] += retweets
        profile['avg_text_length'].append(len(text))

        # トピック判定
        if 'claude' in text.lower():
            profile['topics']['Claude'] += 1
        if 'gpt' in text.lower() or 'chatgpt' in text.lower():
            profile['topics']['GPT'] += 1
        if 'openai' in text.lower():
            profile['topics']['OpenAI'] += 1
        if 'gemini' in text.lower():
            profile['topics']['Gemini'] += 1
        if any(kw in text.lower() for kw in ['agent', 'エージェント']):
            profile['topics']['Agent'] += 1

    # TOP 20 投稿者の詳細プロファイル
    top_authors = sorted(author_profiles.items(), key=lambda x: x[1]['post_count'], reverse=True)[:20]

    result = {
        'top_20_profiles': []
    }

    print(f"【TOP 20 投稿者プロファイル】\n")
    for author, profile in top_authors:
        avg_likes = round(profile['total_likes'] / profile['post_count'], 1)
        avg_text_len = round(statistics.mean(profile['avg_text_length']), 1) if profile['avg_text_length'] else 0
        top_topics = profile['topics'].most_common(3)

        profile_data = {
            'username': author,
            'post_count': profile['post_count'],
            'avg_likes': avg_likes,
            'avg_text_length': avg_text_len,
            'top_topics': [{'topic': t[0], 'count': t[1]} for t in top_topics],
            'specialization': top_topics[0][0] if top_topics else 'General'
        }
        result['top_20_profiles'].append(profile_data)

        print(f"@{author}:")
        print(f"  投稿数: {profile['post_count']}件")
        print(f"  平均いいね: {avg_likes}")
        print(f"  平均文字数: {avg_text_len}")
        print(f"  主要トピック: {', '.join([f'{t[0]}({t[1]})' for t in top_topics])}")
        print(f"  専門性: {profile_data['specialization']}")
        print()

    return result

# ========================================
# 4. 時系列トレンド分析
# ========================================

def analyze_time_trends(bookmarks):
    """時系列トレンド分析"""
    print("\n=== 4. 時系列トレンド分析 ===\n")

    # 日付別トピック
    date_topics = defaultdict(lambda: Counter())
    # 月別集計
    monthly_counts = Counter()
    weekly_counts = Counter()

    for bm in bookmarks:
        posted_at = bm.get('posted_at', '')
        text = bm.get('text', '')

        if not posted_at:
            continue

        try:
            dt = datetime.fromisoformat(posted_at.replace('Z', '+00:00'))
            month_key = dt.strftime('%Y-%m')
            week_key = dt.strftime('%Y-W%U')

            monthly_counts[month_key] += 1
            weekly_counts[week_key] += 1

            # トピック抽出
            if 'claude' in text.lower():
                date_topics[month_key]['Claude'] += 1
            if 'gpt' in text.lower():
                date_topics[month_key]['GPT'] += 1
            if 'gemini' in text.lower():
                date_topics[month_key]['Gemini'] += 1
        except:
            continue

    result = {
        'monthly_distribution': dict(monthly_counts.most_common()),
        'weekly_distribution': dict(weekly_counts.most_common(10)),
        'monthly_topics': {month: dict(topics.most_common(5)) for month, topics in date_topics.items()}
    }

    print(f"【月別ブックマーク数】")
    for month, count in sorted(monthly_counts.items()):
        print(f"  {month}: {count}件")

    print(f"\n【週別ブックマーク数 TOP 10】")
    for week, count in result['weekly_distribution'].items():
        print(f"  {week}: {count}件")

    print(f"\n【月別トピックトレンド】")
    for month in sorted(date_topics.keys()):
        topics = date_topics[month].most_common(3)
        print(f"  {month}: {', '.join([f'{t[0]}({t[1]})' for t in topics])}")

    return result

# ========================================
# 5. 情報の深さ・質的評価
# ========================================

def analyze_information_depth(bookmarks):
    """情報の深さ・質的評価"""
    print("\n=== 5. 情報の深さ・質的評価 ===\n")

    depth_categories = {
        'primary_source': 0,      # 一次情報（公式発表、実装者の体験）
        'secondary_source': 0,    # 二次情報（解説記事、まとめ）
        'tutorial': 0,            # チュートリアル・ガイド
        'news': 0,                # ニュース・アナウンス
        'opinion': 0,             # 意見・考察
        'data_driven': 0          # データドリブン（数値分析）
    }

    # 実装可能性
    actionability = {
        'immediately_actionable': 0,  # すぐ実行可能
        'requires_setup': 0,          # セットアップ必要
        'conceptual_only': 0          # 概念的のみ
    }

    # 情報の独自性
    uniqueness = {
        'unique_insight': 0,      # 独自の洞察
        'curated_info': 0,        # キュレーション
        'repost': 0               # 再投稿・拡散
    }

    examples_by_depth = defaultdict(list)

    for bm in bookmarks:
        text = bm.get('text', '')
        author = bm.get('author_username', '')
        likes = bm['engagement'].get('likes', 0)

        # 一次情報判定
        if any(kw in text for kw in ['発表', 'リリース', '公開', '実装した', 'やってみた', '作った']):
            depth_categories['primary_source'] += 1
            if len(examples_by_depth['primary_source']) < 3:
                examples_by_depth['primary_source'].append({'text': text[:100], 'author': author, 'likes': likes})

        # 二次情報判定
        if any(kw in text for kw in ['まとめ', '解説', '紹介', 'について', '〜とは']):
            depth_categories['secondary_source'] += 1

        # チュートリアル判定
        if any(kw in text for kw in ['方法', 'ガイド', '手順', 'チュートリアル', 'やり方']):
            depth_categories['tutorial'] += 1
            if len(examples_by_depth['tutorial']) < 3:
                examples_by_depth['tutorial'].append({'text': text[:100], 'author': author, 'likes': likes})

        # ニュース判定
        if any(kw in text for kw in ['速報', 'ニュース', '〜が発表', '〜がローンチ']):
            depth_categories['news'] += 1

        # 意見・考察判定
        if any(kw in text for kw in ['思う', '考える', '感じる', '〜べき', '〜だと思います']):
            depth_categories['opinion'] += 1

        # データドリブン判定
        if re.search(r'\d+%|\d+倍|\d+件|\d+人', text):
            depth_categories['data_driven'] += 1
            if len(examples_by_depth['data_driven']) < 3:
                examples_by_depth['data_driven'].append({'text': text[:100], 'author': author, 'likes': likes})

        # 実装可能性判定
        if any(kw in text for kw in ['こちら', 'リンク', 'URL', 'ダウンロード', 'インストール']):
            actionability['immediately_actionable'] += 1
        elif any(kw in text for kw in ['セットアップ', '設定', '環境構築']):
            actionability['requires_setup'] += 1
        else:
            actionability['conceptual_only'] += 1

        # 独自性判定
        if any(kw in text for kw in ['独自', 'オリジナル', '新しい視点', '〜という考え方']):
            uniqueness['unique_insight'] += 1
        elif any(kw in text for kw in ['まとめ', 'キュレーション', '整理']):
            uniqueness['curated_info'] += 1
        elif 'RT' in text or '引用' in text:
            uniqueness['repost'] += 1

    result = {
        'depth_categories': depth_categories,
        'actionability': actionability,
        'uniqueness': uniqueness,
        'examples': examples_by_depth
    }

    total = len(bookmarks)
    print(f"【情報の深さカテゴリ】")
    for cat, count in depth_categories.items():
        print(f"  {cat}: {count}件 ({round(count/total*100, 1)}%)")

    print(f"\n【実装可能性】")
    for cat, count in actionability.items():
        print(f"  {cat}: {count}件 ({round(count/total*100, 1)}%)")

    print(f"\n【独自性】")
    for cat, count in uniqueness.items():
        print(f"  {cat}: {count}件 ({round(count/total*100, 1)}%)")

    print(f"\n【カテゴリ別例】")
    for cat, examples in examples_by_depth.items():
        if examples:
            print(f"\n  {cat}:")
            for ex in examples:
                print(f"    - {ex['text']}... (@{ex['author']}, {ex['likes']}いいね)")

    return result

# ========================================
# メイン実行
# ========================================

def main():
    print("=" * 80)
    print("Xブックマーク深掘り分析")
    print("=" * 80)

    bookmarks, metadata = load_bookmarks()
    print(f"\n総ブックマーク数: {len(bookmarks)} 件")
    print(f"スクレイピング日時: {metadata['scrape_date']}\n")

    # 各分析の実行
    results = {
        'metadata': {
            'analyzed_at': datetime.now().isoformat(),
            'total_bookmarks': len(bookmarks)
        }
    }

    results['writing_style'] = analyze_writing_style(bookmarks)
    results['engagement_correlation'] = analyze_engagement_correlation(bookmarks)
    results['author_profiling'] = analyze_author_profiling(bookmarks)
    results['time_trends'] = analyze_time_trends(bookmarks)
    results['information_depth'] = analyze_information_depth(bookmarks)

    # JSON保存
    output_file = OUTPUT_DIR / "deep_bookmark_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"深掘り分析完了！")
    print(f"出力ファイル: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
