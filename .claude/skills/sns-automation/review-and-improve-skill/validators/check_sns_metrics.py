#!/usr/bin/env python3
"""
SNS数値データ検出スクリプト

生成された投稿案からSNS数値データ（いいね、リツイート、ビュー等）を自動検出
"""

import re
import sys
from typing import Dict, List


def detect_sns_metrics(text: str) -> Dict:
    """SNS数値データを自動検出"""

    patterns = {
        'いいね数': r'いいね\s?\d[\d,]*',
        'リツイート数': r'リツイート\s?\d[\d,]*',
        'ビュー数': r'\d[\d,]*\s?ビュー',
        'インプレッション数': r'\d[\d,]*\s?インプレッション',
        'フォロワー数': r'フォロワー\s?\d[\d,]*',
        'シェア数': r'\d[\d,]*\s?シェア',
        'コメント数': r'\d[\d,]*\s?コメント',
        'リプライ数': r'\d[\d,]*\s?リプライ',
        'アカウント名': r'@[a-zA-Z0-9_]+',
        'ユーザー投稿': r'[a-zA-Z0-9_]+のスレッド',
        'ユーザーツイート': r'[a-zA-Z0-9_]+のツイート',
    }

    detections = []

    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            detections.append({
                'type': name,
                'matches': matches,
                'count': len(matches),
                'severity': 'ERROR'
            })

    return {
        'has_issues': len(detections) > 0,
        'total_issues': len(detections),
        'detections': detections,
        'status': 'FAIL' if len(detections) > 0 else 'PASS'
    }


def suggest_alternatives(detection_type: str) -> List[str]:
    """検出された問題に対する代替表現を提案"""

    alternatives = {
        'いいね数': [
            "大きな反響を呼んでいる",
            "注目を集めている",
            "話題になっている",
        ],
        'リツイート数': [
            "広く共有されている",
            "拡散されている",
            "多くの人に届いている",
        ],
        'ビュー数': [
            "多くの閲覧を集めている",
            "注目されている",
            "視聴数を伸ばしている",
        ],
        'アカウント名': [
            "AI開発者コミュニティ",
            "業界専門家",
            "技術コミュニティ",
        ],
        'ユーザー投稿': [
            "AI研究者の投稿",
            "開発者の見解",
            "専門家の分析",
        ],
    }

    return alternatives.get(detection_type, ["一般的な表現に置き換える"])


def format_report(result: Dict) -> str:
    """検出結果をフォーマット"""

    if result['status'] == 'PASS':
        return "✅ SNS数値データは検出されませんでした"

    report = f"❌ SNS数値データが検出されました（{result['total_issues']}件）\n\n"

    for detection in result['detections']:
        report += f"### {detection['type']} ({detection['count']}件)\n"
        report += f"**検出**: {', '.join(detection['matches'])}\n\n"

        alternatives = suggest_alternatives(detection['type'])
        report += "**推奨代替表現**:\n"
        for alt in alternatives:
            report += f"  - {alt}\n"
        report += "\n"

    return report


def main():
    """メイン実行"""

    # テストケース
    test_cases = [
        {
            'name': 'SNS数値あり（不合格）',
            'text': "SuguruKun_aiのスレッドがいいね1,132、リツイート105、163,736ビューを記録。",
            'expected': 'FAIL'
        },
        {
            'name': 'SNS数値なし（合格）',
            'text': "AI開発者コミュニティで大きな反響を呼んでいる。OpenAI Cookbookで正式公開され、注目を集めている。",
            'expected': 'PASS'
        },
        {
            'name': 'アカウント名のみ（不合格）',
            'text': "@elonmuskが発言した内容について、業界で議論が巻き起こっている。",
            'expected': 'FAIL'
        },
    ]

    print("=" * 60)
    print("SNS数値データ検出スクリプト - テスト実行")
    print("=" * 60)
    print()

    all_passed = True

    for i, test_case in enumerate(test_cases, 1):
        print(f"## テストケース {i}: {test_case['name']}")
        print(f"**テキスト**: {test_case['text'][:100]}...")
        print()

        result = detect_sns_metrics(test_case['text'])

        print(format_report(result))

        if result['status'] == test_case['expected']:
            print(f"✅ テスト合格（期待値: {test_case['expected']}）\n")
        else:
            print(f"❌ テスト失敗（期待値: {test_case['expected']}, 実際: {result['status']}）\n")
            all_passed = False

        print("-" * 60)
        print()

    if all_passed:
        print("✅ 全テストケース合格")
        sys.exit(0)
    else:
        print("❌ 一部のテストケースが失敗しました")
        sys.exit(1)


if __name__ == '__main__':
    main()
