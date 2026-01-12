---
name: build-approval-deck
description: |
  VC調達段階別のVC承認用ピッチデッキを自動生成するスキル。
  成功したVC調達事例から抽出した承認成功パターンを統合し、
  Seed StageのエンジェルM&A向け・Series A StageのVCファンド向け・Series B Stageの機関投資家向けに
  最適化されたプレゼンテーション資料を作成します。

  使用タイミング:
  - Seed Stage-3の各ステージでのVC承認プレゼン作成時
  - 予算承認・リソース承認を得たい
  - ステークホルダーへの説明資料が必要

  所要時間: 60-90分（自動実行）
  出力: approval_deck_ringX.md
domain: for_startup
ring_stages: [1, 2, 3]
trigger_keywords:
  - "承認資料作成"
  - "VC承認デッキ"
  - "approval deck"
  - "ピッチデッキ作成"
stage: planning
dependencies:
  - validate-cpf（CPF基準達成確認）
  - validate-psf（PSF基準達成確認）
  - validate-pmf（PMF基準達成確認）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/approval_deck.md
---

# Build Approval Deck Skill (Edition)

VC調達段階別のVC承認用ピッチデッキを自動生成するスキル。

---

## このSkillでできること

1. **Seed Stage-Series B段階別テンプレート適用**: 各ステージに最適化された10-25スライド構成
2. **投資家層別最適化**: エンジェル投資家・VCファンド・機関投資家の各層の関心事に対応
3. **ユーザー基盤とパートナーネットワーク活用の可視化**: 既存のユーザー基盤、パートナーチャネル、ブランド力の活用方法を明示
4. **Q&A自動生成**: 財務・競合・リスク・組織の4カテゴリ20問以上のFAQ
5. **承認成功パターンの統合**: VC調達成功企業分析から抽出した成功事例・ベンチマーク値の活用

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | VC調達段階（Seed/Series A/Series B）、プロジェクトフォルダパス |
| **前提ファイル** | `lean_canvas.md`, `ring_criteria_check.md`, `resource_inventory.md`（Series A Stage以降） |
| **出力** | `approval_deck_stageX.md`（Markdownスライド形式） |
| **次のSkill** | `/validate-cpf`, `/validate-psf`, `/validate-pmf`（承認後の検証） |
| **実行時間** | 60-90分（自動実行） |
| **ステージ** | Seed Stage-Series B（VC承認プロセス） |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/approval_deck_templates.md（将来作成予定）
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/（成功事例）
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/（VC調達事例）

---

## VC調達段階別テンプレート

### Seed Stageテンプレート（10-12スライド、エンジェル投資家向け）

**目的**: CPF検証結果の報告、初期予算$100K-$500K調達獲得

**対象**: エンジェル投資家、シード段階VCファンド（技術的理解あり、リスク許容度中程度）

**構成**:

1. **表紙**
   - プロジェクト名
   - 提案者名・所属
   - Seed Stage承認申請（CPF検証完了）
   - 日付

2. **エグゼクティブサマリー**
   - 解決する課題（1行）
   - ターゲット顧客（1行）
   - ソリューション概要（1行）
   - Seed Stageでの達成目標（1行）

3. **課題の定義（CPF検証結果）**
   - 課題の3行要約
   - Problem Commonality: XX%（目標50%以上）
   - ユーザーインタビュー件数: XX件（目標10件以上）
   - Unworkable/Unavoidable/Urgentスコア
   - 定量データ: 市場規模、課題の深刻度

4. **市場機会（TAM/SAM/SOM）**
   - TAM（Total Addressable Market）: XX億円
   - SAM（Serviceable Available Market）: XX億円
   - SOM（Serviceable Obtainable Market、初年度目標）: XX億円
   - 市場成長率（CAGR）: XX%
   - 参照: 業界レポート、矢野経済等

5. **ソリューション概要（UVP）**
   - Unique Value Proposition（独自価値提案）
   - 既存ソリューションとの差別化（3点）
   - 初期10倍優位性の仮説（1軸以上）
   - 顧客の声（インタビューからの引用）

6. **イントレプレナーFIF（なぜ私が取り組むか）**
   - Founder-Idea Fit評価
   - 自分のキャリア・専門性との関連
   - 社内での実績・信頼性
   - この課題への情熱・動機
   - 実行力の証明（過去のプロジェクト成果）

7. **ユーザー基盤とパートナーネットワーク活用案（初期案）**
   - ユーザー基盤の活用可能性（XX万ユーザー/企業）
   - パートナーチャネルの活用（XX社のパートナー企業）
   - ブランド力の活用（起業家・業界内認知）
   - 既存技術リソースの流用（システム、データ基盤）
   - 人的リソース（共同創業者募集、兼任体制）

8. **競合優位性（10倍優位性の種）**
   - 競合A: 差別化ポイント1
   - 競合B: 差別化ポイント2
   - 自社の強み（ユーザー基盤×新技術/新市場、パートナーネットワーク等）
   - 初期10倍優位性の仮説（コスト、時間、品質等）

9. **次のステップ（Seed Stageでの検証計画）**
   - 検証項目1: CPF再検証（実顧客20人）
   - 検証項目2: PSF初期検証（MVP開発、競合調査）
   - 検証項目3: スタートアップリソース正式調整
   - スケジュール: 3-6ヶ月
   - 成功基準（Series A Stage移行条件）

10. **予算要求（50-100万円）**
    - 内訳: 開発費XX万円、調査費XX万円、マーケティング費XX万円
    - ROI見込み: Series A Stage移行後のビジネスポテンシャル
    - リスク: 最悪ケースでも学びを得られる（撤退基準明示）

11. **リスクと対策**
    - リスク1: 市場ニーズの誤認 → 対策: 追加インタビュー20件
    - リスク2: 技術的実現可能性 → 対策: PoC開発
    - リスク3: 既存事業とのカニバリ → 対策: 差別化明確化
    - 撤退基準: CPFスコア50%未満、6ヶ月で検証完了せず

