# Ralph Wiggum Integration Rules

Ralph Wiggum（自律的ループ実行プラグイン）の統合ルール。

## 概要

Ralph WiggumはClaude Code公式プラグインで、`while`ループによる自律的な反復実行を可能にします。

**コア機構**:
```bash
while :; do
  cat PROMPT.md | claude-code --continue
done
```

**Week 5統合**: Settings Management（`week5_settings.md`）で設定管理が統一され、プラグイン有効化が`.claude/project-settings.json`で一元管理されています。

**プラグイン有効化の歴史**:
- **2026-01-09**: Week 5 Settings Management実装時に統合
- **設定ファイル**: `.claude/project-settings.json` 行80-83
- **有効化スクリプト**: `scripts/setup_claude_settings.sh`（Week 5で作成）

## 前提条件

### プラグイン確認

Ralph Wiggumプラグインが有効化されていることを確認：

```bash
# プラグイン設定確認
cat .claude/project-settings.json | grep -A 5 "enabledPlugins"

# 期待される出力:
# {
#   "enabledPlugins": {
#     "ralph-wiggum@claude-plugins-official": true
#   }
# }
```

プラグインが無効の場合、Week 5のマージスクリプトを実行：

```bash
bash scripts/setup_claude_settings.sh
```

### Git要件

**必須**: Ralph Wiggum実行前に必ずGitリポジトリで作業してください。

理由:
1. 各イテレーションで自動コミットが作成される
2. 失敗時に`git reset`で復旧可能
3. 変更履歴の追跡が容易

### コスト予算

Ralph Wiggumは反復実行のため、コストが累積します。

| タスクタイプ | 推奨max-iterations | 推定コスト（Haiku） | 推定コスト（Sonnet） |
|------------|------------------|------------------|-------------------|
| 軽量タスク | 10-20 | $0.5-2.0 | $10-40 |
| 中規模タスク | 20-40 | $2.0-8.0 | $40-160 |
| 大規模タスク | 40-80 | $8.0-32.0 | $160-640 |

**重要**: 初回実行時は必ず`--max-iterations 10`で開始してください。

## セットアップ手順

### ステップ1: プラグイン有効化確認

```bash
# 1. プラグイン設定確認
cat .claude/project-settings.json | jq '.enabledPlugins'

# 2. プラグインが無効の場合
bash scripts/setup_claude_settings.sh

# 3. 再確認
cat .claude/project-settings.json | jq '.enabledPlugins'
# → "ralph-wiggum@claude-plugins-official": true であることを確認
```

### ステップ2: Git環境準備

```bash
# 1. 現在の状態を確認
git status

# 2. 新規ブランチを作成
git checkout -b ralph-<task-name>
# 例: ralph-skill-documentation

# 3. 現在の状態をコミット
git add .
git commit -m "chore: Snapshot before Ralph Wiggum execution"

# 4. ブランチ確認
git branch
# → * ralph-<task-name> が表示されること
```

### ステップ3: コンテキスト管理設定

**重要**: Ralph Wiggumは反復実行のため、コンテキストが急速に肥大化します。

`.claudeignore` に以下を追加：

```
# 依存関係
node_modules/
.venv/
venv/
env/
vendor/

# ビルド成果物
dist/
build/
out/
target/
*.min.js
*.min.css

# ログ・キャッシュ
*.log
*.cache
__pycache__/
.pytest_cache/
.mypy_cache/

# 大容量データ
data/
datasets/
*.csv
*.db
*.sqlite

# Ralph実行時の一時ファイル（必要に応じて）
Flow/
.DS_Store
```

コンテキスト使用率を確認：

```bash
/context
# → 50%以下であることを確認
```

### ステップ4: プロンプトファイル作成

Ralph Wiggumは`PROMPT.md`ファイルから指示を読み込みます。

```bash
# プロンプトファイル作成
cat > PROMPT.md << 'EOF'
# Task: スキルドキュメント作成

以下の83個のスキルについて、`README.md`を作成してください。

**完了条件**:
1. 全83スキルの`README.md`が作成されている
2. 各READMEが最低200行以上
3. フォーマットが統一されている

**完了時の出力**:
<promise>TASK COMPLETE: 83 skills documented</promise>

**参照**:
- `.claude/skills/` - スキルディレクトリ
- `@.claude/skills/_shared/skill_template.md` - テンプレート
EOF

# ファイル確認
cat PROMPT.md
```

