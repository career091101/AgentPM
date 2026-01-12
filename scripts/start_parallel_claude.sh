#!/bin/bash

# Start Parallel Claude - Terminal Parallel Execution
# 5つのClaude Codeインスタンスをtmuxで並列実行

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
SESSION_NAME="claude-parallel-${TIMESTAMP}"
LOG_DIR="${PROJECT_ROOT}/logs/parallel_claude_${TIMESTAMP}"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🚀 Claude Code Parallel Execution Manager${NC}"
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

# Check if tmux is installed
if ! command -v tmux &> /dev/null; then
    print_error "tmux is not installed. Please run: brew install tmux"
    exit 1
fi

# Check if a tmux session with the same name already exists
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    print_warning "Session '$SESSION_NAME' already exists."
    read -p "Do you want to attach to it? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        tmux attach-session -t "$SESSION_NAME"
        exit 0
    else
        print_error "Aborted. Please choose a different session name or kill the existing session."
        exit 1
    fi
fi

# Create log directory
mkdir -p "$LOG_DIR"
print_status "Log directory created: $LOG_DIR"

# Display header
print_header
echo ""
print_info "Session Name: $SESSION_NAME"
print_info "Log Directory: $LOG_DIR"
print_info "Number of Agents: 5"
echo ""

# Task input mode
TASK_FILE="$1"

if [ -z "$TASK_FILE" ]; then
    # Interactive mode: ask user for tasks
    print_info "Interactive mode: Enter tasks for each agent"
    echo ""

    declare -a TASKS
    for i in {1..5}; do
        read -p "$(echo -e ${BLUE}Agent $i task:${NC} )" task
        TASKS+=("$task")
    done

    echo ""
    print_status "Tasks configured:"
    for i in {1..5}; do
        echo "  Agent $i: ${TASKS[$((i-1))]}"
    done
    echo ""
else
    # File mode: read tasks from file
    if [ ! -f "$TASK_FILE" ]; then
        print_error "Task file not found: $TASK_FILE"
        exit 1
    fi

    print_status "Reading tasks from: $TASK_FILE"

    # Read tasks into array (Bash 3.2+ compatible)
    TASKS=()
    while IFS= read -r line; do
        TASKS+=("$line")
    done < "$TASK_FILE"

    if [ ${#TASKS[@]} -ne 5 ]; then
        print_error "Task file must contain exactly 5 lines (tasks). Found: ${#TASKS[@]}"
        exit 1
    fi

    echo ""
    print_status "Tasks configured:"
    for i in {1..5}; do
        echo "  Agent $i: ${TASKS[$((i-1))]}"
    done
    echo ""
fi

# Confirmation
read -p "$(echo -e ${YELLOW}Start parallel execution? \(y/n\):${NC} )" -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_error "Aborted by user."
    exit 1
fi

# Create tmux session
print_status "Creating tmux session: $SESSION_NAME"

# Start tmux session in detached mode with first window
tmux new-session -d -s "$SESSION_NAME" -n "Agent-1"

# Split window into 5 panes
# Layout: 2 rows, 3 columns (3 panes on top, 2 on bottom)
tmux split-window -h -t "$SESSION_NAME:0"
tmux split-window -h -t "$SESSION_NAME:0"
tmux split-window -v -t "$SESSION_NAME:0.0"
tmux split-window -v -t "$SESSION_NAME:0.2"

# Apply tiled layout for better distribution
tmux select-layout -t "$SESSION_NAME:0" tiled

# Send commands to each pane
for i in {0..4}; do
    agent_num=$((i + 1))
    log_file="${LOG_DIR}/agent_${agent_num}.log"
    task="${TASKS[$i]}"

    # Set pane title
    tmux select-pane -t "$SESSION_NAME:0.${i}" -T "Agent ${agent_num}"

    # Send task command to pane
    # Format: cd to project root, then run claude with task as prompt
    tmux send-keys -t "$SESSION_NAME:0.${i}" "cd ${PROJECT_ROOT}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${i}" "echo '🤖 Agent ${agent_num}: ${task}' | tee ${log_file}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${i}" "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' | tee -a ${log_file}" C-m

    # Note: User needs to manually start claude and paste the task
    # Auto-starting claude with task is complex due to interactive nature
    tmux send-keys -t "$SESSION_NAME:0.${i}" "echo 'To start: run \"claude\" and paste the task above'" C-m
    tmux send-keys -t "$SESSION_NAME:0.${i}" "echo 'Task: ${task}'" C-m
    tmux send-keys -t "$SESSION_NAME:0.${i}" "echo ''" C-m
done

# Set status bar with session info
tmux set-option -t "$SESSION_NAME" status-right "#{session_name} | Agents: 5 | #(date +'%H:%M:%S')"
tmux set-option -t "$SESSION_NAME" status-interval 1

# Save session info to log directory
cat > "${LOG_DIR}/session_info.txt" <<EOF
Session Name: $SESSION_NAME
Created: $(date)
Log Directory: $LOG_DIR
Number of Agents: 5

Tasks:
$(for i in {1..5}; do echo "  Agent $i: ${TASKS[$((i-1))]}"; done)

Commands:
  Attach to session: tmux attach-session -t $SESSION_NAME
  Kill session:      tmux kill-session -t $SESSION_NAME
  List sessions:     tmux list-sessions
EOF

print_status "Session created successfully!"
echo ""
print_info "Session Info:"
echo "  Session Name:   $SESSION_NAME"
echo "  Agents:         5"
echo "  Log Directory:  $LOG_DIR"
echo ""
print_info "Commands:"
echo "  Attach:  tmux attach-session -t $SESSION_NAME"
echo "  Kill:    tmux kill-session -t $SESSION_NAME"
echo ""
print_status "Attaching to session..."
sleep 1

# Attach to session
tmux attach-session -t "$SESSION_NAME"
