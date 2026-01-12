#!/usr/bin/env python3
"""
Tier 3-8のinterview_countとproblem_commonalityのnullフィールドを補完するスクリプト

実行方法:
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research
python3 scripts/補完_null_fields.py
"""

import re
import os
from pathlib import Path

# ベースディレクトリ
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents")

# 業界別の標準値
INDUSTRY_DEFAULTS = {
    # AI業界
    "ai": {"interview_count": 30, "problem_commonality": 40},
    "generative_ai": {"interview_count": 25, "problem_commonality": 35},

    # B2B SaaS
    "saas": {"interview_count": 25, "problem_commonality": 65},
    "enterprise": {"interview_count": 20, "problem_commonality": 70},
    "b2b": {"interview_count": 25, "problem_commonality": 65},
    "productivity": {"interview_count": 30, "problem_commonality": 65},

    # Consumer
    "social": {"interview_count": 50, "problem_commonality": 55},
    "consumer": {"interview_count": 50, "problem_commonality": 55},
    "marketplace": {"interview_count": 40, "problem_commonality": 50},
    "fintech": {"interview_count": 35, "problem_commonality": 60},

    # Hardware / Deep Tech
    "hardware": {"interview_count": 15, "problem_commonality": 40},
    "aerospace": {"interview_count": 10, "problem_commonality": 30},
    "biotech": {"interview_count": 15, "problem_commonality": 35},
    "energy": {"interview_count": 10, "problem_commonality": 40},

    # Web3
    "crypto": {"interview_count": 20, "problem_commonality": 15},
    "blockchain": {"interview_count": 20, "problem_commonality": 15},
    "web3": {"interview_count": 20, "problem_commonality": 15},
    "nft": {"interview_count": 15, "problem_commonality": 10},

    # Developer Tools
    "developer_tools": {"interview_count": 30, "problem_commonality": 45},
    "devops": {"interview_count": 25, "problem_commonality": 50},

    # Gaming
    "gaming": {"interview_count": 40, "problem_commonality": 45},
    "game": {"interview_count": 30, "problem_commonality": 70},

    # Japan EC
    "ecommerce": {"interview_count": 25, "problem_commonality": 60},
    "fashion": {"interview_count": 25, "problem_commonality": 60},
    "ec": {"interview_count": 25, "problem_commonality": 60},

    # Japan SNS
    "sns": {"interview_count": 50, "problem_commonality": 75},
    "messaging": {"interview_count": 50, "problem_commonality": 75},

    # Default
    "default": {"interview_count": 20, "problem_commonality": 50}
}

def extract_tags(content):
    """YAMLフロントマターからtagsを抽出"""
    match = re.search(r'tags:\s*\[(.*?)\]', content)
    if match:
        tags_str = match.group(1)
        tags = [tag.strip().strip('"\'') for tag in tags_str.split(',')]
        return tags
    return []

def extract_industry(content):
    """industryフィールドを抽出"""
    match = re.search(r'industry:\s*"([^"]+)"', content)
    if match:
        return match.group(1).lower()
    return None

def determine_defaults(tags, industry):
    """タグと業界から適切なデフォルト値を決定"""
    # タグから業界を推定
    for tag in tags:
        tag_lower = tag.lower()
        if tag_lower in INDUSTRY_DEFAULTS:
            return INDUSTRY_DEFAULTS[tag_lower]

    # industryフィールドから推定
    if industry:
        for key in INDUSTRY_DEFAULTS:
            if key in industry:
                return INDUSTRY_DEFAULTS[key]

    # デフォルト値
    return INDUSTRY_DEFAULTS["default"]

def get_estimation_comment(field, value, tags, industry, tier):
    """推定根拠のコメントを生成"""
    if field == "interview_count":
        if tier == "pivot":
            return f"  # 推定: ピボット前後の顧客調査を合算、{tags}業界標準"
        elif tier == "failure":
            if value == 0:
                return "  # 情報源なし、プロダクト主導型と推測"
            else:
                return f"  # 推定: 失敗原因分析より、{tags}業界の最低限実施数"
        elif tier == "emerging":
            return f"  # 推定: 新興企業の標準インタビュー数、{tags}業界"
        else:
            return f"  # 推定: {tags}業界標準"

    elif field == "problem_commonality":
        if "ai" in tags or "generative_ai" in tags:
            return f"  # 推定: AI業界標準値30-50%、新興市場"
        elif "web3" in tags or "crypto" in tags or "blockchain" in tags or "nft" in tags:
            return f"  # 推定: Web3業界標準値10-20%、超ニッチ市場"
        elif "enterprise" in tags or "saas" in tags or "b2b" in tags:
            return f"  # 推定: B2B SaaS業界標準値60-70%"
        elif "hardware" in tags:
            return f"  # 推定: ハードウェア業界標準値、製造課題の共通性"
        else:
            return f"  # 推定: {tags}業界標準値、市場調査データ不足"

    return ""

def update_file(filepath):
    """単一ファイルのnullフィールドを補完"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # タグと業界を抽出
    tags = extract_tags(content)
    industry = extract_industry(content)

    # tierを判定
    if "06_Pivot_Success" in str(filepath):
        tier = "pivot"
    elif "07_Failure_Study" in str(filepath):
        tier = "failure"
    elif "08_Emerging" in str(filepath):
        tier = "emerging"
    else:
        tier = "unknown"

    # デフォルト値を決定
    defaults = determine_defaults(tags, industry)

    # interview_countの補完
    if "interview_count: null" in content:
        # Failureで情報源なしの場合は0にする確率が高い
        if tier == "failure" and ("hardware" in tags or "overfunding" in tags):
            value = 0
            comment = "  # 情報源なし、プロダクト主導型・ハードウェア中心と推測"
        else:
            value = defaults["interview_count"]
            comment = get_estimation_comment("interview_count", value, tags, industry, tier)

        content = content.replace(
            "interview_count: null",
            f"interview_count: {value}{comment}"
        )

    # problem_commonalityの補完
    if "problem_commonality: null" in content:
        value = defaults["problem_commonality"]
        comment = get_estimation_comment("problem_commonality", value, tags, industry, tier)

        content = content.replace(
            "problem_commonality: null",
            f"problem_commonality: {value}{comment}"
        )

    # ファイルに書き戻し
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath.name

def main():
    """メイン処理"""
    tiers = [
        "03_VC_Backed",
        "04_IPO_Japan",
        "05_IPO_Global",
        "06_Pivot_Success",
        "07_Failure_Study",
        "08_Emerging"
    ]

    updated_files = []

    for tier in tiers:
        tier_dir = BASE_DIR / tier
        if not tier_dir.exists():
            continue

        print(f"\n{'='*60}")
        print(f"Processing {tier}...")
        print(f"{'='*60}")

        for md_file in tier_dir.glob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            has_null = "interview_count: null" in content or "problem_commonality: null" in content

            if has_null:
                filename = update_file(md_file)
                updated_files.append(f"{tier}/{filename}")
                print(f"✓ {filename}")

    print(f"\n{'='*60}")
    print(f"Summary: {len(updated_files)} files updated")
    print(f"{'='*60}")

    if updated_files:
        print("\nUpdated files:")
        for f in updated_files[:20]:  # 最初の20件のみ表示
            print(f"  - {f}")
        if len(updated_files) > 20:
            print(f"  ... and {len(updated_files) - 20} more")

if __name__ == "__main__":
    main()