### ステップ5: 初回テスト実行（必須）

**重要**: 本番実行前に必ず10イテレーション以下でテストしてください。

```bash
/ralph-loop "Test task execution with PROMPT.md" \
  --completion-promise "TEST DONE" \
  --max-iterations 10
```

テスト成功後、本番実行：

```bash
/ralph-loop "Skill documentation generation" \
  --completion-promise "TASK COMPLETE" \
  --max-iterations 40
```

## コマンドリファレンス

### /ralph-loop

自律的ループ実行を開始します。

**基本構文**:
```bash
/ralph-loop "<task-description>" \
  --completion-promise "<promise-text>" \
  --max-iterations <number>
```

**パラメータ**:
- `<task-description>`: タスクの説明（Claude Codeに表示）
- `--completion-promise`: 完了を示すプロミステキスト（PROMPT.mdで出力）
- `--max-iterations`: 最大イテレーション数（安全装置）

**実行例**:
```bash
/ralph-loop "Generate documentation for 83 skills" \
  --completion-promise "DOCUMENTATION COMPLETE" \
  --max-iterations 40
```

### /cancel-ralph

実行中のRalph Wiggumループを中断します。

**使用タイミング**:
- 無限ループに陥った時
- コストが予想を超えた時
- 意図しない変更が発生した時

**実行方法**:
```bash
/cancel-ralph
```

**中断後の復旧**:
```bash
# 1. 最後の正常なコミットを確認
git log --oneline -20

# 2. 問題のあるコミットまで戻す
git reset --hard <commit-hash>

# 3. ブランチをクリーンアップ
git clean -fd
```

### <promise>タグ

PROMPT.mdの中で完了を示すために使用します。

**構文**:
```markdown
<promise>TASK COMPLETE</promise>
```

**重要**:
- `--completion-promise`パラメータと一致する文字列を使用
- XML形式のタグで囲む
- PROMPT.mdの「完了時の出力」セクションに記載

**良い例**:
```markdown
# PROMPT.md
**完了時の出力**:
<promise>ALL SKILLS DOCUMENTED</promise>
```

```bash
/ralph-loop "..." --completion-promise "ALL SKILLS DOCUMENTED" --max-iterations 40
```

**悪い例**（不一致）:
```markdown
# PROMPT.md
<promise>TASK DONE</promise>
```

```bash
/ralph-loop "..." --completion-promise "TASK COMPLETE" --max-iterations 40
# → 完了検知が機能しない
```

## 安全ルール

### 必須ルール（MUST）

#### 1. max-iterationsを必ず設定

**理由**: 無限ループ防止

**推奨値**:
- 初回テスト: `--max-iterations 10`
- 軽量タスク: `--max-iterations 20`
- 中規模タスク: `--max-iterations 40`
- 大規模タスク: `--max-iterations 80`（最大）

**例外なし**: max-iterationsを省略すると無限ループのリスクがあります。

#### 2. Gitリポジトリで実行

**理由**: 各イテレーションで自動コミットが作成され、失敗時の復旧が可能

**確認方法**:
```bash
git status
# → "On branch ralph-<task-name>" と表示されること
```

**NG**: Gitリポジトリ外での実行は禁止

#### 3. 新規ブランチで実行

**理由**: mainブランチの破損を防ぐ

**ブランチ命名規則**:
```bash
ralph-<task-name>
# 例: ralph-documentation, ralph-refactoring
```

**確認方法**:
```bash
git branch
# → * ralph-<task-name> が選択されていること
```

#### 4. コスト監視

**理由**: 反復実行によるコスト爆発を防ぐ

**監視方法**:
1. 初回10イテレーションでコストを測定
2. 総イテレーション数からコストを予測
3. 予算オーバーの場合は中断

**計算例**:
```
初回10イテレーション = $2.0
予定80イテレーション = $2.0 × 8 = $16.0
→ 予算$10の場合は max-iterations を50に削減
```

### 推奨ルール（SHOULD）

#### 1. 初回10イテレーションでテスト

**理由**: プロンプト品質とコストを事前検証

**テスト手順**:
```bash
# 1. テスト実行
/ralph-loop "Test" --completion-promise "TEST DONE" --max-iterations 10

# 2. 結果確認
git log --oneline -10  # コミット履歴
git diff HEAD~10       # 変更内容

# 3. コスト確認（APIダッシュボード）

# 4. 問題なければ本番実行
/ralph-loop "..." --completion-promise "..." --max-iterations 40
```

