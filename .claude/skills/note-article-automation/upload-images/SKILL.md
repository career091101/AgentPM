---
name: upload-images
description: 生成された画像をNote.comの下書きにアップロードするスキル。Claude in Chrome MCPのupload_imageツールを使用し、記事内の適切な位置に画像を挿入。
version: 1.0.0
author: aipm_v0
tags:
  - note
  - image-upload
  - browser-automation
  - claude-in-chrome
triggers:
  - note画像アップロード
  - Note画像挿入
invocable: false
---

# upload-images スキル

生成された画像をNote.comの下書きにアップロードするスキル。

## 概要

- **目的**: 記事に画像を挿入
- **方式**: Claude in Chrome MCP（`upload_image`ツール）
- **対応画像**: PNG, JPG, GIF（最大5MB）

## 入力パラメータ

| パラメータ | 必須 | 説明 | デフォルト |
|-----------|------|------|-----------|
| `draft_url` | ○ | 下書きURL | - |
| `image_manifest_path` | ○ | 画像マニフェストJSONパス | - |
| `tab_id` | ○ | ブラウザタブID | - |

## 出力

### ファイル出力

```
Flow/YYYYMM/YYYY-MM-DD/note_article/
└── upload_result.json      # アップロード結果
```

### upload_result.json 構造

```json
{
  "completed_at": "2026-01-08T12:00:00+09:00",
  "total_images": 3,
  "successful_uploads": 3,
  "failed_uploads": 0,
  "uploads": [
    {
      "image_id": "image_001",
      "filename": "image_001.png",
      "status": "success",
      "position": 1,
      "upload_time": "2026-01-08T12:01:00+09:00"
    }
  ]
}
```

## 実行手順

### STEP 1: 下書きページに移動

下書き編集ページに移動：

```
mcp__claude-in-chrome__navigate(
  tabId=<tab_id>,
  url="<draft_url>"
)

# ページ読み込み待機
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="wait",
  duration=3
)
```

### STEP 2: 画像マニフェスト読み込み

アップロードする画像情報を取得：

```python
import json

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

images = manifest["images"]
```

### STEP 3: 画像挿入位置の特定

本文エディタ内で画像を挿入する位置を特定：

**方式A: 段落末尾への挿入**

```
# エディタの構造を取得
mcp__claude-in-chrome__read_page(
  tabId=<tab_id>,
  filter="interactive"
)

# 本文エディタを特定
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="本文入力エリア"
)
```

**方式B: 特定位置への挿入（座標指定）**

1. スクリーンショットで視覚的に位置を確認
2. エディタ内の適切な位置の座標を取得
3. `upload_image`で座標指定アップロード

### STEP 4: 画像アップロード実行

各画像をアップロード：

**upload_imageツールの使用方法**:

```
# 方式1: ref指定（ファイル入力要素）
mcp__claude-in-chrome__upload_image(
  tabId=<tab_id>,
  imageId="<screenshot_id または user_upload_id>",
  ref="<file_input_ref>",
  filename="image_001.png"
)

# 方式2: coordinate指定（ドラッグ&ドロップ）
mcp__claude-in-chrome__upload_image(
  tabId=<tab_id>,
  imageId="<screenshot_id>",
  coordinate=[x, y],
  filename="image_001.png"
)
```

**重要**: `imageId`は以下のいずれかが必要：
1. `mcp__claude-in-chrome__computer`の`screenshot`アクションで取得したID
2. ユーザーがアップロードした画像のID

### STEP 5: ローカル画像のアップロード準備

ローカルファイルをupload_imageで使用するための準備：

**方式1: スクリーンショット経由**

ローカル画像をブラウザで開いてスクリーンショットを取得：

```
# 画像ファイルをブラウザで開く
mcp__claude-in-chrome__navigate(
  tabId=<tab_id>,
  url="file:///path/to/image_001.png"
)

# スクリーンショット取得
screenshot_result = mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="screenshot"
)

# screenshot_resultからimageIdを取得
image_id = screenshot_result["imageId"]
```

**方式2: ファイル入力使用**

