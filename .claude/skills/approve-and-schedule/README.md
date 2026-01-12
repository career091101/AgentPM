# Approve and Schedule Skill

Phase 3生成投稿3案のSlack承認 → SNS自動投稿スキル。

---

## 概要

**ClaudeCode LLM実行型**により、投稿文の人間承認とSNS自動投稿を完全自動化。Slack MCP通知、スレッド返信承認、LinkedIn/X API投稿、Facebook Claude in Chrome投稿、結果レポート生成を一括実行。

---

## クイックスタート

### 1. 前提条件

Phase 3の投稿生成が完了していること：

```bash
# Phase 3実行済みの確認
ls Stock/programs/副業/projects/SNS/data/posts_generated_ai_*.json
```

### 2. Slack MCP サーバー設定（必須）

ClaudeCode で Slack MCP サーバーを有効化：

**設定ファイル**: `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-bot-token",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

**Slack Bot Token 取得**:
1. https://api.slack.com/apps でアプリ作成
2. "OAuth & Permissions" でスコープ追加：`chat:write`, `channels:history`, `channels:read`
3. "Install to Workspace" でインストール
4. "Bot User OAuth Token" をコピーして上記の `SLACK_BOT_TOKEN` に設定
5. Workspace IDを `SLACK_TEAM_ID` に設定

### 3. 環境変数設定（SNS API）

SNS投稿用の認証情報を環境変数に設定：

```bash
# LinkedIn（オプション - Claude in Chrome経由で取得）
export LINKEDIN_ACCESS_TOKEN="AQV..."
export LINKEDIN_PERSON_URN="abc123"

# X (Twitter)（オプション - Claude in Chrome経由で取得）
export X_BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAA..."
export X_API_KEY="xxxxxxxxxxxx"
export X_API_SECRET="xxxxxxxxxxxx"
export X_ACCESS_TOKEN="123456789-xxxxxxxxxxxx"
export X_ACCESS_TOKEN_SECRET="xxxxxxxxxxxx"

# Facebook（不要 - Claude in Chromeでブラウザ操作）
```

**注意**:
- Slack MCP サーバーが必須（Webhook不要）
- LinkedIn/X API認証情報はClaude in Chrome経由で取得（下記参照）
- FacebookはClaude in Chromeで直接ブラウザ操作するため認証情報不要

### 4. スキル実行

```bash
# Claude Codeで実行
投稿承認

# または
/approve-and-schedule
```

### 5. Slack承認フロー

実行すると、Slack #sns-automation チャンネルに通知が届きます：

```
🚀 LinkedIn投稿3案生成完了

トピック: Tesla Optimus × NVIDIA Jensen Huang
生成日時: 2026-01-02T09:00:00+09:00
高野メソッド準拠率: 100%

━━━━━━━━━━━━━━━━━━━━

案1: 数字インパクト型 (★★★★☆)
文字数: 892字 | 予測ER: 3.2%

【速報】ヒューマノイドロボット市場「数兆ドル産業」へ...

━━━━━━━━━━━━━━━━━━━━

案2: 衝撃発言型 (★★★★★) 推奨
文字数: 1,247字 | 予測ER: 4.5%

「Elon Muskは、マジで異次元のエンジニアだ」...

━━━━━━━━━━━━━━━━━━━━

案3: 問題提起型 (★★★☆☆)
文字数: 923字 | 予測ER: 2.8%

なぜヒューマノイドロボットは「まだ」実用化されないのか？...

━━━━━━━━━━━━━━━━━━━━

承認方法: このスレッドに「1」「2」「3」のいずれかを返信してください。
または、24時間以内に返信がない場合、推奨案（案2）を自動承認します。
```

Slackスレッドに「1」「2」「3」のいずれかを返信して承認します。

### 6. 自動投稿

承認後、自動的に以下のプラットフォームに投稿：

- **LinkedIn**: API経由で投稿（1,500字対応）
- **Facebook**: Claude in Chrome経由でブラウザ操作により投稿（300-500字に要約）
- **X (Twitter)**: API経由でスレッド形式投稿（150字フック + 詳細）

### 7. 結果確認

```bash
# 投稿結果レポート
cat Stock/programs/副業/projects/SNS/data/posted_status_20260102.json | jq '.posting_results'
```

出力例：
```json
{
  "linkedin": {
    "status": "success",
    "post_url": "https://www.linkedin.com/feed/update/urn:li:share:1234567890"
  },
  "facebook": {
    "status": "success",
    "post_url": "https://www.facebook.com/123456789/posts/987654321"
  },
  "x": {
    "status": "success",
    "thread_url": "https://x.com/username/status/1745678901234567890"
  }
}
```

---

## 実行パラメータ

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| **入力ファイル** | 最新の Phase 3 出力 | posts_generated_ai_*.json |
| **承認タイムアウト** | 24時間 | タイムアウト時は推奨案を自動承認 |
| **model** | haiku | API実行のみなので軽量モデル |
| **thinking** | false | 処理速度優先 |

---

## 認証情報取得方法

### Slack MCP サーバー設定（必須）

上記「2. Slack MCP サーバー設定」セクションを参照。Webhook URLは不要です。

### LinkedIn/X API認証情報（Claude in Chrome経由で取得）

**重要**: LinkedIn/XのAPI認証情報は、Claude in Chromeを使って取得してください。

#### LinkedIn Access Token

Claude in Chromeに以下を依頼：

```
LinkedIn API認証情報を取得してください：

