# コードフォーマッター選定ガイド

**作成日**: 2026-01-09
**対象**: aipm_v0 プロジェクト
**フェーズ**: Week 2（実装準備）

---

## エグゼクティブサマリー

本プロジェクト向けの推奨フォーマッター構成：

| 言語 | 推奨ツール | 副次ツール | 理由 |
|------|----------|----------|------|
| **Python** | Black | isort | 無条件フォーマット + 標準化, インポート整理 |
| **JavaScript/TypeScript** | Prettier | ESLint | 包括的フォーマット + コード品質チェック |
| **Markdown** | Prettier | markdownlint | 統一フォーマット + スタイルチェック |
| **JSON/YAML** | Prettier | - | 統一フォーマット |

**推奨インストール方法**: Homebrew (macOS) / npm (JavaScript系) / pip (Python)

---

## 各言語別 詳細分析

### 1. Python フォーマッター比較

#### Black （推奨）

**特徴**:
- 「無条件（uncompromising）」なフォーマッター
- 設定項目を最小限に抑え、一貫性を優先
- ダブルクォート使用（文字列内にダブルクォートがある場合はシングルクォート）
- 2025年安定スタイル導入で Unicode エスケープ正規化

**パフォーマンス**: 大規模コードベースにも対応

**インストール**:
```bash
# pip での インストール
pip install black==25.12.0

# Homebrew での インストール (macOS)
brew install black
```

**設定例** (`pyproject.toml`):
```toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # ディレクトリ・ファイルを除外
  \.git
  | \.venv
  | venv
  | node_modules
  | build
  | dist
  | \.mypy_cache
  | \.pytest_cache
  | __pycache__
)/
'''
```

**設定ポイント**:
- `line-length`: デフォルト88文字（推奨：保持）
- `target-version`: サポート対象Python バージョン指定
- `extend-exclude`: 正規表現でファイル除外（シングルクォート使用）

---

#### autopep8

**特徴**:
- PEP 8 ガイドライン準拠
- フォーマット範囲を細かく制御可能
- 最小限のフォーマット処理（Black より保守的）
- 段階的な採用に向く

**パフォーマンス**: Black と同等以上

**インストール**:
```bash
pip install autopep8
```

**設定例** (`.style.yapf` または `setup.cfg`):
```ini
[pep8]
max-line-length = 100
ignore = E501,W503
```

**Black との比較**:
- Black: 無条件フォーマット
- autopep8: カスタマイズ重視

→ **プロジェクト向けには Black が推奨**（統一性重視）

---

#### YAPF (Yet Another Python Formatter)

**特徴**:
- Google 製
- PEP 8 違反のみならず、スタイル不統一も修正
- 3 種類のプリセット（pep8, google, chromium）
- 柔軟な設定

**パフォーマンス**: 速い

**インストール**:
```bash
pip install yapf
```

**Black との比較**: YAPF はより設定可能だが、プロジェクトでは Black の「無条件」アプローチが統一性に優れている

---

#### isort （推奨：副次ツール）

**役割**: Python インポートの自動整理

**特徴**:
- Black と完全互換
- インポートを論理グループに分類
  - 標準ライブラリ
  - サードパーティ
  - ローカルプロジェクト

**インストール**:
```bash
pip install isort
```

**設定例** (`pyproject.toml`):
```toml
[tool.isort]
profile = "black"
line_length = 88
multi_line_mode = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
skip_glob = ["*/migrations/*", "venv/*"]
```

**Black との連携**:
```bash
# isort → Black の順で実行
isort .
black .
```

---

### 2. JavaScript/TypeScript フォーマッター比較

#### Prettier （推奨）

**特徴**:
- 一般的なコードフォーマッター
- JavaScript, TypeScript, CSS, HTML, JSON, Markdown 対応
- Black の JavaScript 版に相当
- ESLint と組み合わせる

**パフォーマンス**: 高速

**インストール**:
```bash
# npm
npm install --save-dev prettier

# Homebrew (macOS)
brew install prettier

# yarn
yarn add --dev prettier
```

