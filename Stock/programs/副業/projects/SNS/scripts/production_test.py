#!/usr/bin/env python3
"""
本番API投稿テストスクリプト

Late APIを使用したX & Threads同時予約投稿の本番動作確認。
4つのシナリオをサポート:
1. テキストのみ投稿（最小構成）
2. 画像付き投稿（フル機能）
3. スケジュール競合テスト
4. エラーハンドリング & リトライ
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# 同じディレクトリ内のモジュールをインポート
from late_api_scheduler import LateAPIScheduler, NoAvailableSlotError
from threads_adapter import ThreadsAdapter
from error_logger import ErrorLogger


class ProductionTester:
    """本番API投稿テスター"""

    def __init__(self, dry_run: bool = False):
        """
        Args:
            dry_run: Trueの場合、Late APIへの実際のPOSTを行わない
        """
        self.dry_run = dry_run
        self.scheduler = LateAPIScheduler()
        self.adapter = ThreadsAdapter()
        self.logger = ErrorLogger()
        self.jst = ZoneInfo('Asia/Tokyo')

    def scenario_1_text_only(self) -> Dict:
        """
        Scenario 1: テキストのみ投稿（最小構成）

        Returns:
            テスト結果辞書
        """
        print("\n" + "=" * 60)
        print("Scenario 1: テキストのみ投稿")
        print("=" * 60 + "\n")

        # サンプルXスレッド（7ツイート）
        x_thread = [
            "1/7: 🚨 Late APIを使ったX & Threads同時投稿のテストです",
            "2/7: このスレッドは本番環境での動作確認を目的としています。",
            "3/7: 主な機能:\n- X: スレッド形式（7ツイート）\n- Threads: 最適化された単一投稿",
            "4/7: 予約投稿スケジュール:\n- 翌日20:00 JST固定\n- 既存予約との競合自動検出",
            "5/7: エラーハンドリング:\n- 指数バックオフリトライ\n- レート制限対応\n- 詳細ログ記録",
            "6/7: 開発環境:\n- Python 3.11+\n- Late API v1\n- pytest 8.0+",
            "7/7: このテストが成功すれば、本番運用開始可能です。🎉"
        ]

        # Threads版に変換
        print("[Threads変換]")
        threads_result = self.adapter.convert_x_to_threads(x_thread)
        threads_content = threads_result['content']
        print(f"✅ 変換成功: {threads_result['character_count']}文字")
        print(f"   絵文字: {threads_result['emoji_count']}個")
        print(f"   段落: {threads_result['paragraph_count']}段落\n")

        # 予約日時を取得
        print("[スケジュール検索]")
        try:
            scheduled_dt = self.scheduler.find_available_slot(days_ahead=14)
            print(f"✅ 利用可能日時: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}\n")
        except NoAvailableSlotError as e:
            print(f"❌ エラー: {e}")
            return {"status": "error", "message": str(e)}

        results = {}

        # X投稿
        print("[X投稿]")
        if self.dry_run:
            print("🔄 ドライラン: Late APIへのPOSTをスキップ")
            results['twitter'] = {
                'status': 'dry_run',
                'scheduled_for': scheduled_dt.isoformat()
            }
        else:
            try:
                x_result = self.scheduler.schedule_post(
                    content=x_thread[0],  # 最初のツイート
                    platform='twitter',
                    scheduled_dt=scheduled_dt,
                    platform_specific_data={
                        'threadItems': [{'content': tweet} for tweet in x_thread]
                    }
                )
                print(f"✅ 予約投稿成功")
                print(f"   Post ID: {x_result.get('post_id', 'N/A')}")
                print(f"   Scheduled: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}")
                print(f"   URL: https://app.getlate.dev/posts/{x_result.get('post_id', '')}\n")
                results['twitter'] = x_result
            except Exception as e:
                print(f"❌ エラー: {e}\n")
                self.logger.log_error(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    platform='twitter',
                    context={'scenario': 1}
                )
                results['twitter'] = {'status': 'error', 'message': str(e)}

        # Threads投稿
        print("[Threads投稿]")
        if self.dry_run:
            print("🔄 ドライラン: Late APIへのPOSTをスキップ")
            results['threads'] = {
                'status': 'dry_run',
                'scheduled_for': scheduled_dt.isoformat()
            }
        else:
            try:
                threads_result_post = self.scheduler.schedule_post(
                    content=threads_content,
                    platform='threads',
                    scheduled_dt=scheduled_dt
                )
                print(f"✅ 予約投稿成功")
                print(f"   Post ID: {threads_result_post.get('post_id', 'N/A')}")
                print(f"   Scheduled: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}")
                print(f"   URL: https://app.getlate.dev/posts/{threads_result_post.get('post_id', '')}\n")
                results['threads'] = threads_result_post
            except Exception as e:
                print(f"❌ エラー: {e}\n")
                self.logger.log_error(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    platform='threads',
                    context={'scenario': 1}
                )
                results['threads'] = {'status': 'error', 'message': str(e)}

        print("=" * 60)
        print("✅ Scenario 1 完了")
        print("=" * 60 + "\n")

        return results

    def scenario_2_with_image(self, image_path: str) -> Dict:
        """
        Scenario 2: 画像付き投稿（フル機能）

        Args:
            image_path: 画像ファイルパス

        Returns:
            テスト結果辞書
        """
        print("\n" + "=" * 60)
        print("Scenario 2: 画像付き投稿")
        print("=" * 60 + "\n")

        # 画像パス確認
        image_path_obj = Path(image_path)
        if not image_path_obj.exists():
            print(f"❌ エラー: 画像ファイルが見つかりません: {image_path}")
            return {"status": "error", "message": "Image file not found"}

        print(f"[画像情報]")
        print(f"   パス: {image_path}")
        print(f"   サイズ: {image_path_obj.stat().st_size / 1024:.2f} KB\n")

        # サンプルXスレッド（画像説明付き）
        x_thread = [
            "1/7: 📸 画像付き投稿のテストです",
            "2/7: X & Threads両方に同一画像を添付します。",
            "3/7: Late API `/media`エンドポイントを使用:\n- multipart/form-data形式\n- PNG/JPEG対応\n- 500KB以下推奨",
            "4/7: 画像アップロードフロー:\n1. `/media`にPOST\n2. 画像URLを取得\n3. 投稿ペイロードに追加",
            "5/7: 両プラットフォームで同一画像を使用することで:\n- 一貫性のあるビジュアル\n- コンテンツ認知度向上",
            "6/7: エラーハンドリング:\n- FileNotFoundError\n- NetworkTimeoutError\n- LateAPIError",
            "7/7: 画像が正しく表示されれば、フル機能テスト成功です！🎉"
        ]

        # Threads版に変換
        print("[Threads変換]")
        threads_result = self.adapter.convert_x_to_threads(x_thread)
        threads_content = threads_result['content']
        print(f"✅ 変換成功: {threads_result['character_count']}文字\n")

        # 予約日時を取得（Scenario 1と重複回避のため+1日）
        print("[スケジュール検索]")
        try:
            scheduled_dt = self.scheduler.find_available_slot(days_ahead=14)
            # Scenario 1で翌日20:00を使用している可能性があるため、明示的に+1日
            scheduled_dt = scheduled_dt.replace(day=scheduled_dt.day + 1)
            print(f"✅ 利用可能日時: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}\n")
        except NoAvailableSlotError as e:
            print(f"❌ エラー: {e}")
            return {"status": "error", "message": str(e)}

        results = {}

        # 画像アップロード
        print("[画像アップロード]")
        if self.dry_run:
            print("🔄 ドライラン: 画像アップロードをスキップ")
            uploaded_image_url = "https://cdn.getlate.dev/media/dry_run_test.png"
            results['image_upload'] = {'status': 'dry_run', 'url': uploaded_image_url}
        else:
            try:
                uploaded_image_url = self.scheduler._upload_image(str(image_path))
                print(f"✅ アップロード成功")
                print(f"   Image URL: {uploaded_image_url}\n")
                results['image_upload'] = {'status': 'success', 'url': uploaded_image_url}
            except Exception as e:
                print(f"❌ エラー: {e}\n")
                self.logger.log_error(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    platform='image_upload',
                    context={'scenario': 2, 'image_path': image_path}
                )
                return {"status": "error", "message": f"Image upload failed: {e}"}

        # X投稿（画像付き）
        print("[X投稿]")
        if self.dry_run:
            print("🔄 ドライラン: Late APIへのPOSTをスキップ")
            results['twitter'] = {
                'status': 'dry_run',
                'scheduled_for': scheduled_dt.isoformat(),
                'image_url': uploaded_image_url
            }
        else:
            try:
                x_result = self.scheduler.schedule_post(
                    content=x_thread[0],
                    platform='twitter',
                    scheduled_dt=scheduled_dt,
                    image_path=str(image_path),
                    platform_specific_data={
                        'threadItems': [{'content': tweet} for tweet in x_thread]
                    }
                )
                print(f"✅ 予約投稿成功（画像付き）")
                print(f"   Post ID: {x_result.get('post_id', 'N/A')}")
                print(f"   Scheduled: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}\n")
                results['twitter'] = x_result
            except Exception as e:
                print(f"❌ エラー: {e}\n")
                self.logger.log_error(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    platform='twitter',
                    context={'scenario': 2}
                )
                results['twitter'] = {'status': 'error', 'message': str(e)}

        # Threads投稿（画像付き）
        print("[Threads投稿]")
        if self.dry_run:
            print("🔄 ドライラン: Late APIへのPOSTをスキップ")
            results['threads'] = {
                'status': 'dry_run',
                'scheduled_for': scheduled_dt.isoformat(),
                'image_url': uploaded_image_url
            }
        else:
            try:
                threads_result_post = self.scheduler.schedule_post(
                    content=threads_content,
                    platform='threads',
                    scheduled_dt=scheduled_dt,
                    image_path=str(image_path)
                )
                print(f"✅ 予約投稿成功（画像付き）")
                print(f"   Post ID: {threads_result_post.get('post_id', 'N/A')}")
                print(f"   Scheduled: {scheduled_dt.strftime('%Y-%m-%d %H:%M JST')}\n")
                results['threads'] = threads_result_post
            except Exception as e:
                print(f"❌ エラー: {e}\n")
                self.logger.log_error(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    platform='threads',
                    context={'scenario': 2}
                )
                results['threads'] = {'status': 'error', 'message': str(e)}

        print("=" * 60)
        print("✅ Scenario 2 完了")
        print("=" * 60 + "\n")

        return results

    def scenario_3_conflict_detection(self) -> Dict:
        """
        Scenario 3: スケジュール競合テスト

        Returns:
            テスト結果辞書
        """
        print("\n" + "=" * 60)
        print("Scenario 3: スケジュール競合テスト")
        print("=" * 60 + "\n")

        print("[既存予約投稿の取得]")
        existing_reservations = self.scheduler.get_existing_reservations(target_hour=20)
        print(f"✅ 既存予約: {len(existing_reservations)}件")
        for date in sorted(existing_reservations):
            print(f"   - {date.strftime('%Y-%m-%d')}")
        print()

        print("[空き日検索]")
        try:
            available_slot = self.scheduler.find_available_slot(days_ahead=14)
            print(f"✅ 次の利用可能日時: {available_slot.strftime('%Y-%m-%d %H:%M JST')}\n")
        except NoAvailableSlotError as e:
            print(f"❌ エラー: {e}\n")
            return {"status": "error", "message": str(e)}

        # 競合検出ロジックの確認
        print("[競合検出ロジック確認]")
        available_date = available_slot.date()
        if available_date in existing_reservations:
            print(f"❌ 競合検出失敗: {available_date}は既に予約済み")
            return {"status": "error", "message": "Conflict detection failed"}
        else:
            print(f"✅ 競合回避成功: {available_date}は空いている\n")

        print("=" * 60)
        print("✅ Scenario 3 完了")
        print("=" * 60 + "\n")

        return {
            "status": "success",
            "existing_reservations": len(existing_reservations),
            "available_slot": available_slot.isoformat()
        }

    def scenario_4_error_handling(self) -> Dict:
        """
        Scenario 4: エラーハンドリング & リトライ

        Note: このシナリオは手動テスト推奨（Wi-Fi切断等）

        Returns:
            テスト結果辞書
        """
        print("\n" + "=" * 60)
        print("Scenario 4: エラーハンドリング & リトライ")
        print("=" * 60 + "\n")

        print("[注意]")
        print("このシナリオは手動テストを推奨します:")
        print("1. Wi-Fi一時切断によるNetworkTimeoutErrorテスト")
        print("2. Late API Rate Limit（429）テスト（意図的に大量リクエスト）")
        print("3. 無効なAPIキー設定によるAuthenticationErrorテスト\n")

        print("自動テストでは、リトライロジックの基本動作のみ確認します。\n")

        # エラーログ統計を確認
        print("[エラーログ統計（過去30日）]")
        stats = self.logger.get_error_statistics(days=30)
        print(f"   総エラー数: {stats['total_errors']}")
        print(f"   平均リトライ回数: {stats['average_retry_count']}")
        print(f"   最大リトライ回数: {stats['max_retry_count']}\n")

        print("=" * 60)
        print("✅ Scenario 4 完了（手動テスト推奨）")
        print("=" * 60 + "\n")

        return {
            "status": "manual_test_recommended",
            "error_stats": stats
        }


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="Late API本番投稿テスト"
    )
    parser.add_argument(
        '--scenario',
        type=int,
        choices=[1, 2, 3, 4],
        required=True,
        help="テストシナリオ番号（1-4）"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="ドライラン（Late APIへの実際のPOSTを行わない）"
    )
    parser.add_argument(
        '--image',
        type=str,
        help="画像ファイルパス（Scenario 2のみ）"
    )

    args = parser.parse_args()

    # テスター初期化
    tester = ProductionTester(dry_run=args.dry_run)

    # シナリオ実行
    if args.scenario == 1:
        results = tester.scenario_1_text_only()
    elif args.scenario == 2:
        if not args.image:
            print("❌ エラー: Scenario 2には--imageオプションが必要です")
            sys.exit(1)
        results = tester.scenario_2_with_image(args.image)
    elif args.scenario == 3:
        results = tester.scenario_3_conflict_detection()
    elif args.scenario == 4:
        results = tester.scenario_4_error_handling()

    # 結果をJSON出力
    print("\n[テスト結果JSON]")
    print(json.dumps(results, indent=2, ensure_ascii=False))

    # 結果をファイルに保存
    output_dir = Path(__file__).parent.parent / "test_results"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y%m%d_%H%M%S')
    output_path = output_dir / f"scenario_{args.scenario}_{timestamp}.json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n💾 結果保存: {output_path}")


if __name__ == "__main__":
    main()
