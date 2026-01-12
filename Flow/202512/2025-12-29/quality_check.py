#!/usr/bin/env python3
"""
Batch 2-3 自動品質スコアリング
作成日: 2025-12-29
"""

import os
import re
from pathlib import Path

# ベースディレクトリ
DOCS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents")

# Batch 2ファイル (7件)
BATCH2_FILES = [
    "03_VC_Backed/FOUNDER_151_airbnb.md",
    "03_VC_Backed/FOUNDER_152_coinbase.md",
    "05_IPO_Global/FOUNDER_351_jan_koum_whatsapp.md",
    "05_IPO_Global/FOUNDER_352_eric_yuan_zoom.md",
    "03_VC_Backed/FOUNDER_157_github.md",
    "05_IPO_Global/FOUNDER_355_coinbase.md",
    "07_Failure_Study/FAILURE_008_jawbone.md",
]

# Batch 3ファイル (11件)
BATCH3_FILES = [
    "07_Failure_Study/FAILURE_009_quibi.md",
    "07_Failure_Study/FAILURE_010_getaround.md",
    "07_Failure_Study/FAILURE_011_humane_ai.md",
    "03_VC_Backed/FOUNDER_159_palantir.md",
    "03_VC_Backed/FOUNDER_160_okta.md",
    "06_Pivot_Success/PIVOT_004_box.md",
    "06_Pivot_Success/PIVOT_005_jasper_ai.md",
    "08_Emerging/EMERGING_001_stability_ai.md",
    "08_Emerging/EMERGING_002_character_ai.md",
    "08_Emerging/EMERGING_003_midjourney.md",
    "08_Emerging/EMERGING_004_runway.md",
]

def count_nulls_in_validation(content):
    """validation_dataセクション内のnull数をカウント"""
    # validation_data から cross_reference までの範囲を抽出
    match = re.search(r'validation_data:.*?(?=cross_reference:)', content, re.DOTALL)
    if not match:
        return 0
    section = match.group(0)
    return section.count(': null')

def get_sources_count(content):
    """ソース数を取得"""
    match = re.search(r'sources_count:\s*(\d+)', content)
    return int(match.group(1)) if match else 0

def get_fact_check(content):
    """Fact Check状態を取得"""
    match = re.search(r'fact_check:\s*"?(\w+)"?', content)
    return match.group(1) if match else "unknown"

def count_ten_x_axes(content):
    """10x axes数をカウント"""
    match = re.search(r'ten_x_axes:.*?(?=mvp_type:)', content, re.DOTALL)
    if not match:
        return 0
    section = match.group(0)
    return section.count('- axis:')

def get_mvp_type(content):
    """MVP typeを取得"""
    match = re.search(r'mvp_type:\s*"?([^"\n]+)"?', content)
    return match.group(1).strip() if match else "null"

def has_orchestrate_section(content):
    """orchestrate-phase1セクション存在チェック"""
    return 'orchestrate-phase1への示唆' in content

def calculate_score(null_count, sources, fact_check, axes_count, mvp_type, has_orchestrate):
    """品質スコア計算 (100点満点)"""
    score = 0

    # データ完全性 (15点)
    if null_count == 0:
        score += 15
    elif null_count <= 2:
        score += 10
    elif null_count <= 4:
        score += 5

    # ソース数 (15点)
    if sources >= 15:
        score += 15
    elif sources >= 12:
        score += 12
    elif sources >= 10:
        score += 10
    elif sources >= 3:
        score += 5

    # Fact Check (30点)
    if fact_check == "pass":
        score += 30

    # 10x axes (15点)
    if axes_count >= 4:
        score += 15
    elif axes_count >= 2:
        score += 12
    elif axes_count >= 1:
        score += 5

    # MVP type (10点)
    if mvp_type != "null" and mvp_type != "":
        score += 10

    # Orchestrate section (10点)
    if has_orchestrate:
        score += 10

    return score

