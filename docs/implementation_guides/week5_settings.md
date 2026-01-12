# Settings Management Rules

Claude Code設定管理の包括的ガイド（Week 5実装）。

## 概要

aipm_v0プロジェクトでは、**プロジェクト設定**と**個人設定**を明確に分離し、チーム全体で一貫性のある開発環境を維持します。

### 設定ファイル構成

| ファイル | 用途 | 管理方法 |
|---------|------|---------|
| `.claude/project-settings.json` | チーム共通設定（Git管理） | プロジェクト標準 |
| `~/.claude/settings.json` | 個人設定 | 各開発者が管理 |
| `scripts/setup_claude_settings.sh` | マージスクリプト | プロジェクトツール |

---

## プロジェクト設定 vs 個人設定

### プロジェクト設定（`.claude/project-settings.json`）

**Git管理対象**で、チーム全員が共有すべき設定：

1. **permissions** - 実行権限の統一
   - `git`, `npm`, `tmux`, `formatter` 等の許可設定
   - プロジェクトで使用するコマンドを事前許可

2. **hooks** - 自動化フックの統一
   - `PostToolUse`: コードフォーマット自動化（Week 2）
   - `Stop`: タスク完了通知（Week 3）

3. **enabledPlugins** - 使用プラグインの統一
   - `ralph-wiggum@claude-plugins-official` 等

4. **statusLine** - ステータスライン表示設定
   - `alwaysShowContext: true` でコンテキスト常時表示

### 個人設定（`~/.claude/settings.json`）

**個人管理**で、各開発者が自由に変更できる設定：

1. **model** - モデル選択（`sonnet` / `opus` / `haiku`）
   - コスト vs 品質のトレードオフを個人判断

2. **alwaysThinkingEnabled** - 思考モードの有効化
   - デバッグ時は `true`、通常は `false` 推奨

3. **その他の個人設定**
   - エディタ統合、キーバインド等

---

## セットアップ手順

### 1. 初回セットアップ

プロジェクト参加時、または設定が未構成の場合：

```bash
# プロジェクトルートで実行
cd /Users/yuichi/AIPM/aipm_v0

# マージ実行（確認プロンプト付き）
bash scripts/setup_claude_settings.sh
```

**実行内容**：
1. `~/.claude/settings.json` の自動バックアップ作成
2. プロジェクト設定との差分表示
3. 確認プロンプト
4. マージ実行（個人設定の `model` や `alwaysThinkingEnabled` は保持）

### 2. 強制マージ（確認なし）

CI/CD や自動化スクリプトで使用：

```bash
bash scripts/setup_claude_settings.sh -f
```

### 3. 差分確認のみ

マージ前に変更内容を確認：

```bash
bash scripts/setup_claude_settings.sh -d
```

**出力例**：
```
Project Permissions:
["Bash(git worktree:*)", "Bash(tmux:*)", ...]

Personal Permissions:
["Bash(grep:*)", "Bash(find:*)", ...]

Project Hooks:
{
  "PostToolUse": [...],
  "Stop": [...]
}
```

### 4. バックアップと復元

#### バックアップ作成

```bash
bash scripts/setup_claude_settings.sh -b
```

**保存先**: `~/.claude/backups/settings_YYYYMMDD_HHMMSS.json`

#### 復元

```bash
bash scripts/setup_claude_settings.sh -r
```

最新バックアップから復元（確認プロンプト付き）。

---

## プロジェクト設定の構造

### `.claude/project-settings.json` 詳細

```json
{
  "$schema": "https://code.claude.com/schemas/settings.json",
  "description": "aipm_v0 project-wide Claude Code settings (team-shared via Git)",
  "version": "1.0.0",

  "permissions": {
    "allow": [
      "Bash(git worktree:*)",    // Week 4: Git Worktrees
      "Bash(git branch:*)",
      "Bash(tmux:*)",            // Week 3-4: 並列実行
      "Bash(black:*)",           // Week 2: コードフォーマット
      "Bash(isort:*)",
      "Bash(prettier:*)",
      "Bash(npm run lint:*)",    // Week 5: lint/test許可
      "Bash(npm test:*)"
    ],
    "defaultMode": "delegate"
  },

  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/format_changed_file.sh \"$file_path\"",
        "description": "Auto-format code after Edit/Write (Week 2 implementation)"
      }]
    }],
    "Stop": [{
      "hooks": [
        {
          "type": "command",
          "command": "afplay /System/Library/Sounds/Glass.aiff",
          "description": "Play sound on task completion"
        },
        {
          "type": "command",
          "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/claude_notify.sh success \"Claude Code\" \"Task completed successfully\" \"Glass\"",
          "description": "Send macOS notification on task completion (Week 3 implementation)"
        }
      ]
    }]
  },

  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true
  },

  "statusLine": {
    "alwaysShowContext": true  // Week 5: コンテキスト常時表示
  },

  "notes": {
    "personalSettings": "Model selection (sonnet/opus/haiku) and alwaysThinkingEnabled should be configured in ~/.claude/settings.json (personal preference)",
    "setupInstructions": "Run: bash scripts/setup_claude_settings.sh to merge this into your personal settings",
    "gitManaged": "This file is tracked in Git for team-wide consistency",
    "weeks": {
      "week2": "PostToolUse hook for code formatting",
      "week3": "Stop hook for notifications",
      "week4": "Git worktrees permissions",
      "week5": "Project settings standardization + context monitoring"
    },
    "contextManagement": "Always show context usage in status line. Monitor /context regularly. Use /compact at 70%, /clear for new tasks."
  }
}
```

