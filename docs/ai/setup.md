# セットアップ手順

## 前提条件

- Node.js 18+ (オプション)
- Python 3.9+ (スクリプト用)
- Git

## クイックスタート

```bash
# リポジトリクローン
git clone https://github.com/miyatti777/aipm_v0.git
cd aipm_v0

# 初期設定スクリプト実行
./setup_workspace_simple.sh
```

## ディレクトリ初期化

プロジェクト開始時は以下のトリガーワードを使用：

```
「[プロジェクト名] 始めたい」
```

これにより以下が自動作成されます：
- `Stock/programs/[プログラム名]/projects/[プロジェクト名]/`
- 各フェーズ用documentsディレクトリ
- `Flow/YYYYMM/YYYY-MM-DD/` 日付フォルダ

## AIツール別設定

### Antigravity
`.agent/` 配下のルール・ワークフローが自動読み込み

### Cursor
`.cursor/rules/basic/` 配下の.mdcが自動適用

### Codex
`.codex/skills/` 配下のSKILL.mdを参照

### Claude Code
`CLAUDE.md` および `.claude/` を参照

## 環境変数

`.env` ファイルで以下を設定（オプション）：

```env
PROGRAM_ID=your_program_name
PROJECT_ID=your_project_name
```
