#!/bin/bash

# check_context_usage.sh - Claude Code Context Usage Monitor (Reference Implementation)
# Week 5 Day 6-7: Context usage monitoring
#
# IMPORTANT: Claude Code does not provide a programmatic API to retrieve context usage.
# This script provides guidance and best practices for manual context management.
#
# Usage:
#   bash scripts/check_context_usage.sh        # Show context management guide
#   bash scripts/check_context_usage.sh -w     # Watch mode (periodic reminders)

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
NOTIFY_SCRIPT="${PROJECT_ROOT}/scripts/claude_notify.sh"
CHECK_INTERVAL=1800  # 30 minutes

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Print header
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  📊 Claude Code Context Usage Monitor${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Show context management guide
show_guide() {
    cat <<'EOF'
📖 Context Management Best Practices

Claude Code does not provide a programmatic API to retrieve context usage.
You must manually monitor context using the following commands:

1️⃣ Check Current Context Usage:
   /context
   → Displays current context window usage percentage

2️⃣ Compact Context (70% threshold):
   /compact
   → Compresses conversation history to free up context
   → Use when context reaches 70%

3️⃣ Clear Context (new task):
   /clear
   → Starts a new session with clean context
   → Use when starting a completely new task

4️⃣ Forget Specific Files:
   /forget <file_path>
   → Removes specific file from context
   → Use after reading large temporary files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Recommended Workflow:

┌─────────────────────────────────────────────────────────┐
│ Context Level │ Action                                  │
├───────────────┼─────────────────────────────────────────┤
│ 0-50%         │ ✅ Continue working normally            │
│ 50-70%        │ ⚠️  Monitor closely, plan /compact      │
│ 70-85%        │ 🔄 Execute /compact immediately         │
│ 85-100%       │ 🚨 Execute /clear for new session       │
└─────────────────────────────────────────────────────────┘

💡 Tips:
- Always show context in status line (set in project-settings.json)
- Use subagents (Task tool) to isolate heavy tasks
- Optimize .claudeignore to exclude unnecessary files
- Clear context after completing each major task

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EOF
}

# Send periodic reminder
send_reminder() {
    local message="⏰ Context Check Reminder\n\nRun /context to check your context usage.\nUse /compact if above 70%."

    if [ -f "$NOTIFY_SCRIPT" ]; then
        bash "$NOTIFY_SCRIPT" "info" "Claude Code" "Time to check context usage" "Ping"
    fi

    echo -e "${YELLOW}⚠️  Reminder: Check context usage with /context command${NC}"
}

# Watch mode
watch_mode() {
    echo -e "${GREEN}✓${NC} Watch mode enabled (checking every ${CHECK_INTERVAL}s = $(($CHECK_INTERVAL / 60)) minutes)"
    echo -e "${BLUE}ℹ${NC} Press Ctrl+C to stop"
    echo ""

    while true; do
        send_reminder
        sleep $CHECK_INTERVAL
    done
}

# Main execution
print_header

case "${1:-}" in
    -w|--watch)
        watch_mode
        ;;
    -h|--help)
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  -w, --watch    Watch mode (periodic reminders every 30 minutes)"
        echo "  -h, --help     Show this help message"
        echo ""
        exit 0
        ;;
    "")
        show_guide
        exit 0
        ;;
    *)
        echo -e "${RED}✗${NC} Unknown option: $1"
        echo "Use -h for help"
        exit 1
        ;;
esac
