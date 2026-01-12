---
name: research-problem-for-startup
description: |
  ForStartup特化版: Web上の生ログから課題の裏付けを発見する自律実行型スキル。Reddit、Yahoo!知恵袋、X、Stack Overflow等から「困りごと」を30件以上収集し、5軸（頻度/深刻度/既存策不満/支払い匂い/緊急性）で50点満点スコアリング。定性インサイト抽出、既存代替案分析を実施し、課題仮説の裏付けを判定します。

  ForStartup固有の特徴:
  - インタビュー数基準緩和（10人以上、社内ネットワーク活用・既存顧客基盤活用）
  - 課題共通率基準緩和（60%以上、内部検証前提での段階的検証）
  - 自社/グループ先行導入オプション推奨（Geppo、エリクラ事例）
  - Seed調達各ステージ対応

  使用タイミング：
  - リーンキャンバス作成後
  - 課題仮説の裏付けを確認したい
  - CPF検証の補強材料が欲しい（企業内リソース活用）

  所要時間：30-60分（自動実行）
  出力：problem_research.md
trigger_keywords:
  - "課題調査"
  - "problem research"
  - "3U検証"
  - "課題裏付け"
stage: planning
dependencies:
  - create-persona（ペルソナ作成完了）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/problem_research.md
---

# Research Problem Skill (ForStartup Edition)

Web上の生ログから課題の裏付けを発見する自律実行型Skill。**ForStartup特化版**では、既存顧客基盤活用とアーリーアダプター導入による低コスト・低リスク検証を前提としています。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Yahoo!知恵袋/X/Stack Overflow等から「困りごと」を収集
2. **5軸スコアリング**: 頻度/深刻度/既存策不満/支払い匂い/緊急性で評価（50点満点）
3. **定性インサイト抽出**: 生の声から本質的課題を発見
4. **既存代替案分析**: 何が使われていて、何が不満か
5. **課題裏付け判定**: 仮説が正しいかを判定
6. **ForStartup適合性評価**: アーリーアダプター導入可能性、既存顧客基盤活用可能性を評価

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`（必須）, `lean_canvas.md`（オプション） |
| **フォールバック** | persona.md未存在時 → demand_discovery.mdから課題情報を取得 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/2_discovery/problem_research.md` |
| **次のSkill** | `/validate-cpf` |
| **ステージ** | CPF検証（Seed調達Seed Stage～Series A Stage） |

---

## ForStartup固有の評価基準

### 課題検証基準（緩和版）

このスキルはSeed調達の**Seed Stage～Series A Stage段階**に対応します。

| 指標 | Origin基準 | ForStartup基準 | 理由 |
|------|----------|-------------|------|
| インタビュー数 | 20人以上 | **10人以上** | 社内ネットワーク活用、既存顧客基盤活用で効率化 |
| 課題共通率 | 70%以上 | **60%以上** | 内部検証前提での段階的検証、早期ピボット前提 |
| 緊急性スコア | 7/10以上 | **6/10以上** | スタートアップリソース活用で解決可能、リスク許容度高め |

### アーリーアダプター導入オプション

ForStartupでは、自社/グループ先行導入による課題検証が可能です。

**実施例**:
- **Geppo**: サイバーエージェント社内2013年～（回答率96%）、リクルート2018年～（1,200名規模）先行運用
- **エリクラ**: リクルート1,200名で検証後に外販（6年間実証実験、最終的に撤退）

**先行導入のメリット**:
- **リスク低減**: PMF到達前にリスク低減、離職率改善等の定量データ取得
- **営業資料化**: 自社での実証データが営業資料になる（顧客獲得率30%向上、推定）
- **製品改善**: 従業員フィードバックで製品改善、実運用での課題発見

**先行導入のリスク**:
- **時間コスト**: Geppoは4年間内部運用後に外販、エリクラは6年実証実験
- **ピボット困難**: 社内で既に運用中だとピボットしにくい
- **撤退判断の遅れ**: エリクラは6年継続も最終的に撤退、早期撤退判断が重要

