---
name: validate-cpf-for-recruit
description: |
  ForRecruit特化版: CPF（Customer Problem Fit）達成基準に基づき、各種成果物を統合して総合判定を行う自律実行型スキル。

  ForRecruit固有の特徴:
  - インタビュー数基準緩和（15人以上、社内ネットワーク・既存顧客基盤活用）
  - 課題共通率基準緩和（60%以上、社内PoC前提での段階的検証）
  - 緊急性スコア基準緩和（6/10以上、社内リソース活用で解決可能）
  - 社内先行導入オプション統合（Geppo、エリクラ事例）
  - Recruit Product Research統合（30-40事例、成功パターン・失敗教訓）

  4つの定量指標（インタビュー数/課題共通率/支払い意思/緊急性）で判定し、次のステップ（PSF検証 or ピボット）を提案します。

  使用タイミング：
  - ペルソナ・仮想インタビュー・課題裏付け調査完了後
  - CPF達成を判断したい（Ring制度Ring 1～Ring 2段階）
  - PSF検証へ進むべきか確認したい

  所要時間：5-10分（自動実行）
  出力：cpf_judgment.md

---

# Validate CPF Skill (ForRecruit Edition)

起業の科学のCPF達成基準に基づき、総合判定を行う自律実行型Skill。**ForRecruit特化版**では、既存顧客基盤・社内ネットワーク・Ring制度を活用した段階的検証を前提としています。

---

## このSkillでできること

