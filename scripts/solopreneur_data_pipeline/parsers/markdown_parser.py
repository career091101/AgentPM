"""Markdownパーサー"""

import re
import unicodedata
from typing import Dict, List


class MarkdownParser:
    """Markdownドキュメントのセクション解析"""

    def parse_sections(self, content: str) -> Dict[str, str]:
        """
        ## でセクション分割（### も含めて抽出）

        Args:
            content: Markdown本文

        Returns:
            セクション名をキー、本文を値とする辞書
        """
        sections = {}
        current_section = None
        current_content = []

        for line in content.split('\n'):
            # ## で始まる行をセクションヘッダーとして認識（H2のみ）
            header_match = re.match(r'^##\s+(.+)$', line)

            if header_match:
                # 前のセクションを保存
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()

                # 新しいセクション開始（正規化適用）
                current_section = self.normalize_section_name(header_match.group(1).strip())
                current_content = []
            else:
                # H2セクション内の全コンテンツ（H3以下も含む）を追加
                current_content.append(line)

        # 最後のセクションを保存
        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()

        return sections

    def extract_lists(self, section_content: str) -> List[str]:
        """
        セクション内のリスト項目を抽出

        Args:
            section_content: セクション本文

        Returns:
            リスト項目の配列
        """
        items = []
        for line in section_content.split('\n'):
            # - または * で始まるリスト項目
            list_match = re.match(r'^\s*[-*]\s+(.+)$', line)
            if list_match:
                items.append(list_match.group(1).strip())
            # 番号付きリスト
            numbered_match = re.match(r'^\s*\d+\.\s+(.+)$', line)
            if numbered_match:
                items.append(numbered_match.group(1).strip())

        return items

    def extract_blockquotes(self, section_content: str) -> List[str]:
        """
        セクション内の引用ブロックを抽出

        Args:
            section_content: セクション本文

        Returns:
            引用文の配列
        """
        quotes = []
        current_quote = []

        for line in section_content.split('\n'):
            if line.strip().startswith('>'):
                # 引用記号を除去
                quote_line = re.sub(r'^\s*>\s?', '', line)
                current_quote.append(quote_line)
            elif current_quote:
                # 引用ブロック終了
                quotes.append('\n'.join(current_quote).strip())
                current_quote = []

        # 最後の引用ブロック
        if current_quote:
            quotes.append('\n'.join(current_quote).strip())

        return quotes

    def normalize_section_name(self, section_name: str) -> str:
        """
        セクション名を正規化

        Args:
            section_name: 元のセクション名

        Returns:
            正規化されたセクション名
        """
        # ⭐順序重要: 先に絵文字を除去してから数字プレフィックスを除去

        # 1. 絵文字と記号を除去 (Unicodeカテゴリベース)
        # So: Other Symbol (絵文字など), Sk: Modifier Symbol, Sm: Math Symbol
        normalized = ''.join(
            char for char in section_name
            if unicodedata.category(char) not in ['So', 'Sk', 'Sm']
        )

        # 2. 先頭の空白を除去してから数字プレフィックスを除去
        normalized = normalized.lstrip()

        # 3. 数字プレフィックスを除去 (例: "1. ", "2) ")
        normalized = re.sub(r'^\d+[\.\)]\s*', '', normalized)

        # 4. バージョン注釈と星印を除去 (例: " ★v3.0必須", "★v4.0新形式")
        normalized = re.sub(r'\s*[★☆]\s*v?\d+\.\d+[^】]*', '', normalized)

        # 5. 余分な空白を除去
        normalized = ' '.join(normalized.split())

        return normalized
