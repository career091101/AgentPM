# Startup Science Knowledge Base

全概念・フレームワークへのパスリスト。Skillsからの参照用。

## Base Path

```
BASE = aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
```

---

## 01_stages/ - ステージ別概念

### CPF (Customer Problem Fit)

- `01_stages/cpf/cpf_overview.md` - CPF概念
- `01_stages/cpf/persona_creation.md` - ペルソナ作成
- `01_stages/cpf/3u_validation.md` - 3U検証
- `01_stages/cpf/customer_interview.md` - 顧客インタビュー

### PSF (Problem Solution Fit)

- `01_stages/psf/psf_overview.md` - PSF概念
- `01_stages/psf/10x_validation.md` - 10倍検証
- `01_stages/psf/mvp_types.md` - MVP10類型
- `01_stages/psf/uvp_canvas.md` - UVPキャンバス

### PMF (Product Market Fit)

- `01_stages/pmf/pmf_overview.md` - PMF概念

---

## 02_frameworks/ - フレームワーク集

### リーンスタートアップ

- `02_frameworks/lean_canvas/lean_canvas_overview.md` - リーンキャンバス

### 戦略分析

- `02_frameworks/five_eyes/five_eyes_overview.md` - 5つの眼
- `02_frameworks/mvv/mvv_overview.md` - MVV（Mission Vision Values）
- `02_frameworks/balance_scorecard/scorecard_overview.md` - バランススコアカード

### 成長指標

- `02_frameworks/aarrr/aarrr_overview.md` - AARRR（Pirate Metrics）
- `02_frameworks/dear_model/dear_overview.md` - DEARモデル（CS）

---

## 03_tactics/ - 戦術・手法

### 創業者検証

- `03_tactics/founder_issue_fit/fif_overview.md` - Founder-Issue-Fit

### 成長戦略

- `03_tactics/flywheel/flywheel_design.md` - フライホイール設計

### 方向転換

- `03_tactics/pivot/pivot_types.md` - ピボット10類型

### 測定・分析

- `03_tactics/nps/nps_measurement.md` - NPS測定
- `03_tactics/retention/retention_analysis.md` - リテンション分析
- `03_tactics/unit_economics/unit_eco_overview.md` - ユニットエコノミクス

---

## 99_reference/ - 参考資料

- `99_reference/sns_content_strategy.md` - SNSコンテンツ戦略（Build in Public）

---

## _index/ - インデックス

- `_index/master_index.md` - マスターインデックス（予定）
- `_index/taxonomy.yaml` - 統制語彙定義
- `_index/cross_reference.md` - クロスリファレンス（予定）

---

## _templates/ - テンプレート

- `_templates/concept_template.md` - 概念テンプレート
- `_templates/framework_template.md` - フレームワークテンプレート
- `_templates/checklist_template.md` - チェックリストテンプレート

---

## Claude Code Autonomous Skills

自律実行型Skillsへのパスリスト。`.claude/skills/`に格納。

**スキルチェーン定義**: `.claude/skills/_shared/skill_chains.md`

### Stage 1: Idea検証

| Skill | 説明 | 出力 |
|-------|------|------|
| `/discover-demand` | 需要発見リサーチ（4軸20点） | demand_discovery.md |
| `/create-mvv` | MVV早期定義 | mvv.md |
| `/build-flywheel` | フライホイール設計 | flywheel_design.md |

### Stage 2: CPF検証

| Skill | 説明 | 出力 |
|-------|------|------|
| `/create-persona` | ペルソナ作成（8要素） | persona.md |
| `/simulate-interview` | 仮想インタビュー（3U検証） | interview_simulation.md |
| `/research-problem` | 課題裏付け収集（5軸50点） | problem_research.md |
| `/validate-cpf` | CPF判定（4指標） | cpf_judgment.md |

### Stage 3: PSF検証

| Skill | 説明 | 出力 |
|-------|------|------|
| `/research-competitors` | 競合調査（5軸比較） | competitor_research.md |
| `/validate-10x` | 10倍優位性検証 | 10x_validation.md |
| `/build-lp` | LP構築（HTML/CSS/JS） | lp_files/ |
| `/validate-unit-economics` | Unit Economics検証（LTV/CAC試算） | unit_economics.md |
| `/validate-psf` | PSF判定（3指標+Unit Economics） | psf_judgment.md |

### Pivot支援（Tier 0新規）

| Skill | 説明 | 出力 |
|-------|------|------|
| `/pivot-decision` | CPF/PSF停止時の自動Pivot判定（10類型） | pivot_decision.md |

### その他

