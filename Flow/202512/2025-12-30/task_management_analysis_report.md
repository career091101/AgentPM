# タスク管理システム分析レポート

**作成日**: 2025-12-30
**対象**: 全AIツールのタスク管理実装(8ファイル)

---

## エグゼクティブサマリー

### 主要発見事項

1. **2つの異なるシステムが混在**
   - **Ultra Light版** (新): 3-4コマンド運用、inbox/candidates/tasks構造
   - **従来版** (旧): カレンダー連携、WBS同期、ルーチンタスク機能

2. **バージョン不整合**
   - `.agent/` と `.claude/` は v2.0/v2.1 (Ultra Light)
   - `.cursor/` は v2.0 (Ultra Light) + v1.0 (従来版) 両方存在
   - `.antigravity/` は簡易版（詳細度が異なる）
   - `.codex/` は参照インデックスのみ

3. **重複と冗長性**
   - Ultra Light仕様が4箇所で重複実装(.agent, .claude/daily, .cursor ultralight, .codex参照)
   - 同じワークフローが異なる詳細度で記述

---

## 1. 実装比較マトリックス

### 1.1 基本情報

| ファイル | 行数 | バージョン | システム種別 | ツール |
|---------|------|-----------|------------|--------|
| `.agent/rules/daily_tasks.md` | 537 | v2.0 Ultra Light | Ultra Light 3コマンド | Antigravity |
| `.antigravity/workflows/daily_tasks.md` | 26 | - | 簡易ワークフロー | Antigravity |
| `.claude/daily/README.md` | 579 | v2.0 Ultra Light | Ultra Light 使い方ガイド | Claude Code |
| `.claude/daily/intake_prompt.md` | 637 | v2.1 Ultra Light | Ultra Light 4コマンド対話台本 | Claude Code |
| `.claude/rules/task_management.md` | 132 | - | トリガー検知ルール | Claude Code |
| `.cursor/rules/basic/07_task_management.mdc` | 550 | v1.0 | 従来版（カレンダー・WBS連携） | Cursor IDE |
| `.cursor/rules/basic/07_task_management_ultralight.mdc` | 381 | v2.0 Ultra Light | Ultra Light 3コマンド | Cursor IDE |
| `.codex/skills/task-management/SKILL.md` | 76 | v2.0 Ultra Light | スキルインデックス | Codex |

### 1.2 トリガーワード比較

#### Ultra Light版（共通トリガー）

| トリガー | .agent | .antigravity | .claude | .cursor UL | .codex |
|---------|--------|-------------|---------|-----------|--------|
| **タスクメモ** | ✓ | - | ✓ | ✓ | ✓ |
| **次の一手** | ✓ | - | ✓ | ✓ | ✓ |
| **全部の一手** | ✓ | - | ✓ | ✓ | ✓ |
| **これやる** | ✓ | - | ✓ | ✓ | ✓ |
| **タスクプロンプト生成** | - | - | ✓ (v2.1) | - | - |

#### 従来版トリガー

| トリガー | .antigravity | .cursor (従来版) |
|---------|-------------|----------------|
| 今日のタスク | ✓ | ✓ |
| 作業開始 | ✓ | ✓ |
| スプリントゴール | ✓ | ✓ |
| カレンダー確認 | - | ✓ |
| 週次レビュー | - | ✓ |
| WBSと同期 | - | ✓ |

### 1.3 YAML構造比較

#### Ultra Light版の共通構造

```yaml
date: YYYY-MM-DD

inbox:              # 気がかり・悩み（無制限）
  - "項目1"
  - "項目2"

candidates:         # A/B/Cパターン（使い捨て）
  - "パターンA: [アプローチ名]"
  - "1. [Todo1]"
  - "2. [Todo2]"
  - "→ 完了: [最終成果物]"

tasks:             # 確定タスク（制限なし）
  - id: T001
    what: "タスク内容"
    done: "完了基準"
    status: pending/completed
    created_at: "YYYY-MM-DD HH:MM"
```

**フィールドの違い**:
- `.agent/`: `why`フィールド削除済み (Ultra Light版)
- `.claude/`: `why`フィールドなし (最初から)
- `.cursor/`: Ultra Light版は`why`なし、従来版は異なる構造

### 1.4 ワークフロー詳細度比較

