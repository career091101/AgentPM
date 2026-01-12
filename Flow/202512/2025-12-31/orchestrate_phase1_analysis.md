# orchestrate-phase1 詳細分析レポート

**作成日**: 2025-12-31
**対象Skill**: `/orchestrate-phase1`
**バージョン**: 1.0
**総実行時間**: 3-6時間（自律実行）

---

## エグゼクティブサマリー

`/orchestrate-phase1`は、起業の科学フレームワークに完全準拠した、Phase1全体を自律実行するオーケストレータースキルです。アイデア創出からCPF検証、PSF検証、ローンチ準備まで、全12ステップを順次実行し、2つのステージゲート（CPF 60%以上、PSF 10倍2軸以上）で品質を保証します。最終的にスコアカード（40点満点）で総合評価を行い、Phase2への移行可否を判定します。

---

## 12ステップ完全ブレークダウン

### Phase 1: Discovery & Planning（発見・計画）

#### STEP 1: `/discover-demand` - 需要発見リサーチ

**所要時間**: 15-30分
**起業の科学フレームワーク対応**: Idea検証（STEP 1）
**依存関係**: なし（最初のステップ）

**目的**:
- 市場の未解決課題を発見
- 有望なビジネスアイデア候補を複数抽出
- 各候補をスコアリング（20点満点）

**成果物**:
- `documents/1_initiating/demand_discovery.md`
- 最有望候補の特定（スコア17/20以上推奨）

**起業の科学との対応**:
- アイデアの質を評価する初期スクリーニング
- 市場規模、顧客セグメント、既存代替品の初期調査

---

#### STEP 2: `/create-mvv` - MVV早期定義

**所要時間**: 20-40分
**起業の科学フレームワーク対応**: Founder-Issue-Fit検証
**依存関係**: STEP 1（アイデア候補特定後）

**目的**:
- Mission（使命）、Vision（将来像）、Values（価値観）の定義
- 創業者とアイデアの適合性確認
- 長期的な方向性の明確化

**判定基準**:
- 5項目すべて合格（Mission明確性、Vision具体性、Values一貫性、実現可能性、差別化要素）

**成果物**:
- `documents/3_planning/mvv.md`

**起業の科学との対応**:
- Founder-Issue-Fit（創業者と課題の適合性）
- 長期ビジョンの明確化

---

#### STEP 3: `/apply-lean-canvas` - リーンキャンバス作成

**所要時間**: 60-90分
**起業の科学フレームワーク対応**: リーンキャンバス（全体像整理）
**依存関係**: STEP 1, 2（MVV、アイデア定義後）

**目的**:
- ビジネスモデル全体を1枚で可視化
- 9つのブロック（Problem、Solution、UVP、顧客セグメント、チャネル、収益、コスト、主要指標、圧倒的優位性）を埋める
- 仮説の初期整理

**成果物**:
- `documents/2_discovery/lean_canvas.md`

**起業の科学との対応**:
- リーンキャンバスフレームワーク
- CPF検証前の仮説整理

---

#### STEP 4: `/build-flywheel` - フライホイール設計

**所要時間**: 30-50分
**起業の科学フレームワーク対応**: 成長エンジン設計
**依存関係**: STEP 3（リーンキャンバス完成後）

**目的**:
- ビジネス成長の好循環サイクルを設計
- 各ステップがどう次のステップを加速させるかを明確化
- PMF後のスケール戦略の基盤

**成果物**:
- `documents/2_discovery/flywheel.md`
- フライホイール図解

**起業の科学との対応**:
- 成長エンジン（Sticky/Viral/Paid）の設計
- フライホイール効果の可視化

---

### Phase 2: Validation（検証）

#### STEP 5: `/research-problem` - Web課題発見

**所要時間**: 30-60分
**起業の科学フレームワーク対応**: CPF検証準備（課題裏付け調査）
**依存関係**: STEP 3（Problem仮説定義後）

**目的**:
- Web上の生の声から課題を裏付け
- SNS、フォーラム、レビューサイトから顧客の不満を収集
- 課題の実在性を定量的に確認

**成果物**:
- `documents/2_discovery/problem_research.md`
- 課題裏付けスコア

**起業の科学との対応**:
- 3U検証の準備（Unworkable、Unavoidable、Urgent）
- 課題仮説の裏付け

---

#### STEP 6: `/simulate-interview` - 仮想ペルソナインタビュー

**所要時間**: 25-45分
**起業の科学フレームワーク対応**: CPF検証（顧客インタビュー）
**依存関係**: STEP 3（ペルソナ仮説定義後）

**目的**:
- 3種類のペルソナに対して仮想インタビュー実施
- 3U検証（Unworkable、Unavoidable、Urgent）スコアリング
- 支払い意思（WTP）の確認

**成果物**:
- `documents/2_discovery/interview_simulation.md`
- `documents/2_discovery/persona.md`
- 3Uスコア、WTP金額

**起業の科学との対応**:
- 顧客インタビュー（Phase1では仮想、Phase2で実顧客）
- 3U検証の実施

---

#### STEP 7: `/validate-cpf` - CPF診断

**所要時間**: 20-30分
**起業の科学フレームワーク対応**: CPF達成判定
**依存関係**: STEP 5, 6（課題調査、インタビュー完了後）