| Skill | 説明 | 出力 |
|-------|------|------|
| `/create-sns-content` | SNSコンテンツ作成 | sns_content.md |
| `/startup-scorecard` | スタートアップ・スコアカード | startup_scorecard.md |
| `/orchestrate-phase1` | Phase1自律オーケストレーター | - |

---

## Case Studies (別ディレクトリ)

```
BASE_CASES = aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/
```

85件のソロプレナー成功事例:

- `case_studies/005_brock_anderson.md` - Brock Anderson
- `case_studies/006_max_artemov.md` - Max Artemov
- `case_studies/007_jack_friks.md` - Jack Friks
- `case_studies/008_alex_nguyen.md` - Alex Nguyen
- ...（全85件）

詳細は `/reference-cases` Skillで参照可能。

---

## 使い方

### Skillsでの参照方法

```markdown
## Knowledge Base参照

@aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/cpf/cpf_overview.md
@aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/03_tactics/pivot/pivot_types.md
```

### Readツール使用例

```python
# CPF概念を読み込む
Read("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/cpf/cpf_overview.md")

# ピボット10類型を読み込む
Read("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/03_tactics/pivot/pivot_types.md")
```

---

## 概念マップ（Tier 0自動化版）

```
┌─────────────────────────────────────────────────────────────┐
│                    IDEA検証ステージ                         │
│  /discover-demand → /create-mvv → /build-flywheel           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    CPF検証ステージ                          │
│  /create-persona → /simulate-interview → /research-problem  │
│                         → /validate-cpf                      │
│                              │                               │
│                              ├─ ✅ CPF ≥ 60% → PSF検証へ    │
│                              └─ ❌ CPF < 60%                 │
│                                   ↓ 自動起動                │
│                            /pivot-decision                   │
│                       （Pivot 10類型から最適案選定）         │
│                                   ↓                          │
│                            推奨Pivot実行                     │
│                       （最大3回リトライ）                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    PSF検証ステージ                          │
│  /research-competitors → /validate-10x → /build-lp          │
│                         → /validate-unit-economics           │
│                              （LTV/CAC試算）                 │
│                                   ↓                          │
│                         → /validate-psf                      │
│                              │                               │
│                              ├─ ✅ LTV/CAC ≥ 3.0 → PMF検証へ│
│                              └─ ❌ LTV/CAC < 1.0             │
│                                   ↓ 自動起動                │
│                            /pivot-decision                   │
│                    （Business Architecture Pivot推奨）       │
└─────────────────────────────────────────────────────────────┘
                            ↓
                         PMF検証
```

**詳細**: `.claude/skills/_shared/skill_chains.md` 参照

**自動Pivot判断基準**（Tier 0完了後、2025-12-28以降）:

| ステージゲート | 停止条件 | 自動アクション |
|--------------|---------|---------------|
| **CPF** | CPFスコア < 60% | `/pivot-decision` 自動起動 → Top 3代替案提示 → 推奨案⭐⭐⭐実行 |
| **PSF** | 10倍0軸 / LTV/CAC < 1.0 | `/pivot-decision` 自動起動 → Pivot 10類型から最適選定 |

**Pivot 5シグナル** - 該当3つ以上で即Pivot実行:
1. 顧客が存在しない（インタビュー < 10人）
2. 課題が深刻でない（緊急性 < 5/10）
3. Solutionが10倍でない（10倍0軸）
4. Unit Economics不成立（LTV/CAC < 1.0）
5. 成長が停滞（3ヶ月横ばい）

**Framework参照**:
- `startup_science/03_tactics/pivot/pivot_types.md` - Pivot 10類型詳細
- `startup_science/03_tactics/unit_economics/unit_eco_overview.md` - LTV/CAC計算
- `.claude/skills/pivot-decision/SKILL.md` - 自動判定仕様
- `.claude/skills/validate-unit-economics/SKILL.md` - Unit Economics検証仕様

---

## ForRecruit Edition - 企業内新規事業特化版

リクルート社内新規事業に特化したスキルセット。Ring制度、社内承認プロセス、既存資産活用を中心とした評価基準の緩和版。

### ForRecruit Base Path

```
RECRUIT_BASE = aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/
RECRUIT_RESEARCH = RECRUIT_BASE + Recruit_Product_Research/
```

### ForRecruit Skills Location

```
SKILLS_BASE = aipm_v0/.claude/skills/for_recruit/
```

### ForRecruit Autonomous Skills（18スキル）

