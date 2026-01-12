# BigQuery MCP Setup Guide

Week 6 Day 3-4: BigQuery MCP統合のためのGCP設定ガイド

## 概要

Claude CodeからBigQuery APIを操作するために、GCPサービスアカウントを作成し、必要な認証情報を取得します。

---

## 前提条件

- Google Cloud Platformアカウント
- GCPプロジェクト（既存または新規作成）
- BigQueryの有効化

---

## Step 1: GCPプロジェクトの準備

### 1-1. GCPコンソールにアクセス

https://console.cloud.google.com/ にアクセス。

### 1-2. プロジェクトの選択または作成

- 既存プロジェクトを使用する場合: 左上のプロジェクト選択ドロップダウンから選択
- 新規プロジェクト作成の場合: 「新しいプロジェクト」をクリック

### 1-3. BigQuery APIの有効化

1. 左サイドバーから「APIとサービス」→「ライブラリ」
2. 「BigQuery API」を検索
3. 「有効にする」をクリック

---

## Step 2: サービスアカウントの作成

### 2-1. サービスアカウントページにアクセス

https://console.cloud.google.com/iam-admin/serviceaccounts にアクセス。

### 2-2. サービスアカウント作成

「サービスアカウントを作成」をクリック。

| フィールド | 値 |
|----------|-----|
| **サービスアカウント名** | `claude-code-bigquery` |
| **サービスアカウントID** | 自動生成（例: `claude-code-bigquery@your-project.iam.gserviceaccount.com`） |
| **説明** | `Claude Code BigQuery MCP Server` |

「作成して続行」をクリック。

### 2-3. ロール（権限）の付与

以下のロールを付与：

| ロール | 説明 | 必須度 |
|--------|------|--------|
| **BigQuery データ閲覧者** | テーブル・データセット情報の取得、クエリ実行（読み取り専用） | 必須 |
| **BigQuery ジョブユーザー** | クエリジョブの実行権限 | 必須 |
| **BigQuery データ編集者** | データの挿入・更新・削除 | オプション（書き込みが必要な場合） |

推奨設定（読み取り専用）:
1. 「BigQuery データ閲覧者」を選択
2. 「BigQuery ジョブユーザー」を追加
3. 「続行」をクリック

### 2-4. サービスアカウントの完了

「完了」をクリック（ユーザーへのアクセス権付与はスキップ可）。

---

## Step 3: JSONキーファイルのダウンロード

### 3-1. キー作成

1. 作成したサービスアカウント（`claude-code-bigquery@...`）をクリック
2. 「キー」タブを選択
3. 「鍵を追加」→「新しい鍵を作成」
4. 「JSON」を選択
5. 「作成」をクリック

JSONファイルが自動ダウンロードされます（例: `your-project-abc123.json`）。

### 3-2. キーファイルの保存

ダウンロードしたJSONファイルを安全な場所に保存：

```bash
# プロジェクトルートのcredentialsディレクトリに保存（推奨）
mkdir -p /Users/yuichi/AIPM/aipm_v0/credentials
mv ~/Downloads/your-project-abc123.json /Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json

# パーミッション設定（自分のみ読み取り可能）
chmod 600 /Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
```

---

## Step 4: プロジェクトIDの取得

### 4-1. GCPコンソールで確認

GCPコンソールのダッシュボード（https://console.cloud.google.com/）で、プロジェクトIDを確認。

例: `my-project-123456`

### 4-2. gcloudコマンドで確認

```bash
gcloud config get-value project
```

---

## Step 5: 環境変数の設定

### 5-1. .envファイルに追加

プロジェクトルートの`.env`ファイルに以下を追加：

```bash
# BigQuery MCP Integration (Week 6 Day 3-4)
GOOGLE_APPLICATION_CREDENTIALS=/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
GCP_PROJECT_ID=my-project-123456
```

**重要**: `GOOGLE_APPLICATION_CREDENTIALS`は**絶対パス**を指定すること。

### 5-2. credentials/ディレクトリを.gitignoreに追加

```bash
# .gitignore に追加
credentials/
```

---

## Step 6: Pythonパッケージのインストール

BigQuery MCPサーバーが依存する`google-cloud-bigquery`パッケージをインストール：

```bash
# Homebrew経由でインストール（推奨）
brew install google-cloud-bigquery

# または pip経由（venv推奨）
python3 -m venv .venv
source .venv/bin/activate
pip install google-cloud-bigquery
```

---

## Step 7: 動作確認（手動テスト）

### 7-1. Python APIでテスト

```python
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    '/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json'
)

client = bigquery.Client(credentials=credentials, project='my-project-123456')

# データセット一覧取得
datasets = list(client.list_datasets())
for dataset in datasets:
    print(f"Dataset: {dataset.dataset_id}")
```

成功すれば、プロジェクト内のデータセット一覧が表示されます。