**推奨期間**: 1-2年以内にPMF判断、達成できなければ速やかに撤退

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns（課題検証成功事例）

1. **Geppo（CORP_M001）**:
   - **課題**: 離職の兆候を早期発見する手段がない（びっくり退職）
   - **課題共通率**: 65%（推定、HR Tech業界標準）
   - **検証手法**: サイバーエージェント社内4年間運用（回答率96%）、確立されたブランド1,200名導入
   - **インタビュー数**: 50回以上（推定、社内検証含む）
   - **成果**: 継続率98%、25名～数万名規模導入

2. **Airレジ（CORP_S009）**:
   - **課題**: 中小飲食店・小売店の75%がPOSレジ未導入（初期費用高額）
   - **課題共通率**: 75%
   - **検証手法**: グルメサイト加盟店ヒアリング30社、ベータテスト
   - **インタビュー数**: 30回
   - **成果**: 90.4万アカウント獲得、市場シェア44%

3. **Airペイ（CORP_S001）**:
   - **課題**: 小規模店舗の85%がキャッシュレス対応未導入（初期費用・月額費用高額）
   - **課題共通率**: 85%
   - **検証手法**: スタートアップ成功製品既存顧客ヒアリング、店舗経営者インタビュー100回
   - **インタビュー数**: 100回（推定）
   - **成果**: 51.5万店舗導入、市場シェア35%

4. **レストランボード**:
   - **課題**: 飲食店の予約管理の非効率性（電話・紙台帳）
   - **課題共通率**: 推定70%
   - **検証手法**: グルメサイト掲載店舗ヒアリング
   - **インタビュー数**: 推定20-30回
   - **成果**: グルメサイトとの連携で導入促進

5. **Airキャッシュ**:
   - **課題**: 中小企業の80%が資金繰り課題を抱える
   - **課題共通率**: 80%
   - **検証手法**: スタートアップ成功製品決済データ分析、導入店舗ヒアリング
   - **インタビュー数**: 推定20回
   - **成果**: 手数料0.5%（業界平均の1/6～1/20）

6. **SUUMO**:
   - **課題**: 不動産情報の非対称性（物件情報の不透明性）
   - **課題共通率**: 推定70%
   - **検証手法**: 不動産仲介会社・ユーザーインタビュー30回
   - **インタビュー数**: 30回
   - **成果**: 国内最大級の不動産情報サイト

7. **じゃらん**:
   - **課題**: 宿泊施設の集客難（地方旅館の情報発信力不足）
   - **課題共通率**: 推定65%
   - **検証手法**: 宿泊施設経営者ヒアリング
   - **インタビュー数**: 推定20回
   - **成果**: 国内最大級の宿泊予約サイト

8. **スタディサプリ**:
   - **課題**: 教育費高騰・地域教育格差
   - **課題共通率**: 推定70%
   - **検証手法**: 学校・個人ユーザー混合インタビュー30回
   - **インタビュー数**: 30回
   - **成果**: 会員数100万人突破

9. **Airシフト**:
   - **課題**: 飲食店のシフト管理の非効率性（紙・Excel）
   - **課題共通率**: 推定65%
   - **検証手法**: スタートアップ成功製品ユーザーからの要望収集
   - **インタビュー数**: 推定15回
   - **成果**: エコシステム統合でLTV向上

10. **ホットペッパービューティー**:
    - **課題**: 美容院・サロンの集客難
    - **課題共通率**: 推定70%
    - **検証手法**: 営業網経由の美容業界ヒアリング
    - **インタビュー数**: 推定20回
    - **成果**: 国内最大級の美容サロン予約サイト

### Common Pitfalls（失敗パターン）

1. **CODE.SCORE（CORP_F002）**:
   - **失敗要因**: エンジニア採用課題の過小評価、課題共通率38%
   - **教訓**: ニーズ検証の甘さ、競合優位性不足
   - **ForStartup教訓**: 既存顧客基盤との関連性を最優先で確認、競合が10倍優れている市場には参入しない

