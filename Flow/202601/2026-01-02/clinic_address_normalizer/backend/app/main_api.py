"""
FastAPI Backend for Clinic Address Normalizer

既存のmain.pyのprocess_row()関数を再利用して、WebAPIとして公開します。
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sys
import os
from pathlib import Path

# 既存main.pyをインポートするためのパス設定
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from main import process_row

# FastAPIアプリケーション初期化
app = FastAPI(
    title="Clinic Address Normalizer API",
    description="Google Maps API を使った医院データ正規化ツール",
    version="1.0.0"
)

# CORS設定（本番環境では特定のオリジンに制限すべき）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番では制限すること
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ========== Pydanticモデル定義 ==========

class NormalizeRequest(BaseModel):
    """正規化リクエストモデル"""
    clinic_query: str
    prefecture: str
    city: str = ""
    area_hint: str = ""
    google_maps_url: str = ""

    class Config:
        json_schema_extra = {
            "example": {
                "clinic_query": "田中歯科クリニック",
                "prefecture": "東京都",
                "city": "渋谷区",
                "area_hint": "恵比寿",
                "google_maps_url": ""
            }
        }


class NormalizeResponse(BaseModel):
    """正規化レスポンスモデル"""
    # 入力データ
    clinic_query: str
    prefecture: str
    city: str
    area_hint: str
    google_maps_url: str

    # 出力データ
    place_id: str
    display_name: str
    formatted_address: str
    postal_code: str
    lat: str
    lng: str
    match_confidence: str  # high/mid/low
    needs_manual_review: str  # true/false
    error_code: str
    error_message: str


# ========== APIエンドポイント ==========

@app.get("/health")
async def health():
    """ヘルスチェックエンドポイント（Cloud Run用）"""
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

    return {
        "status": "healthy",
        "api_key_configured": bool(api_key)
    }


@app.post("/api/normalize", response_model=NormalizeResponse)
async def normalize_single(req: NormalizeRequest):
    """
    単一施設の住所正規化

    既存のmain.pyのprocess_row()関数を呼び出して処理します。
    """
    # API keyの確認
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GOOGLE_MAPS_API_KEY environment variable is not set"
        )

    # リクエストを辞書に変換（既存のprocess_row()はDictを受け取る）
    row = req.dict()

    try:
        # 既存のprocess_row()を直接呼び出し
        result = process_row(row, api_key)

        return NormalizeResponse(**result)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )


# ========== アプリケーション起動時の処理 ==========

@app.on_event("startup")
async def startup_event():
    """アプリケーション起動時の処理"""
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        print("⚠️  WARNING: GOOGLE_MAPS_API_KEY is not set")
        print("   The API will not work without a valid API key")
    else:
        print("✅ GOOGLE_MAPS_API_KEY is configured")


# ========== 静的ファイル配信 ==========

# フロントエンドの静的ファイルを配信（最後にマウント）
# SPAのルーティングをサポート（html=True）
frontend_dist_path = Path(__file__).parent.parent.parent / "frontend" / "dist"
if frontend_dist_path.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist_path), html=True), name="static")
    print(f"✅ Serving frontend from: {frontend_dist_path}")
else:
    print(f"⚠️  WARNING: Frontend dist directory not found: {frontend_dist_path}")
    print("   Run 'npm run build' in the frontend directory to build the frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