1. **成果物統合**: persona.md, interview_simulation.md, problem_research.md を読み込み
2. **4指標評価（ForRecruit調整版）**: 社内リソース活用を前提とした基準
3. **総合判定**: CPF達成/要改善/見直しの判断
4. **社内先行導入オプション**: Geppo/エリクラ事例に基づく推奨
5. **次ステップ提案**: PSF検証へ進むか、Ring継続か、改善すべきかを提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`, `interview_simulation.md`, `problem_research.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/documents/2_discovery/cpf_judgment.md` |
| **次のSkill** | `/research-competitors` → `/validate-psf`（CPF達成時） |
| **ステージ** | CPF検証（Ring制度Ring 1～Ring 2） |

---

## ForRecruit固有の評価基準

### CPF達成基準（調整版）

このスキルはRing制度の**Ring 1～Ring 2段階**に対応します。

| 指標 | Origin基準 | ForRecruit基準 | 理由 |
|------|----------|-------------|------|
| **インタビュー数** | 20人以上 | **15人以上** | 社内ネットワーク活用、既存顧客基盤活用で効率化 |
| **課題共通率** | 70%以上 | **60%以上** | 社内PoC前提での段階的検証、早期ピボット前提 |
| **支払い意思（WTP）** | 50%以上 | **40%以上** | 社内実証段階での検証、Ring 2での本格検証 |
| **緊急性スコア** | 7/10以上 | **6/10以上** | 社内リソース活用で解決可能、リスク許容度高め |

### 判定基準（ForRecruit調整版）

#### 個別指標判定

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|-----------|----------|
| インタビュー数 | 15人以上 | 10-14人 | 9人以下 |
| 課題共通率 | 60%以上 | 50-59% | 50%未満 |
| 支払い意思 | 40%以上 | 25-39% | 25%未満 |
| 緊急性 | 6/10以上 | 4-5.9/10 | 4未満 |

#### 総合判定

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **CPF達成** | すべて✅ | PSF検証へ（/research-competitors）、Ring 2進出 |
| ⚠️ **社内先行導入検討** | 2-3個✅、1個⚠️ | Geppo/エリクラ事例参照、Ring 1継続 |
| ⚠️ **要改善** | 2個以上⚠️ | 追加インタビュー、ペルソナ修正 |
| ❌ **見直し** | 1個以上❌ | 課題仮説を根本から再検討 |

---

## Domain-Specific Knowledge (from Recruit_Product_Research)

### Success Patterns（CPF検証成功事例）

#### 1. Airレジ（CORP_S009）- CPF 65%
**検証手法**:
- User Research Count: **30回**（ホットペッパーグルメ既存顧客ヒアリング）
- Problem Commonality: **75%**（中小飲食店・小売店の75%がPOSレジ未導入）
- 営業網活用: ホットペッパーグルメ営業網2,000名で現場課題収集
- ベータテスト: 限定ユーザーでのプロトタイプ検証

**成果**:
- 90.4万アカウント獲得、市場シェア44%
- 1年で10万店舗突破（競合Squareの3倍速）

**ForRecruit教訓**:
- 既存顧客基盤活用により、User Research 30回を低コストで実現
- 営業網2,000名による現場観察で高いProblem Commonality確保
- ベータテスト段階での早期検証、リスク低減

#### 2. Airペイ（CORP_S001）- CPF 70%
**検証手法**:
- User Research Count: **100回**（Airレジ既存顧客90.4万店舗+新規ヒアリング）
- Problem Commonality: **85%**（小規模店舗の85%がキャッシュレス対応未導入）
- 既存顧客活用: Airレジ導入店舗へのクロスセル
- 店舗経営者インタビュー、プロトタイプ検証

**成果**:
- 51.5万店舗導入、市場シェア35%
- LTV/CAC比 10-15倍（健全なUnit Economics）

**ForRecruit教訓**:
- 既存製品（Airレジ）の顧客基盤を活用し、User Research 100回を実現
- クロスセル戦略で初期CAC削減（推定2-3万円、競合比1/3～1/5）
- Problem Commonality 85%の高水準で市場ニーズ確証

#### 3. Geppo（CORP_M001）- CPF 80%
**検証手法**:
- User Research Count: **50回以上**（サイバーエージェント社内+リクルート社内）
- Problem Commonality: **65%**（推定、HR Tech業界標準）
- 自社先行導入: サイバーエージェント社内2013年～運用（回答率96%）
- リクルート社内: 2018年～1,200名規模で先行運用

**成果**:
- 継続率98%、離職率改善（20%→10%）
- 25名～数万名規模導入、幅広い顧客層

**ForRecruit教訓**:
- **社内先行導入の成功モデル**: 自社で4年間運用後に外販、リスク低減
- 回答率96%の実証データが営業資料になる（顧客獲得率30%向上、推定）
- Problem Commonality 65%でもPMF到達、社内検証の有効性

#### 4. SUUMO - CPF 70%
**検証手法**:
- User Research Count: **30回**（不動産仲介会社、ユーザーインタビュー）
- Problem Commonality: **70%**（推定、不動産情報の非対称性）
- 既存顧客活用: リクルート既存不動産事業ネットワーク

**成果**:
- 国内最大級の不動産情報サイト
- LTV/CAC比 10-20倍

**ForRecruit教訓**:
- 既存事業ネットワーク活用でUser Research 30回を効率化
- 不動産仲介会社との既存信頼関係でProblem Commonality検証精度向上

#### 5. スタディサプリ - CPF 70%
**検証手法**:
- User Research Count: **30回**（学校・個人ユーザー混合インタビュー）
- Problem Commonality: **70%**（推定、教育費高騰・地域教育格差）
- 混合インタビュー: 学校（BtoB）+保護者・生徒（BtoC）の両面検証

**成果**:
- 会員数100万人突破
- 学校版・個人版の複数展開

**ForRecruit教訓**:
- BtoB/BtoC混合市場での両面検証の重要性
- User Research 30回で両面のニーズを確証

### Common Pitfalls（失敗パターン）

#### 1. CODE.SCORE（CORP_F002）- CPF 38%
**失敗要因**:
- User Research不足: 推定10-20回（Airレジ等の1/2～1/3）
- Problem Commonality: **38%**（エンジニア採用課題の過小評価）
- 競合優位性不足: atama+, Monoxerに劣位
- サービス期間: 約2年で撤退

**Lessons Learned**:
- Problem Commonality 38%では市場ニーズ不足
- 既存顧客基盤との関連性を最優先で確認すべき
- 競合が10倍優れている市場には参入しない

#### 2. エリクラ - CPF 52%（推定）
**失敗要因**:
- 差別化要素「10分単位」「地産地消」は顧客ニーズが弱い
- Problem Commonality: 推定52%（単発バイトニーズは普遍的だが、10分単位は限定的）
- 6年間「実証実験」レベル継続は異常
- サービス期間: 6年（2018-2025）で撤退

**Lessons Learned**:
- 社内PoC期間は**1-2年に限定**、成長曲線が見えない場合は速やかに撤退
- 差別化は「自社が提供したいもの」でなく「顧客が本当に求めるもの」
- 6年間実証実験は失敗、早期ピボット判断が重要

#### 3. リクルートDMPフォロー
**失敗要因**:
- 採用担当者のDMP活用意欲を過大評価
- User Research不足: 既存顧客への軽いヒアリングで済ませた
- ニーズ検証不足: 定量調査併用せず

**Lessons Learned**:
- 既存顧客ヒアリングでもバイアスに注意、定量検証必須
- 「既存顧客が使いたいと言っている」≠「実際に使う・お金を払う」

### Quantitative Benchmarks

| 指標 | 成功製品（Official） | 失敗製品（Withdrawn） | ForRecruit推奨 |
|------|------------------|------------------|-------------|
| **User Research Count** | 平均35.2回（範囲10-100回） | 推定10-20回 | **15回以上** |
| **Problem Commonality** | 平均72.9%（範囲52-85%） | 推定52-65% | **60%以上** |
| **社内先行導入率** | 31%（5/16製品） | 0% | 推奨オプション |
| **検証期間** | 平均2-3ヶ月 | - | 社内PoC 1-2年以内 |

**ForRecruit特化指標**:
- **既存顧客活用率**: 成功製品85%（12/16製品）
- **営業網活用率**: 成功製品48%（Airレジ、Airペイ、レストランボード等）
- **社内先行導入成功率**: 100%（Geppo、エリクラ等、最終的に外販またはピボット）

### Best Practices

#### 1. 既存顧客基盤活用による低コスト検証
- **Airレジ**: ホットペッパーグルメ加盟店8万店へのヒアリング
- **Airペイ**: Airレジ既存顧客90.4万店舗からのフィードバック
- **効果**: User Research 30-100回を低コストで実施、CAC削減

#### 2. 社内ネットワーク活用インタビュー
- **営業網活用**: ホットペッパーグルメ営業網2,000名による現場課題収集
- **効果**: 正直なフィードバック獲得、顧客との信頼関係構築

#### 3. 社内先行導入によるリスク低減
- **Geppo**: リクルート1,200名で先行運用→離職防止効果実証→外販
- **エリクラ**: サイバーエージェント社内2013年～運用→回答率96%実証
- **効果**: PMF到達前にリスク低減、実証データが営業資料になる
- **注意**: 社内PoC期間は1-2年に限定、成長曲線が見えない場合は撤退

#### 4. 段階的投資（Ring制度対応）
- **Ring 1**: 社内PoC、User Research 15回、Problem Commonality 60%
- **Ring 2**: 外部ベータテスト、User Research 30回、Problem Commonality 70%
- **Ring 3**: 本格展開、User Research 50回以上、Problem Commonality 75%以上

### Reference

- 詳細: @Recruit_Product_Research/analysis/integrated_analysis_report.md
- CPFパターン: @Recruit_Product_Research/analysis/cpf_patterns/
- 成功事例: @Recruit_Product_Research/documents/SUCCESS/
- 失敗事例: @Recruit_Product_Research/documents/WITHDRAWN/

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/persona_creation.md
- @startup_science/01_stages/cpf/customer_interview.md
- **@Recruit_Product_Research/analysis/integrated_analysis_report.md**

---

## Instructions

### 自動実行フロー

**STEP 1: 成果物読み込み**
- `persona.md` → ペルソナ情報
- `interview_simulation.md` → 仮想インタビュー結果、3U検証スコア
- `problem_research.md` → 課題裏付けスコア

**STEP 2: インタビュー数の集計**
- 実インタビュー数（もしあれば）
- 仮想インタビューのペルソナ数
- 課題裏付け調査の生ログ件数から推定

**STEP 3: 課題共通率の算出**
- 複数ペルソナ/生ログから共通課題の割合を計算
- 例: 10人中6人が同じ課題 → 60%（ForRecruit基準達成）

**STEP 4: 支払い意思（WTP）の評価**
- インタビュー結果から「お金を払う」回答を抽出
- WTP金額の中央値・範囲も記録

**STEP 5: 緊急性スコアの算出**
- 3U検証の「Urgent」スコア
- 生ログの「今すぐ」「早く」表現の頻度

**STEP 6: ForRecruit適合性評価（追加）**
- 既存顧客基盤との関連性（5点満点）
- 社内先行導入可能性（7点満点）
- 営業網活用可能性（5点満点）
- ブランド信頼性活用（3点満点）

**STEP 7: 総合判定**
- 4指標の個別判定（ForRecruit基準）
- 総合CPF達成判定
- 社内先行導入オプションの検討
- 次ステップの提案

**STEP 8: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/documents/2_discovery/cpf_judgment.md`

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## 成果物フォーマット

