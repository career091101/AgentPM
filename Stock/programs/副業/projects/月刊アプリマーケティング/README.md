# 月刊アプリマーケティング記事抽出プロジェクト

[月刊アプリマーケティング](https://markelabo.com/m/mc375c9b46464)（アプリマーケティング研究所）の記事を自動抽出し、落合式リサーチ手法で体系的に学習するプロジェクトです。

## プロジェクト概要

- **対象マガジン**: 月刊アプリマーケティング（月額2,000円）
- **記事数**: 14記事（2026-01-01時点）
- **手法**: 落合式リサーチ（6つの質問）を記事用にカスタマイズ
- **目的**: アプリマーケティング・グロースハックの実践的知見を体系的に蓄積

## ディレクトリ構造

```
月刊アプリマーケティング/
├── README.md                          # 本ファイル
├── data/
│   ├── article_list.csv               # 記事一覧（14件）
│   ├── markelabo_articles/            # 抽出した記事データ（未実行）
│   │   ├── articles/                  # JSON + Markdown
│   │   ├── images/                    # 記事画像
│   │   ├── metadata/                  # メタデータ
│   │   └── logs/                      # エラーログ
│   └── cookies/                       # 認証クッキー（gitignore）
├── documents/
│   └── 2_research/
│       └── article_extraction_plan.md # 実行計画書
└── scripts/
    └── markelabo_note_fetcher.py      # 記事抽出スクリプト
```

## セットアップ

### 1. 依存パッケージのインストール

```bash
cd Stock/programs/副業/projects/月刊アプリマーケティング/scripts

pip install requests beautifulsoup4 markdownify playwright
python -m playwright install chromium
```

### 2. noteへの購読登録

月刊アプリマーケティングを購読している必要があります（月額2,000円）。

## 使い方

### 基本的な実行

```bash
cd Stock/programs/副業/projects/月刊アプリマーケティング/scripts

# 初回: ログインしてcookiesを保存
python markelabo_note_fetcher.py --login --output ../data/markelabo_articles

# 2回目以降: cookiesを使って自動実行
python markelabo_note_fetcher.py --output ../data/markelabo_articles
```

### オプション

```bash
# 記事数を制限（テスト用）
python markelabo_note_fetcher.py --output ../data/markelabo_articles --limit 3

# カスタムcookiesファイルを指定
python markelabo_note_fetcher.py --output ../data/markelabo_articles --cookies /path/to/cookies.json

# Netscape形式のcookies.txtから変換
python markelabo_note_fetcher.py --output ../data/markelabo_articles --cookies-txt /path/to/cookies.txt
```

### ログイン手順（初回のみ）

1. `--login` オプションで実行すると、Chromeブラウザが起動
2. noteにログイン（Googleアカウント等）
3. ログイン完了後、別ターミナルで以下を実行:
   ```bash
   touch Stock/programs/副業/projects/月刊アプリマーケティング/data/cookies/login_done.flag
   ```
4. スクリプトがcookiesを保存して終了
5. 次回から自動でログイン状態で実行可能

## 出力形式

### 記事データ（JSON）

```json
{
  "id": "n4f6ce8c8da72",
  "file_stem": "2026-01-01_大手ECサイトにフッターナビをつけたらCVRが約1.3倍になった理由",
  "title": "大手ECサイトに「フッターナビ」をつけたらCVRが約1.3倍になった理由...",
  "url": "https://markelabo.com/n/n4f6ce8c8da72",
  "published_at": "2026-01-01T10:00:00.000+09:00",
  "tags": ["#アプリマーケティング", "#CVR改善"],
  "is_paid": false,
  "image_paths": ["../images/.../001.jpg"],
  "image_descriptions": {},
  "scraped_at": "2026-01-01T19:30:00"
}
```

### 記事データ（Markdown）

```markdown
# 大手ECサイトに「フッターナビ」をつけたらCVRが約1.3倍になった理由

今月に気になった記事などを、紹介させていただきます。

## 1、ECサイトに「フッターナビ」をつけたらCVRが約1.3倍に。

ウクライナの大手小売チェーン...

![](../images/.../001.jpg)
```

## 次のステップ: 6つの質問による分析

抽出した記事に対して、落合式リサーチの「6つの質問」を適用します。

### 質問1: どんなもの？
- 記事のテーマと主要メッセージを3行要約

### 質問2: 既存知識と比べてどこがユニークか？
- 一般的な施策との違い、新規性のポイント

### 質問3: 施策・手法のキモはどこ？
- 具体的な実装内容、なぜ効果的だったか

### 質問4: どうやって検証した？効果は？
- ABテストの実施方法、測定した指標、結果の数値

### 質問5: 議論・限界点・応用可能性は？
- 施策の限界点、今後の改善余地、批判的視点

### 質問6: 次に読むべき記事は？
- マガジン内の関連記事、外部リンク先の重要記事

詳細は `documents/2_research/article_extraction_plan.md` を参照。

## トラブルシューティング

### エラー: `HTTP 401` または `HTTP 403`

- cookiesが期限切れの可能性があります
- `--login` オプションで再度ログインしてください

### エラー: `Playwright import failed`

```bash
pip install playwright
python -m playwright install chromium
```

### 記事が抽出されない

- マガジンを購読しているか確認してください
- `ARCHIVE_START_YM` と `ARCHIVE_END_YM` の期間を調整してください（スクリプト内）

### 画像のダウンロードに失敗する

- 画像のダウンロードエラーは警告として表示されますが、記事本文の抽出は継続されます
- `logs/failures.jsonl` にエラーログが記録されます

## 参考資料

- **元スクリプト**: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/note_archive_fetcher.py`
- **実行計画書**: `documents/2_research/article_extraction_plan.md`
- **記事リスト**: `data/article_list.csv`
- **マガジンURL**: https://markelabo.com/m/mc375c9b46464

## ライセンス

- スクリプト: 元の `note_archive_fetcher.py` を基に改変
- 記事コンテンツ: アプリマーケティング研究所の著作物（購読者のみアクセス可能）

---

**作成日**: 2026-01-01
**更新日**: 2026-01-01
**ステータス**: Ready to Use
