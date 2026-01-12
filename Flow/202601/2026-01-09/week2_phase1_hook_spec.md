# Claude Code フック仕様書 - PostToolUse詳細ガイド

## 概要

**PostToolUse** は、ツール実行完了直後に自動実行されるフック。ツール結果の検査と Claude へのフィードバック提供が可能。

### 実行タイミング

```
Claude の指示 → ツール実行（完了） → PostToolUse フック実行 → 次のステップ
```

---

## 1. フック種類と違い

### フック種別

| フック名 | 実行タイミング | 用途 | 実行制御可 |
|----------|---------------|------|----------|
| **PostToolUse** | ツール成功直後 | 結果検査、フィードバック提供 | ⭕ 可能 |
| **PreToolUse** | ツール実行前 | 入力検証、実行許可制御 | ⭕ 可能 |
| **PostPrompt** | Claude 応答後 | 応答品質チェック | ⭕ 可能 |

### PostToolUse の特徴

- **ツール既実行**: フック実行時点でツールは既に完了している
- **検査のみ**: 結果を検査してフィードバック提供
- **結果確認**: `tool_response` で成功/失敗を確認可能

---

## 2. Matcher 構文

### 基本形式

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|Read",
        "hooks": [...]
      }
    ]
  }
}
```

### サポートされるツール

#### ネイティブツール

- `Write` - ファイル書き込み
- `Edit` - ファイル編集
- `Read` - ファイル読み取り
- `Bash` - シェルコマンド
- `Glob` - ファイルパターンマッチ
- `Grep` - コンテンツ検索
- `Task` - サブエージェント実行
- `WebFetch` - URL コンテンツ取得
- `WebSearch` - ウェブ検索
- `NotebookEdit` - Jupyter セル編集

#### MCP ツール

```json
{
  "matcher": "mcp__memory__.*",          // memory サーバーの全ツール
  "matcher": "mcp__filesystem__.*",      // filesystem サーバーの全ツール
  "matcher": "mcp__<server>__<tool>"     // 特定ツール
}
```

### マッチング例

```json
// 例1: 複数ツール
{
  "matcher": "Write|Edit|Read"
}

// 例2: 全ツール
{
  "matcher": ".*"
}

// 例3: MCP ツールのみ
{
  "matcher": "mcp__.*"
}

// 例4: 特定 MCP サーバー
{
  "matcher": "mcp__slack__.*"
}

// 例5: Bash と Edit
{
  "matcher": "Bash|Edit"
}
```

---

## 3. フック入力スキーマ

### stdin で受け取る JSON 構造

```json
{
  "session_id": "abc123def456",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/Users/user/project/file.py",
    "content": "def hello():\n    print('world')"
  },
  "tool_response": {
    "filePath": "/Users/user/project/file.py",
    "success": true
  },
  "tool_use_id": "toolu_01ABC123DEF456..."
}
```

### 主要フィールド

| フィールド | 型 | 説明 |
|-----------|-----|------|
| `session_id` | string | セッション識別子 |
| `tool_name` | string | 実行されたツール名（Write, Edit, Bash等） |
| `tool_input` | object | ツール実行時の入力パラメータ |
| `tool_response` | object | ツールの実行結果 |
| `tool_use_id` | string | ツール使用の一意識別子 |
| `cwd` | string | 現在の作業ディレクトリ |

---

## 4. 利用可能な変数

### stdin データの変数

```python
import json
import sys

input_data = json.load(sys.stdin)

# 主要変数
session_id = input_data["session_id"]
tool_name = input_data["tool_name"]
tool_input = input_data["tool_input"]
tool_response = input_data["tool_response"]
cwd = input_data["cwd"]
```

### ツール別の tool_input 変数

#### Write ツール
```python
file_path = tool_input.get("file_path")
content = tool_input.get("content")
```

#### Edit ツール
```python
file_path = tool_input.get("file_path")
old_string = tool_input.get("old_string")
new_string = tool_input.get("new_string")
```

#### Bash ツール
```python
command = tool_input.get("command")
```

#### Grep ツール
```python
pattern = tool_input.get("pattern")
path = tool_input.get("path")
```

### 環境変数

```bash
# フック実行環境で利用可能
CLAUDE_PROJECT_DIR  # プロジェクトルート（絶対パス）
CLAUDE_CODE_REMOTE  # "true" = Web環境, "false" = デスクトップ

