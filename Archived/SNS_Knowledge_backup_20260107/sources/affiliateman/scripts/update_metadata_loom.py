import json

metadata_path = "../metadata.json"

with open(metadata_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for video in data["videos"]:
    if "loom.com" in video.get("url", "") and "インスタマネタイズ最新2025年" in video.get("title", ""):
        video["has_transcript"] = True
        video["transcript_file"] = "video_transcripts/instagram_strategy/インスタマネタイズ最新2025年.md"
        video["method"] = "whisper"
        print(f"✅ 更新: {video['title']}")
        break

stats = data.get("video_stats", {})
stats["with_transcript"] = stats.get("with_transcript", 44) + 1
stats["without_transcript"] = max(0, stats.get("without_transcript", 6) - 1)
stats["completion_rate"] = f"{(stats['with_transcript'] / stats.get('total_videos', 50) * 100):.1f}%"
data["video_stats"] = stats

with open(metadata_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ metadata.json更新完了")
print(f"完了率: {stats['completion_rate']}")
print(f"文字起こし済み: {stats['with_transcript']}/{stats['total_videos']}")
