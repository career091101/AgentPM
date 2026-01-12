#!/usr/bin/env python3
"""
ForSolo Tier 2 Case Studies Quality Audit Script

品質監査基準（100点満点）:
1. 定量データ完全性 (30点): MRR, 開発期間, コスト, ユーザー数等
2. ソース信頼性 (25点): 1次ソースリンク (X/Twitter, 公式サイト, Product Hunt)
3. 1人実行可能性 (30点): Solo Fit評価 (6軸)
4. スキルカバレッジ (15点): 対象スキルの検証ポイント網羅

目標: 全ファイル95点以上
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
import json

# Base path
BASE_PATH = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies")

# Required elements for 95+ quality score
REQUIRED_ELEMENTS = {
    "yaml_frontmatter": {
        "weight": 10,
        "keywords": ["---", "id:", "solo_fit_score:", "category:", "mrr:"]
    },
    "solo_fit_evaluation": {
        "weight": 30,
        "keywords": ["Solo Fit", "技術実行可能性", "スキル充足度", "時間確保可能性", "コスト実現可能性", "マーケ実行可能性", "サポート実行可能性"]
    },
    "quality_score_section": {
        "weight": 15,
        "keywords": ["Quality Score", "定量データ完全性", "ソース信頼性", "1人実行可能性", "スキルカバレッジ"]
    },
    "primary_sources": {
        "weight": 25,
        "keywords": ["twitter.com", "x.com", "producthunt.com", "https://"],
        "min_count": 2
    },
    "japan_market_adaptation": {
        "weight": 10,
        "keywords": ["日本市場", "Japanese Market", "文化的適応", "推奨アプローチ（日本）"]
    },
    "playbook": {
        "weight": 10,
        "keywords": ["Playbook", "Week 1", "Month", "ステップ", "タスク", "- [ ]"]
    }
}

# Quantitative data keywords
QUANTITATIVE_KEYWORDS = [
    "MRR", "ARR", "$", "ドル",
    "開発期間", "日", "週間", "ヶ月",
    "初期投資", "コスト",
    "ユーザー数", "フォロワー",
    "LTV", "CAC", "利益率"
]


def check_yaml_frontmatter(content: str) -> Tuple[bool, int]:
    """Check if file has valid YAML frontmatter"""
    if not content.startswith("---"):
        return False, 0

    # Extract YAML section
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return False, 0

    yaml_content = yaml_match.group(1)
    required_fields = ["id:", "solo_fit_score:", "category:"]
    score = sum(10 for field in required_fields if field in yaml_content) / len(required_fields)

    return len([f for f in required_fields if f in yaml_content]) >= 2, int(score * 10)


def check_solo_fit_evaluation(content: str) -> Tuple[bool, int]:
    """Check for 6-axis Solo Fit evaluation"""
    axes = [
        "技術実行可能性", "スキル充足度", "時間確保可能性",
        "コスト実現可能性", "マーケ実行可能性", "サポート実行可能性"
    ]

    found_axes = sum(1 for axis in axes if axis in content)

    # Check for scoring (X/10 pattern)
    score_patterns = re.findall(r'(\d+)/10', content)
    has_scores = len(score_patterns) >= 6

    if found_axes >= 6 and has_scores:
        return True, 30
    elif found_axes >= 4:
        return False, 20
    else:
        return False, 10


def check_quality_score_section(content: str) -> Tuple[bool, int]:
    """Check for Quality Score breakdown section"""
    required_criteria = ["定量データ完全性", "ソース信頼性", "1人実行可能性", "スキルカバレッジ"]
    found_criteria = sum(1 for criterion in required_criteria if criterion in content)

    has_score_heading = "Quality Score" in content or "品質スコア" in content

    if has_score_heading and found_criteria >= 4:
        return True, 15
    elif found_criteria >= 2:
        return False, 8
    else:
        return False, 0


def check_primary_sources(content: str) -> Tuple[bool, int]:
    """Check for primary source links (X/Twitter, Product Hunt, official sites)"""
    # Count URLs
    urls = re.findall(r'https?://[^\s\)]+', content)

    # Check for primary sources
    primary_sources = [
        url for url in urls
        if any(domain in url.lower() for domain in ["twitter.com", "x.com", "producthunt.com"])
    ]

    # Check for References section
    has_references_section = "## References" in content or "## 参照" in content

    if len(primary_sources) >= 2 and has_references_section:
        return True, 25
    elif len(primary_sources) >= 1:
        return False, 15
    elif len(urls) >= 1:
        return False, 8
    else:
        return False, 0


def check_japan_market_adaptation(content: str) -> Tuple[bool, int]:
    """Check for Japan market adaptation section"""
    keywords = ["日本市場", "Japanese Market", "文化的適応", "推奨アプローチ（日本）"]
    found = sum(1 for keyword in keywords if keyword in content)

    has_section = any(heading in content for heading in ["## 日本市場適用", "## Japanese Market", "### 文化的適応"])

    if has_section and found >= 2:
        return True, 10
    elif found >= 1:
        return False, 5
    else:
        return False, 0


def check_playbook(content: str) -> Tuple[bool, int]:
    """Check for actionable playbook section"""
    playbook_keywords = ["Playbook", "実行プラン", "Week 1", "Month", "フェーズ"]
    has_playbook_heading = any(keyword in content for keyword in playbook_keywords)

    # Check for task checkboxes
    task_checkboxes = re.findall(r'- \[ \]', content)

    if has_playbook_heading and len(task_checkboxes) >= 5:
        return True, 10
    elif has_playbook_heading:
        return False, 5
    else:
        return False, 0


def check_quantitative_data(content: str) -> int:
    """Check for quantitative data completeness"""
    found_keywords = sum(1 for keyword in QUANTITATIVE_KEYWORDS if keyword in content)

    # Bonus for specific metrics
    has_mrr = bool(re.search(r'\$\d+[,\d]*', content))
    has_timeline = bool(re.search(r'\d+日|\d+週間|\d+ヶ月', content))

    score = min(15, found_keywords * 2)
    if has_mrr:
        score += 5
    if has_timeline:
        score += 5

    return min(25, score)


def audit_file(file_path: Path) -> Dict:
    """Audit a single file and return quality assessment"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            "file": str(file_path),
            "error": str(e),
            "total_score": 0
        }

    # Perform checks
    results = {}
    total_score = 0

    # 1. YAML Frontmatter (10 points)
    has_yaml, yaml_score = check_yaml_frontmatter(content)
    results["yaml_frontmatter"] = {"present": has_yaml, "score": yaml_score}
    total_score += yaml_score

    # 2. Solo Fit Evaluation (30 points)
    has_solo_fit, solo_fit_score = check_solo_fit_evaluation(content)
    results["solo_fit_evaluation"] = {"present": has_solo_fit, "score": solo_fit_score}
    total_score += solo_fit_score

    # 3. Quality Score Section (15 points)
    has_quality, quality_score = check_quality_score_section(content)
    results["quality_score_section"] = {"present": has_quality, "score": quality_score}
    total_score += quality_score

    # 4. Primary Sources (25 points)
    has_sources, sources_score = check_primary_sources(content)
    results["primary_sources"] = {"present": has_sources, "score": sources_score}
    total_score += sources_score

    # 5. Japan Market Adaptation (10 points)
    has_japan, japan_score = check_japan_market_adaptation(content)
    results["japan_market_adaptation"] = {"present": has_japan, "score": japan_score}
    total_score += japan_score

    # 6. Playbook (10 points)
    has_playbook_section, playbook_score = check_playbook(content)
    results["playbook"] = {"present": has_playbook_section, "score": playbook_score}
    total_score += playbook_score

    # Calculate word count
    word_count = len(content)

    return {
        "file": str(file_path.relative_to(BASE_PATH)),
        "skill": file_path.parent.name,
        "word_count": word_count,
        "total_score": total_score,
        "elements": results,
        "needs_improvement": total_score < 95,
        "priority": "高" if total_score < 80 else "中" if total_score < 90 else "低"
    }


