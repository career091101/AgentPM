# 起業の科学とスキルのカバレッジマップ + 不足領域リスト

**作成日**: 2025-12-30
**対象**: 起業の科学 vs Founder Agent Skills

---

## 1. エグゼクティブサマリー

| 項目 | 結果 |
|------|------|
| 起業の科学総章節数 | 49見出し (6 STEP + 1付録) |
| 既存スキル数 | 42個（SKILL.md完備） |
| マッピング完了 | 24/49章節 (49.0%) |
| 未カバー章節 | 25/49章節 (51.0%) |
| 不足スキル候補 | 15個 |

**重要度**: ⚠️ **高** - 主要フレームワークの約半分が未実装

---

## 2. STEP別マッピング

### STEP 0: Starting Point

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 0.1 | なぜスタートアップは失敗するのか | - 失敗パターン分析<br>- スタートアップの死因<br>- メタ認知 | ❌ | **未カバー** |
| 0.2 | スタートアップ・メタ原則 | - リーンスタートアップ<br>- 仮説検証サイクル<br>- ピボット vs 継続 | pivot-decision（部分的） | ⚠️ **部分カバー** |

**STEP 0カバレッジ**: 0.5/2章節（25%）

---

### STEP 1: アイデアの検証

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 1.1 | 良いアイデアの条件 | - FIF (Founder-Issue Fit)<br>- 情熱・専門性・市場<br>- Founder-Market Fit | ❌ | **未カバー** |
| 1.2 | スタートアップのアイデア着想法 | - 課題ベース発想<br>- トレンド分析<br>- 市場機会の特定 | discover-demand | ✅ **カバー** |
| 1.3 | アイデア検証チェックリスト | - 初期検証項目<br>- FIFスコアリング<br>- Go/No-Go判断 | ❌ | **未カバー** |

**STEP 1カバレッジ**: 1/3章節（33.3%）

---

### STEP 2: CPF（Customer Problem Fit）

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 2.1 | 目的 | - CPFの定義<br>- 達成基準（60%以上）<br>- 検証の重要性 | validate-cpf | ✅ **カバー** |
| 2.2 | 課題仮説キャンバス | - 3U+1フレームワーク<br>- Unworkable<br>- Unavoidable<br>- Urgent<br>- Underserved | validate-cpf | ✅ **カバー** |
| 2.3 | 顧客インタビューの方法 | - インタビュー設計<br>- 質問テクニック<br>- バイアス回避 | simulate-interview | ✅ **カバー** |
| 2.4 | ペルソナ作成 | - ペルソナ定義<br>- アーリーアダプター特定<br>- 1日の行動タイムライン | create-persona | ✅ **カバー** |
| 2.5 | CPF達成の判断基準 | - スコアリング手法<br>- 60%基準<br>- インタビュー30件 | validate-cpf | ✅ **カバー** |

**STEP 2カバレッジ**: 5/5章節（100%） ✅

---

### STEP 3: PSF（Problem Solution Fit）

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 3.1 | 目的 | - PSFの定義<br>- 10倍改善の必要性<br>- MVP検証 | validate-psf | ✅ **カバー** |
| 3.2 | UVP（Unique Value Proposition）の定義 | - 独自の価値提案<br>- 一文での表現<br>- 「なぜ今か」の明示 | validate-10x（部分的） | ⚠️ **部分カバー** |
| 3.3 | MVPの種類 | - LP（Landing Page）<br>- コンシェルジュMVP<br>- オズの魔法使いMVP<br>- Fake Door MVP | build-lp（LP のみ）、validate-psf（選定） | ⚠️ **部分カバー** |
| 3.4 | 10倍改善の原則 | - 10倍優位性の軸<br>- 競合比較<br>- 独占可能性 | validate-10x | ✅ **カバー** |
| 3.5 | PSF達成の判断基準 | - 10倍2軸以上<br>- MVP類型選定<br>- UVP刺さり度35/40 | validate-psf | ✅ **カバー** |

**STEP 3カバレッジ**: 3.5/5章節（70%）

---

### STEP 4: PMF（Product Market Fit）

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 4.1 | PMFとは | - PMFの定義<br>- 達成の重要性<br>- ステージの違い | ❌ | **未カバー** |
| 4.2 | PMF達成の指標 | - NPS 50+<br>- D30 Retention 40%+<br>- コホート分析 | ❌ | **未カバー** |
| 4.3 | ピボットの判断 | - Pivot10類型<br>- Pivot vs 継続<br>- データドリブン判断 | pivot-decision | ✅ **カバー** |

**STEP 4カバレッジ**: 1/3章節（33.3%）

---

