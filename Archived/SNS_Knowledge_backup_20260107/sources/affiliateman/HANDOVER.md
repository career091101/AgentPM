# affiliateman プロジェクト作業引き継ぎ

## 作業日時
- 開始: 2025-12-28
- 最終更新: 2025-12-29 08:36
- 作業時間: 約12時間

---

## プロジェクト概要

**目的**: affiliatemanプロジェクトの全動画（52件）の文字起こしを取得し、RAGシステム用のチャンクデータを生成する

**プロジェクトパス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman`

---

## 現在の状況サマリー

### ✅ 完了事項

1. **文字起こし取得**: 35/53件完了（66.0%）
   - YouTube Transcript API: 30件
   - Whisper API: 6件（ZOOM 8月〜12月、3月スペース）

2. **メタデータ統合**: 完了
   - `metadata.json`に35件の動画情報を統合
   - 文字起こしファイルパスをマッピング済み

3. **RAGチャンク生成**: 完了
   - 総チャンク数: 666件
   - ブログ: 316件
   - 動画: 350件
   - 出力ファイル: `chunks/all_chunks.jsonl`

4. **品質検証**: 完了
   - 総文字数: 599,152文字
   - 日本語率: 89.5%
   - 品質問題なし

### 🔄 進行中タスク

**Whisper API処理（9件）** - バックグラウンド実行中
- プロセスID: 75262
- 実行時間: 45分経過（開始: 07:51頃）
- 状態: 2件目処理中だが遅延している
- **問題**: タイムアウト設定が効いていない可能性

### ❌ 未完了タスク

1. **ZOOM consultations（9件）** - Whisper API必要
   - 1月〜9月ZOOMコンサル（2回分含む）
   - 現在処理中だが進捗が遅い

2. **interview_videos（5件）** - YouTube ID取得不可
   - 恋愛ジャンルで月100マン稼ぐ方法
   - ニッチなジャンルで稼ぐ方法(対談)
   - 神奈川のグルメアカでPR毎月100万円稼ぐ方法
   - 少ないフォロワーで月100万稼ぐ方法
   - noteで稼ぐ方法(恋愛)
   - **原因**: サイト内ページでYouTube URLが抽出できない

3. **その他スキップ（3件）**
   - プレイリスト: 2件
   - Loom動画: 1件

---

## 重要ファイルパス

### データファイル
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/
├── video_urls_complete.json          # 全52件の動画情報
├── metadata.json                      # メタデータ（35件統合済み）
├── chunks/all_chunks.jsonl            # RAGチャンク（666件）
├── .env                               # OpenAI APIキー
└── video_transcripts/                 # 文字起こしファイル（35件）
    ├── twitter_strategy/              # 4件
    ├── monetization_marketing/        # 5件
    ├── instagram_strategy/            # 6件
    ├── twitter_monetization/          # 2件
    ├── tiktok_strategy/               # 3件
    ├── interview_videos/              # 9件
    └── zoom_consultations/            # 6件
```

### スクリプト
```
scripts/
├── check_transcript_status.py         # 現状把握スクリプト
├── youtube_transcriber_whisper_batch.py  # Whisper APIバッチ処理（修正済み）
├── integrate_video_metadata.py        # メタデータ統合
├── regenerate_chunks.py               # RAGチャンク生成
├── final_validation.py                # 最終検証
├── test_whisper_api.py                # Whisper APIテスト
├── whisper_progress.json              # Whisper進捗ファイル
├── transcript_status_report.json      # 文字起こし状況レポート
└── run_whisper_batch.sh               # Whisper実行シェル
```

### ログファイル
```
scripts/
├── whisper_final_run.log              # Whisper最終実行ログ
└── FINAL_VALIDATION_REPORT.json       # 検証レポート
```

---

## 技術的詳細

### Whisper API問題と修正内容

**発見された問題**:
1. **タイムアウトエラー**: デフォルトタイムアウトが短すぎた
   - 大きなファイル（20MB、60分動画）の処理に5-10分かかる

2. **ファイルサイズ超過**: Whisper API制限25MB
   - 初期圧縮目標23MB → 一部が25MB超過（413エラー）

**実施した修正**:
1. タイムアウト設定追加:
   ```python
   # youtube_transcriber_whisper_batch.py
   client = OpenAI(timeout=600.0)  # クライアント初期化
   transcript = client.audio.transcriptions.create(
       timeout=600.0  # create呼び出し
   )
   ```

2. 圧縮目標変更:
   ```python
   MAX_SIZE_MB = 20  # 23MB → 20MB（安全マージン）
   ```

3. .env直接読み込み:
   ```python
   env_file = PROJECT_ROOT / ".env"
   with open(env_file, 'r') as f:
       for line in f:
           key, value = line.strip().split('=', 1)
           os.environ[key] = value
   ```

### 現在実行中のコマンド
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 youtube_transcriber_whisper_batch.py --batch-size 9 --reset
```

**バックグラウンドタスクID**: b2bc763
**プロセスID**: 75262

---

## 次のアクション（優先順位順）

### 🔴 緊急: Whisper API処理確認

**現在の問題**:
- 2件目（2月ZOOMコンサル）が19分経過してもまだ完了していない
- タイムアウト設定（600秒=10分）を超過している

**推奨アクション**:

1. **プロセス状態確認**:
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts

   # プロセス確認
   ps aux | grep youtube_transcriber_whisper_batch | grep -v grep

   # 進捗確認
   cat whisper_progress.json | python3 -m json.tool

   # ログ確認
   tail -100 whisper_final_run.log
   ```

2. **プロセスキルして調査**:
   ```bash
   # プロセスキル
   kill -9 75262

   # タイムアウト設定確認（スクリプト修正が反映されているか）
   grep -n "timeout" youtube_transcriber_whisper_batch.py
   ```

