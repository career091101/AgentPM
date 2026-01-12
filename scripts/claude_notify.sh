#!/bin/bash

# Claude Notify - System Notification for Claude Code Task Completion
# macOS Notification Center integration

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
LOG_DIR="${PROJECT_ROOT}/logs/notifications"
LOG_FILE="${LOG_DIR}/notifications_$(date +"%Y%m%d").log"

# Notification types
TYPE="${1:-info}"  # success, error, warning, info
TITLE="${2:-Claude Code}"
MESSAGE="${3:-Task completed}"
SOUND="${4:-Glass}"  # Glass, Hero, Ping, Pop, Purr, Sosumi, Submarine, Blow, Bottle, Frog

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Function to send macOS notification
send_notification() {
    local type="$1"
    local title="$2"
    local message="$3"
    local sound="$4"

    # Map type to emoji
    case "$type" in
        success)
            emoji="✅"
            ;;
        error)
            emoji="❌"
            ;;
        warning)
            emoji="⚠️"
            ;;
        info)
            emoji="ℹ️"
            ;;
        *)
            emoji="🔔"
            ;;
    esac

    # Send notification using osascript
    osascript -e "display notification \"${message}\" with title \"${emoji} ${title}\" sound name \"${sound}\""

    # Log notification
    log_notification "$type" "$title" "$message"
}

# Function to log notification
log_notification() {
    local type="$1"
    local title="$2"
    local message="$3"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    echo "[$timestamp] [$type] $title: $message" >> "$LOG_FILE"
}

# Main execution
send_notification "$TYPE" "$TITLE" "$MESSAGE" "$SOUND"

# Exit code based on type
case "$TYPE" in
    error)
        exit 1
        ;;
    *)
        exit 0
        ;;
esac
