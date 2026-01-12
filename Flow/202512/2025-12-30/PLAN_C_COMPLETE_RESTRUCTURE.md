# プランC: 完全再構築 - 詳細実装計画書

**作成日**: 2025-12-30
**対象期間**: 3-6ヶ月
**所要時間**: 160-240時間 (20-30日)
**削減効果**: メンテナンス時間 -75%

---

## エグゼクティブサマリー

### 目的
5つのAI設定フォルダを抜本的に再構築し、`.cursor/` を唯一の真実の源(SSOT)として確立する。他のフォルダは全て参照のみとし、冗長性を最小化する。

### 投資対効果

**現状コスト**:
- 月間: 42-84時間
- 年間: 504-1,008時間

**完全再構築後のコスト**:
- 月間: 10.5-21時間 (-75%)
- 年間: 126-252時間

**削減効果**:
- 年間削減: 378-756時間 (47-94日分)
- 投資回収期間: 3-4ヶ月

**投資内訳**:
- 設計・計画: 40時間
- 実装: 80-120時間
- テスト・検証: 40-80時間

### 主要な変更点

1. **.cursor を SSOT として確立**
   - 全ての実装詳細を .cursor に集約
   - YAMLフロントマター + MDC形式の統一
   - 他フォルダは参照のみ

2. **共有ライブラリの構築**
   - `docs/ai/lib/` ディレクトリを新設
   - 再利用可能なコンポーネント化
   - ツール横断的な共通ロジック

3. **アダプタパターンの徹底**
   - ツール固有の薄いアダプタ層のみ保持
   - カスタマイズは設定ファイルで実現

---

## 1. 新アーキテクチャ設計

### 1.1 階層構造

```
┌─────────────────────────────────────────────────────┐
│         Single Source of Truth (SSOT) Layer        │
│                                                     │
│  .cursor/rules/basic/*.mdc                          │
│  - 00_master_rules.mdc        (ルーティング)        │
│  - pmbok_paths.mdc            (パス定義)            │
│  - 01-06_pmbok_*.mdc          (PMBOK実装)           │
│  - 07_task_management_*.mdc   (タスク管理実装)      │
│  - 08-09_*.mdc                (その他機能)          │
│                                                     │
│  docs/ai/lib/                 (共有ライブラリ)      │
│  - core/                      (コアロジック)        │
│  - templates/                 (テンプレート)        │
│  - validators/                (検証ロジック)        │
└─────────────────────────────────────────────────────┘
                         ↑
                         │ 参照のみ
                         │
┌─────────────────────────────────────────────────────┐
│            Tool-Specific Adapter Layer              │
│                                                     │
│  .agent/                                            │
│  ├── config.yaml           (Antigravity設定)        │
│  ├── workflows/            (スタートアップWF拡張)    │
│  └── adapters/             (Antigravity→SSOT橋渡し) │
│                                                     │
│  .claude/                                           │
│  ├── config.yaml           (Claude Code設定)        │
│  ├── agents/               (エージェント定義)       │
│  └── adapters/             (Claude→SSOT橋渡し)      │
│                                                     │
│  .codex/                                            │
│  ├── config.yaml           (Codex設定)              │
│  └── skills/               (スキルインデックス)     │
└─────────────────────────────────────────────────────┘
```

### 1.2 データフロー

```
ユーザー入力
    ↓
ツール固有インターフェース (.agent/.claude/.codex)
    ↓
アダプタ層 (ツール固有 → 共通フォーマット変換)
    ↓
SSOT参照 (.cursor/rules/ または docs/ai/lib/)
    ↓
実行ロジック (テンプレート適用、検証、ファイル生成)
    ↓
出力 (Flow/Stock フォルダ)
```

---

## 2. フォルダ別再定義

### 2.1 .cursor/ - SSOT層

**役割**: 全ての実装詳細を保持する唯一の真実の源

**新構造**:
```
.cursor/
├── rules/
│   ├── basic/
│   │   ├── 00_master_rules.mdc         (トリガーワードルーティング)
│   │   ├── 00_foundation.mdc           (基礎定義)
│   │   ├── pmbok_paths.mdc             (パス定義 - SPOF)
│   │   ├── 01_pmbok_initiating.mdc     (立ち上げフェーズ)
│   │   ├── 02_pmbok_discovery.mdc      (発見フェーズ)
│   │   ├── 02_pmbok_research.mdc       (リサーチフェーズ)
│   │   ├── 03_pmbok_planning.mdc       (計画フェーズ)
│   │   ├── 04_pmbok_executing.mdc      (実行フェーズ)
│   │   ├── 05_pmbok_monitoring.mdc     (監視フェーズ)
│   │   ├── 06_pmbok_closing.mdc        (終結フェーズ)
│   │   ├── 07_task_management_v3.mdc   (タスク管理 統合版)
│   │   ├── 08_pmbok_flow_assist.mdc    (アイディア発散)
│   │   ├── 09_pmbok_development.mdc    (開発支援)
│   │   └── 90_rule_maintenance.mdc     (ルールメンテナンス)
│   └── advanced/                       (将来拡張用)
├── templates/
│   ├── pmbok/                          (PMBOKテンプレート)
│   ├── tasks/                          (タスク管理テンプレート)
│   └── startup/                        (スタートアップテンプレート)
└── mcp.json                            (MCP設定)
```

