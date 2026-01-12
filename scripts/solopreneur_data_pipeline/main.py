"""Markdown→JSONL変換パイプライン メインスクリプト"""

import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

from .config import config
from .transformers import AppTransformer, SnsTransformer, NewsletterTransformer
from .output import JsonlWriter, ReportGenerator


def setup_logging(verbose: bool = False) -> logging.Logger:
    """ロギング設定"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s'
    )
    return logging.getLogger(__name__)


def process_category(
    category: str,
    transformer: Any,
    logger: logging.Logger
) -> tuple[List[Dict], List[Dict], List[Dict]]:
    """
    カテゴリごとのファイル処理

    Args:
        category: カテゴリ名（app/newsletter/sns）
        transformer: トランスフォーマーインスタンス
        logger: ロガー

    Returns:
        (results, errors, warnings)のタプル
    """
    results = []
    errors = []
    warnings = []

    source_dir = config.get_source_dir(category)

    if not source_dir or not source_dir.exists():
        logger.warning(f"ディレクトリが存在しません: {source_dir}")
        return results, errors, warnings

    # Markdownファイルを検索
    md_files = list(source_dir.glob("**/*.md"))
    logger.info(f"{category}: {len(md_files)} ファイルを処理中...")

    for md_file in md_files:
        try:
            # ファイル読み込み
            content = md_file.read_text(encoding="utf-8")

            # 変換
            record = transformer.transform(content, str(md_file))

            results.append(record)
            logger.debug(f"✓ {md_file.name}")

        except Exception as e:
            error_msg = str(e)
            errors.append({
                "file": str(md_file),
                "error": error_msg
            })
            logger.error(f"✗ {md_file.name}: {error_msg}")

    logger.info(f"{category}: {len(results)} 件成功, {len(errors)} 件エラー")

    return results, errors, warnings


def main():
    """メインエントリーポイント"""
    parser = argparse.ArgumentParser(
        description="ソロプレナー調査データ Markdown→JSONL変換パイプライン"
    )
    parser.add_argument(
        "--category",
        choices=["app", "sns", "newsletter", "all"],
        default="all",
        help="変換対象カテゴリ"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="出力ファイルパス（デフォルト: 自動生成）"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=config.OUTPUT_DIR,
        help=f"出力ディレクトリ（デフォルト: {config.OUTPUT_DIR}）"
    )
    parser.add_argument(
        "--split",
        action="store_true",
        help="カテゴリ別にファイル分割"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="詳細ログ出力"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="処理ファイル数制限（テスト用）"
    )

    args = parser.parse_args()

    # ロギング設定
    logger = setup_logging(args.verbose)

    logger.info("=== Markdown→JSONL変換パイプライン開始 ===")

    # トランスフォーマー初期化
    transformers = {
        "app": AppTransformer(),
        "sns": SnsTransformer(),
        "newsletter": NewsletterTransformer()
    }

    # 出力クラス初期化
    writer = JsonlWriter()
    report_gen = ReportGenerator()

    # カテゴリ決定
    if args.category == "all":
        categories = ["app", "sns", "newsletter"]
    else:
        categories = [args.category]

    # 全結果を格納
    all_results = []
    all_errors = []
    all_warnings = []

    # カテゴリごとに処理
    for category in categories:
        transformer = transformers[category]
        results, errors, warnings = process_category(category, transformer, logger)

        all_results.extend(results)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    # 結果サマリー
    logger.info(f"\n=== 変換完了 ===")
    logger.info(f"総ファイル数: {len(all_results) + len(all_errors)}")
    logger.info(f"成功: {len(all_results)}")
    logger.info(f"エラー: {len(all_errors)}")
    logger.info(f"警告: {len(all_warnings)}")

    # 出力
    if args.split:
        # カテゴリ別分割出力
        logger.info(f"\n=== カテゴリ別ファイル出力 ===")
        counts = writer.write_split_files(all_results, args.output_dir)

        for category, count in counts.items():
            logger.info(f"{category}: {count} 件")

    else:
        # 単一ファイル出力
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = args.output or (args.output_dir / f"solopreneur_data_{timestamp}.jsonl")

        count = writer.write(all_results, output_path)
        logger.info(f"\n出力: {output_path} ({count} records)")

    # レポート生成
    report = report_gen.generate(all_results, all_errors, all_warnings)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = args.output_dir / f"conversion_report_{timestamp}.md"
    report_path.write_text(report_gen.to_markdown(report), encoding="utf-8")

    logger.info(f"レポート: {report_path}")

    logger.info("\n=== 完了 ===")

    # エラーがあれば終了コード1
    return 1 if all_errors else 0


if __name__ == "__main__":
    exit(main())
