---
name: note-article-automation
description: Note.com記事の作成から投稿までを自動化するオーケストレータースキル。記事生成、AI画像生成、下書き作成、画像アップロード、公開までの全工程を統合制御。
version: 1.0.0
author: aipm_v0
tags:
  - note
  - automation
  - orchestrator
  - content-creation
triggers:
  - note記事自動化
  - Note記事作成
  - note投稿
invocable: true
---

# note-article-automation スキル

Note.com記事の作成から投稿までを自動化するオーケストレータースキル。

## 概要

- **目的**: Note記事の全自動作成・投稿
- **所要時間**: 30〜60分
- **出力**: 公開済み記事URL + 全工程のレポート

## スキル構成

```
note-article-automation (本スキル)
         │
    ┌────┼────┬──────────┬──────────┬──────────┐
    │    │    │          │          │          │
    ▼    ▼    ▼          ▼          ▼          ▼
generate  create  generate  upload   publish  (knowledge)
-article  -draft  -images   -images  -article  algorithm.md
                  (Gemini)                     best_practices.md
```

## 入力パラメータ

| パラメータ | 必須 | 説明 | デフォルト |
|-----------|------|------|-----------|
| `topic` | ○ | 記事のトピック/テーマ | - |
| `target_audience` | △ | ターゲット読者層 | 一般 |
| `tone` | △ | 文体（カジュアル/フォーマル/専門的） | カジュアル |
| `word_count` | △ | 目標文字数 | 3,000 |
| `image_source` | △ | 画像ソース（ai/local/both） | ai |
| `local_images` | △ | ローカル画像パス（リスト） | - |
| `hashtags` | △ | ハッシュタグ（リスト） | 自動生成 |
| `is_paid` | △ | 有料記事にするか | false |
| `price` | △ | 価格（有料の場合） | 100 |
| `auto_publish` | △ | 自動公開するか（false=下書き保存） | false |

## 出力

### ディレクトリ構造

```
Flow/YYYYMM/YYYY-MM-DD/note_article/
├── draft_article.md        # 生成された記事
├── article_metadata.json   # 記事メタデータ
├── draft_info.json         # 下書き情報
├── upload_result.json      # 画像アップロード結果
├── publish_result.json     # 公開結果
├── preview_screenshot.png  # プレビュー画像
└── final_report.md         # 最終レポート
```

### final_report.md 構造

```markdown
# Note記事自動化レポート

## 実行サマリー
- 実行日時: 2026-01-08 12:00
- 所要時間: 35分
- ステータス: 成功

## 記事情報
- タイトル: [記事タイトル]
- 文字数: 3,200文字
- 画像数: 3枚
- URL: https://note.com/username/n/nxxxxxxxxxx

## 工程詳細
| 工程 | ステータス | 所要時間 |
|------|-----------|---------|
| 記事生成 | ✅ 成功 | 8分 |
| 画像生成 | ✅ 成功 | 6分 |
| 下書き作成 | ✅ 成功 | 7分 |
| 画像アップロード | ✅ 成功 | 10分 |
| 公開 | ✅ 成功 | 4分 |

## コスト
- 画像生成: $0.39 (3枚 × $0.13)
- 合計: $0.39
```

## 実行フロー

```
┌─────────────────────────────────────────────────────────────┐
│                    STEP 1: 初期化                           │
│  - 出力ディレクトリ作成                                       │
│  - ナレッジベース読み込み                                     │
│  - パラメータ検証                                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 STEP 2: 記事生成                            │
│  [generate-article スキル]                                  │
│  - SEO最適化記事を生成                                       │
│  - 画像マーカーを配置                                        │
│  出力: draft_article.md, article_metadata.json              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 STEP 3: 画像生成                            │
│  [generate-images スキル]                                   │
│  - 画像マーカーからプロンプト生成                              │
│  - Gemini APIで画像生成                                     │
│  出力: note_images/*.png, image_manifest.json               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 STEP 4: 下書き作成                          │
│  [create-draft スキル]                                      │
│  - Note.comにブラウザでアクセス                               │
│  - タイトル・本文を入力                                       │
│  - 下書きを保存                                              │
│  出力: draft_info.json, draft_url.txt                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               STEP 5: 画像アップロード                       │
│  [upload-images スキル]                                     │
│  - 生成画像を下書きにアップロード                              │
│  - 適切な位置に挿入                                          │
│  出力: upload_result.json                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 STEP 6: 公開                                │
│  [publish-article スキル]                                   │
│  - プレビュー確認                                            │
│  - ユーザー承認                                              │
│  - 公開または下書き保存                                       │
│  出力: publish_result.json, preview_screenshot.png          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 STEP 7: レポート生成                         │
│  - 全工程の結果を統合                                        │
│  - 最終レポートを生成                                        │
│  出力: final_report.md                                      │
└─────────────────────────────────────────────────────────────┘
```

## 実行手順

### STEP 1: 初期化

```python
from datetime import datetime
from pathlib import Path

# 出力ディレクトリ作成
today = datetime.now().strftime("%Y-%m-%d")
month = datetime.now().strftime("%Y%m")
output_dir = Path(f"Flow/{month}/{today}/note_article")
output_dir.mkdir(parents=True, exist_ok=True)

# ナレッジベース読み込み
knowledge_base = {
    "algorithm": read_file("Stock/programs/副業/projects/SNS/knowledge/Note/algorithm.md"),
    "best_practices": read_file("Stock/programs/副業/projects/SNS/knowledge/Note/best_practices.md")
}

# パラメータ検証
validate_params(topic, target_audience, tone, word_count)
```

