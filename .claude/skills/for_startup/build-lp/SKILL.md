---
name: build-lp-for-startup
description: |
  ForStartup特化版: MVP検証用のランディングページを構築する自律実行型スキル。早期ユーザー（early adopters）と外部顧客の2段階展開を想定し、トラクション実績を社会的証明として活用するLP設計を実現します。

  ForStartup固有の特徴:
  - ターゲット二層化（早期ユーザー（early adopters）→外部顧客の2段階展開）
  - 社会的証明の強調（既存顧客導入実績、プロダクト主導成長連携）
  - 創業者ブランド活用による初期信頼獲得
  - 成功LP事例分析統合（15-20事例、成功パターン・失敗教訓）

  使用タイミング:
  - Series A Stage段階（PSF検証段階）
  - 社内PoC完了後の外部展開準備
  - CVR測定の準備

  所要時間: 40-80分（自動実行）
  出力: mvp/lp/（HTML/CSS/JS/README）
trigger_keywords:
  - "/for-startup-build-lp"
  - "LP作成"
  - "ランディングページ"
  - "build landing page"
  - "LP制作"
stage: "planning"
dependencies:
  - validate-10x（10倍優位性検証完了推奨）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/lp/README.md
---

# Build LP Skill (ForStartup Edition)

MVP検証用のランディングページを構築する自律実行型Skill。**ForStartup特化版**では、トラクション実績を社会的証明として活用し、創業者ブランドによる初期信頼獲得を最大化するLP設計を実現します。

---

## このSkillでできること

1. **LP構成設計（ForStartup調整版）**: トラクション実績セクション追加、7→8セクション構成
2. **UVP最適化**: 既存リソース・パートナーシップ活用を明示した3パターン生成
3. **HTML/CSS/JS生成**: レスポンシブ対応の完全なLPコード生成
4. **フォーム統合**: 早期ユーザー（early adopters）用と外部顧客用の2種類
5. **8項目チェック**: コンテンツ/UVP/CTA/レスポンシブ/フォーム/トラクション実績/ブランド/信頼性を検証

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `persona.md`, `psf_diagnosis.md`, `resource_inventory.md`（ForStartup特化） |
| **出力** | `{IDEA_FOLDER}/mvp/lp/`（HTML/CSS/JS/README） |
| **次のSkill** | `/create-sns-content` または `/orchestrate-phase1` |
| **ステージ** | Series A Stage（PSF検証段階、社内PoC完了後の外部展開） |

---

## ForStartup固有の評価基準

### LP構成調整（8セクション）

| セクション | Origin | ForStartup | 理由 |
|----------|--------|------------|------|
| **1. Hero** | UVP + CTA | **UVP + 創業者ブランド + CTA** | ブランド信頼性で初期信頼獲得 |
| **2. Problem** | ペルソナの困りごと | ペルソナの困りごと | 同じ |
| **3. Solution** | どう解決するか | どう解決するか | 同じ |
| **4. Features** | 3つの核心機能 | 3つの核心機能 | 同じ |
| **5. How it Works** | 3ステップ | 3ステップ | 同じ |
| **6. Social Proof** | - | **トラクション実績・導入事例（新規）** | 既存顧客導入実績、パートナーシップ連携 |
| **7. Pricing** | 価格プラン（1-3個） | 価格プラン（1-3個） | 同じ |
| **8. CTA** | メール登録/事前予約 | **早期ユーザー（early adopters）募集 + 外部顧客登録** | 2段階展開 |

### ターゲット二層化

| ターゲット | Origin | ForStartup | 理由 |
|----------|--------|------------|------|
| **主要ターゲット** | 外部顧客のみ | **早期ユーザー（early adopters）（1st）→外部顧客（2nd）** | Series A Stage段階での段階的検証 |
| **CTA設計** | 単一CTA | **社内用CTA + 外部用CTA** | 社内ベータテスト募集と外部顧客登録の並行 |

### 社会的証明の強調

| 指標 | Origin | ForStartup | 理由 |
|------|--------|------------|------|
| **実績表示** | 外部実績のみ | **トラクション実績優先** | Notion: 確立されたブランド1,200名、Stripe: プロダクト主導成長連携 |
| **信頼性構築** | スタートアップ標準 | **創業者ブランド活用** | ブランド信頼性で初期信頼獲得、CAC削減30-50% |

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns（LP成功事例）

#### 1. スタートアップ成功製品（CORP_S009）- LP成功パターン

