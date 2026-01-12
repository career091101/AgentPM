# Week 4 Phase 1: Claude Code CLI セッション管理仕様調査レポート

**調査日**: 2026-01-09
**調査対象**: Claude Code CLI v2.1.1
**出力ファイル**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-09/week4_phase1_claude_cli_spec.md`

---

## 目次

1. [Claude Code CLIバージョン情報](#claude-code-cliバージョン情報)
2. [`--resume` フラグの仕様](#--resume-フラグの仕様)
3. [`--continue` フラグの仕様](#--continue-フラグの仕様)
4. [セッション一覧表示機能](#セッション一覧表示機能)
5. [セッション名の推奨パターン](#セッション名の推奨パターン)
6. [バックグラウンド実行との組み合わせ](#バックグラウンド実行との組み合わせ)
7. [セッション分岐機能（--fork-session）](#セッション分岐機能--fork-session)
8. [実践ガイド](#実践ガイド)
9. [参考資料](#参考資料)

---

## Claude Code CLIバージョン情報

### インストール済みバージョン

```bash
$ claude --version
2.1.1 (Claude Code)
```

**バージョン**: 2.1.1
**リリース日**: 2025年以降
**アップデート方法**:
```bash
# アップデート確認と自動インストール
claude update

# 特定バージョンをインストール
claude install latest   # 最新版
claude install stable   # 安定版
claude install 2.1.1    # 特定バージョン
```

### ヘルスチェック機能

```bash
# 自動アップデータのヘルスチェック
claude doctor
```

---

## `--resume` フラグの仕様

### 基本仕法

```bash
# 長形式
claude --resume <session-id-or-name>

# 短縮形
claude -r <session-id-or-name>

# インタラクティブピッカーで選択（引数なし）
claude --resume
claude -r
```

### 使用方法

#### 1. セッションIDで指定（フルID）

```bash
# UUID形式の完全なセッションID
claude --resume a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**メリット**:
- 一意性が保証されている
- 自動化スクリプトに向いている
- セッション履歴ファイルから取得可能

#### 2. セッション名で指定（推奨）

```bash
# セッション名で指定（ブランチ名推奨）
claude --resume auth-refactor

# 短縮形も可能（部分一致）
claude --resume auth
```

**メリット**:
- 人間が読みやすい
- ワークフロー管理が容易
- プロジェクト構成に合わせやすい

#### 3. インタラクティブピッカー（推奨：選択に迷う場合）

```bash
# セッション一覧から選択
claude --resume

# 検索語で絞り込み
claude --resume feature
```

**インタラクティブピッカーの機能**:
- 最近のセッション一覧表示
- キーボードナビゲーション（矢印キー）
- セッション検索機能
- `P` キー: プレビュー表示
- `Enter`: 選択したセッションを再開

### セッション再開時の動作

| 項目 | 説明 |
|------|------|
| **コンテキスト保持** | ✅ 完全保持（会話履歴、ファイル状態、パーミッション） |
| **作業ディレクトリ** | ✅ 元のディレクトリで再開 |
| **ファイル変更** | ✅ 前回の編集内容を記憶 |
| **セッションID** | ⚠️ デフォルトではID不変（元のセッションに追記） |

### `--resume` のユースケース

1. **中断した作業の再開**
   ```bash
   # 1時間前に中断した認証実装の続き
   claude --resume auth-implementation
   ```

2. **長時間タスクの継続**
   ```bash
   # データマイグレーション（1時間目）
   cd worktrees/data-migration/aipm_v0
   claude

   # 1時間後、同じワークツリーで再開
   claude --resume data-migration
   ```

3. **別のターミナルから再開**
   ```bash
   # 別ターミナル、別ディレクトリから再開可能
   cd /tmp
   claude --resume auth-refactor
   # → 元のディレクトリでセッション継続
   ```

---

## `--continue` フラグの仕様

### 基本仕法

```bash
# 長形式
claude --continue

# 短縮形
claude -c
```

### 機能と動作

| 項目 | 説明 |
|------|------|
| **動作** | 最新のセッションを自動的に継続 |
| **引数** | 不要（省略可能） |
| **セッション検出** | 現在のディレクトリ内の最新セッション |
| **ユースケース** | 直前の作業の続き、素早い再開 |

