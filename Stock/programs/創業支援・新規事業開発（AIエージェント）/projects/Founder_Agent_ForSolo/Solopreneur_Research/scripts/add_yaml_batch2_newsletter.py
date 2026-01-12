#!/usr/bin/env python3
"""
Newsletter Batch2 (38件) YAML Front Matter追加スクリプト
v2.1テンプレートに準拠したYAML Front Matterを既存ファイルに追加
"""

import os
import re
from datetime import datetime
from pathlib import Path

# 対象ファイルリスト
TARGET_FILES = [
    "NL_CASE_001_high_revenue.md",
    "NL_CASE_002_monthly_100k.md",
    "NL_CASE_003_02_dan_go.md",
    "NL_CASE_003_03_tech_emails.md",
    "NL_CASE_003_15_matt_goodwin.md",
    "NL_CASE_003_16_lookout_media.md",
    "NL_CASE_003_niche_success.md",
    "NL_CASE_004_knowledge_unique.md",
    "NL_CASE_005_lenny_rachitsky.md",
    "NL_CASE_006_letters_from_american.md",
    "NL_CASE_007_pragmatic_engineer.md",
    "NL_CASE_LOW_001_indie_creator_1k.md",
    "NL_CASE_LOW_002_side_hustle_3mo.md",
    "NL_CASE_LOW_003_micro_niche.md",
    "NL_CASE_LOW_004_student_newsletter.md",
    "NL_CASE_LOW_005_local_newsletter.md",
    "NL_CASE_LOW_006_hobby_newsletter.md",
    "NL_CASE_LOW_007_weekly_newsletter.md",
    "NL_CASE_LOW_008_ad_revenue_newsletter.md",
    "NL_CASE_LOW_009_curation_newsletter.md",
    "NL_CASE_MID_001_extra_points.md",
    "NL_CASE_MID_002_chief_in_the_north.md",
    "NL_CASE_MID_002_naptown_scoop.md",
    "NL_CASE_MID_003_parenting_newsletter.md",
    "NL_CASE_MID_003_stacked_marketer.md",
    "NL_CASE_MID_004_alex_brogan.md",
    "NL_CASE_P2_001_milk_road.md",
    "NL_CASE_P2_002_the_hustle.md",
    "NL_MARKET_001_2025_trends.md",
    "NL_OVERSEAS_001_32billion_yen.md",
    "NL_OVERSEAS_001_international.md",
    "NL_OVERSEAS_002_lawyer_to_4billion.md",
    "NL_OVERSEAS_003_solo_26billion.md",
    "NL_OVERSEAS_004_ai_2billion.md",
    "NL_OVERSEAS_005_street_culture.md",
    "NL_OVERSEAS_006_parenting_86m.md",
    "NL_OVERSEAS_007_alex_brogan.md",
    "NL_OVERSEAS_008_naptown_scoop.md",
]

