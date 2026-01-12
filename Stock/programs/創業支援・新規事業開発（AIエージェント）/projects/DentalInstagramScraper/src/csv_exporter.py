"""
CSV Exporter Module

This module handles exporting the collected and verified Instagram data to CSV format.
"""

import csv
from datetime import datetime
from pathlib import Path
from typing import List
import logging

from .models import FinalRecord


class CSVExporter:
    """CSV出力クラス：Instagram収集データをCSV形式で出力"""

    HEADERS = [
        'instagram_handle', 'clinic_name', 'postal_code', 'address',
        'extracted_person_name', 'external_link_url', 'phone_number',
        'follower_count', 'bio_text', 'fact_check_status',
        'fact_check_confidence', 'verified_address', 'verification_source',
        'needs_manual_review', 'collected_at'
    ]

    def __init__(self):
        """CSVExporterの初期化"""
        self.logger = logging.getLogger(__name__)

    def export(self, records: List[FinalRecord], output_dir: str) -> str:
        """
        レコードをCSVファイルに出力

        Args:
            records: 出力するFinalRecordのリスト
            output_dir: 出力先ディレクトリのパス

        Returns:
            str: 出力したCSVファイルのパス

        Raises:
            IOError: ファイル書き込みに失敗した場合
        """
        # 出力ディレクトリの作成
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # ファイル名の生成（dental_instagram_YYYYMMDD_HHMMSS.csv）
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'dental_instagram_{timestamp}.csv'
        filepath = output_path / filename

        self.logger.info(f"CSVファイルを出力中: {filepath}")

        try:
            # UTF-8 BOM付きでCSVファイルを書き込み
            with open(filepath, 'w', encoding='utf-8-sig', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.HEADERS)

                # ヘッダー行を書き込み
                writer.writeheader()

                # データ行を書き込み
                for record in records:
                    row = self._record_to_dict(record)
                    writer.writerow(row)

            self.logger.info(f"CSVファイルを正常に出力しました: {filepath} ({len(records)}件)")
            return str(filepath)

        except Exception as e:
            self.logger.error(f"CSVファイルの出力に失敗しました: {e}")
            raise IOError(f"CSVファイルの書き込みエラー: {e}") from e

    def _record_to_dict(self, record: FinalRecord) -> dict:
        """
        FinalRecordを辞書形式に変換

        Args:
            record: 変換するFinalRecord

        Returns:
            dict: CSVの1行分のデータ
        """
        # bio_textの改行を\\nにエスケープ
        bio_text = record.bio_text.replace('\n', '\\n') if record.bio_text else ''

        return {
            'instagram_handle': record.instagram_handle or '',
            'clinic_name': record.clinic_name or '',
            'postal_code': record.postal_code or '',
            'address': record.address or '',
            'extracted_person_name': record.extracted_person_name or '',
            'external_link_url': record.external_link_url or '',
            'phone_number': record.phone_number or '',
            'follower_count': record.follower_count or 0,
            'bio_text': bio_text,
            'fact_check_status': record.fact_check_status or '',
            'fact_check_confidence': f"{record.fact_check_confidence:.2f}" if record.fact_check_confidence is not None else '',
            'verified_address': record.verified_address or '',
            'verification_source': record.verification_source or '',
            'needs_manual_review': str(record.needs_manual_review).lower() if record.needs_manual_review is not None else 'false',
            'collected_at': record.collected_at or ''
        }
