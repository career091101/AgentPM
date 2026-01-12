# Meta App セットアップガイド（クリエイターアカウント向け）

このガイドは、Instagramクリエイターアカウント向けのMeta App設定手順です。

## 前提条件

- ✅ Instagramアカウント: クリエイターアカウントに変換済み
- ⚠️ Threadsアカウント: 状態確認中（通常はInstagramと自動連携）

---

## ステップ1: Threadsアカウント状態の確認

### 1.1 Threadsアプリで確認

1. Threadsアプリを開く
2. プロフィール画面 → 右上の設定アイコン（⚙️）
3. 「アカウント」セクションを確認

**確認ポイント**:
- Instagramアカウント名が表示されているか
- 「プロフェッショナルツール」または「クリエイターツール」のメニューがあるか

**結論**:
- InstagramがクリエイターアカウントなのでThreadsも自動的にクリエイター扱いになっている可能性が高い
- InstagramとThreadsは同じアクセストークンを共有

---

## ステップ2: Meta App作成の続き（手動完了）

### 2.1 ビジネスポートフォリオの選択

developers.facebook.com/apps/create の画面で以下を実行：

**選択肢A: 新規ビジネスポートフォリオを作成（推奨）**

1. 「新しいビジネスポートフォリオを作成」を選択
2. ビジネス名: `SNS Analytics` （任意の名前）
3. メールアドレス: 通知を受け取るメールアドレス
4. 「作成」をクリック

**選択肢B: 既存のポートフォリオを選択**

- Facebookページやビジネスマネージャをすでに持っている場合は選択可能

### 2.2 アプリ作成完了

作成が完了すると、アプリダッシュボードが表示されます。

---

## ステップ3: App IDとApp Secretの取得

### 3.1 App IDの確認

アプリダッシュボードの上部に表示されている数字が **App ID** です。

```
App ID: 1234567890123456
```

### 3.2 App Secretの確認

1. 左メニュー「設定」→「ベーシック」
2. 「App Secret」の横にある「表示」ボタンをクリック
3. Facebookパスワードを入力して認証
4. 表示された **App Secret** をコピー

**⚠️ 重要**: App Secretは絶対に公開しないこと（.envファイルで管理し、.gitignoreで除外）

---

## ステップ4: Instagram Graph APIとThreads APIの追加

### 4.1 製品の追加

1. アプリダッシュボード → 左メニュー「製品を追加」
2. **Instagram Graph API** を見つけて「設定」をクリック
3. **Threads API** を見つけて「設定」をクリック

### 4.2 権限の確認

以下の権限が必要です（後のステップで設定）：

**Instagram Graph API**:
- `instagram_basic`
- `instagram_manage_insights`
- `pages_show_list`
- `pages_read_engagement`

**Threads API**:
- `threads_basic`
- `threads_read_insights`

---

## ステップ5: クリエイターアカウント向けアクセストークン取得

### 5.1 Graph API Explorerを開く

1. https://developers.facebook.com/tools/explorer にアクセス
2. 右上のドロップダウンで、作成したアプリ（SNS Analytics Tool）を選択

### 5.2 権限の追加

1. 「Permissions」タブをクリック
2. 以下の権限を検索して追加（チェックを入れる）：
   - `instagram_basic`
   - `instagram_manage_insights`
   - `pages_show_list`
   - `pages_read_engagement`
   - `threads_basic`
   - `threads_read_insights`

### 5.3 短期トークンの生成

1. 「Generate Access Token」ボタンをクリック
2. Instagramアカウントでログイン
3. 権限を承認
4. 表示された**短期アクセストークン**（1時間有効）をコピー

**コピーしたトークン例**:
```
EAAG... (約200文字の文字列)
```

### 5.4 長期トークンへの変換

**方法A: curlコマンド（ターミナル）**

```bash
curl -i -X GET "https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret={YOUR_APP_SECRET}&access_token={SHORT_LIVED_TOKEN}"
```

**置き換え**:
- `{YOUR_APP_SECRET}`: ステップ3.2で取得したApp Secret
- `{SHORT_LIVED_TOKEN}`: ステップ5.3でコピーした短期トークン

**レスポンス例**:
```json
{
  "access_token": "EAAG...(新しい長期トークン)",
  "token_type": "bearer",
  "expires_in": 5184000
}
```

**方法B: Pythonスクリプト**

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
python3 -c "
import requests
import sys

APP_SECRET = input('App Secretを入力: ')
SHORT_TOKEN = input('短期トークンを入力: ')

url = 'https://graph.instagram.com/access_token'
params = {
    'grant_type': 'ig_exchange_token',
    'client_secret': APP_SECRET,
    'access_token': SHORT_TOKEN
}

