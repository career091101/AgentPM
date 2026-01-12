# T007: Xブックマーク傾向分析 実行ガイド

**タスク概要**: Xのブックマークを自動取得し、5エージェント並列分析で傾向レポートを生成

**推定実行時間**: 85-115分（並列実行時）

---

## 準備完了チェックリスト

- [x] スクレイピングスクリプト作成完了: `scripts/x_bookmark_scraper.py`
- [x] 環境変数ファイル作成完了: `.env`
- [x] Pythonライブラリインストール完了: `venv/`
- [x] Phase 2実行ガイド作成完了: `phase2_agent_execution_guide.md`
- [ ] `.env`に実際の認証情報を設定（ユーザー作業）
- [ ] スクリプト実行（ユーザー作業）
- [ ] Phase 2エージェント並列起動（ユーザー作業）

---

## Phase 1: ブックマークデータ取得（60-90分）

### ステップ1: 認証情報の設定（5分）

`.env`ファイルを編集し、実際のXアカウント情報を設定してください：

```bash
# エディタで開く
nano /Users/yuichi/AIPM/aipm_v0/.env

# または直接編集
```

**設定内容**:
```env
X_USERNAME=your_actual_username_or_email
X_PASSWORD=your_actual_password
```

保存後、ファイルの内容を確認：
```bash
cat /Users/yuichi/AIPM/aipm_v0/.env
```

### ステップ2: スクリプト実行（55-85分）

仮想環境を有効化してスクリプトを実行：

```bash
cd /Users/yuichi/AIPM/aipm_v0
source venv/bin/activate
python3 scripts/x_bookmark_scraper.py
```

**実行時の流れ**:

1. Chromiumブラウザが自動起動
2. https://x.com/i/bookmarks に移動
3. **手動でXにログイン**（初回のみ、Cookie保存後は自動）
   - ユーザー名/メールアドレスを入力
   - パスワードを入力
   - 二段階認証（必要な場合）
4. ログイン成功を検出すると自動的にブックマーク取得開始
5. スクロールしながら全ブックマークを収集（進捗はターミナルに表示）
6. 完了すると以下に保存:
   - `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data.json`

**ログ確認**:
```bash
tail -f /Users/yuichi/AIPM/aipm_v0/scripts/x_bookmark_scraper.log
```

### ステップ3: データ検証（5分）

取得したデータを確認：

```bash
# ファイル存在確認
ls -lh /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data.json

# 件数確認（JSONのmetadata.total_bookmarksを確認）
cat /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data.json | grep "total_bookmarks"

# 最初の投稿サンプル確認
cat /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data.json | head -50
```

**期待される出力**:
```json
{
  "metadata": {
    "scrape_date": "2025-12-31T...",
    "total_bookmarks": 150,
    "scrape_duration_seconds": 180
  },
  "bookmarks": [
    {
      "id": "...",
      "text": "...",
      "author_username": "...",
      ...
    }
  ]
}
```

---

## Phase 2: 並列分析（25分）

**重要**: x_bookmarks_data.jsonが正常に取得されていることを確認してから実行してください。

### エージェントA-D: 並列起動（20-25分）

**単一メッセージで4つのエージェントを並列起動します**。

以下のプロンプトをClaude Codeに送信してください：

```
Phase 2の分析を開始します。以下の4つのエージェントを並列起動してください：

【エージェントA: テーマ分類・キーワード抽出】
{phase2_agent_execution_guide.mdのエージェントAプロンプトをコピー}

【エージェントB: 投稿者傾向分析】
{phase2_agent_execution_guide.mdのエージェントBプロンプトをコピー}

【エージェントC: 時間帯分析】
{phase2_agent_execution_guide.mdのエージェントCプロンプトをコピー}

【エージェントD: エンゲージメント相関分析】
{phase2_agent_execution_guide.mdのエージェントDプロンプトをコピー}

各エージェントをrun_in_background=Trueで起動し、全て完了したらTaskOutputで結果を取得してください。
```

**または、直接Task toolを使用**:

