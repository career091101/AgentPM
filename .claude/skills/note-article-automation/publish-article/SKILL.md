---
name: publish-article
description: Note.comの下書きを公開するスキル。プレビュー確認、ユーザー承認を経て公開または下書き保存を実行。
version: 1.0.0
author: aipm_v0
tags:
  - note
  - publish
  - browser-automation
  - claude-in-chrome
triggers:
  - note記事公開
  - Note公開
invocable: false
---

# publish-article スキル

Note.comの下書きを公開するスキル。

## 概要

- **目的**: 下書きをプレビュー確認後に公開
- **方式**: Claude in Chrome MCP（ブラウザ自動化）
- **ユーザー承認**: 公開前に必ずユーザー確認

## 入力パラメータ

| パラメータ | 必須 | 説明 | デフォルト |
|-----------|------|------|-----------|
| `draft_url` | ○ | 下書きURL | - |
| `tab_id` | ○ | ブラウザタブID | - |
| `hashtags` | △ | ハッシュタグ（カンマ区切り） | - |
| `is_paid` | △ | 有料記事にするか | false |
| `price` | △ | 価格（有料の場合） | 100 |

## 出力

### ファイル出力

```
Flow/YYYYMM/YYYY-MM-DD/note_article/
├── preview_screenshot.png  # プレビュー画像
└── publish_result.json     # 公開結果
```

### publish_result.json 構造

```json
{
  "published_at": "2026-01-08T12:00:00+09:00",
  "status": "published",
  "article_url": "https://note.com/username/n/nxxxxxxxxxx",
  "title": "記事タイトル",
  "is_paid": false,
  "price": null,
  "hashtags": ["AI", "副業", "自動化"]
}
```

## 実行手順

### STEP 1: 下書きページに移動

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

### STEP 2: プレビュー表示

プレビューモードで記事を確認：

```
# プレビューボタンをクリック
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="プレビューボタン"
)

mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<preview_button_ref>"
)

# プレビュー読み込み待機
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="wait",
  duration=2
)
```

### STEP 3: プレビュースクリーンショット取得

ユーザー確認用のスクリーンショットを取得：

```
# プレビュー画面のスクリーンショット
screenshot_result = mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="screenshot"
)

# スクリーンショットを保存（imageIdを記録）
preview_image_id = screenshot_result["imageId"]
```

### STEP 4: ユーザー承認

AskUserQuestionでユーザーに公開可否を確認：

```
AskUserQuestion:
  質問: "以下の記事を公開しますか？"

  # プレビュースクリーンショットを表示
  [プレビュー画像を添付]

  選択肢:
    - 公開する: 記事を公開
    - 下書き保存: 公開せず下書きのまま保存
    - 編集する: 内容を修正（中断）
```

**ユーザー応答による分岐**:

| 応答 | アクション |
|------|-----------|
| 公開する | STEP 5へ進む |
| 下書き保存 | 下書き保存してSTEP 8へ |
| 編集する | 処理中断、draft_urlを返す |

### STEP 5: 公開設定画面へ移動

公開ボタンをクリックして設定画面を表示：

```
# 公開ボタンをクリック
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="公開ボタン"
)

mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<publish_button_ref>"
)

# 設定画面読み込み待機
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="wait",
  duration=2
)
```

### STEP 6: 公開設定入力

ハッシュタグ、価格などを設定：

**ハッシュタグ入力**:

```
# ハッシュタグ入力欄を検索
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="ハッシュタグ入力"
)

# 各タグを入力
for tag in hashtags:
    mcp__claude-in-chrome__form_input(
      tabId=<tab_id>,
      ref="<hashtag_input_ref>",
      value=tag
    )

    # Enterで確定
    mcp__claude-in-chrome__computer(
      tabId=<tab_id>,
      action="key",
      text="Enter"
    )
```

**有料設定（オプション）**:

```
if is_paid:
    # 有料記事トグルをON
    mcp__claude-in-chrome__find(
      tabId=<tab_id>,
      query="有料設定"
    )

    mcp__claude-in-chrome__computer(
      tabId=<tab_id>,
      action="left_click",
      ref="<paid_toggle_ref>"
    )

    # 価格入力
    mcp__claude-in-chrome__form_input(
      tabId=<tab_id>,
      ref="<price_input_ref>",
      value=price
    )
```

