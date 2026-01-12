# Code Formatting Rules

PostToolUseフック自動コードフォーマット機能のユーザーガイド。

## 概要

Claude Codeの公式PostToolUseフック機能を使用した自動コードフォーマットシステム。Edit/Writeツール実行後に自動的にコードフォーマットを適用し、プロジェクト全体で統一されたコード品質を維持します。

**実装方式**: Claude Code公式のPostToolUseフック（Bashコマンド型）

### 主な特徴

- **自動実行**: Edit/Write後に自動でフォーマット実行（手動操作不要）
- **マルチ言語対応**: Python, JavaScript, TypeScript, Markdown, JSON, YAML, CSS
- **非侵入的**: タイムアウト/エラー時もClaude Codeの処理を中断しない
- **カスタマイズ可能**: プロジェクトごとに設定ファイルで調整
- **選択的除外**: 特定ファイル・ディレクトリを除外可能

## 対応言語とフォーマッタ

| 言語 | フォーマッタ | 設定ファイル | バージョン |
|------|------------|------------|----------|
| **Python** | black + isort | pyproject.toml | black 25.12.0, isort 7.0.0 |
| **JavaScript/TypeScript** | prettier | .prettierrc | prettier 3.7.4 |
| **Markdown** | prettier | .prettierrc | prettier 3.7.4 |
| **JSON** | prettier | .prettierrc | prettier 3.7.4 |
| **YAML** | prettier | .prettierrc | prettier 3.7.4 |
| **CSS/SCSS** | prettier | .prettierrc | prettier 3.7.4 |

## セットアップ

### 1. 初回セットアップ（1回のみ）

```bash
# プロジェクトルートで実行
cd /Users/yuichi/AIPM/aipm_v0

# フォーマッタのインストール
bash scripts/setup_formatters.sh
```

このスクリプトは以下をインストールします:
- **black** 25.12.0（Homebrew経由、システムワイドインストール）
- **isort** 7.0.0（Homebrew経由）
- **prettier** 3.7.4（npx経由、自動ダウンロード）
- **jq** 1.7.1（オプション、JSONフォーマット強化）

**所要時間**: 3-5分（初回のみ）

### 2. PostToolUseフック設定確認

`~/.claude/settings.json` に以下の設定が既に追加されています:

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

**動作フロー**:
1. Claude Codeが `Edit`/`Write` ツールを実行
2. ツール完了直後にPostToolUseフックが起動
3. `format_changed_file.sh` がファイルを自動フォーマット
4. Claude Codeの処理が継続

### 3. 設定確認

```bash
# フォーマッタのインストール確認
black --version    # 25.12.0
isort --version    # 7.0.0
npx prettier --version  # 3.7.4

# 設定ファイル確認
ls -la pyproject.toml .prettierrc .prettierignore .claudeignore_format
```

## 使い方

### 基本動作

Claude Codeで通常通りEdit/Writeツールを使用すると、自動的にフォーマットが実行されます。

**例: Pythonファイルの編集**

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

**例: JavaScriptファイルの作成**

```javascript
// Claude Codeで以下を作成
// scripts/example.js

const hello=(name)=>{console.log("Hello, "+name)}
```

**結果（prettierが自動実行）**:

```javascript
const hello = (name) => {
  console.log("Hello, " + name);
};
```

### ON/OFFの切り替え

#### 一時的に無効化（セッション単位）

```bash
# 環境変数で無効化
export CLAUDE_AUTO_FORMAT=false

# Claude Code起動
claude

# この状態ではフォーマットが実行されない
```

#### 恒久的に無効化

```bash
# ~/.zshrc または ~/.bashrc に追加
export CLAUDE_AUTO_FORMAT=false

# シェル再起動
source ~/.zshrc
```

#### 再度有効化

```bash
# 環境変数を削除
unset CLAUDE_AUTO_FORMAT

# または明示的に有効化
export CLAUDE_AUTO_FORMAT=true
```

