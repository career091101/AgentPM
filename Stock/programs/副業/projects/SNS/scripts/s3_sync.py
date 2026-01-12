#!/usr/bin/env python3
"""
S3とSQLiteデータベースを同期するスクリプト
Lambda実行前にS3からダウンロード、実行後にS3へアップロード
"""

import boto3
import os
from pathlib import Path
from datetime import datetime

# 設定
S3_BUCKET = os.environ.get("S3_BUCKET", "sns-analytics-backup")
DB_FILENAME = "analytics.db"
BASE_DIR = Path(__file__).parent.parent
LOCAL_DB_PATH = BASE_DIR / "data" / DB_FILENAME
S3_DB_KEY = f"databases/{DB_FILENAME}"


def download_db_from_s3():
    """S3からデータベースをダウンロード"""
    s3_client = boto3.client('s3')

    try:
        print(f"Downloading {S3_DB_KEY} from S3...")
        s3_client.download_file(S3_BUCKET, S3_DB_KEY, str(LOCAL_DB_PATH))
        print(f"✓ Downloaded to {LOCAL_DB_PATH}")
        return True

    except s3_client.exceptions.NoSuchKey:
        print(f"⚠ Database not found in S3. Creating new database...")
        return False

    except Exception as e:
        print(f"✗ Download failed: {str(e)}")
        return False


def upload_db_to_s3():
    """データベースをS3へアップロード"""
    s3_client = boto3.client('s3')

    try:
        print(f"Uploading {LOCAL_DB_PATH} to S3...")

        # バックアップキー（タイムスタンプ付き）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_key = f"databases/backups/{DB_FILENAME}.{timestamp}"

        # 現行版アップロード
        s3_client.upload_file(
            str(LOCAL_DB_PATH),
            S3_BUCKET,
            S3_DB_KEY,
            ExtraArgs={'ContentType': 'application/x-sqlite3'}
        )
        print(f"✓ Uploaded to s3://{S3_BUCKET}/{S3_DB_KEY}")

        # バックアップアップロード
        s3_client.upload_file(
            str(LOCAL_DB_PATH),
            S3_BUCKET,
            backup_key,
            ExtraArgs={'ContentType': 'application/x-sqlite3'}
        )
        print(f"✓ Backup saved to s3://{S3_BUCKET}/{backup_key}")

        return True

    except Exception as e:
        print(f"✗ Upload failed: {str(e)}")
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python s3_sync.py [download|upload]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "download":
        success = download_db_from_s3()
    elif action == "upload":
        success = upload_db_to_s3()
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

    sys.exit(0 if success else 1)
