#!/usr/bin/env python3
"""
SNS Post Generator using Gemini API
指定されたURLまたはテキストから、SNS（X/Twitter, LinkedIn, Facebook）用の投稿案、
コメント案、画像生成プロンプトを自動生成します。
"""

import os
import sys
import argparse
import datetime
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from urllib.parse import urlparse

# 設定
# gemini-1.5-pro-latest が使えない場合は適宜変更。
DEFAULT_MODEL = "gemini-2.0-flash-exp" 
FLOW_DIR_BASE = "/Users/yuichi/AIPM/aipm_v0/Flow"

def get_api_key():
    """APIキーの取得"""
    # 1. 環境変数から
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key
        
    # 2. pdf-reader-mcpのconfigから (既存の環境を流用)
    import json
    from pathlib import Path
    
    config_file = Path.home() / ".config" / "pdf-reader-mcp" / "config.json"
    if config_file.exists():
        try:
            with open(config_file) as f:
                config = json.load(f)
                api_key = config.get("gemini_api_key")
                if api_key:
                    return api_key
        except Exception:
            pass
            
    # 3. 失敗
    print("エラー: GEMINI_API_KEY が見つかりません。")
    print("環境変数 GEMINI_API_KEY を設定するか、~/.config/pdf-reader-mcp/config.json に設定してください。")
    sys.exit(1)

def setup_gemini(api_key, model_name=DEFAULT_MODEL):
    """Gemini APIの初期化"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def extract_content_from_url(url):
    """URLからコンテンツを抽出"""
    print(f"URLからコンテンツを取得中: {url}")
    try:
        # User-Agentを設定してスクレイピング対策回避（簡易的）
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # タイトル取得
        title = soup.title.string if soup.title else "No Title"
        
        # 本文取得 (簡易的)
        # script, styleタグを除去
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        
        # 空白削除
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # 文字数制限 (Geminiのトークン制限考慮、ただし1.5は長いので緩めでOK)
        return title, clean_text[:30000] 
        
    except Exception as e:
        print(f"コンテンツ取得エラー: {e}")
        return None, None

def generate_sns_content(model, title, content, target_platform="X"):
    """Geminiを使ってSNSコンテンツを生成"""
    
    prompt = f"""
あなたはプロフェッショナルなSNSインフルエンサーです。
以下のコンテンツを元に、{target_platform}で高いエンゲージメント（いいね、リポスト、コメント）を獲得できる投稿を作成してください。

【コンテンツ情報】
タイトル: {title}
内容:
{content}

【出力要件】
以下の形式で出力してください。

# 1. 投稿案 (Post Draft)
- 読者の興味を惹くフックを入れる
- 要点を3〜5点にまとめる
- 絵文字を適切に使用する
- 最後に議論を呼ぶような問いかけ、または行動を促す
- 適切なハッシュタグを3〜5個つける

# 2. コメント/リプライ案 (Comment Draft)
- この投稿に対して、さらに深掘りする、または補足する自分のコメント（スレッド投稿や引用リポスト用）
- 批評的、または独自の視点を入れる

# 3. 画像生成プロンプト (Image Prompt)
- この投稿のアイキャッチ画像を作成するための画像生成プロンプト（英語）
- スタイル: モダン、ミニマル、テクノロジー、高画質
- 具体的なオブジェクトや色味を指定する

"""
    print("Geminiでコンテンツ生成中...")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini生成エラー: {e}")
        return None

def save_to_markdown(url, title, generated_text):
    """結果をMarkdownファイルに保存"""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    year_month = now.strftime("%Y%m")
    timestamp = now.strftime("%H%M%S")
    
    # 保存ディレクトリ: Flow/YYYYMM/YYYY-MM-DD/
    save_dir = os.path.join(FLOW_DIR_BASE, year_month, date_str)
    os.makedirs(save_dir, exist_ok=True)
    
    filename = f"sns_draft_{timestamp}.md"
    filepath = os.path.join(save_dir, filename)
    
    content = f"""# SNS投稿ドラフト

- **生成日時**: {now.strftime("%Y-%m-%d %H:%M:%S")}
- **ソースURL**: {url}
- **ソースタイトル**: {title}

---

{generated_text}

"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return filepath

def main():
    parser = argparse.ArgumentParser(description="SNS Post Generator")
    parser.add_argument("input", help="URL or Text content")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Gemini Model Name")
    parser.add_argument("--platform", default="X", help="Target Platform (X, LinkedIn, Facebook)")
    
    args = parser.parse_args()
    
    api_key = get_api_key()
    model = setup_gemini(api_key, args.model)
    
    input_data = args.input
    
    # URLかテキストか判定
    parsed = urlparse(input_data)
    if parsed.scheme and parsed.netloc:
        # URLの場合
        title, content = extract_content_from_url(input_data)
        if not content:
            print("コンテンツの抽出に失敗しました。")
            sys.exit(1)
    else:
        # テキストの場合
        title = "User Input Text"
        content = input_data
        
    generated_text = generate_sns_content(model, title, content, args.platform)
    
    if generated_text:
        filepath = save_to_markdown(input_data, title, generated_text)
        print(f"\n✅ 生成完了！ファイルに保存しました:\n{filepath}")
        print("\n--- 生成プレビュー ---\n")
        print(generated_text[:500] + "\n...(省略)...")
    else:
        print("生成に失敗しました。")

if __name__ == "__main__":
    main()
