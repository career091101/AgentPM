# Ralph Wiggum Usage Guide

自律的ループ実行プラグインの使用ガイド（Week 8実装）。

## 概要

Ralph Wiggumは、Geoffrey Huntleyが提唱した**自律的反復開発技法**を実装したClaude Code公式プラグインです。

**核心的な仕組み**:
```bash
while :; do
  cat PROMPT.md | claude-code --continue
done
```

- 同じプロンプトを繰り返し投入
- Claude自身の前回作業をファイルとGit履歴で参照
- 完了条件を満たすまで自動反復

## セットアップ

### プラグイン有効化確認

1. `.claude/project-settings.json` を確認
```json
{
  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true
  }
}
```

2. プラグインが有効化されていない場合、Week 5のマージスクリプトを実行
```bash
bash scripts/setup_claude_settings.sh
```

### Git環境準備

1. 新規ブランチを作成
```bash
git checkout -b ralph-<task-name>
```

2. 現在の状態をコミット
```bash
git add .
git commit -m "chore: Snapshot before Ralph Wiggum execution"
```

3. コンテキスト使用率を確認
```bash
/context
# → 50%以下であることを確認
```

### .claudeignore設定

不要なファイルを除外してコンテキストを最適化：
```
node_modules/
.venv/
*.log
dist/
build/
```

### 初回テスト実行

本番実行前に10イテレーション以下でテスト：
```bash
/ralph-loop "Test task" --completion-promise "TEST DONE" --max-iterations 10
```

## 基本使用方法

### コマンド構文

```bash
/ralph-loop "タスク説明" --completion-promise "DONE" --max-iterations 20
```

### 実行例

#### 例1: ドキュメント生成
```bash
/ralph-loop "Generate comprehensive documentation for all skills in .claude/skills/. Output <promise>DOCS COMPLETE</promise> when all skills have README.md" --completion-promise "DOCS COMPLETE" --max-iterations 30
```

#### 例2: パス参照統一
```bash
/ralph-loop "Find all hardcoded /Users/yuichi/AIPM paths in .md and .py files, replace with pathlib or environment variables. Output <promise>PATHS FIXED</promise> when complete" --completion-promise "PATHS FIXED" --max-iterations 25
```

#### 例3: テストカバレッジ向上
```bash
/ralph-loop "Add pytest test cases for all Python scripts in scripts/. Output <promise>TESTS COMPLETE</promise> when coverage reaches 70%" --completion-promise "TESTS COMPLETE" --max-iterations 40
```

## 完了シグナル

### 完了を通知する方法

Claudeがタスク完了を通知するには、`<promise>`タグを出力：

```markdown
<promise>TASK COMPLETE</promise>
```

**重要**:
- このタグがないと、`--max-iterations`に到達するまで無限ループ
- プロンプトに明示的に指示すること

### 例

```bash
/ralph-loop "Refactor auth system. Output <promise>REFACTOR DONE</promise> when all tests pass" --completion-promise "REFACTOR DONE" --max-iterations 20
```

## 安全ルール

### 必須ルール

1. **MUST**: 必ず `--max-iterations` を設定（無限ループ防止）
2. **MUST**: Gitリポジトリ内で実行（失敗時のロールバック）
3. **MUST**: 新規ブランチで実行（`git checkout -b ralph-<task-name>`）
4. **MUST**: コスト監視（50イテレーション ≈ $50-100）

### 推奨ルール

1. **推奨**: 初回は10イテレーション以下でテスト
2. **推奨**: `/context` で定期的にコンテキスト使用率を確認
3. **推奨**: 大規模タスクは `haiku` モデルでコスト削減
4. **推奨**: 実行前に現在の状態をコミット

## 実行前チェックリスト

### 事前準備

```bash
# 1. 新規ブランチ作成
git checkout -b ralph-<task-name>

# 2. 現在の状態をコミット
git add .
git commit -m "chore: Snapshot before Ralph Wiggum execution"

# 3. コンテキスト確認
/context
# → 50%以下であることを確認

# 4. .claudeignore確認
cat .claudeignore
# → 不要なファイルが除外されているか確認
```

### チェックリスト

- [ ] Gitブランチを作成済み（`git checkout -b ralph-<task-name>`）
- [ ] 現在の状態をコミット済み
- [ ] `--max-iterations` を設定済み（デフォルト: 20）
- [ ] コスト予算を確認済み（イテレーション数 × $1-2）
- [ ] `.claudeignore` で不要なファイルを除外済み
- [ ] `/context` でコンテキスト使用率 < 50% を確認
- [ ] 完了条件を明確にプロンプトに記載

## 適用範囲

### ✅ 適しているタスク

