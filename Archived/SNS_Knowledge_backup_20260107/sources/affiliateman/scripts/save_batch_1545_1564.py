#!/usr/bin/env python3
"""
Batch 1545-1564の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1545-1564の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1545,
        "filename": "image_260.png",
        "description": "インスタグラムのコンテンツ戦略についての質問。アカウント運用のジャンル選定から発信軸までの基本構成、フォロワー獲得のための投稿戦略についての相談が記載されている。"
    },
    {
        "index": 1546,
        "filename": "image_261.png",
        "description": "SNS初心者向けの発信軸設定とコンテンツ企画についてのアドバイス。「ビジネス」「ライフスタイル」「マインドセット」などのテーマ構成と、投稿の質を高める工夫についての説明。"
    },
    {
        "index": 1547,
        "filename": "image_262.png",
        "description": "ユーザーからの複数質問。Instagramのストーリーズとフィード投稿の使い分け、リール投稿のコンテンツ構成、キャプション作成についての相談が含まれている。"
    },
    {
        "index": 1548,
        "filename": "image_263.png",
        "description": "キャプション作成の具体的な方法論。ターゲットユーザーへの訴求方法、数字を使った表現、セール要素の組み込みについてのガイダンスが記載されている。"
    },
    {
        "index": 1549,
        "filename": "image_264.png",
        "description": "Tiktokでのコンテンツ展開戦略についての返答。Instagramで成功したコンテンツをTiktokに転用する方法、プラットフォーム別の最適化についての説明。"
    },
    {
        "index": 1550,
        "filename": "image_265.png",
        "description": "アフィリエイト案件選定と紹介文の作成についてのアドバイス。高単価案件の選び方、リスティング広告的な思考法、ターゲットの絞り込みについての具体的な手法。"
    },
    {
        "index": 1551,
        "filename": "image_266.png",
        "description": "ユーザーの投稿パフォーマンス分析。インプレッション数、保存数、シェア数などのメトリクスと、改善施策の優先順位付けについてのコンサルテーション。"
    },
    {
        "index": 1552,
        "filename": "image_267.png",
        "description": "コンテンツの質と量のバランスについての議論。投稿頻度の最適化、ストーリーズとフィード投稿の配分、エンゲージメント率の改善方法についての提案。"
    },
    {
        "index": 1553,
        "filename": "image_268.png",
        "description": "フォロワー増加ための戦略。ハッシュタグの活用方法、コメント対策、フォローバックの効率化についてのアドバイスが含まれている。"
    },
    {
        "index": 1554,
        "filename": "image_269.png",
        "description": "プロフィール最適化についてのコンサル。プロフィール文の作成、リンク設定、プロフィール画像の選択についての具体的なガイドラインが記載されている。"
    },
    {
        "index": 1555,
        "filename": "image_270.png",
        "description": "ユーザーからのメッセージ返信機能に関する相談。DM自動化、テンプレート作成、顧客サービスの効率化についての提案が記載されている。"
    },
    {
        "index": 1556,
        "filename": "image_271.png",
        "description": "アカウント分析ツールの使用方法についての説明。インサイト機能の見方、リーチ分析、フォロワーの属性データの活用についてのガイダンス。"
    },
    {
        "index": 1557,
        "filename": "image_272.png",
        "description": "マネタイズ方法の詳細説明。インスタグラムアフィリエイト、オリジナル商品販売、コンサルティング、スクール販売などの複数の収益化戦略。"
    },
    {
        "index": 1558,
        "filename": "image_273.png",
        "description": "ユーザーの売上目標達成のためのロードマップ。3ヶ月での月5万円達成、6ヶ月での月20万円達成に向けた具体的なマイルストーン。"
    },
    {
        "index": 1559,
        "filename": "image_274.png",
        "description": "SNS運用の初期段階での注意点。継続性の重要性、失敗の最小化、メンタル管理についてのアドバイスが記載されている。"
    },
    {
        "index": 1560,
        "filename": "image_275.png",
        "description": "ブランド構築についてのコンサル。独自性の演出、ポジショニング戦略、競合との差別化についての理論とアドバイス。"
    },
    {
        "index": 1561,
        "filename": "image_276.png",
        "description": "複数のユーザーからの質問が集約されたスクリーンショット。異なるジャンルのアカウント運用、成長段階による施策の変更についての複数の相談例。"
    },
    {
        "index": 1562,
        "filename": "image_277.png",
        "description": "インスタグラムビジネスアカウントの設定方法と機能説明。プロアカウント化のメリット、広告配信機能、分析ツールについての詳細ガイド。"
    },
    {
        "index": 1563,
        "filename": "image_278.png",
        "description": "コンテンツカレンダーの作成方法。月間投稿計画、テーマ別の配分、トレンド対応についての実務的なテンプレートと説明。"
    },
    {
        "index": 1564,
        "filename": "image_279.png",
        "description": "クライアント獲得戦略の詳細解説。営業プロセス、提案資料作成、契約金額の決定までのエンドツーエンドのフローについての実例とアドバイス。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {inventory[idx]['filename']}: 説明更新")

    total = len(inventory)

    # 自動生成でない詳細説明のカウント
    def is_auto_generated(desc):
        if not desc:
            return True
        auto_patterns = [
            "運用に関する説明画像または投稿サムネイル。記事",
            "運用に関する説明画像または図解。",
            "記事のバナー画像またはメインビジュアル。",
            "関連コンテンツ。"
        ]
        for pattern in auto_patterns:
            if pattern in desc:
                return True
        return False

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1545-1564 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