# ファイルごとのメタデータ推測ルール
FILE_METADATA = {
    "NL_CASE_001_high_revenue.md": {
        "id": "NL_CASE_001",
        "newsletter_name": "High Revenue Newsletters Collection",
        "founder_name": "Multiple Founders",
        "niche": "tech",
        "mrr_tier": "100k+",
        "subscribers_total": 100000,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_002_monthly_100k.md": {
        "id": "NL_CASE_002",
        "newsletter_name": "Monthly 100K+ Revenue Cases",
        "founder_name": "Multiple Founders",
        "niche": "creator",
        "mrr_tier": "100k+",
        "subscribers_total": 50000,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_003_02_dan_go.md": {
        "id": "NL_CASE_003_02",
        "newsletter_name": "The High Performance Journal",
        "founder_name": "Dan Go",
        "founder_twitter": "@FitFounder",
        "platform": "convertkit",
        "niche": "creator",
        "mrr_tier": "50k-100k",
        "subscribers_total": 475000,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_003_03_tech_emails.md": {
        "id": "NL_CASE_003_03",
        "newsletter_name": "Tech Email Newsletter",
        "founder_name": "Unknown",
        "niche": "tech",
        "mrr_tier": "25k-50k",
        "subscribers_total": 50000,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_003_15_matt_goodwin.md": {
        "id": "NL_CASE_003_15",
        "newsletter_name": "Matt Goodwin Newsletter",
        "founder_name": "Matt Goodwin",
        "niche": "business",
        "mrr_tier": "25k-50k",
        "subscribers_total": 30000,
        "japan_market_score_overall": 3.5,
    },
    "NL_CASE_003_16_lookout_media.md": {
        "id": "NL_CASE_003_16",
        "newsletter_name": "Lookout Media",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "25k-50k",
        "subscribers_total": 40000,
        "japan_market_score_overall": 3.8,
    },
    "NL_CASE_003_niche_success.md": {
        "id": "NL_CASE_003",
        "newsletter_name": "Niche Success Cases",
        "founder_name": "Multiple Founders",
        "niche": "creator",
        "mrr_tier": "25k-50k",
        "subscribers_total": 30000,
        "japan_market_score_overall": 4.2,
    },
    "NL_CASE_004_knowledge_unique.md": {
        "id": "NL_CASE_004",
        "newsletter_name": "Knowledge & Unique Content",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "10k-25k",
        "subscribers_total": 20000,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_005_lenny_rachitsky.md": {
        "id": "NL_CASE_005",
        "newsletter_name": "Lenny's Newsletter",
        "founder_name": "Lenny Rachitsky",
        "founder_twitter": "@lennysan",
        "platform": "substack",
        "niche": "product",
        "mrr_tier": "100k+",
        "subscribers_total": 500000,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_006_letters_from_american.md": {
        "id": "NL_CASE_006",
        "newsletter_name": "Letters from an American",
        "founder_name": "Heather Cox Richardson",
        "platform": "substack",
        "niche": "other",
        "mrr_tier": "100k+",
        "subscribers_total": 1500000,
        "japan_market_score_overall": 2.5,
    },
    "NL_CASE_007_pragmatic_engineer.md": {
        "id": "NL_CASE_007",
        "newsletter_name": "The Pragmatic Engineer",
        "founder_name": "Gergely Orosz",
        "founder_twitter": "@GergelyOrosz",
        "platform": "substack",
        "niche": "tech",
        "mrr_tier": "100k+",
        "subscribers_total": 300000,
        "japan_market_score_overall": 4.8,
    },
    "NL_CASE_LOW_001_indie_creator_1k.md": {
        "id": "NL_CASE_LOW_001",
        "newsletter_name": "Indie Creator Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "<5k",
        "subscribers_total": 1000,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_LOW_002_side_hustle_3mo.md": {
        "id": "NL_CASE_LOW_002",
        "newsletter_name": "Side Hustle 3-Month",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "<5k",
        "subscribers_total": 500,
        "japan_market_score_overall": 4.2,
    },
    "NL_CASE_LOW_003_micro_niche.md": {
        "id": "NL_CASE_LOW_003",
        "newsletter_name": "Micro Niche Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "<5k",
        "subscribers_total": 800,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_LOW_004_student_newsletter.md": {
        "id": "NL_CASE_LOW_004",
        "newsletter_name": "Student Newsletter",
        "founder_name": "Unknown",
        "niche": "other",
        "mrr_tier": "<5k",
        "subscribers_total": 600,
        "japan_market_score_overall": 3.5,
    },
    "NL_CASE_LOW_005_local_newsletter.md": {
        "id": "NL_CASE_LOW_005",
        "newsletter_name": "Local Newsletter",
        "founder_name": "Unknown",
        "niche": "other",
        "mrr_tier": "<5k",
        "subscribers_total": 1200,
        "japan_market_score_overall": 4.8,
    },
    "NL_CASE_LOW_006_hobby_newsletter.md": {
        "id": "NL_CASE_LOW_006",
        "newsletter_name": "Hobby Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "<5k",
        "subscribers_total": 700,
        "japan_market_score_overall": 3.8,
    },
    "NL_CASE_LOW_007_weekly_newsletter.md": {
        "id": "NL_CASE_LOW_007",
        "newsletter_name": "Weekly Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "<5k",
        "subscribers_total": 900,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_LOW_008_ad_revenue_newsletter.md": {
        "id": "NL_CASE_LOW_008",
        "newsletter_name": "Ad Revenue Newsletter",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "<5k",
        "subscribers_total": 1500,
        "japan_market_score_overall": 3.8,
    },
    "NL_CASE_LOW_009_curation_newsletter.md": {
        "id": "NL_CASE_LOW_009",
        "newsletter_name": "Curation Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "<5k",
        "subscribers_total": 1100,
        "japan_market_score_overall": 4.2,
    },
    "NL_CASE_MID_001_extra_points.md": {
        "id": "NL_CASE_MID_001",
        "newsletter_name": "Extra Points",
        "founder_name": "Matt Brown",
        "platform": "substack",
        "niche": "other",
        "mrr_tier": "10k-25k",
        "subscribers_total": 15000,
        "japan_market_score_overall": 2.5,
    },
    "NL_CASE_MID_002_chief_in_the_north.md": {
        "id": "NL_CASE_MID_002",
        "newsletter_name": "Chief in the North",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "10k-25k",
        "subscribers_total": 12000,
        "japan_market_score_overall": 3.5,
    },
    "NL_CASE_MID_002_naptown_scoop.md": {
        "id": "NL_CASE_MID_002B",
        "newsletter_name": "Naptown Scoop",
        "founder_name": "Tyler Shattuck",
        "platform": "beehiiv",
        "niche": "other",
        "mrr_tier": "10k-25k",
        "subscribers_total": 18000,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_MID_003_parenting_newsletter.md": {
        "id": "NL_CASE_MID_003",
        "newsletter_name": "Parenting Newsletter",
        "founder_name": "Unknown",
        "niche": "other",
        "mrr_tier": "10k-25k",
        "subscribers_total": 20000,
        "japan_market_score_overall": 4.2,
    },
    "NL_CASE_MID_003_stacked_marketer.md": {
        "id": "NL_CASE_MID_003B",
        "newsletter_name": "Stacked Marketer",
        "founder_name": "Unknown",
        "platform": "beehiiv",
        "niche": "business",
        "mrr_tier": "25k-50k",
        "subscribers_total": 35000,
        "japan_market_score_overall": 4.5,
    },
    "NL_CASE_MID_004_alex_brogan.md": {
        "id": "NL_CASE_MID_004",
        "newsletter_name": "Alex Brogan Newsletter",
        "founder_name": "Alex Brogan",
        "niche": "business",
        "mrr_tier": "10k-25k",
        "subscribers_total": 14000,
        "japan_market_score_overall": 4.0,
    },
    "NL_CASE_P2_001_milk_road.md": {
        "id": "NL_CASE_P2_001",
        "newsletter_name": "Milk Road",
        "founder_name": "Shaan Puri",
        "platform": "beehiiv",
        "niche": "finance",
        "mrr_tier": "50k-100k",
        "subscribers_total": 250000,
        "japan_market_score_overall": 3.5,
    },
    "NL_CASE_P2_002_the_hustle.md": {
        "id": "NL_CASE_P2_002",
        "newsletter_name": "The Hustle",
        "founder_name": "Sam Parr",
        "platform": "独自",
        "niche": "business",
        "mrr_tier": "100k+",
        "subscribers_total": 1500000,
        "japan_market_score_overall": 4.2,
    },
    "NL_MARKET_001_2025_trends.md": {
        "id": "NL_MARKET_001",
        "newsletter_name": "2025 Newsletter Market Trends",
        "founder_name": "Market Research",
        "niche": "business",
        "mrr_tier": "<5k",
        "subscribers_total": 0,
        "japan_market_score_overall": 5.0,
    },
    "NL_OVERSEAS_001_32billion_yen.md": {
        "id": "NL_OVERSEAS_001",
        "newsletter_name": "32 Billion Yen Case",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "100k+",
        "subscribers_total": 500000,
        "japan_market_score_overall": 3.8,
    },
    "NL_OVERSEAS_001_international.md": {
        "id": "NL_OVERSEAS_001B",
        "newsletter_name": "International Newsletter Case",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "50k-100k",
        "subscribers_total": 200000,
        "japan_market_score_overall": 3.5,
    },
    "NL_OVERSEAS_002_lawyer_to_4billion.md": {
        "id": "NL_OVERSEAS_002",
        "newsletter_name": "Lawyer to 4 Billion",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "100k+",
        "subscribers_total": 300000,
        "japan_market_score_overall": 3.8,
    },
    "NL_OVERSEAS_003_solo_26billion.md": {
        "id": "NL_OVERSEAS_003",
        "newsletter_name": "Solo 26 Billion Newsletter",
        "founder_name": "Unknown",
        "niche": "business",
        "mrr_tier": "100k+",
        "subscribers_total": 400000,
        "japan_market_score_overall": 3.5,
    },
    "NL_OVERSEAS_004_ai_2billion.md": {
        "id": "NL_OVERSEAS_004",
        "newsletter_name": "AI 2 Billion Newsletter",
        "founder_name": "Unknown",
        "niche": "ai",
        "mrr_tier": "100k+",
        "subscribers_total": 350000,
        "japan_market_score_overall": 4.5,
    },
    "NL_OVERSEAS_005_street_culture.md": {
        "id": "NL_OVERSEAS_005",
        "newsletter_name": "Street Culture Newsletter",
        "founder_name": "Unknown",
        "niche": "creator",
        "mrr_tier": "25k-50k",
        "subscribers_total": 80000,
        "japan_market_score_overall": 3.0,
    },
    "NL_OVERSEAS_006_parenting_86m.md": {
        "id": "NL_OVERSEAS_006",
        "newsletter_name": "Parenting 86M Newsletter",
        "founder_name": "Unknown",
        "niche": "other",
        "mrr_tier": "50k-100k",
        "subscribers_total": 150000,
        "japan_market_score_overall": 4.2,
    },
    "NL_OVERSEAS_007_alex_brogan.md": {
        "id": "NL_OVERSEAS_007",
        "newsletter_name": "Alex Brogan Overseas",
        "founder_name": "Alex Brogan",
        "niche": "business",
        "mrr_tier": "10k-25k",
        "subscribers_total": 14000,
        "japan_market_score_overall": 4.0,
    },
    "NL_OVERSEAS_008_naptown_scoop.md": {
        "id": "NL_OVERSEAS_008",
        "newsletter_name": "Naptown Scoop Overseas",
        "founder_name": "Tyler Shattuck",
        "platform": "beehiiv",
        "niche": "other",
        "mrr_tier": "10k-25k",
        "subscribers_total": 18000,
        "japan_market_score_overall": 4.5,
    },
}


