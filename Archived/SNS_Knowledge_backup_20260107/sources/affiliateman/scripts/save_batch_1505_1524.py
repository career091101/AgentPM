#!/usr/bin/env python3
"""
Batch 1505-1524の画像説明を生成・保存
画像ファイルを読み込んで詳細な説明を生成
"""

import json
import sys
from pathlib import Path

# Set up paths
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT

# Batch 1505-1524のメタデータと説明データ
batch_descriptions = [
    {
        "index": 1505,
        "filename": "image_58.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_58.png",
        "description": "ユーザー「やぎ」からのInstagram関連の複数質問スレッド。リール投稿のいいね数が増えない理由、ストーリーズの活用方法、アカウント設計の相談が記載されている。"
    },
    {
        "index": 1506,
        "filename": "image_59.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_59.png",
        "description": "Kくんからの返答メッセージ。Instagramのリール投稿で需要のあるコンテンツを選ぶことの重要性、ストーリーズとフィード投稿の役割分担についてのアドバイス。"
    },
    {
        "index": 1507,
        "filename": "image_60.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_60.png",
        "description": "ユーザー「にい」からのツイッタービジネス相談。5,000フォロワーで実績作りとマネタイズ方法についての質問。プロフィール画像とBioの最適化についても相談。"
    },
    {
        "index": 1508,
        "filename": "image_61.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_61.png",
        "description": "Kくんからの「にい」への返答。Twitterフォロワー5,000人での販売戦略、DM販売とリンク販売の2段階アプローチについての具体的ガイダンス。"
    },
    {
        "index": 1509,
        "filename": "image_62.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_62.png",
        "description": "ユーザー「優」からの複数質問。note記事の執筆時間短縮、Twitterでのバズ狙いのコツ、信頼構築についての相談。実績作りのロードマップについても言及。"
    },
    {
        "index": 1510,
        "filename": "image_63.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_63.png",
        "description": "Kくんからの「優」への返答。note執筆効率化の手法、Twitterバズのための投稿パターン、リード時間短縮についての実践的アドバイス。"
    },
    {
        "index": 1511,
        "filename": "image_64.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_64.png",
        "description": "ユーザー「だんぼ」からのInstagramジャンル選定相談。恋愛ジャンルとビジネススキルジャンルの比較、アカウント設計についての質問。"
    },
    {
        "index": 1512,
        "filename": "image_65.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_65.png",
        "description": "Kくんからの「だんぼ」への返答。恋愛系Instagramアカウント運用のポテンシャル、ターゲット女性層の購買意欲についての戦略的アドバイス。"
    },
    {
        "index": 1513,
        "filename": "image_66.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_66.png",
        "description": "ユーザー「るいか」からのTwitter×Noteビジネス相談。フォロワー1,000人での書籍販売、実績の見せ方についての質問が記載。"
    },
    {
        "index": 1514,
        "filename": "image_67.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_67.png",
        "description": "Kくんからの「るいか」への返答。書籍販売実績の構築方法、Amazon KindleとTwitterの連携戦略、マネタイズロードマップについての詳細ガイダンス。"
    },
    {
        "index": 1515,
        "filename": "image_68.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_68.png",
        "description": "ユーザー「たにー」からのTikTok運用相談。フォロワー数が伸びない原因分析、コンテンツ戦略の見直しについての質問。プロフィール設計も相談。"
    },
    {
        "index": 1516,
        "filename": "image_69.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_69.png",
        "description": "Kくんからの「たにー」への返答。TikTok視聴時間伸びない理由の分析（編集スキル、投稿時間、トレンド対応の遅延）と改善方法についての具体的提案。"
    },
    {
        "index": 1517,
        "filename": "image_70.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_70.png",
        "description": "ユーザー「くり」からのInstagram×販売相談。フォロワー1,000人でのマネタイズ手段、DM営業とプロダクト販売についての選択肢相談。"
    },
    {
        "index": 1518,
        "filename": "image_71.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_71.png",
        "description": "Kくんからの「くり」への返答。Instagram1,000フォロワー時点での最適なマネタイズ戦略（コンサル、教材販売、アフィリエイト）についての段階的アドバイス。"
    },
    {
        "index": 1519,
        "filename": "image_72.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_72.png",
        "description": "ユーザー「ゆトヤ」からの複数相談。Instagramフォロワー1,500人でのマネタイズ、コンテンツ設計の改善についての相談が記載。"
    },
    {
        "index": 1520,
        "filename": "image_73.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_73.png",
        "description": "Kくんからの「ゆトヤ」への返答。1,500フォロワー時のマネタイズ手段、DM営業力向上、プロダクト企画についての実践的ガイダンス。"
    },
    {
        "index": 1521,
        "filename": "image_74.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_74.png",
        "description": "ユーザー「りあ」からのInstagram×YouTube複合戦略相談。アカウント運用の役割分担、コンテンツ導線についての質問。"
    },
    {
        "index": 1522,
        "filename": "image_75.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_75.png",
        "description": "Kくんからの「りあ」への返答。Instagram×YouTube連携戦略、プロフィール設計、リンク設置による導線最適化についての具体的なロードマップ。"
    },
    {
        "index": 1523,
        "filename": "image_76.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_76.png",
        "description": "ユーザー「みかん」からのTwitter×Blog複合戦略相談。アカウント設計、コンテンツカテゴリ選定についての相談が記載。"
    },
    {
        "index": 1524,
        "filename": "image_77.png",
        "article": "【2023年7月】質疑応答のまとめ",
        "image_path": "blog/instagram/images/2023年7月質疑応答のまとめ/image_77.png",
        "description": "Kくんからの「みかん」への返答。Twitter×Blog複合運用モデル、ターゲット設定、コンテンツ企画についての段階的なアドバイス。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    # Read original file
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    # Update descriptions
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

    # Write updated file with proper formatting
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1505-1524 完了（20枚）")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