**変更点**:
- `07_task_management.mdc` (従来版) を削除
- `07_task_management_ultralight.mdc` を `07_task_management_v3.mdc` にアップグレード
- 全ての機能を v3.0 として統一

### 2.2 docs/ai/ - 共有ライブラリ層

**役割**: ツール非依存の共有ロジックとドキュメント

**新構造**:
```
docs/ai/
├── lib/                                (新設: 共有ライブラリ)
│   ├── core/
│   │   ├── trigger_router.py           (トリガーワードルーティング)
│   │   ├── path_resolver.py            (パス解決ロジック)
│   │   ├── template_engine.py          (テンプレートエンジン)
│   │   └── validator.py                (入力検証)
│   ├── templates/
│   │   ├── pmbok/                      (.cursorから参照)
│   │   ├── tasks/                      (.cursorから参照)
│   │   └── shared/                     (共通テンプレート)
│   └── adapters/
│       ├── antigravity_adapter.py      (Antigravity用)
│       ├── claude_adapter.py           (Claude Code用)
│       └── codex_adapter.py            (Codex用)
├── overview.md                         (既存)
├── pmbok_workflow.md                   (既存)
├── TRIGGER_WORDS_REFERENCE.md          (新規作成)
└── AI_TOOLS_GUIDE.md                   (新規: ツール別使い方)
```