3. **1件ずつテスト実行**:
   ```bash
   # より詳細なログ出力で1件ずつ実行
   python3 youtube_transcriber_whisper_batch.py --batch-size 1 --reset
   ```

### 🟡 通常: Whisper完了後の作業

Whisper処理が完了したら：

1. **メタデータ再統合**:
   ```bash
   python3 integrate_video_metadata.py
   ```

2. **RAGチャンク再生成**:
   ```bash
   python3 regenerate_chunks.py
   ```

3. **最終検証**:
   ```bash
   python3 final_validation.py
   ```

### 🟢 オプション: interview_videos対応

YouTube IDが取得できない5件の動画について：

1. **手動URL確認**:
   - video_urls_complete.jsonの該当URLをブラウザで開く
   - 実際のYouTube URLを特定
   - video_urls_complete.jsonを更新

2. **再実行**:
   ```bash
   python3 check_transcript_status.py
   python3 youtube_transcriber_whisper_batch.py --batch-size 5
   ```

---

## コスト情報

### 既知のコスト
- **Whisper API**: $0.006/分
- **推定コスト**（9件ZOOM動画）:
  - 平均60分 × 9件 = 540分
  - 540分 × $0.006 = **約$3.24**

### 現在の累積コスト
- `whisper_progress.json`の`total_cost`フィールドで確認可能
- 現状: $0.00（まだ成功0件）

---

## トラブルシューティング

### Whisper APIエラー対応

1. **APITimeoutError**:
   - timeout=600.0が設定されているか確認
   - ファイルサイズを15MB以下に再圧縮

2. **Error code: 413 (File size exceeded)**:
   - MAX_SIZE_MB = 20に設定されているか確認
   - 既存圧縮ファイルを削除: `rm /tmp/whisper_transcripts/*_compressed.mp3`

3. **APIキーエラー**:
   ```bash
   # .envファイル確認
   cat .env

   # APIキー動作確認
   python3 test_whisper_api.py
   ```

### プロセスハング時

```bash
# プロセス確認
ps aux | grep python | grep whisper

# 強制終了
kill -9 <PID>

# 進捗ファイルから再開
python3 youtube_transcriber_whisper_batch.py --resume
```

---

## 環境情報

- **Python**: 3.9
- **OS**: macOS (Darwin 25.1.0)
- **必要ライブラリ**:
  - openai
  - youtube-transcript-api
  - yt-dlp
  - ffmpeg（音声圧縮用）

---

## 完了条件

このプロジェクトは以下を満たせば完了:

1. ✅ 全動画の文字起こし取得（スキップ除く）
2. ✅ metadata.json統合
3. ✅ all_chunks.jsonl生成
4. ✅ 最終検証レポート作成
5. ⏳ Whisper API 9件完了（現在進行中）
6. ❌ interview_videos 5件対応（オプション）

**現在の完了率**: 66.0% → 目標: 94.3%（スキップ3件除く）

---

## 参考コマンド集

### 状況確認
```bash
# 文字起こしファイル数
find video_transcripts -name "*.md" -not -name "*_formatted.md" | wc -l

# カテゴリ別集計
python3 -c "
from pathlib import Path
base_dir = Path('video_transcripts')
categories = {}
for md_file in base_dir.rglob('*.md'):
    if '_formatted' not in md_file.name:
        category = md_file.parent.name
        categories[category] = categories.get(category, 0) + 1
for cat in sorted(categories.keys()):
    print(f'{cat}: {categories[cat]}件')
print(f'合計: {sum(categories.values())}件')
"

# 進捗確認
cat scripts/whisper_progress.json | python3 -m json.tool
```

### Whisper実行
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts

# 初回実行
python3 youtube_transcriber_whisper_batch.py --batch-size 9 --reset

# 再開
python3 youtube_transcriber_whisper_batch.py --resume

# コスト上限設定
python3 youtube_transcriber_whisper_batch.py --resume --max-cost 10.0
```

### 後処理
```bash
# メタデータ統合
python3 integrate_video_metadata.py

# RAGチャンク生成
python3 regenerate_chunks.py

# 最終検証
python3 final_validation.py
```

---

## 連絡事項

### 既知の問題
1. Whisper APIのタイムアウトが想定より長い（実測5-10分/件）
2. interview_videos 5件はYouTube ID抽出不可（手動対応必要）
3. プロセスがハングする可能性（長時間応答なしの場合はキル推奨）

### 注意事項
- .envファイルは.gitignoreに追加済み（APIキー保護）
- /tmp/whisper_transcripts/には大きな音声ファイルが残っている
- バックグラウンドプロセスは必ず確認してからキル

---

## 作業ログ

### 2025-12-28
- 現状把握スクリプト作成・実行
- Whisper APIスクリプト作成
- タイムアウト問題発見

### 2025-12-29
- タイムアウト設定修正（timeout=600.0追加）
- ファイルサイズ上限修正（20MB）
- メタデータ統合完了（35件）
- RAGチャンク生成完了（666件）
- 最終検証完了
- Whisper API 9件実行開始（07:51〜、進行中）

---

## 引き継ぎ後の最初のアクション

```bash
# 1. プロジェクトディレクトリに移動
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman

# 2. 現在のWhisper処理状態確認
ps aux | grep youtube_transcriber_whisper_batch | grep -v grep
cat scripts/whisper_progress.json | python3 -m json.tool

# 3. 状況に応じて判断
# - 処理中なら待機（進捗ファイル監視）
# - ハングしていればキルして再実行
# - 完了していれば後処理実行
```

---

以上が作業引き継ぎ内容です。
何か不明点があれば、このHANDOVER.mdと各スクリプトのコメントを参照してください。
