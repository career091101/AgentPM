# Dental Instagram Scraper

歯科医院のInstagramアカウントを自動収集し、プロフィール情報を抽出・検証してCSV出力するツールです。

## プロジェクト概要

このツールは、以下の機能を提供します：

1. **Instagram収集**: 指定したハッシュタグから歯科医院のアカウントを自動収集
2. **データ抽出**: Claude AI（Anthropic API）を使用してプロフィール情報を構造化
3. **ファクトチェック**: 外部リンクをスクレイピングして住所等の情報を検証
4. **CSV出力**: 収集・検証したデータをExcel対応のCSV形式で出力

### 主な特徴

- Claude AI（Sonnet 3.5）による高精度な情報抽出
- 自動ファクトチェックによる情報の信頼性確保
- レート制限対応による安定した動作
- エラー時の部分結果保存機能
- 詳細なログ出力とプログレスバー表示

## 法的注意事項

### Instagram利用規約の遵守

このツールを使用する前に、以下の点を必ず確認してください：

1. **利用規約の遵守**: [Instagram利用規約](https://help.instagram.com/581066165581870)および[APIガイドライン](https://developers.facebook.com/docs/instagram-api)を必ず確認し、遵守してください。

2. **収集対象の制限**:
   - **法人アカウント（歯科医院）の公開情報のみ**を収集対象としてください
   - 個人アカウントや非公開アカウントは収集しないでください
   - 医療機関として公開されている情報のみを対象としてください

3. **個人情報保護法の遵守**:
   - 収集したデータは個人情報保護法に従って適切に管理してください
   - データの利用目的を明確にし、目的外利用は行わないでください
   - 本人からの開示・訂正・削除請求に適切に対応できる体制を整えてください

4. **レート制限の遵守**:
   - Instagramのレート制限を遵守し、サーバーに過度な負荷をかけないでください
   - config.yamlで適切な待機時間を設定してください

5. **商用利用時の注意**:
   - 商用目的で使用する場合は、必要に応じて法務担当者に相談してください
   - データの販売や第三者への提供には特別な注意が必要です

### 免責事項

- このツールの使用によって生じたいかなる損害についても、開発者は責任を負いません
- ユーザーは自己の責任において本ツールを使用してください
- 法的問題が発生した場合、ユーザー自身が責任を負うものとします

## セットアップ手順

### 1. 前提条件

- Python 3.8以上
- Instagramアカウント（ビジネスアカウント推奨）
- Anthropic APIキー（[こちら](https://console.anthropic.com/)で取得）

### 2. プロジェクトのクローンまたはダウンロード

```bash
cd /path/to/your/workspace
# プロジェクトディレクトリに移動
cd DentalInstagramScraper
```

### 3. 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化（macOS/Linux）
source venv/bin/activate

# 仮想環境の有効化（Windows）
venv\Scripts\activate
```

### 4. 依存パッケージのインストール

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. 環境変数の設定

```bash
# .env.exampleをコピーして.envを作成
cp .env.example .env

# .envファイルを編集して認証情報を設定
# エディタで.envを開き、以下を設定：
# - INSTAGRAM_USERNAME: Instagramのユーザー名
# - INSTAGRAM_PASSWORD: Instagramのパスワード
# - ANTHROPIC_API_KEY: Anthropic APIキー
```

### 6. 設定ファイルの確認

`config.yaml`を開き、必要に応じて設定を変更してください：

```yaml
# 検索対象のハッシュタグ
hashtags:
  - 歯科
  - 歯医者
  - デンタルクリニック

# ハッシュタグあたりの最大投稿数
max_posts_per_hashtag: 100

# 出力ディレクトリ
output_dir: data/output

# レート制限（秒）
rate_limit:
  instagram: 5
  anthropic: 1
  web_scraping: 2
```

## 使い方

### 基本的な実行方法

```bash
# 仮想環境を有効化（まだの場合）
source venv/bin/activate

# スクリプトを実行
python main.py
```

### 実行の流れ

1. **初期化**: 設定ファイルと環境変数の読み込み
2. **Instagram収集**: ハッシュタグ検索によるプロフィール収集
3. **データ処理**: 各プロフィールの抽出と検証（プログレスバー表示）
4. **CSV出力**: 結果をCSVファイルに保存
5. **サマリー表示**: 処理結果の統計情報を表示

### 中断と再開

- **Ctrl+C**で処理を中断できます
- 中断時には、その時点までの部分結果が自動保存されます
- 再開する場合は、再度`python main.py`を実行してください

### 実行例

```bash
$ python main.py
2026-01-02 10:30:00 - __main__ - INFO - ================================================================================
2026-01-02 10:30:00 - __main__ - INFO - Dental Instagram Scraper を開始します
2026-01-02 10:30:00 - __main__ - INFO - ================================================================================
2026-01-02 10:30:01 - __main__ - INFO - .env ファイルを読み込みました
2026-01-02 10:30:01 - __main__ - INFO - config.yaml を読み込みました
2026-01-02 10:30:02 - __main__ - INFO - コンポーネントを初期化しています...
2026-01-02 10:30:03 - __main__ - INFO - ハッシュタグ検索を開始します: ['歯科', '歯医者', 'デンタルクリニック']
処理中: 100%|██████████████████████████████| 45/45 [15:30<00:00, 20.67s/profile]
2026-01-02 10:45:33 - __main__ - INFO - ================================================================================
2026-01-02 10:45:33 - __main__ - INFO - 処理が完了しました
2026-01-02 10:45:33 - __main__ - INFO - ================================================================================
2026-01-02 10:45:33 - __main__ - INFO - 総プロフィール数: 45
2026-01-02 10:45:33 - __main__ - INFO - 検証成功: 38 件
2026-01-02 10:45:33 - __main__ - INFO - 検証失敗/エラー: 7 件
2026-01-02 10:45:33 - __main__ - INFO - 出力ファイル: data/output/dental_instagram_20260102_103000.csv
2026-01-02 10:45:33 - __main__ - INFO - ================================================================================
```

## 出力ファイルの見方

### ファイル形式

- **ファイル名**: `dental_instagram_YYYYMMDD_HHMMSS.csv`
- **エンコーディング**: UTF-8 with BOM（Excelで開いても文字化けしません）
- **保存場所**: `data/output/`ディレクトリ

### CSVカラムの説明

| カラム名 | 説明 | 例 |
|---------|------|---|
| instagram_handle | Instagramのユーザー名 | `sample_dental` |
| clinic_name | 医院名 | `サンプル歯科クリニック` |
| postal_code | 郵便番号 | `150-0043` |
| address | 住所 | `東京都渋谷区道玄坂1-2-3` |
| extracted_person_name | 抽出された人名（院長名など） | `山田太郎` |
| external_link_url | 外部リンクURL | `https://example.com` |
| phone_number | 電話番号 | `03-1234-5678` |
| follower_count | フォロワー数 | `1500` |
| bio_text | プロフィール文（改行は\\nで表示） | `サンプル歯科\\n東京都渋谷区` |
| fact_check_status | 検証ステータス | `verified`, `failed`, `partial` |
| fact_check_confidence | 検証の信頼度（0-1） | `0.95` |
| verified_address | 検証済み住所 | `東京都渋谷区道玄坂1-2-3` |
| verification_source | 検証に使用したソースURL | `https://example.com/access` |
| needs_manual_review | 手動レビューが必要か | `true`, `false` |
| collected_at | 収集日時（ISO 8601形式） | `2026-01-02T10:30:00+09:00` |

### Excelでの開き方

1. Excelを起動
2. ファイル > 開く > CSVファイルを選択
3. または、CSVファイルをダブルクリック（UTF-8 BOM付きなので自動認識されます）

## トラブルシューティング

### 1. Instagram認証エラー

**症状**: `Login failed` や `Two-factor authentication required` エラー

**解決方法**:
- Instagramのユーザー名とパスワードが正しいか確認
- 2段階認証を有効にしている場合は、一時的に無効化するか、アプリパスワードを使用
- アカウントがロックされていないか確認

### 2. APIレート制限エラー

**症状**: `Rate limit exceeded` や `Too many requests` エラー

**解決方法**:
- `config.yaml`の`rate_limit`設定を増やす（待機時間を長くする）
- 一度に処理する投稿数（`max_posts_per_hashtag`）を減らす
- 時間をおいて再実行する

### 3. Anthropic APIエラー

**症状**: `API key invalid` や `API error` メッセージ

**解決方法**:
- `.env`ファイルの`ANTHROPIC_API_KEY`が正しいか確認
- APIキーの有効期限やクレジットを確認
- [Anthropicコンソール](https://console.anthropic.com/)でAPIの状態を確認

### 4. メモリ不足エラー

**症状**: プログラムが途中で停止または遅くなる

**解決方法**:
- `max_posts_per_hashtag`を減らして、一度に処理する量を減らす
- 複数回に分けて実行する
- 不要なプログラムを終了してメモリを確保

### 5. ネットワークエラー

**症状**: `Connection timeout` や `Network unreachable` エラー

**解決方法**:
- インターネット接続を確認
- プロキシ設定が必要な環境の場合は、環境変数を設定
- ファイアウォールやVPNの設定を確認

### ログの確認方法

詳細なエラー情報は`logs/`ディレクトリのログファイルに記録されます：

```bash
# 最新のログファイルを確認
ls -lt logs/
cat logs/scraper_YYYYMMDD_HHMMSS.log

# エラー行のみを抽出
grep ERROR logs/scraper_YYYYMMDD_HHMMSS.log

# 最新のログをリアルタイムで監視
tail -f logs/scraper_YYYYMMDD_HHMMSS.log
```

## プロジェクト構造

```
DentalInstagramScraper/
├── main.py                 # メインスクリプト
├── config.yaml            # 設定ファイル
├── requirements.txt       # 依存パッケージ
├── .env.example          # 環境変数のサンプル
├── .env                  # 環境変数（gitignore）
├── .gitignore            # Git除外設定
├── README.md             # このファイル
├── src/                  # ソースコード
│   ├── __init__.py
│   ├── models.py         # データモデル
│   ├── instagram_collector.py    # Instagram収集
│   ├── data_extractor.py         # データ抽出
│   ├── fact_checker.py           # ファクトチェック
│   └── csv_exporter.py           # CSV出力
├── data/                 # データディレクトリ
│   ├── raw/             # 生データ（gitignore）
│   ├── processed/       # 処理済みデータ（gitignore）
│   └── output/          # 出力CSV
│       └── sample.csv   # サンプルデータ
├── logs/                # ログファイル（gitignore）
└── tests/               # テストコード
    └── test_models.py
```

## 開発者向け情報

### テストの実行

```bash
# 全テストを実行
pytest

# カバレッジ付きで実行
pytest --cov=src --cov-report=html
```

### コードの品質チェック

```bash
# flake8でコードスタイルをチェック
pip install flake8
flake8 src/ tests/

# blackでコードをフォーマット
pip install black
black src/ tests/
```

### 新機能の追加

1. `src/`ディレクトリに新しいモジュールを追加
2. `tests/`にテストコードを追加
3. `requirements.txt`に依存パッケージを追加（必要な場合）
4. README.mdを更新

## ライセンス

このプロジェクトは個人利用・商用利用ともに可能ですが、以下の条件を遵守してください：

- Instagram利用規約の遵守
- 個人情報保護法の遵守
- 医療広告ガイドラインの遵守（収集データを広告に使用する場合）

## サポート

問題が発生した場合は、以下の情報を含めてissueを作成してください：

1. エラーメッセージの全文
2. ログファイルの該当部分
3. 実行環境（OS、Pythonバージョン）
4. 再現手順

## 更新履歴

### v1.0.0 (2026-01-02)
- 初回リリース
- 基本機能の実装（Instagram収集、データ抽出、ファクトチェック、CSV出力）