**新設ファイル**:
1. **TRIGGER_WORDS_REFERENCE.md**: 全トリガーワードの統一レジストリ
2. **AI_TOOLS_GUIDE.md**: 各ツールの使い方ガイド
3. **lib/**: 共有Pythonライブラリ

### 2.3 .agent/ - Antigravity特化層

**役割**: Antigravity固有のワークフローと設定

**新構造**:
```
.agent/
├── config.yaml                         (Antigravity設定)
├── workflows/
│   ├── startup/                        (スタートアップWF - 45種維持)
│   │   ├── cpf_validation.md
│   │   ├── pmf_validation.md
│   │   └── ... (他43種)
│   └── custom/                         (カスタムWF)
├── adapters/
│   ├── pmbok_adapter.md                (PMBOK → .cursor 参照)
│   ├── task_adapter.md                 (タスク管理 → .cursor 参照)
│   └── trigger_adapter.md              (トリガー → docs/ai/lib 参照)
└── README.md                           (Antigravity使い方)
```

**変更点**:
- `rules/daily_tasks.md` を削除 → `adapters/task_adapter.md` に変更
- `orchestration/` を削除 → `workflows/startup/` に統合
- 45種のスタートアップWFは維持（Antigravity特化機能）

**削除ファイル**: ~12ファイル

### 2.4 .antigravity/ - 削除・統合

**決定**: `.antigravity/` を完全に削除し、`.agent/` に統合

**理由**:
- 両方ともAntigravity用
- .antigravityは簡易版（500-900バイト/ファイル）
- .agentの方が詳細で高機能
- 重複が大きい

**移行先**:
```
.antigravity/rules/foundation.md    → .agent/README.md に統合
.antigravity/workflows/*.md         → .agent/adapters/*.md に変換
```

**削減**: 12ファイル全削除

### 2.5 .claude/ - Claude Code特化層

**役割**: Claude Code固有のエージェントとスキル

**新構造**:
```
.claude/
├── config.yaml                         (Claude Code設定)
├── agents/                             (11エージェント - 維持)
│   ├── pmbok_agents/
│   └── trading_agents/
├── skills/                             (スキル - 軽量化)
│   ├── daily-tasks-ultralight/         (v3にアップグレード)
│   ├── startup/                        (.agent/workflows 参照)
│   └── trading/                        (19種 - 維持)
├── adapters/
│   ├── pmbok_adapter.md                (PMBOK → .cursor 参照)
│   ├── task_adapter.md                 (タスク → .cursor 参照)
│   └── trigger_adapter.md              (トリガー → docs/ai/lib 参照)
├── commands/                           (削除 → config.yaml に統合)
└── README.md                           (Claude Code使い方)
```

**変更点**:
- `daily/` を削除 → `skills/daily-tasks-ultralight/` にv3として統合
- `rules/*.md` を削除 → `adapters/*.md` に変換
- `commands/*.md` を削除 → `config.yaml` に統合
- トレーディングエージェント19種は維持（Claude特化機能）

**削減**: ~25ファイル

### 2.6 .codex/ - Codexインデックス層

**役割**: Codex用の軽量スキルインデックス（現状維持）

**新構造**:
```
.codex/
├── config.yaml                         (Codex設定)
└── skills/                             (12スキル - 維持)
    ├── task-management/SKILL.md        (.cursor 参照)
    ├── pmbok-initiating/SKILL.md       (.cursor 参照)
    └── ... (他10種)
```

**変更点**:
- 参照先を最新の .cursor/rules/basic/*.mdc に更新
- v3対応

**削減**: 0ファイル（参照先更新のみ）

---

## 3. 詳細実装計画

### フェーズ0: 準備・計画 (Week 1-2, 40時間)

#### 目標
完全な設計と移行計画の確定、ツール準備

#### タスク

| ID | タスク | 所要時間 | 担当 | 成果物 |
|----|--------|---------|------|--------|
| P0.1 | アーキテクチャ詳細設計レビュー | 8h | Architect | 設計書 |
| P0.2 | 移行スクリプト設計 | 8h | Dev | 移行スクリプト仕様 |
| P0.3 | テスト戦略策定 | 6h | QA | テスト計画書 |
| P0.4 | ロールバック計画作成 | 4h | DevOps | ロールバック手順書 |
| P0.5 | バックアップ作成 | 2h | DevOps | フルバックアップ |
| P0.6 | リスク分析ワークショップ | 4h | All | リスク登録簿 |
| P0.7 | ツール準備・環境構築 | 4h | Dev | 開発環境 |
| P0.8 | ステークホルダー承認 | 4h | PM | 承認文書 |

**成果物**:
- [ ] アーキテクチャ詳細設計書 v1.0
- [ ] 移行スクリプト仕様書
- [ ] テスト計画書 v1.0
- [ ] ロールバック手順書
- [ ] フルバックアップ (Git tag: `pre-restructure`)
- [ ] リスク登録簿
- [ ] 開発環境一式

### フェーズ1: SSOT層構築 (Week 3-6, 60時間)

#### 目標
.cursor を完全なSSOTとして確立、docs/ai/lib を構築

#### タスク

| ID | タスク | 所要時間 | 担当 | 優先度 |
|----|--------|---------|------|--------|
| P1.1 | docs/ai/lib/ ディレクトリ構造作成 | 2h | Dev | 🔴 |
| P1.2 | trigger_router.py 実装 | 8h | Dev | 🔴 |
| P1.3 | path_resolver.py 実装 | 6h | Dev | 🔴 |
| P1.4 | template_engine.py 実装 | 10h | Dev | 🔴 |
| P1.5 | validator.py 実装 | 6h | Dev | 🟡 |
| P1.6 | .cursor/rules/basic/07_task_management_v3.mdc 作成 | 8h | Dev | 🔴 |
| P1.7 | TRIGGER_WORDS_REFERENCE.md 作成 | 4h | Writer | 🔴 |
| P1.8 | AI_TOOLS_GUIDE.md 作成 | 6h | Writer | 🟡 |
| P1.9 | 共有テンプレートライブラリ構築 | 10h | Dev | 🟡 |

**成果物**:
- [ ] docs/ai/lib/core/*.py (4ファイル)
- [ ] .cursor/rules/basic/07_task_management_v3.mdc
- [ ] docs/ai/TRIGGER_WORDS_REFERENCE.md
- [ ] docs/ai/AI_TOOLS_GUIDE.md
- [ ] docs/ai/lib/templates/shared/*.md

**テスト**:
- [ ] trigger_router.py 単体テスト
- [ ] path_resolver.py 単体テスト
- [ ] template_engine.py 単体テスト
- [ ] 統合テスト (基本フロー)

### フェーズ2: アダプタ層構築 (Week 7-10, 60時間)

#### 目標
各ツール用のアダプタ層を実装、SSOT参照を確立

#### タスク

| ID | タスク | 所要時間 | 担当 | 優先度 |
|----|--------|---------|------|--------|
| P2.1 | docs/ai/lib/adapters/antigravity_adapter.py | 12h | Dev | 🔴 |
| P2.2 | docs/ai/lib/adapters/claude_adapter.py | 12h | Dev | 🔴 |
| P2.3 | docs/ai/lib/adapters/codex_adapter.py | 8h | Dev | 🟡 |
| P2.4 | .agent/adapters/*.md 作成 (3ファイル) | 6h | Dev | 🔴 |
| P2.5 | .claude/adapters/*.md 作成 (3ファイル) | 6h | Dev | 🔴 |
| P2.6 | .agent/config.yaml 作成 | 4h | Dev | 🔴 |
| P2.7 | .claude/config.yaml 作成 | 4h | Dev | 🔴 |
| P2.8 | .codex/config.yaml 作成 | 2h | Dev | 🟡 |
| P2.9 | 参照関係のテスト | 6h | QA | 🔴 |

**成果物**:
- [ ] docs/ai/lib/adapters/*.py (3ファイル)
- [ ] .agent/adapters/*.md (3ファイル)
- [ ] .claude/adapters/*.md (3ファイル)
- [ ] config.yaml × 3ツール

**テスト**:
- [ ] Antigravityアダプタ テスト
- [ ] Claude Codeアダプタ テスト
- [ ] Codexアダプタ テスト
- [ ] 参照整合性テスト

### フェーズ3: 移行・統合 (Week 11-14, 40-60時間)

#### 目標
.antigravity削除、重複ファイル削減、ツール特化機能の整理

#### タスク

| ID | タスク | 所要時間 | 担当 | 優先度 |
|----|--------|---------|------|--------|
| P3.1 | .antigravity → .agent 統合 | 6h | Dev | 🔴 |
| P3.2 | .antigravity/ 削除 (12ファイル) | 1h | Dev | 🔴 |
| P3.3 | .agent/workflows/startup/ 整理 (45種維持) | 12h | Dev | 🟡 |
| P3.4 | .claude/daily/ → skills/daily-tasks-ultralight/ v3移行 | 8h | Dev | 🔴 |
| P3.5 | .claude/rules/*.md → adapters/*.md 移行 | 6h | Dev | 🔴 |
| P3.6 | .claude/commands/*.md → config.yaml 統合 | 4h | Dev | 🟡 |
| P3.7 | .cursor/07_task_management.mdc 削除 | 0.5h | Dev | 🔴 |
| P3.8 | .codex 参照先更新 (12ファイル) | 3h | Dev | 🟡 |
| P3.9 | 全ファイルの参照関係検証 | 8h | QA | 🔴 |

**成果物**:
- [ ] .antigravity/ 削除完了
- [ ] .agent/ 統合完了
- [ ] .claude/ 軽量化完了
- [ ] .cursor/ v3統一完了
- [ ] .codex/ 参照更新完了

**ファイル削減目標**:
- .antigravity: -12ファイル
- .agent: -12ファイル (冗長削減)
- .claude: -25ファイル (統合・軽量化)
- .cursor: -1ファイル (従来版削除)
- **合計: -50ファイル (-26%)**

### フェーズ4: 包括的テスト (Week 15-16, 40時間)

#### 目標
全ツール・全ワークフローの動作検証

#### タスク

| ID | タスク | 所要時間 | 担当 | 優先度 |
|----|--------|---------|------|--------|
| P4.1 | PMBOKフェーズ統合テスト (7フェーズ × 3ツール) | 16h | QA | 🔴 |
| P4.2 | タスク管理統合テスト (4コマンド × 3ツール) | 8h | QA | 🔴 |
| P4.3 | スタートアップWFテスト (45種 × Antigravity) | 8h | QA | 🟡 |
| P4.4 | トレーディングエージェントテスト (19種 × Claude) | 4h | QA | 🟡 |
| P4.5 | パフォーマンステスト | 2h | QA | 🟢 |
| P4.6 | バグ修正 | 12h | Dev | 🔴 |

**テストケース**:
- [ ] PMBOK 7フェーズ × 3ツール = 21ケース
- [ ] Ultra Light 4コマンド × 3ツール = 12ケース
- [ ] スタートアップWF 45種 × Antigravity = 45ケース
- [ ] トレーディング 19種 × Claude = 19ケース
- **合計: 97ケース**

**合格基準**:
- 成功率: 95%以上
- 重大バグ: 0件
- 中バグ: 3件以下

### フェーズ5: ドキュメント・デプロイ (Week 17-18, 20時間)

#### 目標
ドキュメント整備、デプロイ、ユーザー教育

#### タスク

| ID | タスク | 所要時間 | 担当 | 優先度 |
|----|--------|---------|------|--------|
| P5.1 | 移行ガイド作成 | 4h | Writer | 🔴 |
| P5.2 | CHANGELOG.md 作成 | 2h | Writer | 🔴 |
| P5.3 | 各フォルダのREADME更新 | 4h | Writer | 🟡 |
| P5.4 | AI_TOOLS_GUIDE.md 完成 | 4h | Writer | 🔴 |
| P5.5 | Git tag作成 (`v3.0.0`) | 0.5h | DevOps | 🔴 |
| P5.6 | デプロイ | 2h | DevOps | 🔴 |
| P5.7 | ユーザー通知・教育 | 3.5h | PM | 🟡 |

**成果物**:
- [ ] MIGRATION_GUIDE.md
- [ ] CHANGELOG.md
- [ ] README.md × 5フォルダ
- [ ] AI_TOOLS_GUIDE.md (完成版)
- [ ] Git tag: `v3.0.0`
- [ ] デプロイ完了

---

## 4. リスク管理と対策

### 4.1 高リスク項目

#### R1: 既存ワークフロー完全破壊 🔴
- **確率**: 中 (40%)
- **影響**: 致命的
- **シナリオ**: 移行ミスにより全ツールが動作不能
- **対策**:
  1. **フルバックアップ必須**: Git tag `pre-restructure`
  2. **段階的移行**: フェーズ1→2→3の厳密な順守
  3. **各フェーズでテスト**: 次フェーズ開始前に必ずテスト合格
  4. **ロールバック計画**: 各フェーズで即座に戻せる手順
  5. **カナリアデプロイ**: 一部ユーザーで先行テスト

#### R2: Cursor SPOF (Single Point of Failure) 🔴
- **確率**: 低 (15%)
- **影響**: 致命的
- **シナリオ**: .cursor が破損すると全システム停止
- **対策**:
  1. **自動バックアップ**: 日次で .cursor をバックアップ
  2. **バージョン管理強化**: Git + 日次コミット
  3. **冗長化オプション**: docs/ai/lib にコアロジックを分散
  4. **監視**: .cursor の変更を自動検知・通知

#### R3: ツール固有カスタマイズ困難 🟡
- **確率**: 高 (60%)
- **影響**: 高
- **シナリオ**: ツール特有のニーズに対応できない
- **対策**:
  1. **config.yaml で柔軟性確保**: ツール別設定ファイル
  2. **アダプタ層の拡張性**: カスタムロジックをアダプタに記述可能
  3. **プラグイン機構**: 将来的にプラグイン対応を検討
  4. **フィードバックループ**: ユーザーからの要望を即座に反映

#### R4: 移行期間の生産性低下 🟡
- **確率**: 高 (70%)
- **影響**: 中
- **シナリオ**: 3-6ヶ月間、機能追加が停滞
- **対策**:
  1. **並行運用**: 旧システムと新システムを一時的に併存
  2. **段階的移行**: 重要度の低い機能から移行
  3. **クイックウィン**: 早期にメリットを実感できる機能を優先

### 4.2 中リスク項目

#### R5: ドキュメント不足によるユーザー混乱 🟡
- **確率**: 高 (60%)
- **影響**: 中
- **対策**: 移行ガイド、CHANGELOG、AI_TOOLS_GUIDEの充実

#### R6: パフォーマンス劣化 🟢
- **確率**: 中 (30%)
- **影響**: 低
- **対策**: パフォーマンステスト、最適化

### 4.3 リスクマトリックス

| リスク | 確率 | 影響 | 優先度 | 対策コスト |
|--------|------|------|--------|----------|
| R1: ワークフロー破壊 | 中(40%) | 致命的 | 🔴 最高 | 高 |
| R2: Cursor SPOF | 低(15%) | 致命的 | 🔴 最高 | 中 |
| R3: カスタマイズ困難 | 高(60%) | 高 | 🟡 高 | 中 |
| R4: 生産性低下 | 高(70%) | 中 | 🟡 高 | 低 |
| R5: ドキュメント不足 | 高(60%) | 中 | 🟡 高 | 低 |
| R6: パフォーマンス劣化 | 中(30%) | 低 | 🟢 中 | 低 |

---

## 5. ロールバック戦略

### 5.1 緊急ロールバック (即座に実行)

**トリガー**:
- 重大バグ (P0) が3件以上発生
- 成功率が80%未満
- ユーザーから強い反対

**手順**:
```bash
# 1. Git tag に戻す
git checkout pre-restructure

# 2. バックアップから復元
cp -r backup/.agent .agent
cp -r backup/.antigravity .antigravity
cp -r backup/.claude .claude
cp -r backup/.codex .codex
cp -r backup/.cursor .cursor

# 3. 動作確認
./scripts/test_all.sh

# 4. ユーザー通知
```

**所要時間**: 30分

### 5.2 部分ロールバック (フェーズ単位)

各フェーズ完了時にGit commitを作成:
- `phase1-complete`: フェーズ1完了
- `phase2-complete`: フェーズ2完了
- `phase3-complete`: フェーズ3完了

問題発生時は直前のフェーズに戻る。

### 5.3 並行運用戦略

**期間**: フェーズ3-4 (Week 11-16)

**方法**:
- 旧システム: `.agent_old/`, `.claude_old/` にコピー
- 新システム: `.agent/`, `.claude/`
- ユーザーがトグルで切り替え可能

**切り替え**:
```yaml
# config.yaml
system_version: "v3"  # "v2" に変更で旧版に戻る
```

---

## 6. 成功基準とKPI

### 6.1 技術的KPI

| 指標 | 現状 | 目標 | 測定方法 |
|------|------|------|---------|
| **ファイル数** | 192 | 142 (-26%) | ファイルカウント |
| **総行数** | 25,900 | 19,425 (-25%) | wc -l |
| **冗長度** | 543% | 100-120% | 重複行数分析 |
| **SPOF数** | 2 | 1 | 依存関係分析 |
| **月間メンテナンス時間** | 42-84h | 10.5-21h (-75%) | タイムトラッキング |
| **テストカバレッジ** | 0% | 80% | テストスイート |
| **参照整合性エラー** | 4-8件/月 | 0件/月 | 自動検証 |

### 6.2 ユーザー体験KPI

| 指標 | 現状 | 目標 | 測定方法 |
|------|------|------|---------|
| **トリガー発見時間** | 15-30分 | 2-5分 (-83%) | ユーザー調査 |
| **ワークフロー成功率** | 85-90% | 98% | ログ分析 |
| **平均エラー解決時間** | 2-4時間 | 30分-1時間 | イシュー追跡 |
| **ユーザー満足度** | - | 8/10以上 | アンケート |

### 6.3 ビジネスKPI

| 指標 | 現状 | 目標 | 測定方法 |
|------|------|------|---------|
| **年間メンテナンスコスト** | 504-1,008h | 126-252h (-75%) | 工数集計 |
| **投資回収期間** | - | 3-4ヶ月 | ROI計算 |
| **年間削減効果** | - | 378-756h | 削減時間集計 |
| **技術的負債削減率** | - | 75% | コード品質分析 |

### 6.4 必達条件 (Go/No-Go)

フェーズ4終了時点で以下を満たす必要あり:

- [ ] テスト成功率 ≥ 95%
- [ ] 重大バグ (P0) = 0件
- [ ] 中バグ (P1) ≤ 3件
- [ ] ファイル削減率 ≥ 20%
- [ ] 冗長度削減率 ≥ 60%
- [ ] 全ツールで基本ワークフロー動作確認

**満たさない場合**: フェーズ5延期、追加修正

---

## 7. 実装ロードマップ (ガントチャート)

```
Month 1 (Week 1-4)
Week 1-2:  [P0: 準備・計画 ████████████████████] 40h
Week 3-4:  [P1: SSOT層構築 ████████████████████] 60h (前半)

Month 2 (Week 5-8)
Week 5-6:  [P1: SSOT層構築 ████████████████████] 60h (後半)
Week 7-8:  [P2: アダプタ層  ████████████████████] 60h (前半)

Month 3 (Week 9-12)
Week 9-10:  [P2: アダプタ層  ████████████████████] 60h (後半)
Week 11-12: [P3: 移行・統合  ████████████████████] 40-60h (前半)

Month 4 (Week 13-16)
Week 13-14: [P3: 移行・統合  ████████████████████] 40-60h (後半)
Week 15-16: [P4: テスト      ████████████████████] 40h

Month 5 (Week 17-18)
Week 17-18: [P5: デプロイ    ████████████████████] 20h

Month 6 (継続的改善)
Week 19-26: [監視・最適化    ░░░░░░░░░░░░░░░░░░░░] 継続
```

**クリティカルパス**:
P0 → P1 → P2 → P3 → P4 → P5

**並行可能タスク**:
- P1.7, P1.8 (ドキュメント) ∥ P1.2-P1.6 (実装)
- P4.1-P4.4 (テスト) ∥ P4.6 (バグ修正)

---

## 8. コスト詳細

### 8.1 人件費

**想定レート**:
- Architect: 80 USD/h
- Senior Dev: 60 USD/h
- Dev: 50 USD/h
- QA: 45 USD/h
- Technical Writer: 40 USD/h
- PM: 70 USD/h

**フェーズ別コスト**:

| フェーズ | 工数 | 主担当 | 概算コスト |
|---------|------|--------|----------|
| P0: 準備・計画 | 40h | Architect | 3,200 USD |
| P1: SSOT層構築 | 60h | Dev | 3,000 USD |
| P2: アダプタ層 | 60h | Dev | 3,000 USD |
| P3: 移行・統合 | 40-60h | Dev | 2,000-3,000 USD |
| P4: テスト | 40h | QA + Dev | 2,100 USD |
| P5: デプロイ | 20h | Writer + PM | 1,100 USD |
| **合計** | **160-240h** | - | **14,400-16,400 USD** |

### 8.2 ツール・インフラコスト

| 項目 | コスト | 備考 |
|------|--------|------|
| Git LFS (追加容量) | 5 USD/月 | バックアップ用 |
| CI/CD (GitHub Actions) | 無料 | 既存枠内 |
| 監視ツール | 無料 | オープンソース |
| **合計** | **5 USD/月** | - |

### 8.3 総コスト

**初期投資**: 14,400-16,400 USD
**月間運用コスト**: 5 USD
**年間運用コスト**: 60 USD

**現状の年間コスト** (メンテナンス):
- 504-1,008h × 50 USD/h = 25,200-50,400 USD

**再構築後の年間コスト** (メンテナンス):
- 126-252h × 50 USD/h = 6,300-12,600 USD

**年間削減額**: 18,900-37,800 USD

**ROI**: (18,900-37,800) / (14,400-16,400) = **1.15-2.62倍**

**投資回収期間**: 5-10ヶ月

---

## 9. ツール別影響分析

### 9.1 Antigravity

**現状**:
- .agent/: 50ファイル
- .antigravity/: 12ファイル

**再構築後**:
- .agent/: 38ファイル (-24%)
  - workflows/startup/: 45種維持
  - adapters/: 3ファイル (新設)
  - config.yaml: 1ファイル (新設)
- .antigravity/: 削除

**影響**:
- ✅ スタートアップWF 45種は維持
- ✅ 参照先が .cursor に統一され、メンテナンスが楽に
- ⚠️ .antigravity 削除によるトリガーワード変更なし（.agentに統合）

**ユーザー体験**:
- トリガーワード: 変更なし
- ワークフロー: 変更なし
- パフォーマンス: 軽微な改善

### 9.2 Claude Code

**現状**:
- .claude/: 100ファイル

**再構築後**:
- .claude/: 75ファイル (-25%)
  - agents/: 11ファイル維持
  - skills/: 軽量化
  - adapters/: 3ファイル (新設)
  - config.yaml: 1ファイル (新設)

**影響**:
- ✅ トレーディングエージェント19種は維持
- ✅ Ultra Light v3にアップグレード
- ⚠️ daily/ フォルダ削除 → skills/daily-tasks-ultralight/ に統合

**ユーザー体験**:
- トリガーワード: v3対応（下位互換あり）
- 新機能: タスクプロンプト生成
- パフォーマンス: 改善

### 9.3 Cursor IDE

**現状**:
- .cursor/: 18+ファイル

**再構築後**:
- .cursor/: 17ファイル (-1ファイル)
  - 従来版削除
  - v3統一

**影響**:
- ✅ SSOTとして明確化
- ✅ v3.0として全機能統一
- ⚠️ 従来版(07_task_management.mdc)削除

**ユーザー体験**:
- トリガーワード: 変更なし
- ワークフロー: v3にアップグレード
- パフォーマンス: 変更なし

### 9.4 Codex

**現状**:
- .codex/: 12ファイル

**再構築後**:
- .codex/: 12ファイル (変更なし)
  - 参照先を v3 に更新

**影響**:
- ✅ ファイル構造変更なし
- ✅ 参照先が最新版に

**ユーザー体験**:
- トリガーワード: 変更なし
- ワークフロー: v3対応
- パフォーマンス: 変更なし

---

## 10. 移行チェックリスト

### 事前準備

- [ ] ステークホルダー承認取得
- [ ] アーキテクチャ詳細設計レビュー完了
- [ ] Git tag `pre-restructure` 作成
- [ ] フルバックアップ作成
- [ ] 開発環境構築完了
- [ ] テスト計画書承認
- [ ] ロールバック手順書作成完了

### フェーズ0 (準備・計画)

- [ ] アーキテクチャ詳細設計書 v1.0
- [ ] 移行スクリプト仕様書
- [ ] テスト計画書 v1.0
- [ ] ロールバック手順書
- [ ] リスク登録簿
- [ ] 開発環境一式

### フェーズ1 (SSOT層構築)

- [ ] docs/ai/lib/core/trigger_router.py
- [ ] docs/ai/lib/core/path_resolver.py
- [ ] docs/ai/lib/core/template_engine.py
- [ ] docs/ai/lib/core/validator.py
- [ ] .cursor/rules/basic/07_task_management_v3.mdc
- [ ] docs/ai/TRIGGER_WORDS_REFERENCE.md
- [ ] docs/ai/AI_TOOLS_GUIDE.md
- [ ] 単体テスト完了
- [ ] 統合テスト完了
- [ ] Git commit `phase1-complete`

### フェーズ2 (アダプタ層構築)

- [ ] docs/ai/lib/adapters/antigravity_adapter.py
- [ ] docs/ai/lib/adapters/claude_adapter.py
- [ ] docs/ai/lib/adapters/codex_adapter.py
- [ ] .agent/adapters/*.md (3ファイル)
- [ ] .claude/adapters/*.md (3ファイル)
- [ ] .agent/config.yaml
- [ ] .claude/config.yaml
- [ ] .codex/config.yaml
- [ ] アダプタテスト完了
- [ ] 参照整合性テスト完了
- [ ] Git commit `phase2-complete`

### フェーズ3 (移行・統合)

- [ ] .antigravity → .agent 統合完了
- [ ] .antigravity/ 削除 (12ファイル)
- [ ] .agent/workflows/startup/ 整理完了
- [ ] .claude/daily/ → skills/daily-tasks-ultralight/ 移行完了
- [ ] .claude/rules/*.md → adapters/*.md 移行完了
- [ ] .claude/commands/*.md → config.yaml 統合完了
- [ ] .cursor/07_task_management.mdc 削除
- [ ] .codex 参照先更新 (12ファイル)
- [ ] 全ファイルの参照関係検証完了
- [ ] ファイル削減目標達成 (-50ファイル)
- [ ] Git commit `phase3-complete`

### フェーズ4 (包括的テスト)

- [ ] PMBOKフェーズ統合テスト (21ケース)
- [ ] タスク管理統合テスト (12ケース)
- [ ] スタートアップWFテスト (45ケース)
- [ ] トレーディングエージェントテスト (19ケース)
- [ ] パフォーマンステスト
- [ ] テスト成功率 ≥ 95%
- [ ] 重大バグ (P0) = 0件
- [ ] 中バグ (P1) ≤ 3件
- [ ] バグ修正完了
- [ ] Git commit `phase4-complete`

### フェーズ5 (デプロイ)

- [ ] MIGRATION_GUIDE.md 作成
- [ ] CHANGELOG.md 作成
- [ ] README.md 更新 (5フォルダ)
- [ ] AI_TOOLS_GUIDE.md 完成
- [ ] Git tag `v3.0.0` 作成
- [ ] デプロイ完了
- [ ] ユーザー通知・教育完了
- [ ] メトリクス収集開始

### 事後確認

- [ ] KPI目標達成確認
- [ ] ユーザーフィードバック収集
- [ ] バグトラッキング開始
- [ ] 継続的改善プロセス確立
- [ ] レトロスペクティブ実施
- [ ] 最終レポート作成

---

## 11. FAQ

### Q1: プランBとプランCの違いは?

**プランB (戦略的統合)**:
- 所要時間: 48時間 (6日)
- 削減効果: -67%
- アプローチ: 重複削減、マスター明確化
- 各フォルダに実装詳細を残す

**プランC (完全再構築)**:
- 所要時間: 160-240時間 (20-30日)
- 削減効果: -75%
- アプローチ: SSOT確立、全て参照化
- .cursor のみに実装詳細

### Q2: なぜ .cursor をSSOTに選んだのか?

**理由**:
1. **最も包括的**: 18+ファイル、最も詳細な実装
2. **既に参照されている**: .codex が参照中
3. **YAMLフロントマター**: 構造化されたメタデータ
4. **番号付き優先度**: 明確な階層構造

### Q3: ツール固有機能はどう扱う?

**スタートアップWF (Antigravity)**:
- .agent/workflows/startup/ に維持
- 45種のWFは削除しない

**トレーディングエージェント (Claude)**:
- .claude/agents/trading/ に維持
- 19種のエージェントは削除しない

**ツール固有機能は尊重**します。

### Q4: 移行中も使い続けられる?

**Yes**:
- フェーズ3-4で並行運用可能
- config.yaml で旧版/新版を切り替え
- 問題発生時は即座にロールバック

### Q5: 投資回収期間は本当に3-4ヶ月?

**計算根拠**:
- 初期投資: 14,400-16,400 USD
- 年間削減額: 18,900-37,800 USD
- 月間削減額: 1,575-3,150 USD
- 回収期間: 14,400 / 3,150 = **4.6ヶ月** (最悪ケース)
- 回収期間: 16,400 / 1,575 = **10.4ヶ月** (保守的見積もり)

**現実的には 5-10ヶ月**が妥当です。

### Q6: リスクが高すぎるのでは?

**対策済み**:
- R1 (ワークフロー破壊): 段階的移行、テスト、ロールバック計画
- R2 (SPOF): 自動バックアップ、冗長化オプション
- R3 (カスタマイズ困難): config.yaml、アダプタ層で柔軟性確保
- R4 (生産性低下): 並行運用、段階的移行

**リスクは管理可能**です。

### Q7: プランBで十分では?

**プランCの追加メリット**:
- メンテナンス削減: 67% → **75%**
- 技術的負債削減: 50% → **75%**
- 長期的な保守性: 大幅向上
- 新機能追加の容易さ: 向上

**トレードオフ**:
- 投資: 48h → **160-240h**
- リスク: 低 → **中**

**判断ポイント**:
- 長期運用 (1年以上) → **プランC推奨**
- 短期・リスク回避 → プランB推奨

---

## 12. 結論と推奨事項

### 12.1 プランCが適している場合

✅ **以下に該当する場合、プランCを推奨**:

1. **長期運用を想定** (1年以上)
2. **技術的負債の抜本的削減が必要**
3. **メンテナンスリソースが限られている**
4. **高い投資対効果を求める** (ROI 1.15-2.62倍)
5. **統一されたアーキテクチャが重要**

### 12.2 プランBの方が適している場合

⚠️ **以下に該当する場合、プランBを推奨**:

1. **短期間で成果が必要** (1-2週間)
2. **リスクを最小化したい**
3. **段階的な改善を好む**
4. **ツール固有カスタマイズが頻繁**
5. **投資予算が限られている** (48時間まで)

### 12.3 最終推奨

**状況**: aipm_v0は長期運用プロジェクトで、複数のAIツールを均等に使用

**推奨**: **プランCを実施**

**理由**:
1. 年間削減効果が非常に大きい (378-756時間)
2. 投資回収期間が妥当 (5-10ヶ月)
3. リスクは管理可能（段階的移行、ロールバック計画）
4. 長期的な保守性が大幅に向上
5. 技術的負債を75%削減できる

**ただし条件**:
- フェーズ0で徹底的な準備
- 各フェーズでテスト合格を必須
- ロールバック計画を常に準備
- ユーザーフィードバックを継続的に収集

### 12.4 次のアクション

1. **承認取得**: 本実装計画書をレビューし、承認
2. **フェーズ0開始**: Week 1-2で準備・計画 (40時間)
3. **マイルストーン設定**: 各フェーズ終了時に進捗確認
4. **Go/No-Go判断**: フェーズ4終了時に最終判断

---

**計画書作成者**: Claude Sonnet 4.5
**作成日**: 2025-12-30
**バージョン**: v1.0
**推定読了時間**: 60分

---

## 付録A: 用語集

- **SSOT (Single Source of Truth)**: 唯一の真実の源。全ての情報が一箇所に集約される設計パターン
- **SPOF (Single Point of Failure)**: 単一障害点。1箇所の故障でシステム全体が停止する箇所
- **Ultra Light**: タスクを考えない3-4コマンド運用のタスク管理システム
- **Adapter Pattern**: 異なるインターフェース間を橋渡しするデザインパターン
- **ROI (Return on Investment)**: 投資対効果。投資額に対する利益の割合
- **Canary Deploy**: 一部のユーザーで先行テストしてからフルデプロイする手法

## 付録B: 関連ドキュメント

- **現状分析**: `AI_FOLDERS_COMPREHENSIVE_REVIEW.md`
- **タスク管理分析**: `task_management_analysis_report.md`
- **トリガーワード分析**: `trigger_word_conflict_analysis.md`
- **メンテナンス負荷評価**: `maintenance_burden_assessment.md`
- **元の計画書**: `/Users/yuichi/.claude/plans/enumerated-wishing-journal.md`

## 付録C: 連絡先

質問や承認が必要な場合は、本計画書を参照してフォローアップしてください。
