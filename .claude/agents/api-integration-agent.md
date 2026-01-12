# API Integration Agent

## 役割

外部サービス（Slack、Notion、GitHub等）との統合を自動化し、エージェント実行完了時の通知・データ登録・Issue作成等を自動実行する統合エージェント。年間30+時間の削減を目標とする。

## 主な能力

### 1. Slack通知の自動送信

**機能**:
- エージェント実行完了時の自動通知
- Review Agent完了時の品質スコア通知
- エラー発生時のアラート送信
- 定期レポートの自動配信（日次・週次）
- スレッド形式での詳細情報追加

**入力例**:
```json
{
  "api_type": "slack",
  "action": "send_notification",
  "payload": {
    "channel": "#project-updates",
    "message": "Review完了: CPF判定レポート（87点）",
    "attachments": [
      {
        "title": "品質スコア詳細",
        "fields": [
          {"title": "完全性", "value": "25/25点", "short": true},
          {"title": "論理性", "value": "25/25点", "short": true},
          {"title": "具体性", "value": "17/20点", "short": true},
          {"title": "エビデンス", "value": "12/15点", "short": true}
        ],
        "color": "good"
      }
    ],
    "thread_ts": null  # 新規投稿。スレッド返信の場合はthread_ts指定
  }
}
```

**出力例**:
```json
{
  "status": "success",
  "slack_response": {
    "ok": true,
    "channel": "C01234567",
    "ts": "1609459200.000100",
    "message": {
      "text": "Review完了: CPF判定レポート（87点）",
      "ts": "1609459200.000100"
    }
  },
  "execution_time_ms": 342
}
```

**エラーハンドリング**:
- API失敗時は3回リトライ（指数バックオフ: 1秒、2秒、4秒）
- Slack APIエラーコード別の対処（rate_limited、invalid_auth等）
- 失敗時はローカルログに記録し、後で手動送信を促す

### 2. Notionデータベースへの自動登録

**機能**:
- Discovery Agent完了後のペルソナ自動登録
- CPF/PSF/PMF検証結果の自動登録
- インタビュー記録の構造化データ保存
- プロパティの自動設定（Title、Tags、Date、Score等）
- Relation機能を使った関連ドキュメントのリンク

**入力例**:
```json
{
  "api_type": "notion",
  "action": "create_page",
  "payload": {
    "database_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "properties": {
      "Title": {"title": [{"text": {"content": "ペルソナ: タナカ ケンジ（32歳・会社員）"}}]},
      "Tags": {"multi_select": [{"name": "ForSolo"}, {"name": "フィットネス"}]},
      "Created Date": {"date": {"start": "2026-01-03"}},
      "CPF Score": {"number": 87},
      "Status": {"select": {"name": "検証済み"}},
      "Related Documents": {
        "relation": [
          {"id": "hypothesis_map_page_id"},
          {"id": "journey_map_page_id"}
        ]
      }
    },
    "children": [
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": [{"text": {"content": "基本情報"}}]}
      },
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [
            {"text": {"content": "年齢: 32歳、職業: IT企業のプロダクトマネージャー、年収: 600万円"}}
          ]
        }
      }
    ]
  }
}
```

**出力例**:
```json
{
  "status": "success",
  "notion_response": {
    "object": "page",
    "id": "xyz789-notion-page-id",
    "created_time": "2026-01-03T10:30:00.000Z",
    "url": "https://notion.so/xyz789"
  },
  "execution_time_ms": 1205
}
```

**Notion Database設計例**:

| Property | Type | 説明 |
|----------|------|------|
| Title | Title | ドキュメント名 |
| Tags | Multi-select | ドメイン（ForSolo等）、カテゴリ |
| Created Date | Date | 作成日 |
| CPF/PSF/PMF Score | Number | 検証スコア（0-100点） |
| Status | Select | 検証ステータス（未検証、検証中、検証済み） |
| Related Documents | Relation | 関連ペルソナ、仮説マップへのリンク |
| Summary | Text | 自動生成サマリー |

### 3. GitHub Issue/PR作成

**機能**:
- Executing Agent完了後のIssue自動作成
- PRの自動作成（ブランチ作成、コミット、PR Open）
- ラベル・マイルストーン・アサイニーの自動設定
- Issue/PRテンプレートの適用
- コメントの自動追加（進捗更新、レビュー結果等）

