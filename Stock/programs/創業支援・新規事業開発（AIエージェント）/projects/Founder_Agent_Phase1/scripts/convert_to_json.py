#!/usr/bin/env python3
"""
Convert YouTube video list from Markdown to JSON format for transcript extraction.
"""

import re
import json
from pathlib import Path

def parse_video_list(md_file: Path) -> list[dict]:
    """Parse the markdown file and extract video information."""
    videos = []
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Match lines with video URLs
            match = re.match(
                r'^0*(\d+)\.\s+(https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+))\s+#\s+\[([^\]]*)\]\s+(.+)\s+\(https://www\.youtube\.com/channel/([a-zA-Z0-9_-]+)\)$',
                line.strip()
            )
            if match:
                idx, url, video_id, tags, title, channel_id = match.groups()
                videos.append({
                    "index": int(idx),
                    "video_id": video_id,
                    "url": url,
                    "title": title.strip(),
                    "tags": [t.strip() for t in tags.split(',')],
                    "channel_id": channel_id
                })
    return videos

def main():
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1")
    md_file = base_dir / "documents/1_initiating/project_charter_youtube_videos_from_channels_all.md"
    output_file = base_dir / "documents/references/transcripts/extraction_targets.json"
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Parse and save
    videos = parse_video_list(md_file)
    
    result = {
        "generated_at": "2025-12-30T09:10:00+09:00",
        "source": str(md_file),
        "total_count": len(videos),
        "videos": videos
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Extracted {len(videos)} videos to {output_file}")

if __name__ == "__main__":
    main()
