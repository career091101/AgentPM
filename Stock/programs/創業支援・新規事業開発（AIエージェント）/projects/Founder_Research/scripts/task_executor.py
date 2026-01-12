#!/usr/bin/env python3
"""
Task Executor for IPO_Global Batch
Executes individual case study generation tasks using Claude Code Task tool
"""

import time
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class TaskResult:
    """Result of task execution"""
    target_id: str
    wave_id: str
    status: str  # 'success', 'failed', 'timeout'
    duration_seconds: float
    sources_count: Optional[int] = None
    fact_check: Optional[str] = None
    error: Optional[str] = None


class TaskExecutor:
    """Execute individual case study generation task"""

    def __init__(self, project_root: Path, timeout: int = 900):
        self.project_root = Path(project_root)
        self.timeout = timeout  # 15 minutes default

    async def execute_task(
        self,
        target: Dict[str, Any],
        wave_id: str,
        prompt: str
    ) -> TaskResult:
        """
        Execute a single case study generation task

        Args:
            target: Target dictionary with id, company, founder
            wave_id: Wave identifier
            prompt: Complete prompt for generation

        Returns:
            TaskResult with execution details
        """
        target_id = target['id']
        company = target['company']

        start_time = time.time()

        try:
            # Here we would use Claude Code's Task tool
            # Since the exact API is not documented, we use a placeholder
            # In actual implementation, this would be replaced with:
            # from claude_code import Task
            # task = Task.create(prompt=prompt, timeout=self.timeout)
            # result = await task.execute()

            # For now, we'll use the existing subprocess approach as fallback
            # This can be replaced once Task tool API is confirmed
            import subprocess

            result = subprocess.run(
                ['claude', 'code', '-p', prompt],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=self.project_root
            )

            duration = time.time() - start_time

            if result.returncode == 0:
                # Success - validate the output
                validation_result = self._validate_output(target_id)

                return TaskResult(
                    target_id=target_id,
                    wave_id=wave_id,
                    status='success',
                    duration_seconds=duration,
                    sources_count=validation_result.get('sources_count'),
                    fact_check=validation_result.get('fact_check')
                )
            else:
                # Failed
                return TaskResult(
                    target_id=target_id,
                    wave_id=wave_id,
                    status='failed',
                    duration_seconds=duration,
                    error=result.stderr[:500] if result.stderr else "Unknown error"
                )

        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            return TaskResult(
                target_id=target_id,
                wave_id=wave_id,
                status='timeout',
                duration_seconds=duration,
                error=f"Timeout after {self.timeout} seconds"
            )

        except Exception as e:
            duration = time.time() - start_time
            return TaskResult(
                target_id=target_id,
                wave_id=wave_id,
                status='failed',
                duration_seconds=duration,
                error=str(e)[:500]
            )

    def _validate_output(self, target_id: str) -> Dict[str, Any]:
        """
        Quick validation of generated output

        Args:
            target_id: Target identifier

        Returns:
            Dict with sources_count and fact_check
        """
        output_dir = self.project_root / "documents" / "05_IPO_Global"

        # Find generated file
        files = list(output_dir.glob(f"{target_id}_*.md"))

        if not files:
            return {'sources_count': 0, 'fact_check': 'fail'}

        file_path = files[0]

        try:
            content = file_path.read_text(encoding='utf-8')

            # Count sources
            sources_count = content.count('primary_sources:')
            sources_count += content.count('- "http')
            sources_count = min(sources_count, 20)  # Cap at 20

            # Check fact_check field
            fact_check = 'pass' if 'fact_check: "pass"' in content else 'fail'

            return {
                'sources_count': sources_count,
                'fact_check': fact_check
            }

        except Exception:
            return {'sources_count': 0, 'fact_check': 'fail'}


if __name__ == '__main__':
    import asyncio

    async def test():
        project_root = Path(__file__).parent.parent
        executor = TaskExecutor(project_root, timeout=60)

        test_target = {
            'id': 'FOUNDER_357',
            'company': 'Snowflake',
            'founder': 'Frank Slootman'
        }

        test_prompt = "Test prompt for FOUNDER_357"

        print("Testing TaskExecutor...")
        print(f"Executing task for {test_target['id']}...")

        result = await executor.execute_task(test_target, 'ipo_wave1', test_prompt)

        print(f"\nResult:")
        print(f"  Status: {result.status}")
        print(f"  Duration: {result.duration_seconds:.2f}s")
        print(f"  Sources: {result.sources_count}")
        print(f"  Fact Check: {result.fact_check}")
        if result.error:
            print(f"  Error: {result.error}")

    # asyncio.run(test())
    print("TaskExecutor module loaded successfully")
