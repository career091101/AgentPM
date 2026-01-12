#!/bin/bash
# Parallel Batch Launcher for Founder Research
# This script helps prepare batch execution commands for Claude Code

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
WAVE_DEFS="$SCRIPT_DIR/wave_definitions.json"
PROGRESS_FILE="$SCRIPT_DIR/progress.json"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Initialize progress file if not exists
if [ ! -f "$PROGRESS_FILE" ]; then
    echo '{
  "started_at": null,
  "completed": [],
  "failed": [],
  "in_progress": [],
  "waves": {}
}' > "$PROGRESS_FILE"
fi

# Function to get pending targets for a wave
get_pending_targets() {
    local wave_id=$1
    local max_count=${2:-5}

    # Extract targets from wave definitions and filter out completed ones
    python3 - <<EOF
import json
import sys

with open('$WAVE_DEFS', 'r') as f:
    data = json.load(f)

with open('$PROGRESS_FILE', 'r') as f:
    progress = json.load(f)

completed = progress.get('completed', [])
in_progress = progress.get('in_progress', [])

wave = next((w for w in data['waves'] if w['id'] == '$wave_id'), None)
if not wave:
    print(f"Wave $wave_id not found", file=sys.stderr)
    sys.exit(1)

pending = []
for target in wave['targets']:
    target_id = target['id']
    if target_id not in completed and target_id not in in_progress:
        pending.append({
            'id': target_id,
            'type': target['type'],
            'category': target['category']
        })
        if len(pending) >= $max_count:
            break

print(json.dumps(pending, indent=2))
EOF
}

# Function to display status
show_status() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}Batch Execution Status${NC}"
    echo -e "${BLUE}========================================${NC}"

    python3 - <<EOF
import json

with open('$WAVE_DEFS', 'r') as f:
    data = json.load(f)

with open('$PROGRESS_FILE', 'r') as f:
    progress = json.load(f)

if progress.get('started_at'):
    print(f"Started: {progress['started_at']}")

total_completed = len(progress.get('completed', []))
total_failed = len(progress.get('failed', []))
total_in_progress = len(progress.get('in_progress', []))
total_targets = sum(w['count'] for w in data['waves'])

print(f"\nOverall: {total_completed}/{total_targets} completed ({100*total_completed/total_targets:.1f}%)")
print(f"In Progress: {total_in_progress}")
print(f"Failed: {total_failed}")

print("\nWave Progress:")
for wave in data['waves']:
    wave_data = progress.get('waves', {}).get(wave['id'], {'completed': 0})
    completed = wave_data.get('completed', 0)
    total = wave['count']
    pct = 100 * completed / total
    print(f"  {wave['name']}: {completed}/{total} ({pct:.1f}%)")
EOF

    echo -e "${BLUE}========================================${NC}\n"
}

# Function to mark target as completed
mark_completed() {
    local target_id=$1
    local wave_id=$2

    python3 - <<EOF
import json
from datetime import datetime

with open('$PROGRESS_FILE', 'r') as f:
    progress = json.load(f)

if '$target_id' not in progress['completed']:
    progress['completed'].append('$target_id')

if '$target_id' in progress.get('in_progress', []):
    progress['in_progress'].remove('$target_id')

if '$wave_id' not in progress.get('waves', {}):
    progress['waves']['$wave_id'] = {'completed': 0}

progress['waves']['$wave_id']['completed'] = progress['waves']['$wave_id'].get('completed', 0) + 1

if not progress.get('started_at'):
    progress['started_at'] = datetime.now().isoformat()

with open('$PROGRESS_FILE', 'w') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)

print(f"✅ Marked $target_id as completed")
EOF
}

# Function to generate Claude Code prompts
generate_batch_prompts() {
    local wave_id=$1
    local batch_size=${2:-10}

    echo -e "${YELLOW}Generating batch prompts for $wave_id (batch size: $batch_size)${NC}\n"

    local targets=$(get_pending_targets "$wave_id" "$batch_size")

    if [ "$targets" == "[]" ] || [ -z "$targets" ]; then
        echo -e "${GREEN}No pending targets for $wave_id${NC}"
        return
    fi

    echo "$targets" | python3 - <<'EOF'
import json
import sys

targets = json.load(sys.stdin)

print(f"Found {len(targets)} pending targets:\n")

for i, target in enumerate(targets, 1):
    target_id = target['id']
    target_type = target['type']
    category = target['category']

    print(f"{i}. {target_id} ({target_type})")

print(f"\n{'='*80}")
print("Copy and paste these prompts to launch agents in parallel:")
print(f"{'='*80}\n")

for target in targets:
    target_id = target['id']
    target_type = target['type']
    category = target['category']

    if target_type == 'founder':
        section_template = "EMERGING_068_bereal.md"
    elif target_type == 'failure':
        section_template = "failure analysis"
    elif target_type == 'pivot':
        section_template = "pivot success story"

    print(f"""
Task: Generate research document for {target_id}

Document type: {target_type}
Category: {category}
Template: {section_template}

Research and create a comprehensive markdown document following the project structure.
Save to: documents/{category}/{target_id}.md

FULLY AUTOMATED - No human input required.
""")
    print(f"{'='*80}\n")
EOF
}

# Main command dispatcher
case "$1" in
    status)
        show_status
        ;;
    pending)
        wave_id=${2:-wave1}
        count=${3:-10}
        echo -e "${YELLOW}Pending targets for $wave_id (showing first $count):${NC}\n"
        get_pending_targets "$wave_id" "$count"
        ;;
    prompts)
        wave_id=${2:-wave1}
        batch_size=${3:-10}
        generate_batch_prompts "$wave_id" "$batch_size"
        ;;
    complete)
        target_id=$2
        wave_id=$3
        mark_completed "$target_id" "$wave_id"
        ;;
    *)
        echo "Usage: $0 {status|pending|prompts|complete}"
        echo ""
        echo "Commands:"
        echo "  status                     - Show overall progress"
        echo "  pending <wave_id> [count]  - Show pending targets for wave"
        echo "  prompts <wave_id> [count]  - Generate batch prompts for Claude Code"
        echo "  complete <target_id> <wave_id> - Mark target as completed"
        echo ""
        echo "Examples:"
        echo "  $0 status"
        echo "  $0 pending wave1 5"
        echo "  $0 prompts wave1 10"
        echo "  $0 complete FOUNDER_321 wave1"
        exit 1
        ;;
esac
