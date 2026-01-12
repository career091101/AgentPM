#!/usr/bin/env python3
"""
Dental Instagram Scraper - デモンストレーション（実際のInstagram接続なし）

このスクリプトは、実際のInstagram認証情報なしで、
システムのデータ抽出とCSV出力機能をデモンストレーションします。
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List

from src.models import InstagramProfile, FinalRecord
from src.data_extractor import DataExtractor
from src.csv_exporter import CSVExporter


def setup_logging() -> None:
    """ロギング設定"""
    log_path = Path('logs')
    log_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_path / f'demo_{timestamp}.log'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def create_demo_profiles() -> List[InstagramProfile]:
    """デモ用のダミープロフィール生成"""
    profiles = [
        InstagramProfile(
            username="sample_dental",
            full_name="サンプル歯科クリニック",
            bio="""
                〒150-0043 東京都渋谷区道玄坂1-2-3
                電話: 03-1234-5678
                院長: 山田太郎
                一般歯科、小児歯科、矯正歯科
                平日 9:00-18:00、土曜 9:00-13:00
            """,
            external_url="https://sample-dental.example.com",
            followers_count=1500,
            following_count=200,
            posts_count=120
        ),
        InstagramProfile(
            username="tokyo_smile_dental",
            full_name="東京スマイル歯科医院",
            bio="""
                東京スマイル歯科医院
                審美歯科・ホワイトニング専門
                〒160-0023 東京都新宿区西新宿2-8-1
                営業時間: 10:00-20:00
                院長: 佐藤花子
            """,
            external_url="https://tokyo-smile-dental.example.com",
            followers_count=2800,
            following_count=300,
            posts_count=250
        ),
        InstagramProfile(
            username="ginza_orthodontics",
            full_name="銀座矯正歯科",
            bio="""
                銀座矯正歯科
                〒104-0061 東京都中央区銀座5-3-1
                インビザライン・マウスピース矯正専門
                院長: 鈴木一郎
                TEL: 03-3456-7890
            """,
            external_url="https://ginza-ortho.example.com",
            followers_count=4200,
            following_count=150,
            posts_count=180
        ),
        InstagramProfile(
            username="yokohama_family_dental",
            full_name="横浜ファミリー歯科",
            bio="""
                横浜ファミリー歯科
                お子様からご年配の方まで
                〒220-0004 神奈川県横浜市西区北幸1-5-10
                院長: 田中健太
                予約優先制
                平日 9:00-17:00
            """,
            external_url="https://yokohama-family.example.com",
            followers_count=1890,
            following_count=250,
            posts_count=95
        ),
        InstagramProfile(
            username="shibuya_whitening",
            full_name="渋谷ホワイトニングデンタル",
            bio="""
                渋谷ホワイトニングデンタル
                当日予約OK
                〒150-0002 東京都渋谷区渋谷1-1-8
                ホワイトニング・審美歯科
            """,
            external_url="https://shibuya-whitening.example.com",
            followers_count=5600,
            following_count=400,
            posts_count=320
        ),
    ]
    return profiles


def demo_data_extraction():
    """デモ：データ抽出"""
    logger = logging.getLogger(__name__)

    print("\n" + "="*80)
    print("デモンストレーション：データ抽出機能")
    print("="*80 + "\n")

    profiles = create_demo_profiles()
    extractor = DataExtractor(scrape_delay=0.5, request_timeout=10)

    logger.info(f"デモ用ダミープロフィール {len(profiles)} 件を作成")

    # FinalRecord生成用
    final_records: List[FinalRecord] = []

    for i, profile in enumerate(profiles, 1):
        print(f"\n[{i}/{len(profiles)}] 処理中: @{profile.username}")
        print("-" * 60)

        try:
            # データ抽出
            extracted = extractor.extract(profile)

            print(f"  医院名: {extracted.clinic_name}")
            print(f"  住所: {extracted.address}")
            print(f"  郵便番号: {extracted.postal_code}")
            print(f"  電話番号: {extracted.phone_number}")
            print(f"  院長名: {extracted.person_name}")
            print(f"  信頼度スコア: {extracted.confidence:.2f}")

            # FinalRecord生成
            final_record = FinalRecord(
                instagram_handle=profile.username,
                clinic_name=extracted.clinic_name,
                postal_code=extracted.postal_code,
                address=extracted.address,
                extracted_person_name=extracted.person_name,
                external_link_url=extracted.external_link,
                phone_number=extracted.phone_number,
                follower_count=profile.followers_count,
                bio_text=profile.bio,
                fact_check_status="demo",
                fact_check_confidence=extracted.confidence,
                verified_address=extracted.address,
                verification_source=profile.external_url,
                needs_manual_review=extracted.needs_manual_review,
                collected_at=datetime.now().isoformat()
            )

            final_records.append(final_record)
            logger.info(f"@{profile.username}: 抽出成功 (信頼度: {extracted.confidence:.2f})")

        except Exception as e:
            logger.error(f"@{profile.username}: 抽出失敗 - {str(e)}")
            print(f"  ❌ エラー: {str(e)}")

    return final_records


def demo_csv_export(records: List[FinalRecord]) -> str:
    """デモ：CSV出力"""
    logger = logging.getLogger(__name__)

    print("\n" + "="*80)
    print("デモンストレーション：CSV出力機能")
    print("="*80 + "\n")

    exporter = CSVExporter()
    output_dir = "data/output"

    try:
        output_path = exporter.export(records, output_dir)
        print(f"✅ CSV出力成功")
        print(f"   ファイルパス: {output_path}")
        print(f"   出力件数: {len(records)} 件")
        logger.info(f"CSV出力完了: {output_path} ({len(records)}件)")
        return output_path

    except Exception as e:
        logger.error(f"CSV出力失敗: {str(e)}")
        print(f"❌ CSV出力エラー: {str(e)}")
        return ""


def main():
    """メイン処理"""
    setup_logging()
    logger = logging.getLogger(__name__)

    print("\n" + "="*80)
    print("Dental Instagram Scraper - デモンストレーション")
    print("="*80)
    print("\n注: このデモはダミーデータを使用しています。")
    print("実際のInstagram収集機能は使用していません。\n")

    try:
        # デモ1: データ抽出
        final_records = demo_data_extraction()

        if not final_records:
            print("\n❌ データ抽出に失敗しました")
            return 1

        # デモ2: CSV出力
        output_path = demo_csv_export(final_records)

        if not output_path:
            print("\n❌ CSV出力に失敗しました")
            return 1

        # サマリー表示
        print("\n" + "="*80)
        print("デモ完了")
        print("="*80)
        print(f"処理プロフィール数: {len(final_records)} 件")
        print(f"出力ファイル: {output_path}")
        print("\n実際のInstagram収集を実行するには：")
        print("  1. .env.exampleをコピーして.envを作成")
        print("  2. INSTAGRAM_USERNAMEとINSTAGRAM_PASSWORDを設定")
        print("  3. ANTHROPIC_API_KEYを設定")
        print("  4. python main.py を実行")
        print("="*80 + "\n")

        return 0

    except KeyboardInterrupt:
        logger.warning("ユーザーによる中断を検出しました")
        print("\n⚠️  デモが中断されました（Ctrl+C）")
        return 1

    except Exception as e:
        logger.error(f"予期しないエラー: {str(e)}")
        print(f"\n❌ エラーが発生しました: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