### 特定ファイルの除外

#### 方法1: .claudeignore_format（推奨）

プロジェクトルートの `.claudeignore_format` に除外したいファイルパスを追加:

```
# Legacy code - フォーマット適用外
Stock/programs/legacy_module/old_script.py

# Auto-generated files - 自動生成ファイル
scripts/auto_generated_config.py
docs/api_reference_auto.md

# Archived projects - アーカイブ済みプロジェクト
Archived/

# Third-party code - サードパーティコード
vendor/
```

**パス形式**: プロジェクトルート `/Users/yuichi/AIPM/aipm_v0` からの相対パスまたは絶対パス

#### 方法2: .prettierignore（prettier専用）

prettierの除外パターンは `.prettierignore` に記載:

```
# Build outputs
dist/
build/
out/

# Dependencies
node_modules/
.venv/
venv/

# Large data files
data/
*.csv
```

#### 方法3: pyproject.toml（black/isort専用）

Pythonファイルの除外は `pyproject.toml` の `extend-exclude` に記載:

```toml
[tool.black]
extend-exclude = '''
/(
  Flow/
  | Archived/
  | legacy_code/
)/
'''

[tool.isort]
extend_skip = [
    "Flow",
    "Archived",
    "legacy_code"
]
```

## 設定のカスタマイズ

### Python（black/isort）

`pyproject.toml` を編集:

```toml
[tool.black]
line-length = 100          # 1行の最大文字数（デフォルト: 88）
target-version = ['py39']  # ターゲットPythonバージョン

[tool.isort]
profile = "black"          # blackとの互換性
line_length = 100          # blackと同じ設定を推奨
multi_line_output = 3      # 複数行インポートの形式
```

**主要設定項目**:

| 項目 | デフォルト | 推奨 | 説明 |
|------|----------|------|------|
| `line-length` | 88 | 100 | 1行の最大文字数 |
| `target-version` | py38 | py39, py310 | Pythonバージョン |
| `profile` | default | black | isortプロファイル（black互換） |

### JavaScript/TypeScript/Markdown（prettier）

`.prettierrc` を編集:

```json
{
  "printWidth": 100,       // 1行の最大文字数
  "tabWidth": 2,           // インデント幅
  "semi": true,            // セミコロンの有無
  "singleQuote": false,    // シングルクォート使用
  "trailingComma": "es5",  // 末尾カンマ
  "proseWrap": "always"    // Markdownの折り返し
}
```

**主要設定項目**:

| 項目 | デフォルト | 説明 |
|------|----------|------|
| `printWidth` | 80 | 1行の最大文字数（推奨: 100） |
| `tabWidth` | 2 | インデント幅 |
| `semi` | true | セミコロン挿入 |
| `singleQuote` | false | シングルクォート使用 |
| `trailingComma` | "es5" | 末尾カンマの挿入ルール |

### ファイル別の設定（prettierのoverrides機能）

```json
{
  "printWidth": 100,
  "overrides": [
    {
      "files": "*.md",
      "options": {
        "proseWrap": "always",
        "printWidth": 80
      }
    },
    {
      "files": "*.json",
      "options": {
        "printWidth": 80,
        "tabWidth": 2
      }
    }
  ]
}
```

## フォーマット実行時の動作

### タイムアウト設定

各フォーマッタは5秒でタイムアウトします（`scripts/format_changed_file.sh` 内で設定）。

```bash
# format_changed_file.sh 内
readonly FORMATTER_TIMEOUT=5
```

**タイムアウト時の動作**: 警告メッセージを表示し、Claude Codeの処理は継続。

```
[ERROR] Formatter timeout (5s): black
```

### エラーハンドリング

フォーマッタがエラーで失敗しても、Claude Codeの処理は中断されません。

**例**:
```
[ERROR] Formatter failed with exit code 1: black
[WARN] Formatting failed for: /path/to/file.py
```

