#!/bin/bash
# ClaudeCode修正ヘルパースクリプト
# 修正リクエストを確認し、ClaudeCodeに修正プロンプトを提示

set -e

SNS_DATA_DIR="/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"

echo "============================================================"
echo "ClaudeCode修正リクエスト確認"
echo "============================================================"
echo ""

# 未処理の修正リクエストを検索
request_files=$(ls -t "$SNS_DATA_DIR"/refine_request_*.json 2>/dev/null || echo "")

if [ -z "$request_files" ]; then
    echo "✅ 現在、未処理の修正リクエストはありません"
    exit 0
fi

# 最新のリクエストを処理
latest_request=$(echo "$request_files" | head -1)
thread_ts=$(basename "$latest_request" | sed 's/refine_request_//' | sed 's/.json//')

echo "📝 未処理の修正リクエストが見つかりました"
echo "   thread_ts: $thread_ts"
echo ""

# リクエスト内容を表示
echo "【リクエスト内容】"
cat "$latest_request" | python3 -m json.tool
echo ""
echo "============================================================"
echo "修正方法:"
echo "============================================================"
echo ""
echo "方法1: 自動修正プロンプト表示"
echo "  python3 scripts/process_refine_request_auto.py $thread_ts"
echo ""
echo "方法2: 手動入力で修正"
echo "  python3 scripts/process_refine_request.py $thread_ts"
echo ""
echo "方法3: ClaudeCodeに直接依頼"
echo "  以下の内容をClaudeCodeに送信してください:"
echo ""
echo "---"
cat "$latest_request" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(f'''
以下のSNS投稿を修正してください:

【元の投稿】
{data['original_content']}

【修正指示】
{data['instruction']}

【ルール】
- 修正指示に従った変更のみ行う
- 投稿の構造は維持
- 200字以内
- LinkedIn投稿として自然な文体

修正後、以下のコマンドで保存:
python3 scripts/process_refine_request_auto.py {data['thread_ts']} \"修正後の内容\"
''')
"
echo "---"
echo ""
