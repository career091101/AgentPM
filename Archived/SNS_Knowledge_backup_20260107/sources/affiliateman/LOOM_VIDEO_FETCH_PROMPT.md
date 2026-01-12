# Loom動画取得タスク - システムプロンプト

このプロンプトを別チャットで使用して、未取得のLoom動画を取得してください。

---

## 🎯 タスク概要

affiliateman.siteプロジェクトの最後の未取得コンテンツである **Loom動画1件** を取得し、文字起こしを行い、metadata.jsonを更新して100%の網羅率を達成する。

---

## 📋 タスク詳細

### 対象コンテンツ

**動画タイトル**: インスタマネタイズ最新2025年
**Loom URL**: https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3?sid=fe4d98be-8c0e-42a7-a000-7bbbcf49e9ed
**検証済みステータス**: ✅ アクセス可能（200 OK）
**ページタイトル**: "Instagram - 31 December 2024 | Loom"
**ページサイズ**: 26,791 bytes
**カテゴリ**: instagram_strategy

### プロジェクトパス

**ベースディレクトリ**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman`

---

## 📁 ディレクトリ構造

```
affiliateman/
├── video_transcripts/
│   └── instagram_strategy/          # ← ここに保存
│       └── インスタマネタイズ最新2025年.md
├── scripts/
│   ├── youtube_transcriber.py       # YouTube用（参考）
│   ├── requirements.txt
│   └── .env                         # OpenAI API Key
├── chunks/
│   └── all_chunks.jsonl            # ← 更新必要
└── metadata.json                    # ← 更新必要
```

---

## 🔧 実行手順

### ステップ1: Loom動画のダウンロード

以下のいずれかの方法でLoom動画をダウンロード：

#### オプションA: Loom Downloader（推奨）

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts

# Loom downloaderのインストール（必要に応じて）
pip install loom-downloader

# 動画ダウンロード
loom-dl "https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3" \
  -o "../temp/loom_video.mp4"
```

#### オプションB: yt-dlp（汎用）

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts

# yt-dlpでダウンロード試行
yt-dlp "https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3" \
  -o "../temp/loom_video.%(ext)s"
```

#### オプションC: ブラウザ経由ダウンロード

1. Claude in Chrome MCPツールを使用
2. Loom URLにアクセス
3. ダウンロードボタンをクリック（ログイン不要の場合）
4. `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/temp/` に保存

---

### ステップ2: Whisper APIで文字起こし

```python
# scripts/transcribe_loom.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 音声ファイルを文字起こし
audio_file_path = "../temp/loom_video.mp4"  # または .mp3, .wav など

with open(audio_file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="ja",
        response_format="text"
    )

# 保存
output_path = "../video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md"

content = f"""# インスタマネタイズ最新2025年

**ソース**: Loom
**URL**: https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3
**カテゴリ**: Instagram戦略
**文字起こし日**: 2025-12-29
**文字起こし方法**: OpenAI Whisper API

---

## 文字起こし

{transcript}
"""

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ 文字起こし完了: {output_path}")
print(f"文字数: {len(transcript):,}")
```

実行:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 transcribe_loom.py
```

---

### ステップ3: metadata.jsonの更新

```python
# scripts/update_metadata_loom.py

import json

metadata_path = "../metadata.json"

with open(metadata_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Loom動画のエントリを探して更新
for video in data["videos"]:
    if "インスタマネタイズ最新2025年" in video.get("title", ""):
        video["has_transcript"] = True
        video["transcript_file"] = "video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md"
        video["method"] = "whisper"
        video["category"] = "instagram_strategy"
        print(f"✅ 更新: {video['title']}")
        break

# 統計を更新
stats = data.get("video_stats", {})
stats["with_transcript"] = stats.get("with_transcript", 44) + 1
stats["without_transcript"] = stats.get("without_transcript", 6) - 1
stats["completion_rate"] = f"{(stats['with_transcript'] / stats['total_videos'] * 100):.1f}%"

data["video_stats"] = stats

# 保存
with open(metadata_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ metadata.json更新完了")
print(f"新しい完了率: {stats['completion_rate']}")
```

実行:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 update_metadata_loom.py
```

---

### ステップ4: RAGチャンクの生成

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts

# 既存のchunker.pyを使用
python3 chunker.py
```

期待される出力:
- `chunks/all_chunks.jsonl` が更新される
- 新しいチャンクが追加される（推定: 5-10チャンク）

---

### ステップ5: 最終検証

