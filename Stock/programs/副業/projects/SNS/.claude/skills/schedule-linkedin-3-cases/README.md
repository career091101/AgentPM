# schedule-linkedin-3-cases

LinkedIn投稿3案を自動生成し、Late API経由で翌日8:00 JSTに一括予約投稿するスキル（高野メソッド準拠）。

## クイックスタート

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# Claude Code CLI
/schedule-linkedin-3-cases

# または直接実行
python3 scripts/schedule_linkedin_post.py
```

## 実行フロー

1. **次の予約投稿日を計算**:
   - `data/post_result_scheduled_*.json` から最新ファイルを検索
   - 最新日付の**翌日8:00 JST**を計算
   - ファイルがない場合は**明日8:00 JST**

2. **コンテンツ生成（3案）**:
   - `data/research_findings_*_v2_*.json` から最新リサーチデータを読み込み
   - Claude API経由で3案を生成:
     - 案1: 数字インパクト型
     - 案2: 衝撃発言型
     - 案3: 問題提起型

3. **Late API予約投稿**:
   - 全3案を同じ時刻（翌日8:00 JST → UTC変換）に予約投稿
   - 成功時: `post_id` をログに記録
   - 失敗時: Markdownファイル生成

4. **ユーザー確認・選択**:
   - Late APIダッシュボード（https://getlate.dev/dashboard）で3案を確認
   - 最適な1案を選択し、残り2案を削除

## 環境変数設定

`.env` ファイルに以下を設定:

```bash
# Late API
LATE_API_KEY=sk_your-late-api-key-here
LATE_LINKEDIN_ACCOUNT_ID=your-linkedin-account-id

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-api03-your-api-key-here
```

## 出力ファイル

### 成功時
- `data/post_result_scheduled_{YYYYMMDD}.json`: 予約投稿ログ

### 失敗時
- `data/manual_posts/linkedin_{YYYYMMDD}.md`: 手動投稿用Markdown

## 詳細ドキュメント

スキル定義: `.claude/skills/schedule-linkedin-3-cases/SKILL.md`
