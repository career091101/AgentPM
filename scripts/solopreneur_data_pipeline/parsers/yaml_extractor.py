"""YAML Front Matter抽出器"""

import re
import yaml
from typing import Optional, Dict, Any, Tuple


class YamlExtractor:
    """Markdown内のYAML Front Matterを抽出"""

    YAML_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL | re.MULTILINE)

    def extract(self, content: str) -> Tuple[Optional[Dict[str, Any]], str]:
        """
        YAML Front Matterを抽出

        Args:
            content: Markdownファイルの内容

        Returns:
            (yaml_data, remaining_markdown)のタプル
            yaml_dataはYAMLが存在しない場合None
        """
        match = self.YAML_PATTERN.match(content)
        if not match:
            return None, content

        yaml_str = match.group(1)

        # コメント行を除去してパース
        yaml_clean = self._remove_yaml_comments(yaml_str)

        try:
            data = yaml.safe_load(yaml_clean)
            remaining = content[match.end():]
            return data, remaining
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parse error: {e}")

    def _remove_yaml_comments(self, yaml_str: str) -> str:
        """
        YAML内の # コメントを除去

        Args:
            yaml_str: YAMLテキスト

        Returns:
            コメント除去後のYAMLテキスト
        """
        lines = []
        for line in yaml_str.split('\n'):
            # インラインコメントを除去（文字列内の#は保持）
            if '#' in line:
                # 文字列リテラル内の#は保持
                if not re.search(r'["\'].*#.*["\']', line):
                    idx = line.find('#')
                    # 行頭コメントはスキップ
                    if idx == 0:
                        continue
                    # フィールド定義後のコメントは除去
                    if line[:idx].strip().endswith(':') or '  ' in line[:idx]:
                        line = line[:idx].rstrip()

            lines.append(line)

        return '\n'.join(lines)

    def validate_required_fields(self, yaml_data: Dict[str, Any], category: str) -> bool:
        """
        必須フィールドの存在を確認

        Args:
            yaml_data: パース済みYAMLデータ
            category: カテゴリ（app/newsletter/sns）

        Returns:
            必須フィールドが全て存在する場合True
        """
        common_required = ["id", "category", "version"]

        # 共通必須フィールドチェック
        for field in common_required:
            if field not in yaml_data:
                return False

        # カテゴリ別必須フィールドチェック
        category_required = {
            "app": ["subject", "main_product"],
            "sns": ["subject", "sns_presence"],
            "newsletter": ["newsletter_name", "founder_name"]
        }

        if category in category_required:
            for field in category_required[category]:
                if field not in yaml_data:
                    return False

        return True