#### Stage 1: Discovery & Planning（5スキル）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-discover-demand` | 需要発見（4軸20点） | TAM 50億円緩和、既存顧客基盤活用 | demand_discovery.md |
| `/for-recruit-research-problem` | 課題検証（5軸50点） | インタビュー10人緩和、社内先行導入オプション | problem_research.md |
| `/for-recruit-inventory-internal-resources` | 社内リソース棚卸し（6カテゴリ） | ROI定量化、Airペイ ROI 11,450%事例 | internal_resources.md |
| `/for-recruit-create-mvv` | MVV企業整合性 | リクルート6つの価値観チェック | mvv.md |
| `/for-recruit-build-flywheel` | フライホイール設計 | Airシリーズエコシステム連携 | flywheel_design.md |

#### Stage 2: CPF Validation（3スキル + Gate 1）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-simulate-interview` | 仮想インタビュー（4U検証） | 社内ネットワーク活用、10-15人 | interview_simulation.md |
| `/for-recruit-validate-cpf` | CPF判定 | CPFスコア50%緩和、社内先行導入前提 | cpf_judgment.md |
| `/for-recruit-build-approval-deck` | 社内承認ピッチデッキ | Ring 1-3段階別テンプレート | approval_deck_ringX.pptx |

**Ring 1 Gate**: CPF 50%以上、課長承認（予算50-100万円）

#### Stage 3: PSF Validation（4スキル + Gate 2）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-research-competitors` | 競合調査 | 外部競合+既存事業、カニバリ回避 | competitor_research.md |
| `/for-recruit-validate-10x` | 10倍優位性検証 | 1軸緩和、社内リソース活用軸追加 | 10x_validation.md |
| `/for-recruit-validate-psf` | PSF判定 | LTV/CAC 3.0緩和、社内PoC前提 | psf_judgment.md |

**Ring 2 Gate**: 10倍優位性1軸以上、部長・事業部長承認（予算500-1,000万円）

#### Stage 4: PMF Validation（2スキル + Gate 3）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-validate-pmf` | PMF判定 | 外部顧客100社/人、3年黒字計画 | pmf_judgment.md |
| `/for-recruit-startup-scorecard` | スタートアップスコアカード | Ring制度評価項目80点満点化 | startup_scorecard.md |

**Ring 3 Gate**: 外部顧客100社以上、役員承認（予算5,000万円-3億円）

#### Stage 5: Growth Optimization（3スキル）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-analyze-aarrr` | AARRR分析 | 社内外顧客統合評価、Ring 3基準準拠 | aarrr_analysis.md |
| `/for-recruit-build-lp` | LP構築 | 2段階CTA（社内+外部）、社内実績活用 | lp_files/ |
| `/for-recruit-design-pricing` | 価格設定 | 基本無料モデル、クロスセル戦略 | pricing_strategy.md |

#### Orchestration（1スキル）

| Skill | 説明 | ForRecruit特化内容 | 出力 |
|-------|------|----------------|------|
| `/for-recruit-orchestrate-phase1-recruit` | Phase1自律オーケストレーター | Ring 1-3段階的実行、18スキル統合 | - |

### Ring制度ステージゲート

| Ring段階 | 目的 | 検証項目 | 承認権限 | 予算規模 | 期間目安 |
|---------|------|---------|---------|---------|---------|
| **Ring 1（準備）** | CPF検証 | CPF 50%以上、課題共通率60%、社内リソース評価 | 課長 | 50-100万円 | 2-3ヶ月 |
| **Ring 2（実証）** | PSF検証 | 10倍優位性1軸、LTV/CAC 3.0、社内PoC成功 | 部長・事業部長 | 500-1,000万円 | 4-6ヶ月 |
| **Ring 3（拡大）** | PMF検証 | 外部顧客100社、3年黒字計画、収益化開始 | 役員 | 5,000万円-3億円 | 1-2年 |

### 社内承認プロセスフロー

```
Ring 1申請 → 課長承認 → CPF検証（2-3ヶ月） → Ring 1判定
     ↓ 合格
Ring 2申請 → 部長・事業部長承認 → PSF検証（4-6ヶ月） → Ring 2判定
     ↓ 合格
Ring 3申請 → 役員承認 → PMF検証（1-2年） → Ring 3判定
     ↓ 合格
事業化判断 → 本格投資
```

### 撤退基準（Yellow/Orange/Red Alert）

#### Yellow Alert（要注意）

- CPFスコア < 50%（Ring 1）
- 10倍優位性 0軸（Ring 2）
- 外部顧客獲得 < 50社（Ring 3）
- 6ヶ月成長率 < 5%

**対応**: ピボット検討、3ヶ月以内に改善計画実行

#### Orange Alert（危険）

- CPFスコア < 40%継続（Ring 1）
- LTV/CAC < 2.0（Ring 2）
- 外部顧客獲得 < 30社（Ring 3）
- 12ヶ月成長率 < 3%

**対応**: 抜本的ピボット or 撤退検討、1ヶ月以内に判断

