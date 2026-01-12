---
name: test-bash-execution
description: |
  Bashツール経由でPythonスクリプト実行をテストする検証用スキル。
  Claude Code skillsがBash toolを使ってPythonコードを実行できるか確認します。
trigger_keywords:
  - "Bash実行テスト"
  - "Python実行検証"
  - "スキルBashテスト"
stage: Verification
dependencies: []
output_file: Flow/202512/2025-12-30/bash_execution_test_result.md
execution_time: 1-2分
priority: P0
---

# Test Bash Execution Skill

Bash/Python実行可能性検証用スキル

---

## このSkillでできること

Claude Code skillsがBash toolを使ってPythonスクリプトを実行できるか検証します。

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 1-2分

### STEP 1: 簡単なPythonコマンド実行テスト（30秒）

**Bashツール使用**:
```bash
python3 -c "print('Hello from Python within Skill')"
```

**期待出力**: "Hello from Python within Skill"

**検証ポイント**:
- ✅ Bashツールが正常に実行される
- ✅ Python 3が利用可能
- ✅ 出力が取得できる

---

### STEP 2: Pythonファイル実行テスト（30秒）

**Bashツール使用**:
```bash
python3 /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/src/test_script.py
```

**期待出力**:
```
============================================================
BASH EXECUTION TEST - SUCCESS
============================================================
Python version: 3.x.x
Platform: ...
Python executable: ...
============================================================
✅ File execution successful
✅ Claude Code skills CAN execute Python scripts via Bash
```

**検証ポイント**:
- ✅ Pythonファイルが実行される
- ✅ sys, platform モジュールが利用可能
- ✅ 複数行の出力が取得できる

---

### STEP 3: ライブラリimportテスト（30秒）

**Bashツール使用**:
```bash
python3 -c "
import sys
print('✅ sys module OK')

try:
    import numpy as np
    print('✅ numpy available')
except ImportError:
    print('❌ numpy not available')

try:
    import pandas as pd
    print('✅ pandas available')
except ImportError:
    print('❌ pandas not available')

try:
    import yfinance as yf
    print('✅ yfinance available')
except ImportError:
    print('❌ yfinance not available')
"
```

**検証ポイント**:
- numpy, pandas, yfinance の availability確認
- Trading Agent実装に必要なライブラリが使えるか

---

### STEP 4: 結果レポート生成（30秒）

検証結果を以下の判定基準で評価します：

| 検証項目 | 成功 | 部分成功 | 失敗 |
|---------|------|---------|------|
| python3 -c 実行 | ✅ 出力取得 | ⚠️ エラーだが実行可 | ❌ 実行不可 |
| .pyファイル実行 | ✅ 出力取得 | ⚠️ 一部制限あり | ❌ 実行不可 |
| import numpy/pandas | ✅ import成功 | - | ❌ import失敗 |
| **最終判定** | **分岐A選択** | **分岐C選択** | **分岐B選択** |

**判定結果**:
- **分岐A（成功）**: Python実装アプローチ（オプションA）を選択可能
- **分岐B（失敗）**: LLM推論アプローチ（オプションB）必須
- **分岐C（部分成功）**: ハイブリッドアプローチを検討

**Writeツールで結果出力**:
- パス: `Flow/202512/2025-12-30/bash_execution_test_result.md`
- 内容: STEP 1-3の出力結果 + 最終判定

---

## 成果物フォーマット

**bash_execution_test_result.md**:
```markdown
# Bash/Python実行検証結果

検証日時: 2025-12-30

## STEP 1: python3 -c 実行
[実行結果]

## STEP 2: .pyファイル実行
[実行結果]

## STEP 3: ライブラリimport
[実行結果]

## 最終判定
- python3 -c: [成功/失敗]
- .pyファイル実行: [成功/失敗]
- numpy/pandas: [利用可能/利用不可]

**推奨アプローチ**: [分岐A/B/C]

## 次のアクション
[Phase 3で採用するアプローチ]
```

---

## 使用例

```
User: Bash実行テスト
```

システムが自動的に：
1. python3 -c でシンプルなコマンド実行
2. test_script.py ファイル実行
3. numpy/pandas import確認
4. 結果レポート生成
5. 推奨アプローチ決定

---

## 更新履歴

- 2025-12-30: 検証用スキル作成（Phase 1-5）
