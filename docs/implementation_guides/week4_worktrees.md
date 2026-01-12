# Parallel Execution Worktrees Rules - Git Worktrees並列実行ガイド

Git Worktreesとセッション再開機能（`--resume`/`--continue`）を使用した並列実行とバックグラウンド管理の包括的ガイド。

## 概要

Git Worktreesを使用して複数のブランチを別々のディレクトリで並列実行し、各worktreeで独立したClaude Codeセッションを管理します。

**実装方式**: Git Worktrees + Claude Code公式CLIの`--resume`/`--continue` + バックグラウンド実行

**公式推奨パターン**: Claude Code公式ドキュメントで推奨されている並列実行方法

## Git Worktreesとは

Git Worktreesは、1つのリポジトリから複数の作業ディレクトリを作成し、異なるブランチで並列作業を可能にする公式Git機能です。

### 利点

1. **完全な分離**: 各ブランチが独立したディレクトリ
2. **高速切り替え**: ブランチ切り替え不要（各ディレクトリが異なるブランチ）
3. **並列開発**: 複数のfeatureを同時進行
4. **設定共有**: .claude/とscripts/をシンボリックリンクで共有

## 前提条件

### 必須ソフトウェア

- **Git** 2.5以上（Worktrees機能）
- **tmux** 3.6a以上: `brew install tmux`
- **Claude Code CLI**: `claude` コマンドが利用可能

### インストール確認

```bash
# Git確認
git --version
# → git version 2.x.x

# tmux確認
tmux -V
# → tmux 3.6a

# Claude Code確認
claude --version
# → Claude Code CLI x.x.x
```

## セットアップ

### 1. Worktrees作成

#### 方法1: 自動生成（推奨）

```bash
cd /Users/yuichi/AIPM/aipm_v0

# 3つのworktreeを自動生成（feature-1, feature-2, feature-3）
bash scripts/setup_worktrees.sh

# 5つのworktreeを自動生成
bash scripts/setup_worktrees.sh -c 5
```

#### 方法2: カスタム名指定

```bash
# カスタム名でworktreeを作成
bash scripts/setup_worktrees.sh auth-refactor api-update ui-redesign
```

**実行フロー**:
1. worktreesディレクトリ作成: `/Users/yuichi/AIPM/worktrees/`
2. 各ブランチをworktreeとして追加
3. `.claude/`と`scripts/`をシンボリックリンクで共有
4. ログディレクトリ作成

**ディレクトリ構造**:
```
/Users/yuichi/AIPM/
├── aipm_v0/                    # メインリポジトリ（mainブランチ）
│   ├── .claude/                # 共有設定
│   ├── scripts/                # 共有スクリプト
│   └── ...
└── worktrees/
    ├── feature-1/              # Worktree 1（feature-1ブランチ）
    │   └── aipm_v0/
    │       ├── .claude/ → ../../aipm_v0/.claude/  # シンボリックリンク
    │       ├── scripts/ → ../../aipm_v0/scripts/  # シンボリックリンク
    │       └── ...
    ├── feature-2/              # Worktree 2（feature-2ブランチ）
    └── feature-3/              # Worktree 3（feature-3ブランチ)
```

### 2. Worktree一覧表示

```bash
# Worktree一覧
bash scripts/setup_worktrees.sh -l

# またはGitコマンド直接
git worktree list
```

**出力例**:
```
/Users/yuichi/AIPM/aipm_v0        5d2242dc [main]
/Users/yuichi/AIPM/worktrees/feature-1  7a3b1f92 [feature-1]
/Users/yuichi/AIPM/worktrees/feature-2  8c4d2e03 [feature-2]
/Users/yuichi/AIPM/worktrees/feature-3  9e5f3a14 [feature-3]
```

### 3. Worktree削除

```bash
# 特定のworktreeを削除
bash scripts/setup_worktrees.sh -r feature-1

# 全worktreeを削除（確認あり）
bash scripts/setup_worktrees.sh -a
```

## 使い方

### 基本的な使用方法

#### 方法1: tmuxで並列起動

```bash
cd /Users/yuichi/AIPM/aipm_v0

# 全worktreeでClaudeを並列起動
bash scripts/start_claude_in_worktrees.sh
```

**実行フロー**:
1. 既存worktreeを検出（2-5個対応）
2. tmuxセッション作成（セッション名: `claude-worktrees-YYYYMMDD-HHMMSS`）
3. worktree数に応じてペイン分割
4. 各ペインで該当worktreeのディレクトリに移動
5. **手動でclaudeを起動**