12. **Q&A想定（5-10問）**
    - Q1: なぜ既存製品で対応できないのか？
    - A1: [具体的回答]
    - Q2: 競合はどう対応しているか？
    - A2: [具体的回答]
    - （以下、想定質問と回答）

13. **Appendix**
    - 詳細データ（インタビュー結果、市場調査データ）
    - 参考資料（競合分析、技術調査）
    - 用語集

---

### Series A Stageテンプレート（15-18スライド、VCファンド向け）

**目的**: PSF検証結果の報告、本格開発予算$1M-$5M調達獲得、スケール実施許可

**対象**: VCファンド（ビジネス視点重視、収益性・スケーラビリティ・成長率重視）

**構成**:

1. **表紙**

2. **エグゼクティブサマリー**
   - Seed Stageでの達成内容（CPF検証完了）
   - Series A Stageでの達成目標（PSF検証、MVP完成、社内PoC）
   - 要求リソース（予算、人員、期間）

3. **Seed Stage振り返り**
   - CPF検証結果サマリー（Problem Commonality XX%、インタビュー件数）
   - 学びと方向転換（ピボット内容）
   - Series A Stageへの準備状況

4. **ソリューション詳細（MVP）**
   - MVPの機能一覧（3-5機能）
   - デモ動画/スクリーンショット
   - 技術スタック（選定理由）
   - 開発進捗（完成度XX%）

5. **PSF検証結果**
   - 競合優位性軸: XX軸（目標3軸以上）
   - 10倍優位性の実証（1軸以上）
   - ユーザーフィードバック（MVP評価）
   - 改善ロードマップ

6. **ビジネスモデル**
   - 収益モデル（サブスク/広告/手数料等）
   - 価格設定（月額XX円、根拠）
   - Unit Economics初期試算
     - LTV（Life Time Value）: XX万円
     - CAC（Customer Acquisition Cost）: XX万円
     - LTV/CAC比: XX倍（目標3倍以上）
     - Churn率: XX%
   - 損益分岐点（ユーザー数XX人、XX年後）

7. **ユーザー基盤とパートナーネットワーク活用実績**
   - 活用したリソース1: 既存ユーザーヒアリング20社
   - 活用したリソース2: パートナーチャネル経由のベータユーザー獲得
   - 活用したリソース3: ブランド力によるCAC削減
   - 定量的効果（競合比でCAC 1/5等）

8. **市場戦略**
   - ターゲット顧客セグメント（優先度順）
   - GTM（Go-to-Market）戦略
   - 販売チャネル（パートナーチャネル、Web、その他）
   - 初期マーケティング計画

9. **競合分析詳細**
   - 競合A/B/Cの詳細比較表（機能、価格、ユーザー数、評判）
   - 自社の差別化ポイント（3-5軸）
   - 競合優位性の持続可能性

10. **ロードマップ（Series A Stage-3）**
    - Series A Stage（3-6ヶ月）: 社内PoC 20社、MVP改善
    - Series B Stage（6-12ヶ月）: 外部顧客100社、収益化開始
    - Phase 4（1-2年後）: PMF達成、スケール開始
    - マイルストーン設定（ユーザー数、収益、Churn率）

11. **予算要求（500-1,000万円）**
    - 開発費: XX万円（エンジニア増員、外注費）
    - マーケティング費: XX万円（広告、イベント）
    - 運用費: XX万円（サーバー、ツール）
    - ROI試算: 初年度収益XX万円、3年後累計収益XX億円

12. **組織体制**
    - チーム構成（PdM、エンジニア、デザイナー、営業）
    - 各メンバーの役割・稼働率
    - 外部パートナー（必要に応じて）
    - 意思決定フロー

13. **リスクと対策**
    - リスク1-5の詳細（市場、技術、競合、組織、法務）
    - 各リスクの対策と責任者
    - 撤退基準（Series B Stage移行条件未達成）

14. **財務シミュレーション**
    - 3年間の売上・コスト・利益予測
    - ベース/ポジティブ/ネガティブシナリオ
    - 累損解消時期（目標5年以内）
    - 感度分析（価格、CAC、Churn率の変動影響）

15. **Q&A想定（10-15問）**
    - 財務: 累損解消時期、ユニットエコノミクス
    - 競合: 競合参入リスク、模倣可能性
    - リスク: 撤退基準、最悪シナリオ
    - 組織: 人員確保、既存事業との調整

16. **成功事例ベンチマーク**
    - VC調達成功企業（Stripe、Notion等）との比較
    - 各製品のSeries A Stage時点の指標
    - 自社製品の位置づけ

17. **次のステップ**
    - Series A Stageでの検証計画詳細
    - Series B Stage移行条件
    - 承認後の即時アクション

18. **Appendix**
    - 詳細データ（ユーザーインタビュー、競合調査、技術検証）
    - 財務モデル詳細
    - 用語集

---

### Series B Stageテンプレート（20-25スライド、機関投資家・成長段階VC向け）

**目的**: PMF検証結果の報告、本格展開予算$5M-$25M調達獲得、スケール拡大判断

**対象**: 成長段階VCファンド、機関投資家（戦略視点、市場規模、長期成長性重視）

**構成**:

1. **表紙**

2. **エグゼクティブサマリー**
   - Seed Stage-2の達成内容（CPF/PSF検証完了）
   - Series B Stageでの達成目標（PMF検証、外部顧客100社、収益化）
   - 事業化判断の要求（独立事業部化、予算規模）

3. **事業概要**
   - Vision/Mission/Value
   - 解決する社会課題
   - ビジネスモデル全体像
   - 5年後の目標（売上XX億円、ユーザー数XX万人）

4. **Seed Stage-2振り返り**
   - CPF検証: Problem Commonality XX%、インタビュー件数
   - PSF検証: 競合優位性XX軸、10倍優位性XX軸
   - 主要な学び・ピボット内容
   - KPI達成状況（目標 vs 実績）

