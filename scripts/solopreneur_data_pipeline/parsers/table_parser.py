"""Markdownテーブルパーサー"""

import re
from typing import List, Dict, Optional


class TableParser:
    """Markdownテーブルを辞書リストに変換"""

    def parse_table(self, table_text: str) -> List[Dict[str, str]]:
        """
        Markdownテーブル → List[Dict]

        Args:
            table_text: Markdownテーブルテキスト

        Returns:
            行データの配列（各行は列名をキーとする辞書）

        Example:
            Input:
                | 項目 | 内容 | ソース |
                |------|------|--------|
                | MRR  | $10K | X Bio  |

            Output:
                [{"項目": "MRR", "内容": "$10K", "ソース": "X Bio"}]
        """
        lines = [line.strip() for line in table_text.strip().split('\n') if line.strip()]

        if len(lines) < 2:
            return []

        # ヘッダー行（1行目）
        header_line = lines[0]
        headers = [h.strip() for h in header_line.split('|') if h.strip()]

        # セパレータ行（2行目）をスキップ
        if len(lines) < 3:
            return []

        # データ行（3行目以降）
        rows = []
        for line in lines[2:]:
            # セパレータ行は除外
            if re.match(r'^\|[\s\-:]+\|$', line):
                continue

            cells = [c.strip() for c in line.split('|') if c.strip()]

            # ヘッダーと同じ列数の場合のみ追加
            if len(cells) == len(headers):
                row_dict = dict(zip(headers, cells))
                rows.append(row_dict)

        return rows

    def extract_tables_from_section(self, section_content: str) -> List[List[Dict[str, str]]]:
        """
        セクション内の全テーブルを抽出

        Args:
            section_content: セクション本文

        Returns:
            テーブルの配列（各テーブルは行辞書のリスト）
        """
        # Markdownテーブルのパターン
        # | で始まり、セパレータ行 |---| を含む複数行
        # セパレータ行は | と - と : と空白の組み合わせ
        table_pattern = re.compile(
            r'^\|.+\|\n\|[\s\-:|]+\|(?:\n\|.+\|)+',
            re.MULTILINE
        )

        tables = []
        for match in table_pattern.finditer(section_content):
            table_data = self.parse_table(match.group())
            if table_data:  # 空でないテーブルのみ追加
                tables.append(table_data)

        return tables

    def find_table_by_header(
        self,
        section_content: str,
        header_keywords: List[str]
    ) -> Optional[List[Dict[str, str]]]:
        """
        指定されたヘッダーキーワードを含むテーブルを検索

        Args:
            section_content: セクション本文
            header_keywords: 検索するヘッダーキーワードのリスト

        Returns:
            最初にマッチしたテーブル、見つからない場合None
        """
        tables = self.extract_tables_from_section(section_content)

        for table in tables:
            if not table:
                continue

            # 最初の行のキーをチェック
            first_row_keys = list(table[0].keys())

            # いずれかのキーワードがヘッダーに含まれているか確認
            for keyword in header_keywords:
                if any(keyword in key for key in first_row_keys):
                    return table

        return None
