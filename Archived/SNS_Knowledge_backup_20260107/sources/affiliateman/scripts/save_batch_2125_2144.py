#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2125, "filename": "image_17.png", "description": "体重推移グラフと食事内容を並べた比較画像。カレンダーと体重変化をトラッキングし、ダイエット料理の実績写真を並べて効果を可視化している。"},
    {"index": 2126, "filename": "image_18.png", "description": "インスタグラム検索画面でハッシュタグ「#ダイエット」と「#ダイエットメニュー」の投稿数（1433万件・84.5万件）を表示したスクリーンショット。"},
    {"index": 2127, "filename": "image_19.png", "description": "フォロワー獲得戦略を示す図解。類似アカウントからフォロー、ハッシュタグ検索での誘導、類似アカウントのフォロワーへのアプローチという3つの方法を並べている。"},
    {"index": 2128, "filename": "image_20.png", "description": "ラッコツール検索画面を示す。「ダイエット」検索時の関連キーワード候補が日本語で大量に表示されたスクリーンショット。"},
    {"index": 2129, "filename": "image_21.png", "description": "Googleアドワーズキーワードプランナーの操作画面。先行キーワードに関連するキーワード候補が青いボタン形式で表示されている。"},
    {"index": 2130, "filename": "image_22.png", "description": "Googleキーワードプランナーの月間ボリュームデータ表。ダイエット関連キーワードの検索数（ダイエット: 65円〜182円など）を一覧表示している。"},
    {"index": 2131, "filename": "image_23.png", "description": "キーワードプランナーのボリューム降順表示画面。ダイエット関連キーワード30以上が月間50万ボリュームで整理されたスクリーンショット。"},
    {"index": 2132, "filename": "image_24.png", "description": "ダイエットアカウント比較画像。左は「競合多い」アカウント（料理画像混在）、右は「競合少ない」アカウント（フォロワー1万以下）を対比している。"},
    {"index": 2133, "filename": "image_25.png", "description": "インスタグラムアカウント分析画面。リーチ2584件、インプレッション2846件、ハッシュタグ別インプレッション数843件などの詳細統計が表示されている。"},
    {"index": 2134, "filename": "image_26.png", "description": "フォロワー1.5万のリポストに紹介されたアカウントの投稿。プロフィールアクセス10,529、リーチ1,765,118、インタラクション1,832,446の詳細データが表示されている。"},
    {"index": 2135, "filename": "image_27.png", "description": "反響の大小比較画像。左は反響の大きかった投稿（平均エンゲージ: 1.541/4.47%）、右は反響の少なかった投稿（平均エンゲージ: 1.002/2.9%）を日付付きで対比。"},
    {"index": 2136, "filename": "image_28.png", "description": "フォロワー獲得方法の図解（重複）。類似アカウントからのフォロー方法とハッシュタグからのアプローチ、類似ユーザーのカラーコーディネートを3ステップで説明。"},
    {"index": 2137, "filename": "image_29.png", "description": "リポスト紹介時の注意点図解。食べ物投稿のタグ付けとメンション、ストーリーズシェアの具体的な実施方法を示したスクリーンショット。"},
    {"index": 2138, "filename": "image_30.png", "description": "インスタグラムアカウント詳細データの表示画面。フォロワー181,192名、フォロー171件、投稿413件、月間投稿数と平均エンゲージメント率を示すグラフ。"},
    {"index": 2139, "filename": "image_31.png", "description": "メインアカウント戦略図。サブアカから6畳・1LDK・同棟住まいといった複数の切り口でセグメント化した事例を示している。"},
    {"index": 2140, "filename": "image_32.png", "description": "メインアカウント→サブアカ誘導画像。「新規アカ作りました」という告知ストーリーズと具体的なサブアカ別メニュー投稿を並べている。"},
    {"index": 2141, "filename": "image_33.png", "description": "悩み回収と解決提案の流れ図。メインアカウント内で悩みを募集し、サブアカで解決策を提案する誘導メカニズムを説明している。"},
    {"index": 2142, "filename": "image_34.png", "description": "インスタグラムフォロワー獲得フロー図。発見タブ（ハッシュタグ）から流入、ストーリーズ・ライブ・DM返しで既存フォロワーを獲得する3ステップを示す。"},
    {"index": 2143, "filename": "image_35.png", "description": "フォロワー理想のトップ画面解説。ストーリーズの左側配置とタイムラインのトップ表示位置の重要性を示したスマートフォン画面キャプチャ。"},
    {"index": 2144, "filename": "image_36.png", "description": "ダイエットスタンスの質問形式。質問募集型、二択問題、4択クイズ、リアクションという4つのエンゲージメント手法を示す図解。"},
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

    print(f"\n✓ Batch 2125-2144 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
