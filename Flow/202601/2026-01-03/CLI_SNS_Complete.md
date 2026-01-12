# CLI System Prompt: SNS自動化プロジェクト Phase 2-3 + Late API統合

## 推定実行時間
5.5-6.5時間

## プロジェクトコンテキスト

### 現在の状態
- **Phase 1 MVP**: 完了 (2/7スキル)
  - ✅ extract-top-tweets
  - ✅ scrape-tweet-details
- **Phase 2**: 未実装 (3スキル)
- **Phase 3**: 未実装 (2スキル)
- **Late API統合**: 未実装

### プロジェクトパス
- ベースディレクトリ: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS`
- スキルディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation`
- データディレクトリ: `{ベース}/data`
- スクリプトディレクトリ: `{ベース}/scripts`

## Task 1: Phase 2実装 (3スキル) - 推定30分

### 1.1 extract-content スキル
**目的**: Xタイムライン・ツイート詳細からコンテンツ抽出

**実装手順**:
1. スキル構造作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/extract-content
   ```

2. `SKILL.md` 作成:
   - **Input**: `x_timeline_*.json` または `tweet_details_*.json`
   - **Process**:
     - ツイート本文抽出
     - URL・ハッシュタグ解析
     - エンゲージメント指標計算 (いいね率、RT率)
     - スレッド構造解析
   - **Output**: `extracted_contents_*.json`
     ```json
     {
       "tweets": [
         {
           "tweet_id": "...",
           "text": "...",
           "urls": [...],
           "hashtags": [...],
           "engagement_rate": 0.05,
           "thread_position": 1
         }
       ]
     }
     ```

3. テストスクリプト作成 (`scripts/extract_content.py`):
   - 入力: `data/x_timeline_20260102_110035.json`
   - 実行: `python3 scripts/extract_content.py`
   - 検証: 抽出精度確認

### 1.2 analyze-replies スキル
**目的**: リプライ分析による反応パターン抽出

**実装手順**:
1. スキル構造作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/analyze-replies
   ```

2. `SKILL.md` 作成:
   - **Input**: `tweet_details_*.json`
   - **Process**:
     - リプライ感情分析 (positive/negative/neutral)
     - 質問パターン抽出
     - 共通トピック識別
     - インフルエンサーリプライ検出
   - **Output**: `reply_insights_*.json`
     ```json
     {
       "sentiment_distribution": {"positive": 0.6, "neutral": 0.3, "negative": 0.1},
       "common_questions": [...],
       "top_topics": [...],
       "influencer_replies": [...]
     }
     ```

3. テストスクリプト (`scripts/analyze_replies.py`):
   - Claude API使用 (感情分析)
   - 実行: `python3 scripts/analyze_replies.py`

### 1.3 research-topic スキル
**目的**: トピックリサーチと知見抽出

**実装手順**:
1. スキル構造作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/research-topic
   ```

2. `SKILL.md` 作成:
   - **Input**: トピックキーワード (例: "AI agents 2026")
   - **Process**:
     - Web検索 (Google/Perplexity API)
     - 記事要約生成
     - 統計データ収集
     - トレンド分析
   - **Output**: `research_findings_*.json`
     ```json
     {
       "topic": "AI agents 2026",
       "key_insights": [...],
       "statistics": {...},
       "trending_subtopics": [...],
       "source_urls": [...]
     }
     ```

3. テストスクリプト (`scripts/research_topic.py`):
   - 実行: `python3 scripts/research_topic.py --topic "AI agents 2026"`

### Phase 2 完了基準
- [ ] 3スキル全てのSKILL.md作成完了
- [ ] 各スキルのテストスクリプト実行成功
- [ ] サンプル出力ファイル生成確認

---

## Task 2: Phase 3実装 (2スキル) - 推定4-5時間

### 2.1 generate-sns-posts スキル
**目的**: マルチプラットフォーム投稿コンテンツ生成

**実装手順**:
1. スキル構造作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/generate-sns-posts
   ```

2. `SKILL.md` 作成:
   - **Input**:
     - `extracted_contents_*.json`
     - `reply_insights_*.json`
     - `research_findings_*.json`
   - **Process**:
     - Claude API使用 (コンテンツ生成)
     - プラットフォーム別最適化:
       - **X/Twitter**: 280文字、スレッド対応
       - **LinkedIn**: 3000文字、プロフェッショナルトーン
       - **Facebook**: 長文OK、画像推奨
       - **Threads**: 500文字、カジュアルトーン
     - ハッシュタグ最適化
     - 投稿時間帯推奨
   - **Output**: `posts_generated_*.json`
     ```json
     {
       "posts": [
         {
           "platform": "twitter",
           "content": "...",
           "hashtags": [...],
           "recommended_time": "2026-01-04T09:00:00Z",
           "is_thread": true,
           "thread_parts": [...]
         }
       ]
     }
     ```

3. プラットフォーム別ロジック実装:
   - 文字数制約チェック
   - トーン調整 (professional vs casual)
   - スレッド分割ロジック (Twitter)
   - 最初のコメントロジック (LinkedIn)

4. テストスクリプト (`scripts/generate_sns_posts.py`):
   - 実行: `python3 scripts/generate_sns_posts.py`
   - 検証: 各プラットフォーム向けコンテンツ確認

