# エリオット波動レポート活用要件定義書

## 1. 概要
隔週で配信される「エリオット波動レポート（PDF）」をAIが自動解析し、トレーディングに直結する「週次戦略サマリー」を生成するシステムの要件を定義する。

## 2. 分析対象とスコープ
*   **対象:** レポートに含まれる**全ての銘柄**を抽出・データベース化する。
*   **優先順位:** データベース化は全銘柄で行うが、サマリー生成時は推奨銘柄（日経225、ドル円、S&P500、ゴールド）をトップに表示する仕様とする。

## 3. 分析の視点（時間軸・波）
*   **時間軸:** スイングトレード（数日～数週間）
*   **対象ウェーブ:**
    *   **Minor (マイナー級)**
    *   **Intermediate (インターミディエイト級)**
    *   ※上記より大きなPrimary級は環境認識として、小さなMinute級は無視する。

## 4. シナリオの扱い
*   **複合アプローチ (A案 + B案):**
    *   **メインシナリオ:** 詳細に追跡。**「無効化レベル（Invalidation Level）」**を明確に抽出・記録し、この価格を割り込んだ際のアラート基準とする。
    *   **代替シナリオ (Alt count):** 無視せず、**「分岐点（Branching Point）」**におけるプライスアクションの監視対象として扱う。
    *   **出力イメージ:** 「基本は上目線（メイン）。ただし$150.00を割ったら代替シナリオ（下落）が発動するため、ここでのプライスアクションを注視」という形式。

## 5. 他分析との統合
*   **統合先:** プロジェクト「統合分析」
*   **統合ロジック:** **「時間のメリマン × 価格のエリオット」**
    *   メリマンの重要変化日（前後数日）と、エリオットの重要価格帯・反転パターンが重複するタイミングを「最高重要度」のセットアップとして定義する。

## 6. 自動処理のゴール (Output)
**「週次戦略サマリー」のMarkdown生成**

### 出力フォーマット案

```markdown
# 週次エリオット波動戦略サマリー (YYYY-MM-DD)

## 🚨 重要ハイライト
*   **日経225**: メジャーサイクルのボトム形成中。38,000円が維持される限り強気。
*   **USD/JPY**: トライアングル形成中。ブレイク待ち。

## 📊 銘柄別詳細分析

### 1. 日経225 (Nikkei 225)
*   **現在の波動**: Intermediate Wave (2) or (B)
*   **トレンド**: ↗️ Bullish (Correction ending)
*   **重要価格 (Key Levels)**:
    *   抵抗帯: 39,500 - 40,000
    *   支持帯: 38,000 (Invalidation Level)
*   **シナリオ分岐点**: 38,000を割るとAltシナリオ（Deep Correction）入り。
*   **アクション**: 38,500付近での反転確認でロング推奨。

### 2. USD/JPY
...
```

## 7. 実装ステップ
1.  **PDF解析**: PythonスクリプトまたはVision APIを用いてテキスト・数値を構造化データとして抽出。
2.  **サマリー生成**: LLMを用い、抽出データから上記フォーマットのMarkdownを生成。
3.  **DB保存**: 抽出した生データをデータベース（SQLite等）に蓄積（将来の検証用）。

## 8. LLM参照用データ要件 (System Data)
ユーザー閲覧用サマリーとは別に、統合分析AIが参照するための**厳密な構造化データ**を生成する。

### 8.1 フォーマット
*   **形式:** JSONライクなMarkdown (YAML Frontmatter + JSON block)
*   **ファイル名:** `data/weekly_processing/report_data_YYYY-MM-DD.json` (または `.md`)

### 8.2 データ構造 (Schema)
```json
{
  "report_date": "YYYY-MM-DD",
  "assets": [
    {
      "symbol": "Nikkei 225",
      "timeframe": "Intermediate",
      "direction": "Bullish",
      "current_wave": "Wave (2) or (B)",
      "key_levels": {
        "resistance": [39500, 40000],
        "support": [38500],
        "invalidation": 38000
      },
      "image_insight": "Ascending triangle pattern observed on daily chart. Momentum divergence on RSI.",
      "scenarios": {
        "main": "Bounce from 38500 targeting 40000.",
        "alt": "Break below 38000 targets 37000 (Deep Correction)."
      }
    }
  ]
}
```

### 8.3 必須フィールド
*   **symbol**: 銘柄名 (統一ID)
*   **invalidation**: メインシナリオの無効化価格（数値型）
*   **image_insight**: チャート画像の言語化記述（AIによる要約）