| 機能 | .agent | .antigravity | .claude/daily | .cursor UL |
|------|--------|-------------|--------------|-----------|
| **inbox追記** | 詳細537行 | 簡易26行 | 詳細579行 | 中程度381行 |
| **候補生成ルール** | ✓ 詳細 | - | ✓ 詳細 | ✓ 中程度 |
| **Todo実行順序推奨** | ✓ | - | ✓ | ✓ |
| **Done定義パターン** | 6パターン固定 | - | 2-5パターン柔軟 | 6パターン固定 |
| **失敗記録** | ✓ failure_log.yaml | - | ✓ failure_log.yaml | - |
| **エラーハンドリング** | ✓ | - | ✓ | ✓ |

---

## 2. システム別詳細分析

### 2.1 Ultra Light版の実装差異

#### 共通仕様
- **3コマンド運用**: タスクメモ → 次の一手 → これやる
- **inbox/candidates/tasks構造**
- **タスクを考えない設計思想**

#### 実装差異

**Done定義の扱い**:
1. `.agent/` + `.cursor/UL`: **6パターン固定**
   ```
   1. 送れる/提出できる状態
   2. 動作確認が1回通る
   3. メモが5行ある
   4. 次のステップが1行で書ける
   5. ファイルが1つ増える
   6. 後で決める（空）
   ```

2. `.claude/daily/`: **2-5パターン柔軟**
   - タスクの性質に応じてAIが候補生成
   - 推奨理由付きで複数選択肢提示可能
   - 例: "A=1または2, C=1"

**Todoパターン生成**:
- `.agent/` + `.claude/`: パターン数は**2〜5個で柔軟**、複雑さに応じて調整
- `.cursor/UL`: パターン数明記なし、実装は同様

**バージョン番号**:
- `.agent/`: v2.0
- `.claude/intake_prompt`: v2.1 (タスクプロンプト生成機能追加)
- `.cursor/UL`: v2.0
- `.codex/`: v2.0と記載（実質は参照のみ）

### 2.2 従来版の機能

**`.cursor/rules/basic/07_task_management.mdc`のみに存在**:

1. **カレンダー連携**
   - トリガー: 「今日の予定」「カレンダー確認」
   - `./scripts/get_calendar_events.sh` 実行

2. **ルーチンタスク定義**
   - `routines.yaml` からタスク生成
   - 頻度: daily/weekly/monthly/quarterly/yearly
   - Pythonスクリプトで自動生成

3. **週次レビュー**
   - トリガー: 「週次レビュー」または金曜17:30
   - Flow内の全タスク集計
   - WBS/リスクログへ同期

4. **WBS同期**
   - トリガー: 「WBSと同期」「リスクログと同期」
   - 完了タスクをプロジェクト文書へ反映

**問題点**:
- この従来版は他のツール（.agent, .claude, .antigravity）では**未実装**
- Cursor固有機能となっている

### 2.3 .antigravity/workflows/daily_tasks.md の位置づけ

**特徴**:
- **最も簡易** (26行のみ)
- トリガーワードのみ記載
- 詳細は `.cursor/rules/basic/07_task_management.mdc` を参照

**問題点**:
- 参照先が従来版（カレンダー連携版）を指している
- Ultra Light版の存在と矛盾

---

## 3. 重大な不整合

### 3.1 タスク数制限の矛盾

| ファイル | 制限 |
|---------|------|
| `.agent/rules/daily_tasks.md` | **最大3個推奨** (395行目) |
| `.claude/daily/README.md` | **最大3個推奨** (289, 403行目) |
| `.claude/daily/intake_prompt.md` | **制限なし** (379行目「tasksは制限なし」) |
| `.cursor/07_task_management_ultralight.mdc` | **制限なし** (348行目) |

**結論**: 同じUltra Light v2.0でも、tasksの最大数について矛盾

### 3.2 バージョン表記の不整合

- `.agent/`: v2.0 (2025-12-30更新)
- `.claude/intake_prompt`: v2.1 (タスクプロンプト生成追加)
- `.claude/README`: v2.0
- `.cursor/UL`: v2.0
- `.codex/`: v2.0

**問題**:
- v2.1機能（タスクプロンプト生成）が `.claude/` のみ
- 他ツールは v2.0 のまま

### 3.3 Done定義の不整合

**固定6パターン方式**:
- `.agent/`
- `.cursor/UL`