2. **エリクラ**:
   - **失敗要因**: 差別化要素「10分単位」「地産地消」は顧客ニーズが弱い、6年間実証実験レベル継続
   - **教訓**: 6年間「実証実験」は異常、早期撤退判断すべき
   - **ForStartup教訓**: 内部検証期間は1-2年に限定、成長曲線が見えない場合は速やかに撤退

3. **既存事業DMP相当品フォロー**:
   - **失敗要因**: 採用担当者のDMP相当品活用意欲を過大評価、ニーズ検証不足
   - **教訓**: 軽いヒアリングで済ませず、定量調査併用
   - **ForStartup教訓**: 既存顧客ヒアリングでもバイアスに注意、定量検証必須

4. **スタディサプリ個別指導相当品オンライン中学講座**:
   - **失敗要因**: 月額10,780円では講師人件費を賄えない、スタートアップ成功製品カニバリゼーション
   - **教訓**: Unit Economics厳密計算、収益性犠牲の成長は持続せず
   - **ForStartup教訓**: スタートアップ成功製品カニバリゼーション回避、価格差に見合う価値提供

### Quantitative Benchmarks

- **課題共通率**: 成功製品平均72.9%、失敗製品平均52-65%、ForStartup推奨: **60%以上**
- **User Research Count**: 成功製品平均35.2回、ForStartup推奨: **10回以上**（既存顧客基盤活用）
- **アーリーアダプター導入率**: 成功製品31%（5/16製品: Geppo、エリクラ、スタサプ学校向け等）
- **検証期間**: 成功製品平均2-3ヶ月、ForStartup推奨: **内部検証 1-2年以内にPMF判断**

### Reference

- 詳細: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/cpf_patterns/
- 成功事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/ /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/

---

## Tier 4: 2025-2026最新事例（ForStartup特化）

### Tier 4A: Enterprise AI導入の障壁発見（Cohere - 2025-08）

**Cohere（Aidan Gomez）: Series D2 2025-08, $6.8B valuation**

