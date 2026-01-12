#!/bin/bash
# flow_to_stock_v2.sh - Flow→Stock自動移行スクリプト v2
# Auto Migration Agent メイン実行スクリプト

set -euo pipefail

# ========================================
# 設定
# ========================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PROJECT_ROOT:-$(cd "${SCRIPT_DIR}/.." && pwd)}"  # 環境変数でオーバーライド可能
echo "[DEBUG] PROJECT_ROOT set to: $PROJECT_ROOT" >&2
readonly PUSH_BACKUP_TAGS="${PUSH_BACKUP_TAGS:-false}"

# ========================================
# 1. Git Backup Manager
# ========================================

# Gitバックアップ作成関数
create_git_backup() {
    local flow_file="$1"
    local tag_name="pre-confirm-$(date +%Y%m%d-%H%M%S)"
    local commit_message="Backup before auto-migration: $(basename "$flow_file")"

    # Gitリポジトリ確認
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo "[ERROR] Not a git repository" >&2
        return 1
    fi

    # 現在の状態をコミット（未コミット変更がある場合）
    if ! git diff-index --quiet HEAD --; then
        git add -A
        git commit -m "Auto-save before migration: $(date +%Y-%m-%d\ %H:%M:%S)"
    fi

    # アノテーテッドタグ作成（メッセージ付き）
    if ! git tag -a "$tag_name" -m "$commit_message" 2>/dev/null; then
        echo "[ERROR] Failed to create backup tag: $tag_name" >&2
        return 1
    fi

    # リモートにプッシュ（オプション、設定で制御）
    if [[ "${PUSH_BACKUP_TAGS:-false}" == "true" ]]; then
        if ! git push origin "$tag_name" 2>/dev/null; then
            echo "[WARN] Failed to push backup tag to remote: $tag_name" >&2
            echo "[WARN] Tag created locally but not pushed" >&2
        else
            echo "✅ Backup tag pushed to remote: $tag_name" >&2
        fi
    fi

    echo "✅ Backup created: $tag_name" >&2
    echo "$tag_name"  # 関数戻り値として返す
}

# バックアップタグ一覧取得
list_backup_tags() {
    git tag -l "pre-confirm-*" --sort=-creatordate
}

# 最新バックアップタグ取得
get_latest_backup_tag() {
    git tag -l "pre-confirm-*" --sort=-creatordate | head -n 1
}

# ========================================
# 2. Path Resolver
# ========================================

# パス解決関数
resolve_stock_path() {
    local metadata_json_path="$1"

    # メタデータJSON読み込み
    if ! [[ -f "$metadata_json_path" ]]; then
        echo "[ERROR] Metadata JSON not found: $metadata_json_path" >&2
        return 1
    fi

    local pmbok_phase=$(jq -r '.pmbok_phase' "$metadata_json_path")
    local doc_type=$(jq -r '.document_type' "$metadata_json_path")
    local project_id=$(jq -r '.project_id' "$metadata_json_path")

    # 必須フィールド検証
    if [[ -z "$pmbok_phase" || "$pmbok_phase" == "null" ]]; then
        echo "[ERROR] Missing required field: pmbok_phase" >&2
        return 1
    fi
    if [[ -z "$doc_type" || "$doc_type" == "null" ]]; then
        echo "[ERROR] Missing required field: document_type" >&2
        return 1
    fi
    if [[ -z "$project_id" || "$project_id" == "null" ]]; then
        echo "[ERROR] Missing required field: project_id" >&2
        return 1
    fi

    # Phase名を小文字に変換
    local phase_dir=$(echo "$pmbok_phase" | tr '[:upper:]' '[:lower:]')

    # Stockパス生成
    local stock_path="Stock/programs/${project_id}/documents/${phase_dir}/${doc_type}.md"

    echo "$stock_path"
}

# プロジェクトディレクトリ作成
ensure_project_directories() {
    local project_id="$1"
    local pmbok_phase="$2"

    local phase_dir=$(echo "$pmbok_phase" | tr '[:upper:]' '[:lower:]')
    local target_dir="Stock/programs/${project_id}/documents/${phase_dir}"

    # ディレクトリが存在しない場合のみ作成
    if [[ ! -d "$target_dir" ]]; then
        mkdir -p "$target_dir"
        echo "✅ Created directory: $target_dir" >&2
    fi

    # バージョン管理ディレクトリも作成
    local version_dir="${target_dir}/_versions"
    if [[ ! -d "$version_dir" ]]; then
        mkdir -p "$version_dir"
        echo "✅ Created version directory: $version_dir" >&2
    fi
}