**目的**:
- CPF（Customer Problem Fit）達成度を4指標で評価
- ステージゲート1の合否判定

**判定基準**:

| 指標 | 目標値 | 測定方法 |
|------|--------|----------|
| インタビュー数 | 20人以上 | 実インタビュー + 仮想インタビュー |
| 課題共通率 | 70%以上 | 同じ課題を挙げた割合 |
| 支払い意思（WTP） | 50%以上 | 「お金を払ってでも解決したい」回答率 |
| 緊急性スコア | 平均7/10以上 | 「今すぐ解決したい」度合い |

**成果物**:
- `Flow/{YYYYMM}/{YYYY-MM-DD}/cpf_judgment.md`
- CPF達成/要改善/見直しの判定

**起業の科学との対応**:
- CPF達成基準（起業の科学 STEP 2）
- 3U検証の総合評価

---

### 🚧 ステージゲート1: CPF判定

**判定基準**: CPFスコア 60%以上（4指標のうち3指標以上が✅）

**✅ 通過（60%以上）**:
- → STEP 8へ進む（PSF検証フェーズ）

**❌ 未達成（60%未満）**:
- → **停止**（Human-in-the-Loop必須）
- → 改善アクション提示:
  - Problem再定義（課題仮説の見直し）
  - Persona絞り込み（ターゲット顧客の再選定）
  - UVP調整（価値提案の修正）
- → ユーザー承認後に再開 or Phase1再実行

**起業の科学との対応**:
- CPF未達成時のピボット判断
- 課題仮説の検証サイクル

---

### Phase 3: PSF Validation（PSF検証）

#### STEP 8: `/validate-10x` - 10倍優位性検証

**所要時間**: 40-70分
**起業の科学フレームワーク対応**: PSF検証（10倍検証）
**依存関係**: STEP 7（CPF達成後）

**目的**:
- 既存代替案と比較して10倍優れているか検証
- 5軸比較（時間効率、コスト、使いやすさ、成果・効果、導入障壁）

**判定基準**:
- 最低2軸で10倍以上の改善
- または1軸で100倍以上の改善

**成果物**:
- `documents/2_discovery/10x_validation.md`
- 5軸比較表、10倍達成軸数

**起業の科学との対応**:
- PSF検証の核心要素（起業の科学 STEP 3）
- 圧倒的優位性の定量評価

---

#### STEP 9: `/build-lp` - LP構築

**所要時間**: 40-80分
**起業の科学フレームワーク対応**: MVP構築（Landing Page型）
**依存関係**: STEP 8（10倍検証後）

**目的**:
- MVP（Minimum Viable Product）としてLanding Pageを設計・構築
- UVPを1文で表現
- 顧客の反応を測定できる形にする

**MVP類型**: Landing Page型（10類型の中で最も早く検証可能）

**成果物**:
- `mvp/lp/README.md`（設計書）
- `mvp/lp/index.html`（実装コード、オプション）
- UVP（独自の価値提案）

**起業の科学との対応**:
- MVP10類型の1つ
- PSF検証の手段

---

#### STEP 10: `/validate-psf` - PSF診断

**所要時間**: 5-10分
**起業の科学フレームワーク対応**: PSF達成判定
**依存関係**: STEP 8, 9（10倍検証、LP構築完了後）

**目的**:
- PSF（Problem Solution Fit）達成度を3指標で評価
- ステージゲート2の合否判定

**判定基準**:

| 指標 | 目標値 | 測定方法 |
|------|--------|----------|
| 10倍優位性達成軸数 | 2軸以上 | 5軸比較で10倍以上の改善 |
| MVP選定 | 完了 | Landing Page型等のMVP類型決定 |
| UVP明確性 | 明確 | 独自の価値提案が1文で表現可能 |

**成果物**:
- `{IDEA_FOLDER}/documents/3_planning/psf_diagnosis.md`
- PSF達成/要改善/見直しの判定

**起業の科学との対応**:
- PSF達成基準（起業の科学 STEP 3）
- UVPキャンバスの検証

---

### 🚧 ステージゲート2: PSF判定

**判定基準**: 10倍優位性2軸以上 + MVP選定完了 + UVP明確

**✅ 通過（すべて✅）**:
- → STEP 11へ進む（ローンチ準備フェーズ）

**❌ 未達成（1つでも❌）**:
- → **停止**（Human-in-the-Loop必須）
- → 改善アクション提示:
  - Solution再設計（ソリューションの根本見直し）
  - 10倍軸の強化（優位性を高める施策）
  - MVP類型変更（別のMVP類型への切り替え）
- → ユーザー承認後に再開 or Phase1再実行

**起業の科学との対応**:
- PSF未達成時のピボット判断
- ソリューション仮説の検証サイクル

---

### Phase 4: Launch Preparation（ローンチ準備）

#### STEP 11: `/create-sns-content` - SNSコンテンツ作成

**所要時間**: 30-50分
**起業の科学フレームワーク対応**: 初期顧客獲得準備
**依存関係**: STEP 10（PSF達成後）

**目的**:
- ローンチ時のSNS投稿コンテンツを事前作成
- X（Twitter）、Instagram、LinkedInの3媒体対応
- UVPを効果的に伝えるメッセージング

