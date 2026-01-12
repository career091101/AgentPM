# UIテスト検証シナリオ実装ガイド

**作成日**: 2026-01-09
**対象シナリオ**: 5パターン（ログイン、フォーム、ページ遷移、Ajax、エラーハンドリング）
**実行時間**: 約10分（並列実行時）
**品質ゲート**: 70点以上で統合OK

---

## 概要

Chrome拡張MCP（Model Context Protocol）ツールを使用したUIテスト検証シナリオの実装ガイド。各シナリオは段階的にテストケースを実行し、検証結果をスコア形式で記録します。

**参照ファイル**: `ui_verification_scenarios.json`

---

## 実行フロー

### Phase 1: 環境セットアップ（3分）

#### Step 1-1: Chrome拡張接続確認

```python
# STEP 1: Chrome拡張接続確認
tabs_info = tabs_context_mcp(createIfEmpty=True)

# 成功判定: tabs_info に tab_id と group_info が含まれている
if "tab_id" not in tabs_info or "group_info" not in tabs_info:
    print("❌ Chrome拡張接続失敗")
    # 対処: Chrome拡張を再起動
    return handle_connection_error()

print(f"✅ Chrome拡張接続成功: {tabs_info}")
```

#### Step 1-2: テスト環境準備

```python
# STEP 2: テストデータの初期化
test_setup = {
    "test_account": {
        "email": "test@example.com",
        "password": "testpass123"
    },
    "environment": {
        "base_url": "http://localhost:3000",
        "server_port": 3000
    },
    "browser": {
        "width": 1920,
        "height": 1080,
        "user_agent": "default"
    }
}

# STEP 3: 新規テストタブ作成
tab_id = tabs_create_mcp()
print(f"✅ テストタブ作成: {tab_id}")

# STEP 4: ウィンドウサイズ設定
resize_window(
    tabId=tab_id,
    width=test_setup["browser"]["width"],
    height=test_setup["browser"]["height"]
)
print(f"✅ ウィンドウサイズ設定: {test_setup['browser']['width']}x{test_setup['browser']['height']}")
```

---

### Phase 2: シナリオ実行（7-8分）

#### パターン1: ログインフロー検証（1-2分）

**目的**: ユーザーが正常にログイン → ダッシュボード遷移を確認

**実行方法**:

```python
scenario_id = "scenario_001"
scenario_name = "ログインフロー検証"

# STEP 1: ログインページへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/login")
computer(tabId=tab_id, action="wait", duration=2)

# STEP 2: 初期スクリーンショット
ss_initial = computer(tabId=tab_id, action="screenshot")
print(f"📸 初期状態: {ss_initial}")

# STEP 3: メール入力欄を検索
find_email = find(tabId=tab_id, query="email input field")
if not find_email:
    print("❌ メール入力欄が見つかりません")
    return handle_element_not_found()

# STEP 4: メール＋パスワード入力
form_input(tabId=tab_id, ref=find_email, value="test@example.com")

find_password = find(tabId=tab_id, query="password input field")
form_input(tabId=tab_id, ref=find_password, value="testpass123")

# STEP 5: ログインボタンクリック
find_button = find(tabId=tab_id, query="login button")
computer(tabId=tab_id, action="left_click", ref=find_button)

# STEP 6: ページ遷移待機
computer(tabId=tab_id, action="wait", duration=5)

# STEP 7: ダッシュボード確認
page_content = read_page(tabId=tab_id, filter="all", depth=10)
ss_result = computer(tabId=tab_id, action="screenshot")

# STEP 8: スコア計算
score = calculate_login_score(page_content, ss_initial, ss_result)
print(f"✅ {scenario_name}: {score}点")
```

**成功基準**（合計100点）:
- ページ遷移成功: 20点
- フォーム入力成功: 15点
- ボタンクリック成功: 10点
- エラーメッセージ非表示: 15点
- ビジュアル品質: 25点
- レスポンス時間: 15点

**タイムアウト**: 60秒 / リトライ: 2回まで