### STEP 7: 公開実行

最終確認ボタンをクリックして公開：

```
# 公開確定ボタンをクリック
mcp__claude-in-chrome__find(
  tabId=<tab_id>,
  query="公開確定ボタン"
)

mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="left_click",
  ref="<confirm_publish_ref>"
)

# 公開完了待機
mcp__claude-in-chrome__computer(
  tabId=<tab_id>,
  action="wait",
  duration=5
)
```

### STEP 8: 公開URL取得

公開された記事のURLを取得：

```
# 現在のURLを取得
article_url = mcp__claude-in-chrome__javascript_tool(
  tabId=<tab_id>,
  action="javascript_exec",
  text="window.location.href"
)
```

### STEP 9: 結果出力

公開結果をファイルに保存：

```python
import json

result = {
    "published_at": datetime.now().isoformat(),
    "status": "published",  # or "draft_saved", "cancelled"
    "article_url": article_url,
    "title": title,
    "is_paid": is_paid,
    "price": price if is_paid else None,
    "hashtags": hashtags
}

with open(output_path / "publish_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

## ユーザー承認フロー

```
         ┌─────────────────────────┐
         │ プレビュースクリーンショット取得 │
         └───────────┬─────────────┘
                     ▼
         ┌─────────────────────────┐
         │   AskUserQuestion       │
         │   「公開しますか？」      │
         └───────────┬─────────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  ┌───────┐    ┌──────────┐   ┌─────────┐
  │ 公開  │    │ 下書き保存 │   │ 編集する │
  └───┬───┘    └─────┬────┘   └────┬────┘
      │              │             │
      ▼              ▼             ▼
  公開設定入力    下書き保存      処理中断
      │              │        draft_url返却
      ▼              │
  公開実行           │
      │              │
      ▼              ▼
  結果出力        結果出力
```

## 公開時間の最適化

Noteのアルゴリズムに基づく最適公開時間：

| 時間帯 | 推奨度 | 理由 |
|--------|--------|------|
| 19:00-22:00 | ★★★ | ゴールデンタイム、最も閲覧が多い |
| 12:00-13:00 | ★★☆ | 昼休み、モバイル閲覧が増加 |
| 7:00-9:00 | ★★☆ | 通勤時間、ニュース的コンテンツに有効 |
| 22:00-24:00 | ★☆☆ | 深夜帯、特定ジャンル向け |

**実装での考慮**:

```python
from datetime import datetime

def is_optimal_publish_time():
    """公開に最適な時間かチェック"""
    hour = datetime.now().hour

    if 19 <= hour <= 22:
        return True, "ゴールデンタイム"
    elif 12 <= hour <= 13:
        return True, "昼休み時間"
    elif 7 <= hour <= 9:
        return True, "通勤時間"
    else:
        return False, f"現在{hour}時です。19-22時の公開を推奨します。"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| プレビュー表示失敗 | リトライ、失敗時は直接公開設定へ |
| 公開設定画面が開かない | スクリーンショット保存、手動対応依頼 |
| ネットワークエラー | リトライ（最大3回） |
| 公開失敗 | エラーメッセージ取得、ログに記録 |

## 注意事項

1. **公開前確認**: 必ずユーザー承認を得る
2. **連続投稿**: 最低5分間隔を空ける
3. **有料記事**: 価格設定は慎重に（後から変更可能）
4. **タイミング**: 19-22時の公開を推奨

## セキュリティ考慮事項

1. **承認フロー**: 公開は必ずユーザー確認後
2. **スクリーンショット**: プレビュー画像は一時保存のみ
3. **価格情報**: ログには記録しない

## 参照

- `../create-draft/selectors.json` - UI要素セレクタ
- `Stock/programs/副業/projects/SNS/knowledge/Note/algorithm.md` - 公開時間の最適化

## 完了後の次ステップ

公開完了後、オーケストレーターが以下を実行：

1. 公開結果のサマリー生成
2. SNS連携（オプション）
3. 分析用データ記録
