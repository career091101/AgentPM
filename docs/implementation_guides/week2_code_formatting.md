# Code Formatting Rules - PostToolUse Hook Auto-Format

Claude Codeの公式PostToolUseフック機能を使用した自動コードフォーマットシステムのガイド。

## 概要

Edit/Writeツール実行後に自動的にコードフォーマットを適用し、コード品質を保ちます。

**実装方式**: Claude Code公式のPostToolUseフック（Bashコマンド型）

## サポート言語

| 言語 | フォーマッタ | 設定ファイル |
|------|------------|------------|
| **Python** | black + isort | pyproject.toml |
| **JavaScript/TypeScript** | prettier | .prettierrc |
| **Markdown** | prettier | .prettierrc |
| **JSON** | prettier | .prettierrc |
| **YAML** | prettier | .prettierrc |
| **CSS/SCSS** | prettier | .prettierrc |

## セットアップ

### 1. 初回セットアップ（1回のみ）

```bash
# フォーマッタのインストール
bash scripts/setup_formatters.sh
```

このスクリプトは以下をインストール：
- **black** 25.12.0（Homebrew経由）
- **isort** 7.0.0（Homebrew経由）
- **prettier** 3.7.4（npx経由）
- **jq** 1.7.1（オプション、JSONフォーマット強化）

### 2. PostToolUseフック設定（既に設定済み）

`~/.claude/settings.json` に以下の設定が追加されています：

```json
{
  "hooks": {
    "PostToolUse": [
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
  }
}
```

**動作**: Edit/Writeツールでファイルを変更すると、自動的に `format_changed_file.sh` が実行されます。

## 使い方

### 基本動作

Claude Codeで通常通りEdit/Writeツールを使用すると、自動的にフォーマットが実行されます。

**例**:
```python
# Claude Codeで以下のファイルを編集
# scripts/test.py

def hello( ):
    print("hello")
```

**結果（blackとisortが自動実行）**:
```python
def hello():
    print("hello")
```

### ON/OFFの切り替え

#### 一時的に無効化（セッション単位）

```bash
# 環境変数で無効化
export CLAUDE_AUTO_FORMAT=false

# Claude Code起動
claude

# フォーマットが無効化された状態で作業
```

#### 恒久的に無効化

```bash
# ~/.zshrc または ~/.bashrc に追加
export CLAUDE_AUTO_FORMAT=false
```

#### 再度有効化

```bash
# 環境変数を削除
unset CLAUDE_AUTO_FORMAT

# または明示的に有効化
export CLAUDE_AUTO_FORMAT=true
```

### 特定ファイルの除外

#### 方法1: .claudeignore_format

プロジェクトルートの `.claudeignore_format` に除外したいファイルパスを追加：

```
# Legacy code
Stock/programs/legacy_module/old_script.py

# Auto-generated files
scripts/auto_generated_config.py

# Archived projects
Archived/
```

**パス形式**: 絶対パスまたはプロジェクトルート `/Users/yuichi/AIPM/aipm_v0` からの相対パス

#### 方法2: .prettierignore（prettier専用）

prettierの除外パターンは `.prettierignore` に記載：

```
# Build outputs
dist/
build/

# Dependencies
node_modules/
```

#### 方法3: pyproject.toml（black/isort専用）

Pythonファイルの除外は `pyproject.toml` の `extend-exclude` に記載：

```toml
[tool.black]
extend-exclude = '''
/(
  Flow/
  | Archived/
)/
'''
```

## 設定のカスタマイズ

### Python（black/isort）

`pyproject.toml` を編集：

```toml
[tool.black]
line-length = 100          # 1行の最大文字数（デフォルト: 88）
target-version = ['py39']  # ターゲットPythonバージョン

[tool.isort]
profile = "black"          # blackとの互換性
line_length = 100          # blackと同じ設定を推奨
```

### JavaScript/TypeScript/Markdown（prettier）

`.prettierrc` を編集：

```json
{
  "printWidth": 100,       // 1行の最大文字数
  "tabWidth": 2,           // インデント幅
  "semi": true,            // セミコロンの有無
  "singleQuote": false,    // シングルクォート使用
  "trailingComma": "es5"   // 末尾カンマ
}
```

## フォーマット実行時の動作

### タイムアウト設定

各フォーマッタは5秒でタイムアウトします（`scripts/format_changed_file.sh` 内で設定）。

**タイムアウト時の動作**: 警告メッセージを表示し、Claude Codeの処理は継続。

### エラーハンドリング

フォーマッタがエラーで失敗しても、Claude Codeの処理は中断されません。

**例**:
```
⚠️  black failed or timed out
⚠️  Formatting failed for: /path/to/file.py
```

## トラブルシューティング

### 問題1: フォーマッタが実行されない

**原因**: 環境変数 `CLAUDE_AUTO_FORMAT` が `false` に設定されている

**確認**:
```bash
echo $CLAUDE_AUTO_FORMAT
```

**解決**:
```bash
unset CLAUDE_AUTO_FORMAT
# または
export CLAUDE_AUTO_FORMAT=true
```

### 問題2: "command not found: black"

**原因**: フォーマッタがインストールされていない

**解決**:
```bash
bash scripts/setup_formatters.sh
```

### 問題3: フォーマットが特定のファイルで失敗する

