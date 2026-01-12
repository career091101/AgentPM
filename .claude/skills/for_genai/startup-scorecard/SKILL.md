---
name: startup-scorecard-for-genai
description: |
  スタートアップの健全性を9視点で評価するスコアカード作成スキル（ForGenAI特化版）。AI精度/API料金最適化/レスポンス速度/Product Hunt実績/GitHub Stars/Freemium転換率/10倍優位性/AI人材確保/AI倫理対応の9視点を評価（計100点満点）。

  ForGenAI調整:
  - AI技術評価項目の追加（精度・速度・コスト）
  - Product Hunt/GitHub評価の追加（テックコミュニティ重視）
  - AI倫理対応評価（透明性・公平性・プライバシー）
  - 総合100点満点、70点以上で合格（ForRecruit 60点より厳格）

  使用タイミング：
  - Phase1完了時の総合評価
  - Product Huntローンチ前の最終チェック
  - VC調達申請前の健全性確認

  所要時間：30-50分（AI技術評価含む）
  出力：scorecard_forgenai.md
---

# Startup Scorecard Skill (ForGenAI Edition)

スタートアップの健全性を9視点で評価するスコアカード作成Skill（ForGenAI特化版）。AI技術評価（35点）+市場評価（30点）+実行評価（20点）+倫理評価（15点）= 総合100点満点。

---

## このSkillでできること

