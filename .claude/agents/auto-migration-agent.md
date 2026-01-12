# Auto Migration Agent - Flow→Stock 自動移行エージェント仕様書

## 役割と目的

**役割**: Completion Judge Agentから渡されたメタデータJSONを基に、FlowディレクトリからStockディレクトリへドキュメントを安全に移行する。

**目的**:
- Git バックアップを自動作成し、ロールバック可能な状態を保証
- PMBOK構造に準拠したパスへ自動配置
- 既存ファイルとのコンフリクトを検出し、バージョン管理で退避
- 並列実行対応（5 worktrees × 5タスク = 25並列）

**実行モデル**: `sonnet`（標準分析、15分タイムアウト）

**入力**: Phase 2（Completion Judge Agent）が生成したメタデータJSON

**出力**:
- 移行されたStockファイル
- Gitタグ（pre-confirm-YYYYMMDD-HHMMSS形式）
- 移行ログ（migration_log.txt）
- コンフリクト検出時のバージョン退避ファイル（_versions/）

---

## アーキテクチャ概要

### フロー図

```
[Phase 2 Output]
    ↓ metadata.json
[Auto Migration Agent]
    ↓
[1. Git Backup]
    ↓ pre-confirm-20260110-143000
[2. Path Resolution]
    ↓ Stock/programs/{project_id}/documents/{phase}/{doc_type}.md
[3. Conflict Detection]
    ↓ 既存ファイルあり？
    ├─ YES → _versions/ へ退避
    └─ NO  → 直接コピー
[4. Migration Execution]
    ↓
[5. Verification]
    ↓ 移行成功確認
[Stock File]
```

### 主要コンポーネント

| コンポーネント | 役割 | 実装場所 |
|--------------|------|---------|
| **Git Backup Manager** | pre-confirm タグ作成・管理 | flow_to_stock_v2.sh |
| **Path Resolver** | PMBOK構造準拠パス生成 | flow_to_stock_v2.sh |
| **Conflict Detector** | 既存ファイル検出・退避 | flow_to_stock_v2.sh |
| **Rollback Manager** | Gitタグからの復元 | flow_to_stock_v2.sh |
| **Migration Logger** | 全操作のログ記録 | flow_to_stock_v2.sh |

---

## 1. Git Backup Manager

### 機能概要

移行実行前に自動的にGitタグを作成し、いつでもロールバック可能な状態を保証します。

### タグ命名規則

```
pre-confirm-YYYYMMDD-HHMMSS
```

**例**:
- `pre-confirm-20260110-143000`
- `pre-confirm-20260110-150530`

### 実装仕様（Bash）

```bash
#!/bin/bash

# Gitバックアップ作成関数
create_git_backup() {
    local flow_file="$1"
    local tag_name="pre-confirm-$(date +%Y%m%d-%H%M%S)"
    local commit_message="Backup before auto-migration: $(basename "$flow_file")"

    # 現在の状態をコミット（未コミット変更がある場合）
    if ! git diff-index --quiet HEAD --; then
        git add -A
        git commit -m "Auto-save before migration: $(date +%Y-%m-%d\ %H:%M:%S)"
    fi

    # アノテーテッドタグ作成（メッセージ付き）
    git tag -a "$tag_name" -m "$commit_message"

    # リモートにプッシュ（オプション、設定で制御）
    if [[ "${PUSH_BACKUP_TAGS:-false}" == "true" ]]; then
        git push origin "$tag_name"
        echo "✅ Backup tag pushed to remote: $tag_name" >&2
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
```

### 使用例

```bash
# 移行前にバックアップ作成
backup_tag=$(create_git_backup "Flow/202601/2026-01-10/project_charter.md")
echo "Backup tag: $backup_tag"
# → Backup tag: pre-confirm-20260110-143000

# 全バックアップタグ表示
list_backup_tags
# → pre-confirm-20260110-143000
# → pre-confirm-20260110-120000
# → pre-confirm-20260109-180000

# 最新バックアップタグ取得
latest_tag=$(get_latest_backup_tag)
echo "Latest backup: $latest_tag"
# → Latest backup: pre-confirm-20260110-143000
```

