---
name: create-mvv
description: |
  MVV（Mission/Vision/Values）を早期定義する自律実行型スキル。ビジネスアイデアまたはリーンキャンバスから、Mission（存在意義）、Vision（目指す未来）、Values（行動指針3-5個）を自動生成。MVV内部整合性とLean Canvas整合性を検証し、5項目チェックで完成度を判定します。

  使用タイミング：
  - ビジネスアイデアが固まった段階
  - リーンキャンバス作成後
  - 組織の理念を明確化したい

  所要時間：20-40分（自動実行）
  出力：mvv.md
---

# Create MVV Skill

MVV（Mission/Vision/Values）を早期定義する自律実行型Skill。

---

## このSkillでできること

1. **Mission定義**: 何のために存在するか（存在意義）を明確化
2. **Vision定義**: どこを目指すか（目指す未来）を描画
3. **Values定義**: どう行動するか（行動指針）を策定
4. **整合性検証**: MVV 3要素の相互整合性を確認
5. **Lean Canvas整合**: リーンキャンバスとの整合性を検証

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `business_idea.md` (オプション), `lean_canvas.md` (オプション) |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/1_initiating/mvv.md` |
| **次のSkill** | `/build-flywheel` または `/orchestrate-phase1` |

### 入力ファイル詳細

| ファイル | パス | 必須/オプション | 未存在時の動作 |
|---------|------|----------------|--------------|
| business_idea.md | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/1_initiating/business_idea.md` | オプション | demand_discovery.mdから推論 |
| lean_canvas.md | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/2_discovery/lean_canvas.md` | オプション | business_idea.mdから推論 |

**フォールバック戦略**:
1. lean_canvas.md → business_idea.md → demand_discovery.md → ユーザー入力から推論

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 20-40分

### 自動実行ステップ

1. ビジネスアイデア・リーンキャンバス読み込み
2. ベンチマーク企業MVV調査
3. Mission草案作成（1-2文、30秒で読める）
4. Vision草案作成（3-5年後の理想状態、定量目標含む）
5. Values草案作成（3-5個の行動指針）
6. MVV整合性検証（Mission→Vision→Values）
7. Lean Canvas整合性検証（Problem/UVP/Solution整合）
8. 成果物出力

### 判定基準（5項目チェック）

| 項目 | 合格条件 |
|------|----------|
| Mission明確性 | 30秒で読め、社会的意義が明確 |
| Vision具体性 | イメージ可能、測定可能要素あり |
| Values実用性 | 3-5個、具体的行動につながる |
| MVV整合性 | Mission→Vision→Values整合（3/3） |
| Lean Canvas整合 | Problem/UVP/Solution整合（3/3） |

**総合判定**:
- 5/5: ✅ MVV完了 → 次のステップへ
- 3-4/5: ⚠️ 要改善 → 不合格項目を再作成
- 0-2/5: ❌ 再定義 → ビジネスアイデア見直し

---

## Knowledge Base参照

- MVV概念: `@startup_science/02_frameworks/mvv/mvv_overview.md`
- リーンキャンバス: `@startup_science/02_frameworks/lean_canvas/lean_canvas_overview.md`
