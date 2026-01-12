---
name: build-flywheel
description: |
  成長を加速させるフライホイールを設計する自律実行型スキル。Viral/Sticky/Paidから最適な成長エンジンを選定し、6-8ステップの成長サイクルを構造化。完全性（サイクル完結性）、接続ロジック（因果関係）、NE（ネガティブ要因）特定、KPI設定を行い、Mermaid図で可視化します。10点満点で評価。

  使用タイミング：
  - リーンキャンバス作成後
  - 成長戦略を設計したい
  - フライホイール構造を可視化したい

  所要時間：30-50分（自動実行）
  出力：flywheel.md（Mermaid図含む）
---

# Build Flywheel Skill

成長を加速させるフライホイールを設計する自律実行型Skill。

---

## このSkillでできること

1. **成長エンジン選定**: Viral/Sticky/Paidから最適なエンジンを選択
2. **フライホイール設計**: 成長サイクルの構造化（Mermaid図）
3. **完全性検証**: サイクルが完結しているかチェック
4. **接続ロジック確認**: 各ステップの因果関係を明確化
5. **KPI設定**: 各ステップの測定指標を定義

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `persona.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/3_planning/flywheel.md` |
| **次のSkill** | `/validate-cpf` または `/validate-10x` |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-50分

### 自動実行ステップ

1. リーンキャンバス・ペルソナ読み込み
2. ベンチマーク企業フライホイール調査
3. 成長エンジン選定（Viral/Sticky/Paid）
4. フライホイール構造設計（6-8ステップ）
5. 完全性検証（サイクル完結性）
6. 接続ロジック確認（因果関係）
7. NE（ネガティブ要因）特定
8. KPI設定
9. Mermaid図生成
10. 成果物出力

### 成長エンジン選定基準

| エンジン | 適用条件 |
|---------|---------|
| Viral   | ユーザー→ユーザー紹介が自然発生する |
| Sticky  | LTV最大化、継続利用が核心価値 |
| Paid    | CACをLTVが大きく上回る |

### 判定基準（10点満点）

| 評価項目 | 配点 |
|---------|:----:|
| 成長エンジン選定 | 2点 |
| 完全性 | 2点 |
| 接続ロジック | 2点 |
| NE特定 | 2点 |
| KPI設定 | 2点 |

**総合判定**:
- 8-10点: ✅ 完了 → 次のステップへ
- 5-7点: ⚠️ 要改善 → 低スコア項目を再設計
- 0-4点: ❌ 再設計 → フライホイール全体見直し

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **WebSearch失敗**: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## Knowledge Base参照

- フライホイール概念: `@startup_science/03_tactics/flywheel/flywheel_design.md`
- リーンキャンバス: `@startup_science/02_frameworks/lean_canvas/lean_canvas_overview.md`
