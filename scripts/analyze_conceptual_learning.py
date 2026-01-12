#!/usr/bin/env python3
"""
概念的学習の詳細分析

94.5%が「概念的のみ」という発見の深掘り：
1. 概念的 vs 実装可能の具体例抽出
2. 概念的学習の種類分類（理論、事例、ベストプラクティス等）
3. なぜ概念的なのか（学習スタイル分析）
4. 概念→実装の橋渡しパターン
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

# パス設定
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0")
INPUT_FILE = BASE_DIR / "Flow/202512/2025-12-31/x_bookmarks_data_fulltext.json"
OUTPUT_DIR = BASE_DIR / "Flow/202512/2025-12-31"

def load_bookmarks():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['bookmarks']

def classify_conceptual_type(text):
    """概念的学習の種類を分類"""
    types = []

    # 1. 理論・原理
    if any(kw in text for kw in ['原理', '理論', '仕組み', 'とは', 'について', '解説', 'なぜ']):
        types.append('理論・原理')

    # 2. 事例紹介・実践報告
    if any(kw in text for kw in ['やってみた', '使ってみた', '試した', '結果', '〇〇した']):
        types.append('事例紹介')

    # 3. ベストプラクティス・ノウハウ
    if any(kw in text for kw in ['ベストプラクティス', 'Tips', 'コツ', 'ポイント', '注意点']):
        types.append('ベストプラクティス')

    # 4. トレンド・ニュース
    if any(kw in text for kw in ['発表', 'リリース', '公開', 'ローンチ', '速報', 'ニュース']):
        types.append('トレンド・ニュース')

    # 5. 比較・分析
    if any(kw in text for kw in ['vs', 'より', 'に比べて', '比較', '違い', '差']):
        types.append('比較・分析')

    # 6. 思考・考察
    if any(kw in text for kw in ['思う', '考える', '感じる', '〜べき', '視点', '洞察']):
        types.append('思考・考察')

    # 7. まとめ・キュレーション
    if any(kw in text for kw in ['まとめ', 'まとめました', '〇選', 'リスト', '一覧']):
        types.append('まとめ')

    return types if types else ['その他']

def analyze_actionability_detail(text):
    """実装可能性の詳細分類"""

    # すぐ実装可能（具体的な手順・コード・リンクあり）
    immediately_actionable_signals = [
        bool(re.search(r'https?://[^\s]+', text)),  # URL
        bool(re.search(r'```|`[^`]+`', text)),       # コードブロック
        'こちら' in text or 'リンク' in text,
        'ダウンロード' in text or 'インストール' in text,
        '手順' in text and '1' in text,              # ステップ手順
    ]

    # セットアップ必要（環境構築・設定が必要）
    requires_setup_signals = [
        '設定' in text,
        '環境構築' in text,
        'セットアップ' in text,
        '準備' in text,
    ]

    # 概念的のみ（理解・知識獲得が主目的）
    conceptual_signals = [
        '理解' in text,
        '知識' in text,
        '学ぶ' in text or '学習' in text,
        '考える' in text,
        '〜とは' in text,
    ]

    actionability_score = sum(immediately_actionable_signals)
    setup_score = sum(requires_setup_signals)
    conceptual_score = sum(conceptual_signals)

    if actionability_score >= 2:
        return 'immediately_actionable', actionability_score
    elif setup_score >= 1:
        return 'requires_setup', setup_score
    else:
        return 'conceptual_only', conceptual_score

def extract_learning_value(text):
    """学習価値の種類を抽出"""
    values = []

    # 知識獲得
    if any(kw in text for kw in ['知る', '理解', '学ぶ', '〜とは']):
        values.append('知識獲得')

    # スキル習得
    if any(kw in text for kw in ['できる', '方法', 'やり方', '手順']):
        values.append('スキル習得')

    # トレンド把握
    if any(kw in text for kw in ['最新', 'トレンド', '動向', '変化']):
        values.append('トレンド把握')

    # 視野拡大
    if any(kw in text for kw in ['視点', '観点', '考え方', 'アプローチ']):
        values.append('視野拡大')

    # 意思決定支援
    if any(kw in text for kw in ['選ぶ', '判断', '比較', '検討']):
        values.append('意思決定支援')

    return values if values else ['その他']

def main():
    print("=" * 80)
    print("概念的学習の詳細分析")
    print("=" * 80)

    bookmarks = load_bookmarks()

    # 統計データ
    conceptual_types = Counter()
    actionability_distribution = Counter()
    learning_values = Counter()

    # カテゴリ別の実装可能性
    category_actionability = defaultdict(lambda: defaultdict(int))

    # 具体例収集
    examples = {
        'immediately_actionable': [],
        'requires_setup': [],
        'conceptual_only_high_value': [],  # 高エンゲージメントの概念的投稿
        'conceptual_only_theory': [],       # 理論型
        'conceptual_only_case': [],         # 事例型
        'conceptual_only_trend': [],        # トレンド型
    }

    for bm in bookmarks:
        text = bm.get('text', '')
        likes = bm['engagement'].get('likes', 0)
        author = bm.get('author_username', '')
        url = bm.get('url', '')

        # 概念的学習の種類
        types = classify_conceptual_type(text)
        for t in types:
            conceptual_types[t] += 1

        # 実装可能性の詳細
        actionability, score = analyze_actionability_detail(text)
        actionability_distribution[actionability] += 1

        # 学習価値
        values = extract_learning_value(text)
        for v in values:
            learning_values[v] += 1

        # カテゴリ判定
        if any(kw in text.lower() for kw in ['claude', 'gpt', 'ai']):
            category = 'AI・生成AI'
        else:
            category = 'その他'
        category_actionability[category][actionability] += 1

        # 具体例収集
        example = {
            'text': text[:200],
            'author': author,
            'likes': likes,
            'url': url,
            'types': types
        }

        if actionability == 'immediately_actionable' and len(examples['immediately_actionable']) < 5:
            examples['immediately_actionable'].append(example)
        elif actionability == 'requires_setup' and len(examples['requires_setup']) < 5:
            examples['requires_setup'].append(example)
        elif actionability == 'conceptual_only':
            # 概念的投稿をさらに分類
            if likes >= 1000 and len(examples['conceptual_only_high_value']) < 5:
                examples['conceptual_only_high_value'].append(example)
            elif '理論・原理' in types and len(examples['conceptual_only_theory']) < 3:
                examples['conceptual_only_theory'].append(example)
            elif '事例紹介' in types and len(examples['conceptual_only_case']) < 3:
                examples['conceptual_only_case'].append(example)
            elif 'トレンド・ニュース' in types and len(examples['conceptual_only_trend']) < 3:
                examples['conceptual_only_trend'].append(example)

    # 結果表示
    total = len(bookmarks)

    print(f"\n【実装可能性の分布】")
    for action, count in actionability_distribution.most_common():
        pct = round(count/total*100, 1)
        print(f"  {action}: {count}件 ({pct}%)")

    print(f"\n【概念的学習の種類】")
    for ctype, count in conceptual_types.most_common():
        pct = round(count/total*100, 1)
        print(f"  {ctype}: {count}件 ({pct}%)")

    print(f"\n【学習価値の種類】")
    for value, count in learning_values.most_common():
        pct = round(count/total*100, 1)
        print(f"  {value}: {count}件 ({pct}%)")

    print(f"\n【カテゴリ別実装可能性】")
    for cat in category_actionability:
        print(f"\n  {cat}:")
        cat_total = sum(category_actionability[cat].values())
        for action, count in category_actionability[cat].items():
            pct = round(count/cat_total*100, 1)
            print(f"    {action}: {count}件 ({pct}%)")

    # 具体例表示
    print(f"\n" + "=" * 80)
    print("【具体例】")
    print("=" * 80)

    print(f"\n■ すぐ実装可能な投稿（{actionability_distribution['immediately_actionable']}件、{round(actionability_distribution['immediately_actionable']/total*100, 1)}%）")
    for i, ex in enumerate(examples['immediately_actionable'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")
        print(f"  種類: {', '.join(ex['types'])}")

    print(f"\n■ セットアップ必要な投稿（{actionability_distribution['requires_setup']}件、{round(actionability_distribution['requires_setup']/total*100, 1)}%）")
    for i, ex in enumerate(examples['requires_setup'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")
        print(f"  種類: {', '.join(ex['types'])}")

    print(f"\n■ 概念的学習（高エンゲージメント）")
    for i, ex in enumerate(examples['conceptual_only_high_value'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")
        print(f"  種類: {', '.join(ex['types'])}")

    print(f"\n■ 概念的学習（理論型）")
    for i, ex in enumerate(examples['conceptual_only_theory'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")

    print(f"\n■ 概念的学習（事例型）")
    for i, ex in enumerate(examples['conceptual_only_case'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")

    print(f"\n■ 概念的学習（トレンド型）")
    for i, ex in enumerate(examples['conceptual_only_trend'], 1):
        print(f"\n  例{i}: @{ex['author']} ({ex['likes']}いいね)")
        print(f"  {ex['text']}...")

    # JSON保存
    result = {
        'actionability_distribution': dict(actionability_distribution),
        'conceptual_types': dict(conceptual_types),
        'learning_values': dict(learning_values),
        'category_actionability': {k: dict(v) for k, v in category_actionability.items()},
        'examples': examples
    }

    output_file = OUTPUT_DIR / "conceptual_learning_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n" + "=" * 80)
    print(f"分析完了！出力: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