**非侵入的設計**:
- Exit Code 0で常に正常終了（`trap 'exit 0' ERR`）
- エラーメッセージはstderrに出力（Claude Codeのログに記録）
- フォーマット失敗時もEdit/Write操作は成功扱い

### ログ記録（オプション）

```bash
# 詳細ログを有効化
export CLAUDE_FORMAT_LOG=true

# Claude Code再起動後、ログファイルを確認
tail -f ~/.claude/logs/format.log
```

**ログ内容**:
- 各フォーマッタの実行開始/完了
- タイムアウト/エラー詳細
- 除外ファイルの判定結果

## トラブルシューティング

### 問題1: フォーマッタが実行されない

**原因**: 環境変数 `CLAUDE_AUTO_FORMAT` が `false` に設定されている

**確認**:
```bash
echo $CLAUDE_AUTO_FORMAT
# → "false" と表示される場合
```

**解決**:
```bash
unset CLAUDE_AUTO_FORMAT
# または
export CLAUDE_AUTO_FORMAT=true

# Claude Code再起動
```

### 問題2: "command not found: black"

**原因**: フォーマッタがインストールされていない

**確認**:
```bash
black --version
isort --version
npx prettier --version
```

**解決**:
```bash
bash scripts/setup_formatters.sh
```

### 問題3: フォーマットが特定のファイルで失敗する

**原因**: ファイル内の文法エラー、またはフォーマッタの互換性問題

**エラー例**:
```
[ERROR] Formatter failed with exit code 1: black
File scripts/broken.py, line 5
    def hello(
            ^
SyntaxError: unexpected EOF while parsing
```

**解決**:
1. 該当ファイルを `.claudeignore_format` に追加して除外
2. 文法エラーを手動で修正後、再度フォーマット

```bash
# .claudeignore_format に追加
scripts/broken.py

# または文法エラーを修正
black scripts/broken.py  # 手動実行で確認
```

### 問題4: Pythonの"externally-managed-environment"エラー

**原因**: macOS/Linuxの新しいPython環境ではpipがシステムワイドインストールを制限

**エラー例**:
```
error: externally-managed-environment

× This environment is externally managed
```

**解決**: `setup_formatters.sh` が自動的にHomebrewを使用します（既に対応済み）

```bash
# Homebrew経由でインストール（自動）
brew install black isort
```

### 問題5: フォーマット結果が期待と異なる

**原因**: 設定ファイル（pyproject.toml, .prettierrc）の設定が意図と異なる

**確認**:
```bash
# Python
black --check /path/to/file.py --diff
isort --check-only /path/to/file.py --diff

# JavaScript/TypeScript
npx prettier --check /path/to/file.js
```

**解決**:
1. 設定ファイルを確認・修正
2. フォーマッタを手動実行して確認

```bash
# Python（設定確認）
black /path/to/file.py --verbose
isort /path/to/file.py --verbose

# JavaScript/TypeScript（設定確認）
npx prettier --write /path/to/file.js --log-level debug
```

### 問題6: タイムアウトが頻発する

**原因**: 大きなファイル（1000行以上）でタイムアウト（5秒）が発生

**解決**: タイムアウト時間を延長

```bash
# scripts/format_changed_file.sh を編集
readonly FORMATTER_TIMEOUT=10  # 5秒 → 10秒
```

## パフォーマンス

### 実行時間目安

| ファイルサイズ | フォーマット時間 | 備考 |
|--------------|----------------|------|
| 1-100行 | 0.5-1秒 | 最速 |
| 100-500行 | 1-2秒 | 通常 |
| 500-1000行 | 2-3秒 | 問題なし |
| 1000行以上 | 3-5秒 | タイムアウトリスク（5秒） |
| 5000行以上 | 5秒以上 | タイムアウト、除外推奨 |

### 並列実行時の動作