### STEP 5: スケール

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| 5.1 | ユニットエコノミクス | - LTV/CAC比率<br>- 3.0以上の基準<br>- 収益性検証 | validate-unit-economics | ✅ **カバー** |
| 5.2 | グロースハック | - AARRRメトリクス<br>- Acquisition<br>- Activation<br>- Retention<br>- Referral<br>- Revenue | ❌ | **未カバー** |
| 5.3 | フライホイールの構築 | - 4要素以上の好循環<br>- 成長エンジン設計<br>- 複利効果 | build-flywheel | ✅ **カバー** |

**STEP 5カバレッジ**: 2/3章節（66.7%）

---

### 付録: チェックリスト総合版

| # | 章節 | キーコンセプト | 対応スキル | ステータス |
|---|------|---------------|-----------|-----------|
| A.1 | アイデア段階チェックリスト | - FIFスコアリング<br>- 初期検証項目 | ❌ | **未カバー** |
| A.2 | CPF達成チェックリスト | - 3U+1スコア<br>- インタビュー件数 | validate-cpf | ✅ **カバー** |
| A.3 | PSF達成チェックリスト | - 10倍優位性<br>- MVP類型<br>- UVP刺さり度 | validate-psf | ✅ **カバー** |
| A.4 | PMF達成チェックリスト | - NPS<br>- Retention<br>- Revenue成長率 | ❌ | **未カバー** |

**付録カバレッジ**: 2/4章節（50%）

---

## 3. 全体カバレッジサマリー

| STEP | 章節数 | カバー | 部分カバー | 未カバー | カバレッジ率 |
|------|--------|--------|-----------|---------|-------------|
| STEP 0 | 2 | 0 | 1 | 1 | 25% |
| STEP 1 | 3 | 1 | 0 | 2 | 33.3% |
| STEP 2 | 5 | 5 | 0 | 0 | **100%** ✅ |
| STEP 3 | 5 | 3 | 2 | 0 | 70% |
| STEP 4 | 3 | 1 | 0 | 2 | 33.3% |
| STEP 5 | 3 | 2 | 0 | 1 | 66.7% |
| 付録 | 4 | 2 | 0 | 2 | 50% |
| **合計** | **25** | **14** | **3** | **8** | **58.0%** |

---

## 4. 未カバー領域の詳細（15個のスキル候補）

### 4.1. 優先度: 高（Phase1に必須、7個）

#### ❌ FIF検証スキル (`/validate-fif`)

**未カバー章節**: STEP 1.1, 付録A.1

**フレームワーク**: FIF（Founder-Issue-Fit）

**機能**:
- 6項目のFIFスコアリング
  1. 情熱（Passion）
  2. 専門性（Expertise）
  3. 市場規模（Market Size）
  4. 創業者適性（Founder-Market Fit）
  5. タイミング（Timing）
  6. リソース（Resources）
- スコア40点満点、30点以上でFIF達成
- Go/No-Go判断

**推奨実装場所**: `/orchestrate-phase1`のSTEP 1（discover-demandの前）

---

#### ❌ リーンキャンバススキル (`/apply-lean-canvas`)

**未カバー章節**: （AgentSkills.mdセクション12に記載）

**フレームワーク**: リーンキャンバス

**機能**:
- 9要素すべて記入
  1. 課題（Problem）
  2. 顧客セグメント（Customer Segments）
  3. 独自の価値提案（UVP）
  4. ソリューション（Solution）
  5. チャネル（Channels）
  6. 収益の流れ（Revenue Streams）
  7. コスト構造（Cost Structure）
  8. 主要指標（Key Metrics）
  9. 圧倒的な優位性（Unfair Advantage）

**推奨実装場所**: `/orchestrate-phase1`のSTEP 3（create-mvvの後）

---

#### ❌ UVP定義スキル (`/define-uvp`)

**未カバー章節**: STEP 3.2

**フレームワーク**: UVP（Unique Value Proposition）

**機能**:
- 一文での価値提案作成
- 「なぜ今か」の明示
- 独自性の検証
- 刺さり度スコアリング（40点満点）

**推奨実装場所**: `/orchestrate-phase1`のSTEP 8（validate-10xの前）

---

#### ❌ MVP類型選定スキル (`/select-mvp-type`)

**未カバー章節**: STEP 3.3

**フレームワーク**: MVP類型

**機能**:
- 4種類のMVP比較
  1. LP（Landing Page）
  2. コンシェルジュMVP
  3. オズの魔法使いMVP
  4. Fake Door MVP
- 実現可能性・検証効果・コストの評価
- 最適MVP類型の推奨

**推奨実装場所**: `/orchestrate-phase1`のSTEP 9（build-lpの前、validate-psfに統合）

