---
description: Phase1全体を自動オーケストレーションし、MVP公開まで完全自律実行する
---
# Phase1 オーケストレーター

AIエージェント（Antigravity）がPhase1（アイデア発見→MVP公開→初期ユーザー獲得）を完全自律的に実行するマスターワークフロー。

## 概要

このワークフローを実行すると、以下のステップを自動的に順次実行し、MVPを公開して初期ユーザーを獲得するまでを完結する。

> [!IMPORTANT]
> **起業の科学準拠**: v2.4より、Founder-Issue-Fit検証（/validate_founder_fit）を追加。

```text
┌─────────────────────────────────────────────────────────────────────┐
│  Phase1 オーケストレーション フロー v2.4                             │
├─────────────────────────────────────────────────────────────────────┤
│  0.   /five_perspectives       → five_perspectives_analysis.md     │
│  0.5  /discover_demand         → demand_discovery.md     【任意】  │
│  1.   /discover_idea           → business_idea.md                  │
│  1.2  /validate_founder_fit    → founder_fit.md          【NEW】   │
│  1.5  /create_mvv              → mvv.md                            │
│  2.   /create_lean_canvas    → lean_canvas.md                      │
│  2.5  /build_flywheel        → flywheel.md                         │
│  3.   /define_persona        → persona.md                          │
│  4.   /validate_problem      → problem_validation.md               │
│  4.3  /research_problem      → problem_research.md      【NEW】    │
│  4.5  /simulate_interview    → interview_simulation.md             │
│  5.   /diagnose_cpf          → cpf_diagnosis.md                    │
│       └─ ❌未達成 → Human-in-the-Loop【厳格化】                    │
│  5.5  /validate_10x          → 10x_validation.md                   │
│  6.   /diagnose_psf          → psf_diagnosis.md                    │
│       └─ ❌未達成 → ソリューション見直し+Human-in-the-Loop         │
│  7.   /build_lp              → mvp/lp/ ディレクトリ                │
│  8.   /deploy_mvp            → 公開URL取得（スキップ可）            │
│  9.   /create_sns_content    → sns_contents/ ディレクトリ          │
│  10.  完了報告               → phase1_completion.md                │
│  10.5 /startup_scorecard     → scorecard.md（簡易版）              │
└─────────────────────────────────────────────────────────────────────┘
```


## 前提条件

- プロジェクトディレクトリ構造が存在する
- `startup_science_knowledge.md` が参照可能
- GitHubアカウントが設定済み（MVP公開用）

---

## アイデアフォルダ管理【NEW】

### フォルダ構造

各アイデアは専用フォルダで管理されます：

```text
projects/ideas/
├── {id}_{name}/                    ← アイデア単位フォルダ
│   ├── metadata.yaml               ← メタ情報（自動更新）
│   ├── README.md                   ← 概要・ステータス
│   ├── documents/                  ← 全成果物
│   │   ├── 1_initiating/
│   │   ├── 2_discovery/
│   │   ├── 3_planning/
│   │   ├── 4_executing/
│   │   └── 5_monitoring/
│   └── mvp/
│       ├── lp/
│       └── sns_contents/
│
└── index.md                        ← 全アイデア一覧
```

### パス変数

以降のステップでは以下の変数を使用します：

| 変数 | 説明 | 例 |
|------|------|----|
| `{IDEA_FOLDER}` | アイデアフォルダのフルパス | `projects/ideas/001_ai-business-assistant` |
| `{IDEA_ID}` | 3桁連番ID | `001` |
| `{IDEA_NAME}` | ケバブケース名 | `ai-business-assistant` |

---

## 実行手順

### STEP -1: アイデアフォルダ初期化【NEW・必須】
// turbo
```text
ツール: run_command + write_to_file
処理:
  1. ideas/ 内の既存フォルダから次のIDを自動採番
  2. アイデア名をケバブケース化（英字20文字以内）
  3. {ID}_{NAME} フォルダを作成
  4. _templates/idea_template/ からコピー
  5. metadata.yaml のプレースホルダを実値で置換
  6. README.md のプレースホルダを実値で置換
出力:
  - {IDEA_FOLDER}/metadata.yaml
  - {IDEA_FOLDER}/README.md
  - {IDEA_FOLDER}/documents/ 構造
  - {IDEA_FOLDER}/mvp/ 構造
```

**自動採番ロジック**:
```
1. ideas/ 内のフォルダ名から最大IDを取得
2. 最大ID + 1 を次のIDとする（存在しない場合は 001）
3. 例: 001, 002 が存在 → 次は 003
```

