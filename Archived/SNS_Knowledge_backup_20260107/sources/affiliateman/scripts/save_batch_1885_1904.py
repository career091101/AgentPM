#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1885, "filename": "image_51.png", "description": "サロンメンバーからの質問に対する回答スクリーンショット。インフルエンサーのアカウント戦略とターゲット設定に関する具体的な相談内容が掲載されている。"},
    {"index": 1886, "filename": "image_52.png", "description": "Twitterとマッチングアプリの活用方法についての回答メッセージ。ターゲットとなる異業種女子の見つけ方と発信方針の相談に対する詳細なアドバイスが記載されている。"},
    {"index": 1887, "filename": "image_53.png", "description": "神代希海からのTwitter・TikTok活用戦略に関する提案内容。5つの導線方法（TikTok投稿、稼ぐ系人間との接点、プレゼント企画、LINE運用、セミナー開催）がリスト化されている。"},
    {"index": 1888, "filename": "image_54.png", "description": "質問に対する詳細な回答テキスト。同ジャンルのインフルエンサー同士の連携方法とimpl数の計算、TikTok発信の必要性に関する説明が含まれている。"},
    {"index": 1889, "filename": "image_55.png", "description": "ソレイユによる有益投稿に関する質問と回答。ブログ記事の有益性と男性ターゲットの属性判定についての相談メッセージが表示されている。"},
    {"index": 1890, "filename": "image_56.png", "description": "復縁系アカウントのマネタイズ戦略に関する質問メッセージ。TikTok発信の必要性、リスト構築、セミナー参加関連の費用に関する相談が記載されている。"},
    {"index": 1891, "filename": "image_57.png", "description": "商品販売とコンサル販売の選択に関する回答。基本は無料相談とコンサル販売が主軸で、割と強気の値付けが必要という具体的なアドバイスが含まれている。"},
    {"index": 1892, "filename": "image_58.png", "description": "TikTokのアニメ紹介ジャンルの投稿戦略に関する詳細な相談。アニメ系HARMの法則と現在の市場環境、投稿スタイルの改善方法についての説明が掲載されている。"},
    {"index": 1893, "filename": "image_59.png", "description": "マネタイズ難易度とジャンル選択に関するやり取り。ダイエット系の競争環境と広告収益の見通し、マッチングアプリ使用時の実績データ不足に関する相談が含まれている。"},
    {"index": 1894, "filename": "image_60.png", "description": "恋愛系コンサル事業の企画配布に関する提案。初期段階のフレキャンと特に効果的なのか、目標テンプレート販売とフォロワー増加施策についての質問が記載されている。"},
    {"index": 1895, "filename": "image_61.png", "description": "Twitterの企画配布結果に関する報告内容。3日間で200人台の新規フォロワー獲得、インプ数9600、70人以上のフォロワー増加という具体的な実績数値が掲載されている。"},
    {"index": 1896, "filename": "image_62.png", "description": "ナンパとマッチングアプリの活用に関する相談と回答。モテ系のダイエット攻略、実践的なテクニック、大手講座の有用性についてのアドバイスメッセージが表示されている。"},
    {"index": 1897, "filename": "image_63.png", "description": "ダイエット系アカウント運用における月100万目指しの実現可能性に関する質問。アカウント作成から1ヶ月で達成困難を指摘する回答内容が記載されている。"},
    {"index": 1898, "filename": "image_64.png", "description": "Twitter企画についてのリプライとコメント。始めたばかりのアカウント向けのフレキャン特に効果的という意見と、継続的なフォロワー増加に関する相談が含まれている。"},
    {"index": 1899, "filename": "image_65.png", "description": "企画配布の具体的な目標設定に関する提案。アカウントのゴール設定、フォロワーターゲット層、企画での参加層拡大方法についての戦略的なアドバイスが掲載されている。"},
    {"index": 1900, "filename": "image_66.png", "description": "企画配布の方向性に関する最終的なアドバイス内容。初期段階でのフレキャン活用の有効性を強調し、SNS連用のキャンペーン選択に関する説明が記載されている。"},
    {"index": 1901, "filename": "image_67.png", "description": "完全初心者のフォロワー70人増加施策に関する質問と回答。期間内での達成可能性についての詳細な説明と、マーケティング戦略改善に向けた具体的なアドバイスが含まれている。"},
    {"index": 1902, "filename": "image_68.png", "description": "恋愛系YouTube動画制作の企画内容に関する長文相談。「占い師は天才に見えなくなる」という占い系プロモーション戦略と投稿スケジュール計画についてのメッセージが掲載されている。"},
    {"index": 1903, "filename": "image_69.png", "description": "マネタイズ手法と年齢ターゲット設定に関する回答メッセージ。TikTok契約について、フォロワー1000人超えてのLINE公式登録促進、コンサル販売戦略についての具体的なアドバイスが記載されている。"},
    {"index": 1904, "filename": "image_70.png", "description": "声を活用したアカウント運用に関する相談と回答。音声コンテンツでの「声×○○」マッチング戦略、恋愛声優系ジャンルの特性、ファン化施策についての詳細なやり取りが掲載されている。"},
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

    print(f"\n✓ Batch 1885-1904 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