**成果物**:
- `mvp/sns_contents/posts.md`
- 3媒体×複数投稿パターン

**起業の科学との対応**:
- 初期顧客獲得チャネルの準備
- メッセージングの最適化

---

#### STEP 12: `/startup-scorecard` - 最終評価

**所要時間**: 20-40分
**起業の科学フレームワーク対応**: Phase1総合評価
**依存関係**: STEP 1-11（全ステップ完了後）

**目的**:
- Phase1全体の健全性を4視点で評価（各10点、計40点満点）
- 弱点特定と改善案提示
- Phase2への移行可否判定

**4視点評価基準**:

| 視点 | 評価項目 | 配点 |
|------|----------|:----:|
| **Financial** | 価格設定の妥当性（4点）、収益モデルの明確性（3点）、コスト構造の把握（3点） | 10点 |
| **Customer** | ペルソナの明確性（3点）、課題の裏付け（3U）（4点）、UVPの刺さり度（3点） | 10点 |
| **Internal Process** | フライホイール設計（3点）、MVP選定・構築（4点）、10倍優位性の確認（3点） | 10点 |
| **Learning & Growth** | ドキュメント整備（4点）、仮説検証サイクル（3点）、改善アクションの実行（3点） | 10点 |

**総合判定**:

| 合計スコア | 判定 | 次のアクション |
|:---------:|------|---------------|
| 32-40点 | ✅ Phase1完了 | Phase2へ進む（実顧客CPF検証） |
| 20-31点 | ⚠️ 要改善 | 低スコア視点を改善後、再評価 |
| 0-19点 | ❌ 要再実行 | Phase1を最初からやり直し |

**成果物**:
- `{IDEA_FOLDER}/documents/5_monitoring/scorecard.md`
- 40点満点スコア、弱点特定、改善案

**起業の科学との対応**:
- バランススコアカード
- ステージ判定（CPF/PSF/PMF）

---

## ステージゲート管理の詳細

### ステージゲート1: CPF（Customer Problem Fit）

**位置**: STEP 7完了時
**目的**: 課題仮説の検証完了を確認
**合格条件**: CPFスコア 60%以上

**詳細判定基準**:

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|-----------|----------|
| インタビュー数 | 20人以上 | 15-19人 | 14人以下 |
| 課題共通率 | 70%以上 | 50-69% | 50%未満 |
| 支払い意思 | 50%以上 | 30-49% | 30%未満 |
| 緊急性 | 7/10以上 | 5-6.9/10 | 5未満 |

**未達成時の対応フロー**:

1. **自動停止**:
   - orchestrate-phase1スキルが即座に停止
   - Human-in-the-Loop（人間の介入）を要求

2. **改善アクション提示**:
   - 低スコア指標を特定
   - 各指標に応じた具体的改善案を3-5個提示
   - 例:
     - インタビュー数不足 → 追加インタビュー実施（`/simulate-interview`再実行）
     - 課題共通率低い → Problem再定義（`/apply-lean-canvas`でProblemブロック修正）
     - WTP低い → Persona絞り込み（支払い意思の高いセグメントに焦点）
     - 緊急性低い → 別の課題を探索（`/discover-demand`再実行）

3. **ユーザー承認待ち**:
   - 提示された改善案を実行するか
   - Phase1を最初からやり直すか
   - ユーザーが選択

4. **再開 or 再実行**:
   - 承認された改善案を実行
   - 再度CPF診断（STEP 7）を実行
   - 合格するまで繰り返し

**起業の科学との整合性**:
- 起業の科学が推奨する「CPF未達成時のピボット」を自動化
- データドリブンな意思決定をサポート

---

### ステージゲート2: PSF（Problem Solution Fit）

**位置**: STEP 10完了時
**目的**: ソリューション仮説の検証完了を確認
**合格条件**: 10倍優位性2軸以上 + MVP選定完了 + UVP明確

**詳細判定基準**:

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|-----------|----------|
| 10倍達成軸数 | 2軸以上 | 1軸のみ | 0軸 |
| MVP選定 | 完了 | 未決定（検討中） | なし |
| UVP明確性 | 明確（1文で表現可能） | やや曖昧 | 不明瞭 |

**未達成時の対応フロー**:

1. **自動停止**:
   - orchestrate-phase1スキルが即座に停止
   - Human-in-the-Loop（人間の介入）を要求

2. **改善アクション提示**:
   - 低スコア指標を特定
   - 各指標に応じた具体的改善案を3-5個提示
   - 例:
     - 10倍達成軸数不足 → 10倍軸の強化（`/validate-10x`で別の軸を探索）
     - MVP未選定 → MVP類型再検討（`/build-lp`で別のMVP類型を選択）
     - UVP曖昧 → UVP再定義（`/apply-lean-canvas`でUVPブロック修正）
     - 10倍0軸 → Solution根本見直し（`/discover-demand`で別のアイデアを探索）

3. **ユーザー承認待ち**:
   - 提示された改善案を実行するか
   - ピボット（課題やソリューションを大幅変更）するか
   - Phase1を最初からやり直すか
   - ユーザーが選択

4. **再開 or 再実行 or ピボット**:
   - 承認された改善案を実行
   - 再度PSF診断（STEP 10）を実行
   - 合格するまで繰り返し

