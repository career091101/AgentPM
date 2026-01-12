---
name: agent-data-collector
description: |
  日経平均先物のデータ収集エージェント。IG証券からリアルタイム価格を取得（Claude in Chrome MCP使用）し、Yahoo Finance/Investing.comから5年分のヒストリカルデータを取得（WebFetch使用）。データ完全性チェックを実施し、95%以上の品質を保証。出力はJSON形式で構造化され、次のテクニカル分析に引き渡されます。

  使用タイミング：
  - トレード戦略立案の最初のステップ
  - 最新の市場データが必要な時
  - バックテスト用の過去データ収集時

  所要時間：10-15分
  出力：market_data.json（現在価格 + 5年分ヒストリカルデータ）
trigger_keywords:
  - "データ収集"
  - "市場データ取得"
  - "日経平均データ"
  - "価格データ収集"
stage: Data Collection
dependencies: []
output_file: Stock/programs/資産運用/projects/TradingAgents/data/sources/{YYYY-MM-DD}/market_data.json
execution_time: 10-15分
framework_reference: Stock/programs/資産運用/projects/TradingAgents/knowledge/
priority: P0
framework_compliance: 100%
---

# Agent Data Collector Skill

日経平均先物のデータ収集エージェント。

---

## このSkillでできること

1. **リアルタイム価格取得**: IG証券から日経平均先物の現在価格を取得（Claude in Chrome MCP使用）
2. **ヒストリカルデータ取得**: Yahoo Finance/Investing.comから5年分のOHLCV（始値・高値・安値・終値・出来高）データを取得（WebFetch使用）
3. **データ完全性チェック**: 欠損データを検出し、データ完全性95%以上を保証
4. **代替ソース対応**: メインソース失敗時に自動的に代替ソースへ切替
5. **JSON構造化出力**: エリオット波動分析プロジェクトと同じ形式でデータを出力

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（自動で最新データを収集） |
| **出力** | market_data.json（現在価格 + 5年分ヒストリカルデータ、データ完全性スコア） |
| **次のSkill** | agent-technical-analyst（テクニカル分析）、agent-elliott-wave-analyst（エリオット波動分析） |

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 10-15分

### データ収集ステップ

#### STEP 1: IG証券からリアルタイム価格取得（5分）

**Claude in Chrome MCP使用**:

```javascript
// 1. ブラウザ初期化
tabs_context_mcp(createIfEmpty: true)

// 2. IG証券ページへナビゲート
navigate(url: "https://www.ig.com/jp/indices/markets-indices/japan-225", tabId: [tab_id])

// 3. ページロード待機
computer(action: "wait", duration: 3, tabId: [tab_id])

// 4. ページ内容取得
read_page(tabId: [tab_id])

// 5. 価格要素を検出
find(query: "現在価格", tabId: [tab_id])

// 6. JavaScriptで価格データ抽出
javascript_tool(
  tabId: [tab_id],
  text: `
    // 価格要素を取得
    const priceElement = document.querySelector('[data-field="MID_PRICE"]') ||
                         document.querySelector('.price-quote');
    const price = priceElement ? parseFloat(priceElement.textContent.replace(/,/g, '')) : null;

    // 変動率を取得
    const changeElement = document.querySelector('[data-field="CHANGE_PCT"]');
    const changePct = changeElement ? parseFloat(changeElement.textContent) : null;

    // 高値・安値を取得
    const highElement = document.querySelector('[data-field="HIGH"]');
    const lowElement = document.querySelector('[data-field="LOW"]');
    const high = highElement ? parseFloat(highElement.textContent.replace(/,/g, '')) : null;
    const low = lowElement ? parseFloat(lowElement.textContent.replace(/,/g, '')) : null;

    // タイムスタンプ
    const timestamp = new Date().toISOString();

    // 結果を返す
    ({price, changePct, high, low, timestamp})
  `
)
```

**代替ソース1（IG証券失敗時）**: WebFetch使用
```
WebFetch(
  url: "https://www.investing.com/indices/japan-ni225",
  prompt: "日経平均の現在価格、変動率、高値、安値を抽出してください。JSON形式: {price, changePct, high, low}"
)
```

