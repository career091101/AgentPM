# Corporate_Product_Research 100件達成システムプロンプト

**目標**: リクルート製品100件のケーススタディを完成させる（現在25件 → 目標100件）
**実行方式**: 5エージェント並列 × 複数バッチ、完全自動実行
**期間**: 2-3ヶ月（15バッチ想定）

---

## 1. 現状と目標

### 現状（25件完了）
- **SUCCESS**: 14件（TIER2: 6件、TIER3: 3件、TIER5: 5件）
- **FAILURE**: 11件（TIER6: 10件、TIER8: 1件）

### 目標（100件）
- **SUCCESS**: 60件（TIER1: 10件、TIER2: 15件、TIER3: 15件、TIER4: 10件、TIER5: 10件）
- **FAILURE**: 40件（TIER6: 15件、TIER7: 10件、TIER8: 15件）

### 不足分（75件）
- **SUCCESS**: 46件
  - TIER1_GLOBAL_MA: 10件（Indeed、Glassdoor等グローバルM&A）
  - TIER2_MEGA_HIT: 9件（じゃらん、ホットペッパーグルメ、リクナビ、タウンワーク等）
  - TIER3_SAAS: 12件（Airシリーズ、SaaS製品）
  - TIER4_DOMESTIC_MA: 10件（国内M&A事例）
  - TIER5_NEW_BUSINESS: 5件（新規事業成功）
- **FAILURE**: 29件
  - TIER6_CLEAR_WITHDRAWAL: 5件（明確な撤退）
  - TIER7_MA_FAILURE: 10件（M&A統合失敗）
  - TIER8_STRATEGIC_EXIT: 14件（戦略的撤退・MBO）

---

## 2. バッチ実行戦略

### Phase構成（15バッチ × 5件 = 75件）

#### Phase 1: TIER1 GLOBAL_MA（2バッチ、10件）
- バッチ1: Indeed、Glassdoor、Indeed Prime、Hired、Chandler Macleod
- バッチ2: Staffmark、RGF Staffing、Advantage Resourcing、USG People、Atimi Software

#### Phase 2: TIER2 MEGA_HIT追加（2バッチ、9件）
- バッチ3: じゃらん、ホットペッパーグルメ、リクナビ、タウンワーク、フロムエー
- バッチ4: はたらいく、リクナビ進学、受験サプリ、タウンワークWeb版

#### Phase 3: TIER3 SAAS（3バッチ、12件）
- バッチ5: Airシフト、Quipper School、スーモカウンター、Airワーク採用管理、AirID
- バッチ6: Airウェイト、Airメイト、Studyplus for School、リクルートドクターズキャリア、ナースエージェント
- バッチ7: 薬キャリエージェント、HELPMAN JAPAN

#### Phase 4: TIER4 DOMESTIC_MA（2バッチ、10件）
- バッチ8: ニジボックス、メディアテクノロジーラボ、キャスティングロード、クロスエイジ、アールストーン
- バッチ9: リクルートジョブズメディカル、リクルート住まいカンパニー、リクルートライフスタイル、リクルートキャリア、リクルートマネジメントソリューションズ

#### Phase 5: TIER5 NEW_BUSINESS追加（1バッチ、5件）
- バッチ10: リクルート進学総研、SUUMO B2B、リクルートカード、リクルートジョブズ、リクルート住まいカンパニー

#### Phase 6: TIER6 CLEAR_WITHDRAWAL追加（1バッチ、5件）
- バッチ11: ATND、ホットペッパービューティーコスメ、フロムエー紙版、ガテン、リクルートブック就職版

#### Phase 7: TIER7 MA_FAILURE（2バッチ、10件）
- バッチ12: Quipper Video統合課題、USG People統合課題、Chandler Macleod統合課題、Advantage Resourcing統合課題、RGF Staffing統合課題
- バッチ13: 国内M&A統合課題（5件）

#### Phase 8: TIER8 STRATEGIC_EXIT追加（2バッチ、14件）
- バッチ14: リクルートエージェント旧体制、フロムエーナビ紙版、リクルートコスモス、住まいの窓口、リクルートゼクシィなび
- バッチ15: タウンワーク社、フロムエー社、リクルートテクノロジーズ、リクルートHRマーケティング、リクルートエグゼクティブエージェント、リクルート事業構造再編事例（4件）

---

## 3. エージェント並列実行の指示

### システムプロンプト（トリガーワード: "100件達成実行"）

```
## 実行指示

ユーザーが "100件達成実行 Phase X バッチY" と入力した場合、以下を自動実行：

### ステップ1: 候補リスト作成（1エージェント）

以下のソースからPhase X バッチYの5製品を特定：
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/candidate_list.md`
- リクルートHD IR資料（WebFetch）
- リクルート公式サイト（WebFetch）

### ステップ2: 5エージェント並列起動

以下の5エージェントを**1つのメッセージで並列起動**：