**設定例** (`.prettierrc`):
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "avoid",
  "bracketSpacing": true,
  "endOfLine": "lf"
}
```

**または YAML** (`.prettierrc.yaml`):
```yaml
semi: true
trailingComma: es5
singleQuote: true
printWidth: 100
tabWidth: 2
useTabs: false
arrowParens: avoid
bracketSpacing: true
endOfLine: lf
```

**除外設定** (`.prettierignore`):
```
node_modules/
.next/
dist/
build/
coverage/
*.lock
.DS_Store
```

---

#### ESLint （補完ツール）

**役割**: コード品質チェック（フォーマットではなく）

**特徴**:
- バグ検出、ベストプラクティス強制
- Prettier とは異なる責務
- 2020 年以降、フォーマット規則から撤退

**インストール**:
```bash
npm install --save-dev eslint
```

**Prettier との連携**:
```bash
npm install --save-dev eslint-config-prettier
```

**設定例** (`.eslintrc.json`):
```json
{
  "extends": [
    "eslint:recommended",
    "prettier"
  ],
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  },
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  }
}
```

**関連パッケージ**:
- `eslint-config-prettier`: ESLint フォーマット規則を無効化
- `eslint-plugin-prettier`: Prettier をESLint プラグインとして実行（オプション）

---

#### Deno fmt （参考情報）

**特徴**:
- Deno ランタイムに統合
- Black 相当の「無条件」フォーマッター
- 設定ほぼ不要

**使用**: Deno プロジェクトの場合のみ

---

### 3. Markdown フォーマッター比較

#### Prettier （推奨）

**特徴**:
- Markdown の自動フォーマット
- コード例のフォーマット対応
- markdownlint との共存可能

**インストール**: JavaScript セクション参照

**設定例** (`.prettierrc` に追加):
```json
{
  "proseWrap": "preserve",
  "markdownLineBreaks": "auto"
}
```

---

#### markdownlint （推奨：副次ツール）

**役割**: Markdown スタイルチェック（linting）

**特徴**:
- 60+ ルール
- Prettier との競合を回避可能
- vs Code 拡張機能あり

**インストール**:
```bash
npm install --save-dev markdownlint-cli
```

**設定例** (`.markdownlint.json`):
```json
{
  "extends": "markdownlint/style/prettier",
  "MD013": false,
  "MD033": false
}
```

**Prettier との共存**:
`extends: "markdownlint/style/prettier"` で競合を自動解決

---

### 4. JSON/YAML フォーマッター比較

#### Prettier （推奨）

**特徴**:
- JSON, YAML 両対応
- 一貫性を保証
- 複数言語フォーマッターを統一可能

**設定例** (`.prettierrc` に追加):
```json
{
  "printWidth": 100,
  "tabWidth": 2
}
```

---

#### jq （JSON 処理用、補完ツール）

**役割**: JSON の変換・フィルタリング（フォーマットではなく処理）

**特徴**:
- C 言語実装で高速
- 複雑な JSON 処理
- ストリーミング対応

**インストール**:
```bash
# Homebrew (macOS)
brew install jq

# Ubuntu
sudo apt-get install jq
```

**使用例**:
```bash
# pretty-print
jq . input.json

# フィルター処理
jq '.users[] | select(.age > 30)' input.json
```

---

## プロジェクト推奨構成

### インストールコマンド一覧

#### Python フォーマッター
```bash
# 方法1: pip
pip install black==25.12.0 isort