**LP構成の特徴**:
| セクション | 内容 | ForStartupへの示唆 |
|----------|------|------------------|
| **Hero** | 「無料POSレジアプリ」+ ブランドロゴ | ブランド信頼性の前面押し出し |
| **Social Proof** | プロダクト主導成長グルメ連携90.4万アカウント | トラクション実績の数値化（XX万社、XX名導入） |
| **Pricing** | 初期費用0円（競合30万円との差別化） | 基本無料モデルの訴求 |
| **CTA** | 無料ダウンロード + 営業担当への問い合わせ | 2段階CTA（セルフサインアップ + 営業支援） |

**成果**:
- 90.4万アカウント獲得、市場シェア44%
- LPからの直接CVR: 推定5-8%（業界標準2-3%の2-3倍）
- 1年で10万店舗突破（競合の3倍速）

**ForStartup教訓**:
- **無料訴求の威力**: 初期費用0円を前面に押し出し、競合との差別化を明確化
- **社会的証明の数値化**: 90.4万アカウント、プロダクト主導成長連携等の具体的数値で信頼獲得
- **2段階CTA**: セルフサインアップ + 営業担当への問い合わせで顧客の意思決定段階に対応

#### 2. スタートアップ成功製品（CORP_M001）- トラクション実績活用の成功パターン

**LP構成の特徴**:
| セクション | 内容 | ForStartupへの示唆 |
|----------|------|------------------|
| **Hero** | 「離職防止クラウド」+ ブランド導入実績 | トラクション実績を最優先で訴求 |
| **Social Proof** | 確立されたブランド1,200名導入、回答率96%、継続率98% | 社内先行運用4年の実績を営業資料化 |
| **Testimonial** | ブランド人事部の声（離職率20%→10%改善） | 社内の成功事例を外部向けに展開 |
| **CTA** | 無料トライアル + 運用代行サービス | 低リスク訴求 |

**成果**:
- 継続率98%（業界標準50-70%の2倍）
- 25名〜数万名規模導入、幅広い顧客層
- トラクション実績による初期信頼獲得で、営業コンバージョン率2倍

**ForStartup教訓**:
- **アーリーアダプター導入の実証データ**: 確立されたブランド1,200名で4年間運用、回答率96%等の具体的成果
- **離職防止効果の数値化**: 離職率20%→10%改善、具体的ROIを明示
- **運用代行サービス**: 導入後の伴走支援を訴求、顧客の不安を解消

#### 3. スタートアップ成功製品（CORP_S001）- クロスセル型LP

**LP構成の特徴**:
| セクション | 内容 | ForStartupへの示唆 |
|----------|------|------------------|
| **Hero** | 「キャッシュレス決済導入0円」+ スタートアップ成功製品連携 | エコシステム連携の訴求 |
| **Social Proof** | スタートアップ成功製品90.4万店舗基盤、決済ブランド81種対応 | 既存製品の顧客基盤を活用 |
| **Pricing** | 初期費用0円キャンペーン、決済手数料2.48-3.74% | 手数料0.5%訴求（業界平均3-10%の1/6〜1/20） |
| **CTA** | スタートアップ成功製品ユーザー優先申込 + 新規申込 | 既存顧客へのクロスセル優先 |

**成果**:
- 51.5万店舗導入、市場シェア35%
- 既存製品からのクロスセル成功率推定30-40%（標準5-15%の2-8倍）
- LPからのCVR: 既存ユーザー12-15%、新規ユーザー3-5%

**ForStartup教訓**:
- **エコシステム連携訴求**: スタートアップ成功製品既存顧客へのクロスセル優先、CVR 12-15%実現
- **手数料業界最安クラス**: 競合比1/6〜1/20の差別化を明示
- **2段階CTA**: 既存顧客優先申込で高CVR獲得、新規顧客も並行獲得

#### 4. スタートアップ成功製品 - ブランド信頼性活用

**LP構成の特徴**:
| セクション | 内容 | ForStartupへの示唆 |
|----------|------|------------------|
| **Hero** | 「国内最大級の情報サイト」+ ブランドロゴ | ブランド信頼性の前面押し出し |
| **Social Proof** | 掲載数数十万件、パートナー企業XX社提携 | 圧倒的な掲載数・提携数で信頼獲得 |
| **Features** | メタサーチ型、条件での絞り込み | ユーザー利便性の訴求 |

