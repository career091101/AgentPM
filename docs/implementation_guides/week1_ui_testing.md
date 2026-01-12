# UI Testing Rules - Chrome拡張使用ガイド

## 概要

Chrome拡張MCP（Model Context Protocol）ツールを使用したUI自動テストのベストプラクティスとルールを定義します。

## 基本方針

- **自動化優先**: 手動UIテストは最小限に、自動検証を最大化
- **並列実行**: 複数シナリオを並列実行して時間短縮
- **証拠記録**: すべてのUIテスト結果をスクリーンショット＋レポートで記録
- **品質ゲート**: 70点以上で統合OK、60点未満でUI改善必須

## Chrome拡張MCPツール一覧

| ツール名 | 用途 | 頻度 |
|---------|------|------|
| `tabs_context_mcp` | タブグループ情報取得 | 必須（初回1回） |
| `tabs_create_mcp` | 新規タブ作成 | 高 |
| `navigate` | ページ遷移 | 高 |
| `read_page` | ページ内容読み取り（アクセシビリティツリー） | 高 |
| `find` | 要素検索（自然言語クエリ） | 中 |
| `form_input` | フォーム入力 | 中 |
| `computer` | スクリーンショット、クリック、キーボード操作 | 高 |
| `resize_window` | ウィンドウサイズ変更 | 中（レスポンシブテスト時） |
| `javascript_tool` | JavaScript実行 | 中（パフォーマンス測定時） |
| `get_page_text` | テキスト抽出 | 低 |
| `gif_creator` | GIF録画 | 低（デモ作成時のみ） |
| `upload_image` | 画像アップロード | 低 |

## 実行フロー（標準パターン）

### 1. テスト環境セットアップ

```python
# STEP 1: Chrome拡張接続確認
tabs_info = tabs_context_mcp(createIfEmpty=True)

# STEP 2: 新規タブ作成（隔離環境）
tab_id = tabs_create_mcp()

# STEP 3: ウィンドウサイズ設定（デスクトップ検証用）
resize_window(tabId=tab_id, width=1920, height=1080)
```

### 2. ページ遷移＋初期スクリーンショット

```python
# STEP 4: テスト対象URLへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/login")

# STEP 5: 初期表示のスクリーンショット取得
screenshot_id = computer(tabId=tab_id, action="screenshot")
# → ss_abc123 のようなIDが返される
```

### 3. UIインタラクション

```python
# STEP 6: 要素検索（自然言語クエリ）
find_result = find(tabId=tab_id, query="email input field")
# → ref_1, ref_2 などの参照IDが返される

# STEP 7: フォーム入力
form_input(tabId=tab_id, ref="ref_1", value="test@example.com")
form_input(tabId=tab_id, ref="ref_2", value="password123")

# STEP 8: ボタンクリック
computer(tabId=tab_id, action="left_click", ref="ref_3")

# STEP 9: 2秒待機（認証処理完了まで）
computer(tabId=tab_id, action="wait", duration=2)

# STEP 10: 結果のスクリーンショット
screenshot_id_2 = computer(tabId=tab_id, action="screenshot")
```

### 4. 評価＋レポート生成

```python
# STEP 11: ページ内容読み取り（アクセシビリティツリー）
page_content = read_page(tabId=tab_id, filter="interactive", depth=10)

# STEP 12: LLM（Claude自身）で視覚的評価
# スクリーンショットを見ながら、レイアウト、配色、タイポグラフィを評価

# STEP 13: スコア計算
visual_quality_score = calculate_visual_score(screenshot_id_2)
accessibility_score = calculate_accessibility_score(page_content)
# ... 他の観点も同様

# STEP 14: レポート生成
generate_report(scores, screenshots, issues, recommendations)
```

## ベストプラクティス

### 1. エラーハンドリング

#### Chrome拡張接続エラー

```python
try:
    tabs_info = tabs_context_mcp(createIfEmpty=True)
except Exception as e:
    if "401" in str(e) or "authentication" in str(e).lower():
        print("⚠️ Chrome拡張認証エラー: OAuth tokenが期限切れです")
        print("対処: Chrome拡張を再起動してください")
        # UI検証をスキップ
        return skip_ui_verification()
    else:
        # 3回リトライ
        for i in range(3):
            time.sleep(2)
            try:
                tabs_info = tabs_context_mcp(createIfEmpty=True)
                break
            except:
                if i == 2:
                    return skip_ui_verification()
```

#### タイムアウトエラー