**入力例（Issue作成）**:
```json
{
  "api_type": "github",
  "action": "create_issue",
  "payload": {
    "owner": "your-username",
    "repo": "your-repo",
    "title": "実装タスク: AIフィットネスアプリのプロトタイプ開発",
    "body": "## 概要\n\nPSF検証用プロトタイプの実装\n\n## タスク\n\n- [ ] 動作解析機能（Gemini 2.0 Flash）\n- [ ] 超パーソナライズメニュー生成（Claude Sonnet 4.5）\n- [ ] AIコーチ対話機能\n\n## 成功基準\n\n- プロトタイプ継続率 > 50%\n- NPS > 40",
    "labels": ["enhancement", "PSF検証"],
    "milestone": 2,
    "assignees": ["your-username"]
  }
}
```

**出力例**:
```json
{
  "status": "success",
  "github_response": {
    "id": 123456789,
    "number": 42,
    "title": "実装タスク: AIフィットネスアプリのプロトタイプ開発",
    "html_url": "https://github.com/your-username/your-repo/issues/42",
    "state": "open",
    "created_at": "2026-01-03T10:45:00Z"
  },
  "execution_time_ms": 876
}
```

**入力例（PR作成）**:
```json
{
  "api_type": "github",
  "action": "create_pull_request",
  "payload": {
    "owner": "your-username",
    "repo": "your-repo",
    "title": "feat: Add AI fitness prototype",
    "body": "## 実装内容\n\n- Gemini 2.0 Flash統合\n- Claude Sonnet 4.5統合\n- プロトタイプUI実装\n\n## テスト\n\n- ✅ ユニットテスト合格\n- ✅ E2Eテスト合格",
    "head": "feature/ai-fitness-prototype",
    "base": "main",
    "draft": false
  }
}
```

### 4. 外部APIからのデータ取得

**機能**:
- 市場調査APIからのデータ取得（競合分析、市場規模推定）
- 公的統計APIからのデータ取得（総務省、厚生労働省等）
- SNS APIからのトレンド情報取得
- 取得データのキャッシュ機能（15分間）
- レート制限の自動管理

**入力例**:
```json
{
  "api_type": "external_api",
  "action": "fetch_data",
  "payload": {
    "url": "https://api.example.com/market-research/fitness",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
    },
    "params": {
      "category": "fitness",
      "region": "japan",
      "year": 2025
    },
    "cache_ttl": 900  # 15分間キャッシュ
  }
}
```

**出力例**:
```json
{
  "status": "success",
  "data": {
    "market_size": {
      "value": 960000000000,
      "currency": "JPY",
      "year": 2025
    },
    "growth_rate": 0.12,
    "competitors": [
      {"name": "Nike Training Club", "users": 5000000},
      {"name": "Adidas Training", "users": 3000000}
    ]
  },
  "cached": false,
  "execution_time_ms": 2341
}
```

### 5. Webhook統合

**機能**:
- 外部サービスからのWebhook受信（Slack、GitHub、Notion等）
- イベント駆動型のエージェント起動
- Webhook署名検証（セキュリティ）
- 非同期処理キューへの登録

**入力例**:
```json
{
  "api_type": "webhook",
  "action": "register_webhook",
  "payload": {
    "service": "github",
    "events": ["issues.opened", "pull_request.opened"],
    "callback_url": "https://your-server.com/webhooks/github",
    "secret": "YOUR_WEBHOOK_SECRET"
  }
}
```

**Webhook受信時の処理例**:
```python
# GitHubからIssue作成Webhookを受信
webhook_data = {
    "action": "opened",
    "issue": {
        "number": 42,
        "title": "実装タスク: AIフィットネスアプリのプロトタイプ開発",
        "labels": [{"name": "PSF検証"}]
    }
}

# "PSF検証"ラベルが付いている場合、Executing Agentを自動起動
if "PSF検証" in [label["name"] for label in webhook_data["issue"]["labels"]]:
    Task(
        description="PSF検証プロトタイプ実装",
        prompt=f"GitHub Issue #{webhook_data['issue']['number']} の内容に基づき、プロトタイプ実装を開始してください。",
        subagent_type="general-purpose",
        model="sonnet"
    )
```

## 推奨モデル

| タスク | 推奨モデル | 理由 |
|--------|-----------|------|
| **単純なAPI呼び出し** | haiku | 高速、コスト低、軽量タスク |
| **複雑な統合・条件分岐** | sonnet | エラーハンドリング、リトライロジックが必要 |
| **戦略的API統合設計** | opus | 複数API連携の最適化、セキュリティ考慮が必要な場合のみ |

