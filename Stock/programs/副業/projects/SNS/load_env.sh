#!/bin/bash
# .envファイルから環境変数を読み込むスクリプト

ENV_FILE="/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo "❌ Error: .env file not found at $ENV_FILE"
    exit 1
fi

# .envファイルを読み込み（コメント行と空行を除外）
set -a
source "$ENV_FILE"
set +a

echo "✅ Environment variables loaded from .env"
echo ""
echo "🔹 X API Status:"
echo "   X_BEARER_TOKEN: ${X_BEARER_TOKEN:0:20}..."
echo "   X_API_KEY: ${X_API_KEY:0:10}..."
echo "   X_ACCESS_TOKEN: ${X_ACCESS_TOKEN:0:15}..."
echo ""
echo "🔹 LinkedIn API Status:"
if [ "$LINKEDIN_ACCESS_TOKEN" = "your_linkedin_access_token_here" ]; then
    echo "   ⚠️  Not configured yet"
else
    echo "   ✅ Configured"
    echo "   LINKEDIN_ACCESS_TOKEN: ${LINKEDIN_ACCESS_TOKEN:0:30}..."
    echo "   LINKEDIN_PERSON_URN: $LINKEDIN_PERSON_URN"
fi
echo ""
echo "🔹 Slack API Status:"
if [ -n "$SLACK_BOT_TOKEN" ] && [ "$SLACK_BOT_TOKEN" != "your_slack_bot_token_here" ]; then
    echo "   ✅ Configured"
    echo "   SLACK_BOT_TOKEN: ${SLACK_BOT_TOKEN:0:20}..."
    echo "   SLACK_TEAM_ID: $SLACK_TEAM_ID"
    echo "   SLACK_CHANNEL: $SLACK_CHANNEL"
else
    echo "   ⚠️  Not configured yet"
fi
echo ""
echo "環境変数が正常に読み込まれました。"
echo "このシェルセッション内でSNS自動投稿スキルを実行できます。"
