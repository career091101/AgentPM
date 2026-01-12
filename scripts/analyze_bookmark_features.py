#!/usr/bin/env python3
"""
Xブックマーク特徴抽出スクリプト

823件のブックマーク投稿を全て読み込んで、以下の特徴を抽出：
1. テキストパターン（文体、構造、文字数分布）
2. トピック・キーワード（頻出語、専門用語）
3. エンゲージメント特性（いいね・RT・返信の相関）
4. 投稿者の特徴（専門性、発信スタイル）
5. コンテンツタイプ（技術解説、事例紹介、ハウツー、ニュース等）
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from datetime import datetime
import unicodedata

# パス設定
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0")
INPUT_FILE = BASE_DIR / "Flow/202512/2025-12-31/x_bookmarks_data_fulltext.json"
OUTPUT_DIR = BASE_DIR / "Flow/202512/2025-12-31"

# 日本語ストップワード（一般的な助詞・助動詞等）
STOP_WORDS = {
    'の', 'に', 'は', 'を', 'た', 'が', 'で', 'て', 'と', 'し', 'れ', 'さ', 'ある', 'いる',
    'も', 'する', 'から', 'な', 'こと', 'として', 'い', 'や', 'れる', 'など', 'なっ',
    'ない', 'この', 'ため', 'その', 'あっ', 'よう', 'また', 'もの', 'という', 'あり',
    'まで', 'られ', 'なる', 'へ', 'か', 'だ', 'これ', 'によって', 'により', 'おり',
    'より', 'による', 'ず', 'なり', 'られる', 'において', 'ば', 'なかっ', 'なく',
    'しかし', 'について', 'せ', 'だっ', 'その後', 'できる', 'それ', 'う', 'ので',
    'なお', 'のみ', 'でき', 'き', 'つ', 'における', 'および', 'いう', 'さらに',
    'でも', 'ら', 'たり', 'その他', 'に関する', 'たち', 'ます', 'ん', 'なら',
    'に対して', '特に', 'せる', 'および', 'あるいは', 'まし', 'ものの', 'といった',
    'のは', 'くる', '的', '中', 'rt', 'x', 'com'
}

def load_bookmarks():
    """ブックマークデータを読み込み"""
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['bookmarks'], data['metadata']

def extract_keywords(text, top_n=100):
    """テキストからキーワードを抽出（簡易版）"""
    # URLを除去
    text = re.sub(r'https?://[^\s]+', '', text)
    text = re.sub(r'x\.com/[^\s]+', '', text)

    # メンション、ハッシュタグを除去
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)

    # 記号を除去（句読点は残す）
    text = re.sub(r'[「」『』（）()【】\[\]｜・…~〜]', ' ', text)

    # 単語に分割（空白、句読点で分割）
    words = re.findall(r'[ぁ-んァ-ヶー一-龠a-zA-Z0-9]+', text)

    # ストップワード除去 & 2文字以上
    words = [w.lower() for w in words if len(w) >= 2 and w.lower() not in STOP_WORDS]

    return words

def categorize_content_type(text):
    """コンテンツタイプを分類"""
    text_lower = text.lower()

    # パターンマッチング
    if any(keyword in text_lower for keyword in ['claude', 'chatgpt', 'gpt', 'llm', 'ai', '生成ai', 'エージェント']):
        return 'AI・生成AI'
    elif any(keyword in text_lower for keyword in ['startup', 'スタートアップ', 'pmf', 'saas', 'ビジネス', '起業']):
        return 'ビジネス・起業'
    elif any(keyword in text_lower for keyword in ['typescript', 'react', 'python', 'docker', 'プログラミング', 'コード', '開発']):
        return '開発・エンジニアリング'
    elif any(keyword in text_lower for keyword in ['ux', 'ui', 'デザイン', 'figma', 'プロダクト']):
        return 'デザイン・UX'
    elif any(keyword in text_lower for keyword in ['効率化', '生産性', 'ノート', 'タスク管理']):
        return '生産性・自己啓発'
    else:
        return 'その他'

def detect_content_structure(text):
    """投稿の構造パターンを検出"""
    features = {
        'has_list': bool(re.search(r'[①②③④⑤⑥⑦⑧⑨⑩123456789]\s*[．.]', text) or
                        re.search(r'\n[-・]\s', text)),
        'has_emoji': bool(re.search(r'[\U0001F300-\U0001F9FF]', text)),
        'has_url': bool(re.search(r'https?://', text)),
        'has_quote': '引用' in text or 'RT' in text.upper(),
        'has_code': bool(re.search(r'```|`[^`]+`', text)),
        'has_numbers': bool(re.search(r'\d+%|\d+倍|\d+円|\d+件', text)),
        'is_thread': '🧵' in text or 'スレッド' in text,
        'is_tutorial': any(keyword in text for keyword in ['方法', '手順', 'やり方', '完全ガイド', 'チュートリアル']),
        'is_announcement': any(keyword in text for keyword in ['発表', 'リリース', '公開', 'ローンチ'])
    }
    return features

def analyze_all_bookmarks():
    """全ブックマークを分析"""
    bookmarks, metadata = load_bookmarks()

    print(f"=== Xブックマーク特徴抽出開始 ===")
    print(f"総件数: {len(bookmarks)} 件")
    print(f"スクレイピング日時: {metadata['scrape_date']}")
    print()

    # 統計データ収集
    all_keywords = []
    category_counter = Counter()
    structure_stats = defaultdict(int)
    engagement_by_category = defaultdict(list)
    author_posts = defaultdict(int)
    text_lengths = []

    # 特徴的な投稿パターンの例を保存
    examples_by_pattern = defaultdict(list)

    for i, bm in enumerate(bookmarks):
        text = bm.get('text', '')
        likes = bm['engagement'].get('likes', 0)
        retweets = bm['engagement'].get('retweets', 0)
        replies = bm['engagement'].get('replies', 0)
        author = bm.get('author_username', 'unknown')

        # キーワード抽出
        keywords = extract_keywords(text)
        all_keywords.extend(keywords)

        # カテゴリ分類
        category = categorize_content_type(text)
        category_counter[category] += 1
        engagement_by_category[category].append(likes)

        # 構造パターン検出
        structure = detect_content_structure(text)
        for key, value in structure.items():
            if value:
                structure_stats[key] += 1
                # 例を保存（各パターン最大5件）
                if len(examples_by_pattern[key]) < 5:
                    examples_by_pattern[key].append({
                        'text': text[:200],
                        'author': author,
                        'likes': likes,
                        'url': bm.get('url', '')
                    })

        # 投稿者カウント
        author_posts[author] += 1

        # テキスト長
        text_lengths.append(len(text))

        if (i + 1) % 100 == 0:
            print(f"処理中... {i + 1}/{len(bookmarks)} 件")

    # 結果集計
    keyword_counter = Counter(all_keywords)
    top_keywords = keyword_counter.most_common(50)
    top_authors = sorted(author_posts.items(), key=lambda x: x[1], reverse=True)[:20]

    # エンゲージメント統計
    avg_engagement_by_category = {
        cat: sum(likes) / len(likes) if likes else 0
        for cat, likes in engagement_by_category.items()
    }

    # テキスト長統計
    avg_text_length = sum(text_lengths) / len(text_lengths)

    # レポート生成
    report = {
        'metadata': {
            'analyzed_at': datetime.now().isoformat(),
            'total_bookmarks': len(bookmarks),
            'unique_authors': len(author_posts),
            'analysis_version': '1.0.0'
        },
        'keyword_analysis': {
            'top_50_keywords': [{'word': w, 'count': c} for w, c in top_keywords],
            'total_unique_keywords': len(keyword_counter)
        },
        'category_distribution': {
            cat: {
                'count': count,
                'percentage': round(count / len(bookmarks) * 100, 1),
                'avg_likes': round(avg_engagement_by_category.get(cat, 0), 1)
            }
            for cat, count in category_counter.most_common()
        },
        'content_structure': {
            pattern: {
                'count': count,
                'percentage': round(count / len(bookmarks) * 100, 1),
                'examples': examples_by_pattern[pattern]
            }
            for pattern, count in sorted(structure_stats.items(), key=lambda x: x[1], reverse=True)
        },
        'author_analysis': {
            'top_20_authors': [
                {'username': author, 'post_count': count, 'percentage': round(count / len(bookmarks) * 100, 1)}
                for author, count in top_authors
            ]
        },
        'text_statistics': {
            'average_length': round(avg_text_length, 1),
            'min_length': min(text_lengths),
            'max_length': max(text_lengths)
        }
    }

    # JSON保存
    output_file = OUTPUT_DIR / "bookmark_features_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n=== 分析完了 ===")
    print(f"出力ファイル: {output_file}")

    # サマリー表示
    print(f"\n【カテゴリ分布】")
    for cat, data in report['category_distribution'].items():
        print(f"  {cat}: {data['count']}件 ({data['percentage']}%) - 平均いいね {data['avg_likes']}")

    print(f"\n【TOP 20 キーワード】")
    for kw in report['keyword_analysis']['top_50_keywords'][:20]:
        print(f"  {kw['word']}: {kw['count']}回")

    print(f"\n【コンテンツ構造パターン】")
    for pattern, data in list(report['content_structure'].items())[:10]:
        print(f"  {pattern}: {data['count']}件 ({data['percentage']}%)")

    print(f"\n【TOP 10 投稿者】")
    for author in report['author_analysis']['top_20_authors'][:10]:
        print(f"  @{author['username']}: {author['post_count']}件 ({author['percentage']}%)")

    return report

if __name__ == "__main__":
    report = analyze_all_bookmarks()