```python
# 疑似コード（実際はTask toolを5回呼び出し）
agents = []
for i, product in enumerate(batch_products, 1):
    agent = Task(
        description=f"ケーススタディ作成: {product}",
        prompt=f"""
{product}のケーススタディを作成してください。

## 必須タスク

1. **情報収集**（WebFetch/WebSearch）:
   - Tier 1ソース: リクルートHD IR資料、公式プレスリリース
   - Tier 2ソース: 日経、東洋経済、ダイヤモンド
   - Tier 3ソース: 書籍、Wikipedia
   - 最低3ソース、推奨10ソース以上

2. **Frontmatter作成**:
   - テンプレート参照: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_templates/corporate_product_template.md`
   - 必須フィールド全て記載（id, title, product, quality, validation_data等）
   - sources_count = primary_sources配列の長さ

3. **セクション作成**（全10セクション必須）:
   - 1. 基本情報
   - 2. 製品開発ストーリー（2.1 課題発見、2.2 CPF検証、2.3 PSF検証）
   - 3. ピボット/失敗経験（失敗事例の場合: 3.3 リクルート撤退基準の検証）
   - 4. 成長戦略（4.4 リクルート資産の活用）
   - 5. M&A戦略（M&A事例のみ）
   - 6. 使用ツール・サービス
   - 7. 成功/失敗要因分析
   - 8. orchestrate-phase1への示唆（8.1-8.4の4サブセクション）
   - 9. 他業界適用性
   - 10. ファクトチェック結果

4. **CPF/PSF検証データ**:
   - 成功パターン参照: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_index/success_patterns.md`
   - 失敗パターン参照: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_index/failure_patterns.md`
   - CPF: interview_count, problem_commonality, wtp_confirmed必須
   - PSF: ten_x_axes 2軸以上、mvp_type、competitive_advantage必須

5. **PASS基準クリア**:
   - ソース数 >= 3（推奨10以上）
   - ファクトチェック: 創業年・M&A年・撤退年を2ソース以上で確認
   - CPF検証データ3項目記載
   - PSF検証データ2軸以上記載

6. **ファイル保存**:
   - SUCCESS事例: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/documents/SUCCESS/TIER{{X}}_{{CATEGORY}}/CORP_S{{番号}}_{{product_slug}}.md`
   - FAILURE事例: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/documents/FAILURE/TIER{{X}}_{{CATEGORY}}/CORP_F{{番号}}_{{product_slug}}.md`

7. **品質自己チェック**:
   - テンプレート準拠度チェック（Frontmatter、10セクション）
   - PASS基準4項目チェック
   - 不足があれば自己修正

## 重要: 完全自動実行

- Human介入不要で完了させる
- エラー発生時は代替ソース検索、推測でデータ補完
- 最低限のPASS基準を満たすまで自己修正
- 完了レポートを標準出力に表示

## ID採番ルール