#### Red Alert（撤退推奨）

- CPFスコア < 30%（Ring 1）
- LTV/CAC < 1.0（Ring 2）
- 外部顧客獲得 < 10社（Ring 3、18ヶ月以上経過）
- 成長停滞6ヶ月以上

**対応**: 即座に撤退判断、優秀な人材を次の事業へ

**撤退判断の原則**（リクルート実践基準）:
- 1.5-2年で撤退判断（エリクラ6年は異常）
- 「3年黒字、5年累損解消では遅すぎる」
- ギリギリ黒字レベルでも撤退（優秀な人材のリソース重視）

### ForRecruit評価基準（Origin比）

#### 市場機会評価（緩和版）

| 指標 | Origin | ForRecruit | 緩和理由 |
|------|--------|----------|---------|
| TAM | 100億円以上 | **50億円以上** | 社内リソース活用で小規模市場も参入可能 |
| 成長率 | 10%/年以上 | **5%/年以上** | 既存顧客基盤で安定成長可能 |
| 競合飽和度 | 3社以下 | **5社以下** | 既存ブランド力で差別化可能 |

#### CPF検証基準（緩和版）

| 指標 | Origin | ForRecruit | 緩和理由 |
|------|--------|----------|---------|
| CPFスコア | 60%以上 | **50%以上** | 社内PoC前提での段階的検証 |
| インタビュー数 | 20人以上 | **10人以上** | 社内ネットワーク、既存顧客基盤活用 |
| 課題共通率 | 70%以上 | **60%以上** | 社内先行導入オプションあり |
| 緊急性スコア | 7/10以上 | **6/10以上** | 社内リソース活用で解決可能 |

#### PSF検証基準（緩和版）

| 指標 | Origin | ForRecruit | 緩和理由 |
|------|--------|----------|---------|
| 10倍優位性 | 2軸以上 | **1軸以上** | 社内リソース活用軸追加で補完 |
| LTV/CAC比 | 5.0以上 | **3.0以上** | 営業網活用でCAC大幅削減可能 |
| 初期顧客獲得 | 100人以上 | **50人以上** | 社内先行導入含む |

#### PMF検証基準（厳格化）

| 指標 | Origin | ForRecruit | 厳格化理由 |
|------|--------|----------|---------|
| 外部顧客獲得 | 50-100人 | **100社/人以上** | Ring 3は外部スケール必須 |
| 収益化開始 | 推奨 | **必須** | 3年黒字計画の実現性証明 |
| 3年黒字計画 | - | **必須** | リクルート撤退基準に準拠 |

### 社内リソース活用評価（6カテゴリ20点満点）

| カテゴリ | 配点 | 評価基準 | 代表事例 |
|---------|------|---------|---------|
| **営業網活用** | 5点 | ホットペッパー営業2,000名等で販売可能か | Airレジ、Airペイ |
| **顧客基盤活用** | 5点 | 既存事業顧客（SUUMO、じゃらん等）と重なるか | Airペイ（Airレジ顧客） |
| **ブランド力活用** | 3点 | リクルートブランド信頼性が活かせるか | 全製品 |
| **データ資産活用** | 3点 | 決済データ、顧客データ等の既存資産活用 | Airキャッシュ |
| **プラットフォーム連携** | 2点 | Airシリーズ等との連携でLTV向上 | Airシリーズ |
| **インフラ活用** | 2点 | 決済基盤、クラウド基盤等の活用 | リクルートID |

**成功率との相関**:
- 15点以上（3種以上活用）: PMF 8.8、成功率100%
- 10-14点（1-2種活用）: PMF 7.5、成功率80%
- 9点以下（資産活用不足）: PMF 5.2、成功率25%

### Recruit_Product_Research参照

企業内新規事業86件（成功16件、失敗15件、進行中55件）の詳細分析。

#### 統合分析レポート

- `@Recruit_Product_Research/analysis/integrated_analysis_report.md` - 31製品統合分析（2,000行）

#### 成功製品詳細（SUCCESS）

主要製品:
- `@Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md` - Airレジ（30,000行超）
- `@Recruit_Product_Research/documents/SUCCESS/CORP_S001_airペイ.md` - Airペイ（800行）
- `@Recruit_Product_Research/documents/SUCCESS/CORP_M001_geppo.md` - Geppo（840行）

#### 撤退製品詳細（WITHDRAWN）

主要製品:
- `@Recruit_Product_Research/documents/WITHDRAWN/CORP_F003_エリクラ.md` - エリクラ6年撤退事例
- `@Recruit_Product_Research/documents/WITHDRAWN/CORP_F002_CODE_SCORE.md` - CODE.SCORE競合優位性欠如