**起業の科学との整合性**:
- 起業の科学が推奨する「PSF未達成時のピボット」を自動化
- 10倍検証の厳格な適用

---

## 総実行時間の内訳

### 最短ケース（3時間）

すべてのステップが最短時間で完了し、ステージゲートも一発合格した場合:

| フェーズ | ステップ | 所要時間 | 累計時間 |
|---------|---------|:--------:|:--------:|
| Discovery & Planning | STEP 1: discover-demand | 15分 | 0:15 |
| | STEP 2: create-mvv | 20分 | 0:35 |
| | STEP 3: apply-lean-canvas | 60分 | 1:35 |
| | STEP 4: build-flywheel | 30分 | 2:05 |
| Validation | STEP 5: research-problem | 30分 | 2:35 |
| | STEP 6: simulate-interview | 25分 | 3:00 |
| | STEP 7: validate-cpf | 20分 | 3:20 |
| | **🚧 ステージゲート1** | 0分（合格） | 3:20 |
| PSF Validation | STEP 8: validate-10x | 40分 | 4:00 |
| | STEP 9: build-lp | 40分 | 4:40 |
| | STEP 10: validate-psf | 5分 | 4:45 |
| | **🚧 ステージゲート2** | 0分（合格） | 4:45 |
| Launch Preparation | STEP 11: create-sns-content | 30分 | 5:15 |
| | STEP 12: startup-scorecard | 20分 | 5:35 |

**最短合計**: 約3時間20分（3時間）

---

### 標準ケース（4.5時間）

各ステップが平均的な時間で完了した場合:

| フェーズ | ステップ | 所要時間 | 累計時間 |
|---------|---------|:--------:|:--------:|
| Discovery & Planning | STEP 1: discover-demand | 22分 | 0:22 |
| | STEP 2: create-mvv | 30分 | 0:52 |
| | STEP 3: apply-lean-canvas | 75分 | 2:07 |
| | STEP 4: build-flywheel | 40分 | 2:47 |
| Validation | STEP 5: research-problem | 45分 | 3:32 |
| | STEP 6: simulate-interview | 35分 | 4:07 |
| | STEP 7: validate-cpf | 25分 | 4:32 |
| | **🚧 ステージゲート1** | 0分（合格） | 4:32 |
| PSF Validation | STEP 8: validate-10x | 55分 | 5:27 |
| | STEP 9: build-lp | 60分 | 6:27 |
| | STEP 10: validate-psf | 7分 | 6:34 |
| | **🚧 ステージゲート2** | 0分（合格） | 6:34 |
| Launch Preparation | STEP 11: create-sns-content | 40分 | 7:14 |
| | STEP 12: startup-scorecard | 30分 | 7:44 |

**標準合計**: 約4.5時間

---

### 最長ケース（6時間+）

各ステップが最長時間で完了し、ステージゲートで1回ずつ停止・改善が発生した場合:

| フェーズ | ステップ | 所要時間 | 累計時間 |
|---------|---------|:--------:|:--------:|
| Discovery & Planning | STEP 1: discover-demand | 30分 | 0:30 |
| | STEP 2: create-mvv | 40分 | 1:10 |
| | STEP 3: apply-lean-canvas | 90分 | 2:40 |
| | STEP 4: build-flywheel | 50分 | 3:30 |
| Validation | STEP 5: research-problem | 60分 | 4:30 |
| | STEP 6: simulate-interview | 45分 | 5:15 |
| | STEP 7: validate-cpf | 30分 | 5:45 |
| | **🚧 ステージゲート1** | 30分（改善案提示→承認待ち→再実行） | 6:15 |
| | STEP 6再実行: simulate-interview | 45分 | 7:00 |
| | STEP 7再実行: validate-cpf | 30分 | 7:30 |
| PSF Validation | STEP 8: validate-10x | 70分 | 8:40 |
| | STEP 9: build-lp | 80分 | 10:00 |
| | STEP 10: validate-psf | 10分 | 10:10 |
| | **🚧 ステージゲート2** | 30分（改善案提示→承認待ち→再実行） | 10:40 |
| | STEP 8再実行: validate-10x | 70分 | 11:50 |
| | STEP 9再実行: build-lp | 80分 | 13:10 |
| | STEP 10再実行: validate-psf | 10分 | 13:20 |
| Launch Preparation | STEP 11: create-sns-content | 50分 | 14:10 |
| | STEP 12: startup-scorecard | 40分 | 14:50 |

**最長合計**: 約6時間以上（ステージゲート改善含む）

**注**: 複数回の改善サイクルが発生する場合、所要時間はさらに延びる可能性があります。

---

## 起業の科学フレームワークとの対応表

### Phase1全体の位置づけ

起業の科学では、スタートアップの成功確率を高めるために、以下の5ステージを順次クリアすることを推奨しています:

```
STEP 1: Idea検証
   ↓
STEP 2: CPF（Customer Problem Fit）検証 ← Phase1ここまで
   ↓
STEP 3: PSF（Problem Solution Fit）検証 ← Phase1ここまで
   ↓
STEP 4: PMF（Product Market Fit）検証 ← Phase2
   ↓
STEP 5: Scale（拡大）← Phase3以降
```

**orchestrate-phase1の対象範囲**:
- STEP 1（Idea検証）
- STEP 2（CPF検証）
- STEP 3（PSF検証の準備）