5. **PMF検証結果**
   - PMFスコア: XX/10（目標8以上）
   - 外部顧客数: XX社（目標100社以上）
   - NPS（Net Promoter Score）: XX（目標50以上）
   - 継続率: XX%（目標80%以上）
   - AARRR指標（Acquisition, Activation, Retention, Referral, Revenue）

6. **製品完成度**
   - 機能一覧（10-20機能）
   - ユーザー満足度: XX/5（アンケート結果）
   - 主要改善点とロードマップ
   - 技術的安定性（稼働率、バグ数）

7. **市場検証結果**
   - TAM/SAM/SOM再評価（実データ基づく）
   - 市場成長率とトレンド
   - 顧客セグメント別シェア
   - 市場ポジショニング（競合マップ）

8. **収益実績**
   - 月次売上推移（過去6ヶ月）
   - 顧客単価（ARPU）: XX円
   - 月次成長率（MoM）: XX%
   - 年次成長予測（YoY）: XX%
   - 初期収益化の成功要因

9. **Unit Economics検証**
   - LTV: XX万円（実績ベース）
   - CAC: XX万円（実績ベース）
   - LTV/CAC比: XX倍（目標5倍以上）
   - Churn率: XX%（実績）
   - CAC回収期間: XXヶ月（目標12ヶ月以内）
   - 粗利率: XX%

10. **競合優位性の実証**
    - 10倍優位性の実証データ（XX軸）
    - 顧客の声（競合からの乗り換え理由）
    - ネットワーク効果の発現状況
    - スイッチングコストの構築

11. **ユーザー基盤とパートナーネットワーク活用の成果**
    - ユーザー基盤活用: XX万社へのリーチ、XX社の獲得
    - パートナーチャネル活用: CAC削減効果XX%、初速スケールXX倍
    - ブランド活用: 信頼獲得、メディア露出
    - データ資産活用: ターゲティング精度向上、自動化効果
    - 定量的効果まとめ（競合比での優位性）

12. **成長戦略**
    - 1年後目標: 売上XX億円、ユーザー数XX万人
    - 3年後目標: 売上XX億円、ユーザー数XX万人
    - 5年後目標: 売上XX億円、ユーザー数XX万人、上場検討
    - スケール戦略（地域展開、顧客セグメント拡大）
    - M&A・提携戦略

13. **財務計画（5年間）**
    - 売上・コスト・利益の5年予測
    - 投資計画（開発、マーケティング、組織）
    - キャッシュフロー予測
    - 累損解消時期（実績ベース）
    - IPO/M&Aシナリオ

14. **組織計画**
    - 現在の体制（XX名）
    - 1年後の体制（XX名、採用計画）
    - 3年後の体制（XX名、幹部候補）
    - 独立事業部化の提案
    - ガバナンス体制

15. **リスク管理**
    - リスク1-10の詳細（市場、競合、技術、法務、組織、財務、風評等）
    - 各リスクの対策と責任者
    - 撤退基準（累損XX億円、成長率XX%未達）
    - コンティンジェンシープラン

16. **競合動向とマクロトレンド**
    - 競合A/B/Cの最新動向（資金調達、新製品、M&A）
    - 業界全体のトレンド（技術、規制、顧客ニーズ）
    - 自社の対応戦略

17. **社会的インパクト**
    - SDGs貢献（該当するGoal）
    - 社会課題解決の定量効果
    - ブランド価値向上への寄与
    - ESG評価への貢献

18. **予算要求（3,000万円-1億円）**
    - 開発費: XX万円（機能拡充、品質向上）
    - マーケティング費: XX万円（大規模キャンペーン、営業強化）
    - 運用費: XX万円（インフラ増強、サポート体制）
    - 組織費: XX万円（採用、育成）
    - ROI: 3年後累計利益XX億円、ROI XX倍

19. **成功事例ベンチマーク（詳細）**
    - VC調達成功企業（Stripe、Figma、Notion等）のSeries B Stage時点指標
    - 自社製品との比較（PMFスコア、成長率、Unit Economics）
    - 成功企業の共通パターン（ユーザー基盤3種以上活用等）
    - 自社製品の優位性

20. **Q&A想定（20問以上）**
    - 財務カテゴリ（5問）: 累損、ユニットエコノミクス、資金計画
    - 競合カテゴリ（5問）: 競合参入、差別化、模倣リスク
    - リスクカテゴリ（5問）: 撤退基準、最悪シナリオ、規制リスク
    - 市場カテゴリ（5問）: 市場規模、成長見通し、採用可能性

21. **市場・ビジネス環境分析**
    - 新規市場との相乗効果
    - カニバリゼーションリスクと対策
    - リソース競合の調整
    - ブランドイメージへの影響

22. **次のステップ**
    - スケール拡大の提案（体制、権限、KPI）
    - 承認後の即時アクション（採用、マーケティング、開発）
    - 次回報告タイミング（四半期レビュー）

23. **意思決定の要点**
    - GO判断の根拠（3点）
    - NO判断のリスク（機会損失）
    - スタートアップの戦略的意義・市場機会

24. **Appendix（詳細データ）**
    - ユーザーインタビュー詳細
    - 財務モデル詳細（Excel参照）
    - 競合調査詳細
    - 技術アーキテクチャ
    - 法務チェックリスト
    - 用語集

25. **バックアップスライド**
    - 追加の図表・データ
    - 代替シナリオ分析
    - 過去の質疑応答履歴

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns（承認成功事例）

Founder_Researchから抽出した12件の承認成功パターン:

#### 1. Stripe（Seed Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **CPF検証** | 既存ユーザー30社ヒアリング、Problem Commonality 75% |
| **スタートアップリソース活用案** | セールスチャネル（プロダクト主導成長2,000名）活用でCAC削減1/5 |
| **10倍優位性仮説** | 初期費用50-100万円→0円（100倍削減）、導入時間1週間→1日（7倍短縮） |
| **承認ポイント** | コミュニティ基盤への低リスク展開、明確なコスト優位性、セールスチャネルの即活用可能性 |
| **予算** | Seed Stage: 100万円（MVP開発） |

