#!/bin/bash
#
# Update CLAUDE.md Script
# Week 8: Compounding Engineering週次CLAUDE.md更新スクリプト
#
# Usage:
#     bash scripts/update_claude_md.sh [--dry-run]
#
# Examples:
#     # 実際に更新
#     bash scripts/update_claude_md.sh
#
#     # ドライラン（確認のみ）
#     bash scripts/update_claude_md.sh --dry-run
#

set -euo pipefail

# ==================== 設定 ====================

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE_MD="${PROJECT_ROOT}/CLAUDE.md"
KNOWLEDGE_DIR="${PROJECT_ROOT}/.claude/knowledge"
REPORT_DIR="${PROJECT_ROOT}/reports/quality"

DRY_RUN=false

# ==================== 関数 ====================

log_info() {
    echo "[INFO] $*"
}

log_success() {
    echo "[✅] $*"
}

log_warning() {
    echo "[⚠️ ] $*"
}

log_error() {
    echo "[❌] $*" >&2
}

check_dependencies() {
    log_info "依存関係をチェック中..."

    if ! command -v jq &> /dev/null; then
        log_warning "jqがインストールされていません（JSONパース用）"
        log_info "インストール: brew install jq"
        return 1
    fi

    if [ ! -f "${CLAUDE_MD}" ]; then
        log_error "CLAUDE.mdが見つかりません: ${CLAUDE_MD}"
        return 1
    fi

    log_success "依存関係チェック完了"
    return 0
}

extract_best_practices() {
    log_info "ベストプラクティスを抽出中..."

    # 直近7日間の成功パターンを取得
    local success_files
    success_files=$(find "${KNOWLEDGE_DIR}/success_patterns" -name "success_*.json" -mtime -7 2>/dev/null | sort -r)

    if [ -z "$success_files" ]; then
        log_warning "直近7日間の成功パターンが見つかりません"
        return 0
    fi

    local best_practices=()

    while IFS= read -r file; do
        if [ -f "$file" ]; then
            log_info "  - $(basename "$file") を分析中..."

            # jqでbest_practices配列を抽出
            local practices
            practices=$(jq -r '.best_practices[]?' "$file" 2>/dev/null || echo "")

            if [ -n "$practices" ]; then
                while IFS= read -r practice; do
                    if [ -n "$practice" ]; then
                        best_practices+=("$practice")
                    fi
                done <<< "$practices"
            fi
        fi
    done <<< "$success_files"

    # 重複除去
    local unique_practices
    unique_practices=$(printf '%s\n' "${best_practices[@]}" | sort -u)

    log_success "抽出完了: $(echo "$unique_practices" | wc -l | tr -d ' ')件のベストプラクティス"

    # グローバル変数に格納
    EXTRACTED_PRACTICES="$unique_practices"
}

check_duplicates() {
    local new_practice="$1"

    # CLAUDE.md内に既に存在するかチェック
    if grep -qi "$new_practice" "${CLAUDE_MD}"; then
        return 0  # 重複あり
    fi

    return 1  # 重複なし
}

