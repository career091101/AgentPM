---
description: エリオット波動週次レポートの自動処理ワークフロー (Agent-Native Vision)
---

# エリオット波動週次レポート処理ワークフロー (Agent-Native Vision版)

このワークフローは、テキスト抽出が困難なPDFレポートに対し、**PDFを画像化してエージェントが「目で見て」分析する**手法を定義します。

## 事前準備

*   **必須ツール**: `PyMuPDF` (Pythonライブラリ)
*   **必須スクリプト**: `scripts/rasterize_pdf.py`
*   **必須パス**: `Stock/programs/資産運用/projects/エリオット波動分析/`

## ワークステップ

### 1. レポート格納 (User Action)
毎週土曜日に配信されるPDFを以下のディレクトリに格納してください。
*   パス: `resources/reports/weekly/`

### 2. ラスタライズ実行 (Agent Action)
// turbo
以下のコマンドを実行して、PDFの全ページを高解像度画像に変換します。

```bash
# 最新のPDFを特定してスクリプト実行
python3 scripts/rasterize_pdf.py "resources/reports/weekly/Elliott_Wave_Weekly_Report_vol_XXX.pdf"
```

*   **出力**: `resources/reports/weekly/page_images/page_01.png` ... `page_30.png`

### 3. 視覚分析とレポート生成 (Agent Action)
エージェントは以下の手順で生成された画像を閲覧します。

1.  **目次確認**: `page_01.png` (または `02`) を開き、「Nikkei 225」「USD/JPY」などの掲載ページ番号を目視で特定します。
2.  **詳細分析**: 特定したページ番号の画像を開き、チャート形状やトレンドライン、重要数値を読み取ります。
3.  **生成**: 読み取った情報を元に、以下の2ファイルを生成します。

#### A. ユーザー閲覧用サマリー
*   **保存先**: `documents/4_executing/strategies/Week_Current_YYYY-MM-DD.md`
*   **内容**: 人間が読みやすいよう、重要なチャート画像を埋め込み、AIの解説を付記したMarkdown。

#### B. システム参照用データ
*   **保存先**: `data/weekly_processing/report_data_YYYY-MM-DD.json`
*   **内容**: 統合分析システムが参照するための厳密なJSONデータ。

## 4. 完了通知 (Agent Action)
生成完了後、ユーザーに成果物を通知します。