---

#### パターン2: フォーム送信検証（1-2分）

**目的**: 複数フィールドのフォーム入力 → 送信 → 確認 → バックエンド検証

**実行方法**:

```python
scenario_id = "scenario_002"
scenario_name = "フォーム送信検証"

# STEP 1: フォームページへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/settings/profile-edit")
computer(tabId=tab_id, action="wait", duration=2)

# STEP 2: フォーム要素を読み取り
page_content = read_page(tabId=tab_id, filter="interactive", depth=10)
ss_initial = computer(tabId=tab_id, action="screenshot")

# STEP 3: 複数フィールドに入力
fields = [
    {"query": "name field", "value": "田中太郎"},
    {"query": "email field", "value": "tanaka@example.com"},
    {"query": "phone field", "value": "09012345678"}
]

for field in fields:
    ref = find(tabId=tab_id, query=field["query"])
    form_input(tabId=tab_id, ref=ref, value=field["value"])

# STEP 4: 送信ボタンをクリック
submit_ref = find(tabId=tab_id, query="submit button")
computer(tabId=tab_id, action="left_click", ref=submit_ref)

# STEP 5: 処理待機
computer(tabId=tab_id, action="wait", duration=4)

# STEP 6: 結果確認
page_content_after = read_page(tabId=tab_id, filter="all", depth=10)
ss_result = computer(tabId=tab_id, action="screenshot")

# STEP 7: バックエンド検証
api_response = javascript_tool(
    tabId=tab_id,
    text="fetch('http://localhost:3000/api/profile').then(r => r.json()).then(d => d);"
)

# STEP 8: スコア計算
score = calculate_form_score(page_content_after, api_response, ss_initial, ss_result)
print(f"✅ {scenario_name}: {score}点")
```

**成功基準**（合計100点）:
- 複数フィールド入力成功: 20点
- フォーム送信成功: 25点
- バックエンド処理成功: 20点
- ユーザーフィードバック: 15点
- フォーム検証: 15点
- レスポンス時間: 5点

**バリデーションテスト**:
- 無効なメール入力 → エラー表示確認
- 必須フィールド未入力 → エラー表示確認

---

#### パターン3: ページ遷移検証（1-2分）

**目的**: 複数ページ間のリンク遷移 → URL確認 → 戻る動作確認

**実行方法**:

```python
scenario_id = "scenario_003"
scenario_name = "ページ遷移検証"

# STEP 1: ダッシュボードホームへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/dashboard")
computer(tabId=tab_id, action="wait", duration=2)
ss_1 = computer(tabId=tab_id, action="screenshot")

# STEP 2: プロジェクトリンクをクリック
projects_link = find(tabId=tab_id, query="projects link")
computer(tabId=tab_id, action="left_click", ref=projects_link)
computer(tabId=tab_id, action="wait", duration=3)
ss_2 = computer(tabId=tab_id, action="screenshot")

# STEP 3: プロジェクト詳細ページへ
first_project = find(tabId=tab_id, query="first project item")
computer(tabId=tab_id, action="left_click", ref=first_project)
computer(tabId=tab_id, action="wait", duration=4)
ss_3 = computer(tabId=tab_id, action="screenshot")

# STEP 4: 戻るボタンをクリック
back_button = find(tabId=tab_id, query="back button")
computer(tabId=tab_id, action="left_click", ref=back_button)
computer(tabId=tab_id, action="wait", duration=2)
ss_4 = computer(tabId=tab_id, action="screenshot")

# STEP 5: URL検証
page_content = read_page(tabId=tab_id, filter="all", depth=10)
current_url = javascript_tool(tabId=tab_id, text="window.location.href;")

# STEP 6: スコア計算
score = calculate_navigation_score(
    page_content,
    [ss_1, ss_2, ss_3, ss_4],
    current_url
)
print(f"✅ {scenario_name}: {score}点")
```