出典: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/08_Emerging/EMERGING_112_cohere.md`

#### 課題発見プロセス

**着想源**:
- Google BrainでTransformer論文（"Attention Is All You Need"）共著後、エンタープライズAI導入の3大障壁を発見
  - **データプライバシー**: 企業データを外部クラウド（OpenAI）に送信したくない
  - **コンプライアンス**: 金融・医療・公共セクターの規制要件未対応
  - **カスタマイズ**: 汎用LLMより業界・企業特化モデルが必要

**インタビュー手法の詳細**:
- **インタビュー数**: 500+（Fortune 500企業、複数セクター検証）
- **手法**:
  - Fortune 500企業向けパイロット（複数業界で同時展開）
  - 業界別ワークショップ（金融、医療、製造、公共セクター）
  - セキュリティ監査ワーキンググループ
  - Geoffrey Hinton、Yee Whye Tehとの学界ネットワーク活用
- **対象**: 金融、ヘルスケア、製造業、公共セクターの規制産業
- **質問内容**:
  - 現在のAI導入の障壁は何か
  - データプライバシーの懸念点
  - 規制コンプライアンスの要件
  - 既存ソリューション（OpenAI API、Google Vertex AI）の不満点
  - 専用AI基盤への支払い意思

#### 3U検証の実例

**Unworkable（現状では解決不可能）**:
- 既存のOpenAI・Googleモデルは企業規制対応不可
- データプライバシー: 外部クラウド送信は金融・医療規制で禁止
- コンプライアンス: HIPAA、GDPR、SOC 2対応が不十分
- カスタマイズ: 汎用LLMでは業界特化ニーズを満たせない（Fine-tuningコストが$$$）

**Unavoidable（避けられない）**:
- 金融・医療・公共セクターの企業はAI導入が急務
- 競合企業がAI活用で優位性を獲得中
- 規制対応しないとビジネスリスク（年間$100M以上の機会損失）

**Urgent（緊急性が高い）**:
- **緊急性スコア**: 8/10
- 競合優位性確保のため即座のAI導入が必要
- 規制対応遅延によるペナルティリスク
- 顧客体験向上の競争圧力

#### 課題共通率

**課題共通率**: 92%（500+企業中460+企業が同様の課題を報告）

**共通課題の内訳**:
- データプライバシー懸念: 95%
- コンプライアンス要件: 90%
- カスタマイズニーズ: 88%
- 主権性（US依存回避）: 85%（カナダ・EU企業）

#### 支払い意思（WTP）

**確認方法**:
- Fortune 500企業向けパイロット
- SLAベース価格戦略
- Enterprise契約の段階的展開

**結果**:
- 企業は専用AI基盤に月額$50K-500K以上の支払い意思あり（OpenAI APIの10-100倍）
- Fine-tuning & Customization Servicesへの追加支出: 年間$500K-5M
- Sovereign AI Solutions（カナダ政府$240M補助獲得）

#### 課題発見の教訓（ForStartup適用）

1. **学界ネットワークの活用**:
   - Google Brain研究者ネットワークでFortune 500企業への早期アクセス
   - 学術的権威（Transformer論文共著）が信頼獲得に直結
   - **ForStartup適用**: 大学研究室、学会コネクションでアーリーアダプター獲得

2. **複数セクター同時検証**:
   - 金融、医療、製造、公共セクターで同じ課題が再現
   - 1セクターのみでは課題の普遍性を証明できない
   - **ForStartup適用**: 複数業界での初期検証でTAM拡大可能性を確認

3. **規制要件からの逆算**:
   - HIPAA、GDPR、SOC 2等の規制要件を先に理解
   - 規制が「Unavoidable」を保証する
   - **ForStartup適用**: 規制産業は課題の緊急性が高く、検証が容易

4. **競合の弱点を特定**:
   - OpenAI: 消費者向け、API限定、データプライバシー制限
   - Google Vertex AI: クラウド限定、ベストプラクティス不明確
   - **ForStartup適用**: 既存ソリューションの「できないこと」が10倍優位性の源泉

5. **政府・戦略投資家の活用**:
   - Canadian Sovereign AI Compute Strategy $240M補助獲得
   - PSP Investments（カナダ年金基金）がSeries D lead investor
   - **ForStartup適用**: 地政学的ニーズ（US依存回避）を活用した資金調達

#### 定量データ

| 指標 | 数値 | 出典 |
|------|------|------|
| インタビュー数 | 500+ | Fortune 500企業パイロット |
| 課題共通率 | 92% | 複数セクター検証 |
| 緊急性スコア | 8/10 | 年間機会損失$100M以上 |
| WTP（月額） | $50K-500K | Enterprise SaaS契約 |
| 総資金調達額 | $1.5B+ | Series A-D2 |
| 最新評価額 | $6.8B | 2025年8月 |
| 政府補助 | $240M | Canadian Sovereign AI Compute Strategy |

---

### Tier 4B: 開発環境構築の課題発見（Replit - 2025-09）

**Replit（Amjad Masad）: Series C 2025-09, $3B valuation**

出典: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/08_Emerging/EMERGING_009_replit.md`

#### 課題発見プロセス

**着想源**:
- Amjad MasadがFacebook、Codecademyで開発者体験を向上させる仕事を経験
- 既存開発環境の3大課題を発見:
  - **時間コスト**: ローカル環境構築に数時間〜数日かかる
  - **依存関係管理**: パッケージ依存関係が複雑で初心者には困難
  - **コラボレーション困難**: Git push/pullでは即時共同編集ができない

**インタビュー手法の詳細**:
- **インタビュー数**: 推定30回（初期ユーザーインタビュー、教育機関ヒアリング）
- **手法**:
  - CVPR会議でのブースツーブースデモ（開発者直接対話）
  - 教育機関向けパイロット（学生、教師の声を収集）
  - オンライン学習プラットフォーム（Codecademy等）でのユーザーテスト
  - 2250万開発者の利用データ分析（2023年時点）
- **対象**: 学生、教師、個人開発者、企業開発者
- **質問内容**:
  - 開発環境構築にかかる時間は？
  - 最も困難なステップは？
  - 既存ツール（VS Code、Git）の不満点
  - リアルタイムコラボレーションのニーズ
  - AIコーディング支援への期待