#### 2. コンテキスト使用率50%以下で開始

**理由**: イテレーション中にコンテキストが肥大化

**確認方法**:
```bash
/context
# → 50%以下を確認
```

**コンテキスト削減方法**:
```bash
# 1. 不要なファイルを.claudeignoreに追加
# 2. /compact でコンテキスト圧縮
# 3. /clear で新規セッション開始（最終手段）
```

#### 3. Haikuモデルを推奨

**理由**: コスト効率が高い（Sonnetの約1/10）

**モデル選択**:
```bash
# ~/.claude/settings.json
{
  "model": "haiku"
}
```

**例外**: 複雑な推論が必要な場合のみSonnet

#### 4. 実行前に現在の状態をコミット

**理由**: 失敗時の復旧ポイント確保

**手順**:
```bash
git add .
git commit -m "chore: Snapshot before Ralph Wiggum execution"
/ralph-loop "..." --completion-promise "..." --max-iterations 40
```

## 適用範囲

### 適しているタスク

Ralph Wiggumは以下のタスクに最適です：

#### 1. 大量の定型ドキュメント作成

**例**: 83個のスキルREADME作成

**特徴**:
- 各ファイルが独立
- テンプレートが存在
- 反復作業が多い

**推奨パラメータ**:
```bash
--max-iterations 40
--completion-promise "ALL DOCUMENTATION COMPLETE"
```

#### 2. パス統一・リファクタリング

**例**: 108箇所のハードコードパス修正

**特徴**:
- 検索＆置換の繰り返し
- 各ファイルが独立
- テスト実行で検証可能

**推奨パラメータ**:
```bash
--max-iterations 60
--completion-promise "ALL PATHS UNIFIED"
```

#### 3. 翻訳タスク

**例**: 26個の英語ドキュメントを日本語化

**特徴**:
- ファイル単位で完結
- 品質確認が容易
- 一定のフォーマット

**推奨パラメータ**:
```bash
--max-iterations 20
--completion-promise "TRANSLATION COMPLETE"
```

#### 4. テストケース生成

**例**: 各モジュールのユニットテスト作成

**特徴**:
- モジュール単位で独立
- テンプレートが存在
- 自動検証可能

**推奨パラメータ**:
```bash
--max-iterations 30
--completion-promise "ALL TESTS GENERATED"
```

#### 5. コード生成（定型パターン）

**例**: CRUDエンドポイント作成

**特徴**:
- パターンが明確
- 各エンドポイントが独立
- 自動テスト可能

**推奨パラメータ**:
```bash
--max-iterations 25
--completion-promise "ALL ENDPOINTS GENERATED"
```

#### 6. データ変換・マイグレーション

**例**: JSON → YAML変換（100ファイル）

**特徴**:
- 変換ロジックが単純
- ファイル単位で完結
- バリデーション可能

**推奨パラメータ**:
```bash
--max-iterations 50
--completion-promise "MIGRATION COMPLETE"
```

#### 7. ドキュメント品質向上

**例**: 全マークダウンファイルのリンク修正

**特徴**:
- 検証ルールが明確
- ファイル単位で処理
- 差分確認が容易

**推奨パラメータ**:
```bash
--max-iterations 40
--completion-promise "QUALITY CHECKS COMPLETE"
```

### 適していないタスク

以下のタスクにはRalph Wiggumを使用しないでください：

#### 1. 複雑な設計・アーキテクチャ

**理由**: 反復より深い思考が必要

**代替手段**: Plan エージェント（Task tool）

#### 2. デバッグ・問題調査

**理由**: 試行錯誤が必要で、ループが予測不能

**代替手段**: 手動デバッグセッション

#### 3. ユーザー入力が必要なタスク

**理由**: 自律ループは人間の介入を想定していない

**代替手段**: インタラクティブセッション

#### 4. カバレッジ測定が必要なタスク

**理由**: Ralph Wiggumはテストカバレッジを自動検出できない

**代替手段**: 手動実装 + テストツール

#### 5. 高度な推論が必要なタスク

**理由**: 反復実行より一発の深い分析が効率的

**代替手段**: Opusモデルで単発実行

## aipm_v0プロジェクトでの定常タスク

