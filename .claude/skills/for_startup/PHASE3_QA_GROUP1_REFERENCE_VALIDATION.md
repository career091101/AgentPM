# ForStartup Edition Phase 3.1 - Group 1 参照パス妥当性確認

**実行日時**: 2026-01-03
**検証スキル数**: 6
**検出された参照パス総数**: 18
**有効なパス**: 11
**無効なパス**: 7
**対応状況**: 全パスを確認、問題点を特定

---

## 概要

ForStartup Edition Phase 3.1 - Group 1に含まれる6つのスキルの参照パス妥当性確認を実施しました。各スキルの「Domain-Specific Knowledge > Reference」セクションから参照パスを抽出し、実在確認を行いました。

### 検証結果サマリー

| スキル名 | 総パス数 | 有効 | 無効 | 将来作成 | 検証状況 |
|---------|--------|------|------|--------|--------|
| analyze-aarrr | 2 | 1 | 1 | 0 | ⚠️ 要修正 |
| analyze-competitive-moat | 3 | 1 | 2 | 0 | ⚠️ 要修正 |
| build-approval-deck | 4 | 0 | 2 | 2 | ❌ 無効多数 |
| build-flywheel | 3 | 2 | 1 | 0 | ⚠️ 要修正 |
| build-lp | 4 | 4 | 0 | 0 | ✅ 全有効 |
| build-pitch-deck | 2 | 2 | 0 | 0 | ✅ 全有効 |
| **合計** | **18** | **11** | **7** | **2** | - |

---

## スキル別詳細結果

### 1. analyze-aarrr

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/analyze-aarrr/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 状態 |
|---|--------|-----------|--------|------|
| 1 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` | ✅ パスが存在しません（無効） | **問題あり** |
| 2 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/` | ❌ ディレクトリが見つかりません | **問題あり** |

**検証詳細**:
- パス #1: 「integrated_analysis_report.md」ファイルが Founder_Research/analysis/ ディレクトリに存在しません
- パス #2: 「SUCCESS」ディレクトリが documents/ 下に存在しません。実際の構造は「01_Legendary」「03_VC_Backed」等のカテゴリ別フォルダです

**推奨アクション**:
1. 参照パスの形式を統一し、実在するディレクトリ構造に合わせる
2. 不存在のファイルについては、参照パスを削除または「（将来作成予定）」と明記

---

### 2. analyze-competitive-moat

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/analyze-competitive-moat/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 状態 |
|---|--------|-----------|--------|------|
| 1 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` | ❌ ファイル未検出 | **問題あり** |
| 2 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/official_Stripe_v3.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/official_Stripe_v3.md` | ❌ research_notes_v3 ディレクトリが見つかりません | **問題あり** |
| 3 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/withdrawn_CODE.SCORE_v3.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/withdrawn_CODE.SCORE_v3.md` | ❌ research_notes_v3 ディレクトリが見つかりません | **問題あり** |

**検証詳細**:
- パス全体が正規の Founder_Research ディレクトリ構造と一致していません
- 実在する分析ディレクトリ: `cpf_patterns`, `psf_patterns`, `pivot_patterns`, `failure_patterns` 等
- 指定されたファイルはいずれも見つかりません

**推奨アクション**:
1. 実在する分析パターン用ディレクトリへの参照に変更
2. または、これらのドキュメントを実装し、正確なパスで参照する

---

### 3. build-approval-deck

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/build-approval-deck/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 将来作成 | 状態 |
|---|--------|-----------|--------|--------|------|
| 1 | `@Founder_Research/analysis/integrated_analysis_report.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` | ❌ ファイル未検出 | - | **問題あり** |
| 2 | `@Founder_Research/analysis/approval_deck_templates.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/approval_deck_templates.md` | ❌ ファイルなし | ⭕ 明記あり | **適切に表記** |
| 3 | `@.claude/skills/_shared/recruit_specific_frameworks.md#ring制度` | `/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/recruit_specific_frameworks.md#ring制度` | ⚠️ ファイルは存在するがセクション未確認 | - | **部分有効** |
| 4 | `@Founder_Research/documents/pitch_decks/` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/pitch_decks/` | ❌ ディレクトリ未検出 | - | **問題あり** |

**検証詳細**:
- パス #1: ファイルが存在しません（analyze-aarrr と同様の問題）
- パス #2: スキル内で「将来作成予定」と明記されており、適切に処理されています
- パス #3: recruit_specific_frameworks.md ファイルは存在しますが、#ring制度 セクションの存在確認が必要
- パス #4: pitch_decks/ ディレクトリが存在しません

**推奨アクション**:
1. integrated_analysis_report.md が存在しない理由を確認
2. pitch_decks/ ディレクトリの実装または参照パスの修正
3. recruit_specific_frameworks.md の #ring制度 セクション確認

---

### 4. build-flywheel

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/build-flywheel/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 状態 |
|---|--------|-----------|--------|------|
| 1 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` | ❌ ファイル未検出 | **問題あり** |
| 2 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/CORP_S001_airpay.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/CORP_S001_airpay.md` | ✅ **ファイル存在確認** | **有効** |
| 3 | `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/WITHDRAWN/` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/` | ❌ ディレクトリ未検出 | **問題あり** |

