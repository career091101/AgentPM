# Claude Code 既存フック設定調査レポート

**実施日**: 2026-01-09  
**対象**: ~/.claude/settings.json と .claude/project-settings.json  
**目的**: Week 2 Phase 1で新規追加予定の PostToolUse フックと既存フックの競合チェック

---

## 1. 既存フック設定概要

### 1.1 settings.json (ユーザー全体設定)

```json
{
  "permissions": {
    "allow": [
      "Bash(grep:*)", "Bash(find:*)", "Bash(ls:*)", "Bash(cat:*)",
      "Bash(git add:*)", "Bash(git commit:*)", "Bash(git push:*)",
      "Bash(git config:*)", "Bash(git gc:*)", "Bash(ssh:*)",
      "Bash(gh auth status:*)", "Bash(git fetch:*)", "Bash(git rev-list:*)",
      "Bash(git cat-file:*)", "Bash(git worktree:*)", "Bash(git branch:*)",
      "Bash(git log:*)", "Bash(git status:*)", "Bash(git diff:*)",
      "Bash(sort:*)", "Bash(git lfs version:*)", "Bash(brew install:*)",
      "Bash(git lfs install:*)", "Bash(git lfs migrate:*)",
      "Bash(git stash:*)", "Bash(git reset:*)", "Bash(python3:*)",
      "Bash(npm install:*)", "Bash(npm run lint:*)", "Bash(npm test:*)",
      "Bash(tmux:*)", "Bash(ps:*)", "Bash(kill:*)", "Bash(chmod:*)",
      "Bash(mkdir:*)", "Bash(ln:*)", "Bash(black:*)", "Bash(isort:*)",
      "Bash(prettier:*)", "WebFetch(domain:example.com)"
    ],
    "defaultMode": "delegate"
  },
  "model": "sonnet",
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
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          },
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/claude_notify.sh success \"Claude Code\" \"Task completed successfully\" \"Glass\""
          }
        ]
      }
    ]
  },
  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true,
    "claude-mem": true,
    "feature-dev@claude-plugins-official": true
  },
  "alwaysThinkingEnabled": false
}
```

### 1.2 project-settings.json (プロジェクト固有設定)

```json
{
  "permissions": { ... },  // settings.json と同一
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/format_changed_file.sh \"$file_path\"",
            "description": "Auto-format code after Edit/Write (Week 2 implementation)"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff",
            "description": "Play sound on task completion"
          },
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/claude_notify.sh success \"Claude Code\" \"Task completed successfully\" \"Glass\"",
            "description": "Send macOS notification on task completion (Week 3 implementation)"
          }
        ]
      }
    ]
  },
  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true,
    "feature-dev@claude-plugins-official": true
  },
  "statusLine": {
    "alwaysShowContext": true
  }
}
```

### 1.3 .claude/hooks/ (シェルベースのhooks)

```bash
# /Users/yuichi/AIPM/aipm_v0/.claude/hooks/post-bash
#!/bin/bash
if [ $? -eq 0 ]; then
    afplay /System/Library/Sounds/Glass.aiff &
else
    afplay /System/Library/Sounds/Basso.aiff &
fi
```

**実行タイミング**: Bashコマンド実行後（成功時=Glass、エラー時=Basso）

---

## 2. 既存フック詳細分析

### 2.1 PostToolUse フック - Auto Format

| 項目 | 値 |
|------|-----|
| **Matcher** | Edit\|Write |
| **実行スクリプト** | format_changed_file.sh |
| **対応言語** | Python, JS/TS, Markdown, JSON, YAML, CSS/SCSS |
| **フォーマッター** | black, isort, prettier |
| **タイムアウト** | 5秒/ファイル |
| **除外設定** | .claudeignore_format で管理 |
| **環境変数** | CLAUDE_AUTO_FORMAT (デフォルト: true) |
| **状態** | ✅ 運用中（2026-01-03から） |

**実装詳細**:
- Edit/Write後に自動的にコードフォーマットを実行
- ファイル存在・拡張子の事前チェック
- フォーマット失敗時も処理を継続（エラーハンドリング）
- 実行履歴: 本日 7回成功

### 2.2 Stop フック - Notification

| 項目 | 値 |
|------|-----|
| **トリガー** | セッション終了時 |
| **Hook 1** | 音声通知 (Glass.aiff) |
| **Hook 2** | macOS通知センター + ログ出力 |
| **実行スクリプト** | claude_notify.sh |
| **ログ保存先** | /logs/notifications/notifications_YYYYMMDD.log |
| **状態** | ✅ 運用中（2026-01-03から） |

