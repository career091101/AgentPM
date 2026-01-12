# d_1d2d メンバーシップ記事抽出プロジェクト

## 概要

note.com/d_1d2d/membership/notes のメンバーシップ限定記事を全て抽出し、JSON + Markdown + 画像形式で保存するプロジェクトです。

## 目的

- d_1d2d メンバーシップ記事（2025年1月〜）の完全アーカイブ
- 記事内容の体系的な学習と分析
- 落合式リサーチ（6つの質問）によるナレッジベース構築

## プロジェクト構造

```
d_1d2d_membership/
├── README.md                          # 本ファイル
├── .gitignore                         # Git除外設定
├── scripts/
│   └── d_1d2d_membership_fetcher.py   # メインスクリプト
├── data/
│   ├── cookies/
│   │   ├── d_1d2d_cookies.json        # 変換後のクッキー（JSON形式）
│   │   └── d_1d2d_cookies.txt         # Netscape形式クッキー
│   └── d_1d2d_articles/
│       ├── articles/                  # JSON + Markdown記事
│       ├── images/                    # 記事内画像
│       ├── metadata/                  # メタデータ
│       │   └── archive_urls.json
│       └── logs/                      # エラーログ
│           ├── failures.jsonl
│           └── url_collection_failures.jsonl
└── documents/
    ├── implementation_plan.md         # 実装計画
    └── api_investigation.md           # API調査結果
```

## 使用方法

### 1. 初回セットアップ

依存パッケージをインストール：

```bash
pip install requests beautifulsoup4 markdownify playwright
python -m playwright install chromium
```

### 2. クッキーの準備

Chrome拡張 "Get cookies.txt LOCALLY" で note.com のクッキーをエクスポートし、`data/cookies/d_1d2d_cookies.txt` に保存します。

### 3. 記事の収集

#### 全記事収集（2025年1月〜）

```bash
cd scripts
python d_1d2d_membership_fetcher.py \
  --cookies ../data/cookies/d_1d2d_cookies.json \
  --output ../data/d_1d2d_articles
```

#### テスト実行（10記事のみ）

```bash
python d_1d2d_membership_fetcher.py \
  --cookies ../data/cookies/d_1d2d_cookies.json \
  --output ../data/d_1d2d_articles \
  --limit 10
```

#### オプション

- `--start-ym YYYY-MM`: 収集開始年月（デフォルト: 2025-01）
- `--end-ym YYYY-MM`: 収集終了年月（デフォルト: 2026-01）
- `--limit N`: 取得する記事数（0=全件）
- `--login`: ブラウザでログインしてクッキーを保存

## 出力データ

### 記事ファイル

各記事は以下の形式で保存されます：

- **JSON**: `articles/YYYY-MM-DD_記事タイトル.json` - メタデータ
- **Markdown**: `articles/YYYY-MM-DD_記事タイトル.md` - 本文
- **画像**: `images/YYYY-MM-DD_記事タイトル/001.jpg` - 記事内画像

### メタデータ

`metadata/archive_urls.json` に収集統計が記録されます：

```json
{
  "source": "note_api_membership",
  "membership_url": "https://note.com/d_1d2d/membership/notes",
  "total_urls": 123,
  "note_count": 123,
  "months": [
    {"ym": "2025-01", "count": 45}
  ]
}
```

## トラブルシューティング

### クッキー期限切れ（HTTP 401/403）

```bash
# 再ログイン
python d_1d2d_membership_fetcher.py --login --cookies ../data/cookies/d_1d2d_cookies.json

# または、ブラウザから新しいクッキーをエクスポート
```

### レート制限（HTTP 429）

スクリプト内の `SLEEP_BETWEEN_REQUESTS` を1.0秒→2.0秒に増やします。

### API仕様変更

`documents/api_investigation.md` の手順に従い、Chrome DevToolsで最新のAPI仕様を確認します。

## 参照

- 元スクリプト: [月刊アプリマーケティング記事抽出](../月刊アプリマーケティング/scripts/markelabo_note_fetcher.py)
- 実装計画: [documents/implementation_plan.md](documents/implementation_plan.md)

## ライセンス

個人利用のみ。抽出した記事の著作権は元の著者に帰属します。