**成功基準**（合計100点）:
- 初期ページ読み込み: 15点
- リンク遷移成功（1回目）: 20点
- 詳細ページ遷移成功: 20点
- 戻るボタン機能: 20点
- ページ遷移時間: 15点
- ビジュアル整合性: 10点

**URL検証**:
- Step 1 後: `localhost:3000/dashboard`
- Step 2 後: `localhost:3000/projects`
- Step 3 後: `localhost:3000/projects/{id}`
- Step 4 後: `localhost:3000/projects`

---

#### パターン4: Ajax/非同期処理検証（1-2分）

**目的**: Ajax呼び出し → ネットワークレベル確認 → UIの動的更新確認

**実行方法**:

```python
scenario_id = "scenario_004"
scenario_name = "Ajax/非同期処理検証"

# STEP 1: リアルタイムデータページへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/analytics/realtime")
computer(tabId=tab_id, action="wait", duration=2)
ss_initial = computer(tabId=tab_id, action="screenshot")

# STEP 2: リクエスト開始数を記録
javascript_tool(
    tabId=tab_id,
    text="window.__requestsStarted = performance.getEntriesByType('resource').length;"
)

# STEP 3: 更新ボタンをクリック（Ajax呼び出しをトリガー）
refresh_button = find(tabId=tab_id, query="refresh button")
computer(tabId=tab_id, action="left_click", ref=refresh_button)

# STEP 4: ネットワークリクエストを確認
network_reqs = read_network_requests(tabId=tab_id, urlPattern="/api/")
print(f"ℹ️ ネットワークリクエスト数: {len(network_reqs)}")

# STEP 5: 処理完了まで待機
computer(tabId=tab_id, action="wait", duration=3)

# STEP 6: UI更新を確認
ss_updated = computer(tabId=tab_id, action="screenshot")
page_content = read_page(tabId=tab_id, filter="all", depth=10)

# STEP 7: ローディング状態確認
loading_status = javascript_tool(
    tabId=tab_id,
    text="!document.querySelector('[class*=\"loading\"]') && !document.querySelector('[class*=\"spinner\"]');"
)

# STEP 8: コンソールエラー確認
console_errors = read_console_messages(
    tabId=tab_id,
    pattern="error|warning|exception",
    onlyErrors=True
)

# STEP 9: スコア計算
score = calculate_ajax_score(
    network_reqs,
    ss_initial,
    ss_updated,
    loading_status,
    console_errors,
    page_content
)
print(f"✅ {scenario_name}: {score}点")
```

**成功基準**（合計100点）:
- Ajax呼び出し成功: 25点
- UIの更新確認: 20点
- ローディング状態の解除: 15点
- エラーなし: 20点
- データ更新確認: 15点
- パフォーマンス（<2秒）: 5点

**パフォーマンス基準**:
- Ajax応答時間: < 2秒（目標）、> 3秒（NGレベル）
- UI更新時間: < 500ms（目標）、> 2秒（NGレベル）

---

#### パターン5: エラーハンドリング検証（1-2分）

**目的**: エラー発生時のUI反応 → エラーメッセージ表示 → リトライ機能確認

**実行方法**:

