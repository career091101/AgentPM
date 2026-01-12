#!/usr/bin/env python3
"""
Batch 865-884の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 865-884の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 865,
        "filename": "image_41.png",
        "description": "Instagram DM上での品質向上相談。Shunが2万5000人規模のZ世代向けファッション系アカウントを運用。Sheinのアフィリエイト報酬11%で商品単価が安いことに悩むユーザーに対する提案と相談。"
    },
    {
        "index": 866,
        "filename": "image_42.png",
        "description": "旅行系インスタアカウント相談。Erika Suzukiが旅行アカウント（フォロワー342人）と美容アカウント（フォロワー390人）を運営。月間リーチ2200～3000でアフィリエイト導入の課題相談。"
    },
    {
        "index": 867,
        "filename": "image_43.png",
        "description": "旅行アカウント運営の実践的なマネタイズ提案。フォロワー1万人で月5万円~15万円の売上目標設定、PR要件、地域別の活動方針などについてのアドバイス内容。"
    },
    {
        "index": 868,
        "filename": "image_44.png",
        "description": "美容系アカウントのマネタイズ戦略相談。コスメ属人性の課題、LINE誘導戦略、フォロワー200万人でも月100投稿の運用負荷に関する相談内容。"
    },
    {
        "index": 869,
        "filename": "image_45.png",
        "description": "複数アカウント運営者の相談。DM記録の削除とジャンル変更に関する不安。フォロワー減少を報告するユーザーへの回答内容。"
    },
    {
        "index": 870,
        "filename": "image_46.png",
        "description": "KKさんとaiの会話。アカウント作成直し時のジャンル変更戦略、フォロワー増加数減少（200日/30-50）への対策提案。"
    },
    {
        "index": 871,
        "filename": "image_47.png",
        "description": "ダイエット・筋トレジャンル運営者との相談。ストーリーズ閲覧率低下、コンテンツマッチング、自分がいない振り分けジャンルの選定への悩み相談。"
    },
    {
        "index": 872,
        "filename": "image_48.png",
        "description": "複数デバイス運営とビジネスアカウント設定の相談。Twitterイメージとインスタの認識違い、iPhone複数端末でのマルチアカウント運営について。"
    },
    {
        "index": 873,
        "filename": "image_49.png",
        "description": "ダイエット関連アカウント運営相談。リーチ低下、マネタイズ方針の相談。月50万円での売上目標達成の難しさと自動商品売却について。"
    },
    {
        "index": 874,
        "filename": "image_50.png",
        "description": "ダイエットコンサル専門家の相談。日単位で個別DM対応、フォロワー150人でのコンサル単価提案（15000円/回と月5万円）についてのアドバイス。"
    },
    {
        "index": 875,
        "filename": "image_51.png",
        "description": "Twitterビジネスアカウント構築相談。フォロワー100万人超でのインスタ発信課題、ツイッターでの情報発信の効率性についての相談。"
    },
    {
        "index": 876,
        "filename": "image_52.png",
        "description": "食品・ダイエット系アカウント相談（りょう）。フォロワー層30～50代主婦、アフィリエイト実績があるもののマネタイズ施策の確認と改善提案。"
    },
    {
        "index": 877,
        "filename": "image_53.png",
        "description": "インスタライブ・ダイエットコンサル相談。ライブ参加者500円の有料オプション設定、DMでのファン化戦略、コンサル月6万円の展開について。"
    },
    {
        "index": 878,
        "filename": "image_54.png",
        "description": "インスタライブ運営悩み相談（りょう）。ライブ中の料率低下、質問が少ない課題、最初のライブで悩みがあると返信。"
    },
    {
        "index": 879,
        "filename": "image_55.png",
        "description": "短期ダイエットコンサル相談。KKさんからの複数提案：ライブ2回、内容アンケート、ライブ内チャット、500円有料アカウント設定など。"
    },
    {
        "index": 880,
        "filename": "image_56.png",
        "description": "インスタライブ・コンサル運営相談。単発コンサル提案、ZOOMでの対応、月5万円のコンサルについてのアドバイスと業界比較。"
    },
    {
        "index": 881,
        "filename": "image_57.png",
        "description": "Excelジャンルアカウント相談（ゆーし）。Twitterで紹介されたExcelジャンルをInstagram運用開始予定。"
    },
    {
        "index": 882,
        "filename": "image_58.png",
        "description": "複数アカウント相談内容まとめ。当日の内容リスト：属性や顔、アカウント収益化、漫画系アカウント、マネタイズ施策など明記。"
    },
    {
        "index": 883,
        "filename": "image_59.png",
        "description": "複数月109万円の恋愛Noterユーザー相談。3つの新ジャンル検討、複数端末でのiPhone・Mac運用、Twitterインスタのイメージ区分について。"
    },
    {
        "index": 884,
        "filename": "image_60.png",
        "description": "複数アカウント運営者の段階認証とデバイス管理相談。段階認証解除、複数デバイス（2段階認証済み等）でのログイン・アカウント管理に関する相談。"
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

    print(f"\n✓ Batch 865-884 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