# パス検証
validate_stock_path() {
    local stock_path="$1"

    # パス形式検証（正規表現）
    if ! [[ "$stock_path" =~ ^Stock/programs/[^/]+/documents/(initiating|discovery|research|planning|executing|monitoring|closing)/[^/]+\.md$ ]]; then
        echo "[ERROR] Invalid stock path format: $stock_path" >&2
        return 1
    fi

    # プロジェクトID抽出
    local project_id=$(echo "$stock_path" | sed -E 's|Stock/programs/([^/]+)/.*|\1|')

    # プロジェクトID有効性チェック（英数字、ハイフン、アンダースコアのみ）
    if ! [[ "$project_id" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        echo "[ERROR] Invalid project_id format: $project_id" >&2
        return 1
    fi

    echo "✅ Stock path validation passed: $stock_path" >&2
    return 0
}

# ========================================
# 3. Conflict Detector
# ========================================

# コンフリクト検出・処理関数
handle_conflict() {
    local target_path="$1"
    local flow_file="$2"

    # 既存ファイルが存在しない場合、直接コピー
    if [[ ! -f "$target_path" ]]; then
        cp "$flow_file" "$target_path"
        echo "✅ No conflict. File copied: $target_path" >&2
        return 0
    fi

    # 既存ファイルあり → バージョン管理
    echo "⚠️  Conflict detected. Existing file found: $target_path" >&2

    local version_dir="$(dirname "$target_path")/_versions"
    mkdir -p "$version_dir"

    local timestamp=$(date +%Y%m%d_%H%M%S)
    local filename=$(basename "$target_path" .md)
    local backup_name="${filename}_${timestamp}.md"
    local backup_path="${version_dir}/${backup_name}"

    # 既存ファイルをバージョンディレクトリへ退避
    mv "$target_path" "$backup_path"
    echo "✅ Old version saved: ${backup_name}" >&2

    # Flowファイルをコピー
    cp "$flow_file" "$target_path"
    echo "✅ New file copied: $target_path" >&2

    return 0
}

# バージョン履歴一覧表示
list_versions() {
    local stock_file="$1"
    local version_dir="$(dirname "$stock_file")/_versions"
    local filename=$(basename "$stock_file" .md)

    if [[ ! -d "$version_dir" ]]; then
        echo "[INFO] No version history found" >&2
        return 0
    fi

    echo "Version history for: $stock_file" >&2
    echo "---" >&2

    # タイムスタンプ降順でソート
    find "$version_dir" -type f -name "${filename}_*.md" | sort -r | while read version_file; do
        local version_name=$(basename "$version_file")
        local file_size=$(du -h "$version_file" | cut -f1)
        local mod_time=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$version_file" 2>/dev/null || stat -c "%y" "$version_file" 2>/dev/null | cut -d'.' -f1)

        echo "  - $version_name (Size: $file_size, Modified: $mod_time)" >&2
    done
}

# 特定バージョンの復元
restore_version() {
    local stock_file="$1"
    local version_timestamp="$2"  # 例: 20260110_120000

    local version_dir="$(dirname "$stock_file")/_versions"
    local filename=$(basename "$stock_file" .md)
    local version_file="${version_dir}/${filename}_${version_timestamp}.md"

    if [[ ! -f "$version_file" ]]; then
        echo "[ERROR] Version not found: $version_file" >&2
        return 1
    fi

    # 現在のファイルをバージョン管理（復元前に退避）
    handle_conflict "$stock_file" "$version_file"

    echo "✅ Restored version: $version_timestamp" >&2
    return 0
}

# ========================================
# 4. Rollback Manager
# ========================================

# ロールバック実行関数
rollback_migration() {
    local tag_name="$1"

    # タグ存在確認
    if ! git rev-parse "$tag_name" >/dev/null 2>&1; then
        echo "[ERROR] Backup tag not found: $tag_name" >&2
        return 1
    fi

    # 現在の変更を確認
    if ! git diff-index --quiet HEAD --; then
        echo "[WARN] You have uncommitted changes. Stashing them..." >&2
        git stash push -m "Auto-stash before rollback: $(date +%Y-%m-%d\ %H:%M:%S)"
    fi

    # タグにチェックアウト（detached HEAD状態）
    git checkout "$tag_name"

    # Detached HEAD状態を解消（新しいブランチ作成）
    local recovery_branch="recovery-$(date +%Y%m%d-%H%M%S)"
    git checkout -b "$recovery_branch"

    echo "🔄 Rolled back to: $tag_name" >&2
    echo "✅ Created recovery branch: $recovery_branch" >&2

    # mainブランチにマージするか確認が必要（Human-in-the-Loop）
    echo "[INFO] To apply rollback to main branch:" >&2
    echo "  git checkout main" >&2
    echo "  git merge $recovery_branch" >&2

    return 0
}

# ロールバック候補タグ一覧
list_rollback_candidates() {
    echo "Available backup tags for rollback:" >&2
    echo "---" >&2

    git tag -l "pre-confirm-*" --sort=-creatordate | head -n 10 | while read tag_name; do
        local tag_date=$(echo "$tag_name" | sed -E 's/pre-confirm-([0-9]{8})-([0-9]{6})/\1 \2/')
        local tag_message=$(git tag -l --format='%(contents)' "$tag_name" | head -n 1)

        echo "  - $tag_name" >&2
        echo "    Date: $tag_date" >&2
        echo "    Message: $tag_message" >&2
        echo "" >&2
    done
}

# 最新バックアップへのロールバック（ショートカット）
rollback_to_latest() {
    local latest_tag=$(get_latest_backup_tag)

    if [[ -z "$latest_tag" ]]; then
        echo "[ERROR] No backup tags found" >&2
        return 1
    fi

    echo "Rolling back to latest backup: $latest_tag" >&2
    rollback_migration "$latest_tag"
}

# ========================================
# 5. Migration Logger
# ========================================

# ログディレクトリ初期化
init_migration_log() {
    local log_dir="logs/migration_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$log_dir"

    echo "$log_dir" > /tmp/current_migration_log_dir.txt
    echo "$log_dir"
}

# ログ出力関数
log_migration() {
    local level="$1"  # INFO, WARN, ERROR, SUCCESS
    local message="$2"

    local log_dir=$(cat /tmp/current_migration_log_dir.txt 2>/dev/null || echo "logs/migration_$(date +%Y%m%d_%H%M%S)")
    local log_file="${log_dir}/migration_log.txt"

    # ログディレクトリが存在しない場合は作成
    mkdir -p "$log_dir"

    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[${timestamp}] [${level}] ${message}" | tee -a "$log_file" >&2
}

# バックアップタグ記録
record_backup_tag() {
    local tag_name="$1"
    local log_dir=$(cat /tmp/current_migration_log_dir.txt)

    echo "$tag_name" > "${log_dir}/backup_tag.txt"
    log_migration "INFO" "Backup tag recorded: $tag_name"
}

# メタデータJSON記録
record_metadata_input() {
    local metadata_json_path="$1"
    local log_dir=$(cat /tmp/current_migration_log_dir.txt)

    cp "$metadata_json_path" "${log_dir}/metadata_input.json"
    log_migration "INFO" "Metadata input recorded: $metadata_json_path"
}

# コンフリクト記録
record_conflict() {
    local stock_file="$1"
    local version_file="$2"
    local log_dir=$(cat /tmp/current_migration_log_dir.txt)

    echo "Conflict: $stock_file → $version_file" >> "${log_dir}/conflict_detected.txt"
    log_migration "WARN" "Conflict detected: $stock_file"
}

# 最終ステータス記録
record_final_status() {
    local status="$1"  # success or error
    local message="$2"
    local log_dir=$(cat /tmp/current_migration_log_dir.txt)

    if [[ "$status" == "success" ]]; then
        echo "$message" > "${log_dir}/success.txt"
        log_migration "SUCCESS" "$message"
    else
        echo "$message" > "${log_dir}/error.txt"
        log_migration "ERROR" "$message"
    fi
}

# ========================================
# メイン処理
# ========================================

main() {
    local metadata_json="$1"

    # メタデータJSONパスを絶対パスに変換（相対パスの場合）
    if [[ ! "$metadata_json" =~ ^/ ]]; then
        metadata_json="$(pwd)/$metadata_json"
    fi

    log_migration "INFO" "=== Auto Migration Started ==="
    log_migration "INFO" "Metadata JSON: $metadata_json"

    # 移行適格性チェック
    local migration_eligible=$(jq -r '.migration_eligible' "$metadata_json")
    if [[ "$migration_eligible" != "true" ]]; then
        record_final_status "error" "Migration not eligible (completion_score < 70)"
        exit 1
    fi

    # 必須フィールド取得
    local flow_file=$(jq -r '.file_path' "$metadata_json")
    local pmbok_phase=$(jq -r '.pmbok_phase' "$metadata_json")
    local doc_type=$(jq -r '.document_type' "$metadata_json")
    local project_id=$(jq -r '.project_id' "$metadata_json")

    # Flow fileパスも絶対パスに変換（相対パスの場合）
    # メタデータJSONの場所を基準に解決（テストワークスペース対応）
    if [[ ! "$flow_file" =~ ^/ ]]; then
        local metadata_dir=$(dirname "$metadata_json")
        local workspace_root=$(cd "$metadata_dir/../../.." && pwd)
        flow_file="$workspace_root/$flow_file"
    fi

    log_migration "INFO" "Flow file: $flow_file"
    log_migration "INFO" "PMBOK Phase: $pmbok_phase"
    log_migration "INFO" "Document type: $doc_type"
    log_migration "INFO" "Project ID: $project_id"

    # Step 1: Gitバックアップ作成
    log_migration "INFO" "Step 1: Creating Git backup..."
    local backup_tag=$(create_git_backup "$flow_file")
    record_backup_tag "$backup_tag"

    # Step 2: パス解決
    log_migration "INFO" "Step 2: Resolving Stock path..."
    local stock_path=$(resolve_stock_path "$metadata_json")
    log_migration "INFO" "Stock path: $stock_path"

    # パス検証
    if ! validate_stock_path "$stock_path"; then
        record_final_status "error" "Invalid stock path: $stock_path"
        exit 1
    fi

    # Step 3: プロジェクトディレクトリ作成
    log_migration "INFO" "Step 3: Ensuring project directories..."
    ensure_project_directories "$project_id" "$pmbok_phase"

    # Step 4: コンフリクト検出・処理
    log_migration "INFO" "Step 4: Handling conflicts..."
    if [[ -f "$stock_path" ]]; then
        local version_dir="$(dirname "$stock_path")/_versions"
        local timestamp=$(date +%Y%m%d_%H%M%S)
        local filename=$(basename "$stock_path" .md)
        local backup_name="${filename}_${timestamp}.md"

        record_conflict "$stock_path" "${version_dir}/${backup_name}"
    fi

    handle_conflict "$stock_path" "$flow_file"

    # Step 5: 移行完了検証
    log_migration "INFO" "Step 5: Verifying migration..."
    if [[ ! -f "$stock_path" ]]; then
        record_final_status "error" "Migration failed: Stock file not found: $stock_path"
        exit 1
    fi

    # メタデータ記録
    record_metadata_input "$metadata_json"

    # 成功
    record_final_status "success" "Migration completed successfully: $stock_path"
    log_migration "INFO" "=== Auto Migration Completed ==="

    # バックアップタグを返す（ロールバック用）
    echo "$backup_tag"
}

# ========================================
# エントリーポイント
# ========================================

# ログ初期化
log_dir=$(init_migration_log)

# メイン実行
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <metadata_json_path>" >&2
    echo "" >&2
    echo "Example:" >&2
    echo "  $0 Flow/202601/2026-01-10/metadata_project_charter.json" >&2
    exit 1
fi

# メタデータJSONパスを絶対パスに変換（cd $PROJECT_ROOT の前に実行）
metadata_json_arg="$1"
if [[ ! "$metadata_json_arg" =~ ^/ ]]; then
    metadata_json_arg="$(pwd)/$metadata_json_arg"
fi

cd "$PROJECT_ROOT"
echo "[DEBUG] Current directory after cd: $(pwd)" >&2

main "$metadata_json_arg"
