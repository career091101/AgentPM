#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {
        "index": 1985,
        "filename": "image_14.jpg",
        "description": "ビジネス向けプロフィールを示す黒スーツ姿の男性イラスト。赤いネクタイが特徴で、Twitter運用関連のマーケティング教材の表紙として使用されている。"
    },
    {
        "index": 1986,
        "filename": "image_15.png",
        "description": "『1日で4000人増加！Twitterのバズ戦略完全版』と記載された広告バナー。黄と赤の配色で、フォロワー増加の実績を強調するプロモーション画像。"
    },
    {
        "index": 1987,
        "filename": "image_16.png",
        "description": "「Twitterのマネタイズ戦略 稼げるおすすめジャンル」と「マネタイズ施策も共有」を記載したヘッダー部分。青と白の配色で段階的なコンテンツ構成を示唆。"
    },
    {
        "index": 1988,
        "filename": "image_17.png",
        "description": "「Twitter マネタイズ施策 1投稿で20万円売上達成」と黄色い注釈で『売上UPのマネタイズ動線』を紹介するスクリーンショット。実績ベースの具体的な成功事例を提示。"
    },
    {
        "index": 1989,
        "filename": "image_18.png",
        "description": "「商品を売りまくるマネタイズ戦略～Twitterで稼ぐ戦略～」と紫色背景で『サロン限定動画 少ないフォロワー月100万稼げる』というツールの紹介セクション。"
    },
    {
        "index": 1990,
        "filename": "image_19.png",
        "description": "『SNSのマネタイズ事例 DMで商品を売る施策例 僕の成功事例紹介』という黄色いバナー。メール📧 アイコンが特徴で、ダイレクトメッセージを活用した販売方法を説明。"
    },
    {
        "index": 1991,
        "filename": "image_20.png",
        "description": "『商品が売れる投稿！！ 超売れるツイートの型 10選 note/アフィ/コンサルが売れる』という青いテンプレート型画像。複数の販売チャネルに対応したツイート構成を紹介。"
    },
    {
        "index": 1992,
        "filename": "image_01.png",
        "description": "「Twitterのマネタイズ戦略 稼げるおすすめジャンル マネタイズ施策も共有」と記載された青いヘッダーバナー。ロケットアイコンと男性キャラが配置されたメインビジュアル。"
    },
    {
        "index": 1993,
        "filename": "image_02.jpg",
        "description": "男性向け恋愛系のTwitterアカウント事例スクリーンショット。『非モテのままモテる Dogma』『恋愛の教科書 Love textbook』『ナンパ遊び』『彼氏作り/恋愛論』の複数ジャンルが表示。"
    },
    {
        "index": 1994,
        "filename": "image_03.png",
        "description": "女性向けの『恋愛系』Twitterアカウント集合スクリーンショット。『get back』『恋愛大学』『さかなさん』など複数のアカウントが『復縁』『彼氏作り』『婚活界限』タイトル付きで紹介。"
    },
    {
        "index": 1995,
        "filename": "image_04.png",
        "description": "『エロや性癖』ジャンルのTwitterアカウント事例。アダルト関連コンテンツ『セクテク』『ちょいエロ系』『エロ』などのカテゴリーに分類された複数アカウントのプロフィール画像と説明。"
    },
    {
        "index": 1996,
        "filename": "image_05.png",
        "description": "『ダイエット』ジャンルのTwitterアカウント事例。『-13kg』『-10kg達成』など具体的な減量成功例を示すプロフィール画像。『トレーニング/ダイエット』セクションでビジュアル変化を記録。"
    },
    {
        "index": 1997,
        "filename": "image_06.png",
        "description": "『美容関連』ジャンルのTwitterアカウント複合スクリーンショット。『美容』『整形』セクションで美容系インフルエンサーとコンサル系アカウントのプロフィール情報が一覧表示。"
    },
    {
        "index": 1998,
        "filename": "image_07.png",
        "description": "『就職活動』ジャンルのTwitterアカウント事例。『11月3日口入場ランキング1-50位』という採用試験関連の情報と『就活生に知られたくない！』という求人情報の発信アカウントを紹介。"
    },
    {
        "index": 1999,
        "filename": "image_08.png",
        "description": "『キャリア』『ビジネス系』ジャンルのTwitterアカウント統合表示。転職関連『転職 仕事術 キャリアUP』と複数のビジネス系インフルエンサー『TikTok学園』『YouTubeマーケター』などを紹介。"
    },
    {
        "index": 2000,
        "filename": "image_09.png",
        "description": "『旅行』『旅行やデートスポット』ジャンルのTwitterアカウント事例。『おさる旅 HITOTOKI』『コスパ旅』などの旅行関連アカウント複数と『デートの旅行スポ』『募囲気あり店紹介』タイプを記載。"
    },
    {
        "index": 2001,
        "filename": "image_10.png",
        "description": "『男性の外見改善』ジャンルのTwitterアカウント統合表示。『ファッション』『外見改善』『美容全般』セクションで、複数の外見改善系アカウントとそのフォロワー数が一覧化されている。"
    },
    {
        "index": 2002,
        "filename": "image_11.png",
        "description": "Twitterのマネタイズ戦略に関する総合ガイド資料。『ジャンル別マネタイズ方法』『成功する投稿パターン』『フォロワー増加戦略』など複数のセクションで具体的なノウハウが整理。"
    },
    {
        "index": 2003,
        "filename": "image_12.png",
        "description": "Twitterジャンル別稼ぎ方ガイドの詳細解説ページ。『恋愛系 稼げる理由』『ビジネス系の戦略』『アダルト系の注意点』など分野別に具体的なマネタイズ手法を記載。"
    },
    {
        "index": 2004,
        "filename": "image_13.png",
        "description": "Twitterアカウント運用のジャンル選定から実装までの全体ロードマップ画像。『初期設定』『コンテンツ企画』『投稿戦略』『マネタイズ実装』のプロセスが段階的に図解されている。"
    },
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

    print(f"\n✓ Batch 1985-2004 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