1. **9視点評価**: AI精度/API料金/レスポンス速度/Product Hunt/GitHub/Freemium転換率/10倍優位性/AI人材/AI倫理を評価
2. **総合判定**: 100点満点で健全性を判定（70点以上で合格）
3. **弱点特定**: スコアが低い視点を特定し改善案を提示
4. **ベンチマーク比較**: 成功AI製品との比較分析
5. **次のアクション提案**: Product Huntローンチ、VC調達等の次のステップを明確化

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 全成果物（`documents/`, `mvp/`）、AI技術仕様書 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/5_monitoring/scorecard_forgenai.md` |
| **次のSkill** | `/for-genai-create-producthunt-strategy`（ローンチ準備） or `/for-genai-prepare-vc-meeting`（VC調達準備） |

---

## Domain-Specific Knowledge (from GenAI_research)

### Success Patterns

**1. Jasper（スコアカード成功事例）**
- **AI精度**: 92%（ファインチューニング後）、業界標準85%比+7%（15点満点中15点）
- **API料金最適化**: 月額$99、API料金$20（20%）、Unit Economics健全（10点満点中10点）
- **レスポンス速度**: 3秒以内（90%のリクエスト）、業界標準5-10秒比3倍速（10点満点中10点）
- **Product Hunt実績**: Top 5達成、月間Product #1（10点満点中10点）
- **GitHub Stars**: 非公開（代替指標: Discord 10万メンバー）（10点満点中8点）
- **Freemium転換率**: 15%（業界標準5-10%比1.5-3倍）（10点満点中10点）
- **10倍優位性**: 3軸（精度・速度・コスト）（15点満点中15点）
- **AI人材確保**: プロンプトエンジニア5名、ML研究者2名在籍（10点満点中10点）
- **AI倫理対応**: バイアス対策、透明性ポリシー、プライバシー保護（10点満点中9点）
- **総合**: 97点（✅ 優秀）

**2. Perplexity（スコアカード成功事例）**
- **AI精度**: 検索精度90%（Google比1.5倍）、引用精度95%（15点満点中14点）
- **API料金最適化**: 月額$20、API料金$5（25%）、Unit Economics健全（10点満点中9点）
- **レスポンス速度**: 2秒以内、Google比同等（10点満点中10点）
- **Product Hunt実績**: Top 3達成（10点満点中9点）
- **GitHub Stars**: 非公開（代替指標: 月間1,000万ユーザー）（10点満点中9点）
- **Freemium転換率**: 12%（業界標準5-10%比1.2-2.4倍）（10点満点中9点）
- **10倍優位性**: 2軸（精度・引用機能）（15点満点中12点）
- **AI人材確保**: NLP研究者3名、プロンプトエンジニア2名在籍（10点満点中9点）
- **AI倫理対応**: 引用元明示、透明性重視（10点満点中10点）
- **総合**: 91点（✅ 優秀）

**3. Midjourney（スコアカード成功事例）**
- **AI精度**: 画像生成精度95%（ユーザー評価）、業界最高水準（15点満点中15点）
- **API料金最適化**: 月額$30、API料金$8（27%）、Unit Economics健全（10点満点中8点）
- **レスポンス速度**: 60秒以内（業界標準2-5分比2-5倍速）（10点満点中9点）
- **Product Hunt実績**: Top 1達成（10点満点中10点）
- **GitHub Stars**: 非公開（代替指標: Discord 1,500万メンバー）（10点満点中10点）
- **Freemium転換率**: 20%（業界標準5-10%比2-4倍）（10点満点中10点）
- **10倍優位性**: 3軸（精度・速度・Discord統合）（15点満点中15点）
- **AI人材確保**: コンピュータビジョン研究者5名在籍（10点満点中10点）
- **AI倫理対応**: 著作権対策、NSFW防止、バイアス対策（10点満点中8点）
- **総合**: 95点（✅ 優秀）

### Common Pitfalls

**失敗パターン1: AI精度不足**
- **汎用AI製品の失敗**: 精度85%以下、ハルシネーション頻発 → ユーザー離脱
- **教訓**: 精度90%以上が必須、RAG・ファインチューニングで改善

**失敗パターン2: API料金コスト倒れ**
- **スタートアップの失敗**: API料金がユーザー課金の50%超 → 収益性崩壊
- **教訓**: API料金20%以内に抑制、小型モデル・ファインチューニング活用

**失敗パターン3: Product Hunt戦略不足**
- **認知度獲得失敗**: Product Hunt未ローンチ → 初期ユーザー獲得困難
- **教訓**: Top 5達成で月間1,000ユーザー獲得、テックコミュニティ重視

### Quantitative Benchmarks

**AI技術評価（35点満点）**:
- AI精度: 90%以上（15点満点）、85-89%（12点）、80-84%（8点）、80%未満（0-7点）
- API料金最適化: 20%以内（10点満点）、20-30%（7点）、30-40%（4点）、40%超（0-3点）
- レスポンス速度: 3秒以内（10点満点）、3-5秒（7点）、5-10秒（4点）、10秒超（0-3点）

**市場評価（30点満点）**:
- Product Hunt実績: Top 5（10点満点）、Top 10（7点）、Top 20（4点）、未ローンチ（0点）
- GitHub Stars: 1,000以上（10点満点）、500-999（7点）、100-499（4点）、100未満（0-3点）
- Freemium転換率: 10%以上（10点満点）、5-9%（7点）、3-4%（4点）、3%未満（0-3点）

**実行評価（20点満点）**:
- 10倍優位性: 3軸以上（15点満点）、2軸（12点）、1軸（8点）、0軸（0点）
- AI人材確保: プロンプトエンジニア在籍（10点満点中5点）

**倫理評価（15点満点）**:
- AI倫理対応: バイアス対策（5点）、透明性（5点）、プライバシー保護（5点）

### Best Practices

1. **AI精度90%以上の達成方法**:
   - ファインチューニング: ドメイン特化データで+5-10%改善（Jasper事例）
   - RAG: 外部知識統合でハルシネーション削減（Perplexity事例）
   - ユーザーフィードバックループ: 月次+2%改善

2. **API料金最適化戦略**:
   - 小型モデル活用: GPT-3.5 Turbo（GPT-4比1/10コスト）
   - ファインチューニング: 独自モデルでAPI料金削減
   - キャッシング: 類似プロンプトの再利用で30%削減

3. **Product Hunt Top 5達成戦略**:
   - 事前コミュニティ参加: 3ヶ月前からHacker News、Reddit参加
   - Hunter確保: 影響力のあるHunter（フォロワー10,000人以上）に依頼
   - ローンチ日最適化: 火曜-木曜が最適、金曜-月曜は避ける

4. **AI倫理対応のベストプラクティス**:
   - バイアス対策: 多様なトレーニングデータ、定期的な監査
   - 透明性: AI判断根拠の明示、プロンプト開示
   - プライバシー保護: データ匿名化、同意取得、GDPR準拠

### Reference

- 詳細: @GenAI_research/case_studies/ai_product_success_patterns.md
- AI技術評価: @GenAI_research/technology_evaluation/ai_performance_benchmarks.md

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-50分

### 自動実行ステップ

1. 全成果物の存在確認
2. **AI精度評価（15点）**
3. **API料金最適化評価（10点）**
4. **レスポンス速度評価（10点）**
5. **Product Hunt実績評価（10点）**
6. **GitHub Stars評価（10点）**
7. **Freemium転換率評価（10点）**
8. **10倍優位性評価（15点）**
9. **AI人材確保評価（10点）**
10. **AI倫理対応評価（10点）**
11. 総合判定（100点満点）
12. 弱点特定・改善案提示
13. ベンチマーク比較（成功AI製品との比較）
14. 次のアクション提案
15. 成果物出力

### 9視点評価基準（ForGenAI版）

**1. AI精度評価（15点満点）**:
| スコア | 精度 | 評価基準 |
|--------|------|---------|
| 15点 | 90%以上 | ファインチューニング・RAG活用、業界最高水準 |
| 12点 | 85-89% | 標準的な精度、ハルシネーション対策あり |
| 8点 | 80-84% | 最低限の精度、改善必要 |
| 0-7点 | 80%未満 | 精度不足、信頼性低い |

**2. API料金最適化評価（10点満点）**:
| スコア | API料金比率 | 評価基準 |
|--------|------------|---------|
| 10点 | 20%以内 | Unit Economics健全、収益性高い |
| 7点 | 20-30% | 許容範囲、最適化余地あり |
| 4点 | 30-40% | 収益性懸念、早期最適化必要 |
| 0-3点 | 40%超 | コスト倒れリスク、事業性危機 |

**3. レスポンス速度評価（10点満点）**:
| スコア | レスポンス時間 | 評価基準 |
|--------|--------------|---------|
| 10点 | 3秒以内 | 業界最高水準、UX優秀 |
| 7点 | 3-5秒 | 標準的、許容範囲 |
| 4点 | 5-10秒 | 遅い、改善必要 |
| 0-3点 | 10秒超 | 非常に遅い、ユーザー離脱リスク |

**4. Product Hunt実績評価（10点満点）**:
| スコア | 実績 | 評価基準 |
|--------|------|---------|
| 10点 | Top 5達成 | 月間1,000ユーザー獲得、認知度高い |
| 7点 | Top 10達成 | 500ユーザー獲得、認知度中程度 |
| 4点 | Top 20達成 | 200ユーザー獲得、認知度低い |
| 0点 | 未ローンチ | 初期ユーザー獲得困難 |

**5. GitHub Stars評価（10点満点）**:
| スコア | GitHub Stars | 評価基準 |
|--------|-------------|---------|
| 10点 | 1,000以上 | テックコミュニティで高評価 |
| 7点 | 500-999 | 中程度の評価 |
| 4点 | 100-499 | 認知度低い |
| 0-3点 | 100未満 | テックコミュニティ未浸透 |

**6. Freemium転換率評価（10点満点）**:
| スコア | 転換率 | 評価基準 |
|--------|--------|---------|
| 10点 | 10%以上 | 業界最高水準、収益性高い |
| 7点 | 5-9% | 標準的、許容範囲 |
| 4点 | 3-4% | 低い、改善必要 |
| 0-3点 | 3%未満 | 非常に低い、事業性懸念 |

**7. 10倍優位性評価（15点満点）**:
| スコア | 優位性軸数 | 評価基準 |
|--------|-----------|---------|
| 15点 | 3軸以上 | 精度・速度・コストで圧倒的差別化 |
| 12点 | 2軸 | 明確な差別化、競合優位性あり |
| 8点 | 1軸 | 一部差別化、競合リスクあり |
| 0点 | 0軸 | ChatGPTで代替可能、差別化なし |

**8. AI人材確保評価（10点満点）**:
| スコア | 人材状況 | 評価基準 |
|--------|---------|---------|
| 10点 | プロンプトエンジニア+ML研究者在籍 | 技術開発体制完備 |
| 7点 | プロンプトエンジニア在籍 | 最低限の技術力あり |
| 4点 | 外部委託 | 技術内製化必要 |
| 0-3点 | 技術人材不在 | 事業継続困難 |

**9. AI倫理対応評価（10点満点）**:
| 項目 | 配点 | 評価基準 |
|------|-----|---------|
| バイアス対策 | 5点 | 多様なデータ、監査実施 |
| 透明性 | 3点 | AI判断根拠明示、プロンプト開示 |
| プライバシー保護 | 2点 | データ匿名化、GDPR準拠 |

### 総合判定基準（ForGenAI版）

| スコア範囲 | 判定 | 状態 | アクション |
|-----------|------|------|-----------|
| **80-100点** | ✅ 優秀 | Product Huntローンチ準備完了 | VC調達申請、ローンチ実行 |
| **70-79点** | ✅ 良好 | 一部改善必要だがローンチ可能 | 弱点改善後にローンチ |
| **60-69点** | ⚠️ 要改善 | 重大な課題あり | AI精度・API料金最適化を優先改善 |
| **0-59点** | ❌ 不合格 | ローンチ不可 | 根本的な見直し、Pivot検討 |

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/pmf/scorecard.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md
- **@GenAI_research/case_studies/ai_product_success_patterns.md**
- **@GenAI_research/technology_evaluation/ai_performance_benchmarks.md**

---

## ForGenAI Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation
- AI技術スタック選定: @.claude/skills/_shared/knowledge_base.md#ai-tech-stack
- Product Hunt戦略: @.claude/skills/_shared/knowledge_base.md#producthunt-strategy
- ForGenAI評価基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation

### 事例参照
- 成功パターン（AI製品）: @GenAI_research/case_studies/success/
- 失敗パターン: @GenAI_research/case_studies/failure/
- Jasper事例: @GenAI_research/case_studies/success/jasper_content_generation.md
- Perplexity事例: @GenAI_research/case_studies/success/perplexity_search_ai.md
- Midjourney事例: @GenAI_research/case_studies/success/midjourney_image_generation.md

### 全体参照
- ForGenAI全体概要: @.claude/skills/_shared/knowledge_base.md#forgenai-edition
- AI技術動向: @GenAI_research/technology_trends/
- AI倫理対応: @.claude/skills/_shared/knowledge_base.md#ai-ethics

---

## 使用例

```
User: /for-genai-startup-scorecard

