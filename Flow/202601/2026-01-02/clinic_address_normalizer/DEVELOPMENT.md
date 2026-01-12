# 開発・テスト手順

## 前提条件

### 必須ソフトウェア
- Python 3.11以上
- Node.js 18以上
- npm 9以上

### Google Maps API キー
環境変数 `GOOGLE_MAPS_API_KEY` を設定してください。

```bash
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
```

または、`.env` ファイルを作成：

```bash
# .env ファイル
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
```

## ローカル開発環境のセットアップ

### 1. Pythonバックエンドのセットアップ

```bash
# 仮想環境作成
python3 -m venv venv

# 仮想環境有効化
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows

# 依存関係インストール
pip install -r requirements.txt
```

### 2. Reactフロントエンドのセットアップ

```bash
cd frontend

# 依存関係インストール
npm install

# 開発サーバー起動（オプション）
npm run dev  # ポート3000で起動
```

## ローカルテスト実行

### 方法1: バックエンド単体テスト（推奨）

バックエンドのみを起動し、フロントエンドをビルドして配信：

```bash
# 1. フロントエンドビルド
cd frontend
npm install
npm run build
cd ..

# 2. バックエンド起動（静的ファイルも配信）
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8080 --reload

# 3. ブラウザでアクセス
open http://localhost:8080
```

**確認項目:**
- ✅ ルートページ（`http://localhost:8080/`）でReactアプリが表示される
- ✅ ヘルスチェック（`http://localhost:8080/health`）が正常に応答
- ✅ API Docs（`http://localhost:8080/docs`）でSwagger UIが表示される
- ✅ フォームから医院名・都道府県を入力して正規化が実行できる

### 方法2: バックエンド＋フロントエンド分離開発

開発中にホットリロードを使いたい場合：

**ターミナル1: バックエンド**
```bash
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8080 --reload
```

**ターミナル2: フロントエンド**
```bash
cd frontend
npm run dev  # ポート3000で起動
```

**ブラウザ:**
- フロントエンド: `http://localhost:3000`
- バックエンドAPI: `http://localhost:8080`

**注意:** この方法では、フロントエンド（3000）からバックエンド（8080）へのAPIリクエストはViteのプロキシ経由で転送されます（`vite.config.ts` で設定済み）。

### 方法3: Dockerコンテナでテスト

本番環境に最も近い方法：

```bash
# Dockerイメージビルド
docker build -t clinic-normalizer .

# コンテナ起動
docker run -p 8080:8080 -e GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE" clinic-normalizer

# ブラウザでアクセス
open http://localhost:8080
```

## テストケース

### 単一施設の正規化テスト

以下の入力でテストしてください：

#### テストケース1: 基本動作確認
- **医院名**: 田中歯科クリニック
- **都道府県**: 東京都
- **市区町村**: 渋谷区
- **地域ヒント**: 恵比寿
- **期待結果**: 信頼度 "high"、住所・郵便番号・座標が正常に取得される

#### テストケース2: 曖昧な名前
- **医院名**: さくら歯科
- **都道府県**: 東京都
- **市区町村**: （空白）
- **期待結果**: 複数候補から最適なものを選択、信頼度 "mid" または "low"

#### テストケース3: Google Maps URL指定
- **医院名**: （任意）
- **都道府県**: （任意）
- **Google Maps URL**: `https://maps.app.goo.gl/XXXXX`
- **期待結果**: URLから直接place_idを抽出、信頼度 "high"

#### テストケース4: 存在しない医院
- **医院名**: 存在しない歯科医院12345
- **都道府県**: 東京都
- **期待結果**: エラーメッセージ表示、`error_code` に値が設定される

### API直接テスト（curl）

```bash
# ヘルスチェック
curl http://localhost:8080/health

# 単一施設正規化
curl -X POST http://localhost:8080/api/normalize \
  -H "Content-Type: application/json" \
  -d '{
    "clinic_query": "田中歯科クリニック",
    "prefecture": "東京都",
    "city": "渋谷区",
    "area_hint": "恵比寿"
  }'
```

## トラブルシューティング

### エラー: "GOOGLE_MAPS_API_KEY environment variable is not set"

**原因:** API keyが環境変数に設定されていない

**解決策:**
```bash
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
# または .env ファイルを作成
```

### エラー: "Frontend dist directory not found"

**原因:** フロントエンドがビルドされていない

**解決策:**
```bash
cd frontend
npm install
npm run build
```

### エラー: "ModuleNotFoundError: No module named 'fastapi'"

**原因:** Python依存関係がインストールされていない

**解決策:**
```bash
pip install -r requirements.txt
```

### ポート8080が既に使用されている

**解決策:**
```bash
# 別のポートを使用
uvicorn backend.app.main_api:app --host 0.0.0.0 --port 8081

# または、既存のプロセスを終了
lsof -ti:8080 | xargs kill -9
```

## 次のステップ

ローカルテストが完了したら、以下の手順でCloud Runにデプロイできます：

1. GCPプロジェクト作成
2. Secret ManagerにAPIキー登録
3. Cloud Runデプロイ

詳細は計画ファイル（`~/.claude/plans/majestic-imagining-cray.md`）のPhase 3を参照してください。

## 参考

- FastAPI公式ドキュメント: https://fastapi.tiangolo.com/
- React公式ドキュメント: https://react.dev/
- Vite公式ドキュメント: https://vitejs.dev/
- Google Maps Platform: https://developers.google.com/maps