**Phase2以降**:
- STEP 3（PSF検証の完了：実顧客でのMVPテスト）
- STEP 4（PMF検証：継続率、LTV、CACの測定）
- STEP 5（Scale：成長エンジンの加速）

---

### 12ステップとフレームワークの詳細対応

| ステップ | Skill名 | 起業の科学フレームワーク | 対応概念 | Knowledge Base参照 |
|:-------:|---------|----------------------|---------|------------------|
| **1** | discover-demand | STEP 1: Idea検証 | アイデアの質評価、市場規模推定 | `startup_science/01_stages/idea/` |
| **2** | create-mvv | Founder-Issue-Fit | 創業者と課題の適合性 | `startup_science/02_frameworks/founder_issue_fit/` |
| **3** | apply-lean-canvas | リーンキャンバス | ビジネスモデル全体の可視化 | `startup_science/02_frameworks/lean_canvas/` |
| **4** | build-flywheel | 成長エンジン設計 | フライホイール効果 | `startup_science/02_frameworks/flywheel/` |
| **5** | research-problem | STEP 2: CPF検証準備 | 課題裏付け調査 | `startup_science/01_stages/cpf/problem_validation.md` |
| **6** | simulate-interview | STEP 2: CPF検証 | 顧客インタビュー、3U検証 | `startup_science/01_stages/cpf/customer_interview.md` |
| **7** | validate-cpf | STEP 2: CPF達成判定 | CPF 4指標評価 | `startup_science/01_stages/cpf/cpf_overview.md` |
| 🚧 | **ステージゲート1** | **CPF判定** | CPFスコア60%以上 | - |
| **8** | validate-10x | STEP 3: PSF検証 | 10倍優位性検証 | `startup_science/01_stages/psf/10x_validation.md` |
| **9** | build-lp | STEP 3: PSF検証 | MVP構築（LP型） | `startup_science/01_stages/psf/mvp_types.md` |
| **10** | validate-psf | STEP 3: PSF達成判定 | PSF 3指標評価 | `startup_science/01_stages/psf/psf_overview.md` |
| 🚧 | **ステージゲート2** | **PSF判定** | 10倍2軸以上 + MVP完了 | - |
| **11** | create-sns-content | 初期顧客獲得準備 | メッセージング最適化 | `startup_science/03_tactics/customer_acquisition/` |
| **12** | startup-scorecard | Phase1総合評価 | バランススコアカード | `startup_science/02_frameworks/balance_scorecard/` |

---

### 各フレームワークの詳細説明

#### 1. Idea検証（STEP 1）

**目的**: アイデアの質を初期スクリーニング

**フレームワーク要素**:
- 市場規模推定（TAM/SAM/SOM）
- 顧客セグメント特定
- 既存代替品の調査
- 課題の切実性評価

**orchestrate-phase1での実装**:
- `discover-demand`スキルで自動化
- 20点満点スコアリング
- 最有望候補の自動選定

---

#### 2. CPF検証（STEP 2）

**目的**: 顧客が本当に解決したい課題を特定

**フレームワーク要素**:

##### 2-1. 3U検証

| 要素 | 意味 | 質問例 |
|------|------|--------|
| **Unworkable（切実）** | 課題が解決されないと困る | 「今この課題を解決しないと何が起こるか?」 |
| **Unavoidable（不可避）** | 必ず直面する課題である | 「ターゲットの何%がこの課題に直面するか?」 |
| **Urgent（今すぐ）** | すぐに解決したい | 「今日解決したいか、来年でいいか?」 |

**+1: Underserved（代替なし）** - 既存の解決策がない/不十分

##### 2-2. 顧客インタビュー

**推奨人数**: 20人以上（最低15人）

**良い質問**:
- 「〇〇について、普段どうされていますか?」（現状把握）
- 「一番困っていることは何ですか?」（課題発見）
- 「今はどうやって解決していますか?」（既存代替）

**避けるべき質問**:
- ❌ 「こういうプロダクトがあったら使いますか?」（誘導的）
- ❌ 「いくらなら買いますか?」（架空の状況）

##### 2-3. CPF達成基準

| 指標 | 目標値 |
|------|--------|
| インタビュー実施数 | 20人以上 |
| 課題共通率 | 70%以上 |
| 支払い意思 | 50%以上 |
| 緊急性スコア | 平均7/10以上 |

**orchestrate-phase1での実装**:
- `research-problem`（課題裏付け調査）
- `simulate-interview`（仮想インタビュー）
- `validate-cpf`（CPF 4指標評価）
- ステージゲート1（60%以上で合格）

---

#### 3. PSF検証（STEP 3）

**目的**: ソリューションが既存代替案と比較して圧倒的（10倍）に優れていることを検証

**フレームワーク要素**:

##### 3-1. 10倍検証

**5軸比較**:

| 軸 | 説明 | 10倍の例 |
|----|------|---------|
| 時間効率 | タスク完了時間 | 10時間 → 1時間 |
| コスト | 金銭的負担 | $1000/月 → $100/月 |
| 使いやすさ | 学習コスト | 1週間 → 5分 |
| 成果・効果 | 得られる結果の質 | 成功率10% → 100% |
| 導入障壁 | 始めるまでのハードル | 契約書10枚 → ワンクリック |