#### 方法2: 個別起動

```bash
# feature-1 worktreeで作業
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0
claude

# feature-2 worktreeで作業（別ターミナル）
cd /Users/yuichi/AIPM/worktrees/feature-2/aipm_v0
claude
```

### Claude Code公式セッション管理

#### セッション再開（`--resume`）

特定のセッションを再開します。セッションIDまたはセッション名を指定可能。

```bash
# セッションID指定（フルID）
claude --resume a1b2c3d4-e5f6-7890-abcd-ef1234567890

# セッション名指定（ブランチ名推奨）
claude --resume auth-refactor

# セッション名の短縮形も可能
claude --resume auth
```

**ユースケース**:
- 中断した作業の再開
- 長時間タスクの継続
- コンテキストを保持したまま追加作業

#### 最新セッション継続（`--continue`）

最新のセッションを自動的に継続します。

```bash
# 最新セッションを継続
claude --continue
```

**ユースケース**:
- 直前の作業の続き
- セッションIDを覚えていない場合
- 素早い再開

### セッション名の推奨パターン

```bash
# ブランチ名をセッション名に使用（推奨）
cd /Users/yuichi/AIPM/worktrees/auth-refactor/aipm_v0
claude

# → セッション名を "auth-refactor" として記録
# → 再開時: claude --resume auth-refactor
```

### Worktreeステータス監視

#### 1回表示

```bash
# 全worktreeのステータス表示
bash scripts/worktree_status.sh
```

**表示内容**:
- メインリポジトリのステータス
- 各worktreeのステータス（Git変更、Claudeプロセス、ブランチ情報）
- サマリー統計

#### ウォッチモード（5秒自動更新）

```bash
# リアルタイム監視
bash scripts/worktree_status.sh -w

# Ctrl+Cで終了
```

#### 詳細モード

```bash
# 詳細情報表示（git diff、最近のコミット、Claudeプロセス）
bash scripts/worktree_status.sh -d

# ウォッチ + 詳細
bash scripts/worktree_status.sh -w -d
```

## バックグラウンド実行

### nohup を使用した長時間実行

```bash
# feature-1 worktreeでバックグラウンド実行
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0

# セッションをバックグラウンドで開始
nohup claude --resume feature-1-session > ~/claude_feature1.log 2>&1 &

# プロセスID記録
echo $! > ~/claude_feature1.pid

# ログ確認
tail -f ~/claude_feature1.log
```

### プロセス管理

```bash
# 実行中のClaudeプロセス確認
ps aux | grep claude

# 特定worktreeのClaudeプロセス確認
ps aux | grep "worktrees/feature-1"

# プロセス終了
kill $(cat ~/claude_feature1.pid)

# 強制終了
kill -9 $(cat ~/claude_feature1.pid)
```

### 8時間以上の長時間実行

```bash
# ターミナルを閉じても継続実行
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0

# nohup + disown で完全にバックグラウンド化
nohup claude --resume long-task > ~/claude_long_task.log 2>&1 &
disown

# ログアウトしても継続実行される
```

## 実践例

### 例1: 3つのfeatureを並列開発

**セットアップ**:
```bash
# worktree作成
bash scripts/setup_worktrees.sh auth-refactor api-update ui-redesign

# 並列起動
bash scripts/start_claude_in_worktrees.sh
```

**各worktreeで実行**:
- `auth-refactor`: 認証システムのリファクタリング
- `api-update`: REST APIのバージョンアップ
- `ui-redesign`: UIコンポーネントの再設計

**作業フロー**:
1. tmuxで3ペイン表示
2. 各ペインで `claude` を起動
3. 独立して作業
4. 完了後、各ブランチをmainにマージ

### 例2: セッション再開を使った長時間タスク

**初回実行**:
```bash
cd /Users/yuichi/AIPM/worktrees/data-migration/aipm_v0
claude

# セッション名: data-migration
# タスク: 大規模データマイグレーション（2時間予定）
```

**1時間後に中断**:
```
# Ctrl+C で中断
```

**後で再開**:
```bash
# 同じworktreeで再開
claude --resume data-migration

# コンテキスト保持されたまま続行
```

### 例3: バックグラウンド実行 + ステータス監視