### シナリオA: スキルドキュメント作成

**対象**: `.claude/skills/` 配下の83スキル

**タスク**: 各スキルの`README.md`を作成

**推奨パラメータ**:
```bash
--max-iterations 40
--completion-promise "SKILL DOCUMENTATION COMPLETE"
```

**PROMPT.md例**:
```markdown
# Task: Skill Documentation

以下の83個のスキルについて、`README.md`を作成してください。

**対象ディレクトリ**: `.claude/skills/`

**作成ルール**:
1. 各スキルディレクトリに`README.md`を作成
2. 最低200行以上
3. `SKILL.md`の内容をベースに、以下を追加：
   - 使用例3-5個
   - トラブルシューティング
   - 他スキルとの連携方法

**テンプレート**: `@.claude/skills/_shared/skill_template.md`

**完了条件**:
1. 全83スキルの`README.md`が存在
2. 各READMEが200行以上
3. フォーマットが統一されている

**完了時の出力**:
<promise>SKILL DOCUMENTATION COMPLETE</promise>
```

**推定コスト**: $7-16（Haiku）、$140-320（Sonnet）

**所要時間**: 約2-3時間（40イテレーション）

### シナリオB: パス統一作業

**対象**: プロジェクト全体の108箇所のハードコードパス

**タスク**: 括弧の統一（半角→全角）、環境変数化

**推奨パラメータ**:
```bash
# Stage 1: 半角→全角置換（25イテレーション）
--max-iterations 25
--completion-promise "STAGE1 COMPLETE"

# Stage 2: 環境変数化（35イテレーション）
--max-iterations 35
--completion-promise "STAGE2 COMPLETE"

# Stage 3: 検証（20イテレーション）
--max-iterations 20
--completion-promise "VALIDATION COMPLETE"
```

**3段階アプローチ**:

**Stage 1**: 半角括弧→全角括弧（25イテレーション）
```markdown
# Task: Path Unification Stage 1

以下のパスの半角括弧を全角に統一してください。

**対象**: 108箇所のハードコードパス

**検索パターン**:
- `創業支援・新規事業開発(AIエージェント)` → `創業支援・新規事業開発（AIエージェント）`
- 半角括弧 `(` → 全角括弧 `（`
- 半角括弧 `)` → 全角括弧 `）`

**完了条件**:
1. 全ファイルで半角括弧を全角に変換
2. `scripts/validate_paths.py` で検証パス

**完了時の出力**:
<promise>STAGE1 COMPLETE: All parentheses unified</promise>
```

**Stage 2**: 環境変数化（35イテレーション）
```markdown
# Task: Path Unification Stage 2

ハードコードパスを環境変数に置き換えてください。

**対象**: 108箇所のハードコードパス（全角統一済み）

**置換ルール**:
```python
# Before
path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）"

# After
from pathlib import Path
import os
BASE_DIR = Path(os.environ.get("AIPM_ROOT", Path.home() / "AIPM"))
path = BASE_DIR / "aipm_v0" / "Stock" / "programs" / "創業支援・新規事業開発（AIエージェント）"
```

**完了条件**:
1. 全ハードコードパスを環境変数化
2. `scripts/validate_paths.py` で検証パス

**完了時の出力**:
<promise>STAGE2 COMPLETE: All paths use environment variables</promise>
```

**Stage 3**: 検証（20イテレーション）
```markdown
# Task: Path Unification Stage 3

パス統一の最終検証を実施してください。

**検証項目**:
1. `scripts/validate_paths.py` 実行
2. 全テストパス
3. リンク切れチェック

**完了条件**:
1. 全検証パス
2. リンク切れ0件

**完了時の出力**:
<promise>VALIDATION COMPLETE: All paths verified</promise>
```

**推定コスト**: $37-60（Haiku）、$740-1200（Sonnet）

**所要時間**: 約4-6時間（合計80イテレーション）

### シナリオC: テストカバレッジ向上

**注意**: このシナリオはRalph Wiggumに**適していません**。

**理由**:
1. Ralph Wiggumはカバレッジを自動検出できない
2. テストの品質判断が難しい
3. 複雑なロジックの理解が必要

**推奨代替手段**:
- 手動で各モジュールのテストを実装
- カバレッジツール（pytest-cov）で測定
- イテレーティブにカバレッジを向上

