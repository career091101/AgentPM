# Late API統合セットアップガイド

## 1. Late APIアカウント作成

1. **Late APIダッシュボードにアクセス**: https://app.getlate.dev/
2. **サインアップ**: メールアドレスまたはGoogle/GitHub認証
3. **プラン選択**:
   - 推奨: **Proプラン**（$49/月）
   - 対応プラットフォーム: 12（X, LinkedIn, Facebook, Threads, Instagram等）
   - スケジュール投稿無制限

## 2. プラットフォーム接続

### 2.1 LinkedIn接続

1. Late APIダッシュボード → "Accounts" → "Connect LinkedIn"
2. LinkedIn認証画面でログイン
3. アクセス許可承認
4. アカウントIDをコピー（例: `ln_abc123xyz`）

### 2.2 X/Twitter接続

1. Late APIダッシュボード → "Accounts" → "Connect Twitter"
2. X認証画面でログイン
3. アクセス許可承認
4. アカウントIDをコピー（例: `tw_abc123xyz`）

### 2.3 Facebook接続

1. Late APIダッシュボード → "Accounts" → "Connect Facebook"
2. Facebook認証画面でログイン
3. ページ選択（ビジネスページ推奨）
4. アカウントIDをコピー（例: `fb_abc123xyz`）

### 2.4 Threads接続

1. Late APIダッシュボード → "Accounts" → "Connect Threads"
2. Instagram認証画面でログイン（ThreadsはInstagramアカウント必須）
3. アクセス許可承認
4. アカウントIDをコピー（例: `th_abc123xyz`）

## 3. API Key取得

1. Late APIダッシュボード → "Settings" → "API Keys"
2. "Create New Key"をクリック
3. キー名入力（例: `sns-automation-production`）
4. API Keyをコピー（例: `sk_abc123xyz...`）
5. **重要**: API Keyは1度しか表示されないため、必ず安全な場所に保存

## 4. 環境変数設定

`.env`ファイルにAPI Keyを追加：

```bash
# Late API Configuration
LATE_API_KEY=sk_abc123xyz...
```

## 5. 設定ファイル作成

`config/late_api_config.json`を作成（テンプレートから）:

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/config
cp late_api_config.template.json late_api_config.json
```

`late_api_config.json`を編集し、各プラットフォームのアカウントIDを設定：

```json
{
  "api_key": "${LATE_API_KEY}",
  "base_url": "https://getlate.dev/api/v1",
  "accounts": {
    "linkedin": {
      "accountId": "ln_abc123xyz",
      "platform": "linkedin"
    },
    "twitter": {
      "accountId": "tw_abc123xyz",
      "platform": "twitter"
    },
    "facebook": {
      "accountId": "fb_abc123xyz",
      "platform": "facebook"
    },
    "threads": {
      "accountId": "th_abc123xyz",
      "platform": "threads"
    }
  },
  "timezone": "Asia/Tokyo",
  "optimal_times": {
    "linkedin": "08:00",
    "twitter": "12:00",
    "threads": "20:00",
    "facebook": "19:00"
  }
}
```

## 6. 接続テスト

テストスクリプトを実行：

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
python3 scripts/late_api_test.py
```

期待出力:
```
✅ Late API接続成功
✅ LinkedIn接続確認完了
✅ X/Twitter接続確認完了
✅ Facebook接続確認完了
✅ Threads接続確認完了
```

## 7. トラブルシューティング

### エラー: 401 Unauthorized

**原因**: API Keyが無効または期限切れ

**対処**:
1. Late APIダッシュボードでAPI Key有効性確認
2. `.env`ファイルのAPI Key確認
3. 必要に応じて新しいAPI Key生成

### エラー: 429 Rate Limit Exceeded

**原因**: レート制限超過（Proプラン: 300リクエスト/分）

**対処**:
1. 1時間待機後リトライ
2. リクエスト間隔を調整（最低1秒）

### エラー: 400 Bad Request

**原因**: パラメータ不正（スレッド投稿時の`content`フィールド未設定等）

**対処**:
1. エラーレスポンスの詳細確認
2. スレッド投稿時は`content`フィールド必須（最初の投稿内容）
3. プラットフォーム固有データの形式確認

## 8. セキュリティ注意事項

1. **API Keyの保護**:
   - `.env`ファイルは`.gitignore`に追加済み
   - Git commitに含めないこと
   - 環境変数経由でのみ参照

2. **アカウントIDの保護**:
   - `late_api_config.json`もGit commitに含めないことを推奨
   - 各環境で個別に設定

3. **Late APIダッシュボードの定期確認**:
   - 投稿ステータス確認
   - エラーログ確認
   - API使用量監視

## 9. Late API統合のメリット

1. **マルチプラットフォーム対応**: 4プラットフォーム（LinkedIn, X, Facebook, Threads）を単一APIで管理
2. **スケジュール投稿**: 最適時間帯に自動投稿
3. **スレッド対応**: X/Threadsのスレッド投稿を簡単に実装
4. **エラーハンドリング**: 自動リトライ機能
5. **統計機能**: エンゲージメント分析（Late APIダッシュボード）

## 10. 参照

- Late API公式ドキュメント: https://docs.getlate.dev/
- Late APIダッシュボード: https://app.getlate.dev/
- 統合提案ドキュメント: `Flow/202601/2026-01-02/late_api_integration_proposals.md`
- 実装スクリプト: `scripts/late_api_post.py`

---

**セットアップ完了日**: 2026-01-03
**バージョン**: 1.0
