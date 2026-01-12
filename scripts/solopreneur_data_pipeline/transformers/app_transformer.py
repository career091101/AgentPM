"""Appカテゴリデータ変換"""

import re
from typing import Dict, Any, List, Optional
from datetime import datetime
from ..parsers import YamlExtractor, MarkdownParser, TableParser


class AppTransformer:
    """App (v4.0) ケーススタディデータの変換"""

    def __init__(self):
        self.yaml_extractor = YamlExtractor()
        self.md_parser = MarkdownParser()
        self.table_parser = TableParser()

    def transform(self, content: str, file_path: str) -> Dict[str, Any]:
        """
        Markdown → 統合JSONレコードに変換

        Args:
            content: Markdownファイル内容
            file_path: ソースファイルパス

        Returns:
            統合スキーマに準拠したJSONレコード
        """
        # 1. YAML Front Matter抽出
        yaml_data, md_content = self.yaml_extractor.extract(content)

        if not yaml_data:
            raise ValueError(f"YAML Front Matter not found in {file_path}")

        # 2. セクション分割
        sections = self.md_parser.parse_sections(md_content)

        # 3. 統合レコード構築
        record = {
            # メタデータ
            "id": yaml_data.get("id"),
            "person_registry_id": self._generate_person_id(yaml_data.get("subject", {})),
            "category": "app",
            "type": "case_study",
            "version": str(yaml_data.get("version", "4.0")),
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
            "tags": self._normalize_tags(yaml_data.get("tags", {})),

            # 収益
            "revenue": self._normalize_revenue(yaml_data.get("revenue", {})),

            # 日本市場スコア
            "japan_score": self._normalize_japan_score(yaml_data.get("japan_score", {})),

            # 品質
            "quality": self._normalize_quality(yaml_data.get("quality", {})),

            # クロスリファレンス
            "cross_reference": self._build_cross_reference(yaml_data),

            # App固有データ
            "app_data": {
                "main_product": yaml_data.get("main_product", {}),
                "tech_stack": yaml_data.get("tags", {}).get("tech_stack", []),
                "products_count": yaml_data.get("revenue", {}).get("products_count"),
                "failure_history": self._extract_failure_history(sections),
                "timeline": self._extract_timeline(sections),
                "japan_factors": self._extract_japan_factors(yaml_data.get("japan_score", {})),
            },

            # 本文セクション
            "sections": self._extract_sections(sections),
        }

        # RAG最適化フィールド生成
        record["embedding_text"] = self._generate_embedding_text(record)
        record["summary"] = self._generate_summary(record, sections)
        record["searchable_tags"] = self._generate_searchable_tags(record)

        return record

    def _generate_person_id(self, subject: Dict) -> str:
        """Person Registry IDを生成"""
        name = subject.get("name", "unknown")
        # スペースをアンダースコアに、小文字化
        normalized_name = name.lower().replace(" ", "_")
        # 特殊文字除去
        normalized_name = re.sub(r'[^a-z0-9_]', '', normalized_name)
        return f"PERSON_{normalized_name}"

    def _normalize_subject(self, subject: Dict) -> Dict:
        """人物情報の正規化"""
        return {
            "name": subject.get("name"),
            "name_ja": subject.get("name_ja"),
            "aliases": subject.get("aliases", []),
            "nationality": subject.get("nationality"),
            "twitter_handle": subject.get("twitter_handle"),
        }

    def _normalize_tags(self, tags: Dict) -> Dict:
        """タグの正規化"""
        return {
            "growth_strategy": tags.get("growth_strategy", []),
            "niche": tags.get("niche", []),
            "marketing_channel": tags.get("marketing_channel", []),
            "success_pattern": tags.get("success_pattern", []),
            "monetization": tags.get("monetization", []),
        }

    def _normalize_revenue(self, revenue: Dict) -> Dict:
        """収益データの正規化"""
        mrr = revenue.get("mrr_usd")
        if isinstance(mrr, str):
            mrr = self._parse_revenue_string(mrr)

        arr = revenue.get("arr_usd")
        if not arr and mrr:
            arr = mrr * 12

        return {
            "mrr_usd": mrr,
            "mrr_tier": revenue.get("mrr_tier"),
            "arr_usd": arr,
            "exit_value_usd": revenue.get("exit_value_usd"),
        }

    def _parse_revenue_string(self, s: str) -> Optional[int]:
        """収益文字列をパース: "$10K", "10000", "$1.2M" → int"""
        if not s:
            return None

        s = s.replace("$", "").replace(",", "").strip()
        multiplier = 1

        if s.endswith("K") or s.endswith("k"):
            multiplier = 1000
            s = s[:-1]
        elif s.endswith("M") or s.endswith("m"):
            multiplier = 1000000
            s = s[:-1]

        try:
            return int(float(s) * multiplier)
        except (ValueError, TypeError):
            return None

    def _normalize_japan_score(self, japan_score: Dict) -> Dict:
        """日本市場スコアの正規化"""
        return {
            "total": japan_score.get("total"),
            "rating": japan_score.get("rating"),
            "comment": japan_score.get("comment"),
        }

    def _normalize_quality(self, quality: Dict) -> Dict:
        """品質情報の正規化"""
        return {
            "fact_check": quality.get("fact_check", "pending"),
            "sources_count": quality.get("sources_count", 0),
            "last_verified": quality.get("last_verified"),
        }

    def _build_cross_reference(self, yaml_data: Dict) -> Dict:
        """クロスリファレンス構築"""
        related = yaml_data.get("related", [])

        return {
            "app_id": None,
            "newsletter_id": None,
            "sns_id": None,
            "funnel_integration": None,
            "related": related if isinstance(related, list) else [],
        }

    def _extract_failure_history(self, sections: Dict) -> Dict:
        """失敗プロダクト情報の抽出"""
        failure_section_keys = ["失敗プロダクト詳細", "失敗歴", "Failure Products"]

        for key in failure_section_keys:
            if key in sections:
                tables = self.table_parser.extract_tables_from_section(sections[key])
                if tables and len(tables) > 0:
                    return {
                        "total_failures": len(tables[0]),
                        "notable_failures": tables[0][:5],  # 最大5件
                    }

        return {"total_failures": None, "notable_failures": []}

    def _extract_timeline(self, sections: Dict) -> List[Dict]:
        """タイムラインの抽出"""
        timeline_keys = [
            "タイムライン",
            "ストーリー（時系列）",
            "ストーリー・タイムライン",
            "ストーリー",
            "Timeline"
        ]

        for key in timeline_keys:
            if key in sections:
                tables = self.table_parser.extract_tables_from_section(sections[key])
                if tables and len(tables) > 0:
                    return tables[0]

        return []

    def _extract_japan_factors(self, japan_score: Dict) -> Dict:
        """日本市場評価詳細の抽出"""
        factors = japan_score.get("factors", {})

        return {
            "product_similarity": factors.get("product_similarity"),
            "market_need": factors.get("market_need"),
            "competition": factors.get("competition"),
            "localization": factors.get("localization"),
            "reproducibility": factors.get("reproducibility"),
        }

    def _extract_sections(self, sections: Dict) -> Dict:
        """本文セクションの抽出（柔軟なマッチング）"""
        # セクション名のバリエーションを定義（複数の候補キーワード）
        section_patterns = {
            "basic_info": ["基本情報"],
            "revenue_summary": ["収益サマリー", "収益・ビジネスモデル", "収益データ", "ビジネスモデル"],
            "product_info": ["プロダクト情報", "メインプロダクト"],
            "story": ["ストーリー（時系列）", "ストーリー・タイムライン", "ストーリー", "タイムライン"],
            "growth_strategy": ["成長施策（マーケティング）", "成長施策", "マーケティング"],
            "tech_stack": ["使用ツール", "技術スタック"],
            "content_strategy": ["コンテンツ発信", "発信戦略"],
            "success_factors": ["成功要因分析", "成功要因"],
            "lessons": ["教訓・アドバイス", "教訓", "アドバイス"],
            "business_ideas": ["事業アイデア候補", "事業アイデア"],
        }

        extracted = {}
        for json_key, patterns in section_patterns.items():
            # 各パターンでマッチングを試行
            for pattern in patterns:
                if pattern in sections:
                    content = sections[pattern]

                    # リスト形式のセクションは配列に変換
                    if json_key in ["lessons", "business_ideas"]:
                        extracted[json_key] = self.md_parser.extract_lists(content)
                    else:
                        extracted[json_key] = content
                    break  # 最初にマッチしたパターンで終了

        return extracted

    def _generate_embedding_text(self, record: Dict) -> str:
        """RAG用embedding_textを生成"""
        subject = record.get("subject", {})
        revenue = record.get("revenue", {})
        app_data = record.get("app_data", {})
        tags = record.get("tags", {})
        japan_score = record.get("japan_score", {})

        name = subject.get("name", "Unknown")
        handle = subject.get("twitter_handle", "")
        product = app_data.get("main_product", {}).get("name", "")

        mrr = revenue.get("mrr_usd")
        mrr_display = f"${mrr/1000:.0f}K" if mrr else "不明"

        # タグを文字列化
        growth_tags = ", ".join(tags.get("growth_strategy", []))
        niche_tags = ", ".join(tags.get("niche", []))
        channel_tags = ", ".join(tags.get("marketing_channel", []))

        rating = japan_score.get("rating", "")
        score = japan_score.get("total", "")

        text = f"""[App] {name} (@{handle}) - {product}

収益: MRR {mrr_display}/月

成長戦略: {growth_tags}
ニッチ: {niche_tags}
マーケティング: {channel_tags}

日本適用性: {rating} ({score}/5.0)
"""

        return text.strip()

    def _generate_summary(self, record: Dict, sections: Dict) -> str:
        """概要テキストを生成"""
        # ストーリーセクションの最初の段落、または基本情報から生成
        story_keys = ["ストーリー（時系列）", "ストーリー・タイムライン", "ストーリー", "Story"]
        for key in story_keys:
            if key in sections:
                story = sections[key]
                # 最初の段落を抽出（最大200文字）
                first_para = story.split('\n\n')[0] if story else ""
                return first_para[:200]

        # フォールバック: 基本情報から
        basic_keys = ["基本情報", "Basic Info"]
        for key in basic_keys:
            if key in sections:
                return sections[key][:200]

        return ""

    def _generate_searchable_tags(self, record: Dict) -> List[str]:
        """検索用タグを生成"""
        tags = []

        # 人物名
        subject = record.get("subject", {})
        if subject.get("name"):
            tags.append(subject["name"].lower().replace(" ", "_"))
        if subject.get("twitter_handle"):
            tags.append(subject["twitter_handle"].lower())

        # プロダクト名
        app_data = record.get("app_data", {})
        product_name = app_data.get("main_product", {}).get("name")
        if product_name:
            tags.append(product_name.lower().replace(" ", "_"))

        # タグカテゴリの全タグ
        for tag_category in record.get("tags", {}).values():
            if isinstance(tag_category, list):
                tags.extend([t.lower() for t in tag_category])

        # 技術スタック
        tech_stack = app_data.get("tech_stack", [])
        tags.extend([t.lower() for t in tech_stack])

        # 重複除去
        return list(set(tags))
