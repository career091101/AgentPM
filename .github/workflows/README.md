# GitHub Actions Workflows

このディレクトリには、プロジェクト自動化のためのGitHub Actionsワークフローが格納されています。

## validate-skills.yml

ForStartupプロジェクトのスキルファイルを自動検証するCI/CDワークフロー。

### 検証項目

1. **YAMLフロントマター必須フィールド検証**
   - `trigger_keywords` （配列、必須）
   - `stage` （文字列、必須）
   - `output_file` （文字列、必須）
   - `dependencies` （配列、必須）
   - `name` （文字列、推奨）
   - `description` （文字列、推奨）

2. **フィールド型検証**
   - 各フィールドが正しい型であることを確認

3. **フロントマター内容検証**
   - `trigger_keywords` が空でないか
   - `stage` が有効な値か
   - `output_file` が全角括弧を使用しているか
   - `dependencies` の各要素が文字列か

4. **ファイル構造検証**
   - Markdown見出し（# Title）が存在するか
   - 本文が十分な長さか（100文字以上）

5. **ForRecruit残骸チェック**
   - "ForRecruit"を含むテキストが存在しないか

### トリガー条件

このワークフローは以下の条件で自動実行されます:

```yaml
on:
  push:
    paths:
      - '.claude/skills/for_startup/**'
  pull_request:
    paths:
      - '.claude/skills/for_startup/**'
```

- `.claude/skills/for_startup/` 以下のファイル変更時
- Push と Pull Request の両方で実行

### 実行ステップ

1. **コード取得** (`actions/checkout@v4`)
   - 最新コードをチェックアウト

2. **Python環境セットアップ** (`actions/setup-python@v5`)
   - Python 3.11をインストール

3. **依存関係インストール**
   - `pyyaml` をインストール（YAML解析用）

4. **YAMLフロントマター検証** (`scripts/validate_skills.py`)
   - Python検証スクリプトを実行
   - `validation_report.json` を生成

5. **ForRecruit残骸チェック**
   - grep で "ForRecruit" を検索
   - 見つかった場合はエラー終了

6. **PRへのコメント投稿** （PR時のみ）
   - 検証結果をコメントとして自動投稿
   - エラー・警告の一覧を表示

7. **最終判定**
   - エラーがある場合はワークフロー失敗（Exit 1）

### 出力

#### validation_report.json

```json
{
  "timestamp": "2026-01-09T10:18:15.963007",
  "errors": [
    {
      "file": ".claude/skills/for_startup/validate-psf/SKILL.md",
      "message": "Error details...",
      "severity": "error"
    }
  ],
  "warnings": [
    {
      "file": ".claude/skills/for_startup/startup-scorecard/SKILL.md",
      "message": "Warning details...",
      "severity": "warning"
    }
  ],
  "summary": {
    "total_files": 30,
    "valid_files": 29,
    "invalid_files": 1,
    "total_issues": 24
  }
}
```

#### PR上のコメント例

```
## ForStartup Skills Validation Report

### Validation Results

❌ **Validation Errors Found**

- **.claude/skills/for_startup/validate-psf/SKILL.md**: Error during validation: Invalid YAML frontmatter...

### Warnings

- **.claude/skills/for_startup/startup-scorecard/SKILL.md**: stage 'Phase5（Monitoring）' may not be in standard format...

### Summary

- Total files scanned: 30
- Valid files: 29
- Invalid files: 1
```

## ローカルでの検証実行

開発時にローカルで検証スクリプトを実行できます:

```bash
# 検証スクリプトの実行
python3 scripts/validate_skills.py

# 結果確認
cat validation_report.json | jq .
```

## 検証ルール詳細

### 必須フィールド

#### trigger_keywords (配列)

スキルをトリガーするキーワードのリスト。

```yaml
trigger_keywords:
  - "CPF検証"
  - "CPF達成判定"
  - "Customer Problem Fit"
```

**検証ルール:**
- 配列型であること
- 1個以上のキーワードを含むこと（警告あり）
- 各要素が文字列であること