**柔軟2-5パターン方式**:
- `.claude/daily/README.md`
- `.claude/daily/intake_prompt.md`

**結論**: 同じUltra Light仕様でも、Done定義の提示方法が異なる

### 3.4 参照関係の循環

**`.codex/skills/task-management/SKILL.md`**:
```markdown
参照:
  - Cursor Rule: @.cursor/rules/basic/07_task_management_ultralight.mdc
  - Antigravity Rule: @.agent/rules/daily_tasks.md
  - Claude Code: @.claude/daily/intake_prompt.md
```

**`.antigravity/workflows/daily_tasks.md`**:
```markdown
参照:
  - @.cursor/rules/basic/07_task_management.mdc  # ← 従来版を参照！
```

**問題**:
- `.antigravity/` は従来版を参照している
- 他は全てUltra Light版

---

## 4. 推奨事項

### 4.1 優先度高: 即座に修正すべき問題

#### ① タスク数制限の統一
**現状**: 「最大3個推奨」と「制限なし」が混在
**推奨**:
- **Option A**: 全て「制限なし」に統一（シンプル）
- **Option B**: 全て「最大3個推奨」に統一（集中力重視）

**影響範囲**:
- `.agent/rules/daily_tasks.md` (395行目)
- `.claude/daily/README.md` (289, 403行目)
- `.claude/daily/intake_prompt.md` (379行目)
- `.cursor/rules/basic/07_task_management_ultralight.mdc` (348行目)

#### ② .antigravity参照先の修正
**現状**: 従来版(07_task_management.mdc)を参照
**推奨**: Ultra Light版(07_task_management_ultralight.mdc)を参照

**変更箇所**:
```markdown
# .antigravity/workflows/daily_tasks.md
参照:
  - @.cursor/rules/basic/07_task_management_ultralight.mdc  # 修正
```

### 4.2 優先度中: バージョン統一

#### ③ v2.1機能の全ツール展開
**現状**: タスクプロンプト生成機能が `.claude/` のみ
**推奨**: `.agent/` と `.cursor/UL` にも追加

**メリット**:
- 全ツールで同じ機能が使える
- バージョン統一 (v2.1)

### 4.3 優先度低: Done定義方式の統一

#### ④ Done定義パターンの標準化
**現状**:
- 固定6パターン方式 (.agent, .cursor/UL)
- 柔軟2-5パターン方式 (.claude)

**推奨**:
- **Option A**: 柔軟方式を標準化（AIが状況に応じて生成）
- **Option B**: 固定6パターンを標準化（シンプル）

**トレードオフ**:
- 柔軟方式: 適切だが複雑
- 固定方式: シンプルだが融通が利かない

---

## 5. 正規版の提案

### 5.1 「正規版」の定義

**提案**: `.agent/rules/daily_tasks.md` を**マスター実装**とする

**理由**:
1. 最も詳細 (537行)
2. 2025-12-30に更新済み
3. エラーハンドリング充実
4. 毎日のルーチン記載あり

**他ツールの位置づけ**:
- `.claude/daily/`: Claude Code向けカスタマイズ版（v2.1機能含む）
- `.cursor/UL`: Cursor IDE向け実装
- `.codex/`: 参照インデックス（実装なし）
- `.antigravity/`: 簡易版（詳細は.agentを参照）

### 5.2 統一後の構造

```
Ultra Light v2.1 (タスク管理標準仕様)
├── Master Implementation
│   └── .agent/rules/daily_tasks.md ← 正規版・詳細実装
│
├── Tool-Specific Adaptations
│   ├── .claude/daily/intake_prompt.md ← Claude Code版（対話台本）
│   ├── .claude/daily/README.md ← 使い方ガイド
│   └── .cursor/rules/basic/07_task_management_ultralight.mdc ← Cursor版
│
├── Reference Index
│   └── .codex/skills/task-management/SKILL.md ← インデックス
│
└── Simplified Workflow
    └── .antigravity/workflows/daily_tasks.md ← 簡易版
```

### 5.3 従来版の扱い

**`.cursor/rules/basic/07_task_management.mdc` (従来版)**:
- **残す**: カレンダー連携・WBS同期が必要な場合
- **廃止検討**: Ultra Light版で十分な場合