def generate_report(audit_results: List[Dict]) -> str:
    """Generate markdown audit report"""

    # Statistics
    total_files = len(audit_results)
    avg_score = sum(r["total_score"] for r in audit_results) / total_files if total_files > 0 else 0
    files_below_95 = sum(1 for r in audit_results if r["total_score"] < 95)
    files_below_90 = sum(1 for r in audit_results if r["total_score"] < 90)
    files_below_80 = sum(1 for r in audit_results if r["total_score"] < 80)

    # Group by skill
    by_skill = {}
    for result in audit_results:
        skill = result["skill"]
        if skill not in by_skill:
            by_skill[skill] = []
        by_skill[skill].append(result)

    # Generate report
    report = f"""# ForSolo Tier 2 Case Studies - 品質監査レポート

**監査日**: 2026-01-03
**対象ファイル数**: {total_files}
**平均品質スコア**: {avg_score:.1f}/100

---

## 1. エグゼクティブサマリー

### 現状分析
- **95点未達**: {files_below_95}件 ({files_below_95/total_files*100:.1f}%)
- **90点未達**: {files_below_90}件 ({files_below_90/total_files*100:.1f}%)
- **80点未達**: {files_below_80}件 ({files_below_80/total_files*100:.1f}%)

### 改善必要性
- **目標**: 全ファイル95点以上
- **現状平均**: {avg_score:.1f}点
- **ギャップ**: {95 - avg_score:.1f}点

### 主要な不足要素（全体傾向）

"""

    # Calculate missing elements statistics
    element_stats = {
        "yaml_frontmatter": 0,
        "solo_fit_evaluation": 0,
        "quality_score_section": 0,
        "primary_sources": 0,
        "japan_market_adaptation": 0,
        "playbook": 0
    }

    for result in audit_results:
        for element, data in result["elements"].items():
            if not data["present"]:
                element_stats[element] += 1

    element_names = {
        "yaml_frontmatter": "YAML Frontmatter",
        "solo_fit_evaluation": "Solo Fit評価（6軸）",
        "quality_score_section": "Quality Scoreセクション",
        "primary_sources": "1次ソースリンク",
        "japan_market_adaptation": "日本市場適用",
        "playbook": "Actionable Playbook"
    }

    for element, count in sorted(element_stats.items(), key=lambda x: x[1], reverse=True):
        percentage = count / total_files * 100
        report += f"- **{element_names[element]}**: {count}件不足 ({percentage:.1f}%)\n"

    report += f"""

---

## 2. スキル別品質サマリー

| スキル | ファイル数 | 平均スコア | 95点未達 | 優先度 |
|--------|-----------|-----------|---------|--------|
"""

    for skill, results in sorted(by_skill.items()):
        skill_avg = sum(r["total_score"] for r in results) / len(results)
        skill_below_95 = sum(1 for r in results if r["total_score"] < 95)
        priority = "高" if skill_avg < 85 else "中" if skill_avg < 92 else "低"
        report += f"| {skill} | {len(results)} | {skill_avg:.1f} | {skill_below_95} | {priority} |\n"

    report += f"""

---

## 3. 詳細ファイル別監査結果

"""

    # Sort by score (lowest first)
    sorted_results = sorted(audit_results, key=lambda x: x["total_score"])

    for result in sorted_results:
        file_name = result["file"]
        score = result["total_score"]
        priority = result["priority"]

        report += f"""### {file_name}
**スコア**: {score}/100 | **優先度**: {priority}

| 要素 | 状態 | スコア |
|------|------|--------|
"""

        for element, data in result["elements"].items():
            status = "✅" if data["present"] else "❌"
            report += f"| {element_names[element]} | {status} | {data['score']} |\n"

        # Missing elements
        missing = [element_names[elem] for elem, data in result["elements"].items() if not data["present"]]
        if missing:
            report += f"\n**不足要素**: {', '.join(missing)}\n"

        report += "\n---\n\n"

    report += f"""
## 4. 改善推奨アクション

### 優先度「高」ファイル（80点未満）: {files_below_80}件
- 全要素を追加
- Solopreneur_Researchから元データ再取得
- 1次ソースリンク必須追加

### 優先度「中」ファイル（80-94点）: {files_below_95 - files_below_80}件
- 不足要素のみ追加
- Solo Fit評価、日本市場適用を重点的に

### 優先度「低」ファイル（95点以上）: {total_files - files_below_95}件
- 微調整のみ
- 品質スコアセクション追加で完了

---

## 5. 推定作業時間

| 優先度 | ファイル数 | 時間/ファイル | 合計時間 |
|--------|-----------|--------------|---------|
| 高 | {files_below_80} | 2時間 | {files_below_80 * 2}時間 |
| 中 | {files_below_95 - files_below_80} | 1時間 | {(files_below_95 - files_below_80) * 1}時間 |
| 低 | {total_files - files_below_95} | 0.5時間 | {(total_files - files_below_95) * 0.5}時間 |
| **合計** | **{total_files}** | - | **{files_below_80 * 2 + (files_below_95 - files_below_80) * 1 + (total_files - files_below_95) * 0.5}時間** |

---

**監査完了**: Phase 1-1完了、Phase 1-2（データ補完）へ移行可能
"""

    return report


