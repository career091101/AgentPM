---
name: approve-and-schedule
description: |
  Slack承認 + Late API投稿スケジューリングスキル。
  投稿3案をSlackで承認し、Late API経由で自動投稿。

  処理内容:
  - Slack承認フロー（インタラクティブボタン）
  - Late API投稿（LinkedIn, X, Facebook, Threads）
  - プラットフォーム別最適化
  - スレッド分割（X/Threads）
  - スケジュール時間設定

  所要時間: 5-10分
  出力: posted_status_{date}.json

trigger_keywords:
  - "承認と投稿"
  - "approve-and-schedule"
  - "Slack承認"

stage: Phase 4
dependencies:
  - generate-sns-posts (posts_generated_{date}.json)

output_file: Stock/programs/副業/projects/SNS/data/posted_status_{date}.json
execution_time: 5-10分
priority: P0
model: claude-haiku-4-5-20251001  # Haiku 4.5 (2026年1月時点の最新モデル)
---

# Approve and Schedule Skill - Phase 4

Slack承認 + Late API投稿スケジューリングスキル。

**Version**: 1.0

---

## このSkillでできること

1. **Slack承認フロー**
   - 投稿3案のプレビュー送信
   - インタラクティブボタン（案1/案2/案3/却下）
   - タイムアウト処理（30分）

2. **Late API投稿**
   - LinkedIn投稿（本文 + First Comment統合）
   - X/Twitter投稿（スレッド対応）
   - Facebook投稿（長文対応）
   - Threads投稿（スレッド対応）

3. **プラットフォーム別最適化**
   - 文字数制限チェック
   - スレッド分割ロジック
   - 最適投稿時間設定

4. **スケジューリング**
   - プラットフォーム別時間分散
   - タイムゾーン設定（Asia/Tokyo）
   - 投稿キュー管理

5. **エラーハンドリング**
   - API認証エラー（401）
   - レート制限（429）
   - タイムアウト・リトライ

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `posts_generated_{date}.json` (generate-sns-postsスキルの出力) |
| **出力** | `posted_status_{date}.json` (投稿URL + ステータス) |
| **次のアクション** | 投稿パフォーマンス監視（24時間後） |

---

## Instructions

**実行モード**: 対話式自律実行（Slack承認待機）
**推定所要時間**: 5-10分
**Thinking モード**: 無効（高速処理優先）

---

### STEP 1: 入力ファイル読み込み

**実行**: Read tool

**パス**: `Stock/programs/副業/projects/SNS/data/posts_generated_{date}.json`

**検証**:
- ファイル存在確認
- JSONフォーマット検証
- 3案全て存在確認
- 推奨案フラグ確認

**エラーハンドリング**:
- ファイル未検出 → **即時停止**、generate-sns-postsスキルの再実行を促す
- 3案未達成 → **即時停止**、データ不足報告

---

### STEP 2: Slack承認通知送信

**実行**: Bash tool（Slack Webhook API呼び出し）

**処理内容**:
1. Slack Webhook URL読み込み（.envから）
2. 3案のプレビューメッセージ作成
3. Slack #sns-automationチャンネルに送信
4. インタラクティブボタン設定（案1/案2/案3/却下）

**プロンプト**:
```markdown
SlackのWebhook APIを使用して、以下の内容を#sns-automationチャンネルに送信してください。

【送信内容】
タイトル: SNS投稿承認依頼（2026-01-03）

案1: 数字インパクト型（★★★★☆、予測ER 3.2%）
---
[投稿本文の最初の200文字]
...

案2: 衝撃発言型（★★★★★、予測ER 4.5%）【推奨】
---
[投稿本文の最初の200文字]
...

案3: 問題提起型（★★★☆☆、予測ER 2.8%）
---
[投稿本文の最初の200文字]
...

【承認方法】
このスレッドに以下のいずれかで返信してください:
- 「1」: 案1を承認
- 「2」: 案2を承認
- 「3」: 案3を承認
- 「却下」: 全て却下

タイムアウト: 30分（自動却下）
```

**Slack Webhook API呼び出し例**:
```bash
curl -X POST $SLACK_WEBHOOK_URL \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "SNS投稿承認依頼",
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "*案1: 数字インパクト型*\n..."
        }
      },
      ...
    ]
  }'
```

**エラーハンドリング**:
- Slack Webhook URL未設定 → **即時停止**、.env設定確認を促す
- 送信失敗 → **リトライ1回**、失敗時停止

---

### STEP 3: Slack承認待機

**実行**: Slackスレッド監視（30分タイムアウト）