#### CPFパターン分析

- `@Recruit_Product_Research/cpf_patterns/` - CPF検証6パターン詳細

### ForRecruit Specific Frameworks

Ring制度、社内承認プロセス、イントレプレナーFIF評価等の詳細フレームワーク。

- `@.claude/skills/_shared/recruit_specific_frameworks.md` - 800行（2026-01-02作成予定）
- `@.claude/skills/_shared/case_reference_for_recruit.md` - 1,200行（2026-01-02作成予定）

---

### ForRecruit成功パターン詳細

#### Ring 1成功パターン（CPF検証段階）

**共通要素**:
- **User Research**: 平均35.2回（業界標準20-30回を上回る、ForRecruit基準15回の2.3倍）
- **Problem Commonality**: 平均72.9%（ForRecruit基準60%を12.9ポイント超過）
- **CPFスコア**: 平均73.6%（ForRecruit基準50%を23.6ポイント超過）
- **社内先行導入**: 5製品中5製品（100%）が既存顧客基盤または社内ネットワークを活用
- **達成期間**: 平均4.2ヶ月（3-6ヶ月レンジ、早期CPF検証でダラダラ検証を回避）

**成功製品の特徴**:
1. Geppo（CPF 80%）: 社内先行運用4年で回答率96%実証、リクルート1,200名導入で外販前検証
2. Airペイ（CPF 70%）: Airレジ既存顧客100回ヒアリング、Problem Commonality 85%
3. スタディサプリ（CPF 70%）: 教育関係者50名+保護者100名、既存顧客100万人活用
4. Airレジ（CPF 65%）: ホットペッパーグルメ加盟店30社、Problem Commonality 75%
5. SUUMO（CPF 62%）: 不動産仲介会社+ユーザー30回、ブランド統合効果検証

#### Ring 2成功パターン（PSF検証段階）

**共通要素**:
- **10倍優位性**: 平均3.0軸（ForRecruit基準1軸を2.0軸超過、少なくとも1軸で圧倒的優位性）
- **リクルート資産活用**: 平均15点以上/20点満点（3種以上活用でPMF 8.8、成功率100%）
- **エコシステム連携**: Airシリーズの相互連携（レジ→ペイ→キャッシュ→シフト）でLTV 3-5倍
- **競合の10倍模倣困難**: 営業網2,000名、既存顧客90.4万、決済データ資産は新規参入が容易に構築不可

**成功製品の特徴**:
1. Airレジ（4軸）: コスト100倍、時間7倍、営業網5倍、エコシステム3倍
2. Airペイ（4軸）: 初期費用100倍削減、対応ブランド8-16倍、手数料6-20倍、データ資産活用
3. Airキャッシュ（3軸）: 入金スピード7倍、手数料6倍、審査自動化
4. Geppo（2軸）: 回答時間10倍短縮、離職率改善2倍、継続率98% vs 競合50-70%
5. スタディサプリ（2軸）: 価格10倍削減、利用時間柔軟性3倍

#### Ring 3成功パターン（PMF達成段階）

**共通要素**:
- **外部顧客獲得**: 平均1,340社/人（ForRecruit Ring 3基準100を13.4倍超過）
- **収益化開始**: 初年度売上5億円以上または3年黒字計画
- **3年黒字達成**: リクルート基準「3年黒字、5年累損解消」の前半達成
- **高継続率・NPS**: 継続率80-98%、NPS 60-70（競合50-60）
- **PMFスコア**: 平均8.7（ForRecruit基準7.0を1.7ポイント超過）
- **LTV/CAC**: 平均21.6倍（ForRecruit基準3.0を18.6倍超過）

**成功製品の特徴**:
1. Airレジ（PMF 9.2）: 1年10万店舗、3年90.4万アカウント、3年黒字達成
2. Airペイ（PMF 9.0）: 1年20万店舗、3年51.5万店舗、クロスセル率57%、初年度売上5億円
3. Geppo（PMF 8.8）: 2年300社、継続率98%、NPS 60-70、3年黒字達成
4. スタディサプリ（PMF 8.5）: 初年度30万ユーザー、2年100万人、3年200万人
5. SUUMO（PMF 8.2）: 不動産仲介会社シェア1位、月間訪問数1,000万以上

### ForRecruit失敗パターン詳細

#### 19件撤退事例の失敗パターン分類

**パターン1: 競合優位性の欠如**（5製品）
- エリクラ: タイミーに100倍差（10万人 vs 1,000万人）、2-3倍程度の優位性は模倣容易
- termhub: クラウドサインに劣後、電子契約市場で差別化不足
- CODE.SCORE: エンジニア採用市場で競合優位性なし、リクルート資産活用3点
- 教訓: **10倍優位性1軸以上必須**、2-3倍程度は模倣容易、競合の成長スピードを常時モニタリング

