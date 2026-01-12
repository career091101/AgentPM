# ローカルテスト報告書

**日時**: 2026-01-03
**テスト環境**: macOS、Python 3.14、Node.js 18

## テスト結果サマリー

✅ **すべてのテスト項目が正常に完了しました**

## テスト手順

### 1. フロントエンド依存関係インストール
```bash
cd frontend && npm install
```
**結果**: ✅ 成功（133パッケージインストール完了）

### 2. フロントエンドビルド
```bash
npm run build
```
**結果**: ✅ 成功（5.83秒でビルド完了）
- 出力: `frontend/dist/`
- ファイルサイズ:
  - `index.html`: 0.46 kB
  - `index-B1F8_yBX.css`: 11.61 kB
  - `index-ChJSFr1x.js`: 150.33 kB

### 3. バックエンド依存関係インストール
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**結果**: ✅ 成功（全依存関係インストール完了）

**インストールされたパッケージ**:
- fastapi 0.128.0
- uvicorn 0.40.0
- pydantic 2.12.5
- pydantic-core 2.41.5（事前ビルド済みwheel使用）
- starlette 0.50.0
- その他依存関係

**注意**: 初回試行時にpydantic-core 2.14.6のRustコンパイルエラーが発生しましたが、requirements.txtを`>=`バージョン指定に変更することで、最新版（2.41.5）の事前ビルド済みwheelを使用し、問題を解決しました。

### 4. バックエンド起動
```bash
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8080
```
**結果**: ✅ 正常起動

**起動ログ**:
```
INFO:     Started server process [87192]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
✅ Serving frontend from: /Users/yuichi/.../frontend/dist
⚠️  WARNING: GOOGLE_MAPS_API_KEY is not set
   The API will not work without a valid API key
```

## エンドポイントテスト

### ✅ ルートエンドポイント（/）
**期待**: Reactアプリのindex.htmlが配信される
**結果**: ✅ 成功

```html
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>歯科クリニック住所正規化ツール</title>
    <script type="module" src="/assets/index-ChJSFr1x.js"></script>
    <link rel="stylesheet" href="/assets/index-B1F8_yBX.css">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

### ✅ ヘルスチェックエンドポイント（/health）
**期待**: API keyの設定状態を含むヘルスチェック情報が返る
**結果**: ✅ 成功

```json
{
  "status": "healthy",
  "api_key_configured": false
}
```

### ✅ API Docsエンドポイント（/docs）
**期待**: Swagger UIが表示される
**結果**: ✅ 成功

```html
<!DOCTYPE html>
<html>
<head>
<link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
...
</head>
```

## 問題と解決策

### 問題1: pydantic-core 2.14.6のRustコンパイルエラー

**エラー内容**:
```
error: failed to run custom build command for `pydantic-core v2.14.6`
```

**原因**: Python 3.14で古いバージョンのpydantic-coreをソースからビルドしようとした際、Rustコンパイラの互換性問題が発生。

**解決策**: requirements.txtのバージョン指定を`==`から`>=`に変更し、最新版（2.12.5）の事前ビルド済みwheelを使用。

**変更前**:
```
pydantic==2.5.3
```

**変更後**:
```
pydantic>=2.5.0
```

### 問題2: ルートエンドポイント（/）でAPIレスポンスが返る

**エラー内容**: `curl http://localhost:8080/` でReactアプリではなく、APIのJSONレスポンスが返る。

**原因**: `@app.get("/")`エンドポイントが静的ファイルマウントよりも優先されていた。

**解決策**: `@app.get("/")`エンドポイントを削除し、静的ファイルマウントのみで処理。

**変更前**:
```python
@app.get("/")
async def root():
    return {"message": "Clinic Address Normalizer API", ...}

# 静的ファイルマウント
app.mount("/", StaticFiles(directory=...), name="static")
```

**変更後**:
```python
# ルートエンドポイント削除

# 静的ファイルマウント（これがルートパスをキャッチ）
app.mount("/", StaticFiles(directory=...), name="static")
```

### 問題3: Pydantic警告 "schema_extra has been renamed to json_schema_extra"

**警告内容**:
```
UserWarning: Valid config keys have changed in V2:
* 'schema_extra' has been renamed to 'json_schema_extra'
```

**原因**: Pydantic v2で`schema_extra`が`json_schema_extra`に変更された。

**解決策**: `schema_extra`を`json_schema_extra`に変更。

**変更前**:
```python
class Config:
    schema_extra = {"example": {...}}
```

**変更後**:
```python
class Config:
    json_schema_extra = {"example": {...}}
```

## 実際のAPI動作確認の制限事項

**Google Maps API keyが未設定のため、`/api/normalize`エンドポイントの実際の動作は確認していません。**

API keyを設定後、以下のテストを実行してください：

```bash
# API keyを設定
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"

# バックエンド起動
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8080

# 単一施設正規化テスト
curl -X POST http://localhost:8080/api/normalize \
  -H "Content-Type: application/json" \
  -d '{
    "clinic_query": "田中歯科クリニック",
    "prefecture": "東京都",
    "city": "渋谷区",
    "area_hint": "恵比寿"
  }'
```

## 総合評価

### ✅ 動作確認済み項目
1. フロントエンドビルド成功
2. バックエンド依存関係インストール成功
3. サーバー起動成功
4. 静的ファイル配信成功（Reactアプリ）
5. ヘルスチェックエンドポイント動作
6. API Docs（Swagger UI）表示

### ⚠️ 未確認項目（API key必要）
1. `/api/normalize`エンドポイントの実際の動作
2. Google Maps APIとの連携
3. エラーハンドリングの動作

## 次のステップ

### 1. Google Maps API keyを設定してフル機能テスト
```bash
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8080
```

ブラウザで`http://localhost:8080`にアクセスし、以下をテスト：
- 医院名・都道府県を入力して正規化実行
- 結果表示（住所、郵便番号、座標、信頼度）
- エラーハンドリング

### 2. Cloud Runデプロイ

ローカルテストが完了したら、Phase 3のCloud Runデプロイに進んでください：

```bash
# GCPプロジェクト設定
gcloud config set project YOUR_PROJECT_ID

# API有効化
gcloud services enable run.googleapis.com secretmanager.googleapis.com

# APIキー登録
echo -n "YOUR_GOOGLE_MAPS_API_KEY" | \
  gcloud secrets create google-maps-api-key --data-file=-

# デプロイ
gcloud run deploy clinic-normalizer \
  --source . \
  --region asia-northeast1 \
  --allow-unauthenticated \
  --set-secrets "GOOGLE_MAPS_API_KEY=google-maps-api-key:latest"
```

## 参考情報

- 計画ファイル: `~/.claude/plans/majestic-imagining-cray.md`
- 開発手順: `DEVELOPMENT.md`
- 既存実装: `main.py`（452行、100%再利用）