複数ファイルを並列でEdit/Writeした場合、各フォーマッタは並列実行されます（Claude Codeの制御下）。

**例**:
```markdown
# Claude Codeが3ファイルを同時にEdit
Edit(file_path="a.py")  # black/isort実行（2秒）
Edit(file_path="b.js")  # prettier実行（1秒）
Edit(file_path="c.md")  # prettier実行（1秒）

# 総実行時間 ≈ 2秒（最長のフォーマッタに依存）
```

## ベストプラクティス

### 1. プロジェクト開始時に設定統一

チーム全員が同じ設定ファイル（pyproject.toml, .prettierrc）を使用し、Gitで管理。

```bash
# 設定ファイルをコミット
git add pyproject.toml .prettierrc .prettierignore .claudeignore_format
git commit -m "Add code formatting configuration"
git push
```

### 2. 既存コードの一括フォーマット

新規プロジェクトまたは大規模リファクタリング時は、事前に一括フォーマット:

```bash
# Python
black .
isort .

# JavaScript/TypeScript/Markdown
npx prettier --write "**/*.{js,jsx,ts,tsx,md,json,yaml,yml,css,scss}"

# コミット
git add -A
git commit -m "Apply initial code formatting"
```

### 3. .claudeignore_formatの適切な管理

以下のファイルは除外を推奨:
- Legacy code（既存のフォーマットを維持）
- Auto-generated files（手動編集しない）
- Third-party vendored code（外部ライブラリ）
- Large data files（処理時間がかかる）

**例**:
```
# .claudeignore_format
Stock/programs/legacy_module/
scripts/auto_generated_*
vendor/
data/*.csv
```

### 4. CI/CDでのフォーマットチェック

PRマージ前にフォーマットチェックを実行（GitHub Actions等）:

```yaml
# .github/workflows/format-check.yml
name: Format Check
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Python formatters
        run: |
          pip install black==25.12.0 isort==7.0.0

      - name: Check Python formatting
        run: |
          black --check .
          isort --check .

      - name: Check JavaScript/TypeScript formatting
        run: npx prettier --check "**/*.{js,jsx,ts,tsx,md,json,yaml,yml,css,scss}"
```

### 5. フォーマット設定の段階的導入

既存プロジェクトへの導入時は段階的に:

1. **Week 1**: フォーマッタインストール、設定ファイル作成
2. **Week 2**: 新規ファイルのみ自動フォーマット有効
3. **Week 3**: 既存ファイルを段階的に一括フォーマット
4. **Week 4**: 全ファイルで自動フォーマット適用

## ファイル構成

| ファイルパス | 役割 | 編集頻度 |
|------------|------|---------|
| `~/.claude/settings.json` | PostToolUseフック設定 | 低（初回のみ） |
| `scripts/format_changed_file.sh` | フォーマット実行スクリプト（Bashフック） | 低（機能拡張時） |
| `scripts/setup_formatters.sh` | フォーマッタインストールスクリプト | 低（初回のみ） |
| `pyproject.toml` | black, isort 設定 | 中（プロジェクト要件に応じて） |
| `.prettierrc` | prettier 設定 | 中（プロジェクト要件に応じて） |
| `.prettierignore` | prettier 除外パターン | 中（除外ファイル追加時） |
| `.claudeignore_format` | 全フォーマッタ共通の除外ファイルリスト | 高（頻繁に追加） |
| `~/.claude/logs/format.log` | フォーマット実行ログ（オプション） | 読み取り専用 |

## フォーマッタの詳細

### black（Python）

**公式サイト**: https://black.readthedocs.io/

**特徴**:
- PEP 8準拠の自動フォーマッタ
- 設定項目が少なく、統一されたスタイル
- インデント: スペース4つ（変更不可）
- 「Uncompromising」哲学（妥協なし）