既存の最大ID + 1を使用:
- SUCCESS最大ID: CORP_S025 → 次はCORP_S026から
- FAILURE最大ID: CORP_F015 → 次はCORP_F016から
        """,
        subagent_type="general-purpose",
        model="sonnet"
    )
    agents.append(agent)
```

### ステップ3: 完了確認とmaster_index更新

全5エージェント完了後、1エージェントで以下を実行：

```
1. 新規5ファイルの品質チェック（PASS基準4項目）
2. master_index.mdに5件追加
3. research_progress.mdを更新（25→30件等）
4. バッチ完了レポート作成
```

---

## 4. 品質保証基準（自動チェック）

### PASS基準（必須）

| 項目 | 基準 | 確認方法 |
|------|------|---------|
| ソース数 | 3ソース以上 | `quality.sources_count >= 3` |
| ファクトチェック | 創業年・M&A年・撤退年を2ソース確認 | セクション10 |
| CPF検証データ | interview_count, problem_commonality, wtp_confirmed | `validation_data.cpf` |
| PSF検証データ | ten_x_axes 2軸以上、mvp_type、competitive_advantage | `validation_data.psf` |

### テンプレート準拠度（必須）

- Frontmatter必須フィールド: id, title, category, tier, type, version, created_at, updated_at, tags, product, quality, validation_data
- 必須セクション10個全て記載
- tier値が定義済みティアに含まれる
- type値が"success"または"failure"

---

## 5. 実行コマンド例

### Phase 1 バッチ1実行（TIER1 GLOBAL_MA 5件）

```
100件達成実行 Phase 1 バッチ1

対象製品:
1. Indeed
2. Glassdoor
3. Indeed Prime
4. Hired
5. Chandler Macleod

TIER: TIER1_GLOBAL_MA
Category: SUCCESS
```

### Phase 6 バッチ11実行（TIER6 CLEAR_WITHDRAWAL 5件）

```
100件達成実行 Phase 6 バッチ11

対象製品:
1. ATND
2. ホットペッパービューティーコスメ
3. フロムエー紙版
4. ガテン
5. リクルートブック就職版

TIER: TIER6_CLEAR_WITHDRAWAL
Category: FAILURE
```

---

## 6. バッチ実行チェックリスト

各バッチ完了時に以下を確認：

### 自動確認項目
- [ ] 5ファイル全て作成完了
- [ ] PASS基準4項目全て達成
- [ ] テンプレート準拠度95%以上
- [ ] master_index.md更新完了
- [ ] research_progress.md更新完了

### 手動確認項目（オプション）
- [ ] ソース品質（Tier 1ソース1件以上含む）
- [ ] CPF/PSFパターン適用の妥当性
- [ ] orchestrate-phase1への示唆の具体性

---

## 7. エラーハンドリング

### ソース不足の場合
1. WebSearchで追加ソース検索（検索キーワード: "リクルート {製品名} IR", "{製品名} リクルート 撤退"）
2. 関連製品のソースから類推
3. 最低3ソース確保できない場合、WARNステータスで保存（後で手動補完）

### データ不足の場合（CPF/PSF）
1. 類似製品のパターンを参照して推測
2. "推測値"として記載し、`validation_data.cpf.validation_method: "類推"`と明記
3. 最低限のフィールドを埋めてWARNステータス

### M&A事例でM&A情報不足の場合
1. IR資料で買収年・買収額を再検索
2. 日経等でM&A発表記事を検索
3. 不明な場合は`acquisition.occurred: false`として保存

---

## 8. 進捗管理

### バッチ実行記録

| Phase | バッチ | 件数 | 完了日 | 累計 | 達成率 |
|-------|-------|------|--------|------|--------|
| 0 | - | 25 | 2025-01-29 | 25 | 25% |
| 1 | 1 | 5 | - | 30 | 30% |
| 1 | 2 | 5 | - | 35 | 35% |
| 2 | 3 | 5 | - | 40 | 40% |
| ... | ... | ... | ... | ... | ... |
| 8 | 15 | 5 | - | 100 | 100% |

### マイルストーン

- **30件達成** (Phase 1完了): TIER1 GLOBAL_MA完成
- **50件達成** (Phase 3完了): TIER3 SAAS完成、全体50%突破
- **75件達成** (Phase 6完了): FAILURE事例大幅拡充
- **100件達成** (Phase 8完了): プロジェクト完遂 🎉

---

## 9. 最終品質監査（100件達成時）

全100件完成後、以下の統合品質チェックを実施：

### 統計検証
- SUCCESS 60件、FAILURE 40件の比率達成
- TIER別分布が目標と一致
- 平均ソース数10件以上維持
- PASS基準達成率80%以上

### パターン分析更新
- success_patterns.md更新（14事例→60事例）
- failure_patterns.md更新（11事例→40事例）
- CPF/PSFパターンの統計的検証

### 最終レポート作成
- 100件統合品質レポート
- ベストプラクティス集（TOP10事例）
- orchestrate-phase1統合ガイド

---

## 10. 参照ドキュメント

### テンプレート・基準
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_templates/corporate_product_template.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_templates/withdrawal_criteria.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/README.md`

### パターン分析
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_index/success_patterns.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_index/failure_patterns.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/analysis/cpf_patterns/`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/analysis/psf_patterns/`

### 品質レポート
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/analysis/quality_reports/quality_report_20250129.md`

### 進捗管理
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/_index/master_index.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Corporate_Product_Research/research_progress.md`

---

## 11. 実装ルール

### エージェント並列実行の必須事項

1. **1メッセージで5エージェント起動**: 5つのTask tool呼び出しを1つのメッセージに含める
2. **完全自動実行**: prompt内に"自動実行で完了させてください"と明記
3. **エラー時の自己修正**: "エラー発生時は代替手段で情報収集し、最低PASS基準を満たすまで自己修正"と指示
4. **Human介入禁止**: "Human介入不要"と明記

### モデル選択

- **ケーススタディ作成**: `model="sonnet"` (高品質が必要)
- **品質チェック**: `model="haiku"` (高速処理)
- **統合レポート**: `model="sonnet"` (分析力が必要)

---

## 12. 成功基準

### バッチ成功基準
- 5ファイル全て作成完了
- PASS基準達成率100%（5/5件）
- 平均ソース数10件以上
- エラー0件で完了

### プロジェクト成功基準（100件達成時）
- 総件数100件達成（SUCCESS 60件、FAILURE 40件）
- TIER別分布が目標と一致（±2件の誤差許容）
- 全体PASS基準達成率80%以上
- 平均ソース数10件以上維持
- テンプレート準拠度95%以上

---

## 実行開始コマンド

```
100件達成実行 Phase 1 バッチ1
```

このコマンドで、5エージェント並列実行が自動開始されます。

---

**作成日**: 2025-01-29
**バージョン**: 1.0
**最終更新**: 2025-01-29