```python
# scripts/final_verification.py

import json
import os

# metadata.json確認
with open("../metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== 最終検証 ===\n")

# 動画統計
stats = data.get("video_stats", {})
print(f"総動画数: {stats.get('total_videos', 0)}")
print(f"文字起こし済み: {stats.get('with_transcript', 0)}")
print(f"未取得: {stats.get('without_transcript', 0)}")
print(f"完了率: {stats.get('completion_rate', 'N/A')}")

# ファイル存在確認
transcript_file = "../video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md"
if os.path.exists(transcript_file):
    size = os.path.getsize(transcript_file)
    print(f"\n✅ 文字起こしファイル存在: {size:,} bytes")
else:
    print(f"\n❌ ファイルが見つかりません: {transcript_file}")

# チャンク数確認
chunks_file = "../chunks/all_chunks.jsonl"
if os.path.exists(chunks_file):
    with open(chunks_file, "r", encoding="utf-8") as f:
        chunk_count = sum(1 for _ in f)
    print(f"✅ 総チャンク数: {chunk_count}")
else:
    print(f"❌ チャンクファイルが見つかりません")

print("\n" + "="*50)
if stats.get('without_transcript', 6) == 0:
    print("🎉 100%の網羅率を達成しました！")
else:
    print(f"⚠️ まだ{stats.get('without_transcript', 0)}件の未取得コンテンツがあります")
```

---

## 📊 期待される成果物

### 1. 文字起こしファイル
- **パス**: `video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md`
- **形式**: Markdown
- **推定サイズ**: 10-50KB（動画の長さによる）

### 2. 更新されたmetadata.json
- `video_stats.with_transcript`: 44 → 45
- `video_stats.without_transcript`: 6 → 5
- `video_stats.completion_rate`: "88.0%" → "90.0%"

### 3. 更新されたRAGチャンク
- `chunks/all_chunks.jsonl`: 708チャンク → 713-718チャンク（推定）

---

## 🚨 トラブルシューティング

### 問題1: Loomダウンロードができない

**症状**: ダウンロードツールがLoomに対応していない

**解決策**:
1. ブラウザで直接視聴し、画面録画
2. Loom公式のダウンロード機能を使用（要ログイン）
3. Claude in Chromeを使って手動ダウンロード

### 問題2: 音声ファイルが大きすぎる（25MB超）

**症状**: Whisper APIが25MBまでしか対応していない

**解決策**:
```bash
# FFmpegで圧縮
ffmpeg -i loom_video.mp4 -vn -ar 16000 -ac 1 -b:a 64k loom_audio_compressed.mp3
```

### 問題3: API料金が心配

**推定コスト**:
- Whisper API: $0.006/分
- 20分の動画の場合: 約$0.12（約18円）
- 非常に低コスト

---

## ✅ 完了チェックリスト

タスク完了時に以下を確認：

- [ ] Loom動画をダウンロード
- [ ] Whisper APIで文字起こし
- [ ] 文字起こしファイルを保存（`video_transcripts/instagram_strategy/`）
- [ ] metadata.jsonを更新
- [ ] RAGチャンクを再生成
- [ ] 最終検証スクリプトを実行
- [ ] 完了率が向上したことを確認（88% → 90%以上）
- [ ] 一時ファイル（temp/）をクリーンアップ

---

## 📝 追加のメタデータ更新（オプション）

既存の3件の対談動画もmetadata.jsonで「取得済み」としてマークすることを推奨：

```python
# 以下の3件のhas_transcriptをTrueに更新
corrections = [
    {"url": "https://affiliateman.site/talk_nao/", "youtube_id": "vEUepyG867M"},
    {"url": "https://affiliateman.site/con_love/", "youtube_id": "uwoKHVJ-w3U"},
    {"url": "https://affiliateman.site/con_twitter/", "youtube_id": "shU5X2CAkjY"}
]
```

---

## 🎯 成功基準

このタスクが成功したと言えるのは：

1. ✅ Loom動画の文字起こしファイルが存在
2. ✅ metadata.jsonが正しく更新されている
3. ✅ RAGチャンクが再生成されている
4. ✅ 完了率が88.0%から向上している
5. ✅ 検証スクリプトがエラーなく完了

---

## 💬 補足情報

### 既存の.envファイル

```bash
# scripts/.env の内容
OPENAI_API_KEY=your-api-key-here
AFFILIATEMAN_PASSWORD=your-password-here
```

**重要**: OpenAI API Keyが設定されていることを確認してください。

### 既存のrequirements.txt

```
openai
python-dotenv
requests
yt-dlp
```

インストール:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
pip install -r requirements.txt
```

---

## 🚀 クイックスタート（推奨手順）

```bash
# 1. プロジェクトディレクトリに移動
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman

# 2. 一時ディレクトリ作成
mkdir -p temp

# 3. Loom動画をダウンロード（方法はオプションA-Cから選択）
# 例: ブラウザで手動ダウンロードして temp/ に保存

# 4. 文字起こしスクリプトを作成・実行
cd scripts
# （上記のtranscribe_loom.pyを作成）
python3 transcribe_loom.py

# 5. metadata.json更新スクリプトを作成・実行
# （上記のupdate_metadata_loom.pyを作成）
python3 update_metadata_loom.py

# 6. RAGチャンク再生成
python3 chunker.py

# 7. 最終検証
# （上記のfinal_verification.pyを作成）
python3 final_verification.py

# 8. 一時ファイルのクリーンアップ
cd ..
rm -rf temp/
```

---

**作成日**: 2025-12-29
**対象プロジェクト**: affiliateman.site コンテンツ取得
**最終目標**: 100%網羅率の達成
**現在の進捗**: 99.4% (177/178件)
**残りタスク**: Loom動画1件
