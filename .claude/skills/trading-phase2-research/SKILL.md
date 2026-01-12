---
name: trading-phase2-research
description: |
  Phase2リサーチチーム全体を自律実行するオーケストレータースキル。
  Bull/Bearシナリオ構築→統合判断の3ステップを順次実行（30-45分）。
  期待リターン計算、Risk/Reward分析で最終推奨を決定。
  Phase3リスク管理チームへの引き継ぎ事項を明確化。

  使用タイミング：
  - Phase1完了後、シナリオ分析を開始する時
  - Phase2を一気通貫で実行したい

  所要時間：30-45分（自動実行）
  出力：research_consensus.md

trigger_keywords:
  - "Phase2実行"
  - "シナリオ分析"
  - "リサーチ開始"

stage: Phase2 - Research Team

dependencies:
  - agent-bull-researcher
  - agent-bear-researcher
  - agent-research-manager

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

execution_time: 30-45分（自動実行）

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P1

framework_compliance: 100%
---

# Trading Phase2 Research Orchestrator Skill

Phase2リサーチチーム全体を自律実行するオーケストレーターSkill。

---

## このSkillでできること

1. **Phase2全自動実行**: 3エージェントを順次実行
2. **ステージゲート管理**: 3エージェント完了・最終推奨明確確認
3. **統合分析**: Bull/Bearシナリオの期待値統合
4. **進捗管理**: 各エージェントの完了状況を可視化
5. **最終評価**: 期待リターン・Risk/Reward比率で総合判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `analysts_summary.md`（Phase1結果） |
| **出力** | Phase2全成果物（`bull_scenario.md`, `bear_scenario.md`, `research_consensus.md`） |
| **次のSkill** | Phase3へ進む（trading-phase3-risk） |

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 30-45分

### 前提条件確認

#### ステップ1: 環境情報取得

1. **Phase1結果確認**: `analysts_summary.md` 存在確認
2. **出力先確認**: `Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/2025-12-29/`

### Phase2実行ステップ（全3エージェント）

**注意**: Claude Code は並列実行非対応のため順次実行。

#### エージェント1: Bull Researcher（強気シナリオ構築）

**実行**: `/agent-bull-researcher`

**推定時間**: 15-25分

**期待成果物**:
- `bull_scenario.md`
- 強気シナリオ確率・目標価格
- 期待リターン（プラス）
- リスク要因明記

**完了確認**:
- [ ] `bull_scenario.md` 存在確認
- [ ] 実現確率XX%明記
- [ ] 目標価格・期待リターン明記
- [ ] WebSearch実行履歴 3件以上

---

#### エージェント2: Bear Researcher（弱気シナリオ構築）

**実行**: `/agent-bear-researcher`

**推定時間**: 15-25分

**期待成果物**:
- `bear_scenario.md`
- 弱気シナリオ確率・目標価格
- 期待リターン（マイナス）
- リスク要因明記

**完了確認**:
- [ ] `bear_scenario.md` 存在確認
- [ ] 実現確率XX%明記
- [ ] 目標価格・期待リターン明記
- [ ] WebSearch実行履歴 3件以上

---

#### エージェント3: Research Manager（シナリオ統合判断）

**実行**: `/agent-research-manager`

**推定時間**: 10-20分

**期待成果物**:
- `research_consensus.md`
- 期待リターン計算
- Risk/Reward比率
- 最終推奨（ロング/ショート/中立/見送り）
- Phase3引き継ぎ事項

**完了確認**:
- [ ] `research_consensus.md` 存在確認
- [ ] 期待リターン計算完了
- [ ] Risk/Reward比率算出
- [ ] 最終推奨明記

---

### ステージゲート判定

**ステージゲート2: Phase2完了確認**

- **合格条件**:
  1. 3エージェント全実行完了
  2. 各エージェントの成果物存在
  3. Bull/Bearシナリオに確率・リターン明記
  4. 期待リターン計算完了
  5. 最終推奨明確（ロング/ショート/中立/見送り）

- **未達成時**: 停止（Human-in-the-Loop必須）
  - 不足エージェント特定
  - 再実行 or データソース追加WebSearch
  - 最大3回リトライ

**チェックリスト**:
```markdown
Phase2 完了確認:
- [ ] agent-bull-researcher 完了
- [ ] agent-bear-researcher 完了
- [ ] agent-research-manager 完了
- [ ] 期待リターン計算完了
- [ ] Risk/Reward比率 ≥ 1.0
- [ ] 最終推奨明確
```

---

### 統合サマリー生成

#### ステップ2: 各成果物読み込み

```markdown
1. Read: `bull_scenario.md`
   - 実現確率: XX%
   - 期待リターン: +X.X%

2. Read: `bear_scenario.md`
   - 実現確率: XX%
   - 期待リターン: -X.X%

3. Read: `research_consensus.md`
   - 期待リターン: +X.XX% or -X.XX%
   - Risk/Reward比率: X.XX
   - 最終推奨: [ロング/ショート/中立/見送り]
```

---

## 成果物

### 最終成果物一覧

```
TradingAgents/data/results/phase2/2025-12-29/
├── bull_scenario.md         ✅ Bull Researcher
├── bear_scenario.md         ✅ Bear Researcher
└── research_consensus.md    ✅ Research Manager（最終成果物）
```

---

## Knowledge Base参照

- Bull Researcher: `.claude/skills/agent-bull-researcher/SKILL.md`
- Bear Researcher: `.claude/skills/agent-bear-researcher/SKILL.md`
- Research Manager: `.claude/skills/agent-research-manager/SKILL.md`
- Phase1結果: `@Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md`

---

## 使用例

```
User: /trading-phase2-research

Skill:
# Phase2 Research Team 自律実行開始

入力: analysts_summary.md
推定所要時間: 30-45分

[自動実行中...]

## エージェント1: Bull Researcher ✅ 完了（18分）
- 実現確率: 62%
- 目標価格: 34,200円（+3.8%）
- 主要根拠: テクニカル強気6/8、Tailwinds優勢

## エージェント2: Bear Researcher ✅ 完了（17分）
- 実現確率: 38%
- 目標価格: 32,000円（-2.8%）
- 主要根拠: RSI買われすぎ、レジスタンス接近

## エージェント3: Research Manager ✅ 完了（15分）
- 期待リターン: (0.62×+3.8%) + (0.38×-2.8%) = +1.29%
- Risk/Reward比率: 3.8/2.8 = 1.36
- 最終推奨: ロング（慎重）
- 確信度: 中

## ステージゲート判定 ✅ 通過
- 3エージェント全完了
- 期待リターン: +1.29%（ポジティブ）
- Risk/Reward比率: 1.36（≥1.0 合格）
- 最終推奨: ロング（慎重）

## Phase2 完了

総実行時間: 50分
最終推奨: ロング（慎重）
期待リターン: +1.29%
Risk/Reward: 1.36

次のアクション:
1. Phase3へ進む（/trading-phase3-risk）
2. Phase2結果精査
3. 個別シナリオ詳細確認

成果物: research_consensus.md 生成完了
```