update_claude_md() {
    log_info "CLAUDE.mdを更新中..."

    if [ -z "${EXTRACTED_PRACTICES}" ]; then
        log_warning "追加するベストプラクティスがありません"
        return 0
    fi

    local today
    today=$(date +"%Y-%m-%d")

    local new_practices=()

    while IFS= read -r practice; do
        if [ -n "$practice" ]; then
            if check_duplicates "$practice"; then
                log_info "  - スキップ（重複）: $practice"
            else
                new_practices+=("$practice")
                log_info "  - 追加: $practice"
            fi
        fi
    done <<< "$EXTRACTED_PRACTICES"

    if [ ${#new_practices[@]} -eq 0 ]; then
        log_warning "重複を除外した結果、追加するベストプラクティスがありません"
        return 0
    fi

    if [ "$DRY_RUN" = true ]; then
        log_info "ドライランモード: 実際には更新しません"
        log_info "以下のベストプラクティスを追加予定:"
        printf '  - %s\n' "${new_practices[@]}"
        return 0
    fi

    # CLAUDE.mdに追記
    {
        echo ""
        echo ""
        echo "## Auto-Generated Best Practices ($today)"
        echo ""
        echo "The following best practices were extracted from weekly quality reports:"
        echo ""

        for practice in "${new_practices[@]}"; do
            echo "- $practice"
        done
    } >> "${CLAUDE_MD}"

    log_success "CLAUDE.mdに${#new_practices[@]}件のベストプラクティスを追加しました"

    # Git commit（オプション）
    if [ -n "${CLAUDE_CODE_AUTO_COMMIT:-}" ]; then
        log_info "Git commitを実行中..."
        git -C "${PROJECT_ROOT}" add "${CLAUDE_MD}"
        git -C "${PROJECT_ROOT}" commit -m "docs: Update CLAUDE.md with best practices from quality reports

🤖 Generated with Claude Code - Compounding Engineering

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
        log_success "Git commit完了"
    fi
}

cleanup_old_knowledge() {
    log_info "古いナレッジファイルをクリーンアップ中..."

    # 90日以上経過したファイルを削除
    local deleted_count=0

    for pattern_dir in "${KNOWLEDGE_DIR}/success_patterns" "${KNOWLEDGE_DIR}/failure_patterns"; do
        if [ -d "$pattern_dir" ]; then
            local old_files
            old_files=$(find "$pattern_dir" -name "*.json" -mtime +90 2>/dev/null || echo "")

            if [ -n "$old_files" ]; then
                while IFS= read -r file; do
                    if [ -f "$file" ]; then
                        if [ "$DRY_RUN" = true ]; then
                            log_info "  - 削除予定: $(basename "$file")"
                        else
                            rm -f "$file"
                            log_info "  - 削除: $(basename "$file")"
                        fi
                        deleted_count=$((deleted_count + 1))
                    fi
                done <<< "$old_files"
            fi
        fi
    done

    if [ $deleted_count -eq 0 ]; then
        log_info "削除対象のファイルはありません"
    else
        log_success "${deleted_count}件のファイルをクリーンアップ"
    fi
}

generate_summary() {
    log_info "サマリーレポートを生成中..."

    local success_count
    local failure_count

    success_count=$(find "${KNOWLEDGE_DIR}/success_patterns" -name "success_*.json" -mtime -30 2>/dev/null | wc -l | tr -d ' ')
    failure_count=$(find "${KNOWLEDGE_DIR}/failure_patterns" -name "failure_*.json" -mtime -30 2>/dev/null | wc -l | tr -d ' ')

    echo ""
    echo "==================== サマリー ===================="
    echo "直近30日間のナレッジ蓄積状況:"
    echo "  - 成功パターン: ${success_count}件"
    echo "  - 失敗パターン: ${failure_count}件"
    echo "=================================================="
    echo ""
}

# ==================== メイン処理 ====================

main() {
    log_info "CLAUDE.md週次更新スクリプトを開始します"
    log_info "プロジェクトルート: ${PROJECT_ROOT}"
    echo ""

    # 引数解析
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                DRY_RUN=true
                log_info "ドライランモード: 実際には変更を行いません"
                shift
                ;;
            *)
                log_error "不明なオプション: $1"
                echo "Usage: $0 [--dry-run]"
                exit 1
                ;;
        esac
    done

    # Step 1: 依存関係チェック
    if ! check_dependencies; then
        exit 1
    fi

    echo ""

    # Step 2: ベストプラクティス抽出
    extract_best_practices

    echo ""

    # Step 3: CLAUDE.md更新
    update_claude_md

    echo ""

    # Step 4: 古いナレッジクリーンアップ
    cleanup_old_knowledge

    echo ""

    # Step 5: サマリー表示
    generate_summary

    log_success "CLAUDE.md週次更新が完了しました"
}

# エントリポイント
main "$@"
