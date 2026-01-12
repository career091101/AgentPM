# 未完了タスク一覧

**作成日**: 2026-01-10
**データソース**: Flow/202601/2026-01-10/ 配下の4ドキュメント
**分析対象期間**: 2026-01-01 〜 2026-01-10

---

## サマリー

| プロジェクト領域 | 未完了タスク数 | 完了済み | 最高優先度 | 推定工数合計 |
|---------------|--------------|---------|-----------|------------|
| **Late API Script** | 6件 | 6件 ✅ | Medium | 9-13時間 |
| **Auto Migration** | 0件 | 1件 ✅ | - | - |
| **Week 8 Ralph Wiggum** | 0件 | 1件 ✅ | - | - |
| **SNS Automation** | 5件 | 0件 | High | 2-4週間 |
| **合計** | **11件** | **8件 ✅** | - | **9-13時間 + 2-4週間** |

**進捗率**: 42% (8/19タスク完了)

---

## 1. Late API Script Issues（Critical 〜 Low）

**出典**: `late_api_script_issues_report.md` (710行)

### 1.1 Critical（即座対応必須）

#### ✅ Task #1: パラメータ名エラー修正 - **完了**
- **ファイル**: `Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py`
- **問題**: `fromDate`/`toDate` → 正しくは `dateFrom`/`dateTo`
- **影響**: 期間フィルタが機能せず、全投稿が返される
- **完了日**: 2026-01-10
- **コミット**: 33c3765f
- **状態**: ✅ **完了** - 行106-107を`dateFrom`/`dateTo`に修正済み

---

### 1.2 High（1週間以内対応）

#### ✅ Task #2: N+1クエリ問題の解決 - **既に実装済み**
- **ファイル**: 同上
- **状態**: ✅ **既に実装済み** - `/analytics`エンドポイントで一括取得実装済み
- **実装内容**:
  - `fetch_analytics_page()`関数で1回のAPI呼び出しで100件取得
  - `post.get("analytics", {})`でレスポンスに含まれるanalyticsデータを直接利用
  - 追加のAPI呼び出しなし（N+1問題解消済み）

#### ✅ Task #3: ページネーション実装 - **既に実装済み**
- **ファイル**: 同上
- **状態**: ✅ **既に実装済み** - whileループでページネーション実装済み
- **実装箇所**: `fetch_all_analytics()`関数（lines 208-279）
- **実装内容**:
  - `page`パラメータでページ単位取得
  - `hasMore`フィールドまたは取得件数で継続判定
  - `all_analytics_data`配列に累積

#### ✅ Task #4: Dual ID System対応 - **既に実装済み**
- **ファイル**: 同上
- **状態**: ✅ **既に実装済み** - `postId`/`_id`, `isExternal`対応済み
- **実装箇所**: lines 228-230, 252-254
- **実装内容**:
  ```python
  post_id = post.get("postId") or post.get("_id")
  is_external = post.get("isExternal", False)
  platform_post_url = post.get("platformPostUrl")
  ```

---

### 1.3 Medium（2週間以内対応）

#### Task #5: エラーハンドリング強化
- **修正内容**: リトライロジック、タイムアウト処理、Rate Limit対応
- **推定工数**: 2-3時間
- **優先度**: ★★★☆☆
- **状態**: ❌ **未実装**

#### ✅ Task #6: ソート機能追加 - **既に実装済み**
- **修正内容**: `sortBy`と`order`パラメータの実装
- **状態**: ✅ **既に実装済み** - `--sort-by {date,engagement}`, `--order {asc,desc}`実装済み
- **実装箇所**: CLI引数とAPI呼び出し

#### Task #7: プロファイルフィルタ追加
- **修正内容**: `profileId`/`profileSlug`パラメータの実装
- **推定工数**: 1時間
- **優先度**: ★★★☆☆
- **状態**: ❌ **未実装**

#### Task #8: データ鮮度向上
- **修正内容**: キャッシュ無効化オプション、リアルタイム取得
- **推定工数**: 2時間
- **優先度**: ★★★☆☆
- **状態**: ⚠️ **部分実装** - `lastUpdated`記録は実装済み、キャッシュ無効化オプションは未実装

