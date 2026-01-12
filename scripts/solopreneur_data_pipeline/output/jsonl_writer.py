"""JSONL出力"""

import json
from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime


class JsonlWriter:
    """JSONLファイル書き込み"""

    def write(
        self,
        records: List[Dict[str, Any]],
        output_path: Path,
        category_filter: Optional[str] = None
    ) -> int:
        """
        JSONLファイルを書き込み

        Args:
            records: レコードリスト
            output_path: 出力ファイルパス
            category_filter: カテゴリでフィルタ（Noneの場合全レコード）

        Returns:
            書き込んだレコード数
        """
        filtered = records
        if category_filter:
            filtered = [r for r in records if r.get("category") == category_filter]

        # 親ディレクトリ作成
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            for record in filtered:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')

        return len(filtered)

    def write_with_metadata(
        self,
        records: List[Dict[str, Any]],
        output_path: Path
    ) -> None:
        """
        メタデータ行を先頭に追加してJSONLファイルを書き込み

        Args:
            records: レコードリスト
            output_path: 出力ファイルパス
        """
        metadata = {
            "_metadata": True,
            "generated_at": datetime.now().isoformat(),
            "total_records": len(records),
            "categories": list(set(r.get("category") for r in records if r.get("category"))),
            "versions": list(set(r.get("version") for r in records if r.get("version"))),
        }

        # 親ディレクトリ作成
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            # メタデータ行
            f.write(json.dumps(metadata, ensure_ascii=False) + '\n')

            # データ行
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')

    def write_split_files(
        self,
        records: List[Dict[str, Any]],
        output_dir: Path,
        prefix: str = "solopreneur"
    ) -> Dict[str, int]:
        """
        カテゴリ別にファイル分割して書き込み

        Args:
            records: レコードリスト
            output_dir: 出力ディレクトリ
            prefix: ファイル名プレフィックス

        Returns:
            カテゴリごとのレコード数
        """
        # カテゴリごとにグループ化
        by_category = {}
        for record in records:
            category = record.get("category", "unknown")
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(record)

        # カテゴリごとに書き込み
        counts = {}
        for category, category_records in by_category.items():
            output_path = output_dir / f"{prefix}_{category}.jsonl"
            count = self.write(category_records, output_path)
            counts[category] = count

        # 統合ファイルも書き込み
        unified_path = output_dir / f"{prefix}_unified.jsonl"
        self.write_with_metadata(records, unified_path)
        counts["unified"] = len(records)

        return counts