#### 3U検証の実例

**Unworkable（現状では解決不可能）**:
- ローカル環境構築は必須、数時間〜数日かかる
- 依存関係管理の複雑さ（node_modules、virtualenv等）
- Git push/pullではリアルタイムコラボレーション不可
- 初心者には技術的障壁が高すぎる

**Unavoidable（避けられない）**:
- 開発者は毎日コーディング（100%の開発者が該当）
- 教育機関ではプログラミング教育が必修化
- 企業開発者は生産性向上が急務

**Urgent（緊急性が高い）**:
- **緊急性スコア**: 9/10
- 開発者不足による時間単価上昇（年間数千万円の機会損失）
- 教育機関は即座に実習環境が必要（授業時間は限られている）
- AIコーディング市場の急成長（GitHub Copilot、ChatGPT登場後）

#### 課題共通率

**課題共通率**: 90%（2250万開発者中2000万以上が同様の課題を経験）

**共通課題の内訳**:
- 環境構築の時間コスト: 95%
- 依存関係管理の困難: 85%
- コラボレーション不便: 80%
- デプロイの複雑さ: 90%

#### 支払い意思（WTP）

**確認方法**:
- 有料プラン（Ghostwriter: $20/月）
- 使用量ベース課金（Replit Agent）
- Teams Plan（エンタープライズ向け）

**結果**:
- 2024年初: ARR $10M
- 2025年: ARR $150M（15倍成長、5.5ヶ月）
- Ghostwriter加入率: 推定10-15%（2250万ユーザーのうち）

#### 課題発見の教訓（ForStartup適用）

1. **製品主導成長（PLG）の活用**:
   - 無料プランで2250万開発者獲得
   - 学生が社会人になり有料ユーザー転換
   - **ForStartup適用**: 教育機関、学生向け無料プランでユーザー基盤構築

2. **バイラル成長の設計**:
   - 作成したアプリをワンクリックでデプロイ・共有
   - 他ユーザーがプロジェクトを発見
   - **ForStartup適用**: 成果物の共有機能で自然な口コミ拡散

3. **AIピボットのタイミング**:
   - 9年間苦闘（2016-2024年）→ AI革命で爆発的成長
   - ChatGPT登場（2022年11月）→ Ghostwriter発表（2023年）
   - **ForStartup適用**: 市場タイミングが全て、忍耐強く製品改善を継続

4. **10倍優位性の複数軸確保**:
   - 環境構築時間: 100倍（数時間 → 0秒）
   - AIコーディング支援: 50倍
   - コラボレーション: 10倍
   - **ForStartup適用**: 単一軸の10倍ではなく、複数軸での圧倒的優位性

5. **コミュニティ投資家戦略**:
   - Wefunder crowdfunding: 2500人参加
   - ユーザーが投資家にもなる
   - **ForStartup適用**: クラウドファンディングでコミュニティとの結びつき強化

#### 定量データ

| 指標 | 数値 | 出典 |
|------|------|------|
| インタビュー数 | 30回（推定） | 初期ユーザーインタビュー、教育機関ヒアリング |
| 課題共通率 | 90% | 2250万開発者の利用データ分析 |
| 緊急性スコア | 9/10 | 開発者不足、教育機関の即時ニーズ |
| ユーザー数 | 2250万開発者 | 2023年時点 |
| ARR成長率 | 15倍（5.5ヶ月） | $10M → $150M（2024-2025年） |
| 総資金調達額 | $350M+ | Seed-Series C |
| 最新評価額 | $3B | 2025年9月 |
| 環境構築時間削減 | 100倍 | 数時間〜数日 → 0秒 |

---

## Tier 4統合: 2025年課題発見トレンド分析

### 共通パターン

1. **規制・技術変化からの課題発見**:
   - Cohere: 企業AI導入の規制障壁（HIPAA、GDPR、SOC 2）
   - Replit: AI革命による開発者生産性向上ニーズ

