# Threads Strategy

このフォルダには Threads に関する攻略情報を格納します。

## ディレクトリ構造
- `_Template/`: 調査用テンプレート
- `[Author Name]/`: 発信者別の調査・攻略情報

## データファイル

### CSVファイル
- `threads_YYYY-MM-DD.csv`: 過去90日分の投稿データ
  - scripts/fetch_threads_data.py で生成

### 分析結果
- `threads_analysis_results.json`: 投稿分析結果
  - scripts/analyze_threads_posts.py で生成

## 関連スクリプト

データ取得:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
python3 scripts/fetch_threads_data.py
```

分析:
```bash
python3 scripts/analyze_threads_posts.py
```
