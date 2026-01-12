#!/usr/bin/env python3
"""
Bash execution test script for Trading Agent Skills
Tests whether Python scripts can be executed from within Claude Code skills
"""

import sys
import platform

def main():
    print("=" * 60)
    print("BASH EXECUTION TEST - SUCCESS")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Python executable: {sys.executable}")
    print("=" * 60)
    print("✅ File execution successful")
    print("✅ Claude Code skills CAN execute Python scripts via Bash")
    return 0

if __name__ == "__main__":
    sys.exit(main())