# 標準シェル変数も利用可
$HOME, $USER, $PWD 等
```

---

## 5. フック出力と決定制御

### Exit Code による制御

| Exit Code | 動作 | 用途 |
|-----------|------|------|
| **0** | 成功、続行 | 正常完了（JSON 出力可） |
| **1** | 警告（詳細モード） | 非ブロッキングエラー |
| **2** | 実行をブロック | クリティカルエラー |

### 出力フォーマット（Exit Code 0）

```python
import json
import sys

output = {
    "decision": "block" | None,  # "block" で Claude に再プロンプト
    "reason": "理由の説明",
    "suppressOutput": False,      # true で stdout をトランスクリプト非表示
    "systemMessage": "警告メッセージ",
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "Claude に提供する追加情報"
    }
}

print(json.dumps(output))
sys.exit(0)
```

### Decision フィールド動作

#### `"block"` - ブロック & 再プロンプト

```python
{
    "decision": "block",
    "reason": "Code style issues detected:\n- Line 5: missing docstring\n- Line 12: too long (105 > 100 chars)"
}
```

→ Claude に「Code style issues detected...」を理由として提示
→ Claude が問題に対応するよう指示される

#### `undefined/None` - ブロックなし

```python
{
    "decision": None  # または JSON に "decision" フィールド自体を含めない
}
```

→ 実行継続、Claude に通知なし

### ブロッキングエラー（Exit Code 2）

```bash
#!/bin/bash
echo "Critical error: File exceeds 50MB limit" >&2
exit 2  # stderr がClaude に表示される
```

### 追加コンテキスト提供（Exit Code 0）

```python
{
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "File passed linting (pylint: 9.5/10)"
    }
}
```

→ Claude がこの情報をコンテキストに含める

---

## 6. タイムアウト設定

### 設定方法

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/validate.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### タイムアウト仕様

| 項目 | 値 |
|------|-----|
| **デフォルト** | 60 秒 |
| **最小** | 1 秒 |
| **最大** | 推奨 300 秒（5分） |
| **タイムアウト時の挙動** | フックをスキップ、ツール実行は継続 |

### 複数フック時の並列化

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/linter.py",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "/path/to/security-check.py",
            "timeout": 20
          }
        ]
      }
    ]
  }
}
```

**実行時間**: max(30秒, 20秒) = 30秒
→ 複数フックは並列実行、総時間は最長フックの時間

---

## 7. エラーハンドリング

### パターン1: 検証失敗時のブロック

```python
#!/usr/bin/env python3
import json
import sys
import subprocess

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Invalid input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name")
tool_response = input_data.get("tool_response", {})

if tool_name == "Write" and tool_response.get("success"):
    file_path = tool_response.get("filePath", "")

    # pylint チェック
    result = subprocess.run(
        ["pylint", "--score=y", file_path],
        capture_output=True,
        text=True,
        timeout=20
    )

    if result.returncode != 0:
        output = {
            "decision": "block",
            "reason": f"Style violations:\n{result.stdout[:500]}"
        }
        print(json.dumps(output))
        sys.exit(0)

sys.exit(0)
```

### パターン2: 警告メッセージ表示

```bash
#!/bin/bash

HOOK_INPUT=$(cat)
FILE_PATH=$(echo "$HOOK_INPUT" | jq -r '.tool_response.filePath')

if [ -f "$FILE_PATH" ]; then
    SIZE=$(stat -f%z "$FILE_PATH" 2>/dev/null || stat -c%s "$FILE_PATH")
    THRESHOLD=$((5 * 1024 * 1024))  # 5MB

    if [ "$SIZE" -gt "$THRESHOLD" ]; then
        OUTPUT=$(cat <<EOF
{
  "systemMessage": "⚠️ Warning: Large file created ($(($SIZE / 1024 / 1024))MB)",
  "suppressOutput": false
}
EOF
)
        echo "$OUTPUT"
    fi
fi

exit 0
```

### パターン3: タイムアウト処理

```python
#!/usr/bin/env python3
import json
import sys
import subprocess

input_data = json.load(sys.stdin)

try:
    # 15秒のタイムアウト付き外部スクリプト実行
    result = subprocess.run(
        ["python", "/path/to/heavy_analysis.py"],
        input=json.dumps(input_data),
        capture_output=True,
        text=True,
        timeout=15
    )

    if result.returncode == 0:
        output = json.loads(result.stdout)
    else:
        output = {
            "decision": "block",
            "reason": f"Validation failed:\n{result.stderr}"
        }

    print(json.dumps(output))
    sys.exit(0)

except subprocess.TimeoutExpired:
    # タイムアウト時は警告のみ
    output = {
        "systemMessage": "⏱️ Validation timeout, skipping detailed check"
    }
    print(json.dumps(output))
    sys.exit(0)

except Exception as e:
    print(f"Hook execution error: {e}", file=sys.stderr)
    sys.exit(1)
```