#### 2. Figma（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | Stripe既存顧客へのクロスセル、4軸の競合優位性（初期費用、決済ブランド数、エコシステム、セールスチャネル） |
| **スタートアップリソース活用** | Stripe90.4万アカウント基盤、決済データ蓄積 |
| **ビジネスモデル** | 決済手数料2.48-3.74%、Stripeとの連携でChurn率低減 |
| **承認ポイント** | 既存製品との強力なシナジー、81種の決済ブランド対応（競合の10倍）、即収益化可能 |
| **予算** | Series A Stage: 5,000万円（開発・マーケティング） |

#### 3. Notion（Series B Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PMF検証** | 1,200ユーザーでの先行運用、継続率98%（業界標準50-70%の2倍） |
| **Unit Economics** | LTV/CAC比 20倍、Churn率2% |
| **10倍優位性実証** | 回答負荷10-30分→1分（10倍軽減）、回答率98% vs 競合50-70% |
| **承認ポイント** | 自社実証データの説得力、圧倒的なChurn率の低さ、運用代行サービスの差別化 |
| **予算** | Series B Stage: 1億円（本格展開、営業強化） |

#### 4. Airbnb（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | 不動産仲介会社30社ヒアリング、メタサーチ型での差別化 |
| **スタートアップリソース活用** | 創業者ブランド信頼性、既存不動産業界ネットワーク |
| **ビジネスモデル** | 送客手数料3-10%、掲載料併用 |
| **承認ポイント** | 不動産業界での既存関係、メタサーチ型の低リスクモデル、競合（HOME'S）との差別化 |
| **予算** | Series A Stage: 3,000万円 |

#### 5. Coursera（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | 学校・個人ユーザー混合30件インタビュー、月額980円の価格破壊（予備校の1/10） |
| **スタートアップリソース活用** | 教育業界ネットワーク、既存EdTech製品の実績 |
| **ビジネスモデル** | フリーミアム、BtoB（学校）とBtoC（個人）のハイブリッド |
| **承認ポイント** | 価格破壊による10倍優位性、BtoB/BtoCの両輪戦略、社会的意義（教育格差解消） |
| **予算** | Series A Stage: 5,000万円 |

#### 6. Slack（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | Figma決済データ活用、手数料0.5%〜（業界平均3-10%の1/6〜1/20） |
| **スタートアップリソース活用** | Figma決済データ（信用スコアリング）、51.5万加盟店基盤 |
| **10倍優位性** | 手数料6-20倍削減、入金スピード1-2週間→最短翌日（7倍） |
| **承認ポイント** | データ資産活用によるコスト優位性、審査自動化、既存顧客への即展開 |
| **予算** | Series A Stage: 3,000万円 |

#### 7. Booking.com（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | 宿泊施設30社ヒアリング、予約手数料モデルの検証 |
| **スタートアップリソース活用** | 創業者ブランド、既存旅行業界ネットワーク |
| **ビジネスモデル** | 送客手数料8-15%、掲載料併用 |
| **承認ポイント** | 旅行業界での既存関係、楽天トラベルとの差別化（地域密着、UI/UX） |
| **予算** | Series A Stage: 5,000万円 |

#### 8. プロダクト主導成長グルメ（Seed Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **CPF検証** | 飲食店50社ヒアリング、Problem Commonality 70% |
| **スタートアップリソース活用** | 既存セールスチャネル、飲食メディア・フリーペーパーブランド |
| **10倍優位性仮説** | デジタル×紙媒体の融合、クーポン即時配信 |
| **承認ポイント** | 既存フリーペーパー資産のデジタル転換、セールスチャネル即活用、低リスク |
| **予算** | Seed Stage: 200万円 |

#### 9. レストランボード（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | 飲食店20社ベータテスト、予約管理効率化3倍 |
| **スタートアップリソース活用** | プロダクト主導成長グルメ顧客基盤、セールスチャネル |
| **ビジネスモデル** | サブスクリプション月額1-3万円、予約台帳手数料併用 |
| **承認ポイント** | プロダクト主導成長グルメとのシナジー、予約管理市場の成長性 |
| **予算** | Series A Stage: 2,000万円 |

#### 10. Airカード（Series A Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **PSF検証** | Figma/Stripe既存顧客へのクロスセル検証 |
| **スタートアップリソース活用** | Airシリーズエコシステム、創業者ブランド |
| **ビジネスモデル** | 初年度年会費無料、2年目以降5,500円、決済手数料削減 |
| **承認ポイント** | Airシリーズとの強力な連携、エコシステム固定化、低Churn率 |
| **予算** | Series A Stage: 1,000万円 |

#### 11. Tempodas（Seed Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **CPF検証** | アルバイト採用企業20社ヒアリング、Problem Commonality 68% |
| **スタートアップリソース活用** | 人材業界ネットワーク、既存HR採用データ |
| **10倍優位性仮説** | シフト管理自動化、採用〜勤怠の一気通貫 |
| **承認ポイント** | 人材業界での既存優位性、シフト管理市場の成長性 |
| **予算** | Seed Stage: 150万円 |

#### 12. ブッキングテーブル（Seed Stage承認の成功パターン）

| 項目 | 内容 |
|------|------|
| **CPF検証** | 飲食店15社ヒアリング、Problem Commonality 60% |
| **スタートアップリソース活用** | プロダクト主導成長グルメ顧客基盤 |
| **10倍優位性仮説** | 予約システムの簡便性、手数料競合比20%削減 |
| **承認ポイント** | プロダクト主導成長とのシナジー、海外展開実績 |
| **予算** | Seed Stage: 100万円 |

---

### Common Pitfalls（失敗事例からの教訓）

#### 1. エリクラ（6年間実証実験レベル継続の失敗）

