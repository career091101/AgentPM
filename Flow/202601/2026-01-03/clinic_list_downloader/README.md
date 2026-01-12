# 歯科クリニックリストCSVダウンローダー

都道府県単位で歯科クリニックを検索し、CSV形式でダウンロードできるWebアプリケーション。

Google Maps Places API (New) を使用して、クリニック名、住所、郵便番号、電話番号、ウェブサイトURLを取得します。

## プロジェクト概要

- **データソース**: Google Maps API only
- **検索範囲**: 都道府県単位（例: 「東京都」→ 都内の全歯科クリニック）
- **出力フィールド**:
  - clinic_name（クリニック名）
  - address（住所）
  - postal_code（郵便番号）
  - phone_number（電話番号）
  - website_url（ウェブサイトURL）
- **データ量**: 中規模（100-1,000件/検索）

## アーキテクチャ

- **Backend**: Python 3.11 + FastAPI + Uvicorn
- **Frontend**: React 18 + TypeScript + Vite（Phase 2で実装予定）
- **Deployment**: Google Cloud Run（Phase 4で実装予定）

## ファイル構成

```
clinic_list_downloader/
├── README.md
├── requirements.txt
│
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── api.py                  # FastAPIエンドポイント
│       └── search_strategies.py    # 都道府県別クエリ生成
│
└── frontend/                       # Phase 2で実装
    └── src/
```

## セットアップ

### 1. 環境変数設定

Google Maps API Keyを環境変数に設定：

```bash
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
```

### 2. 依存パッケージインストール

```bash
pip install -r requirements.txt
```

## 使用方法

### ローカル起動

```bash
# プロジェクトディレクトリに移動
cd /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/clinic_list_downloader

# uvicornでAPI起動
uvicorn backend.app.api:app --reload --host 0.0.0.0 --port 8000
```

起動後、以下のURLにアクセス：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API使用例

#### 1. POST /api/search（クリニック検索）

```bash
curl -X POST "http://localhost:8000/api/search" \
  -H "Content-Type: application/json" \
  -d '{"prefecture": "東京都"}'
```

レスポンス例：
```json
{
  "prefecture": "東京都",
  "total_count": 120,
  "clinics": [
    {
      "place_id": "ChIJ...",
      "clinic_name": "〇〇歯科クリニック",
      "address": "東京都千代田区...",
      "postal_code": "100-0001",
      "phone_number": "03-1234-5678",
      "website_url": "https://example.com"
    },
    ...
  ]
}
```

#### 2. GET /api/export（CSV エクスポート）

```bash
curl "http://localhost:8000/api/export?prefecture=東京都" \
  --output dental_clinics_tokyo.csv
```

ダウンロードされるCSVファイル：
```csv
clinic_name,address,postal_code,phone_number,website_url
〇〇歯科クリニック,東京都千代田区...,100-0001,03-1234-5678,https://example.com
△△デンタルクリニック,東京都中央区...,104-0061,03-2345-6789,https://example2.com
...
```

## 技術仕様

### Google Maps API使用状況

| API | 用途 | 料金 |
|-----|------|------|
| Places Text Search (New) | クリニック検索 | $32/1,000リクエスト |
| Place Details (New) | 郵便番号取得 | $17/1,000リクエスト |

### 都道府県別クエリ戦略

Text Search APIは1クエリ最大20件制限のため、都道府県を市区町村に分割して複数クエリを実行：

| 都道府県 | クエリ数 | 推定件数 |
|---------|---------|---------|
| 東京都 | 37クエリ（23区+主要市） | 500+件 |
| 大阪府 | 33クエリ | 450+件 |
| 神奈川県 | 15クエリ | 200+件 |
| 鳥取県 | 1クエリ（単一） | 15件 |

重複排除: place_idでデデュプリケーション

### CSV エンコーディング

- **文字コード**: UTF-8 BOM（Excel互換）
- **改行コード**: CRLF（Windows互換）
- **フィールド区切り**: カンマ（,）

## 開発ロードマップ

### Phase 1: MVPバックエンド（Week 1-2、完了）

- ✅ プロジェクトセットアップ
- ✅ POST /api/search実装
- ✅ GET /api/export実装
- ✅ 都道府県別クエリ戦略（主要13都道府県）

### Phase 2: MVPフロントエンド（Week 2-3、未着手）

- [ ] Vite + React + TypeScript セットアップ
- [ ] UIコンポーネント実装
  - [ ] PrefectureSelector
  - [ ] SearchButton
  - [ ] ResultsTable
  - [ ] DownloadButton
- [ ] API統合
- [ ] Tailwind CSSスタイリング

### Phase 3: 拡張検索機能（Week 3-4、未着手）

- [ ] 47都道府県の完全マッピング
- [ ] 複数クエリ実行＋重複排除
- [ ] プログレスバー実装
- [ ] エラーハンドリング強化

### Phase 4: Cloud Runデプロイ（Week 4-5、未着手）

- [ ] Dockerfile作成
- [ ] Secret Manager設定
- [ ] デプロイ実行
- [ ] 本番テスト

## トラブルシューティング

### API Key not configured

```bash
# 環境変数が設定されているか確認
echo $GOOGLE_MAPS_API_KEY

# 未設定の場合
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY"
```

### Rate Limit (429 エラー)

指数バックオフでリトライ（最大5回、2^n秒待機）を実装済み。

### websiteUri 取得率が低い

websiteUriは60-70%のクリニックでのみ利用可能。空欄の場合はGoogleマップURLで代替可能（今後の拡張予定）。

## 既存実装の再利用

以下の関数を既存の `clinic_address_normalizer/main.py` から再利用：

- `exponential_backoff_retry()`: リトライロジック
- `extract_postal_code_from_address_components()`: 郵便番号抽出

## ライセンス

MIT License

## 作成者

- AIPM v0 Project
- 2026-01-03