# 方法2: Homebrew (macOS)
brew install black
pip install isort
```

#### JavaScript/TypeScript フォーマッター
```bash
npm install --save-dev prettier eslint eslint-config-prettier
```

#### Markdown/JSON/YAML フォーマッター
```bash
npm install --save-dev prettier markdownlint-cli
```

#### その他ユーティリティ
```bash
# macOS
brew install jq
```

---

### 設定ファイル構成

プロジェクトルート（`/Users/yuichi/AIPM/aipm_v0/`) に以下を配置：

#### `pyproject.toml` (Python 設定)

```toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.git
  | \.venv
  | venv
  | node_modules
  | build
  | dist
  | \.mypy_cache
  | \.pytest_cache
  | __pycache__
  | Flow
  | Archived
  | Stock/SNS_Knowledge
)/
'''

[tool.isort]
profile = "black"
line_length = 88
multi_line_mode = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
skip_glob = ["*/migrations/*", "venv/*", "Stock/SNS_Knowledge/*"]
```

#### `.prettierrc.json` (JavaScript/TypeScript/Markdown/JSON/YAML 設定)

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "avoid",
  "bracketSpacing": true,
  "endOfLine": "lf",
  "proseWrap": "preserve"
}
```

#### `.prettierignore` (除外設定)

```
# Dependencies
node_modules/
.venv/
venv/
env/
vendor/

# Build artifacts
dist/
build/
out/
target/
*.min.js
*.min.css
coverage/
htmlcov/

# Logs and caches
*.log
*.cache
__pycache__/
.pytest_cache/
.mypy_cache/
.tox/

# Project-specific
Flow/
Archived/
Stock/SNS_Knowledge/
.DS_Store

# Lock files and environment
*.lock
.env
.env.local

# Media files
*.png
*.jpg
*.jpeg
*.gif
*.mp4
*.mov
```

#### `.markdownlint.json` (Markdown linting 設定)

```json
{
  "extends": "markdownlint/style/prettier",
  "MD013": false,
  "MD033": false,
  "MD034": false,
  "no-hard-tabs": false
}
```

#### `.eslintrc.json` (JavaScript/TypeScript linting 設定)

```json
{
  "extends": [
    "eslint:recommended",
    "prettier"
  ],
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  },
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  },
  "rules": {
    "no-unused-vars": [
      "warn",
      {
        "argsIgnorePattern": "^_"
      }
    ]
  }
}
```

---

## 使用方法

### コマンドライン実行

#### Python コード
```bash
# Black でフォーマット
black .

# isort でインポート整理
isort .

# 両方を実行（推奨）
isort . && black .

# 特定ディレクトリ
black src/
isort src/
```

#### JavaScript/TypeScript/JSON/YAML/Markdown
```bash
# Prettier でフォーマット
prettier --write .

# 特定ファイル
prettier --write src/**/*.ts

# 確認のみ（フォーマットしない）
prettier --check .
```

#### Markdown linting
```bash
# マークダウンチェック
markdownlint-cli2 '**/*.md'

# 自動修正（対応する場合）
markdownlint-cli2 --fix '**/*.md'
```

#### ESLint
```bash
# コード品質チェック
eslint .

# 自動修正（可能な場合）
eslint --fix .
```

---

### IDE 統合（VS Code）

#### 推奨拡張機能

1. **Prettier - Code formatter**
   - ID: `esbenp.prettier-vscode`
   - 機能: JavaScript/TypeScript/JSON/Markdown/YAML 自動フォーマット

2. **Python**
   - ID: `ms-python.python`
   - 機能: Black, isort 統合

3. **markdownlint**
   - ID: `DavidAnson.vscode-markdownlint`
   - 機能: Markdown linting（リアルタイム）

4. **ESLint**
   - ID: `dbaeumer.vscode-eslint`
   - 機能: JavaScript/TypeScript linting（リアルタイム）

#### 設定例 (`.vscode/settings.json`)

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python",
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },
  "[javascript]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[yaml]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "[jsonc]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

---

## パフォーマンス比較

### 実行速度（相対値）

| フォーマッター | 相対速度 | 用途 |
|-------------|---------|------|
| Black | 100% | 基準値 |
| autopep8 | 95-110% | Black 並み |
| YAPF | 90-105% | Black 並み |
| Prettier | 100% | 基準値 |
| ESLint + Prettier | 150-200% | linting 含むため遅い |
| jq | 50-80% | 高速（処理に特化） |

**推奨**: 開発中は linting 無効化、CI/CD で実行

---

## 除外戦略

### プロジェクト固有

本プロジェクトでは以下を除外：

1. **大容量データ**
   - `Stock/SNS_Knowledge/` - Markdown 事例が多数、フォーマット不要

2. **自動生成ファイル**
   - `build/`, `dist/`, `__pycache__/`

3. **バージョン管理外**
   - `node_modules/`, `.venv/`, `venv/`

4. **ロック ファイル**
   - `*.lock`, `package-lock.json`

5. **環境設定**
   - `.env`, `.env.local`

---

## トラブルシューティング

### Black と isort の競合

**問題**: isort と Black のインポート整理が異なる場合

**解決策**:
```bash
# isort --profile=black を使用（設定ファイルで既に指定）
isort --profile=black .

# その後 Black 実行
black .
```

---

### Prettier と markdownlint の競合

**問題**: markdownlint ルールが Prettier フォーマットに違反

**解決策**:
```json
{
  "extends": "markdownlint/style/prettier"
}
```

---

### ESLint と Prettier の競合

**問題**: ESLint フォーマット規則が Prettier 出力と競合

**解決策**:
```json
{
  "extends": [
    "eslint:recommended",
    "prettier"
  ]
}
```

`eslint-config-prettier` を最後に追加（Prettier ルール優先）

---

## 次のステップ

### Week 2 実装計画

1. **プロジェクトルートに設定ファイル配置**
   - `pyproject.toml`, `.prettierrc.json`, `.markdownlint.json`, `.eslintrc.json`

2. **インストール実行**
   ```bash
   # Python
   pip install black==25.12.0 isort

   # JavaScript/TypeScript
   npm install --save-dev prettier eslint eslint-config-prettier markdownlint-cli

   # ユーティリティ
   brew install jq
   ```

3. **IDE 拡張機能インストール**
   - VS Code: Prettier, Python, markdownlint, ESLint

4. **フォーマット実行テスト**
   ```bash
   # Python
   isort . && black .

   # JavaScript/TypeScript/その他
   prettier --write .

   # Markdown
   markdownlint-cli2 '**/*.md'
   ```

5. **CI/CD 統合準備**
   - GitHub Actions で自動フォーマットチェック

---

## 参考資料

### Python

- [Black 25.12.0 Documentation](https://black.readthedocs.io/en/stable/)
- [isort Documentation](https://pycqa.github.io/isort/)
- [awesome-python-code-formatters](https://github.com/life4/awesome-python-code-formatters)
- 関連記事:
  - [A quick performance comparison of Python code formatters](https://medium.com/@boxed/a-quick-performance-comparison-of-python-code-formatters-3a89478da8b8)
  - [The 3 best auto formatters for Python](https://www.kevinpeters.net/auto-formatters-for-python)
  - [Python code formatters comparison: Black, autopep8 and YAPF](https://blog.frank-mich.com/python-code-formatters-comparison-black-autopep8-and-yapf/)

### JavaScript/TypeScript

- [Prettier Documentation](https://prettier.io/docs/)
- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)
- [Deno Documentation - Linting and Formatting](https://docs.deno.com/runtime/fundamentals/linting_and_formatting/)
- 関連記事:
  - [Prettier vs ESLint: Choosing the Right Tool](https://betterstack.com/community/guides/scaling-nodejs/prettier-vs-eslint/)
  - [Setting Up ESLint and Prettier for a TypeScript Project](https://medium.com/@robinviktorsson/setting-up-eslint-and-prettier-for-a-typescript-project-aa2434417b8f)
  - [How to use Prettier with ESLint and TypeScript in VSCode](https://khalilstemmler.com/blogs/tooling/prettier/)

### Markdown

- [markdownlint Documentation](https://github.com/DavidAnson/markdownlint)
- [Prettier Markdown Support](https://prettier.io/docs/options#markdown)
- 関連記事:
  - [Configuring Markdownlint Alongside Prettier](https://www.joshuakgoldberg.com/blog/configuring-markdownlint-alongside-prettier/)
  - [markdownlint/doc/Prettier.md](https://github.com/DavidAnson/markdownlint/blob/main/doc/Prettier.md)

### JSON/YAML

- [Prettier - Ignoring Code](https://prettier.io/docs/ignore.html)
- [jq Manual](https://stedolan.github.io/jq/manual/)
- 関連記事:
  - [Pretty-print JSON with jq](https://lornajane.net/posts/2024/pretty-print-json-with-jq)
  - [How To Transform JSON Data with jq](https://www.digitalocean.com/community/tutorials/how-to-transform-json-data-with-jq)

---

## 版履歴

| バージョン | 日付 | 更新内容 |
|----------|------|--------|
| v1.0 | 2026-01-09 | 初版作成 |

---

**作成者**: Claude Code
**対象プロジェクト**: aipm_v0
**参照**: @CLAUDE.md, @docs/ai/overview.md