response = requests.get(url, params=params)
print(response.json())
"
```

**⚠️ 注意**: 長期トークンは60日間有効です。

---

## ステップ6: Instagram Business Account IDの取得

### 6.1 Facebookページの確認

クリエイターアカウントの場合、Facebookページと連携している必要があります。

**確認方法**:
1. Instagramアプリ → プロフィール → 設定 → アカウント
2. 「リンク済みアカウント」で「Facebook」を確認

### 6.2 ページIDの取得

```bash
curl -i -X GET "https://graph.facebook.com/v21.0/me/accounts?access_token={LONG_LIVED_TOKEN}"
```

**レスポンス例**:
```json
{
  "data": [
    {
      "id": "123456789012345",
      "name": "あなたのFacebookページ名"
    }
  ]
}
```

**`id`の値**をメモ（これが`PAGE_ID`）

### 6.3 Instagram Business Account IDの取得

```bash
curl -i -X GET "https://graph.facebook.com/v21.0/{PAGE_ID}?fields=instagram_business_account&access_token={LONG_LIVED_TOKEN}"
```

**置き換え**:
- `{PAGE_ID}`: ステップ6.2で取得したページID
- `{LONG_LIVED_TOKEN}`: ステップ5.4で取得した長期トークン

**レスポンス例**:
```json
{
  "instagram_business_account": {
    "id": "17841400000000000"
  },
  "id": "123456789012345"
}
```

**`instagram_business_account.id`の値**をメモ（これが`INSTAGRAM_BUSINESS_ACCOUNT_ID`）

---

## ステップ7: Threads User IDの取得

```bash
curl -i -X GET "https://graph.threads.net/v1.0/me?fields=id,username&access_token={LONG_LIVED_TOKEN}"
```

**レスポンス例**:
```json
{
  "id": "1234567890",
  "username": "your_threads_username"
}
```

**`id`の値**をメモ（これが`THREADS_USER_ID`）

---

## ステップ8: .envファイルの作成

### 8.1 .envファイルの作成

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
cp .env.example .env
```

### 8.2 .envファイルの編集

取得した値を入力してください：

```bash
# Meta App認証情報
FACEBOOK_APP_ID=あなたのApp ID
FACEBOOK_APP_SECRET=あなたのApp Secret

# Instagram認証情報
INSTAGRAM_BUSINESS_ACCOUNT_ID=17841400000000000
INSTAGRAM_ACCESS_TOKEN=EAAG...(長期トークン)

# Threads認証情報
THREADS_USER_ID=1234567890
THREADS_ACCESS_TOKEN=EAAG...(長期トークン)

# データ保存先
DATA_DIR=/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
```

**⚠️ 注意**:
- `INSTAGRAM_ACCESS_TOKEN`と`THREADS_ACCESS_TOKEN`は通常**同じトークン**です
- `.env`ファイルは`.gitignore`で除外されているため、Gitにコミットされません

---

## ステップ9: 動作確認

### 9.1 依存パッケージのインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
pip install -r requirements.txt
```

### 9.2 Instagramデータ取得テスト

```bash
python3 scripts/fetch_instagram_data.py
```

**期待される出力**:
```
================================================================================
Instagram Graph API データ取得
================================================================================

📥 過去90日分のメディア一覧を取得中...
取得中: 10/50件
取得中: 20/50件
...

✅ 全50件のメディアを取得しました

📊 各メディアのInsightsを取得中...
取得中: 10/50件
...

💾 データをCSVで保存: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/Instagram/instagram_2026-01-01.csv

✅ 処理完了
```

### 9.3 Threadsデータ取得テスト

```bash
python3 scripts/fetch_threads_data.py
```

### 9.4 全プラットフォーム統合分析

```bash
python3 scripts/analyze_all_platforms.py
```

---

## トラブルシューティング

### エラー1: `Invalid OAuth access token`

**原因**: トークンの期限切れ、または権限不足

**解決策**:
1. Graph API Explorerで権限を再確認（全6つの権限がチェックされているか）
2. 新しい短期トークンを生成 → 長期トークンに変換
3. `.env`ファイルの`INSTAGRAM_ACCESS_TOKEN`を更新

### エラー2: `Unsupported get request`

**原因**: Instagram Business Account IDが間違っている、またはアカウントがビジネス/クリエイターに変換されていない

**解決策**:
1. Instagramアプリでアカウントタイプを再確認（プロフィール → 設定 → アカウント）
2. クリエイターアカウントでない場合は変換（設定 → アカウント → プロアカウントに切り替える）
3. ステップ6を再実行してIDを再取得

### エラー3: `Rate limit exceeded`

**原因**: APIリクエスト制限（200リクエスト/時間）を超過

**解決策**:
- スクリプトは自動的に指数バックオフで待機します
- 手動実行の場合は1時間待機してから再実行

### エラー4: Threadsデータが取得できない

**原因**: Threads APIの権限不足、またはThreadsアカウントが個人アカウント

**解決策**:
1. Threadsアプリでアカウントタイプを確認
2. InstagramとThreadsの連携を確認（Threads設定 → アカウント）
3. `threads_basic`と`threads_read_insights`の権限を再確認

---

## 次のステップ

1. ✅ Meta App作成完了
2. ✅ アクセストークン取得
3. ✅ .envファイル作成
4. ⬜ 初回データ取得テスト
5. ⬜ 全プラットフォーム統合分析
6. ⬜ 月次トークンリフレッシュの習慣化（`refresh_access_token.py`を月1回実行）

---

## 参考リンク

- Meta for Developers: https://developers.facebook.com
- Graph API Explorer: https://developers.facebook.com/tools/explorer
- Instagram Graph API リファレンス: https://developers.facebook.com/docs/instagram-api
- Threads API リファレンス: https://developers.facebook.com/docs/threads

---

**作成日**: 2026-01-01
**対象**: Instagramクリエイターアカウント保有者
