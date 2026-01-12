import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

audio_file_path = "../temp/loom_audio_compressed.mp3"

print(f"文字起こし開始: {audio_file_path}")

with open(audio_file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="ja",
        response_format="text"
    )

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
