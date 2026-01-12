#!/usr/bin/env python3
"""
Weekly Quality Report Generator
Week 8: Compounding Engineering週次品質レポート生成スクリプト

Usage:
    python scripts/weekly_quality_report.py [--format FORMAT] [--save]

Examples:
    # Markdown形式でレポート生成
    python scripts/weekly_quality_report.py --format markdown

    # JSON形式で保存
    python scripts/weekly_quality_report.py --format json --save

    # HTMLダッシュボード生成
    python scripts/weekly_quality_report.py --format html --save
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional


class WeeklyQualityReport:
    """週次品質レポート生成クラス"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.config_path = self.project_root / ".claude" / "config" / "quality_metrics.json"
        self.report_dir = self.project_root / "reports" / "quality"
        self.knowledge_dir = self.project_root / ".claude" / "knowledge"

        # ディレクトリ作成
        self.report_dir.mkdir(parents=True, exist_ok=True)

        self.current_metrics: Dict[str, Any] = {}
        self.previous_metrics: Dict[str, Any] = {}
        self.improvements: List[Dict[str, Any]] = []
        self.degradations: List[Dict[str, Any]] = []
        self.best_practices: List[str] = []

    def generate_report(self, format: str = "markdown", save: bool = False) -> str:
        """週次レポート生成"""
        print("📊 週次品質レポートを生成中...")

        # Step 1: 現在の品質測定
        print("  1. 現在の品質を測定中...")
        self.current_metrics = self._measure_current_quality()

        # Step 2: 前回レポートとの比較
        print("  2. 前回レポートと比較中...")
        self.previous_metrics = self._load_previous_report()
        self._compare_with_previous()

        # Step 3: 改善提案の生成
        print("  3. 改善提案を生成中...")
        improvement_suggestions = self._generate_improvement_suggestions()

        # Step 4: ベストプラクティス抽出
        print("  4. ベストプラクティスを抽出中...")
        self._extract_best_practices()

        # Step 5: レポート生成
        print("  5. レポートを生成中...")
        if format == "markdown":
            report_content = self._generate_markdown_report(improvement_suggestions)
        elif format == "json":
            report_content = self._generate_json_report(improvement_suggestions)
        elif format == "html":
            report_content = self._generate_html_report(improvement_suggestions)
        else:
            raise ValueError(f"Unsupported format: {format}")

        # Step 6: 保存
        if save:
            filename = self._save_report(report_content, format)
            print(f"\n✅ レポートを保存しました: {filename}")

        # Step 7: CLAUDE.md更新
        if self.best_practices:
            print("  6. CLAUDE.mdにベストプラクティスを追記中...")
            self._update_claude_md()

        # Step 8: ナレッジ蓄積
        print("  7. ナレッジベースを更新中...")
        self._save_knowledge()

        return report_content

    def _measure_current_quality(self) -> Dict[str, Any]:
        """現在の品質を測定"""
        try:
            result = subprocess.run(
                ["python", "scripts/measure_quality.py", "--output", "json"],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode != 0:
                print(f"    ⚠️  品質測定エラー: {result.stderr}")
                return {}

            # JSON出力から測定結果を抽出
            output_lines = result.stdout.strip().split("\n")
            json_start = False
            json_lines = []

            for line in output_lines:
                if line.strip().startswith("{"):
                    json_start = True
                if json_start:
                    json_lines.append(line)

            if json_lines:
                json_str = "\n".join(json_lines)
                return json.loads(json_str)

            return {}

        except Exception as e:
            print(f"    ⚠️  品質測定エラー: {e}")
            return {}

    def _load_previous_report(self) -> Dict[str, Any]:
        """前回レポート読み込み"""
        # 最新のJSONレポートを検索
        json_reports = sorted(self.report_dir.glob("quality_report_*.json"), reverse=True)

        if not json_reports:
            print("    ℹ️  前回レポートが見つかりません（初回実行）")
            return {}

        latest_report = json_reports[0]
        print(f"    ℹ️  前回レポート: {latest_report.name}")

        with open(latest_report, "r", encoding="utf-8") as f:
            return json.load(f)

    def _compare_with_previous(self):
        """前回レポートとの比較"""
        if not self.previous_metrics:
            return

        current_overall = self.current_metrics.get("overall", {}).get("score", 0)
        previous_overall = self.previous_metrics.get("overall", {}).get("score", 0)

        improvement = current_overall - previous_overall

        if improvement > 0:
            print(f"    ✅ 全体スコア: {previous_overall} → {current_overall} (+{improvement:.2f})")
        elif improvement < 0:
            print(f"    ⚠️  全体スコア: {previous_overall} → {current_overall} ({improvement:.2f})")
        else:
            print(f"    ➡️  全体スコア: {current_overall} (変化なし)")

        # カテゴリ別比較
        for category_name in self.current_metrics.keys():
            if category_name in ["overall", "trend", "metadata"]:
                continue

            current_score = self.current_metrics[category_name].get("score", 0)
            previous_score = self.previous_metrics.get(category_name, {}).get("score", 0)

            diff = current_score - previous_score

            if diff > 5:
                self.improvements.append({
                    "category": category_name,
                    "previous": previous_score,
                    "current": current_score,
                    "improvement": diff
                })
            elif diff < -5:
                self.degradations.append({
                    "category": category_name,
                    "previous": previous_score,
                    "current": current_score,
                    "degradation": diff
                })

    def _generate_improvement_suggestions(self) -> List[Dict[str, Any]]:
        """改善提案生成"""
        suggestions = []

        for category_name, category_data in self.current_metrics.items():
            if category_name in ["overall", "trend", "metadata"]:
                continue

            score = category_data.get("score", 0)

            # スコア60未満のカテゴリに改善提案
            if score < 60:
                suggestions.append({
                    "category": category_name,
                    "score": score,
                    "priority": "高",
                    "suggestion": self._get_improvement_suggestion(category_name, category_data)
                })
            elif score < 75:
                suggestions.append({
                    "category": category_name,
                    "score": score,
                    "priority": "中",
                    "suggestion": self._get_improvement_suggestion(category_name, category_data)
                })

        return suggestions

    def _get_improvement_suggestion(self, category_name: str, category_data: Dict[str, Any]) -> str:
        """カテゴリ別改善提案"""
        indicators = category_data.get("indicators", [])

        # スコアの低い指標を特定
        low_score_indicators = [ind for ind in indicators if ind.get("score", 0) < 60]

        if not low_score_indicators:
            return f"{category_name}の全体的な改善が必要です。"

        suggestions_list = []

        for indicator in low_score_indicators:
            name = indicator.get("displayName", "")
            actual = indicator.get("actual", 0)
            target = indicator.get("target", 0)

            if "カバレッジ" in name:
                suggestions_list.append(f"- {name}を{target}%まで向上（現在: {actual}%）→ テスト追加")
            elif "複雑度" in name:
                suggestions_list.append(f"- {name}を{target}以下に削減（現在: {actual}）→ リファクタリング")
            elif "脆弱性" in name:
                suggestions_list.append(f"- {name}を解消（現在: {actual}件）→ セキュリティパッチ適用")
            elif "ドキュメント" in name:
                suggestions_list.append(f"- {name}を改善（現在: {actual}%）→ ドキュメント追加")
            else:
                suggestions_list.append(f"- {name}を改善（目標: {target}、現在: {actual}）")

        return "\n".join(suggestions_list)

    def _extract_best_practices(self):
        """ベストプラクティス抽出"""
        overall_score = self.current_metrics.get("overall", {}).get("score", 0)

        # 優秀スコア（90以上）の場合
        if overall_score >= 90:
            self.best_practices.append(f"週次品質スコアが{overall_score}点を達成（優秀レベル）")

        # 大幅改善（10点以上）の場合
        for improvement in self.improvements:
            if improvement["improvement"] >= 10:
                self.best_practices.append(
                    f"{improvement['category']}が{improvement['improvement']:.2f}点改善（{improvement['previous']} → {improvement['current']}）"
                )

        # 高スコアカテゴリの手法を抽出
        for category_name, category_data in self.current_metrics.items():
            if category_name in ["overall", "trend", "metadata"]:
                continue

            score = category_data.get("score", 0)

            if score >= 90:
                # このカテゴリの手法をベストプラクティスとして記録
                indicators = category_data.get("indicators", [])
                for indicator in indicators:
                    if indicator.get("score", 0) >= 90:
                        self.best_practices.append(
                            f"{category_name}/{indicator['displayName']}が{indicator['score']}点達成"
                        )

    def _update_claude_md(self):
        """CLAUDE.mdにベストプラクティスを追記"""
        claude_md_path = self.project_root / "CLAUDE.md"

        if not claude_md_path.exists():
            print("    ⚠️  CLAUDE.mdが見つかりません（スキップ）")
            return

        today = datetime.now().strftime("%Y-%m-%d")

        # 既存内容に追記
        with open(claude_md_path, "a", encoding="utf-8") as f:
            f.write(f"\n\n## Auto-Generated Best Practices ({today})\n\n")
            f.write("The following best practices were extracted from weekly quality reports:\n\n")

            for practice in self.best_practices[:5]:  # 上位5件のみ
                f.write(f"- {practice}\n")

        print(f"    ✅ CLAUDE.mdに{len(self.best_practices[:5])}件のベストプラクティスを追記")

    def _save_knowledge(self):
        """ナレッジベースに保存"""
        # 成功パターン
        if self.improvements:
            success_file = self.knowledge_dir / "success_patterns" / f"success_{datetime.now().strftime('%Y%m%d')}.json"
            success_file.parent.mkdir(parents=True, exist_ok=True)

            with open(success_file, "w", encoding="utf-8") as f:
                json.dump({
                    "date": datetime.now().isoformat(),
                    "improvements": self.improvements,
                    "best_practices": self.best_practices
                }, f, indent=2, ensure_ascii=False)

            print(f"    ✅ 成功パターンを保存: {success_file.name}")

        # 失敗パターン
        if self.degradations:
            failure_file = self.knowledge_dir / "failure_patterns" / f"failure_{datetime.now().strftime('%Y%m%d')}.json"
            failure_file.parent.mkdir(parents=True, exist_ok=True)

            with open(failure_file, "w", encoding="utf-8") as f:
                json.dump({
                    "date": datetime.now().isoformat(),
                    "degradations": self.degradations
                }, f, indent=2, ensure_ascii=False)

            print(f"    ✅ 失敗パターンを保存: {failure_file.name}")

    def _generate_markdown_report(self, suggestions: List[Dict[str, Any]]) -> str:
        """Markdownレポート生成"""
        report = f"""# 週次品質レポート

**生成日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 総合スコア

**{self.current_metrics.get('overall', {}).get('score', 0)}/100** - {self.current_metrics.get('overall', {}).get('status', 'N/A')}

"""

        # トレンド表示
        if self.previous_metrics:
            previous_score = self.previous_metrics.get('overall', {}).get('score', 0)
            current_score = self.current_metrics.get('overall', {}).get('score', 0)
            diff = current_score - previous_score

            if diff > 0:
                report += f"📈 **前回比**: +{diff:.2f}点（改善）\n\n"
            elif diff < 0:
                report += f"📉 **前回比**: {diff:.2f}点（低下）\n\n"
            else:
                report += f"➡️ **前回比**: 変化なし\n\n"

        # カテゴリ別スコア
        report += "## 📋 カテゴリ別スコア\n\n"

        for category_name, category_data in self.current_metrics.items():
            if category_name in ["overall", "trend", "metadata"]:
                continue

            score = category_data.get('score', 0)
            status = self._get_score_emoji(score)

            report += f"### {status} {category_name}: {score}/100\n\n"
            report += f"*{category_data.get('description', '')}*\n\n"

            # 指標詳細
            for indicator in category_data.get('indicators', []):
                ind_score = indicator.get('score', 0)
                ind_status = self._get_score_emoji(ind_score)
                report += f"- {ind_status} **{indicator['displayName']}**: {indicator['actual']} (目標: {indicator['target']}) → {ind_score}/100\n"

            report += "\n"

        # 改善提案
        if suggestions:
            report += "## 💡 改善提案\n\n"

            for suggestion in suggestions:
                priority_emoji = "🔴" if suggestion["priority"] == "高" else "🟡"
                report += f"### {priority_emoji} {suggestion['category']} (優先度: {suggestion['priority']})\n\n"
                report += f"**現在スコア**: {suggestion['score']}/100\n\n"
                report += f"{suggestion['suggestion']}\n\n"

        # 改善・低下
        if self.improvements:
            report += "## ✅ 改善されたカテゴリ\n\n"
            for imp in self.improvements:
                report += f"- **{imp['category']}**: {imp['previous']:.2f} → {imp['current']:.2f} (+{imp['improvement']:.2f})\n"
            report += "\n"

        if self.degradations:
            report += "## ⚠️ 低下したカテゴリ\n\n"
            for deg in self.degradations:
                report += f"- **{deg['category']}**: {deg['previous']:.2f} → {deg['current']:.2f} ({deg['degradation']:.2f})\n"
            report += "\n"

        # ベストプラクティス
        if self.best_practices:
            report += "## 🏆 ベストプラクティス\n\n"
            for practice in self.best_practices:
                report += f"- {practice}\n"
            report += "\n"

        report += "---\n\n"
        report += "*🤖 Generated by Compounding Engineering System*\n"

        return report

    def _generate_json_report(self, suggestions: List[Dict[str, Any]]) -> str:
        """JSONレポート生成"""
        report_data = {
            "generated_at": datetime.now().isoformat(),
            "overall": self.current_metrics.get("overall", {}),
            "categories": {
                cat: self.current_metrics[cat]
                for cat in self.current_metrics
                if cat not in ["overall", "trend", "metadata"]
            },
            "improvements": self.improvements,
            "degradations": self.degradations,
            "suggestions": suggestions,
            "best_practices": self.best_practices,
            "metadata": self.current_metrics.get("metadata", {})
        }

        return json.dumps(report_data, indent=2, ensure_ascii=False)

    def _generate_html_report(self, suggestions: List[Dict[str, Any]]) -> str:
        """HTMLダッシュボード生成"""
        # 簡易HTML生成（将来的にはChartJSなどで可視化強化）
        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>週次品質レポート</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
        h2 {{ color: #555; margin-top: 30px; }}
        .overall-score {{ font-size: 48px; font-weight: bold; color: #4CAF50; text-align: center; margin: 20px 0; }}
        .category {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .score-excellent {{ color: #4CAF50; }}
        .score-good {{ color: #2196F3; }}
        .score-acceptable {{ color: #FFC107; }}
        .score-needs-improvement {{ color: #FF9800; }}
        .score-critical {{ color: #F44336; }}
        .indicator {{ margin-left: 20px; padding: 5px 0; }}
        .suggestion {{ background: #FFF3CD; padding: 15px; margin: 10px 0; border-left: 4px solid #FFC107; border-radius: 4px; }}
        .best-practice {{ background: #D4EDDA; padding: 10px; margin: 5px 0; border-left: 4px solid #4CAF50; border-radius: 4px; }}
        .footer {{ text-align: center; margin-top: 40px; color: #888; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 週次品質レポート</h1>
        <p><strong>生成日時</strong>: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

        <h2>総合スコア</h2>
        <div class="overall-score">{self.current_metrics.get('overall', {}).get('score', 0)}/100</div>
        <p style="text-align: center; font-size: 20px;">ステータス: {self.current_metrics.get('overall', {}).get('status', 'N/A')}</p>

        <h2>カテゴリ別スコア</h2>
"""

        for category_name, category_data in self.current_metrics.items():
            if category_name in ["overall", "trend", "metadata"]:
                continue

            score = category_data.get('score', 0)
            score_class = self._get_score_class(score)

            html += f"""
        <div class="category">
            <h3 class="{score_class}">{category_name}: {score}/100</h3>
            <p>{category_data.get('description', '')}</p>
"""

            for indicator in category_data.get('indicators', []):
                ind_score = indicator.get('score', 0)
                ind_class = self._get_score_class(ind_score)
                html += f"""
            <div class="indicator {ind_class}">
                • {indicator['displayName']}: {indicator['actual']} (目標: {indicator['target']}) → {ind_score}/100
            </div>
"""

            html += """
        </div>
"""

        if suggestions:
            html += """
        <h2>💡 改善提案</h2>
"""
            for suggestion in suggestions:
                html += f"""
        <div class="suggestion">
            <h4>{suggestion['category']} (優先度: {suggestion['priority']})</h4>
            <p><strong>現在スコア</strong>: {suggestion['score']}/100</p>
            <pre>{suggestion['suggestion']}</pre>
        </div>
"""

        if self.best_practices:
            html += """
        <h2>🏆 ベストプラクティス</h2>
"""
            for practice in self.best_practices:
                html += f"""
        <div class="best-practice">
            {practice}
        </div>
"""

        html += """
        <div class="footer">
            <p>🤖 Generated by Compounding Engineering System</p>
        </div>
    </div>
</body>
</html>
"""

        return html

    def _get_score_emoji(self, score: float) -> str:
        """スコアに応じた絵文字取得"""
        if score >= 90:
            return "🟢"
        elif score >= 75:
            return "🔵"
        elif score >= 60:
            return "🟡"
        elif score >= 40:
            return "🟠"
        else:
            return "🔴"

    def _get_score_class(self, score: float) -> str:
        """スコアに応じたCSSクラス取得"""
        if score >= 90:
            return "score-excellent"
        elif score >= 75:
            return "score-good"
        elif score >= 60:
            return "score-acceptable"
        elif score >= 40:
            return "score-needs-improvement"
        else:
            return "score-critical"

    def _save_report(self, content: str, format: str) -> str:
        """レポート保存"""
        today = datetime.now().strftime("%Y%m%d")
        filename = f"quality_report_{today}.{format}"
        filepath = self.report_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return str(filepath)


def main():
    """メインエントリポイント"""
    parser = argparse.ArgumentParser(description="週次品質レポート生成スクリプト")
    parser.add_argument("--format", type=str, choices=["markdown", "json", "html"], default="markdown", help="レポート形式")
    parser.add_argument("--save", action="store_true", help="レポートをファイルに保存")

    args = parser.parse_args()

    # レポート生成
    reporter = WeeklyQualityReport()
    report = reporter.generate_report(format=args.format, save=args.save)

    # 画面出力
    if not args.save:
        print("\n" + "=" * 80)
        print(report)
        print("=" * 80)

    print("\n✅ 週次品質レポート生成が完了しました。")


if __name__ == "__main__":
    main()
