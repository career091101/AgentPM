# スキル定義とコマンド照合結果レポート

**作成日**: 2025-12-30
**対象**: Founder Agent & Trading Agents

---

## 1. エグゼクティブサマリー

| 項目 | 結果 |
|------|------|
| 総スキル数 | 48ディレクトリ |
| SKILL.md存在 | 42/48 (87.5%) |
| SKILL.md不足 | 6/48 (12.5%) |
| Founder Agent不一致 | 1/12依存スキル (8.3%) |
| Trading Agents不一致 | 0/4依存スキル (0%) |

**重要度**: ⚠️ **中** - `apply-lean-canvas`スキルが不足（/orchestrate-phase1の依存関係に記載）

---

## 2. 全スキル一覧（48個）

### 2.1. Founder Agent関連スキル（16個）

| # | スキル名 | SKILL.md | コマンド | カテゴリ |
|---|----------|----------|----------|----------|
| 1 | discover-demand | ✅ | /discover-demand | Discovery |
| 2 | create-mvv | ✅ | /create-mvv | Planning |
| 3 | build-flywheel | ✅ | /build-flywheel | Planning |
| 4 | create-persona | ✅ | /create-persona | Discovery |
| 5 | research-problem | ✅ | /research-problem | Research |
| 6 | research-competitors | ✅ | /research-competitors | Research |
| 7 | simulate-interview | ✅ | /simulate-interview | Validation |
| 8 | validate-cpf | ✅ | /validate-cpf | Validation |
| 9 | validate-10x | ✅ | /validate-10x | Validation |
| 10 | validate-psf | ✅ | /validate-psf | Validation |
| 11 | validate-unit-economics | ✅ | /validate-unit-economics | Validation |
| 12 | build-lp | ✅ | /build-lp | Execution |
| 13 | create-sns-content | ✅ | /create-sns-content | Marketing |
| 14 | startup-scorecard | ✅ | /startup-scorecard | Monitoring |
| 15 | pivot-decision | ✅ | /pivot-decision | Decision |
| 16 | orchestrate-phase1 | ✅ | /orchestrate-phase1 | Orchestrator |

### 2.2. Trading Agent関連スキル（24個）

#### オーケストレーター（6個）

| # | スキル名 | SKILL.md | コマンド | 役割 |
|---|----------|----------|----------|------|
| 1 | trading-agents | ✅ | /trading-agents | Main Orchestrator |
| 2 | orchestrate-trading-strategy | ✅ | /orchestrate-trading-strategy | Alternative Orchestrator |
| 3 | trading-phase1-analysts | ✅ | /trading-phase1-analysts | Phase1 Orchestrator |
| 4 | trading-phase2-research | ✅ | /trading-phase2-research | Phase2 Orchestrator |
| 5 | trading-phase3-risk | ✅ | /trading-phase3-risk | Phase3 Orchestrator |
| 6 | trading-phase4-execution | ✅ | /trading-phase4-execution | Phase4 Orchestrator |

#### 個別エージェント（18個）

| # | スキル名 | SKILL.md | コマンド | フェーズ |
|---|----------|----------|----------|----------|
| 1 | agent-data-collector | ✅ | /agent-data-collector | Phase1 |
| 2 | agent-technical-analyst | ✅ | /agent-technical-analyst | Phase1 |
| 3 | agent-elliott-wave-analyst | ✅ | /agent-elliott-wave-analyst | Phase1 |
| 4 | agent-sentiment-analyst | ✅ | /agent-sentiment-analyst | Phase1 |
| 5 | agent-fundamentals-analyst | ✅ | /agent-fundamentals-analyst | Phase1 |
| 6 | agent-market-analyst | ✅ | /agent-market-analyst | Phase1 |
| 7 | agent-news-analyst | ✅ | /agent-news-analyst | Phase1 |
| 8 | agent-strategy-synthesizer | ✅ | /agent-strategy-synthesizer | Phase2 |
| 9 | agent-backtest-validator | ✅ | /agent-backtest-validator | Phase2 |
| 10 | agent-bull-researcher | ✅ | /agent-bull-researcher | Phase2 |
| 11 | agent-bear-researcher | ✅ | /agent-bear-researcher | Phase2 |
| 12 | agent-research-manager | ✅ | /agent-research-manager | Phase2 |
| 13 | agent-risk-manager | ✅ | /agent-risk-manager | Phase3 |
| 14 | agent-fund-manager | ✅ | /agent-fund-manager | Phase3 |
| 15 | agent-risky-portfolio | ✅ | /agent-risky-portfolio | Phase4 |
| 16 | agent-safe-portfolio | ✅ | /agent-safe-portfolio | Phase4 |
| 17 | agent-neutral-portfolio | ✅ | /agent-neutral-portfolio | Phase4 |
| 18 | agent-trader | ✅ | /agent-trader | Phase4 |