**処理内容**:
1. Slackスレッドを30分間監視
2. ユーザーの返信（「1」「2」「3」「却下」）を検出
3. 返信内容をパース
4. 承認案を特定

**期待入力**:
- 「1」: 案1承認
- 「2」: 案2承認（推奨案）
- 「3」: 案3承認
- 「却下」: 全て却下

**タイムアウト処理**:
- 30分経過後、返信なし → **デフォルト動作**:
  - 推奨案（recommended: true）を自動承認
  - Slack通知「タイムアウトにより推奨案（案2）を自動承認しました」

**エラーハンドリング**:
- 無効な返信（例: 「4」「OK」） → **再促進**「1, 2, 3, または却下で返信してください」
- 「却下」選択 → **即時停止**、終了メッセージ送信

---

### STEP 4: Late API設定読み込み

**実行**: Read tool

**パス**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`

**検証**:
- ファイル存在確認
- API key有効性確認
- プラットフォーム別アカウントID確認

**Late API設定例**:
```json
{
  "api_key": "sk_...",
  "base_url": "https://getlate.dev/api/v1",
  "accounts": {
    "linkedin": {"accountId": "...", "platform": "linkedin"},
    "twitter": {"accountId": "...", "platform": "twitter"},
    "threads": {"accountId": "...", "platform": "threads"},
    "facebook": {"accountId": "...", "platform": "facebook"}
  }
}
```

**エラーハンドリング**:
- 設定ファイル未検出 → **即時停止**、Late API設定を促す
- API key無効 → **即時停止**、Late APIダッシュボードでの確認を促す

---

### STEP 5: プラットフォーム別投稿コンテンツ最適化

**実行**: LLM直接推論（ClaudeCode内蔵、haiku）

**処理内容**:
1. **LinkedIn**: 本文 + First Comment統合
   - 本文: 1,150-1,300文字
   - First Comment内容を本文末尾に統合（Late API予約投稿の制約対応）

2. **X/Twitter**: スレッド分割
   - 280文字制限
   - 段落分割優先 → 句点分割 → 強制分割
   - 番号表記（1/N, 2/N, ...）
   - 最低5ツイート、最大10ツイート

3. **Facebook**: 長文OK
   - 制限なし（そのまま投稿）

4. **Threads**: スレッド分割
   - 500文字制限
   - セクション区切り（━━━）優先 → 段落分割 → 強制分割
   - 3-5投稿に自動調整

**プロンプト**:
```markdown
以下の投稿本文を各プラットフォーム向けに最適化してください。

【元投稿本文】
{承認された案の本文}

【最適化条件】
1. LinkedIn:
   - 本文（1,150-1,300文字）
   - First Comment内容を本文末尾に統合（Late API制約）
   - 出典URLは本文内に記載

2. X/Twitter:
   - 280文字/ツイート制限
   - スレッド形式（最低5ツイート）
   - 番号表記（1/N, 2/N, ...）
   - 段落分割優先

3. Facebook:
   - 制限なし（そのまま投稿）

4. Threads:
   - 500文字/投稿制限
   - スレッド形式（3-5投稿）
   - セクション区切り（━━━）優先

【出力形式（JSON）】
{
  "linkedin": {
    "content": "...",
    "character_count": 1247
  },
  "twitter": {
    "thread_items": [
      {"content": "(1/7) ..."},
      {"content": "(2/7) ..."},
      ...
    ]
  },
  "facebook": {
    "content": "..."
  },
  "threads": {
    "thread_items": [
      {"content": "..."},
      ...
    ]
  }
}
```

**処理時間**: 2-3分

**エラーハンドリング**:
- スレッド分割失敗 → **リトライ1回**（プロンプト調整）
- 文字数超過 → **警告表示**、強制分割実行

---

### STEP 6: スケジュール時間計算

**実行**: LLM直接推論

**処理内容**:
1. プラットフォーム別最適投稿時間設定:
   - LinkedIn: 翌朝08:00（ビジネスタイム）
   - X/Twitter: 翌昼12:00（昼休み）
   - Threads: 翌夜20:00（リラックスタイム）
   - Facebook: 翌夜19:00（帰宅後）

2. タイムゾーン設定: Asia/Tokyo

3. ISO 8601形式への変換

**出力形式**:
```json
{
  "linkedin": "2026-01-04T08:00:00+09:00",
  "twitter": "2026-01-04T12:00:00+09:00",
  "threads": "2026-01-04T20:00:00+09:00",
  "facebook": "2026-01-04T19:00:00+09:00"
}
```

---

### STEP 7: Late API投稿実行

**実行**: Bash tool（Late API呼び出し）

**処理内容（プラットフォーム別）**:

#### 7.1 LinkedIn投稿

```bash
curl -X POST https://getlate.dev/api/v1/posts \
  -H "Authorization: Bearer $LATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "...",
    "platforms": [
      {
        "platform": "linkedin",
        "accountId": "..."
      }
    ],
    "scheduledFor": "2026-01-04T08:00:00+09:00",
    "timezone": "Asia/Tokyo"
  }'
