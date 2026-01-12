#!/usr/bin/env python3
"""
Solopreneur Research 386件 → 23スキル 完全マッピング v2.0

改善点:
- 23スキル全てに対応
- App/Newsletter/SNS各カテゴリの構造差異を考慮
- 重複検出（duplicate_ofフィールド）
- より詳細な選定理由
"""

import os
import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple, Set
import yaml

BASE_DIR = Path(__file__).parent.parent
RESEARCH_DIR = BASE_DIR / "Solopreneur_Research" / "documents"
OUTPUT_CSV = BASE_DIR / "knowledge_base" / "tier2_mapping_matrix.csv"

# 23スキルの完全定義
SKILL_RULES = {
    # Phase 1: 需要発見・仮説検証
    "discover-demand": {
        "keywords": ["demand", "customer_research", "problem_validation", "initial_users"],
        "fields": ["growth_strategies", "success_pattern"],
        "category_weight": {"app": 15, "newsletter": 15, "sns": 10}
    },
    "validate-solo-fit": {
        "keywords": ["solo", "indie", "build_in_public", "bootstrapped", "one_person"],
        "fields": ["tags.success_pattern", "growth_strategies"],
        "category_weight": {"app": 25, "newsletter": 5, "sns": 5}
    },

    # Phase 2: CPF/PSF/PMF検証
    "validate-cpf": {
        "keywords": ["cpf", "problem_solution_fit", "mvp", "early_adopter"],
        "fields": ["success_pattern"],
        "category_weight": {"app": 10, "newsletter": 3, "sns": 5}
    },
    "validate-psf": {
        "keywords": ["psf", "prototype", "beta", "validation"],
        "fields": ["success_pattern"],
        "category_weight": {"app": 10, "newsletter": 3, "sns": 5}
    },
    "validate-pmf": {
        "keywords": ["pmf", "product_market_fit", "retention", "revenue_proof"],
        "fields": ["success_pattern", "monetization"],
        "category_weight": {"app": 10, "newsletter": 3, "sns": 5}
    },

    # Phase 3: AARRR分析・グロース
    "analyze-aarrr": {
        "keywords": ["aarrr", "acquisition", "activation", "retention", "revenue", "referral"],
        "fields": ["metrics", "growth_strategies"],
        "category_weight": {"app": 8, "newsletter": 2, "sns": 3}
    },
    "build-waitlist": {
        "keywords": ["waitlist", "pre_launch", "early_access", "beta_signup"],
        "fields": ["growth_strategies", "marketing_channel"],
        "category_weight": {"app": 5, "newsletter": 10, "sns": 5}
    },
    "design-pricing": {
        "keywords": ["pricing", "subscription", "tier", "freemium", "paid_plan"],
        "fields": ["monetization", "revenue"],
        "category_weight": {"app": 15, "newsletter": 5, "sns": 2}
    },

    # Phase 4: マーケティング・集客
    "create-bip-strategy": {
        "keywords": ["build_in_public", "twitter", "x_twitter", "transparency", "community"],
        "fields": ["tags.success_pattern", "growth_strategies", "marketing_channel"],
        "category_weight": {"app": 15, "newsletter": 8, "sns": 20}
    },
    "automate-sns-posting": {
        "keywords": ["automation", "scheduling", "sns", "social_media", "posting"],
        "fields": ["tags.tech_stack", "marketing_channel"],
        "category_weight": {"app": 5, "newsletter": 3, "sns": 20}
    },
    "create-content-flywheel": {
        "keywords": ["content", "flywheel", "multi_channel", "cross_promotion"],
        "fields": ["marketing_channel", "content_style"],
        "category_weight": {"app": 10, "newsletter": 20, "sns": 15}
    },

    # Phase 5: ソロプレナー特化
    "design-micro-saas-model": {
        "keywords": ["micro_saas", "saas", "subscription", "mrr", "arr"],
        "fields": ["main_product.category", "revenue"],
        "category_weight": {"app": 30, "newsletter": 0, "sns": 0}
    },
    "optimize-tool-stack": {
        "keywords": ["tech_stack", "tools", "no_code", "automation", "efficiency"],
        "fields": ["tags.tech_stack"],
        "category_weight": {"app": 20, "newsletter": 3, "sns": 2}
    },
    "design-boilerplate": {
        "keywords": ["boilerplate", "template", "starter_kit", "shipfast"],
        "fields": ["tags.success_pattern", "main_product.name"],
        "category_weight": {"app": 15, "newsletter": 0, "sns": 0}
    },

    # Phase 6: 成長・最適化
    "collect-user-feedback": {
        "keywords": ["feedback", "user_interview", "survey", "testimonial"],
        "fields": ["growth_strategies"],
        "category_weight": {"app": 10, "newsletter": 5, "sns": 5}
    },
    "identify-growth-levers": {
        "keywords": ["growth_lever", "viral", "referral", "network_effect"],
        "fields": ["growth_strategies", "success_pattern"],
        "category_weight": {"app": 10, "newsletter": 5, "sns": 5}
    },
    "refine-value-prop": {
        "keywords": ["value_proposition", "positioning", "differentiation"],
        "fields": ["success_pattern"],
        "category_weight": {"app": 10, "newsletter": 5, "sns": 5}
    },
    "track-kpis": {
        "keywords": ["kpi", "metrics", "analytics", "tracking"],
        "fields": ["metrics"],
        "category_weight": {"app": 10, "newsletter": 5, "sns": 5}
    },
    "optimize-conversion": {
        "keywords": ["conversion", "funnel", "cro", "landing_page"],
        "fields": ["growth_strategies"],
        "category_weight": {"app": 12, "newsletter": 3, "sns": 5}
    },
    "scale-marketing": {
        "keywords": ["scale", "paid_ads", "seo", "content_marketing"],
        "fields": ["growth_strategies", "marketing_channel"],
        "category_weight": {"app": 8, "newsletter": 5, "sns": 10}
    },
    "automate-operations": {
        "keywords": ["automation", "workflow", "efficiency", "zapier", "n8n"],
        "fields": ["tags.tech_stack"],
        "category_weight": {"app": 10, "newsletter": 3, "sns": 2}
    },
    "prepare-scaling": {
        "keywords": ["scale", "expansion", "team", "hiring"],
        "fields": ["growth_strategies"],
        "category_weight": {"app": 5, "newsletter": 2, "sns": 3}
    },
    "analyze-competitors": {
        "keywords": ["competitor", "competitive_analysis", "market_research"],
        "fields": ["growth_strategies"],
        "category_weight": {"app": 10, "newsletter": 5, "sns": 5}
    }
}


