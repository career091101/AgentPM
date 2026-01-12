#!/bin/bash

# LinkedIn投稿用画像生成スキル実行スクリプト
# 使用方法: /generate-linkedin-image

set -e

# プロジェクトルート
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS"
SCRIPT_PATH="$PROJECT_ROOT/scripts/generate_linkedin_image_nanobananapro.py"

# 環境変数チェック
if [ -z "$GOOGLE_GEMINI_API_KEY" ]; then
    echo "❌ エラー: 環境変数 GOOGLE_GEMINI_API_KEY が設定されていません"
    echo ""
    echo "以下の手順でAPIキーを設定してください:"
    echo "1. https://aistudio.google.com/apikey にアクセス"
    echo "2. APIキーを取得"
    echo "3. 環境変数を設定:"
    echo "   export GOOGLE_GEMINI_API_KEY='your-api-key-here'"
    echo ""
    exit 1
fi

# 依存ライブラリチェック
if ! python3 -c "import genai" 2>/dev/null; then
    echo "⚠️  警告: google-genai ライブラリが見つかりません"
    echo "インストール中..."
    pip install google-genai pillow -q
fi

# スクリプト実行
cd "$PROJECT_ROOT"
python3 "$SCRIPT_PATH"