**パターン2: 市場構造変化への対応遅れ**（4製品）
- エイビーロード: 旅行業界の構造変化、紙媒体からオンライン予約へシフト
- チラシ部: 紙媒体市場縮小、デジタル広告へシフト
- 教訓: **市場変化の兆候を常時モニタリング**、TAM 50%以上縮小で即座撤退

**パターン3: ビジネスモデルの構造的欠陥**（3製品）
- スタサプ個別指導: LTV/CAC 1-2倍、ベーシックコース優秀すぎて高額版売れず
- CODE.SCORE: Unit Economics不健全、LTV/CAC推定2倍
- 教訓: **LTV/CAC 3.0未満は即座ピボットまたは撤退**、ビジネスモデル再設計必須

**パターン4: CPF検証不足のまま拡大**（3製品）
- エリクラ: 6年間実証実験レベル（サイバーエージェント社内）、外部スケール失敗
- リクルートDMPフォロー: ニーズ過大評価、CPFスコア推定40%
- 教訓: **Ring 1達成期間6ヶ月以上は異常**、1-2年でPMF判断必須

**パターン5: 自社製品カニバリゼーション**（2製品）
- スタサプ個別指導: ベーシック2,178円優秀すぎて高額版10,780円売れず
- 教訓: **既存製品売上10%以上減で即座撤退**、差別化10倍規模で設計

#### 失敗の兆候・警告指標（Yellow/Orange/Red Alert発動タイミング）

**Yellow Alert発動タイミング**:
- CPFスコア < 50%が**3ヶ月継続**
- User Research Count < 15件が**2ヶ月継続**
- 10倍優位性 0軸が**Ring 2開始後2ヶ月継続**
- 月次成長率 < 10%が**3ヶ月継続**

**Orange Alert発動タイミング**:
- Ring 1達成期間 **6ヶ月以上経過**（即座にPMF判断へ移行）
- 社内先行導入 **2年以上外部スケールせず**（外部展開不可と判断）
- LTV/CAC < 3.0が**6ヶ月継続**（ビジネスモデル再設計必須）
- 競合が**100倍スケール**（市場タイミング喪失、即座撤退検討）

**Red Alert発動タイミング**:
- Ring 3失敗: 外部顧客100社/人未達、**3年経過**（PMF達成不可能）
- 自社製品カニバリ: 既存製品売上**10%以上減**（全社売上減少）
- 市場構造変化: TAM **50%以上縮小**（市場消滅）
- 撤退判断遅延: **1.5年以上赤字継続**（機会損失拡大）

#### Ring 1→2、Ring 2→3移行失敗パターン

**Ring 1→2移行失敗**:
- CPFスコア50%達成したが、社内リソース活用10点未満（リソース活用不足）
- User Research 15件達成したが、Problem Commonality 60%未満（課題の共通性不足）
- 社内先行導入成功したが、外部展開失敗（社内と外部のギャップ）

**Ring 2→3移行失敗**:
- 10倍優位性1軸達成したが、LTV/CAC 3.0未満（Unit Economics不健全）
- 社内PoC成功したが、外部顧客獲得100社/人未達（スケーラビリティ不足）
- リクルート資産活用15点達成したが、外部市場で競争力不足（資産依存過多）

### ForRecruit定量ベンチマーク拡充

#### Ring段階別達成期間（成功製品平均）

| Ring段階 | 平均達成期間 | 最短 | 最長 | 中央値 | 標準偏差 |
|---------|------------|------|------|--------|---------|
| **Ring 1（CPF）** | 4.2ヶ月 | 3ヶ月（Airレジ、Airペイ） | 6ヶ月（スタディサプリ、SUUMO） | 4ヶ月 | 1.2ヶ月 |
| **Ring 2（PSF）** | 8.2ヶ月 | 6ヶ月（Airレジ、Airペイ） | 12ヶ月（スタディサプリ） | 8ヶ月 | 2.3ヶ月 |
| **Ring 3（PMF）** | 16.2ヶ月 | 12ヶ月（Airレジ、Airペイ） | 24ヶ月（SUUMO） | 15ヶ月 | 4.8ヶ月 |

**達成期間の警告指標**:
- Ring 1: 6ヶ月以上でYellow Alert、9ヶ月以上でOrange Alert
- Ring 2: 12ヶ月以上でYellow Alert、18ヶ月以上でOrange Alert
- Ring 3: 24ヶ月以上でYellow Alert、36ヶ月以上でRed Alert

#### リソース活用数別成功率（製品数別）