**判断基準**:
- カレンダー連携機能を使っているか？ → Yes: 残す / No: 廃止
- WBS同期機能を使っているか？ → Yes: 残す / No: 廃止

---

## 6. 実装ロードマップ

### フェーズ1: 緊急修正（1-2時間）

**目標**: 致命的な不整合を解消

1. ✅ **タスク数制限の統一**
   - 全ファイルで「制限なし」または「最大3個推奨」に統一
   - 推奨: 「制限なし」（柔軟性重視）

2. ✅ **.antigravity参照先修正**
   ```diff
   - @.cursor/rules/basic/07_task_management.mdc
   + @.cursor/rules/basic/07_task_management_ultralight.mdc
   ```

### フェーズ2: バージョン統一（2-3時間）

**目標**: 全ツールをv2.1に統一

1. ✅ **v2.1機能を全ツールに展開**
   - `.agent/rules/daily_tasks.md` にタスクプロンプト生成機能追加
   - `.cursor/rules/basic/07_task_management_ultralight.mdc` に同機能追加

2. ✅ **バージョン番号更新**
   - 全ファイルのバージョンを v2.1 に統一

### フェーズ3: Done定義標準化（3-4時間）

**目標**: Done定義方式を統一

1. ✅ **柔軟方式を標準化**（推奨）
   - `.agent/` と `.cursor/UL` を柔軟方式に変更
   - 6パターン固定をやめて、AIが2-5パターン生成

2. **または**: 固定方式を標準化
   - `.claude/daily/` を6パターン固定に変更

### フェーズ4: ドキュメント整備（1-2時間）

**目標**: 参照関係を明確化

1. ✅ **マスター実装の明記**
   - 各ファイルに「正規版は .agent/rules/daily_tasks.md」と記載

2. ✅ **ツール別使い分けガイド作成**
   - どのツールでどのファイルを使うか明記

---

## 7. 成功基準

### 必須条件
- [ ] タスク数制限が全ツールで統一されている
- [ ] .antigravityの参照先がUltra Light版になっている
- [ ] バージョン番号が全ツールで一致している
- [ ] Done定義方式が統一されている

### 推奨条件
- [ ] タスクプロンプト生成機能が全ツールで使える
- [ ] 正規版が明確に定義されている
- [ ] ツール別使い分けガイドが存在する
- [ ] 従来版の存続/廃止が決定されている

---

## 8. 付録: ファイル詳細

### A. .agent/rules/daily_tasks.md
- **行数**: 537
- **バージョン**: v2.0 Ultra Light
- **特徴**: 最も詳細な実装、エラーハンドリング充実
- **推奨**: マスター実装として位置づけ

### B. .antigravity/workflows/daily_tasks.md
- **行数**: 26
- **バージョン**: 記載なし
- **特徴**: 簡易ワークフロー定義
- **問題**: 参照先が従来版

### C. .claude/daily/README.md
- **行数**: 579
- **バージョン**: v2.0 Ultra Light
- **特徴**: 使い方ガイド、豊富な例
- **推奨**: ユーザー向けドキュメントとして維持

### D. .claude/daily/intake_prompt.md
- **行数**: 637
- **バージョン**: v2.1 Ultra Light
- **特徴**: 4コマンド対話台本、タスクプロンプト生成機能
- **推奨**: v2.1機能を他ツールに展開

### E. .claude/rules/task_management.md
- **行数**: 132
- **バージョン**: 記載なし
- **特徴**: トリガー検知ルール、他ファイルへ委譲
- **推奨**: 維持（Claude Code用エントリーポイント）

### F. .cursor/rules/basic/07_task_management.mdc
- **行数**: 550
- **バージョン**: v1.0
- **特徴**: カレンダー連携、WBS同期、ルーチンタスク
- **推奨**: 使用状況に応じて存続/廃止判断

### G. .cursor/rules/basic/07_task_management_ultralight.mdc
- **行数**: 381
- **バージョン**: v2.0 Ultra Light
- **特徴**: Cursor IDE向けUltra Light実装
- **推奨**: v2.1へ更新

### H. .codex/skills/task-management/SKILL.md
- **行数**: 76
- **バージョン**: v2.0 Ultra Light
- **特徴**: スキルインデックス、他実装への参照
- **推奨**: 維持（Codex用エントリーポイント）

---

**分析完了日時**: 2025-12-30
**分析者**: Claude Sonnet 4.5