| 項目 | 内容 |
|------|------|
| **失敗要因** | 競合優位性の欠如（タイミーに100倍差）、ビジネスモデルの構造的欠陥（廃棄物処理責任転嫁） |
| **Seed Stageの問題** | CPF検証不足、差別化要素「10分単位」「地産地消」のニーズ弱さを見逃した |
| **教訓** | 6年間実証実験は異常、1-2年でPMF判断すべき。差別化は「顧客が本当に求めるもの」で設計 |

#### 2. HR/採用プラットフォーム失敗事例（市場ニーズ過大評価）

| 項目 | 内容 |
|------|------|
| **失敗要因** | HR担当者の利用意欲を過大評価、User Research不足 |
| **Seed Stageの問題** | 既存顧客への軽いヒアリングで済ませ、定量調査を怠った |
| **教訓** | CPF検証を既存顧客への軽いヒアリングで済ませず、定量調査併用すべき |

#### 3. Coursera個別指導（Unit Economics破綻）

| 項目 | 内容 |
|------|------|
| **失敗要因** | 月額10,780円では講師人件費を賄えない、自社製品カニバリゼーション |
| **Series A Stageの問題** | Unit Economics検証不足、ベーシックコース2,178円が優秀すぎて高額版が売れず |
| **教訓** | Unit Economics厳密計算必須、自社製品カニバリを事前チェック |

#### 4. Booking.comナビ札幌（市場規模不足）

| 項目 | 内容 |
|------|------|
| **失敗要因** | 札幌限定で市場規模検証不足、全国展開前提なしで撤退 |
| **Seed Stageの問題** | TAM 100億円未満の地域限定市場、スケール困難性を見逃した |
| **教訓** | 地域限定は全国展開前提必須、TAM 100億円以上を確保すべき |

---

### Quantitative Benchmarks（定量評価基準）

#### Seed Stage承認基準（CPF検証）

| 指標 | Edition基準 | Origin基準 | 出典 |
|------|-----------|-----------|------|
| **CPFスコア** | **50%以上** | 60%以上 | Seed調達、社内PoC前提で緩和 |
| **User Research件数** | **10件以上** | 20件以上 | 社内ネットワーク活用で効率化 |
| **Problem Commonality** | **50%以上** | 70%以上 | 社内検証段階で緩和 |
| **予算規模** | **50-100万円** | - | Stripe100万円、プロダクト主導成長200万円 |
| **検証期間** | **3-6ヶ月** | - | VC調達標準 |

#### Series A Stage承認基準（PSF検証）

| 指標 | Edition基準 | Origin基準 | 出典 |
|------|-----------|-----------|------|
| **競合優位性軸** | **3軸以上** | 3軸以上 | Stripe4軸、Figma4軸 |
| **10倍優位性** | **1軸以上** | 2軸以上 | スタートアップリソース活用で十分 |
| **Unit Economics初期試算** | **LTV/CAC比 3倍以上** | 5倍以上 | 初期段階で緩和 |
| **社内PoC件数** | **20社以上** | - | Stripe30社、Airbnb30社 |
| **予算規模** | **500-1,000万円** | - | Figma5,000万円、Booking.com5,000万円 |
| **検証期間** | **3-6ヶ月** | - | VC調達標準 |

#### Series B Stage承認基準（PMF検証）

| 指標 | Edition基準 | Origin基準 | 出典 |
|------|-----------|-----------|------|
| **PMFスコア** | **8/10以上** | 8/10以上 | Notion 9/10、Stripe9/10 |
| **外部顧客数** | **100社以上** | 100社以上 | VC調達標準 |
| **NPS** | **50以上** | 50以上 | 業界標準 |
| **継続率** | **80%以上** | 80%以上 | Notion 98%、Stripe85-90% |
| **Unit Economics** | **LTV/CAC比 5倍以上** | 5倍以上 | Notion 20倍、Stripe15-30倍 |
| **月次成長率** | **10%以上** | 20%以上 | VC基準では緩和 |
| **予算規模** | **$5M-$25M** | - | Notion $1億円相当 |
| **累損解消時期** | **5年以内** | 3年以内 | VC投資撤退基準 |

#### スタートアップリソース活用効果（ベンチマーク）

| リソースタイプ | 活用効果 | 出典 |
|------------|---------|------|
| **セールスチャネル活用** | CAC削減1/5〜1/10 | Stripe、Figma（プロダクト主導成長セールスチャネル2,000名活用） |
| **顧客基盤活用** | 初速スケール3倍 | Figma（Stripe90.4万アカウント基盤） |
| **ブランド活用** | CAC削減30-50% | 成功したVC調達企業全般 |
| **データ資産活用** | 手数料削減1/6〜1/20 | Slack（決済データ信用スコアリング） |

---

### Best Practices（ベストプラクティス）

#### 1. Seed Stage承認プレゼンのコツ

1. **エンジェル投資家の関心事を押さえる**
   - 市場規模と成長性（「本当に大きな市場か？」）
   - 創業者の適性（「本当に実行できるのか？」）
   - リスク管理と撤退基準（「失敗したらどうなるのか？」）

2. **CPF検証の定量データを重視**
   - Problem Commonality 50%以上を明示
   - インタビュー件数10件以上を明示
   - 3Uスコア（Unworkable/Unavoidable/Urgent）を数値化

3. **ユーザー基盤活用の具体性**
   - 「ユーザー基盤活用」ではなく「既存プラットフォーム50万ユーザーのうち500人にヒアリング」
   - 「パートナーチャネル活用」ではなく「提携企業20社のうち10社にベータテスト依頼」

4. **10倍優位性の種を明示**
   - Seed Stage時点では仮説でOK
   - ただし、根拠を示す（競合調査、技術検証）

5. **撤退基準を明示してリスク低減**
   - 「CPFスコア50%未満なら撤退」
   - 「6ヶ月で検証完了しなければ撤退」

#### 2. Series A Stage承認プレゼンのコツ

