# ========== Stage 1: フロントエンドビルド ==========
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# package.jsonとpackage-lock.jsonをコピー（依存関係のキャッシュ最適化）
COPY frontend/package*.json ./

# 依存関係インストール
RUN npm ci

# フロントエンドソースコードをコピー
COPY frontend/ ./

# ビルド実行
RUN npm run build

# ========== Stage 2: Pythonバックエンド ==========
FROM python:3.11-slim

# 作業ディレクトリ設定
WORKDIR /app

# Pythonパッケージインストール（キャッシュ最適化）
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 既存main.pyとバックエンドコピー
COPY main.py ./
COPY backend/ ./backend/

# フロントエンドビルド成果物をコピー
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# 環境変数設定
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# ポート公開
EXPOSE 8080

# ヘルスチェック
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8080/health')"

# アプリケーション起動
CMD uvicorn backend.app.main_api:app --host 0.0.0.0 --port ${PORT}
