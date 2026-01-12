#!/usr/bin/env python3
"""
Retry Handler for IPO_Global Batch
Manages retry logic for failed tasks
"""

from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class RetryPolicy:
    """Retry policy configuration"""
    max_retries: int = 2
    timeout_multiplier: float = 2.0  # 2x timeout for retries
    retryable_errors: List[str] = None

    def __post_init__(self):
        if self.retryable_errors is None:
            self.retryable_errors = [
                'timeout',
                'fact_check',
                'insufficient_sources',
                'network',
                'connection',
                'temporary'
            ]


class RetryHandler:
    """Handle retry logic for failed tasks"""

    def __init__(self, policy: RetryPolicy = None):
        self.policy = policy or RetryPolicy()

    def should_retry(self, target_id: str, error: str, attempts: int) -> bool:
        """
        Determine if a failed task should be retried

        Args:
            target_id: Target identifier
            error: Error message
            attempts: Number of attempts so far

        Returns:
            True if should retry, False otherwise
        """
        # Check attempt limit
        if attempts >= self.policy.max_retries:
            return False

        # Check if error is retryable
        error_lower = error.lower()
        for retryable in self.policy.retryable_errors:
            if retryable in error_lower:
                return True

        return False

    def get_retry_timeout(self, original_timeout: int) -> int:
        """
        Get timeout for retry attempt

        Args:
            original_timeout: Original timeout in seconds

        Returns:
            Extended timeout for retry
        """
        return int(original_timeout * self.policy.timeout_multiplier)

    def classify_error(self, error: str) -> str:
        """
        Classify error type

        Args:
            error: Error message

        Returns:
            Error category
        """
        error_lower = error.lower()

        if 'timeout' in error_lower:
            return 'timeout'
        elif 'fact' in error_lower or 'check' in error_lower:
            return 'fact_check'
        elif 'source' in error_lower:
            return 'insufficient_sources'
        elif 'network' in error_lower or 'connection' in error_lower:
            return 'network'
        else:
            return 'other'

    def prepare_retry_batch(
        self,
        failed_tasks: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Prepare batch of tasks for retry

        Args:
            failed_tasks: List of failed task dictionaries

        Returns:
            List of tasks eligible for retry
        """
        retry_batch = []

        for task in failed_tasks:
            target_id = task.get('target_id')
            error = task.get('error', '')
            attempts = task.get('attempts', 1)

            if self.should_retry(target_id, error, attempts):
                retry_task = task.copy()
                retry_task['is_retry'] = True
                retry_task['retry_number'] = attempts
                retry_task['error_type'] = self.classify_error(error)
                retry_batch.append(retry_task)

        return retry_batch

    def get_retry_stats(self, failed_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Get statistics about retry eligibility

        Args:
            failed_tasks: List of failed tasks

        Returns:
            Statistics dictionary
        """
        total_failed = len(failed_tasks)
        retryable = len(self.prepare_retry_batch(failed_tasks))
        permanent_failures = total_failed - retryable

        error_types = {}
        for task in failed_tasks:
            error = task.get('error', '')
            error_type = self.classify_error(error)
            error_types[error_type] = error_types.get(error_type, 0) + 1

        return {
            'total_failed': total_failed,
            'retryable': retryable,
            'permanent_failures': permanent_failures,
            'retry_rate': round((retryable / total_failed) * 100, 1) if total_failed > 0 else 0,
            'error_types': error_types
        }


if __name__ == '__main__':
    # Test retry handler
    policy = RetryPolicy(max_retries=2)
    handler = RetryHandler(policy)

    # Test should_retry
    print("Testing RetryHandler...")
    print()

    test_cases = [
        ("FOUNDER_357", "Timeout after 900 seconds", 1, True),
        ("FOUNDER_358", "Timeout after 900 seconds", 2, False),  # Max retries
        ("FOUNDER_359", "Fact check failed", 1, True),
        ("FOUNDER_360", "Unknown fatal error", 1, False),  # Not retryable
        ("FOUNDER_361", "Network connection error", 1, True),
    ]

    for target_id, error, attempts, expected in test_cases:
        result = handler.should_retry(target_id, error, attempts)
        status = "✓" if result == expected else "✗"
        print(f"{status} {target_id}: {error[:30]}... (attempt {attempts}) -> {'RETRY' if result else 'SKIP'}")

    print()
    print("Retry timeout test:")
    original = 900
    retry_timeout = handler.get_retry_timeout(original)
    print(f"  Original: {original}s -> Retry: {retry_timeout}s")

    print()
    print("Error classification test:")
    errors = [
        "Timeout after 900 seconds",
        "Fact check validation failed",
        "Insufficient sources (only 8 found)",
        "Network connection refused",
        "Unknown error"
    ]
    for error in errors:
        error_type = handler.classify_error(error)
        print(f"  '{error[:40]}...' -> {error_type}")

    print("\nTest completed successfully!")
