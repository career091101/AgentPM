#!/usr/bin/env python3
"""
Update CLAUDE.md Script
Week 7 Day 4-5: CLAUDE.md自動更新スクリプト

This script:
1. Reads new rules from environment variable
2. Checks for duplicates in existing CLAUDE.md
3. Appends new rules to CLAUDE.md
4. Formats the output properly

Environment Variables:
- NEW_RULES: JSON array of new rules to add
"""

import json
import os
import sys
from datetime import datetime
from typing import List


def read_claude_md() -> str:
    """Read existing CLAUDE.md content"""
    claude_md_path = "CLAUDE.md"
    if os.path.exists(claude_md_path):
        with open(claude_md_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def is_duplicate_rule(new_rule: str, existing_content: str) -> bool:
    """Check if rule already exists in CLAUDE.md"""
    # Normalize for comparison (lowercase, remove extra spaces)
    new_rule_normalized = " ".join(new_rule.lower().split())

    # Split existing content into lines
    for line in existing_content.split("\n"):
        # Check bullet points
        if line.strip().startswith("-") or line.strip().startswith("*"):
            existing_rule = line.strip()[1:].strip()
            existing_rule_normalized = " ".join(existing_rule.lower().split())

            # Simple similarity check (exact match or high overlap)
            if new_rule_normalized in existing_rule_normalized or existing_rule_normalized in new_rule_normalized:
                return True

    return False


def append_rules_to_claude_md(new_rules: List[str]) -> bool:
    """Append new rules to CLAUDE.md"""
    claude_md_path = "CLAUDE.md"
    existing_content = read_claude_md()

    # Filter out duplicate rules
    unique_rules = []
    for rule in new_rules:
        if not is_duplicate_rule(rule, existing_content):
            unique_rules.append(rule)
        else:
            print(f"Skipping duplicate rule: {rule}")

    if not unique_rules:
        print("No new unique rules to add")
        return False

    # Prepare new section
    today = datetime.now().strftime("%Y-%m-%d")
    new_section = f"\n\n## Auto-Generated Rules ({today})\n\n"
    new_section += "The following rules were extracted from PR reviews:\n\n"

    for rule in unique_rules:
        new_section += f"- {rule}\n"

    # Append to CLAUDE.md
    with open(claude_md_path, "a", encoding="utf-8") as f:
        f.write(new_section)

    print(f"✅ Added {len(unique_rules)} new rules to CLAUDE.md")
    for rule in unique_rules:
        print(f"  - {rule}")

    return True


def main():
    """Main entry point"""
    # Get new rules from environment variable
    new_rules_json = os.getenv("NEW_RULES")

    if not new_rules_json:
        print("No new rules to add (NEW_RULES not set)")
        sys.exit(0)

    try:
        new_rules = json.loads(new_rules_json)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse NEW_RULES as JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(new_rules, list):
        print(f"Error: NEW_RULES must be a JSON array", file=sys.stderr)
        sys.exit(1)

    if not new_rules:
        print("No new rules to add (empty array)")
        sys.exit(0)

    print(f"Processing {len(new_rules)} new rules...")

    # Append rules to CLAUDE.md
    success = append_rules_to_claude_md(new_rules)

    if success:
        print("✅ CLAUDE.md updated successfully")
    else:
        print("ℹ️  No changes made to CLAUDE.md")


if __name__ == "__main__":
    main()