def get_grade(score):
    """グレード判定"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"

def process_file(filepath):
    """ファイルを処理して品質メトリクスを返す"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        null_count = count_nulls_in_validation(content)
        sources = get_sources_count(content)
        fact_check = get_fact_check(content)
        axes_count = count_ten_x_axes(content)
        mvp_type = get_mvp_type(content)
        has_orchestrate = has_orchestrate_section(content)

        score = calculate_score(null_count, sources, fact_check, axes_count, mvp_type, has_orchestrate)
        grade = get_grade(score)

        return {
            'file': filepath.name,
            'nulls': null_count,
            'sources': sources,
            'fact_check': fact_check,
            'axes': axes_count,
            'mvp_type': mvp_type,
            'has_orchestrate': has_orchestrate,
            'score': score,
            'grade': grade
        }
    except Exception as e:
        print(f"エラー処理中: {filepath.name} - {e}")
        return None

def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║     Batch 2-3 自動品質スコアリング (18件)                     ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print(f"║ 実行時刻: 2025-12-29 11:30                              ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")

    all_results = []

    print("=== Batch 2 (7件) ===\n")
    batch2_results = []
    for file_rel in BATCH2_FILES:
        filepath = DOCS_DIR / file_rel
        result = process_file(filepath)
        if result:
            batch2_results.append(result)
            all_results.append(result)
            fc_icon = "✅" if result['fact_check'] == "pass" else "❌"
            print(f"{result['file']:40s} | Score: {result['score']:3d} | Grade: {result['grade']} | Nulls: {result['nulls']} | Sources: {result['sources']:2d} | FC: {fc_icon} | Axes: {result['axes']}")

    print("\n=== Batch 3 (11件) ===\n")
    batch3_results = []
    for file_rel in BATCH3_FILES:
        filepath = DOCS_DIR / file_rel
        result = process_file(filepath)
        if result:
            batch3_results.append(result)
            all_results.append(result)
            fc_icon = "✅" if result['fact_check'] == "pass" else "❌"
            print(f"{result['file']:40s} | Score: {result['score']:3d} | Grade: {result['grade']} | Nulls: {result['nulls']} | Sources: {result['sources']:2d} | FC: {fc_icon} | Axes: {result['axes']}")

    # サマリー統計
    total_files = len(all_results)
    if total_files > 0:
        total_nulls = sum(r['nulls'] for r in all_results)
        total_sources = sum(r['sources'] for r in all_results)
        total_axes = sum(r['axes'] for r in all_results)
        fact_check_pass = sum(1 for r in all_results if r['fact_check'] == 'pass')
        files_with_nulls = sum(1 for r in all_results if r['nulls'] > 0)
        total_score = sum(r['score'] for r in all_results)

        avg_sources = total_sources / total_files
        avg_axes = total_axes / total_files
        avg_score = total_score / total_files
        pass_rate = (fact_check_pass / total_files) * 100
        null_rate = (files_with_nulls / total_files) * 100

        grade_counts = {}
        for r in all_results:
            grade_counts[r['grade']] = grade_counts.get(r['grade'], 0) + 1

        print("\n╔══════════════════════════════════════════════════════════════╗")
        print("║ サマリー統計                                                  ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║ 総ファイル数: {total_files:d}                                           ║")
        print(f"║ 平均スコア: {avg_score:.1f}/100                                    ║")
        print(f"║ Grade分布: A:{grade_counts.get('A', 0)} B:{grade_counts.get('B', 0)} C:{grade_counts.get('C', 0)} D:{grade_counts.get('D', 0)} F:{grade_counts.get('F', 0)}                               ║")
        print(f"║ Fact Check Pass率: {pass_rate:.0f}% ({fact_check_pass}/{total_files})                       ║")
        print(f"║ 平均ソース数: {avg_sources:.1f}件                                       ║")
        print(f"║ 総Null数: {total_nulls}件                                         ║")
        print(f"║ Nullを含むファイル: {files_with_nulls}件 ({null_rate:.0f}%)                       ║")
        print(f"║ 平均10x axes: {avg_axes:.1f}軸                                       ║")
        print("╚══════════════════════════════════════════════════════════════╝\n")

        # 成功判定
        if pass_rate == 100 and avg_sources >= 12:
            print("🎉 品質基準達成: Fact Check 100%, 平均ソース12+件")
        elif avg_score >= 85:
            print("✅ 平均スコア85点以上達成")
        else:
            print("⚠️  品質改善余地あり")

if __name__ == "__main__":
    main()
