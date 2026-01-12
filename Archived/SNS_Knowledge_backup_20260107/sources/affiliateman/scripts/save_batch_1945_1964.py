#!/usr/bin/env python3
"""
Batch 1945-1964の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1945-1964の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1945,
        "filename": "image_06.png",
        "description": "Kくんの「SNS攻略」アカウント紹介。Twitter運用に関するDMでの相談内容をスクリーンショット化した投稿で、コンサル感想や有料化の具体的なアドバイスが記載されている。"
    },
    {
        "index": 1946,
        "filename": "image_07.png",
        "description": "Twitter運用の課題相談。インスタとの専門性の違いや基本的な情報発信、初心者向けのコア層への情報提供についての実践的なアドバイスが表示されている。"
    },
    {
        "index": 1947,
        "filename": "image_08.png",
        "description": "月100万円稼ぎ方に関する限定企画の告知。ストーリーネタの悩み解決方法や企画・コンテンツ作成の具体的なステップについてのガイドが示されている。"
    },
    {
        "index": 1948,
        "filename": "image_09.png",
        "description": "フォロー感謝のDM返信テンプレート集。フォロワーからの有益な投稿へのリアクション方法や感謝メッセージの具体例を複数パターン紹介している図解。"
    },
    {
        "index": 1949,
        "filename": "image_10.jpg",
        "description": "Twitter拡散メカニズムの図解。フォロワー1万人のアカウントAが投稿してイイネ/リツイートされ、その投稿がアカウントBに拡散される流れを視覚的に説明している。"
    },
    {
        "index": 1950,
        "filename": "image_11.jpg",
        "description": "Twitter固定ツイート関数UPの実績。投稿バズるのプロセスと「いいね&リツイート」「固定ツイート拡散」「フォロワー増加」の連鎖メカニズムを矢印で説明している。"
    },
    {
        "index": 1951,
        "filename": "image_12.jpg",
        "description": "マッチングアプリ攻略テーマの懇親テキスト。他のコメント欄でも同じ視点が生まれるユーザーファースト的なコンテンツづくりと、オリジナリティを両立させるコツが記載されている。"
    },
    {
        "index": 1952,
        "filename": "image_13.png",
        "description": "投稿バズるプロセスの図解。投稿→バズる→プロフィール遷移→いいね&リツイート→固定ツイート拡散→フォロワー増加という一連の流れを青・赤・オレンジの色分けで説明。"
    },
    {
        "index": 1953,
        "filename": "image_14.png",
        "description": "SEO好きユーザーからのフォロガー情報共有。複数のSEO/ブログ関連のインフルエンサー（ブロガー、YouTuber、Webマーケター）の推薦ツイートが引用されている。"
    },
    {
        "index": 1954,
        "filename": "image_15.png",
        "description": "フォロワー増加10施策のバナー。外部誘導でのフォロワー増加、Instagram・Twitterの成功事例紹介パッケージを示唆するタイトルバナー画像。"
    },
    {
        "index": 1955,
        "filename": "image_16.png",
        "description": "Twitter0→1攻略のフォロワーUP成功事例紹介バナー。初期段階での最強施策をテーマにしたコンテンツを示す青と白のカラーデザイン。"
    },
    {
        "index": 1956,
        "filename": "image_17.png",
        "description": "Twitter売上マネタイズ戦略の紹介。サロン限定動画で「少ないフォロワー月100万稼げる」という具体的な成功事例をKくんとコンサル受講者の対比で表現している。"
    },
    {
        "index": 1957,
        "filename": "image_18.png",
        "description": "Twitterマネタイズ施策の告知。1投稿で20万円売上達成の実績紹介と、売上UPのマネタイズ動線、投稿とマネタイズ誘導の施策説明をまとめたバナー。"
    },
    {
        "index": 1958,
        "filename": "image_19.png",
        "description": "Twitterバズ構文の教材告知。初心者でもバズる仕組みを学べるコンテンツ紹介で、バズるパターン100選を黄色と黒で強調したダークテーマバナー。"
    },
    {
        "index": 1959,
        "filename": "image_20.png",
        "description": "実際のTwitterバズ戦略完全版の販売告知。1日で4000人フォロワー増加という実績を強調した、派手な金色背景デザインの広告バナー。"
    },
    {
        "index": 1960,
        "filename": "image_01.png",
        "description": "Twitterのフォロワー増成功事例の記事カバー。フォロワーUP成功事例とアカウント初期段階の最強施策をテーマにした青と赤のグラデーション背景デザイン。"
    },
    {
        "index": 1961,
        "filename": "image_02.jpg",
        "description": "女性向けビジネス人物イラスト。スーツ姿で赤いネクタイをした女性の横顔を描いたシンプルな線画イラスト。"
    },
    {
        "index": 1962,
        "filename": "image_03.png",
        "description": "Twitter提案資料の図解。DMでの恋愛アカウント提案、請求書作成、3日後のインサイト数値（いいね532、リツイート129等）を段階的に説明した実績紹介図。"
    },
    {
        "index": 1963,
        "filename": "image_04.png",
        "description": "有益投稿からファン化までの流れの図解。大手アカウントのいいね/リツイートから有益投稿、モーメントURL記載によるフォロー率UPの因果関係を矢印で説明。"
    },
    {
        "index": 1964,
        "filename": "image_05.png",
        "description": "モテる男のテーマ選定と運用方法の図解。モテる男会話10選の投稿テーマとインスタ運用方法を並置し、さらにモーメントURLでの下記説明記載という2段階の情報構造を表示。"
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

    print(f"\n✓ Batch 1945-1964 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
