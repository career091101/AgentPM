#!/bin/bash

# test_all_mcp.sh - MCP Integration Test (All Servers)
# Week 6 Phase 3: 全3MCPサーバー（Slack, BigQuery, Sentry）の統合テスト
#
# Usage:
#   bash scripts/test_all_mcp.sh

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"

# Test results
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Print header
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🔌 MCP Integration Test - All Servers${NC}"
    echo -e "${BLUE}  Week 6 Phase 3: Slack + BigQuery + Sentry${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Increment test counter
pass_test() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    PASSED_TESTS=$((PASSED_TESTS + 1))
    echo -e "${GREEN}✓${NC} $1"
}

fail_test() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    FAILED_TESTS=$((FAILED_TESTS + 1))
    echo -e "${RED}✗${NC} $1"
}

# Test 1: .mcp.json exists
test_mcp_json_exists() {
    echo -e "${CYAN}Test 1: .mcp.json exists${NC}"

    if [ -f "${PROJECT_ROOT}/.mcp.json" ]; then
        pass_test ".mcp.json found"
    else
        fail_test ".mcp.json not found"
        return 1
    fi
    echo ""
}

# Test 2: .mcp.json is valid JSON
test_mcp_json_valid() {
    echo -e "${CYAN}Test 2: .mcp.json is valid JSON${NC}"

    if jq empty "${PROJECT_ROOT}/.mcp.json" 2>/dev/null; then
        pass_test ".mcp.json is valid JSON"
    else
        fail_test ".mcp.json is invalid JSON"
        return 1
    fi
    echo ""
}

# Test 3: All 3 MCP servers are configured
test_mcp_servers_configured() {
    echo -e "${CYAN}Test 3: All 3 MCP servers are configured${NC}"

    local all_configured=true

    if jq -e '.mcpServers.slack' "${PROJECT_ROOT}/.mcp.json" > /dev/null 2>&1; then
        pass_test "Slack MCP server configured"
    else
        fail_test "Slack MCP server not configured"
        all_configured=false
    fi

    if jq -e '.mcpServers.bigquery' "${PROJECT_ROOT}/.mcp.json" > /dev/null 2>&1; then
        pass_test "BigQuery MCP server configured"
    else
        fail_test "BigQuery MCP server not configured"
        all_configured=false
    fi

    if jq -e '.mcpServers.sentry' "${PROJECT_ROOT}/.mcp.json" > /dev/null 2>&1; then
        pass_test "Sentry MCP server configured"
    else
        fail_test "Sentry MCP server not configured"
        all_configured=false
    fi

    echo ""
    if [ "$all_configured" = false ]; then
        return 1
    fi
}

# Test 4: .env file exists
test_env_exists() {
    echo -e "${CYAN}Test 4: .env file exists${NC}"

    if [ -f "${PROJECT_ROOT}/.env" ]; then
        pass_test ".env file found"
    else
        fail_test ".env file not found (copy from .env.example)"
        return 1
    fi
    echo ""
}