```markdown
# CPF判定レポート（ForRecruit Edition）

**作成日**: [YYYY-MM-DD]
**対象ソリューション**: [ソリューション名]
**総合判定**: ✅ CPF達成 / ⚠️ 社内先行導入検討 / ⚠️ 要改善 / ❌ 見直し
**Ring制度ステージ**: Ring 1 / Ring 2 / Ring 3

---

## エグゼクティブサマリー

| 指標 | ForRecruit目標 | 実績 | 判定 |
|------|-------------|------|:----:|
| インタビュー数 | 15人以上 | XX人 | ✅/⚠️/❌ |
| 課題共通率 | 60%以上 | XX% | ✅/⚠️/❌ |
| 支払い意思（WTP） | 40%以上 | XX% | ✅/⚠️/❌ |
| 緊急性スコア | 6/10以上 | X.X/10 | ✅/⚠️/❌ |

**総合判定**: [判定とその理由]

**ベンチマーク比較**:
- User Research Count: [実績XX回] vs [成功製品平均35.2回]
- Problem Commonality: [実績XX%] vs [成功製品平均72.9%]
- 参照事例: [Airレジ/Geppo/その他]

---

## ForRecruit適合性評価

| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 既存顧客基盤との関連性 | X/5 | [既存事業名]の顧客層と[関連性] |
| 社内先行導入可能性 | X/7 | [社内部門]で先行運用可能、[Geppo/エリクラ]事例参照 |
| 営業網活用可能性 | X/5 | [営業網名]で[活用方法] |
| ブランド信頼性活用 | X/3 | リクルートブランドで[信頼獲得方法] |
| **合計** | **XX/20** | |

**ForRecruit適合性判定**:
- 15点以上: ✅ 既存資産活用の好機、Ring 2進出推奨
- 10-14点: ⚠️ 一部資産活用可能、外部検証と併用
- 9点以下: ❌ 資産活用困難、Origin基準で再評価

---

## 詳細分析

### 1. インタビュー分析

| 種別 | 件数 | 備考 |
|------|------|------|
| 実インタビュー | X人 | [実施方法] |
| 仮想インタビュー | X人 | [ペルソナ数] |
| 課題裏付け生ログ | X件 | [収集元] |
| **合計** | **XX件** | ForRecruit基準15件以上 |

**評価**: [インタビュー数の評価とコメント]

**ベンチマーク比較**:
- Airレジ: 30回（ホットペッパーグルメ既存顧客）
- Airペイ: 100回（Airレジ既存顧客90.4万店舗）
- Geppo: 50回以上（社内先行導入）

---

### 2. 課題共通率

**特定された共通課題（Top 3）**:

| 順位 | 課題 | 出現率 |
|:----:|------|:------:|
| 1 | [課題1] | XX% |
| 2 | [課題2] | XX% |
| 3 | [課題3] | XX% |

**課題共通率**: XX%（ForRecruit目標60%以上）

**評価**: [課題共通率の評価とコメント]

**ベンチマーク比較**:
- 成功製品平均: 72.9%
- Airペイ: 85%（小規模店舗の85%がキャッシュレス未導入）
- Airレジ: 75%（中小飲食店の75%がPOSレジ未導入）
- Geppo: 65%（HR Tech業界標準）

---

### 3. 支払い意思（WTP）

**WTP分布**:

| 回答 | 人数 | 割合 |
|------|------|------|
| 「絶対払う」 | X人 | XX% |
| 「おそらく払う」 | X人 | XX% |
| 「払わない」 | X人 | XX% |

**WTP金額（中央値）**: 月額X,XXX円
**WTP金額（範囲）**: X,XXX円〜X,XXX円

**評価**: [WTPの評価とコメント]

---

### 4. 緊急性スコア

**3U検証結果**:

| 要素 | スコア | 評価 |
|------|:------:|:----:|
| Unworkable（切実性） | X/5 | ✅/⚠️/❌ |
| Unavoidable（不可避性） | X/5 | ✅/⚠️/❌ |
| Urgent（今すぐ性） | X/5 | ✅/⚠️/❌ |

**緊急性平均スコア**: X.X/10（ForRecruit目標6/10以上）

**評価**: [緊急性の評価とコメント]

---

## CPF達成判定

### 判定結果: [✅ CPF達成 / ⚠️ 社内先行導入検討 / ⚠️ 要改善 / ❌ 見直し]

**判定理由**:
[具体的な理由を記述]

**Ring制度判定**:
- Ring 2進出: [可/条件付き可/不可]
- 社内先行導入検討: [推奨/検討/不要]

---

## 社内先行導入オプション（該当時のみ）

### 推奨理由
- Problem Commonality XX% → 社内PoC段階での検証に適合
- [部門名]で先行運用可能（推定XX名規模）
- Geppo/エリクラ成功事例を参照

### 実施計画
**対象部門**: [部門名]（規模XX名）
**検証期間**: 1-2年以内にPMF判断
**成功基準**:
- 継続率80%以上
- 課題解決効果の定量データ取得
- 外販時の営業資料化

**リスク**:
- 社内PoC期間長期化（エリクラ6年は失敗、1-2年に限定）
- ピボット困難性（社内で既に運用中だと変更しにくい）
- 撤退判断の遅れ（成長曲線が見えない場合は速やかに撤退）

---

## 改善提案（要改善/見直しの場合）

### 改善が必要な項目

| 指標 | 現状 | 目標 | 改善案 |
|------|------|------|--------|
| [指標1] | XX | XX | [改善案] |
| [指標2] | XX | XX | [改善案] |

### 具体的アクション

1. [アクション1]
2. [アクション2]
3. [アクション3]

---

## 次のステップ

### CPF達成の場合

| コマンド | 内容 | Ring制度ステージ |
|----------|------|---------------|
| `/research-competitors` | 競合調査へ（PSF検証開始） | Ring 2進出 |
| `/validate-psf` | PSF検証へ | Ring 2 |

### 社内先行導入検討の場合

| コマンド | 内容 | Ring制度ステージ |
|----------|------|---------------|
| `/build-internal-pilot` | 社内先行導入計画作成 | Ring 1継続 |
| `/simulate-interview` | 追加インタビュー実施（社内） | Ring 1 |

### 要改善/見直しの場合

| コマンド | 内容 | Ring制度ステージ |
|----------|------|---------------|
| `/simulate-interview` | 追加インタビュー実施 | Ring 1継続 |
| `/create-persona` | ペルソナ再定義 | Ring 1 |
| `/discover-demand` | 別の課題を探索 | Ring 0 |

---

## 参照成果物

| ファイル | 作成日 |
|----------|--------|
| persona.md | [日付] |
| interview_simulation.md | [日付] |
| problem_research.md | [日付] |

---

## Research Case Studies参照

**成功事例**:
- Airレジ: CPF 65%, User Research 30回, Problem Commonality 75%
- Airペイ: CPF 70%, User Research 100回, Problem Commonality 85%
- Geppo: CPF 80%, User Research 50回以上, Problem Commonality 65%

**失敗事例**:
- CODE.SCORE: CPF 38%, Problem Commonality低値、2年で撤退
- エリクラ: CPF 52%, 6年間実証実験レベル、最終撤退
- リクルートDMPフォロー: User Research不足、ニーズ過大評価

**Quantitative Benchmarks**:
- User Research Count: 成功製品平均35.2回、ForRecruit推奨15回以上
- Problem Commonality: 成功製品平均72.9%、ForRecruit推奨60%以上
- 社内先行導入率: 成功製品31%、推奨オプション
```