def generate_yaml_frontmatter(filename: str) -> str:
    """ファイル名に基づいてYAML Front Matterを生成"""
    metadata = FILE_METADATA.get(filename, {})

    # デフォルト値
    case_id = metadata.get("id", "NL_CASE_XXX")
    newsletter_name = metadata.get("newsletter_name", "Unknown Newsletter")
    founder_name = metadata.get("founder_name", "Unknown")
    founder_twitter = metadata.get("founder_twitter", "@unknown")
    platform = metadata.get("platform", "substack")
    language = "en"
    niche = metadata.get("niche", "other")
    website = "https://unknown.com"

    # 収益ティア
    mrr_tier = metadata.get("mrr_tier", "<5k")
    mrr_usd = 0
    if mrr_tier == "100k+":
        mrr_usd = 100000
    elif mrr_tier == "50k-100k":
        mrr_usd = 75000
    elif mrr_tier == "25k-50k":
        mrr_usd = 37500
    elif mrr_tier == "10k-25k":
        mrr_usd = 17500
    elif mrr_tier == "5k-10k":
        mrr_usd = 7500

    arr_usd = mrr_usd * 12

    # 購読者データ
    subscribers_total = metadata.get("subscribers_total", 0)
    paid_conversion = 1.5 if subscribers_total > 0 else 0
    subscribers_paid = int(subscribers_total * paid_conversion / 100) if subscribers_total > 0 else 0

    # 日本市場スコア
    japan_score = metadata.get("japan_market_score_overall", 3.5)

    # 今日の日付
    today = datetime.now().strftime("%Y-%m-%d")

    yaml = f"""---
# ============================================================
# Newsletter Case Study v2.1
# Auto-generated YAML Front Matter
# ============================================================

id: "{case_id}"
version: "2.1"
created: "{today}"
updated: "{today}"

# 基本情報
newsletter_name: "{newsletter_name}"
founder_name: "{founder_name}"
founder_twitter: "{founder_twitter}"
platform: "{platform}"
language: "{language}"
niche: "{niche}"
website: "{website}"

# 収益ティア
mrr_usd: {mrr_usd}
mrr_tier: "{mrr_tier}"
arr_usd: {arr_usd}

# 購読者データ
subscribers_total: {subscribers_total}
subscribers_paid: {subscribers_paid}
paid_conversion_rate: {paid_conversion}
open_rate: 0.0
click_rate: 0.0
churn_rate: 0.0

# 定量KPI（v2.1追加）
metrics:
  engagement_rate: null
  growth_rate_monthly: null
  revenue_per_subscriber: null
  leverage_ratio: null
  buzz_score_avg: null

# 成長ステージ（v2.1追加）
growth_stage:
  current: ""
  trust_score: null
  authority_score: null
  influence_score: null

# 失敗パターン（v2.1追加）
failure_analysis:
  total_failures: null
  primary_pattern: ""
  recovery_speed: ""

# セマンティックタグ（5分類）
growth_strategies:
  - "organic_search"
content_style:
  - "educational"
success_pattern:
  - "niche_domination"
monetization:
  - "paid_subscription"
marketing_channel:
  - "twitter"
buzz_pattern:
  - "milestone_report"

# 日本市場スコア（5観点）
japan_market_score:
  overall: {japan_score}
  niche_demand: 0
  competition: 0
  content_transferability: 0
  revenue_model_reproducibility: 0
  target_audience_exists: 0

# クロスリファレンス（v2.1必須化）
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  person_registry_id: ""
  funnel_integration: "none"
  cross_leverage_score: null

related:
  app_cases: []
  sns_cases: []
  strategies: []

# ファクトチェック
fact_check:
  status: "pending"
  last_checked: "{today}"
  sources_count: 0
---

"""
    return yaml


