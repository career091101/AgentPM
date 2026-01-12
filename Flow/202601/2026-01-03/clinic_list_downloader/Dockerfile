# ========== Stage 1: フロントエンドビルド ==========
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# package.jsonをコピーして依存関係をインストール
COPY frontend/package*.json ./
RUN npm ci

# フロントエンドソースをコピーしてビルド
COPY frontend/ ./
RUN npm run build

# ========== Stage 2: バックエンド ==========
FROM python:3.11-slim

WORKDIR /app

# Pythonパッケージインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# バックエンドコードをコピー
COPY backend/ ./backend/

# フロントエンドビルド成果物をコピー
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# データディレクトリを作成（SQLiteデータベース用）
RUN mkdir -p /app/data

# 環境変数の設定
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# ポート8080を公開（Cloud Run デフォルト）
EXPOSE 8080

# uvicornでアプリケーションを起動
CMD ["uvicorn", "backend.app.api:app", "--host", "0.0.0.0", "--port", "8080"]