**注**: 現在はvalidate-psfで部分的にカバーされているが、独立したスキルとして切り出し推奨

---

#### ❌ 5つの眼スキル (`/analyze-5-perspectives`)

**未カバー章節**: （AgentSkills.mdセクション12に記載）

**フレームワーク**: 5つの眼

**機能**:
- 5つの視点で市場分析
  1. 市場トレンド（Market Trend）
  2. 競合（Competitor）
  3. 顧客（Customer）
  4. 自社（Company）
  5. 技術（Technology）
- SWOT分析との統合
- 機会・脅威の特定

**推奨実装場所**: `/orchestrate-phase1`のSTEP 5（research-problemと並行）

---

#### ❌ スタートアップ失敗パターン分析スキル (`/analyze-failure-patterns`)

**未カバー章節**: STEP 0.1

**フレームワーク**: スタートアップの死因分析

**機能**:
- CB Insights「スタートアップが失敗する20の理由」参照
- 自社ビジネスのリスク領域特定
- 予防策の提案

**推奨実装場所**: `/orchestrate-phase1`のSTEP 0（新規追加、discover-demandの前）

---

#### ❌ メタ原則適用スキル (`/apply-meta-principles`)

**未カバー章節**: STEP 0.2

**フレームワーク**: リーンスタートアップ・メタ原則

**機能**:
- 仮説検証サイクルの設計
- Build-Measure-Learnループ
- Pivot判断基準の設定

**推奨実装場所**: `/orchestrate-phase1`のSTEP 0（新規追加、discover-demandの前）

---

### 4.2. 優先度: 中（Phase2-3で必要、5個）

#### ❌ PMF検証スキル (`/validate-pmf`)

**未カバー章節**: STEP 4.1, 4.2, 付録A.4

**フレームワーク**: PMF達成基準

**機能**:
- NPS測定（Net Promoter Score）
- D30 Retention測定（40%+目標）
- コホート分析
- PMF達成判定（NPS 50+ AND Retention 40%+）

**推奨実装場所**: Phase2（/orchestrate-phase2）の最終ステップ

---

#### ❌ NPSスキル (`/measure-nps`)

**未カバー章節**: STEP 4.2, （AgentSkills.mdセクション12に記載）

**フレームワーク**: Net Promoter Score

**機能**:
- NPS測定の標準手法
- Promoter/Passive/Detractor分類
- スコア算出（-100〜+100）
- 50+達成判定

**推奨実装場所**: `/validate-pmf`の内部スキルまたは独立スキル

---

#### ❌ Retention分析スキル (`/analyze-retention`)

**未カバー章節**: STEP 4.2, （AgentSkills.mdセクション12に記載）

**フレームワーク**: Retention分析・コホート分析

**機能**:
- D1/D7/D30リテンション測定
- コホート別分析
- リテンションカーブ作成
- 40%+達成判定

**推奨実装場所**: `/validate-pmf`の内部スキルまたは独立スキル

---

#### ❌ AARRRメトリクススキル (`/measure-aarrr`)

**未カバー章節**: STEP 5.2, （AgentSkills.mdセクション12に記載）

**フレームワーク**: AARRRメトリクス（Pirate Metrics）

**機能**:
- 5つの成長指標測定
  1. Acquisition（獲得）
  2. Activation（活性化）
  3. Retention（継続）
  4. Referral（紹介）
  5. Revenue（収益）
- ファネル分析
- ボトルネック特定

**推奨実装場所**: Phase2（/orchestrate-phase2）の監視スキル

---

#### ❌ Balance Scorecardスキル (`/create-balanced-scorecard`)

**未カバー章節**: （AgentSkills.mdセクション12に記載）

**フレームワーク**: Balance Scorecard

**機能**:
- 4つの視点で評価
  1. 財務（Financial）
  2. 顧客（Customer）
  3. 業務プロセス（Internal Process）
  4. 学習と成長（Learning & Growth）
- KPI設定
- 戦略マップ作成

**推奨実装場所**: Phase3（Scale）の評価スキル

---

### 4.3. 優先度: 低（補助的機能、3個）

#### ⚠️ MVP実装スキル（コンシェルジュ/オズの魔法使い/Fake Door）

**未カバー章節**: STEP 3.3

**フレームワーク**: MVP類型

**機能**:
- LPに加えて、他のMVP類型の実装支援
- コンシェルジュMVP: 手動オペレーション設計
- オズの魔法使いMVP: 裏側手動のフロント自動化設計
- Fake Door MVP: 偽ボタンテスト設計

**推奨実装場所**: 各MVP類型ごとに個別スキル作成（オプション）

