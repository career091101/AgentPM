#!/usr/bin/env python3
"""
Facebook投稿テストスクリプト（投稿直前で止める）
"""
import json
from datetime import datetime

def load_approved_post():
    """承認された投稿案を読み込み"""
    data_file = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/posts_generated_ai_20260102.json"

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 案2（衝撃発言型）を取得
    approved_post = data["posts"][1]  # 案2はインデックス1

    return approved_post

def generate_facebook_version(linkedin_post):
    """Facebook用投稿（LinkedIn全文をそのまま使用）"""

    # Facebook用もLinkedInと同じ全文を使用
    facebook_post = linkedin_post

    return facebook_post

def preview_facebook_post():
    """Facebook投稿のプレビュー表示（投稿はしない）"""

    print("=" * 60)
    print("Facebook投稿テスト（投稿直前で停止）")
    print("=" * 60)

    # 承認された投稿を読み込み
    print("\n📂 承認済み投稿読み込み中...")
    approved_post = load_approved_post()
    print(f"✅ 読み込み完了: {approved_post['variant']}")
    print(f"   元の文字数: {approved_post['character_count']}字")

    # Facebook用に準備（全文使用）
    print("\n📝 Facebook用投稿準備中（LinkedIn全文使用）...")
    facebook_post = generate_facebook_version(approved_post["content"])
    facebook_char_count = len(facebook_post)
    print(f"✅ 準備完了: {facebook_char_count}字")

    # プレビュー表示
    print("\n" + "=" * 60)
    print("📝 Facebook投稿プレビュー")
    print("=" * 60)
    print(facebook_post)
    print("=" * 60)

    # 投稿準備完了メッセージ
    print("\n✅ Facebook投稿準備完了")
    print("\n📋 投稿情報")
    print(f"   文字数: {facebook_char_count}字")
    print(f"   投稿先: Facebook")
    print(f"   投稿方法: Claude in Chrome（ブラウザ操作）")

    print("\n🛑 テストモード: 投稿は実行しません")

    print("\n" + "-" * 60)
    print("📌 実際に投稿する場合の手順:")
    print("-" * 60)
    print("1. ブラウザでFacebookにログイン")
    print("2. https://www.facebook.com を開く")
    print("3. 「今何してる？」投稿ボックスをクリック")
    print("4. 上記の投稿文をコピー＆ペースト")
    print("5. 投稿ボタンをクリック")
    print("-" * 60)

    # 投稿データ保存
    post_data = {
        "platform": "facebook",
        "variant": approved_post["variant"],
        "char_count": facebook_char_count,
        "content": facebook_post,
        "note": "LinkedIn全文をそのまま使用",
        "test_mode": True,
        "prepared_at": datetime.now().isoformat()
    }

    output_file = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/facebook_post_preview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 投稿プレビューデータ保存: {output_file}")

    print("\n" + "=" * 60)
    print("Facebook投稿テスト完了")
    print("=" * 60)

if __name__ == "__main__":
    preview_facebook_post()