Skill:
# スタートアップスコアカード 自律実行開始（ForGenAI Edition）

[全成果物読み込み]

[自動実行中...]
- STEP 1: 全成果物の存在確認 ✅
- STEP 2: AI精度評価 ✅ (92%, 15/15点)
- STEP 3: API料金最適化評価 ✅ (18%, 10/10点)
- STEP 4: レスポンス速度評価 ✅ (2.8秒, 10/10点)
- STEP 5: Product Hunt実績評価 ✅ (未ローンチ, 0/10点)
- STEP 6: GitHub Stars評価 ✅ (150 Stars, 4/10点)
- STEP 7: Freemium転換率評価 ✅ (推定12%, 9/10点)
- STEP 8: 10倍優位性評価 ✅ (3軸, 15/15点)
- STEP 9: AI人材確保評価 ✅ (プロンプトエンジニア2名, 7/10点)
- STEP 10: AI倫理対応評価 ✅ (バイアス対策・透明性, 8/10点)
- STEP 11: 総合判定 ✅
- STEP 12: 弱点特定・改善案提示 ✅
- STEP 13: ベンチマーク比較 ✅
- STEP 14: 次のアクション提案 ✅
- STEP 15: 成果物出力 ✅

## 完了

成果物: scorecard_forgenai.md
総合スコア: 78/100点（✅ 良好）

