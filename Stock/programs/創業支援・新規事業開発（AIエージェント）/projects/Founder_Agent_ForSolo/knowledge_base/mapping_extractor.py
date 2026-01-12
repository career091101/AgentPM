#!/usr/bin/env python3
"""
Solopreneur Research 386件から23スキルへのマッピング表作成スクリプト

入力: Solopreneur_Research/documents/{01_App,02_Newsletter,03_SNS}/case_studies/*.md
出力: knowledge_base/tier2_mapping_matrix.csv
"""

import os
import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple
import yaml

# パス設定
BASE_DIR = Path(__file__).parent.parent
RESEARCH_DIR = BASE_DIR / "Solopreneur_Research" / "documents"
OUTPUT_CSV = BASE_DIR / "knowledge_base" / "tier2_mapping_matrix.csv"

# 23スキルのマッピング方針（ユーザー提供）
SKILL_MAPPING_RULES = {
    "validate-solo-fit": {
        "target_count": {"app": 25, "newsletter": 5, "sns": 5},
        "criteria": [
            "1人実行可能性が明示",
            "コスト最小化戦略",
            "Build in Public",
            "数日でMVP構築"
        ]
    },
    "create-bip-strategy": {
        "target_count": {"app": 15, "newsletter": 8, "sns": 20},
        "criteria": [
            "X/Twitter透明性",
            "フォロワー獲得戦略",
            "エンゲージメント施策",
            "コミュニティ形成"
        ]
    },
    "design-micro-saas-model": {
        "target_count": {"app": 30, "newsletter": 0, "sns": 0},
        "criteria": [
            "Micro-SaaS収益化",
            "サブスクリプションモデル",
            "月額課金",
            "ARR/MRR明記"
        ]
    },
    "optimize-tool-stack": {
        "target_count": {"app": 20, "newsletter": 3, "sns": 2},
        "criteria": [
            "技術スタック明記",
            "ノーコード/ローコード",
            "AI活用",
            "自動化ツール"
        ]
    },
    "create-content-flywheel": {
        "target_count": {"app": 10, "newsletter": 20, "sns": 15},
        "criteria": [
            "コンテンツマーケティング",
            "ニュースレター戦略",
            "SNS相乗効果",
            "フライホイール構築"
        ]
    },
    "discover-demand": {
        "target_count": {"app": 15, "newsletter": 15, "sns": 10},
        "criteria": [
            "需要発見プロセス",
            "顧客課題特定",
            "市場調査",
            "初期ユーザー獲得"
        ]
    },
    # 残り17スキル（簡略化）
    "validate-cpf": {"target_count": {"app": 10, "newsletter": 3, "sns": 5}, "criteria": ["CPFスコア"]},
    "validate-psf": {"target_count": {"app": 10, "newsletter": 3, "sns": 5}, "criteria": ["PSFスコア"]},
    "validate-pmf": {"target_count": {"app": 10, "newsletter": 3, "sns": 5}, "criteria": ["PMFスコア"]},
    "analyze-aarrr": {"target_count": {"app": 8, "newsletter": 2, "sns": 3}, "criteria": ["AARRR指標"]},
    "build-waitlist": {"target_count": {"app": 5, "newsletter": 10, "sns": 5}, "criteria": ["ウェイトリスト"]},
    "design-pricing": {"target_count": {"app": 15, "newsletter": 5, "sns": 2}, "criteria": ["価格戦略"]},
    "automate-sns-posting": {"target_count": {"app": 5, "newsletter": 3, "sns": 20}, "criteria": ["SNS自動化"]},
    "collect-user-feedback": {"target_count": {"app": 10, "newsletter": 5, "sns": 5}, "criteria": ["フィードバック"]},
    "identify-growth-levers": {"target_count": {"app": 10, "newsletter": 5, "sns": 5}, "criteria": ["成長レバー"]},
    "refine-value-prop": {"target_count": {"app": 10, "newsletter": 5, "sns": 5}, "criteria": ["価値提案"]},
    "track-kpis": {"target_count": {"app": 10, "newsletter": 5, "sns": 5}, "criteria": ["KPI追跡"]},
    "optimize-conversion": {"target_count": {"app": 12, "newsletter": 3, "sns": 5}, "criteria": ["コンバージョン"]},
    "scale-marketing": {"target_count": {"app": 8, "newsletter": 5, "sns": 10}, "criteria": ["マーケティング"]},
    "automate-operations": {"target_count": {"app": 10, "newsletter": 3, "sns": 2}, "criteria": ["運用自動化"]},
    "prepare-scaling": {"target_count": {"app": 5, "newsletter": 2, "sns": 3}, "criteria": ["スケール準備"]},
    "analyze-competitors": {"target_count": {"app": 10, "newsletter": 5, "sns": 5}, "criteria": ["競合分析"]},
    "design-boilerplate": {"target_count": {"app": 15, "newsletter": 0, "sns": 0}, "criteria": ["Boilerplate"]}
}


