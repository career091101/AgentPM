# API Integration Command

**コマンド**: `/api-integration`

**説明**: 外部サービス（Slack、Notion、GitHub等）との統合を自動実行

**エージェント**: API Integration Agent

---

## 使用方法

```
/api-integration
```

または

```
Slack通知を送信してください
Notionに登録してください
GitHub Issueを作成してください
```

---

## 実行内容

1. **API種別の選択**: Slack / Notion / GitHub / External API / Webhook
2. **アクションの選択**: 通知送信 / データ登録 / Issue作成 / データ取得 等
3. **Payloadの設定**: チャネル名、メッセージ内容、データベースID等
4. **実行**: APIリクエスト送信（リトライ機能付き）
5. **結果返却**: 成功/失敗ステータス、実行時間、エラーログ

---

## 入力パラメータ（対話形式で質問）

### 必須パラメータ

1. **API種別**:
   - 質問: 「API種別を選択してください（slack / notion / github / external_api / webhook）」
   - 例: `slack`
   - デフォルト: なし（必須）

2. **アクション**:
   - 質問: 「アクションを選択してください」
   - Slack: `send_notification`
   - Notion: `create_page`, `update_page`, `query_database`
   - GitHub: `create_issue`, `create_pull_request`, `add_comment`
   - External API: `fetch_data`
   - Webhook: `register_webhook`
   - デフォルト: なし（必須）

### Slack通知の場合

3. **チャネル名**:
   - 質問: 「通知先のチャネル名を教えてください（例: #project-updates）」
   - 例: `#project-updates`

4. **メッセージ内容**:
   - 質問: 「送信するメッセージを入力してください」
   - 例: `Review完了: CPF判定レポート（87点）`

5. **添付情報**（オプション）:
   - 質問: 「添付情報を追加しますか？（スキップ可）」
   - 例: 品質スコア詳細（完全性25/25点、論理性25/25点等）

6. **スレッド返信**（オプション）:
   - 質問: 「スレッド返信にしますか？ thread_tsを入力（スキップで新規投稿）」
   - 例: `1609459200.000100`

### Notion登録の場合

3. **Database ID**:
   - 質問: 「NotionデータベースのIDを入力してください」
   - 例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`

4. **ページタイトル**:
   - 質問: 「ページタイトルを入力してください」
   - 例: `ペルソナ: タナカ ケンジ（32歳・会社員）`

5. **プロパティ**:
   - 質問: 「プロパティを設定してください（Tags, Created Date, CPF Score等）」
   - 例: `Tags: ForSolo, フィットネス / CPF Score: 87 / Status: 検証済み`

6. **ページ内容**:
   - 質問: 「ページ本文のパス、または直接入力してください」
   - 例: `Flow/202601/2026-01-03/discovery_output/persona_updated.md`

### GitHub Issue作成の場合

3. **リポジトリ**:
   - 質問: 「リポジトリ名を入力してください（owner/repo形式）」
   - 例: `your-username/your-repo`

4. **Issueタイトル**:
   - 質問: 「Issueタイトルを入力してください」
   - 例: `実装タスク: AIフィットネスアプリのプロトタイプ開発`

5. **Issue本文**:
   - 質問: 「Issue本文のパス、または直接入力してください」
   - 例: `Flow/202601/2026-01-03/development_plan.md`

6. **ラベル**:
   - 質問: 「ラベルを入力してください（カンマ区切り）」
   - 例: `enhancement, PSF検証`

7. **マイルストーン**（オプション）:
   - 質問: 「マイルストーン番号を入力してください（スキップ可）」
   - 例: `2`

8. **アサイニー**（オプション）:
   - 質問: 「アサイニーを入力してください（カンマ区切り、スキップ可）」
   - 例: `your-username`

---

## 出力結果

### 成功時

```json
{
  "status": "success",
  "api_type": "slack",
  "action": "send_notification",
  "response": {
    "ok": true,
    "channel": "C01234567",
    "ts": "1609459200.000100"
  },
  "execution_time_ms": 342
}
```

### 失敗時

```json
{
  "status": "failed",
  "api_type": "slack",
  "action": "send_notification",
  "reason": "rate_limited",
  "retry_count": 3,
  "error_log": "Flow/202601/2026-01-03/api_error.log"
}
```

---

## 実行例

### 例1: Slack通知（Review完了）

```
ユーザー: /api-integration

エージェント: API種別を選択してください（slack / notion / github / external_api / webhook）
ユーザー: slack

エージェント: アクションを選択してください
ユーザー: send_notification

エージェント: 通知先のチャネル名を教えてください（例: #project-updates）
ユーザー: #project-updates

エージェント: 送信するメッセージを入力してください
ユーザー: Review完了: CPF判定レポート（87点）

エージェント: 添付情報を追加しますか？（スキップ可）
ユーザー: 品質スコア詳細を追加

エージェント: Slack通知を送信します...

[3秒後]

エージェント: ✅ Slack通知が正常に送信されました
- チャネル: #project-updates
- タイムスタンプ: 1609459200.000100
- 実行時間: 342ms
- Slack URL: https://your-workspace.slack.com/archives/C01234567/p1609459200000100
```

### 例2: Notion登録（ペルソナ）

```
ユーザー: Notionにペルソナを登録してください

エージェント: NotionデータベースのIDを入力してください
ユーザー: a1b2c3d4-e5f6-7890-abcd-ef1234567890

エージェント: ページタイトルを入力してください
ユーザー: ペルソナ: タナカ ケンジ（32歳・会社員）

