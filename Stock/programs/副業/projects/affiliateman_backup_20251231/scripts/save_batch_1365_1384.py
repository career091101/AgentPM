#!/usr/bin/env python3
"""
Batch 1365-1384の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
記事: 【2023年6月】質疑応答のまとめ (20枚)
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1365-1384の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1365,
        "filename": "image_43.png",
        "description": "インスタグラムのDMでのマネタイズ相談。ユーザーKくんがマネタイズ方法について質問し、キヨさんが具体的な施策（100円ほどのコース販売、サブスクなど）について説明している。"
    },
    {
        "index": 1366,
        "filename": "image_44.png",
        "description": "よるとユーザーが発信ジャンルについて質問。健康・ダイエット系アフィリエイトのマネタイズ方法を、アフィリエイトとnote両軸で検討する相談内容。"
    },
    {
        "index": 1367,
        "filename": "image_45.png",
        "description": "キヨさんの詳しい回答。ダイエット商品のアフィリエイトについて、競争が激しいため独自の視点が重要であることと、noteでの高額商品販売について述べている。"
    },
    {
        "index": 1368,
        "filename": "image_46.png",
        "description": "転職くんのリール投稿についての相談。リール投稿で強いキャラクターを活かしたフィード投稿と、リール攻略・TikTok攻略について専門的なアドバイスを求めている。"
    },
    {
        "index": 1369,
        "filename": "image_47.png",
        "description": "ふっきーユーザーの初めての質問。占いジャンルで30～60代の女性をターゲットにしており、フォロワー増加とマネタイズについて相談している。"
    },
    {
        "index": 1370,
        "filename": "image_48.png",
        "description": "キヨさんの長文回答。フォロワー増加策としてコンテンツ内容の改善、マネタイズ目的での施策の順序、note活用などについて複数の提案をしている。"
    },
    {
        "index": 1371,
        "filename": "image_49.png",
        "description": "キヨさんによるYouTube有益動画教材リストの共有。過去の有益動画をプレイリスト化して紹介し、教材活用の効率化を図っている。"
    },
    {
        "index": 1372,
        "filename": "image_50.png",
        "description": "ひじりユーザーの複数の質問。メンズ美容・モテ垢、転職アカウントについて、ジャンル別の施策やマネタイズの工夫について詳しく相談している。"
    },
    {
        "index": 1373,
        "filename": "image_51.png",
        "description": "キヨさんの詳しい回答。転職ジャンルのリール活用、マネタイズ方法（メール無料講座→コンサル）、TikTok連携について実践的なアドバイスをしている。"
    },
    {
        "index": 1374,
        "filename": "image_52.png",
        "description": "日下部宇宙ユーザーの飲食店紹介に関する質問。7選フィード投稿とリール攻略、フォロワー許可取得などについて、キヨさんがグルメアフィリについて説明している。"
    },
    {
        "index": 1375,
        "filename": "image_53.png",
        "description": "キヨさんの投稿写真のリポスト許可についての補足説明。店舗との許可取得パターン、特にBluetooth接続での許可取得について詳しく述べている。"
    },
    {
        "index": 1376,
        "filename": "image_54.png",
        "description": "いくみユーザーの初めての相談。女性向け恋愛ジャンルで、複数の女性ターゲット層（独立女性、意見を言える女性など）の設定とリール・フィード戦略について質問。"
    },
    {
        "index": 1377,
        "filename": "image_55.png",
        "description": "キヨさんの詳細な回答。恋愛ジャンルのリール活用、フォロワーペルソナの重要性、TikTok連携によるメリットについて複数の視点から説明している。"
    },
    {
        "index": 1378,
        "filename": "image_56.png",
        "description": "ジャック恋愛高単価セールスユーザーの質問。恋愛ジャンル、リール構成、フォロワー増加策、占いジャンルとの組み合わせについて相談している。"
    },
    {
        "index": 1379,
        "filename": "image_57.png",
        "description": "いくみユーザーの追加質問とキヨさんの回答。TikTok連携、フィード10スライドの構成、アカウント設計とコンテンツ最適化について実践的なアドバイスをしている。"
    },
    {
        "index": 1380,
        "filename": "image_58.png",
        "description": "キヨさんの補足説明。フィード10スライド構成の具体例、リール・フィード・TikTok全体での戦略、アカウント設計の重要性について述べている。"
    },
    {
        "index": 1381,
        "filename": "image_59.png",
        "description": "mizuユーザーの新規質問。言語コーチとしてインスタ・Twitterを活用し、教材販売とnote活用についてキヨさんに相談している。"
    },
    {
        "index": 1382,
        "filename": "image_60.png",
        "description": "キヨさんの詳細な回答。言語教材の市場分析、ターゲット設定（韓国語など）、教材販売戦略とマネタイズについて複数の提案をしている。"
    },
    {
        "index": 1383,
        "filename": "image_61.png",
        "description": "しゅうユーザーの新規相談。ビジネスマナー記事を発信し、転職エージェント・キャリアアップ向けのアフィリエイト検討について質問している。"
    },
    {
        "index": 1384,
        "filename": "image_62.png",
        "description": "しゅうユーザーの追加質問とキヨさんの回答。投稿内容の転職関連性、プロフィール最適化、マネタイズ順序などについて実践的なアドバイスをしている。"
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

    print(f"\n✓ Batch 1365-1384 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
