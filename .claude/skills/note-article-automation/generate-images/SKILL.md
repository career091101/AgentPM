---
name: generate-images
description: 記事内の画像マーカーからAI画像を自動生成するスキル。Gemini 3 Pro Image APIを使用し、Note記事に最適化された画像を生成。
version: 1.0.0
author: aipm_v0
tags:
  - note
  - image-generation
  - gemini-api
  - ai
triggers:
  - note画像生成
  - AI画像生成
invocable: false
---

# generate-images スキル

記事内の画像マーカーからAI画像を自動生成するスキル。

## 概要

- **目的**: Note記事用のAI画像を自動生成
- **API**: Gemini 3 Pro Image API
- **出力**: 1200x800px PNG画像（3〜5枚）
- **コスト**: 約$0.13/枚

## 入力パラメータ

| パラメータ | 必須 | 説明 | デフォルト |
|-----------|------|------|-----------|
| `article_path` | ○ | 記事ファイルパス（画像マーカー含む） | - |
| `metadata_path` | △ | メタデータJSONパス | - |
| `style` | △ | 画像スタイル（モダン/イラスト/写真風） | モダン |
| `color_scheme` | △ | カラースキーム | 自動 |
| `output_dir` | △ | 出力ディレクトリ | Flow/YYYYMM/YYYY-MM-DD/note_images/ |

## 出力

### ファイル出力

```
Flow/YYYYMM/YYYY-MM-DD/note_images/
├── image_001.png           # 生成画像1
├── image_002.png           # 生成画像2
├── image_003.png           # 生成画像3
└── image_manifest.json     # 画像マニフェスト
```

### image_manifest.json 構造

```json
{
  "generated_at": "2026-01-08T12:00:00+09:00",
  "total_images": 3,
  "total_cost_usd": 0.39,
  "images": [
    {
      "id": "image_001",
      "filename": "image_001.png",
      "path": "Flow/202601/2026-01-08/note_images/image_001.png",
      "marker_description": "AIを活用したビジネス効率化のイメージ図",
      "prompt": "Modern business efficiency illustration...",
      "dimensions": "1200x800",
      "format": "PNG",
      "position_in_article": 1
    }
  ]
}
```

## 実行手順

### STEP 1: 画像マーカー抽出

記事ファイルから画像マーカーを抽出：

```python
import re

def extract_image_markers(article_content):
    pattern = r'<!--IMAGE:(.+?)-->'
    markers = re.findall(pattern, article_content)
    return markers
```

**抽出例**:
```
入力: <!--IMAGE:AIを活用したビジネス効率化のイメージ図-->
出力: "AIを活用したビジネス効率化のイメージ図"
```

### STEP 2: プロンプト生成

各マーカーの説明文からGemini API用のプロンプトを生成：

**プロンプトテンプレート**:

```
Generate a modern, professional illustration for a Japanese blog article.

Subject: {marker_description}
Style: {style}
Dimensions: 1200x800 pixels
Requirements:
- Clean, minimalist design
- Professional appearance suitable for business/tech blog
- No text or watermarks
- High contrast for readability
- Japanese aesthetic sensibility
- {additional_requirements}

Color scheme: {color_scheme}
```

**スタイル別設定**:

| スタイル | 追加要件 |
|---------|---------|
| モダン | Flat design, geometric shapes, gradient backgrounds |
| イラスト | Hand-drawn style, warm colors, friendly appearance |
| 写真風 | Photorealistic, professional lighting, depth of field |

### STEP 3: Gemini API呼び出し

**API設定**:

```python
import google.generativeai as genai
import os

# API設定
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# モデル選択
model = genai.GenerativeModel("gemini-2.0-flash-exp")  # 画像生成対応モデル

# 画像生成
response = model.generate_content(
    prompt,
    generation_config={
        "response_mime_type": "image/png",
    }
)
```

**環境変数**:
- `GEMINI_API_KEY`: Gemini APIキー（必須）

**コスト見積もり**:
- 1画像あたり: 約$0.13
- 3画像生成: 約$0.39
- 5画像生成: 約$0.65

### STEP 4: 画像保存

生成された画像を保存：

```python
from pathlib import Path
from datetime import datetime

def save_image(image_data, output_dir, index):
    # 出力ディレクトリ作成
    today = datetime.now().strftime("%Y-%m-%d")
    month = datetime.now().strftime("%Y%m")
    output_path = Path(f"Flow/{month}/{today}/note_images")
    output_path.mkdir(parents=True, exist_ok=True)

    # 画像保存
    filename = f"image_{index:03d}.png"
    filepath = output_path / filename

    with open(filepath, "wb") as f:
        f.write(image_data)

    return str(filepath)
```

### STEP 5: マニフェスト生成

画像情報をまとめたマニフェストファイルを生成：

```python
import json

manifest = {
    "generated_at": datetime.now().isoformat(),
    "total_images": len(images),
    "total_cost_usd": len(images) * 0.13,
    "images": [
        {
            "id": f"image_{i:03d}",
            "filename": f"image_{i:03d}.png",
            "path": str(path),
            "marker_description": marker,
            "prompt": prompt,
            "dimensions": "1200x800",
            "format": "PNG",
            "position_in_article": i
        }
        for i, (path, marker, prompt) in enumerate(zip(paths, markers, prompts), 1)
    ]
}

with open(output_dir / "image_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
```

## 画像仕様

| 項目 | 値 |
|------|-----|
| 解像度 | 1200x800px |
| フォーマット | PNG |
| カラーモード | RGB |
| 最大ファイルサイズ | 5MB |

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| APIキー未設定 | 環境変数の設定を促す |
| API呼び出し失敗 | 最大3回リトライ |
| 画像生成失敗 | プレースホルダー画像を使用、ログに記録 |
| ディスク容量不足 | 警告を出して処理中断 |

**リトライロジック**:

```python
import time

def generate_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.image
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # 指数バックオフ
                continue
            raise e
```

## 代替手段（API失敗時）

Gemini API失敗時の代替手段：

1. **プレースホルダー画像**: グレーの画像に説明テキストを配置
2. **手動アップロード指示**: ユーザーに手動アップロードを依頼
3. **スキップ**: 画像なしで記事を投稿

## 使用例

### 基本的な使用

```
記事パス: Flow/202601/2026-01-08/note_article/draft_article.md
スタイル: モダン
出力先: Flow/202601/2026-01-08/note_images/
```

### コマンドライン実行（将来的）

```bash
python generate_images.py \
  --article Flow/202601/2026-01-08/note_article/draft_article.md \
  --style modern \
  --output Flow/202601/2026-01-08/note_images/
```

## 注意事項

1. **APIコスト**: 1画像$0.13、大量生成時は注意
2. **著作権**: 生成画像はGeminiの利用規約に従う
3. **品質**: 複雑な図表は手動作成を推奨
4. **レート制限**: API制限に注意（必要に応じて間隔を空ける）

## 参照

- `.claude/skills/generate-linkedin-image/SKILL.md` - 画像生成スキル参考
- [Gemini API Documentation](https://ai.google.dev/docs)

## 次のスキル

このスキルの出力は以下のスキルで使用：

- `upload-images`: 生成画像をNote.comにアップロード