```python
scenario_id = "scenario_005"
scenario_name = "エラーハンドリング検証"

# STEP 1: テストページへ遷移
navigate(tabId=tab_id, url="http://localhost:3000/dashboard")
computer(tabId=tab_id, action="wait", duration=2)
ss_normal = computer(tabId=tab_id, action="screenshot")

# STEP 2: APIエラーをシミュレート
javascript_tool(
    tabId=tab_id,
    text="""
    window.mockApiError = true;
    fetch = new Proxy(fetch, {
        apply: (target, thisArg, args) => {
            if(window.mockApiError) {
                return Promise.reject(new Error('Mock API Error: 500'));
            }
            return Reflect.apply(target, thisArg, args);
        }
    });
    """
)

# STEP 3: データ読み込みボタンをクリック（エラーをトリガー）
load_button = find(tabId=tab_id, query="load data button")
computer(tabId=tab_id, action="left_click", ref=load_button)

# STEP 4: エラー処理待機
computer(tabId=tab_id, action="wait", duration=2)

# STEP 5: エラーメッセージ確認
ss_error = computer(tabId=tab_id, action="screenshot")
page_content = read_page(tabId=tab_id, filter="all", depth=10)

error_message = javascript_tool(
    tabId=tab_id,
    text="""
    document.querySelector('[role="alert"]')?.textContent ||
    document.querySelector('[class*="error"]')?.textContent ||
    'Error message not found';
    """
)
print(f"ℹ️ エラーメッセージ: {error_message}")

# STEP 6: リトライボタンを検索
retry_button = find(tabId=tab_id, query="retry button")

# STEP 7: APIエラーを解除
javascript_tool(tabId=tab_id, text="window.mockApiError = false;")

# STEP 8: リトライボタンをクリック
computer(tabId=tab_id, action="left_click", ref=retry_button)

# STEP 9: 再試行処理待機
computer(tabId=tab_id, action="wait", duration=3)

# STEP 10: 成功確認
ss_recovered = computer(tabId=tab_id, action="screenshot")
page_content_after = read_page(tabId=tab_id, filter="all", depth=10)

# STEP 11: バリデーションエラーテスト
form_element = javascript_tool(
    tabId=tab_id,
    text="const form = document.querySelector('form'); if(form) { form.submit(); } true;"
)

computer(tabId=tab_id, action="wait", duration=1)
ss_validation_error = computer(tabId=tab_id, action="screenshot")

# STEP 12: スコア計算
score = calculate_error_handling_score(
    page_content,
    error_message,
    page_content_after,
    ss_error,
    ss_recovered,
    ss_validation_error
)
print(f"✅ {scenario_name}: {score}点")
```

**成功基準**（合計100点）:
- エラーメッセージ表示: 20点
- エラーメッセージ明確性: 15点
- リトライボタン表示: 15点
- リトライ機能動作: 20点
- バリデーションエラー表示: 15点
- エラーハンドリング堅牢性: 15点

**テストされるエラーシナリオ**:
- API 500エラー
- フォームバリデーションエラー
- リトライ成功後の復帰

---

### Phase 3: レポート生成＆品質判定（2-3分）

#### Step 3-1: スコア集計

```python
# 全シナリオのスコアを集計
all_scores = {
    "scenario_001_login": score_1,
    "scenario_002_form": score_2,
    "scenario_003_navigation": score_3,
    "scenario_004_ajax": score_4,
    "scenario_005_error": score_5
}

total_score = sum(all_scores.values())
average_score = total_score / len(all_scores)

print(f"""
📊 UIテスト検証結果
━━━━━━━━━━━━━━━━━━━━━━
Scenario 1 (ログイン):        {score_1}/100
Scenario 2 (フォーム):        {score_2}/100
Scenario 3 (ページ遷移):      {score_3}/100
Scenario 4 (Ajax):           {score_4}/100
Scenario 5 (エラーハンドリング): {score_5}/100
━━━━━━━━━━━━━━━━━━━━━━
総合スコア:                   {total_score}/500
平均スコア:                   {average_score:.1f}/100
━━━━━━━━━━━━━━━━━━━━━━
""")
```

#### Step 3-2: 品質ゲート判定

```python
# 品質ゲート基準
if total_score >= 420:
    quality_level = "優秀 (高品質)"
    recommendation = "本番環境への統合推奨"
    color = "🟢"
elif total_score >= 350:
    quality_level = "合格"
    recommendation = "統合OK、改善点を記録"
    color = "🟡"
else:
    quality_level = "要改善"
    recommendation = "UI修正後に再検証"
    color = "🔴"

print(f"""
{color} 品質判定: {quality_level}
   推奨アクション: {recommendation}
   スコア閾値: {total_score}/500 (合格: 350点以上)
""")
```

#### Step 3-3: レポート生成

