#!/bin/bash

# Aggregate Logs - Parallel Claude Execution Log Aggregator
# Collects and aggregates logs from parallel execution sessions

set -e

# Configuration
PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"
LOGS_BASE_DIR="${PROJECT_ROOT}/logs"

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
    echo -e "${BLUE}  📊 Claude Code Parallel Execution Log Aggregator${NC}"
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
Usage: $0 [OPTIONS] [SESSION_DIR]

Aggregate logs from parallel Claude execution sessions.

OPTIONS:
    -h, --help          Show this help message
    -l, --list          List all available sessions
    -a, --all           Aggregate all sessions
    -o, --output FILE   Output report file (default: stdout)

EXAMPLES:
    $0                                  # Aggregate latest session
    $0 -l                               # List all sessions
    $0 -a                               # Aggregate all sessions
    $0 logs/parallel_claude_20260103_120000  # Aggregate specific session
    $0 -o report.md                     # Output to file

EOF
}

# List all sessions
list_sessions() {
    print_header
    echo ""
    print_info "Available parallel execution sessions:"
    echo ""

    local sessions=("${LOGS_BASE_DIR}"/parallel_claude_*)

    if [ ${#sessions[@]} -eq 0 ] || [ ! -e "${sessions[0]}" ]; then
        print_warning "No sessions found in ${LOGS_BASE_DIR}"
        return
    fi

    for session_dir in "${sessions[@]}"; do
        if [ -d "$session_dir" ]; then
            local session_name=$(basename "$session_dir")
            local timestamp=$(echo "$session_name" | sed 's/parallel_claude_//')
            local agent_count=$(find "$session_dir" -name "agent_*.log" | wc -l | tr -d ' ')

            echo -e "  ${CYAN}●${NC} $session_name"
            echo "    Timestamp: $timestamp"
            echo "    Agents:    $agent_count"

            if [ -f "$session_dir/session_info.txt" ]; then
                echo "    Info file: ✓"
            fi

            echo ""
        fi
    done
}

# Aggregate a single session
aggregate_session() {
    local session_dir="$1"
    local output_file="$2"

    if [ ! -d "$session_dir" ]; then
        print_error "Session directory not found: $session_dir"
        return 1
    fi

    local session_name=$(basename "$session_dir")
    local timestamp=$(echo "$session_name" | sed 's/parallel_claude_//')

    # Start aggregation
    {
        echo "# Claude Code Parallel Execution Report"
        echo ""
        echo "**Session**: $session_name"
        echo "**Timestamp**: $timestamp"
        echo "**Generated**: $(date '+%Y-%m-%d %H:%M:%S')"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""

        # Session info
        if [ -f "$session_dir/session_info.txt" ]; then
            echo "## Session Information"
            echo ""
            echo '```'
            cat "$session_dir/session_info.txt"
            echo '```'
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
        fi

        # Agent logs
        echo "## Agent Logs"
        echo ""

        local agent_logs=("$session_dir"/agent_*.log)

        if [ ${#agent_logs[@]} -eq 0 ] || [ ! -e "${agent_logs[0]}" ]; then
            echo "_No agent logs found._"
            echo ""
        else
            for log_file in "${agent_logs[@]}"; do
                if [ -f "$log_file" ]; then
                    local agent_name=$(basename "$log_file" .log)
                    local line_count=$(wc -l < "$log_file" | tr -d ' ')

                    echo "### ${agent_name}"
                    echo ""
                    echo "**Log file**: \`$(basename "$log_file")\`"
                    echo "**Lines**: $line_count"
                    echo ""

                    if [ "$line_count" -gt 0 ]; then
                        echo '```'
                        head -n 100 "$log_file"
                        if [ "$line_count" -gt 100 ]; then
                            echo ""
                            echo "... (truncated, showing first 100 lines of $line_count total)"
                        fi
                        echo '```'
                    else
                        echo "_Empty log file._"
                    fi

                    echo ""
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo ""
                fi
            done
        fi

        # Summary statistics
        echo "## Summary Statistics"
        echo ""
        echo "| Metric | Value |"
        echo "|--------|-------|"
        echo "| Session | $session_name |"
        echo "| Agents | ${#agent_logs[@]} |"

        local total_lines=0
        for log_file in "${agent_logs[@]}"; do
            if [ -f "$log_file" ]; then
                local lines=$(wc -l < "$log_file" | tr -d ' ')
                total_lines=$((total_lines + lines))
            fi
        done

        echo "| Total Log Lines | $total_lines |"
        echo "| Session Directory | \`$session_dir\` |"
        echo ""

    } | if [ -n "$output_file" ]; then
        tee "$output_file"
    else
        cat
    fi
}

# Aggregate all sessions
aggregate_all() {
    local output_file="$1"

    print_header
    echo ""
    print_info "Aggregating all parallel execution sessions..."
    echo ""

    local sessions=("${LOGS_BASE_DIR}"/parallel_claude_*)

    if [ ${#sessions[@]} -eq 0 ] || [ ! -e "${sessions[0]}" ]; then
        print_warning "No sessions found in ${LOGS_BASE_DIR}"
        return
    fi

    {
        echo "# Claude Code Parallel Execution - All Sessions Report"
        echo ""
        echo "**Generated**: $(date '+%Y-%m-%d %H:%M:%S')"
        echo "**Total Sessions**: ${#sessions[@]}"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""

        for session_dir in "${sessions[@]}"; do
            if [ -d "$session_dir" ]; then
                aggregate_session "$session_dir" ""
            fi
        done

    } | if [ -n "$output_file" ]; then
        tee "$output_file"
        print_status "Report saved to: $output_file"
    else
        cat
    fi
}

# Get latest session
get_latest_session() {
    local latest_session=$(ls -td "${LOGS_BASE_DIR}"/parallel_claude_* 2>/dev/null | head -1)

    if [ -z "$latest_session" ]; then
        print_error "No sessions found in ${LOGS_BASE_DIR}"
        exit 1
    fi

    echo "$latest_session"
}

# Main execution
main() {
    local list_mode=false
    local all_mode=false
    local output_file=""
    local session_dir=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help)
                usage
                exit 0
                ;;
            -l|--list)
                list_mode=true
                shift
                ;;
            -a|--all)
                all_mode=true
                shift
                ;;
            -o|--output)
                output_file="$2"
                shift 2
                ;;
            *)
                session_dir="$1"
                shift
                ;;
        esac
    done

    # Execute based on mode
    if [ "$list_mode" = true ]; then
        list_sessions
    elif [ "$all_mode" = true ]; then
        aggregate_all "$output_file"
    elif [ -n "$session_dir" ]; then
        aggregate_session "$session_dir" "$output_file"
    else
        # Default: aggregate latest session
        local latest_session=$(get_latest_session)
        print_header
        echo ""
        print_info "Aggregating latest session: $(basename "$latest_session")"
        echo ""
        aggregate_session "$latest_session" "$output_file"
    fi
}

# Run main
main "$@"