### 使用シーン

```bash
# 直前の作業を続ける（最速再開）
claude --continue

# セッションIDを覚えていない場合
claude -c

# すぐに前回のコンテキストを回復したい場合
claude -c
```

### `--resume` vs `--continue` の使い分け

| 項目 | `--resume` | `--continue` |
|------|-----------|-------------|
| **セッション指定** | 明示的に指定 | 最新セッションを自動選択 |
| **使用例** | `--resume auth-refactor` | `--continue` |
| **適用範囲** | 任意のセッション | 現在のディレクトリの最新セッション |
| **推奨用途** | セッションID/名を知っている | 直前の作業をすぐ続けたい |
| **セッション選択** | 対話的または指定 | 自動（最新） |

### 実践例

```bash
# シナリオ: 認証機能を実装中に一度コマンドラインに戻った

# 再開（直前の続きをすぐ）
$ claude --continue

# または短縮形
$ claude -c

# コンテキスト完全保持で再開
# → 前回の編集内容、会話履歴、ファイル状態が復元される
```

---

## セッション一覧表示機能

### セッション保存場所

```bash
# Claude Code セッション履歴
~/.claude/history.jsonl

# セッション環境情報
~/.claude/session-env/  (複数ファイル)

# プロジェクト情報
~/.claude/projects/
```

### セッション情報の確認方法

#### 1. CLIでのリスト表示

```bash
# インタラクティブピッカー（セッション一覧）
claude --resume

# 最新セッション自動選択
claude --continue
```

#### 2. ファイル直接確認（高度な用途）

```bash
# セッション履歴ファイル確認
cat ~/.claude/history.jsonl | jq '.' | head -50

# JSONL形式なので、最新行がセッション情報
tail -1 ~/.claude/history.jsonl | jq '.'
```

**出力例**:
```json
{
  "type": "session",
  "session_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "name": "auth-refactor",
  "timestamp": "2026-01-09T10:30:00Z",
  "directory": "/Users/yuichi/AIPM/worktrees/feature-auth/aipm_v0",
  "messages": 42,
  "last_active": "2026-01-09T10:45:00Z"
}
```

### セッション一覧スクリプト（カスタム）

```bash
#!/bin/bash
# セッション一覧を見やすく表示

echo "=== Recent Claude Code Sessions ==="
tail -20 ~/.claude/history.jsonl | \
  jq -r 'select(.type=="session") |
          "\(.name) | \(.session_id) | \(.directory)"' | \
  column -t -s '|'
```

---

## セッション名の推奨パターン

### 命名規則（Git Worktrees連携）

セッション名はワークツリーのブランチ名と統一することで、管理を簡素化します。

```bash
# Feature実装
feature-auth
feature-api-v2
feature-ui-redesign

# バグ修正
fix-login-issue
fix-api-timeout

# リファクタリング
refactor-auth-system
refactor-db-queries

# 実験・プロトタイピング
exp-graphql-migration
exp-new-framework

# ホットフィックス（本番対応）
hotfix-security-issue
```

### セッション名の設定方法

#### 1. セッション開始時に設定

```bash
# セッション開始
cd /Users/yuichi/AIPM/worktrees/auth-refactor/aipm_v0
claude

# セッション内で /rename コマンド実行
# → プロンプト内で:
# /rename auth-refactor-session
```

#### 2. ワークツリー + セッション名の統一例

```bash
# ワークツリー: feature-1
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0
claude

# セッション名: feature-1
# → 再開: claude --resume feature-1
```

#### 3. 複雑な作業の場合：拡張パターン

```bash
# 複数フェーズの作業
feature-payment-frontend-phase1  # 初期実装
feature-payment-frontend-phase2  # テスト・デバッグ
feature-payment-backend-phase1   # API実装

# 再開時に明確
claude --resume feature-payment-frontend-phase2
```

### 推奨ベストプラクティス

1. **ブランチ名とセッション名を一致させる**
   ```bash
   ブランチ: feature-auth
   セッション名: feature-auth
   再開: claude --resume feature-auth
   ```

2. **タイムスタンプは不要**（CLIが自動管理）

