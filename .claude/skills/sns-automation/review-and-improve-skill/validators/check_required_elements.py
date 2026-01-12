#!/usr/bin/env python3
"""
必須要素チェックスクリプト

生成された投稿案の必須要素（口語体、数値データ、企業名等）を自動評価
"""

import re
import sys
from typing import Dict, List


def check_casual_tone(text: str) -> Dict:
    """口語体の使用回数をチェック"""

    casual_phrases = [
        "ヤバい", "やばい",
        "マジで", "まじで",
        "完全に",
        "の件",
        "これ、",
        "だけど",
        "すぎる",
        "大丈夫？",
        "どう思う？",
        "間違いない",
        "確実だ",
        "桁違い",
        "次元が違う",
        "ありえない",
        "前代未聞",
    ]

    count = sum(text.count(phrase) for phrase in casual_phrases)

    if count == 0:
        status = "不合格"
        score = 0
    elif count == 1:
        status = "改善推奨"
        score = 50
    else:
        status = "合格"
        score = 100

    return {
        "score": score,
        "count": count,
        "status": status,
        "suggestion": f"口語体を最低2回使用してください（現在: {count}回）" if count < 2 else None
    }


def check_expansion_phrases(text: str) -> Dict:
    """拡張フレーズの使用をチェック"""

    expansion_phrases = [
        "でも、ここからが本当の話だ",
        "でも、本質はここからだ",
        "でも、ここからが重要だ",
        "真実はここにある",
        "本当の問題はこれだ",
        "核心はここだ",
        "でも、見逃せない事実がある",
        "本当に注目すべきはこれだ",
        "でも、最も重要なのはこれだ",
        "真の意味はここにある",
    ]

    used_phrases = [p for p in expansion_phrases if p in text]

    if len(used_phrases) == 0:
        status = "未使用"
        score = 0
    else:
        status = "使用"
        score = 100

    return {
        "score": score,
        "used": used_phrases[0] if used_phrases else None,
        "status": status,
        "suggestion": "パターン1・3の場合は拡張フレーズを使用してください" if score == 0 else None
    }


def check_numeric_data(text: str) -> Dict:
    """具体的数値データの数をチェック"""

    numeric_patterns = [
        r'\d+億ドル', r'\d+兆円', r'\d+億円', r'\d+万円',  # 財務
        r'\d+%', r'年率\d+%', r'CAGR\s?\d+%',  # 成長率
        r'バージョン\s?\d+\.?\d*', r'v\d+\.?\d*',  # バージョン
        r'\d{4}年', r'\d+月', r'\d+日',  # 時系列
        r'\d+人', r'\d+社', r'\d+件',  # 数量
        r'\d+倍', r'\d+万', r'\d+千',  # 倍率・単位
    ]

    # SNS数値パターン（除外）
    invalid_patterns = [
        r'いいね\s?\d+',
        r'リツイート\s?\d+',
        r'\d+\s?ビュー',
        r'\d+\s?インプレッション',
    ]

    # 有効な数値をカウント
    valid_count = sum(len(re.findall(p, text)) for p in numeric_patterns)

    # 無効な数値を検出
    invalid_count = sum(len(re.findall(p, text)) for p in invalid_patterns)

    # 総数から無効数値を引く
    net_count = max(0, valid_count - invalid_count)

    if net_count < 5:
        status = "不合格"
        score = 0
    elif net_count < 7:
        status = "最低基準"
        score = 70
    elif net_count < 10:
        status = "良好"
        score = 85
    else:
        status = "優秀"
        score = 100

    return {
        "score": score,
        "count": net_count,
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "status": status,
        "suggestion": f"有効な数値データを最低5個含めてください（現在: {net_count}個）" if net_count < 5 else None
    }


def check_company_names(text: str) -> Dict:
    """企業名・人名の使用回数をチェック"""

    # カタカナ2文字以上、または英字3文字以上（頭文字大文字）
    company_patterns = [
        r'[ァ-ヴー]{2,}',  # カタカナ2文字以上
        r'[A-Z][a-z]{2,}',  # 英字（頭文字大文字）3文字以上
        r'[A-Z]{2,}',  # 英字大文字2文字以上（略称）
    ]

    count = sum(len(re.findall(p, text)) for p in company_patterns)

    if count < 3:
        status = "不合格"
        score = 0
    elif count == 3:
        status = "最低基準"
        score = 80
    elif count == 4:
        status = "良好"
        score = 90
    else:
        status = "優秀"
        score = 100

    return {
        "score": score,
        "count": count,
        "status": status,
        "suggestion": f"企業名・人名を最低3回使用してください（現在: {count}回）" if count < 3 else None
    }


