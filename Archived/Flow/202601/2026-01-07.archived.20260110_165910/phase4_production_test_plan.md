# Phase 4: 本番API投稿テスト計画

**作成日時**: 2026-01-07
**目的**: Late APIを使用したX & Threads同時予約投稿の本番動作確認

---

## テスト環境

### 前提条件

- ✅ Late APIアカウント登録済み
- ✅ X（Twitter）アカウント連携済み
- ✅ Threadsアカウント連携済み
- ✅ Late API認証情報設定済み（`config/late_api_config.json`）

### 必要ファイル

1. **Late API設定**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`
2. **テスト画像**: `Stock/programs/副業/projects/SNS/test_data/sample_image.png`
3. **テストスクリプト**: `Stock/programs/副業/projects/SNS/scripts/production_test.py`（新規作成）

---

## テストシナリオ

### Scenario 1: テキストのみ投稿（最小構成）

**目的**: 基本的なX & Threads同時予約投稿の動作確認

**入力**:
- X投稿: 7ツイートスレッド（各140文字以内）
- Threads投稿: 1投稿（400文字、3絵文字、2段落）
- 予約日時: 翌日20:00 JST
- 画像: なし

**期待結果**:
- Late API `/posts`エンドポイントへの2回のPOSTリクエスト成功
- X投稿: `post_id`取得、`scheduledFor`が翌日20:00 JSTに設定
- Threads投稿: `post_id`取得、`scheduledFor`が翌日20:00 JSTに設定
- Late APIダッシュボード（https://app.getlate.dev/posts）に2件の予約投稿が表示

**成功基準**:
- HTTPステータス: 200 OK（両方）
- レスポンスに`post_id`が含まれる
- スケジュール日時が正しく設定されている
- エラーログに記録がない

---

### Scenario 2: 画像付き投稿（フル機能）

**目的**: 画像アップロード機能を含む完全なフロー確認

**入力**:
- X投稿: 7ツイートスレッド + 画像1枚
- Threads投稿: 1投稿 + 同一画像
- 予約日時: 翌々日20:00 JST（Scenario 1と重複回避）
- 画像: `test_data/sample_image.png`（PNG形式、500KB以下）

**期待結果**:
- 画像アップロード成功（`/media`エンドポイント）
- Late APIから画像URLを取得
- X投稿: 画像URL付きで予約成功
- Threads投稿: 同一画像URL付きで予約成功
- Late APIダッシュボードに画像プレビュー表示

**成功基準**:
- 画像アップロードHTTPステータス: 200 OK
- レスポンスに`url`フィールドが含まれる
- 両投稿のペイロードに`media: [{'url': '...'}]`が含まれる
- ダッシュボードで画像が正しく表示される

---

### Scenario 3: スケジュール競合テスト

**目的**: 既存予約投稿との競合検出・回避機能の確認

**ステップ**:
1. Scenario 1で翌日20:00 JSTに予約投稿を作成
2. 同じ日時に再度予約を試行
3. `find_available_slot()`が翌々日20:00 JSTにスキップすることを確認

**期待結果**:
- `get_existing_reservations()`が既存予約を検出
- `find_available_slot()`が重複日をスキップ
- 新規予約が翌々日20:00 JSTに設定される

**成功基準**:
- ログに「既存予約検出: YYYY-MM-DD」が記録される
- 新規予約の日時が既存予約と異なる
- 競合エラーが発生しない

---

### Scenario 4: エラーハンドリング & リトライ

**目的**: ネットワークエラー時のリトライロジック確認

**テスト方法**:
- 一時的にWi-Fi切断 → リトライ → 再接続
- または Late APIのRate Limit（429）を意図的に発生させる

**期待結果**:
- `NetworkTimeoutError`または`RateLimitError`が発生
- 指数バックオフ（10秒 → 20秒 → 40秒）でリトライ
- 最大3回リトライ後に失敗を記録
- エラーログに詳細情報が保存

**成功基準**:
- リトライ回数がログに記録される
- 最終的に成功または明確なエラーメッセージ
- システムがクラッシュしない

---

## テスト実行手順

### STEP 1: Late API設定確認（1分）

```bash
# Late API設定ファイルの存在確認
cat Stock/programs/副業/projects/SNS/config/late_api_config.json

# 期待される内容:
# {
#   "api_key": "sk_...",
#   "base_url": "https://getlate.dev/api/v1",
#   "accounts": {
#     "twitter": {"accountId": "...", "platform": "twitter"},
#     "threads": {"accountId": "...", "platform": "threads"}
#   }
# }
```

**確認項目**:
- ✅ `api_key`が設定されている（`sk_`で始まる）
- ✅ `twitter`と`threads`の`accountId`が設定されている

---

### STEP 2: テスト画像準備（2分）

```bash
# テストデータディレクトリ作成
mkdir -p Stock/programs/副業/projects/SNS/test_data

# サンプル画像のダウンロードまたは作成
# （既存の画像を使用する場合はコピー）
cp /path/to/your/image.png Stock/programs/副業/projects/SNS/test_data/sample_image.png

