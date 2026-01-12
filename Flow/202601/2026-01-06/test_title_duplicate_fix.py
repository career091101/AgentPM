#!/usr/bin/env python3
"""
タイトル重複修正のテストスクリプト

修正内容の検証:
- 本文1行目がタイトルと同じ場合は除去
- タイトルと本文が異なる場合は除去しない
"""

import re


def extract_variant_content_fixed(markdown: str, variant_number: int) -> dict:
    """
    案Nのタイトルと本文を抽出（Markdown装飾除去版 + タイトル重複除去）

    修正: 本文1行目がタイトルと同じ場合は除去
    """
    # 案N: パターンX → ### タイトル → ### 本文 → --- の構造を抽出
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    # タイトルと本文を抽出
    title = match.group(1).strip()
    body = match.group(2).strip()

    # Markdown装飾を除去
    def remove_markdown(text):
        """Markdown装飾を除去"""
        # **太字** → 通常テキスト
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # - 箇条書き → 通常テキスト
        text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
        # 1. 番号付きリスト → 通常テキスト
        text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
        return text

    title_clean = remove_markdown(title)
    body_clean = remove_markdown(body)

    # 【修正】本文1行目がタイトルと同じ場合は除去（タイトル重複防止）
    body_lines = body_clean.split('\n')
    if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
        # 1行目（タイトル重複）を除去
        body_clean = '\n'.join(body_lines[1:]).strip()

    # 完全なコンテンツ = タイトル + 本文（タイトル重複除去済み）
    full_content = f"{title_clean}\n\n{body_clean}"

    return {
        "title": title_clean,
        "body": body_clean,
        "full_content": full_content
    }


def test_case_1_duplicate_title():
    """テストケース1: タイトル重複あり（実際のデータ）"""
    markdown = """
## 案2: パターン3（ニュース引用 → 深掘り解説 → 示唆）

### タイトル
**OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か**

### 本文（1,195文字）

OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が報じた衝撃のレポート。
OpenAIが約200兆円規模のインフラ投資を発表し、その資金調達手法が「売り手と買い手で資金が循環する手法はIT（情報技術）バブル期に類似する」と警告されている。
なぜ世界トップのAI企業が、こんな危うい手法を取るのか。

---
"""

    result = extract_variant_content_fixed(markdown, 2)

    print("=" * 60)
    print("テストケース1: タイトル重複あり")
    print("=" * 60)
    print(f"タイトル: {result['title']}")
    print()
    print("期待される出力:")
    print("OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か")
    print()
    print("日本経済新聞が報じた衝撃のレポート。")
    print("OpenAIが約200兆円規模のインフラ投資を発表し...")
    print()
    print("実際の出力:")
    print(result['full_content'])
    print()

    # 検証
    lines = result['full_content'].split('\n')
    first_line = lines[0].strip()
    second_line = lines[2].strip() if len(lines) > 2 else ""

    # タイトルが1回のみ表示されているか確認
    title_count = result['full_content'].count(result['title'])

    print("検証結果:")
    print(f"  - タイトルの出現回数: {title_count} (期待値: 1)")
    print(f"  - 1行目: {first_line}")
    print(f"  - 3行目: {second_line[:50]}...")
    print(f"  - テスト結果: {'✅ 合格' if title_count == 1 else '❌ 不合格'}")
    print()

    return title_count == 1


def test_case_2_no_duplicate():
    """テストケース2: タイトル重複なし（互換性確認）"""
    markdown = """
## 案1: パターン1（断定型主張 → データ展開 → 読者問いかけ）

### タイトル
**テストタイトル**

### 本文（100文字）

これは本文の1行目です。
これは本文の2行目です。
これは本文の3行目です。

---
"""

    result = extract_variant_content_fixed(markdown, 1)

    print("=" * 60)
    print("テストケース2: タイトル重複なし（互換性確認）")
    print("=" * 60)
    print(f"タイトル: {result['title']}")
    print()
    print("期待される出力:")
    print("テストタイトル")
    print()
    print("これは本文の1行目です。")
    print("これは本文の2行目です。")
    print()
    print("実際の出力:")
    print(result['full_content'])
    print()

    # 検証
    lines = result['full_content'].split('\n')
    first_line = lines[0].strip()
    third_line = lines[2].strip() if len(lines) > 2 else ""

    print("検証結果:")
    print(f"  - 1行目: {first_line} (期待値: テストタイトル)")
    print(f"  - 3行目: {third_line} (期待値: これは本文の1行目です。)")
    print(f"  - テスト結果: {'✅ 合格' if first_line == 'テストタイトル' and third_line == 'これは本文の1行目です。' else '❌ 不合格'}")
    print()

    return first_line == "テストタイトル" and third_line == "これは本文の1行目です。"


def test_case_3_title_with_punctuation():
    """テストケース3: タイトルに句点ありの重複"""
    markdown = """
## 案3: パターン2（問題提起 → 反論 → 正論）

### タイトル
**AI時代の新常識**

### 本文（200文字）

AI時代の新常識。

多くの企業がAI導入を進めているが、成功しているのはごく一部だ。
なぜこのような差が生まれるのか。

---
"""

    result = extract_variant_content_fixed(markdown, 3)

    print("=" * 60)
    print("テストケース3: タイトルに句点ありの重複")
    print("=" * 60)
    print(f"タイトル: {result['title']}")
    print()
    print("実際の出力:")
    print(result['full_content'])
    print()

    # 検証
    title_count = result['full_content'].count("AI時代の新常識")

    print("検証結果:")
    print(f"  - タイトルの出現回数: {title_count} (期待値: 1)")
    print(f"  - テスト結果: {'✅ 合格' if title_count == 1 else '❌ 不合格'}")
    print()

    return title_count == 1


def main():
    """メイン処理"""
    print("=" * 60)
    print("タイトル重複修正テスト")
    print("=" * 60)
    print()

    results = []

    # テストケース1: タイトル重複あり
    results.append(("テストケース1", test_case_1_duplicate_title()))

    # テストケース2: タイトル重複なし
    results.append(("テストケース2", test_case_2_no_duplicate()))

    # テストケース3: タイトルに句点ありの重複
    results.append(("テストケース3", test_case_3_title_with_punctuation()))

    # サマリー
    print("=" * 60)
    print("テスト結果サマリー")
    print("=" * 60)
    for name, passed in results:
        status = "✅ 合格" if passed else "❌ 不合格"
        print(f"{name}: {status}")

    all_passed = all(result for _, result in results)
    print()
    print(f"総合結果: {'🎉 全テスト合格' if all_passed else '❌ 一部テスト失敗'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