**主な設定項目**:
- `line-length`: 1行の最大文字数（デフォルト: 88、推奨: 100）
- `target-version`: Pythonバージョン（複数指定可）
- `extend-exclude`: 除外パターン（正規表現）

**実行例**:
```bash
# 標準実行
black script.py

# チェックのみ（変更なし）
black --check script.py

# 差分表示
black --check script.py --diff
```

### isort（Python import文）

**公式サイト**: https://pycqa.github.io/isort/

**特徴**:
- import文の自動ソート・グループ化
- blackとの互換性プロファイル提供
- セクション別グループ分け（STDLIB, THIRDPARTY, FIRSTPARTY等）

**主な設定項目**:
- `profile`: `"black"` を推奨（black互換）
- `line_length`: blackと同じ値に設定
- `sections`: import文のグループ分け順序
- `multi_line_output`: 複数行インポートの形式

**実行例**:
```bash
# 標準実行
isort script.py

# チェックのみ（変更なし）
isort --check-only script.py

# 差分表示
isort --check-only script.py --diff
```

### prettier（JavaScript/TypeScript/Markdown等）

**公式サイト**: https://prettier.io/

**特徴**:
- 複数言語対応（JS, TS, JSON, YAML, Markdown, CSS等）
- 設定項目が少なく、統一されたスタイル
- オピニオネイテッド（意見を持つ）フォーマッタ

**主な設定項目**:
- `printWidth`: 1行の最大文字数（デフォルト: 80、推奨: 100）
- `tabWidth`: インデント幅（デフォルト: 2）
- `semi`: セミコロンの有無（デフォルト: true）
- `singleQuote`: シングルクォート使用（デフォルト: false）
- `trailingComma`: 末尾カンマ挿入ルール

**実行例**:
```bash
# 標準実行（npx経由）
npx prettier --write script.js

# チェックのみ（変更なし）
npx prettier --check script.js

# 複数ファイル一括
npx prettier --write "**/*.{js,ts,md,json}"
```

## 更新履歴

- **2026-01-03**: Week 2実装完了（PostToolUseフック + 自動フォーマット）
  - フック設定追加（~/.claude/settings.json）
  - フォーマットスクリプト作成（format_changed_file.sh）
  - フォーマッタインストールスクリプト作成（setup_formatters.sh）
  - 設定ファイル作成（pyproject.toml, .prettierrc, .prettierignore, .claudeignore_format）
  - 使用ガイド作成（本ドキュメント）

- **2026-01-09**: ユーザーガイド更新
  - トラブルシューティング強化
  - ベストプラクティス追加
  - フォーマッタ詳細セクション追加

## チェックリスト

新規プロジェクトでの導入時に以下を確認:

- [ ] フォーマッタがインストールされているか？（`bash scripts/setup_formatters.sh`）
- [ ] PostToolUseフック設定が有効か？（`~/.claude/settings.json`）
- [ ] 設定ファイルがプロジェクトルートに存在するか？（`pyproject.toml`, `.prettierrc`）
- [ ] 除外ファイルを設定したか？（`.claudeignore_format`, `.prettierignore`）
- [ ] 既存コードを一括フォーマットしたか？（`black .`, `isort .`, `npx prettier --write`）
- [ ] CI/CDでフォーマットチェックを設定したか？（GitHub Actions等）
- [ ] チーム全員が同じ設定を使用しているか？（Git管理）

## 参照

- [Claude Code公式ドキュメント - Hooks](https://code.claude.com/docs/en/hooks)
- [black公式ドキュメント](https://black.readthedocs.io/)
- [isort公式ドキュメント](https://pycqa.github.io/isort/)
- [prettier公式ドキュメント](https://prettier.io/)
- @.claude/rules/execution_preference.md - LLM優先アプローチ
- @docs/implementation_guides/week2_code_formatting.md - 実装詳細
- @scripts/setup_formatters.sh - フォーマッタセットアップ
- @scripts/format_changed_file.sh - フォーマット実行ロジック