# ファイルサイズ確認（500KB以下推奨）
ls -lh Stock/programs/副業/projects/SNS/test_data/sample_image.png
```

---

### STEP 3: 本番テストスクリプト作成（5分）

**新規ファイル**: `Stock/programs/副業/projects/SNS/scripts/production_test.py`

内容は次のステップで作成します。

---

### STEP 4: Scenario 1実行（テキストのみ）（3分）

```bash
cd Stock/programs/副業/projects/SNS

# ドライラン（Late APIへの実際のPOSTなし）
python3 scripts/production_test.py --scenario 1 --dry-run

# 本番実行
python3 scripts/production_test.py --scenario 1
```

**期待出力**:
```
========================================
Scenario 1: テキストのみ投稿
========================================

[X投稿]
✅ 予約投稿成功
Post ID: 67abc123def456...
Scheduled: 2026-01-08 20:00:00 JST
URL: https://app.getlate.dev/posts/67abc123def456...

[Threads投稿]
✅ 予約投稿成功
Post ID: 67abc789ghi012...
Scheduled: 2026-01-08 20:00:00 JST
URL: https://app.getlate.dev/posts/67abc789ghi012...

========================================
✅ Scenario 1 完了
========================================
```

---

### STEP 5: Late APIダッシュボード確認（2分）

1. ブラウザで https://app.getlate.dev/posts にアクセス
2. 2件の予約投稿が表示されることを確認
   - X投稿（スレッド形式）
   - Threads投稿（単一投稿）
3. スケジュール日時が翌日20:00 JSTであることを確認
4. ステータスが「Scheduled」であることを確認

---

### STEP 6: Scenario 2実行（画像付き）（5分）

```bash
# 画像パスを指定して実行
python3 scripts/production_test.py --scenario 2 --image test_data/sample_image.png
```

**期待出力**:
```
========================================
Scenario 2: 画像付き投稿
========================================

[画像アップロード]
✅ アップロード成功
Image URL: https://cdn.getlate.dev/media/abc123...

[X投稿]
✅ 予約投稿成功（画像付き）
Post ID: 67def456ghi789...
Scheduled: 2026-01-09 20:00:00 JST

[Threads投稿]
✅ 予約投稿成功（画像付き）
Post ID: 67jkl012mno345...
Scheduled: 2026-01-09 20:00:00 JST

========================================
✅ Scenario 2 完了
========================================
```

---

### STEP 7: ダッシュボードで画像確認（2分）

1. Late APIダッシュボードで新しい2件の投稿を確認
2. 画像プレビューが表示されることを確認
3. 両投稿に同一画像が添付されていることを確認

---

### STEP 8: エラーログ確認（1分）

```bash
# エラーログの確認
cat Stock/programs/副業/projects/SNS/logs/error_log_20260107.jsonl

# 成功ログの確認
cat Stock/programs/副業/projects/SNS/logs/success_log_20260107.jsonl
```

**期待結果**:
- エラーログにエントリがない（または警告のみ）
- 成功ログに4件のエントリがある（Scenario 1: 2件、Scenario 2: 2件）

---

## 成功基準サマリー

| テスト項目 | 成功基準 |
|----------|---------|
| **Scenario 1** | X & Threads両方とも予約成功、`post_id`取得 |
| **Scenario 2** | 画像アップロード成功、両投稿に画像添付 |
| **Scenario 3** | 競合検出・日付スキップ機能動作 |
| **Scenario 4** | エラー時のリトライロジック動作 |
| **ダッシュボード** | 予約投稿が正しく表示される |
| **ログ** | エラーログなし、成功ログに全件記録 |

---

## トラブルシューティング

### 問題1: 401 Unauthorized

**原因**: Late API `api_key`が無効または期限切れ

**解決策**:
1. Late APIダッシュボード（https://app.getlate.dev/settings/api）でAPIキーを再生成
2. `config/late_api_config.json`を更新
3. テスト再実行

---

### 問題2: 404 Not Found (Account ID)

**原因**: `twitter`または`threads`の`accountId`が無効

**解決策**:
1. Late APIダッシュボード（https://app.getlate.dev/settings/accounts）でアカウントIDを確認
2. `config/late_api_config.json`を更新
3. テスト再実行

---

### 問題3: 画像アップロード失敗

**原因**: ファイルサイズ超過、サポートされていないフォーマット

**解決策**:
1. 画像サイズを500KB以下に圧縮
2. PNG/JPEGフォーマットを使用
3. テスト再実行

---

### 問題4: スケジュール日時が過去

**原因**: システム時刻のタイムゾーン設定ミス

**解決策**:
1. `LateAPIScheduler`が`Asia/Tokyo`タイムゾーンを使用していることを確認
2. `datetime.now(ZoneInfo('Asia/Tokyo'))`で現在時刻を確認
3. `find_available_slot()`の戻り値を検証

---

## 次のステップ

Phase 4完了後の推奨アクション:

1. **24時間後**: 実際に投稿が実行されたか確認
2. **エンゲージメント測定**: X & Threads両方の反応を記録
3. **Phase 5計画**: A/Bテスト機能の設計開始

---

**作成者**: Claude Code Agent
**バージョン**: Phase 4 v1.0
**最終更新**: 2026-01-07