```python
# タイムアウト付きでページ遷移
try:
    navigate(tabId=tab_id, url=target_url)
    # 5秒待機してページ読み込み完了確認
    computer(tabId=tab_id, action="wait", duration=5)
except TimeoutError:
    print("⚠️ ページ読み込みタイムアウト（5秒超過）")
    # 10秒に延長して再試行
    navigate(tabId=tab_id, url=target_url)
    computer(tabId=tab_id, action="wait", duration=10)
```

#### 要素検出エラー

```python
# 要素が見つからない場合
find_result = find(tabId=tab_id, query="submit button")
if not find_result or "error" in find_result.lower():
    print("⚠️ 要素が見つかりません: submit button")
    # 5秒待機後に再試行
    computer(tabId=tab_id, action="wait", duration=5)
    find_result = find(tabId=tab_id, query="submit button")

    if not find_result:
        # read_page で全要素を取得して目視確認
        all_elements = read_page(tabId=tab_id, filter="all", depth=15)
        print(f"ℹ️ ページ内の全要素:\n{all_elements}")
        # このシナリオはスキップして次へ
        return skip_scenario()
```

### 2. スクリーンショット管理

```markdown
**命名規則**:
- `{scenario_id}_{step}.jpeg` - 例: `login_flow_initial.jpeg`, `login_flow_success.jpeg`

**保存先**:
- `Flow/YYYYMM/YYYY-MM-DD/ui_verification/screenshots/`

**品質設定**:
- フォーマット: JPEG
- 品質: 85（デフォルト）
- サイズ: ウィンドウサイズに依存
```

**実装例**:

```python
# スクリーンショット取得＋保存
screenshot_id = computer(tabId=tab_id, action="screenshot")

# スクリーンショットIDをレポートに記録
screenshots[scenario_id] = {
    "initial": screenshot_id_1,
    "interaction": screenshot_id_2,
    "result": screenshot_id_3
}

# レポートMarkdownに埋め込み
report_md += f"![Initial State]({screenshot_id_1})\n"
```

### 3. レスポンシブデザインテスト

```python
# 3つのブレークポイントでテスト
breakpoints = [
    {"name": "mobile", "width": 375, "height": 667},   # iPhone SE
    {"name": "tablet", "width": 768, "height": 1024},  # iPad
    {"name": "desktop", "width": 1920, "height": 1080}
]

screenshots = {}

for bp in breakpoints:
    # ウィンドウサイズ変更
    resize_window(tabId=tab_id, width=bp["width"], height=bp["height"])

    # 2秒待機（レンダリング完了まで）
    computer(tabId=tab_id, action="wait", duration=2)

    # スクリーンショット取得
    screenshot_id = computer(tabId=tab_id, action="screenshot")
    screenshots[bp["name"]] = screenshot_id

    # LLMで視覚的評価
    evaluate_responsive_layout(screenshot_id, bp["name"])
```

### 4. パフォーマンスメトリクス取得

```python
# JavaScript実行でパフォーマンスデータ取得
perf_script = """
const perfData = performance.getEntriesByType('navigation')[0];
const metrics = {
  domContentLoaded: perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart,
  loadComplete: perfData.loadEventEnd - perfData.loadEventStart,
  firstPaint: performance.getEntriesByType('paint')[0].startTime
};
metrics;
"""

perf_result = javascript_tool(tabId=tab_id, text=perf_script)

# 結果の解析
perf_data = json.loads(perf_result)
page_load_time = perf_data["loadComplete"] / 1000  # ミリ秒 → 秒

# スコア計算
if page_load_time <= 2:
    page_load_score = 10
elif page_load_time <= 3:
    page_load_score = 7
elif page_load_time <= 5:
    page_load_score = 4
else:
    page_load_score = 0
```

### 5. アクセシビリティチェック

```python
# ARIA属性カバレッジ確認
aria_script = """
const ariaCheck = {
  buttons: document.querySelectorAll('button[aria-label]').length,
  totalButtons: document.querySelectorAll('button').length,
  interactiveElements: document.querySelectorAll('[role]').length
};
ariaCheck;
"""

aria_result = javascript_tool(tabId=tab_id, text=aria_script)
aria_data = json.loads(aria_result)

# ARIA属性カバレッジ計算
aria_coverage = aria_data["buttons"] / aria_data["totalButtons"] if aria_data["totalButtons"] > 0 else 0

# スコア計算
if aria_coverage >= 1.0:
    aria_score = 8
elif aria_coverage >= 0.8:
    aria_score = 6
elif aria_coverage >= 0.5:
    aria_score = 3
else:
    aria_score = 0
```

## 禁止事項

### 1. JavaScriptアラート・モーダルダイアログのトリガー