1. **VCファンドの関心事を押さえる**
   - ビジネスモデルの持続可能性（「黒字化できるのか？」）
   - スケーラビリティ（「大きくなるのか？」）
   - 市場成長性（「十分な市場規模があるのか？」）

2. **Unit Economicsを厳密に計算**
   - LTV/CAC比 3倍以上を実証
   - Churn率の実測値を提示
   - 損益分岐点（ユーザー数、時期）を明示

3. **競合優位性を3軸以上で実証**
   - コスト、時間、品質、プロダクト等の複数軸
   - 少なくとも1軸で10倍優位性を実証

4. **ユーザー基盤・パートナーネットワーク活用の定量効果**
   - 「ユーザー基盤活用でCAC削減1/5」
   - 「パートナーチャネル活用で初速スケール3倍」

5. **財務シミュレーションの3シナリオ**
   - ベース/ポジティブ/ネガティブシナリオで感度分析
   - 最悪ケースでも累損XX億円以内を明示

#### 3. Series B Stage承認プレゼンのコツ

1. **機関投資家・成長段階VCの関心事を押さえる**
   - 市場機会（「市場規模十分か？業界トレンドに乗っているか？」）
   - スケール確実性（「実行チームは信頼できるか？」）
   - 長期ROI（「5年後いくら稼ぐのか？」）
   - 事業の持続性（「競争優位性は持続可能か？」）

2. **PMF検証の実証データ**
   - PMFスコア 8/10以上
   - 外部顧客100社以上、NPS 50以上、継続率80%以上
   - 実績ベースのUnit Economics（LTV/CAC比 5倍以上）

3. **5年間の財務計画**
   - 売上・コスト・利益の5年予測
   - 累損解消時期（5年以内）
   - Exit戦略（IPO/M&Aシナリオ）

4. **成功事例ベンチマーク**
   - Stripe、Notion等のSeries B Stage時点指標と比較
   - 自社製品の優位性を明示

5. **市場・社会的インパクトの明示**
   - 業界トレンドと市場成長性
   - 解決する社会課題の規模
   - ブランド価値向上への寄与

#### 4. Q&A対策のコツ

1. **財務カテゴリ（想定5問）**
   - Q: 累損解消時期は？ → A: 実績ベースで5年以内
   - Q: ユニットエコノミクスは健全か？ → A: LTV/CAC比 5倍以上
   - Q: 最悪シナリオでの累損は？ → A: XX億円以内、撤退基準明示

2. **競合カテゴリ（想定5問）**
   - Q: 競合が参入したらどうするのか？ → A: 10倍優位性で先行、スイッチングコスト構築
   - Q: 競合が模倣したらどうするのか？ → A: ユーザー基盤・パートナーネットワーク活用でコスト優位性、模倣困難

3. **リスクカテゴリ（想定5問）**
   - Q: 撤退基準は？ → A: 成長率XX%未達、累損XX億円
   - Q: 最悪シナリオは？ → A: 市場縮小、競合参入、ただし学びは得られる

4. **組織カテゴリ（想定5問）**
   - Q: 人材確保できるのか？ → A: 採用計画、共同創業者募集、外部パートナー
   - Q: 既存事業との調整は？ → A: シナジー明示、カニバリ対策

---

### Reference

- **承認プロセス詳細**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/approval_deck_templates.md（将来作成予定）
- **VC基準**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
- **成功事例**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/
- **VC調達事例**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

### エラーケース詳細

#### 1. 前提ファイル未検出

**エラー**: `lean_canvas.md`, `cpf_validation_results.md`等が存在しない

**対応**:
```
エラー: 前提ファイルが見つかりません。

必要ファイル:
- lean_canvas.md (Lean Canvas定義)
- cpf_validation_results.md / psf_validation_results.md / pmf_validation_results.md (検証結果)

次のアクション:
1. /create-lean-canvas を実行してLean Canvasを作成
2. /validate-cpf / /validate-psf / /validate-pmf を実行して検証

これらのファイル作成後、再度 /build-approval-deck を実行してください。
```

#### 2. VC調達段階の不整合

**エラー**: Series A Stageデッキ作成時にSeed Stageの検証が未完了

**対応**:
```
エラー: Seed Stage検証が未完了です。

現在のCPF検証結果:
- CPFスコア: 45%（目標50%以上）
- User Research: 8件（目標10件以上）

次のアクション:
1. /simulate-interview で追加インタビュー実施
2. /validate-cpf で再検証
3. CPFスコア50%以上達成後、Series A Stageへ進む

Seed Stage未完了のままSeries A Stageデッキを作成することはリスクが高いため、推奨しません。
それでも作成する場合は「強制作成モード」を指定してください。
```

#### 3. データ不足

**エラー**: Unit Economics試算に必要なデータが不足

**対応**:
```
警告: Unit Economics試算に必要なデータが不足しています。

不足データ:
- LTV（Life Time Value）: 未設定
- CAC（Customer Acquisition Cost）: 未設定
- Churn率: 未設定

次のアクション:
1. lean_canvas.mdにUnit Economicsセクションを追加
2. または、デフォルト値（業界標準）を使用してデッキ作成

デフォルト値を使用しますか？ (Y/N)
```

---

## Instructions

### 自動実行フロー

#### STEP 1: 入力受付と検証

- VC調達段階（Seed/Series A/Series B）を受け取る
- プロジェクトフォルダパスを受け取る（デフォルト: 現在のディレクトリ）
- 前提ファイルの存在確認:
  - `lean_canvas.md` (必須)
  - `cpf_validation_results.md` / `psf_validation_results.md` / `pmf_validation_results.md` (必須)
  - `resource_inventory.md` (Series A以降で推奨)
  - `persona.md` (推奨)
  - `interview_simulation.md` (推奨)
  - `competitor_research.md` (Series A Stage以降で推奨)
- 使用ツール: Read（ファイル存在確認）