---

## コンテキスト管理

### コンテキスト監視の重要性

Claude Codeのコンテキストウィンドウは有限です。適切に管理しないと、「Context low」警告が頻発し、作業効率が低下します。

### 推奨ワークフロー

#### 1. ステータスラインで常時監視

`project-settings.json` の `statusLine.alwaysShowContext: true` により、コンテキスト使用率が常時表示されます。

#### 2. コンテキストレベル別アクション

| コンテキストレベル | アクション |
|-----------------|----------|
| **0-50%** | ✅ 通常通り作業継続 |
| **50-70%** | ⚠️ 監視強化、`/compact` を計画 |
| **70-85%** | 🔄 `/compact` を即座に実行 |
| **85-100%** | 🚨 `/clear` で新規セッション開始 |

#### 3. 定期的なコンテキストチェック

```bash
# コンテキスト使用率確認
/context

# コンテキスト圧縮（70%到達時）
/compact

# 新規セッション開始（タスク完了時）
/clear

# 特定ファイルを忘れる（一時ファイル読み込み後）
/forget <file_path>
```

#### 4. 監視スクリプトの活用

```bash
# コンテキスト管理ガイド表示
bash scripts/check_context_usage.sh

# 定期リマインダー（30分ごと）
bash scripts/check_context_usage.sh -w
```

### コンテキスト最適化のベストプラクティス

1. **`.claudeignore` の活用**
   - 不要なファイル/ディレクトリを除外
   - 大容量ファイル（ログ、データ、メディア）を除外

2. **サブエージェント（Task tool）の活用**
   - データ収集・リサーチは必ずサブエージェント化
   - 各サブエージェントは独立したコンテキストを持つ
   - 並列実行で効率化（詳細: @.claude/rules/context_management.md）

3. **1セッション = 1タスクの原則**
   - タスク完了後は即座に `/clear`
   - 複数タスクを1セッションで実行しない

4. **ファイル読み込みの最適化**
   - 必要な箇所のみ読み込み（`Read` の `offset`/`limit` パラメータ活用）
   - 読み込み後は `/forget` で削除

---

## チーム協働ガイドライン

### 設定変更のワークフロー

#### 1. プロジェクト設定の変更（チーム全体に影響）

```bash
# 1. .claude/project-settings.json を編集
vim .claude/project-settings.json

# 2. 変更をコミット
git add .claude/project-settings.json
git commit -m "feat: Add new permission for docker commands"

# 3. プッシュ
git push origin main

# 4. チームメンバーに通知
# Slackなどで「設定更新したので setup_claude_settings.sh を実行してください」と伝える
```

#### 2. 個人設定の変更（自分のみに影響）

```bash
# ~/.claude/settings.json を直接編集
vim ~/.claude/settings.json

# 変更例: モデルを opus に変更
{
  "model": "opus",
  "alwaysThinkingEnabled": true
}

# Git管理対象外のため、コミット不要
```

### 新規メンバーのオンボーディング

#### Step 1: リポジトリクローン

```bash
git clone https://github.com/your-org/aipm_v0.git
cd aipm_v0
```

#### Step 2: フォーマッタのインストール

```bash
bash scripts/setup_formatters.sh
```

**インストール内容**:
- black 25.12.0（Pythonフォーマッタ）
- isort 7.0.0（Pythonインポート整理）
- prettier 3.7.4（JS/TS/Markdown/JSON/YAMLフォーマッタ）
- jq 1.7.1（JSON処理ツール）

#### Step 3: 設定のマージ

```bash
bash scripts/setup_claude_settings.sh
```

確認プロンプトで内容を確認後、`y` で実行。

#### Step 4: 動作確認

```bash
# Claude Code起動
claude

# コンテキスト表示確認（ステータスライン）
# ファイル編集後の自動フォーマット確認
# タスク完了時の通知確認
```

---

## トラブルシューティング

### 問題1: マージ後に設定が反映されない

**症状**: `setup_claude_settings.sh` 実行後も、フックや許可設定が反映されない。

**原因**: Claude Codeがキャッシュを保持している。

**解決策**:
```bash
# Claude Codeを完全に再起動
# ターミナルを閉じて、新規ターミナルで claude コマンド実行
```

