#!/usr/bin/env python3
"""
Batch 1625-1644の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年8月】質疑応答まとめ記事の20枚
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1625-1644の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1625,
        "filename": "image_75.png",
        "description": "インスタグラム運用に関するユーザーからの質問。アカウント開設初期段階でのフォロワー獲得方法、初期投稿戦略、プロフィール設定についての相談が記載されている。"
    },
    {
        "index": 1626,
        "filename": "image_76.png",
        "description": "SNS初心者向けのアカウント設定ガイダンス。プロフィール文の最適化、プロフィール画像選択、初期投稿の方針についての具体的なアドバイスと実例。"
    },
    {
        "index": 1627,
        "filename": "image_77.png",
        "description": "ユーザーからの複数の運用に関する質問。コンテンツジャンルの選定、発信軸の決め方、ターゲット設定についての相談が含まれている。"
    },
    {
        "index": 1628,
        "filename": "image_78.png",
        "description": "ジャンル選定と発信軸の構築方法についての詳細解説。自分の専門性を活かしたニッチ選定、競合分析、ターゲットペルソナの設定についてのガイドライン。"
    },
    {
        "index": 1629,
        "filename": "image_79.png",
        "description": "コンテンツ企画と投稿戦略についてのユーザー相談。どのようなネタを投稿すべきか、投稿頻度、リール投稿の活用方法についての複数の質問。"
    },
    {
        "index": 1630,
        "filename": "image_80.png",
        "description": "SNSコンテンツの企画方法論。トレンド活用、ユーザーの悩み解決型コンテンツ、視聴者参加型企画についての具体的な事例とテンプレート。"
    },
    {
        "index": 1631,
        "filename": "image_81.png",
        "description": "ユーザーからの投稿効果測定に関する質問。インプレッション数、リーチ、エンゲージメント率の見方、分析の重要性についての相談が記載されている。"
    },
    {
        "index": 1632,
        "filename": "image_82.png",
        "description": "アカウント分析とメトリクス解釈についてのコンサルテーション。重要な指標の説明、パフォーマンス改善のためのPDCA、データドリブンな運用方法。"
    },
    {
        "index": 1633,
        "filename": "image_83.png",
        "description": "フォロワー増加に関するユーザーからの質問。ハッシュタグ戦略、リール投稿の優先度、コメント対策についての複数の相談が含まれている。"
    },
    {
        "index": 1634,
        "filename": "image_84.png",
        "description": "ハッシュタグ戦略の実装方法。ターゲット層に到達するハッシュタグ選定、大規模タグと小規模タグのバランス、投稿タイミング最適化についての詳細ガイド。"
    },
    {
        "index": 1635,
        "filename": "image_85.png",
        "description": "ユーザーからのマネタイズに関する質問。いつからアフィリエイトを始めるべきか、案件選定、提案文の書き方についての相談が記載されている。"
    },
    {
        "index": 1636,
        "filename": "image_86.png",
        "description": "アフィリエイト案件選定と提案文作成についてのコンサルテーション。高単価案件と高成約率案件のバランス、ターゲットユーザーへの訴求方法、実際の成功事例。"
    },
    {
        "index": 1637,
        "filename": "image_87.png",
        "description": "ユーザーからのDMやコメント対応に関する質問。顧客対応の効率化、テンプレート化、フォロワー獲得につながるコミュニケーション戦略についての相談。"
    },
    {
        "index": 1638,
        "filename": "image_88.png",
        "description": "コミュニティ運営とエンゲージメント向上についてのアドバイス。DM自動化ツール、テンプレート作成による効率化、顧客満足度向上の方法についての具体的な施策。"
    },
    {
        "index": 1639,
        "filename": "image_89.png",
        "description": "ユーザーからの長期的な運用方針に関する質問。成長段階による施策変更、マネタイズのタイミング、スケール拡大についての相談が含まれている。"
    },
    {
        "index": 1640,
        "filename": "image_90.png",
        "description": "特殊な画像フォーマットまたは小サイズのメディアファイル。記事の補助要素またはスペーサーとして機能している可能性が高い。"
    },
    {
        "index": 1641,
        "filename": "image_91.png",
        "description": "アカウント成長の各段階における戦略ロードマップ。初期段階から月1万円、月10万円、月100万円達成に向けた具体的なマイルストーン・施策変更。"
    },
    {
        "index": 1642,
        "filename": "image_92.png",
        "description": "ユーザーからのブランド構築に関する質問。独自性の演出方法、他のアカウントとの差別化、長期的なブランド価値構築についての複数の相談。"
    },
    {
        "index": 1643,
        "filename": "image_93.png",
        "description": "ブランドポジショニングと差別化戦略についてのコンサルテーション。市場内での立ち位置、ユニークバリュープロポジション、競合分析と差別化ポイントの特定方法。"
    },
    {
        "index": 1644,
        "filename": "image_94.png",
        "description": "SNS運用における複数のユーザーからの集約型相談。異なるジャンルのアカウント実例、共通成功要因、失敗パターン回避についての総合的なアドバイス。"
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

    print(f"\n✓ Batch 1625-1644 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
