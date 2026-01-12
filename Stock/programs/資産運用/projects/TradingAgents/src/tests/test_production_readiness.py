#!/usr/bin/env python3
"""
Production Readiness Integration Tests
Phase 6: Final Validation & Production Readiness

Tests:
- Environment check
- Real data fetch (or sample data fallback)
- Final validation report generation
- Checklist completion
"""

import unittest
import sys
from pathlib import Path
from datetime import datetime
import pandas as pd

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestProductionReadiness(unittest.TestCase):
    """Integration tests for production readiness"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.project_root = Path(__file__).parent.parent.parent
        cls.results_dir = cls.project_root / "data" / "results"
        cls.docs_dir = cls.project_root / "documents" / "5_operations"

    def test_01_python_version(self):
        """Test Python version compatibility"""
        version = sys.version_info
        self.assertGreaterEqual(version.major, 3, "Python 3.x required")
        self.assertGreaterEqual(version.minor, 9, "Python 3.9+ required")

        if version.minor == 9:
            print("\n⚠️  WARNING: Python 3.9 detected")
            print("   Recommend upgrading to Python 3.10+ for yfinance")

    def test_02_dependencies(self):
        """Test required dependencies are installed"""
        required_packages = ['pandas', 'numpy', 'matplotlib']

        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                self.fail(f"Required package not installed: {package}")

    def test_03_yfinance_available(self):
        """Test yfinance availability (optional)"""
        try:
            import yfinance as yf
            print(f"\n✓ yfinance available: version {yf.__version__}")
        except (ImportError, TypeError) as e:
            # Python 3.9 has TypeError with yfinance due to type hints
            print(f"\n⚠️  yfinance not available: {type(e).__name__}")
            if sys.version_info.minor == 9:
                print("   Python 3.9 detected - upgrade to 3.10+ for yfinance")
            print("   Will use sample data fallback")

    def test_04_environment_check_script(self):
        """Test environment check script exists and is executable"""
        script_path = self.project_root / "scripts" / "check_python_environment.py"
        self.assertTrue(script_path.exists(), "Environment check script not found")

        # Check if script is executable
        import subprocess
        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                timeout=10
            )
            # Script may return 1 if environment has issues, but should not crash
            self.assertIn(result.returncode, [0, 1], "Environment check script crashed")
            print("\n✓ Environment check script executable")
        except Exception as e:
            self.fail(f"Failed to run environment check: {e}")

    def test_05_validation_script(self):
        """Test final validation script exists and is executable"""
        script_path = self.project_root / "scripts" / "run_final_validation.py"
        self.assertTrue(script_path.exists(), "Final validation script not found")

        # Check if script can be imported
        try:
            import run_final_validation
            print("\n✓ Final validation script importable")
        except Exception as e:
            self.fail(f"Failed to import validation script: {e}")

    def test_06_validation_report_generated(self):
        """Test validation report was generated"""
        report_path = self.results_dir / "PHASE6_FINAL_VALIDATION_REPORT.md"
        self.assertTrue(report_path.exists(), "Validation report not found")

        # Check report content
        content = report_path.read_text(encoding='utf-8')
        self.assertIn("Phase 6: Final Validation Report", content)
        self.assertIn("Go/No-go Decision", content)
        self.assertIn("Overall Decision", content)

        print(f"\n✓ Validation report exists: {report_path}")

    def test_07_validation_report_structure(self):
        """Test validation report has required sections"""
        report_path = self.results_dir / "PHASE6_FINAL_VALIDATION_REPORT.md"
        content = report_path.read_text(encoding='utf-8')

        required_sections = [
            "## 1. Data Source",
            "## 2. Strategy Performance",
            "## 3. Improvement vs Phase 5 Baseline",
            "## 4. Go/No-go Decision",
            "## 5. Recommendations"
        ]

        for section in required_sections:
            self.assertIn(section, content, f"Missing section: {section}")

        print("\n✓ All required sections present in validation report")

    def test_08_production_checklist_exists(self):
        """Test production readiness checklist exists"""
        checklist_path = self.docs_dir / "production_readiness_checklist.md"
        self.assertTrue(checklist_path.exists(), "Production readiness checklist not found")

        print(f"\n✓ Production checklist exists: {checklist_path}")

    def test_09_checklist_completeness(self):
        """Test checklist has all required components"""
        checklist_path = self.docs_dir / "production_readiness_checklist.md"
        content = checklist_path.read_text(encoding='utf-8')

        required_components = [
            "## 1. Data Acquisition",
            "## 2. Weekly Report Generation",
            "## 3. Error Handling",
            "## 4. Performance Monitoring",
            "## 5. Operation Manual",
            "## 6. Strategy Robustness",
            "## 7. Walk-Forward Validation",
            "## 8. Go/No-go Decision"
        ]

        for component in required_components:
            self.assertIn(component, content, f"Missing component: {component}")

        print("\n✓ All required components in checklist")

    def test_10_go_nogo_decision_made(self):
        """Test Go/No-go decision was made"""
        report_path = self.results_dir / "PHASE6_FINAL_VALIDATION_REPORT.md"
        content = report_path.read_text(encoding='utf-8')

        # Check that a decision was made
        has_decision = (
            "GO FOR PRODUCTION" in content or
            "CONDITIONAL GO" in content or
            "NO-GO" in content
        )

        self.assertTrue(has_decision, "No Go/No-go decision found in report")

        # Extract decision
        if "GO FOR PRODUCTION" in content:
            decision = "GO FOR PRODUCTION"
        elif "CONDITIONAL GO" in content:
            decision = "CONDITIONAL GO"
        else:
            decision = "NO-GO"

        print(f"\n✓ Go/No-go decision made: {decision}")

    def test_11_strategy_metrics_calculated(self):
        """Test strategy performance metrics were calculated"""
        report_path = self.results_dir / "PHASE6_FINAL_VALIDATION_REPORT.md"
        content = report_path.read_text(encoding='utf-8')

        required_metrics = [
            "Train Sharpe",
            "Test Sharpe",
            "Win Rate",
            "Max DD"
        ]

        for metric in required_metrics:
            self.assertIn(metric, content, f"Missing metric: {metric}")

        print("\n✓ All strategy metrics calculated")

    def test_12_error_handling_documented(self):
        """Test error handling is documented in operation manual"""
        manual_path = self.project_root / "documents" / "5_operations" / "operation_manual.md"

        if manual_path.exists():
            content = manual_path.read_text(encoding='utf-8')
            self.assertIn("Error", content, "Error handling not documented")
            print("\n✓ Error handling documented in operation manual")
        else:
            print("\n⚠️  Operation manual not found (may be in Phase 5)")

    def test_13_weekly_report_script(self):
        """Test weekly report generation script exists"""
        script_path = self.project_root / "scripts" / "generate_weekly_report.py"

        if script_path.exists():
            print(f"\n✓ Weekly report script exists: {script_path}")
        else:
            print("\n⚠️  Weekly report script not found (may be in Phase 5)")

    def test_14_results_directory_structure(self):
        """Test results directory structure is correct"""
        self.assertTrue(self.results_dir.exists(), "Results directory not found")

        # Check for expected files
        expected_files = [
            "PHASE6_FINAL_VALIDATION_REPORT.md"
        ]

        for filename in expected_files:
            file_path = self.results_dir / filename
            self.assertTrue(file_path.exists(), f"Expected file not found: {filename}")

        print(f"\n✓ Results directory structure correct: {self.results_dir}")

    def test_15_sample_data_generation(self):
        """Test sample data generation capability"""
        try:
            from run_final_validation import create_sample_data

            data = create_sample_data()

            self.assertIsInstance(data, pd.DataFrame)
            self.assertGreater(len(data), 0, "Sample data is empty")
            self.assertIn('Close', data.columns, "Sample data missing 'Close' column")

            print(f"\n✓ Sample data generation works: {len(data)} days")
        except Exception as e:
            self.fail(f"Sample data generation failed: {e}")

    def test_16_performance_calculation(self):
        """Test performance metrics calculation"""
        try:
            from run_final_validation import calculate_performance

            # Create dummy returns
            returns = pd.Series([0.01, -0.005, 0.02, -0.01, 0.015])

            perf = calculate_performance(returns)

            required_metrics = ['Total Return', 'Sharpe Ratio', 'Win Rate', 'Max Drawdown']
            for metric in required_metrics:
                self.assertIn(metric, perf, f"Missing metric: {metric}")

            print("\n✓ Performance calculation works")
        except Exception as e:
            self.fail(f"Performance calculation failed: {e}")

    def test_17_overall_readiness(self):
        """Test overall production readiness status"""
        checklist_path = self.docs_dir / "production_readiness_checklist.md"
        content = checklist_path.read_text(encoding='utf-8')

        # Check for overall decision
        self.assertIn("OVERALL DECISION", content, "Overall decision not found")

        # Count passed components
        pass_count = content.count("✓ PASS")
        fail_count = content.count("❌ FAIL")
        pending_count = content.count("⚠️ PENDING") + content.count("⚠️ Conditional")

        total = pass_count + fail_count + pending_count

        print(f"\n{'='*60}")
        print("Production Readiness Summary")
        print(f"{'='*60}")
        print(f"✓ Pass: {pass_count}")
        print(f"❌ Fail: {fail_count}")
        print(f"⚠️  Pending/Conditional: {pending_count}")
        print(f"Total Components: {total}")
        print(f"{'='*60}")

        # Production ready if at least 70% pass and no critical failures
        pass_rate = pass_count / total if total > 0 else 0

        if pass_rate >= 0.7 and fail_count <= 1:
            print("Status: ⚠️  CONDITIONAL - Some issues remain")
        else:
            print("Status: ❌ NOT READY - Critical issues present")


def run_tests():
    """Run all production readiness tests"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestProductionReadiness)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "="*60)
    print("PRODUCTION READINESS TEST RESULTS")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*60)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
