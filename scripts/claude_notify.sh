#!/bin/bash
# Claude Code macOS通知スクリプト
# 使用法: bash claude_notify.sh <type> <title> <message> [sound]

TYPE=$1
TITLE=$2
MESSAGE=$3
SOUND=${4:-"Glass"}

osascript -e "display notification \"$MESSAGE\" with title \"$TITLE\" sound name \"$SOUND\""
