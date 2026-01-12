"""Newsletterカテゴリデータ変換"""

from typing import Dict, Any
from ..transformers.app_transformer import AppTransformer


class NewsletterTransformer(AppTransformer):
    """Newsletter (v2.1) ケーススタディデータの変換"""

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
            "person_registry_id": self._generate_person_id_from_founder(yaml_data),
            "category": "newsletter",
            "type": "case_study",
            "version": str(yaml_data.get("version", "2.1")),
            "created_at": yaml_data.get("created"),
            "updated_at": yaml_data.get("updated"),
            "source_file": file_path,

            # 人物情報（Newsletter用に調整）
            "subject": self._normalize_newsletter_subject(yaml_data),

            # RAG最適化フィールド（後で生成）
            "embedding_text": "",
            "summary": "",
            "searchable_tags": [],

            # タグ
            "tags": self._normalize_newsletter_tags(yaml_data),

            # 収益
            "revenue": self._normalize_newsletter_revenue(yaml_data),

            # 日本市場スコア
            "japan_score": self._normalize_newsletter_japan_score(yaml_data.get("japan_market_score", {})),

            # 品質
            "quality": {
                "fact_check": "pending",
                "sources_count": 0,
                "last_verified": None,
            },

            # クロスリファレンス
            "cross_reference": self._build_newsletter_cross_reference(yaml_data),

            # Newsletter固有データ
            "newsletter_data": {
                "newsletter_name": yaml_data.get("newsletter_name"),
                "platform": yaml_data.get("platform"),
                "language": yaml_data.get("language"),
                "start_date": None,
                "frequency": None,
                "subscribers": {
                    "total": yaml_data.get("subscribers_total"),
                    "paid": yaml_data.get("subscribers_paid"),
                    "paid_conversion_rate": yaml_data.get("paid_conversion_rate"),
                    "open_rate": yaml_data.get("open_rate"),
                    "click_rate": yaml_data.get("click_rate"),
                    "churn_rate": yaml_data.get("churn_rate"),
                },
                "content_style": yaml_data.get("content_style", []),
                "viral_analysis": yaml_data.get("viral_metrics", {}),
                "growth_stage": yaml_data.get("growth_stage", {}),
                "unit_economics": {
                    "ltv_usd": None,
                    "cac_usd": None,
                    "ltv_cac_ratio": None,
                },
            },

            # 本文セクション
            "sections": self._extract_newsletter_sections(sections),
        }

        # RAG最適化フィールド生成
        record["embedding_text"] = self._generate_newsletter_embedding_text(record)
        record["summary"] = self._generate_summary(record, sections)
        record["searchable_tags"] = self._generate_searchable_tags(record)

        return record

    def _generate_person_id_from_founder(self, yaml_data: Dict) -> str:
        """創業者名からPerson Registry IDを生成"""
        founder_name = yaml_data.get("founder_name", "unknown")
        normalized_name = founder_name.lower().replace(" ", "_")
        import re
        normalized_name = re.sub(r'[^a-z0-9_]', '', normalized_name)
        return f"PERSON_{normalized_name}"

    def _normalize_newsletter_subject(self, yaml_data: Dict) -> Dict:
        """Newsletter用人物情報の正規化"""
        return {
            "name": yaml_data.get("founder_name"),
            "name_ja": None,
            "aliases": [],
            "nationality": None,
            "twitter_handle": yaml_data.get("founder_twitter"),
        }

    def _normalize_newsletter_tags(self, yaml_data: Dict) -> Dict:
        """Newsletter用タグの正規化"""
        return {
            "growth_strategy": yaml_data.get("growth_strategies", []),
            "niche": [yaml_data.get("niche")] if yaml_data.get("niche") else [],
            "marketing_channel": yaml_data.get("marketing_channel", []),
            "success_pattern": yaml_data.get("success_pattern", []),
            "monetization": yaml_data.get("monetization", []),
            "content_style": yaml_data.get("content_style", []),
        }

    def _normalize_newsletter_revenue(self, yaml_data: Dict) -> Dict:
        """Newsletter用収益の正規化"""
        mrr = yaml_data.get("mrr_usd")
        arr = yaml_data.get("arr_usd")

        if not arr and mrr:
            arr = mrr * 12

        return {
            "mrr_usd": mrr,
            "mrr_tier": yaml_data.get("mrr_tier"),
            "arr_usd": arr,
            "exit_value_usd": None,
        }

    def _normalize_newsletter_japan_score(self, japan_market_score: Dict) -> Dict:
        """Newsletter用日本市場スコアの正規化"""
        overall = japan_market_score.get("overall")

        # ratingの推定
        rating = None
        if overall:
            if overall >= 4.0:
                rating = "very_high"
            elif overall >= 3.0:
                rating = "high"
            elif overall >= 2.0:
                rating = "medium"
            else:
                rating = "low"

        return {
            "total": overall,
            "rating": rating,
            "comment": None,
        }

    def _build_newsletter_cross_reference(self, yaml_data: Dict) -> Dict:
        """Newsletter用クロスリファレンス構築"""
        cross_ref = yaml_data.get("cross_reference", {})

        return {
            "app_id": cross_ref.get("app_id"),
            "newsletter_id": None,  # 自分自身はNone
            "sns_id": cross_ref.get("sns_id"),
            "person_registry_id": cross_ref.get("person_registry_id"),
            "funnel_integration": cross_ref.get("funnel_integration"),
        }

    def _extract_newsletter_sections(self, sections: Dict) -> Dict:
        """Newsletter用本文セクションの抽出"""
        section_mapping = {
            "基本情報": "basic_info",
            "運営者プロフィール": "founder_profile",
            "成功要因分析": "success_factors",
            "学びとアクションポイント": "lessons",
        }

        extracted = {}
        for md_key, json_key in section_mapping.items():
            if md_key in sections:
                content = sections[md_key]

                # リスト形式のセクションは配列に変換
                if json_key in ["lessons"]:
                    extracted[json_key] = self.md_parser.extract_lists(content)
                else:
                    extracted[json_key] = content

        return extracted

    def _generate_newsletter_embedding_text(self, record: Dict) -> str:
        """Newsletter用embedding_textを生成"""
        subject = record.get("subject", {})
        revenue = record.get("revenue", {})
        newsletter_data = record.get("newsletter_data", {})
        tags = record.get("tags", {})
        japan_score = record.get("japan_score", {})

        founder = subject.get("name", "Unknown")
        handle = subject.get("twitter_handle", "")
        newsletter_name = newsletter_data.get("newsletter_name", "")
        platform = newsletter_data.get("platform", "")

        subscribers_total = newsletter_data.get("subscribers", {}).get("total", 0)

        mrr = revenue.get("mrr_usd")
        mrr_display = f"${mrr/1000:.0f}K" if mrr else "不明"

        # タグを文字列化
        growth_tags = ", ".join(tags.get("growth_strategy", []))
        content_style = ", ".join(tags.get("content_style", []))

        rating = japan_score.get("rating", "")
        score = japan_score.get("total", "")

        text = f"""[Newsletter] {founder} (@{handle}) - {newsletter_name}

プラットフォーム: {platform}
購読者: {subscribers_total:,}人
収益: MRR {mrr_display}/月

成長戦略: {growth_tags}
コンテンツスタイル: {content_style}

日本適用性: {rating} ({score}/5.0)
"""

        return text.strip()