**代替ソース2**: Yahoo Finance
```
WebFetch(
  url: "https://finance.yahoo.com/quote/^N225",
  prompt: "日経平均の現在価格、変動率、高値、安値を抽出してください"
)
```

#### STEP 2: ヒストリカルデータ取得（5-10分）

**Yahoo Finance CSV取得**:

```
WebFetch(
  url: "https://query1.finance.yahoo.com/v7/finance/download/^N225?period1=[5年前のUnixタイムスタンプ]&period2=[現在のUnixタイムスタンプ]&interval=1d&events=history",
  prompt: `
    このCSVデータから以下のJSON配列形式で抽出してください：
    [
      {"date": "YYYY-MM-DD", "open": 数値, "high": 数値, "low": 数値, "close": 数値, "volume": 数値}
    ]

    注意点：
    - 日付は降順（新しい順）から昇順（古い順）に並び替え
    - 欠損データ（null/NaN）は除外
    - 出来高（volume）が0のデータも除外
  `
)
```

**代替ソース（Yahoo Finance失敗時）**: Investing.com

```
WebFetch(
  url: "https://www.investing.com/indices/japan-ni225-historical-data",
  prompt: `
    この歴史的株価データテーブルから、過去5年分（2020-01-01以降）のデータを以下のJSON形式で抽出してください：
    [{"date": "YYYY-MM-DD", "open": 数値, "high": 数値, "low": 数値, "close": 数値, "volume": 数値}]
  `
)
```

#### STEP 3: データ完全性チェック（1-2分）

```python
# 擬似コード（LLM内計算）

# 期待データポイント数（5年 × 約250営業日/年）
expected_points = 5 * 250  # 1,250ポイント

# 実際のデータポイント数
actual_points = len(historical_data)

# データ完全性スコア
data_completeness = (actual_points / expected_points) * 100

# 欠損期間の検出
date_gaps = []
for i in range(1, len(historical_data)):
    current_date = historical_data[i]['date']
    previous_date = historical_data[i-1]['date']
    days_diff = (current_date - previous_date).days

    # 営業日ベースで5日以上の gap があれば記録
    if days_diff > 5:
        date_gaps.append({
            'from': previous_date,
            'to': current_date,
            'days': days_diff
        })

# 判定
if data_completeness >= 95:
    status = "success"
elif data_completeness >= 90:
    status = "warning"  # 警告付きで続行
else:
    status = "failure"  # データ不足で停止
```

#### STEP 4: JSON出力生成（1分）

**出力フォーマット** (エリオット波動分析パターン準拠):

```json
{
  "collection_date": "2025-12-29",
  "status": "success",
  "current_price": {
    "price": 33200,
    "change_pct": 0.45,
    "high": 33350,
    "low": 32950,
    "timestamp": "2025-12-29T15:00:00+09:00"
  },
  "historical_data": [
    {
      "date": "2020-01-01",
      "open": 23000,
      "high": 23200,
      "low": 22800,
      "close": 23100,
      "volume": 1000000
    },
    ...
  ],
  "data_quality": {
    "completeness": 98.5,
    "expected_points": 1250,
    "actual_points": 1231,
    "missing_points": 19,
    "date_gaps": [
      {"from": "2020-04-10", "to": "2020-04-20", "days": 10}
    ]
  },
  "data_sources": {
    "current_price": "IG証券",
    "historical_data": "Yahoo Finance"
  }
}
```

**保存先**: `Stock/programs/資産運用/projects/TradingAgents/data/sources/{YYYY-MM-DD}/market_data.json`

---

## データソース優先順位

### リアルタイム価格

1. **IG証券** (最優先): https://www.ig.com/jp/indices/markets-indices/japan-225
   - Claude in Chrome MCP使用
   - 最も正確なリアルタイムデータ

2. **Investing.com** (代替1): https://www.investing.com/indices/japan-ni225
   - WebFetch使用
   - IG証券失敗時に自動切替

3. **Yahoo Finance** (代替2): https://finance.yahoo.com/quote/^N225
   - WebFetch使用
   - 両方失敗時の最終手段