def main():
    """Main audit execution"""
    print("ForSolo Tier 2 品質監査開始...")
    print(f"対象ディレクトリ: {BASE_PATH}")

    # Find all markdown files
    all_files = list(BASE_PATH.rglob("*.md"))
    print(f"発見ファイル数: {len(all_files)}")

    # Audit each file
    audit_results = []
    for i, file_path in enumerate(all_files, 1):
        print(f"監査中 ({i}/{len(all_files)}): {file_path.name}")
        result = audit_file(file_path)
        audit_results.append(result)

    # Generate report
    print("\n監査レポート生成中...")
    report = generate_report(audit_results)

    # Save report
    report_path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/existing_files_quality_audit_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    # Save JSON data
    json_path = report_path.with_suffix('.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(audit_results, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 監査完了")
    print(f"📄 レポート: {report_path}")
    print(f"📊 JSONデータ: {json_path}")

    # Print summary
    avg_score = sum(r["total_score"] for r in audit_results) / len(audit_results)
    files_below_95 = sum(1 for r in audit_results if r["total_score"] < 95)
    print(f"\n📊 サマリー:")
    print(f"  - 平均スコア: {avg_score:.1f}/100")
    print(f"  - 95点未達: {files_below_95}件 ({files_below_95/len(audit_results)*100:.1f}%)")


if __name__ == "__main__":
    main()
