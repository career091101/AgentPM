#!/usr/bin/env python3
"""
インフルエンサーリストのマージスクリプト

既存の手動キュレーションリスト + 今回収集した日本人アカウント（実測データ）をマージ
"""

import csv
import re
from pathlib import Path
from datetime import datetime

# 日本人アカウントの判定（ユーザー名、ツイート内容から推定）
JAPANESE_ACCOUNTS = {
    'Hayakawashobo', 'Ryosuke_Nishida', 'KeiTanaka_Radio', 'Yacamochi_db',
    'KOBA789', 'daibakuto', 'KoukichiTakahashi', 'toricls', 'ksk_S',
    'nikkei', 'JILPT_SOUKEN', 'yuki_99_s', 'tomohiroarasaki', 'daishicrypto',
    'AnEngineer_s', 's_kajita', 'tomos_jp', 'takahiroanno', 'makaibito',
    'kakeruixy', 'ikedanoriyuki', 'Tsuyoshi_SEINO', 'hori_shigeki',
    'takapon_jp', 'chibichilo0913', 'amachino', 'sasakitoshinao',
    'atsukim0ri', 'rimowalock', 'Yuto_SayMove', 'TakehikoTakano',
    'nicosokufx', 'nopainkiller', 'noatake1127', 'haru_tachibana8',
    'mameyama_kun', '666169koshimizu', 'GyyARm5pyYHddh0'
}

# 既存リストのTwitterハンドル（@なし）
EXISTING_ACCOUNTS = {
    'masahiro_chaen': {'name': 'チャエン（茶圓将裕）', 'category': 'トップインフルエンサー', 'priority': 5},
    'shota7180': {'name': '木内翔大', 'category': 'トップインフルエンサー', 'priority': 5},
    'fladdict': {'name': '深津貴之', 'category': 'トップインフルエンサー', 'priority': 5},
    'ochyai': {'name': '落合陽一', 'category': 'トップインフルエンサー', 'priority': 5},
    'takapon_jp': {'name': '堀江貴文', 'category': 'トップインフルエンサー', 'priority': 4},
    'ai_syacho': {'name': '元木大介', 'category': 'スタートアップCEO', 'priority': 5},
    'fukkyy': {'name': '福島良典', 'category': 'スタートアップCEO', 'priority': 4},
    'onoharuaki': {'name': '大野峻典', 'category': 'スタートアップCEO', 'priority': 4},
    'hillbig': {'name': '岡野原大輔', 'category': 'スタートアップCEO', 'priority': 4},
    'notef': {'name': 'ノトフ', 'category': 'スタートアップCEO', 'priority': 3},
    'ymatsuo': {'name': '松尾豊', 'category': '研究者・学者', 'priority': 5},
    'ImAI_Eruel': {'name': '今井翔太', 'category': '研究者・学者', 'priority': 4},
    '_daichikonno': {'name': '紺野大地', 'category': '研究者・学者', 'priority': 4},
    'nomnok': {'name': '新井紀子', 'category': '研究者・学者', 'priority': 3},
    'miyayou': {'name': '三宅陽一郎', 'category': '研究者・学者', 'priority': 3},
    'TetsuyaOgata': {'name': '尾形哲也', 'category': '研究者・学者', 'priority': 3},
    'MacopeninSUTABA': {'name': 'かずなり', 'category': 'プロンプトエンジニア', 'priority': 4},
    'usutaku_channel': {'name': 'usutaku（臼井拓水）', 'category': 'プロンプトエンジニア', 'priority': 4},
    'chatgptair': {'name': 'あるる', 'category': 'プロンプトエンジニア', 'priority': 4},
    'Suguru_AI_Biz': {'name': 'すぐる', 'category': 'プロンプトエンジニア', 'priority': 4},
    'iketomohiro': {'name': '池田朋弘', 'category': 'プロンプトエンジニア', 'priority': 4},
    'AI_sokuho': {'name': 'AI速報', 'category': 'ニュース系', 'priority': 4},
    'KEITO_AI_x_WEB': {'name': 'KEITO（三浦圭人）', 'category': 'YouTuber', 'priority': 4},
    'nyanta_AI': {'name': 'にゃんたのAIチャンネル', 'category': 'YouTuber', 'priority': 3},
    'iketomo_ch': {'name': 'いけともch', 'category': 'YouTuber', 'priority': 3},
    'nakajijp': {'name': 'ウェブ職TV（なかじ）', 'category': 'YouTuber', 'priority': 3},
    'hirochuu8': {'name': 'ひろちゅ〜', 'category': 'YouTuber', 'priority': 4},
}