3. **短い、意味のある名前**
   - ✅ `auth-refactor` (5-6単語以下)
   - ❌ `auth-refactor-2026-01-09-phase-1-attempt-3` (長すぎる)

4. **特殊文字は避ける**
   - ✅ `feature-api-v2`
   - ❌ `feature/api-v2!@#`

---

## バックグラウンド実行との組み合わせ

### パターン1: `nohup` + `--resume`

```bash
# バックグラウンド実行：セッション再開
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0

nohup claude --resume feature-1-session > ~/claude_feature1.log 2>&1 &

# PIDを記録
echo $! > ~/claude_feature1.pid
```

**利点**:
- ターミナルを閉じてもプロセス継続
- ログファイルに出力記録
- PID記録で管理可能

**ログ確認**:
```bash
# リアルタイムログ
tail -f ~/claude_feature1.log

# 実行状況確認
ps aux | grep claude

# PIDから確認
kill $(cat ~/claude_feature1.pid)
```

### パターン2: `nohup` + `--continue`

```bash
# 最新セッションをバックグラウンド続行
nohup claude --continue > ~/claude_latest.log 2>&1 &
disown
```

**用途**:
- 直前の作業を自動継続
- セッションIDを指定したくない場合

### パターン3: `tmux` を使用した永続化

```bash
# tmuxセッション作成
tmux new-session -d -s claude-long-task

# セッション内で実行
tmux send-keys -t claude-long-task "cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0" Enter
tmux send-keys -t claude-long-task "claude --resume feature-1-long-task" Enter

# デタッチ（ターミナルを閉じても継続）
tmux detach-client -s claude-long-task

# 後で再接続
tmux attach-session -t claude-long-task
```

**メリット**:
- 完全なセッション永続化
- 別ターミナルからアクセス可能
- 複数ウィンドウ・ペイン管理可能

### パターン4: 複数ワークツリーの並列バックグラウンド実行

```bash
#!/bin/bash
# 3つのワークツリーで並列実行

WORKTREES=("feature-1" "feature-2" "feature-3")
LOG_DIR=~/claude_logs

mkdir -p $LOG_DIR

for wt in "${WORKTREES[@]}"; do
    cd /Users/yuichi/AIPM/worktrees/$wt/aipm_v0

    echo "Starting Claude in $wt..."
    nohup claude --resume $wt > $LOG_DIR/${wt}.log 2>&1 &
    echo $! > $LOG_DIR/${wt}.pid
done

echo "All worktrees started in background"
```

**確認方法**:
```bash
# 全プロセス確認
ps aux | grep "claude --resume"

# ログ監視
tail -f ~/claude_logs/*.log

# 実行停止
for pid in ~/claude_logs/*.pid; do
    kill $(cat $pid)
done
```

---

## セッション分岐機能（`--fork-session`）

### 概要

`--fork-session` フラグを使用すると、既存セッションを再開する際に新しいセッションIDを生成し、元のセッション履歴を保持したまま別の道を探索できます。

### 基本仕法

```bash
# セッション再開＋新しいセッションID生成
claude --resume <session-id> --fork-session

# 短縮形
claude -r <session-id> --fork-session
```

### `--fork-session` なし（デフォルト）vs あり

| 項目 | デフォルト（ID継続） | `--fork-session` |
|------|-----------------|----------------|
| **セッションID** | 元のIDを使用 | 新しいIDを生成 |
| **履歴** | 元のセッションに追記 | 新しいセッションとして開始 |
| **元のセッション** | 影響を受ける | 保持される |
| **ユースケース** | 単純な継続 | 別の手法を試す |

### ユースケース

#### 1. 異なるアプローチの試行

```bash
# 初期セッション: REST API設計
claude
# → セッションID: api-design-001

# REST APIで1時間作業後...
# 異なるアプローチ（GraphQL）を試したい

# フォーク：新しいセッションで別の設計を試す
claude --resume api-design-001 --fork-session

# → 新セッションID: api-design-fork-001
# → 元の api-design-001 は保持される
# → 後で api-design-001 に戻って REST 続行可能
```

#### 2. リスク軽減（破壊的変更の試行）

