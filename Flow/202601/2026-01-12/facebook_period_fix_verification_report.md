# Facebook期間指定機能 実装検証レポート

**実装日**: 2026-01-12
**検証者**: Claude Code
**対象スキル**: collect-facebook-performance, analyze-sns-performance-weekly

---

## 1. 実装概要

### 問題点
collect-facebook-performance スキルが常に28日間のデータを収集し、analyze-sns-performance-weekly で指定した期間（例: 2026-01-01～2026-01-11の11日間）と一致しない。

### 解決方法
Facebook Professional Dashboard の日付フィルターUIを操作し、カスタム期間を設定する機能を追加。

### 実装内容
1. **STEP 1.5 追加**: 日付フィルターUI操作手順（collect-facebook-performance SKILL.md）
2. **入力仕様変更**: since_date/until_date パラメータ追加
3. **データ構造変更**: 動的期間計算
4. **analyze-sns-performance-weekly 修正**: 期間パラメータを渡す仕様に変更

---

## 2. 実装詳細

### 2.1 STEP 1.5: 期間フィルター設定

**追加場所**: collect-facebook-performance SKILL.md (lines 137-235)

**実装内容**:
```markdown
### STEP 1.5: 期間フィルター設定（2-3分）【NEW】

**目的**: Professional Dashboardで指定期間のデータのみ取得

**Chrome MCPツール使用**:
1. navigate(url="https://www.facebook.com/professional_dashboard/profile_insights/views")
2. wait(duration=3)
3. screenshot() → 初期状態確認（28日間表示）
4. find(query="過去28日間") → 日付フィルターボタン検索
5. left_click(ref=date_button_ref) → ドロップダウン展開
6. wait(duration=1)
7. find(query="カスタム") → カスタムオプション検索
8. left_click(ref=custom_option_ref) → カスタム期間選択
9. wait(duration=1) → カレンダーUI表示待機
10. [日付選択処理]
11. find(query="適用") → 適用ボタン検索
12. left_click(ref=apply_button_ref) → フィルター適用
13. wait(duration=3) → データ再読み込み待機
14. screenshot() → フィルター適用後確認
```

**DOM構造（実機確認済み）**:
```
button "過去28日間: 12月15日 ～ 1月11日"
  → menuitem "今日"
  → menuitem "過去7日間"
  → menuitem "過去14日間"
  → menuitem "過去28日間"（デフォルト）
  → menuitem "過去60日間"
  → menuitem "過去90日間"
  → menuitem "カスタム" ← クリック
    → grid[role="grid"] カレンダーダイアログ
      → gridcell × 35（日付セル）
      → button "前月" / "翌月"
      → button "戻る" / "適用"
```

### 2.2 入力仕様変更

**変更箇所**: collect-facebook-performance SKILL.md (lines 68-71)

**変更前**:
```markdown
| **入力** | 期間（デフォルト: 過去28日間）、Chromeログインセッション |
```

**変更後**:
```markdown
| **入力** | 開始日（since_date: YYYY-MM-DD）、終了日（until_date: YYYY-MM-DD）、Chromeログインセッション |
| **注意** | since_date/until_date未指定時はデフォルト28日間 |
```

### 2.3 データ構造変更

**変更箇所**: collect-facebook-performance SKILL.md (lines 636-637)

**変更前**:
```json
"period": "2025-12-15 ~ 2026-01-11",
"period_days": 28,
```

**変更後**:
```json
"period": "{since_date} ~ {until_date}",
"period_days": "{計算された日数: (until - since).days + 1}",
```

### 2.4 analyze-sns-performance-weekly 修正

**変更箇所**: analyze-sns-performance-weekly SKILL.md (lines 101-130)

**追加内容**:
```python
facebook_result = Task(
    description="Facebook収集",
    prompt=f"""
    **期間指定（重要）**:
    - 開始日（since_date）: {WEEK_AGO}
    - 終了日（until_date）: {TODAY}

    **実行手順**:
    1. STEP 1.5 で日付フィルターを設定
    2. 上記期間のデータのみ収集
    3. 28日間データではなく、指定期間データを返すこと
    """,
    timeout=2100000  # 35分（期間設定+5分）
)
```

---

## 3. 実機テスト結果

