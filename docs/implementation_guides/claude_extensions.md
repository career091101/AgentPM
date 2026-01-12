# Claude Code 拡張ツール導入ガイド

Issue #5 対応として導入した Claude Code 拡張ツールのガイド。

## 導入済みツール一覧

| ツール | 状態 | バージョン | 用途 |
|--------|------|-----------|------|
| **Claude-Mem** | ✅ 稼働中 | 最新 | 無限メモリ（セッション間コンテキスト保持） |
| **Ralph Wiggum** | ✅ 有効 | 公式 | 自律的ループ実行 |
| **feature-dev** | ✅ 有効 | 公式 | 7フェーズ構造化開発ワークフロー |
| **Auto-Claude** | ✅ インストール済 | v2.7.2 | 12並列自律実行 |

---

## 1. Claude-Mem（無限メモリ）

### 概要

セッション間でメモリを永続化し、コンテキスト制限を突破するプラグイン。

### 主な効果

- **トークン95%削減**: ツール出力を約500トークンに圧縮
- **20倍のツールコール**: 通常約50回 → 1000回以上
- **セッション継続**: 翌日再開時も前回のコンテキストを自動注入

### 設定ファイル

```
~/.claude-mem/settings.json
```

### 主要設定

| 設定 | 値 | 説明 |
|------|-----|------|
| `CLAUDE_MEM_MODEL` | claude-sonnet-4-5 | 圧縮に使用するモデル |
| `CLAUDE_MEM_CONTEXT_OBSERVATIONS` | 50 | 注入するコンテキスト数 |
| `CLAUDE_MEM_WORKER_PORT` | 37777 | ワーカーサービスポート |

### Web UI

```
http://localhost:37777
```

メモリ内容のリアルタイム監視が可能。

### 機密情報の除外

```markdown
<private>
この内容はメモリに保存されません
</private>
```

### 参照

- [GitHub - thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- [Claude-Mem ドキュメント](https://docs.claude-mem.ai/)

---

## 2. Ralph Wiggum（自律的ループ実行）

### 概要

同じプロンプトを繰り返し投入し、完了条件を満たすまで自動反復する公式プラグイン。

### 使用方法

```bash
/ralph-loop "タスク説明" --completion-promise "DONE" --max-iterations 20
```

### 完了シグナル

```markdown
<promise>TASK COMPLETE</promise>
```

### 詳細ガイド

→ @docs/implementation_guides/week8_ralph_wiggum.md

---

## 3. feature-dev（構造化開発ワークフロー）

### 概要

7フェーズの構造化ワークフローで機能開発を支援する公式プラグイン。
Issue #5 で言及された「Planning-with-Files」の代替として導入。

### 7フェーズ

1. **Discovery** - 要件理解
2. **Codebase Exploration** - 既存コード調査（並列エージェント）
3. **Clarifying Questions** - 曖昧さ解消
4. **Architecture Design** - 3つの実装アプローチ設計
5. **Implementation** - 実装
6. **Quality Review** - コードレビュー
7. **Summary** - ドキュメント化

### 使用方法

```bash
/feature-dev Add user authentication with OAuth
```

### 専門エージェント

| エージェント | 役割 |
|------------|------|
| **code-explorer** | 既存コードの実行パス分析 |
| **code-architect** | アーキテクチャ設計 |
| **code-reviewer** | バグ・品質レビュー |

### 参照

- [claude-plugins-official/feature-dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/feature-dev)

---

## 4. Auto-Claude（12並列自律実行）

### 概要

最大12のClaude Codeセッションを同時制御するスタンドアロンアプリケーション。

### インストール場所

```
/Applications/Auto-Claude.app
```

### 主な機能

| 機能 | 説明 |
|------|------|
| **Parallel Agent Execution** | 最大12ターミナル同時実行 |
| **Isolated Git Workspaces** | Git Worktreeで完全隔離 |
| **Self-Validating QA Loop** | 自動ビルド検証 |
| **Headless Mode** | CI/CD統合用CLIモード |

### 4エージェント構成

```
Planner → Coder → QA Reviewer → QA Fixer
```

### 適したユースケース

- 4-6個の新機能を並列開発
- 10-12個のバグを同時修正
- 依存関係の一括アップデート
- 大規模リファクタリング

### 参照

- [GitHub - AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)
- [Auto-Claude 紹介記事](https://www.vibesparking.com/en/blog/ai/andymik90/auto-claude/)

---

## ツール組み合わせパターン

### パターン1: 長時間単一タスク

```
Claude-Mem + Ralph Wiggum
```

- Claude-Memでコンテキスト保持
- Ralph Wiggumで自動反復

### パターン2: 複雑な機能開発

```
Claude-Mem + feature-dev
```

- Claude-Memでセッション間継続
- feature-devで構造化ワークフロー

### パターン3: 大規模並列開発

```
Auto-Claude + Claude-Mem
```

- Auto-Claudeで12並列実行
- Claude-Memで各セッションのコンテキスト保持

---

## 設定ファイル

### グローバル設定

```
~/.claude/settings.json
```

```json
{
  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true,
    "claude-mem": true,
    "feature-dev@claude-plugins-official": true
  }
}
```

### プロジェクト設定

```
.claude/project-settings.json
```

---

## トラブルシューティング

### Claude-Memワーカーが起動しない

```bash
# ステータス確認
curl http://localhost:37777/health

# 手動起動
cd ~/.claude/plugins/claude-mem && bun run start
```

### プラグインが認識されない

```bash
# Claude Code再起動
claude --restart

# プラグイン再インストール
/plugin uninstall claude-mem
/plugin install claude-mem
```

---

## 更新履歴

- **2026-01-07**: Issue #5 対応として全ツール導入完了
  - Claude-Mem: 既存インストール確認・稼働中
  - feature-dev: 設定追加（Planning-with-Files代替）
  - Auto-Claude: v2.7.2 インストール確認

## 参照

- Issue #5: Claude-Memなどを導入して
- @docs/implementation_guides/week8_ralph_wiggum.md
- @.claude/rules/context_management.md
- @.claude/rules/parallel_execution.md
