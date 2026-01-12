# Claude Code エージェント一覧

このディレクトリには、aipm_v0で使用可能なSubagentスキルが含まれています。

## エージェント一覧

### PMBOKフェーズ別エージェント

#### 1. Initiating Agent (`initiating-agent.md`)

- **役割**: プロジェクト立ち上げフェーズを支援
- **主な機能**:
  - プロジェクト憲章の作成支援
  - ステークホルダー分析
  - プロダクト定義
- **トリガー**: 「プロジェクト憲章」「ステークホルダー分析」「プロダクト定義」

#### 2. Discovery Agent (`discovery-agent.md`)

- **役割**: UX発見フェーズを支援（Opus推論力を活用）
- **主な機能**:
  - ペルソナ設計
  - ジャーニーマップ作成
  - 仮説マップ構築
  - 課題定義
  - ソリューション定義
  - 検証計画
- **トリガー**: 「ペルソナ作成」「ジャーニーマップ」「仮説マップ」「課題定義」「ソリューション定義」「検証計画」

#### 3. Research Agent (`research-agent.md`)

- **役割**: 調査・分析フェーズを支援
- **主な機能**:
  - 競合調査
  - 市場規模推定
  - デスクリサーチ
  - 顧客調査
- **トリガー**: 「顧客調査」「競合調査」「デスクリサーチ」「市場規模推定」

#### 4. Planning Agent (`planning-agent.md`)

- **役割**: 計画策定フェーズを支援
- **主な機能**:
  - WBS作成
  - PRD（プロダクト要求仕様書）作成
  - バックログ初期化
  - リスク計画
  - ロードマップ作成
- **トリガー**: 「WBS作成」「プロダクトバックログ初期化」「リスク計画」「プロジェクトスコープ記述書」「プロダクト要求仕様書」「ロードマップ作成」

#### 5. Executing Agent (`executing-agent.md`)

- **役割**: 実行フェーズを支援
- **主な機能**:
  - 開発計画作成
  - ストーリー実装支援
  - スプリントゴール管理
- **トリガー**: 「Development」「開発計画作成」「ストーリー実装」「スプリントゴール」

#### 6. Monitoring Agent (`monitoring-agent.md`)

- **役割**: 監視・コントロールフェーズを支援
- **主な機能**:
  - ステータスレポート作成
  - 変更要求管理
  - リスク更新
- **トリガー**: 「ステータスレポート」「変更要求」

#### 7. Closing Agent (`closing-agent.md`)

- **役割**: 終結フェーズを支援
- **主な機能**:
  - レッスンズラーンド作成
  - 移行文書作成
  - 完了報告書
- **トリガー**: 「レッスンズラーンド」「移行文書」

### 機能別エージェント

#### 8. Task Manager Agent (`task-manager.md`)

- **役割**: 日次タスク管理を支援
- **主な機能**:
  - 今日のタスク生成
  - スプリントゴール管理
  - 週次レビュー
  - カレンダー予定確認との連携
- **トリガー**: 「今日のタスク」「作業開始」「カレンダー確認」「今日の予定」

#### 9. Flow Assist Agent (`flow-assist-agent.md`)

- **役割**: アイディア発散を支援
- **主な機能**:
  - ブレインストーミング支援
  - コンセプト生成
  - アイディア発散記録
- **トリガー**: 「アイディア発散」

#### 10. Development Agent (`development-agent.md`)

- **役割**: 開発作業を支援
- **主な機能**:
  - コード生成
  - 実装支援
  - 開発環境セットアップ
  - ソース管理連携
- **トリガー**: 「開発環境初期化」「ストーリー実装」

#### 11. Rule Maintainer Agent (`rule-maintainer.md`)

- **役割**: ルール管理を支援
- **主な機能**:
  - ルール追加・更新
  - 整合性チェック
  - マルチツール同期（Antigravity/Cursor/Codex/Claude Code）
  - フェーズ追加ウィザード
- **トリガー**: 「フェーズ追加」「Phase追加」「新フェーズ作成」

### 専門領域エージェント

#### 12. Deep Research to Note Agent (`deep_research_to_note.md`) ⭐新規

- **役割**: 学術論文やテクニカルドキュメントに対する高速かつ深い理解を実現し、落合陽一式の6つの質問に基づくA4 1枚サマリーを作成
- **主な機能**:
  - 論文PDF構造解析（Abstract, Conclusion, Experiments, Related Work等のセクション特定）
  - 戦略的読解順序による逆順アプローチ（Abstract→Conclusion→Experiments→Related Work）
  - 落合フォーマット6つの質問への自動回答生成
  - A4 1枚相当の圧縮要約作成（800-1200単語、図表1-3点含む）
  - Notionデータベース連携による論文管理（タグ自動生成、引用ネットワーク構築）
  - 次に読むべき論文の推薦（References分析と引用頻度ランキング）
  - 週次進捗管理（週25-100本の読了トラッキング）
- **トリガー**: 「ディープリサーチ」「落合式リサーチ」「論文サマリー作成」「6つの質問」「研究サーベイ」
- **参照**: `@.claude/rules/deep_research_to_note.md`（作成予定）

## 使い方

### 基本的な呼び出し方法

#### 1. トリガーワードを使用

会話の中でトリガーワードを含めることで、対応するエージェントが自動的に起動します。

**例**:
```
「プロジェクト憲章を作成してください」
→ Initiating Agentが起動し、プロジェクト憲章作成のための質問を開始

「ディープリサーチを実行してください」
→ Deep Research to Note Agentが起動し、論文サマリー作成を支援

「今日のタスクを確認したい」
→ Task Manager Agentが起動し、daily_tasks.mdを生成

「ペルソナ作成」
→ Discovery Agentが起動し、ペルソナ設計のための質問を開始
```

