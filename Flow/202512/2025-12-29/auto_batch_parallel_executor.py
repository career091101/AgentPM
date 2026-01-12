#!/usr/bin/env python3
"""
完全自動化並列バッチ実行システム
- Claude Code (Task tool) を「複数エージェント」として並列起動
- エージェントはバッチ（まとまり）単位で処理し、同時起動は最大N（デフォルト5）
- Human介入不要（input待ちなし / 確認質問なし）
- 生成物は各タスクの指示（タスクリスト内の「実行方法」）に従って保存

作成日: 2025-12-29
更新日: 2025-12-29
"""

import subprocess
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import threading

class AutoBatchParallelExecutor:
    """完全自動化並列バッチ実行マネージャー"""

    def __init__(
        self,
        max_concurrent_agents: int = 5,
        timeout_seconds_per_agent: int = 8 * 60 * 60,
        claude_cmd: str = "claude",
    ):
        """
        初期化

        Args:
            max_concurrent_agents: 同時実行する最大エージェント数
            timeout_seconds_per_agent: 1エージェント（1バッチ）あたりのタイムアウト秒
            claude_cmd: Claude Code CLIのコマンド名（通常は "claude"）
        """
        self.max_concurrent_agents = max_concurrent_agents
        self.timeout_seconds_per_agent = timeout_seconds_per_agent
        self.claude_cmd = claude_cmd

        self.flow_dir = Path(__file__).resolve().parent
        self.base_dir = self.flow_dir.parent.parent.parent  # .../aipm_v0
        self.log_dir = self.flow_dir / "logs"
        self.log_dir.mkdir(exist_ok=True)

        # 進捗管理
        self.agent_status = {}
        self.lock = threading.Lock()

    @dataclass(frozen=True)
    class AgentJob:
        agent_id: int
        task_file: str
        prompt: str
        log_file: Path

    def _build_agent_prompt(self, task_file: str) -> str:
        """
        1エージェント（=1 Claude Codeプロセス）に渡すプロンプトを生成。

        重要: ここでいう「エージェント」は Claude Code の1プロセスを指し、
        Claude Code 側で Task tool を使って並列処理する想定。
        """
        return (
            f"@Flow/202512/2025-12-29/{task_file} を読み込んで、"
            "このタスクリストの全件を『並列バッチ（Task tool）』で実行してください。\n\n"
            "要件:\n"
            "- Humanへの質問・確認は一切しない（完全自動）\n"
            "- 失敗は最大3回まで自動リトライ\n"
            "- タスクリスト内の『実行方法』『品質基準』『準拠事項』に厳密に従う\n"
            "- 各成果物は所定のパス/テンプレートに保存\n"
        )

    def build_jobs_from_task_files(self, task_files: List[str]) -> List["AutoBatchParallelExecutor.AgentJob"]:
        jobs: List[AutoBatchParallelExecutor.AgentJob] = []
        for i, task_file in enumerate(task_files, start=1):
            task_path = self.flow_dir / task_file
            if not task_path.exists():
                raise FileNotFoundError(f"Task file not found: {task_path}")

            agent_name = f"Agent-{i}"
            log_file = self.log_dir / f"{agent_name}_{task_path.stem}.log"
            jobs.append(
                AutoBatchParallelExecutor.AgentJob(
                    agent_id=i,
                    task_file=task_file,
                    prompt=self._build_agent_prompt(task_file),
                    log_file=log_file,
                )
            )
        return jobs

    def execute_agent_job(self, job: "AutoBatchParallelExecutor.AgentJob") -> Dict[str, object]:
        agent_name = f"Agent-{job.agent_id}"
        started_at = datetime.now()

        with self.lock:
            self.agent_status[agent_name] = {
                "status": "starting",
                "task_file": job.task_file,
                "start_time": started_at,
            }

        print(f"🚀 {agent_name} 起動: {job.task_file}")

        try:
            with self.lock:
                self.agent_status[agent_name]["status"] = "running"

            result = subprocess.run(
                [self.claude_cmd, "code", "-p", job.prompt],
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds_per_agent,
                cwd=self.base_dir,
            )

            finished_at = datetime.now()
            duration_seconds = (finished_at - started_at).total_seconds()

            job.log_file.write_text(
                (
                    f"=== {agent_name} 実行ログ ===\n"
                    f"task_file: {job.task_file}\n"
                    f"started_at: {started_at}\n"
                    f"finished_at: {finished_at}\n"
                    f"duration_seconds: {duration_seconds:.1f}\n"
                    f"returncode: {result.returncode}\n\n"
                    "----- STDOUT -----\n"
                    f"{result.stdout}\n\n"
                    "----- STDERR -----\n"
                    f"{result.stderr}\n"
                ),
                encoding="utf-8",
            )

            status = "completed" if result.returncode == 0 else "failed"
            with self.lock:
                self.agent_status[agent_name].update(
                    {
                        "status": status,
                        "end_time": finished_at,
                        "duration_seconds": duration_seconds,
                        "returncode": result.returncode,
                        "log_file": str(job.log_file),
                    }
                )

            print(f"✅ {agent_name} 完了: {status} ({duration_seconds/60:.1f}分)")
            return {
                "agent": agent_name,
                "task_file": job.task_file,
                "status": status,
                "duration_seconds": duration_seconds,
                "returncode": result.returncode,
                "log_file": str(job.log_file),
            }

        except subprocess.TimeoutExpired:
            finished_at = datetime.now()
            duration_seconds = (finished_at - started_at).total_seconds()
            with self.lock:
                self.agent_status[agent_name].update(
                    {
                        "status": "timeout",
                        "end_time": finished_at,
                        "duration_seconds": duration_seconds,
                        "log_file": str(job.log_file),
                    }
                )
            print(f"⏱️ {agent_name} タイムアウト ({duration_seconds/60:.1f}分)")
            return {
                "agent": agent_name,
                "task_file": job.task_file,
                "status": "timeout",
                "duration_seconds": duration_seconds,
                "returncode": None,
                "log_file": str(job.log_file),
            }

        except Exception as e:
            finished_at = datetime.now()
            duration_seconds = (finished_at - started_at).total_seconds()
            with self.lock:
                self.agent_status[agent_name].update(
                    {
                        "status": "error",
                        "end_time": finished_at,
                        "duration_seconds": duration_seconds,
                        "error": str(e),
                        "log_file": str(job.log_file),
                    }
                )
            print(f"❌ {agent_name} エラー: {e}")
            return {
                "agent": agent_name,
                "task_file": job.task_file,
                "status": "error",
                "duration_seconds": duration_seconds,
                "error": str(e),
                "returncode": None,
                "log_file": str(job.log_file),
            }

    def run_parallel_batches(self, jobs: List["AutoBatchParallelExecutor.AgentJob"]) -> List[Dict[str, object]]:
        """
        エージェント（= Claude Codeプロセス）を最大N並列で実行。
        jobs が N を超える場合、ThreadPoolExecutor が自動的にバッチングする。
        """
        print("\n" + "=" * 70)
        print("🚀 完全自動化並列バッチ実行システム起動")
        print("=" * 70)
        print(f"同時実行上限: {self.max_concurrent_agents}")
        print(f"ジョブ数: {len(jobs)}")
        print(f"開始時刻: {datetime.now()}")
        print("=" * 70 + "\n")

        results: List[Dict[str, object]] = []

        with ThreadPoolExecutor(max_workers=self.max_concurrent_agents) as executor:
            futures = [executor.submit(self.execute_agent_job, job) for job in jobs]
            for future in as_completed(futures):
                results.append(future.result())

        self._generate_final_report(results)
        return results

    def _generate_final_report(self, results: List[Dict[str, object]]):
        """最終レポート生成（エージェント単位）"""
        print("\n" + "="*70)
        print("📋 最終実行レポート")
        print("="*70)

        total = len(results)
        ok = len([r for r in results if r.get("status") == "completed"])
        ng = total - ok
        success_rate = (ok / total * 100) if total else 0

        print(f"\nジョブ数: {total}")
        print(f"成功: {ok} ({success_rate:.1f}%)")
        print(f"失敗/その他: {ng}")

        print("\n## エージェント別\n")
        for r in sorted(results, key=lambda x: str(x.get("agent", ""))):
            dur = float(r.get("duration_seconds") or 0.0) / 60
            print(f"{r.get('agent')}: {r.get('status')} ({dur:.1f}分) - {r.get('task_file')} - log: {r.get('log_file')}")

        report_path = self.flow_dir / f"auto_batch_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# 自動並列バッチ実行レポート\n\n")
            f.write(f"**実行日時**: {datetime.now()}\n\n")
            f.write(f"## サマリー\n\n")
            f.write(f"- ジョブ数: {total}\n")
            f.write(f"- 成功: {ok} ({success_rate:.1f}%)\n")
            f.write(f"- 失敗/その他: {ng}\n\n")

            f.write(f"## エージェント別詳細\n\n")
            for r in sorted(results, key=lambda x: str(x.get("agent", ""))):
                f.write(f"### {r.get('agent')}\n\n")
                f.write(f"- status: {r.get('status')}\n")
                f.write(f"- task_file: {r.get('task_file')}\n")
                f.write(f"- duration_seconds: {r.get('duration_seconds')}\n")
                f.write(f"- returncode: {r.get('returncode')}\n")
                f.write(f"- log_file: {r.get('log_file')}\n\n")

        print(f"\n📄 レポート保存: {report_path}")
        print("="*70 + "\n")