| リソース活用数 | 製品数 | 成功率 | PMFスコア平均 | LTV/CAC平均 | 代表製品 |
|-------------|--------|--------|-------------|-----------|---------|
| **3種類以上** | 8製品 | **100%** | **8.8** | **25倍** | Airレジ（4種）、Airペイ（5種）、Airキャッシュ（4種）、Geppo（3種） |
| **1-2種類** | 10製品 | **83%** | **7.5** | **15倍** | スタディサプリ（2種）、レストランボード（2種）、じゃらん（2種） |
| **0種類** | 4製品 | **25%** | **5.2** | **3倍** | CODE.SCORE、termhub、リクルートDMPフォロー |

**リソース活用数とPMFスコアの相関係数**: 0.92（強い正の相関）

**教訓**: **3種類以上のリソース活用で成功率100%**、0-1種類は成功率25%

#### LTV/CAC比較（成功製品 vs 失敗製品）

| 製品カテゴリ | 平均LTV/CAC | 最高 | 最低 | 中央値 | 標準偏差 |
|------------|------------|------|------|--------|---------|
| **成功製品（16件）** | **21.6倍** | 30倍（Airレジ） | 15倍（SUUMO） | 20倍 | 5.2倍 |
| **失敗製品（15件）** | **2.3倍** | 3倍（CODE.SCORE推定） | 1倍（スタサプ個別指導） | 2倍 | 0.8倍 |

**ForRecruit基準**: LTV/CAC 3.0以上（Origin版5.0から緩和）

**警告指標**:
- LTV/CAC < 3.0: Yellow Alert
- LTV/CAC < 2.0: Orange Alert
- LTV/CAC < 1.0: Red Alert（即座撤退）

#### Cross-sell率ベンチマーク（Airシリーズ vs 業界標準）

| 製品 | Cross-sell率 | 業界標準 | 倍率 | 算出根拠 |
|------|------------|---------|------|---------|
| **Airレジ→Airペイ** | **57%** | 5-15% | **4-11倍** | Airペイ51.5万店舗 ÷ Airレジ90.4万アカウント = 57% |
| **Airペイ→Airキャッシュ** | 推定30% | 2-8% | 4-15倍 | Airキャッシュ利用推定15万店舗 ÷ Airペイ51.5万 ≈ 30% |
| **Airレジ→Airシフト** | 推定20% | 3-10% | 2-7倍 | Airシフト利用推定18万店舗 ÷ Airレジ90.4万 ≈ 20% |

**エコシステム連携効果**:
- クロスセル率57%（業界標準の4-11倍）
- LTV 3-5倍向上（単一製品 vs エコシステム）
- Churn率1/2〜1/3削減（複数製品利用でロックイン）

**教訓**: **エコシステム連携でクロスセル率4-11倍、LTV 3-5倍**

---

## Phase 2: 戦略深化フレームワーク（ForRecruit/ForStartup Edition）

### Exit Strategy設計

#### M&A Exit（リクルート社の事例）

リクルートグループは積極的なM&A戦略により、グローバル展開と事業ポートフォリオ拡大を実現。

**主要買収事例**:
- **Indeed買収**: $1.0B（2012年）→ グローバル展開で10倍成長、世界最大の求人検索エンジンへ
- **Glassdoor買収**: $1.2B（2018年）→ 求人×企業口コミのシナジー、Indeed統合で相乗効果
- **USENavi買収**: リクルートUSA統合、北米市場への本格参入

#### Exit判断基準（Ring 3到達企業向け）

| 指標 | 基準値 | 備考 |
|------|--------|------|
| **年間売上** | $10M以上 | Ring 3達成水準 |
| **外部顧客数** | 100社/人以上 | スケーラビリティ実証済み |
| **シナジー効果** | 既存事業との相乗効果3倍以上 | クロスセル、データ連携等 |
| **市場タイミング** | 市場成長期（競合激化前） | 先行者利益が残存 |

#### Exit Options詳細

**1. M&A Exit**
- **適用ケース**: グローバル展開が必要、巨額投資が必要
- **成功例**: Indeed（$1B）、Glassdoor（$1.2B）
- **タイミング**: Ring 3到達後、年間売上$10M以上
- **評価額目安**: 年間売上の5-10倍（SaaS企業基準）

**2. スピンオフ Exit**
- **適用ケース**: 独立経営が有利、事業文化の差異が大きい
- **成功例**: リクルートマーケティングパートナーズ（ゼクシィ・SUUMO）、リクルート住まいカンパニー
- **タイミング**: 年間売上$50M以上、独立採算可能
- **注意点**: 後に再統合される可能性あり（SUUMO事例）

