---
name: discover-demand
description: |
  ForSolo Edition: ソロプレナー向けに最適化された需要発見スキル。Reddit、Yahoo!知恵袋、X等から「困りごと」を自動収集し、4軸スコアリング（20点満点）で評価。Build in Public戦略と組み合わせた需要候補を特定し、1人実行可能性を重視した解決アイデアとマネタイズ仮説を提示します。

  使用タイミング：
  - 新規ビジネスアイデアを探している
  - ソロプレナーとして実行可能な課題を発見したい
  - Build in Public戦略に適した課題を見つけたい

  所要時間：15-30分（自動実行）
  出力：demand_discovery.md
---

# Discover Demand Skill (ForSolo Edition)

ソロプレナー向けに最適化された需要発見スキル。1人実行可能性とBuild in Public戦略を重視。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Yahoo!知恵袋/X等から「困りごと」を自動収集
2. **4軸スコアリング**: 切実度/頻度/支払い匂い/未解決度で評価（20点満点）
3. **需要候補抽出**: スコア12/20以上の有望候補を特定
4. **1人実行可能性評価**: ソロプレナーとして実行可能かを判定
5. **Build in Public戦略**: 透明性の高い開発プロセスに適した課題を優先
6. **解決アイデア生成**: 各候補に対する実装可能なソリューション案を提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 探索分野キーワード（オプション） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/1_initiating/demand_discovery.md` |
| **次のSkill** | `/for-solo-create-mvv` → `/for-solo-create-persona` |
| **ステージ** | Idea検証（ForSolo特化） |

---

## Instructions

### セッション開始

探索分野キーワードを入力してください（省略可）:

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 15-30分

以下のステップを自動実行します:
1. 検索クエリ生成（日本語・英語各5個以上、ソロプレナー向け課題重視）
2. 生ログ収集（日本語圏・英語圏）
3. 需要候補の構造化
4. 4軸スコアリング
5. **[ForSolo追加]** 1人実行可能性評価（6点満点）
6. **[ForSolo追加]** Build in Public適合性評価
7. 解決アイデア生成
8. マネタイズ仮説策定
9. 成果物出力

### 自動実行フロー

**STEP 1: 検索クエリ生成**
- ツール: 内部生成
- 出力: 日本語クエリ5-10個、英語クエリ5-10個
- **[ForSolo特化]**: 「Micro-SaaS」「ソロプレナー」「1人開発」「副業」等のキーワードを含むクエリを優先

**STEP 2: 生ログ収集（日本語圏）**
- ツール: WebSearch
- 対象: Yahoo!知恵袋, X, teratail, note
- 収集基準: 「困っている」「うまくいかない」等の発言、同様の悩みが複数回出現、いいね/回答数が多い投稿
- **[ForSolo追加]**: 個人開発者・フリーランス・副業者の悩みを優先収集
- エラー対応: 検索結果0件 → クエリ変更して再検索（最大3回）

**STEP 3: 生ログ収集（英語圏）**
- ツール: WebSearch
- 対象: Reddit, Stack Overflow, G2, Quora, IndieHackers, Product Hunt
- **[ForSolo追加]**: IndieHackersとProduct Huntを重視（ソロプレナーコミュニティ）
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
- 16-20点: ✅ 有望需要あり → 優先的に活用
- 12-15点: ⚠️ 検討余地 → 参考情報として活用
- 1-11点: ❌ 見送り → 別の探索分野を推奨

**STEP 6: 1人実行可能性評価（ForSolo特化）**

| 項目 | 2点 | 1点 | 0点 |
|------|-----|-----|-----|
| **技術スタック** | 既存スキルで実装可能 | 一部学習が必要 | 大幅な学習が必要 |
| **時間投資** | 月40時間以下で実装可能 | 月40-80時間 | 月80時間以上 |
| **ツールコスト** | 月$100以下 | 月$100-$500 | 月$500以上 |

**実行可能性スコア**: 6点満点
- 6点: ✅ 即座に実行可能
- 4-5点: ⚠️ 一部調整で実行可能
- 0-3点: ❌ 実行困難

**STEP 7: Build in Public適合性評価（ForSolo特化）**

Build in Public戦略に適した課題かを評価:

| 評価項目 | 判定 |
|---------|------|
| **透明性** | プロセスを公開しやすいか |
| **コミュニティ参加** | X/Twitterで共感を得やすいか |
| **段階的リリース** | 小さくリリースし、フィードバックを得られるか |

**STEP 8: 解決アイデア生成**
- 対象: スコア12/20以上の候補
- 出力: ソリューション案、技術的実現可能性
- **[ForSolo追加]**: 1人で実装可能な技術スタックを明記（Next.js, Supabase, Stripe等）

**STEP 9: マネタイズ仮説策定**
- 出力: 誰が/何に/いくら払うか
- **[ForSolo追加]**: Micro-SaaS収益化パターンを参照
  - 月額$10-$50の低価格帯SaaS
  - Boilerplate/Template販売（$50-$200）
  - Build in Publicによる有機的なリード獲得

**STEP 10: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/1_initiating/demand_discovery.md`

---

## 成果物フォーマット

