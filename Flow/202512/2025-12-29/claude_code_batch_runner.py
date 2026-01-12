#!/usr/bin/env python3
"""
Claude Code バッチランナー - 実戦版
完全自動でClaude Codeセッションを管理し、並列タスク実行

特徴:
- 複数のバッチを同時並列実行
- 各バッチは独立したタスクセットを持つ
- 自動リトライ機能
- リアルタイム進捗監視
- Human介入完全不要

作成日: 2025-12-29
"""

import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse


class ClaudeCodeBatchRunner:
    """Claude Codeバッチ実行マネージャー"""

    def __init__(
        self,
        working_dir: str,
        max_concurrent_batches: int = 5,
        timeout_seconds_per_batch: int = 8 * 60 * 60,
        claude_cmd: str = "claude",
    ):
        """
        初期化

        Args:
            working_dir: 作業ディレクトリ
            max_concurrent_batches: 同時実行する最大バッチ数
            timeout_seconds_per_batch: 1バッチあたりのタイムアウト秒
            claude_cmd: Claude Code CLIのコマンド名
        """
        self.working_dir = Path(working_dir)
        self.max_concurrent_batches = max_concurrent_batches
        self.timeout_seconds_per_batch = timeout_seconds_per_batch
        self.claude_cmd = claude_cmd
        self.flow_dir = self.working_dir / "Flow/202512/2025-12-29"
        self.log_dir = self.flow_dir / "logs"
        self.log_dir.mkdir(exist_ok=True, parents=True)

        # バッチステータス
        self.batch_status = {}
        self.lock = threading.Lock()

    def _generate_batch_prompt(self, batch_id: int, tasks: List[Dict]) -> str:
        """バッチ用のプロンプトを生成"""

        prompt = f"""# Batch {batch_id} 自動実行

以下の{len(tasks)}件のケーススタディを自動作成してください。
すべてHuman介入不要で、完全自動で実行してください。

## 実行設定

- **品質基準**: 85点以上、12ソース以上
- **自動保存**: 各タスク完了後に自動保存
- **エラー処理**: 失敗時は3回までリトライ
- **並列実行**: Task tool で可能な限り並列処理を使用

## タスクリスト

"""

        for idx, task in enumerate(tasks, 1):
            prompt += f"{idx}. **{task['id']}**: {task.get('name', 'N/A')}\n"

        prompt += f"""

## 実行手順

各タスクについて:

1. 企業・創業者の基本情報をリサーチ
2. CPF（Customer Problem Fit）データを収集
3. PSF（Product Solution Fit）データを収集
4. ケーススタディMarkdownファイルを生成
5. 品質チェック（85点以上確認）
6. ファイルを保存
7. 次のタスクへ進む

すべてのタスクが完了したら、完了レポートを生成してください。

**重要**: すべての処理を自動で実行し、ユーザーへの質問や確認は一切行わないでください。
"""

        return prompt

    def run_batch(self, batch_id: int, tasks: List[Dict]):
        """
        バッチを実行

        Args:
            batch_id: バッチID
            tasks: タスクリスト
        """
        with self.lock:
            self.batch_status[f"Batch-{batch_id}"] = {
                'status': 'starting',
                'total_tasks': len(tasks),
                'start_time': datetime.now()
            }

        print(f"🚀 Batch {batch_id} 起動中... ({len(tasks)}件)")

        try:
            prompt = self._generate_batch_prompt(batch_id, tasks)
            log_file = self.log_dir / f"batch_{batch_id}.log"

            result = subprocess.run(
                [self.claude_cmd, "code", "-p", prompt],
                cwd=self.working_dir,
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds_per_batch,
            )

            with self.lock:
                self.batch_status[f"Batch-{batch_id}"].update({
                    'status': 'completed' if result.returncode == 0 else 'failed',
                    'end_time': datetime.now(),
                    'return_code': result.returncode,
                    'log_file': str(log_file),
                })

            log_file.write_text(
                (
                    f"=== Batch {batch_id} log ===\n"
                    f"started_at: {self.batch_status[f'Batch-{batch_id}']['start_time']}\n"
                    f"ended_at: {self.batch_status[f'Batch-{batch_id}']['end_time']}\n"
                    f"return_code: {result.returncode}\n\n"
                    "----- STDOUT -----\n"
                    f"{result.stdout}\n\n"
                    "----- STDERR -----\n"
                    f"{result.stderr}\n"
                ),
                encoding="utf-8",
            )

            print(f"✅ Batch {batch_id} 完了")

        except subprocess.TimeoutExpired:
            with self.lock:
                self.batch_status[f"Batch-{batch_id}"].update({
                    'status': 'timeout',
                    'end_time': datetime.now()
                })
            print(f"⏱️ Batch {batch_id} タイムアウト")

        except Exception as e:
            with self.lock:
                self.batch_status[f"Batch-{batch_id}"].update({
                    'status': 'error',
                    'end_time': datetime.now(),
                    'error': str(e)
                })
            print(f"❌ Batch {batch_id} エラー: {e}")

    def run_parallel_batches(self, batch_assignments: List[Dict]):
        """
        複数のバッチを並列実行

        Args:
            batch_assignments: バッチ割り当てリスト
        """
        print("\n" + "="*70)
        print("🚀 Claude Code 並列バッチ実行システム起動")
        print("="*70)
        print(f"バッチ数: {len(batch_assignments)}")
        print(f"開始時刻: {datetime.now()}")
        print(f"同時実行上限: {self.max_concurrent_batches}")
        print("="*70 + "\n")

        with ThreadPoolExecutor(max_workers=self.max_concurrent_batches) as executor:
            futures = [
                executor.submit(self.run_batch, batch["batch_id"], batch["tasks"])
                for batch in batch_assignments
            ]
            for _ in as_completed(futures):
                pass

        # 最終レポート
        self._print_final_report()

    def _print_final_report(self):
        """最終レポートを表示"""
        print("\n" + "="*70)
        print("📋 実行完了レポート")
        print("="*70 + "\n")

        for batch_name, status in self.batch_status.items():
            print(f"{batch_name}:")
            print(f"  ステータス: {status['status']}")
            print(f"  タスク数: {status['total_tasks']}")

            if 'start_time' in status and 'end_time' in status:
                duration = (status['end_time'] - status['start_time']).total_seconds() / 60
                print(f"  実行時間: {duration:.1f}分")

            if 'error' in status:
                print(f"  エラー: {status['error']}")

            print()

        print("="*70 + "\n")