| タスクタイプ | 説明 | イテレーション目安 |
|------------|------|----------------|
| **大規模リファクタリング** | 多数ファイルの一括変更 | 20-40 |
| **バッチ処理** | 100件のMarkdownファイル更新等 | 30-50 |
| **テストカバレッジ向上** | 全モジュールにテスト追加 | 30-50 |
| **ドキュメント生成** | 全スキルのREADME作成 | 20-30 |
| **フレームワークマイグレーション** | React 17 → 18等 | 40-60 |
| **コード規約統一** | ESLintルール適用 | 15-25 |
| **翻訳** | 全ドキュメントの日英翻訳 | 20-40 |

### ❌ 適していないタスク

| タスクタイプ | 理由 |
|------------|------|
| **人間の判断が必要なタスク** | 戦略立案、設計判断等 |
| **外部API連携** | レート制限でループが無意味 |
| **短時間で完了** | 1-2回で終わるもの |
| **本番環境デバッグ** | ターゲットを絞ったデバッグが適切 |
| **不明確な完了基準** | ループが収束しない |

## コスト管理

### コスト見積もり

| イテレーション数 | コスト目安（Sonnet） | コスト目安（Haiku） | 時間目安 |
|---------------|------------------|------------------|---------|
| 10 | $10-20 | $2-5 | 30-60分 |
| 20 | $20-40 | $5-10 | 1-2時間 |
| 50 | $50-100 | $10-25 | 2-5時間 |
| 100 | $100-200 | $20-50 | 5-10時間 |

### モデル選択戦略

| タスクタイプ | 推奨モデル | 理由 |
|------------|----------|------|
| ドキュメント生成 | **haiku** | 機械的タスク、コスト削減 |
| コードリファクタリング | **sonnet** | バランス重視 |
| アーキテクチャ変更 | **opus** | 複雑な判断が必要 |

**設定方法**:
```bash
# 個人設定ファイルで変更
vim ~/.claude/settings.json

# 例: haikuモデルに変更
{
  "model": "haiku"
}
```

## 実行中の監視

### リアルタイム監視

```bash
# 別ターミナルで監視
watch -n 30 'git log --oneline -n 10'  # 30秒ごとにコミット履歴確認

# コンテキスト使用率チェック
bash scripts/check_context_usage.sh -w  # 定期リマインダー

# プロセス確認
ps aux | grep claude
```

### 中断方法

```bash
# ループ中断（推奨）
/cancel-ralph

# または強制終了
Ctrl+C
```

## 失敗時の復旧

### 変更を破棄

```bash
# 最新N回のイテレーションを破棄
git reset --hard HEAD~<イテレーション数>

# 例: 最新5イテレーションを破棄
git reset --hard HEAD~5

# ブランチを削除して再開
git checkout main
git branch -D ralph-<task-name>
git checkout -b ralph-<task-name>-v2
```

### 部分的にコミットを残す

```bash
# 特定のイテレーションまで戻る
git log --oneline  # コミットハッシュ確認
git reset --hard <commit-hash>
```

## aipm_v0プロジェクト向け定常タスク

### シナリオA: スキルドキュメント生成

```bash
/ralph-loop "For each skill in .claude/skills/, ensure it has:
1. A comprehensive SKILL.md with description, usage, and examples
2. A corresponding command in .claude/commands/
3. Consistent YAML frontmatter across all skills

Output <promise>SKILL DOCS COMPLETE</promise> when all 26 skills have these components." --completion-promise "SKILL DOCS COMPLETE" --max-iterations 30
```

**期待効果**: 26スキル × 3コンポーネント = 78ファイルの一括管理

---

### シナリオB: パス参照の統一

```bash
/ralph-loop "Find all hardcoded paths in .md and .py files, replace with:
- Environment variables (AIPM_ROOT)
- pathlib.Path relative paths
- Symbolic paths (@-prefix)

Output <promise>PATHS STANDARDIZED</promise> when no hardcoded /Users/yuichi/AIPM paths remain." --completion-promise "PATHS STANDARDIZED" --max-iterations 25
```

**期待効果**: パス管理の一元化（@.claude/rules/path_conventions.md 準拠）

---

### シナリオC: テストカバレッジ向上

```bash
/ralph-loop "Add pytest test cases for all Python scripts in scripts/:
- Unit tests for each function
- Integration tests for main flows
- Mocking for external dependencies

Output <promise>TEST COVERAGE 70%</promise> when coverage reaches 70%." --completion-promise "TEST COVERAGE 70%" --max-iterations 40
```

**期待効果**: テストカバレッジ 0% → 70%

---

### シナリオD: ドキュメント翻訳（日英）

```bash
/ralph-loop "Translate all Japanese-language documentation in docs/ to English:
- Keep original Japanese files with _ja suffix
- Create English versions without suffix
- Preserve markdown structure and links

Output <promise>TRANSLATION COMPLETE</promise> when all .md files have English versions." --completion-promise "TRANSLATION COMPLETE" --max-iterations 20
```

**期待効果**: グローバル対応

## 並列実行との統合

### Week 3-4の並列実行と組み合わせ

