#!/bin/bash

# Setup Git Worktrees - Git Worktrees Parallel Execution Environment
# 複数ブランチを別ディレクトリで並列実行するためのGit Worktrees環境構築

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
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🌲 Git Worktrees Parallel Execution Setup${NC}"
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
Usage: $0 [OPTIONS] [BRANCH_NAMES...]

Setup Git Worktrees for parallel Claude Code execution.

OPTIONS:
    -h, --help          Show this help message
    -c, --count N       Create N worktrees with auto-generated names (default: 3)
    -l, --list          List existing worktrees
    -r, --remove BRANCH Remove a specific worktree
    -a, --remove-all    Remove all worktrees (except main)

EXAMPLES:
    $0                              # Create 3 worktrees (feature-1, feature-2, feature-3)
    $0 -c 5                         # Create 5 worktrees
    $0 auth-refactor api-update     # Create 2 worktrees with specific names
    $0 -l                           # List all worktrees
    $0 -r feature-1                 # Remove feature-1 worktree
    $0 -a                           # Remove all worktrees

EOF
}

# List existing worktrees
list_worktrees() {
    print_header
    echo ""
    print_info "Existing Git Worktrees:"
    echo ""

    git worktree list

    echo ""
}

# Remove a worktree
remove_worktree() {
    local branch_name="$1"

    if [ -z "$branch_name" ]; then
        print_error "Branch name is required for removal"
        exit 1
    fi

    local worktree_path="${WORKTREE_BASE_DIR}/${branch_name}"

    if [ ! -d "$worktree_path" ]; then
        print_error "Worktree not found: $worktree_path"
        exit 1
    fi

    print_info "Removing worktree: $branch_name"

    # Remove worktree
    git worktree remove "$worktree_path" --force

    # Delete branch
    git branch -D "$branch_name" 2>/dev/null || true

    print_status "Worktree removed: $branch_name"
}

# Remove all worktrees
remove_all_worktrees() {
    print_header
    echo ""
    print_warning "This will remove ALL worktrees (except main repository)"
    read -p "$(echo -e ${YELLOW}Continue? \(y/n\):${NC} )" -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_error "Aborted by user."
        exit 1
    fi

    # Get all worktree paths except main
    local worktrees=$(git worktree list | grep -v "(main)" | awk '{print $1}')

    for worktree_path in $worktrees; do
        if [ -d "$worktree_path" ]; then
            local branch_name=$(basename "$worktree_path")
            print_info "Removing worktree: $branch_name"
            git worktree remove "$worktree_path" --force
            git branch -D "$branch_name" 2>/dev/null || true
        fi
    done

    # Remove worktree base directory
    if [ -d "$WORKTREE_BASE_DIR" ]; then
        rm -rf "$WORKTREE_BASE_DIR"
        print_status "Worktree directory removed: $WORKTREE_BASE_DIR"
    fi

    print_status "All worktrees removed"
}

# Create a worktree
create_worktree() {
    local branch_name="$1"
    local worktree_path="${WORKTREE_BASE_DIR}/${branch_name}"

    # Check if worktree already exists
    if [ -d "$worktree_path" ]; then
        print_warning "Worktree already exists: $branch_name"
        return 1
    fi

    # Create worktree base directory if it doesn't exist
    mkdir -p "$WORKTREE_BASE_DIR"

    # Create worktree
    print_info "Creating worktree: $branch_name"
    git worktree add "$worktree_path" -b "$branch_name"

    # Setup shared directories (.claude and scripts)
    setup_shared_directories "$worktree_path"

    print_status "Worktree created: $branch_name"
    print_info "Path: $worktree_path"
}

# Setup shared directories
setup_shared_directories() {
    local worktree_path="$1"

    print_info "Setting up shared directories (.claude, scripts)..."

    # Remove existing .claude and scripts if they exist
    if [ -d "$worktree_path/aipm_v0/.claude" ]; then
        rm -rf "$worktree_path/aipm_v0/.claude"
    fi

    if [ -d "$worktree_path/aipm_v0/scripts" ]; then
        rm -rf "$worktree_path/aipm_v0/scripts"
    fi

    # Create symbolic links to shared directories
    ln -s "${PROJECT_ROOT}/.claude" "$worktree_path/aipm_v0/.claude"
    ln -s "${PROJECT_ROOT}/scripts" "$worktree_path/aipm_v0/scripts"

    print_status "Shared directories configured (symlinks)"
}

# Main setup
main_setup() {
    local count="${1:-3}"
    local branch_names=("${@:2}")

    print_header
    echo ""

    # If no branch names provided, generate auto names
    if [ ${#branch_names[@]} -eq 0 ]; then
        print_info "Generating $count auto-named branches (feature-1, feature-2, ...)"
        echo ""

        for i in $(seq 1 $count); do
            branch_names+=("feature-$i")
        done
    else
        count=${#branch_names[@]}
    fi

    print_info "Creating $count worktrees:"
    for branch in "${branch_names[@]}"; do
        echo "  - $branch"
    done
    echo ""

    read -p "$(echo -e ${YELLOW}Continue? \(y/n\):${NC} )" -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_error "Aborted by user."
        exit 1
    fi

    # Create worktrees
    for branch in "${branch_names[@]}"; do
        create_worktree "$branch"
    done

    echo ""
    print_status "Setup complete!"
    echo ""

    # Summary
    print_info "Summary:"
    echo "  Worktrees created: $count"
    echo "  Base directory:    $WORKTREE_BASE_DIR"
    echo ""

    print_info "Next steps:"
    echo "  1. cd ${WORKTREE_BASE_DIR}/feature-1/aipm_v0"
    echo "  2. claude"
    echo ""

    print_info "To start Claude in all worktrees in parallel:"
    echo "  bash scripts/start_claude_in_worktrees.sh"
    echo ""

    # List all worktrees
    echo ""
    git worktree list
}

# Main execution
cd "$PROJECT_ROOT"

case "${1:-}" in
    -h|--help)
        usage
        exit 0
        ;;
    -l|--list)
        list_worktrees
        exit 0
        ;;
    -r|--remove)
        remove_worktree "$2"
        exit 0
        ;;
    -a|--remove-all)
        remove_all_worktrees
        exit 0
        ;;
    -c|--count)
        count="$2"
        shift 2
        main_setup "$count" "$@"
        ;;
    *)
        if [[ "$1" == -* ]]; then
            usage
            exit 1
        else
            main_setup 3 "$@"
        fi
        ;;
esac