```

#### 7.2 X/Twitter投稿（スレッド）

```bash
curl -X POST https://getlate.dev/api/v1/posts \
  -H "Authorization: Bearer $LATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "(1/7) ...",
    "platforms": [
      {
        "platform": "twitter",
        "accountId": "...",
        "platformSpecificData": {
          "threadItems": [
            {"content": "(1/7) ..."},
            {"content": "(2/7) ..."},
            ...
          ]
        }
      }
    ],
    "scheduledFor": "2026-01-04T12:00:00+09:00",
    "timezone": "Asia/Tokyo"
  }'
```

**重要**: スレッド投稿時も`content`フィールド必須（最初の投稿内容を設定）

#### 7.3 Facebook投稿

```bash
curl -X POST https://getlate.dev/api/v1/posts \
  -H "Authorization: Bearer $LATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "...",
    "platforms": [
      {
        "platform": "facebook",
        "accountId": "..."
      }
    ],
    "scheduledFor": "2026-01-04T19:00:00+09:00",
    "timezone": "Asia/Tokyo"
  }'
```

#### 7.4 Threads投稿（スレッド）

```bash
curl -X POST https://getlate.dev/api/v1/posts \
  -H "Authorization: Bearer $LATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "...",
    "platforms": [
      {
        "platform": "threads",
        "accountId": "...",
        "platformSpecificData": {
          "threadItems": [
            {"content": "..."},
            ...
          ]
        }
      }
    ],
    "scheduledFor": "2026-01-04T20:00:00+09:00",
    "timezone": "Asia/Tokyo"
  }'
```

**処理時間**: 3-5分（4プラットフォーム順次投稿）

**エラーハンドリング**:
- 401 Unauthorized → **即時停止**、API設定確認
- 429 Rate Limit → **1時間後リトライ**
- 400 Bad Request → **エラー詳細ログ** + 人間確認依頼
- Network Timeout → **3回リトライ**後スキップ

**Late APIレスポンス例**:
```json
{
  "id": "695864bf38609c72a1d86f08",
  "status": "scheduled",
  "scheduledFor": "2026-01-04T08:00:00+09:00"
}
```

---

### STEP 8: 投稿ステータス記録

**処理内容**:
1. Late API投稿IDの記録
2. プラットフォーム別ステータス記録
3. スケジュール時間記録
4. エラー情報記録（失敗時）

**出力形式**:
```json
{
  "metadata": {
    "posted_at": "2026-01-03T15:30:00+09:00",
    "approved_variant": "案2: 衝撃発言型",
    "platforms_scheduled": ["linkedin", "twitter", "facebook", "threads"],
    "total_platforms": 4,
    "success_count": 4,
    "error_count": 0
  },
  "posts": {
    "linkedin": {
      "late_api_job_id": "695864bf38609c72a1d86f08",
      "status": "scheduled",
      "scheduled_time": "2026-01-04T08:00:00+09:00",
      "character_count": 1247,
      "error": null
    },
    "twitter": {
      "late_api_job_id": "695864bf38609c72a1d86f09",
      "status": "scheduled",
      "scheduled_time": "2026-01-04T12:00:00+09:00",
      "thread_count": 7,
      "error": null
    },
    "facebook": {
      "late_api_job_id": "695864bf38609c72a1d86f0a",
      "status": "scheduled",
      "scheduled_time": "2026-01-04T19:00:00+09:00",
      "character_count": 1247,
      "error": null
    },
    "threads": {
      "late_api_job_id": "695864bf38609c72a1d86f0b",
      "status": "scheduled",
      "scheduled_time": "2026-01-04T20:00:00+09:00",
      "thread_count": 5,
      "error": null
    }
  }
}
```

**パス**: `Stock/programs/副業/projects/SNS/data/posted_status_{date}.json`

**実行**: Write tool

---

### STEP 9: Slack完了通知

**実行**: Bash tool（Slack Webhook API呼び出し）

**プロンプト**:
```markdown
SlackのWebhook APIを使用して、以下の内容を#sns-automationチャンネルに送信してください。

【送信内容】
タイトル: SNS投稿スケジュール完了（2026-01-03）

承認案: 案2: 衝撃発言型