```bash
# 本セッション：安定版実装
claude --resume production-impl

# 実験セッション：新技術試行（破壊的な変更）
claude --resume production-impl --fork-session

# 実験が失敗しても、元のセッションはそのまま
```

#### 3. 複数案の並列検討

```bash
# セッションA: パフォーマンス最適化（アプローチ1）
claude --resume optimization-base --fork-session
# → optimization-fork-001

# セッションB: パフォーマンス最適化（アプローチ2）
claude --resume optimization-base --fork-session
# → optimization-fork-002

# 後で2つの実装結果を比較可能
```

### 実装例

```bash
# Step 1: 基本設計セッション
cd /Users/yuichi/AIPM/worktrees/design/aipm_v0
claude
# → セッション名: api-design

# Step 2: 1時間作業後、別の実装を試す
claude --resume api-design --fork-session
# → 新セッション開始（元は保持）

# Step 3: 両方を比較
claude --resume api-design          # 元のセッション
claude --resume api-design-fork-001 # フォークされたセッション

# 最良の方法を選択して統合
```

---

## 実践ガイド

### シナリオ1: Week 4 ワークツリー + セッション管理

```bash
# ① ワークツリー作成
cd /Users/yuichi/AIPM/aipm_v0
bash scripts/setup_worktrees.sh auth-refactor api-update

# ② 各ワークツリーでセッション開始
cd /Users/yuichi/AIPM/worktrees/auth-refactor/aipm_v0
claude

# セッション内で /rename auth-refactor を実行

# ③ 別のワークツリーで作業
cd /Users/yuichi/AIPM/worktrees/api-update/aipm_v0
claude

# ④ 後で継続
claude --resume auth-refactor    # auth-refactor セッション再開
claude --resume api-update       # api-update セッション再開

# ⑤ 最新セッション続行（どちらのワークツリーでも動作）
claude --continue
```

### シナリオ2: 長時間タスク（バックグラウンド実行）

```bash
# ① セッション開始（データマイグレーション）
cd /Users/yuichi/AIPM/worktrees/data-migration/aipm_v0
claude

# セッション名: data-migration

# ② 1時間後、ターミナルを閉じて終了
# Ctrl+C で一度中断

# ③ バックグラウンドで再開
nohup claude --resume data-migration > ~/logs/migration.log 2>&1 &
disown

# ④ ログ監視
tail -f ~/logs/migration.log

# ⑤ 進捗確認（別ターミナル）
ps aux | grep "claude --resume data-migration"

# ⑥ 完了後、成果確認
claude --resume data-migration
# コンテキスト完全保持で再開
```

### シナリオ3: セッション分岐での複数実装検証

```bash
# ① 初期実装セッション
cd /Users/yuichi/AIPM/worktrees/optimization/aipm_v0
claude

# セッション名: perf-optimization-base
# 1時間作業...

# ② アプローチA を別セッションで試す
claude --resume perf-optimization-base --fork-session
# セッション名: perf-optimization-fork-a
# 実装完了...

# ③ アプローチB を別セッションで試す（元のセッションから）
claude --resume perf-optimization-base --fork-session
# セッション名: perf-optimization-fork-b
# 実装完了...

# ④ 3つのセッション全部にアクセス可能
claude --resume perf-optimization-base      # 元の実装
claude --resume perf-optimization-fork-a    # アプローチA
claude --resume perf-optimization-fork-b    # アプローチB

# ⑤ 最良のアプローチを選択して統合
# セッション比較 → fork-b が最適
# → fork-b の実装を本セッションにマージ
```

### シナリオ4: インタラクティブピッカーでのセッション管理

```bash
# ① セッション選択（最近のセッション一覧）
claude --resume

# インタラクティブピッカー表示
# ─────────────────────────────────
# auth-refactor
# api-update
# data-migration
# ─────────────────────────────────

# ② 検索で絞り込み
claude --resume api
# → api-update のみ表示

# ③ セッションプレビュー
# P キー押下 → セッション情報表示
# ├── 最後のメッセージ
# ├── ファイル変更履歴
# └── 作業ディレクトリ

# ④ セッション選択
# 矢印キーで移動 → Enter で選択
```

---

## 参考資料

### 公式ドキュメント

