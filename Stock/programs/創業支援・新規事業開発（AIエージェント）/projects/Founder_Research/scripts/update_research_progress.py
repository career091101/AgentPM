#!/usr/bin/env python3
"""
Update research_progress.md with IPO_Global batch results
Auto-updates progress file after batch completion
"""

import re
from pathlib import Path
from datetime import datetime


class ResearchProgressUpdater:
    """Update research_progress.md with batch results"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.progress_file = self.project_root / "research_progress.md"
        self.docs_dir = self.project_root / "documents" / "05_IPO_Global"

    def count_completed_documents(self) -> int:
        """Count completed IPO_Global documents"""
        if not self.docs_dir.exists():
            return 0

        return len(list(self.docs_dir.glob("FOUNDER_*.md")))

    def update_progress_file(self):
        """Update research_progress.md with new progress"""
        if not self.progress_file.exists():
            print(f"Error: {self.progress_file} not found")
            return

        # Count completed IPO_Global documents
        ipo_global_count = self.count_completed_documents()

        # Read current content
        content = self.progress_file.read_text(encoding='utf-8')

        # Update overall progress (400 -> 400 + new_count, max 425)
        old_total = 400
        new_total = min(old_total + ipo_global_count - 21, 425)  # 21 already existed
        new_percentage = round((new_total / 500) * 100, 1)

        content = re.sub(
            r'現在の進捗\*\*: \d+/500 \([\d.]+%\)',
            f'現在の進捗**: {new_total}/500 ({new_percentage}%)',
            content
        )

        # Update 05_IPO_Global tier
        ipo_percentage = round((ipo_global_count / 50) * 100)

        # Find tier table and update 05_IPO_Global line
        tier_pattern = r'\| 05_IPO_Global \| \d+ \| \d+ \| \d+% \| [^|]+ \|'
        tier_replacement = f'| 05_IPO_Global | 50 | {ipo_global_count} | {ipo_percentage}% | {"🟢 ほぼ完了" if ipo_percentage >= 90 else "🟡 進行中"} |'

        content = re.sub(tier_pattern, tier_replacement, content)

        # Add update entry to history table
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        new_entry = f"| {timestamp} | **IPO_Global Batch完了**: Task tool並列実行で{ipo_global_count-21}件追加（FOUNDER_357-381） | {new_total}/500 ({new_percentage}%) | Claude Code |\n"

        # Insert at top of update history (after header)
        history_pattern = r'(\| 日時 \| 内容 \| 進捗 \| 担当 \|\n\|[-|\s]+\|\n)'
        content = re.sub(history_pattern, r'\1' + new_entry, content)

        # Update last updated timestamp
        content = re.sub(
            r'最終更新: \d{4}-\d{2}-\d{2} \d{2}:\d{2}',
            f'最終更新: {timestamp}',
            content
        )

        # Write back
        self.progress_file.write_text(content, encoding='utf-8')

        print(f"\n{'='*80}")
        print("research_progress.md Updated")
        print(f"{'='*80}")
        print(f"05_IPO_Global: 21 → {ipo_global_count} ({ipo_global_count-21} new)")
        print(f"Overall Progress: {old_total}/500 → {new_total}/500 ({new_percentage}%)")
        print(f"{'='*80}\n")

    def print_completed_files(self):
        """Print list of completed files"""
        if not self.docs_dir.exists():
            print("No documents found")
            return

        files = sorted(self.docs_dir.glob("FOUNDER_*.md"))

        print("\n" + "="*80)
        print(f"Completed IPO_Global Documents ({len(files)} files)")
        print("="*80)

        for file_path in files:
            # Extract founder/company from filename
            filename = file_path.stem
            parts = filename.split('_', 1)
            if len(parts) == 2:
                target_id = parts[0]
                company = parts[1].replace('_', ' ').title()
                print(f"  ✓ {target_id}: {company}")

        print("="*80 + "\n")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Update research_progress.md')
    parser.add_argument('--list', action='store_true', help='List completed files only')

    args = parser.parse_args()

    # Setup
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    updater = ResearchProgressUpdater(project_root)

    if args.list:
        # Just list files
        updater.print_completed_files()
    else:
        # Update progress and list files
        updater.update_progress_file()
        updater.print_completed_files()
