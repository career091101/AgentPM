# ワークフロー: 週次統合分析ルーティン (Weekly Integrated Analysis)

## 目的
週末に翌週の市場環境を分析し、**「時間はMMA、価格と形状はエリオット」**の原則に基づいてトレード計画（シナリオ）を策定する。

---

## 運用フロー (Operational Flow)

### 1. 準備 (Preparation) - Human in the Loop
1. **PDF配置**: ユーザーはMerriman週次レポート(PDF)を取得し、`resources/weekly_reports/` に配置する（またはURLを提供）。
2. **指示**: ユーザーはエージェントに「今週の分析」を指示。

### 2. 分析実行 (Execution) - Agent
1. **画像化**: `scripts/rasterize_for_vision.py` を実行し、PDFを全ページ画像化する(300DPI)。
2. **視覚的分析 (Visual Analysis)**:
   - 生成された画像をエージェントが「目視」で確認する。
   - **抽出対象**:
     - 市場概況 (Market Review)
     - ジオコスミック分析 (Geocosmics) / 重要日程 (Key Dates)
     - **条件付き抽出**: レポートに「重要価格帯（Support/Resistance）」や「チャート画像」が含まれている場合のみ抽出し、記載/埋め込みを行う。なければ不要。
3. **年次サイクル照合 (Cycle Check)**:
   - **必須アクション**: `resources/reference/market_cycles_summary.md` を読み込み、現在の週次アクションが「年次サイクルのどのフェーズ（強気/弱気、天井/底）」にあるかを必ず確認する。
   - **JP225必須言及**: 日経225（JP225/Nikkei 225）に関しては、年次レポート (`forecast_2026_jp225_ja.md`) の情報も参照し、可能な限り具体的な展望を記載すること。

### 3. レポート作成 (Reporting)
1. `analysis/weekly/YYYY-Wxx_outlook.md` を作成する。
2. 以下の構造で記述する：
   - **概要**: 執筆者、休刊予定など。
   - **ジオコスミック分析**: 重要イベント、CRD、リスク期間。
   - **市場別分析 (Stocks, Metals, Crypto, etc.)**: 
     - 状況 (Status)
     - 年次サイクルの位置づけ (Cycle Phase)
     - シナリオ (Scenario)
   - **戦略 (Strategy)**: 前半/後半の方針、注意点。

---

## テンプレート (Markdown Template)

```markdown
# 週間市場分析: YYYY-Wxx (MM/DD - MM/DD)
**参照**: [Report Name/PDF]

## 1. 概要 (Overview)
- **全体感**: ...
- **重要アナウンス**: ...

## 2. ジオコスミック分析 (Geocosmics)
> **参照**: 2026_calendar_events.md
- **今週の配置**: ...
- **重要日程 (Key Dates)**:

| 日程 | イベント | 市場への影響 |
| :--- | :--- | :--- |
| MM/DD | ... | ... |

## 3. 市場別分析 (Market Specifics)

### 株式市場 (Stock Markets)
- **Status**: ...
- **年次サイクル照合**: 現在[強気/弱気]フェーズの[第x]局面。
- **重要価格帯**: (レポートに記載がある場合のみ表形式で記述)
- **チャート**: (レポートに記載がある場合のみ埋め込み)

### 貴金属 (Precious Metals)
...

## 4. 統合戦略 (Integrated Strategy)
- **方針**: ...
```