```python
# マークダウンレポート生成
report_md = f"""
# UIテスト検証レポート

**実行日時**: {datetime.now().isoformat()}
**テスト環境**: http://localhost:3000
**ブラウザ**: Chrome (1920x1080)
**実行時間**: 約10分

## 検証結果サマリー

| シナリオ | スコア | 判定 |
|---------|--------|------|
| Scenario 1: ログインフロー検証 | {score_1}/100 | {'✅' if score_1 >= 70 else '❌'} |
| Scenario 2: フォーム送信検証 | {score_2}/100 | {'✅' if score_2 >= 70 else '❌'} |
| Scenario 3: ページ遷移検証 | {score_3}/100 | {'✅' if score_3 >= 70 else '❌'} |
| Scenario 4: Ajax/非同期処理検証 | {score_4}/100 | {'✅' if score_4 >= 70 else '❌'} |
| Scenario 5: エラーハンドリング検証 | {score_5}/100 | {'✅' if score_5 >= 70 else '❌'} |
| **総合** | **{total_score}/500** | **{quality_level}** |

## 詳細結果

### Scenario 1: ログインフロー検証
- ページ遷移成功: ✅
- フォーム入力成功: ✅
- ボタンクリック成功: ✅
- エラーメッセージ非表示: ✅
- ビジュアル品質: ✅
- レスポンス時間: ✅

### Scenario 2: フォーム送信検証
[詳細結果]

### Scenario 3: ページ遷移検証
[詳細結果]

### Scenario 4: Ajax/非同期処理検証
[詳細結果]

### Scenario 5: エラーハンドリング検証
[詳細結果]

## 推奨事項

{generate_recommendations(all_scores)}

## 品質ゲート判定

**総合スコア**: {total_score}/500 ({total_score/500*100:.1f}%)
**判定**: {quality_level}
**推奨アクション**: {recommendation}

---

*レポート生成: 2026-01-09 Claude Code UI Testing Agent*
"""

# JSON形式でスコアを保存
scores_json = {
    "timestamp": datetime.now().isoformat(),
    "total_score": total_score,
    "average_score": average_score,
    "quality_level": quality_level,
    "scenarios": all_scores,
    "passing_score": 350,
    "quality_gates": {
        "high_quality": {"min": 420, "label": "優秀"},
        "acceptable": {"min": 350, "label": "合格"},
        "needs_improvement": {"max": 349, "label": "要改善"}
    }
}

# ファイルに保存
save_report(report_md, "ui_verification_report.md")
save_scores(scores_json, "ui_verification_scores.json")
save_screenshots(screenshots, "ui_verification/screenshots/")

print("✅ レポート生成完了")
print(f"   📄 ui_verification_report.md")
print(f"   📊 ui_verification_scores.json")
print(f"   📸 ui_verification/screenshots/")
```

---

## トラブルシューティング

### 問題1: "Failed to find element: 401 authentication_error"

**原因**: OAuth tokenが期限切れ

**解決方法**:
```python
try:
    tabs_info = tabs_context_mcp(createIfEmpty=True)
except AuthenticationError:
    print("❌ Chrome拡張認証エラー: OAuth tokenが期限切れです")
    print("対処: Chrome拡張を再起動してください")
    return skip_ui_verification()
```

### 問題2: スクリーンショットが空白（真っ白）

**原因**: ページ読み込みが完了していない

**解決方法**:
```python
# スクリーンショット前に2-5秒待機
computer(tabId=tab_id, action="wait", duration=5)
screenshot_id = computer(tabId=tab_id, action="screenshot")
```

### 問題3: 要素が見つからない

**原因**: ページがまだレンダリング中 or 要素が動的生成される

**解決方法**:
```python
# 5秒待機後に再試行
computer(tabId=tab_id, action="wait", duration=5)
find_result = find(tabId=tab_id, query="submit button")

if not find_result:
    # read_page で全要素確認
    all_elements = read_page(tabId=tab_id, filter="all", depth=15)
    print(f"ℹ️ ページ内の全要素:\n{all_elements}")
```

