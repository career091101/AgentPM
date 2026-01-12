#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1765, "filename": "image_82.png", "description": "サロン入会者「しゅん」からの質問と、Kくん（K社長）による回答スクリーンショット。コンビニ食材の編集方法やサムネイル設計、アカウントプロフィール最適化についての具体的なアドバイス内容。"},
    {"index": 1766, "filename": "image_83.png", "description": "サロン入会者「まひろ」からの3点質問スクリーンショット。ターゲット層の設定方法、発信マインドの重要性、Twitterとマネタイズのコツについてのやり取り。"},
    {"index": 1767, "filename": "image_84.png", "description": "Twitterでの恋愛アカウント運用戦略についてのスクリーンショット。『動画がバズる』『LINEに誘導』『無料コンサル→有料コンサル』の段階的マネタイズ方法とnoteやTwitter連携の実例説明。"},
    {"index": 1768, "filename": "image_85.png", "description": "Kくんが恋愛アカウント運用で5年以上売上を実現した経験とマネタイズ戦略についての説明スクリーンショット。下積みの重要性とLINE誘導、無料動画マッチングアプリ活用法など。"},
    {"index": 1769, "filename": "image_86.png", "description": "YouTubeコンテンツ販売について質問するユーザーとKくんの回答スクリーンショット。Tipsプラットフォームの特徴、ビジネス系アフィリエイト戦略、高単価商品の販売方法についてのやり取り。"},
    {"index": 1770, "filename": "image_87.png", "description": "TK農人性なしYouTubeユーザーからの『AppsとStripe決済によるアフィリエイト』についての質問と、Kくんの回答スクリーンショット。プラットフォーム選定とTips販売戦略について。"},
    {"index": 1771, "filename": "image_88.png", "description": "新人サロン入会者『けの』からの1点質問スクリーンショット。1つのアカウントで複数人性を出す方法と、Kくんによるアカウント戦略の具体的な説明コンテンツ。"},
    {"index": 1772, "filename": "image_89.png", "description": "各アカウントの基本型（教育・理想・独折・最恵・投資）と、ホテル写真撮影やマッチングアプリ攻略についての質問と回答スクリーンショット。ケン新人からのアドバイス受け取り画面。"},
    {"index": 1773, "filename": "image_90.png", "description": "ハッピーバイヤーユーザーからの海外ブランド品販売ノウハウについての2点質問と、Kくんの具体的な販売戦略回答スクリーンショット。50万円クラスの商品販売方法と事前告知テクニック。"},
    {"index": 1774, "filename": "image_91.png", "description": "ハッピーバイヤーユーザーからの『海外ブランド品の販売ノウハウ』についての実践的な質問スクリーンショット。1万〜2万円の商品販売とLINEサンプ提供戦略についての詳細な説明。"},
    {"index": 1775, "filename": "image_92.png", "description": "TK農人性なしYouTubeユーザーからのアダルト情報教材販売についての質問と、Kくんの『風俗関連素材の販売戦略』回答スクリーンショット。発信内容と販売方法についてのアドバイス。"},
    {"index": 1776, "filename": "image_93.png", "description": "シトラスユーザーからの『看護師転職アフィリエイト』についての相談と、Kくんの具体的なSNS戦略回答スクリーンショット。複数プラットフォーム運用とマネタイズ方法の説明。"},
    {"index": 1777, "filename": "image_94.png", "description": "まさき『リクルートtoフリーランスのリアル』ユーザーからの質問と、Kくんのコンサル費用やアカウント構築戦略についての詳細な回答スクリーンショット。"},
    {"index": 1778, "filename": "image_95.png", "description": "Kくんのコンサル生「シマアジ」からのビジネス系アカウント運用について、複数プラットフォーム展開と月商50万円達成戦略についての相談スクリーンショット。"},
    {"index": 1779, "filename": "image_96.png", "description": "M-K『キセキ』ユーザーからの『フォロワー100万人達成の無料企画活用法』についての質問と、KくんによるTwitter無料企画とティップス販売の連携戦略説明スクリーンショット。"},
    {"index": 1780, "filename": "image_97.png", "description": "シマアジユーザーからの『初期資金の配分方法とアカウント分け戦略』についての質問と、Kくんの段階的資金配分、投資管理、マインド管理についての詳細な回答スクリーンショット。"},
    {"index": 1781, "filename": "image_98.png", "description": "Kくんからシマアジへの『SNS攻略サロン限定』YouTubeコンテンツ紹介スクリーンショット。『SNSで稼ぐための最強の教え完全公開』というサムネイル画像付き動画の推奨。"},
    {"index": 1782, "filename": "image_99.png", "description": "まなぶんユーザーからの『Twitter子育て系アカウント設計』についての質問と、Kくんによるプログラミング・タブレット教育などのジャンル提案と運用方法の回答スクリーンショット。"},
    {"index": 1783, "filename": "image_100.png", "description": "ケンシンユーザーからの『ビジネス系アカウント運用の現状』と『10日で経ちた進捗状況』についての相談スクリーンショット。アカウント選定からマネタイズまでの具体的な構築方法。"},
    {"index": 1784, "filename": "image_101.png", "description": "Kくんからケンシンへの『SNS攻略ラジオ #13』についての回答スクリーンショット。Voicy音声プラットフォームの『さとちんさんとのSNS攻略対談』がアップロードされたことの案内。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
    ]
    return any(p in desc for p in patterns)

def update_inventory_with_descriptions(batch_descriptions):
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {desc['filename']}: 説明更新")

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))
    total = len(inventory)
    remaining = total - completed
    percentage = (completed / total) * 100

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1765-1784 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
