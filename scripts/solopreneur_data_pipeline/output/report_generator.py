"""変換レポート生成"""

from typing import List, Dict, Any
from dataclasses import dataclass
from collections import Counter
from datetime import datetime


@dataclass
class ConversionReport:
    """変換レポートデータクラス"""
    total_files: int
    success_count: int
    warning_count: int
    error_count: int
    errors: List[Dict[str, str]]
    warnings: List[Dict[str, str]]
    category_stats: Dict[str, int]
    version_stats: Dict[str, int]
    missing_fields: Dict[str, int]


class ReportGenerator:
    """変換レポート生成"""

    def generate(
        self,
        results: List[Dict[str, Any]],
        errors: List[Dict[str, str]],
        warnings: List[Dict[str, str]]
    ) -> ConversionReport:
        """
        変換結果からレポートを生成

        Args:
            results: 変換成功レコードのリスト
            errors: エラーリスト
            warnings: 警告リスト

        Returns:
            変換レポート
        """
        # カテゴリ別統計
        category_stats = Counter(r.get("category") for r in results if r.get("category"))

        # バージョン別統計
        version_stats = Counter(r.get("version") for r in results if r.get("version"))

        # 欠損フィールド統計
        missing = Counter()
        for r in results:
            if not r.get("revenue", {}).get("mrr_usd"):
                missing["revenue.mrr_usd"] += 1
            if not r.get("japan_score", {}).get("total"):
                missing["japan_score.total"] += 1
            if not r.get("quality", {}).get("fact_check"):
                missing["quality.fact_check"] += 1
            if not r.get("embedding_text"):
                missing["embedding_text"] += 1

        return ConversionReport(
            total_files=len(results) + len(errors),
            success_count=len(results),
            warning_count=len(warnings),
            error_count=len(errors),
            errors=errors,
            warnings=warnings,
            category_stats=dict(category_stats),
            version_stats=dict(version_stats),
            missing_fields=dict(missing)
        )

    def to_markdown(self, report: ConversionReport) -> str:
        """
        レポートをMarkdown形式で出力

        Args:
            report: 変換レポート

        Returns:
            Markdownテキスト
        """
        success_rate = (report.success_count / report.total_files * 100) if report.total_files > 0 else 0

        md = f"""# Markdown→JSONL変換レポート

生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## サマリー

- 処理ファイル数: {report.total_files}
- 成功: {report.success_count} ({success_rate:.1f}%)
- 警告: {report.warning_count}
- エラー: {report.error_count}

## カテゴリ別統計

{self._format_stats_table(report.category_stats)}

## バージョン別統計

{self._format_stats_table(report.version_stats)}

## 欠損フィールド

{self._format_stats_table(report.missing_fields)}

## エラー詳細

"""

        if report.errors:
            md += "| ファイル | エラー |\n|---------|-------|\n"
            for error in report.errors[:20]:  # 最初の20件のみ
                file_name = error.get("file", "")
                error_msg = error.get("error", "").replace("\n", " ")[:100]
                md += f"| {file_name} | {error_msg} |\n"

            if len(report.errors) > 20:
                md += f"\n...他 {len(report.errors) - 20} 件のエラー\n"
        else:
            md += "エラーなし\n"

        md += "\n## 警告詳細\n\n"

        if report.warnings:
            md += "| ファイル | 警告 |\n|---------|-----|\n"
            for warning in report.warnings[:20]:  # 最初の20件のみ
                file_name = warning.get("file", "")
                warning_msg = str(warning.get("warnings", "")).replace("\n", " ")[:100]
                md += f"| {file_name} | {warning_msg} |\n"

            if len(report.warnings) > 20:
                md += f"\n...他 {len(report.warnings) - 20} 件の警告\n"
        else:
            md += "警告なし\n"

        return md

    def _format_stats_table(self, stats: Dict[str, int]) -> str:
        """統計データをMarkdownテーブル形式に変換"""
        if not stats:
            return "データなし\n"

        table = "| 項目 | 件数 |\n|------|------|\n"
        for key, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            table += f"| {key} | {count} |\n"

        return table
