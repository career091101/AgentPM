# API調査ガイド（Phase 2）

## 目的

note.com/d_1d2d/membership/notes のメンバーシップAPIの仕様を特定し、スクリプトの暫定値を確定します。

## 調査手順

### 1. Chrome にクッキーをインポート

**方法1: Chrome拡張 "EditThisCookie" を使用**

1. Chrome Web Store から "EditThisCookie" をインストール
2. note.com を開く
3. 拡張機能アイコンをクリック → "Import" を選択
4. `data/cookies/d_1d2d_cookies.txt` の内容を貼り付け
5. "Submit" をクリック

**方法2: 手動でコピー（推奨）**

1. Chrome で note.com を開く
2. DevTools を開く（F12 または Cmd+Option+I）
3. "Application" タブ → "Cookies" → "https://note.com" を選択
4. `data/cookies/d_1d2d_cookies.txt` から以下のクッキーを手動で追加：
   - `_note_session_v5`
   - `note_gql_auth_token`
   - `XSRF-TOKEN`

### 2. メンバーシップページにアクセス

1. https://note.com/d_1d2d/membership/notes にアクセス
2. メンバーシップコンテンツが表示されることを確認
3. ログインが必要と表示される場合は、クッキーが正しくインポートされていません

### 3. Chrome DevTools でAPI呼び出しを確認

1. DevTools の "Network" タブを開く
2. "Fetch/XHR" フィルタを有効化
3. ページをリロード（Cmd+R）
4. ページを下にスクロールして追加の記事を読み込む

### 4. API エンドポイントを特定

Network タブで以下の情報を確認：

#### 4.1 API URL形式

**期待される候補**:
- `https://note.com/api/v1/layout/membership/d_1d2d`
- `https://note.com/api/v2/creators/d_1d2d/membership_contents`
- `https://note.com/api/v1/memberships/d_1d2d/notes`

**確認項目**:
- [ ] 実際のAPI URL: `____________________________`

#### 4.2 リクエストパラメータ

**ページング方式の確認**:
- [ ] `?page=1` 形式（ページ番号）
- [ ] `?cursor=abc123` 形式（カーソルベース）
- [ ] `?offset=0&limit=20` 形式（オフセット）
- [ ] 月別フィルタ: `?ym=2025-01-01` の有無

**実際のパラメータ**: `____________________________`

#### 4.3 レスポンス構造

Network タブで API レスポンスを表示し、JSON構造を確認：

**確認項目**:
- [ ] レスポンスのルートキー: `data` / `result` / その他
- [ ] メンバーシップデータのキー: `membership_layout` / `creator_notes` / その他
- [ ] 記事配列の場所: `page_layout.section.contents` / `notes` / その他
- [ ] 記事総数フィールド: `note_count` の有無
- [ ] ページング終了判定: `is_last_page` / 空配列 / その他

**レスポンス例**（主要部分をコピー）:

```json
{
  "data": {
    "???_layout": {
      "note_count": 123,
      "page_layout": {
        "section": {
          "contents": [
            {
              "note_url": "/d_1d2d/n/nxxxxxxxxx",
              "title": "記事タイトル",
              ...
            }
          ],
          "is_last_page": false
        }
      }
    }
  }
}
```

## 調査結果の記録

調査完了後、以下の情報を記録してください：

### 確定したAPI仕様

| 項目 | 値 |
|------|-----|
| API URL | `https://note.com/api/v1/layout/membership/d_1d2d` |
| ページングパラメータ | `?ym=2025-01-01&page=1` |
| レスポンスキー（メンバーシップデータ） | `data.magazine_layout` / `data.membership_layout` |
| レスポンスキー（記事配列） | `page_layout.section.contents` |
| 記事総数フィールド | `note_count` |
| ページング終了判定 | `is_last_page: true` / 空配列 |

### スクリプト修正箇所

調査結果をもとに、以下のスクリプト箇所を修正：

**ファイル**: `scripts/d_1d2d_membership_fetcher.py`

#### 修正1: API URL（行24-25）

```python
# 現在（暫定値）
MEMBERSHIP_API_URL = "https://note.com/api/v1/layout/membership/d_1d2d"

# 修正後（調査結果）
MEMBERSHIP_API_URL = "実際のAPI URL"
```

#### 修正2: レスポンスキー（行196）

```python
# 現在（暫定値）
membership = payload.get("data", {}).get("magazine_layout", {})

# 修正後（調査結果）
membership = payload.get("data", {}).get("実際のキー名", {})
```

## トラブルシューティング

### クッキー認証が失敗する

**症状**: メンバーシップページにアクセスしてもログイン画面が表示される

**対処法**:
1. クッキーの有効期限を確認（`note_gql_auth_token` の `exp` フィールド）
2. クッキーのドメインが正しいか確認（`.note.com` または `note.com`）
3. ブラウザで直接ログインし、新しいクッキーをエクスポート

### API呼び出しが見つからない

**症状**: Network タブにAPI呼び出しが表示されない

**対処法**:
1. "Fetch/XHR" フィルタが有効か確認
2. ページをリロードしてもう一度確認
3. ページを下にスクロールして追加の記事を読み込む
4. "All" フィルタに切り替えて、すべてのリクエストを確認

### レスポンス構造が月刊アプリマーケティングと異なる

**症状**: `magazine_layout` キーが存在しない

**対処法**:
1. レスポンス全体をコピーして、構造を分析
2. 記事URLが含まれているキーを探す
3. スクリプトの `collect_article_urls_via_api()` 関数を修正

## 調査完了チェックリスト

- [ ] API URLを特定した
- [ ] ページングパラメータを特定した
- [ ] レスポンスのキー名を特定した
- [ ] 記事配列の場所を特定した
- [ ] ページング終了判定を特定した
- [ ] スクリプトを修正した
- [ ] 本ドキュメントに調査結果を記録した

## 次のステップ

調査完了後、Phase 4（クッキー変換とテスト）に進んでください。
