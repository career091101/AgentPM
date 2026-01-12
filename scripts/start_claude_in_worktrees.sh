#!/bin/bash

# Start Claude in Worktrees - Launch Claude Code in all Git Worktrees
# すべてのworktreeでClaude Codeを並列起動

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
BASE_DIR="/Users/yuichi/AIPM"
WORKTREE_BASE_DIR="${BASE_DIR}/worktrees"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
SESSION_NAME="claude-worktrees-${TIMESTAMP}"
LOG_DIR="${PROJECT_ROOT}/logs/worktree_sessions_${TIMESTAMP}"

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
    echo -e "${BLUE}  🌲 Claude Code Worktree Parallel Execution${NC}"
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

# Get all worktrees except main
get_worktrees() {
    git worktree list | grep -v "(main)" | awk '{print $1}'
}

# Count worktrees
worktrees=$(get_worktrees)
worktree_count=$(echo "$worktrees" | grep -c '^' || echo 0)

if [ "$worktree_count" -eq 0 ]; then
    print_error "No worktrees found. Please create worktrees first:"
    echo "  bash scripts/setup_worktrees.sh"
    exit 1
fi

# Display header
print_header
echo ""
print_info "Found $worktree_count worktrees"
echo ""

# List worktrees
print_info "Worktrees:"
i=1
declare -a WORKTREE_PATHS
for worktree_path in $worktrees; do
    branch_name=$(basename "$worktree_path")
    echo "  $i. $branch_name ($worktree_path)"
    WORKTREE_PATHS+=("$worktree_path")
    i=$((i + 1))
done
echo ""

# Confirmation
read -p "$(echo -e ${YELLOW}Start Claude in all worktrees? \(y/n\):${NC} )" -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_error "Aborted by user."
    exit 1
fi

# Create log directory
mkdir -p "$LOG_DIR"
print_status "Log directory created: $LOG_DIR"

# Create tmux session
print_status "Creating tmux session: $SESSION_NAME"

# Start tmux session in detached mode
tmux new-session -d -s "$SESSION_NAME" -n "Worktree-1"

# Split window based on worktree count
if [ "$worktree_count" -eq 2 ]; then
    tmux split-window -h -t "$SESSION_NAME:0"
elif [ "$worktree_count" -eq 3 ]; then
    tmux split-window -h -t "$SESSION_NAME:0"
    tmux split-window -v -t "$SESSION_NAME:0.0"
elif [ "$worktree_count" -eq 4 ]; then
    tmux split-window -h -t "$SESSION_NAME:0"
    tmux split-window -v -t "$SESSION_NAME:0.0"
    tmux split-window -v -t "$SESSION_NAME:0.1"
elif [ "$worktree_count" -ge 5 ]; then
    tmux split-window -h -t "$SESSION_NAME:0"
    tmux split-window -h -t "$SESSION_NAME:0"
    tmux split-window -v -t "$SESSION_NAME:0.0"
    tmux split-window -v -t "$SESSION_NAME:0.2"
fi

# Apply tiled layout
tmux select-layout -t "$SESSION_NAME:0" tiled

# Send commands to each pane
pane_index=0
for worktree_path in "${WORKTREE_PATHS[@]}"; do
    if [ $pane_index -ge $worktree_count ]; then
        break
    fi

    branch_name=$(basename "$worktree_path")
    project_path="${worktree_path}/aipm_v0"
    log_file="${LOG_DIR}/${branch_name}.log"

    # Set pane title
    tmux select-pane -t "$SESSION_NAME:0.${pane_index}" -T "$branch_name"

    # Send commands to pane
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "cd ${project_path}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "echo '🌲 Worktree: ${branch_name}' | tee ${log_file}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "echo 'Path: ${project_path}' | tee -a ${log_file}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' | tee -a ${log_file}" C-m
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "echo 'To start: run \"claude\"'" C-m
    tmux send-keys -t "$SESSION_NAME:0.${pane_index}" "echo ''" C-m

    pane_index=$((pane_index + 1))
done

# Set status bar
tmux set-option -t "$SESSION_NAME" status-right "#{session_name} | Worktrees: $worktree_count | #(date +'%H:%M:%S')"
tmux set-option -t "$SESSION_NAME" status-interval 1

# Save session info
cat > "${LOG_DIR}/session_info.txt" <<EOF
Session Name: $SESSION_NAME
Created: $(date)
Log Directory: $LOG_DIR
Number of Worktrees: $worktree_count

Worktrees:
$(i=1; for path in "${WORKTREE_PATHS[@]}"; do echo "  $i. $(basename "$path") ($path)"; i=$((i + 1)); done)

Commands:
  Attach to session: tmux attach-session -t $SESSION_NAME
  Kill session:      tmux kill-session -t $SESSION_NAME
  List sessions:     tmux list-sessions
EOF

print_status "Session created successfully!"
echo ""
print_info "Session Info:"
echo "  Session Name:   $SESSION_NAME"
echo "  Worktrees:      $worktree_count"
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
