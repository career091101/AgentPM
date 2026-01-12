---
name: create-draft
description: Claude in Chrome MCPを使用してNote.comに記事の下書きを作成するスキル。Cookie認証でログイン状態を維持し、タイトル・本文を自動入力。
version: 1.0.0
author: aipm_v0
tags:
  - note
  - browser-automation
  - claude-in-chrome
  - draft
triggers:
  - note下書き作成
  - Note下書き
invocable: false
---

# create-draft スキル

Claude in Chrome MCPを使用してNote.comに下書きを作成するスキル。

## 概要

- **目的**: Note.comに記事の下書きを自動作成
- **方式**: Claude in Chrome MCP（ブラウザ自動化）
- **認証**: Cookie認証（事前ログイン必須）

## 前提条件

1. **Claude in Chrome拡張機能**がインストール済み
2. **Note.comにログイン済み**（ブラウザでCookie認証が有効）
3. **MCPサーバー**が起動済み

## 入力パラメータ

| パラメータ | 必須 | 説明 | デフォルト |
|-----------|------|------|-----------|
| `article_path` | ○ | 記事ファイルパス | - |
| `title` | △ | 記事タイトル（記事から抽出も可） | - |

## 出力

### ファイル出力

```
Flow/YYYYMM/YYYY-MM-DD/note_article/
├── draft_url.txt           # 下書きURL
└── draft_info.json         # 下書き情報
```

### draft_info.json 構造

```json
{
  "draft_url": "https://note.com/api/v2/drafts/xxxxx",
  "draft_id": "xxxxx",
  "title": "記事タイトル",
  "created_at": "2026-01-08T12:00:00+09:00",
  "status": "draft"
}
```

## 実行手順

### STEP 1: タブコンテキスト取得

Claude in Chrome MCPのタブコンテキストを取得：

```
mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=true)
```

**重要**:
- 既存タブがある場合は再利用可能
- 新規作成時は `createIfEmpty=true` を指定

### STEP 2: Note.comにナビゲート

新しいタブを作成し、Note.comの新規投稿ページに移動：

```
# 新規タブ作成
mcp__claude-in-chrome__tabs_create_mcp()

# Note.comの投稿ページに移動
mcp__claude-in-chrome__navigate(
  tabId=<tab_id>,
  url="https://note.com/new"
)
```

### STEP 3: ログイン状態確認

Cookie認証が有効か確認：

```
# ページ構造を取得
mcp__claude-in-chrome__read_page(tabId=<tab_id>)

# ログインページにリダイレクトされた場合
→ ユーザーに手動ログインを依頼
```

**ログイン判定**:
- 投稿フォームが表示されれば認証済み
- ログインフォームが表示されれば未認証

**未認証時の対応**:
```
AskUserQuestion:
  質問: "Note.comにログインしていません。ブラウザでログインしてから続行してください。ログイン完了後、'続行'と入力してください。"
  選択肢: ["続行", "キャンセル"]
```

### STEP 4: 記事内容の準備

記事ファイルを読み込み、画像マーカーを除去：

```python
import re

def prepare_content(article_content):
    # 画像マーカーを除去（後でupload-imagesで処理）
    content = re.sub(r'<!--IMAGE:.+?-->\n?', '', article_content)

    # タイトルを抽出（#で始まる最初の行）
    title_match = re.match(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    # タイトル行を除去
    body = re.sub(r'^#\s+.+\n?', '', content, count=1)

    return title, body.strip()
```

### STEP 5: タイトル入力

タイトルフィールドを見つけて入力：

```
# タイトル入力欄を検索
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="記事タイトル入力欄"
)

# または直接セレクタで指定（selectors.json参照）
mcp__claude-in-chrome__form_input(
  tabId=<tab_id>,
  ref="<title_input_ref>",
  value="<article_title>"
)
```

### STEP 6: 本文入力

本文エディタに記事内容を入力：

```
# 本文入力欄を検索
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="本文入力エリア"
)

# エディタにフォーカス
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<editor_ref>"
)

# 本文を入力（段落ごとに入力推奨）
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="type",
  text="<article_body>"
)
```

**長文入力の注意**:
- 一度に入力する文字数は1000文字以下を推奨
- 段落ごとに分割して入力
- 各入力後に少し待機（0.5秒）

### STEP 7: 下書き保存

下書きを保存して情報を取得：

```
# 下書き保存ボタンをクリック
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

### STEP 8: 下書き情報取得

現在のURLから下書きIDを取得：

```
# 現在のページURLを取得
mcp__claude-in-chrome__javascript_tool(
  tabId=<tab_id>,
  action="javascript_exec",
  text="window.location.href"
)

# URLから下書きIDを抽出
# 例: https://note.com/draft/xxxxx → xxxxx
```

### STEP 9: 結果出力

下書き情報をファイルに保存：

```python
import json
from datetime import datetime

draft_info = {
    "draft_url": draft_url,
    "draft_id": draft_id,
    "title": title,
    "created_at": datetime.now().isoformat(),
    "status": "draft"
}

with open(output_path / "draft_info.json", "w", encoding="utf-8") as f:
    json.dump(draft_info, f, ensure_ascii=False, indent=2)

with open(output_path / "draft_url.txt", "w") as f:
    f.write(draft_url)
```

## UI要素セレクタ

詳細は `selectors.json` を参照。Note.comのUI変更に応じて更新が必要。

**主要セレクタ**:

| 要素 | セレクタ候補 |
|------|------------|
| タイトル入力 | `input[placeholder*="タイトル"]`, `.note-title-input` |
| 本文エディタ | `.ProseMirror`, `[contenteditable="true"]` |
| 下書き保存 | `button:contains("下書き")`, `.save-draft-button` |
| 公開ボタン | `button:contains("公開")`, `.publish-button` |

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| ログイン未完了 | ユーザーに手動ログインを依頼 |
| 要素が見つからない | スクリーンショット保存、セレクタ更新を促す |
| タイムアウト | リトライ（最大2回） |
| 入力失敗 | 段落分割して再入力 |

**エラー発生時のスクリーンショット保存**:

```
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="screenshot"
)

# スクリーンショットをエラーログと共に保存
# Flow/YYYYMM/YYYY-MM-DD/note_article/error_screenshot.png
```

## 注意事項

1. **Cookie期限**: 定期的にログイン状態を確認
2. **UI変更**: Note.comのUI更新時はセレクタ更新が必要
3. **レート制限**: 連続投稿は避ける（最低5分間隔推奨）
4. **プライバシー**: ログイン情報は保存しない

## セキュリティ考慮事項

1. **認証情報**: パスワードは入力しない（Cookie認証のみ）
2. **個人情報**: 記事内容以外のデータは収集しない
3. **エラーログ**: 認証トークンなどは記録しない

## 参照

- `selectors.json` - UI要素セレクタ定義
- `.claude/skills/approve-and-schedule/SKILL.md` - Claude in Chrome参考実装

## 次のスキル

このスキルの出力は以下のスキルで使用：

- `upload-images`: 下書きに画像をアップロード
- `publish-article`: 下書きを公開