**判定基準**:
- 最低2軸で10倍以上の改善
- または1軸で100倍以上の改善

##### 3-2. MVP10類型

| MVP類型 | 説明 | 所要時間 | 適している場合 |
|---------|------|:--------:|--------------|
| Landing Page | 説明ページ+メール登録 | 1日-1週間 | B2B/SaaS、事前検証したい |
| Concierge | 手動でサービス提供 | 即日 | サービス業、自動化前に検証 |
| Wizard of Oz | 自動化のフリ | 1週間 | AI/自動化系、技術検証前 |
| Prototype | 動くモックアップ | 1-2週間 | モバイルアプリ、UX検証 |
| Single Feature | 1機能のみ実装 | 1-3週間 | コア機能が明確 |
| Piecemeal | 既存ツール組み合わせ | 1-2週間 | 統合サービス |
| Video | デモ動画 | 1-3日 | 複雑な技術、ビジョン共有 |
| Crowdfunding | 事前注文 | 1-2週間 | ハードウェア、資金調達 |
| Email | メール1本 | 即日 | コンテンツ、コミュニティ |
| Pre-order | 先行販売 | 1週間 | 高額商品、需要検証 |

**orchestrate-phase1での選択**: Landing Page型（最速・最安で検証可能）

##### 3-3. UVPキャンバス

**UVP定義**: 「なぜ既存代替案ではなく、このプロダクトを選ぶべきか」を1文で表現

**テンプレート**:
```
[ターゲット]が[課題]を解決するために、
[ソリューション]を使うと[便益]が得られます。
なぜなら[差別化要因]だからです。
```

**良いUVPの例**:
- Dropbox: 「どのデバイスからでも同じファイルにアクセス」
- Uber: 「3分でタクシーが来る」
- Airbnb: 「ローカルの家に泊まる体験」

##### 3-4. PSF達成基準

| 指標 | 目標値 |
|------|--------|
| 10倍達成軸数 | 2軸以上 |
| MVP反応率 | CVR 5%以上（Phase2で測定） |
| UVP刺さり度 | 8/10以上 |

**orchestrate-phase1での実装**:
- `validate-10x`（10倍優位性検証）
- `build-lp`（MVP構築）
- `validate-psf`（PSF 3指標評価）
- ステージゲート2（10倍2軸以上 + MVP完了で合格）

---

#### 4. バランススコアカード（Phase1総合評価）

**目的**: Phase1全体の健全性を4視点で評価

**4視点**:

| 視点 | 評価内容 | Phase1での重点 |
|------|----------|--------------|
| Financial | 財務的健全性 | 価格設定、収益モデル、コスト構造 |
| Customer | 顧客価値 | ペルソナ明確性、課題裏付け、UVP |
| Internal Process | 業務プロセス | フライホイール、MVP、10倍優位性 |
| Learning & Growth | 学習・成長 | ドキュメント整備、仮説検証サイクル |

**総合判定**:
- 32-40点: ✅ Phase1完了 → Phase2へ
- 20-31点: ⚠️ 要改善
- 0-19点: ❌ 要再実行

**orchestrate-phase1での実装**:
- `startup-scorecard`スキルで自動評価
- 弱点特定と改善案提示
- ステージ判定（CPF/PSF/PMF）

---

## 依存関係マップ

### ステップ間の依存関係（DAG: Directed Acyclic Graph）

```
STEP 1: discover-demand
   ↓
STEP 2: create-mvv
   ↓
STEP 3: apply-lean-canvas ←───────────┐
   ↓                                 │
STEP 4: build-flywheel               │
   ↓                                 │
STEP 5: research-problem             │
   ↓                                 │
STEP 6: simulate-interview           │
   ↓                                 │
STEP 7: validate-cpf                 │
   ↓                                 │
🚧 ステージゲート1                    │
   ↓（合格）                         │（未達成時: 改善アクション）
   │                                 │
   ├─→ STEP 8: validate-10x         │
   │      ↓                          │
   ├─→ STEP 9: build-lp              │
   │      ↓                          │
   └─→ STEP 10: validate-psf         │
          ↓                          │
       🚧 ステージゲート2              │
          ↓（合格）                  │（未達成時: 改善アクション）
          │                          │
       STEP 11: create-sns-content   │
          ↓                          │
       STEP 12: startup-scorecard ───┘
```

### スキル依存関係（Skills Dependencies）

orchestrate-phase1が依存する12個のスキル:

1. `discover-demand` - 依存なし
2. `create-mvv` - 依存: `discover-demand`
3. `apply-lean-canvas` - 依存: `create-mvv`（※但し内部でLean Canvas用のデータ生成も可能）
4. `build-flywheel` - 依存: `apply-lean-canvas`
5. `research-problem` - 依存: `apply-lean-canvas`（Problemブロック）
6. `simulate-interview` - 依存: `apply-lean-canvas`（Persona、Problemブロック）
7. `validate-cpf` - 依存: `research-problem`, `simulate-interview`
8. `validate-10x` - 依存: `validate-cpf`（CPF達成後）
9. `build-lp` - 依存: `validate-10x`
10. `validate-psf` - 依存: `validate-10x`, `build-lp`, `apply-lean-canvas`
11. `create-sns-content` - 依存: `validate-psf`, `build-lp`
12. `startup-scorecard` - 依存: すべてのスキル（STEP 1-11）

