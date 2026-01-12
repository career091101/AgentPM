#!/usr/bin/env python3
"""
Dental Instagram Scraper - Main Script

このスクリプトは、歯科医院のInstagramアカウントを収集し、
プロフィール情報を抽出・検証してCSV出力します。

法的注意事項:
- Instagram利用規約を遵守してください
- 法人アカウント（歯科医院）の公開情報のみを収集します
- 個人情報保護法を遵守してください
- 収集したデータの利用目的を明確にしてください
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List

import yaml
from dotenv import load_dotenv
from tqdm import tqdm

from src.instagram_collector import InstagramCollector
from src.data_extractor import DataExtractor
from src.fact_checker import FactChecker
from src.csv_exporter import CSVExporter
from src.models import FinalRecord


def setup_logging(log_dir: str = 'logs') -> None:
    """
    ロギングの設定

    Args:
        log_dir: ログファイルの出力先ディレクトリ
    """
    # ログディレクトリの作成
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    # ログファイル名の生成
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_path / f'scraper_{timestamp}.log'

    # ロギング設定
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def load_config(config_path: str = 'config.yaml') -> dict:
    """
    設定ファイルの読み込み

    Args:
        config_path: 設定ファイルのパス

    Returns:
        dict: 設定データ
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def main():
    """メイン処理"""
    logger = logging.getLogger(__name__)

    try:
        # ロギングの設定
        setup_logging()
        logger.info("=" * 80)
        logger.info("Dental Instagram Scraper を開始します")
        logger.info("=" * 80)

        # 環境変数の読み込み
        load_dotenv()
        logger.info(".env ファイルを読み込みました")

        # 設定ファイルの読み込み
        config = load_config()
        logger.info("config.yaml を読み込みました")

        # 各コンポーネントの初期化
        logger.info("コンポーネントを初期化しています...")

        # Instagram収集設定
        instagram_username = os.getenv('INSTAGRAM_USERNAME')
        instagram_password = os.getenv('INSTAGRAM_PASSWORD')
        anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

        if not instagram_username or not instagram_password:
            raise ValueError("INSTAGRAM_USERNAME と INSTAGRAM_PASSWORD を .env ファイルに設定してください")
        if not anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY を .env ファイルに設定してください")

        collector = InstagramCollector(
            session_file=config.get('instagram', {}).get('session_file', '.instagram_session'),
            rate_limit_delay=config.get('rate_limit', {}).get('instagram', 5.0)
        )

        # Instagramにログイン
        logger.info("Instagramにログイン中...")
        if not collector.login(instagram_username, instagram_password):
            raise Exception("Instagramへのログインに失敗しました")

        extractor = DataExtractor(
            scrape_delay=config.get('rate_limit', {}).get('web_scraping', 2.0),
            request_timeout=config.get('timeout', {}).get('http_request', 30)
        )
        fact_checker = FactChecker(anthropic_api_key)
        exporter = CSVExporter()

        # ハッシュタグ検索とプロフィール収集
        hashtags = config.get('hashtags', ['歯科', '歯医者', 'デンタルクリニック'])
        max_posts = config.get('max_posts_per_hashtag', 100)

        logger.info(f"ハッシュタグ検索を開始します: {hashtags}")
        logger.info(f"ハッシュタグあたりの最大投稿数: {max_posts}")

        profiles = []
        for hashtag in hashtags:
            logger.info(f"ハッシュタグ #{hashtag} を検索中...")
            hashtag_profiles = collector.collect_from_hashtag(hashtag, max_posts)
            profiles.extend(hashtag_profiles)
            logger.info(f"#{hashtag} から {len(hashtag_profiles)} 件のプロフィールを収集しました")

        # 重複削除
        unique_profiles = {p.username: p for p in profiles}.values()
        logger.info(f"重複を除外: 合計 {len(unique_profiles)} 件のユニークなプロフィール")

        # 各プロフィールの処理
        final_records: List[FinalRecord] = []
        verified_count = 0
        failed_count = 0

        logger.info("プロフィールの抽出と検証を開始します...")

        with tqdm(total=len(unique_profiles), desc="処理中", unit="profile") as pbar:
            for profile in unique_profiles:
                try:
                    # データ抽出
                    extracted_data = extractor.extract(profile)

                    # ファクトチェック
                    verification_result = fact_checker.verify(extracted_data)

                    # FinalRecord生成
                    final_record = FinalRecord(
                        instagram_handle=profile.username,
                        clinic_name=extracted_data.clinic_name,
                        postal_code=extracted_data.postal_code,
                        address=extracted_data.address,
                        extracted_person_name=extracted_data.person_name,
                        external_link_url=extracted_data.external_link,
                        phone_number=extracted_data.phone_number,
                        follower_count=profile.followers_count,
                        bio_text=profile.bio,
                        fact_check_status=verification_result.status,
                        fact_check_confidence=verification_result.similarity_score,
                        verified_address=verification_result.verified_address,
                        verification_source=verification_result.sources[0] if verification_result.sources else None,
                        needs_manual_review=extracted_data.needs_manual_review or (verification_result.status != 'verified'),
                        collected_at=datetime.now().isoformat()
                    )

                    final_records.append(final_record)

                    if verification_result.status == 'verified':
                        verified_count += 1
                    else:
                        failed_count += 1

                except KeyboardInterrupt:
                    logger.warning("ユーザーによる中断を検出しました")
                    raise

                except Exception as e:
                    logger.error(f"プロフィール {profile.username} の処理中にエラーが発生: {e}")
                    failed_count += 1

                finally:
                    pbar.update(1)

        # CSV出力
        output_dir = config.get('output_dir', 'data/output')
        logger.info(f"CSV出力を開始します: {output_dir}")
        output_path = exporter.export(final_records, output_dir)

        # サマリー出力
        logger.info("=" * 80)
        logger.info("処理が完了しました")
        logger.info("=" * 80)
        logger.info(f"総プロフィール数: {len(unique_profiles)}")
        logger.info(f"検証成功: {verified_count} 件")
        logger.info(f"検証失敗/エラー: {failed_count} 件")
        logger.info(f"出力ファイル: {output_path}")
        logger.info("=" * 80)

        return 0

    except KeyboardInterrupt:
        logger.warning("\n" + "=" * 80)
        logger.warning("処理が中断されました（Ctrl+C）")

        # 部分結果を保存
        if final_records:
            logger.info("収集済みの部分結果を保存します...")
            try:
                output_dir = config.get('output_dir', 'data/output')
                output_path = exporter.export(final_records, output_dir)
                logger.info(f"部分結果を保存しました: {output_path} ({len(final_records)}件)")
            except Exception as e:
                logger.error(f"部分結果の保存に失敗しました: {e}")

        logger.warning("=" * 80)
        return 1

    except Exception as e:
        logger.error("=" * 80)
        logger.error("予期しないエラーが発生しました")
        logger.error("=" * 80)
        logger.exception(e)
        logger.error("=" * 80)
        return 1


if __name__ == '__main__':
    sys.exit(main())
