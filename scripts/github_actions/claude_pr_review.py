#!/usr/bin/env python3
"""
Claude PR Review Script
Week 7 Day 3-5: GitHub Action用PRレビュースクリプト

This script:
1. Fetches PR diff from GitHub API
2. Sends diff to Claude API for review
3. Extracts review comments and new rules
4. Outputs results for GitHub Action

Environment Variables:
- ANTHROPIC_API_KEY: Anthropic API key
- PR_NUMBER: Pull Request number
- GITHUB_TOKEN: GitHub token for API access
- GITHUB_REPOSITORY: Repository name (owner/repo)
"""

import json
import os
import sys
from typing import Dict, List, Optional

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed", file=sys.stderr)
    print("Install with: pip install anthropic", file=sys.stderr)
    sys.exit(1)

try:
    import requests
except ImportError:
    print("Error: requests package not installed", file=sys.stderr)
    print("Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


def get_pr_diff(pr_number: int, github_token: str, repo: str) -> Optional[str]:
    """Fetch PR diff from GitHub API"""
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3.diff",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching PR diff: {e}", file=sys.stderr)
        return None


def get_pr_info(pr_number: int, github_token: str, repo: str) -> Optional[Dict]:
    """Fetch PR information from GitHub API"""
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching PR info: {e}", file=sys.stderr)
        return None


def read_claude_md() -> str:
    """Read existing CLAUDE.md content"""
    claude_md_path = "CLAUDE.md"
    if os.path.exists(claude_md_path):
        with open(claude_md_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def review_pr_with_claude(
    pr_info: Dict, pr_diff: str, claude_md: str, api_key: str
) -> Dict[str, str]:
    """Send PR to Claude API for review"""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are a senior software engineer reviewing a Pull Request.

**PR Information:**
- Title: {pr_info.get('title', 'N/A')}
- Description: {pr_info.get('body', 'N/A')}
- Author: {pr_info.get('user', {}).get('login', 'N/A')}
- Files changed: {pr_info.get('changed_files', 0)}

**Existing Project Rules (CLAUDE.md):**
{claude_md[:2000] if claude_md else "No existing rules"}

**PR Diff:**
```diff
{pr_diff[:10000]}  # Limit to 10000 chars to avoid token limits
```

**Task:**
1. Review the code changes for:
   - Security vulnerabilities
   - Performance issues
   - Code quality and best practices
   - Test coverage
   - Documentation completeness

2. Extract any new project-wide rules that should be added to CLAUDE.md
   - Only include rules that are general and reusable
   - Avoid rules specific to this PR only
   - Format as bullet points

**Output Format:**
Please provide your response in the following JSON format:
{{
  "review_summary": "Brief summary of the review",
  "issues": [
    {{"severity": "high|medium|low", "description": "Issue description", "suggestion": "How to fix"}}
  ],
  "new_rules": [
    "Rule 1 description",
    "Rule 2 description"
  ],
  "overall_assessment": "approve|request_changes|comment"
}}
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = message.content[0].text

        # Try to extract JSON from response
        # Claude might wrap JSON in markdown code blocks
        if "```json" in response_text:
            json_start = response_text.index("```json") + 7
            json_end = response_text.rindex("```")
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.index("```") + 3
            json_end = response_text.rindex("```")
            response_text = response_text[json_start:json_end].strip()

        result = json.loads(response_text)
        return result

    except anthropic.APIError as e:
        print(f"Claude API error: {e}", file=sys.stderr)
        return {"error": str(e)}
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}", file=sys.stderr)
        print(f"Response text: {response_text}", file=sys.stderr)
        return {"error": "Failed to parse Claude response as JSON"}
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return {"error": str(e)}


def format_review_comment(review: Dict) -> str:
    """Format review result as GitHub comment"""
    if "error" in review:
        return f"❌ **Claude Review Error**\n\n{review['error']}"

    comment = "## 🤖 Claude Code Review\n\n"

    # Summary
    comment += f"**Summary:** {review.get('review_summary', 'N/A')}\n\n"

    # Overall Assessment
    assessment = review.get('overall_assessment', 'comment')
    if assessment == 'approve':
        comment += "✅ **Recommendation:** Approve\n\n"
    elif assessment == 'request_changes':
        comment += "⚠️ **Recommendation:** Request Changes\n\n"
    else:
        comment += "💬 **Recommendation:** Comment\n\n"

    # Issues
    issues = review.get('issues', [])
    if issues:
        comment += "### Issues Found\n\n"
        for i, issue in enumerate(issues, 1):
            severity = issue.get('severity', 'medium')
            emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(severity, '⚪')
            comment += f"{i}. {emoji} **{severity.upper()}**: {issue.get('description', 'N/A')}\n"
            if issue.get('suggestion'):
                comment += f"   - **Suggestion:** {issue['suggestion']}\n"
            comment += "\n"

    # New Rules
    new_rules = review.get('new_rules', [])
    if new_rules:
        comment += "### 📝 New Rules to Add to CLAUDE.md\n\n"
        for rule in new_rules:
            comment += f"- {rule}\n"
        comment += "\n"

    comment += "---\n"
    comment += "*🤖 Generated with Claude Code*\n"

    return comment


def set_github_output(name: str, value: str):
    """Set GitHub Action output"""
    github_output = os.getenv("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            # Escape newlines for multiline output
            value_escaped = value.replace("\n", "%0A").replace("\r", "%0D")
            f.write(f"{name}={value_escaped}\n")
    else:
        # Fallback for local testing
        print(f"::set-output name={name}::{value}")


def main():
    """Main entry point"""
    # Get environment variables
    api_key = os.getenv("ANTHROPIC_API_KEY")
    pr_number = os.getenv("PR_NUMBER")
    github_token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")

    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    if not pr_number:
        print("Error: PR_NUMBER not set", file=sys.stderr)
        sys.exit(1)

    if not github_token:
        print("Error: GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    if not repo:
        print("Error: GITHUB_REPOSITORY not set", file=sys.stderr)
        sys.exit(1)

    pr_number = int(pr_number)

    # Fetch PR info and diff
    print(f"Fetching PR #{pr_number} from {repo}...")
    pr_info = get_pr_info(pr_number, github_token, repo)
    if not pr_info:
        print("Failed to fetch PR info", file=sys.stderr)
        sys.exit(1)

    pr_diff = get_pr_diff(pr_number, github_token, repo)
    if not pr_diff:
        print("Failed to fetch PR diff", file=sys.stderr)
        sys.exit(1)

    # Read CLAUDE.md
    print("Reading CLAUDE.md...")
    claude_md = read_claude_md()

    # Review with Claude
    print("Sending to Claude for review...")
    review = review_pr_with_claude(pr_info, pr_diff, claude_md, api_key)

    # Format comment
    review_comment = format_review_comment(review)
    print("\n--- Review Comment ---")
    print(review_comment)
    print("--- End Review Comment ---\n")

    # Set GitHub Action outputs
    set_github_output("review_comment", review_comment)

    # Extract new rules
    new_rules = review.get('new_rules', [])
    if new_rules:
        new_rules_json = json.dumps(new_rules)
        set_github_output("new_rules", new_rules_json)
        print(f"New rules to add: {new_rules}")
    else:
        set_github_output("new_rules", "")

    print("✅ Review completed successfully")


if __name__ == "__main__":
    main()