2. **500+インタビューの徹底検証**:
   - Cohere: 500+ Fortune 500企業検証
   - Replit: 2250万開発者の利用データ分析

3. **複数軸での10倍優位性**:
   - Cohere: Data Privacy 15x、Fine-tuning Cost 15x、Sovereign AI 100x
   - Replit: 環境構築時間 100x、AIコーディング 50x、コラボレーション 10x

4. **政府・戦略投資家の活用**:
   - Cohere: カナダ政府$240M補助
   - Replit: Y Combinator、A16Z、Khosla Venturesの戦略支援

### ForStartup特化適用ポイント

| 教訓 | Cohere事例 | Replit事例 | ForStartup適用 |
|------|----------|----------|--------------|
| 学界ネットワーク活用 | Google Brain研究者脈 | CVPR会議デモ | 大学研究室、学会コネクション活用 |
| 複数セクター同時検証 | 金融・医療・製造・公共 | 教育・個人・企業開発者 | 複数業界で初期検証してTAM拡大 |
| 規制要件からの逆算 | HIPAA、GDPR準拠 | 教育機関プライバシー | 規制産業は課題の緊急性が高い |
| 製品主導成長（PLG） | Fortune 500パイロット | 無料プラン2250万ユーザー | 教育機関、学生向け無料プラン |
| AIピボット成功 | Transformer論文応用 | Ghostwriter → Replit Agent | 市場タイミングを逃さず即座にピボット |

### 課題検証基準（2025年最新）

| 指標 | Origin基準 | ForStartup基準（従来） | 2025年最新基準（Tier 4） | 根拠 |
|------|----------|-------------------|------------------|------|
| インタビュー数 | 20人以上 | 10人以上 | **30-500人以上** | Cohere 500+、Replit推定30回 |
| 課題共通率 | 70%以上 | 60%以上 | **90%以上** | Cohere 92%、Replit 90% |
| 緊急性スコア | 7/10以上 | 6/10以上 | **8-9/10** | Cohere 8/10、Replit 9/10 |
| 10倍優位性軸数 | 1軸以上 | 2軸以上 | **3軸以上** | Cohere 5軸（15x, 15x, 100x, 8x, 10x）、Replit 3軸（100x, 50x, 10x） |

### 推奨アクション（2025年版）

**従来のForStartup基準（緩和版）を満たす場合**:
- インタビュー数: 10人以上 → `/simulate-interview` で追加検証
- 課題共通率: 60%以上 → アーリーアダプター導入を検討

**2025年Tier 4基準（厳格版）を目指す場合**:
- インタビュー数: 30-500人 → 複数セクター同時検証、学界ネットワーク活用
- 課題共通率: 90%以上 → 規制要件からの逆算、既存ソリューションの弱点特定
- 緊急性スコア: 8-9/10 → 競合優位性の機会損失を定量化（年間$100M以上）
- 10倍優位性: 3軸以上 → 複数軸での圧倒的優位性（Data Privacy + Cost + Control等）

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
9. **ForStartup適合性評価（追加）**
10. 成果物出力

### 5軸スコアリング基準（50点満点）

| 項目 | 10点 | 6-9点 | 3-5点 | 0-2点 |
|------|------|-------|-------|-------|
| **頻度** | 同様の声10件以上 | 5-9件 | 2-4件 | 1件以下 |
| **深刻度** | 「困り果てている」「限界」 | 「困っている」 | 「できれば解決したい」 | 「別にいい」 |
| **既存策不満** | 「使い物にならない」多数 | 不満の声多い | 一部不満あり | 概ね満足 |
| **支払い匂い** | 「お金払ってでも」発言あり | 時間・労力コスト言及 | コスト意識なし | 無料希望明確 |
| **緊急性** | 「今すぐ」「早く」多数 | 「近いうちに」 | 「いつか」 | 急がない |

### 判定基準（ForStartup調整版）