**3. エコシステム統合**
- **適用ケース**: 既存事業とのシナジーが大きい、クロスセル効果が見込める
- **成功例**: Airシリーズ（レジ→ペイ→キャッシュ→シフト→整備）
- **タイミング**: Ring 3達成、エコシステム連携価値が明確
- **統合効果**: LTV 3-5倍向上、Churn率1/2削減

### エコシステム最適化

#### リクルートエコシステム統合パターン

**クロスセル成功事例**（20件以上）:

| 統合パターン | 事例 | クロスセル率 | 効果 |
|------------|------|------------|------|
| **SaaS×決済** | Airレジ→Airペイ | **57%** | LTV 3倍向上 |
| **決済×資金調達** | Airペイ→Airキャッシュ | 30% | 入金スピード7倍 |
| **旅行×グルメ** | じゃらん×Hot Pepper | 25% | 送客シナジー |
| **不動産×決済** | SUUMO×Airペイ | 15% | 新規市場開拓 |
| **中古車×整備** | カーセンサー×Air整備 | 20% | サービス統合 |

**データ活用シナジー**:
- **リクルートID統合**: 5,000万人の共通会員基盤、会員データの横展開
- **レコメンドエンジン共通化**: AI技術の横展開、開発コスト1/3削減
- **顧客行動データ**: 求人→結婚→住宅のライフイベント連携、タイミング最適化

**エコシステム設計の原則**:
1. **補完性**: 既存製品と競合せず、補完関係にある
2. **データ連携**: 顧客データ、行動データの相互活用
3. **段階的拡大**: 小さく始めて、成功パターンを横展開
4. **クロスセル設計**: 自然な導線設計、押し売りしない

#### エコシステム最適化評価指標

| 指標 | 目標値 | 業界標準 | リクルート実績 |
|------|--------|---------|--------------|
| **クロスセル率** | 20%以上 | 5-15% | **57%**（Airレジ→Airペイ） |
| **LTV向上** | 3倍以上 | 1.5-2倍 | **3-5倍**（Airシリーズ） |
| **Churn率削減** | 50%削減 | 20-30%削減 | **50-67%削減**（複数製品利用） |
| **CAC削減** | 30%削減 | 10-20%削減 | **40%削減**（既存顧客活用） |

### Reference（Phase 2フレームワーク）

- **Exit Strategy詳細**: `@Recruit_Product_Research/exit_strategies/exit_decision_framework.md`
- **M&A事例**: `@Recruit_Product_Research/exit_strategies/ma_case_studies.md`
- **エコシステム設計**: `@Recruit_Product_Research/ecosystem/ecosystem_design_patterns.md`
- **クロスセル戦略**: `@Recruit_Product_Research/ecosystem/cross_sell_best_practices.md`

---

## 更新履歴

- 2026-01-03: **ForRecruit Phase 2フレームワーク追加** - Exit Strategy・エコシステム最適化
  - Phase 2フレームワーク追加（Exit Strategy、エコシステム最適化）
  - M&A Exit事例3件統合（Indeed、Glassdoor、USENavi）
  - エコシステム統合パターン20件追加
  - クロスセル成功事例の定量評価
  - Knowledge Base拡張 (+300行 → +400行、Phase 2完了)
- 2026-01-02: **ForRecruit Edition完成** - 企業内新規事業特化版18スキル
  - 18スキル作成完了（Batch 1-3）
  - Ring制度ステージゲート統合
  - 社内承認プロセスフロー確立
  - 撤退基準（Yellow/Orange/Red Alert）策定
  - 社内リソース活用評価6カテゴリ20点満点化
  - Recruit_Product_Research 86件統合
  - Knowledge Base拡張 (+218行 → +300行、Phase 2 Batch 5完了)
- 2025-12-29: **Tier 0実装完了** - Pivot Decision自動化 + Unit Economics検証
  - `/validate-unit-economics` 新規作成（332行、Framework準拠100%）
  - `/pivot-decision` 新規作成（398行、Pivot 10類型自動判定）
  - `skill_chains.md` 大幅拡張（Pivot Decision Path 230行追加）
  - `knowledge_base.md` 更新（Tier 0スキル2件追加、概念マップ自動化版）
  - Framework準拠率: 89.2% → 95.0%達成（Gap 1, 9解消）
- 2025-12-28: 起業の科学準拠版スキル追加（create-persona, research-competitors, validate-cpf, validate-psf）
- 2025-12-28: スキルチェーン定義追加（skill_chains.md）
- 2025-12-28: 既存スキル修正（discover-demand, simulate-interview, research-problem）
- 2025-12-28: Phase A/B/C概念作成完了（19ファイル）
- 2025-12-28: Knowledge Base初版作成