**実行履歴** (本日):
```
[2026-01-09 08:48:00] [success] Claude Code: Task completed successfully
[2026-01-09 08:50:05] [success] Claude Code: Task completed successfully
[2026-01-09 09:01:22] [success] Claude Code: Task completed successfully
[2026-01-09 10:22:22] [success] Claude Code: Task completed successfully
[2026-01-09 10:24:43] [success] Claude Code: Task completed successfully
[2026-01-09 10:43:53] [success] Claude Code: Task completed successfully
[2026-01-09 10:50:36] [success] Claude Code: Task completed successfully
```

### 2.3 post-bash hook (シェルベース)

| 項目 | 値 |
|------|-----|
| **実行タイミング** | Bashコマンド実行後 |
| **成功時** | Glass.aiff を再生 |
| **エラー時** | Basso.aiff を再生 |
| **目的** | コマンド完了の即座フィードバック |
| **実装言語** | Shell script |
| **状態** | ✅ 有効（ディレクトリ存在） |

---

## 3. Week 2 Phase 1 新規フック仕様との競合分析

### 3.1 新規フック仕様（計画）

**トリガー**: Read/Glob/Grep/Bash 実行後  
**目的**: LLM実行結果の自動構造化・キャッシュ化

```json
{
  "PostToolUse": [
    {
      "matcher": "Bash|Read|Glob|Grep",
      "hooks": [
        {
          "type": "command",
          "command": "bash cache_tool_results.sh \"$tool_name\" \"$output_file\""
        }
      ]
    }
  ]
}
```

### 3.2 競合リスク評価

#### ❌ **重大な競合リスク: PostToolUse マッチャーの重複**

**問題点**:
1. **既存**: `matcher: "Edit|Write"` → format_changed_file.sh
2. **新規**: `matcher: "Bash|Read|Glob|Grep"` → cache_tool_results.sh
3. **共存可能**: ✅ マッチ対象が完全に異なるため、直接的な競合なし

**ただし、実装上の注意**:
- Edit/Write のフォーマット実行中に新規フック（Read結果キャッシュ）が混在する可能性
- 実行順序が不明確（settings.json では配列順序が保証されない可能性）
- タイムアウト累積（フォーマット 5秒 + キャッシュ N秒）

#### ⚠️ **中程度の競合リスク: Stop フック**

既存 Stop フック:
```
1. Glass 音声再生
2. macOS 通知センター + ログ記録
```

新規追加の Stop フック（提案）:
```
3. セッション終了統計レポート生成
4. 流れ作業の自動確定反映判定
```

**影響**:
- Stop フック実行時間が増加 → セッション終了待機時間が長くなる可能性
- 複数 Stop フックの実行順序未定義

---

## 4. 実装上の推奨事項

### 4.1 新規フック追加時の安全な統合方法

#### **推奨パターン: マッチャー分離**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/format_changed_file.sh \"$file_path\"",
            "description": "Week 2: Auto-format code (existing)"
          }
        ]
      },
      {
        "matcher": "Bash|Read|Glob|Grep",
        "hooks": [
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/cache_tool_results.sh \"$tool_name\" \"$output\" \"$timestamp\"",
            "description": "Week 2 Phase 1: Cache LLM execution results"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff",
            "description": "Week 2: Audio feedback"
          },
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/claude_notify.sh success \"Claude Code\" \"Task completed successfully\" \"Glass\"",
            "description": "Week 3: macOS notification"
          },
          {
            "type": "command",
            "command": "bash /Users/yuichi/AIPM/aipm_v0/scripts/generate_session_stats.sh",
            "description": "Week 2 Phase 1: Session statistics report"
          }
        ]
      }
    ]
  }
}
```

### 4.2 実装チェックリスト

#### **新規フック追加前**

- [ ] settings.json と project-settings.json の同期確認
- [ ] 既存マッチャーと新規マッチャーが重複していないか確認
- [ ] タイムアウト設定（5-10秒以内推奨）
- [ ] エラー時のハンドリング（失敗してもClaude処理を止めない）

#### **新規フック追加後**

- [ ] 各ツール種別で実行確認（Bash, Read, Glob, Grep）
- [ ] ログファイル出力確認
- [ ] 複数フック実行時の順序・タイミング確認
- [ ] セッション終了時のStop フック実行確認

#### **定期メンテナンス**

- [ ] 月次でフック実行ログを集計（成功率、実行時間）
- [ ] 失敗したフックのスクリプト修正
- [ ] 新規フック追加時のパフォーマンス評価

### 4.3 パフォーマンス予測

| フェーズ | PostToolUse 実行時間 | Stop 実行時間 | 合計セッション追加時間 |
|---------|---------------------|--------------|----------------------|
| **現在** (Edit/Write + Stop) | 5秒 | 2秒 | 7秒 |
| **Week 2追加後** (Bash/Read/Glob/Grep キャッシュ) | 5-15秒 | 2秒 | 10-20秒 |
| **Week 2 Phase 1追加後** (セッション統計) | 5-15秒 | 5-8秒 | 15-28秒 |

**推奨対策**:
- キャッシュ処理は非同期化（run_in_background: true 設定検討）
- セッション統計はStop フックではなく、別途定期実行スケジューラとして実装

---

## 5. 既存フックの動作確認結果

### 5.1 Auto Format フック (format_changed_file.sh)

**テスト対象**: Edit/Write 後の自動フォーマット  
**結果**: ✅ 正常動作

**実行例**:
```bash
$ # Edit でPythonファイルを修正
✅ Auto-format executed
🐍 Formatting Python file: /path/to/file.py
✅ Formatting completed