#### Task #9: コンテンツフィールド拡充
- **修正内容**: `mediaUrls`, `hashtags`の詳細情報追加
- **推定工数**: 1-2時間
- **優先度**: ★★★☆☆
- **状態**: ⚠️ **部分実装** - `text_full`は実装済み、`mediaUrls`/`hashtags`詳細は未実装

---

### 1.4 Low（優先度低、時間があれば対応）

#### Task #10: アドオン検証
- **推定工数**: 1-2時間
- **優先度**: ★★☆☆☆

#### Task #11: スキーマバリデーション
- **推定工数**: 2-3時間
- **優先度**: ★★☆☆☆

#### Task #12: i18n対応
- **推定工数**: 3-4時間
- **優先度**: ★★☆☆☆

---

## 2. Auto Migration Testing

**出典**: `week5_phase1_integration_test_summary.md` (321行)

### ✅ Task #13: 統合テスト自動実行 - **完了**
- **完了日**: 2026-01-10
- **コミット**: f13e4c1e
- **状態**: ✅ **完了** - 全5テストシナリオPass（21/21 assertions passed）
- **実行結果**:
  - Test 1: Normal Migration - ✅ PASS (8/8 assertions)
  - Test 2: Version History - ✅ PASS (4/4 assertions)
  - Test 3: Rollback Functionality - ✅ PASS (2/2 assertions)
  - Test 4: Parallel Execution (5 Worktrees) - ✅ PASS (5/5 assertions)
  - Test 5: Error Handling - ✅ PASS (2/2 assertions)
- **修正内容**:
  - 環境変数継承問題を修正（subshell対応）
  - Test 5のエラー検出ロジックを改善（出力キャプチャ方式変更）
  - 並列実行のrace condition対策（警告表示）

---

## 3. Week 8 Ralph Wiggum Integration

**出典**: `week8_phase3_improvement_report.md` (279行)

### ✅ Task #14: 統合ルール作成 - **完了**
- **完了日**: 2026-01-10
- **コミット**: dd3793b9
- **状態**: ✅ **完了** - `.claude/rules/ralph_wiggum.md`作成済み
- **ファイル**: `.claude/rules/ralph_wiggum.md`（80行）
- **内容**:
  - 基本コマンド（/ralph-loop, /cancel-ralph, 完了プロミスタグ）
  - 安全ルール4項目（必須遵守）
  - 推奨モデル選択（Haiku/Sonnet）
  - 適用シナリオ（適している/適していないタスク）
  - Week 5設定管理との統合確認
  - 詳細ガイドへの参照リンク
- **効果**: Week 8品質スコア 94→97点（+3点達成見込み）

---

## 4. SNS Automation

**出典**: `sns_performance_analysis_20260101-0110.md` (466行)

### Task #15: 投稿カレンダー作成
- **問題番号**: Issue #21
- **内容**: セクション5-4の推奨投稿スケジュールをカレンダー形式で実装
- **推奨スケジュール**:
  | 曜日 | LinkedIn | X | Threads | Instagram |
  |-----|----------|---|---------|-----------|
  | 火 | 23:00 | 11:00 | 11:00 | - |
  | 水 | 23:00 | 11:00 | - | 10:00 |
  | 金 | 23:00 | 11:00 | 11:00 | - |
  | 土 | 23:00 | 11:00 | - | 10:00 |
  | 日 | 23:00 | 11:00 | 11:00 | - |
- **推定工数**: 2-3時間
- **優先度**: ★★★☆☆（Medium）

### Task #16: Threads Graph API統合スクリプト
- **優先度**: Week 1最優先タスク
- **問題**: 現在Threads投稿のインプレッション数が常に0（API制限）
- **目標**: Views/Reach/Engagementデータを取得可能にする
- **推定工数**: 4-6時間
- **優先度**: ★★★★☆（High）
- **備考**: APIドキュメント調査 + スクリプト実装 + テスト

