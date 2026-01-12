#!/bin/bash

# Setup Claude Settings - Merge Project Settings into Personal Settings
# プロジェクト設定（.claude/project-settings.json）を個人設定（~/.claude/settings.json）にマージ

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
PROJECT_SETTINGS="${PROJECT_ROOT}/.claude/project-settings.json"
PERSONAL_SETTINGS="${HOME}/.claude/settings.json"
BACKUP_DIR="${HOME}/.claude/backups"

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
    echo -e "${BLUE}  ⚙️  Claude Code Settings Setup${NC}"
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

Merge project-wide Claude Code settings into personal settings.

OPTIONS:
    -h, --help      Show this help message
    -b, --backup    Create backup only (no merge)
    -r, --restore   Restore from latest backup
    -d, --diff      Show diff between project and personal settings
    -f, --force     Force merge without confirmation

EXAMPLES:
    $0              # Merge with confirmation
    $0 -d           # Show diff first
    $0 -b           # Create backup only
    $0 -r           # Restore from backup
    $0 -f           # Force merge

EOF
}

# Check if jq is installed
check_jq() {
    if ! command -v jq &> /dev/null; then
        print_error "jq is not installed. Installing via Homebrew..."
        brew install jq
    fi
}

# Create backup
create_backup() {
    if [ ! -f "$PERSONAL_SETTINGS" ]; then
        print_warning "Personal settings file not found: $PERSONAL_SETTINGS"
        return 1
    fi

    mkdir -p "$BACKUP_DIR"

    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local backup_file="${BACKUP_DIR}/settings_${timestamp}.json"

    cp "$PERSONAL_SETTINGS" "$backup_file"
    print_status "Backup created: $backup_file"
}

# Restore from backup
restore_backup() {
    if [ ! -d "$BACKUP_DIR" ]; then
        print_error "No backups found in $BACKUP_DIR"
        exit 1
    fi

    local latest_backup=$(ls -t "$BACKUP_DIR"/settings_*.json 2>/dev/null | head -1)

    if [ -z "$latest_backup" ]; then
        print_error "No backup files found"
        exit 1
    fi

    print_info "Latest backup: $latest_backup"
    read -p "$(echo -e ${YELLOW}Restore from this backup? \(y/n\):${NC} )" -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp "$latest_backup" "$PERSONAL_SETTINGS"
        print_status "Settings restored from: $latest_backup"
    else
        print_error "Restore cancelled"
        exit 1
    fi
}

# Show diff
show_diff() {
    if [ ! -f "$PROJECT_SETTINGS" ]; then
        print_error "Project settings not found: $PROJECT_SETTINGS"
        exit 1
    fi

    if [ ! -f "$PERSONAL_SETTINGS" ]; then
        print_error "Personal settings not found: $PERSONAL_SETTINGS"
        exit 1
    fi

    print_info "Diff between project and personal settings:"
    echo ""

    # Extract relevant sections for comparison
    echo -e "${CYAN}Project Permissions:${NC}"
    jq '.permissions.allow' "$PROJECT_SETTINGS"
    echo ""

    echo -e "${CYAN}Personal Permissions:${NC}"
    jq '.permissions.allow' "$PERSONAL_SETTINGS"
    echo ""

    echo -e "${CYAN}Project Hooks:${NC}"
    jq '.hooks' "$PROJECT_SETTINGS"
    echo ""

    echo -e "${CYAN}Personal Hooks:${NC}"
    jq '.hooks' "$PERSONAL_SETTINGS"
    echo ""
}

# Merge settings
merge_settings() {
    local force="${1:-false}"

    if [ ! -f "$PROJECT_SETTINGS" ]; then
        print_error "Project settings not found: $PROJECT_SETTINGS"
        exit 1
    fi

    if [ ! -f "$PERSONAL_SETTINGS" ]; then
        print_warning "Personal settings not found. Creating new file..."
        mkdir -p "$(dirname "$PERSONAL_SETTINGS")"
        echo '{}' > "$PERSONAL_SETTINGS"
    fi

    # Create backup first
    create_backup

    if [ "$force" = "false" ]; then
        echo ""
        print_warning "This will merge project settings into your personal settings."
        print_info "The following will be updated:"
        echo "  - permissions.allow"
        echo "  - hooks (PostToolUse, Stop)"
        echo "  - enabledPlugins"
        echo ""
        print_info "Your personal settings will be preserved:"
        echo "  - model (sonnet/opus/haiku)"
        echo "  - alwaysThinkingEnabled"
        echo "  - Any custom settings"
        echo ""

        read -p "$(echo -e ${YELLOW}Continue? \(y/n\):${NC} )" -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_error "Merge cancelled"
            exit 1
        fi
    fi

    # Merge using jq
    local merged=$(jq -s '
        .[0] as $personal |
        .[1] as $project |
        $personal +
        {
            permissions: $project.permissions,
            hooks: $project.hooks,
            enabledPlugins: $project.enabledPlugins,
            statusLine: $project.statusLine
        }
    ' "$PERSONAL_SETTINGS" "$PROJECT_SETTINGS")

    # Write merged settings
    echo "$merged" | jq '.' > "$PERSONAL_SETTINGS"

    print_status "Settings merged successfully!"
    echo ""
    print_info "Personal settings location: $PERSONAL_SETTINGS"
    print_info "Backup location: $BACKUP_DIR"
}

# Main execution
print_header
echo ""

# Check dependencies
check_jq

# Parse arguments
case "${1:-}" in
    -h|--help)
        usage
        exit 0
        ;;
    -b|--backup)
        create_backup
        exit 0
        ;;
    -r|--restore)
        restore_backup
        exit 0
        ;;
    -d|--diff)
        show_diff
        exit 0
        ;;
    -f|--force)
        merge_settings true
        exit 0
        ;;
    "")
        merge_settings false
        exit 0
        ;;
    *)
        usage
        exit 1
        ;;
esac
