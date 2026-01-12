"""SNSカテゴリデータ変換"""

import re
from typing import Dict, Any, List
from ..transformers.app_transformer import AppTransformer


class SnsTransformer(AppTransformer):
    """SNS (v5.0) 分析データの変換（Appトランスフォーマーを継承）"""

    def transform(self, content: str, file_path: str) -> Dict[str, Any]:
        """
        Markdown → 統合JSONレコードに変換

        Args:
            content: Markdownファイル内容
            file_path: ソースファイルパス

        Returns:
            統合スキーマに準拠したJSONレコード
        """
        # YAML Front Matter抽出
        yaml_data, md_content = self.yaml_extractor.extract(content)

        if not yaml_data:
            raise ValueError(f"YAML Front Matter not found in {file_path}")

        # セクション分割
        sections = self.md_parser.parse_sections(md_content)

        # 統合レコード構築
        record = {
            # メタデータ
            "id": yaml_data.get("id"),
            "person_registry_id": self._generate_person_id(yaml_data.get("subject", {})),
            "category": "sns",
            "type": "case_study",
            "version": str(yaml_data.get("version", "5.0")),
            "created_at": yaml_data.get("created_at"),
            "updated_at": yaml_data.get("updated_at"),
            "source_file": file_path,

            # 人物情報
            "subject": self._normalize_subject(yaml_data.get("subject", {})),

            # RAG最適化フィールド（後で生成）
            "embedding_text": "",
            "summary": "",
            "searchable_tags": [],

            # タグ
            "tags": self._normalize_sns_tags(yaml_data.get("tags", {})),

            # 収益
            "revenue": self._normalize_revenue(yaml_data.get("revenue", {})),

            # 日本市場スコア
            "japan_score": self._normalize_japan_score(yaml_data.get("japan_score", {})),

            # 品質
            "quality": self._normalize_quality(yaml_data.get("quality", {})),

            # クロスリファレンス（v5.0必須）
            "cross_reference": self._build_sns_cross_reference(yaml_data),

            # SNS固有データ
            "sns_data": {
                "primary_platform": yaml_data.get("sns_presence", {}).get("primary_platform"),
                "followers": yaml_data.get("sns_presence", {}).get("followers", {}),
                "follower_tier": yaml_data.get("sns_presence", {}).get("follower_tier"),
                "metrics": yaml_data.get("metrics", {}),
                "content_style": yaml_data.get("tags", {}).get("content_style", []),
                "buzz_patterns": yaml_data.get("tags", {}).get("buzz_pattern", []),
                "buzz_score_avg": yaml_data.get("metrics", {}).get("buzz_score_avg"),
                "top_buzz_posts": self._extract_buzz_posts(sections),
                "growth_stage": yaml_data.get("growth_stage", {}),
                "failure_analysis": yaml_data.get("failure_analysis", {}),
            },

            # 本文セクション
            "sections": self._extract_sns_sections(sections),
        }

        # RAG最適化フィールド生成
        record["embedding_text"] = self._generate_sns_embedding_text(record)
        record["summary"] = self._generate_summary(record, sections)
        record["searchable_tags"] = self._generate_searchable_tags(record)

        return record

    def _normalize_sns_tags(self, tags: Dict) -> Dict:
        """SNS用タグの正規化"""
        return {
            "growth_strategy": tags.get("growth_strategy", []),
            "niche": tags.get("niche", []),
            "marketing_channel": tags.get("marketing_channel", []),
            "success_pattern": tags.get("success_pattern", []),
            "monetization": tags.get("monetization", []),
            "content_style": tags.get("content_style", []),
            "buzz_pattern": tags.get("buzz_pattern", []),
        }

    def _build_sns_cross_reference(self, yaml_data: Dict) -> Dict:
        """SNS用クロスリファレンス構築（v5.0必須化）"""
        cross_ref = yaml_data.get("cross_reference", {})

        return {
            "app_id": cross_ref.get("app_id"),
            "newsletter_id": cross_ref.get("newsletter_id"),
            "sns_id": None,  # 自分自身はNone
            "person_registry_id": cross_ref.get("person_registry_id"),
            "funnel_integration": cross_ref.get("funnel_integration"),
            "cross_leverage_score": cross_ref.get("cross_leverage_score"),
        }

    def _extract_buzz_posts(self, sections: Dict) -> List[Dict]:
        """バズ投稿TOP5の抽出"""
        buzz_keys = ["バズ投稿TOP5", "Top Buzz Posts"]

        for key in buzz_keys:
            if key in sections:
                tables = self.table_parser.extract_tables_from_section(sections[key])
                if tables and len(tables) > 0:
                    return tables[0][:5]

        return []

    def _extract_sns_sections(self, sections: Dict) -> Dict:
        """SNS用本文セクションの抽出"""
        section_mapping = {
            "基本情報": "basic_info",
            "成長曲線分析": "growth_analysis",
            "成功要因分析": "success_factors",
            "SNS戦略示唆": "strategy_insights",
            "事業アイデア候補": "business_ideas",
        }

        extracted = {}
        for md_key, json_key in section_mapping.items():
            if md_key in sections:
                content = sections[md_key]

                # リスト形式のセクションは配列に変換
                if json_key in ["business_ideas"]:
                    extracted[json_key] = self.md_parser.extract_lists(content)
                else:
                    extracted[json_key] = content

        return extracted

    def _generate_sns_embedding_text(self, record: Dict) -> str:
        """SNS用embedding_textを生成"""
        subject = record.get("subject", {})
        revenue = record.get("revenue", {})
        sns_data = record.get("sns_data", {})
        tags = record.get("tags", {})
        japan_score = record.get("japan_score", {})

        name = subject.get("name", "Unknown")
        handle = subject.get("twitter_handle", "")
        platform = sns_data.get("primary_platform", "")
        followers = sns_data.get("followers", {})

        # メインフォロワー数
        main_followers = followers.get(platform, 0) if platform else 0

        mrr = revenue.get("mrr_usd")
        mrr_display = f"${mrr/1000:.0f}K" if mrr else "不明"

        # タグを文字列化
        growth_tags = ", ".join(tags.get("growth_strategy", []))
        content_style = ", ".join(tags.get("content_style", []))

        rating = japan_score.get("rating", "")
        score = japan_score.get("total", "")

        text = f"""[SNS] {name} (@{handle})

主要プラットフォーム: {platform} ({main_followers:,} followers)
収益: MRR {mrr_display}/月

成長戦略: {growth_tags}
コンテンツスタイル: {content_style}

日本適用性: {rating} ({score}/5.0)
"""

        return text.strip()