```markdown
❌ **禁止**: JavaScript `alert()`, `confirm()`, `prompt()` を発生させる操作

**理由**: ブラウザモーダルダイアログはすべてのブラウザイベントをブロックし、
         Chrome拡張が応答不能になる。

**対処**:
- アラートが発生する可能性のあるボタン（削除、確認等）はクリックしない
- デバッグには `console.log()` を使用し、`read_console_messages` で読み取る
```

### 2. 無限ループ・ラビットホール

```markdown
❌ **禁止**: 同じ操作を2-3回以上繰り返す

**理由**: 失敗する操作を繰り返してもコストと時間の無駄。

**対処**:
- 2回失敗したら即座にユーザーに報告
- 別のアプローチを試すか、スキップ
```

### 3. タブIDの再利用（セッション跨ぎ）

```markdown
❌ **禁止**: 前回セッションのタブIDを使用

**理由**: タブIDはセッション固有。別セッションのIDは無効。

**対処**:
- 毎回 `tabs_context_mcp()` で最新タブ情報を取得
- 新規タブが必要な場合は `tabs_create_mcp()` を使用
```

## トラブルシューティング

### 問題1: "Failed to find element: 401 authentication_error"

**原因**: OAuth tokenが期限切れ

**解決策**:
1. Chrome in Chrome拡張を再起動
2. `tabs_context_mcp(createIfEmpty=True)` を再実行
3. それでも失敗する場合はUI検証をスキップ

### 問題2: スクリーンショットが空白（真っ白）

**原因**: ページ読み込みが完了していない

**解決策**:
```python
# スクリーンショット前に2-5秒待機
computer(tabId=tab_id, action="wait", duration=3)
screenshot_id = computer(tabId=tab_id, action="screenshot")
```

### 問題3: 要素が見つからない（find/read_pageが空）

**原因**: ページがまだレンダリング中 or 要素が動的生成される

**解決策**:
```python
# 5秒待機後に再試行
computer(tabId=tab_id, action="wait", duration=5)
find_result = find(tabId=tab_id, query="submit button")

# それでも見つからない場合は read_page で全要素確認
if not find_result:
    all_elements = read_page(tabId=tab_id, filter="all", depth=15)
    # 手動で要素を特定
```

### 問題4: JavaScript実行が失敗する

**原因**: ページのCSP（Content Security Policy）制限

**解決策**:
- CSP制限があるページではJavaScript実行不可
- パフォーマンスメトリクスが取得できない場合はスキップ

## 実行時間の目安

| 操作 | 標準時間 | 最大時間 |
|------|---------|---------|
| タブ作成＋ページ遷移 | 5秒 | 10秒 |
| スクリーンショット取得 | 2秒 | 5秒 |
| フォーム入力 | 1秒 | 3秒 |
| クリック操作 | 1秒 | 3秒 |
| JavaScript実行 | 2秒 | 5秒 |
| レスポンシブテスト（3サイズ） | 30秒 | 60秒 |
| 1シナリオ全体 | 30-60秒 | 120秒 |
| 5シナリオ全体 | 3-5分 | 10分 |

## 品質ゲート

### 統合判定基準

| 総合スコア | 判定 | 対応 |
|----------|------|------|
| 70点以上 | ✅ 統合OK（高品質） | ドキュメントと統合してStockへ移動 |
| 60-69点 | ⚠️ 条件付き統合OK | 改善推奨項目を記録、統合は実施 |
| 60点未満 | ❌ 統合NG（UI改善必須） | レポートの推奨事項を実装後、再検証 |

### スコア配分

- **視覚品質**: 25点（レイアウト10 + 配色8 + タイポグラフィ7）
- **レスポンス速度**: 20点（ページ読み込み10 + インタラクション6 + アニメーション4）
- **アクセシビリティ**: 20点（ARIA8 + キーボード8 + セマンティックHTML4）
- **ユーザビリティ**: 20点（ナビゲーション8 + エラーハンドリング6 + フィードバック6）
- **モバイル対応**: 15点（レスポンシブ8 + タッチターゲット4 + 最適化3）

**合計**: 100点満点

## 参照

- @.claude/agents/ui-verification-agent.md - UI Verification Agent仕様書（502行）
- @.claude/skills/verify-ui-quality/SKILL.md - UI検証スキル
- @.claude/config/ui_verification.json - 検証シナリオ定義
- @.claude/skills/orchestrate-review-loop/SKILL.md - フィードバックループ統合（Phase 2.5）
- @.claude/rules/parallel_execution.md - 並列実行ガイドライン

## 更新履歴

- **2026-01-03**: 初版作成（Week 1 完了時）
- **項目追加予定**: パフォーマンスベンチマーク（Lighthouse統合）、クロスブラウザテスト