エージェント: プロパティを設定してください（Tags, Created Date, CPF Score等）
ユーザー: Tags: ForSolo, フィットネス / CPF Score: 87 / Status: 検証済み

エージェント: ページ本文のパス、または直接入力してください
ユーザー: Flow/202601/2026-01-03/discovery_output/persona_updated.md

エージェント: Notionページを作成します...

[1.2秒後]

エージェント: ✅ Notionページが正常に作成されました
- ページID: xyz789-notion-page-id
- タイトル: ペルソナ: タナカ ケンジ（32歳・会社員）
- タグ: ForSolo, フィットネス
- CPFスコア: 87点
- 実行時間: 1205ms
- Notion URL: https://notion.so/xyz789
```

### 例3: GitHub Issue作成（実装タスク）

```
ユーザー: GitHub Issueを作成してください

エージェント: リポジトリ名を入力してください（owner/repo形式）
ユーザー: your-username/your-repo

エージェント: Issueタイトルを入力してください
ユーザー: 実装タスク: AIフィットネスアプリのプロトタイプ開発

エージェント: Issue本文のパス、または直接入力してください
ユーザー: Flow/202601/2026-01-03/development_plan.md

エージェント: ラベルを入力してください（カンマ区切り）
ユーザー: enhancement, PSF検証

エージェント: マイルストーン番号を入力してください（スキップ可）
ユーザー: 2

エージェント: アサイニーを入力してください（カンマ区切り、スキップ可）
ユーザー: your-username

エージェント: GitHub Issueを作成します...

[0.9秒後]

エージェント: ✅ GitHub Issueが正常に作成されました
- Issue番号: #42
- タイトル: 実装タスク: AIフィットネスアプリのプロトタイプ開発
- ラベル: enhancement, PSF検証
- マイルストーン: 2
- アサイニー: your-username
- 実行時間: 876ms
- GitHub URL: https://github.com/your-username/your-repo/issues/42
```

### 例4: エラーハンドリング（Rate Limit）

```
ユーザー: Slack通知を送信してください

[... パラメータ入力 ...]

エージェント: Slack通知を送信します...

[3秒後]

エージェント: ⚠️ Slack APIがレート制限に達しました。リトライ中...
- リトライ 1/3: 1秒待機後に再試行
- リトライ 2/3: 2秒待機後に再試行
- リトライ 3/3: 4秒待機後に再試行

[10秒後]

エージェント: ❌ Slack通知が失敗しました
- 理由: rate_limited
- リトライ回数: 3回
- エラーログ: Flow/202601/2026-01-03/api_error.log
- 推奨対処: 数分後に再実行してください
```

---

## 既存エージェントとの連携

### Review Agent完了後の自動通知

```python
# Review Agent実行
review_result = Task(description="品質レビュー", ...)

# 完了後、API Integration Agentで自動通知
Task(
    description="Slack通知 - Review完了",
    prompt=generate_slack_notification_prompt(review_result),
    model="haiku"
)
```

### Discovery Agent完了後のNotion登録

```python
# Discovery Agent実行
discovery_result = Task(description="インタビュー分析", ...)

# 完了後、API Integration AgentでNotion登録
Task(
    description="Notion登録 - ペルソナ",
    prompt=generate_notion_page_prompt(discovery_result),
    model="sonnet"
)
```

### Executing Agent完了後のGitHub Issue作成

```python
# Executing Agent実行
executing_result = Task(description="開発計画作成", ...)

# 完了後、API Integration AgentでGitHub Issue作成
Task(
    description="GitHub Issue作成 - 実装タスク",
    prompt=generate_github_issue_prompt(executing_result),
    model="sonnet"
)
```

---

## エラーハンドリング

### リトライポリシー

- **最大リトライ回数**: 3回
- **バックオフ戦略**: 指数バックオフ（1秒、2秒、4秒）
- **リトライ対象エラー**: Rate Limit、Network Timeout、5xx Server Error
- **即座に失敗**: Authentication Error、4xx Client Error

### エラー種別と推奨対処

| エラー | 対処方法 |
|--------|---------|
| **rate_limited** | 数分待機後に再実行 |
| **invalid_auth** | API Key・Token確認 |
| **network_timeout** | ネットワーク接続確認 |
| **4xx_client_error** | リクエスト内容確認（チャネル名、Database ID等） |
| **5xx_server_error** | サーバー側の一時的障害、10分後に再実行 |

---

## セキュリティ

### API Key管理

- **環境変数**: `.env`ファイルでAPI Keyを管理
- **Git除外**: `.gitignore`に`.env`を追加し、コミット防止
- **Key rotation**: 30-90日ごとにKey更新

### Webhook署名検証

- **GitHub**: `X-Hub-Signature-256`ヘッダーで署名検証
- **Slack**: `X-Slack-Signature`ヘッダーで署名検証
- **署名不一致**: リクエスト拒否

---

## 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| Slack通知成功率 | > 95% | 成功/総実行回数 |
| Notion登録成功率 | > 90% | 成功/総実行回数 |
| GitHub Issue/PR作成成功率 | > 90% | 成功/総実行回数 |
| API応答時間 | < 3秒 | 実行時間の平均値 |
| エラーリトライ成功率 | > 80% | リトライ成功/リトライ実行回数 |

---

## 参照

- **エージェント仕様**: `@.claude/agents/api-integration-agent.md`
- **並列実行**: `@.claude/rules/parallel_execution.md`
- **Review Agent**: `@.claude/agents/review-agent.md`
- **Discovery Automation Agent**: `@.claude/agents/discovery-automation-agent.md`

---

**作成日**: 2026-01-03
**Week 2実装**: API Integration Agent（P0）