---

## セキュリティベストプラクティス

### 1. キーファイルの保護

- **絶対にGitにコミットしない**（`.gitignore`に`credentials/`を追加）
- **パーミッション制限**（`chmod 600`で自分のみ読み取り可能）
- **定期的にローテーション**（6ヶ月ごとに再生成推奨）

### 2. 最小権限の原則

- 読み取り専用でよい場合は「BigQuery データ閲覧者」のみ付与
- 書き込みが必要な場合のみ「BigQuery データ編集者」を追加
- 管理者権限（「BigQuery 管理者」）は付与しない

### 3. サービスアカウントの分離

- プロジェクトごと、環境（dev/staging/prod）ごとに異なるサービスアカウントを使用
- キーの混在を避ける

---

## トラブルシューティング

### 問題1: `PermissionDenied` エラー

**症状**: クエリ実行時に権限エラー

**原因**: サービスアカウントに必要なロールが付与されていない

**解決策**:
1. GCPコンソール → IAMと管理 → サービスアカウント
2. 該当サービスアカウントの権限を確認
3. 「BigQuery データ閲覧者」と「BigQuery ジョブユーザー」を付与

---

### 問題2: `GOOGLE_APPLICATION_CREDENTIALS` not found

**症状**: 環境変数が認識されない

**原因**: パスが相対パスになっている

**解決策**:
```bash
# ❌ 相対パス（動作しない）
GOOGLE_APPLICATION_CREDENTIALS=credentials/bigquery-service-account.json

# ✅ 絶対パス（正しい）
GOOGLE_APPLICATION_CREDENTIALS=/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
```

---

### 問題3: `google-cloud-bigquery` import エラー

**症状**: `ModuleNotFoundError: No module named 'google.cloud'`

**原因**: パッケージ未インストール

**解決策**:
```bash
pip install google-cloud-bigquery
```

---

## セキュリティベストプラクティス

### 1. SQLインジェクション対策

BigQuery MCPサーバーは以下のセキュリティ対策を実装しています：

**実装済み保護機能**:
- SQLコメント（`--`, `/* */`）のブロック
- 危険なSQL文のブロック（DROP, DELETE, TRUNCATE, ALTER, EXEC）
- スキーマ探索クエリのブロック（INFORMATION_SCHEMA）
- 権限変更文のブロック（GRANT, REVOKE）
- クエリタイムアウト設定（300秒）

**安全な使用例**:
```sql
-- ✅ 安全なクエリ（SELECTのみ）
SELECT * FROM dataset.table WHERE date >= '2024-01-01' LIMIT 100

-- ❌ ブロックされるクエリ
SELECT * FROM dataset.table; DROP TABLE dataset.table;
SELECT * FROM dataset.table -- comment injection
```

### 2. 認証情報の保護

**必須設定**:
1. `credentials/`ディレクトリは`.gitignore`で除外済み
2. サービスアカウントキーは絶対にGitにコミットしない
3. `.env`ファイルでパスを管理（`.gitignore`済み）

**安全なファイル配置**:
```
/Users/yuichi/AIPM/aipm_v0/
├── credentials/               # ← .gitignoreで除外
│   └── bigquery-sa-key.json  # ← サービスアカウントキー
├── .env                       # ← .gitignoreで除外
│   └── GOOGLE_APPLICATION_CREDENTIALS=/absolute/path/to/key.json
└── scripts/
    └── mcp_servers/
        └── bigquery_server.py # ← キーは含まない
```

### 3. 最小権限の原則

サービスアカウントには必要最小限の権限のみを付与：

| 操作 | 必要な権限 | 推奨ロール |
|------|-----------|-----------|
| データセット一覧 | `bigquery.datasets.get` | BigQuery User |
| テーブル一覧 | `bigquery.tables.list` | BigQuery User |
| クエリ実行 | `bigquery.jobs.create` | BigQuery User |
| スキーマ取得 | `bigquery.tables.get` | BigQuery User |

**❌ 避けるべき設定**:
- `roles/bigquery.admin` - 管理者権限は不要
- `roles/owner` - プロジェクト所有者権限は危険

---

## 次のステップ

BigQuery設定完了後、以下のファイルで動作確認：

1. **動作確認スクリプト**: `scripts/test_bigquery_mcp.sh`（作成予定）
2. **MCP設定**: `.mcp.json` に `bigquery` サーバーが追加済み
3. **Claude Code起動**: Claude Code内でBigQuery APIを操作可能

---

## 参照

- **BigQuery Documentation**: https://cloud.google.com/bigquery/docs
- **Service Account Best Practices**: https://cloud.google.com/iam/docs/best-practices-service-accounts
- **Python Client Library**: https://cloud.google.com/python/docs/reference/bigquery/latest
- **Week 6実装ガイド**: @docs/implementation_guides/week6_mcp.md