**完了条件**:
- `{IDEA_FOLDER}` が作成されている
- `metadata.yaml` にID, 名前, 作成日時が記録されている
- `README.md` のプレースホルダが実値で置換されている

> [!NOTE]
> 以降のすべてのステップの出力パスは `{IDEA_FOLDER}` を基準とする。

---

### STEP 0: 5つの眼分析【NEW】
// turbo
```
ツール: /five_perspectives を実行
入力: なし（市場・自社・トレンドを自律分析）
出力: {IDEA_FOLDER}/documents/1_initiating/five_perspectives_analysis.md
```

**目的**: メガトレンド（鳥の眼）、顧客心理（虫の眼）、潮流（魚の眼）を事前分析し、アイデア発見の精度を向上

**完了条件**: 5つの視点がすべて記述されていること

**出典**: 田所雅之「起業参謀の教科書」

---

### STEP 0.5: 需要発見リサーチ【NEW・任意】
// turbo
```text
ツール: /discover_demand を実行
入力: なし（または探索分野キーワード）
出力: {IDEA_FOLDER}/documents/1_initiating/demand_discovery.md
```

**目的**: 「困りごとの生ログ」を起点に、Reddit・Yahoo!知恵袋・Stack Overflow等の実際のユーザー発言から有望な需要を発見

**完了条件**: 
- 最低3件の需要候補が抽出されていること
- 各候補のスコアリング（4軸評価: 切実度/頻度/支払い匂い/未解決度）が完了していること

**判定ロジック**:

| 結果 | 条件 | 次のアクション |
|------|------|--------------| 
| ✅ 有望需要あり | スコア16/20以上の候補あり | 優先的にSTEP 1で活用 |
| ⚠️ 可能性あり | スコア12-15/20 | 参考情報としてSTEP 1で活用 |
| ❌ 需要不明確 | 全候補12/20未満 | STEP 1で別アプローチ推奨 |

> [!NOTE]
> **任意ステップ**: このステップはスキップ可能です。スキップする場合は STEP 1 から開始。
> 生ログベースの需要発見により、STEP 1のアイデア生成精度が向上します。

**出典**: 需要発見リサーチエージェント（生ログ起点アプローチ）

---

### STEP 1: アイデア発見
// turbo
```text
ツール: /discover_idea を実行
入力: {IDEA_FOLDER}/documents/*（参考）
出力: {IDEA_FOLDER}/documents/2_discovery/business_idea.md
```

**完了条件**: `business_idea.md` が作成され、選定アイデアが1つ決定していること

**エラー対応**:
- 検索結果不足 → クエリを変更して再検索（最大3回）
- スコアが低いアイデアのみ → 市場を変更して再調査

---


### STEP 1.5: MVV早期定義【NEW】
// turbo
```text
ツール: /create_mvv を実行
入力: {IDEA_FOLDER}/documents/2_discovery/business_idea.md
出力: {IDEA_FOLDER}/documents/3_planning/mvv.md
```

**目的**: アイデア段階でMission/Vision/Valueを定義し、一貫したビジョンで以降のステップを実行

**完了条件**: 
- Mission/Vision/Valueが定義されていること
- 戦略ストーリー（エレベーターピッチ）が作成されていること

> [!NOTE]
> Phase1段階では簡易版でOK。PMF達成後に精緻化します。

**出典**: 田所雅之「起業大全」

---

### STEP 2: リーンキャンバス作成
// turbo
```
ツール: /create_lean_canvas を実行
入力: {IDEA_FOLDER}/documents/2_discovery/business_idea.md
出力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md
```

**完了条件**: 9要素すべてが記入されていること

---

### STEP 2.5: フライホイール設計【NEW】
// turbo
```
ツール: /build_flywheel を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md
出力: {IDEA_FOLDER}/documents/2_discovery/flywheel.md
```

**目的**: 成長の好循環（フライホイール）を早期に設計し、持続的成長の仕組みを明確化

**完了条件**: フライホイール図と各要素の説明が記述されていること

**出典**: 田所雅之「起業大全」- Amazonフライホイールモデル

---

### STEP 3: ペルソナ定義
// turbo
```
ツール: /define_persona を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md
出力: {IDEA_FOLDER}/documents/3_planning/persona.md
```

**完了条件**: ペルソナシートが完成していること

---

