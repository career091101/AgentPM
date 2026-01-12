"""
歯科クリニックリストダウンローダー - FastAPI Backend

Google Maps Places API (New) を使用して都道府県単位で歯科クリニックを検索し、
CSV形式でダウンロードできるAPIを提供します。
"""

import os
import io
import csv
import sys
import time
import requests
from pathlib import Path
from typing import List, Dict, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse
import asyncio
import json as json_lib

# ローカルモジュールのインポート
from .search_strategies import get_search_queries
from .auth import get_current_user, verify_credentials, User, LoginRequest
from . import database

# ========== 設定 ==========
API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
PLACES_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"
PLACE_DETAILS_URL_TEMPLATE = "https://places.googleapis.com/v1/places/{place_id}"
TIMEOUT = 20
MAX_RETRIES = 5

# ========== ライフサイクル管理 ==========

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    アプリケーションのライフサイクル管理
    起動時と終了時の処理を定義
    """
    # 起動時の処理
    print("[INFO] Application startup...")
    database.sync_db_startup()
    print("[INFO] Application ready")

    yield  # アプリケーション実行中

    # 終了時の処理
    print("[INFO] Application shutdown...")
    database.sync_db_shutdown()
    print("[INFO] Shutdown complete")

# ========== FastAPI App ==========
app = FastAPI(
    title="Dental Clinic List Downloader",
    description="都道府県単位で歯科クリニックを検索してCSVダウンロード",
    version="1.0.0",
    lifespan=lifespan
)

# CORS設定（ローカルフロントエンド開発用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite/React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== Pydantic Models ==========

class SearchRequest(BaseModel):
    """検索リクエスト"""
    prefectures: List[str]  # 都道府県名リスト（例: ["東京都", "大阪府"]）
    keywords: List[str] = ["歯科クリニック"]  # 検索キーワードリスト（例: ["歯科クリニック", "デンタルクリニック"]）
    min_rating: float = 0.0  # 最小評価スコア（0.0-5.0）
    min_review_count: int = 0  # 最小口コミ件数
    max_results: int = 1000  # 最大抽出件数（デフォルト: 1000件）

class ClinicData(BaseModel):
    """クリニック情報"""
    place_id: str
    clinic_name: str
    address: str
    postal_code: str
    phone_number: str
    website_url: str
    rating: float  # 評価スコア（0.0-5.0）
    user_rating_count: int  # 口コミ件数

class SearchProgress(BaseModel):
    """検索進捗情報"""
    total_queries: int  # 総クエリ数
    completed_queries: int  # 完了クエリ数
    total_found: int  # 見つかったクリニック数（重複含む）
    unique_count: int  # 重複排除後の件数
    current_prefecture: str = ""  # 現在処理中の都道府県
    current_keyword: str = ""  # 現在処理中のキーワード

class SearchResponse(BaseModel):
    """検索レスポンス"""
    prefectures: List[str]  # 検索した都道府県リスト
    keywords: List[str]  # 使用したキーワードリスト
    total_count: int
    clinics: List[ClinicData]
    progress: SearchProgress  # 検索進捗情報

# ========== ヘルパー関数 ==========

def exponential_backoff_retry(func, *args, max_retries: int = 5, **kwargs):
    """
    指数バックオフでリトライを実行

    Args:
        func: 実行する関数
        *args: 関数の位置引数
        max_retries: 最大リトライ回数
        **kwargs: 関数のキーワード引数

    Returns:
        関数の実行結果、またはNone（失敗時）
    """
    for attempt in range(max_retries):
        try:
            response = func(*args, **kwargs)
            if response.status_code == 200:
                return response
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Max retries reached: {e}")
                return None
            wait_time = (2 ** attempt) + (time.time() % 1)
            print(f"Retry {attempt + 1}/{max_retries} after {wait_time:.2f}s")
            time.sleep(wait_time)
    return None

def extract_postal_code_from_address_components(components: List[Dict]) -> str:
    """
    addressComponents から郵便番号を抽出

    Args:
        components: addressComponents リスト

    Returns:
        郵便番号（7桁）、見つからない場合は空文字列
    """
    for component in components:
        types = component.get("types", [])
        if "postal_code" in types:
            postal_code = component.get("longText", "")
            # ハイフンを除去
            postal_code = postal_code.replace("-", "").replace("〒", "")
            return postal_code
    return ""

def search_clinics_in_area(query: str, api_key: str, max_results: int = 20) -> List[Dict]:
    """
    指定エリアで歯科クリニックを検索

    Args:
        query: 検索クエリ（例: "歯科クリニック 東京都 千代田区"）
        api_key: Google Maps API Key
        max_results: 最大取得件数（デフォルト20件、API制限）

    Returns:
        クリニック情報のリスト
    """
    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.nationalPhoneNumber,places.websiteUri,places.rating,places.userRatingCount"
    }
    body = {
        "textQuery": query,
        "languageCode": "ja",
        "maxResultCount": max_results
    }

    try:
        response = exponential_backoff_retry(
            requests.post,
            PLACES_SEARCH_URL,
            headers=headers,
            json=body,
            timeout=TIMEOUT
        )

        if response and response.status_code == 200:
            data = response.json()
            return data.get("places", [])

    except Exception as e:
        print(f"  [ERROR] Places Text Search failed for query '{query}': {e}")

    return []

def get_place_details_postal_code(place_id: str, api_key: str) -> str:
    """
    Place Details APIで郵便番号を取得

    Args:
        place_id: Google Maps Place ID
        api_key: Google Maps API Key

    Returns:
        郵便番号（取得できない場合は空文字列）
    """
    url = PLACE_DETAILS_URL_TEMPLATE.format(place_id=place_id)
    headers = {
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "addressComponents"
    }
    params = {"languageCode": "ja"}

    try:
        response = exponential_backoff_retry(
            requests.get,
            url,
            headers=headers,
            params=params,
            timeout=TIMEOUT
        )

        if response and response.status_code == 200:
            data = response.json()
            components = data.get("addressComponents", [])
            postal_code = extract_postal_code_from_address_components(components)
            if postal_code:
                return postal_code

    except Exception as e:
        print(f"  [ERROR] Place Details failed for {place_id}: {e}")

    return ""

def search_clinics_by_prefecture(prefecture: str, keywords: List[str], api_key: str) -> List[Dict]:
    """
    都道府県単位で歯科クリニックを検索（複数キーワード対応）

    複数クエリ実行＋重複排除により、100-1,000件の取得を実現。

    Args:
        prefecture: 都道府県名（例: "東京都"）
        keywords: 検索キーワードリスト（例: ["歯科クリニック", "デンタルクリニック"]）
        api_key: Google Maps API Key

    Returns:
        クリニック情報のリスト（重複排除済み）
    """
    # place_idで重複排除
    unique_places = {}
    total_queries = 0

    # 各キーワードで検索
    for keyword in keywords:
        # 都道府県別クエリリストを取得
        queries = get_search_queries(prefecture, keyword)
        total_queries += len(queries)
        print(f"[INFO] Searching {prefecture} with keyword '{keyword}': {len(queries)} queries")

        # 各クエリを実行
        for i, query in enumerate(queries, 1):
            print(f"[INFO] Query {i}/{len(queries)}: {query}")
            places = search_clinics_in_area(query, api_key, max_results=20)

            # 重複排除しながら追加
            for place in places:
                place_id = place.get("id")
                if place_id and place_id not in unique_places:
                    unique_places[place_id] = place

            # レート制限対策: 短い待機
            if i < len(queries):
                time.sleep(0.1)

    print(f"[INFO] Found {len(unique_places)} unique clinics in {prefecture} (total queries: {total_queries})")
    return list(unique_places.values())

def parse_clinic_data(place: Dict, api_key: str) -> ClinicData:
    """
    Places APIレスポンスからクリニック情報を抽出

    Args:
        place: Places API レスポンスの1要素
        api_key: Google Maps API Key

    Returns:
        ClinicData オブジェクト
    """
    place_id = place.get("id", "")
    clinic_name = place.get("displayName", {}).get("text", "")
    address = place.get("formattedAddress", "")
    phone_number = place.get("nationalPhoneNumber", "")
    website_url = place.get("websiteUri", "")
    rating = place.get("rating", 0.0)
    user_rating_count = place.get("userRatingCount", 0)

    # 郵便番号は Place Details API で取得
    postal_code = get_place_details_postal_code(place_id, api_key)

    return ClinicData(
        place_id=place_id,
        clinic_name=clinic_name,
        address=address,
        postal_code=postal_code,
        phone_number=phone_number,
        website_url=website_url,
        rating=rating,
        user_rating_count=user_rating_count
    )

# ========== API Endpoints ==========

@app.get("/api/health")
def health_check():
    """ヘルスチェック"""
    return {"status": "ok", "message": "Dental Clinic List Downloader API"}

@app.post("/api/login")
def login(request: LoginRequest):
    """
    ログイン

    Args:
        request: ログインリクエスト（username, password）

    Returns:
        ログイン成功時のユーザー情報

    Raises:
        HTTPException: 認証失敗時
    """
    user = verify_credentials(request.username, request.password)

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "user_id": user.user_id,
        "username": user.username,
        "message": "Login successful"
    }

@app.get("/api/search-history")
def get_user_search_history(current_user: User = Depends(get_current_user)):
    """
    検索履歴を取得（認証必須）

    Args:
        current_user: 現在のユーザー（依存性注入）

    Returns:
        検索履歴のリスト
    """
    history = database.get_search_history(current_user.user_id)
    return {"search_history": history}

@app.get("/api/download-history")
def get_user_download_history(current_user: User = Depends(get_current_user)):
    """
    ダウンロード履歴を取得（認証必須）

    Args:
        current_user: 現在のユーザー（依存性注入）

    Returns:
        ダウンロード履歴のリスト
    """
    history = database.get_download_history(current_user.user_id)
    return {"download_history": history}

@app.post("/api/search", response_model=SearchResponse)
def search_clinics(request: SearchRequest):
    """
    複数都道府県で歯科クリニックを検索

    Args:
        request: SearchRequest（prefectures必須）

    Returns:
        SearchResponse（クリニックリスト）

    Raises:
        HTTPException: API Keyが未設定、または検索失敗時
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="GOOGLE_MAPS_API_KEY not configured")

    if not request.prefectures or len(request.prefectures) == 0:
        raise HTTPException(status_code=400, detail="At least one prefecture must be selected")

    try:
        # プログレス情報の初期化
        total_queries = 0
        completed_queries = 0
        total_found = 0

        # 複数都道府県の検索結果を統合（place_idで重複排除）
        all_places = {}

        for prefecture in request.prefectures:
            print(f"[INFO] Searching {prefecture}...")
            places = search_clinics_by_prefecture(prefecture, request.keywords, API_KEY)
            total_found += len(places)

            # 重複排除しながら追加
            for place in places:
                place_id = place.get("id")
                if place_id and place_id not in all_places:
                    all_places[place_id] = place

        unique_count = len(all_places)
        print(f"[INFO] Found {unique_count} unique clinics across {len(request.prefectures)} prefecture(s)")

        # パース & フィルタリング
        clinics = []
        for place in all_places.values():
            clinic = parse_clinic_data(place, API_KEY)

            # フィルタリング: 評価スコアと口コミ件数
            if clinic.rating >= request.min_rating and clinic.user_rating_count >= request.min_review_count:
                clinics.append(clinic)

        print(f"[INFO] Filtered {len(clinics)} clinics (rating >= {request.min_rating}, reviews >= {request.min_review_count})")

        # 最大件数制限
        if len(clinics) > request.max_results:
            # 評価スコア順でソート（高い順）
            clinics.sort(key=lambda x: (x.rating, x.user_rating_count), reverse=True)
            clinics = clinics[:request.max_results]
            print(f"[INFO] Limited to {request.max_results} clinics (sorted by rating)")

        # プログレス情報を作成
        progress = SearchProgress(
            total_queries=len(request.prefectures) * len(request.keywords),
            completed_queries=len(request.prefectures) * len(request.keywords),
            total_found=total_found,
            unique_count=unique_count,
            current_prefecture="完了",
            current_keyword="完了"
        )

        return SearchResponse(
            prefectures=request.prefectures,
            keywords=request.keywords,
            total_count=len(clinics),
            clinics=clinics,
            progress=progress
        )

    except Exception as e:
        print(f"[ERROR] Search failed: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

@app.get("/api/export")
def export_csv(
    prefectures: str = "東京都",  # カンマ区切りの都道府県リスト
    keywords: str = "歯科クリニック",  # カンマ区切りのキーワードリスト
    min_rating: float = 0.0,
    min_review_count: int = 0,
    max_results: int = 1000,
    current_user: User = Depends(get_current_user)
):
    """
    検索結果をCSVでエクスポート

    Args:
        prefectures: 都道府県名（カンマ区切り、例: "東京都,大阪府"）
        keywords: 検索キーワード（カンマ区切り、例: "歯科クリニック,デンタルクリニック"）
        min_rating: 最小評価スコア（0.0-5.0）
        min_review_count: 最小口コミ件数

    Returns:
        StreamingResponse（CSV file）
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="GOOGLE_MAPS_API_KEY not configured")

    try:
        # カンマ区切りを配列に変換
        prefecture_list = [p.strip() for p in prefectures.split(",")]
        keyword_list = [k.strip() for k in keywords.split(",")]

        # 複数都道府県の検索結果を統合
        all_places = {}

        for prefecture in prefecture_list:
            places = search_clinics_by_prefecture(prefecture, keyword_list, API_KEY)

            # 重複排除しながら追加
            for place in places:
                place_id = place.get("id")
                if place_id and place_id not in all_places:
                    all_places[place_id] = place

        # CSV生成用データ準備
        clinics_for_export = []
        for place in all_places.values():
            clinic = parse_clinic_data(place, API_KEY)

            # フィルタリング: 評価スコアと口コミ件数
            if clinic.rating >= min_rating and clinic.user_rating_count >= min_review_count:
                clinics_for_export.append(clinic)

        # 最大件数制限（評価スコア順）
        if len(clinics_for_export) > max_results:
            clinics_for_export.sort(key=lambda x: (x.rating, x.user_rating_count), reverse=True)
            clinics_for_export = clinics_for_export[:max_results]

        # CSV生成
        output = io.StringIO()
        output.write('\ufeff')  # UTF-8 BOM (Excel互換)

        fieldnames = ["clinic_name", "address", "postal_code", "phone_number", "website_url", "rating", "user_rating_count"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for clinic in clinics_for_export:
            writer.writerow({
                "clinic_name": clinic.clinic_name,
                "address": clinic.address,
                "postal_code": clinic.postal_code,
                "phone_number": clinic.phone_number,
                "website_url": clinic.website_url,
                "rating": clinic.rating,
                "user_rating_count": clinic.user_rating_count
            })

        # ポインタをリセット
        output.seek(0)

        # ファイル名生成
        if len(prefecture_list) == 1:
            filename = f"dental_clinics_{prefecture_list[0]}.csv"
        else:
            filename = f"dental_clinics_multiple_{len(prefecture_list)}prefectures.csv"

        # ダウンロード履歴を保存
        database.add_download_history(
            user_id=current_user.user_id,
            search_history_id=None,  # 直接ダウンロードの場合はNone
            prefectures=prefecture_list,
            keywords=keyword_list,
            file_name=filename,
            record_count=len(clinics_for_export)
        )

        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'}
        )

    except Exception as e:
        print(f"[ERROR] Export failed: {e}")
        raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")

@app.post("/api/search/stream")
async def search_clinics_stream(request: SearchRequest, current_user: User = Depends(get_current_user)):
    """
    Server-Sent Eventsを使用したリアルタイム検索

    Args:
        request: SearchRequest
        current_user: 現在のユーザー（認証必須）

    Returns:
        EventSourceResponse: SSEストリーム
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="GOOGLE_MAPS_API_KEY not configured")

    if not request.prefectures or len(request.prefectures) == 0:
        raise HTTPException(status_code=400, detail="At least one prefecture must be selected")

    async def event_generator():
        try:
            # 初期化イベント
            total_queries = len(request.prefectures) * len(request.keywords)
            completed_queries = 0
            total_found = 0
            all_places = {}

            yield {
                "event": "start",
                "data": json_lib.dumps({
                    "total_queries": total_queries,
                    "message": "検索を開始しました"
                })
            }

            # 各都道府県を検索
            for pref_idx, prefecture in enumerate(request.prefectures, 1):
                # 各キーワードで検索
                for keyword_idx, keyword in enumerate(request.keywords, 1):
                    # 進捗イベント送信
                    yield {
                        "event": "progress",
                        "data": json_lib.dumps({
                            "total_queries": total_queries,
                            "completed_queries": completed_queries,
                            "total_found": total_found,
                            "unique_count": len(all_places),
                            "current_prefecture": prefecture,
                            "current_keyword": keyword
                        })
                    }

                    # 検索実行（同期処理を非同期で実行）
                    await asyncio.sleep(0)  # イベントループに制御を戻す
                    queries = get_search_queries(prefecture, keyword)

                    for query_idx, query in enumerate(queries, 1):
                        # クエリ実行
                        places = search_clinics_in_area(query, API_KEY, max_results=20)

                        # 重複排除しながら追加
                        for place in places:
                            place_id = place.get("id")
                            if place_id and place_id not in all_places:
                                all_places[place_id] = place
                                total_found += 1

                        # サブクエリ進捗イベント送信
                        sub_progress = ((completed_queries * len(queries)) + query_idx) / (total_queries * len(queries))
                        yield {
                            "event": "sub_progress",
                            "data": json_lib.dumps({
                                "prefecture": prefecture,
                                "keyword": keyword,
                                "query_index": query_idx,
                                "query_total": len(queries),
                                "sub_progress": sub_progress,
                                "total_found": total_found,
                                "unique_count": len(all_places)
                            })
                        }

                        # レート制限対策
                        if query_idx < len(queries):
                            await asyncio.sleep(0.1)

                    completed_queries += 1

                    # キーワード完了イベント
                    yield {
                        "event": "keyword_complete",
                        "data": json_lib.dumps({
                            "prefecture": prefecture,
                            "keyword": keyword,
                            "completed_queries": completed_queries,
                            "total_queries": total_queries,
                            "unique_count": len(all_places)
                        })
                    }

            # パース & フィルタリング
            clinics = []
            for place in all_places.values():
                clinic = parse_clinic_data(place, API_KEY)

                # フィルタリング
                if clinic.rating >= request.min_rating and clinic.user_rating_count >= request.min_review_count:
                    clinics.append(clinic)

            # 最大件数制限
            if len(clinics) > request.max_results:
                clinics.sort(key=lambda x: (x.rating, x.user_rating_count), reverse=True)
                clinics = clinics[:request.max_results]

            # 検索履歴を保存
            search_history_id = database.add_search_history(
                user_id=current_user.user_id,
                prefectures=request.prefectures,
                keywords=request.keywords,
                min_rating=request.min_rating,
                min_review_count=request.min_review_count,
                max_results=request.max_results,
                total_found=total_found,
                unique_count=len(all_places),
                total_count=len(clinics)
            )

            # 完了イベント
            yield {
                "event": "complete",
                "data": json_lib.dumps({
                    "search_history_id": search_history_id,
                    "total_count": len(clinics),
                    "unique_count": len(all_places),
                    "total_found": total_found,
                    "clinics": [clinic.dict() for clinic in clinics],
                    "progress": {
                        "total_queries": total_queries,
                        "completed_queries": completed_queries,
                        "total_found": total_found,
                        "unique_count": len(all_places),
                        "current_prefecture": "完了",
                        "current_keyword": "完了"
                    }
                })
            }

        except Exception as e:
            # エラーイベント
            yield {
                "event": "error",
                "data": json_lib.dumps({
                    "error": str(e),
                    "message": "検索中にエラーが発生しました"
                })
            }

    return EventSourceResponse(event_generator())

# ========== 静的ファイル配信 ==========

# フロントエンドビルド成果物を配信（本番環境のみ）
frontend_dist = Path(__file__).parent.parent.parent / "frontend" / "dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="static")
    print(f"[INFO] Serving frontend from {frontend_dist}")

# ========== エントリポイント ==========

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