### STEP 2: 記事生成

```
# generate-article スキルを実行
generate_article(
    topic=topic,
    target_audience=target_audience,
    tone=tone,
    word_count=word_count,
    image_count=3,
    output_dir=output_dir
)

# 出力確認
assert (output_dir / "draft_article.md").exists()
assert (output_dir / "article_metadata.json").exists()
```

### STEP 3: 画像生成

```python
# image_sourceに応じた処理
if image_source == "ai":
    # generate-images スキルを実行
    generate_images(
        article_path=output_dir / "draft_article.md",
        metadata_path=output_dir / "article_metadata.json",
        style="モダン",
        output_dir=output_dir / "note_images"
    )
elif image_source == "local":
    # ローカル画像をコピー
    copy_local_images(local_images, output_dir / "note_images")
elif image_source == "both":
    # AI生成 + ローカル画像を併用
    generate_images(...)
    copy_local_images(...)

# 出力確認
assert (output_dir / "note_images" / "image_manifest.json").exists()
```

### STEP 4: 下書き作成

```
# ブラウザタブ取得
tab_context = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=true)
tab_id = mcp__claude-in-chrome__tabs_create_mcp()

# create-draft スキルを実行
create_draft(
    article_path=output_dir / "draft_article.md",
    tab_id=tab_id
)

# 出力確認
assert (output_dir / "draft_info.json").exists()
draft_url = read_json(output_dir / "draft_info.json")["draft_url"]
```

### STEP 5: 画像アップロード

```
# upload-images スキルを実行
upload_images(
    draft_url=draft_url,
    image_manifest_path=output_dir / "note_images" / "image_manifest.json",
    tab_id=tab_id
)

# 出力確認
assert (output_dir / "upload_result.json").exists()
```

### STEP 6: 公開

```
# publish-article スキルを実行
publish_article(
    draft_url=draft_url,
    tab_id=tab_id,
    hashtags=hashtags,
    is_paid=is_paid,
    price=price
)

# 出力確認
assert (output_dir / "publish_result.json").exists()
```

### STEP 7: レポート生成

```python
# 全工程の結果を集約
results = {
    "article": read_json(output_dir / "article_metadata.json"),
    "images": read_json(output_dir / "note_images" / "image_manifest.json"),
    "draft": read_json(output_dir / "draft_info.json"),
    "upload": read_json(output_dir / "upload_result.json"),
    "publish": read_json(output_dir / "publish_result.json")
}

# 最終レポート生成
generate_final_report(results, output_dir / "final_report.md")
```

## エラーハンドリング

### ステージゲート管理

各STEPの完了を確認し、失敗時は適切に処理：

| STEP | 失敗時の対応 |
|------|------------|
| 記事生成 | リトライ（最大2回）、失敗時は中断 |
| 画像生成 | プレースホルダー画像を使用、または画像なしで続行 |
| 下書き作成 | ログイン状態確認、手動ログイン依頼 |
| 画像アップロード | 失敗画像をスキップ、残りを続行 |
| 公開 | 下書き保存に切り替え |

### リカバリーポイント

中断時のリカバリー用に各STEPで中間状態を保存：

```python
def save_checkpoint(step_name, state):
    checkpoint = {
        "step": step_name,
        "state": state,
        "timestamp": datetime.now().isoformat()
    }
    with open(output_dir / ".checkpoint.json", "w") as f:
        json.dump(checkpoint, f)

def load_checkpoint():
    checkpoint_file = output_dir / ".checkpoint.json"
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            return json.load(f)
    return None
```

## 使用例

### 基本的な使用（AIで画像自動生成）

```
/note-article-automation
トピック: AIを活用した副業の始め方
ターゲット: 会社員、30〜40代
文体: カジュアル
```

### ローカル画像を使用

```
/note-article-automation
トピック: プログラミング学習の始め方
画像ソース: local
ローカル画像:
  - /path/to/image1.png
  - /path/to/image2.png
  - /path/to/image3.png
```

### 有料記事として公開

```
/note-article-automation
トピック: 投資初心者向け完全ガイド
有料: true
価格: 500
```

## コスト見積もり

| 項目 | コスト |
|------|--------|
| 画像生成（3枚） | $0.39 |
| 画像生成（5枚） | $0.65 |
| LLM推論 | Claude Code使用量に含む |
| **合計（3枚）** | **約$0.39** |

## 成功基準

- ✅ 2,000〜5,000文字の記事が生成される
- ✅ 3〜5枚の画像が正しい位置に挿入される
- ✅ 30〜60分以内に全工程が完了
- ✅ 公開された記事URLが取得できる

## 注意事項

1. **事前準備**: Note.comにブラウザでログイン済みであること
2. **API設定**: Gemini APIキーが環境変数に設定されていること
3. **連続実行**: 複数記事を連続投稿する場合は5分以上間隔を空ける
4. **承認フロー**: 公開前に必ずユーザー確認を行う

## 参照

- `generate-article/SKILL.md` - 記事生成スキル
- `generate-images/SKILL.md` - AI画像生成スキル
- `create-draft/SKILL.md` - 下書き作成スキル
- `upload-images/SKILL.md` - 画像アップロードスキル
- `publish-article/SKILL.md` - 投稿実行スキル
- `create-draft/selectors.json` - UI要素セレクタ
- `Stock/programs/副業/projects/SNS/knowledge/Note/algorithm.md` - Noteアルゴリズム
- `Stock/programs/副業/projects/SNS/knowledge/Note/best_practices.md` - Noteベストプラクティス
