# Sources - ソース別管理

このディレクトリには、ソース別に整理されたトランスクリプトファイルを格納します。

## ディレクトリ構造

- **Founder_Agent_Videos/** - Founder Agent Phase1プロジェクトで収集した469本のYouTube動画トランスクリプト

## ファイル形式

全てのトランスクリプトファイルは以下のYAML frontmatter付きMarkdown形式：

```markdown
---
video_url: "https://www.youtube.com/watch?v=XXXXX"
video_id: "XXXXX"
title: "[動画タイトル]"
speaker: "[話者名]"
channel: "[チャンネル名]"
date: "YYYY-MM-DD"
topic_tags:
  - "#GenAI"
  - "#Startup"
summary: |
  [要約]
key_points:
  - "[キーポイント1]"
technologies_mentioned:
  - "OpenAI GPT-4"
use_cases:
  - "スタートアップ支援"
source: "Founder_Agent_Videos"
---

# Transcript: [video_id]

- URL: https://www.youtube.com/watch?v=[video_id]
- Retrieved at: [ISO 8601 timestamp]

## Text

- [HH:MM] [トランスクリプトテキスト]
...
```

## 参照方法

- カテゴリ別フォルダ（topics/, technologies/, use_cases/, speakers/）には、このディレクトリ内のファイルへのシンボリックリンクが配置されます
- 実ファイルはこのsources/ディレクトリに維持されます

---

**管理者**: Founder Agent System
**最終更新**: 2025-12-30