1. **Claude Code CLI Reference**
   - URL: https://code.claude.com/docs/en/cli-reference
   - セッション管理の詳細仕様
   - 全オプション一覧

2. **Claude Agent SDK Sessions**
   - URL: https://platform.claude.com/docs/en/agent-sdk/sessions
   - セッション再開の実装例
   - フォーク機能の詳細

3. **Claude Code Common Workflows**
   - URL: https://code.claude.com/docs/en/common-workflows
   - 実践的なセッション管理ガイド

### 関連実装ガイド

1. **Week 4: Git Worktrees並列実行ガイド**
   - ファイルパス: `@docs/implementation_guides/week4_worktrees.md`
   - セッション再開との組み合わせ
   - バックグラウンド実行パターン

2. **Parallel Execution Rules**
   - ファイルパス: `@.claude/rules/parallel_execution.md`
   - 並列エージェント実行ガイド

3. **Execution Preference**
   - ファイルパス: `@.claude/rules/execution_preference.md`
   - LLM優先実行アプローチ

### 外部リソース

- [Claude Code Session Management Workflows](https://stevekinney.com/courses/ai-development/claude-code-session-management)
- [Resume Claude Code Sessions After Restart](https://mehmetbaykar.com/posts/resume-claude-code-sessions-after-restart/)
- [Never Lose Your Work: Session Management](https://dev.to/rajeshroyal/never-lose-your-work-session-management-that-saves-your-sanity-4dp8)
- [Teaching Claude To Remember: Sessions And Resumable Workflow](https://medium.com/@porter.nicholas/teaching-claude-to-remember-part-3-sessions-and-resumable-workflow-1c356d9e442f)

---

## まとめ

### 主要ポイント

| 機能 | 用途 | コマンド |
|------|------|---------|
| **`--resume` 指定** | 特定セッションを再開 | `claude --resume <name>` |
| **`--resume` 選択** | インタラクティブ選択 | `claude --resume` |
| **`--continue`** | 最新セッション自動継続 | `claude --continue` / `claude -c` |
| **`--fork-session`** | セッション分岐 | `claude --resume <id> --fork-session` |
| **バックグラウンド** | 長時間実行 | `nohup claude --resume <id> & disown` |

### Week 4 実装計画との連携

```
Git Worktrees                Claude Code CLI
├── ワークツリー作成         ├── セッション開始
├── 各ブランチ独立           ├── --resume で再開
├── .claude/ 共有            ├── セッション名 = ブランチ名
└── 並列実行                 ├── --continue で続行
                             └── --fork-session で分岐
```

### 推奨実装（Week 4完全版）

1. **セッション命名規則を統一**
   - `claude --resume <branch-name>` で常に再開可能

2. **バックグラウンド実行の活用**
   - 長時間タスクは `nohup + disown` パターン

3. **セッション分岐の活用**
   - 複数実装検証時は `--fork-session` で安全探索

4. **ワークツリーとセッションの一対一対応**
   ```bash
   worktree: feature-auth
   session:  feature-auth
   resume:   claude --resume feature-auth
   ```

---

## 更新履歴

| 日付 | 作業 | 内容 |
|------|------|------|
| 2026-01-09 | 調査・作成 | Claude Code CLI v2.1.1 セッション管理仕様レポート作成 |
|  |  | `--resume`, `--continue`, `--fork-session` 仕様調査 |
|  |  | バックグラウンド実行パターン整理 |
|  |  | Week 4 実装計画との統合ガイド作成 |

---

## ファイル情報

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-09/week4_phase1_claude_cli_spec.md`

**作成日**: 2026-01-09 10:30-11:00 JST

**関連ファイル**:
- `@docs/implementation_guides/week4_worktrees.md` - Git Worktrees実装ガイド
- `@.claude/rules/parallel_execution.md` - 並列実行ルール
- `@.claude/rules/execution_preference.md` - 実行優先度ルール

---

## 次のステップ（Week 4 Phase 2）

1. **実装検証**: 上記パターンの実際の動作確認
2. **スクリプト統合**: セッション管理自動化スクリプト作成
3. **ドキュメント統合**: 本レポートを実装ガイドに統合
4. **チーム共有**: セッション命名規則の標準化