### パターン4: クリティカルエラーでブロック

```bash
#!/bin/bash

HOOK_INPUT=$(cat)
FILE_PATH=$(echo "$HOOK_INPUT" | jq -r '.tool_response.filePath')

# セキュリティチェック: config ファイルに認証情報がないか確認
if grep -q "API_KEY\|PASSWORD\|SECRET" "$FILE_PATH" 2>/dev/null; then
    echo "CRITICAL: Credentials found in file" >&2
    exit 2  # ブロッキングエラー、stderr が Claude に表示される
fi

exit 0
```

---

## 8. 実践的なコード例

### 例1: Python コード品質チェック

```python
#!/usr/bin/env python3
"""
PostToolUse フック: Python ファイルの品質チェック
- Pylint でスタイルをチェック
- isort でインポート順序をチェック
- Black でフォーマットをチェック
"""
import json
import sys
import subprocess
from pathlib import Path

def check_python_file(file_path: str) -> dict:
    """Python ファイルの品質をチェック"""

    if not file_path.endswith(".py"):
        return {"decision": None}

    errors = []

    # Pylint チェック
    try:
        result = subprocess.run(
            ["pylint", "--disable=all", "--enable=E,F", file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            errors.append(f"Pylint errors:\n{result.stdout[:300]}")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # isort チェック
    try:
        result = subprocess.run(
            ["isort", "--check-only", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            errors.append("Import order issues (run: isort <file>)")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    if errors:
        return {
            "decision": "block",
            "reason": "\n".join(errors)
        }

    return {
        "decision": None,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "✅ File passed quality checks"
        }
    }

def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(1)

    tool_name = input_data.get("tool_name")
    tool_response = input_data.get("tool_response", {})

    if tool_name in ["Write", "Edit"] and tool_response.get("success"):
        file_path = tool_response.get("filePath")
        result = check_python_file(file_path)
        print(json.dumps(result))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 例2: ファイルサイズと複雑度チェック

```bash
#!/bin/bash
"""
PostToolUse フック: ファイルサイズと複雑度チェック
- ファイルサイズ > 500行 で警告
- サイクロマティック複雑度 > 15 でブロック
"""

HOOK_INPUT=$(cat)
TOOL_NAME=$(echo "$HOOK_INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$HOOK_INPUT" | jq -r '.tool_response.filePath')

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

if [ ! -f "$FILE_PATH" ]; then
    exit 0
fi

# ファイルサイズチェック
LINE_COUNT=$(wc -l < "$FILE_PATH" | tr -d ' ')

if [ "$LINE_COUNT" -gt 500 ]; then
    JSON_OUTPUT=$(cat <<EOF
{
  "systemMessage": "⚠️ Large file: $LINE_COUNT lines (consider splitting into modules)",
  "suppressOutput": false
}
EOF
)
    echo "$JSON_OUTPUT"
fi

# Python ファイルの複雑度チェック
if [[ "$FILE_PATH" == *.py ]]; then
    if command -v radon &> /dev/null; then
        COMPLEXITY=$(radon cc "$FILE_PATH" -a | grep -oE "[A-F]" | tail -1)

        if [[ "$COMPLEXITY" == "F" ]]; then
            echo "File has excessive complexity (Grade F)" >&2
            exit 2
        fi
    fi
fi

exit 0
```

### 例3: セキュリティチェック（認証情報検出）

```python
#!/usr/bin/env python3
"""
PostToolUse フック: セキュリティチェック
- 認証情報（API キー、パスワード）の誤入力を検出
- .env ファイルに認証情報を含めないかチェック
"""
import json
import sys
import re
from pathlib import Path

# 検出対象のパターン
SECRETS_PATTERNS = [
    r"(?i)(api[_-]?key|password|secret|token|auth)\s*[=:]\s*['\"]?[a-zA-Z0-9]{20,}",
    r"(?i)bearer\s+[a-zA-Z0-9\-._~+/]+=*",
    r"(?i)aws[_-]?(access[_-]?key|secret[_-]?access[_-]?key)\s*[=:]\s*",
]