```markdown
# 需要発見レポート (ForSolo Edition)

**作成日**: [YYYY-MM-DD]
**探索分野**: [キーワード or 自動探索]
**総合判定**: ✅有望 / ⚠️検討余地 / ❌見送り

---

## エグゼクティブサマリー

| 順位 | 需要候補 | 4軸スコア | 実行可能性 | BIP適合 | 判定 |
|:----:|---------|:--------:|:----------:|:-------:|:----:|
| 1 | [タイトル] | XX/20 | XX/6 | ✅/❌ | ✅/⚠️/❌ |
| 2 | [タイトル] | XX/20 | XX/6 | ✅/❌ | ✅/⚠️/❌ |

---

## 需要候補詳細

### 需要候補 #1: [タイトル]

#### 生ログ引用
> "[日本語原文]"
> 出典: [プラットフォーム]

#### 需要スコア（4軸）
| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 切実度 | X/5 | [根拠] |
| 頻度 | X/5 | [根拠] |
| 支払い匂い | X/5 | [根拠] |
| 未解決度 | X/5 | [根拠] |
| **合計** | **XX/20** | |

#### 1人実行可能性スコア (ForSolo)
| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 技術スタック | X/2 | [既存スキルで実装可能 / 学習必要] |
| 時間投資 | X/2 | [月XX時間で実装可能] |
| ツールコスト | X/2 | [月$XX] |
| **合計** | **XX/6** | |

#### Build in Public適合性 (ForSolo)
- **透明性**: ✅/❌ [プロセス公開のしやすさ]
- **コミュニティ参加**: ✅/❌ [X/Twitterで共感を得やすいか]
- **段階的リリース**: ✅/❌ [小さくリリース可能か]

#### 解決アイデア
- **ソリューション案**: [具体的な形態]
- **技術スタック**: [Next.js / Supabase / Stripe 等]
- **実装期間**: [X週間 / Xヶ月]

#### マネタイズ仮説 (ForSolo)
| 項目 | 内容 |
|------|------|
| 誰が払うか | [個人 / 小規模企業] |
| 課金形態 | [月額 / 買い切り / フリーミアム] |
| 想定価格帯 | [月額$XX / 買い切り$XX] |
| 初年度目標 | [MRR $X,XXX] |

#### Solopreneur Research参照
- 類似事例: @Solopreneur_Research/documents/01_App/case_studies/[事例名].md
- 成功パターン: [Build in Public / Boilerplate販売 / 等]
```

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **WebSearch失敗**: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## Knowledge Base参照

### ForSolo Edition専用
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Solopreneur_Research/documents/01_App/case_studies/*.md`
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies/discover-demand/*.md`

### 共通Knowledge Base
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/persona_creation.md
- @startup_science/03_tactics/founder_issue_fit/fif_overview.md
- @startup_science/01_stages/cpf/cpf_overview.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md

### ForSolo固有ドメイン知識

#### 1人実行可能性パターン
- **Micro-SaaS**: 月額$10-$50、シンプルな機能に特化
- **Boilerplate/Template**: Next.js/Supabase/Stripe等の頻出スタック
- **API活用型**: 既存APIを組み合わせ、フロントエンドに注力

#### Build in Public戦略
- **X/Twitter透明性**: 開発プロセスをリアルタイムで共有
- **フォロワー獲得**: 共感と信頼を得て、ローンチ前から顧客獲得
- **エンゲージメント**: コミュニティからフィードバックを得る

#### Micro-SaaS収益化
- **初期目標**: MRR $1K（月間経常収益$1,000）
- **成長目標**: MRR $5K → $10K（18-24ヶ月）
- **料金設定**: 月額$20-$50の低価格帯、セルフサービス型

---

## 使用例

```
User: /for-solo-discover-demand

Skill: 探索分野キーワードを入力してください（省略可）:

User: Micro-SaaS フリーランス 業務効率化

Skill:
# 需要発見リサーチ (ForSolo Edition) 自律実行開始

探索分野: 「Micro-SaaS フリーランス 業務効率化」

[自動実行中...]
- STEP 1: 検索クエリ生成 ✅
- STEP 2: 日本語圏生ログ収集 ✅ (12件)
- STEP 3: 英語圏生ログ収集 ✅ (18件、IndieHackers重視)
- STEP 4: 需要候補構造化 ✅ (7候補)
- STEP 5: 4軸スコアリング ✅
- STEP 6: 1人実行可能性評価 ✅
- STEP 7: Build in Public適合性評価 ✅
- STEP 8: 解決アイデア生成 ✅
- STEP 9: マネタイズ仮説 ✅
- STEP 10: 成果物出力 ✅

## 完了

成果物: demand_discovery.md (ForSolo Edition)
最有望候補: 「フリーランスの請求書管理自動化」
- 4軸スコア: 17/20
- 実行可能性: 5/6
- BIP適合: ✅

推奨: `/for-solo-create-mvv` でMVV定義へ
```

---

## 注意事項

1. **1人実行可能性を最優先**: 市場規模よりも実行可能性を重視
2. **Build in Public前提**: X/Twitterでの透明性の高い開発を想定
3. **Micro-SaaS収益化**: 月額$10-$50の低価格帯、MRR $1K-$10Kを目標
4. **ツールコスト制約**: 月$100以下のツールスタックを優先

---

## 更新履歴

- 2026-01-02: ForSolo Edition作成（1人実行可能性、Build in Public戦略追加）
