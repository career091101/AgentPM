# Facebook個人アカウント アナリティクスAPI セットアップガイド

## 概要

個人アカウントの投稿データを**Meta Graph API（公式）**を使って安全に取得します。

### 取得できるデータ

- ✅ いいね数
- ✅ コメント数
- ✅ シェア数
- ✅ 投稿日時
- ✅ 投稿内容

### 取得できないデータ（ビジネスページのみ）

- ❌ Reach（リーチ）
- ❌ Impressions（インプレッション）
- ❌ Click-through Rate（CTR）
- ❌ 詳細な人口統計データ

---

## セットアップ手順

### ステップ1: Facebook Developerアカウント作成

1. **Facebook Developersにアクセス**
   https://developers.facebook.com/

2. **「スタート」をクリック**
   初めての場合、開発者登録が必要です

3. **利用規約に同意**
   電話番号認証が必要な場合があります

---

### ステップ2: アプリを作成

1. **Apps → 「アプリを作成」をクリック**
   https://developers.facebook.com/apps

2. **アプリタイプを選択**
   - 「その他」を選択
   - 「次へ」をクリック

3. **ユースケースを選択**
   - 「Consumer」を選択
   - 「次へ」をクリック

4. **アプリ情報を入力**
   - アプリ名: `My Personal Analytics`（任意）
   - アプリの連絡先メールアドレス: あなたのメールアドレス
   - 「アプリを作成」をクリック

5. **セキュリティチェック**
   CAPTCHAを完了

---

### ステップ3: アクセストークンを生成

1. **Graph APIエクスプローラーにアクセス**
   https://developers.facebook.com/tools/explorer/

2. **アプリを選択**
   - 右上の「Meta App」ドロップダウン
   - 先ほど作成したアプリ（`My Personal Analytics`）を選択

3. **権限を追加**
   - 「User Token」セクションで「Generate Access Token」をクリック
   - 以下の権限を追加:
     - ✅ `user_posts` - 自分の投稿を読み取り
     - ✅ `user_photos` - 自分の写真を読み取り
     - ✅ `user_videos` - 自分の動画を読み取り
   - 「Generate Access Token」をクリック

4. **Facebookログイン**
   - 権限の許可画面が表示される
   - 「続行」→「完了」をクリック

5. **トークンをコピー**
   - 生成されたトークン（`EAAxxxxxxxxxxxx...`形式）をコピー
   - **重要**: このトークンは秘密にしてください！

---

### ステップ4: スクリプトに設定

1. **スクリプトを開く**
   ```bash
   nano /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/facebook_personal_analytics.py
   ```

2. **ACCESS_TOKENを設定**
   ```python
   ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"  # ← ここにコピーしたトークンを貼り付け
   ```

3. **保存して閉じる**
   - Ctrl+O → Enter → Ctrl+X

---

### ステップ5: 実行

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts
python3 facebook_personal_analytics.py
```

---

## 出力例

### コンソール出力

```
🚀 Facebook個人アカウント アナリティクス取得開始

================================================================================
1. 接続テスト
================================================================================
🔍 ユーザー情報取得中...
✅ ユーザー: 佐藤 優一

================================================================================
2. 投稿データ取得
================================================================================
📊 Facebook個人投稿データ取得中...
✅ 25件の投稿を取得しました

================================================================================
📊 Facebookアナリティクスサマリー（個人アカウント）
================================================================================

総投稿数: 25

合計エンゲージメント:
  いいね: 1,234
  コメント: 56
  シェア: 12
  合計: 1,302

平均エンゲージメント:
  いいね: 49.4
  コメント: 2.2
  シェア: 0.5

Top 5エンゲージメント投稿:

  2026-01-02 10:30
  「Late APIでSNS投稿を自動化してみた！」
  エンゲージメント: 234 (👍198 💬24 🔄12)

  2025-12-28 14:15
  「Playwrightでブラウザ自動化を実装...」
  エンゲージメント: 156 (👍142 💬10 🔄4)

  ...
```

### CSVファイル

`data/facebook_personal_analytics_20260103_120000.csv`

| post_id | message | created_time | likes | comments | shares | total_engagement |
|---------|---------|--------------|-------|----------|--------|------------------|
| 123... | Late APIで... | 2026-01-02 10:30:00 | 198 | 24 | 12 | 234 |
| 456... | Playwrightで... | 2025-12-28 14:15:00 | 142 | 10 | 4 | 156 |

---

## トラブルシューティング

### エラー: "Invalid OAuth access token"

**原因**: トークンが無効または期限切れ

**解決策**:
1. Graph APIエクスプローラーで新しいトークンを生成
2. スクリプトのACCESS_TOKENを更新

---

### エラー: "Permissions error"

**原因**: 必要な権限が付与されていない

**解決策**:
1. Graph APIエクスプローラーで権限を追加
   - `user_posts`
   - `user_photos`
   - `user_videos`
2. 「Generate Access Token」を再実行

---

### エラー: "Rate limit exceeded"

**原因**: API呼び出し制限に達した

**解決策**:
- 1時間待ってから再実行
- 個人アカウントは200リクエスト/時間の制限があります

---

## トークンの有効期限

**短期トークン**: 1-2時間で期限切れ

**長期トークン**: 60日間有効（拡張が必要）

### 長期トークンの取得方法

```bash
curl -i -X GET "https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_SHORT_LIVED_TOKEN"
```

詳細: https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived

---

## セキュリティ注意事項

1. **トークンを公開しない**
   - GitHubにコミットしない
   - 環境変数または設定ファイルで管理

2. **定期的にトークンを再生成**
   - セキュリティのため、定期的に更新

3. **最小限の権限のみ付与**
   - 必要な権限だけを有効化

---

## 参考リンク

- [Facebook Graph API ドキュメント](https://developers.facebook.com/docs/graph-api)
- [アクセストークン ガイド](https://developers.facebook.com/docs/facebook-login/guides/access-tokens)
- [Graph APIエクスプローラー](https://developers.facebook.com/tools/explorer/)
