# クイックスタートガイド（ビジネスポートフォリオなし）

ビジネスポートフォリオを作成せずにInstagram/Threadsデータを取得する方法。

## 前提条件

- ✅ Instagramクリエイターアカウント
- ✅ Instagramに紐づいたFacebookページ

---

## ステップ1: Facebookページの確認

### 1.1 Instagramとリンクされたページを確認

1. Instagramアプリ → プロフィール → 設定
2. 「アカウント」→「リンク済みアカウント」→「Facebook」
3. リンクされているFacebookページ名を確認

---

## ステップ2: Facebook Access Token Toolでトークン取得

### 2.1 Access Token Toolにアクセス

https://developers.facebook.com/tools/accesstoken

### 2.2 ユーザートークンを取得

1. ページを開くと「ユーザートークン」セクションが表示される
2. 「デバッグ」または「延長」ボタンをクリック
3. 表示されたトークンをコピー

### 2.3 ページアクセストークンを取得

以下のコマンドでページアクセストークンを取得：

```bash
curl -X GET "https://graph.facebook.com/v21.0/me/accounts?access_token={USER_TOKEN}"
```

**レスポンス例**:
```json
{
  "data": [
    {
      "access_token": "EAAG...(ページアクセストークン)",
      "category": "Personal Blog",
      "name": "あなたのページ名",
      "id": "123456789012345",
      "tasks": ["ANALYZE", "ADVERTISE", "MODERATE", "CREATE_CONTENT", "MANAGE"]
    }
  ]
}
```

**`access_token`の値**をメモ（これがページアクセストークン）

### 2.4 ページアクセストークンを長期化

```bash
curl -X GET "https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id={YOUR_APP_ID}&client_secret={YOUR_APP_SECRET}&fb_exchange_token={PAGE_ACCESS_TOKEN}"
```

**注意**: App IDとApp Secretが必要ですが、ビジネスポートフォリオなしでアプリを作成する方法があります。

---

## ステップ3: 簡易アプリ作成（ポートフォリオなし）

### 3.1 Meta for Developersでアプリ作成（別フロー）

以下のURLから直接テストアプリを作成：

https://developers.facebook.com/apps/

**方法A: テストアプリとして作成**

1. 「アプリを作成」をクリック
2. 「その他」のユースケースを選択
3. アプリタイプ: 「なし」または「Consumer」
4. アプリ名: 「Instagram Data Test」
5. ビジネスポートフォリオ: **スキップ可能な場合はスキップ**

**方法B: レガシーアプリIDを使用**

既存の「制限されたアプリ(3)」があるようなので、それを使用できる可能性があります。

1. アプリ一覧ページで「制限されたアプリ(3)」をクリック
2. 既存のアプリIDを確認
3. そのアプリに Instagram Graph API を追加

---

## ステップ4: より簡易な方法（推奨）

### 4.1 Instagram Basic Display APIを使用

**重要**: Instagram Basic Display APIは個人アカウントでも使用可能ですが、Insightsデータ（インプレッション、リーチ等）は取得できません。

**利用可能なデータ**:
- ユーザープロフィール情報
- メディア一覧（投稿、ストーリー）
- メディアの基本情報（キャプション、メディアタイプ、タイムスタンプ）

**取得できないデータ**:
- インプレッション数
- リーチ数
- エンゲージメント数
- 詳細な統計情報

### 4.2 クリエイターアカウントならGraph APIを使用（推奨）

Instagramがクリエイターアカウントの場合、Graph APIでInsightsデータを取得できます。

**必要な手順**:
1. Facebookページとリンク（すでに完了している可能性が高い）
2. アプリを作成（テストモードでOK）
3. Instagram Graph APIを製品として追加
4. ページアクセストークンを取得

---

## ステップ5: 手動でのセットアップ（完全版）

ブラウザ自動化がうまくいかなかったため、以下を手動で実施してください：

### 5.1 ビジネスポートフォリオの作成

https://business.facebook.com/settings/portfolios

1. 「ポートフォリオを作成」
2. 名前: 「SNS Analytics Portfolio」
3. 作成完了後、Meta for Developersのアプリ作成に戻る

### 5.2 アプリ作成の続き

1. https://developers.facebook.com/apps/creation/ にアクセス
2. 作成したポートフォリオを選択
3. アプリ作成を完了

---

## 次のアクション候補

以下のいずれかを選択してください：

### オプション1: 手動でビジネスポートフォリオを作成
- https://business.facebook.com/settings/portfolios にアクセス
- ポートフォリオを作成
- アプリ作成フローを再開

### オプション2: 既存の制限されたアプリを使用
- 「制限されたアプリ(3)」の中に使えるアプリがあるか確認
- そのアプリにInstagram Graph APIを追加

### オプション3: Instagram Basic Display API（制限付き）
- Insightsデータなし
- 基本的なメディア情報のみ取得可能
- セットアップが簡単

### オプション4: サードパーティツールを使用
- Later、Iconosquare、Hootsuite等のSNS管理ツール
- APIキーなしでデータエクスポート可能
- コストがかかる場合あり

---

## 推奨アプローチ

**最も確実な方法**:

1. **手動でビジネスポートフォリオを作成** (5分)
   - https://business.facebook.com/settings/portfolios

2. **アプリ作成を完了** (5分)
   - Meta for Developersでアプリ作成フローを再開

3. **以降は自動スクリプトで実行** (5分)
   - アクセストークン取得
   - データ取得スクリプト実行
   - 分析実行

合計15分程度で完了します。

---

**次にどのオプションを試しますか？**
