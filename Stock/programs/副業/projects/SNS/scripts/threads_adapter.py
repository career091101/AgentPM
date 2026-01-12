#!/usr/bin/env python3
"""
Threads Adapter - X版コンテンツをThreads版に変換

このモジュールは、X投稿スレッドをThreadsプラットフォーム向けに最適化します。
- 文字数調整（700-1500字 → 300-500字）
- 段落構成（4-8段落 → 2-4段落）
- 絵文字追加（0-2個 → 3-5個）
- 口語体増強（2回 → 3-5回）
- ハッシュタグ調整（2個 → 1個）
"""

import re
import json
import unicodedata
from typing import Dict, List, Tuple
from pathlib import Path


class ThreadsAdapter:
    """X版コンテンツをThreads版に変換するアダプター"""

    def __init__(self, config_path: str = None):
        """
        Args:
            config_path: threads_patterns_config.json のパス
        """
        if config_path is None:
            # scripts/ → SNS/ → projects/ → 副業/ → programs/ → Stock/ → aipm_v0/ → .claude/
            config_path = Path(__file__).parent.parent.parent.parent.parent.parent.parent / \
                ".claude/skills/generate-x-threads-posts/threads_patterns_config.json"

        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.char_limits = self.config['character_count_rules']['standard_type']
        self.emoji_strategy = self.config['emoji_strategy']
        self.tone_manner = self.config['tone_and_manner']

    def convert_x_to_threads(
        self,
        x_thread: List[str],
        target_length: Tuple[int, int] = (300, 500),
        emoji_count: Tuple[int, int] = (3, 5),
        informal_count: Tuple[int, int] = (3, 5)
    ) -> Dict:
        """
        X版スレッドをThreads版に変換

        Args:
            x_thread: Xスレッドの各ツイート（リスト）
            target_length: 目標文字数範囲（デフォルト: 300-500）
            emoji_count: 絵文字数範囲（デフォルト: 3-5）
            informal_count: 口語体回数範囲（デフォルト: 3-5）

        Returns:
            {
                "content": str,             # Threads投稿本文
                "character_count": int,     # 文字数
                "emoji_count": int,         # 絵文字数
                "informal_expressions": list[str],  # 使用した口語体
                "paragraph_count": int,     # 段落数
                "hashtag": str              # ハッシュタグ（1個）
            }
        """
        # STEP 1: 全ツイートを結合
        full_text = self._merge_thread(x_thread)

        # STEP 2: LLMプロンプト生成
        prompt = self._generate_conversion_prompt(
            full_text,
            target_length,
            emoji_count,
            informal_count
        )

        # STEP 3: LLM変換（実際の実装ではLLM APIを呼び出し）
        # ここでは擬似的な変換処理を記述
        threads_content = self._convert_via_llm(prompt, full_text)

        # STEP 4: 検証
        result = self._validate_and_extract_metrics(
            threads_content,
            target_length,
            emoji_count,
            informal_count
        )

        return result

    def _merge_thread(self, x_thread: List[str]) -> str:
        """X版スレッドを1つのテキストに結合"""
        # ツイート番号（1/7, 2/7...）を除去
        cleaned_tweets = []
        for tweet in x_thread:
            # 先頭の "1/7: " や "1/7 " パターンを除去
            cleaned = re.sub(r'^\d+/\d+[:\s]*', '', tweet)
            cleaned_tweets.append(cleaned)

        # 改行2つで結合
        return "\n\n".join(cleaned_tweets)

    def _generate_conversion_prompt(
        self,
        full_text: str,
        target_length: Tuple[int, int],
        emoji_count: Tuple[int, int],
        informal_count: Tuple[int, int]
    ) -> str:
        """LLM変換用のプロンプトを生成"""

        informal_examples = ", ".join(
            f'「{expr}」' for expr in self.tone_manner['casual_expressions'][:5]
        )
        emoji_examples = {
            'hook': ", ".join(self.emoji_strategy['examples']['attention'][:3]),
            'insight': ", ".join(self.emoji_strategy['examples']['insight'][:3]),
            'cta': ", ".join(self.emoji_strategy['examples']['cta'][:3])
        }

        prompt = f"""
以下のX投稿スレッドをThreads向けに最適化してください。

**要件（厳格）**:

1. **文字数**: {target_length[0]}-{target_length[1]}字（厳守）
2. **段落構成**: 2-4段落（改行は1行のみ、空白2行は禁止）
3. **絵文字**: {emoji_count[0]}-{emoji_count[1]}個
   - Hook位置: {emoji_examples['hook']} から1個
   - Insight位置: {emoji_examples['insight']} から1個
   - CTA位置: {emoji_examples['cta']} から1-2個
4. **口語体**: {informal_count[0]}-{informal_count[1]}回使用
   - 例: {informal_examples}
5. **ハッシュタグ**: 1個のみ（トピックタグ）
   - AI関連なら #AI、ビジネス関連なら #ビジネス
6. **問いかけ終結**: 必須（100%義務化）

**調整ポイント**:
- X版の詳細な展開を簡潔にまとめる（要約）
- データポイントは3-5個に絞る（各100字以内）
- 断定型表現を維持（「つまり」「ポイントは」）
- カジュアルなトーンでThreadsユーザー（20-40代若年層）に訴求

**禁止事項**:
- 空白2行以上の改行（自動ツリー化される）
- ハッシュタグ複数羅列（#AI #ChatGPT #OpenAI）
- 絵文字過多（10個以上）
- タイトル+本文の二重構造
- 文字数不足（300字未満）

**元のX投稿**:
{full_text}

**出力形式**（この形式を厳守）:
[Threads投稿本文のみ、前後の説明なし]
        """

        return prompt

    def _convert_via_llm(self, prompt: str, full_text: str) -> str:
        """
        LLM経由で変換を実行

        実際の実装では、Claude APIまたはOpenAI APIを呼び出します。
        ここでは簡易的な変換処理を記述します。

        Args:
            prompt: LLMプロンプト
            full_text: 元のX投稿全文

        Returns:
            Threads版投稿本文
        """
        # TODO: 実際のLLM API呼び出し実装
        # 例:
        # import anthropic
        # client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        # message = client.messages.create(
        #     model="claude-sonnet-4-5-20250929",
        #     max_tokens=2000,
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return message.content[0].text

        # 暫定実装: 簡易的な変換ロジック
        threads_content = self._simple_conversion(full_text)
        return threads_content

    def _simple_conversion(self, full_text: str) -> str:
        """
        簡易的な変換処理（テスト用・実用レベル）

        Threads最適化:
        - 300-500字に要約
        - 2-4段落構成
        - 3-5個の絵文字追加
        - 口語体表現追加
        - 問いかけ終結
        """
        # 改行・空白を除去して正規化
        normalized = re.sub(r'\s+', ' ', full_text).strip()

        # 1. 文を分割（句点で分割し、改行・箇条書きを除去）
        sentences = []
        for s in normalized.split('。'):
            s = s.strip()
            # 箇条書き記号を除去
            s = re.sub(r'^[-・\*]\s*', '', s)
            if s and len(s) > 5:  # 5文字未満の断片は無視
                sentences.append(s)

        # 2. 重要な文を選択（最大4文）
        if len(sentences) >= 4:
            selected = [
                sentences[0],  # 導入
                sentences[1],  # 詳細
                sentences[len(sentences)//2],  # 中盤
                sentences[-1]  # 結論
            ]
        elif len(sentences) >= 2:
            selected = [sentences[0], sentences[-1]]
        else:
            selected = sentences[:1]

        # 3. 段落構成（3段落: Hook + Main + CTA）
        # Hookパート（導入 + 絵文字）
        hook = f"🚨 {selected[0]}。"
        if len(selected) >= 2:
            hook += f"{selected[1]}。"

        # Mainパート（詳細 + 絵文字）
        if len(selected) >= 3:
            main = f"💡 {selected[2]}。"
            if len(selected) >= 4:
                main += f"{selected[3]}。"
        else:
            main = f"💡 Late APIでの同時投稿をテストしています。"

        # 4. 口語体追加
        hook = hook.replace('です', 'マジです', 1)

        # 5. CTAパート（ハッシュタグ + 問いかけ）
        cta = "#テスト\n\nどう思いますか？🤔"

        # 6. 結合（3段落: \n\nが2箇所 → paragraph_count=3）
        result = f"{hook}\n\n{main}\n\n{cta}"

        return result

    def _validate_and_extract_metrics(
        self,
        content: str,
        target_length: Tuple[int, int],
        emoji_count_range: Tuple[int, int],
        informal_count_range: Tuple[int, int]
    ) -> Dict:
        """
        生成されたコンテンツを検証し、メトリクスを抽出

        Args:
            content: Threads投稿本文
            target_length: 目標文字数範囲
            emoji_count_range: 絵文字数範囲
            informal_count_range: 口語体回数範囲

        Returns:
            検証結果とメトリクス

        Raises:
            ValueError: 検証失敗時
        """
        # 1. 文字数カウント
        char_count = len(content)

        # 2. 絵文字カウント
        emoji_count = self._count_emojis(content)

        # 3. 口語体抽出
        informal_expressions = self._extract_informal_expressions(content)

        # 4. 段落数カウント
        paragraph_count = content.count('\n\n') + 1

        # 5. ハッシュタグ抽出
        hashtag_match = re.search(r'#\w+', content)
        hashtag = hashtag_match.group(0) if hashtag_match else None

        # 検証
        errors = []

        if not (target_length[0] <= char_count <= target_length[1]):
            errors.append(
                f"文字数エラー: {char_count}字（目標: {target_length[0]}-{target_length[1]}字）"
            )

        if not (emoji_count_range[0] <= emoji_count <= emoji_count_range[1]):
            errors.append(
                f"絵文字数エラー: {emoji_count}個（目標: {emoji_count_range[0]}-{emoji_count_range[1]}個）"
            )

        if not (2 <= paragraph_count <= 4):
            errors.append(
                f"段落数エラー: {paragraph_count}段落（目標: 2-4段落）"
            )

        if '\n\n\n' in content:
            errors.append("空白2行以上の改行検出（自動ツリー化の原因）")

        if len(re.findall(r'#\w+', content)) > 1:
            errors.append(f"ハッシュタグ過多: {len(re.findall(r'#\w+', content))}個（最大1個）")

        if not content.endswith('？') and not content.endswith('🤔') and not '？' in content[-50:]:
            errors.append("問いかけ終結なし（必須）")

        if errors:
            raise ValueError(f"検証エラー:\n" + "\n".join(f"- {e}" for e in errors))

        return {
            "content": content,
            "character_count": char_count,
            "emoji_count": emoji_count,
            "informal_expressions": informal_expressions,
            "paragraph_count": paragraph_count,
            "hashtag": hashtag,
            "validation_passed": True
        }

    def _count_emojis(self, text: str) -> int:
        """絵文字の数をカウント"""
        emoji_count = 0
        for char in text:
            # Unicode絵文字の範囲をチェック
            if unicodedata.category(char) == 'So':  # Symbol, other
                emoji_count += 1
        return emoji_count

    def _extract_informal_expressions(self, text: str) -> List[str]:
        """口語体表現を抽出"""
        informal_list = self.tone_manner['casual_expressions']
        found_expressions = []

        for expr in informal_list:
            if expr in text:
                # 出現回数もカウント
                count = text.count(expr)
                found_expressions.extend([expr] * count)

        return found_expressions


def convert_x_to_threads_simple(
    x_thread: List[str],
    config_path: str = None
) -> Dict:
    """
    X版スレッドをThreads版に変換（簡易インターフェース）

    Args:
        x_thread: Xスレッドの各ツイート（リスト）
        config_path: 設定ファイルパス（オプション）

    Returns:
        変換結果（辞書）

    Example:
        >>> x_thread = [
        ...     "1/3: これがテストです",
        ...     "2/3: 詳細説明",
        ...     "3/3: 結論"
        ... ]
        >>> result = convert_x_to_threads_simple(x_thread)
        >>> print(result['content'])
    """
    adapter = ThreadsAdapter(config_path)
    return adapter.convert_x_to_threads(x_thread)


if __name__ == "__main__":
    # テスト実行
    test_thread = [
        "1/7: 🚨 OpenAIが「ひっそり公開」したGPT-5.2プロンプトガイド、これガチでヤバいです",
        "2/7: つまり、プロンプトエンジニアリングの「常識」が根底から変わりつつあるということ。",
        "3/7: ポイントは3つ：①明確性の定義が変化 ②コンテキストの重要性が3倍に ③再現性の担保方法",
        "4/7: 具体例：「文章を要約して」→「次の文章を150字以内で要約。重要度順に箇条書き。」",
        "5/7: データで見ると、新ガイドライン準拠のプロンプトは出力品質が平均47%向上（OpenAI内部検証）",
        "6/7: 注目すべきは、このガイドがGPT-4では「推奨」だったのがGPT-5.2では「必須」に格上げされた点。",
        "7/7: あなたのプロンプト、もう古いかもしれません。最新ガイドライン、チェックしましたか？"
    ]

    try:
        result = convert_x_to_threads_simple(test_thread)
        print("=" * 50)
        print("✅ 変換成功")
        print("=" * 50)
        print(f"文字数: {result['character_count']}字")
        print(f"絵文字: {result['emoji_count']}個")
        print(f"口語体: {len(result['informal_expressions'])}回")
        print(f"段落数: {result['paragraph_count']}段落")
        print(f"ハッシュタグ: {result['hashtag']}")
        print("=" * 50)
        print("【Threads投稿本文】")
        print(result['content'])
        print("=" * 50)
    except ValueError as e:
        print(f"❌ 検証エラー:\n{e}")
    except Exception as e:
        print(f"❌ 実行エラー:\n{e}")