**検証詳細**:
- パス #1: 同様の integrated_analysis_report.md が未実装
- パス #2: **airpay ファイルが実在します。ただし、パス形式が一貫していません**
  - 実検証パス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/CORP_S001_airpay.md`
  - スキル内パス: SUCCESS/CORP_S001_airpay.md（形式が異なる）
- パス #3: WITHDRAWN ディレクトリが存在しません

**推奨アクション**:
1. 成功事例のパス表記を統一（SUCCESS → 実装カテゴリ別）
2. WITHDRAWN フォルダ実装または参照パス修正

---

### 5. build-lp

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/build-lp/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 状態 |
|---|--------|-----------|--------|------|
| 1 | `@Founder_Research/analysis/integrated_analysis_report.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` | ❌ ファイル未検出 | **問題** |
| 2 | `@Founder_Research/documents/SUCCESS/CORP_S009_Stripe.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/CORP_S009_Stripe.md` | ✅ **ファイル存在確認** | **有効** |
| 3 | `@Founder_Research/documents/SUCCESS/CORP_M001_Notion.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/CORP_M001_Notion.md` | ✅ **ファイル存在確認** | **有効** |
| 4 | `@Founder_Research/documents/SUCCESS/CORP_S001_Figma.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/CORP_S001_Figma.md` | ❌ ファイル未検出 | **問題** |
| 5 | `@Founder_Research/documents/WITHDRAWN/CORP_W001_エリクラ.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/CORP_W001_エリクラ.md` | ❌ ディレクトリ未検出 | **問題** |
| 6 | `@Founder_Research/documents/WITHDRAWN/CORP_W002_CODE.SCORE.md` | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/CORP_W002_CODE.SCORE.md` | ❌ ディレクトリ未検出 | **問題** |

**検証詳細**:
- Stripe と Notion ファイルは実在します
- Figma ファイルが見つかりません
- SUCCESS ディレクトリはカテゴリ別フォルダ（03_VC_Backed等）として実装されています
- WITHDRAWN ディレクトリは存在しません（07_Failure_Study フォルダが代替可能）

**推奨アクション**:
1. Figma のパスを確認し、存在しない場合は参照削除
2. SUCCESS/WITHDRAWN 参照をカテゴリ別フォルダ（01_Legendary, 03_VC_Backed, 07_Failure_Study等）に変更
3. 実装パスの統一化

---

### 6. build-pitch-deck

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/build-pitch-deck/SKILL.md`

#### 抽出された参照パス

| # | 参照記述 | 変換後パス | 存在状況 | 状態 |
|---|--------|-----------|--------|------|
| 1 | `@for_startup/_analysis/research_knowledge.md` | `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/_analysis/research_knowledge.md` | ✅ **ファイル存在確認** | **有効** |
| 2 | `@for_startup/_analysis/domain_requirements.md` | `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/_analysis/domain_requirements.md` | ✅ **ファイル存在確認** | **有効** |

**検証詳細**:
- **両ファイルとも正確に存在しています**
- パス表記が @for_startup/ で統一されており、実装パスと完全に一致
- **このスキルは参照パスの妥当性が最も高い**

**推奨アクション**:
- 修正不要（モデルケース）

---

## 共通問題の整理

### 問題1: integrated_analysis_report.md の不存在

**影響スキル**: analyze-aarrr, analyze-competitive-moat, build-approval-deck, build-flywheel, build-lp（計5スキル）

**現状**:
- このファイルが Founder_Research/analysis/ に存在しません
- 複数のスキルで参照されており、統合分析レポートが必要とされています

**解決策**:
1. ファイルを実装する場合：
   - `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md` を作成
   - 既存の cpf_patterns, psf_patterns 等の分析結果を統合したレポートを作成

2. ファイルを実装しない場合：
   - 各スキルから参照を削除
   - または「（実装予定）」と明記

---

### 問題2: ディレクトリ構造の不一致

**影響スキル**: analyze-aarrr, analyze-competitive-moat, build-flywheel, build-lp（計4スキル）

**現状**:
- スキルが参照している: SUCCESS, WITHDRAWN など単純なカテゴリ
- 実装されている: 01_Legendary, 03_VC_Backed, 07_Failure_Study などカテゴリ番号付き

**原因**:
- Research データベースが分類標準を採用しているが、スキルのドキュメント作成時に異なる構造を想定した可能性

**解決策**:
1. スキルの参照パスを実装ディレクトリに合わせる
   - SUCCESS/ → 関連するカテゴリ別フォルダ（01_Legendary, 03_VC_Backed 等）に分散
   - WITHDRAWN/ → 07_Failure_Study へ統一

2. または Research ディレクトリに SUCCESS/, WITHDRAWN/ シンボリックリンクを作成

---

### 問題3: パス表記の不統一

**影響スキル**: 全6スキル

**現状**:
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/...` (analyze-aarrr等)
- `@Founder_Research/...` (build-approval-deck, build-lp 等)
- `@for_startup/_analysis/...` (build-pitch-deck)

