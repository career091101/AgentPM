"""
データベース管理
SQLiteを使用してユーザー、検索履歴、ダウンロード履歴を管理
Cloud Storageとの同期機能付き
"""

import sqlite3
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from contextlib import contextmanager

# データベースファイルパス
DB_PATH = Path(__file__).parent.parent.parent / "data" / "clinic_downloader.db"

# Cloud Storage設定
BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "clinic-downloader-data-project-b105c429")
DB_BLOB_NAME = "clinic_downloader.db"

def get_password_hash(password: str) -> str:
    """パスワードをハッシュ化"""
    return hashlib.sha256(password.encode()).hexdigest()

@contextmanager
def get_db():
    """データベース接続を取得"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def init_db():
    """データベース初期化"""
    with get_db() as conn:
        cursor = conn.cursor()

        # ユーザーテーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 検索履歴テーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                prefectures TEXT NOT NULL,
                keywords TEXT NOT NULL,
                min_rating REAL DEFAULT 0.0,
                min_review_count INTEGER DEFAULT 0,
                max_results INTEGER DEFAULT 500,
                total_found INTEGER DEFAULT 0,
                unique_count INTEGER DEFAULT 0,
                total_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

        # ダウンロード履歴テーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS download_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                search_history_id INTEGER,
                prefectures TEXT NOT NULL,
                keywords TEXT NOT NULL,
                file_name TEXT NOT NULL,
                record_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (search_history_id) REFERENCES search_history (id)
            )
        """)

        conn.commit()

def create_user(username: str, password: str) -> bool:
    """ユーザーを作成"""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            password_hash = get_password_hash(password)
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            return True
    except sqlite3.IntegrityError:
        # ユーザーが既に存在する場合
        return False

def verify_user(username: str, password: str) -> Optional[int]:
    """ユーザー認証（成功時はuser_idを返す）"""
    with get_db() as conn:
        cursor = conn.cursor()
        password_hash = get_password_hash(password)
        cursor.execute(
            "SELECT id FROM users WHERE username = ? AND password_hash = ?",
            (username, password_hash)
        )
        result = cursor.fetchone()
        return result['id'] if result else None

def add_search_history(
    user_id: int,
    prefectures: List[str],
    keywords: List[str],
    min_rating: float,
    min_review_count: int,
    max_results: int,
    total_found: int,
    unique_count: int,
    total_count: int
) -> int:
    """検索履歴を追加"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO search_history
            (user_id, prefectures, keywords, min_rating, min_review_count, max_results,
             total_found, unique_count, total_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            json.dumps(prefectures, ensure_ascii=False),
            json.dumps(keywords, ensure_ascii=False),
            min_rating,
            min_review_count,
            max_results,
            total_found,
            unique_count,
            total_count
        ))
        return cursor.lastrowid

def get_search_history(user_id: int, limit: int = 50) -> List[Dict]:
    """検索履歴を取得"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, prefectures, keywords, min_rating, min_review_count, max_results,
                   total_found, unique_count, total_count, created_at
            FROM search_history
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
        """, (user_id, limit))

        results = []
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'prefectures': json.loads(row['prefectures']),
                'keywords': json.loads(row['keywords']),
                'min_rating': row['min_rating'],
                'min_review_count': row['min_review_count'],
                'max_results': row['max_results'],
                'total_found': row['total_found'],
                'unique_count': row['unique_count'],
                'total_count': row['total_count'],
                'created_at': row['created_at']
            })
        return results

def add_download_history(
    user_id: int,
    search_history_id: Optional[int],
    prefectures: List[str],
    keywords: List[str],
    file_name: str,
    record_count: int
) -> int:
    """ダウンロード履歴を追加"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO download_history
            (user_id, search_history_id, prefectures, keywords, file_name, record_count)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            search_history_id,
            json.dumps(prefectures, ensure_ascii=False),
            json.dumps(keywords, ensure_ascii=False),
            file_name,
            record_count
        ))
        return cursor.lastrowid

def get_download_history(user_id: int, limit: int = 50) -> List[Dict]:
    """ダウンロード履歴を取得"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, search_history_id, prefectures, keywords, file_name,
                   record_count, created_at
            FROM download_history
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
        """, (user_id, limit))

        results = []
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'search_history_id': row['search_history_id'],
                'prefectures': json.loads(row['prefectures']),
                'keywords': json.loads(row['keywords']),
                'file_name': row['file_name'],
                'record_count': row['record_count'],
                'created_at': row['created_at']
            })
        return results

def download_db_from_gcs():
    """
    Cloud Storageからデータベースファイルをダウンロード
    ファイルが存在しない場合は何もしない（新規作成）
    """
    try:
        from google.cloud import storage

        # Cloud Storageクライアント作成
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(DB_BLOB_NAME)

        # ファイルが存在する場合のみダウンロード
        if blob.exists():
            print(f"[INFO] Downloading database from gs://{BUCKET_NAME}/{DB_BLOB_NAME}")
            DB_PATH.parent.mkdir(parents=True, exist_ok=True)
            blob.download_to_filename(str(DB_PATH))
            print(f"[INFO] Database downloaded successfully")
        else:
            print(f"[INFO] No existing database in Cloud Storage, creating new one")
    except Exception as e:
        print(f"[WARNING] Failed to download database from Cloud Storage: {e}")
        print(f"[INFO] Continuing with local database")

def upload_db_to_gcs():
    """
    データベースファイルをCloud Storageにアップロード
    """
    try:
        from google.cloud import storage

        # データベースファイルが存在しない場合はスキップ
        if not DB_PATH.exists():
            print(f"[WARNING] Database file does not exist, skipping upload")
            return

        # Cloud Storageクライアント作成
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(DB_BLOB_NAME)

        # アップロード
        print(f"[INFO] Uploading database to gs://{BUCKET_NAME}/{DB_BLOB_NAME}")
        blob.upload_from_filename(str(DB_PATH))
        print(f"[INFO] Database uploaded successfully")
    except Exception as e:
        print(f"[ERROR] Failed to upload database to Cloud Storage: {e}")

def sync_db_startup():
    """
    起動時のデータベース同期
    1. Cloud Storageからダウンロード
    2. 初期化
    3. デフォルトユーザー作成
    """
    print("[INFO] Starting database synchronization...")

    # Cloud Storageからダウンロード
    download_db_from_gcs()

    # データベース初期化
    init_db()

    # デフォルトユーザーを作成（既に存在する場合は無視される）
    create_user("tanabe", "19901101")

    print("[INFO] Database synchronization completed")

def sync_db_shutdown():
    """
    終了時のデータベース同期
    Cloud Storageにアップロード
    """
    print("[INFO] Syncing database to Cloud Storage on shutdown...")
    upload_db_to_gcs()
