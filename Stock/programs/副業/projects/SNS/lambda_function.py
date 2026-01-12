"""
AWS Lambda用エントリーポイント
EventBridge（CloudWatch Events）から毎日AM 9:00 JSTにトリガー
"""

import json
import sys
from pathlib import Path

# プロジェクトルートをPATHに追加
sys.path.append(str(Path(__file__).parent))

# 既存スクリプトをインポート
from scripts.daily_analytics_collection import main as collect_analytics


def lambda_handler(event, context):
    """
    AWS Lambda ハンドラー関数（S3同期版）

    Args:
        event: EventBridgeからのイベントデータ
        context: Lambdaランタイム情報

    Returns:
        dict: ステータスコードとメッセージ
    """
    try:
        print(f"Starting analytics collection at {context.request_id}")

        # STEP 1: S3からデータベースをダウンロード
        from scripts.s3_sync import download_db_from_s3, upload_db_to_s3

        db_existed = download_db_from_s3()
        print(f"Database existed in S3: {db_existed}")

        # STEP 2: アナリティクス収集実行
        result = collect_analytics()

        # STEP 3: 更新されたデータベースをS3へアップロード
        upload_success = upload_db_to_s3()
        if not upload_success:
            raise Exception("Failed to upload database to S3")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Analytics collection completed successfully',
                'request_id': context.request_id,
                'db_existed': db_existed,
                'result': result
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Analytics collection failed',
                'error': str(e),
                'request_id': context.request_id
            })
        }


# ローカルテスト用
if __name__ == "__main__":
    class MockContext:
        request_id = "local-test"

    result = lambda_handler({}, MockContext())
    print(json.dumps(result, indent=2))