---

## ForRecruit Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/recruit_specific_frameworks.md#cpf-evaluation
- Ring制度詳細: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-system
- 社内リソース活用: @.claude/skills/_shared/recruit_specific_frameworks.md#resource-leverage
- ForRecruit評価基準: @.claude/skills/_shared/knowledge_base.md#forrecruit-evaluation

### 事例参照
- 成功パターン（Tier 1-4）: @.claude/skills/_shared/case_reference_for_recruit.md#success-patterns
- 失敗パターン: @.claude/skills/_shared/case_reference_for_recruit.md#failure-patterns
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-validate-cpf
- Geppo CPF 80%事例: @Recruit_Product_Research/documents/SUCCESS/CORP_M001_geppo.md

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 使用例

```
User: /validate-cpf-for-recruit

Skill:
# CPF判定 自律実行開始（ForRecruit Edition）

入力ファイル読み込み中...
- persona.md ✅
- interview_simulation.md ✅
- problem_research.md ✅

[自動判定中...]
- STEP 1: 成果物読み込み ✅
- STEP 2: インタビュー数集計 ✅ (18件 - ForRecruit基準達成)
- STEP 3: 課題共通率算出 ✅ (62% - ForRecruit基準達成)
- STEP 4: WTP評価 ✅ (42% - ForRecruit基準達成)
- STEP 5: 緊急性スコア算出 ✅ (6.5/10 - ForRecruit基準達成)
- STEP 6: ForRecruit適合性評価 ✅ (16/20点)
- STEP 7: 総合判定 ✅
- STEP 8: 成果物出力 ✅

## 完了

成果物: cpf_judgment.md
総合判定: ✅ CPF達成（ForRecruit基準）
Ring制度: Ring 2進出可能

| 指標 | 実績 | ForRecruit基準 | 判定 |
|------|------|-------------|:----:|
| インタビュー数 | 18人 | 15人以上 | ✅ |
| 課題共通率 | 62% | 60%以上 | ✅ |
| WTP | 42% | 40%以上 | ✅ |
| 緊急性 | 6.5/10 | 6/10以上 | ✅ |

ForRecruit適合性: 16/20点（既存顧客基盤活用の好機）
ベンチマーク比較: Airレジ事例（CPF 65%, User Research 30回）に近似

推奨: `/research-competitors` で競合調査→PSF検証へ
Ring制度: Ring 2進出
```

---

## 注意事項

1. **ForRecruit基準の適用**: Origin基準より緩和されているが、社内リソース活用が前提
2. **社内先行導入の有効性**: Geppo、エリクラ事例参照、ただし期間は1-2年に限定
3. **既存顧客基盤活用**: User Research 15回を低コストで実現、CAC削減
4. **Ring制度連携**: Ring 1（社内PoC）→Ring 2（外部ベータ）→Ring 3（本格展開）
5. **早期撤退判断**: 成長曲線が見えない場合は1-2年で撤退、エリクラ6年は失敗例

---

## 更新履歴

- 2026-01-02: ForRecruit特化版として作成、Recruit Product Research統合（30事例）

---

**テンプレートバージョン**: v4.0-ForRecruit
**最終更新**: 2026-01-02
**作成者**: Claude Code
**ForRecruit特化要素**: CPF基準緩和、社内先行導入オプション、30事例統合、Ring制度連携
