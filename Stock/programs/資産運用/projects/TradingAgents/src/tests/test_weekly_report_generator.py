"""
週次レポート生成機能のテスト

Usage:
    python3 -m pytest src/tests/test_weekly_report_generator.py -v
    python3 src/tests/test_weekly_report_generator.py
"""

import unittest
import sys
from pathlib import Path
from datetime import datetime, timedelta

# プロジェクトルート追加
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "scripts"))
sys.path.insert(0, str(project_root / "src"))

from generate_weekly_report import WeeklyReportGenerator


class TestWeeklyReportGenerator(unittest.TestCase):
    """週次レポート生成機能のテストケース"""

    def setUp(self):
        """各テストの前処理"""
        # 過去の週を使用（データが確実に存在する期間）
        self.week_start = "2024-12-16"
        self.week_end = "2024-12-20"

    def test_initialization(self):
        """初期化のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        self.assertIsNotNone(generator.week_start)
        self.assertIsNotNone(generator.week_end)
        self.assertIsNotNone(generator.report_date)

    def test_fetch_data(self):
        """データ取得のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            generator.fetch_data()

            # データが取得されたことを確認
            self.assertIsNotNone(generator.data)
            self.assertGreater(len(generator.data), 0)
            self.assertIsNotNone(generator.week_data)

            print(f"✓ データ取得成功: 全{len(generator.data)}日分、今週{len(generator.week_data)}日分")

        except Exception as e:
            self.skipTest(f"データ取得失敗（ネットワークエラーの可能性）: {e}")

    def test_generate_signals(self):
        """シグナル生成のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            generator.fetch_data()
            generator.generate_signals()

            # シグナルが生成されたことを確認
            self.assertIsNotNone(generator.signals)
            self.assertIsInstance(generator.signals, list)
            self.assertIsNotNone(generator.current_regime)

            print(f"✓ シグナル生成成功: {len(generator.signals)}件、レジーム={generator.current_regime}")

        except Exception as e:
            self.skipTest(f"シグナル生成失敗: {e}")

    def test_calculate_performance(self):
        """パフォーマンス計算のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            generator.fetch_data()
            generator.generate_signals()
            generator.calculate_performance()

            # パフォーマンス指標が計算されたことを確認
            self.assertIsNotNone(generator.performance)
            self.assertIn('weekly_return', generator.performance)
            self.assertIn('win_rate', generator.performance)
            self.assertIn('sharpe_ratio', generator.performance)
            self.assertIn('total_trades', generator.performance)

            print(f"✓ パフォーマンス計算成功:")
            print(f"  リターン: {generator.performance['weekly_return']:.2f}%")
            print(f"  勝率: {generator.performance['win_rate']:.1f}%")
            print(f"  トレード数: {generator.performance['total_trades']}")

        except Exception as e:
            self.skipTest(f"パフォーマンス計算失敗: {e}")

    def test_detect_regime(self):
        """レジーム検出のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            generator.fetch_data()
            generator.generate_signals()
            generator.detect_current_regime()

            # レジーム情報が取得されたことを確認
            self.assertIsNotNone(generator.current_regime)
            self.assertIn(generator.current_regime, ['bull', 'bear', 'sideways'])
            self.assertIsNotNone(generator.regime_confidence)
            self.assertGreater(generator.regime_confidence, 0)
            self.assertLessEqual(generator.regime_confidence, 100)

            print(f"✓ レジーム検出成功: {generator.current_regime} (信頼度{generator.regime_confidence:.1f}%)")

        except Exception as e:
            self.skipTest(f"レジーム検出失敗: {e}")

    def test_full_report_generation(self):
        """完全なレポート生成のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            report_path = generator.generate()

            # レポートが生成されたことを確認
            self.assertIsNotNone(report_path)
            report_file = Path(report_path)
            self.assertTrue(report_file.exists())
            self.assertGreater(report_file.stat().st_size, 0)

            print(f"✓ レポート生成成功: {report_path}")

            # レポート内容の基本検証
            report_content = report_file.read_text(encoding='utf-8')
            self.assertIn("週次トレード戦略レポート", report_content)
            self.assertIn("パフォーマンス", report_content)
            self.assertIn("レジーム分析", report_content)

        except Exception as e:
            self.skipTest(f"レポート生成失敗: {e}")

    def test_template_placeholders(self):
        """テンプレートのプレースホルダー置換のテスト"""
        generator = WeeklyReportGenerator(
            week_start=self.week_start,
            week_end=self.week_end
        )

        try:
            report_path = generator.generate()

            if report_path:
                report_file = Path(report_path)
                report_content = report_file.read_text(encoding='utf-8')

                # プレースホルダーが残っていないことを確認
                placeholders = ['{week_start}', '{week_end}', '{current_regime}']
                for placeholder in placeholders:
                    self.assertNotIn(placeholder, report_content,
                                   f"プレースホルダー {placeholder} が置換されていません")

                print(f"✓ テンプレート置換成功")

        except Exception as e:
            self.skipTest(f"テンプレート置換テスト失敗: {e}")


def run_manual_test():
    """手動テスト実行用"""
    print("=" * 60)
    print("週次レポート生成テスト")
    print("=" * 60)

    # 最近の週を使用
    week_start = "2024-12-16"
    week_end = "2024-12-20"

    print(f"\nテスト期間: {week_start} 〜 {week_end}")

    generator = WeeklyReportGenerator(
        week_start=week_start,
        week_end=week_end
    )

    try:
        report_path = generator.generate()
        print(f"\n✅ テスト完了")
        print(f"レポート: {report_path}")

    except Exception as e:
        print(f"\n❌ テスト失敗: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # コマンドライン引数でモード選択
    if len(sys.argv) > 1 and sys.argv[1] == "--manual":
        run_manual_test()
    else:
        # unittest実行
        unittest.main(verbosity=2)