$ # Write でJSONファイルを作成
✅ Auto-format executed
📦 Formatting JSON file: /path/to/file.json
✅ Formatting completed
```

**除外ファイル** (.claudeignore_format):
```
Archived/
# その他、手動で追加可能
```

### 5.2 Notification フック (claude_notify.sh)

**テスト対象**: セッション終了時の通知  
**結果**: ✅ 正常動作

**実行履歴** (本日):
- 08:48 成功
- 08:50 成功
- 09:01 成功
- 10:22 成功
- 10:24 成功
- 10:43 成功
- 10:50 成功

**ログ保存**: /logs/notifications/notifications_20260109.log

### 5.3 Post-Bash フック

**テスト対象**: Bashコマンド実行後の音声フィードバック  
**結果**: ✅ 存在確認（動作はOSレベル）

---

## 6. Week 2 Phase 1 統合戦略

### 6.1 推奨実装順序

#### **STEP 1: 新規フック スクリプト作成**
```bash
/Users/yuichi/AIPM/aipm_v0/scripts/cache_tool_results.sh
```
- Bash/Read/Glob/Grep 実行結果をキャッシュ
- タイムスタンプ付きJSON形式で保存
- 構造化データへの自動変換

#### **STEP 2: project-settings.json 更新**
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write", ... },  // 既존
      { "matcher": "Bash|Read|Glob|Grep", ... }  // 新규
    ]
  }
}
```

#### **STEP 3: 動作検証**
- Edit/Write → 既존 format_changed_file.sh 実행
- Bash → 新규 cache_tool_results.sh 실행
- Read → 新규 cache_tool_results.sh 실행
- 同時実行時の순序 및 타이밍 확인

#### **STEP 4: 统合테스트**
```bash
# 複수ツール同時実行
Edit + Bash → 両フック実行
Read + Write → 両フック実行
세션終료 → Stop フック(3つ) 모두 실행
```

### 6.2 롤백계획

新規フック追加後に問題が발생した場合:

**case 1: Performance degradation**
```json
// キャッシュフックを非同期に変更
{
  "type": "command",
  "command": "bash cache_tool_results.sh ... &"
}
```

**case 2: Conflicting execution**
```bash
# フック無效化（환경변수로 제어）
export CLAUDE_CACHE_ENABLED=false
```

**case 3: Complete rollback**
```bash
# project-settings.json から新規フック定義를 삭제
# 기존 설정만 유지
```

---

## 7. 参考資料

### 7.1 ファイル一覧

| ファイル | 用途 | 状態 |
|---------|------|------|
| ~/.claude/settings.json | ユーザー全体フック設定 | ✅ 运营中 |
| /aipm_v0/.claude/project-settings.json | プロジェクト固有フック設定 | ✅ 运营中 |
| /aipm_v0/scripts/format_changed_file.sh | Auto-format script | ✅ 运営中 |
| /aipm_v0/scripts/claude_notify.sh | Notification script | ✅ 运营中 |
| /aipm_v0/.claude/hooks/post-bash | Shell-based Bash hook | ✅ 有効 |
| /aipm_v0/.claudeignore_format | Format除外リスト | ✅ 管理中 |

### 7.2 ログファイル

```
/aipm_v0/logs/notifications/notifications_20260109.log  # 本日実行履歴
/aipm_v0/logs/notifications/notifications_*.log  # 過去ログ（日付別）
```

---

## 8. まとめ

### 既存フック設定状況
- ✅ **PostToolUse フック (Edit|Write)**: Auto-format 運营中
- ✅ **Stop フック**: Notification 운영중 (2개 hook)
- ✅ **post-bash フック**: Shell-based feedback 有효

### Week 2 Phase 1 新規フック統合
- ✅ **競合なし**: 新규 matcher (Bash|Read|Glob|Grep) は既存 (Edit|Write) と분리됨
- ⚠️ **推奨**: マッチャー分離により각 フック independently動作
- 📋 **チェックリスト**: 4.2項参照

### 即座アクション
1. 新規 cache_tool_results.sh 스크립트 작성
2. project-settings.json에 PostToolUse matcher 추가
3. 동작검증 및 통합테스트
4. 롤백계획 準備