**成果**:
- 国内最大級のサイトとしての地位確立
- 創業者ブランドによる初期信頼獲得、CAC削減推定30-50%

**ForStartup教訓**:
- **創業者ブランドの前面押し出し**: ブランドロゴを Hero セクションに配置、初期信頼獲得
- **圧倒的な規模の訴求**: 掲載数数十万件、提携数XX社等の数値で差別化

#### 5. スタートアップ成功製品 - 手数料訴求型LP

**LP構成の特徴**:
| セクション | 内容 | ForStartupへの示唆 |
|----------|------|------------------|
| **Hero** | 「手数料業界最安クラス0.5%」+ スタートアップ成功製品連携 | 手数料6-20倍削減の訴求 |
| **Social Proof** | スタートアップ成功製品51.5万加盟店基盤、決済データ審査自動化 | データ資産活用による差別化 |
| **How it Works** | スタートアップ成功製品決済データで自動審査→最短翌日入金 | 審査自動化による時間短縮7倍 |
| **Pricing** | 手数料0.5%〜（業界平均3-10%の1/6〜1/20） | 圧倒的なコスト優位性 |

**成果**:
- 手数料業界最安クラス0.5%（業界平均3-10%の1/6〜1/20）
- 審査自動化で人件費削減、手数料最安化

**ForStartup教訓**:
- **手数料6-20倍削減の訴求**: 業界平均との比較で圧倒的なコスト優位性を明示
- **データ資産活用**: スタートアップ成功製品決済データで信用スコアリング、審査自動化を訴求
- **時間短縮7倍**: 入金1-2週間→最短翌日、時間短縮効果を明示

### Common Pitfalls（失敗パターン）

#### 1. エリクラ - 社会的証明不足

**LP構成の問題点**:
| セクション | 内容 | 問題点 |
|----------|------|--------|
| **Hero** | 「10分単位の仕事マッチング」 | 差別化が弱い（タイミーとの10倍差） |
| **Social Proof** | ユーザー数10万人 | 競合タイミー1,000万人との100倍差 |
| **Features** | 地産地消、10分単位 | 顧客ニーズが弱い（2-3倍程度の差別化） |

**失敗要因**:
- 社会的証明の弱さ: ユーザー数10万人では競合1,000万人に劣後
- 差別化の弱さ: 10分単位、地産地消は顧客ニーズが弱い（2-3倍程度）
- 6年間実証実験レベル継続: 社会的証明を構築できないまま終了

**Lessons Learned**:
- 2-3倍優位性では競合が容易に模倣、10倍優位性が必須
- プラットフォーム事業は初速が命、100倍差を覆せない
- 社会的証明を構築できないまま6年継続は異常、早期撤退判断すべき

#### 2. CODE.SCORE - ターゲット市場の誤認

**LP構成の問題点**:
| セクション | 内容 | 問題点 |
|----------|------|--------|
| **Hero** | 「エンジニアスキル可視化」 | 教育市場のニーズと不一致 |
| **Features** | プログラミングスキル診断 | 競合（atama+, Monoxer）に劣位 |
| **Pricing** | 月額XX円 | 価値提供に見合わない価格設定 |

**失敗要因**:
- ターゲット市場の誤認: エンジニアスキル可視化は教育市場のニーズと不一致
- 競合優位性不足: AI個別最適化学習に対して10倍優位性なし
- 2年で撤退判断: 早期撤退の好例

**Lessons Learned**:
- ターゲット市場のニーズと自社技術のマッチング重要
- 競合が10倍優れている市場には参入しない

#### 3. Coursera個別指導 - カニバリゼーション

**LP構成の問題点**:
| セクション | 内容 | 問題点 |
|----------|------|--------|
| **Hero** | 「個別指導オンライン」 | ベーシックコース（2,178円）との差別化不足 |
| **Pricing** | 月額10,780円 | 5倍の価格差に見合う価値提供できず |
| **Features** | 講師との個別指導 | 講師人件費を賄えない価格設定 |

**失敗要因**:
- 自社製品カニバリゼーション: ベーシックコース（2,178円）が優秀すぎて高額版が売れない
- Unit Economics不健全: 月額10,780円では講師人件費を賄えない
- 1.5年で撤退判断: 超短期撤退、事業性見込めないと即断

**Lessons Learned**:
- 自社製品カニバリゼーション回避、既存製品が優秀すぎると高額版が売れない
- Unit Economicsを厳密に計算、収益性を犠牲にした成長は持続しない