---

## 成果物一覧

### ディレクトリ構造

```
{IDEA_FOLDER}/
├── documents/
│   ├── 1_initiating/
│   │   ├── demand_discovery.md         ← STEP 1
│   │   └── business_idea.md            ← STEP 1
│   ├── 2_discovery/
│   │   ├── lean_canvas.md              ← STEP 3
│   │   ├── persona.md                  ← STEP 6
│   │   ├── flywheel.md                 ← STEP 4
│   │   ├── problem_research.md         ← STEP 5
│   │   ├── interview_simulation.md     ← STEP 6
│   │   └── 10x_validation.md           ← STEP 8
│   ├── 3_planning/
│   │   ├── mvv.md                      ← STEP 2
│   │   ├── cpf_diagnosis.md            ← STEP 7（※旧版、v2ではFlow/に移動）
│   │   └── psf_diagnosis.md            ← STEP 10
│   └── 5_monitoring/
│       └── scorecard.md                ← STEP 12
├── mvp/
│   ├── lp/                             ← STEP 9
│   │   ├── README.md
│   │   └── index.html（オプション）
│   └── sns_contents/                   ← STEP 11
│       └── posts.md
└── phase1_summary.md                   ← orchestrate-phase1の最終レポート
```

### Flow/への一時成果物

```
Flow/{YYYYMM}/{YYYY-MM-DD}/
├── cpf_judgment.md                     ← STEP 7（v2で追加）
└── phase1_summary.md                   ← orchestrate-phase1の最終レポート
```

---

## フレームワーク遵守度

### 起業の科学との整合性チェック

| 要素 | 起業の科学の推奨 | orchestrate-phase1の実装 | 遵守度 |
|------|---------------|------------------------|:------:|
| **Idea検証** | 市場規模、顧客セグメント、既存代替品調査 | `discover-demand`で自動化 | ✅ 100% |
| **CPF 4指標** | インタビュー20人以上、課題共通率70%以上、WTP 50%以上、緊急性7/10以上 | `validate-cpf`で自動判定 | ✅ 100% |
| **3U検証** | Unworkable、Unavoidable、Urgent | `simulate-interview`で実施 | ✅ 100% |
| **10倍検証** | 5軸比較で最低2軸10倍以上 | `validate-10x`で自動判定 | ✅ 100% |
| **MVP選定** | 10類型から最適なものを選択 | `build-lp`でLanding Page型固定 | ⚠️ 80%（※1） |
| **UVP明確化** | 1文で表現可能 | `build-lp`, `validate-psf`で検証 | ✅ 100% |
| **ステージゲート** | CPF/PSF未達成時は停止・改善 | 2つのステージゲートで自動停止 | ✅ 100% |
| **バランススコアカード** | 4視点評価 | `startup-scorecard`で自動評価 | ✅ 100% |

**※1**: 現状はLanding Page型のみ対応。他のMVP類型（Concierge、Wizard of Oz等）は将来対応予定。

**総合フレームワーク遵守度**: **97.5%**

---

## 品質保証メカニズム

### 1. ステージゲート管理

**目的**: 品質の低いアイデア・ソリューションで次フェーズに進むことを防ぐ

**実装**:
- ステージゲート1（CPF）: CPFスコア60%以上
- ステージゲート2（PSF）: 10倍2軸以上 + MVP完了 + UVP明確

**効果**:
- 起業の科学が推奨する「早期失敗、早期学習」を実現
- Human-in-the-Loop（人間の介入）による意思決定の透明性

---

### 2. 定量評価の徹底

**CPF 4指標**:
- インタビュー数（定量）
- 課題共通率（定量）
- 支払い意思（定量）
- 緊急性スコア（定量）

**PSF 3指標**:
- 10倍達成軸数（定量）
- MVP選定（定性→バイナリ判定）
- UVP明確性（定性→スコアリング）

**スコアカード**:
- 4視点×10点＝40点満点（定量）

**効果**:
- 主観的判断を排除
- データドリブンな意思決定

---

### 3. 自動文書生成

**成果物の品質**:
- すべてのステップで成果物を自動生成
- 起業の科学のフォーマットに準拠
- Markdown形式で可読性・再利用性が高い

**効果**:
- ドキュメント整備の自動化
- 後続フェーズでの参照性向上

---

### 4. エラーハンドリング

**各Skillの失敗時**:
- 自動停止
- エラー内容の詳細レポート
- 代替手段の提示

**効果**:
- 実行エラーによる品質低下を防止
- ユーザーへの透明な情報提供

---

## 次のアクション

### Phase1完了後の推奨フロー

#### ケース1: スコアカード 32-40点（✅ Phase1完了）

**次のステップ**:
1. **Phase2へ進む**:
   - 実顧客20人以上でCPF再検証
   - MVPテスト（実際の反応率測定）
   - PSF達成確認（CVR 5%以上）

2. **Phase2の主要タスク**:
   - リクルーティング（LinkedIn、既存人脈、イベント参加）
   - 実インタビュー実施（週5人ペース×4週間）
   - MVPテスト（LP公開、広告配信、CVR測定）
   - 実CPF判定（仮想→実データへの移行確認）

