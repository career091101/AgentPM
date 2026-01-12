#!/usr/bin/env python3
"""
Auto Parallel Executor for Founder Research
This script prepares batch execution instructions for Claude Code's Task tool
"""

import json
from pathlib import Path
from datetime import datetime

class AutoParallelExecutor:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.scripts_dir = self.project_root / "scripts"
        self.wave_defs_file = self.scripts_dir / "wave_definitions.json"
        self.progress_file = self.scripts_dir / "progress.json"
        self.load_definitions()
        self.load_progress()

    def load_definitions(self):
        with open(self.wave_defs_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.waves = data['waves']
            self.strategy = data.get('execution_strategy', {})

    def load_progress(self):
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                'started_at': None,
                'completed': [],
                'failed': [],
                'in_progress': [],
                'waves': {}
            }

    def save_progress(self):
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)

    def get_batch_targets(self, wave_id, batch_size=10):
        """Get next batch of targets to process"""
        wave = next((w for w in self.waves if w['id'] == wave_id), None)
        if not wave:
            return []

        completed = set(self.progress.get('completed', []))
        in_progress = set(self.progress.get('in_progress', []))

        batch = []
        for target in wave['targets']:
            target_id = target['id']
            if target_id not in completed and target_id not in in_progress:
                batch.append({
                    'id': target_id,
                    'type': target['type'],
                    'category': target['category'],
                    'wave_id': wave_id,
                    'wave_name': wave['name']
                })
                if len(batch) >= batch_size:
                    break

        return batch

    def generate_task_prompts(self, wave_id, batch_size=10):
        """Generate prompts for Claude Code Task tool"""
        batch = self.get_batch_targets(wave_id, batch_size)

        if not batch:
            print(f"\n✅ No pending targets for {wave_id} - all completed!\n")
            return []

        print(f"\n{'='*80}")
        print(f"Batch Execution Plan for {wave_id}")
        print(f"{'='*80}")
        print(f"Batch size: {len(batch)} agents")
        print(f"Targets: {', '.join([t['id'] for t in batch])}")
        print(f"{'='*80}\n")

        prompts = []
        for target in batch:
            prompt = self._create_prompt(target)
            prompts.append({
                'target': target,
                'prompt': prompt
            })

        return prompts

    def _create_prompt(self, target):
        """Create detailed prompt for a single document generation"""
        target_id = target['id']
        target_type = target['type']
        category = target['category']
        wave_name = target['wave_name']

        base_path = f"aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research"

        if target_type == 'founder':
            return f"""# {target_id} - Founder Research Document Generation

## Objective
Generate a comprehensive founder research document for {target_id}.

## Document Structure
Follow the format in documents/08_Emerging/EMERGING_068_bereal.md with these 12 sections:
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
12. 追加情報・特記事項 (including クオリティスコア)

## Research Instructions
1. Use WebSearch to find information about this company/founder
2. Look for: company background, founder bio, funding history, growth metrics, business model
3. Analyze failure patterns, pivot stories, or success factors as applicable
4. Include specific data points: revenue, funding, user numbers, etc.
5. Provide quality score (0-100) based on source reliability and data completeness

## Output
- File path: {base_path}/documents/{category}/{target_id}.md
- Format: Markdown with proper Japanese formatting
- Include information sources at the end

## Execution Mode
🤖 FULLY AUTOMATED - No human input required. Make best judgment based on available sources.

Wave: {wave_name}
Category: {category}
"""

        elif target_type == 'failure':
            return f"""# {target_id} - Failure Study Document Generation

## Objective
Generate a comprehensive failure analysis document for {target_id}.

## Document Structure
Create detailed failure study with these sections:
1. 企業概要 - Company overview
2. 失敗の概要 - Failure summary
3. 初期の成功要因 - Early success factors
4. 失敗の兆候 - Warning signs
5. 決定的な失敗要因 - Critical failure factors
6. 経営判断の分析 - Management decision analysis
7. ステークホルダーへの影響 - Stakeholder impact
8. 教訓・学び - Lessons learned
9. データ・KPI - Key metrics and data
10. タイムライン - Timeline of events
11. 追加情報・特記事項 - Additional notes (including クオリティスコア)

## Research Instructions
1. Use WebSearch to find detailed information about this company failure
2. Look for: founding story, initial success, pivot points, failure triggers
3. Analyze root causes: market fit, execution, timing, competition, etc.
4. Include specific failure data: burn rate, user churn, revenue decline
5. Provide quality score based on source depth

## Output
- File path: {base_path}/documents/{category}/{target_id}.md
- Format: Markdown with proper Japanese formatting
- Include information sources

## Execution Mode
🤖 FULLY AUTOMATED - No human input required.

Wave: {wave_name}
Category: {category}
"""

        elif target_type == 'pivot':
            return f"""# {target_id} - Pivot Success Document Generation

## Objective
Generate a comprehensive pivot success story for {target_id}.

## Document Structure
Analyze successful pivot with these sections:
1. 初期ビジネス - Original business
2. ピボットの経緯 - Pivot background/trigger
3. 新ビジネス - New business model
4. ピボットの実行 - Pivot execution
5. 成果 - Results and outcomes
6. 学び・洞察 - Insights and learnings
7. データ・KPI - Metrics before/after pivot
8. タイムライン - Pivot timeline
9. 追加情報・特記事項 - Additional notes (including クオリティスコア)

## Research Instructions
1. Use WebSearch to find pivot story details
2. Compare before/after states: business model, target market, metrics
3. Analyze why pivot was necessary and how it was executed
4. Include specific pivot data: timeline, team changes, metrics shift
5. Provide quality score

## Output
- File path: {base_path}/documents/{category}/{target_id}.md
- Format: Markdown with proper Japanese formatting
- Include information sources

## Execution Mode
🤖 FULLY AUTOMATED - No human input required.

Wave: {wave_name}
Category: {category}
"""

    def print_execution_instructions(self, wave_id, batch_size=10):
        """Print instructions for manual parallel execution via Claude Code"""
        prompts = self.generate_task_prompts(wave_id, batch_size)

        if not prompts:
            return

        print("\n" + "="*80)
        print("PARALLEL EXECUTION INSTRUCTIONS")
        print("="*80)
        print("\nTo execute this batch in parallel, I will launch multiple Task agents.")
        print(f"Total agents: {len(prompts)}")
        print("\nEach agent will:")
        print("  1. Research the target company/founder using WebSearch")
        print("  2. Generate comprehensive markdown document")
        print("  3. Save to appropriate category folder")
        print("  4. Complete automatically without human input")
        print("\n" + "="*80 + "\n")

        return prompts

    def create_batch_file(self, wave_id, batch_size=10, output_file=None):
        """Create a batch file for execution"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.scripts_dir / f"batch_{wave_id}_{timestamp}.json"

        prompts = self.generate_task_prompts(wave_id, batch_size)

        batch_data = {
            'wave_id': wave_id,
            'batch_size': len(prompts),
            'created_at': datetime.now().isoformat(),
            'targets': [p['target'] for p in prompts],
            'prompts': [p['prompt'] for p in prompts]
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Batch file created: {output_file}")
        print(f"Targets: {len(prompts)}")

        return output_file, prompts


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Auto Parallel Executor for Founder Research')
    parser.add_argument('--wave', type=str, required=True, help='Wave ID (e.g., wave1)')
    parser.add_argument('--batch-size', type=int, default=10, help='Batch size')
    parser.add_argument('--create-batch', action='store_true', help='Create batch file')
    parser.add_argument('--project-root', type=str, default='.', help='Project root')

    args = parser.parse_args()

    executor = AutoParallelExecutor(project_root=args.project_root)

    if args.create_batch:
        executor.create_batch_file(args.wave, args.batch_size)
    else:
        executor.print_execution_instructions(args.wave, args.batch_size)


if __name__ == '__main__':
    main()
