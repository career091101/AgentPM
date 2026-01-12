#!/usr/bin/env python3
"""
Index Builder for Founder Research Case Studies

ケーススタディのインデックスを自動生成するスクリプト。
6種類のインデックスを作成:
- by_industry.md (業界別)
- by_stage.md (ステージ別)
- by_pivot_type.md (Pivot類型別)
- by_failure_pattern.md (失敗パターン別)
- by_10x_axis.md (10倍優位性軸別)
- by_cpf_score.md (CPFスコア別)
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any

class IndexBuilder:
    """ケーススタディインデックス自動生成"""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.documents_path = self.base_path / "documents"
        self.index_path = self.base_path / "_index"
        self.case_studies = []

    def load_all_case_studies(self):
        """全ケーススタディのYAML Front Matterを読み込み"""
        print("📚 ケーススタディを読み込み中...")

        for category_dir in self.documents_path.iterdir():
            if not category_dir.is_dir():
                continue

            for md_file in category_dir.glob("FOUNDER_*.md"):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # YAML Front Matter抽出
                    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if match:
                        yaml_content = match.group(1)
                        metadata = yaml.safe_load(yaml_content)

                        # ファイルパス追加
                        metadata['_file_path'] = str(md_file.relative_to(self.base_path))
                        metadata['_file_name'] = md_file.name

                        self.case_studies.append(metadata)

                except Exception as e:
                    print(f"⚠️  {md_file.name}: {e}")

        print(f"✅ {len(self.case_studies)}件のケーススタディを読み込みました")

    def build_industry_index(self):
        """業界別インデックス作成"""
        print("\n🏭 業界別インデックス作成中...")

        industry_map = defaultdict(list)

        for cs in self.case_studies:
            # タグから業界を抽出
            tags = cs.get('tags', [])
            industry = cs.get('company', {}).get('industry', '不明')

            # 業界分類
            if any(tag in ['saas', 'enterprise', 'b2b'] for tag in tags):
                category = 'SaaS'
            elif any(tag in ['marketplace', 'ecommerce', 'e-commerce'] for tag in tags):
                category = 'Marketplace / E-commerce'
            elif any(tag in ['fintech', 'finance', 'payment'] for tag in tags):
                category = 'Fintech'
            elif any(tag in ['healthtech', 'medtech', 'health'] for tag in tags):
                category = 'Healthtech'
            elif any(tag in ['ai', 'ml', 'machine_learning'] for tag in tags):
                category = 'AI / ML'
            else:
                category = industry

            industry_map[category].append(cs)

        # Markdown生成
        md_content = "# ケーススタディ業界別インデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        for industry, cases in sorted(industry_map.items(), key=lambda x: len(x[1]), reverse=True):
            md_content += f"## {industry}（{len(cases)}件）\n\n"

            for cs in sorted(cases, key=lambda x: x.get('id', '')):
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')
                cpf_score = cs.get('validation_data', {}).get('cpf', {}).get('problem_commonality', 'N/A')
                ten_x_count = len(cs.get('validation_data', {}).get('psf', {}).get('ten_x_axes', []))

                md_content += f"- [{title}]({file_path})\n"
                md_content += f"  - CPF: {cpf_score}%, PSF: {ten_x_count}軸\n"

            md_content += "\n"

        # ファイル保存
        self.index_path.mkdir(exist_ok=True)
        with open(self.index_path / "by_industry.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_industry.md 作成完了（{len(industry_map)}業界）")

    def build_stage_index(self):
        """ステージ別インデックス作成"""
        print("\n📊 ステージ別インデックス作成中...")

        stage_map = defaultdict(list)

        for cs in self.case_studies:
            tier = cs.get('tier', 'unknown')

            # ステージ分類
            if tier in ['legendary', 'ipo_japan', 'ipo_global']:
                stage = 'IPO / Legendary'
            elif tier == 'unicorn':
                stage = 'Unicorn ($1B+)'
            elif tier == 'vc_backed':
                # 資金調達ラウンドで細分化
                rounds = cs.get('funding', {}).get('funding_rounds', [])
                if any(r.get('round', '') in ['series_d', 'series_e'] for r in rounds):
                    stage = 'Series D+'
                elif any(r.get('round', '') == 'series_c' for r in rounds):
                    stage = 'Series C'
                elif any(r.get('round', '') == 'series_b' for r in rounds):
                    stage = 'Series B'
                elif any(r.get('round', '') == 'series_a' for r in rounds):
                    stage = 'Series A'
                else:
                    stage = 'Seed / Early'
            elif tier == 'emerging':
                stage = 'Emerging (2020-)'
            else:
                stage = 'その他'

            stage_map[stage].append(cs)

        # Markdown生成
        md_content = "# ケーススタディステージ別インデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        # ステージ順序定義
        stage_order = ['IPO / Legendary', 'Unicorn ($1B+)', 'Series D+', 'Series C',
                       'Series B', 'Series A', 'Seed / Early', 'Emerging (2020-)', 'その他']

        for stage in stage_order:
            if stage not in stage_map:
                continue

            cases = stage_map[stage]
            md_content += f"## {stage}（{len(cases)}件）\n\n"

            for cs in sorted(cases, key=lambda x: x.get('id', '')):
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')
                valuation = cs.get('company', {}).get('valuation', 'N/A')

                md_content += f"- [{title}]({file_path})\n"
                md_content += f"  - 評価額: {valuation}\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "by_stage.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_stage.md 作成完了（{len(stage_map)}ステージ）")

    def build_10x_axis_index(self):
        """10倍優位性軸別インデックス作成"""
        print("\n🚀 10倍優位性軸別インデックス作成中...")

        axis_map = defaultdict(list)

        for cs in self.case_studies:
            ten_x_axes = cs.get('validation_data', {}).get('psf', {}).get('ten_x_axes', [])

            for axis_data in ten_x_axes:
                axis = axis_data.get('axis', '不明')
                multiplier = axis_data.get('multiplier', 0)

                # Convert to float for comparison (handle string values)
                try:
                    multiplier_num = float(multiplier) if multiplier else 0
                except (ValueError, TypeError):
                    multiplier_num = 0

                if multiplier_num >= 3:  # 3倍以上のみ
                    axis_map[axis].append({
                        'case_study': cs,
                        'multiplier': multiplier
                    })

        # Markdown生成
        md_content = "# ケーススタディ10倍優位性軸別インデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        for axis, items in sorted(axis_map.items(), key=lambda x: len(x[1]), reverse=True):
            md_content += f"## {axis}（{len(items)}件）\n\n"

            # 倍率降順でソート
            for item in sorted(items, key=lambda x: x['multiplier'], reverse=True):
                cs = item['case_study']
                multiplier = item['multiplier']
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')

                md_content += f"- [{title}]({file_path}) - **{multiplier}倍**\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "by_10x_axis.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_10x_axis.md 作成完了（{len(axis_map)}軸）")

    def build_cpf_score_index(self):
        """CPFスコア別インデックス作成"""
        print("\n📈 CPFスコア別インデックス作成中...")

        score_ranges = {
            '90-100%（優秀）': [],
            '80-89%（良好）': [],
            '70-79%（合格）': [],
            '60-69%（基準値）': [],
            '60%未満（要改善）': [],
            'データなし': []
        }

        for cs in self.case_studies:
            cpf_score = cs.get('validation_data', {}).get('cpf', {}).get('problem_commonality')

            if cpf_score is None:
                score_ranges['データなし'].append(cs)
            elif cpf_score >= 90:
                score_ranges['90-100%（優秀）'].append(cs)
            elif cpf_score >= 80:
                score_ranges['80-89%（良好）'].append(cs)
            elif cpf_score >= 70:
                score_ranges['70-79%（合格）'].append(cs)
            elif cpf_score >= 60:
                score_ranges['60-69%（基準値）'].append(cs)
            else:
                score_ranges['60%未満（要改善）'].append(cs)

        # Markdown生成
        md_content = "# ケーススタディCPFスコア別インデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"
        md_content += "**CPF基準値**: 60%以上\n\n"

        for range_name, cases in score_ranges.items():
            if not cases:
                continue

            md_content += f"## {range_name}（{len(cases)}件）\n\n"

            # Sort with safe numeric conversion
            def get_cpf_score(cs):
                val = cs.get('validation_data', {}).get('cpf', {}).get('problem_commonality', 0)
                try:
                    return float(val) if val is not None else 0
                except (ValueError, TypeError):
                    return 0

            for cs in sorted(cases, key=get_cpf_score, reverse=True):
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')
                cpf_score = cs.get('validation_data', {}).get('cpf', {}).get('problem_commonality', 'N/A')
                interview_count = cs.get('validation_data', {}).get('cpf', {}).get('interview_count', 'N/A')

                md_content += f"- [{title}]({file_path})\n"
                md_content += f"  - CPF: {cpf_score}%, インタビュー数: {interview_count}\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "by_cpf_score.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_cpf_score.md 作成完了")

    def build_pivot_index(self):
        """Pivot類型別インデックス作成"""
        print("\n🔄 Pivot類型別インデックス作成中...")

        pivot_map = defaultdict(list)

        for cs in self.case_studies:
            pivot_occurred = cs.get('validation_data', {}).get('pivot', {}).get('occurred', False)

            if pivot_occurred:
                pivot_trigger = cs.get('validation_data', {}).get('pivot', {}).get('pivot_trigger', '不明')
                pivot_map[pivot_trigger].append(cs)

        # Markdown生成
        md_content = "# ケーススタディPivot類型別インデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**Pivot実施**: {sum(len(cases) for cases in pivot_map.values())}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        for trigger, cases in sorted(pivot_map.items(), key=lambda x: len(x[1]), reverse=True):
            md_content += f"## {trigger}（{len(cases)}件）\n\n"

            for cs in sorted(cases, key=lambda x: x.get('id', '')):
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')
                original_idea = cs.get('validation_data', {}).get('pivot', {}).get('original_idea', 'N/A')
                pivoted_to = cs.get('validation_data', {}).get('pivot', {}).get('pivoted_to', 'N/A')

                md_content += f"- [{title}]({file_path})\n"
                md_content += f"  - 元: {original_idea}\n"
                md_content += f"  - 後: {pivoted_to}\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "by_pivot_type.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_pivot_type.md 作成完了（{len(pivot_map)}類型）")

    def build_failure_pattern_index(self):
        """失敗パターン別インデックス作成（起業の科学P11-P30対応）"""
        print("\n❌ 失敗パターン別インデックス作成中...")

        failure_map = defaultdict(list)

        for cs in self.case_studies:
            failure_pattern = cs.get('outcome', {}).get('failure_pattern', '')

            if failure_pattern:
                failure_map[failure_pattern].append(cs)

        # Markdown生成
        md_content = "# ケーススタディ失敗パターン別インデックス\n\n"
        md_content += "**起業の科学P11-P30失敗パターン対応**\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**失敗事例**: {sum(len(cases) for cases in failure_map.values())}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        for pattern, cases in sorted(failure_map.items(), key=lambda x: len(x[1]), reverse=True):
            md_content += f"## {pattern}（{len(cases)}件）\n\n"

            for cs in sorted(cases, key=lambda x: x.get('id', '')):
                title = cs.get('title', '不明')
                file_path = cs.get('_file_path', '')

                md_content += f"- [{title}]({file_path})\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "by_failure_pattern.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ by_failure_pattern.md 作成完了（{len(failure_map)}パターン）")

    def build_master_index(self):
        """マスターインデックス作成（全ケーススタディのリスト）"""
        print("\n📋 マスターインデックス作成中...")

        md_content = "# ケーススタディマスターインデックス\n\n"
        md_content += f"**総件数**: {len(self.case_studies)}件\n"
        md_content += f"**最終更新**: {self._get_today()}\n\n"

        # カテゴリ別
        categories = defaultdict(list)
        for cs in self.case_studies:
            tier = cs.get('tier', 'unknown')
            categories[tier].append(cs)

        for tier, cases in sorted(categories.items()):
            tier_name = self._tier_name(tier)
            md_content += f"## {tier_name}（{len(cases)}件）\n\n"

            md_content += "| ID | タイトル | 業界 | CPF | PSF軸数 | ファイル |\n"
            md_content += "|:--:|---------|------|:---:|:------:|--------|\n"

            for cs in sorted(cases, key=lambda x: x.get('id', '')):
                cs_id = cs.get('id', 'N/A')
                title = cs.get('title', '不明')
                industry = cs.get('company', {}).get('industry', 'N/A')
                cpf = cs.get('validation_data', {}).get('cpf', {}).get('problem_commonality', 'N/A')
                psf_axes = len(cs.get('validation_data', {}).get('psf', {}).get('ten_x_axes', []))
                file_path = cs.get('_file_path', '')

                md_content += f"| {cs_id} | {title} | {industry} | {cpf}% | {psf_axes} | [{cs.get('_file_name', '')}]({file_path}) |\n"

            md_content += "\n"

        # ファイル保存
        with open(self.index_path / "master_index.md", 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ master_index.md 作成完了")

    def build_all_indexes(self):
        """全インデックスを一括作成"""
        print("\n" + "="*60)
        print("🚀 インデックス自動生成開始")
        print("="*60)

        self.load_all_case_studies()

        if not self.case_studies:
            print("⚠️  ケーススタディが見つかりません")
            return

        self.build_industry_index()
        self.build_stage_index()
        self.build_10x_axis_index()
        self.build_cpf_score_index()
        self.build_pivot_index()
        self.build_failure_pattern_index()
        self.build_master_index()

        print("\n" + "="*60)
        print(f"✅ インデックス作成完了: {len(self.case_studies)}件")
        print("="*60)

    def _get_today(self):
        """今日の日付取得"""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')

    def _tier_name(self, tier: str) -> str:
        """Tier名を日本語に変換"""
        tier_map = {
            'legendary': '01_Legendary（レジェンド）',
            'unicorn': '02_Unicorn（ユニコーン）',
            'vc_backed': '03_VC_Backed（VC調達済み）',
            'ipo_japan': '04_IPO_Japan（日本上場）',
            'ipo_global': '05_IPO_Global（海外上場）',
            'pivot': '06_Pivot_Success（ピボット成功）',
            'failure': '07_Failure_Study（失敗事例）',
            'emerging': '08_Emerging（新興）'
        }
        return tier_map.get(tier, tier)


if __name__ == "__main__":
    # 実行
    base_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research"

    builder = IndexBuilder(base_path)
    builder.build_all_indexes()
