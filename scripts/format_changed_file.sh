#!/bin/bash
#
# format_changed_file.sh
# PostToolUse Hook for automatic code formatting
#
# Usage: format_changed_file.sh <file_path>
#
# Environment Variables:
#   CLAUDE_AUTO_FORMAT=false  - Disable auto-formatting
#   CLAUDE_FORMAT_LOG=true    - Enable detailed logging
#
# Exit Codes:
#   Always exits 0 to prevent Claude Code interruption
#

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

readonly SCRIPT_NAME="$(basename "$0")"
readonly LOG_DIR="${HOME}/.claude/logs"
readonly LOG_FILE="${LOG_DIR}/format.log"
readonly FORMATTER_TIMEOUT=5
readonly IGNORE_FILE=".claudeignore_format"

# ============================================================================
# Logging Functions
# ============================================================================

log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

    if [[ "${CLAUDE_FORMAT_LOG:-false}" == "true" ]]; then
        mkdir -p "${LOG_DIR}"
        echo "[${timestamp}] [${level}] ${message}" | tee -a "${LOG_FILE}" >&2
    elif [[ "${level}" == "ERROR" ]] || [[ "${level}" == "WARN" ]]; then
        echo "[${level}] ${message}" >&2
    fi
}

# ============================================================================
# Validation Functions
# ============================================================================

check_environment() {
    if [[ "${CLAUDE_AUTO_FORMAT:-true}" == "false" ]]; then
        log "INFO" "Auto-formatting disabled via CLAUDE_AUTO_FORMAT=false"
        exit 0
    fi
}

validate_file() {
    local file="$1"

    if [[ -z "${file}" ]]; then
        log "ERROR" "No file path provided"
        exit 0
    fi

    if [[ ! -f "${file}" ]]; then
        log "WARN" "File does not exist: ${file}"
        exit 0
    fi

    if [[ ! -r "${file}" ]]; then
        log "ERROR" "File is not readable: ${file}"
        exit 0
    fi
}