**原因**: ファイル内の文法エラー、またはフォーマッタの互換性問題

**解決**:
1. 該当ファイルを `.claudeignore_format` に追加して除外
2. 文法エラーを手動で修正後、再度フォーマット

### 問題4: Pythonの"externally-managed-environment"エラー

**原因**: macOS/Linuxの新しいPython環境ではpipがシステムワイドインストールを制限

**解決**: `setup_formatters.sh` が自動的にHomebrewを使用します（既に対応済み）

### 問題5: フォーマット結果が期待と異なる

**原因**: 設定ファイル（pyproject.toml, .prettierrc）の設定が意図と異なる

**解決**:
1. 設定ファイルを確認・修正
2. フォーマッタを手動実行して確認

```bash
# Python
black /path/to/file.py
isort /path/to/file.py

# JavaScript/TypeScript
npx prettier --write /path/to/file.js
```

## パフォーマンス

### 実行時間目安

| ファイルサイズ | フォーマット時間 |
|--------------|----------------|
| 1-100行 | 0.5-1秒 |
| 100-500行 | 1-2秒 |
| 500-1000行 | 2-3秒 |
| 1000行以上 | 3-5秒（タイムアウト: 5秒） |

### 並列実行時の注意

複数ファイルを並列でEdit/Writeした場合、各フォーマッタは並列実行されます（Claude Codeの制御下）。

## ベストプラクティス

### 1. プロジェクト開始時に設定統一

チーム全員が同じ設定ファイル（pyproject.toml, .prettierrc）を使用し、Gitで管理。

### 2. 既存コードの一括フォーマット

新規プロジェクトまたは大規模リファクタリング時は、事前に一括フォーマット：

```bash
# Python
black .
isort .

# JavaScript/TypeScript/Markdown
npx prettier --write "**/*.{js,jsx,ts,tsx,md,json,yaml,yml,css,scss}"
```

### 3. .claudeignore_formatの適切な管理

以下のファイルは除外を推奨：
- Legacy code（既存のフォーマットを維持）
- Auto-generated files（手動編集しない）
- Third-party vendored code（外部ライブラリ）

### 4. CI/CDでのフォーマットチェック

PRマージ前にフォーマットチェックを実行（GitHub Actions等）：

```yaml
# .github/workflows/format-check.yml
name: Format Check
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check Python formatting
        run: |
          black --check .
          isort --check .
      - name: Check JavaScript/TypeScript formatting
        run: npx prettier --check "**/*.{js,jsx,ts,tsx}"
```

## ファイル構成

| ファイルパス | 役割 |
|------------|------|
| `~/.claude/settings.json` | PostToolUseフック設定 |
| `scripts/format_changed_file.sh` | フォーマット実行スクリプト（Bashコマンドフック） |
| `scripts/setup_formatters.sh` | フォーマッタインストールスクリプト |
| `pyproject.toml` | black, isort 設定 |
| `.prettierrc` | prettier 設定 |
| `.prettierignore` | prettier 除外パターン |
| `.claudeignore_format` | 全フォーマッタ共通の除外ファイルリスト |

## フォーマッタの詳細

### black（Python）

**公式サイト**: https://black.readthedocs.io/

**特徴**:
- PEP 8準拠
- 設定項目が少なく、統一されたスタイル
- インデント: スペース4つ（変更不可）

**主な設定項目**:
- `line-length`: 1行の最大文字数（デフォルト: 88、推奨: 100）
- `target-version`: Pythonバージョン

### isort（Python import文）

**公式サイト**: https://pycqa.github.io/isort/

**特徴**:
- import文の自動ソート・グループ化
- blackとの互換性プロファイル提供

**主な設定項目**:
- `profile`: `"black"` を推奨
- `line_length`: blackと同じ値に設定
- `sections`: import文のグループ分け順序

### prettier（JavaScript/TypeScript/Markdown等）

**公式サイト**: https://prettier.io/

**特徴**:
- 複数言語対応（JS, TS, JSON, YAML, Markdown, CSS等）
- 設定項目が少なく、統一されたスタイル

**主な設定項目**:
- `printWidth`: 1行の最大文字数（デフォルト: 80、推奨: 100）
- `tabWidth`: インデント幅（デフォルト: 2）
- `semi`: セミコロンの有無（デフォルト: true）
- `singleQuote`: シングルクォート使用（デフォルト: false）

## 更新履歴

- **2026-01-03**: Week 2実装完了（PostToolUseフック + 自動フォーマット）
  - フック設定追加（~/.claude/settings.json）
  - フォーマットスクリプト作成（format_changed_file.sh）
  - フォーマッタインストールスクリプト作成（setup_formatters.sh）
  - 設定ファイル作成（pyproject.toml, .prettierrc, .prettierignore, .claudeignore_format）
  - 使用ガイド作成（本ドキュメント）

## 参照

- [Claude Code公式ドキュメント - Hooks](https://code.claude.com/docs/en/hooks)
- [black公式ドキュメント](https://black.readthedocs.io/)
- [isort公式ドキュメント](https://pycqa.github.io/isort/)
- [prettier公式ドキュメント](https://prettier.io/)
- @.claude/rules/execution_preference.md - LLM優先アプローチ
- @scripts/setup_formatters.sh - フォーマッタセットアップ
- @scripts/format_changed_file.sh - フォーマット実行ロジック