def check_character_count(text: str) -> Dict:
    """文字数をチェック"""

    char_count = len(text)

    if char_count < 700:
        status = "不合格"
        score = 0
    elif char_count < 900:
        status = "最低基準"
        score = 80
    elif char_count < 1500:
        status = "最適"
        score = 100
    else:
        status = "やや長い"
        score = 90

    return {
        "score": score,
        "count": char_count,
        "status": status,
        "suggestion": f"文字数を最低700字にしてください（現在: {char_count}字）" if char_count < 700 else None
    }


def check_all_elements(text: str) -> Dict:
    """すべての必須要素をチェック"""

    results = {
        "口語体": check_casual_tone(text),
        "拡張フレーズ": check_expansion_phrases(text),
        "数値データ": check_numeric_data(text),
        "企業名・人名": check_company_names(text),
        "文字数": check_character_count(text),
    }

    # 総合スコア計算
    total_score = sum(r["score"] for r in results.values()) / len(results)

    return {
        "total_score": total_score,
        "scores": results,
        "status": "合格" if total_score >= 70 else "不合格"
    }


def format_report(result: Dict) -> str:
    """評価結果をフォーマット"""

    report = f"## 必須要素チェック結果\n\n"
    report += f"**総合スコア**: {result['total_score']:.1f}点 ({result['status']})\n\n"

    report += "| 評価項目 | スコア | 状態 | 詳細 |\n"
    report += "|---------|--------|------|------|\n"

    for name, data in result['scores'].items():
        details = []
        if 'count' in data:
            details.append(f"{data['count']}回" if name in ["口語体", "企業名・人名"] else f"{data['count']}個" if name == "数値データ" else f"{data['count']}字")
        if 'used' in data and data['used']:
            details.append(f"使用: {data['used']}")

        detail_str = ", ".join(details)

        status_emoji = "✅" if data['score'] >= 70 else "⚠️" if data['score'] >= 50 else "❌"

        report += f"| {name} | {data['score']}点 | {status_emoji} {data['status']} | {detail_str} |\n"

    report += "\n"

    # 改善提案
    suggestions = [data['suggestion'] for data in result['scores'].values() if data.get('suggestion')]

    if suggestions:
        report += "### 改善提案\n\n"
        for i, suggestion in enumerate(suggestions, 1):
            report += f"{i}. {suggestion}\n"
        report += "\n"

    return report


def main():
    """メイン実行"""

    # テストケース
    test_cases = [
        {
            'name': '高品質投稿（合格）',
            'text': """SoftBankが3.5兆円ぶち込んだOpenAI投資、マジでヤバい件。

2026年1月、OpenAIへの追加投資が発表された。これ、経営者は見逃せない。投資額は3.5兆円、持分は14%。Googleも30億ドル投資している。

でも、ここからが本当の話だ。AI開発競争が単なる性能争いから、総力戦へ突入したことを示唆している。市場規模は2025年に1.8兆ドル、2030年には5.2兆ドルに達する見込み。成長率はCAGR 35%だ。

つまり、2026年はAI戦略の分岐点。経営者の判断が企業の命運を分ける年になる。

あなたの会社、AI戦略は大丈夫？
""",
            'expected_score': 85
        },
        {
            'name': '低品質投稿（不合格）',
            'text': """AI技術が進化している。

企業が投資を増やしている。
将来的には市場が拡大するかもしれない。

どう思いますか？
""",
            'expected_score': 30
        },
    ]

    print("=" * 60)
    print("必須要素チェックスクリプト - テスト実行")
    print("=" * 60)
    print()

    for i, test_case in enumerate(test_cases, 1):
        print(f"## テストケース {i}: {test_case['name']}")
        print()

        result = check_all_elements(test_case['text'])

        print(format_report(result))

        if result['total_score'] >= test_case['expected_score']:
            print(f"✅ テスト合格（期待スコア: {test_case['expected_score']}点以上, 実際: {result['total_score']:.1f}点）\n")
        else:
            print(f"⚠️ テスト不合格（期待スコア: {test_case['expected_score']}点以上, 実際: {result['total_score']:.1f}点）\n")

        print("-" * 60)
        print()


if __name__ == '__main__':
    main()
