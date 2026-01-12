#!/usr/bin/env python3
"""
Parallel Batch Orchestrator for Founder Research Document Generation
Executes multiple Claude Code agents in parallel to generate research documents
"""

import json
import subprocess
import time
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

class ParallelBatchOrchestrator:
    def __init__(self, wave_definitions_path, project_root, max_parallel=10):
        self.wave_definitions_path = Path(wave_definitions_path)
        self.project_root = Path(project_root)
        self.max_parallel = max_parallel
        self.progress_file = self.project_root / "scripts" / "progress.json"
        self.load_definitions()
        self.load_progress()

    def load_definitions(self):
        """Load wave definitions from JSON file"""
        with open(self.wave_definitions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.waves = data['waves']
            self.execution_strategy = data.get('execution_strategy', {})

    def load_progress(self):
        """Load progress tracking data"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                'started_at': None,
                'completed': [],
                'failed': [],
                'in_progress': [],
                'pending': [],
                'total': 0,
                'waves': {}
            }

    def save_progress(self):
        """Save progress tracking data"""
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)

    def get_pending_targets(self, wave_id=None):
        """Get list of pending targets to process"""
        pending = []

        waves_to_process = [w for w in self.waves if wave_id is None or w['id'] == wave_id]

        for wave in waves_to_process:
            for target in wave['targets']:
                target_id = target['id']
                if (target_id not in self.progress['completed'] and
                    target_id not in self.progress['in_progress']):
                    pending.append({
                        'wave_id': wave['id'],
                        'wave_name': wave['name'],
                        **target
                    })

        return pending

    def execute_agent(self, target):
        """Execute a single Claude Code agent for a target"""
        target_id = target['id']
        target_type = target['type']
        category = target['category']
        wave_id = target['wave_id']
        wave_name = target['wave_name']

        # Mark as in progress
        self.progress['in_progress'].append(target_id)
        self.save_progress()

        # Create agent prompt based on document type
        if target_type == 'founder':
            prompt = f"""Generate a comprehensive founder research document for {target_id}.

Document should follow the EMERGING_068_bereal.md format with these sections:
1. 創業の経緯・課題認識
2. ソリューション・事業内容
3. 市場環境・競合分析
4. 成長プロセス
5. 資金調達・投資家
6. 技術・イノベーション
7. チーム・組織文化
8. 課題と解決アプローチ
9. 学び・洞察
10. データ・KPI
11. 創業者の特徴・思考
12. 追加情報・特記事項

Research the company/founder thoroughly using web search and create a detailed markdown document.
Save to: aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/{category}/{target_id}.md

This is a FULLY AUTOMATED batch execution. DO NOT ask for human input. Use your best judgment and available online sources."""

        elif target_type == 'failure':
            prompt = f"""Generate a comprehensive failure study document for {target_id}.

Document should analyze the failure with these sections:
1. 企業概要
2. 失敗の概要
3. 初期の成功要因
4. 失敗の兆候
5. 決定的な失敗要因
6. 経営判断の分析
7. ステークホルダーへの影響
8. 教訓・学び
9. データ・KPI
10. タイムライン
11. 追加情報・特記事項

Research the company failure thoroughly using web search and create a detailed markdown document.
Save to: aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/{category}/{target_id}.md

This is a FULLY AUTOMATED batch execution. DO NOT ask for human input. Use your best judgment and available online sources."""

        elif target_type == 'pivot':
            prompt = f"""Generate a comprehensive pivot success document for {target_id}.

Document should analyze the successful pivot with these sections:
1. 初期ビジネス
2. ピボットの経緯
3. 新ビジネス
4. ピボットの実行
5. 成果
6. 学び・洞察
7. データ・KPI
8. タイムライン
9. 追加情報・特記事項

Research the company pivot thoroughly using web search and create a detailed markdown document.
Save to: aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/{category}/{target_id}.md

This is a FULLY AUTOMATED batch execution. DO NOT ask for human input. Use your best judgment and available online sources."""

        # Execute Claude Code agent
        start_time = time.time()
        try:
            # Using subprocess to call claude command
            # This assumes 'claude' is available in PATH
            result = subprocess.run(
                ['claude', 'code', '-p', prompt],
                capture_output=True,
                text=True,
                timeout=600,  # 10 minute timeout per document
                cwd=self.project_root
            )

            duration = time.time() - start_time

            if result.returncode == 0:
                # Success
                self.progress['in_progress'].remove(target_id)
                self.progress['completed'].append(target_id)

                # Update wave progress
                if wave_id not in self.progress['waves']:
                    self.progress['waves'][wave_id] = {'completed': 0, 'total': 0}
                self.progress['waves'][wave_id]['completed'] += 1

                self.save_progress()

                return {
                    'target_id': target_id,
                    'status': 'success',
                    'duration': duration,
                    'wave_id': wave_id,
                    'wave_name': wave_name
                }
            else:
                # Failed
                self.progress['in_progress'].remove(target_id)
                self.progress['failed'].append({
                    'target_id': target_id,
                    'error': result.stderr,
                    'timestamp': datetime.now().isoformat()
                })
                self.save_progress()

                return {
                    'target_id': target_id,
                    'status': 'failed',
                    'error': result.stderr,
                    'duration': duration,
                    'wave_id': wave_id,
                    'wave_name': wave_name
                }

        except subprocess.TimeoutExpired:
            self.progress['in_progress'].remove(target_id)
            self.progress['failed'].append({
                'target_id': target_id,
                'error': 'Timeout after 10 minutes',
                'timestamp': datetime.now().isoformat()
            })
            self.save_progress()

            return {
                'target_id': target_id,
                'status': 'timeout',
                'duration': 600,
                'wave_id': wave_id,
                'wave_name': wave_name
            }
        except Exception as e:
            self.progress['in_progress'].remove(target_id)
            self.progress['failed'].append({
                'target_id': target_id,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
            self.save_progress()

            return {
                'target_id': target_id,
                'status': 'error',
                'error': str(e),
                'duration': time.time() - start_time,
                'wave_id': wave_id,
                'wave_name': wave_name
            }

    def execute_wave(self, wave_id=None, dry_run=False):
        """Execute a wave of document generation in parallel"""

        if self.progress['started_at'] is None:
            self.progress['started_at'] = datetime.now().isoformat()

        pending = self.get_pending_targets(wave_id)

        if not pending:
            print(f"No pending targets to process for wave: {wave_id or 'all'}")
            return

        # Initialize wave totals
        for wave in self.waves:
            if wave['id'] not in self.progress['waves']:
                self.progress['waves'][wave['id']] = {
                    'completed': 0,
                    'total': wave['count']
                }

        self.progress['total'] = sum(w['count'] for w in self.waves)
        self.save_progress()

        print(f"\n{'='*80}")
        print(f"Parallel Batch Execution Started")
        print(f"{'='*80}")
        print(f"Wave: {wave_id or 'ALL'}")
        print(f"Total targets: {len(pending)}")
        print(f"Max parallel agents: {self.max_parallel}")
        print(f"Dry run: {dry_run}")
        print(f"{'='*80}\n")

        if dry_run:
            print("DRY RUN - Would process:")
            for target in pending:
                print(f"  - {target['id']} ({target['wave_name']})")
            return

        # Execute in parallel
        results = []
        with ThreadPoolExecutor(max_workers=self.max_parallel) as executor:
            futures = {executor.submit(self.execute_agent, target): target for target in pending}

            for future in as_completed(futures):
                result = future.result()
                results.append(result)

                # Print progress
                completed = len([r for r in results if r['status'] == 'success'])
                failed = len([r for r in results if r['status'] in ['failed', 'timeout', 'error']])
                total = len(pending)

                status_emoji = "✅" if result['status'] == 'success' else "❌"
                print(f"{status_emoji} {result['target_id']} - {result['status']} ({result.get('duration', 0):.1f}s) [{completed}/{total} completed, {failed} failed]")

        # Final summary
        print(f"\n{'='*80}")
        print(f"Batch Execution Complete")
        print(f"{'='*80}")
        print(f"Total processed: {len(results)}")
        print(f"Successful: {len([r for r in results if r['status'] == 'success'])}")
        print(f"Failed: {len([r for r in results if r['status'] != 'success'])}")
        print(f"{'='*80}\n")

        # Print wave progress
        print("\nWave Progress:")
        for wave_id, wave_data in self.progress['waves'].items():
            wave = next((w for w in self.waves if w['id'] == wave_id), None)
            if wave:
                completion_pct = (wave_data['completed'] / wave_data['total']) * 100
                print(f"  {wave['name']}: {wave_data['completed']}/{wave_data['total']} ({completion_pct:.1f}%)")

        return results

    def get_status(self):
        """Get current execution status"""
        print(f"\n{'='*80}")
        print(f"Execution Status")
        print(f"{'='*80}")

        if self.progress['started_at']:
            print(f"Started: {self.progress['started_at']}")

        total_completed = len(self.progress['completed'])
        total_failed = len(self.progress['failed'])
        total_in_progress = len(self.progress['in_progress'])
        total_targets = self.progress.get('total', 64)

        print(f"\nOverall Progress: {total_completed}/{total_targets} completed ({(total_completed/total_targets)*100:.1f}%)")
        print(f"In Progress: {total_in_progress}")
        print(f"Failed: {total_failed}")

        print(f"\nWave Progress:")
        for wave in self.waves:
            wave_data = self.progress['waves'].get(wave['id'], {'completed': 0, 'total': wave['count']})
            completion_pct = (wave_data['completed'] / wave_data['total']) * 100
            print(f"  {wave['name']}: {wave_data['completed']}/{wave_data['total']} ({completion_pct:.1f}%)")

        print(f"{'='*80}\n")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Parallel Batch Orchestrator for Founder Research')
    parser.add_argument('--wave', type=str, help='Specific wave ID to execute (e.g., wave1, wave2)')
    parser.add_argument('--max-parallel', type=int, default=10, help='Maximum number of parallel agents')
    parser.add_argument('--dry-run', action='store_true', help='Dry run without executing')
    parser.add_argument('--status', action='store_true', help='Show current status only')
    parser.add_argument('--project-root', type=str, default='.', help='Project root directory')

    args = parser.parse_args()

    # Determine paths
    script_dir = Path(__file__).parent
    wave_definitions = script_dir / 'wave_definitions.json'
    project_root = Path(args.project_root).resolve()

    # Create orchestrator
    orchestrator = ParallelBatchOrchestrator(
        wave_definitions_path=wave_definitions,
        project_root=project_root,
        max_parallel=args.max_parallel
    )

    if args.status:
        orchestrator.get_status()
    else:
        orchestrator.execute_wave(wave_id=args.wave, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