### シナリオD: ドキュメント翻訳（英語→日本語）

**対象**: `docs/implementation_guides/` 配下の26ファイル

**タスク**: 英語ドキュメントを日本語に翻訳

**推奨パラメータ**:
```bash
--max-iterations 20
--completion-promise "TRANSLATION COMPLETE"
```

**PROMPT.md例**:
```markdown
# Task: Documentation Translation

以下の26個のドキュメントを英語から日本語に翻訳してください。

**対象ディレクトリ**: `docs/implementation_guides/`

**翻訳ルール**:
1. 技術用語は英語のまま（例: Claude Code, Ralph Wiggum, Git Worktrees）
2. コードブロックは翻訳しない
3. フォーマットを維持
4. 翻訳後のファイル名: `<original>_ja.md`

**完了条件**:
1. 全26ファイルの翻訳完了
2. フォーマット維持
3. リンク切れなし

**完了時の出力**:
<promise>TRANSLATION COMPLETE: 26 files translated</promise>
```

**推定コスト**: $10-20（Haiku）、$200-400（Sonnet）

**所要時間**: 約1-2時間（20イテレーション）

## コスト管理

### 見積もり表

| タスクタイプ | イテレーション数 | Haiku | Sonnet | Opus |
|------------|---------------|-------|--------|------|
| **軽量** | 10-20 | $0.5-2.0 | $10-40 | $50-200 |
| **中規模** | 20-40 | $2.0-8.0 | $40-160 | $200-800 |
| **大規模** | 40-80 | $8.0-32.0 | $160-640 | $800-3200 |

### モデル選択戦略

**Haiku推奨タスク**:
- ドキュメント作成（テンプレートあり）
- パス統一・置換
- 翻訳
- データ変換

**Sonnet推奨タスク**:
- コード生成（ロジック含む）
- リファクタリング（複雑）
- テストケース生成（ロジック検証付き）

**Opus使用禁止**:
- Ralph Wiggumとの組み合わせは非推奨
- コストが爆発的に増加（$800-3200）

### コスト削減テクニック

#### 1. 初回10イテレーションで測定

```bash
# 1. テスト実行（Haiku）
/ralph-loop "Test" --completion-promise "TEST" --max-iterations 10

# 2. APIダッシュボードでコスト確認
# 例: 10イテレーション = $2.0

# 3. 総コスト予測
# 総イテレーション40 = $2.0 × 4 = $8.0

# 4. 予算に応じてmax-iterations調整
```

#### 2. タスク分割

大規模タスク（80イテレーション予定）を分割：

```bash
# 悪い例: 1回で80イテレーション
/ralph-loop "All tasks" --max-iterations 80
# → コスト$32、失敗時のリカバリが困難

# 良い例: 4回に分割（各20イテレーション）
/ralph-loop "Task 1/4" --max-iterations 20  # $4
/ralph-loop "Task 2/4" --max-iterations 20  # $4
/ralph-loop "Task 3/4" --max-iterations 20  # $4
/ralph-loop "Task 4/4" --max-iterations 20  # $4
# → 各段階で検証可能、失敗時のロスが小さい
```

#### 3. Haikuモデル使用

```bash
# モデル設定確認
cat ~/.claude/settings.json | jq '.model'

# Haikuに設定
# ~/.claude/settings.json
{
  "model": "haiku"
}
```

#### 4. .claudeignoreでコンテキスト削減

コンテキストが大きいほど、各イテレーションのコストが増加。

```
# .claudeignore
node_modules/
.venv/
dist/
build/
*.log
data/
```

## 実行中の監視

### リアルタイム監視

Ralph Wiggum実行中は以下をモニタリング：

#### 1. イテレーション進捗

```bash
# 別のターミナルで監視
watch -n 5 'git log --oneline -20'
```

各イテレーションで自動コミットが作成されるため、ログを確認することで進捗を把握。

#### 2. コンテキスト使用率

```bash
# メインターミナルで定期確認
/context
```

70%を超えた場合：
```bash
/compact
```

90%を超えた場合：
```bash
/cancel-ralph
# → 中断して /clear で新規セッション
```

#### 3. コスト累積

APIダッシュボードで確認：
- 累積コスト
- イテレーションあたりのコスト
- 予測総コスト

### 中断方法

#### 正常中断（完了）

完了プロミスが出力されると自動停止。