Note.comの画像アップロード機能を使用：

```
# 画像アップロードボタンをクリック
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="画像アップロードボタン"
)

mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<upload_button_ref>"
)

# ファイル選択ダイアログが開く
# → Bashツールでファイルパスを入力（OS依存）
```

### STEP 6: 各画像の挿入

画像を順番にアップロード：

```python
upload_results = []

for i, image_info in enumerate(images):
    image_path = image_info["path"]
    position = image_info["position_in_article"]

    try:
        # 1. エディタ内の挿入位置にカーソルを移動
        move_to_insertion_point(tab_id, position)

        # 2. 画像アップロードボタンをクリック
        click_upload_button(tab_id)

        # 3. 画像ファイルをアップロード
        result = upload_image_file(tab_id, image_path)

        # 4. アップロード完了を待機
        wait_for_upload(tab_id)

        upload_results.append({
            "image_id": image_info["id"],
            "filename": image_info["filename"],
            "status": "success",
            "position": position,
            "upload_time": datetime.now().isoformat()
        })

    except Exception as e:
        upload_results.append({
            "image_id": image_info["id"],
            "filename": image_info["filename"],
            "status": "failed",
            "error": str(e),
            "position": position
        })

        # エラー時はスキップして次の画像へ
        continue
```

### STEP 7: 下書き更新保存

すべての画像アップロード後、下書きを保存：

```
# 下書き更新ボタンをクリック
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="下書き保存ボタン"
)

mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<save_button_ref>"
)

# 保存完了を待機
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="wait",
  duration=3
)
```

### STEP 8: 結果出力

アップロード結果をファイルに保存：

```python
import json

result = {
    "completed_at": datetime.now().isoformat(),
    "total_images": len(images),
    "successful_uploads": len([r for r in upload_results if r["status"] == "success"]),
    "failed_uploads": len([r for r in upload_results if r["status"] == "failed"]),
    "uploads": upload_results
}

with open(output_path / "upload_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

## 画像挿入位置の決定ロジック

記事内の適切な位置に画像を挿入：

| 画像位置 | 挿入場所 |
|---------|---------|
| 1（アイキャッチ） | リード文直後 |
| 2 | セクション1の末尾 |
| 3 | セクション3の末尾 |
| 4+ | 対応するセクションの末尾 |

**位置特定の実装**:

```python
def find_insertion_point(editor_content, position):
    """
    画像の挿入位置を特定

    Args:
        editor_content: エディタのDOM構造
        position: 画像の位置番号（1〜）

    Returns:
        挿入位置の座標またはref
    """
    # H2見出しを数えて対応する位置を特定
    headings = find_all_h2_headings(editor_content)

    if position == 1:
        # アイキャッチ: 最初のH2の前
        return headings[0]["before_coordinate"]
    elif position <= len(headings):
        # 対応するセクションの末尾
        return headings[position - 1]["after_coordinate"]
    else:
        # 末尾
        return get_editor_end_coordinate()
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| 画像ファイルが見つからない | 警告を出してスキップ |
| アップロードタイムアウト | リトライ（最大2回） |
| ファイルサイズ超過 | 圧縮を試みる、または警告 |
| エディタ要素が見つからない | スクリーンショット保存、手動対応依頼 |

**リトライロジック**:

```python
def upload_with_retry(tab_id, image_path, max_retries=2):
    for attempt in range(max_retries):
        try:
            result = perform_upload(tab_id, image_path)
            return result
        except TimeoutError:
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            raise
```

## 注意事項

1. **ファイルサイズ**: 最大5MB、超過時は圧縮が必要
2. **対応形式**: PNG, JPG, GIF
3. **アップロード間隔**: 各画像間に1秒以上の間隔を推奨
4. **DOM変更**: Note.comのUI更新時は要動作確認

## 参照

- `../create-draft/selectors.json` - UI要素セレクタ
- `../generate-images/SKILL.md` - 画像生成スキル

## 次のスキル

このスキルの出力は以下のスキルで使用：

- `publish-article`: 画像付き下書きを公開
