#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2145, "filename": "image_37.png", "description": "ダイエット企画のフォロワー向け質問回答ガイド。停滞期の過ごし方、効果期の計画、1-3ヶ月別の変化率を示す図解。"},
    {"index": 2146, "filename": "image_38.png", "description": "ダイエット成功事例の悩み回収と解決パターン。フォロワーの失敗談を集計し、具体的な改善策を提示する構成図。"},
    {"index": 2147, "filename": "image_39.png", "description": "ダイエットの悩みと解決策のマッピング図解。フォロワーの共通課題（YES/NO 94%/6%）から対策を導く仕組み。"},
    {"index": 2148, "filename": "image_40.png", "description": "食品比較クイズ形式の投稿例。ぐみ vs ミストのカロリー比較で栄養教育する二択形式。"},
    {"index": 2149, "filename": "image_41.png", "description": "プロテインバークイズの質問と解説パート。タンパク質量とカロリーの実値解説で学習価値を提供。"},
    {"index": 2150, "filename": "image_42.png", "description": "ダイエット方法の二択アンケート投稿。フォロワーの選択分布（76%/24%）から需要を探る図解。"},
    {"index": 2151, "filename": "image_43.png", "description": "カロリー消費量クイズの質問と解説。体温上昇による消費カロリー（30%アップ）の科学的説明図。"},
    {"index": 2152, "filename": "image_44.png", "description": "ダイエット方法の複合比較図。糖質制限・脂質制限・カロリー制限の3軸で利用者の選択傾向を示す。"},
    {"index": 2153, "filename": "image_45.png", "description": "フォロワーへのダイエット方法アンケート。効果があった自己流ダイエットをテキスト入力で収集する仕組み。"},
    {"index": 2154, "filename": "image_46.png", "description": "ダイエット成功者の詳細インタビュー結果。14時間断食、16時間断食によるリバウンド体験の集計グラフ。"},
    {"index": 2155, "filename": "image_47.png", "description": "フォロワーの知りたい情報収集とアンケート質問群。テーマの回収からストーリーでの質問提示までの流れを図解。"},
    {"index": 2156, "filename": "image_48.png", "description": "ダイエット情報の需要調査結果。フォロワーが知りたい内容（96%）とあまり興味のない内容（4%）の実態。"},
    {"index": 2157, "filename": "image_49.png", "description": "リバウンド体験者のコメント募集投稿。複数キロの減量方法と体験談をテキストで回答してもらう募集形式。"},
    {"index": 2158, "filename": "image_50.png", "description": "ダイエットゴール達成時のコメント募集。リバウンド経験の有無と対策をフォロワーから集める調査投稿。"},
    {"index": 2159, "filename": "image_51.png", "description": "リバウンド経験別ダイエット方法の提案図。アイコンで5kg/3kg/1kg/5kg以上の体重変化に対応する方法を表示。"},
    {"index": 2160, "filename": "image_52.png", "description": "リバウンド診断と食物リスト。5キロ以上のリバウンド経験者向けに12種類の食べ物と消費カロリー対策を提示。"},
    {"index": 2161, "filename": "image_53.png", "description": "長文ストーリー形式のダイエット体験談。4つのターニングポイントで視聴者の共感を引き出す叙述形構成。"},
    {"index": 2162, "filename": "image_54.png", "description": "ダイエット成功事例とIGTV誘導の例。5ヶ月で10kg減による金森式ケトジェニック体験とプラットフォーム連携。"},
    {"index": 2163, "filename": "image_55.png", "description": "Instagramホーム画面のストーリーズ位置図。トップ左のストーリーズ最初表示位置とタイムライン内容の解説。"},
    {"index": 2164, "filename": "image_56.png", "description": "ダイエット悩み回収と解決の全体図。フォロワーの失敗パターン、共通課題を集計してコンテンツ化する仕組み。"},
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

    print(f"\n✓ Batch 2145-2164 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
