# 歯科医院院長名収集タスク

## 概要
CSVファイルの行1-107に記載された107医院から院長名を収集し、CSV形式で出力

## 入力ファイル
- `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/歯科医院リスト - nationwide_45prefectures_split_address_20260102_233408.csv.csv`
- 行1: ヘッダー
- 行2-108: 医院データ（107医院）
- 列: 医院名（列1）, 公式ウェブサイト（列8）

## 出力ファイル
- `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_1.csv`
- 列: 医院名, 院長名

## 実行手順

### STEP 1: サンプル医院で動作確認（最初の10医院）
実行順序:
1. CSVファイルから最初の10医院を抽出
2. 各医院について:
   - 公式ウェブサイトがあればWebFetchで取得
   - ウェブページから「院長」「理事長」「Dr.」などのキーワードで院長名を抽出
   - 見つからない場合は「医院名 院長」でWebSearch実行
   - どちらでも見つからない場合は「不明」と記録
3. インターバル: 2秒

### STEP 2: 残り医院を処理（11-107医院）
1. STEP 1と同じ手順で残り97医院を処理
2. インターバル: 2秒

## 抽出ルール

### キーワード（優先順）
1. 院長: 「院長」「院長名」「代表」「管理者」
2. 役職: 「理事長」「副院長」
3. 敬称なし: 「Dr.」「医師」

### 処理ルール
- **複数候補**: 最初の1名のみ採用
- **敬称除外**: 「先生」「Dr.」「等」などは削除して氏名のみ
- **名前の妥当性**: 1文字以上30文字以下
- **エラーハンドリング**: タイムアウト/接続エラーは「不明」

## 医院リスト（サンプル：最初の10医院）

| # | 医院名 | 公式ウェブサイト |
|---|--------|-----------------|
| 1 | おとなとこどもの経堂歯科 | https://www.otonatokodomo-kyodo-dental.com/ |
| 2 | 原宿こども歯科 | https://www.hk-dental.net/ |
| 3 | 医療法人社団心音会こどもの歯科｜祐天寺 歯医者・小児歯科/小児矯正 | https://kodomonoshika.net/?utm_source=mybusiness |
| 4 | 永福町駅前歯科・矯正歯科・小児歯科 | https://eifuku-dental.net/ |
| 5 | かつらファミリー歯科 | http://www.dental-katsura.com/ |
| 6 | キッズデンタル麻布 | http://www.kids-azabu.com/ |
| 7 | 浜田山おとなこども歯科・矯正歯科 | http://hamadayama-shika.net/ |
| 8 | 下高井戸パール歯科クリニック・世田谷 | http://www.pearl-shika.com/ |
| 9 | 永福町木村歯科クリニック | http://www.dc-kimura.com/ |
| 10 | You矯正歯科 新宿医院 | https://www.bubunkyousei.com/?utm_source=google&utm_medium=maps&utm_campaign=shinjuku |

## 実装例（最初の3医院）

### 医院1: おとなとこどもの経堂歯科
**WebFetch**:
```
URL: https://www.otonatokodomo-kyodo-dental.com/
キーワード: 院長、理事長、Dr.
予想結果: 院長名が見つかる or 見つからない
```

### 医院2: 原宿こども歯科
**WebFetch**:
```
URL: https://www.hk-dental.net/
キーワード: 院長、医師、Dr.
予想結果: 院長情報が掲載されているか確認
```

### 医院3: 医療法人社団心音会...
**WebFetch**:
```
URL: https://kodomonoshika.net/?utm_source=mybusiness
キーワード: 院長、医師、スタッフ紹介
予想結果: スタッフ紹介ページから院長名抽出
```

## 代替検索（WebFetchで見つからない場合）

医院1でWebFetchが失敗または院長名が見つからない場合:
```
WebSearch: "おとなとこどもの経堂歯科 院長"
結果: GoogleやDuckDuckGoの検索結果から院長名を抽出
```

## 出力フォーマット

### サンプル出力
```csv
医院名,院長名
おとなとこどもの経堂歯科,山田太郎
原宿こども歯科,不明
医療法人社団心音会こどもの歯科｜祐天寺 歯医者・小児歯科/小児矯正,鈴木花子
...
```

### 進捗表示
```
[1/107] おとなとこどもの経堂歯科
  → WebFetch: https://www.otonatokodomo-kyodo-dental.com/
  ✓ 院長名: 山田太郎 (source: webfetch)

[2/107] 原宿こども歯科
  → WebFetch: https://www.hk-dental.net/
  × 院長名: 見つかりません
  → WebSearch: 原宿こども歯科 院長
  ✓ 院長名: 佐藤次郎 (source: websearch)

[3/107] 医療法人社団心音会...
  → WebFetch: https://kodomonoshika.net/?utm_source=mybusiness
  ✓ 院長名: 鈴木花子 (source: webfetch)
```

## 注意事項

### レート制限対策
- WebSearch/WebFetch実行後、2秒のインターバルを設ける
- 大量の連続リクエストを避ける

### エラーハンドリング
- **タイムアウト**: 「不明」として記録
- **接続エラー**: 「不明」として記録
- **403/404エラー**: 「不明」として記録
- **複数候補**: 最初の1名のみ

### データ品質
- 敬称は除外（「先生」「Dr.」など）
- 複数の敬称が付いている場合は除外
- 氏名の妥当性チェック（1-30文字）

## タイムライン
- **STEP 1**: 最初の10医院 → 約30秒（2秒×10 + 処理時間）
- **STEP 2**: 残り97医院 → 約3-5分（処理効率に依存）
- **総処理時間**: 約4-6分

## 出力先
- CSV: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_1.csv`
- ログ: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/collection_log.txt`（オプション）