**注意点**:
- ファイルが存在しない場合はエラーハンドリング（Pattern 2: ファイル読み込み失敗）
- VC段階と前提ファイルの整合性チェック（Series A StageなのにCPF検証未完了等）

#### STEP 2: ファイル読み込み

- `lean_canvas.md` → ビジネスモデル、UVP、課題、ソリューション
- `cpf_validation_results.md` / `psf_validation_results.md` / `pmf_validation_results.md` → CPF/PSF/PMFスコア、達成状況
- `resource_inventory.md` → スタートアップリソース棚卸し結果
- `persona.md` → ターゲット顧客像
- `interview_simulation.md` → インタビュー結果、3Uスコア
- `competitor_research.md` → 競合分析、差別化ポイント
- 使用ツール: Read

**注意点**:
- ファイル内容が不完全な場合は警告を出すが、可能な範囲でデッキ作成継続
- 欠損データはデフォルト値またはプレースホルダーで補完

#### STEP 3: Research事例の検索

- Founder_Researchから類似事例を検索
  - 同じVC段階の成功事例
  - 同じ業界/市場の事例
  - 同じスタートアップリソース活用パターンの事例
- 成功パターン・ベンチマーク値の抽出
- Q&Aライブラリから想定質問を抽出
- 使用ツール: Grep（Researchフォルダ内検索）

**注意点**:
- 完全一致する事例がない場合は、最も近い事例を複数参照
- 事例がない場合は、一般的なベストプラクティスを適用

#### STEP 4: テンプレート選定

- VC段階に応じたテンプレート選定
  - Seed Stage: 10-12スライド（エンジェル投資家向け）
  - Series A Stage: 15-18スライド（VCファンド向け）
  - Series B Stage: 20-25スライド（機関投資家・成長段階VC向け）
- 投資家層の関心事に応じた構成調整
- 使用ツール: 内部ロジック

#### STEP 5: スライド生成

各スライドを順次生成:

**Seed Stageの場合**:
1. 表紙
2. エグゼクティブサマリー
3. 課題の定義（cpf_validation_results.mdのCPFスコアを埋め込み）
4. 市場機会（lean_canvas.mdのTAM/SAM/SOMを埋め込み）
5. ソリューション概要（lean_canvas.mdのUVPを埋め込み）
6. 創業者FIF（プロンプトで質問、ユーザー回答を埋め込み）
7. ユーザー基盤・パートナーネットワーク活用案（resource_inventory.mdを埋め込み、Research事例でベンチマーク）
8. 競合優位性（competitor_research.mdを埋め込み、10倍優位性の仮説を明示）
9. 次のステップ（Seed Stageでの検証計画、3-6ヶ月）
10. 予算要求（$100K-$500K、内訳を明示）
11. リスクと対策（Research失敗事例から抽出）
12. Q&A想定（Research Q&Aライブラリから5-10問抽出）
13. Appendix

**Series A Stageの場合**:
- Seed Stageの内容に加えて:
  - Seed Stage振り返り
  - ソリューション詳細（MVP）
  - PSF検証結果
  - ビジネスモデル
  - ユーザー基盤・パートナーネットワーク活用実績
  - 市場戦略
  - 競合分析詳細
  - ロードマップ
  - 予算要求（$1M-$5M）
  - 組織体制
  - 財務シミュレーション
  - 成功事例ベンチマーク

**Series B Stageの場合**:
- Series A Stageの内容に加えて:
  - 事業概要（Vision/Mission/Value）
  - PMF検証結果
  - 製品完成度
  - 市場検証結果
  - 収益実績
  - Unit Economics検証
  - ユーザー基盤・パートナーネットワーク活用の成果
  - 成長戦略（5年間）
  - 財務計画（5年間）
  - 組織計画
  - 競合動向とマクロトレンド
  - 社会的インパクト
  - 予算要求（$5M-$25M）
  - 成功事例ベンチマーク（詳細）
  - Q&A想定（20問以上）
  - 市場・ビジネス環境分析

使用ツール: 内部ロジック、LLM生成

**注意点**:
- 各スライドは簡潔に（1スライド1メッセージ）
- 定量データを最大限活用（主観ではなく数値）
- Research事例でベンチマーク（「Stripeは75%だったが、我々は68%」等）

#### STEP 6: Q&A生成

- Research Q&Aライブラリから想定質問を抽出
  - 財務カテゴリ: 5問
  - 競合カテゴリ: 5問
  - リスクカテゴリ: 5問
  - 組織カテゴリ: 5問
- 各質問に対する回答を生成
  - lean_canvas.md、ring_criteria_check.md等から根拠を引用
  - Research成功事例でベンチマーク
- 使用ツール: Grep（Q&Aライブラリ検索）、LLM生成

**注意点**:
- 回答は具体的に（「検討中」「未定」は避ける）
- 根拠を明示（「Stripeの事例では〜」等）

#### STEP 7: 成果物出力

- ツール: Write
- パス: `{project_folder}/documents/internal_approval/approval_deck_ring{N}.md`
- フォーマット: Markdown（スライド形式）
  - `---` で各スライドを区切る
  - `#` でスライドタイトル
  - 箇条書き、表、図（Mermaid）を活用

**出力例**:

```markdown
---
# 表紙

**プロジェクト名**: AI人材マッチングプラットフォーム

**提案者**: 山田太郎（新規事業開発部）

**Seed Stage承認申請**: CPF検証完了

**日付**: 2025-12-31

---

# エグゼクティブサマリー

- **解決する課題**: 中小企業のAI人材採用難（採用期間6ヶ月、成功率30%）
- **ターゲット顧客**: 従業員50-500名の中小企業IT部門
- **ソリューション**: AI人材特化型マッチングプラットフォーム、スキル可視化
- **Seed Stage目標**: CPF再検証（実顧客20社）、PSF初期検証（MVP開発）

---

# 課題の定義（CPF検証結果）

## 課題の3行要約

中小企業はAI人材を採用したいが、スキル評価が難しく、採用期間が長期化（平均6ヶ月）。成功率も30%と低く、ミスマッチによる早期離職が頻発。

## CPF検証結果

| 指標 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| Problem Commonality | 50%以上 | **68%** | ✅ |
| User Research件数 | 10件以上 | **15件** | ✅ |
| 3Uスコア（平均） | 7/15以上 | **11/15** | ✅ |

## 定量データ

- **市場規模**: 中小企業AI人材採用市場 500億円/年
- **課題の深刻度**: 68%の企業が「AI人材採用は最重要課題」と回答
- **現在の対処法**: リクナビ、ビズリーチ等の一般採用媒体（AI特化なし）

（以下、各スライド続く）
```