is_ignored() {
    local file="$1"

    # スクリプトのディレクトリから1つ上がプロジェクトルート
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local project_root="$(cd "${script_dir}/.." && pwd)"
    local ignore_file="${project_root}/${IGNORE_FILE}"

    log "INFO" "Project root: ${project_root}"
    log "INFO" "Checking ignore file: ${ignore_file}"

    if [[ ! -f "${ignore_file}" ]]; then
        log "INFO" "Ignore file not found: ${ignore_file}"
        return 1
    fi

    local pattern_count=0
    while IFS= read -r pattern; do
        # Skip empty lines and comments
        [[ -z "${pattern}" ]] && continue
        [[ "${pattern}" =~ ^[[:space:]]*# ]] && continue

        # パターンからスペースを除去
        pattern=$(echo "${pattern}" | xargs)
        pattern_count=$((pattern_count + 1))

        log "INFO" "Testing pattern #${pattern_count}: '${pattern}' against '${file}'"

        # Check if file matches pattern (glob pattern support)
        # パターンがディレクトリの場合は末尾の/を削除して部分一致チェック
        if [[ "${pattern}" == */ ]]; then
            local dir_pattern="${pattern%/}"
            log "INFO" "  Directory pattern: checking if '${file}' contains '${dir_pattern}'"
            if [[ "${file}" == *"${dir_pattern}"* ]]; then
                log "INFO" "File ignored by ${IGNORE_FILE}: ${file} (matches ${pattern})"
                return 0
            fi
        elif [[ "${file}" == *"${pattern}"* ]]; then
            log "INFO" "File ignored by ${IGNORE_FILE}: ${file} (matches ${pattern})"
            return 0
        fi
    done < "${ignore_file}"

    log "INFO" "File is not ignored (checked ${pattern_count} patterns)"
    return 1
}

# ============================================================================
# Formatter Functions
# ============================================================================

run_formatter() {
    local formatter="$1"
    local file="$2"
    shift 2
    local args=("$@")

    if ! command -v "${formatter}" &> /dev/null; then
        log "WARN" "Formatter not found: ${formatter}"
        return 1
    fi

    log "INFO" "Running: ${formatter} ${args[*]} ${file}"

    # macOS互換性のため、timeoutコマンドをオプショナルに
    if command -v timeout &> /dev/null; then
        # GNU timeout利用可能
        if timeout "${FORMATTER_TIMEOUT}" "${formatter}" "${args[@]}" "${file}" 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "Successfully formatted with ${formatter}: ${file}"
            return 0
        else
            local exit_code=$?
            if [[ ${exit_code} -eq 124 ]]; then
                log "ERROR" "Formatter timeout (${FORMATTER_TIMEOUT}s): ${formatter}"
            else
                log "ERROR" "Formatter failed with exit code ${exit_code}: ${formatter}"
            fi
            return 1
        fi
    else
        # timeoutコマンドなし（macOSデフォルト）
        if "${formatter}" "${args[@]}" "${file}" 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "Successfully formatted with ${formatter}: ${file}"
            return 0
        else
            local exit_code=$?
            log "ERROR" "Formatter failed with exit code ${exit_code}: ${formatter}"
            return 1
        fi
    fi
}

format_python() {
    local file="$1"
    local formatted=false

    # Run black
    if run_formatter "black" "${file}" "--quiet"; then
        formatted=true
    fi

    # Run isort
    if run_formatter "isort" "${file}" "--quiet"; then
        formatted=true
    fi

    if [[ "${formatted}" == "true" ]]; then
        log "INFO" "Python file formatted: ${file}"
    fi
}

format_javascript() {
    local file="$1"

    # npx経由でprettierを実行（グローバルインストール不要）
    if command -v npx &> /dev/null; then
        if npx prettier "${file}" --write --log-level warn 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "JavaScript/TypeScript file formatted: ${file}"
        else
            log "ERROR" "prettier failed for: ${file}"
        fi
    else
        log "WARN" "npx not found, skipping prettier"
    fi
}

format_markdown() {
    local file="$1"

    # npx経由でprettierを実行
    if command -v npx &> /dev/null; then
        if npx prettier "${file}" --write --log-level warn --prose-wrap preserve 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "Markdown file formatted: ${file}"
        else
            log "ERROR" "prettier failed for: ${file}"
        fi
    else
        log "WARN" "npx not found, skipping prettier"
    fi
}

format_json() {
    local file="$1"

    # npx経由でprettierを実行
    if command -v npx &> /dev/null; then
        if npx prettier "${file}" --write --log-level warn 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "JSON file formatted: ${file}"
        else
            log "ERROR" "prettier failed for: ${file}"
        fi
    else
        log "WARN" "npx not found, skipping prettier"
    fi
}

format_yaml() {
    local file="$1"

    # npx経由でprettierを実行
    if command -v npx &> /dev/null; then
        if npx prettier "${file}" --write --log-level warn 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "YAML file formatted: ${file}"
        else
            log "ERROR" "prettier failed for: ${file}"
        fi
    else
        log "WARN" "npx not found, skipping prettier"
    fi
}

format_css() {
    local file="$1"

    # npx経由でprettierを実行
    if command -v npx &> /dev/null; then
        if npx prettier "${file}" --write --log-level warn 2>&1 | tee -a "${LOG_FILE}" >&2; then
            log "INFO" "CSS/SCSS file formatted: ${file}"
        else
            log "ERROR" "prettier failed for: ${file}"
        fi
    else
        log "WARN" "npx not found, skipping prettier"
    fi
}

# ============================================================================
# Main Logic
# ============================================================================

format_file() {
    local file="$1"
    local extension="${file##*.}"

    case "${extension}" in
        py)
            format_python "${file}"
            ;;
        js|jsx|ts|tsx|mjs|cjs)
            format_javascript "${file}"
            ;;
        md|markdown)
            format_markdown "${file}"
            ;;
        json)
            format_json "${file}"
            ;;
        yaml|yml)
            format_yaml "${file}"
            ;;
        css|scss|sass|less)
            format_css "${file}"
            ;;
        *)
            log "INFO" "No formatter configured for extension: ${extension}"
            ;;
    esac
}

main() {
    local file="$1"

    log "INFO" "Starting format check: ${file}"

    # Environment and file validation
    check_environment
    validate_file "${file}"

    # Check if file should be ignored
    log "INFO" "Checking if file should be ignored..."
    if is_ignored "${file}"; then
        log "INFO" "File is ignored, skipping format"
        exit 0
    fi
    log "INFO" "File is not ignored, proceeding with format"

    # Format the file
    format_file "${file}"

    log "INFO" "Format check completed: ${file}"
}

# ============================================================================
# Entry Point
# ============================================================================

# Ensure we always exit 0 to prevent Claude Code interruption
trap 'exit 0' ERR

if [[ $# -lt 1 ]]; then
    log "ERROR" "Usage: ${SCRIPT_NAME} <file_path>"
    exit 0
fi

main "$1"
exit 0