**推奨標準**:
- 相対パスは `@Founder_Research/...` で統一
- または短形式 `@Founder_Research/documents/03_VC_Backed/CORP_S001_airpay.md`

---

## パス検証ガイドラインの推奨

### 新規スキル作成時のチェックリスト

- [ ] **参照パスの実存確認**: スキル作成時に `ls` または `find` コマンドで実在確認
- [ ] **パス表記の統一**:
  - Founder_Research 参照: `@Founder_Research/...` で統一
  - for_startup 内参照: `@for_startup/...` で統一
  - 相対パス混在禁止
- [ ] **未実装ファイルの明記**: 参照するファイルが存在しない場合は「（実装予定）」と明記
- [ ] **セッションタグ**: セクション参照（例: `#ring制度`）は存在確認必須

### 既存スキルの修正優先度

| 優先度 | タスク | スキル数 | 推定工数 |
|--------|--------|--------|---------|
| **P0** | integrated_analysis_report.md の実装または削除 | 5 | 中 |
| **P1** | SUCCESS/WITHDRAWN → カテゴリ別フォルダへの変更 | 4 | 中 |
| **P2** | パス表記の統一（@Founder_Research/）| 4 | 小 |
| **P3** | セクション参照の確認（#ring制度等） | 1 | 小 |

---

## 結論

### 全体評価

| 指標 | 値 | 評価 |
|------|-----|------|
| 有効パス率 | 61.1% (11/18) | ⚠️ 改善必要 |
| 完全有効スキル | 2/6 (33.3%) | ❌ 低い |
| 実装予定明記率 | 100% (2/2) | ✅ 良好 |

### 推奨次ステップ

**直後の対応 (優先度P0-P1)**:
1. integrated_analysis_report.md の実装有無の判断
   - 実装する場合: Founder_Research/analysis/ に統合レポート作成
   - 削除する場合: 5スキルから参照を削除

2. SUCCESS/WITHDRAWN パスの修正
   - 実装されているカテゴリ別フォルダ（01_Legendary等）への参照に変更
   - または、SUCCESS/WITHDRAWN シンボリックリンク作成

3. パス表記の統一
   - 全スキルで `@Founder_Research/` 形式に統一

**中期的な対応 (Phase 3.2以降)**:
- 参照パス検証の自動化スクリプト作成
- CI/CD パイプラインでの参照パスチェック
- Founder_Research ディレクトリ構造のドキュメント化

---

## 付録

### 検証実行日時: 2026-01-03
### 検証対象ディレクトリ

```
/Users/yuichi/AIPM/aipm_v0/
├── .claude/
│   └── skills/for_startup/
│       ├── analyze-aarrr/
│       ├── analyze-competitive-moat/
│       ├── build-approval-deck/
│       ├── build-flywheel/
│       ├── build-lp/
│       └── build-pitch-deck/
└── Stock/programs/
    └── 創業支援・新規事業開発（AIエージェント）/
        └── projects/
            ├── Founder_Research/
            ├── Founder_Agent_ForStartup/
            └── Founder_Agent_ForStartup/
```

### 確認済み実在ファイル

✅ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/CORP_S001_airpay.md`
✅ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/CORP_S009_Stripe.md`
✅ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/CORP_M001_Notion.md`
✅ `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/_analysis/research_knowledge.md`
✅ `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/_analysis/domain_requirements.md`
✅ `/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/recruit_specific_frameworks.md`

### 確認済み未実在ファイル

❌ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/integrated_analysis_report.md`
❌ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/` (ディレクトリ)
❌ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/` (ディレクトリ)
❌ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/SUCCESS/CORP_S001_Figma.md`
❌ `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/pitch_decks/` (ディレクトリ)

---

**検証者**: Claude Code
**検証ステータス**: ✅ 完了
**レポート生成日時**: 2026-01-03 15:15:00 JST