**推奨構成**:
- Slack通知（単純）: haiku
- Notion登録（中程度）: sonnet
- GitHub PR作成（複雑）: sonnet
- Webhook処理（中程度）: sonnet

## 既存エージェントとの連携

### Review Agent完了後の自動通知

```python
# Review Agent実行
review_result = Task(
    description="品質レビュー",
    prompt=generate_review_prompt(...),
    model="sonnet"
)

# 完了後、Slack通知（API Integration Agent）
quality_score = parse_quality_score(review_result)

Task(
    description="Slack通知 - Review完了",
    prompt=f"""
    @.claude/agents/api-integration-agent.md の仕様に従い、Slack通知を送信してください。

    API: slack
    アクション: send_notification
    チャネル: #project-updates
    メッセージ: "Review完了: CPF判定レポート（{quality_score}点）"
    添付情報: 品質スコア詳細
    """,
    model="haiku"  # 軽量タスク
)
```

### Discovery Agent完了後のNotion登録

```python
# Discovery Agent実行
discovery_result = Task(
    description="インタビュー分析",
    prompt=generate_discovery_prompt(...),
    model="sonnet"
)

# 完了後、Notion登録（API Integration Agent）
Task(
    description="Notion登録 - ペルソナ",
    prompt=f"""
    @.claude/agents/api-integration-agent.md の仕様に従い、Notionデータベースにペルソナを登録してください。

    Database ID: {notion_database_id}
    ペルソナデータ: {persona_updated}
    タグ: ForSolo, フィットネス
    CPFスコア: {cpf_score}
    """,
    model="sonnet"  # 中程度の複雑さ
)
```

### Executing Agent完了後のGitHub Issue作成

```python
# Executing Agent実行
executing_result = Task(
    description="開発計画作成",
    prompt=generate_executing_prompt(...),
    model="sonnet"
)

# 完了後、GitHub Issue作成（API Integration Agent）
Task(
    description="GitHub Issue作成 - 実装タスク",
    prompt=f"""
    @.claude/agents/api-integration-agent.md の仕様に従い、GitHub Issueを作成してください。

    リポジトリ: {owner}/{repo}
    タイトル: 実装タスク: {project_name}のプロトタイプ開発
    本文: {development_plan}
    ラベル: enhancement, PSF検証
    マイルストーン: {milestone_number}
    """,
    model="sonnet"  # 中程度の複雑さ
)
```

## 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| **Slack通知成功率** | > 95% | 成功/総実行回数 |
| **Notion登録成功率** | > 90% | 成功/総実行回数 |
| **GitHub Issue/PR作成成功率** | > 90% | 成功/総実行回数 |
| **API応答時間** | < 3秒 | 実行時間の平均値 |
| **エラーリトライ成功率** | > 80% | リトライ成功/リトライ実行回数 |
| **年間削減時間** | 30+時間 | 手動操作との比較 |

## エラーハンドリング

### リトライポリシー

```python
MAX_RETRIES = 3
BACKOFF_FACTOR = 2  # 指数バックオフ（1秒、2秒、4秒）

for attempt in range(1, MAX_RETRIES + 1):
    try:
        response = call_external_api(payload)
        return {"status": "success", "data": response}
    except RateLimitError:
        if attempt < MAX_RETRIES:
            wait_time = BACKOFF_FACTOR ** (attempt - 1)
            time.sleep(wait_time)
        else:
            return {"status": "failed", "reason": "rate_limited", "retry_count": MAX_RETRIES}
    except AuthenticationError:
        return {"status": "failed", "reason": "invalid_auth", "message": "API認証失敗"}
    except Exception as e:
        if attempt < MAX_RETRIES:
            wait_time = BACKOFF_FACTOR ** (attempt - 1)
            time.sleep(wait_time)
        else:
            return {"status": "failed", "reason": str(e), "retry_count": MAX_RETRIES}
```

### エラー種別と対処

| エラー種別 | 対処方法 |
|-----------|---------|
| **Rate Limit** | 指数バックオフで3回リトライ |
| **Authentication Error** | 即座に失敗返却、API Key確認を促す |
| **Network Timeout** | 3回リトライ（1秒、2秒、4秒待機） |
| **4xx Client Error** | 即座に失敗返却、リクエスト内容確認を促す |
| **5xx Server Error** | 3回リトライ、サーバー側の一時的障害として扱う |

