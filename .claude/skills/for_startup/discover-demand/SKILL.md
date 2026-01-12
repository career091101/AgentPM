---
name: discover-demand-for-startup
description: |
  ForStartup特化版:「困りごとの生ログ」を起点に有望な需要を発見する自律実行型スキル。VC調達基準に準拠した厳格な評価を実施。Reddit、Yahoo!知恵袋、X等から「困りごと」を自動収集し、4軸（切実度/頻度/支払い匂い/未解決度）でスコアリング（20点満点）。スコア15点以上の有望候補を特定し、解決アイデアとマネタイズ仮説を提示します。

  ForStartup固有の特徴:
  - VC投資基準に準拠（TAM $1B以上、月次成長率20%以上）
  - 10倍優位性3軸（速度・コスト・品質）を必須化
  - スケーラビリティ・ネットワーク効果を重視
  - ピッチデッキ用の定量データ抽出

  使用タイミング：
  - VC調達を目指す新規ビジネスアイデアを探している
  - 大規模市場の未解決課題を発見したい
  - データドリブンな需要検証をしたい（VC視点）

  所要時間：15-30分（自動実行）
  出力：demand_discovery.mdレポート
trigger_keywords:
  - "/for-startup-discover-demand"
  - "需要発見"
  - "市場機会発見"
  - "困りごと調査"
  - "demand discovery"
  - "discover demand"
stage: "planning"
dependencies: []
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/demand_discovery.md
---

# Discover Demand Skill (ForStartup Edition)