```python
# このコードブロックをClaude Codeに渡す
Task(subagent_type="general-purpose", prompt="...", run_in_background=True, model="sonnet")  # エージェントA
Task(subagent_type="general-purpose", prompt="...", run_in_background=True, model="haiku")   # エージェントB
Task(subagent_type="general-purpose", prompt="...", run_in_background=True, model="haiku")   # エージェントC
Task(subagent_type="general-purpose", prompt="...", run_in_background=True, model="sonnet")  # エージェントD
```

### 進捗確認

エージェント実行中、以下のファイルが順次生成されます：

```bash
# 生成ファイル確認
ls -lh /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/

# 期待されるファイル:
# - theme_analysis.md （エージェントA）
# - author_analysis.md （エージェントB）
# - time_analysis.md （エージェントC）
# - engagement_analysis.md （エージェントD）
```

### エージェントE: レポート統合（20-25分）

**エージェントA-D完了後**、エージェントEを起動：

```
エージェントE（レポート統合生成）を起動してください。

{phase2_agent_execution_guide.mdのエージェントEプロンプトをコピー}
```

### 最終成果物確認

```bash
# 最終レポート確認
cat /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmark_analysis_report.md
```

---

## 成果物一覧

全て完了すると、以下のファイルが生成されます：

```
Flow/202512/2025-12-31/
├── x_bookmarks_data.json              # Phase 1: ブックマークデータ（150件想定）
├── theme_analysis.md                  # Phase 2A: テーマ分類
├── author_analysis.md                 # Phase 2B: 投稿者傾向
├── time_analysis.md                   # Phase 2C: 時間帯分析
├── engagement_analysis.md             # Phase 2D: エンゲージメント相関
├── x_bookmark_analysis_report.md      # Phase 2E: 統合レポート（最終成果物）
└── charts/                            # グラフ画像（エージェントEが生成）
    ├── theme_distribution.png
    ├── top_authors.png
    ├── time_distribution.png
    └── engagement_scatter.png
```

---

## トラブルシューティング

### スクリプト実行時

**問題**: `playwright: command not found`
**解決**: Playwrightブラウザのインストール
```bash
source venv/bin/activate
playwright install chromium
```

**問題**: ログイン検出に失敗
**解決**: ブラウザで手動ログイン後、30秒待機してください。Cookie保存後は自動ログインされます。

**問題**: スクロールが途中で止まる
**解決**: スクリプトは自動的に5回連続で新規取得なしの場合に終了します。これは正常動作です。

### Phase 2実行時

**問題**: x_bookmarks_data.jsonが見つからない
**解決**: Phase 1が正常完了しているか確認。ファイルパスを確認してください。

**問題**: エージェントが並列起動されない
**解決**: 単一メッセージ内で複数のTask toolを呼び出す必要があります。`run_in_background=True`を指定してください。

**問題**: グラフが生成されない
**解決**: matplotlibがインストールされているか確認：
```bash
source venv/bin/activate
pip install matplotlib
```

---

## 実行時間の目安

| フェーズ | タスク | 推定時間 |
|---------|--------|---------|
| Phase 1 | 認証情報設定 | 5分 |
| Phase 1 | スクリプト実行（データ取得） | 55-85分 |
| Phase 1 | データ検証 | 5分 |
| **Phase 1 合計** | | **65-95分** |
| Phase 2 | エージェントA-D 並列実行 | 20-25分 |
| Phase 2 | エージェントE レポート統合 | 20-25分 |
| **Phase 2 合計** | | **40-50分** |
| **総合計** | | **105-145分** |

**並列実行の効果**: Phase 2を45-70分短縮（逐次実行と比較）

---

## 次のステップ

レポート生成後、以下のアクションを実行できます：

1. **投稿戦略の最適化**: レポートの「6. アクションプラン」を参照
2. **フォローアカウント追加**: 推奨アカウントをフォロー
3. **コンテンツキュレーション改善**: 多様なテーマのブックマークを意識
4. **定期実行の設定**: 月次で同じ分析を実行し、トレンド変化を追跡

---

**実行準備完了！** Phase 1から順次実行してください。