### エラーハンドリング

```bash
create_git_backup() {
    # ...

    # Gitリポジトリ確認
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo "[ERROR] Not a git repository" >&2
        return 1
    fi

    # タグ作成失敗時
    if ! git tag -a "$tag_name" -m "$commit_message" 2>/dev/null; then
        echo "[ERROR] Failed to create backup tag: $tag_name" >&2
        return 1
    fi

    # プッシュ失敗時（警告のみ、処理継続）
    if [[ "${PUSH_BACKUP_TAGS:-false}" == "true" ]]; then
        if ! git push origin "$tag_name" 2>/dev/null; then
            echo "[WARN] Failed to push backup tag to remote: $tag_name" >&2
            echo "[WARN] Tag created locally but not pushed" >&2
        fi
    fi

    echo "$tag_name"
}
```

---

## 2. Path Resolver - PMBOK構造準拠パス生成

### 機能概要

Phase 2から渡されたメタデータJSON（pmbok_phase, document_type, project_id）を基に、Stock配置先パスを自動生成します。

### パス構造規則

```
Stock/programs/{project_id}/documents/{pmbok_phase}/{document_type}.md
```

**PMBOK Phaseのディレクトリ名変換**:
- `Initiating` → `initiating`
- `Discovery` → `discovery`
- `Research` → `research`
- `Planning` → `planning`
- `Executing` → `executing`
- `Monitoring` → `monitoring`
- `Closing` → `closing`

### 実装仕様（Bash）

```bash
#!/bin/bash

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
```

### 使用例

```bash
# メタデータJSONからパス解決
metadata_file="Flow/202601/2026-01-10/metadata_project_charter.json"
stock_path=$(resolve_stock_path "$metadata_file")
echo "Stock path: $stock_path"
# → Stock path: Stock/programs/aipm-v3-project/documents/initiating/project_charter.md

# プロジェクトディレクトリ作成
ensure_project_directories "aipm-v3-project" "Initiating"
# → ✅ Created directory: Stock/programs/aipm-v3-project/documents/initiating
# → ✅ Created version directory: Stock/programs/aipm-v3-project/documents/initiating/_versions
```

### パス検証

```bash
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
```

---

## 3. Conflict Detector - コンフリクト検出・バージョン管理

### 機能概要

Stock配置先に既存ファイルが存在する場合、既存ファイルを `_versions/` ディレクトリに退避してから新規ファイルを配置します。

### バージョンディレクトリ構造

```
Stock/programs/aipm-v3-project/documents/initiating/
├── project_charter.md              # 最新版（現在配置されているファイル）
└── _versions/
    ├── project_charter_20260110_120000.md  # 前回バージョン
    ├── project_charter_20260109_180000.md  # 前々回バージョン
    └── project_charter_20260109_150000.md  # さらに前のバージョン
```

### 実装仕様（Bash）

```bash
#!/bin/bash

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
```

### 使用例

```bash
# コンフリクト検出・処理
flow_file="Flow/202601/2026-01-10/project_charter.md"
stock_file="Stock/programs/aipm-v3-project/documents/initiating/project_charter.md"

handle_conflict "$stock_file" "$flow_file"
# → ⚠️  Conflict detected. Existing file found: Stock/.../project_charter.md
# → ✅ Old version saved: project_charter_20260110_143000.md
# → ✅ New file copied: Stock/.../project_charter.md

# バージョン履歴表示
list_versions "$stock_file"
# → Version history for: Stock/.../project_charter.md
# → ---
# →   - project_charter_20260110_143000.md (Size: 5.2K, Modified: 2026-01-10 14:30:00)
# →   - project_charter_20260110_120000.md (Size: 4.8K, Modified: 2026-01-10 12:00:00)

# 特定バージョンの復元
restore_version "$stock_file" "20260110_120000"
# → ⚠️  Conflict detected. Existing file found: ...
# → ✅ Old version saved: project_charter_20260110_143500.md
# → ✅ New file copied: ...
# → ✅ Restored version: 20260110_120000
```