def check_for_secrets(file_path: str, content: str) -> dict:
    """ファイルに認証情報が含まれていないかチェック"""

    # ソースコードのみチェック（バイナリは除外）
    if not any(file_path.endswith(ext) for ext in ['.py', '.js', '.json', '.yaml', '.yml', '.env']):
        return {"decision": None}

    detected_secrets = []

    for i, line in enumerate(content.split('\n'), 1):
        for pattern in SECRETS_PATTERNS:
            if re.search(pattern, line):
                detected_secrets.append({
                    "line": i,
                    "pattern": pattern[:40] + "..."
                })

    if detected_secrets:
        # .env ファイルは許可（本番環境では別途チェック）
        if not file_path.endswith('.env'):
            reason = f"Potential secrets detected in {len(detected_secrets)} line(s):\n"
            for secret in detected_secrets[:3]:
                reason += f"  Line {secret['line']}: Check for hardcoded credentials\n"

            return {
                "decision": "block",
                "reason": reason
            }

    return {"decision": None}

def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(1)

    tool_name = input_data.get("tool_name")
    tool_input = input_data.get("tool_input", {})
    tool_response = input_data.get("tool_response", {})

    if tool_name in ["Write", "Edit"] and tool_response.get("success"):
        file_path = tool_response.get("filePath", "")
        content = tool_input.get("content", "") or tool_input.get("new_string", "")

        result = check_for_secrets(file_path, content)
        print(json.dumps(result))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

---

## 9. 設定例

### claude.json 設定例

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python /path/to/hooks/code_quality.py",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "bash /path/to/hooks/security_check.sh",
            "timeout": 20
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python /path/to/hooks/bash_analyzer.py",
            "timeout": 15
          }
        ]
      },
      {
        "matcher": "mcp__.*",
        "hooks": [
          {
            "type": "command",
            "command": "python /path/to/hooks/mcp_logger.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

---

## 10. セキュリティ考慮事項

### 推奨プラクティス

1. **入力検証**
   ```python
   # ❌ 危険
   subprocess.run(f"cat {file_path}")

   # ✅ 安全
   subprocess.run(["cat", file_path])
   ```

2. **パストラバーサル検対**
   ```python
   from pathlib import Path

   file_path = Path(input_data["tool_response"]["filePath"]).resolve()
   base_dir = Path(os.environ["CLAUDE_PROJECT_DIR"]).resolve()

   # ファイルが project_dir 内か確認
   assert file_path.is_relative_to(base_dir)
   ```

3. **タイムアウト設定**
   ```python
   subprocess.run(cmd, timeout=20)  # 必ず設定
   ```

4. **シェル変数の安全性**
   ```bash
   # ❌ 危険
   eval "$user_input"

   # ✅ 安全
   subprocess.run([cmd, arg], shell=False)
   ```

5. **機密情報の非表示**
   ```python
   {
       "decision": "block",
       "reason": "Contains sensitive data",
       "suppressOutput": True  # stdout を非表示
   }
   ```

---

## 11. デバッグ方法

### デバッグモード有効化

```bash
claude --debug
```

### フック実行ログ確認

```bash
# 詳細モード（Ctrl+O）でフック実行情報表示
# - フック実行時間
# - Exit code
# - stdout/stderr
```

### ローカルテスト

```bash
# フック入力のモック
cat > test_input.json <<EOF
{
  "session_id": "test",
  "tool_name": "Write",
  "tool_input": {"file_path": "test.py", "content": "def foo(): pass"},
  "tool_response": {"filePath": "test.py", "success": true}
}
EOF

# フック実行テスト
cat test_input.json | python /path/to/hook_script.py
```

---

## 12. 既知の制限事項

| 制限事項 | 説明 | 回避策 |
|---------|------|--------|
| **ツール既実行** | PostToolUse はツール実行後のため、ツール実行自体を防止できない | PreToolUse を使用 |
| **タイムアウト固定** | フックタイムアウト中にツール実行は継続 | 非ブロッキング警告を使用 |
| **stdin/stdout 限定** | ファイル I/O での結果返却不可 | JSON stdout で結果返却 |
| **複数ツールの同時検証** | 1つのフック = 1つのツールマッチ | matcher で複数ツール指定 |

---

## 参照

- **公式ドキュメント**: https://code.claude.com/docs/en/hooks
- **Claude Code CLI**: `claude --help`
- **フック実行環境**: $CLAUDE_PROJECT_DIR で project root アクセス可

---

## 次のステップ（Week 2 実装予定）

1. **orchestrate-review-loop での PostToolUse 統合**
   - SubAgent 出力の自動検証フック
   - quality_score.json の事前検証

2. **フック出力の logger 統合**
   - フック実行ログを Flow に自動保存
   - evidence_dir への履歴記録

3. **並列フック実行の最適化**
   - 複数フックのタイムアウト調整
   - エラーハンドリングパターン確立
