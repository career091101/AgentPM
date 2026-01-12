---
name: validate-psf
description: |
  ForSolo Edition: ソロプレナー向けPSF検証スキル。
  10倍優位性検証結果とMVP選定状況から、PSF達成/未達成を判定。
  実行可能性スコア6点以上、市場機会スコア4点以上を重視。
  次のステップ（ローンチ準備 or ソリューション再設計）を提案します。

  使用タイミング：
  - CPF達成後
  - 10倍優位性検証・MVP選定完了後
  - PSF達成を判断したい（ステージゲート2）

  所要時間：5-10分（自動実行）
  出力：psf_diagnosis.md
---

# Validate PSF Skill (ForSolo Edition)

ソロプレナー向けPSF達成基準に基づき、総合判定を行う自律実行型Skill。

---

## このSkillでできること

1. **成果物統合**: cpf_diagnosis.md, 10x_validation.md, lean_canvas.md を読み込み
2. **PSF判定**: 10倍優位性2軸以上 + MVP選定完了を確認
3. **実行可能性重視**: 実行可能性スコア6点以上を必須条件として評価
4. **市場機会評価**: 市場機会スコア4点以上で判定（ForStartup 6点より緩和）
5. **総合判定**: PSF達成/要改善/見直しの判断
6. **次ステップ提案**: ローンチ準備へ進むか、ソリューション再設計すべきかを提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `cpf_diagnosis.md`, `10x_validation.md`, `lean_canvas.md`, `lp/README.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/3_planning/psf_diagnosis.md` |
| **次のSkill** | `/for-solo-create-sns-content` → `/for-solo-startup-scorecard`（PSF達成時） |
| **ステージ** | PSF検証（ステージゲート2、ForSolo特化） |

---

## Knowledge Base参照

### ForSolo Edition専用
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Solopreneur_Research/documents/01_App/case_studies/*.md`
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies/validate-psf/*.md`

### 共通Knowledge Base
- @startup_science/01_stages/psf/psf_overview.md
- @startup_science/01_stages/psf/10x_validation.md
- @startup_science/01_stages/psf/mvp_types.md
- @startup_science/01_stages/psf/uvp_canvas.md

---

## PSF達成基準（ForSolo特化）

### 3指標の目標値（ForStartupとの比較）

| 指標 | ForStartup | ForSolo | 測定方法 |
|------|-----------|---------|----------|
| **10倍優位性達成軸数** | 2軸以上 | 2軸以上 | 5軸比較で10倍以上の改善 |
| **MVP選定** | 完了 | 完了 | Landing Page型/Concierge型等のMVP類型決定 |
| **UVP明確性** | 明確 | 明確 | 独自の価値提案が1文で表現可能 |

### ForSolo独自評価

| 指標 | ForStartup | ForSolo | 理由 |
|------|-----------|---------|------|
| **実行可能性スコア** | 4点以上 | **6点** ✅ 必須 | 1人で実行可能であることが必須 |
| **市場機会スコア** | 6点以上 | **4点以上** ✅ 緩和 | ニッチ市場OKのため基準緩和 |

---

## 判定基準

### 個別指標判定（ForSolo版）

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|-----------|----------|
| 10倍達成軸数 | 2軸以上 | 1軸のみ | 0軸 |
| MVP選定 | 完了 | 未決定（検討中） | なし |
| UVP明確性 | 明確 | やや曖昧 | 不明瞭 |
| **実行可能性** | **6点** ✅ | 4-5点 | 3点以下 |
| **市場機会** | **4点以上** ✅ | 3点 | 2点以下 |

### 総合判定（ForSolo版）

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **PSF達成** | 基本3指標✅ + 実行可能性6点 + 市場機会4点以上 | ローンチ準備へ（/for-solo-create-sns-content） |
| ⚠️ **要改善** | 基本2指標✅ + 実行可能性4-5点 | 10倍軸の強化、MVP類型再検討 |
| ❌ **見直し** | 実行可能性3点以下 or 市場機会2点以下 | ソリューション根本見直し |

---

## Solopreneur固有ドメイン知識

### Micro-SaaS収益化パターン
- **初期目標**: MRR $1K（月間経常収益$1,000）
- **成長目標**: MRR $5K → $10K（18-24ヶ月）
- **料金設定**: 月額$20-$50の低価格帯、セルフサービス型

### Build in Public戦略
- **X/Twitter透明性**: 開発プロセスをリアルタイムで共有
- **フォロワー獲得**: 共感と信頼を得て、ローンチ前から顧客獲得
- **エンゲージメント**: コミュニティからフィードバックを得る

---

## 更新履歴

- 2026-01-02: ForSolo Edition作成（実行可能性6点必須、市場機会4点基準）
