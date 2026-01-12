# SNS運用自動化プロジェクト

**月間インプレッション100万達成、作成時間68%削減を実現するSNS運用自動化システム**

---

## 📊 プロジェクト概要

SNS運用の全工程を自動化し、3ヶ月で以下を達成：
- **月間インプレッション**: 346,766 → 1,000,000（+188%）
- **投稿作成時間**: 47.5分 → 15分（68%削減）
- **X活性化**: 4.4% → 10%以上の貢献度

### 対象プラットフォーム
- **Facebook** / **LinkedIn** / **X** / **Instagram** / **Threads**

---

## 🚀 Month 1: Xタイムライン監視システム（Claude In Chrome）

### セットアップ（Month 1）

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 依存ライブラリインストール
pip install -r requirements.txt

# Claude In Chromeが利用可能であることを確認
# ブラウザでXにログイン済みであることを確認
```

### Xタイムライン自動収集（Claude In Chrome）

**実行方法**:
```
ClaudeCodeで以下のコマンドを実行:
/sns-automation

または手動で「SNS自動化」「X収集」とメッセージ送信
```

**実行内容**:
1. Claude In Chromeで新規タブ作成
2. Xホームタイムライン (https://x.com/home) に遷移
3. タイムラインをスクロールして200件のツイートを収集
4. エンゲージメント率でフィルタリング（ER>5%、imp>1,000）
5. 上位10件をJSON形式で保存

**出力データ**:
- `data/x_timeline_{YYYY-MM-DD}.json` - 高エンゲージメント投稿（上位10件）

**所要時間**: 5-10分（200件収集、20-30回スクロール）

**推奨実行時刻**: 毎朝7:00（手動トリガー）

### Month 1末目標

| KPI | 現状 | 目標 |
|-----|------|------|
| X月間imp | 15,242 | **30,000** (+97%) |
| ネタ収集時間 | 10-15分/日 | **2-3分/日** |

---

## 📁 Instagram & Threads データ収集（既存機能）

### セットアップ（既存）

```bash
# Playwright依存追加
playwright install chromium
```

### 一括実行

```bash
cd scripts
python3 collect_all_sns_data.py
```

実行内容:
1. Instagram Insightsからデータ収集
2. Threads 週間総括からデータ収集

### 個別実行

**Instagramのみ**:
```bash
python3 scripts/scrape_instagram_insights.py
```

**Threadsのみ**:
```bash
python3 scripts/scrape_threads_insights.py
```

### 出力データ（既存）

- `Instagram/instagram_summary_*.csv` - Instagramアカウントサマリー
- `Instagram/instagram_posts_*.csv` - Instagram個別投稿データ
- `Threads/threads_weekly_recap_*.csv` - Threads週間総括データ
- `Threads/threads_insights_*.csv` - Threads洞察データ（フォロワー100人以上）

### 注意事項

1. **初回実行時**: ブラウザが開き、手動でログインが必要
2. **ログイン状態**: 次回以降は自動保存
3. **Threads洞察データ**: フォロワー100人以上で詳細データ利用可能

---

## 📁 ディレクトリ構造

```
SNS/
├── README.md                        # 本ドキュメント
├── .env.example                     # 環境変数サンプル
├── requirements.txt                 # Python依存ライブラリ
│
├── config/                          # 設定ファイル
│   └── automation_config.yaml       # Month 1: インフルエンサーリスト、フィルタリング基準
│
├── scripts/                         # 実行スクリプト
│   ├── x_timeline_collector.py      # Month 1: Xタイムライン収集
│   ├── scrape_instagram_insights.py # 既存: Instagram収集
│   ├── scrape_threads_insights.py   # 既存: Threads収集
│   └── collect_all_sns_data.py      # 既存: 一括収集
│
├── templates/                       # Month 1: テンプレート
│   └── x_post_template_v2.md        # X投稿テンプレート（130-180字）
│
├── data/                            # データ保存先
│   └── x_timeline_{YYYY-MM-DD}.json # Month 1: X収集結果
│
├── logs/                            # ログファイル
│   └── x_timeline_collector.log     # Month 1: 収集ログ
│
├── documents/                       # プロジェクト管理（PMBOK準拠）
│   ├── 1_initiating/                # プロジェクト憲章
│   ├── 2_discovery/                 # ペルソナ、課題分析
│   └── 3_planning/                  # WBS、PRD
│
├── X/                               # Xメディア別攻略情報
├── Instagram/                       # Instagramメディア別攻略情報
├── Facebook/                        # Facebookメディア別攻略情報
├── LinkedIn/                        # LinkedInメディア別攻略情報
├── Threads/                         # Threadsメディア別攻略情報
└── General/                         # 複数メディア横断分析
```

---

## 🔧 トラブルシューティング

### Claude In Chromeが利用できない

**症状**:
`/sns-automation`実行時にClaude In Chromeツールが使えない

**解決策**:
1. Claude In Chrome拡張機能がインストールされているか確認
2. ブラウザを再起動
3. ClaudeCodeセッションを再起動

### Xにログインしていない

**症状**:
タイムライン読み取り時に「ログインしてください」と表示される

**解決策**:
1. ブラウザでhttps://x.com にアクセス
2. ログイン
3. 再度`/sns-automation`を実行

### ページ読み取りエラー

**症状**:
`read_page`ツールでツイートが読み取れない

**解決策**:
1. ページ読み込み完了を待つ（3秒）
2. スクロールして追加ツイートを表示
3. `filter="all"`オプションを使用

---

## 📚 詳細ドキュメント

### Month 1（X自動化）

- **X投稿テンプレート**: `templates/x_post_template_v2.md`
- **バズ構文100選**: `knowledge/X/resources/Twitterのバズ構文 100選.md`
- **X best practices**: `knowledge/X/best_practices.md`（35項目）
- **戦略計画**: `/Users/yuichi/.claude/plans/virtual-sleeping-marshmallow.md`

### 既存（Instagram/Threads）

- **Instagram**: `Instagram/DATA_COLLECTION_GUIDE.md`
- **Threads**: `Threads/DATA_COLLECTION_GUIDE.md`

### プロジェクト管理

- **課題分析**: `documents/2_discovery/SNS運用戦略_課題深掘りレポート_20260101.md`
- **ペルソナv2**: `documents/2_discovery/persona_v2.md`

---

## 🔜 次のアクション

### Month 1 Week 1（今すぐ）

1. **環境確認**: Claude In Chrome拡張機能がインストールされているか確認
2. **Xログイン**: ブラウザでhttps://x.com にログイン
3. **テスト実行**: ClaudeCodeで`/sns-automation`を実行
4. **収集結果確認**: `data/x_timeline_YYYYMMDD.json`を確認

### Month 1 Week 2-4

5. **毎朝実行を習慣化**（推奨時刻: 7:00）
6. **収集データ分析開始**（高エンゲージメント投稿の傾向分析）
7. **フォローリスト最適化**（エンゲージメント高いアカウントを追加フォロー）

### Month 2以降（実装予定）

- **LinkedIn/Facebook投稿自動生成**
- **Reply Guy自動化**
- **週次PDCAレポート自動生成**

---

**作成日**: 2026-01-01
**更新日**: 2026-01-01（Claude In Chrome対応）
**プロジェクト**: SNS運用戦略 Month 1-3
**バージョン**: v3.0（Claude In Chrome版）