#### 2. エージェント名を明示的に指定（将来的に実装予定）

```
例: 「@research-agent 競合調査を実施してください」
例: 「@deep-research-to-note-agent 論文サマリーを作成してください」
```

### 成果物の確定フロー

エージェントが生成したドラフトファイルは、`Flow/YYYYMM/YYYY-MM-DD/` 配下に保存されます。

内容を確認し、問題なければ以下のコマンドで確定版として Stock へ移動できます。

```
「確定反映して」
```

これにより、`Stock/programs/.../documents/[phase]/` へファイルが移動されます。

### ディレクトリ構造

```
.claude/
├── agents/           # エージェントスキルファイル（本ディレクトリ）
│   ├── initiating-agent.md
│   ├── discovery-agent.md
│   ├── research-agent.md
│   ├── planning-agent.md
│   ├── executing-agent.md
│   ├── monitoring-agent.md
│   ├── closing-agent.md
│   ├── task-manager.md
│   ├── flow-assist-agent.md
│   ├── development-agent.md
│   ├── rule-maintainer.md
│   ├── deep_research_to_note.md ⭐新規
│   └── README.md（本ファイル）
└── rules/            # 詳細ルールファイル
    ├── pmbok_initiating.md
    ├── pmbok_discovery.md
    ├── pmbok_research.md
    ├── pmbok_planning.md
    ├── pmbok_executing.md
    ├── pmbok_monitoring.md
    ├── pmbok_closing.md
    ├── task_management.md
    ├── flow_assist.md
    ├── development.md
    ├── rule_maintenance.md
    └── deep_research_to_note.md ⭐新規（作成予定）
```

### エージェント拡張ルール

新しいエージェントスキルを追加する場合：

#### 1. エージェントファイル作成 (`.claude/agents/`配下)

3セクション構造で記述：

```markdown
# [エージェント名] Agent

## 役割
[エージェントの役割を1-2行で簡潔に記述]

## 能力
- [能力1]
- [能力2]
- [能力3]

## 参照
- @.claude/rules/[対応するルールファイル].md
```

軽量アプローチ（詳細はルールファイルに委譲）を採用してください。

#### 2. ルールファイル作成 (`.claude/rules/`配下)

詳細な実行手順、トリガーワード、質問セット、テンプレートを定義：

```markdown
# [エージェント名] Rules

[エージェントの詳細説明]

## トリガー
- 「[トリガーワード1]」「[トリガーワード2]」

## 参照
- @.cursor/rules/basic/[番号]_[ルールファイル].mdc
```

#### 3. README.md更新

本ファイルに新規エージェントを追記してください。

## PMBOKフェーズとの対応

| フェーズ | エージェント | 主要トリガー |
|----------|--------------|--------------|
| 立ち上げ | Initiating Agent | プロジェクト憲章、ステークホルダー分析 |
| 発見 | Discovery Agent | ペルソナ、ジャーニーマップ、仮説マップ |
| 調査 | Research Agent | 競合調査、市場規模推定 |
| 計画 | Planning Agent | WBS、PRD、バックログ初期化 |
| 実行 | Executing Agent | 開発計画、ストーリー実装 |
| 監視 | Monitoring Agent | ステータスレポート、変更要求 |
| 終結 | Closing Agent | レッスンズラーンド、移行文書 |

## 参考資料

- **プロジェクト概要**: `@docs/ai/overview.md`
- **PMBOKワークフロー**: `@docs/ai/pmbok_workflow.md`
- **CLAUDE.md**: `@CLAUDE.md`
- **パス管理規約**: `@.claude/rules/path_conventions.md`

## マルチツール対応

このリポジトリは以下のAIツールで共通運用できます：

- **Antigravity** - 主軸ツール
- **Cursor** - 既存.mdcルール活用
- **Codex** - Skills経由
- **Claude Code** - Subagents経由（本ディレクトリ）

各ツール固有の設定ファイルは、対応するディレクトリを参照してください：

- Antigravity: `.agent/`
- Cursor: `.cursor/rules/`
- Codex: `.codex/`
- Claude Code: `.claude/`（本ディレクトリ）

## 運用Tips

### エージェントの選択基準

- **プロジェクト立ち上げ時**: Initiating Agent
- **ユーザー理解・課題発見**: Discovery Agent
- **市場・競合分析**: Research Agent
- **計画策定**: Planning Agent
- **開発・実装**: Executing Agent + Development Agent
- **進捗管理**: Monitoring Agent
- **振り返り**: Closing Agent
- **日々のタスク管理**: Task Manager Agent
- **アイディア出し**: Flow Assist Agent
- **ルール追加・更新**: Rule Maintainer Agent
- **論文・技術調査**: Deep Research to Note Agent ⭐新規

### 複数エージェントの組み合わせ

エージェントは独立して動作しますが、フェーズを跨いで連携することも可能です。

**例**:
1. Discovery Agent でペルソナを作成
2. Research Agent で市場規模を推定
3. Planning Agent でWBSとPRDを作成
4. Executing Agent で開発を実行
5. Monitoring Agent で進捗をトラッキング
6. Closing Agent でレッスンズラーンドを記録

## 更新履歴

- **2025-12-31**: README.md初版作成、Deep Research to Note Agent追加（12個目のエージェント）
- 既存11エージェント + 新規1エージェント = 合計12エージェント

---

aipm_v0 - PMBOK × Lean UX × Agile ハイブリッドプロジェクト管理システム