### 2.3. その他のスキル（8個）

| # | スキル名 | SKILL.md | コマンド | カテゴリ |
|---|----------|----------|----------|----------|
| 1 | daily-tasks-ultralight | ✅ | /daily-tasks-ultralight | Productivity |
| 2 | test-bash-execution | ✅ | /test-bash-execution | Testing |
| 3 | _shared | ❌ | - | Shared Resources |
| 4 | autonomous_backup | ❌ | - | Utilities |
| 5 | case_reference | ❌ | - | Reference |
| 6 | frameworks | ❌ | - | Reference |
| 7 | mentor | ❌ | - | Guidance |
| 8 | stage_validation | ❌ | - | Validation |

---

## 3. 依存関係の検証

### 3.1. /orchestrate-phase1の依存関係

| # | 依存スキル | 存在 | ステータス |
|---|-----------|------|------------|
| 1 | discover-demand | ✅ | OK |
| 2 | create-mvv | ✅ | OK |
| 3 | **apply-lean-canvas** | ❌ | **MISSING** |
| 4 | build-flywheel | ✅ | OK |
| 5 | research-problem | ✅ | OK |
| 6 | simulate-interview | ✅ | OK |
| 7 | validate-cpf | ✅ | OK |
| 8 | validate-10x | ✅ | OK |
| 9 | build-lp | ✅ | OK |
| 10 | validate-psf | ✅ | OK |
| 11 | create-sns-content | ✅ | OK |
| 12 | startup-scorecard | ✅ | OK |

**結果**: 11/12存在（91.7%）
**不足**: apply-lean-canvas

### 3.2. /trading-agentsの依存関係

| # | 依存スキル | 存在 | ステータス |
|---|-----------|------|------------|
| 1 | trading-phase1-analysts | ✅ | OK |
| 2 | trading-phase2-research | ✅ | OK |
| 3 | trading-phase3-risk | ✅ | OK |
| 4 | trading-phase4-execution | ✅ | OK |

**結果**: 4/4存在（100%）
**不足**: なし

---

## 4. 不一致の詳細

### 4.1. SKILL.md不足（6個）

以下のディレクトリはSKILL.mdファイルが存在しません：

| # | ディレクトリ名 | 推定用途 | 対応必要性 |
|---|---------------|---------|-----------|
| 1 | _shared | 共有リソース（ドキュメント、エラーハンドリング等） | 低（内部リソース） |
| 2 | autonomous_backup | 自動バックアップ機能 | 中（実装コード確認必要） |
| 3 | case_reference | ケーススタディ参照 | 低（参照資料） |
| 4 | frameworks | フレームワークドキュメント | 低（参照資料） |
| 5 | mentor | メンター機能 | 中（機能不明） |
| 6 | stage_validation | ステージ検証機能 | 中（機能不明） |

### 4.2. 不足スキル（1個）

| # | スキル名 | 参照元 | 影響範囲 | 対応優先度 |
|---|----------|--------|---------|-----------|
| 1 | apply-lean-canvas | /orchestrate-phase1 SKILL.md dependencies | /orchestrate-phase1実行時にエラー発生の可能性 | **高** |

---

## 5. 対応推奨事項

### 5.1. 即座に対応が必要（優先度: 高）

#### ❌ `apply-lean-canvas`スキルの不足

**問題**:
- `/orchestrate-phase1`のSKILL.mdのdependenciesに記載されているが、実装が存在しない

**影響**:
- `/orchestrate-phase1`実行時にSTEP 3でエラーが発生する可能性
- Phase1全自動実行が中断される

**推奨対応**（3つの選択肢）:

1. **スキル新規作成** - `/apply-lean-canvas`スキルを実装
   - 所要時間: 2-4時間
   - メリット: SKILL.mdの記載通りの動作を保証
   - デメリット: 実装工数がかかる

2. **既存スキルで代替** - リーンキャンバス機能を既存スキルに統合
   - 候補: `/create-mvv`または`/validate-cpf`に統合
   - 所要時間: 1-2時間
   - メリット: 新規スキル不要
   - デメリット: スキル責務が曖昧になる

3. **依存関係から削除** - `/orchestrate-phase1`のdependenciesから削除
   - 所要時間: 5分
   - メリット: 最速
   - デメリット: リーンキャンバス作成機能が失われる