### STEP 4: 課題仮説検証
// turbo
```
ツール: /validate_problem を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/3_planning/persona.md
出力: {IDEA_FOLDER}/documents/2_discovery/problem_validation.md
```

**完了条件**: 3U検証が完了し、総合スコアが算出されていること

---

### STEP 4.3: Web課題発見【NEW・自動実行】
// turbo
```
ツール: /research_problem を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/3_planning/persona.md
出力: {IDEA_FOLDER}/documents/2_discovery/problem_research.md
```

**目的**: SNS・ブログ・Reddit等から実際の課題投稿を収集し、3U検証にリアルなエビデンスを追加

**完了条件**: 
- 最低10件以上の課題投稿を収集
- Web投稿スコアが算出されていること
- 3U検証への統合が完了していること

**判定ロジック**:
| 結果 | 条件 | 次のアクション |
|------|------|--------------| 
| ✅ 強い裏付け | スコア35/50以上 | STEP 4.5へ進行 |
| ⚠️ 中程度の裏付け | スコア20-34/50 | 警告を記録しSTEP 4.5へ進行 |
| ❌ 裏付け不足 | スコア20/50未満 | 課題仮説の見直しを推奨 |

> [!TIP]
> **リアルな顧客の声**: Web上の課題投稿は、実際の顧客インタビューの代替として有効です。
> 特にRedditやX（Twitter）には生の不満・課題が多く投稿されています。

---

### STEP 4.5: 仮想ペルソナインタビュー【NEW・必須】
// turbo
```
ツール: /simulate_interview を実行
入力: {IDEA_FOLDER}/documents/3_planning/persona.md, {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md
出力: {IDEA_FOLDER}/documents/2_discovery/interview_simulation.md
```

**目的**: ペルソナ視点での課題深堀りとUVP刺さり度の事前検証

**完了条件**: 
- インタビュー記録が完成
- UVP刺さり度スコアが算出されていること

**判定ロジック**:
| 結果 | 条件 | 次のアクション |
|------|------|--------------|
| ✅ 良好 | UVP刺さり度 32/40以上 | STEP 5へ進行 |
| ⚠️ 要改善 | UVP刺さり度 24-31/40 | UVP見直しを推奨しつつ進行 |
| ❌ 要見直し | UVP刺さり度 24/40未満 | ペルソナ・課題の再定義を検討 |

> [!NOTE]
> **AIシミュレーションの限界**: 仮想インタビューは検証の補助手段です。
> Phase2以降では実顧客インタビュー（最低20人）を強く推奨します。

---

### STEP 5: CPF達成判定【厳格化】
// turbo
```
ツール: /diagnose_cpf を実行
入力: {IDEA_FOLDER}/documents/2_discovery/problem_validation.md, {IDEA_FOLDER}/documents/3_planning/persona.md, {IDEA_FOLDER}/documents/2_discovery/interview_simulation.md
出力: {IDEA_FOLDER}/documents/2_discovery/cpf_diagnosis.md
```

**判定ロジック**:
| 結果 | 条件 | 次のアクション |
|------|------|--------------|
| ✅ 達成 | スコア80%以上 | STEP 6へ自動進行 |
| ⚠️ 条件付き達成 | スコア60-79% | 警告を記録し、STEP 6へ進行 |
| ❌ 未達成 | スコア60%未満 | **Human-in-the-Loop 必須** |

> [!CAUTION]
> **ステージゲート厳格化**: CPF未達成（60%未満）の場合、自動リトライせず必ずユーザー判断を仰ぎます。
> 課題の根本的な見直しが必要な可能性があるため、プレマチュア・スケーリングを防止します。

**Human-in-the-Loop時の選択肢**:
1. 課題・顧客セグメントを見直して再実行（STEP 1-4に戻る）
2. ピボット検討（`/decide_pivot` を実行）
3. 強行突破（リスクを承知で次に進む）

---

### STEP 5.5: 10倍優位性検証【NEW】
// turbo
```text
ツール: /validate_10x を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/2_discovery/problem_validation.md
出力: {IDEA_FOLDER}/documents/2_discovery/10x_validation.md
```

**目的**: PSF診断の前に、既存代替案と比較して10倍優れているかを詳細検証

**完了条件**: 
- 競合・代替案が特定されていること
- 5軸（時間/コスト/使いやすさ/成果/導入障壁）での比較が完了
- 10倍達成判定が実施されていること