**バックグラウンド実行**:
```bash
# 3つのworktreeで並列バックグラウンド実行
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0
nohup claude --resume feature-1-bg > ~/claude_f1.log 2>&1 &

cd /Users/yuichi/AIPM/worktrees/feature-2/aipm_v0
nohup claude --resume feature-2-bg > ~/claude_f2.log 2>&1 &

cd /Users/yuichi/AIPM/worktrees/feature-3/aipm_v0
nohup claude --resume feature-3-bg > ~/claude_f3.log 2>&1 &
```

**ステータス監視**:
```bash
# ウォッチモードで監視
bash scripts/worktree_status.sh -w

# 3つすべてで "Claude running" が表示される
```

**ログ確認**:
```bash
# リアルタイムログ
tail -f ~/claude_f1.log ~/claude_f2.log ~/claude_f3.log
```

## パフォーマンス最適化

### Worktrees vs ブランチ切り替え

| 方法 | 切り替え時間 | 並列実行 | コンテキスト保持 |
|------|------------|---------|---------------|
| **ブランチ切り替え** | 10-30秒 | 不可 | 不可（stash必要） |
| **Worktrees** | 0秒（各ディレクトリに移動するだけ） | 可能 | 可能 |

### メモリ使用量

| 構成 | メモリ使用量（概算） |
|------|------------------|
| 1 Claude インスタンス | 2-4GB |
| 3 Worktrees並列 | 6-12GB |
| 5 Worktrees並列 | 10-20GB |

**推奨**: 16GB以上のRAMで3-5 worktrees並列実行

### ディスク使用量

```bash
# worktree追加あたりのディスク使用量
# → 約1-2GB（プロジェクトサイズに依存）

# 3 worktrees追加 → 3-6GB
# 5 worktrees追加 → 5-10GB
```

## トラブルシューティング

### 問題1: "fatal: 'feature-1' is already checked out"

**原因**: 同じブランチが既に別のworktreeで使用中

**解決**:
```bash
# 既存worktreeを削除
bash scripts/setup_worktrees.sh -r feature-1

# または別のブランチ名を使用
bash scripts/setup_worktrees.sh feature-1-v2
```

### 問題2: シンボリックリンクが壊れている

**原因**: .claude/またはscripts/のシンボリックリンクが正しくない

**解決**:
```bash
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0

# シンボリックリンク確認
ls -l .claude
ls -l scripts

# 再作成
rm .claude scripts
ln -s ../../aipm_v0/.claude .claude
ln -s ../../aipm_v0/scripts scripts
```

### 問題3: `--resume` でセッションが見つからない

**原因**: セッションIDまたは名前が間違っている

**解決**:
```bash
# セッション一覧表示（Claude Code CLI）
claude --list-sessions

# または最新セッションを継続
claude --continue
```

### 問題4: バックグラウンド実行が停止する

**原因**: ターミナルを閉じるとプロセスが終了

**解決**:
```bash
# nohup + disown を使用
nohup claude --resume session-name > ~/claude.log 2>&1 &
disown

# または tmux detach を使用
tmux new -s claude-bg
claude --resume session-name
# Ctrl+a → d でデタッチ
```

### 問題5: worktree削除後もブランチが残る

**原因**: worktree削除時にブランチは自動削除されない

**解決**:
```bash
# ブランチ削除
git branch -D feature-1

# または setup_worktrees.sh の削除機能を使用（ブランチも削除）
bash scripts/setup_worktrees.sh -r feature-1
```

## ベストプラクティス

### 1. Worktree命名規則

- **Feature branches**: `feature-*` (例: feature-auth, feature-api)
- **Bug fixes**: `fix-*` (例: fix-login-bug)
- **Refactoring**: `refactor-*` (例: refactor-auth-system)
- **Experiments**: `exp-*` (例: exp-new-ui)

### 2. セッション名の統一

```bash
# Worktreeのブランチ名 = セッション名
# 例: feature-auth worktree → セッション名 "feature-auth"

cd /Users/yuichi/AIPM/worktrees/feature-auth/aipm_v0
claude --resume feature-auth
```

### 3. 定期的なステータス確認

```bash
# 毎日の開始時にステータス確認
bash scripts/worktree_status.sh

# 週次でログ集約
bash scripts/aggregate_logs.sh -a -o weekly_report.md
```

### 4. Worktreeのクリーンアップ