```bash
# PROMPT.mdの出力
<promise>TASK COMPLETE</promise>

# → Ralph Wiggum自動停止
```

#### 手動中断

```bash
/cancel-ralph
```

#### 緊急停止（ターミナル）

```bash
# Ctrl+C（ターミナルで実行している場合）
^C

# プロセス強制終了
pkill -f "claude-code"
```

## トラブルシューティング

### 問題1: 無限ループに陥る

**症状**: max-iterationsに到達しても停止しない

**原因**:
- 完了プロミスの不一致
- PROMPT.mdの完了条件が曖昧

**解決策**:

1. **完了プロミスの一致確認**

```bash
# PROMPT.md
<promise>TASK COMPLETE</promise>

# コマンド
/ralph-loop "..." --completion-promise "TASK COMPLETE" --max-iterations 40
# → 一致している ✅
```

2. **PROMPT.mdの完了条件を明確化**

悪い例:
```markdown
**完了条件**: すべてのファイルを処理する
```

良い例:
```markdown
**完了条件**:
1. `.claude/skills/` 配下の全83スキルに`README.md`が存在
2. 各READMEが200行以上
3. `scripts/validate_skills.sh` がパス
```

3. **max-iterations削減**

```bash
# 40イテレーションで完了しない場合
/cancel-ralph

# 20イテレーションに削減
/ralph-loop "..." --max-iterations 20
```

### 問題2: コンテキストが肥大化

**症状**: "Context low" 警告が頻発

**原因**:
- 各イテレーションで出力が蓄積
- .claudeignoreが不十分

**解決策**:

1. **.claudeignore拡充**

```bash
# .claudeignore に追加
Flow/
Archived/
*.log
*.cache
data/
```

2. **/compactでコンテキスト圧縮**

```bash
# 実行中に
/compact
```

3. **セッション再起動**

```bash
# 1. 現在の進捗を確認
git log --oneline -20

# 2. Ralph中断
/cancel-ralph

# 3. 新規セッション
/clear

# 4. 途中から再開
# PROMPT.mdを更新して残りのタスクのみ記載
/ralph-loop "Resume from iteration 30" --max-iterations 10
```

### 問題3: 意図しない変更が発生

**症状**: 想定外のファイルが編集される

**原因**:
- PROMPT.mdの指示が曖昧
- 対象ファイルが明示されていない

**解決策**:

1. **対象ファイルを明示**

悪い例:
```markdown
**対象**: すべてのPythonファイル
```

良い例:
```markdown
**対象**:
- `.claude/skills/*/SKILL.md`（83ファイル）
- **除外**: `_shared/`, `_archive/`
```

2. **Git reset で復旧**

```bash
# 1. 問題のあるコミットを特定
git log --oneline -20

# 2. 正常なコミットまで戻す
git reset --hard <commit-hash>

# 3. ブランチクリーンアップ
git clean -fd
```

3. **PROMPT.mdを修正して再実行**

```bash
# PROMPT.mdの対象ファイルを明確化
vi PROMPT.md

# 再実行
/ralph-loop "..." --completion-promise "..." --max-iterations 40
```

### 問題4: コストが予想以上に高い

**症状**: APIダッシュボードで想定の2-3倍のコスト

**原因**:
- Sonnetモデルが選択されている
- max-iterationsが過大

**解決策**:

1. **モデル確認**

```bash
cat ~/.claude/settings.json | jq '.model'
# → "haiku" であることを確認
```

2. **モデル変更**

```bash
# ~/.claude/settings.json
{
  "model": "haiku"
}
```

3. **max-iterations削減**

```bash
# 初回テスト
/ralph-loop "Test" --max-iterations 10

# コスト測定（例: $2.0）

# 総コスト予測
# 40イテレーション = $2.0 × 4 = $8.0

# 予算$5の場合
# max-iterations = 25（$2.0 × 2.5 = $5.0）
/ralph-loop "..." --max-iterations 25
```

### 問題5: プロンプト品質低下

**症状**: イテレーションが進むにつれて出力品質が低下

**原因**:
- コンテキストに古い出力が蓄積
- プロンプトの曖昧さが増幅される

**解決策**:

1. **プロンプトを明確化**

悪い例:
```markdown
**タスク**: ドキュメントを作成してください
```

良い例:
```markdown
**タスク**: 以下の具体的なフォーマットでドキュメントを作成してください

**フォーマット**:
```
# {スキル名}

## 概要
[2-3行で説明]

## 使用方法
[3-5個の実例]

## トラブルシューティング
[よくある問題3-5個]
```

**完了条件**:
1. 上記フォーマットに完全に一致
2. 各セクションが指定行数以上
```

2. **/compactでコンテキスト圧縮**