**判定ロジック**:
| 結果 | 条件 | 次のアクション |
|------|------|--------------|
| ✅ 達成 | 最低2軸で10倍以上改善 | STEP 6へ進行 |
| ⚠️ 部分達成 | 1軸のみ10倍以上改善 | 警告を記録しSTEP 6へ進行 |
| ❌ 未達成 | 10倍達成軸なし | ソリューション強化を検討 |

**出典**: 田所雅之「起業の科学」

---

### STEP 6: PSF達成判定【厳格化】
// turbo
```text
ツール: /diagnose_psf を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/2_discovery/cpf_diagnosis.md, {IDEA_FOLDER}/documents/2_discovery/10x_validation.md
出力: {IDEA_FOLDER}/documents/2_discovery/psf_diagnosis.md
```

**判定ロジック**:
| 結果 | 条件 | 次のアクション |
|------|------|--------------|
| ✅ 達成 | MVPタイプ選定済み + 10倍優位性達成 | STEP 7へ自動進行 |
| ⚠️ 条件付き達成 | オファー型MVP推奨 | STEP 7へ進行（LP構築で検証継続） |
| ❌ 未達成 | ソリューション要見直し | **Human-in-the-Loop 必須** |

> [!WARNING]
> **10倍優位性チェック**: 既存代替案と比較して最低2軸で10倍改善がなければ、ソリューション再設計を検討してください。

---

### STEP 7: LP構築
// turbo
```
ツール: /build_lp を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/3_planning/persona.md, {IDEA_FOLDER}/documents/2_discovery/psf_diagnosis.md, {IDEA_FOLDER}/documents/2_discovery/flywheel.md
出力: {IDEA_FOLDER}/mvp/lp/ ディレクトリ（index.html, css/, js/, images/）
```

**完了条件**: 
- index.html が存在
- ローカルプレビューでエラーなし

**エラー対応**:
- 画像生成失敗 → プレースホルダー画像を使用
- HTML構文エラー → 自動修正を試行

---

### STEP 8: MVPデプロイ【スキップ可】
<!-- このステップは自動実行をスキップします -->
```
ツール: /deploy_mvp を実行（手動オプション）
入力: {IDEA_FOLDER}/mvp/lp/ ディレクトリ
出力: {IDEA_FOLDER}/documents/4_executing/deploy_report.md + 公開URL
```

> **⏭️ スキップ**: このステップはオーケストレーション実行時に自動スキップされます。
> デプロイが必要な場合は、Phase1完了後に `/deploy_mvp` を手動で実行してください。

**完了条件**: 公開URLにアクセス可能であること

**エラー対応**:
- GitHub Pages失敗 → Netlifyにフォールバック
- Netlify失敗 → Vercelにフォールバック
- 全失敗 → エラーレポート生成、Human-in-the-Loop へ

---

### STEP 9: SNSコンテンツ作成
// turbo
```
ツール: /create_sns_content を実行
入力: {IDEA_FOLDER}/documents/2_discovery/lean_canvas.md, {IDEA_FOLDER}/documents/3_planning/persona.md, 公開URL
出力: {IDEA_FOLDER}/mvp/sns_contents/ ディレクトリ
```

**完了条件**: 最低3投稿分のコンテンツが作成されていること

---

### STEP 10: 完了報告
// turbo
```
ツール: write_to_file
出力: {IDEA_FOLDER}/documents/4_executing/phase1_completion.md
```

以下の内容で完了レポートを生成：

```markdown
# Phase1 完了レポート

**完了日時**: [日時]
**所要時間**: [開始からの経過時間]
**バージョン**: v2.0（起業の科学準拠）

## 成果物サマリー

| 成果物 | ステータス | リンク |
|--------|----------|-------|
| 5つの眼分析 | ✅ | [five_perspectives_analysis.md] |
| ビジネスアイデア | ✅ | [business_idea.md] |
| リーンキャンバス | ✅ | [lean_canvas.md] |
| フライホイール | ✅ | [flywheel.md] |
| ペルソナ | ✅ | [persona.md] |
| 課題検証 | ✅ | [problem_validation.md] |
| 仮想インタビュー | ✅ | [interview_simulation.md] |
| CPF診断 | ✅ | [cpf_diagnosis.md] |
| PSF診断 | ✅ | [psf_diagnosis.md] |
| MVP（LP） | ✅ | [公開URL] |
| SNSコンテンツ | ✅ | [sns_contents/] |

## 選定ビジネス
- **サービス名**: [名前]
- **UVP**: [1文]
- **ターゲット**: [ペルソナ要約]
- **フライホイール**: [好循環の説明]

## 公開URL
🌐 [URL]

## Phase2への推奨事項
> [!IMPORTANT]
> Phase2（PMF達成）に進む前に、**実顧客インタビュー（最低20人）**を実施することを強く推奨します。

### 次のアクション
→ 実インタビュー実施後、`/diagnose_cpf` を再実行してスコア確認
→ Phase2（PMF達成）へ進む場合は `/diagnose_pmf` を実行
→ ピボット検討は `/decide_pivot` を実行
```