### Task #17: X（Twitter）ハッシュタグA/Bテスト
- **期間**: 2週間
- **目的**: ハッシュタグの効果測定
- **実施内容**:
  - パターンA: ハッシュタグあり投稿（週3回）
  - パターンB: ハッシュタグなし投稿（週3回）
  - インプレッション・エンゲージメント比較
- **推定工数**: 2週間（投稿継続 + データ収集 + 分析）
- **優先度**: ★★★☆☆（Medium）

### Task #18: LinkedIn投稿時間テスト
- **目的**: 23:00（夜）vs 08:00（朝）の効果比較
- **実施内容**:
  - 2週間 × 各時間帯での投稿
  - インプレッション数比較
- **推定工数**: 2週間（投稿継続 + データ収集 + 分析）
- **優先度**: ★★★☆☆（Medium）

### Task #19: Instagram継続判断
- **期間**: 1ヶ月
- **判断基準**:
  - インプレッション数の改善傾向
  - エンゲージメント率の推移
  - 投稿労力対効果
- **選択肢**:
  - 継続: 投稿頻度・内容を最適化
  - 停止: リソースをLinkedIn/X/Threadsに集中
- **推定工数**: 1ヶ月（データ収集期間）
- **優先度**: ★★☆☆☆（Low）

---

## タスク優先順位マトリクス

### ✅ 完了済みタスク（2026-01-10）

| タスク | 優先度 | 工数 | 状態 | コミット |
|-------|--------|------|------|---------|
| **#1: Late API パラメータ名修正** | Critical | 10分 | ✅ 完了 | 33c3765f |
| **#13: Auto Migration テスト実行** | High | 30分 | ✅ 完了 | f13e4c1e |
| **#2: N+1クエリ解決** | High | - | ✅ 既存実装 | - |
| **#3: ページネーション実装** | High | - | ✅ 既存実装 | - |
| **#4: Dual ID System対応** | High | - | ✅ 既存実装 | - |
| **#6: ソート機能追加** | Medium | - | ✅ 既存実装 | - |
| **#14: Ralph統合ルール** | Medium | 5-10分 | ✅ 完了 | dd3793b9 |

### 最優先（今週中）

| タスク | 優先度 | 工数 | 影響度 |
|-------|--------|------|--------|
| **#16: Threads Graph API統合** | High | 4-6時間 | High（データ欠損解消） |

### 高優先度（2週間以内）

| タスク | 優先度 | 工数 | 影響度 |
|-------|--------|------|--------|
| **#5: エラーハンドリング強化** | Medium | 2-3時間 | Medium（安定性向上） |
| **#15: 投稿カレンダー作成** | Medium | 2-3時間 | Medium（運用効率化） |

### 1ヶ月以内（継続監視）

| タスク | 優先度 | 工数 | 影響度 |
|-------|--------|------|--------|
| **#17: Xハッシュタグテスト** | Medium | 2週間 | Low（最適化） |
| **#18: LinkedIn時間テスト** | Medium | 2週間 | Low（最適化） |
| **#19: Instagram継続判断** | Low | 1ヶ月 | Low（リソース最適化） |
| **#10-12: Late API低優先度** | Low | 6-9時間 | Low（Nice-to-have） |

---

## 推奨実行順序（更新版）

### ✅ Phase 1-2: 完了済み（2026-01-10）

```bash
# ✅ 1. Late APIパラメータ名修正（10分） - コミット 33c3765f
# ✅ 2. Auto Migration テスト実行（30分） - コミット f13e4c1e
# ✅ 3. Ralph統合ルール作成（5-10分） - コミット dd3793b9
# ✅ 4. N+1クエリ解決 - 既存実装確認済み
# ✅ 5. ページネーション実装 - 既存実装確認済み
# ✅ 6. Dual ID System対応 - 既存実装確認済み
# ✅ 7. ソート機能追加 - 既存実装確認済み
```

**進捗**: Phase 1-2完了（8/19タスク完了、42%）

### Phase 3: 最優先対応（今週中）

```bash
# 1. Threads Graph API統合（4-6時間）
# - Meta Graph APIドキュメント調査
# - スクリプト実装（fetch_threads_analytics.py）
# - Views/Reach/Engagement取得
# - 既存Late APIスクリプトとの統合
```

