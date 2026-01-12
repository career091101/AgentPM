# SNS アナリティクスデータ格納フォルダ

## データファイル一覧

### ✅ X (Twitter)
- **ファイル**: `account_overview_analytics.csv`
- **期間**: 直近3ヶ月
- **状態**: ✅ 配置済み
- **手動追加**: ツイート詳細データ（`tweet_activity_metrics_*.csv`）があれば、このフォルダに配置してください。

### ⏳ Facebook
- **エクスポート状態**: レポート生成完了
- **ダウンロード**: ブラウザで「ダウンロード」ボタンをクリック済み
- **期待ファイル名**: `facebook_export_*.csv` または類似の名前
- **次のステップ**: Downloadsフォルダに表示されたら、このフォルダに移動してください。
- **注**: Facebookのエクスポートはファイル生成とダウンロードに時間がかかる場合があります。

### ❓ LinkedIn
- **エクスポート状態**: 「エクスポート」ボタンをクリックしましたが、ダウンロードが完了していない可能性があります。
- **代替データ**: ブラウザから抽出したパフォーマンスデータ（上位49件）は分析レポートに反映済みです。
- **次のステップ**: 手動でLinkedInからエクスポートする場合は、このフォルダに配置してください。

## データ配置手順

### ターミナルから移動する場合:
```bash
mv ~/Downloads/<ファイル名>.csv "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/documents/2_discovery/data/"
```

### Finderから移動する場合:
1. Finderで「ダウンロード」フォルダを開く
2. 該当のCSVファイルを探す
3. このフォルダ（`/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/documents/2_discovery/data/`）にドラッグ&ドロップ

## 現在のディレクトリパス
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/documents/2_discovery/data/
```
