#!/bin/bash

# Cloud Run デプロイスクリプト
# 歯科クリニックリストダウンローダー

set -e

# ========== 設定 ==========
PROJECT_ID="${GCP_PROJECT_ID:-your-project-id}"
SERVICE_NAME="clinic-list-downloader"
REGION="asia-northeast1"
SECRET_NAME="google-maps-api-key"

# 色付き出力
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Clinic List Downloader - Cloud Run${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ========== プロジェクトIDの確認 ==========
if [ "$PROJECT_ID" = "your-project-id" ]; then
    echo -e "${RED}Error: GCP_PROJECT_ID環境変数を設定してください${NC}"
    echo "例: export GCP_PROJECT_ID=your-actual-project-id"
    exit 1
fi

echo -e "${GREEN}✓ Project ID: ${PROJECT_ID}${NC}"
echo ""

# ========== GCPプロジェクトの設定 ==========
echo -e "${BLUE}Step 1: GCPプロジェクト設定${NC}"
gcloud config set project ${PROJECT_ID}
echo ""

# ========== 必要なAPIの有効化 ==========
echo -e "${BLUE}Step 2: 必要なAPIの有効化${NC}"
gcloud services enable \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    secretmanager.googleapis.com
echo ""

# ========== Secret Managerにキーが存在するか確認 ==========
echo -e "${BLUE}Step 3: Secret Manager確認${NC}"
if gcloud secrets describe ${SECRET_NAME} --project=${PROJECT_ID} > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Secret '${SECRET_NAME}' が存在します${NC}"
else
    echo -e "${YELLOW}⚠ Secret '${SECRET_NAME}' が存在しません${NC}"
    echo -e "${YELLOW}Google Maps API Keyを入力してください:${NC}"
    read -s API_KEY
    echo ""
    echo -n "${API_KEY}" | gcloud secrets create ${SECRET_NAME} --data-file=-
    echo -e "${GREEN}✓ Secret '${SECRET_NAME}' を作成しました${NC}"
fi
echo ""

# ========== Cloud Buildでイメージビルド ==========
echo -e "${BLUE}Step 4: Dockerイメージビルド${NC}"
gcloud builds submit \
    --tag asia-northeast1-docker.pkg.dev/${PROJECT_ID}/clinic-list-downloader/${SERVICE_NAME} \
    --timeout=20m
echo ""

# ========== Cloud Runにデプロイ ==========
echo -e "${BLUE}Step 5: Cloud Runデプロイ${NC}"
gcloud run deploy ${SERVICE_NAME} \
    --image asia-northeast1-docker.pkg.dev/${PROJECT_ID}/clinic-list-downloader/${SERVICE_NAME} \
    --region ${REGION} \
    --platform managed \
    --allow-unauthenticated \
    --memory 1Gi \
    --cpu 1 \
    --timeout 300 \
    --max-instances 10 \
    --set-secrets "GOOGLE_MAPS_API_KEY=${SECRET_NAME}:latest"
echo ""

# ========== デプロイ完了 ==========
SERVICE_URL=$(gcloud run services describe ${SERVICE_NAME} --region ${REGION} --format='value(status.url)')

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  デプロイ完了！${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${GREEN}サービスURL:${NC}"
echo -e "${BLUE}${SERVICE_URL}${NC}"
echo ""
echo -e "${YELLOW}初回ログイン情報:${NC}"
echo -e "  Username: tanabe"
echo -e "  Password: 19901101"
echo ""