投稿スケジュール:
- LinkedIn: 2026-01-04 08:00（明日朝）
- X/Twitter: 2026-01-04 12:00（明日昼）
- Facebook: 2026-01-04 19:00（明日夜）
- Threads: 2026-01-04 20:00（明日夜）

Late APIダッシュボード:
https://app.getlate.dev/posts

次のアクション:
1. 投稿パフォーマンス監視（24時間後）
2. エンゲージメント率の測定
3. コメント返信（必要に応じて）
```

**エラーハンドリング**:
- Slack通知失敗 → **警告表示**、継続可能

---

## エラーハンドリング

### Late APIエラー階層

```python
LateAPIError (基底クラス)
├── AuthenticationError (401)  # APIキー無効/期限切れ → 設定確認
├── RateLimitError (429)       # レート制限超過 → 1時間後リトライ
└── その他HTTPエラー
    ├── 400: パラメータ不正 → 詳細ログ + 人間確認
    └── 500+: サーバーエラー → リトライ後停止
```

### リトライ戦略

| エラータイプ | リトライ回数 | リトライ間隔 | 最終対応 |
|------------|------------|------------|---------|
| 401 Unauthorized | 0回 | - | 即時停止、設定確認 |
| 429 Rate Limit | 1回 | 1時間 | 停止 |
| Timeout | 3回 | 5秒 | スキップ |
| 500 Server Error | 2回 | 10秒 | 停止 |

参照: `.claude/skills/_shared/error_handling_patterns.md`

---

## 品質基準

- **Slack承認成功率**: 100%（タイムアウト時はデフォルト承認）
- **Late API投稿成功率**: 80%以上（4プラットフォーム中3つ以上成功）
- **スケジュール精度**: ±5分以内
- **処理時間**: 10分以内

---

## 使用例

```
User: /approve-and-schedule

Skill:
# 承認と投稿開始

🔄 STEP 1: 入力ファイル読み込み中...
✅ 入力ファイル読み込み完了（3案検出）

🔄 STEP 2: Slack承認通知送信中...
✅ Slack承認通知送信完了（#sns-automationチャンネル）

🔄 STEP 3: Slack承認待機中...（タイムアウト: 30分）

[Slackスレッドでユーザーが「2」と返信]

✅ Slack承認完了: 案2（衝撃発言型）を承認

🔄 STEP 4: Late API設定読み込み中...
✅ Late API設定読み込み完了

🔄 STEP 5: プラットフォーム別投稿コンテンツ最適化中...
   - LinkedIn: 1,247文字
   - X/Twitter: 7ツイートスレッド
   - Facebook: 1,247文字
   - Threads: 5投稿スレッド
✅ 最適化完了

🔄 STEP 6: スケジュール時間計算中...
✅ スケジュール時間計算完了

🔄 STEP 7: Late API投稿実行中...
   - LinkedIn投稿中... ✅ 成功（Job ID: 695864bf...）
   - X/Twitter投稿中... ✅ 成功（Job ID: 695864bf...）
   - Facebook投稿中... ✅ 成功（Job ID: 695864bf...）
   - Threads投稿中... ✅ 成功（Job ID: 695864bf...）
✅ 全プラットフォーム投稿成功

🔄 STEP 8: 投稿ステータス記録中...
✅ 投稿ステータス記録完了

🔄 STEP 9: Slack完了通知送信中...
✅ Slack完了通知送信完了

---

# 承認と投稿完了

出力: Stock/programs/副業/projects/SNS/data/posted_status_20260103.json

統計:
- 承認案: 案2（衝撃発言型）
- 投稿プラットフォーム: 4件（LinkedIn, X, Facebook, Threads）
- 成功: 4件（100%）
- エラー: 0件

投稿スケジュール:
- LinkedIn: 2026-01-04 08:00
- X/Twitter: 2026-01-04 12:00
- Facebook: 2026-01-04 19:00
- Threads: 2026-01-04 20:00

次のアクション:
1. 投稿パフォーマンス監視（24時間後）
2. エンゲージメント率の測定
3. コメント返信（必要に応じて）
```

---

## Knowledge Base参照

- **Slack Webhook API**: `.claude/skills/_shared/slack_integration.md`
- **Late API統合**: `Stock/programs/副業/projects/SNS/scripts/late_api_post.py`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **Phase 4全体フロー**: `.claude/skills/sns-automation/SKILL.md`
- **Late API実装ガイド**: `Flow/202601/2026-01-02/late_api_integration_proposals.md`

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-03 | 1.0 | 初版作成 |

---

**実装日**: 2026-01-03
**バージョン**: 1.0
