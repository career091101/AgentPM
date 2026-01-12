#!/usr/bin/env python3
"""
Progress Tracker for IPO_Global Batch Execution
Thread-safe progress tracking with atomic file updates
"""

import json
import fcntl
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Callable, Optional
from contextlib import contextmanager


class ProgressTracker:
    """Thread-safe progress tracking for parallel batch execution"""

    def __init__(self, progress_file: Path):
        self.progress_file = Path(progress_file)
        self.lock_file = self.progress_file.with_suffix('.lock')

        # Initialize if doesn't exist
        if not self.progress_file.exists():
            self._initialize_progress()

    def _initialize_progress(self):
        """Initialize progress file with default structure"""
        initial_data = {
            "batch_id": f"ipo_global_batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "started_at": datetime.now().isoformat(),
            "total_targets": 25,
            "completed": [],
            "failed": [],
            "in_progress": [],
            "waves": {},
            "real_time_stats": {
                "tasks_running": 0,
                "tasks_completed": 0,
                "tasks_failed": 0,
                "avg_duration_seconds": 0,
                "avg_sources_count": 0,
                "fact_check_pass_rate": 0
            },
            "retry_queue": [],
            "completed_at": None
        }

        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=2, ensure_ascii=False)

    @contextmanager
    def _atomic_update(self):
        """
        Context manager for atomic file updates with exclusive locking

        Usage:
            with tracker._atomic_update() as data:
                data['completed'].append(target_id)
                # data is automatically saved on exit
        """
        # Ensure lock file exists
        self.lock_file.parent.mkdir(parents=True, exist_ok=True)
        lock_fd = open(self.lock_file, 'w')

        try:
            # Acquire exclusive lock
            fcntl.flock(lock_fd.fileno(), fcntl.LOCK_EX)

            # Read current data
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Yield data for modification
            yield data

            # Write updated data atomically
            temp_file = self.progress_file.with_suffix('.tmp')
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # Atomic rename
            temp_file.replace(self.progress_file)

        finally:
            # Release lock
            fcntl.flock(lock_fd.fileno(), fcntl.LOCK_UN)
            lock_fd.close()

    def mark_in_progress(self, target_id: str, wave_id: str):
        """Mark a target as in progress"""
        with self._atomic_update() as data:
            if target_id not in data['in_progress']:
                data['in_progress'].append(target_id)

            # Initialize wave if needed
            if wave_id not in data['waves']:
                data['waves'][wave_id] = {
                    'total': 0,
                    'completed': 0,
                    'failed': 0,
                    'in_progress': 0,
                    'targets': {}
                }

            # Initialize target
            data['waves'][wave_id]['targets'][target_id] = {
                'status': 'in_progress',
                'started_at': datetime.now().isoformat(),
                'completed_at': None,
                'duration_seconds': None,
                'attempts': 1,
                'sources_count': None,
                'fact_check': None,
                'error': None
            }

            data['waves'][wave_id]['in_progress'] += 1
            data['real_time_stats']['tasks_running'] += 1

    def mark_completed(
        self,
        target_id: str,
        wave_id: str,
        duration_seconds: float,
        sources_count: int = None,
        fact_check: str = None
    ):
        """Mark a target as completed"""
        with self._atomic_update() as data:
            # Remove from in_progress
            if target_id in data['in_progress']:
                data['in_progress'].remove(target_id)

            # Add to completed
            if target_id not in data['completed']:
                data['completed'].append(target_id)

            # Update wave
            if wave_id in data['waves']:
                data['waves'][wave_id]['in_progress'] -= 1
                data['waves'][wave_id]['completed'] += 1

                # Update target details
                if target_id in data['waves'][wave_id]['targets']:
                    target_data = data['waves'][wave_id]['targets'][target_id]
                    target_data['status'] = 'completed'
                    target_data['completed_at'] = datetime.now().isoformat()
                    target_data['duration_seconds'] = duration_seconds
                    target_data['sources_count'] = sources_count
                    target_data['fact_check'] = fact_check

            # Update stats
            data['real_time_stats']['tasks_running'] -= 1
            data['real_time_stats']['tasks_completed'] += 1

            # Update averages
            self._update_averages(data)

    def mark_failed(
        self,
        target_id: str,
        wave_id: str,
        error: str,
        duration_seconds: float = None
    ):
        """Mark a target as failed"""
        with self._atomic_update() as data:
            # Remove from in_progress
            if target_id in data['in_progress']:
                data['in_progress'].remove(target_id)

            # Add to failed
            failed_entry = {
                'target_id': target_id,
                'wave_id': wave_id,
                'error': error,
                'timestamp': datetime.now().isoformat(),
                'duration_seconds': duration_seconds
            }

            if failed_entry not in data['failed']:
                data['failed'].append(failed_entry)

            # Update wave
            if wave_id in data['waves']:
                data['waves'][wave_id]['in_progress'] -= 1
                data['waves'][wave_id]['failed'] += 1

                # Update target details
                if target_id in data['waves'][wave_id]['targets']:
                    target_data = data['waves'][wave_id]['targets'][target_id]
                    target_data['status'] = 'failed'
                    target_data['completed_at'] = datetime.now().isoformat()
                    target_data['duration_seconds'] = duration_seconds
                    target_data['error'] = error

            # Update stats
            data['real_time_stats']['tasks_running'] -= 1
            data['real_time_stats']['tasks_failed'] += 1

    def add_to_retry_queue(self, target_id: str, wave_id: str, error: str):
        """Add a failed target to retry queue"""
        with self._atomic_update() as data:
            retry_entry = {
                'target_id': target_id,
                'wave_id': wave_id,
                'error': error,
                'added_at': datetime.now().isoformat(),
                'attempts': self._get_attempts(data, target_id, wave_id)
            }

            data['retry_queue'].append(retry_entry)

    def get_retry_queue(self) -> list:
        """Get current retry queue"""
        with open(self.progress_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('retry_queue', [])

    def clear_retry_queue(self):
        """Clear retry queue after processing"""
        with self._atomic_update() as data:
            data['retry_queue'] = []

    def _get_attempts(self, data: Dict, target_id: str, wave_id: str) -> int:
        """Get number of attempts for a target"""
        if wave_id in data['waves']:
            if target_id in data['waves'][wave_id]['targets']:
                return data['waves'][wave_id]['targets'][target_id].get('attempts', 0)
        return 0

    def increment_attempts(self, target_id: str, wave_id: str):
        """Increment attempt counter for a target"""
        with self._atomic_update() as data:
            if wave_id in data['waves']:
                if target_id in data['waves'][wave_id]['targets']:
                    current = data['waves'][wave_id]['targets'][target_id].get('attempts', 0)
                    data['waves'][wave_id]['targets'][target_id]['attempts'] = current + 1

    def _update_averages(self, data: Dict):
        """Update average statistics"""
        completed_targets = []
        total_duration = 0
        total_sources = 0
        fact_check_pass = 0

        for wave_id, wave_data in data['waves'].items():
            for target_id, target_data in wave_data['targets'].items():
                if target_data['status'] == 'completed':
                    completed_targets.append(target_data)

                    if target_data.get('duration_seconds'):
                        total_duration += target_data['duration_seconds']

                    if target_data.get('sources_count'):
                        total_sources += target_data['sources_count']

                    if target_data.get('fact_check') == 'pass':
                        fact_check_pass += 1

        count = len(completed_targets)
        if count > 0:
            data['real_time_stats']['avg_duration_seconds'] = round(total_duration / count, 1)
            data['real_time_stats']['avg_sources_count'] = round(total_sources / count, 1)
            data['real_time_stats']['fact_check_pass_rate'] = round((fact_check_pass / count) * 100, 1)

    def get_progress(self) -> Dict[str, Any]:
        """Get current progress data"""
        with open(self.progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_wave_progress(self, wave_id: str) -> Optional[Dict[str, Any]]:
        """Get progress for specific wave"""
        data = self.get_progress()
        return data['waves'].get(wave_id)

    def is_completed(self, target_id: str) -> bool:
        """Check if target is completed"""
        data = self.get_progress()
        return target_id in data['completed']

    def is_in_progress(self, target_id: str) -> bool:
        """Check if target is in progress"""
        data = self.get_progress()
        return target_id in data['in_progress']

    def get_completion_percentage(self) -> float:
        """Get overall completion percentage"""
        data = self.get_progress()
        total = data['total_targets']
        completed = len(data['completed'])
        return round((completed / total) * 100, 1) if total > 0 else 0

    def print_status(self):
        """Print current status"""
        data = self.get_progress()

        print("\n" + "=" * 80)
        print("IPO_Global Batch Execution Status")
        print("=" * 80)
        print(f"Batch ID: {data['batch_id']}")
        print(f"Started: {data['started_at']}")
        print()
        print(f"Overall Progress: {len(data['completed'])}/{data['total_targets']} ({self.get_completion_percentage()}%)")
        print(f"  - Completed: {len(data['completed'])}")
        print(f"  - Failed: {len(data['failed'])}")
        print(f"  - In Progress: {len(data['in_progress'])}")
        print(f"  - Retry Queue: {len(data['retry_queue'])}")
        print()

        stats = data['real_time_stats']
        print("Real-Time Statistics:")
        print(f"  - Tasks Running: {stats['tasks_running']}")
        print(f"  - Avg Duration: {stats['avg_duration_seconds']}s")
        print(f"  - Avg Sources: {stats['avg_sources_count']}")
        print(f"  - Fact Check Pass: {stats['fact_check_pass_rate']}%")
        print()

        print("Wave Progress:")
        for wave_id, wave_data in data['waves'].items():
            total = wave_data.get('total', 5)
            completed = wave_data['completed']
            pct = round((completed / total) * 100, 1) if total > 0 else 0
            print(f"  {wave_id}: {completed}/{total} ({pct}%) [in_progress: {wave_data['in_progress']}, failed: {wave_data['failed']}]")

        print("=" * 80 + "\n")

    def mark_batch_completed(self):
        """Mark entire batch as completed"""
        with self._atomic_update() as data:
            data['completed_at'] = datetime.now().isoformat()


if __name__ == '__main__':
    # Test progress tracker
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        progress_file = Path(tmpdir) / "test_progress.json"
        tracker = ProgressTracker(progress_file)

        print("Testing Progress Tracker...")

        # Test mark in progress
        tracker.mark_in_progress("FOUNDER_357", "ipo_wave1")
        tracker.print_status()

        # Test mark completed
        time.sleep(1)
        tracker.mark_completed("FOUNDER_357", "ipo_wave1", 10.5, sources_count=15, fact_check="pass")
        tracker.print_status()

        # Test mark failed
        tracker.mark_in_progress("FOUNDER_358", "ipo_wave1")
        tracker.mark_failed("FOUNDER_358", "ipo_wave1", "Timeout error", duration_seconds=5.0)
        tracker.print_status()

        # Test retry queue
        tracker.add_to_retry_queue("FOUNDER_358", "ipo_wave1", "Timeout error")
        tracker.print_status()

        print(f"Completion: {tracker.get_completion_percentage()}%")
        print("\nTest completed successfully!")
