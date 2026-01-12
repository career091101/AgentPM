"""
パフォーマンスモニターのテスト

Usage:
    python3 -m pytest src/tests/test_performance_monitor.py -v
"""

import sys
from pathlib import Path
import time
import numpy as np

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.utils.performance_monitor import PerformanceMonitor


def test_monitor_start_stop():
    """Test monitor start and stop"""
    monitor = PerformanceMonitor()
    monitor.start()

    # Simulate work
    time.sleep(0.1)

    monitor.stop()

    report = monitor.get_report()

    assert 'start_time' in report
    assert 'elapsed_time_sec' in report
    assert 'start_memory_mb' in report
    assert 'end_memory_mb' in report
    assert report['elapsed_time_sec'] >= 0.1

    print(f"✅ Monitor start/stop test passed")
    print(f"   Elapsed time: {report['elapsed_time_sec']:.2f} sec")


def test_memory_tracking():
    """Test memory usage tracking"""
    monitor = PerformanceMonitor()
    monitor.start()

    # Allocate some memory
    large_array = np.random.randn(1000000)

    monitor.stop()

    report = monitor.get_report()

    assert 'memory_delta_mb' in report
    assert report['memory_delta_mb'] >= 0  # Memory should increase or stay same

    print(f"✅ Memory tracking test passed")
    print(f"   Memory delta: {report['memory_delta_mb']:.2f} MB")


def test_log_save():
    """Test log file saving"""
    monitor = PerformanceMonitor()
    monitor.start()

    time.sleep(0.05)

    monitor.stop()

    log_path = "logs/test_performance_monitor.log"
    monitor.save_log(log_path)

    log_file = Path(log_path)
    assert log_file.exists()

    print(f"✅ Log save test passed")
    print(f"   Log file: {log_path}")


if __name__ == "__main__":
    print("Running Performance Monitor Tests")
    print("=" * 60)

    try:
        test_monitor_start_stop()
        test_memory_tracking()
        test_log_save()

        print("\n" + "=" * 60)
        print("✅ All tests passed")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