def extract_yaml_frontmatter(file_path: Path) -> Dict:
    """MDファイルからYAML Front Matterを抽出"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # YAML Front Matter抽出（---で囲まれた部分）
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    try:
        metadata = yaml.safe_load(match.group(1))
        return metadata if metadata else {}
    except yaml.YAMLError:
        return {}


def determine_category(file_path: Path) -> str:
    """ファイルパスからカテゴリ判定"""
    if "/01_App/" in str(file_path):
        return "app"
    elif "/02_Newsletter/" in str(file_path):
        return "newsletter"
    elif "/03_SNS/" in str(file_path):
        return "sns"
    return "unknown"


def match_skills(metadata: Dict, category: str, file_path: Path) -> List[Tuple[str, str]]:
    """メタデータとカテゴリから適用スキルを判定

    Returns:
        List of (skill_name, selection_reason)
    """
    matched_skills = []

    # タイトルと本文の簡易抽出
    title = metadata.get("title", "")
    tags = metadata.get("tags", {})
    revenue = metadata.get("revenue", {})

    # 各スキルの判定
    for skill_name, rule in SKILL_MAPPING_RULES.items():
        criteria = rule.get("criteria", [])
        reason = None

        # validate-solo-fit
        if skill_name == "validate-solo-fit":
            if any(keyword in str(tags) for keyword in ["solo", "build_in_public", "indie_maker"]):
                reason = "1人実行可能性が明示"
            elif (revenue.get("mrr_usd") or 0) > 0 and "solo" in str(metadata).lower():
                reason = "ソロ収益化成功"

        # create-bip-strategy
        elif skill_name == "create-bip-strategy":
            if any(keyword in str(tags) for keyword in ["build_in_public", "x_twitter", "community"]):
                reason = "Build in Public戦略"

        # design-micro-saas-model
        elif skill_name == "design-micro-saas-model":
            if category == "app" and (revenue.get("mrr_usd") or 0) > 0:
                reason = "Micro-SaaS収益モデル"

        # optimize-tool-stack
        elif skill_name == "optimize-tool-stack":
            tech_stack = tags.get("tech_stack", [])
            if tech_stack and len(tech_stack) > 0:
                reason = f"技術スタック明記: {', '.join(tech_stack[:3])}"

        # create-content-flywheel
        elif skill_name == "create-content-flywheel":
            marketing_channels = tags.get("marketing_channel", [])
            if len(marketing_channels) >= 2:
                reason = f"マルチチャネル戦略: {', '.join(marketing_channels[:2])}"

        if reason:
            matched_skills.append((skill_name, reason))

    return matched_skills


def process_all_cases() -> List[Dict]:
    """全事例を処理してマッピング結果生成"""
    results = []

    for category_dir in ["01_App", "02_Newsletter", "03_SNS"]:
        case_dir = RESEARCH_DIR / category_dir / "case_studies"
        if not case_dir.exists():
            continue

        for md_file in case_dir.glob("*.md"):
            metadata = extract_yaml_frontmatter(md_file)
            if not metadata:
                continue

            case_id = metadata.get("id", md_file.stem)
            case_title = metadata.get("title", "Unknown")
            category = determine_category(md_file)

            # スキルマッチング
            matched_skills = match_skills(metadata, category, md_file)

            # 各スキルごとに1行追加
            for skill_name, reason in matched_skills:
                results.append({
                    "skill_name": skill_name,
                    "case_id": case_id,
                    "case_title": case_title,
                    "category": category,
                    "selection_reason": reason
                })

    return results


def write_csv(results: List[Dict]):
    """CSV出力"""
    # knowledge_baseディレクトリ作成
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["skill_name", "case_id", "case_title", "category", "selection_reason"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"✅ CSV出力完了: {OUTPUT_CSV}")
    print(f"   総行数: {len(results)}行")


def main():
    print("🚀 Solopreneur Research → 23スキル マッピング開始")
    print(f"   入力: {RESEARCH_DIR}")
    print(f"   出力: {OUTPUT_CSV}\n")

    results = process_all_cases()
    write_csv(results)

    # 統計表示
    print("\n📊 マッピング統計:")
    from collections import Counter
    skill_counts = Counter([r["skill_name"] for r in results])
    for skill, count in skill_counts.most_common():
        print(f"   {skill}: {count}件")


if __name__ == "__main__":
    main()