### Quantitative Benchmarks

#### LP成功製品のCVR（メール登録率）

| 製品名 | CVR | トラフィック | 測定期間 | 成功要因 |
|--------|-----|----------|---------|---------|
| **スタートアップ成功製品A** | 推定5-8% | 初期数千/月 | 1年 | 無料訴求、プロダクト主導成長連携、創業者ブランド |
| **スタートアップ成功製品B** | 推定8-12% | 初期数百/月 | 6ヶ月 | トラクション実績（確立されたブランド1,200名）、継続率98% |
| **スタートアップ成功製品C** | 既存ユーザー12-15%、新規3-5% | 既存基盤90.4万 | 6ヶ月 | クロスセル、手数料最安クラス、既存顧客信頼 |

**ForStartup基準**:
- **目標CVR**: 5%以上（一般的LP 2-3%の2倍）
- **早期ユーザー（early adopters）CVR**: 10-15%（トラクション実績活用で高CVR）
- **外部顧客CVR**: 3-5%（創業者ブランド活用で標準より高い）

#### 社会的証明の効果測定

| 社会的証明タイプ | CVR向上効果 | 代表製品 |
|---------------|----------|---------|
| **社内導入実績** | 2-3倍 | スタートアップ成功製品（確立されたブランド1,200名）→ CVR 8-12% |
| **既存製品連携** | 2-4倍 | スタートアップ成功製品（スタートアップ成功製品90.4万）→ CVR 12-15% |
| **ブランドロゴ** | 1.5-2倍 | Airbnb、Booking.com（創業者ブランド）→ CAC削減30-50% |
| **具体的数値** | 1.5-2倍 | Stripe（90.4万アカウント）→ 信頼性向上 |

#### 創業者ブランド活用効果

| 指標 | 創業者ブランドあり | 創業者ブランドなし | 効果 |
|------|-------------------|-------------------|------|
| **CAC** | 推定1-2万円 | 推定5-10万円 | **1/5〜1/10削減** |
| **初期CVR** | 5-8% | 2-3% | **2-3倍向上** |
| **継続率** | 85-90% | 70-80% | **1.1-1.3倍向上** |

### Best Practices

#### 1. トラクション実績の社会的証明化

**実践方法**:
- **スタートアップ成功製品パターン**: 確立されたブランド1,200名で先行運用4年、回答率96%、継続率98%、離職率20%→10%改善
- **スタートアップ成功製品パターン**: プロダクト主導成長連携90.4万アカウント、1年で10万店舗突破
- **数値の具体化**: XX名導入、回答率XX%、継続率XX%、改善率XX%

**効果**:
- トラクション実績による初期信頼獲得、CVR 2-3倍向上
- 外部顧客への営業資料化、営業コンバージョン率2倍

#### 2. 基本無料モデルの訴求

**実践例**:
- **スタートアップ成功製品A**: 初期費用0円（競合30万円との差別化）、基本機能無料
- **スタートアップ成功製品B**: 初期費用0円キャンペーン、決済手数料2.48-3.74%のみ

**効果**:
- 初期導入障壁削減、CVR向上
- 無料訴求で競合との差別化明確化

#### 3. 手数料・オプション課金の明確化

**実践例**:
- **スタートアップ成功製品A**: 決済手数料2.48-3.74%（業界標準）
- **スタートアップ成功製品B**: 手数料0.5%〜（業界平均3-10%の1/6〜1/20）

**効果**:
- 手数料モデルによる収益化明確化
- 競合比での圧倒的コスト優位性訴求

#### 4. クロスセル戦略の組み込み

**実践例**:
- **スタートアップ成功製品A**: スタートアップ成功製品B既存顧客へのクロスセル、CVR 12-15%（標準5-15%の上限）
- **スタートアップ成功製品B**: スタートアップ成功製品A既存顧客へのクロスセル、CVR 10-12%

**効果**:
- クロスセル率57%（標準5-15%の4-11倍）
- LTV向上、単体製品比3-5倍

#### 5. 2段階CTA設計

**実践方法**:
- **早期ユーザー（early adopters）募集**: 社内の関心ある部署・メンバーを募集、10-15%のCVR
- **外部顧客登録**: 創業者ブランド活用、3-5%のCVR

**効果**:
- 社内ベータテストで初期検証、外部展開の成功確率向上
- トラクション実績を外部向け社会的証明に転換

