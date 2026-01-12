---
name: research-problem
description: |
  ForSolo Edition: ソロプレナー向け課題裏付けスキル。
  Web上の生ログから課題の裏付けを発見し、5軸（頻度/深刻度/既存策不満/支払い匂い/緊急性）で50点満点スコアリング。
  定性インサイト抽出、既存代替案分析を実施し、課題仮説の裏付けを判定します。

  使用タイミング：
  - リーンキャンバス作成後
  - 課題仮説の裏付けを確認したい
  - CPF検証の補強材料が欲しい

  所要時間：30-60分（自動実行）
  出力：problem_research.md
---

# Research Problem Skill (ForSolo Edition)

ソロプレナー向け課題裏付けスキル。Web上の生ログから課題を発見し、1人実行可能性を重視。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Yahoo!知恵袋/X/Stack Overflow/IndieHackers等から「困りごと」を収集
2. **5軸スコアリング**: 頻度/深刻度/既存策不満/支払い匂い/緊急性で評価（50点満点）
3. **定性インサイト抽出**: 生の声から本質的課題を発見
4. **既存代替案分析**: 何が使われていて、何が不満か
5. **課題裏付け判定**: 仮説が正しいかを判定
6. **[ForSolo追加]** IndieHackersコミュニティからの収集強化

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`（必須）, `lean_canvas.md`（オプション） |
| **フォールバック** | persona.md未存在時 → demand_discovery.mdから課題情報を取得 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/problem_research.md` |
| **次のSkill** | `/for-solo-validate-cpf` |
| **ステージ** | CPF検証（ForSolo特化） |

---

## Knowledge Base参照

### ForSolo Edition専用
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Solopreneur_Research/documents/01_App/case_studies/*.md`
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies/research-problem/*.md`

### 共通Knowledge Base
- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/customer_interview.md
- @startup_science/01_stages/cpf/persona_creation.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md

---

## Solopreneur固有ドメイン知識

### IndieHackersコミュニティ重視
- **IndieHackers**: ソロプレナーのリアルな悩みが集まる
- **Product Hunt**: 成功事例と失敗事例の両方から学ぶ
- **X/Twitter**: Build in Publicを実践する創業者の生ログ

---

## 更新履歴

- 2026-01-02: ForSolo Edition作成（IndieHackers重視）
