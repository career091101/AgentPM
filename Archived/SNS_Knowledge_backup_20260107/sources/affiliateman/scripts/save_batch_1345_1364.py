#!/usr/bin/env python3
"""
Batch 1345-1364の画像説明を保存
実際に画像を読み込んで詳細な説明を生成（2023年6月質疑応答のまとめ 20枚）
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1345-1364の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1345,
        "filename": "image_23.png",
        "description": "DM質問への回答。しらっぱさんからのコメント：全部実行、プレゼントハイライト色変更できない点、2980→0円効果について。回答内容と今後の実施予定を記載。"
    },
    {
        "index": 1346,
        "filename": "image_24.png",
        "description": "じゅんさんによる質問と回答のスクリーンショット。復縁系ジャンルでアカウント参入について相談し、ターゲット層・ジャンル選定のアドバイスを受けている。"
    },
    {
        "index": 1347,
        "filename": "image_25.png",
        "description": "KくんからのDM。子連れ出かけアカウント運営相談。売上商品ある程度決めてから参入、フォロワー500人でマネタイズ可能、ハイライトと固定ピン2つ活用のアドバイス。"
    },
    {
        "index": 1348,
        "filename": "image_26.png",
        "description": "しほさんからの質問回答。子連れ出かけアカウント自社商品について。以前アドバイスした子連れ出かけスポットMAP販売、MAPとnote版売却について記載。"
    },
    {
        "index": 1349,
        "filename": "image_27.png",
        "description": "KくんへのDM。カフェマップでマネタイズ事例（フォロワー数による効率性）とコンセプト選定、ノート販売戦略について詳細なアドバイスを記載。"
    },
    {
        "index": 1350,
        "filename": "image_28.png",
        "description": "くまさんからのDM質問。3つのアドバイス：①リポスト投稿のコツ（マン幅、ターゲット選定）②DMで依頼方法③写真使用許可。編集済みの内容で対応。"
    },
    {
        "index": 1351,
        "filename": "image_29.png",
        "description": "KくんのDM回答。リポストのジャンル選択、YouTubeリンク、ゆるコン雑貨・高級ブランドとのリリ戦略について詳細な回答を記載。"
    },
    {
        "index": 1352,
        "filename": "image_30.png",
        "description": "せいさんの質問へのKくん回答。ビジネス（副業×アフィリエイト）アカウント用Auditブルやnote販売、ASP会員登録について戦略を記載。"
    },
    {
        "index": 1353,
        "filename": "image_31.png",
        "description": "KくんのDM。リボストするコツ、サーバーのアフィについて詳細な説明。月100万円到達のプロセスと目標設定について回答。"
    },
    {
        "index": 1354,
        "filename": "image_32.png",
        "description": "せいさんからの複数質問回答。ドメイン/サーバーアフィの戦略、ブログ有料テンプレート、ASP会員登録について詳細な説明を記載。"
    },
    {
        "index": 1355,
        "filename": "image_33.png",
        "description": "公式カラコン通販メイリーのDM。EC運営アドバイス。資産運用・副業・転職アフィの3分野戦略、マッチングアプリ軽視等の複数相談に対して戦略を回答。"
    },
    {
        "index": 1356,
        "filename": "image_34.png",
        "description": "公式カラコン通販メイリーへの回答。資産運用と転職アフィの分け方、副業×SNSの3ヶ月目標とマネタイズ目指し戦略。"
    },
    {
        "index": 1357,
        "filename": "image_35.png",
        "description": "としおさんの初質問回答。ジャンル選択段階のため、4つのジャンル（夫婦コミュニケーション系、上司部下系、notion系、ボイトレ系）の展開と収益化の視点について回答。"
    },
    {
        "index": 1358,
        "filename": "image_36.png",
        "description": "KくんからのDM。グルメアカウント3つの質問に対する回答。①未だアカウント開設がない場合の先行投資、②グルメアカウント作成での写真や外観の準備、③いいね周りの戦略について記載。"
    },
    {
        "index": 1359,
        "filename": "image_37.png",
        "description": "くまさんの複数質問回答。①アカウント開設問題②グルメアカウント作成について③いいね周りについて。食べログなどの文字入れについても触れた詳細な回答。"
    },
    {
        "index": 1360,
        "filename": "image_38.png",
        "description": "リエさんの相談回答。インスタ初心者向けアドバイス。7才兼ぎ兄弟の母親として片付けジャンル検討。アカウント概要、いいね周りについての詳細な戦略を記載。"
    },
    {
        "index": 1361,
        "filename": "image_39.png",
        "description": "KくんへのDM。マネタイズについて。フォロワー単価50-100円でのアフィ収益目標とコンサルの活用方法、リール動画タイミング戦略について詳細に記載。"
    },
    {
        "index": 1362,
        "filename": "image_40.png",
        "description": "ざわさんの相談。グルメ垢でリール再生数2000人くらい目標での3つの質問：①リール再生数、②フィード投稿リール比率、③リール投稿タイミングについての回答。"
    },
    {
        "index": 1363,
        "filename": "image_41.png",
        "description": "KくんのDM。リールでのフォロワー伸びについて。初期段階ではリール重視で2000人到達。ストーリー活用、フィード投稿頻度とのバランスについて詳細に記載。"
    },
    {
        "index": 1364,
        "filename": "image_42.png",
        "description": "キョウさんの質問回答。2つのアカウント運用相談。ChatGPT関連アカウント、Excel効率化アカウント、転職・SBIアフィなどマネタイズターゲット別の戦略を記載。"
    },
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

    print(f"\n✓ Batch 1345-1364 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