**おすすめ**: **選択肢1（スキル新規作成）** - 起業の科学ではリーンキャンバスが重要なフレームワークのため、独立したスキルとして実装すべき

### 5.2. 中期的に対応（優先度: 中）

#### ⚠️ SKILL.md不足のスキルディレクトリ（6個）

**対応**:
1. 各ディレクトリの中身を確認
2. 実装コードが存在する場合: SKILL.mdを作成
3. 参照資料のみの場合: ディレクトリ名をREADME.md等に変更し、明示的に「スキルではない」ことを示す

**推奨順序**:
1. autonomous_backup - 自動バックアップ機能の有無を確認
2. mentor - メンター機能の有無を確認
3. stage_validation - ステージ検証機能の有無を確認
4. _shared, case_reference, frameworks - 参照資料として整理

### 5.3. 長期的に対応（優先度: 低）

#### 📋 AgentSkills.mdの更新

**現状**:
- AgentSkills.mdはFounder Agentのルールセット（制約条件）のみ記載
- 利用可能なスキルコマンド一覧が記載されていない

**推奨**:
- AgentSkills.mdに「利用可能なスキルコマンド一覧」セクションを追加
- または、別ファイル（AVAILABLE_SKILLS.md）を作成

---

## 6. 起業の科学との整合性（予備調査）

### 6.1. 起業の科学の主要フレームワーク（19個）

以下のフレームワークが`AgentSkills.md`セクション11-12に記載されています：

| # | フレームワーク | 対応スキル候補 | ステータス |
|---|---------------|---------------|-----------|
| 1 | FIF（Founder-Issue-Fit） | ❌ | **未実装** |
| 2 | 3U+1（CPF基準） | validate-cpf | ✅ |
| 3 | 10倍優位性 | validate-10x | ✅ |
| 4 | リーンキャンバス | ❌ apply-lean-canvas | **未実装** |
| 5 | MVV | create-mvv | ✅ |
| 6 | フライホイール | build-flywheel | ✅ |
| 7 | 5つの眼 | ❌ | **未実装** |
| 8 | AARRRメトリクス | ❌ | **未実装** |
| 9 | Unit Economics | validate-unit-economics | ✅ |
| 10 | Pivot10類型 | pivot-decision | ✅ |
| 11 | NPS測定 | ❌ | **未実装** |
| 12 | Retention分析 | ❌ | **未実装** |
| 13 | Balance Scorecard | ❌ | **未実装** |
| 14 | MVP類型選定 | validate-psf（部分的） | ⚠️ |
| 15 | CPF達成基準 | validate-cpf | ✅ |
| 16 | PSF達成基準 | validate-psf | ✅ |
| 17 | PMF達成基準 | ❌ | **未実装** |
| 18 | 顧客インタビュー | simulate-interview | ✅ |
| 19 | ペルソナ作成 | create-persona | ✅ |

**カバレッジ**: 10/19実装（52.6%）
**未実装**: 9個（FIF、リーンキャンバス、5つの眼、AARRRメトリクス、NPS測定、Retention分析、Balance Scorecard、PMF達成基準、MVP類型選定）

**次のステップ**:
- T005（起業の科学の目次とスキルのマッピング）で詳細分析
- T006（Phase1の12ステップと起業の科学の照合）で実装ギャップ特定
- T007（スキル追加の優先順位付けと実装計画）で追加スキル設計

---

## 7. 結論

### 7.1. 全体評価

| 評価項目 | スコア | 備考 |
|---------|-------|------|
| スキル定義の充実度 | ⭐⭐⭐⭐☆ (4/5) | 42/48がSKILL.md完備 |
| Founder Agent整合性 | ⭐⭐⭐⭐☆ (4/5) | apply-lean-canvas以外OK |
| Trading Agents整合性 | ⭐⭐⭐⭐⭐ (5/5) | 全依存スキル存在 |
| 起業の科学カバレッジ | ⭐⭐⭐☆☆ (3/5) | 10/19実装（52.6%） |

### 7.2. 次のアクション

1. **即座**: `apply-lean-canvas`スキルの実装（T004完了後）
2. **短期**: 起業の科学の詳細マッピング（T005-T007実行）
3. **中期**: SKILL.md不足の6ディレクトリ整理
4. **長期**: AgentSkills.mdへの利用可能スキル一覧追加

---

**レポート作成**: 2025-12-30 14:45
**次のタスク**: T005（起業の科学の目次とスキルのマッピング）