```bash
# 20イテレーション毎に
/compact
```

3. **イテレーション数を減らす**

```bash
# 40 → 20に削減
/ralph-loop "..." --max-iterations 20
```

4. **完了条件を厳格化**

```markdown
**完了条件**:
1. 全83スキルの`README.md`が存在
2. 各READMEが**正確に**200-300行
3. `scripts/validate_format.sh` が**エラー0件**でパス
```

### 問題6: モデル選択間違いによるコスト爆発

**症状**: 予想の3-5倍のコスト請求

**原因**: Opusモデルが誤って選択されている

**解決策**:

1. **モデル確認**

```bash
cat ~/.claude/settings.json | jq '.model'
# → "opus" になっていないか確認
```

2. **Haikuに修正**

```bash
# ~/.claude/settings.json
{
  "model": "haiku"  // または "sonnet"
}
```

3. **プロジェクト設定でモデルを固定**

```bash
# .claude/project-settings.json
{
  "defaultModel": "haiku"
}
```

4. **実行前にモデル選択を明示的に確認**

```bash
# モデル確認を習慣化
cat ~/.claude/settings.json | jq '.model'
# → haiku であることを確認してから実行
```

## Week 3-4統合

### tmux並列実行との連携（Week 3）

Ralph Wiggumは単一タスクの自律ループですが、tmuxと組み合わせることで複数タスクを並列実行可能。

**シナリオ**: 4つの独立タスクを並列実行

```bash
# 1. tmuxセッション作成
tmux new-session -d -s ralph-parallel

# 2. 4ペイン作成
tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v

# 3. 各ペインでRalph Wiggum実行
tmux select-pane -t 0
tmux send-keys "/ralph-loop 'Task 1' --completion-promise 'TASK1 DONE' --max-iterations 20" C-m

tmux select-pane -t 1
tmux send-keys "/ralph-loop 'Task 2' --completion-promise 'TASK2 DONE' --max-iterations 20" C-m

tmux select-pane -t 2
tmux send-keys "/ralph-loop 'Task 3' --completion-promise 'TASK3 DONE' --max-iterations 20" C-m

tmux select-pane -t 3
tmux send-keys "/ralph-loop 'Task 4' --completion-promise 'TASK4 DONE' --max-iterations 20" C-m

# 4. tmuxセッションにアタッチ
tmux attach-session -t ralph-parallel
```

**注意**: 各タスクは完全に独立している必要があります。

### Git Worktreesとの連携（Week 4）

Ralph Wiggumは各イテレーションで自動コミットを作成するため、Git Worktreesと相性が良いです。

**シナリオ**: 4つのブランチで並列実行

```bash
# 1. 4つのworktreeを作成
git worktree add ../aipm_v0-task1 -b ralph-task1
git worktree add ../aipm_v0-task2 -b ralph-task2
git worktree add ../aipm_v0-task3 -b ralph-task3
git worktree add ../aipm_v0-task4 -b ralph-task4

# 2. 各worktreeで独立してRalph Wiggum実行
cd ../aipm_v0-task1
/ralph-loop "Task 1" --completion-promise "TASK1 DONE" --max-iterations 20

cd ../aipm_v0-task2
/ralph-loop "Task 2" --completion-promise "TASK2 DONE" --max-iterations 20

# ... 以下同様
```

**利点**:
- 各タスクが完全に独立
- コミット履歴が混在しない
- 失敗時のロールバックが容易

## リスク管理

Ralph Wiggum実行時の主要リスクとその対策：

### リスク1: 無限ループ

**発生確率**: 中

**影響度**: 高（コスト爆発）

**対策**:
- 必ず`--max-iterations`を設定（必須ルール1）
- 初回10イテレーションでテスト（推奨ルール1）
- 完了プロミスの厳密な一致確認

**検知方法**:
```bash
# イテレーション数監視
watch -n 5 'git log --oneline -10 | wc -l'
```

### リスク2: コンテキスト肥大化

**発生確率**: 高

**影響度**: 中（品質低下）