1. https://www.linkedin.com/developers にアクセス
2. アプリを作成（App name: "SNS Automation"）
3. OAuth 2.0認証フローを実行
4. Access TokenとPerson URNを取得
5. 環境変数に設定する形式で出力
```

詳細手順は `.claude/skills/approve-and-schedule/SKILL.md` の「認証情報取得方法」セクションを参照。

#### X (Twitter) API Credentials

Claude in Chromeに以下を依頼：

```
X API認証情報を取得してください：

1. https://developer.twitter.com/en/portal にアクセス
2. プロジェクトとアプリを作成
3. API Key, API Secret, Access Token, Access Token Secret, Bearer Tokenを取得
4. 環境変数に設定する形式で出力
```

詳細手順は `.claude/skills/approve-and-schedule/SKILL.md` の「認証情報取得方法」セクションを参照。

### Facebook（認証不要）

Claude in Chromeで直接ブラウザ操作するため、API認証情報は不要です。Facebookに通常通りログインしていれば投稿可能です。

---

## 投稿時刻のスケジューリング（オプション）

**デフォルト**: 承認後すぐに投稿

**スケジュール投稿**（SKILL.md内のコード変更が必要）:

- LinkedIn: 朝8:00 JST
- Facebook/X: 夜20:00 JST

または、cron + フラグファイルで外部スケジューリング推奨。

---

## トラブルシューティング

### Slack通知が届かない

**症状**: Slack #sns-automation に通知なし

**対処法**:
1. Webhook URLが正しいか確認
2. チャンネル名が #sns-automation であることを確認
3. Slack Appがチャンネルに追加されているか確認

**フォールバック**: Webhook失敗時はコンソール出力で3案を表示し、手動承認プロンプトが起動します。

### SNS投稿が失敗する

**症状**: `401 Unauthorized` や `403 Forbidden`

**対処法**:
1. Access Tokenの有効期限確認（LinkedIn/Facebook: 60日）
2. Developer Consoleで権限スコープ確認
3. 必要に応じて再認証

**フォールバック**: 失敗したプラットフォームはスキップされ、他のプラットフォームは正常投稿されます。

### 承認タイムアウト

**症状**: 24時間以内に承認なし

**対処法**: 自動的に推奨案（案2）が承認され、投稿されます。

---

## パフォーマンス

| 指標 | 実績 |
|------|------|
| **実行時間** | 5-10分（承認待機除く） |
| **Slack通知送信** | 2-3秒 |
| **SNS投稿（3プラットフォーム）** | 10-15秒 |
| **成功率** | 95%以上 |

---

## 次のアクション

投稿完了後、以下のアクションを実行できます：

1. **エンゲージメント追跡**: 24-48時間後にER実測値を取得
2. **予測精度検証**: 予測ER vs 実測ERの比較
3. **週次レポート**: SNSパフォーマンスレポート自動生成（未実装）

---

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## 更新履歴

- 2026-01-02: 初版作成（Phase 4実装）
  - Slack通知、インタラクティブ承認、LinkedIn/Facebook/X自動投稿対応
- 2026-01-02: 投稿方法変更
  - LinkedIn: API経由（変更なし）
  - X: API経由（変更なし）
  - Facebook: API → Claude in Chrome経由に変更
  - LinkedIn/X API認証情報取得をClaude in Chrome経由に変更
- 2026-01-02: Slack通知方法変更
  - Slack Webhook URL → Slack MCP サーバーに変更
  - インタラクティブボタン → スレッド返信（「1」「2」「3」）による承認に変更
  - Webhook URL不要、Slack MCPサーバー設定のみで動作