### 3.1 テスト環境
- **実行日**: 2026-01-12
- **対象期間**: 2026-01-01 ～ 2026-01-11（11日間）
- **ブラウザ**: Chrome with Claude MCP
- **Facebook Tab ID**: 1816165795

### 3.2 STEP 1.5 実行ログ

#### ステップ1: Professional Dashboard遷移
```
✅ navigate(url="https://www.facebook.com/.../views")
✅ wait(duration=3)
✅ screenshot() → 初期状態確認
   表示: "過去28日間: 12月15日～1月11日"
```

#### ステップ2: 日付フィルターボタンクリック
```
✅ find(query="過去28日間 12月15日 1月11日")
   → ref_65: button "過去28日間: 12月15日 ～ 1月11日"
✅ left_click(ref=ref_65)
✅ wait(duration=1)
✅ screenshot() → ドロップダウン表示確認
```

#### ステップ3: カスタムオプション選択
```
✅ find(query="カスタム")
   → ref_202: menuitem "カスタム"
✅ left_click(ref=ref_202)
✅ wait(duration=1)
✅ screenshot() → カレンダーダイアログ表示確認
   表示: "2026年1月" カレンダー
```

#### ステップ4: 日付選択
```
✅ find(query="1日 gridcell")
   → ref_227: gridcell "2026年1月1日木曜日"
✅ left_click(ref=ref_227) → 開始日選択
✅ wait(duration=1)

✅ find(query="11日 gridcell")
   → ref_259: gridcell "2026年1月11日日曜日"
✅ left_click(ref=ref_259) → 終了日選択
✅ wait(duration=1)
✅ screenshot() → 選択確認
   表示: 1日～11日が青色ハイライト
   表示: "2026/01/01 - 2026/01/11"
```

#### ステップ5: 適用ボタンクリック
```
✅ find(query="適用")
   → ref_328: button "適用"
✅ left_click(ref=ref_328)
✅ wait(duration=3) → データ再読み込み待機
✅ screenshot() → フィルター適用後確認
```

### 3.3 検証結果

#### URL確認
```
変更前: https://www.facebook.com/professional_dashboard/profile_insights/views
変更後: https://www.facebook.com/professional_dashboard/profile_insights/views/?date_range=CUSTOM&start_date=2026-01-01&end_date=2026-01-11
```
✅ URLパラメータが正しく設定されている

#### UI表示確認
```
日付フィルターボタン: "カスタム: 1月1日～1月11日" ✅
グラフX軸: 1月1日～1月11日の範囲表示 ✅
```

#### データ確認（11日間）
| 指標 | 28日間（変更前） | 11日間（変更後） | 変化 |
|------|-----------------|-----------------|------|
| **総閲覧数** | 304,534回 | **223,804回** | -26.5% |
| **閲覧者** | 92,133人 | **82,205人** | -10.8% |
| **3秒再生** | 1,835回 | **61回** | -96.7% |
| **1分再生** | 0回 | **0回** | - |

✅ データが11日間の期間に正しく更新されている

#### コンテンツタイプ別（11日間）
| タイプ | 28日間 | 11日間 | 変化 |
|--------|--------|--------|------|
| **写真** | 71.8% | **66.1%** | -5.7pt |
| **テキスト** | 23.6% | **32.2%** | +8.6pt |
| **複数写真** | 2.6% | **1.4%** | -1.2pt |
| **リール** | 1.9% | **0.1%** | -1.8pt |

✅ コンテンツタイプ別の比率も期間に応じて変化

---

## 4. 技術的な課題と解決策

### 4.1 課題1: 要素参照の無効化

**問題**: ドロップダウンメニュー展開後、ref_202が無効になる

**原因**: DOMの再レンダリングによる要素の再生成

**解決策**:
- screenshot()で状態確認後、find()で要素を再検索
- 各クリック操作後にwait()を挿入して安定化

### 4.2 課題2: カレンダーUI操作の複雑性

**問題**: 日付セルのrefが動的に変化

**原因**: カレンダーの月切り替えでgridcellが再生成される

**解決策**:
- find(query="N日 gridcell")で毎回検索
- gridcell要素のaria-labelを利用して正確な日付を特定

### 4.3 課題3: データ再読み込みの待機時間

**問題**: 適用ボタンクリック後、即座にデータが更新されない

**解決策**:
- wait(duration=3)で十分な待機時間を確保
- URLパラメータの変化を確認してから次のステップへ

---

## 5. 制約事項