「困りごとの生ログ」を起点に有望な需要を発見する自律実行型Skill。**ForStartup特化版**では、VC調達基準（TAM $1B以上、月次成長率20%以上）に準拠した厳格な評価を実施します。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Yahoo!知恵袋/X等から「困りごと」を自動収集
2. **4軸スコアリング**: 切実度/頻度/支払い匂い/未解決度で評価（20点満点）
4. **解決アイデア生成**: 10倍優位性を持つソリューション案を提示
5. **VC投資魅力度評価**: 市場規模、成長率、スケーラビリティを評価

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 探索分野キーワード（オプション） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/demand_discovery.md` |
| **次のSkill** | `/for-startup-create-mvv` → `/for-startup-validate-cpf` |
| **ステージ** | Idea検証（Seed調達準備段階） |

---

## ForStartup固有の評価基準

### 市場機会評価（厳格版）

このスキルはVC調達の**Seed調達準備段階**に対応します。

| 指標 | Origin基準 | ForStartup基準 | 理由 |
|------|----------|---------------|------|
| 市場規模（TAM） | 100億円以上 | **$1B以上** | VC投資基準（10倍リターン獲得） |
| 成長率 | 10%/年以上 | **20%/月以上** | 急成長可能性の証明 |
| 競合飽和度 | 3社以下 | **3社以下** | 10倍優位性獲得の余地 |
| スケーラビリティ | 評価対象外 | **必須** | VC投資の前提条件 |

### VC投資魅力度チェック

**確認事項**:
- [ ] TAM $1B以上の市場規模
- [ ] 月次成長率20%以上の実現可能性
- [ ] 10倍優位性（速度・コスト・品質の3軸）
- [ ] ネットワーク効果 or プラットフォーム特性
- [ ] ピッチデッキ用の定量データ抽出可能性

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns（需要発見成功事例）

1. **Stripe** (Patrick & John Collison):
   - **市場ニーズ**: オンライン決済の複雑さ（従来は数週間かかる統合）
   - **発見手法**: 開発者コミュニティでの課題ヒアリング
   - **TAM**: $100B以上（グローバル決済市場）
   - **10倍優位性**: 7行のコードで決済実装（従来の1/100の工数）
   - **成果**: $95B評価（2021）

2. **Notion** (Ivan Zhao):
   - **市場ニーズ**: 仕事ツールが分散（Trello、Evernote、Wiki等を併用）
   - **発見手法**: 自社内でのツール乱立問題の観察
   - **TAM**: $10B以上（ワークスペース市場）
   - **10倍優位性**: オールインワンで他ツール10個分を統合
   - **成果**: $10B評価（2021）、月次成長率30%以上

3. **Figma** (Dylan Field):
   - **市場ニーズ**: デザインツール（Sketch、Adobe XD）が共同編集に非対応
   - **発見手法**: リモートワーク時代のデザイナー課題調査
   - **TAM**: $5B以上（デザインツール市場）
   - **10倍優位性**: リアルタイム共同編集（デザイン速度10倍）
   - **成果**: Adobe $20Bで買収（2022）

4. **Airtable** (Howie Liu):
   - **市場ニーズ**: ExcelとDBの間のギャップ（Excelは限界、DBは難しい）
   - **発見手法**: 非エンジニアのデータベース需要調査
   - **TAM**: $20B以上（ノーコード/ローコード市場）
   - **10倍優位性**: スプレッドシート感覚でDB構築
   - **成果**: $11B評価（2021）

5. **DoorDash** (Tony Xu):
   - **市場ニーズ**: 郊外エリアで食事配達サービスがない
   - **発見手法**: スタンフォード大学周辺での実地調査
   - **TAM**: $100B以上（米国食事配達市場）
   - **10倍優位性**: 郊外市場特化（Uber Eatsが都市部集中）
   - **成果**: $60B評価（IPO 2020）、COVID-19で急成長

### Common Pitfalls（失敗パターン）

1. **Theranos** (Elizabeth Holmes):
   - **失敗要因**: 技術未実証のまま資金調達、詐欺疑惑
   - **教訓**: 技術的実現可能性の厳格な検証が必須
   - **ForStartup教訓**: PSF検証を早期に実施、技術リスクを明示

2. **WeWork** (Adam Neumann):
   - **失敗要因**: ユニットエコノミクス破綻（成長すればするほど赤字拡大）
   - **教訓**: LTV/CAC、CAC回収期間の早期検証
   - **ForStartup教訓**: ユニットエコノミクス厳格検証を必須化

3. **Quibi** (Jeffrey Katzenberg):
   - **失敗要因**: 市場ニーズ誤認（短尺動画需要を過大評価）
   - **教訓**: PMF検証の重要性、ユーザーインタビュー不足
   - **ForStartup教訓**: 需要スコア15点以上を必須化、定性・定量両面の検証

### Quantitative Benchmarks

- **User Research Count**: VC調達成功企業平均50回以上、ForStartup推奨: **30回以上**
- **市場規模（TAM）**: VC調達成功企業平均$1B以上、ForStartup必須: **$1B以上**
- **成長率**: VC調達成功企業平均月次20%以上、ForStartup必須: **20%以上**
- **Problem Commonality**: VC調達成功企業平均80%以上、ForStartup推奨: **70%以上**
- **LTV/CAC**: VC調達成功企業平均5.0以上、ForStartup必須: **5.0以上**

### Reference

- 詳細: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
- Stripe事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_181_stripe_patrick_john_collison.md
- Notion事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_188_notion_ivan_zhao.md
- Figma事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_190_figma_dylan_field.md

---

## Instructions

### セッション開始

探索分野キーワードを入力してください（省略可）:

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 15-30分

以下のステップを自動実行します:
1. 検索クエリ生成（日本語・英語各5個以上）
2. 生ログ収集（日本語圏・英語圏）
3. 需要候補の構造化
4. 4軸スコアリング
5. 解決アイデア生成（10倍優位性重視）
6. マネタイズ仮説策定
7. **VC投資魅力度評価（追加）**
8. 成果物出力

### 自動実行フロー

**STEP 1: 検索クエリ生成**
- ツール: 内部生成
- 出力: 日本語クエリ5-10個、英語クエリ5-10個

**STEP 2: 生ログ収集（日本語圏）**
- ツール: WebSearch
- 対象: Yahoo!知恵袋, X, teratail, note
- 収集基準: 「困っている」「うまくいかない」等の発言、同様の悩みが複数回出現、いいね/回答数が多い投稿
- エラー対応: 検索結果0件 → クエリ変更して再検索（最大3回）

**STEP 3: 生ログ収集（英語圏）**
- ツール: WebSearch
- 対象: Reddit, Stack Overflow, G2, Quora, Product Hunt
- 収集基準: 同上

**STEP 4: 需要候補の構造化**
- 処理: 収集した生ログから需要候補を抽出
- 出力: 最低5件の需要候補

**STEP 5: 4軸スコアリング**

| 項目 | 5点 | 3点 | 1点 |
|------|-----|-----|-----|
| **切実度** | 「今すぐ解決必須」「困り果てている」 | 「できれば解決したい」 | 「別にいい」「あれば便利」 |
| **頻度** | 同様の声10件以上 | 3-9件 | 1-2件 |
| **支払い匂い** | 「お金払ってでも」発言あり | 時間・労力コスト言及 | 無料希望が明確 |
| **未解決度** | 既存策なし or 強い不満多数 | 既存策あるが不十分 | 十分解決済み |

**総合判定**:
- 18-20点: ✅ 非常に有望 → VC調達可能性高い
- 15-17点: ✅ 有望 → CPF/PSF検証へ進む
- 12-14点: ⚠️ 要改善 → 需要の深堀り必要
- 1-11点: ❌ 見送り → 別の探索分野を推奨

**STEP 6: 解決アイデア生成**
- 対象: スコア15/20以上の候補
- 出力: ソリューション案、10倍優位性（3軸）、技術的実現可能性

**STEP 7: マネタイズ仮説策定**
- 出力: 誰が/何に/いくら払うか、LTV/CAC初期試算

**STEP 8: VC投資魅力度評価（追加）**

各需要候補について、以下を評価:

| 評価項目 | 評価基準 | 配点 |
|---------|---------|------|
| **市場規模（TAM）** | $1B以上の市場規模が証明できるか | 5点満点 |
| **成長率** | 月次成長率20%以上が実現可能か | 5点満点 |
| **10倍優位性** | 速度・コスト・品質の3軸で10倍を達成できるか | 5点満点 |
| **スケーラビリティ** | ネットワーク効果 or プラットフォーム特性があるか | 3点満点 |
| **ピッチデッキ適合性** | 定量データでVC説得可能か | 2点満点 |

**VC投資魅力度スコア**: 20点満点
- 16点以上: ✅ VC調達可能性高い
- 12-15点: ⚠️ 一部改善で調達可能
- 11点以下: ❌ VC調達困難、ForSolo/ForStartup推奨

**STEP 9: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/demand_discovery.md`

