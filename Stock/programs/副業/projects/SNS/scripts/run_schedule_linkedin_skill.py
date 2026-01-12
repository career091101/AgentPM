#!/usr/bin/env python3
"""
LinkedIn 3案自動予約投稿スキル実行ラッパー

Usage:
    python3 scripts/run_schedule_linkedin_skill.py

    または Claude Code CLI:
    /schedule-linkedin-3-cases
"""

import sys
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "scripts"))

# 既存のメインスクリプトをインポートして実行
from schedule_linkedin_post import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  ユーザーによる中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ エラー: {e}")
        sys.exit(1)