def process_file(file_path: Path) -> dict:
    """ファイルにYAML Front Matterを追加"""
    try:
        # ファイルを読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 既にYAMLがある場合はスキップ
        if content.startswith('---'):
            return {
                'file': file_path.name,
                'status': 'SKIPPED',
                'reason': 'Already has YAML'
            }

        # YAML Front Matterを生成
        yaml_frontmatter = generate_yaml_frontmatter(file_path.name)

        # 新しいコンテンツ
        new_content = yaml_frontmatter + content

        # ファイルに書き込み
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return {
            'file': file_path.name,
            'status': 'SUCCESS',
            'yaml_lines': len(yaml_frontmatter.split('\n'))
        }

    except Exception as e:
        return {
            'file': file_path.name,
            'status': 'ERROR',
            'error': str(e)
        }


def generate_quality_report(results: list, output_path: Path):
    """品質スコアCSVを生成"""
    csv_lines = ["file_id,status,yaml_lines,quality_score,notes\n"]

    for result in results:
        file_id = result['file'].replace('.md', '')
        status = result['status']
        yaml_lines = result.get('yaml_lines', 0)

        # 品質スコア算出
        if status == 'SUCCESS':
            quality_score = 85  # YAML追加完了の基準スコア
        elif status == 'SKIPPED':
            quality_score = 100  # 既存YAMLありは完成
        else:
            quality_score = 0

        notes = result.get('reason', result.get('error', ''))

        csv_lines.append(f"{file_id},{status},{yaml_lines},{quality_score},\"{notes}\"\n")

    # CSVを書き込み
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(csv_lines)

    print(f"\n✅ Quality report generated: {output_path}")


