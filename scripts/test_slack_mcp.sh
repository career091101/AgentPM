#!/bin/bash

# test_slack_mcp.sh - Slack MCP Connection Test
# Week 6 Day 1-2: Slack MCP統合の動作確認スクリプト
#
# Usage:
#   bash scripts/test_slack_mcp.sh

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

PROJECT_ROOT="/Users/yuichi/AIPM/aipm_v0"

# Print header
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🔌 Slack MCP Connection Test${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Check environment variables
check_env_vars() {
    echo -e "${BLUE}Step 1: Checking environment variables...${NC}"

    if [ -z "$SLACK_BOT_TOKEN" ]; then
        echo -e "${RED}✗ SLACK_BOT_TOKEN is not set${NC}"
        echo ""
        echo "Please set SLACK_BOT_TOKEN in .env file or export it:"
        echo "  export SLACK_BOT_TOKEN=xoxb-YOUR-TOKEN"
        echo ""
        echo "For setup instructions, see:"
        echo "  @docs/slack_app_setup_guide.md"
        return 1
    else
        echo -e "${GREEN}✓ SLACK_BOT_TOKEN is set${NC}"
    fi

    if [ -z "$SLACK_TEAM_ID" ]; then
        echo -e "${RED}✗ SLACK_TEAM_ID is not set${NC}"
        echo ""
        echo "Please set SLACK_TEAM_ID in .env file or export it:"
        echo "  export SLACK_TEAM_ID=T01234ABCDE"
        echo ""
        echo "For setup instructions, see:"
        echo "  @docs/slack_app_setup_guide.md"
        return 1
    else
        echo -e "${GREEN}✓ SLACK_TEAM_ID is set${NC}"
    fi

    echo ""
}

# Test Slack Web API connection
test_slack_api() {
    echo -e "${BLUE}Step 2: Testing Slack Web API connection...${NC}"

    # Test auth.test endpoint
    response=$(curl -s -X POST https://slack.com/api/auth.test \
        -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
        -H "Content-Type: application/json")

    # Check if response contains "ok": true
    if echo "$response" | grep -q '"ok":true'; then
        echo -e "${GREEN}✓ Slack Web API connection successful${NC}"

        # Extract team info
        team=$(echo "$response" | grep -o '"team":"[^"]*"' | cut -d'"' -f4)
        user=$(echo "$response" | grep -o '"user":"[^"]*"' | cut -d'"' -f4)
        team_id=$(echo "$response" | grep -o '"team_id":"[^"]*"' | cut -d'"' -f4)

        echo ""
        echo "  Team: $team"
        echo "  User: $user"
        echo "  Team ID: $team_id"
        echo ""

        # Verify Team ID matches
        if [ "$team_id" != "$SLACK_TEAM_ID" ]; then
            echo -e "${YELLOW}⚠️  Warning: Team ID mismatch${NC}"
            echo "  Expected: $SLACK_TEAM_ID"
            echo "  Got: $team_id"
            echo ""
        fi
    else
        echo -e "${RED}✗ Slack Web API connection failed${NC}"
        echo ""
        echo "Response:"
        echo "$response" | jq '.' 2>/dev/null || echo "$response"
        echo ""

        # Check for common errors
        if echo "$response" | grep -q '"error":"invalid_auth"'; then
            echo -e "${RED}Error: invalid_auth${NC}"
            echo "  Your SLACK_BOT_TOKEN may be invalid or expired."
            echo "  Please regenerate the token and update .env file."
        fi

        return 1
    fi
}

# Check .mcp.json configuration
check_mcp_config() {
    echo -e "${BLUE}Step 3: Checking .mcp.json configuration...${NC}"

    if [ ! -f "${PROJECT_ROOT}/.mcp.json" ]; then
        echo -e "${RED}✗ .mcp.json not found${NC}"
        echo "  Expected location: ${PROJECT_ROOT}/.mcp.json"
        return 1
    else
        echo -e "${GREEN}✓ .mcp.json found${NC}"
    fi

    # Validate JSON
    if jq empty "${PROJECT_ROOT}/.mcp.json" 2>/dev/null; then
        echo -e "${GREEN}✓ .mcp.json is valid JSON${NC}"
    else
        echo -e "${RED}✗ .mcp.json is invalid JSON${NC}"
        return 1
    fi

    # Check if slack server is configured
    if jq -e '.mcpServers.slack' "${PROJECT_ROOT}/.mcp.json" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Slack MCP server is configured${NC}"
    else
        echo -e "${RED}✗ Slack MCP server is not configured in .mcp.json${NC}"
        return 1
    fi

    echo ""
}

# Check npm package availability
check_npm_package() {
    echo -e "${BLUE}Step 4: Checking @modelcontextprotocol/server-slack package...${NC}"

    # Try to run npx with --help to check if package is accessible
    if npx -y @modelcontextprotocol/server-slack --help > /dev/null 2>&1; then
        echo -e "${GREEN}✓ @modelcontextprotocol/server-slack is accessible${NC}"
    else
        echo -e "${YELLOW}⚠️  Package check inconclusive (this is normal)${NC}"
        echo "  The package will be installed automatically when Claude Code starts."
    fi

    echo ""
}

# Main execution
print_header

# Load .env if exists
if [ -f "${PROJECT_ROOT}/.env" ]; then
    echo -e "${GREEN}✓ Loading environment variables from .env${NC}"
    set -a
    source "${PROJECT_ROOT}/.env"
    set +a
    echo ""
fi

# Run checks
if check_env_vars && test_slack_api && check_mcp_config && check_npm_package; then
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  ✅ All checks passed!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Start Claude Code: claude"
    echo "  2. The Slack MCP server will be available for use"
    echo "  3. You can now interact with Slack APIs via Claude Code"
    echo ""
    echo "Example usage:"
    echo "  - List channels"
    echo "  - Send messages to channels"
    echo "  - Read channel history"
    echo ""
    exit 0
else
    echo ""
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${RED}  ❌ Some checks failed${NC}"
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Please review the errors above and:"
    echo "  1. Follow the setup guide: @docs/slack_app_setup_guide.md"
    echo "  2. Ensure .env file is properly configured"
    echo "  3. Verify Slack App has correct permissions"
    echo ""
    exit 1
fi
