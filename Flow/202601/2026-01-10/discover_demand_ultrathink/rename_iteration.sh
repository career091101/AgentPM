#!/bin/bash
# discover-demand実行後の自動ファイルリネームスクリプト

ITERATION=$1
THEME=$2

if [ -z "$ITERATION" ] || [ -z "$THEME" ]; then
    echo "Usage: ./rename_iteration.sh <iteration_num> <theme>"
    echo "Example: ./rename_iteration.sh 001 success_cases"
    exit 1
fi

SOURCE="Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Agent_Phase1/documents/1_initiating/demand_discovery.md"
TARGET="Flow/202601/2026-01-10/discover_demand_ultrathink/iterations/iteration_${ITERATION}_${THEME}.md"

if [ ! -f "$SOURCE" ]; then
    echo "エラー: ソースファイルが見つかりません: $SOURCE"
    exit 1
fi

cp "$SOURCE" "$TARGET"
echo "✅ イテレーション${ITERATION}をコピー: $TARGET"
ls -lh "$TARGET"
