---
name: research-problem
description: |
  Web上の生ログから課題の裏付けを発見する自律実行型スキル。Reddit、Yahoo!知恵袋、X、Stack Overflow等から「困りごと」を30件以上収集し、5軸（頻度/深刻度/既存策不満/支払い匂い/緊急性）で50点満点スコアリング。定性インサイト抽出、既存代替案分析を実施し、課題仮説の裏付けを判定します。

  使用タイミング：
  - リーンキャンバス作成後
  - 課題仮説の裏付けを確認したい
  - CPF検証の補強材料が欲しい

  所要時間：30-60分（自動実行）
  出力：problem_research.md
---

# Research Problem Skill

Web上の生ログから課題の裏付けを発見する自律実行型Skill。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Yahoo!知恵袋/X/Stack Overflow等から「困りごと」を収集
2. **5軸スコアリング**: 頻度/深刻度/既存策不満/支払い匂い/緊急性で評価（50点満点）
3. **定性インサイト抽出**: 生の声から本質的課題を発見
4. **既存代替案分析**: 何が使われていて、何が不満か
5. **課題裏付け判定**: 仮説が正しいかを判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`（必須）, `lean_canvas.md`（オプション） |
| **フォールバック** | persona.md未存在時 → demand_discovery.mdから課題情報を取得 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/2_discovery/problem_research.md` |
| **次のSkill** | `/validate-cpf` |
| **ステージ** | CPF検証 |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-60分

### 自動実行ステップ

1. リーンキャンバス・ペルソナ読み込み
2. 検索クエリ生成（日本語・英語各10個以上）
3. 生ログ収集（日本語圏30件以上）
4. 生ログ収集（英語圏30件以上）
5. 5軸スコアリング
6. 定性インサイト抽出
7. 既存代替案分析
8. 課題裏付け判定
9. 成果物出力

### 5軸スコアリング基準（50点満点）

| 項目 | 10点 | 6-9点 | 3-5点 | 0-2点 |
|------|------|-------|-------|-------|
| **頻度** | 同様の声10件以上 | 5-9件 | 2-4件 | 1件以下 |
| **深刻度** | 「困り果てている」「限界」 | 「困っている」 | 「できれば解決したい」 | 「別にいい」 |
| **既存策不満** | 「使い物にならない」多数 | 不満の声多い | 一部不満あり | 概ね満足 |
| **支払い匂い** | 「お金払ってでも」発言あり | 時間・労力コスト言及 | コスト意識なし | 無料希望明確 |
| **緊急性** | 「今すぐ」「早く」多数 | 「近いうちに」 | 「いつか」 | 急がない |

### 判定基準

**総合判定**:
- 35-50点: ✅ 強い裏付け → CPF検証へ進む
- 20-34点: ⚠️ 中程度の裏付け → ニッチ化を検討
- 0-19点: ❌ 裏付け不足 → 課題仮説見直し

**起業の科学CPF基準との対応**:
- スコア35点以上 → CPF検証の補強材料として有効
- スコア20-34点 → 追加インタビューで深堀り、またはニッチ化検討
- スコア19点以下 → 課題仮説の根本見直し、`/discover-demand`で別課題を探索

**次ステップへの連携**:
| スコア | 次のアクション |
|:------:|---------------|
| 35点以上 | `/validate-cpf` で総合判定へ |
| 20-34点 | `/simulate-interview` で追加検証 |
| 19点以下 | `/discover-demand` で別課題を探索 |

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **WebSearch失敗**: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/customer_interview.md
- @startup_science/01_stages/cpf/persona_creation.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md