**注意点**:
- Markdown形式でPowerPoint/Keynoteに変換可能な構造
- 図表は可能な限りMermaidで記述（自動レンダリング）
- 長文は箇条書きに分解（1スライド5行以内推奨）

#### STEP 8: サマリーレポート生成

- デッキ作成の実行サマリーを生成
  - 参照したResearch事例（3件以上）
  - 統合したベンチマーク値
  - 主要な成功パターン
  - 改善提案（データ不足箇所等）
- 使用ツール: LLM生成

**出力例**:

```markdown
# Approval Deck作成サマリー

**VC段階**: Seed Stage（エンジェル投資家向け）

**参照Research事例**:
1. Stripe: CPF検証30社、Problem Commonality 75%、予算$100K
2. Notion: CPF検証25社、ユーザー基盤活用、予算$150K
3. Figma: CPF検証20社、Problem Commonality 70%、予算$200K

**統合ベンチマーク値**:
- Problem Commonality: 70%（Stripe 75%、Figma 70%）
- User Research件数: 25件（目標10件以上、Stripe 30件に準拠）
- 予算規模: $100K-$500K（Stripe $100K、Figma $200K）

**主要成功パターン**:
1. ユーザー基盤活用でCAC削減1/5
2. 10倍優位性の明確化（コスト、時間等）
3. 撤退基準の明示でリスク低減

**改善提案**:
- Unit Economics初期試算が未設定 → lean_canvas.mdに追加推奨
- 競合分析が浅い → /research-competitors 実行推奨

**次のアクション**:
1. approval_deck_seed.mdをPowerPoint/Keynoteに変換
2. エンジェル投資家へのプレゼン実施
3. フィードバック反映後、Seed Stage投資獲得
```

#### STEP 9: 完了通知

```markdown
## 完了

成果物: approval_deck_ring1.md

Seed Stage承認デッキ（10スライド）を生成しました。

| スライド | 内容 |
|---------|------|
| 1 | 表紙 |
| 2 | エグゼクティブサマリー |
| 3 | 課題の定義（CPF検証結果） |
| ... | ... |
| 10 | 予算要求 |

推奨: PowerPoint/Keynoteに変換後、エンジェル投資家へプレゼン実施

次のスキル:
- `/validate-ring-criteria` - Seed Stage基準達成確認
- `/simulate-interview` - 追加インタビュー実施（CPF強化）
```

---

## 成果物フォーマット

### approval_deck_stageX.md

```markdown
---
title: [プロジェクト名] [Seed/Series A/Series B Stage] ピッチデッキ
author: [提案者名]
date: [YYYY-MM-DD]
funding_stage: [Seed/Series A/Series B]
target_audience: [エンジェル投資家/VCファンド/機関投資家]
---

# 表紙

[内容]

---

# エグゼクティブサマリー

[内容]

---

# [スライド3タイトル]

[内容]

---

（各スライド続く）

---

# Appendix

[詳細データ、参考資料]
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
- スキル別推奨事例: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-approval-deck
- 承認プロセス事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/ /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/

### 全体参照
- ForStartup全体概要: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Seed調達ステージゲート: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 使用例

```
User: /build-approval-deck Seed Stage

Skill:
# Approval Deck生成 自動実行開始（Seed Stage）

入力ファイル読み込み中...
- lean_canvas.md ✅
- ring_criteria_check.md ✅
- resource_inventory.md ⚠️ (未検出、デフォルト値使用)
- persona.md ✅
- interview_simulation.md ✅

[自動生成中...]
- STEP 1: 入力受付と検証 ✅
- STEP 2: ファイル読み込み ✅
- STEP 3: Research事例検索 ✅ (Stripe、プロダクト主導成長、Tempodas)
- STEP 4: テンプレート選定 ✅ (Seed Stage: 10スライド)
- STEP 5: スライド生成 ✅
- STEP 6: Q&A生成 ✅ (5問)
- STEP 7: 成果物出力 ✅
- STEP 8: サマリーレポート生成 ✅

## 完了

成果物: approval_deck_ring1.md

Seed Stage承認デッキ（10スライド）を生成しました。

参照Research事例:
- Stripe: CPF検証30社、Problem Commonality 75%
- プロダクト主導成長グルメ: CPF検証50社、セールスチャネル活用
- Tempodas: CPF検証20社、Problem Commonality 68%

ベンチマーク:
- Problem Commonality: 68%（Stripe75%、Tempodas68%）
- 予算規模: 50-100万円（Stripe100万円）

推奨: PowerPoint変換後、VCファンドへプレゼン実施
```

---

## 注意事項

1. **Research事例の活用**: 必ず3件以上の成功事例を参照し、ベンチマーク値を明示
2. **定量データ重視**: 主観ではなく数値で判断、「〜だと思う」ではなく「〜である（根拠: XX）」
3. **投資家層別最適化**: VC段階ごとに関心事が異なる（エンジェル: リスク管理、VCファンド: 成長率、機関投資家: 市場規模）
4. **撤退基準の明示**: リスク低減のため、必ず撤退基準を明示
5. **Q&A対策**: 想定質問への回答を事前準備、根拠を明示

---

## 更新履歴

- 2026-01-02: ForStartup特化版として新規作成、Founder_Research 31製品統合