**対策**:
- コンテキスト50%以下で開始（推奨ルール2）
- .claudeignore設定（セットアップステップ3）
- 定期的に`/compact`実行

**検知方法**:
```bash
/context
# → 70%超えたら警告
```

### リスク3: 意図しない変更

**発生確率**: 中

**影響度**: 高（データ破損）

**対策**:
- 新規ブランチで実行（必須ルール3）
- 実行前にスナップショットコミット（推奨ルール4）
- 対象ファイルを明示（PROMPT.md）

**復旧方法**:
```bash
git reset --hard <safe-commit-hash>
git clean -fd
```

### リスク4: コスト爆発

**発生確率**: 中

**影響度**: 高（予算オーバー）

**対策**:
- Haikuモデル使用（推奨ルール3）
- 初回10イテレーションでコスト測定（推奨ルール1）
- max-iterations厳守（必須ルール1）

**検知方法**:
- APIダッシュボード監視
- 10イテレーション毎にコスト確認

## 失敗時の復旧

Ralph Wiggum実行が失敗した場合の復旧手順：

### ステップ1: 現在の状態確認

```bash
# 1. ブランチ確認
git branch
# → ralph-<task-name> にいることを確認

# 2. コミット履歴確認
git log --oneline -20

# 3. 変更内容確認
git diff HEAD~10
```

### ステップ2: 正常なコミットの特定

```bash
# コミットメッセージから判断
git log --oneline -20
# 例:
# abc123 Ralph iteration 15: Success
# def456 Ralph iteration 14: Success
# ghi789 Ralph iteration 13: Error ← ここで問題発生
```

### ステップ3: リセット実行

```bash
# 問題のあるコミットの1つ前まで戻す
git reset --hard def456

# 作業ディレクトリをクリーンアップ
git clean -fd
```

### ステップ4: 原因分析

```bash
# 失敗したコミットの変更内容を確認
git show ghi789
```

### ステップ5: PROMPT.md修正

```bash
# 問題の原因に応じてPROMPT.mdを修正
vi PROMPT.md

# 例: 対象ファイルを明確化、完了条件を厳格化
```

### ステップ6: 再実行

```bash
# 修正したPROMPT.mdで再実行
/ralph-loop "Resume task" --completion-promise "TASK COMPLETE" --max-iterations 30
```

## チェックリスト

Ralph Wiggum実行前後のチェックリスト。

### 実行前（必須）

- [ ] プラグイン有効化確認（`ralph-wiggum@claude-plugins-official: true`）
- [ ] Gitリポジトリ確認（`git status`）
- [ ] 新規ブランチ作成（`ralph-<task-name>`）
- [ ] スナップショットコミット作成
- [ ] コンテキスト使用率50%以下確認（`/context`）
- [ ] .claudeignore設定
- [ ] PROMPT.md作成
- [ ] 完了プロミス一致確認（PROMPT.md ↔ `--completion-promise`）
- [ ] 初回10イテレーションでテスト実行
- [ ] コスト見積もり確認

### 実行中（監視）

- [ ] イテレーション進捗監視（`git log --oneline -20`）
- [ ] コンテキスト使用率監視（`/context`）
- [ ] コスト累積監視（APIダッシュボード）
- [ ] 出力品質確認（定期的にコミット内容確認）
- [ ] エラー発生時の即座対応準備（`/cancel-ralph`）

### 実行後（検証）

- [ ] 完了プロミス出力確認
- [ ] 全タスク完了確認（PROMPT.mdの完了条件）
- [ ] コミット履歴確認（`git log --oneline -20`）
- [ ] 変更内容レビュー（`git diff main`）
- [ ] テスト実行（該当する場合）
- [ ] 総コスト確認（APIダッシュボード）
- [ ] ブランチマージ準備（`git checkout main && git merge ralph-<task-name>`）

## 参照

- **使用ガイド**: `@docs/implementation_guides/week8_ralph_wiggum.md`（508行）
- **Week 5統合**: `@docs/implementation_guides/week5_settings.md`
- **並列実行**: `@.claude/rules/parallel_execution.md`
- **コンテキスト管理**: `@.claude/rules/context_management.md`

---

**最終更新**: 2026-01-10
**作成者**: Claude Code（Sonnet 4.5）
**Week**: 8 - Ralph Wiggum Integration
**Phase**: 3（品質向上 - 統合ルール作成）