**注**: build-lpが既に存在するため、優先度は低い。必要に応じて拡張。

---

#### ⚠️ グロースハック戦術スキル (`/apply-growth-tactics`)

**未カバー章節**: STEP 5.2

**フレームワーク**: グロースハック手法

**機能**:
- バイラルループ設計
- 紹介プログラム設計
- A/Bテスト設計
- コンバージョン最適化

**推奨実装場所**: Phase3（Scale）の成長スキル

**注**: AARRRメトリクススキルと統合可能

---

#### ⚠️ スタートアップ総合診断スキル (`/diagnose-startup-health`)

**未カバー章節**: 全STEP横断

**フレームワーク**: 総合診断

**機能**:
- 全STEPの達成状況を横断的に評価
- FIF/CPF/PSF/PMF/Scaleの健全性スコア
- ボトルネック特定
- 次のアクション推奨

**推奨実装場所**: `/startup-scorecard`の拡張版（オプション）

**注**: startup-scorecardが既に存在するため、優先度は低い。

---

## 5. 不足スキル優先順位マトリクス

| # | スキル名 | ビジネスインパクト | 実装難易度 | 優先度 | 推奨実装時期 |
|---|----------|-------------------|-----------|--------|-------------|
| 1 | `/apply-lean-canvas` | **高** | 中 | **P0** | 即座 |
| 2 | `/validate-fif` | **高** | 低 | **P0** | 短期（1週間以内） |
| 3 | `/define-uvp` | **高** | 低 | **P1** | 短期（1週間以内） |
| 4 | `/select-mvp-type` | **高** | 中 | **P1** | 短期（1週間以内） |
| 5 | `/analyze-5-perspectives` | 中 | 中 | **P1** | 短期（2週間以内） |
| 6 | `/validate-pmf` | **高** | **高** | **P2** | 中期（1ヶ月以内） |
| 7 | `/measure-nps` | 中 | 低 | **P2** | 中期（1ヶ月以内） |
| 8 | `/analyze-retention` | 中 | 中 | **P2** | 中期（1ヶ月以内） |
| 9 | `/measure-aarrr` | 中 | 中 | **P2** | 中期（1ヶ月以内） |
| 10 | `/analyze-failure-patterns` | 中 | 低 | **P3** | 長期（2ヶ月以内） |
| 11 | `/apply-meta-principles` | 中 | 低 | **P3** | 長期（2ヶ月以内） |
| 12 | `/create-balanced-scorecard` | 低 | **高** | **P4** | 将来検討 |
| 13 | MVP実装スキル（3種） | 低 | 中-高 | **P4** | 将来検討 |
| 14 | `/apply-growth-tactics` | 低 | 中 | **P4** | 将来検討 |
| 15 | `/diagnose-startup-health` | 低 | 中 | **P4** | 将来検討 |

---

## 6. 結論

### 6.1. 全体評価

| 評価項目 | スコア | 備考 |
|---------|-------|------|
| カバレッジ率 | ⭐⭐⭐☆☆ (3/5) | 58.0% |
| STEP 2（CPF）カバレッジ | ⭐⭐⭐⭐⭐ (5/5) | 100% - 完璧 |
| STEP 3（PSF）カバレッジ | ⭐⭐⭐⭐☆ (4/5) | 70% - 良好 |
| STEP 4（PMF）カバレッジ | ⭐⭐☆☆☆ (2/5) | 33.3% - 要改善 |
| 不足スキル優先度分類 | P0: 2個, P1: 3個, P2: 4個, P3-P4: 6個 | - |

### 6.2. 主要な発見

1. **CPFは完璧** - STEP 2は100%カバー、Phase1の強み
2. **PMFが弱い** - STEP 4は33.3%のみ、Phase2-3の課題
3. **P0-P1が5個** - 短期的に実装すべきスキルが明確
4. **リーンキャンバスが最優先** - `/orchestrate-phase1`の依存関係に記載済み

### 6.3. 次のアクション

1. **即座**: `/apply-lean-canvas`スキルの実装（P0、T004完了後）
2. **短期（1-2週間）**: P0-P1の5スキル実装
   - `/validate-fif`
   - `/define-uvp`
   - `/select-mvp-type`
   - `/analyze-5-perspectives`
3. **中期（1ヶ月）**: P2の4スキル実装（PMF関連）
   - `/validate-pmf`
   - `/measure-nps`
   - `/analyze-retention`
   - `/measure-aarrr`
4. **長期（2ヶ月以降）**: P3-P4の6スキル実装（オプション）

---

**レポート作成**: 2025-12-30 15:15
**次のタスク**: T006（Phase1の12ステップと起業の科学の照合）