**総合判定**:
- 35-50点: ✅ 強い裏付け → CPF検証へ進む
- **25-34点**: ⚠️ 中程度の裏付け → **アーリーアダプター導入を検討**（ForStartup推奨）
- **20-24点**: ⚠️ 弱い裏付け → ニッチ化または追加検証
- 0-19点: ❌ 裏付け不足 → 課題仮説見直し

**起業の科学CPF基準との対応**:
- スコア35点以上 → CPF検証の補強材料として有効
- スコア25-34点 → **アーリーアダプター導入で低リスク検証**（ForStartup推奨）
- スコア20-24点 → 追加インタビューで深堀り、またはニッチ化検討
- スコア19点以下 → 課題仮説の根本見直し、`/discover-demand`で別課題を探索

**次ステップへの連携（ForStartup調整版）**:
| スコア | 次のアクション |
|:------:|---------------|
| 35点以上 | `/validate-cpf` で総合判定へ（Series A Stage進出） |
| 20-24点 | `/simulate-interview` で追加検証 |
| 19点以下 | `/discover-demand` で別課題を探索 |

### ForStartup適合性評価（追加ステップ）

課題について、以下を評価:

| 評価項目 | 評価基準 | 配点 |
|---------|---------|------|
| **アーリーアダプター導入可能性** | 自社/グループで先行運用可能か（Geppo事例） | 7点満点 |
| **既存顧客基盤活用** | 既存顧客（ホットペッパー、じゃらん、SUUMO、リクナビ等）の課題と重なるか | 5点満点 |
| **社内ネットワーク活用** | 社内インタビュー・ヒアリングで低コスト検証可能か | 3点満点 |
| **クロスセル機会** | 既存製品とのエコシステム統合が可能か | 3点満点 |
| **ブランド信頼性活用** | 確立されたブランドで顧客の信頼獲得が容易か | 2点満点 |

**ForStartup適合性スコア**: 20点満点
- 15点以上: ✅ アーリーアダプター導入推奨、既存資産活用の好機
- 10-14点: ⚠️ 一部資産活用可能、外部検証と併用
- 9点以下: ❌ 資産活用困難、Origin基準で再評価

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **WebSearch失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/customer_interview.md
- @startup_science/01_stages/cpf/persona_creation.md
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/skill_chains.md
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md
- **/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/cpf_patterns/**
- **/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/** /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/

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
User: /research-problem-for-startup

Skill:
# 課題リサーチ 自律実行開始（ForStartup Edition）

[persona.md読み込み]
ペルソナ: 中小飲食店経営者
課題: 予約管理の非効率性（電話・紙台帳）

[自動実行中...]
- STEP 1: リーンキャンバス・ペルソナ読み込み ✅
- STEP 2: 検索クエリ生成 ✅ (日本語10個、英語10個)
- STEP 3: 日本語圏生ログ収集 ✅ (35件)
- STEP 4: 英語圏生ログ収集 ✅ (42件)
- STEP 5: 5軸スコアリング ✅
- STEP 6: 定性インサイト抽出 ✅
- STEP 7: 既存代替案分析 ✅
- STEP 8: 課題裏付け判定 ✅
- STEP 9: ForStartup適合性評価 ✅
- STEP 10: 成果物出力 ✅

## 完了

成果物: problem_research.md
課題スコア: 38/50点（✅ 強い裏付け）
ForStartup適合性: 17/20点（✅ アーリーアダプター導入推奨）

既存資産活用:
- グルメサイト掲載店舗8万店へのヒアリング可能
- 営業網2,000名で現場課題収集可能
- レストランボード成功事例（類似課題）参照

アーリーアダプター導入オプション:
- 確立されたブランド社内の会議室予約システムで先行検証可能
- 1,200名規模での実運用データ取得（Geppo事例参照）
- 推奨期間: 1-2年以内にPMF判断

推奨: `/validate-cpf` で総合判定へ
Seed調達ステージ: Series A Stage進出可能
```

---

**テンプレートバージョン**: v3.1-ForStartup
**最終更新**: 2026-01-02
**作成者**: Claude Code
**ForStartup特化要素**: 10件の成功事例統合、アーリーアダプター導入オプション追加、適合性評価基準追加、Seed調達連携
