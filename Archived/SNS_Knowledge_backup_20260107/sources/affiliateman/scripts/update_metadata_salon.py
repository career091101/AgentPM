#!/usr/bin/env python3
"""
metadata.jsonにサロン限定特典セクションを追加するスクリプト
"""

import json
from pathlib import Path

# パス設定
project_root = Path(__file__).parent.parent
metadata_path = project_root / "metadata.json"

# metadata.jsonを読み込み
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# サロン限定特典セクションを追加
salon_exclusive = [
    {
        "title": "【サロン限定企画】売れている有料note 全てプレゼント！！",
        "url": "https://affiliateman.site/notelink/",
        "category": "salon_exclusive",
        "description": "カテゴリーごとに300URL記載、合計3万URLのスプレッドシート配布企画",
        "filepath": str(project_root / "salon_exclusive" / "売れている有料note_3万URL配布.md")
    },
    {
        "title": "【サロン限定特典】インスタ分析シート一覧",
        "url": "https://affiliateman.site/insta_pre/",
        "category": "salon_exclusive",
        "description": "インスタ30ジャンル/計1000アカ以上の分析シート",
        "filepath": str(project_root / "salon_exclusive" / "インスタ全ジャンルアカ一覧.md")
    },
    {
        "title": "【サロン限定】拡散部屋の説明について",
        "url": "https://fqw45966.site/bazz/",
        "category": "salon_exclusive",
        "description": "サロンメンバー同士でエンゲージメントを高める拡散部屋の使い方",
        "filepath": str(project_root / "salon_exclusive" / "サロン限定拡散部屋.md")
    },
    {
        "title": "【KBSの実績】Kくんビジネス系スクールの実績まとめ",
        "url": "https://fqw45966.site/kbs/",
        "category": "salon_exclusive",
        "description": "Twitterビジネス系特化スクール(KBS)の実績と詳細",
        "filepath": str(project_root / "salon_exclusive" / "Twitterビジネス系攻略_KBS.md")
    }
]

# サロン限定特典セクションを追加
metadata["salon_exclusive"] = salon_exclusive

# 統計情報を更新
if "content_stats" not in metadata:
    metadata["content_stats"] = {}

metadata["content_stats"]["salon_exclusive_count"] = len(salon_exclusive)
metadata["content_stats"]["total_items"] = (
    len(metadata.get("blog", [])) +
    len(metadata.get("videos", [])) +
    len(salon_exclusive)
)

# 保存
with open(metadata_path, 'w', encoding='utf-8') as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print(f"✅ metadata.json更新完了")
print(f"  - サロン限定特典: {len(salon_exclusive)}件追加")
print(f"  - 総コンテンツ数: {metadata['content_stats']['total_items']}件")