#### stage (文字列)

スキルが属するPMBOKフェーズまたはプロジェクトステージ。

```yaml
stage: Phase2（CPF検証）
```

**標準値:**
- `Phase1` （需要発見）
- `Phase2` （CPF検証）
- `Phase3` （PSF検証）
- `Phase4` （実装）
- `planning`, `discovery`, `research`

**拡張値:**
- `Phase1（需要発見）`
- `Phase2（CPF検証）`
- `Phase3（PSF検証）`
- `Phase4（実装）`
- その他の詳細説明（警告が出る可能性あり）

#### output_file (文字列)

スキル実行後の出力ファイルパス。プロジェクト内の相対パスまたは変数を使用。

```yaml
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/persona.md
```

**検証ルール:**
- フォルダ名に括弧を使用する場合は全角括弧（）のみ
- 半角括弧(AIエージェント)は検出されエラーになる

**変数使用例（非推奨）:**
```yaml
output_file: {OUTPUT_DIR}/output.md  # YAML構文エラー！
```

代わりに以下を推奨:
```yaml
output_file: Stock/programs/.../output.md  # 完全パスを記述
```

#### dependencies (配列)

このスキルが依存する他のスキル。

```yaml
dependencies:
  - create-persona
  - simulate-interview
  - research-problem
```

**検証ルール:**
- 配列型であること
- 空配列は許可（依存なし）
- 各要素が文字列であること

### 推奨フィールド

#### name (文字列)

スキルの一意な識別子。

```yaml
name: create-persona
```

#### description (文字列)

スキルの説明。複数行対応（マルチラインストリング）。

```yaml
description: |
  ペルソナを自動生成する自律実行型スキル。
  起業の科学のペルソナ8要素に加え、市場規模評価を統合します。
```

## ForRecruit残骸チェック

### 検出ルール

- `ForRecruit` というテキストを含むファイルを検出
- ケース非依存（`forrecruit`, `FORRECRUIT` も検出）
- スキルファイル内（_analysisや PHASEドキュメント除外）での検出時は警告

### 除外パターン

以下のファイルは検出対象外:
- `*_analysis/*.md`
- `PHASE*.md`
- 完了レポート類

### 修復方法

ForRecruit参照が見つかった場合:

```bash
# 対象ファイルを確認
grep -r "ForRecruit" .claude/skills/for_startup/ --include="*.md"

# 参照を削除・置換
# フォルダ側で ForRecruit → for_startup に修正
```

## 既知の警告

検証スクリプト実行時に出力される主な警告:

1. **stage値が標準形式でない**
   - `Phase5（Monitoring）` → 非標準
   - `Phase1`, `Phase2`, `Phase3`, `Phase4` が標準

2. **ForRecruit参照が残存**
   - 旧プロジェクト構造への参照を検出
   - パスの置換が必要

## トラブルシューティング

### ワークフロー失敗時

1. **YAML構文エラー**
   ```
   Invalid YAML frontmatter: while parsing a block mapping...
   ```
   → `validation_report.json` を確認、フロントマターのYAML構文を修正

2. **ForRecruit検出**
   ```
   ERROR: ForRecruit remnants found!
   ```
   → `grep -r "ForRecruit"` で対象ファイルを特定、テキストを置換

3. **必須フィールド不足**
   ```
   Missing required fields: trigger_keywords, stage
   ```
   → YAML フロントマターに必須フィールドを追加

### ローカルでの再現

```bash
# PR前にローカルでテスト
python3 scripts/validate_skills.py

# JSON レポート確認
jq . validation_report.json

# PR用エラーリスト表示
jq '.errors' validation_report.json
```

## 参考資料

- 検証スクリプト: `/scripts/validate_skills.py`
- ワークフロー定義: `/.github/workflows/validate-skills.yml`
- PMBOK ワークフロー: `/docs/ai/pmbok_workflow.md`
- パス規約: `/.claude/rules/path_conventions.md`
