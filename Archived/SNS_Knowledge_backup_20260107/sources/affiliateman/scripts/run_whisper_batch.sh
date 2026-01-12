#!/bin/bash

# .envファイルから環境変数を読み込み
if [ -f "../.env" ]; then
    set -a
    source ../.env
    set +a
else
    echo "⚠ .envファイルが見つかりません"
    exit 1
fi

# Pythonスクリプトを実行
python3 youtube_transcriber_whisper_batch.py "$@"