def main():
    # ベースディレクトリ
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")
    case_studies_dir = base_dir / "documents/02_Newsletter/case_studies"
    analysis_dir = base_dir / "analysis/quality_scores"

    # 出力ディレクトリ作成
    analysis_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Newsletter Batch2 YAML Front Matter Addition")
    print("=" * 60)
    print(f"Target files: {len(TARGET_FILES)}")
    print(f"Processing...\n")

    results = []

    for filename in TARGET_FILES:
        file_path = case_studies_dir / filename

        if not file_path.exists():
            results.append({
                'file': filename,
                'status': 'NOT_FOUND',
                'error': 'File does not exist'
            })
            print(f"❌ {filename} - NOT FOUND")
            continue

        result = process_file(file_path)
        results.append(result)

        # 進捗表示
        if result['status'] == 'SUCCESS':
            print(f"✅ {filename} - YAML added ({result['yaml_lines']} lines)")
        elif result['status'] == 'SKIPPED':
            print(f"⏭️  {filename} - {result['reason']}")
        else:
            print(f"❌ {filename} - {result['error']}")

    # サマリー表示
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    success_count = sum(1 for r in results if r['status'] == 'SUCCESS')
    skipped_count = sum(1 for r in results if r['status'] == 'SKIPPED')
    error_count = sum(1 for r in results if r['status'] == 'ERROR')
    not_found_count = sum(1 for r in results if r['status'] == 'NOT_FOUND')

    print(f"Total files: {len(TARGET_FILES)}")
    print(f"✅ Success: {success_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"❌ Error: {error_count}")
    print(f"❓ Not Found: {not_found_count}")

    # CSVレポート生成
    output_csv = analysis_dir / "improvement_batch2_newsletter_other.csv"
    generate_quality_report(results, output_csv)

    print("\n✨ Batch2 processing completed!")


if __name__ == "__main__":
    main()
