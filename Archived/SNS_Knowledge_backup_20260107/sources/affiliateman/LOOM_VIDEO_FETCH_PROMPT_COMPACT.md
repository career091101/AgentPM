# 【別チャット用】Loom動画取得プロンプト

以下を新しいClaude Codeチャットにコピペして実行してください。

---

## タスク

affiliateman.siteプロジェクトの最後の未取得コンテンツ（Loom動画1件）を取得し、文字起こしして、metadata.jsonを更新してください。

## 対象動画

- **タイトル**: インスタマネタイズ最新2025年
- **URL**: https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3?sid=fe4d98be-8c0e-42a7-a000-7bbbcf49e9ed
- **ステータス**: アクセス可能（検証済み）
- **カテゴリ**: instagram_strategy

## プロジェクトパス

`/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman`

## 実行手順

### 1. Loom動画のダウンロード

以下のいずれかの方法で動画をダウンロード：

**オプションA**: ブラウザ経由（推奨）
- Claude in Chrome MCPツールを使用
- URLにアクセスしてダウンロード
- `temp/loom_video.mp4` として保存

**オプションB**: yt-dlp
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman
mkdir -p temp
cd temp
yt-dlp "https://www.loom.com/share/d0bce25956c3487e8e8c5fe73d4d12a3" -o "loom_video.%(ext)s"
```

### 2. 文字起こしスクリプトの作成と実行

`scripts/transcribe_loom.py`:
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 音声ファイルパス（実際のファイル名に合わせて調整）
audio_file_path = "../temp/loom_video.mp4"

print(f"文字起こし開始: {audio_file_path}")

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

print(f"✅ 完了: {output_path}")
print(f"文字数: {len(transcript):,}")
```

実行:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 transcribe_loom.py
```

### 3. metadata.jsonの更新

`scripts/update_metadata_loom.py`:
```python
import json

metadata_path = "../metadata.json"

with open(metadata_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Loom動画を更新
for video in data["videos"]:
    if "loom.com" in video.get("url", "") and "インスタマネタイズ最新2025年" in video.get("title", ""):
        video["has_transcript"] = True
        video["transcript_file"] = "video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md"
        video["method"] = "whisper"
        print(f"✅ 更新: {video['title']}")
        break

# 統計更新
stats = data.get("video_stats", {})
stats["with_transcript"] = stats.get("with_transcript", 44) + 1
stats["without_transcript"] = max(0, stats.get("without_transcript", 6) - 1)
stats["completion_rate"] = f"{(stats['with_transcript'] / stats.get('total_videos', 50) * 100):.1f}%"
data["video_stats"] = stats

with open(metadata_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ metadata.json更新完了")
print(f"完了率: {stats['completion_rate']}")
```

実行:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 update_metadata_loom.py
```

### 4. RAGチャンク再生成

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 chunker.py
```

### 5. 検証

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 -c "
import json
with open('../metadata.json', 'r') as f:
    data = json.load(f)
stats = data.get('video_stats', {})
print(f'完了率: {stats.get(\"completion_rate\", \"N/A\")}')
print(f'文字起こし済み: {stats.get(\"with_transcript\", 0)}/{stats.get(\"total_videos\", 0)}')
"
```

## トラブルシューティング

### ファイルサイズが25MB超の場合

```bash
# FFmpegで圧縮
ffmpeg -i temp/loom_video.mp4 -vn -ar 16000 -ac 1 -b:a 64k temp/loom_audio_compressed.mp3
```

スクリプト内の`audio_file_path`を`../temp/loom_audio_compressed.mp3`に変更

### Loomダウンロードができない場合

1. ブラウザで視聴して画面録画
2. OBSなどで音声を録音
3. MP3/MP4で保存

## 完了確認

- [ ] 文字起こしファイル作成済み: `video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md`
- [ ] metadata.json更新済み
- [ ] 完了率が向上（88.0% → 90.0%以上）
- [ ] 一時ファイル削除: `rm -rf temp/`

## 環境確認

```bash
# OpenAI API Key確認
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
cat .env | grep OPENAI_API_KEY
```

キーが設定されていない場合は`.env`ファイルに追加してください。

---

**期待される結果**: 網羅率 99.4% → 99.4%以上（Loom動画1件追加）
**推定所要時間**: 15-30分
**推定コスト**: 約$0.12（Whisper API）