```bash
# tmuxで3ペインに分割
bash scripts/start_parallel_claude.sh

# ペイン1: スキルドキュメント生成
/ralph-loop "Generate skill documentation" --completion-promise "SKILL DOCS COMPLETE" --max-iterations 30

# ペイン2: パス参照統一
/ralph-loop "Standardize path references" --completion-promise "PATHS STANDARDIZED" --max-iterations 25

# ペイン3: テストカバレッジ向上
/ralph-loop "Add test coverage" --completion-promise "TEST COVERAGE 70%" --max-iterations 40
```

**総実行時間**: 3-6時間（並列実行）
**総コスト**: $95-190（30+25+40 = 95イテレーション × $1-2）

## トラブルシューティング

### 問題1: 無限ループに陥る

**症状**: `--max-iterations`に到達してもタスクが完了しない

**原因**: 完了条件が不明確 or `<promise>`タグ出力なし

**解決策**:
1. `/cancel-ralph` でループ中断
2. プロンプトを修正して完了条件を明確化
3. `--max-iterations`を低く設定して再実行（例: 10）

---

### 問題2: コンテキストが肥大化

**症状**: 「Context low」警告が頻発

**原因**: `.claudeignore`が不十分 or 大量のファイル読み込み

**解決策**:
1. `/cancel-ralph` でループ中断
2. `.claudeignore` に不要なファイル/ディレクトリを追加
3. `/clear` で新規セッション開始
4. 再実行

---

### 問題3: 意図しない変更が発生

**症状**: Ralphが不要なファイルを変更

**原因**: プロンプトが曖昧 or スコープが広すぎる

**解決策**:
1. `/cancel-ralph` でループ中断
2. `git reset --hard HEAD~<イテレーション数>` で変更破棄
3. プロンプトを具体化してスコープを限定
4. 新規ブランチで再実行

---

### 問題4: コストが予想以上に高い

**症状**: 50イテレーションで$150以上の請求

**原因**: コンテキストサイズが大きい or Opusモデル使用

**解決策**:
1. `.claudeignore` で不要ファイルを除外
2. モデルを `haiku` に変更（~/.claude/settings.json）
3. `--max-iterations` を低く設定

---

### 問題5: プロンプト品質低下

**症状**: イテレーションが進むにつれて出力品質が低下

**原因**:
- コンテキストに古い出力が蓄積
- プロンプトの曖昧さが増幅される

**解決策**:
1. プロンプトを明確化（具体的な完了条件）
2. `/compact` でコンテキスト圧縮
3. イテレーション数を減らす（40 → 20）
4. 完了条件を厳格化

---

### 問題6: モデル選択間違いによるコスト爆発

**症状**: 予想の3-5倍のコスト請求

**原因**: Opusモデルが誤って選択されている

**解決策**:
1. `~/.claude/settings.json` でモデル確認
```json
{
  "model": "haiku"  // または "sonnet"
}
```
2. プロジェクト設定でモデルを固定
3. 実行前にモデル選択を明示的に確認

## リスク管理

### リスク1: 無限ループ

**影響**: 高額な請求 + タスク未完了

**軽減策**:
- 必ず `--max-iterations` 設定
- 初回は10イテレーション以下でテスト
- `/context` で定期監視

---

### リスク2: コスト超過

**影響**: 予算オーバー

**軽減策**:
- イテレーション数 × $1-2 で事前見積もり
- 50イテレーション以上は事前承認制
- haikuモデル使用でコスト削減

---

### リスク3: 意図しない変更

**影響**: コードベース破壊 + 復旧時間

**軽減策**:
- 新規ブランチで実行
- 各イテレーション後に `git diff` で確認
- PRレビュー必須

---

### リスク4: コンテキスト肥大化

**影響**: 動作速度低下 + コスト増加

**軽減策**:
- `.claudeignore` で大容量ファイル除外
- `/compact` を定期実行
- 50%到達時は `/clear` で新規セッション

## 参照

### 調査元ソース
- [Ralph Wiggum: Autonomous Loops for Claude Code - Paddo.dev](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)
- [claude-plugins-official/ralph-wiggum - GitHub](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum)
- [The Ralph Wiggum Technique - Cyrus](https://www.atcyrus.com/stories/ralph-wiggum-technique-claude-code-autonomous-loops)
- [Ralph Wiggum - Awesome Claude](https://awesomeclaude.ai/ralph-wiggum)

### 関連ドキュメント
- @.claude/rules/settings_management.md - Week 5設定管理
- @.claude/rules/context_management.md - コンテキスト管理
- @.claude/rules/parallel_execution.md - 並列実行ガイドライン
- @.claude/rules/execution_preference.md - LLM優先アプローチ

### 関連スクリプト
- `scripts/check_context_usage.sh` - コンテキスト監視
- `scripts/start_parallel_claude.sh` - 並列実行

## 更新履歴

- **2026-01-04**: Week 8実装完了（Ralph Wiggum導入）
  - プラグイン有効化
  - プロジェクト設定更新
  - 包括的使用ガイド作成
  - 定常タスクシナリオ定義