---

### STEP 10.5: スタートアップ・スコアカード【NEW・簡易版】
// turbo
```text
ツール: /startup_scorecard を実行（簡易版）
入力: {IDEA_FOLDER}/documents/*（全成果物）
出力: {IDEA_FOLDER}/documents/5_monitoring/scorecard.md
```

**目的**: Phase1完了時点での健康状態を4つの視点から可視化

**評価視点**:
| 視点 | Phase1での評価項目 |
|------|-------------------|
| Financial | 予想価格帯設定、収益モデルの明確さ |
| Customer | ペルソナ定義の質、CPFスコア、UVP刺さり度 |
| Internal Process | LP完成度、MVPタイプ選定の適切さ |
| Learning & Growth | フライホイール設計、次フェーズへの準備度 |

**完了条件**: 4視点すべてでスコアが算出されていること

> [!NOTE]
> Phase1の簡易版では、実績データがないためシミュレーション値を使用。
> Phase2以降で実データに基づく本格評価を実施します。

**出典**: 田所雅之「起業大全」

---

## グローバルエラーハンドリング

| エラータイプ | 対応 |
|-------------|------|
| ファイル保存失敗 | ディレクトリ作成を試行後、再保存 |
| 外部API失敗（検索等） | 30秒待機後、リトライ（最大3回） |
| リトライ上限到達 | エラーレポート生成、Human-in-the-Loop へ |
| 致命的エラー | 処理停止、エラーログ出力、ユーザー通知 |

## Human-in-the-Loop ポイント【強化】

以下の状況では**必ず**ユーザー判断を仰ぐ：

| ポイント | 条件 | 選択肢 |
|---------|------|-------|
| CPF未達成 | スコア60%未満 | 再実行 / ピボット / 強行 |
| PSF未達成 | ソリューション要見直し | 再設計 / ピボット / 強行 |
| 仮想インタビュー低評価 | UVP刺さり度24/40未満 | 再定義 / 継続（警告付き） |
| デプロイ全失敗 | 全プラットフォーム失敗 | 手動対応依頼 |
| 致命的エラー | 予期せぬ例外 | ログ確認後に判断 |

---

## 顧客インタビューオプション【NEW】

### オプションA: 仮想インタビュー（デフォルト・自動実行）
- `/simulate_interview` を自動実行
- AIによるペルソナシミュレーション
- 即時実行可能だが検証精度は限定的

### オプションB: 実インタビューガイド生成（推奨）
```text
ツール: /generate_interview_guide を実行
出力: documents/2_discovery/interview_guide.md
```
- インタビュー計画・質問リスト・記録テンプレートを生成
- ユーザーが手動でインタビュー実施（目標20人）
- 分析フレームワークで結果を集計
- 結果入力後に `/diagnose_cpf` を再実行

> [!TIP]
> **Phase2以降では必ずオプションBを実施してください。**
> 実顧客の声なしにPMFは達成できません。

---

## 変更履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| v1.0 | 2025-12-25 | 初版作成 |
| v2.0 | 2025-12-25 | 起業の科学準拠: 5つの眼/フライホイール/仮想インタビュー追加、ステージゲート厳格化 |
| v2.1 | 2025-12-25 | 中期改善: MVV早期定義/10倍検証独立化/スコアカード/実インタビューガイド追加 |
| v2.2 | 2025-12-25 | 需要発見リサーチ追加: STEP 0.5 `/discover_demand` を新設、生ログ起点の需要発見機能を統合 |
| v2.3 | 2025-12-25 | Web課題発見追加: STEP 4.3 `/research_problem` を新設、SNS・ブログ・Reddit等から課題投稿を収集し3U検証を補強 |

---

## 実行コマンド

このワークフロー全体を開始するには：
```
/orchestrate_phase1
```

個別ステップを実行する場合は各ワークフローを直接呼び出し。

---

**出典**: 田所雅之「起業の科学」「起業大全」「起業参謀の教科書」
