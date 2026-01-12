#!/bin/bash

# Worktree Status - Monitor Git Worktrees Status
# 各worktreeのGitステータス、実行中プロセス、変更ファイルを監視

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
BASE_DIR="/Users/yuichi/AIPM"
WORKTREE_BASE_DIR="${BASE_DIR}/worktrees"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🌲 Git Worktrees Status Monitor${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Usage
usage() {
    cat <<EOF
Usage: $0 [OPTIONS]

Monitor status of all Git Worktrees.

OPTIONS:
    -h, --help      Show this help message
    -w, --watch     Watch mode (auto-refresh every 5 seconds)
    -d, --detailed  Show detailed status (git diff, claude processes)

EXAMPLES:
    $0              # Show status once
    $0 -w           # Watch mode (refresh every 5 seconds)
    $0 -d           # Detailed status

EOF
}

# Get all worktrees except main
get_worktrees() {
    git worktree list | grep -v "(main)" | awk '{print $1}'
}

# Check if Claude is running in worktree
check_claude_process() {
    local worktree_path="$1"
    local project_path="${worktree_path}/aipm_v0"

    # Look for claude processes in this directory
    # Remove newlines to prevent "integer expression expected" error
    local claude_count=$(ps aux | grep "claude" | grep -v "grep" | grep -c "$project_path" || echo 0)
    claude_count=$(echo "$claude_count" | tr -d '\n')

    if [ "$claude_count" -gt 0 ]; then
        echo -e "${GREEN}●${NC} Claude running ($claude_count processes)"
    else
        echo -e "${RED}○${NC} Claude not running"
    fi
}

# Get git status
get_git_status() {
    local worktree_path="$1"

    cd "$worktree_path/aipm_v0"

    local status=$(git status --porcelain)

    if [ -z "$status" ]; then
        echo -e "${GREEN}✓${NC} Clean (no changes)"
    else
        local modified=$(echo "$status" | grep -c "^ M" || echo 0)
        modified=$(echo "$modified" | tr -d '\n')
        local added=$(echo "$status" | grep -c "^A " || echo 0)
        added=$(echo "$added" | tr -d '\n')
        local deleted=$(echo "$status" | grep -c "^D " || echo 0)
        deleted=$(echo "$deleted" | tr -d '\n')
        local untracked=$(echo "$status" | grep -c "^??" || echo 0)
        untracked=$(echo "$untracked" | tr -d '\n')

        echo -e "${YELLOW}!${NC} Modified: $modified, Added: $added, Deleted: $deleted, Untracked: $untracked"
    fi
}

# Get branch info
get_branch_info() {
    local worktree_path="$1"

    cd "$worktree_path/aipm_v0"

    local branch=$(git branch --show-current)
    local commit=$(git log -1 --format="%h - %s" 2>/dev/null || echo "No commits")

    echo -e "  ${CYAN}Branch:${NC} $branch"
    echo -e "  ${CYAN}Commit:${NC} $commit"
}

# Show detailed status
show_detailed_status() {
    local worktree_path="$1"
    local branch_name=$(basename "$worktree_path")

    cd "$worktree_path/aipm_v0"

    echo ""
    echo -e "${MAGENTA}━━━ Detailed Status: $branch_name ━━━${NC}"
    echo ""

    # Git diff summary
    echo -e "${CYAN}Modified Files:${NC}"
    git diff --name-status | head -n 10
    if [ $(git diff --name-status | wc -l) -gt 10 ]; then
        echo "  ... (showing first 10 files)"
    fi

    echo ""

    # Recent commits
    echo -e "${CYAN}Recent Commits (last 3):${NC}"
    git log -3 --oneline

    echo ""

    # Claude processes
    echo -e "${CYAN}Claude Processes:${NC}"
    ps aux | grep "claude" | grep "$worktree_path" | grep -v "grep" || echo "  No Claude processes running"

    echo ""
}

# Main status display
show_status() {
    local detailed="${1:-false}"

    print_header
    echo ""
    echo -e "${CYAN}$(date '+%Y-%m-%d %H:%M:%S')${NC}"
    echo ""

    # Get all worktrees
    local worktrees=$(get_worktrees)
    local worktree_count=$(echo "$worktrees" | grep -c '^' || echo 0)
    worktree_count=$(echo "$worktree_count" | tr -d '\n')

    if [ "$worktree_count" -eq 0 ]; then
        print_warning "No worktrees found"
        echo ""
        print_info "To create worktrees:"
        echo "  bash scripts/setup_worktrees.sh"
        return
    fi

    print_info "Found $worktree_count worktrees"
    echo ""

    # Main repository status
    echo -e "${BLUE}Main Repository:${NC} /Users/yuichi/AIPM/aipm_v0"
    cd "$PROJECT_ROOT"
    echo -n "  Status: "
    get_git_status "$BASE_DIR"
    echo ""

    # Worktree statuses
    local i=1
    for worktree_path in $worktrees; do
        branch_name=$(basename "$worktree_path")

        echo -e "${BLUE}$i. Worktree:${NC} $branch_name"
        echo "  Path: $worktree_path/aipm_v0"
        echo -n "  Process: "
        check_claude_process "$worktree_path"
        echo -n "  Status: "
        get_git_status "$worktree_path"
        get_branch_info "$worktree_path"

        if [ "$detailed" = "true" ]; then
            show_detailed_status "$worktree_path"
        fi

        echo ""
        i=$((i + 1))
    done

    # Summary
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}Summary:${NC}"
    echo "  Total worktrees: $worktree_count"

    local running_count=0
    for worktree_path in $worktrees; do
        local project_path="${worktree_path}/aipm_v0"
        local claude_count=$(ps aux | grep "claude" | grep -v "grep" | grep -c "$project_path" || echo 0)
        claude_count=$(echo "$claude_count" | tr -d '\n')
        if [ "$claude_count" -gt 0 ]; then
            running_count=$((running_count + 1))
        fi
    done

    echo "  Claude running: $running_count/$worktree_count"
    echo ""
}

# Watch mode
watch_mode() {
    local detailed="${1:-false}"

    while true; do
        clear
        show_status "$detailed"
        echo -e "${YELLOW}Press Ctrl+C to exit${NC}"
        sleep 5
    done
}

# Main execution
cd "$PROJECT_ROOT"

case "${1:-}" in
    -h|--help)
        usage
        exit 0
        ;;
    -w|--watch)
        if [ "$2" = "-d" ] || [ "$2" = "--detailed" ]; then
            watch_mode true
        else
            watch_mode false
        fi
        ;;
    -d|--detailed)
        if [ "$2" = "-w" ] || [ "$2" = "--watch" ]; then
            watch_mode true
        else
            show_status true
        fi
        ;;
    "")
        show_status false
        ;;
    *)
        usage
        exit 1
        ;;
esac
