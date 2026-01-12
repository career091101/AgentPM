# Cloud Run デプロイガイド

歯科クリニックリストダウンローダーをGoogle Cloud Runにデプロイする手順です。

## 前提条件

- Google Cloud Platform (GCP) アカウント
- Google Cloud SDK (`gcloud`) インストール済み
- Google Maps Platform API Key

## デプロイ手順

### 1. 環境変数の設定

```bash
export GCP_PROJECT_ID=your-actual-project-id
```

### 2. デプロイスクリプトの実行

```bash
./deploy.sh
```

スクリプトは以下を自動実行します:

1. **GCPプロジェクト設定**: プロジェクトIDを設定
2. **必要なAPIの有効化**:
   - Cloud Run API
   - Cloud Build API
   - Secret Manager API
3. **Secret Manager設定**: Google Maps API Keyを安全に保存
4. **Dockerイメージビルド**: Cloud Buildでイメージ作成
5. **Cloud Runデプロイ**: サービスをデプロイ

### 3. デプロイ完了

デプロイが完了すると、サービスURLが表示されます:

```
https://clinic-list-downloader-xxxxx-an.a.run.app
```

## 初回ログイン情報

- **ユーザー名**: `tanabe`
- **パスワード**: `19901101`

## ローカルテスト（オプション）

Cloud Runにデプロイする前に、ローカルでDockerイメージをテストできます:

```bash
# Dockerイメージのビルド
docker build -t clinic-list-downloader .

# コンテナの実行
docker run -p 8080:8080 \
  -e GOOGLE_MAPS_API_KEY=your-api-key \
  clinic-list-downloader

# ブラウザでアクセス
open http://localhost:8080
```

## アーキテクチャ

```
┌─────────────────────────────────┐
│  Cloud Run Container            │
│  ┌───────────────────────────┐  │
│  │ Uvicorn (Port 8080)       │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ FastAPI Backend     │  │  │
│  │  │ - Authentication    │  │  │
│  │  │ - SSE Streaming     │  │  │
│  │  │ - Search History    │  │  │
│  │  │ - Download History  │  │  │
│  │  └─────────────────────┘  │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ Static Files        │  │  │
│  │  │ (React Frontend)    │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ SQLite Database           │  │
│  │ (/app/data/clinic.db)     │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
          ↓
┌─────────────────────────────────┐
│  Secret Manager                 │
│  - GOOGLE_MAPS_API_KEY          │
└─────────────────────────────────┘
          ↓
┌─────────────────────────────────┐
│  Google Maps Platform API       │
│  - Places API (New)             │
└─────────────────────────────────┘
```

## リソース設定

- **メモリ**: 1Gi
- **CPU**: 1 vCPU
- **タイムアウト**: 300秒
- **最大インスタンス数**: 10
- **認証**: 不要 (allow-unauthenticated)

## コスト試算

### Cloud Run
- **無料枠**: 月間200万リクエスト、360,000 vCPU秒
- **超過時**: 約$0.24/100万リクエスト

### Google Maps Platform API
- **Places Text Search**: $32/1,000リクエスト
- **例**: 月100検索（中規模県）→ 約$48/月

### 合計コスト例
- **軽量使用**: $0-10/月（無料枠内）
- **中程度**: $50-100/月（100-200検索/月）

## トラブルシューティング

### デプロイエラー: "API not enabled"

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com
```

### デプロイエラー: "Permission denied"

```bash
gcloud projects add-iam-policy-binding ${GCP_PROJECT_ID} \
  --member="user:your-email@example.com" \
  --role="roles/run.admin"
```

### アプリエラー: "GOOGLE_MAPS_API_KEY not configured"

Secret Managerの設定を確認:

```bash
gcloud secrets versions access latest --secret="google-maps-api-key"
```

### データベースが保存されない

Cloud Runはステートレスなので、データベースは永続化されません。
本番環境では以下のいずれかを検討:

1. **Cloud SQL**: PostgreSQL/MySQLデータベース
2. **Cloud Firestore**: NoSQLデータベース
3. **Cloud Storage**: SQLiteファイルの永続化

## アップデート

コードを修正した後、再デプロイ:

```bash
./deploy.sh
```

Cloud Buildが自動的に新しいイメージをビルドし、Cloud Runにデプロイします。

## 削除

サービスの削除:

```bash
gcloud run services delete clinic-list-downloader --region asia-northeast1
```

Secretの削除:

```bash
gcloud secrets delete google-maps-api-key
```

## 参照

- [Cloud Run公式ドキュメント](https://cloud.google.com/run/docs)
- [Google Maps Platform料金](https://developers.google.com/maps/billing-and-pricing/pricing)
