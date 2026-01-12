#!/usr/bin/env python3
"""
Claude Code評価結果統合スクリプト

バッチ評価結果を統合し、統計情報を生成。

使用例:
    python merge_evaluation_results.py --input-dir Flow/202512/2025-12-31/batch_evaluation
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Any
from collections import Counter
from datetime import datetime


def merge_results(results_dir: Path) -> List[Dict[str, Any]]:
    """バッチ評価結果を統合"""

    all_results = []
    batch_files = sorted(results_dir.glob("evaluation_results_batch_*.json"))

    if not batch_files:
        print(f"警告: {results_dir} に評価結果ファイルが見つかりません。")
        return []

    for batch_file in batch_files:
        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_results = json.load(f)
            all_results.extend(batch_results)
        print(f"✓ {batch_file.name} を読み込み（{len(batch_results)}件）")

    # スコア順にソート
    all_results.sort(key=lambda x: x.get('総合スコア', 0), reverse=True)

    return all_results


def generate_statistics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """統計情報を生成"""

    if not results:
        return {}

    total = len(results)
    scores = [r.get('総合スコア', 0) for r in results]
    judgments = [r.get('判定', '').split()[0] for r in results]
    categories = [r.get('カテゴリ', '') for r in results]
    types = [r.get('概念的タイプ', '') for r in results]

    stats = {
        "総評価数": total,
        "スコア統計": {
            "平均": round(sum(scores) / total, 1) if total > 0 else 0,
            "最高": max(scores) if scores else 0,
            "最低": min(scores) if scores else 0,
            "中央値": sorted(scores)[total // 2] if scores else 0
        },
        "判定分布": {
            "VERY HIGH (80-100点)": sum(1 for j in judgments if j == 'VERY'),
            "HIGH (60-79点)": sum(1 for j in judgments if j == 'HIGH'),
            "MEDIUM (40-59点)": sum(1 for j in judgments if j == 'MEDIUM'),
            "LOW (0-39点)": sum(1 for j in judgments if j == 'LOW')
        },
        "カテゴリ分布": dict(Counter(categories).most_common()),
        "概念的タイプ分布": dict(Counter(types).most_common(10)),
        "TOP 10投稿": [
            {
                "順位": i,
                "スコア": r.get('総合スコア'),
                "判定": r.get('判定'),
                "投稿番号": r.get('投稿番号'),
                "理由": r.get('理由', '')[:100] + "..."
            }
            for i, r in enumerate(results[:10], 1)
        ]
    }

    return stats


def generate_insights(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """LLM評価による洞察を抽出"""

    high_value_insights = []
    hidden_values = []

    for r in results[:20]:  # TOP 20のみ
        context_eval = r.get('文脈評価', {})

        if context_eval.get('深い洞察'):
            high_value_insights.append({
                "投稿番号": r.get('投稿番号'),
                "スコア": r.get('総合スコア'),
                "洞察": context_eval.get('深い洞察')
            })

        if context_eval.get('隠れた価値'):
            hidden_values.append({
                "投稿番号": r.get('投稿番号'),
                "スコア": r.get('総合スコア'),
                "隠れた価値": context_eval.get('隠れた価値')
            })

    return {
        "高価値洞察": high_value_insights[:10],
        "ルールベースで見落とす価値": hidden_values[:10]
    }


def main():
    parser = argparse.ArgumentParser(description='評価結果統合・統計生成')

    parser.add_argument('--input-dir',
                       default='Flow/202512/2025-12-31/batch_evaluation',
                       help='評価結果ディレクトリ')
    parser.add_argument('--output',
                       help='出力ファイル（デフォルト: final_evaluation_results_{日付}.json）')

    args = parser.parse_args()

    results_dir = Path(args.input_dir)

    if not results_dir.exists():
        print(f"エラー: {results_dir} が存在しません。")
        return

    # 結果統合
    print("="*60)
    print("評価結果統合開始")
    print("="*60)

    all_results = merge_results(results_dir)

    if not all_results:
        print("評価結果が見つかりません。")
        return

    # 統計生成
    stats = generate_statistics(all_results)
    insights = generate_insights(all_results)

    # 最終結果
    final_result = {
        "評価日時": datetime.now().isoformat(),
        "総評価数": len(all_results),
        "統計情報": stats,
        "LLM洞察": insights,
        "全評価結果": all_results
    }

    # 出力
    output_file = args.output or results_dir / f"final_evaluation_results_{datetime.now().strftime('%Y%m%d')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 統合完了: {output_file}")

    # サマリー表示
    print("\n" + "="*60)
    print("評価サマリー")
    print("="*60)
    print(f"総評価数: {stats['総評価数']}件")
    print(f"\nスコア統計:")
    print(f"  平均: {stats['スコア統計']['平均']}点")
    print(f"  最高: {stats['スコア統計']['最高']}点")
    print(f"  最低: {stats['スコア統計']['最低']}点")
    print(f"\n判定分布:")
    for judgment, count in stats['判定分布'].items():
        pct = round(count / stats['総評価数'] * 100, 1)
        print(f"  {judgment}: {count}件 ({pct}%)")

    print(f"\nカテゴリ分布:")
    for cat, count in list(stats['カテゴリ分布'].items())[:5]:
        pct = round(count / stats['総評価数'] * 100, 1)
        print(f"  {cat}: {count}件 ({pct}%)")

    print(f"\nTOP 3投稿:")
    for item in stats['TOP 10投稿'][:3]:
        print(f"  {item['順位']}位: {item['スコア']}点 - {item['理由'][:60]}...")


if __name__ == '__main__':
    main()