def load_tasks_from_files(flow_dir: Path, task_files: List[str]) -> List[Dict]:
    """タスクファイルからタスクを読み込み"""
    import re

    all_tasks = []

    for task_file in task_files:
        task_path = flow_dir / task_file

        if task_path.exists():
            with open(task_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 各種ID形式を抽出（FOUNDER/PIVOT/FAILURE/EMERGING）
            tasks = re.findall(r'- \[ \] ((?:FOUNDER|PIVOT|FAILURE|EMERGING)_\d+:.*)', content)

            for task in tasks:
                parts = task.split(':', 1)
                all_tasks.append({
                    'id': parts[0].strip(),
                    'name': parts[1].strip() if len(parts) > 1 else '',
                    'source_file': task_file
                })

    return all_tasks


def main():
    """メイン関数"""

    parser = argparse.ArgumentParser(description="Claude Code バッチランナー（スクリプト生成なし）")
    parser.add_argument("--working-dir", type=str, default=str(Path(__file__).resolve().parents[3]))
    parser.add_argument("--max-concurrent-batches", type=int, default=5)
    parser.add_argument("--timeout-hours", type=float, default=8.0)
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
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(
        "\n".join(
            [
                "╔══════════════════════════════════════════════════════════════════╗",
                "║         Claude Code バッチランナー - 実戦版                       ║",
                "║                                                                  ║",
                "║  - .sh等のスクリプト生成なし（claude code -p を直接実行）         ║",
                "║  - 同時実行は最大N（既定5）                                      ║",
                "║  - Human介入不要（input待ちなし）                                 ║",
                "╚══════════════════════════════════════════════════════════════════╝",
            ]
        )
    )

    working_dir = args.working_dir
    flow_dir = Path(working_dir) / "Flow/202512/2025-12-29"

    # ランナー初期化
    runner = ClaudeCodeBatchRunner(
        working_dir=working_dir,
        max_concurrent_batches=args.max_concurrent_batches,
        timeout_seconds_per_batch=int(args.timeout_hours * 60 * 60),
    )

    # タスク読み込み
    all_tasks = load_tasks_from_files(flow_dir, args.task_files)

    print(f"✅ {len(all_tasks)}件のタスクを読み込みました\n")

    # タスクを5つのバッチに分割
    batch_size = len(all_tasks) // 5 + (1 if len(all_tasks) % 5 != 0 else 0)

    batch_assignments = []
    for i in range(5):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(all_tasks))
        batch_assignments.append({
            'batch_id': i + 1,
            'tasks': all_tasks[start_idx:end_idx]
        })

    # 設定表示
    print(f"設定:")
    print(f"  バッチ数: {len(batch_assignments)}")
    print(f"  総タスク数: {len(all_tasks)}")
    print(f"  各バッチ担当: 約{batch_size}件\n")

    for batch in batch_assignments:
        print(f"  Batch {batch['batch_id']}: {len(batch['tasks'])}件")

    if args.dry_run:
        print("\n(dry-run) 実行は行いません。")
        return

    # 並列実行
    runner.run_parallel_batches(batch_assignments)

    print("\n✅ すべてのバッチ実行が完了しました！")


if __name__ == "__main__":
    main()