### Reference

- **成功事例**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/
- **VC調達事例**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
- **失敗事例**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/07_Failure_Study/

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 40-80分

### 自動実行ステップ（ForStartup調整版）

1. **【NEW】スタートアップリソース読み込み**: resource_inventory.md → トラクション実績、内部資産の特定
2. リーンキャンバス・ペルソナ読み込み
3. **【NEW】Researchベンチマーク調査**: スタートアップ成功製品等の成功LP事例
4. LP構成設計（8セクション: Hero/Problem/Solution/Features/How it Works/Social Proof/Pricing/CTA）
5. **【NEW】トラクション実績セクション生成**: 内部XX名導入、回答率XX%、継続率XX%
6. UVP最適化（3パターン生成、内部資産活用を明示）
7. HTML生成（セマンティックHTML、創業者ブランドロゴ配置）
8. CSS生成（レスポンシブデザイン、創業者ブランドカラー適用）
9. JavaScript生成（2段階フォームバリデーション: 社内用・外部用）
10. フォーム実装（早期ユーザー（early adopters）募集フォーム + 外部顧客登録フォーム）
11. **【NEW】8項目チェック**: コンテンツ/UVP/CTA/レスポンシブ/フォーム/トラクション実績/ブランド/信頼性
12. **【NEW】Research事例との比較**: スタートアップ成功製品等のCVR、社会的証明と比較
13. 成果物出力

### 8セクション構成（ForStartup調整版）

1. **Hero**: UVP + **創業者ブランドロゴ** + CTA
2. **Problem**: ペルソナの困りごと
3. **Solution**: どう解決するか（内部資産活用を明示）
4. **Features**: 3つの核心機能
5. **How it Works**: 3ステップ
6. **Social Proof（新規）**: 社内導入実績（内部XX名、回答率XX%、継続率XX%）
7. **Pricing**: 価格プラン（基本無料モデル、手数料・オプション課金）
8. **CTA**: 早期ユーザー（early adopters）募集 + 外部顧客登録

### 判定基準（8項目チェック、ForStartup調整版）

| 項目 | 合格条件 |
|------|----------|
| **コンテンツ** | 8セクションすべて実装 |
| **UVP明確性** | 3秒で価値が伝わる（30文字以内）、内部資産活用を明示 |
| **CTA配置** | 2段階CTA（社内用・外部用）、2箇所以上、目立つ配置 |
| **レスポンシブ** | モバイル/タブレット/PC対応 |
| **フォーム動作** | 社内用・外部用の2種類フォーム、送信テスト成功 |
| **トラクション実績（新規）** | 社内導入実績を数値化（XX名、回答率XX%、継続率XX%） |
| **ブランド活用（新規）** | 創業者ブランドロゴ配置、ブランドカラー適用 |
| **信頼性（新規）** | 社会的証明セクション実装、具体的数値で信頼獲得 |

**総合判定**:
- 8/8: ✅ 完了 → LP公開、早期ユーザー（early adopters）募集開始
- 6-7/8: ⚠️ 要修正 → 不合格項目を修正
- 0-5/8: ❌ 再構築 → LP設計から見直し

---

## 成果物フォーマット

### README.md（ForStartup調整版）

```markdown
# Landing Page（ForStartup Edition）

**作成日**: [YYYY-MM-DD]
**プロジェクト**: [プロジェクト名]
**ターゲット**: 早期ユーザー（early adopters）（1st）→外部顧客（2nd）

---

## LP概要

**URL**: [LP URL]
**目標CVR**: 社内5-10%、外部3-5%
**測定期間**: 2週間

---

## 8セクション構成（ForStartup調整版）

1. **Hero**: UVP + 創業者ブランドロゴ + CTA
2. **Problem**: ペルソナの困りごと
3. **Solution**: どう解決するか（内部資産活用）
4. **Features**: 3つの核心機能
5. **How it Works**: 3ステップ
6. **Social Proof**: 社内導入実績（内部XX名、回答率XX%、継続率XX%）
7. **Pricing**: 基本無料モデル、手数料・オプション課金
8. **CTA**: 早期ユーザー（early adopters）募集 + 外部顧客登録

---

## 測定指標（ForStartup調整版）

| 指標 | 目標値 | 測定方法 |
|------|--------|----------|
| **CVR（社内）** | 5-10% | Google Analytics / Mixpanel |
| **CVR（外部）** | 3-5% | Google Analytics / Mixpanel |
| **平均滞在時間** | 60秒以上 | GA / Hotjar |
| **ヒートマップ** | CTA 50%クリック | Hotjar / Crazy Egg |
| **離脱率** | Hero 30%以下 | GA |

---

## Research事例との比較

| 製品名 | CVR | 社会的証明 | 差分 |
|--------|-----|----------|------|
| **Stripe** | 5-8% | プロダクト主導成長連携90.4万 | [比較コメント] |
| **Notion** | 8-12% | リクルート1,200名、継続率98% | [比較コメント] |
| **Figma** | 12-15%（Stripeユーザー） | Stripe90.4万基盤 | [比較コメント] |

---

## 成功判定（2週間後）

- CVR 5%以上（社内）、3%以上（外部） → ✅ PSF合格候補
- CVR 3-5%（社内）、2-3%（外部） → ⚠️ LP改善実施後に再測定
- CVR 3%未満 → ❌ UVP再定義、またはPivot検討
```

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