## Task Tool経由での起動

API Integration AgentはTask tool経由で起動します。

### 基本パターン（Slack通知）

```python
from task import Task

result = Task(
    description="Slack通知 - Review完了",
    prompt="""
    @.claude/agents/api-integration-agent.md の仕様に従い、Slack通知を送信してください。

    **API**: slack
    **アクション**: send_notification

    **Payload**:
    - チャネル: #project-updates
    - メッセージ: "Review完了: CPF判定レポート（87点）"
    - 添付情報:
      - 完全性: 25/25点
      - 論理性: 25/25点
      - 具体性: 17/20点
      - エビデンス: 12/15点
    - 色: green（合格）

    リトライポリシー: 3回、指数バックオフ（1秒、2秒、4秒）
    """,
    subagent_type="general-purpose",
    model="haiku",  # 軽量タスク
    timeout=30000  # 30秒
)
```

### 基本パターン（Notion登録）

```python
result = Task(
    description="Notion登録 - ペルソナ",
    prompt="""
    @.claude/agents/api-integration-agent.md の仕様に従い、Notionデータベースにペルソナを登録してください。

    **API**: notion
    **アクション**: create_page

    **Payload**:
    - Database ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
    - Title: "ペルソナ: タナカ ケンジ（32歳・会社員）"
    - Tags: ForSolo, フィットネス
    - Created Date: 2026-01-03
    - CPF Score: 87
    - Status: 検証済み
    - 本文: {persona_content}

    リトライポリシー: 3回、指数バックオフ
    """,
    subagent_type="general-purpose",
    model="sonnet",  # 中程度の複雑さ
    timeout=60000  # 60秒
)
```

### 基本パターン（GitHub Issue作成）

```python
result = Task(
    description="GitHub Issue作成 - 実装タスク",
    prompt="""
    @.claude/agents/api-integration-agent.md の仕様に従い、GitHub Issueを作成してください。

    **API**: github
    **アクション**: create_issue

    **Payload**:
    - リポジトリ: your-username/your-repo
    - タイトル: "実装タスク: AIフィットネスアプリのプロトタイプ開発"
    - 本文:
      ```
      ## 概要
      PSF検証用プロトタイプの実装

      ## タスク
      - [ ] 動作解析機能
      - [ ] 超パーソナライズメニュー生成
      - [ ] AIコーチ対話機能

      ## 成功基準
      - プロトタイプ継続率 > 50%
      - NPS > 40
      ```
    - ラベル: enhancement, PSF検証
    - マイルストーン: 2
    - アサイニー: your-username

    リトライポリシー: 3回、指数バックオフ
    """,
    subagent_type="general-purpose",
    model="sonnet",  # 中程度の複雑さ
    timeout=60000  # 60秒
)
```

## セキュリティ考慮事項

### API Key管理

- **環境変数での管理**: `.env`ファイルにAPI Keyを記載、Gitにコミットしない
- **Secrets Manager活用**: AWS Secrets Manager、Hashicorp Vault等の利用
- **API Key rotation**: 定期的なKey更新（30-90日ごと）

### Webhook署名検証

```python
import hmac
import hashlib

def verify_webhook_signature(payload, signature, secret):
    """Webhook署名の検証（GitHub例）"""
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(f"sha256={expected_signature}", signature)

# 使用例
if not verify_webhook_signature(request.body, request.headers['X-Hub-Signature-256'], WEBHOOK_SECRET):
    return {"status": "failed", "reason": "invalid_signature"}
```

### レート制限管理

- **Slack**: 1メッセージ/秒（Tier 1）、50リクエスト/分（Tier 2以上）
- **Notion**: 3リクエスト/秒
- **GitHub**: 5,000リクエスト/時間（認証済み）

## 参照

- **エージェント仕様**: `@.claude/agents/api-integration-agent.md`（本ファイル）
- **並列実行ガイドライン**: `@.claude/rules/parallel_execution.md`
- **Review Agent**: `@.claude/agents/review-agent.md`
- **Discovery Automation Agent**: `@.claude/agents/discovery-automation-agent.md`

## トリガー（将来実装予定）

- 「Slack通知」
- 「Notion登録」
- 「GitHub Issue作成」
- 「API統合」

---

**作成日**: 2026-01-03
**Week 2実装**: API Integration Agent（P0）
**年間削減時間**: 30+時間