---

## 4. Rollback Manager - ロールバック機能

### 機能概要

移行失敗時や誤操作時に、Gitタグから以前の状態に復元します。

### 実装仕様（Bash）

```bash
#!/bin/bash

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
```

### 使用例

```bash
# ロールバック候補一覧表示
list_rollback_candidates
# → Available backup tags for rollback:
# → ---
# →   - pre-confirm-20260110-143000
# →     Date: 20260110 143000
# →     Message: Backup before auto-migration: project_charter.md
# →
# →   - pre-confirm-20260110-120000
# →     Date: 20260110 120000
# →     Message: Backup before auto-migration: wbs.md

# 特定タグへのロールバック
rollback_migration "pre-confirm-20260110-120000"
# → [WARN] You have uncommitted changes. Stashing them...
# → 🔄 Rolled back to: pre-confirm-20260110-120000
# → ✅ Created recovery branch: recovery-20260110-144000
# → [INFO] To apply rollback to main branch:
# →   git checkout main
# →   git merge recovery-20260110-144000

# 最新バックアップへのロールバック
rollback_to_latest
# → Rolling back to latest backup: pre-confirm-20260110-143000
# → 🔄 Rolled back to: pre-confirm-20260110-143000
# → ✅ Created recovery branch: recovery-20260110-144100
```

---

## 5. Migration Logger - 移行ログ記録

### 機能概要

全移行操作をタイムスタンプ付きでログファイルに記録します。

### ログファイル構造

```
logs/
└── migration_YYYYMMDD_HHMMSS/
    ├── migration_log.txt          # 全体ログ
    ├── backup_tag.txt             # 使用したバックアップタグ
    ├── metadata_input.json        # 入力メタデータJSON
    ├── conflict_detected.txt      # コンフリクト検出リスト（ある場合）
    └── success.txt または error.txt  # 最終ステータス
```

### 実装仕様（Bash）

```bash
#!/bin/bash

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
```

### 使用例

```bash
# ログ初期化
log_dir=$(init_migration_log)
echo "Log directory: $log_dir"
# → Log directory: logs/migration_20260110_143000

# 各種ログ記録
log_migration "INFO" "Migration started"
record_backup_tag "pre-confirm-20260110-143000"
record_metadata_input "Flow/202601/2026-01-10/metadata_project_charter.json"
record_conflict "Stock/.../project_charter.md" "_versions/project_charter_20260110_143000.md"
record_final_status "success" "Migration completed successfully"

# ログファイル内容確認
cat "${log_dir}/migration_log.txt"
# → [2026-01-10 14:30:00] [INFO] Migration started
# → [2026-01-10 14:30:01] [INFO] Backup tag recorded: pre-confirm-20260110-143000
# → [2026-01-10 14:30:02] [INFO] Metadata input recorded: ...
# → [2026-01-10 14:30:05] [WARN] Conflict detected: Stock/.../project_charter.md
# → [2026-01-10 14:30:10] [SUCCESS] Migration completed successfully
```

---

## 統合実行フロー

### メイン処理（flow_to_stock_v2.sh）

```bash
#!/bin/bash
# flow_to_stock_v2.sh - Flow→Stock自動移行スクリプト v2

set -euo pipefail

# 設定
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
readonly PUSH_BACKUP_TAGS="${PUSH_BACKUP_TAGS:-false}"

# ログ初期化
log_dir=$(init_migration_log)
cd "$PROJECT_ROOT"

# メイン関数
main() {
    local metadata_json="$1"

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

# メイン実行
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <metadata_json_path>" >&2
    exit 1
fi

main "$1"
```

---

## 成功基準

Week 3-4の成功基準:

### 1. Gitバックアップ100%成功
- [ ] pre-confirm-YYYYMMDD-HHMMSS タグが全移行で作成される
- [ ] タグにアノテーテッドメッセージが含まれる
- [ ] タグからロールバック可能

### 2. コンフリクト検出100%
- [ ] 既存ファイルが100%検出される
- [ ] 全ての既存ファイルが _versions/ に退避される
- [ ] タイムスタンプ付きバージョン名で保存される

