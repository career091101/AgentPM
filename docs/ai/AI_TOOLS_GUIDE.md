# AI Tools 統合使い方ガイド

**作成日**: 2025-12-30
**バージョン**: 1.0
**対象ツール**: Claude Code, Antigravity, Cursor, Codex

---

## 📋 目次

1. [概要](#概要)
2. [4つのAIツール比較](#4つのaiツール比較)
3. [統合トリガーワード一覧](#統合トリガーワード一覧)
4. [各ツール固有の使い方](#各ツール固有の使い方)
5. [環境切替ガイド](#環境切替ガイド)
6. [トラブルシューティング](#トラブルシューティング)

---

## 概要

このガイドは、aipm_v0プロジェクトで使用する4つのAIツールの統合的な使い方をまとめたものです。

### 4つのツール
- **Claude Code** - CLI型AI開発ツール（Anthropic公式）
- **Antigravity** - エージェント型AI（ワークフロー自動化）
- **Cursor** - AI統合エディタ（コード編集特化）
- **Codex** - スキル型AI（タスク自動化）

### 共通の設計思想
- **PMBOK準拠**: プロジェクト管理の標準プロセス
- **3層フォルダ構造**: Flow/Stock/Archived
- **トリガーワード運用**: 自然言語でAIを起動

---

## 4つのAIツール比較

| 項目 | Claude Code | Antigravity | Cursor | Codex |
|------|-------------|-------------|--------|-------|
| **用途** | CLI開発全般 | ワークフロー自動化 | コード編集 | タスク自動化 |
| **起動方法** | ターミナル | エージェント起動 | エディタ内 | スキル実行 |
| **設定場所** | `.claude/` | `.agent/` | `.cursor/` | `.codex/` |
| **ルール形式** | Markdown | Markdown | MDC | SKILL.md |
| **強み** | 多機能CLI操作 | 複雑なワークフロー | コード補完 | 単一タスク特化 |
| **推奨シーン** | 探索・調査 | バッチ処理 | コーディング | 定型作業 |

### 使い分けガイド

#### Claude Code を使う場合
- プロジェクト全体の調査・探索
- 複数ファイルの横断検索
- ドキュメント生成
- インタラクティブな作業

#### Antigravity を使う場合
- 複数ステップのワークフロー
- バッチ処理（一括変換など）
- 定期実行タスク
- 他ツール連携

#### Cursor を使う場合
- コード編集・リファクタリング
- バグ修正
- コード補完
- リアルタイム開発

#### Codex を使う場合
- 単一タスクの自動化
- スキル実行（ペルソナ作成など）
- 定型作業の繰り返し

---

## 統合トリガーワード一覧

### 日次タスク管理トリガー（Ultra Light 3コマンド運用）

| トリガー | 目的 | 対応ツール |
|----------|------|-----------|
| **タスクメモ** | inbox に気がかりを追記（何行でもOK） | 全ツール |
| **次の一手** | inbox から1件選択して A/B/C 候補生成 | 全ツール |
| **全部の一手** | inbox 全件の A/B/C 候補を一括表示 | 全ツール |
| **これやる** | candidates から tasks へ確定 | 全ツール |
| **今日のタスク** | 日次タスク開始 | 全ツール |
| **作業開始** | 日次タスク開始 | 全ツール |

---

### PMBOKフェーズ系トリガー

#### 1. Initiating（立ち上げ）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| プロジェクト憲章 | draft_project_charter.md | 全ツール |
| ステークホルダー分析 | draft_stakeholder_analysis.md | 全ツール |
| プロダクト定義 | draft_program_definition.md | 全ツール |

#### 2. Discovery（発見）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| ペルソナ作成 | draft_persona.md | 全ツール |
| ジャーニーマップ | draft_user_journey_map.md | 全ツール |
| 仮説マップ | draft_assumption_map.md | 全ツール |
| 課題定義 | draft_problem_statement.md | 全ツール |

#### 3. Research（調査）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| 競合調査 | draft_competitor_research.md | 全ツール |
| 市場規模推定 | draft_market_size_estimation.md | 全ツール |
| デスクリサーチ | draft_desk_research.md | 全ツール |

#### 4. Planning（計画）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| WBS作成 | draft_wbs.md | 全ツール |
| プロダクトバックログ初期化 | backlog.yaml | 全ツール |
| リスク計画 | draft_risk_plan.md | 全ツール |

#### 5. Executing（実行）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| Development | 開発メニュー表示 | 全ツール |
| 開発計画作成 | draft_development_plan.md | 全ツール |

#### 6. Monitoring（監視）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| ステータスレポート | status_report.md | 全ツール |
| 変更要求 | change_request.md | 全ツール |

#### 7. Closing（終結）
| トリガー | 生成物 | 対応ツール |
|----------|--------|-----------|
| レッスンズラーンド | lessons_learned.md | 全ツール |
| 移行文書 | transition_document.md | 全ツール |

---

## 各ツール固有の使い方

### 1. Claude Code（CLI型）

#### 起動方法
```bash
# ターミナルから起動
claude
```

#### 設定ファイル構造
```
.claude/
├── rules/              # ルール定義
│   ├── pmbok_*.md      # PMBOKフェーズ別
│   ├── task_management.md
│   └── flow_assist.md
├── agents/             # Subagents
│   ├── initiating-agent.md
│   ├── discovery-agent.md
│   └── ...
├── skills/             # スキル定義
│   └── ...
├── commands/           # コマンド
│   └── ...
└── daily/              # 日次タスク管理
    ├── README.md
    └── intake_prompt.md
```

#### 基本コマンド
```bash
# ヘルプ表示
/help

# ファイル読み込み
@filename

# プロジェクト構造確認
@docs/ai/overview.md

# ルール確認
@.claude/rules/pmbok_initiating.md
```

#### トリガーワード使用例
```
# 日次タスク管理（Ultra Light 3コマンド）
タスクメモ
次の一手
これやる

# PMBOKフェーズ実行
プロジェクト憲章
ペルソナ作成
```

#### 参考ファイル
- 使い方ガイド: `.claude/daily/README.md`
- 対話台本: `.claude/daily/intake_prompt.md`
- タスク管理ルール: `.claude/rules/task_management.md`

---

### 2. Antigravity（エージェント型）

#### 起動方法
```bash
# エージェント起動（ツール固有の起動方法に従う）
antigravity start
```

#### 設定ファイル構造
```
.agent/
├── rules/              # ルール定義
│   └── daily_tasks.md
└── workflows/          # ワークフロー定義
    ├── create_lean_canvas.md
    ├── define_persona.md
    └── ...
```

#### ワークフロー実行
```bash
# ワークフロー一覧
antigravity list

# ワークフロー実行
antigravity run create_lean_canvas

# ペルソナ定義ワークフロー
antigravity run define_persona
```

#### トリガーワード使用例
```
# 日次タスク管理（Ultra Light 3コマンド）
タスクメモ
次の一手
これやる

# PMBOKフェーズ実行
ペルソナ作成
競合調査
```

#### 参考ファイル
- 日次タスクルール: `.agent/rules/daily_tasks.md`
- ワークフロー一覧: `.agent/workflows/`

---

### 3. Cursor（エディタ型）

#### 起動方法
```bash
# Cursorエディタを開く
cursor .
```

#### 設定ファイル構造
```
.cursor/
└── rules/
    └── basic/
        ├── 01_pmbok_initiating.mdc
        ├── 02_pmbok_discovery.mdc
        ├── 03_pmbok_planning.mdc
        ├── 04_pmbok_executing.mdc
        ├── 05_pmbok_monitoring.mdc
        ├── 06_pmbok_closing.mdc
        ├── 07_task_management_ultralight.mdc
        └── pmbok_paths.mdc
```

#### ルール読み込み
```
# Cursor内でルールを参照
@.cursor/rules/basic/01_pmbok_initiating.mdc
```

#### トリガーワード使用例
```
# 日次タスク管理（Ultra Light 3コマンド）
タスクメモ
次の一手
これやる

# PMBOKフェーズ実行
プロジェクト憲章
WBS作成
```

#### 参考ファイル
- Ultra Lightルール: `.cursor/rules/basic/07_task_management_ultralight.mdc`
- PMBOKパス設定: `.cursor/rules/basic/pmbok_paths.mdc`

---

### 4. Codex（スキル型）

#### 起動方法
```bash
# Codexスキル実行（ツール固有の起動方法に従う）
codex run [skill-name]
```

#### 設定ファイル構造
```
.codex/
└── skills/
    ├── initiating/
    │   └── SKILL.md
    ├── discovery/
    │   └── SKILL.md
    ├── planning/
    │   └── SKILL.md
    ├── task-management/
    │   └── SKILL.md
    └── ...
```

#### スキル実行
```bash
# スキル一覧
codex list

# スキル実行
codex run initiating
codex run discovery
codex run task-management
```

#### トリガーワード使用例
```
# タスク管理スキル
タスクメモ
次の一手
これやる

# PMBOKフェーズスキル
プロジェクト憲章
ペルソナ作成
```

#### 参考ファイル
- タスク管理スキル: `.codex/skills/task-management/SKILL.md`
- PMBOKスキル一覧: `.codex/skills/`

---

## 環境切替ガイド

### ツール間の切り替え

#### Claude Code → Cursor
```bash
# Claude CodeのCLIを終了
exit

# Cursorエディタを開く
cursor .
```

#### Cursor → Antigravity
```bash
# Cursorは開いたまま、別ターミナルでAntigravity起動
antigravity start
```

#### 複数ツール同時使用
```bash
# Terminal 1: Claude Code
claude

# Terminal 2: Antigravity
antigravity start

# Cursor エディタ: 常時起動
cursor .
```

### 設定ファイルの共通化

すべてのツールは以下を共有：
- **3層フォルダ構造**: `Flow/`, `Stock/`, `Archived/`
- **PMBOKフェーズ**: 全ツール共通のトリガーワード
- **日次タスク管理**: `Flow/YYYYMM/YYYY-MM-DD/daily_tasks.yaml`

### パス設定

各ツールの設定ファイルで共通パスを参照：
```markdown
# Cursor
path_reference: "pmbok_paths.mdc"

# Claude Code
参照: @docs/ai/pmbok_workflow.md

# Antigravity
参照: @.agent/rules/daily_tasks.md

# Codex
参照: @.codex/skills/task-management/SKILL.md
```

---

## トラブルシューティング

### Q1: どのツールを使えばいいかわからない

**A**: 以下のフローチャートで判断してください：

```
タスクの種類は？
├─ コード編集・リファクタリング → Cursor
├─ 複数ステップのワークフロー → Antigravity
├─ 探索・調査・ドキュメント生成 → Claude Code
└─ 定型タスクの自動化 → Codex
```

---

### Q2: トリガーワードが動かない

**A**: 以下を確認してください：

1. **ツールが正しく起動しているか**
   ```bash
   # Claude Code
   claude

   # Cursor
   cursor .
   ```

2. **設定ファイルが存在するか**
   ```bash
   # Claude Code
   ls .claude/rules/

   # Cursor
   ls .cursor/rules/basic/

   # Antigravity
   ls .agent/rules/

   # Codex
   ls .codex/skills/
   ```

3. **トリガーワードのスペルミスがないか**
   - 正: 「タスクメモ」
   - 誤: 「タスクめも」「task memo」

---

### Q3: 日次タスク管理が動かない

**A**: Ultra Light 3コマンド運用の確認手順：

1. **YAMLファイルが存在するか**
   ```bash
   ls Flow/202512/2025-12-30/daily_tasks.yaml
   ```

2. **トリガーワードを正確に入力**
   - 「タスクメモ」（inbox追記）
   - 「次の一手」（候補生成）
   - 「これやる」（タスク確定）

3. **ルールファイルを確認**
   - Claude Code: `.claude/rules/task_management.md`
   - Cursor: `.cursor/rules/basic/07_task_management_ultralight.mdc`
   - Antigravity: `.agent/rules/daily_tasks.md`
   - Codex: `.codex/skills/task-management/SKILL.md`

---

### Q4: ファイルパスが見つからない

**A**: ベースディレクトリを確認してください：

```bash
# 現在のディレクトリ確認
pwd
# 出力例: /Users/yuichi/AIPM/aipm_v0

# aipm_v0 ディレクトリに移動
cd /Users/yuichi/AIPM/aipm_v0

# 構造確認
ls -la
# 出力: Flow/, Stock/, Archived/, .claude/, .cursor/, .agent/, .codex/
```

**環境別パス書き換え**:
- macOS: `/Users/[username]/AIPM/aipm_v0`
- Linux: `/home/[username]/AIPM/aipm_v0`
- Windows: `C:\Users\[username]\AIPM\aipm_v0`

---

### Q5: ツール間で設定が同期されない

**A**: 設定は各ツール独立しています。共通化する場合：

1. **共通ドキュメントを参照**
   - `docs/ai/overview.md` - システム概要
   - `docs/ai/pmbok_workflow.md` - PMBOKワークフロー
   - `CLAUDE.md` - プロジェクトコンテキスト

2. **YAMLファイルは共有**
   - `Flow/YYYYMM/YYYY-MM-DD/daily_tasks.yaml` - 全ツール共通
   - `Flow/YYYYMM/YYYY-MM-DD/failure_log.yaml` - 全ツール共通

3. **ルールファイルは個別管理**
   - Claude Code: `.claude/rules/`
   - Cursor: `.cursor/rules/basic/`
   - Antigravity: `.agent/rules/`
   - Codex: `.codex/skills/`

---

### Q6: トリガーワードが競合する

**A**: トリガーワードは以下の2種類に分類されています：

**日次タスク管理系**:
- 「タスクメモ」「次の一手」「これやる」- Ultra Light 3コマンド運用
- 「今日のタスク」「作業開始」- 日次タスク開始

**PMBOKフェーズ系**:
- 「プロジェクト憲章」「ペルソナ作成」「WBS作成」など

これらは互いに競合しないように設計されています。

---

## 📚 参考ファイル一覧

### 共通ドキュメント
- **このガイド**: `docs/ai/AI_TOOLS_GUIDE.md`
- **システム概要**: `docs/ai/overview.md`
- **PMBOKワークフロー**: `docs/ai/pmbok_workflow.md`
- **プロジェクトコンテキスト**: `CLAUDE.md`

### Claude Code
- **日次タスクREADME**: `.claude/daily/README.md`
- **対話台本**: `.claude/daily/intake_prompt.md`
- **タスク管理ルール**: `.claude/rules/task_management.md`

### Cursor
- **Ultra Lightルール**: `.cursor/rules/basic/07_task_management_ultralight.mdc`
- **PMBOKパス設定**: `.cursor/rules/basic/pmbok_paths.mdc`

### Antigravity
- **日次タスクルール**: `.agent/rules/daily_tasks.md`
- **ワークフロー一覧**: `.agent/workflows/`

### Codex
- **タスク管理スキル**: `.codex/skills/task-management/SKILL.md`
- **PMBOKスキル一覧**: `.codex/skills/`

### データファイル（全ツール共通）
- **タスクリスト**: `Flow/202512/2025-12-30/daily_tasks.yaml`
- **失敗記録**: `Flow/202512/2025-12-30/failure_log.yaml`

---

## 🔄 次のステップ

### 1. まずは1つのツールから始める
- **推奨**: Claude Code（多機能で探索に適している）
- **または**: Cursor（コード編集が多い場合）

### 2. トリガーワードを覚える
1. **日次タスク管理**: 「タスクメモ」「次の一手」「これやる」
2. **PMBOKフェーズ**: 「プロジェクト憲章」「ペルソナ作成」など

### 3. 複数ツールを組み合わせる
- **朝**: Claude Code で「タスクメモ」
- **日中**: Cursor でコード編集
- **夜**: Antigravity でワークフロー実行

---

## ✅ 成功基準

### 各ツールが使えている状態
- [ ] Claude Code でトリガーワードが動作する
- [ ] Cursor でルールが読み込まれる
- [ ] Antigravity でワークフロー実行できる
- [ ] Codex でスキル実行できる

### 日次タスク管理が回っている状態
- [ ] 毎朝「タスクメモ」で inbox に3行入れられる
- [ ] 「次の一手」で A/B/C 候補が生成される
- [ ] 「これやる」で tasks に確定できる
- [ ] `daily_tasks.yaml` が正しく更新される

### PMBOKフェーズが使えている状態
- [ ] 「プロジェクト憲章」でドラフトが生成される
- [ ] 「ペルソナ作成」で質問応答が始まる
- [ ] Flow フォルダにドラフトが保存される
- [ ] Stock フォルダに確定版が移動できる

---

**更新履歴**:
- 2025-12-30 v1.0: 初版リリース（4ツール統合ガイド）

**作成者**: Claude Sonnet 4.5
**設計方針**: トリガーワード競合回避、共通データ形式、ツール間シームレス切替