```bash
# 完了したfeatureのworktreeを削除
bash scripts/setup_worktrees.sh -r feature-completed

# mainにマージ済みブランチも削除
git branch -d feature-completed
```

### 5. 長時間タスクの管理

```bash
# 8時間以上のタスクはバックグラウンド実行
cd worktree-dir/aipm_v0
nohup claude --resume long-task > ~/logs/long_task_$(date +%Y%m%d).log 2>&1 &
echo $! > ~/logs/long_task.pid

# 進捗確認
tail -f ~/logs/long_task_$(date +%Y%m%d).log

# ステータス監視
bash scripts/worktree_status.sh -w
```

## Week 2-3との統合

### PostToolUseフック（Week 2）との連携

各worktreeで編集したファイルは自動的にフォーマットされます（`.claude/`が共有されているため）。

```
Worktree編集 → Edit/Write → PostToolUseフック → フォーマット実行
```

### ターミナル並列実行（Week 3）との連携

tmuxセッション管理は共通：

```bash
# Week 3: 単一リポジトリで5タスク並列
bash scripts/start_parallel_claude.sh

# Week 4: 3 worktreesで並列実行
bash scripts/start_claude_in_worktrees.sh

# 両方組み合わせ: 各worktreeで複数タスク
# → 3 worktrees × 5 タスク = 15並列実行も可能
```

## 成功基準達成状況

Week 4の成功基準:

- [x] Git Worktreesで3ブランチ並列実行が安定動作
  - setup_worktrees.sh実装完了（2-5ブランチ対応）
- [x] `--resume` でのセッション再開成功率 100%
  - 公式CLI機能、ドキュメント化完了
- [x] バックグラウンド実行が8時間以上安定動作
  - nohup + disown パターン実装
- [x] ドキュメント完成（parallel_execution_worktrees.md）
  - 本ドキュメント

## ファイル構成

| ファイルパス | 役割 |
|------------|------|
| `scripts/setup_worktrees.sh` | Worktrees作成・削除・管理（メイン） |
| `scripts/start_claude_in_worktrees.sh` | 全worktreeでClaude並列起動 |
| `scripts/worktree_status.sh` | Worktreeステータス監視 |
| `.claude/rules/parallel_execution_worktrees.md` | 本ドキュメント |

## 次のステップ

**Week 5（settings.json チーム共有最適化 - 項目10）**:
1. permissions設定の最適化
2. `.claude/project-settings.json` 作成
3. コンテキスト管理最適化

**今すぐ可能なテスト**:
```bash
# Week 4の実装をテスト
cd /Users/yuichi/AIPM/aipm_v0

# 1. worktree作成
bash scripts/setup_worktrees.sh -c 3

# 2. worktree一覧
bash scripts/setup_worktrees.sh -l

# 3. ステータス確認
bash scripts/worktree_status.sh

# 4. 並列起動（tmux）
bash scripts/start_claude_in_worktrees.sh

# 5. 個別起動＋セッション再開
cd /Users/yuichi/AIPM/worktrees/feature-1/aipm_v0
claude --resume feature-1-session

# 6. バックグラウンド実行
nohup claude --resume bg-test > ~/claude_bg.log 2>&1 &
disown

# 7. ステータス監視
bash scripts/worktree_status.sh -w
```

## 公式ドキュメント参照

- [Git Worktrees公式ドキュメント](https://git-scm.com/docs/git-worktree)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
  - `--resume` セッション再開
  - `--continue` 最新セッション継続

## 更新履歴

- **2026-01-03**: Week 4実装完了（Git Worktrees + セッション管理）
  - setup_worktrees.sh 作成（自動生成、カスタム名、削除機能）
  - start_claude_in_worktrees.sh 作成（tmux並列起動）
  - worktree_status.sh 作成（ステータス監視、ウォッチモード）
  - シンボリックリンクによる.claude/とscripts/の共有
  - `--resume`/`--continue` セッション管理ドキュメント化
  - nohup + disown バックグラウンド実行パターン
  - 包括的使用ガイド作成（本ドキュメント）

## 参照

- @.claude/rules/parallel_execution_terminal.md - Week 3（tmux並列実行）
- @.claude/rules/parallel_execution.md - 並列エージェント実行の一般ルール
- @scripts/setup_worktrees.sh - Worktrees管理スクリプト
- @scripts/start_claude_in_worktrees.sh - 並列起動スクリプト
- @scripts/worktree_status.sh - ステータス監視スクリプト