---

### 問題2: PostToolUseフックが動作しない

**症状**: ファイル編集後、自動フォーマットが実行されない。

**診断手順**:

1. **設定ファイル確認**
   ```bash
   cat ~/.claude/settings.json | jq '.hooks.PostToolUse'
   ```

   期待される出力:
   ```json
   [
     {
       "matcher": "Edit|Write",
       "hooks": [
         {
           "type": "command",
           "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/format_changed_file.sh \"$file_path\""
         }
       ]
     }
   ]
   ```

2. **スクリプト実行権限確認**
   ```bash
   ls -l scripts/format_changed_file.sh
   # -rwxr-xr-x であることを確認
   ```

3. **フォーマッタインストール確認**
   ```bash
   which black
   which isort
   which prettier
   ```

4. **環境変数確認**
   ```bash
   echo $CLAUDE_AUTO_FORMAT
   # 未設定または "true" であることを確認
   ```

**解決策**:
```bash
# フォーマッタ再インストール
bash scripts/setup_formatters.sh

# 設定再マージ
bash scripts/setup_claude_settings.sh -f

# Claude Code再起動
```

---

### 問題3: 並列実行でworktreeエラー

**症状**: `git worktree add` が失敗する。

**エラー例**:
```
fatal: 'feature-a' is already checked out at '/Users/yuichi/AIPM/worktrees/feature-a'
```

**解決策**:
```bash
# 既存worktreeをリスト表示
git worktree list

# 重複worktreeを削除
git worktree remove feature-a

# 再作成
bash scripts/setup_worktrees.sh feature-a
```

---

### 問題4: コンテキストが102%表示される

**症状**: コンテキスト使用率が100%を超えて表示される（Claude Codeのバグ）。

**解決策**:
```bash
# Claude Codeを再起動
# または
/clear  # 新規セッション開始
```

---

### 問題5: tmuxセッションが残り続ける

**症状**: `tmux ls` で大量の古いセッションが表示される。

**解決策**:
```bash
# 全tmuxセッションを終了
tmux kill-server

# または個別に終了
tmux kill-session -t claude-parallel-20260104-120000
```

---

## 設定変更履歴

### Week 2（2026-01-02）: PostToolUseフック

- 追加: `hooks.PostToolUse` でコードフォーマット自動化
- 追加: `permissions.allow` に `Bash(black:*)`, `Bash(isort:*)`, `Bash(prettier:*)`

### Week 3（2026-01-03）: Stopフック + tmux許可

- 拡張: `hooks.Stop` でシステム通知追加
- 追加: `permissions.allow` に `Bash(tmux:*)`, `Bash(ps:*)`, `Bash(kill:*)`

### Week 4（2026-01-03）: Git Worktrees許可

- 追加: `permissions.allow` に `Bash(git worktree:*)`, `Bash(git branch:*)`, `Bash(git log:*)`, `Bash(git status:*)`, `Bash(git diff:*)`
- 追加: `Bash(chmod:*)`, `Bash(mkdir:*)`, `Bash(ln:*)` でsymlink管理

### Week 5（2026-01-04）: チーム設定標準化

- 作成: `.claude/project-settings.json`（Git管理）
- 作成: `scripts/setup_claude_settings.sh`（マージスクリプト）
- 最適化: `.claudeignore`（プロジェクト固有除外ルール）
- 追加: `statusLine.alwaysShowContext: true`
- 追加: `permissions.allow` に `Bash(npm run lint:*)`, `Bash(npm test:*)`
- 作成: `scripts/check_context_usage.sh`（コンテキスト監視ガイド）

---

## 参照

### 関連ドキュメント

- **コンテキスト管理の詳細**: @.claude/rules/context_management.md
- **並列実行ガイド**: @.claude/rules/parallel_execution.md
- **Week 2実装詳細**: @.claude/rules/code_formatting.md
- **Week 3実装詳細**: @.claude/rules/parallel_execution_terminal.md
- **Week 4実装詳細**: @.claude/rules/parallel_execution_worktrees.md

### 関連スクリプト

- **設定マージ**: `scripts/setup_claude_settings.sh`
- **フォーマッタセットアップ**: `scripts/setup_formatters.sh`
- **コードフォーマット**: `scripts/format_changed_file.sh`
- **システム通知**: `scripts/claude_notify.sh`
- **コンテキスト監視**: `scripts/check_context_usage.sh`
- **worktree管理**: `scripts/setup_worktrees.sh`
- **並列実行**: `scripts/start_parallel_claude.sh`, `scripts/start_claude_in_worktrees.sh`

### 公式ドキュメント

- **Claude Code Settings**: https://code.claude.com/docs/en/settings.md
- **Claude Code Hooks**: https://code.claude.com/docs/en/hooks.md
- **Claude Code CLI Reference**: https://code.claude.com/docs/en/cli-reference.md