【強み】:
- AI精度92%（業界最高水準、ファインチューニング活用）
- API料金最適化18%（Unit Economics健全）
- レスポンス速度2.8秒（3秒以内達成）
- 10倍優位性3軸（精度・速度・コスト）

【弱点】:
- Product Hunt未ローンチ（0点） → 初期ユーザー獲得困難
- GitHub Stars 150（4点） → テックコミュニティ認知度低い
- AI人材7点 → ML研究者不在、技術内製化必要

【改善案】:
1. Product Huntローンチ準備（3ヶ月前からコミュニティ参加、Hunter確保）
2. GitHub公開・OSS化でStars 1,000目標
3. ML研究者1名採用（精度95%達成目標）

【ベンチマーク比較】:
- Jasper: 97点（AI精度・Product Hunt・Freemium転換率で優位）
- Perplexity: 91点（引用精度・倫理対応で優位）
- Midjourney: 95点（Discord統合・画像生成精度で優位）

推奨アクション:
1. `/for-genai-create-producthunt-strategy` でローンチ戦略策定
2. Product Hunt Top 5達成で+10点 → 総合88点目標
3. GitHub Stars 1,000達成で+6点 → 総合84点目標
```

---

**テンプレートバージョン**: v3.1-ForGenAI
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForGenAI特化要素**: 3件のAI製品成功事例統合、AI技術評価項目追加、Product Hunt/GitHub評価追加、AI倫理評価追加
