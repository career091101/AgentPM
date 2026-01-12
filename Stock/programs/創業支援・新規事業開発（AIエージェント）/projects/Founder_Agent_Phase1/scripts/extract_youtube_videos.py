#!/usr/bin/env python3
"""
YouTube動画抽出スクリプト（Founder Agent用）

チャンネルIDリストから関連テーマの動画を検索・抽出
キーワード: Macrohard, AIエージェント, OpenAI, AGI, 自律型AI, 起業等
"""

import json
import re
import time
from pathlib import Path
from datetime import datetime
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    TRANSCRIPT_API_AVAILABLE = True
except ImportError:
    TRANSCRIPT_API_AVAILABLE = False
    print("⚠ youtube-transcript-api がインストールされていません")

# 設定
PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1")
CHANNEL_FILE = PROJECT_ROOT / "documents/1_initiating/Youtube_Chanels"
OUTPUT_DIR = PROJECT_ROOT / "documents/references/transcripts"
DELAY = 2  # リクエスト間隔（秒）

# 関連キーワード（project_charter.mdより抽出）
KEYWORDS = [
    # 英語キーワード
    "macrohard", "xai", "elon musk", "ai agent", "agentic ai",
    "openai", "level 5", "organizer", "agi", "artificial general intelligence",
    "autonomous", "grok", "claude", "gemini", "anthropic",
    "startup", "founder", "mvp", "lean startup", "pmf",
    # 日本語キーワード
    "aiエージェント", "エージェントai", "自律型ai", "自律ai",
    "起業", "スタートアップ", "創業", "事業創出",
    "リーンスタートアップ", "起業の科学", "田所",
    "マネタイズ", "ビジネスモデル", "サービス開発",
    "ソロプレナー", "個人開発", "indie hacker",
    "生成ai", "大規模言語モデル", "llm", "gpt",
]

def clean_channel_id(channel_id: str) -> str:
    """チャンネルIDをクリーンアップ"""
    # エスケープ文字とスペースを削除
    cleaned = channel_id.strip()
    cleaned = cleaned.replace("\\", "")
    cleaned = cleaned.replace("*", "")
    cleaned = cleaned.replace("_", "")
    return cleaned

def load_channel_ids() -> list:
    """チャンネルIDリストを読み込み"""
    if not CHANNEL_FILE.exists():
        print(f"✗ チャンネルファイルが見つかりません: {CHANNEL_FILE}")
        return []
    
    with open(CHANNEL_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    channel_ids = []
    for line in lines:
        line = line.strip()
        if line and line.startswith("UC"):
            cleaned = clean_channel_id(line)
            if len(cleaned) >= 20:  # 有効なチャンネルIDは24文字
                channel_ids.append(cleaned)
    
    return channel_ids

def is_relevant_video(title: str, description: str = "") -> bool:
    """動画が関連テーマに合致するか判定"""
    text = (title + " " + description).lower()
    for keyword in KEYWORDS:
        if keyword.lower() in text:
            return True
    return False

def get_channel_url(channel_id: str) -> str:
    """チャンネルURLを生成"""
    return f"https://www.youtube.com/channel/{channel_id}/videos"

def save_video_list(videos: list, filename: str):
    """動画リストをJSONで保存"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / filename
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 保存完了: {output_file}")
    return output_file

def create_url_list_md(videos: list, filename: str):
    """動画URLリストをMarkdownで保存"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / filename
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# YouTube動画URL一覧（Founder Agent関連）\n\n")
        f.write(f"**生成日時**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**動画数**: {len(videos)}件\n\n")
        f.write("---\n\n")
        
        for i, video in enumerate(videos, 1):
            f.write(f"## {i}. {video.get('title', 'タイトル不明')}\n\n")
            f.write(f"- **URL**: https://www.youtube.com/watch?v={video.get('video_id', '')}\n")
            f.write(f"- **チャンネル**: {video.get('channel_name', '不明')}\n")
            if video.get('matched_keywords'):
                f.write(f"- **マッチしたキーワード**: {', '.join(video['matched_keywords'])}\n")
            f.write("\n")
    
    print(f"✓ Markdown保存完了: {output_file}")
    return output_file

def main():
    """メイン処理"""
    print("=" * 60)
    print("YouTube動画抽出（Founder Agent関連）")
    print("=" * 60)
    
    # チャンネルID読み込み
    channel_ids = load_channel_ids()
    print(f"\n読み込んだチャンネル数: {len(channel_ids)}")
    
    if not channel_ids:
        print("✗ チャンネルIDが見つかりません")
        return
    
    # チャンネルURLリストを出力
    print("\n=== チャンネルURL一覧（最初の10件） ===")
    for i, cid in enumerate(channel_ids[:10], 1):
        print(f"{i}. {get_channel_url(cid)}")
    
    print(f"\n... 他 {len(channel_ids) - 10} チャンネル")
    
    # チャンネルIDリストをJSONで保存
    channel_data = [{"channel_id": cid, "url": get_channel_url(cid)} for cid in channel_ids]
    save_video_list(channel_data, "channel_list.json")
    
    print("\n" + "=" * 60)
    print("次のステップ:")
    print("1. ブラウザで各チャンネルにアクセスして動画リストを確認")
    print("2. または YouTube Data API を使用して動画を自動取得")
    print("=" * 60)

if __name__ == "__main__":
    main()