### Phase 4: 高優先度対応（2週間以内）

```bash
# 1. エラーハンドリング強化（2-3時間）
# - リトライロジック
# - タイムアウト処理
# - Rate Limit対応

# 2. SNS投稿カレンダー作成（2-3時間）
# - 推奨スケジュールをカレンダー形式で実装
# - 曜日×プラットフォーム×時間のマトリクス
```

### Phase 4: 継続監視（1ヶ月）

```bash
# 1. Xハッシュタグテスト開始（2週間データ収集）
# 2. LinkedIn時間テスト開始（2週間データ収集）
# 3. Instagram継続判断（1ヶ月データ収集）
```

---

## 技術的詳細メモ

### Late API OpenAPI仕様（参照用）

**ファイル**: `Flow/202601/2026-01-10/late-api-openapi.yaml`

**重要パラメータ**:
```yaml
/analytics:
  parameters:
    - name: dateFrom      # ✅ 正しい
      schema: { type: string, format: date }
    - name: dateTo        # ✅ 正しい
      schema: { type: string, format: date }
    - name: platform
      schema: { type: string, enum: [linkedin, x, threads, instagram] }
    - name: limit
      schema: { type: integer, default: 100 }
    - name: offset        # ページネーション用
      schema: { type: integer, default: 0 }
    - name: sortBy
      schema: { type: string, enum: [postedAt, views, likes, ...] }
    - name: order
      schema: { type: string, enum: [asc, desc] }
```

### Auto Migration バグ修正済み（参照用）

**修正済みバグ（全5件）**:
1. Log directory path problem（絶対パス化）
2. Metadata JSON path problem（cd前に絶対パス変換）
3. Flow file path problem（絶対パス化）
4. PROJECT_ROOT override problem（環境変数対応）
5. readonly variable error（readonly削除）

**残作業**: 自動テスト実行のみ（Bash環境復旧待ち）

---

## 次のアクション

### 今すぐ実行可能

```bash
# Task #1: Late API パラメータ名修正（10分）
cd /Users/yuichi/AIPM/aipm_v0
vim Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py

# 行194-197を修正:
# params["fromDate"] → params["dateFrom"]
# params["toDate"] → params["dateTo"]

# 動作確認
python Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py \
  --from-date 2026-01-01 \
  --to-date 2026-01-10 \
  --platform linkedin

# コミット
git add Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py
git commit -m "fix: Correct parameter names dateFrom/dateTo in Late API script"
```

### 環境復旧後

```bash
# Task #13: Auto Migration テスト実行（30分）
cd /Users/yuichi/AIPM/aipm_v0
bash tests/test_auto_migration.sh
# 期待結果: ✓ ALL TESTS PASSED
```

### 今週中

```bash
# Task #2-4: Late API高優先度改善（5-7時間）
# N+1クエリ解決 → ページネーション → Dual ID System

# Task #16: Threads API統合（4-6時間）
# Graph API調査 → スクリプト実装 → テスト
```

---

## 補足情報

### ドキュメント参照

- **Late API Issues**: `Flow/202601/2026-01-10/late_api_script_issues_report.md` (710行)
- **Auto Migration Status**: `Flow/202601/2026-01-10/week5_phase1_integration_test_summary.md` (321行)
- **Week 8 Status**: `Flow/202601/2026-01-10/week8_phase3_improvement_report.md` (279行)
- **SNS Performance**: `Flow/202601/2026-01-10/sns_performance_analysis_20260101-0110.md` (466行)

### 関連ルール

- **並列実行**: `@.claude/rules/parallel_execution.md`
- **実行方針**: `@.claude/rules/execution_preference.md`
- **Ralph Wiggum**: `@.claude/rules/ralph_wiggum_integration.md`
- **コンテキスト管理**: `@.claude/rules/context_management.md`

---

**作成者**: Claude Code (Sonnet 4.5)
**総タスク数**: 19件
**最優先タスク**: #1（Late APIパラメータ名修正、10分）
**総推定工数**: 20-30時間 + 継続監視2-4週間
