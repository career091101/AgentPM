
import os
import re

def clean_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    seen = set()
    
    for line in lines:
        line = line.strip()
        # Skip headers, timestamps, and empty lines
        if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:') or '-->' in line or not line:
            continue
        # Remove tags like <c>...</c>
        line = re.sub(r'<[^>]+>', '', line)
        # Skip duplicates (common in auto-subs)
        if line in seen:
            continue
        seen.add(line)
        cleaned_lines.append(line)
    
    return cleaned_lines

def main():
    directory = "/Users/yuichi/AIPM/aipm_v0/Flow/YouTube_Transcripts"
    output_file = "/Users/yuichi/AIPM/aipm_v0/Flow/YouTube_Transcripts/Note_YouTube_Transcripts.md"
    
    # Video IDs in order
    videos = [
        {"id": "mcQw-nvjThs", "title": "Main Video"},
        {"id": "OsiAx4-wll8", "title": "Additional Video 1"},
        {"id": "Pmyk5vY6A0A", "title": "Additional Video 2"},
        {"id": "AJv_MemNRdA", "title": "Additional Video 3"},
        {"id": "kgBW-RT01Nk", "title": "Additional Video 4"},
        {"id": "I-73fguAXTg", "title": "Additional Video 5"}
    ]
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# Note YouTube Transcripts\n\n")
        
        for video in videos:
            vtt_file = os.path.join(directory, f"{video['id']}.ja.vtt")
            if os.path.exists(vtt_file):
                print(f"Processing {video['id']}...")
                transcript = clean_vtt(vtt_file)
                outfile.write(f"## {video['title']} (ID: {video['id']})\n")
                outfile.write(f"URL: https://www.youtube.com/watch?v={video['id']}\n\n")
                outfile.write("\n".join(transcript))
                outfile.write("\n\n---\n\n")
            else:
                print(f"File not found: {vtt_file}")
                # Try finding any file with the ID if extension varies
                found = False
                for f in os.listdir(directory):
                    if video['id'] in f and f.endswith('.vtt'):
                         print(f"Found alternative: {f}")
                         transcript = clean_vtt(os.path.join(directory, f))
                         outfile.write(f"## {video['title']} (ID: {video['id']})\n")
                         outfile.write(f"URL: https://www.youtube.com/watch?v={video['id']}\n\n")
                         outfile.write("\n".join(transcript))
                         outfile.write("\n\n---\n\n")
                         found = True
                         break
                if not found:
                    outfile.write(f"## {video['title']} (ID: {video['id']})\n")
                    outfile.write("Transcription not available.\n\n---\n\n")

if __name__ == "__main__":
    main()