---

## 成果物フォーマット

```markdown
# 需要発見レポート (ForStartup Edition)

**作成日**: [YYYY-MM-DD]
**探索分野**: [キーワード or 自動探索]
**総合判定**: ✅有望 / ⚠️改善必要 / ❌見送り

---

## エグゼクティブサマリー

| 順位 | 需要候補 | スコア | VC投資魅力度 | 判定 |
|:----:|---------|:------:|:-----------:|:----:|
| 1 | [タイトル] | XX/20 | XX/20 | ✅/⚠️/❌ |
| 2 | [タイトル] | XX/20 | XX/20 | ✅/⚠️/❌ |

---

## 需要候補詳細

### 需要候補 #1: [タイトル]

#### 生ログ引用
> "[日本語原文]"
> 出典: [プラットフォーム]

#### 需要スコア
| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 切実度 | X/5 | [根拠] |
| 頻度 | X/5 | [根拠] |
| 支払い匂い | X/5 | [根拠] |
| 未解決度 | X/5 | [根拠] |
| **合計** | **XX/20** | |

#### VC投資魅力度評価
| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 市場規模（TAM） | X/5 | [TAM推定額]（[調査ソース]） |
| 成長率 | X/5 | 月次成長率[%]が実現可能（[根拠]） |
| 10倍優位性 | X/5 | 速度[倍]、コスト[倍]、品質[倍] |
| スケーラビリティ | X/3 | [ネットワーク効果/プラットフォーム特性] |
| ピッチデッキ適合性 | X/2 | [定量データ抽出可否] |
| **合計** | **XX/20** | |

#### 解決アイデア
- ソリューション案: [具体的な形態]
- 10倍優位性:
  - 速度: [X倍高速化]
  - コスト: [X倍削減]
  - 品質: [X倍向上]
- 技術的実現可能性: [評価]

#### マネタイズ仮説
| 項目 | 内容 |
|------|------|
| 誰が払うか | [BtoB/BtoC] |
| 課金形態 | [月額/従量等] |
| 想定価格帯 | [金額] |
| **LTV/CAC初期試算** | LTV: [金額]、CAC: [金額]、比率: [X.X] |

#### VC調達成功事例ベンチマーク
類似成功事例: [Stripe/Notion/Figma等]
- TAM: [金額]
- 月次成長率: [%]
- 10倍優位性: [軸]
- 評価額: [金額]
```

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **WebSearch失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/persona_creation.md
- @startup_science/03_tactics/founder_issue_fit/fif_overview.md
- @startup_science/01_stages/cpf/cpf_overview.md
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/skill_chains.md
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md
- **/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/**

---

## ForStartup Knowledge Base Reference

### 評価基準・フレームワーク
- VC投資基準総合: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - CPF/PSF/PMF ≥70%、TAM ≥$1B、月次成長率 ≥20%、10倍優位性 3軸以上
  - NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）
- VC調達ロードマップ: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - Pre-Seed → Seed → Series A基準
- ユニットエコノミクス: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - LTV/CAC ≥5.0、CAC回収期間 ≤12ヶ月、Gross Margin ≥70%

### ケーススタディ
- 成功事例（Legendary）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/
  - Brian Chesky（Airbnb）、Patrick Collison（Stripe）、Brian Armstrong（Coinbase）
- 成功事例（Unicorn）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/
  - Girish Mathrubootham（Freshworks）、Henrique Dubugras（Brex）
- 成功事例（VC-Backed）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
  - Dylan Field（Figma）、Vlad Tenev（Robinhood）、Melanie Perkins（Canva）
- 失敗事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
  - Elizabeth Holmes（Theranos）、Adam Neumann（WeWork）

---

## 使用例

```
User: /for-startup-discover-demand

Skill: 探索分野キーワードを入力してください（省略可）:

User: デザイナー 共同編集

Skill:
# 需要発見リサーチ 自律実行開始（ForStartup Edition）

探索分野: 「デザイナー 共同編集」

[自動実行中...]
- STEP 1: 検索クエリ生成 ✅
- STEP 2: 日本語圏生ログ収集 ✅ (15件)
- STEP 3: 英語圏生ログ収集 ✅ (25件)
- STEP 4: 需要候補構造化 ✅ (6候補)
- STEP 5: スコアリング ✅
- STEP 6: 解決アイデア生成 ✅
- STEP 7: マネタイズ仮説 ✅
- STEP 8: VC投資魅力度評価 ✅
- STEP 9: 成果物出力 ✅

## 完了

成果物: demand_discovery.md
最有望候補: 「デザインツールの共同編集未対応」(需要スコア: 18/20, VC投資魅力度: 17/20)
10倍優位性: リアルタイム共同編集でデザイン速度10倍
参照事例: Figma成功事例（Adobe $20B買収）

推奨: `/for-startup-create-mvv` でMVV定義へ
次ステップ: CPF 70%基準検証
```

---

**テンプレートバージョン**: v1.0-ForStartup
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForStartup特化要素**: VC調達55事例統合、VC投資魅力度評価基準追加、ピッチデッキ準備連携