def load_collected_data(csv_path):
    """今回収集したCSVデータを読み込み"""
    data = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def categorize_account(username, engagement):
    """アカウントのカテゴリを推定"""
    username_lower = username.lower()

    # ニュース・メディア
    if any(keyword in username_lower for keyword in ['nikkei', 'news', 'jilpt']):
        return 'ニュース・メディア'

    # プログラミング・開発
    if any(keyword in username_lower for keyword in ['engineer', 'dev', 'code', 'programming']):
        return 'プログラミング・開発'

    # AI・テック
    if any(keyword in username_lower for keyword in ['ai', 'tech', 'takano']):
        return 'AI・テック'

    # ビジネス・投資
    if any(keyword in username_lower for keyword in ['biz', 'invest', 'crypto', 'fx']):
        return 'ビジネス・投資'

    # その他
    return 'その他'

def merge_lists(collected_csv, output_md):
    """リストをマージしてMarkdownレポート生成"""

    # 今回収集データの読み込み
    collected_data = load_collected_data(collected_csv)

    # 日本人アカウントのみフィルタリング
    japanese_collected = [
        row for row in collected_data
        if row['Username'] in JAPANESE_ACCOUNTS
    ]

    print(f"📊 今回収集リストから日本人アカウント抽出: {len(japanese_collected)}名")

    # 既存リストとの重複チェック
    new_accounts = []
    overlap_accounts = []

    for row in japanese_collected:
        username = row['Username']
        if username in EXISTING_ACCOUNTS:
            overlap_accounts.append({
                'username': username,
                'name': EXISTING_ACCOUNTS[username]['name'],
                'category': EXISTING_ACCOUNTS[username]['category'],
                'priority': EXISTING_ACCOUNTS[username]['priority'],
                'engagement': int(row['Total Engagement']),
                'likes': int(row['Total Likes']),
                'retweets': int(row['Total Retweets']),
                'tweets': int(row['Tweet Count'])
            })
        else:
            new_accounts.append({
                'username': username,
                'category': categorize_account(username, int(row['Total Engagement'])),
                'engagement': int(row['Total Engagement']),
                'likes': int(row['Total Likes']),
                'retweets': int(row['Total Retweets']),
                'tweets': int(row['Tweet Count'])
            })

    print(f"✅ 既存リストと重複: {len(overlap_accounts)}名")
    print(f"🆕 新規発見アカウント: {len(new_accounts)}名")

    # Markdownレポート生成
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# AI/生成AI インフルエンサーリスト（統合版）\n\n")
        f.write(f"**作成日**: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**プロジェクト**: SNS生産性向上プロジェクト\n")
        f.write(f"**データソース**: 手動キュレーション（50名） + X実測データ（日本人{len(japanese_collected)}名）\n\n")
        f.write("---\n\n")

        f.write("## 📊 統合サマリー\n\n")
        f.write(f"- **既存リスト**: 50名（AI/生成AI特化、優先度付き）\n")
        f.write(f"- **今回収集**: {len(japanese_collected)}名（実測エンゲージメントデータ）\n")
        f.write(f"- **重複アカウント**: {len(overlap_accounts)}名\n")
        f.write(f"- **新規発見**: {len(new_accounts)}名\n\n")
        f.write("---\n\n")

        # 重複アカウントのエンゲージメント実績
        if overlap_accounts:
            f.write("## ✅ 既存リスト × 実測エンゲージメント（重複アカウント）\n\n")
            f.write("既存リストに含まれていたアカウントの実測エンゲージメントデータ。\n\n")
            f.write("| ランク | 名前 | Username | カテゴリ | 優先度 | エンゲージメント | いいね | リツイート | ツイート数 |\n")
            f.write("|--------|------|----------|----------|--------|----------------|--------|-----------|----------|\n")

            overlap_accounts.sort(key=lambda x: x['engagement'], reverse=True)
            for i, acc in enumerate(overlap_accounts, 1):
                f.write(f"| {i} | **{acc['name']}** | @{acc['username']} | {acc['category']} | ")
                f.write(f"{'★' * acc['priority']} | {acc['engagement']:,} | {acc['likes']:,} | ")
                f.write(f"{acc['retweets']:,} | {acc['tweets']} |\n")

            f.write("\n---\n\n")

        # 新規発見アカウント
        if new_accounts:
            f.write("## 🆕 新規発見アカウント（実測エンゲージメント）\n\n")
            f.write("既存リストに含まれていなかった日本人アカウント。\n\n")

            # カテゴリ別に整理
            categories = {}
            for acc in new_accounts:
                cat = acc['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(acc)

            for category, accounts in sorted(categories.items()):
                f.write(f"### {category} ({len(accounts)}名)\n\n")
                f.write("| ランク | Username | エンゲージメント | いいね | リツイート | ツイート数 |\n")
                f.write("|--------|----------|----------------|--------|-----------|----------|\n")

                accounts.sort(key=lambda x: x['engagement'], reverse=True)
                for i, acc in enumerate(accounts, 1):
                    f.write(f"| {i} | @{acc['username']} | {acc['engagement']:,} | ")
                    f.write(f"{acc['likes']:,} | {acc['retweets']:,} | {acc['tweets']} |\n")

                f.write("\n")

            f.write("---\n\n")

        # 既存リストの残り（今回未収集）
        f.write("## 📋 既存リスト（今回未収集アカウント）\n\n")
        f.write("既存50名リストのうち、今回のX収集では捕捉されなかったアカウント。\n\n")

        collected_usernames = {row['Username'] for row in japanese_collected}
        uncollected = {
            username: info
            for username, info in EXISTING_ACCOUNTS.items()
            if username not in collected_usernames
        }

        f.write(f"**未収集数**: {len(uncollected)}名\n\n")

        # カテゴリ別に整理
        cat_uncollected = {}
        for username, info in uncollected.items():
            cat = info['category']
            if cat not in cat_uncollected:
                cat_uncollected[cat] = []
            cat_uncollected[cat].append({'username': username, **info})

        for category, accounts in sorted(cat_uncollected.items()):
            f.write(f"### {category} ({len(accounts)}名)\n\n")
            f.write("| # | 名前 | Username | 優先度 |\n")
            f.write("|---|------|----------|--------|\n")

            accounts.sort(key=lambda x: x['priority'], reverse=True)
            for i, acc in enumerate(accounts, 1):
                f.write(f"| {i} | {acc['name']} | @{acc['username']} | {'★' * acc['priority']} |\n")

            f.write("\n")

        f.write("---\n\n")

        # アクションプラン
        f.write("## 📈 推奨アクション\n\n")
        f.write("### 1. 新規発見アカウントの詳細調査\n\n")
        f.write(f"今回新たに発見された{len(new_accounts)}名のアカウントについて、以下を調査:\n")
        f.write("- プロフィール確認（AI/生成AI関連か？）\n")
        f.write("- 過去ツイートの内容分析\n")
        f.write("- フォロワー数・影響力の評価\n")
        f.write("- 既存リストへの追加可否判断\n\n")

        f.write("### 2. 既存リストの優先度見直し\n\n")
        if overlap_accounts:
            f.write("重複アカウントの実測エンゲージメントを基に優先度を再評価:\n")
            for acc in overlap_accounts[:5]:
                f.write(f"- **{acc['name']}** (@{acc['username']}): {acc['engagement']:,}エンゲージメント\n")
        f.write("\n")

        f.write("### 3. 未収集アカウントのフォロー・監視\n\n")
        f.write(f"既存リストの{len(uncollected)}名について、今後のX収集で捕捉できるよう:\n")
        f.write("- フォロー推奨リストに追加\n")
        f.write("- 定期的な手動チェック\n")
        f.write("- アカウント活動状況の確認\n\n")

        f.write("---\n\n")
        f.write(f"*レポート生成: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")

    print(f"\n💾 統合レポート保存: {output_md}")

    # CSVも生成
    csv_output = str(output_md).replace('.md', '.csv')
    with open(csv_output, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Type', 'Username', 'Name', 'Category', 'Priority', 'Engagement', 'Likes', 'Retweets', 'Tweets']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # 重複アカウント
        for acc in overlap_accounts:
            writer.writerow({
                'Type': '既存+実測',
                'Username': acc['username'],
                'Name': acc['name'],
                'Category': acc['category'],
                'Priority': acc['priority'],
                'Engagement': acc['engagement'],
                'Likes': acc['likes'],
                'Retweets': acc['retweets'],
                'Tweets': acc['tweets']
            })

        # 新規アカウント
        for acc in new_accounts:
            writer.writerow({
                'Type': '新規発見',
                'Username': acc['username'],
                'Name': '',
                'Category': acc['category'],
                'Priority': '',
                'Engagement': acc['engagement'],
                'Likes': acc['likes'],
                'Retweets': acc['retweets'],
                'Tweets': acc['tweets']
            })

        # 未収集アカウント
        for username, info in uncollected.items():
            writer.writerow({
                'Type': '既存のみ',
                'Username': username,
                'Name': info['name'],
                'Category': info['category'],
                'Priority': info['priority'],
                'Engagement': '',
                'Likes': '',
                'Retweets': '',
                'Tweets': ''
            })

    print(f"💾 CSV保存: {csv_output}")

    return {
        'total_japanese': len(japanese_collected),
        'overlap': len(overlap_accounts),
        'new': len(new_accounts),
        'uncollected': len(uncollected)
    }

if __name__ == '__main__':
    # パス設定
    base_dir = Path(__file__).parent.parent
    collected_csv = base_dir / 'data' / 'x_timeline_20260101_final' / 'top_50_influencers.csv'
    output_md = base_dir / 'documents' / '2_discovery' / 'ai_influencer_list_merged.md'

    # マージ実行
    stats = merge_lists(collected_csv, output_md)

    print("\n" + "="*60)
    print("✅ インフルエンサーリストマージ完了")
    print("="*60)
    print(f"📊 統計:")
    print(f"  - 日本人アカウント: {stats['total_japanese']}名")
    print(f"  - 既存リストと重複: {stats['overlap']}名")
    print(f"  - 新規発見: {stats['new']}名")
    print(f"  - 既存リスト未収集: {stats['uncollected']}名")
