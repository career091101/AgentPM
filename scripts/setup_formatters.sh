#!/usr/bin/env bash

# ============================================================================
# Formatter Setup Script for aipm_v0
# ============================================================================
#
# このスクリプトは以下をインストール・設定します:
# - black 25.12.0 (Homebrew経由)
# - isort 7.0.0 (Homebrew経由)
# - prettier 3.7.4 (npx経由、グローバルインストール不要)
# - jq (オプション、Homebrew経由)
#
# 実行: bash scripts/setup_formatters.sh
# ============================================================================

set -e  # エラー時に即座終了

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# プロジェクトルート取得
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# ============================================================================
# ヘルパー関数
# ============================================================================

print_header() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "  $1"
}

# ============================================================================
# Homebrew 確認
# ============================================================================

check_homebrew() {
    print_header "Homebrew 確認"

    if ! command -v brew &> /dev/null; then
        print_error "Homebrew がインストールされていません"
        print_info "以下のコマンドでインストールしてください:"
        print_info '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        exit 1
    fi

    print_success "Homebrew 検出: $(brew --version | head -n1)"
}

# ============================================================================
# black インストール
# ============================================================================

install_black() {
    print_header "black インストール"

    if command -v black &> /dev/null; then
        local current_version=$(black --version 2>&1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
        print_info "既存バージョン: $current_version"

        # バージョン 25.12.0 以上ならスキップ
        if [ "$(printf '%s\n' "25.12.0" "$current_version" | sort -V | head -n1)" = "25.12.0" ]; then
            print_success "black は既に要件を満たしています"
            return 0
        fi

        print_warning "古いバージョンを検出、アップグレード中..."
    fi

    print_info "Homebrew 経由で black をインストール中..."
    if brew install black 2>&1 | grep -q "already installed"; then
        brew upgrade black
    fi

    # インストール確認
    if command -v black &> /dev/null; then
        local installed_version=$(black --version 2>&1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
        print_success "black インストール完了: v$installed_version"
    else
        print_error "black のインストールに失敗しました"
        exit 1
    fi
}

# ============================================================================
# isort インストール
# ============================================================================

install_isort() {
    print_header "isort インストール"

    if command -v isort &> /dev/null; then
        local current_version=$(isort --version 2>&1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
        print_info "既存バージョン: $current_version"

        # バージョン 7.0.0 以上ならスキップ
        if [ "$(printf '%s\n' "7.0.0" "$current_version" | sort -V | head -n1)" = "7.0.0" ]; then
            print_success "isort は既に要件を満たしています"
            return 0
        fi

        print_warning "古いバージョンを検出、アップグレード中..."
    fi

    print_info "Homebrew 経由で isort をインストール中..."
    if brew install isort 2>&1 | grep -q "already installed"; then
        brew upgrade isort
    fi

    # インストール確認
    if command -v isort &> /dev/null; then
        local installed_version=$(isort --version 2>&1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
        print_success "isort インストール完了: v$installed_version"
    else
        print_error "isort のインストールに失敗しました"
        exit 1
    fi
}

# ============================================================================
# prettier 確認（npx経由、インストール不要）
# ============================================================================

check_prettier() {
    print_header "prettier 確認"

    # Node.js/npm/npx の確認
    if ! command -v node &> /dev/null; then
        print_error "Node.js がインストールされていません"
        print_info "以下のコマンドでインストールしてください:"
        print_info "brew install node"
        exit 1
    fi

    if ! command -v npx &> /dev/null; then
        print_error "npx がインストールされていません"
        print_info "Node.js をアップグレードしてください:"
        print_info "brew upgrade node"
        exit 1
    fi

    print_success "Node.js 検出: $(node --version)"
    print_success "npx 検出: $(npx --version)"

    # prettier バージョン確認（npx経由）
    print_info "prettier バージョン確認中..."
    local prettier_version=$(npx prettier --version 2>/dev/null || echo "未確認")
    print_success "prettier 利用可能: v$prettier_version (npx経由)"
    print_info "注: prettier はグローバルインストール不要（npx で自動取得）"
}

# ============================================================================
# jq インストール（オプション）
# ============================================================================

install_jq() {
    print_header "jq インストール（オプション）"

    if command -v jq &> /dev/null; then
        local current_version=$(jq --version 2>&1 | grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -n1)
        print_success "jq は既にインストール済み: v$current_version"
        return 0
    fi

    print_info "Homebrew 経由で jq をインストール中..."
    if brew install jq 2>&1; then
        local installed_version=$(jq --version 2>&1 | grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -n1)
        print_success "jq インストール完了: v$installed_version"
    else
        print_warning "jq のインストールに失敗しましたが、必須ではないため続行します"
    fi
}

# ============================================================================
# 設定ファイル作成
# ============================================================================

create_config_files() {
    print_header "設定ファイル作成"

    cd "$PROJECT_ROOT"

    # ========================================
    # pyproject.toml (black + isort)
    # ========================================

    if [ -f "pyproject.toml" ]; then
        print_info "pyproject.toml は既に存在します（スキップ）"
    else
        print_info "pyproject.toml を作成中..."
        cat > pyproject.toml << 'EOF'
[tool.black]
line-length = 100
target-version = ['py39', 'py310', 'py311']
extend-exclude = '''
/(
  Flow/
  | Archived/
  | \.venv/
  | venv/
  | env/
  | node_modules/
  | dist/
  | build/
)/
'''

[tool.isort]
profile = "black"
line_length = 100
skip = [
    "Flow",
    "Archived",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build"
]
sections = ['FUTURE', 'STDLIB', 'THIRDPARTY', 'FIRSTPARTY', 'LOCALFOLDER']
known_first_party = []
EOF
        print_success "pyproject.toml 作成完了"
    fi

    # ========================================
    # .prettierrc (prettier)
    # ========================================

    if [ -f ".prettierrc" ]; then
        print_info ".prettierrc は既に存在します（スキップ）"
    else
        print_info ".prettierrc を作成中..."
        cat > .prettierrc << 'EOF'
{
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": false,
  "quoteProps": "as-needed",
  "jsxSingleQuote": false,
  "trailingComma": "es5",
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always",
  "proseWrap": "preserve",
  "endOfLine": "lf"
}
EOF
        print_success ".prettierrc 作成完了"
    fi

    # ========================================
    # .prettierignore (prettier除外)
    # ========================================

    if [ -f ".prettierignore" ]; then
        print_info ".prettierignore は既に存在します（スキップ）"
    else
        print_info ".prettierignore を作成中..."
        cat > .prettierignore << 'EOF'
# Dependencies
node_modules/
.venv/
venv/
env/

# Build outputs
dist/
build/
out/
target/

# Cache
.cache/
.parcel-cache/
.next/
.nuxt/

# Archived/Flow
Archived/
Flow/

# Logs
*.log

# Lock files (generated)
package-lock.json
yarn.lock
pnpm-lock.yaml

# Minified files
*.min.js
*.min.css
EOF
        print_success ".prettierignore 作成完了"
    fi

    # ========================================
    # .claudeignore_format (全フォーマッター共通除外)
    # ========================================

    if [ -f ".claudeignore_format" ]; then
        print_info ".claudeignore_format は既に存在します（スキップ）"
    else
        print_info ".claudeignore_format を作成中..."
        cat > .claudeignore_format << 'EOF'
# ============================================================================
# .claudeignore_format - フォーマット除外ファイルリスト
# ============================================================================
#
# このファイルに記載されたファイル/ディレクトリは、
# Edit/Write後のPostToolUse自動フォーマット対象外になります。
#
# パス形式: 絶対パスまたはプロジェクトルートからの相対パス
# 例: Stock/programs/legacy_module/old_script.py
# ============================================================================

# Archived projects (自動除外)
Archived/

# Flow drafts (自動除外)
Flow/

# Auto-generated files
scripts/auto_generated_*.py
scripts/auto_generated_*.js

# Legacy code (必要に応じて追加)
# Stock/programs/legacy_module/old_script.py

# Third-party vendored code
# vendor/
EOF
        print_success ".claudeignore_format 作成完了"
    fi
}

# ============================================================================
# 動作確認
# ============================================================================

verify_installation() {
    print_header "動作確認"

    cd "$PROJECT_ROOT"

    # テスト用一時ディレクトリ作成
    local temp_dir="$PROJECT_ROOT/.formatter_test_$$"
    mkdir -p "$temp_dir"

    print_info "サンプルファイルでフォーマットをテスト中..."

    # ========================================
    # black テスト
    # ========================================

    cat > "$temp_dir/test_black.py" << 'EOF'
def hello(  ):
    print("hello")
EOF

    if black "$temp_dir/test_black.py" &> /dev/null; then
        print_success "black 動作確認 OK"
    else
        print_error "black の動作確認に失敗"
    fi

    # ========================================
    # isort テスト
    # ========================================

    cat > "$temp_dir/test_isort.py" << 'EOF'
import os
import sys
from pathlib import Path
EOF

    if isort "$temp_dir/test_isort.py" &> /dev/null; then
        print_success "isort 動作確認 OK"
    else
        print_error "isort の動作確認に失敗"
    fi

    # ========================================
    # prettier テスト
    # ========================================

    cat > "$temp_dir/test_prettier.js" << 'EOF'
const hello = (  ) => {
  console.log("hello");
}
EOF

    if npx prettier --write "$temp_dir/test_prettier.js" &> /dev/null; then
        print_success "prettier 動作確認 OK (npx経由)"
    else
        print_warning "prettier の動作確認に失敗（必須ではないため続行）"
    fi

    # 一時ディレクトリ削除
    rm -rf "$temp_dir"
}

# ============================================================================
# 次のステップ案内
# ============================================================================

print_next_steps() {
    print_header "セットアップ完了"

    print_success "すべてのフォーマッタのインストールが完了しました"
    echo ""

    print_info "次のステップ:"
    echo ""
    echo -e "  ${GREEN}1.${NC} Claude Code の settings.json を設定"
    echo -e "     ${BLUE}パス:${NC} ~/.claude/settings.json"
    echo ""
    echo -e '     以下を追加:'
    echo -e '     {
       "hooks": {
         "PostToolUse": [
           {
             "matcher": "Edit|Write",
             "hooks": [
               {
                 "type": "command",
                 "command": "bash '"$PROJECT_ROOT"'/scripts/format_changed_file.sh \"$file_path\""
               }
             ]
           }
         ]
       }
     }'
    echo ""
    echo -e "  ${GREEN}2.${NC} フォーマット実行スクリプトを作成"
    echo -e "     ${BLUE}作成:${NC} scripts/format_changed_file.sh"
    echo -e "     ${BLUE}詳細:${NC} @docs/implementation_guides/week2_code_formatting.md 参照"
    echo ""
    echo -e "  ${GREEN}3.${NC} Claude Code でファイルを編集して自動フォーマットをテスト"
    echo ""

    print_info "設定の詳細は以下を参照:"
    echo -e "  ${BLUE}@docs/implementation_guides/week2_code_formatting.md${NC}"
    echo ""
}

# ============================================================================
# メイン実行
# ============================================================================

main() {
    print_header "aipm_v0 Formatter Setup"

    print_info "プロジェクトルート: $PROJECT_ROOT"
    echo ""

    # Homebrew 確認
    check_homebrew

    # フォーマッタインストール
    install_black
    install_isort
    check_prettier
    install_jq

    # 設定ファイル作成
    create_config_files

    # 動作確認
    verify_installation

    # 次のステップ案内
    print_next_steps
}

# スクリプト実行
main