### 事例参照
- 成功パターン（Tier 1-4）: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#success-patterns
- 失敗パターン: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
- スキル別推奨事例: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-build-lp
- 2段階CTA事例: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#lp-success-patterns

### 全体参照
- ForStartup全体概要: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#forstartup-edition
- VC投資ステージゲート: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-stage-gates
- 撤退基準: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 使用例

```
User: /build-lp-for-startup

Skill:
# LP構築 自律実行開始（ForStartup Edition）

入力ファイル読み込み中...
- lean_canvas.md ✅
- persona.md ✅
- psf_diagnosis.md ✅
- resource_inventory.md ✅（スタートアップリソース棚卸し）

[自動生成中...]
- STEP 1: スタートアップリソース読み込み ✅（営業チャネル2,000名、顧客基盤XX万社）
- STEP 2: リーンキャンバス・ペルソナ読み込み ✅
- STEP 3: Researchベンチマーク調査 ✅（スタートアップ成功製品）
- STEP 4: LP構成設計（8セクション） ✅
- STEP 5: トラクション実績セクション生成 ✅（内部XX名導入、回答率XX%）
- STEP 6: UVP最適化（3パターン、内部資産活用明示） ✅
- STEP 7: HTML生成（創業者ブランドロゴ配置） ✅
- STEP 8: CSS生成（ブランドカラー適用） ✅
- STEP 9: JavaScript生成（2段階フォームバリデーション） ✅
- STEP 10: フォーム実装（社内用・外部用） ✅
- STEP 11: 8項目チェック ✅
- STEP 12: Research事例との比較 ✅
- STEP 13: 成果物出力 ✅

## 完了

成果物: mvp/lp/（HTML/CSS/JS/README）

8項目チェック結果: 8/8 ✅

| 項目 | 判定 |
|------|:----:|
| コンテンツ | ✅ |
| UVP明確性 | ✅ |
| CTA配置 | ✅ |
| レスポンシブ | ✅ |
| フォーム動作 | ✅ |
| トラクション実績 | ✅ |
| ブランド活用 | ✅ |
| 信頼性 | ✅ |

Research事例との比較:
- Stripe: CVR 5-8%、プロダクト主導成長連携90.4万
- Notion: CVR 8-12%、リクルート1,200名、継続率98%
- 本LP: トラクション実績を前面押し出し、目標CVR 社内5-10%、外部3-5%

推奨: LP公開、早期ユーザー（early adopters）募集開始
Seed調達: Series A Stage（PSF検証段階、社内PoC完了後の外部展開）
```

---

## 注意事項

1. **トラクション実績の活用**: リクルートXX名導入、回答率XX%等の具体的数値で社会的証明
2. **2段階展開**: 早期ユーザー（early adopters）→外部顧客の段階的検証
3. **創業者ブランド**: ブランドロゴ、ブランドカラー、ブランド信頼性を最大限活用
4. **Research事例との比較**: Stripe、Notion等の成功LP事例とのCVR、社会的証明比較
5. **基本無料モデル**: 初期導入障壁削減、手数料・オプション課金で収益化

---

## 更新履歴

- 2026-01-02: ForStartup特化版として作成、Recruit Product Research統合（15事例）

---

**テンプレートバージョン**: v2.0-ForStartup
**最終更新**: 2026-01-02
**作成者**: Claude Code
**ForStartup特化要素**: トラクション実績活用、2段階展開、創業者ブランド活用、15事例統合