### 3. ロールバック機能100%成功
- [ ] 任意のバックアップタグから復元可能
- [ ] 復元後にrecoveryブランチが作成される
- [ ] 未コミット変更は自動stash

### 4. 並列実行（5 worktrees）で正常動作
- [ ] 5つの異なるworktreeで同時実行可能
- [ ] Git操作の競合が発生しない
- [ ] ログファイルが重複なく記録される

---

## テストシナリオ

### テストケース1: 正常移行（コンフリクトなし）

```bash
# 初回移行
metadata_json="Flow/202601/2026-01-10/metadata_project_charter.json"
backup_tag=$(bash scripts/flow_to_stock_v2.sh "$metadata_json")

# 検証
[[ -f "Stock/programs/aipm-v3-project/documents/initiating/project_charter.md" ]]
git tag -l | grep "$backup_tag"
```

### テストケース2: コンフリクト検出・バージョン管理

```bash
# 2回目移行（既存ファイルあり）
metadata_json="Flow/202601/2026-01-10/metadata_project_charter_v2.json"
bash scripts/flow_to_stock_v2.sh "$metadata_json"

# 検証
[[ -d "Stock/programs/aipm-v3-project/documents/initiating/_versions" ]]
ls -la "Stock/programs/aipm-v3-project/documents/initiating/_versions/" | grep "project_charter_"
```

### テストケース3: ロールバック

```bash
# ロールバック実行
rollback_migration "$backup_tag"

# 検証
git branch -l | grep "recovery-"
git diff "$backup_tag" HEAD  # 差分なし
```

### テストケース4: 並列実行

```bash
# 5つのworktreeで同時実行
for wt in worktrees/feature-{1..5}/aipm_v0; do
    (cd "$wt" && bash scripts/flow_to_stock_v2.sh "metadata_test.json") &
done
wait

# 検証: 全てのバックアップタグ作成確認
git tag -l "pre-confirm-*" | wc -l  # 5個以上
```

---

## エラーハンドリング

| エラーケース | 検出方法 | 対応 |
|------------|---------|------|
| **Gitリポジトリ未初期化** | `git rev-parse --git-dir` | エラー終了、ログ記録 |
| **メタデータJSON不正** | `jq` パースエラー | エラー終了、ログ記録 |
| **必須フィールド欠損** | `jq -r '.field'` が null | エラー終了、ログ記録 |
| **Flowファイル不存在** | `[[ -f "$flow_file" ]]` | エラー終了、ログ記録 |
| **Stock パス不正** | `validate_stock_path` | エラー終了、ログ記録 |
| **タグ作成失敗** | `git tag` exit code | エラー終了、ロールバック不可警告 |
| **ファイルコピー失敗** | `cp` exit code | エラー終了、ロールバック推奨 |
| **並列実行時のGit競合** | Git lock file検出 | リトライ（最大3回）、失敗時エラー |

---

## 次フェーズへの引き継ぎ

### Phase 4（Week 5-6）への出力

Auto Migration Agentは以下をPhase 4（Quality Assurance）に引き渡します：

```json
{
  "migration_status": "success",
  "stock_file_path": "Stock/programs/aipm-v3-project/documents/initiating/project_charter.md",
  "backup_tag": "pre-confirm-20260110-143000",
  "log_directory": "logs/migration_20260110_143000",
  "conflict_detected": true,
  "version_file": "Stock/.../documents/initiating/_versions/project_charter_20260110_143000.md"
}
```

Phase 4はこの情報を基に、Stock配置後のドキュメント品質を再評価します（Review Agent）。

---

## 参照

- Phase 2仕様: @.claude/agents/completion-judge-agent.md
- Phase 4仕様: @.claude/agents/review-agent.md（既存502行）
- Phase 3実装計画: @/Users/yuichi/.claude/plans/zippy-yawning-lightning.md (Week 3-4)
- Week 3並列実行: @.claude/rules/parallel_execution_terminal.md
- Week 4 Worktrees: @.claude/rules/parallel_execution_worktrees.md