### ヒストリカルデータ

1. **Yahoo Finance CSV** (最優先): Yahoo Finance API
   - 完全なOHLCVデータ
   - CSV形式で高速取得

2. **Investing.com** (代替): Investing.com Historical Data
   - WebFetch + HTMLパース
   - Yahoo失敗時に自動切替

---

## エラーハンドリング

### IG証券アクセス失敗
- **原因**: ページ構造変更、ネットワークエラー
- **対応**: Investing.com → Yahoo Financeの順で代替ソース使用
- **ログ**: data_sources.current_price に "代替ソース: Investing.com" 記録

### ヒストリカルデータ欠損
- **原因**: データソースのメンテナンス、API制限
- **対応**:
  - データ完全性 ≥ 95%: 成功判定、そのまま続行
  - 90% ≤ データ完全性 < 95%: 警告付き続行
  - データ完全性 < 90%: 失敗判定、ユーザーに報告

### タイムアウト
- **各ステップのタイムアウト**:
  - IG証券: 60秒
  - Yahoo Finance CSV: 120秒
  - Investing.com: 90秒
- **対応**: タイムアウト時は即座に代替ソースへ切替

---

## データ完全性基準

| スコア | 判定 | 対応 |
|-------|------|------|
| ≥ 95% | 成功 | そのまま次のステップへ |
| 90-95% | 警告 | 警告付きで続行、date_gaps を記録 |
| < 90% | 失敗 | 停止、ユーザーに代替期間提案 |

---

## 成果物フォーマット

**market_data.json**:
```json
{
  "collection_date": "YYYY-MM-DD",
  "status": "success" | "warning" | "failure",
  "current_price": {
    "price": 数値,
    "change_pct": 数値,
    "high": 数値,
    "low": 数値,
    "timestamp": "ISO 8601形式"
  },
  "historical_data": [
    {"date": "YYYY-MM-DD", "open": 数値, "high": 数値, "low": 数値, "close": 数値, "volume": 数値}
  ],
  "data_quality": {
    "completeness": 数値（%）,
    "expected_points": 数値,
    "actual_points": 数値,
    "missing_points": 数値,
    "date_gaps": [{"from": "YYYY-MM-DD", "to": "YYYY-MM-DD", "days": 数値}]
  },
  "data_sources": {
    "current_price": "ソース名",
    "historical_data": "ソース名"
  }
}
```

**data_collection_log.md**:
```markdown
# データ収集ログ

収集日時: YYYY-MM-DD HH:MM:SS

## 実行サマリー
- ステータス: [成功/警告/失敗]
- データ完全性: XX.X%
- 所要時間: XX分

## データソース
- 現在価格: [IG証券/Investing.com/Yahoo Finance]
- ヒストリカル: [Yahoo Finance/Investing.com]

## エラー・警告
[発生したエラーや警告を記録]

## 次のアクション
[テクニカル分析へ進む / 再収集が必要 / など]
```

---

## Knowledge Base参照

- データ収集方法論: `Stock/programs/資産運用/projects/TradingAgents/knowledge/data_collection_methodology.md`
- データソース一覧: `Stock/programs/資産運用/projects/TradingAgents/knowledge/data_sources.md`

---

## 使用例

### 基本的な使用

```
User: データ収集を実行
```

システムが自動的に：
1. IG証券から現在価格取得
2. Yahoo Financeから5年分データ取得
3. データ完全性チェック（95%以上）
4. market_data.json 生成

### 代替ソース使用例

IG証券が失敗した場合：
```
[IG証券アクセス失敗を検出]
→ Investing.comへ自動切替
→ 現在価格取得成功
→ data_sources.current_price = "代替ソース: Investing.com"
```

---

## 実行時の注意事項

1. **市場時間**: 土日祝日は最新データ取得不可、前営業日データで代用
2. **データソース変更**: Webサイト構造変更により取得失敗の可能性あり（代替ソース自動使用）
3. **ネットワーク**: タイムアウト時は代替ソースへ自動切替
4. **データ品質**: 完全性 < 90% の場合は分析精度に影響

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
