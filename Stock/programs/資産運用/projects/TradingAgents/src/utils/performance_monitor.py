"""
パフォーマンスモニタリングモジュール

実行時間、メモリ使用量、API呼び出し回数などを監視。
"""

import time
import psutil
from pathlib import Path
from datetime import datetime


class PerformanceMonitor:
    """
    システムパフォーマンスモニター

    Usage:
        monitor = PerformanceMonitor()
        monitor.start()

        # ... your code ...

        monitor.stop()
        print(monitor.get_report())
        monitor.save_log('logs/performance.log')
    """

    def __init__(self):
        self.start_time = None
        self.metrics = {}

    def start(self):
        """Start monitoring"""
        self.start_time = time.time()
        self.metrics['start_time'] = datetime.now().isoformat()
        self.metrics['start_memory_mb'] = self._get_memory_usage()

    def stop(self):
        """Stop monitoring and calculate metrics"""
        if self.start_time is None:
            raise ValueError("Monitor not started")

        elapsed_time = time.time() - self.start_time
        self.metrics['elapsed_time_sec'] = elapsed_time
        self.metrics['end_memory_mb'] = self._get_memory_usage()
        self.metrics['memory_delta_mb'] = (
            self.metrics['end_memory_mb'] - self.metrics['start_memory_mb']
        )

    def _get_memory_usage(self):
        """Get current memory usage in MB"""
        process = psutil.Process()
        return process.memory_info().rss / 1024 / 1024

    def get_report(self):
        """Get performance report"""
        return self.metrics

    def save_log(self, log_path: str):
        """Save performance log"""
        log_file = Path(log_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file, 'a') as f:
            f.write(f"\n--- {self.metrics.get('start_time', 'N/A')} ---\n")
            for key, value in self.metrics.items():
                f.write(f"{key}: {value}\n")


# Example usage
if __name__ == "__main__":
    print("Performance Monitor - Test Run")
    print("=" * 60)

    monitor = PerformanceMonitor()
    monitor.start()

    # Simulate some work
    import numpy as np
    data = np.random.randn(1000000)
    result = data.sum()

    time.sleep(1)

    monitor.stop()

    report = monitor.get_report()
    print("\nPerformance Report:")
    print(f"  Start Time: {report['start_time']}")
    print(f"  Elapsed Time: {report['elapsed_time_sec']:.2f} sec")
    print(f"  Start Memory: {report['start_memory_mb']:.2f} MB")
    print(f"  End Memory: {report['end_memory_mb']:.2f} MB")
    print(f"  Memory Delta: {report['memory_delta_mb']:.2f} MB")

    # Save log
    monitor.save_log("logs/test_performance.log")
    print("\n✅ Log saved to logs/test_performance.log")
