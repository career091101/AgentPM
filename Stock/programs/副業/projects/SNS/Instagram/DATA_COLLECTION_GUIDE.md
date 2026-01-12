# Instagram Insights データ収集ガイド

Instagram Web版のInsightsページから過去90日間のデータを収集します。

## セットアップ

### 1. 依存パッケージのインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
pip install -r requirements.txt
playwright install chromium
```

### 2. 環境変数設定（オプション）

`.env`ファイルに以下を設定（Graph API使用時のみ）:

```bash
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## 使用方法

### Instagram Webスクレイピング（推奨）

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts
python3 scrape_instagram_insights.py
```

**実行手順:**

1. スクリプトを実行するとChromeブラウザが自動的に開きます
2. Instagramにログインしてください（初回のみ）
3. ログイン後、スクリプトが自動的にデータを取得します
4. 次回以降はログイン状態が保存されるため、自動実行されます

**取得データ:**

- `instagram_summary_YYYYMMDD_HHMMSS.csv` - アカウント全体のサマリー
- `instagram_posts_YYYYMMDD_HHMMSS.csv` - 個別投稿のデータ

### 出力CSV形式

**サマリーファイル (`instagram_summary_*.csv`):**

| カラム名 | 説明 |
|---------|------|
| 期間 | データ取得期間（過去90日間） |
| 取得日時 | データ取得日時 |
| 総閲覧数 | 過去90日間の総閲覧数 |
| リーチしたアカウント数 | リーチしたユニークアカウント数 |
| 総インタラクション数 | いいね、コメント、保存などの合計 |
| プロフィールアクティビティ | プロフィールアクセス数 |
| フォロワー数 | 現在のフォロワー数 |

**投稿データファイル (`instagram_posts_*.csv`):**

| カラム名 | 説明 |
|---------|------|
| 投稿番号 | 投稿の連番 |
| 投稿日時 | 投稿日時 |
| メディアタイプ | 画像投稿/リール動画/カルーセル/ストーリーズ |
| インプレッション数 | 投稿が表示された回数 |
| リーチ数 | 投稿を見たユニークアカウント数 |
| エンゲージメント数 | いいね+コメント+保存+シェアの合計 |
| いいね数 | いいね数 |
| コメント数 | コメント数 |
| 保存数 | 保存数 |
| シェア数 | シェア数 |

## トラブルシューティング

### エラー: `playwright._impl._api_types.Error: Executable doesn't exist`

**解決策:**

```bash
playwright install chromium
```

### エラー: ログインページから進まない

**解決策:**

1. 手動でログインしてください
2. 2段階認証が有効な場合は、認証コードを入力してください
3. ログイン後、スクリプトが自動的に進行します

### データが取得できない

**原因:**

- Instagram Web UIの構造が変更された可能性があります
- インターネット接続が不安定です
- アカウントがクリエイターアカウント/ビジネスアカウントではない

**解決策:**

1. Instagramアプリでアカウントタイプを確認してください
2. クリエイターアカウントまたはビジネスアカウントに切り替えてください
3. スクリプトを再実行してください

### ブラウザが閉じない

**解決策:**

- `Ctrl+C`でスクリプトを強制終了してください
- 手動でブラウザを閉じてください

## 注意事項

1. **利用規約遵守**: Instagramの利用規約に従ってデータを取得してください
2. **レート制限**: 短時間に大量のリクエストを送信しないでください
3. **データ保存**: 取得したデータは個人使用のみに限定してください
4. **UI変更**: Instagram Web UIは頻繁に変更されるため、スクリプトが動作しなくなる可能性があります

## 次のステップ

データ取得後、以下のスクリプトでデータ分析を実行できます:

```bash
# 分析スクリプト（作成予定）
python3 analyze_instagram_posts.py
```
