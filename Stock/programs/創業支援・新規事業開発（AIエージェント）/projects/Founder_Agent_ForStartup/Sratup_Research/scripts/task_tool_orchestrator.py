#!/usr/bin/env python3
"""
Task Tool Orchestrator for IPO_Global Batch Generation
Main controller for parallel batch execution with wave overlap strategy
"""

import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

from prompt_generator import PromptGenerator
from progress_tracker import ProgressTracker
from task_executor import TaskExecutor, TaskResult
from retry_handler import RetryHandler, RetryPolicy
from validation import DocumentValidator


class TaskToolOrchestrator:
    """Main orchestrator for IPO_Global batch generation"""

    def __init__(
        self,
        wave_definitions_path: Path,
        project_root: Path,
        max_parallel: int = 20
    ):
        self.wave_definitions_path = Path(wave_definitions_path)
        self.project_root = Path(project_root)
        self.max_parallel = max_parallel

        # Load wave definitions
        with open(self.wave_definitions_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            self.waves = config['waves']
            self.execution_strategy = config.get('execution_strategy', {})

        # Initialize components
        self.progress_file = self.project_root / "scripts" / "progress_ipo_global.json"
        self.progress_tracker = ProgressTracker(self.progress_file)
        self.prompt_generator = PromptGenerator(self.project_root)
        self.task_executor = TaskExecutor(
            self.project_root,
            timeout=self.execution_strategy.get('timeout_per_task', 900)
        )
        self.retry_handler = RetryHandler(
            RetryPolicy(max_retries=self.execution_strategy.get('max_retries', 2))
        )
        self.validator = DocumentValidator(self.project_root)

    def can_start_wave(self, wave: Dict, active_tasks: List) -> bool:
        """
        Check if a new wave can be started based on overlap strategy

        Args:
            wave: Wave configuration
            active_tasks: List of currently active tasks

        Returns:
            True if wave can start
        """
        # Get wave progress
        wave_progress = self.progress_tracker.get_wave_progress(wave['id'])

        if not wave_progress:
            # Wave not started yet, can start
            return len(active_tasks) < self.max_parallel

        # Check if 60% of wave is completed
        total = wave['count']
        completed = wave_progress['completed']
        completion_pct = (completed / total) * 100 if total > 0 else 0

        overlap_trigger = self.execution_strategy.get('overlap_trigger_percent', 60)

        return completion_pct >= overlap_trigger

    async def execute_wave_with_overlap(
        self,
        waves: List[Dict],
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        Execute all waves with overlap strategy

        Args:
            waves: List of wave configurations
            dry_run: If True, only print what would be done

        Returns:
            Execution results
        """
        print("\n" + "=" * 80)
        print("IPO_Global Batch Execution with Wave Overlap")
        print("=" * 80)
        print(f"Total Waves: {len(waves)}")
        print(f"Total Targets: {sum(w['count'] for w in waves)}")
        print(f"Max Parallel: {self.max_parallel}")
        print(f"Dry Run: {dry_run}")
        print("=" * 80 + "\n")

        if dry_run:
            print("Dry Run - Waves to Execute:")
            for wave in waves:
                print(f"\n{wave['id']}: {wave['name']}")
                for target in wave['targets']:
                    print(f"  - {target['id']}: {target['company']} ({target['founder']})")
            return {'dry_run': True}

        # Initialize wave totals in progress tracker
        for wave in waves:
            progress = self.progress_tracker.get_wave_progress(wave['id'])
            if not progress:
                # Initialize wave
                with self.progress_tracker._atomic_update() as data:
                    data['waves'][wave['id']] = {
                        'total': wave['count'],
                        'completed': 0,
                        'failed': 0,
                        'in_progress': 0,
                        'targets': {}
                    }

        # Execute waves with overlap
        active_tasks = {}  # task_id -> asyncio.Task
        wave_idx = 0
        results = []

        while wave_idx < len(waves) or active_tasks:
            # Start new wave if possible
            if wave_idx < len(waves):
                wave = waves[wave_idx]

                if self.can_start_wave(wave, list(active_tasks.values())):
                    # Get pending targets for this wave
                    pending_targets = self._get_pending_targets(wave)

                    if pending_targets:
                        print(f"\n🚀 Starting {wave['id']}: {wave['name']} ({len(pending_targets)} targets)")

                        # Create tasks for this wave
                        for target in pending_targets:
                            if len(active_tasks) < self.max_parallel:
                                task_id = target['id']
                                task = asyncio.create_task(
                                    self._execute_single_task(target, wave['id'])
                                )
                                active_tasks[task_id] = task

                        wave_idx += 1

            # Wait for any task to complete
            if active_tasks:
                done, pending = await asyncio.wait(
                    active_tasks.values(),
                    return_when=asyncio.FIRST_COMPLETED
                )

                # Process completed tasks
                for task in done:
                    result = await task
                    results.append(result)

                    # Remove from active tasks
                    for task_id, t in list(active_tasks.items()):
                        if t == task:
                            del active_tasks[task_id]
                            break

                    # Print progress
                    self._print_progress(result)

            await asyncio.sleep(0.1)  # Small delay to prevent busy loop

        print("\n" + "=" * 80)
        print("Batch Execution Complete")
        print("=" * 80)
        self.progress_tracker.print_status()

        # Handle retries
        if self.execution_strategy.get('retry_failed', True):
            await self._handle_retries()

        return {'results': results}

    async def _execute_single_task(
        self,
        target: Dict,
        wave_id: str
    ) -> TaskResult:
        """Execute a single task"""
        target_id = target['id']

        # Mark as in progress
        self.progress_tracker.mark_in_progress(target_id, wave_id)

        # Generate prompt
        prompt = self.prompt_generator.generate_ipo_prompt(target)

        # Execute
        result = await self.task_executor.execute_task(target, wave_id, prompt)

        # Update progress
        if result.status == 'success':
            self.progress_tracker.mark_completed(
                target_id,
                wave_id,
                result.duration_seconds,
                result.sources_count,
                result.fact_check
            )
        else:
            self.progress_tracker.mark_failed(
                target_id,
                wave_id,
                result.error,
                result.duration_seconds
            )

            # Add to retry queue if eligible
            if self.retry_handler.should_retry(target_id, result.error, 1):
                self.progress_tracker.add_to_retry_queue(target_id, wave_id, result.error)

        return result

    def _get_pending_targets(self, wave: Dict) -> List[Dict]:
        """Get pending targets for a wave"""
        pending = []
        for target in wave['targets']:
            target_id = target['id']
            if not self.progress_tracker.is_completed(target_id) and \
               not self.progress_tracker.is_in_progress(target_id):
                pending.append(target)
        return pending

    def _print_progress(self, result: TaskResult):
        """Print progress for a completed task"""
        emoji = "✅" if result.status == 'success' else "❌"
        msg = f"{emoji} {result.target_id} - {result.status} ({result.duration_seconds:.1f}s)"

        if result.status == 'success':
            msg += f" [sources: {result.sources_count}, fact_check: {result.fact_check}]"
        elif result.error:
            msg += f" [{result.error[:50]}...]"

        completion_pct = self.progress_tracker.get_completion_percentage()
        msg += f" [{completion_pct}% complete]"

        print(msg)

    async def _handle_retries(self):
        """Handle retry queue"""
        retry_queue = self.progress_tracker.get_retry_queue()

        if not retry_queue:
            print("\nNo tasks to retry.")
            return

        print(f"\n{'='*80}")
        print(f"Processing Retry Queue ({len(retry_queue)} tasks)")
        print(f"{'='*80}\n")

        retry_tasks = []
        for retry_item in retry_queue:
            target_id = retry_item['target_id']
            wave_id = retry_item['wave_id']

            # Find target
            target = self._find_target(target_id)
            if target:
                # Increment attempts
                self.progress_tracker.increment_attempts(target_id, wave_id)

                # Execute with extended timeout
                task = asyncio.create_task(
                    self._execute_single_task(target, wave_id)
                )
                retry_tasks.append(task)

        # Wait for all retries
        if retry_tasks:
            results = await asyncio.gather(*retry_tasks)
            print(f"\n✓ Retry completed: {len(results)} tasks processed")

        # Clear retry queue
        self.progress_tracker.clear_retry_queue()

    def _find_target(self, target_id: str) -> Dict:
        """Find target by ID"""
        for wave in self.waves:
            for target in wave['targets']:
                if target['id'] == target_id:
                    return target
        return None

    async def execute_wave(self, wave_id: str, dry_run: bool = False):
        """Execute a single wave"""
        wave = next((w for w in self.waves if w['id'] == wave_id), None)

        if not wave:
            print(f"Error: Wave {wave_id} not found")
            return

        return await self.execute_wave_with_overlap([wave], dry_run)

    async def execute_all(self, dry_run: bool = False):
        """Execute all waves"""
        return await self.execute_wave_with_overlap(self.waves, dry_run)


async def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Task Tool Orchestrator for IPO_Global')
    parser.add_argument('--wave', type=str, help='Execute specific wave (e.g., ipo_wave1)')
    parser.add_argument('--max-parallel', type=int, default=20, help='Max parallel tasks')
    parser.add_argument('--dry-run', action='store_true', help='Dry run mode')
    parser.add_argument('--status', action='store_true', help='Show status only')
    parser.add_argument('--validate', action='store_true', help='Validate documents only')

    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent
    wave_definitions = script_dir / 'wave_definitions_ipo_global.json'
    project_root = script_dir.parent

    # Create orchestrator
    orchestrator = TaskToolOrchestrator(
        wave_definitions_path=wave_definitions,
        project_root=project_root,
        max_parallel=args.max_parallel
    )

    if args.status:
        # Show status
        orchestrator.progress_tracker.print_status()

    elif args.validate:
        # Validate documents
        print("Validating all documents...")
        results = orchestrator.validator.validate_all()
        orchestrator.validator.print_validation_report(results)

    elif args.wave:
        # Execute specific wave
        await orchestrator.execute_wave(args.wave, dry_run=args.dry_run)

    else:
        # Execute all waves
        await orchestrator.execute_all(dry_run=args.dry_run)

        # Final validation
        if not args.dry_run:
            print("\n" + "="*80)
            print("Running Final Validation...")
            print("="*80 + "\n")
            results = orchestrator.validator.validate_all()
            orchestrator.validator.print_validation_report(results)

            # Mark batch as completed
            orchestrator.progress_tracker.mark_batch_completed()


if __name__ == '__main__':
    asyncio.run(main())