def extract_yaml_frontmatter(file_path: Path) -> Dict:
    """YAML Front Matter抽出"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    try:
        metadata = yaml.safe_load(match.group(1))
        return metadata if metadata else {}
    except yaml.YAMLError:
        return {}


def get_nested_value(data: Dict, path: str):
    """ネストされた辞書から値を取得 (例: "tags.tech_stack")"""
    keys = path.split('.')
    value = data
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        else:
            return None
        if value is None:
            return None
    return value


def check_duplicate(metadata: Dict) -> bool:
    """重複事例かチェック"""
    return metadata.get("duplicate_of") is not None


def determine_category(file_path: Path) -> str:
    """カテゴリ判定"""
    if "/01_App/" in str(file_path):
        return "app"
    elif "/02_Newsletter/" in str(file_path):
        return "newsletter"
    elif "/03_SNS/" in str(file_path):
        return "sns"
    return "unknown"


def match_skills_comprehensive(metadata: Dict, category: str) -> List[Tuple[str, str]]:
    """包括的スキルマッチング"""
    matched = []

    # 基本情報
    case_id = metadata.get("id", "")
    title = metadata.get("title", metadata.get("newsletter_name", ""))

    # App用フィールド
    tags = metadata.get("tags", {})
    revenue = metadata.get("revenue", {})
    main_product = metadata.get("main_product", {})

    # Newsletter用フィールド
    growth_strategies = metadata.get("growth_strategies", [])
    content_style = metadata.get("content_style", [])
    monetization = metadata.get("monetization", [])
    marketing_channel = metadata.get("marketing_channel", [])

    # SNS用フィールド（cross_referenceでAppと紐付け）
    cross_ref = metadata.get("cross_reference", {})

    # 全スキルをチェック
    for skill_name, rule in SKILL_RULES.items():
        keywords = rule.get("keywords", [])
        fields = rule.get("fields", [])
        reason = None

        # キーワードマッチング（全フィールドを文字列化して検索）
        metadata_str = str(metadata).lower()
        matched_keywords = [kw for kw in keywords if kw.lower() in metadata_str]

        if matched_keywords:
            reason = f"キーワード一致: {', '.join(matched_keywords[:2])}"

        # フィールド特化マッチング
        if not reason:
            for field in fields:
                value = get_nested_value(metadata, field)
                if value:
                    if isinstance(value, list) and len(value) > 0:
                        reason = f"{field}に該当: {', '.join(str(v) for v in value[:2])}"
                        break
                    elif isinstance(value, str):
                        reason = f"{field}に該当: {value[:30]}"
                        break
                    elif isinstance(value, dict) and len(value) > 0:
                        reason = f"{field}データ存在"
                        break

        # スキル別特殊ロジック
        if not reason:
            # design-micro-saas-model: MRR/ARRが存在する場合
            if skill_name == "design-micro-saas-model":
                mrr = revenue.get("mrr_usd") or metadata.get("mrr_usd")
                if mrr and mrr > 0:
                    reason = f"MRR ${mrr:,}/月"

            # validate-solo-fit: solo/indie/bootstrapキーワード
            elif skill_name == "validate-solo-fit":
                if any(kw in metadata_str for kw in ["solo", "indie", "bootstrap", "build_in_public"]):
                    reason = "ソロプレナー特性"

            # create-bip-strategy: Build in Public戦略
            elif skill_name == "create-bip-strategy":
                if "build_in_public" in str(tags.get("success_pattern", [])):
                    reason = "Build in Public戦略"
                elif "x_twitter" in marketing_channel or "twitter" in marketing_channel:
                    reason = "Twitter/X活用"

            # optimize-tool-stack: 技術スタック明記
            elif skill_name == "optimize-tool-stack":
                tech_stack = tags.get("tech_stack", [])
                if tech_stack and len(tech_stack) >= 2:
                    reason = f"技術スタック: {', '.join(tech_stack[:3])}"

            # create-content-flywheel: マルチチャネル
            elif skill_name == "create-content-flywheel":
                if len(marketing_channel) >= 2:
                    reason = f"マルチチャネル: {', '.join(marketing_channel[:2])}"

        if reason:
            matched.append((skill_name, reason))

    return matched


def process_all_cases() -> List[Dict]:
    """全事例処理"""
    results = []
    duplicates_skipped = 0

    for category_dir in ["01_App", "02_Newsletter", "03_SNS"]:
        case_dir = RESEARCH_DIR / category_dir / "case_studies"
        if not case_dir.exists():
            print(f"⚠️  {case_dir} が存在しません")
            continue

        for md_file in sorted(case_dir.glob("*.md")):
            metadata = extract_yaml_frontmatter(md_file)
            if not metadata:
                continue

            # 重複チェック
            if check_duplicate(metadata):
                duplicates_skipped += 1
                continue

            case_id = metadata.get("id", md_file.stem)
            case_title = metadata.get("title", metadata.get("newsletter_name", metadata.get("subject", {}).get("name", "Unknown")))
            category = determine_category(md_file)

            # スキルマッチング
            matched_skills = match_skills_comprehensive(metadata, category)

            # 各スキルごとに1行追加
            for skill_name, reason in matched_skills:
                results.append({
                    "skill_name": skill_name,
                    "case_id": case_id,
                    "case_title": case_title,
                    "category": category,
                    "selection_reason": reason
                })

    print(f"\n📊 処理サマリー:")
    print(f"   重複スキップ: {duplicates_skipped}件")

    return results


def write_csv(results: List[Dict]):
    """CSV出力"""
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["skill_name", "case_id", "case_title", "category", "selection_reason"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for row in sorted(results, key=lambda x: (x["skill_name"], x["category"], x["case_id"])):
            writer.writerow(row)

    print(f"\n✅ CSV出力完了: {OUTPUT_CSV}")
    print(f"   総行数: {len(results)}行")


def print_statistics(results: List[Dict]):
    """統計表示"""
    from collections import Counter

    print("\n" + "="*60)
    print("📊 マッピング統計（23スキル）")
    print("="*60)

    skill_counts = Counter([r["skill_name"] for r in results])
    for skill, count in sorted(skill_counts.items()):
        print(f"   {skill:30s}: {count:3d}件")

    print("\n" + "="*60)
    print("📊 カテゴリ別統計")
    print("="*60)
    category_counts = Counter([r["category"] for r in results])
    for category, count in category_counts.items():
        print(f"   {category:12s}: {count:3d}件")

    # 目標配分との比較
    print("\n" + "="*60)
    print("🎯 目標配分との比較（主要スキル）")
    print("="*60)

    target_skills = {
        "validate-solo-fit": {"app": 25, "newsletter": 5, "sns": 5},
        "create-bip-strategy": {"app": 15, "newsletter": 8, "sns": 20},
        "design-micro-saas-model": {"app": 30, "newsletter": 0, "sns": 0},
        "optimize-tool-stack": {"app": 20, "newsletter": 3, "sns": 2},
        "create-content-flywheel": {"app": 10, "newsletter": 20, "sns": 15}
    }

    for skill, targets in target_skills.items():
        actual = {}
        for r in results:
            if r["skill_name"] == skill:
                cat = r["category"]
                actual[cat] = actual.get(cat, 0) + 1

        print(f"\n   {skill}:")
        for cat, target in targets.items():
            act = actual.get(cat, 0)
            status = "✅" if act >= target * 0.8 else "⚠️"
            print(f"      {cat:12s}: 目標{target:2d}件 → 実際{act:2d}件 {status}")


def main():
    print("🚀 Solopreneur Research → 23スキル 完全マッピング v2.0")
    print(f"   入力: {RESEARCH_DIR}")
    print(f"   出力: {OUTPUT_CSV}\n")

    results = process_all_cases()
    write_csv(results)
    print_statistics(results)


if __name__ == "__main__":
    main()