### 2.2 approve-and-schedule スキル
**目的**: Slack承認 + Late API投稿スケジューリング

**実装手順**:
1. スキル構造作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/approve-and-schedule
   ```

2. `SKILL.md` 作成:
   - **Input**: `posts_generated_*.json`
   - **Process**:
     1. **Slack承認フロー**:
        - Slack Webhook経由で投稿プレビュー送信
        - インタラクティブボタン (承認/却下/修正依頼)
        - タイムアウト処理 (24時間)
     2. **Late API投稿**:
        - 承認済み投稿をLate API経由でスケジュール
        - プラットフォーム: X, LinkedIn, Facebook, Threads
        - スケジュール時間設定
        - 投稿キュー管理
   - **Output**: `posts_queue_*.json`
     ```json
     {
       "scheduled_posts": [
         {
           "post_id": "...",
           "platform": "twitter",
           "scheduled_time": "2026-01-04T09:00:00Z",
           "late_api_job_id": "...",
           "status": "scheduled"
         }
       ]
     }
     ```

3. Slack承認実装 (`scripts/test_slack_approval.py`):
   - Slack Webhook URL設定 (`.env`)
   - インタラクティブメッセージ送信
   - 承認/却下ハンドラー実装

4. Late API統合 (`scripts/late_api_post.py`):
   - Late API認証設定
   - プラットフォーム別投稿API実装:
     - `POST /api/posts` (Twitter/X)
     - `POST /api/linkedin` (LinkedIn)
     - `POST /api/facebook` (Facebook)
     - `POST /api/threads` (Threads)
   - スケジュール設定
   - エラーハンドリング

5. 統合テスト:
   - エンドツーエンドテスト実行
   - 承認→投稿フロー確認
   - Late API投稿成功確認

### Phase 3 完了基準
- [ ] generate-sns-posts スキル完成 (4プラットフォーム対応)
- [ ] approve-and-schedule スキル完成 (Slack + Late API統合)
- [ ] エンドツーエンドテスト成功

---

## Task 3: Late API統合強化 - 推定1時間

### 3.1 Late API設定
**参照**: `aipm_v0/Flow/202601/2026-01-02/late_api_integration_proposals.md`

**実装内容**:
1. **Late API Pro プラン契約**:
   - 料金: $49/month
   - 対応プラットフォーム: 12 (X, LinkedIn, Facebook, Threads, Instagram等)
   - スケジュール投稿無制限

2. **認証設定** (`config/late_api_config.json`):
   ```json
   {
     "api_key": "LATE_API_KEY",
     "platforms": {
       "twitter": {"account_id": "..."},
       "linkedin": {"account_id": "..."},
       "facebook": {"page_id": "..."},
       "threads": {"account_id": "..."}
     }
   }
   ```

3. **投稿テンプレート実装**:
   - Twitter/X: スレッド対応
   - LinkedIn: 最初のコメント対応
   - Facebook: 画像最適化
   - Threads: カジュアルトーン

4. **エラーハンドリング**:
   - API制限対応 (rate limiting)
   - リトライロジック
   - 失敗通知 (Slack)

### 3.2 統合テスト
1. テスト投稿実行:
   ```bash
   python3 scripts/test_late_api_full_integration.py
   ```

2. 検証項目:
   - [ ] 各プラットフォームへの投稿成功
   - [ ] スケジュール設定確認
   - [ ] エラー時のSlack通知確認

---

## 最終成果物

### 1. 新規スキルファイル (5個)
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/extract-content/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/analyze-replies/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/research-topic/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/generate-sns-posts/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/approve-and-schedule/SKILL.md`

### 2. テストスクリプト (5個)
- `scripts/extract_content.py`
- `scripts/analyze_replies.py`
- `scripts/research_topic.py`
- `scripts/generate_sns_posts.py`
- `scripts/test_full_integration.py`

### 3. 設定ファイル
- `config/late_api_config.json`

### 4. 完了レポート
- `Flow/202601/2026-01-03/SNS_PHASE2-3_COMPLETION_REPORT.md`
  - 実装完了スキル一覧
  - テスト結果
  - Late API統合状況
  - 次のアクション (Phase 4検討)

---

## 重要な注意事項

1. **環境変数設定**:
   ```bash
   # .env ファイル
   ANTHROPIC_API_KEY=your_key
   SLACK_WEBHOOK_URL=your_webhook
   LATE_API_KEY=your_late_api_key
   ```

2. **依存パッケージ**:
   ```bash
   pip install anthropic slack-sdk requests
   ```

3. **エラーハンドリング**:
   - すべてのAPIコールにtry-except
   - Slack通知でエラー報告
   - ログファイル記録

4. **セキュリティ**:
   - API keyは`.env`管理
   - `.gitignore`に`.env`追加済み確認

---

## 実行開始コマンド

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# Phase 2実装
python3 scripts/extract_content.py
python3 scripts/analyze_replies.py
python3 scripts/research_topic.py --topic "AI agents 2026"

# Phase 3実装
python3 scripts/generate_sns_posts.py
python3 scripts/test_slack_approval.py
python3 scripts/late_api_post.py

# 統合テスト
python3 scripts/test_full_integration.py
```