# Test 5: All required environment variables are set
test_env_vars() {
    echo -e "${CYAN}Test 5: All required environment variables are set${NC}"

    # Load .env
    if [ -f "${PROJECT_ROOT}/.env" ]; then
        set -a
        source "${PROJECT_ROOT}/.env"
        set +a
    fi

    local all_vars_set=true

    # Slack
    if [ -n "$SLACK_BOT_TOKEN" ]; then
        pass_test "SLACK_BOT_TOKEN is set"
    else
        fail_test "SLACK_BOT_TOKEN is not set"
        all_vars_set=false
    fi

    if [ -n "$SLACK_TEAM_ID" ]; then
        pass_test "SLACK_TEAM_ID is set"
    else
        fail_test "SLACK_TEAM_ID is not set"
        all_vars_set=false
    fi

    # BigQuery
    if [ -n "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
        pass_test "GOOGLE_APPLICATION_CREDENTIALS is set"
    else
        fail_test "GOOGLE_APPLICATION_CREDENTIALS is not set"
        all_vars_set=false
    fi

    if [ -n "$GCP_PROJECT_ID" ]; then
        pass_test "GCP_PROJECT_ID is set"
    else
        fail_test "GCP_PROJECT_ID is not set"
        all_vars_set=false
    fi

    # Sentry
    if [ -n "$SENTRY_AUTH_TOKEN" ]; then
        pass_test "SENTRY_AUTH_TOKEN is set"
    else
        fail_test "SENTRY_AUTH_TOKEN is not set"
        all_vars_set=false
    fi

    if [ -n "$SENTRY_ORG_SLUG" ]; then
        pass_test "SENTRY_ORG_SLUG is set"
    else
        fail_test "SENTRY_ORG_SLUG is not set"
        all_vars_set=false
    fi

    echo ""
    if [ "$all_vars_set" = false ]; then
        return 1
    fi
}

# Test 6: BigQuery MCP server Python script exists and is valid
test_bigquery_script() {
    echo -e "${CYAN}Test 6: BigQuery MCP server script validation${NC}"

    local script="${PROJECT_ROOT}/scripts/mcp_servers/bigquery_server.py"

    if [ -f "$script" ]; then
        pass_test "bigquery_server.py exists"
    else
        fail_test "bigquery_server.py not found"
        return 1
    fi

    if python3 -m py_compile "$script" 2>/dev/null; then
        pass_test "bigquery_server.py has valid Python syntax"
    else
        fail_test "bigquery_server.py has syntax errors"
        return 1
    fi

    echo ""
}

# Test 7: Sentry MCP server Python script exists and is valid
test_sentry_script() {
    echo -e "${CYAN}Test 7: Sentry MCP server script validation${NC}"

    local script="${PROJECT_ROOT}/scripts/mcp_servers/sentry_server.py"

    if [ -f "$script" ]; then
        pass_test "sentry_server.py exists"
    else
        fail_test "sentry_server.py not found"
        return 1
    fi

    if python3 -m py_compile "$script" 2>/dev/null; then
        pass_test "sentry_server.py has valid Python syntax"
    else
        fail_test "sentry_server.py has syntax errors"
        return 1
    fi

    echo ""
}

# Test 8: credentials/ directory exists (for BigQuery)
test_credentials_dir() {
    echo -e "${CYAN}Test 8: credentials/ directory exists${NC}"

    if [ -d "${PROJECT_ROOT}/credentials" ]; then
        pass_test "credentials/ directory found"
    else
        fail_test "credentials/ directory not found (create for BigQuery service account key)"
        return 1
    fi
    echo ""
}

# Test 9: Setup guides exist for all 3 services
test_setup_guides() {
    echo -e "${CYAN}Test 9: Setup guides exist${NC}"

    local all_guides_exist=true

    if [ -f "${PROJECT_ROOT}/docs/slack_app_setup_guide.md" ]; then
        pass_test "slack_app_setup_guide.md exists"
    else
        fail_test "slack_app_setup_guide.md not found"
        all_guides_exist=false
    fi

    if [ -f "${PROJECT_ROOT}/docs/bigquery_mcp_setup_guide.md" ]; then
        pass_test "bigquery_mcp_setup_guide.md exists"
    else
        fail_test "bigquery_mcp_setup_guide.md not found"
        all_guides_exist=false
    fi

    if [ -f "${PROJECT_ROOT}/docs/sentry_mcp_setup_guide.md" ]; then
        pass_test "sentry_mcp_setup_guide.md exists"
    else
        fail_test "sentry_mcp_setup_guide.md not found"
        all_guides_exist=false
    fi

    echo ""
    if [ "$all_guides_exist" = false ]; then
        return 1
    fi
}

# Test 10: .env.example has all required variables
test_env_example() {
    echo -e "${CYAN}Test 10: .env.example has all required variables${NC}"

    local all_vars_present=true

    if grep -q "^SLACK_BOT_TOKEN=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "SLACK_BOT_TOKEN in .env.example"
    else
        fail_test "SLACK_BOT_TOKEN not in .env.example"
        all_vars_present=false
    fi

    if grep -q "^SLACK_TEAM_ID=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "SLACK_TEAM_ID in .env.example"
    else
        fail_test "SLACK_TEAM_ID not in .env.example"
        all_vars_present=false
    fi

    if grep -q "^GOOGLE_APPLICATION_CREDENTIALS=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "GOOGLE_APPLICATION_CREDENTIALS in .env.example"
    else
        fail_test "GOOGLE_APPLICATION_CREDENTIALS not in .env.example"
        all_vars_present=false
    fi

    if grep -q "^GCP_PROJECT_ID=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "GCP_PROJECT_ID in .env.example"
    else
        fail_test "GCP_PROJECT_ID not in .env.example"
        all_vars_present=false
    fi

    if grep -q "^SENTRY_AUTH_TOKEN=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "SENTRY_AUTH_TOKEN in .env.example"
    else
        fail_test "SENTRY_AUTH_TOKEN not in .env.example"
        all_vars_present=false
    fi

    if grep -q "^SENTRY_ORG_SLUG=" "${PROJECT_ROOT}/.env.example"; then
        pass_test "SENTRY_ORG_SLUG in .env.example"
    else
        fail_test "SENTRY_ORG_SLUG not in .env.example"
        all_vars_present=false
    fi

    echo ""
    if [ "$all_vars_present" = false ]; then
        return 1
    fi
}

# Main execution
print_header

# Run all tests
test_mcp_json_exists || true
test_mcp_json_valid || true
test_mcp_servers_configured || true
test_env_exists || true
test_env_vars || true
test_bigquery_script || true
test_sentry_script || true
test_credentials_dir || true
test_setup_guides || true
test_env_example || true

# Print summary
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Test Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Total Tests: $TOTAL_TESTS"
echo -e "${GREEN}Passed: $PASSED_TESTS${NC}"
echo -e "${RED}Failed: $FAILED_TESTS${NC}"
echo ""

# Calculate success rate
if [ "$TOTAL_TESTS" -gt 0 ]; then
    SUCCESS_RATE=$(echo "scale=1; $PASSED_TESTS * 100 / $TOTAL_TESTS" | bc)
    echo "Success Rate: ${SUCCESS_RATE}%"
    echo ""
fi

# Final verdict
if [ "$FAILED_TESTS" -eq 0 ]; then
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  ✅ All tests passed!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Start Claude Code: claude"
    echo "  2. All 3 MCP servers (Slack, BigQuery, Sentry) will be available"
    echo "  3. Test individual servers:"
    echo "     - bash scripts/test_slack_mcp.sh"
    echo "     - (Create test scripts for BigQuery and Sentry if needed)"
    echo ""
    exit 0
else
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${RED}  ❌ Some tests failed${NC}"
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Please review the errors above and:"
    echo "  1. Check .env configuration"
    echo "  2. Review setup guides:"
    echo "     - @docs/slack_app_setup_guide.md"
    echo "     - @docs/bigquery_mcp_setup_guide.md"
    echo "     - @docs/sentry_mcp_setup_guide.md"
    echo "  3. Ensure all required dependencies are installed"
    echo ""
    exit 1
fi