def main():
    """メイン実行関数"""
    parser = argparse.ArgumentParser(description="完全自動化 並列バッチ実行 (Claude Code / Task tool)")
    parser.add_argument(
        "--task-files",
        nargs="*",
        default=[
            "cli1_vc_backed_tasks.md",
            "cli2_pivot_success_tasks.md",
            "cli3_failure_study_tasks.md",
            "cli4_emerging_part1_tasks.md",
            "cli5_emerging_part2_tasks.md",
        ],
        help="Flowディレクトリ配下のタスクリストファイル名（未指定は5CLI既定）",
    )
    parser.add_argument("--max-concurrent-agents", type=int, default=5, help="同時起動する最大エージェント数")
    parser.add_argument("--timeout-hours", type=float, default=8.0, help="1エージェントあたりのタイムアウト（時間）")
    parser.add_argument("--dry-run", action="store_true", help="実行せず、ジョブ構成のみ表示")
    args = parser.parse_args()

    print(
        "\n".join(
            [
                "╔══════════════════════════════════════════════════════════════════╗",
                "║           完全自動化並列バッチ実行システム                        ║",
                "║                                                                  ║",
                "║  - Task tool前提でClaude Codeを複数プロセス起動                   ║",
                "║  - 同時起動は最大N（既定5）                                      ║",
                "║  - Human介入不要（input待ちなし）                                 ║",
                "╚══════════════════════════════════════════════════════════════════╝",
            ]
        )
    )

    executor = AutoBatchParallelExecutor(
        max_concurrent_agents=args.max_concurrent_agents,
        timeout_seconds_per_agent=int(args.timeout_hours * 60 * 60),
    )

    jobs = executor.build_jobs_from_task_files(args.task_files)

    print("\n設定:")
    print(f"  task_files: {len(args.task_files)}")
    print(f"  max_concurrent_agents: {args.max_concurrent_agents}")
    print(f"  timeout_hours: {args.timeout_hours}")
    for job in jobs:
        print(f"  - Agent-{job.agent_id}: {job.task_file}")

    if args.dry_run:
        print("\n(dry-run) 実行は行いません。")
        return

    executor.run_parallel_batches(jobs)
    print("\n✅ すべてのバッチ実行が完了しました！")


if __name__ == "__main__":
    main()