### 問題4: JavaScript実行が失敗

**原因**: ページのCSP（Content Security Policy）制限

**解決方法**:
```python
try:
    result = javascript_tool(tabId=tab_id, text=script)
except CSPError:
    print("⚠️ CSP制限のため、JavaScript実行不可")
    # パフォーマンスメトリクスがない場合はスキップ
    return skip_performance_check()
```

---

## ベストプラクティス

### 1. 並列実行による高速化

```python
# 5つのシナリオを3並列で実行
scenarios = [scenario_001, scenario_002, scenario_003, scenario_004, scenario_005]

# グループ1 (並列)
task1 = Task(subagent_type="general-purpose", prompt=scenario_001)
task2 = Task(subagent_type="general-purpose", prompt=scenario_002)
task3 = Task(subagent_type="general-purpose", prompt=scenario_003)

# グループ2 (順序: scenario_001の後に実行)
task4 = Task(subagent_type="general-purpose", prompt=scenario_004)
task5 = Task(subagent_type="general-purpose", prompt=scenario_005)

# 結果を集計
total_time = max(
    execution_time(task1),
    execution_time(task2),
    execution_time(task3)
) + max(
    execution_time(task4),
    execution_time(task5)
)
# = 順序実行の約60% の時間
```

### 2. エラーハンドリング

```python
# すべてのStep実行をtry-exceptで包む
try:
    execute_step(step_number, step_config)
except Exception as e:
    print(f"❌ Step {step_number} 失敗: {e}")

    # リトライ可能な場合
    if step_config.get("retry_on_failure"):
        for retry in range(step_config.get("max_retries", 2)):
            try:
                execute_step(step_number, step_config)
                break
            except:
                if retry == step_config.get("max_retries", 2) - 1:
                    raise  # 最終リトライ失敗
    else:
        raise
```

### 3. スクリーンショット管理

```python
# 検証ステップごとにスクリーンショットを保存
screenshots = {
    f"{scenario_id}_01_initial": ss_initial,
    f"{scenario_id}_02_interaction": ss_interaction,
    f"{scenario_id}_03_result": ss_result
}

# 比較用に保存
for name, ss_id in screenshots.items():
    save_to_disk(f"Flow/YYYYMM/YYYY-MM-DD/ui_verification/screenshots/{name}.jpeg", ss_id)
```

---

## 実行時間目安

| 操作 | 標準時間 | 最大時間 |
|------|---------|---------|
| タブ作成＋ページ遷移 | 5秒 | 10秒 |
| スクリーンショット取得 | 2秒 | 5秒 |
| フォーム入力 | 1秒 | 3秒 |
| クリック操作 | 1秒 | 3秒 |
| JavaScript実行 | 2秒 | 5秒 |
| **1シナリオ全体** | **30-60秒** | **120秒** |
| **5シナリオ全体（順序実行）** | **3-5分** | **10分** |
| **5シナリオ全体（並列実行）** | **1.5-2分** | **5分** |

---

## チェックリスト

テスト実行前に以下を確認：

- [ ] テスト環境のアプリケーションが起動している（localhost:3000）
- [ ] テストアカウント（test@example.com）が存在する
- [ ] ブラウザクッキーがクリアされている
- [ ] Chrome拡張が正常に動作している
- [ ] ネットワークが正常に接続されている
- [ ] テスト開始時刻を記録している

テスト実行後に以下を確認：

- [ ] 全5シナリオが完了している
- [ ] スコアが計算されている
- [ ] レポートが生成されている
- [ ] スクリーンショットが保存されている
- [ ] 品質ゲート判定が実施されている
- [ ] テスト結果をSlackに通知している

---

## 参照

- `ui_verification_scenarios.json` - 検証シナリオ定義
- @docs/implementation_guides/week1_ui_testing.md - Chrome拡張MCPガイド
- @.claude/rules/execution_preference.md - LLM優先アプローチ

---

**作成**: 2026-01-09 Claude Code
**更新予定**: テスト実行後に検証結果を追加