### 5.1 Facebook Professional Dashboard制約
- **最大期間**: 90日間
- **最小期間**: 1日間
- **対象**: 過去データのみ（未来日付は指定不可）

### 5.2 Chrome MCP依存
- Facebook Professional Dashboardはログイン必須
- Chrome MCPの接続が必須
- ブラウザUIの変更に依存（Facebookが仕様変更した場合は修正必要）

### 5.3 実行時間
- STEP 1.5追加により、従来の30分から**35分**に延長
- UI操作による追加時間: 2-3分

---

## 6. 今後の改善提案

### 6.1 フォールバック機能
```python
try:
    # STEP 1.5: カスタム期間設定
    set_custom_date_filter(since_date, until_date)
except DateFilterError:
    logger.warning("期間フィルター設定失敗、28日間デフォルトで継続")
    # STEP 3以降を続行（28日間データで）
```

### 6.2 エラーハンドリング強化
| エラーケース | 現在の対応 | 改善案 |
|------------|----------|--------|
| 日付ボタンが見つからない | スクリーンショット撮影 | 3回リトライ後、手動確認依頼 |
| カスタムオプションがない | なし | プリセット（7日/60日）で代替 |
| カレンダーUI操作失敗 | なし | JavaScript tool で直接DOM操作 |
| フィルター適用失敗 | なし | 3回リトライ後、28日間で継続 |

### 6.3 パフォーマンス最適化
- スクリーンショット撮影回数を削減（デバッグ時のみ）
- wait()の時間を動的に調整（read_page()でDOM確認）

### 6.4 ドキュメント改善
- UI構造のスクリーンショット付きドキュメント作成
- トラブルシューティングガイド追加
- Facebook UIバージョン情報の記録

---

## 7. 結論

### 7.1 実装成功
✅ Facebook Professional DashboardのカスタムDuration設定機能を正常に実装
✅ 指定期間（2026-01-01～2026-01-11）でのデータ収集を確認
✅ 28日間固定の問題を解消
✅ Late APIとFacebookで期間を統一可能に

### 7.2 検証結果
- **UI操作**: 14ステップすべて成功
- **データ整合性**: 期間に応じたデータ変化を確認
- **URL パラメータ**: `date_range=CUSTOM&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` 正常
- **スキル統合**: analyze-sns-performance-weekly からの呼び出し成功

### 7.3 本番利用可能
本実装は**本番環境で利用可能**な状態です。

**推奨される利用方法**:
```bash
# analyze-sns-performance-weekly スキル実行時
--start-date 2026-01-01 --end-date 2026-01-11
```

これにより、Late API（LinkedIn, X, Threads）とFacebook Professional Dashboardで**同一期間**のデータを収集し、正確な週次分析が可能になります。

---

## 8. 関連ファイル

### 8.1 修正ファイル
- `/Users/yuichi/agentpm/.claude/skills/collect-facebook-performance/SKILL.md`
  - STEP 1.5 追加（lines 137-235）
  - 入力仕様変更（lines 68-71）
  - データ構造変更（lines 636-637）
  - 更新履歴追加（lines 936-944）

- `/Users/yuichi/agentpm/.claude/skills/analyze-sns-performance-weekly/SKILL.md`
  - Facebook収集タスク修正（lines 101-130）
  - スキル引数セクション追加（lines 1167-1188）
  - STEP 1パラメータ設定修正（lines 42-63）

### 8.2 検証ファイル
- `/Users/yuichi/.claude/plans/stateless-tinkering-karp.md` - 実装計画（543行）
- `/Users/yuichi/agentpm/Flow/202601/2026-01-12/facebook_period_fix_verification_report.md` - 本レポート

### 8.3 スクリーンショット
- `ss_0078knd2d`: 初期状態（28日間表示、ドロップダウンオープン）
- `ss_9744afm5b`: Facebookホームに戻った状態
- `ss_67027ep59`: Professional Dashboard再遷移後
- `ss_57944advt`: ドロップダウンメニュー展開状態
- `ss_1795b1sgp`: カレンダーダイアログ（2026年1月）
- `ss_5587grik5`: 日付選択完了（1日～11日ハイライト）
- `ss_1614j4122`: フィルター適用後（カスタム期間確定）

---

**検証完了日**: 2026-01-12
**検証者**: Claude Code
**ステータス**: ✅ 本番利用可能