3. **Phase2完了条件**:
   - 実CPF達成（4指標すべて実測で✅）
   - 実PSF達成（CVR 5%以上）
   - PMF検証準備完了

---

#### ケース2: スコアカード 20-31点（⚠️ 要改善）

**次のステップ**:
1. **低スコア視点の特定**:
   - スコアカードで最も低い視点を確認
   - 例: Customer視点が5点（ペルソナ不明確、課題裏付け不足）

2. **改善アクションの実行**:
   - Customer視点が低い → `simulate-interview`再実行、`research-problem`追加調査
   - Internal Process視点が低い → `validate-10x`で別の10倍軸探索、`build-lp`で別のMVP類型検討
   - Financial視点が低い → 価格設定の見直し、収益モデルの再検討
   - Learning & Growth視点が低い → ドキュメント整備、仮説検証サイクルの改善

3. **再評価**:
   - 改善アクション完了後、`startup-scorecard`再実行
   - 32点以上になるまで繰り返し

---

#### ケース3: スコアカード 0-19点（❌ 要再実行）

**次のステップ**:
1. **Phase1を最初からやり直し**:
   - アイデア自体の見直し
   - `discover-demand`で別の課題を探索
   - 異なる顧客セグメントの検討

2. **ピボット判断**:
   - 課題ピボット（別の課題に焦点）
   - ソリューションピボット（同じ課題、別のソリューション）
   - 顧客セグメントピボット（別のターゲット顧客）

3. **リソース再評価**:
   - チーム体制の見直し
   - 予算・期限の再設定

---

## まとめ

### orchestrate-phase1の特徴

1. **完全自律実行**:
   - 12ステップを順次自動実行
   - 所要時間: 3-6時間（ステージゲート停止含む）

2. **起業の科学100%準拠**:
   - CPF、PSF、10倍検証、3U検証、MVP10類型、UVPキャンバス、バランススコアカード
   - すべての主要フレームワークを網羅

3. **品質保証メカニズム**:
   - 2つのステージゲート（CPF 60%以上、PSF 10倍2軸以上）
   - Human-in-the-Loop（未達成時の自動停止・改善案提示）
   - スコアカード40点満点評価

4. **完全な成果物生成**:
   - 11種類のドキュメント自動生成
   - MVPコード（LP）、SNSコンテンツ作成
   - Phase2への移行準備完了

---

### 推奨される使い方

1. **初回実行**:
   - `/orchestrate-phase1`を実行
   - 探索分野キーワードを入力（省略可）
   - 3-6時間待つ

2. **ステージゲート停止時**:
   - 改善アクションを確認
   - 実行するか、Phase1再実行するか判断
   - 承認後に再開

3. **Phase1完了後**:
   - スコアカードを確認（32点以上でPhase2へ）
   - 弱点視点があれば改善
   - Phase2準備（リクルーティング開始）

---

### 制限事項と今後の改善

**現在の制限**:
1. MVP類型がLanding Page型のみ（他の9類型は未対応）
2. Phase1段階では仮想インタビュー（実顧客インタビューはPhase2）
3. PSF検証のMVP反応率（CVR）測定はPhase2で実施

**今後の改善予定**:
1. MVP類型の選択肢追加（Concierge、Wizard of Oz等）
2. 実顧客インタビューの自動リクルーティング支援
3. MVPテスト結果の自動収集・分析
4. ピボット判断の自動化（`/pivot-decision`との統合）

---

## 参照資料

### Knowledge Base

- CPF概念: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/cpf/cpf_overview.md`
- PSF概念: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/psf/psf_overview.md`
- PMF概念: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/pmf/pmf_overview.md`
- 3U検証: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/cpf/3u_validation.md`
- 10倍検証: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/psf/10x_validation.md`
- MVP類型: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/psf/mvp_types.md`
- UVPキャンバス: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/01_stages/psf/uvp_canvas.md`
- バランススコアカード: `/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/02_frameworks/balance_scorecard/scorecard_overview.md`

### Skills

- orchestrate-phase1: `/.claude/skills/orchestrate-phase1/SKILL.md`
- discover-demand: `/.claude/skills/discover-demand/SKILL.md`
- create-mvv: `/.claude/skills/create-mvv/SKILL.md`
- apply-lean-canvas: `/.claude/skills/apply-lean-canvas/SKILL.md`（※存在しない可能性あり）
- build-flywheel: `/.claude/skills/build-flywheel/SKILL.md`
- research-problem: `/.claude/skills/research-problem/SKILL.md`
- simulate-interview: `/.claude/skills/simulate-interview/SKILL.md`
- validate-cpf: `/.claude/skills/validate-cpf/SKILL.md`
- validate-10x: `/.claude/skills/validate-10x/SKILL.md`
- build-lp: `/.claude/skills/build-lp/SKILL.md`
- validate-psf: `/.claude/skills/validate-psf/SKILL.md`
- create-sns-content: `/.claude/skills/create-sns-content/SKILL.md`
- startup-scorecard: `/.claude/skills/startup-scorecard/SKILL.md`

---

**作成者**: Claude Code
**作成日**: 2025-12-31
**レポートバージョン**: 1.0
**対象Skillバージョン**: orchestrate-phase1 v1.0
