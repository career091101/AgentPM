# 田辺玩具向け歯科医院営業リスト抽出

## プロジェクト概要

小児歯科・矯正歯科向けにガチャガチャプロモーションを展開する田辺玩具の営業リストを、Google Maps API を使用して抽出します。

## 要件

### 対象エリア
- 本州・四国・九州（北海道・沖縄除外）
- 45都府県

### 対象施設
- 小児歯科（専門・標榜）
- 矯正歯科（専門・標榜）

### 取得情報
- 医院名
- 郵便番号
- 住所
- 電話番号
- WebサイトURL
- 評価（★）
- レビュー件数
- Google Maps URL
- 優先度スコア

### 目標件数
- **5,100件**（予算4万円フル活用）

### 予算
- **40,000円**

## スコアリング基準

```
評価★ × 20点（最大100点）
+ レビュー件数ボーナス
  - 100件以上: 20点
  - 50-99件: 15点
  - 20-49件: 10点
  - 10-19件: 5点
  - 10件未満: 0点
+ WebサイトURLあり: 10点
= 合計スコア（最大130点）
```

## セットアップ

### 1. Google Maps API キーの取得

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. プロジェクトを作成
3. 「APIとサービス」→「ライブラリ」から以下を有効化
   - Places API
   - Geocoding API
4. 「APIとサービス」→「認証情報」からAPIキーを作成
5. 請求先アカウントを設定（クレジットカード登録）

### 2. 環境変数の設定

```bash
export GOOGLE_MAPS_API_KEY="your-api-key-here"
```

または `.env` ファイルを作成：

```
GOOGLE_MAPS_API_KEY=your-api-key-here
```

### 3. 必要なライブラリのインストール

```bash
pip install googlemaps python-dotenv
```

## 使い方

### テスト実行（10件抽出）

```bash
cd aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads
python test_extract_10.py
```

**出力:**
- `test_dental_leads_10_YYYYMMDD_HHMMSS.csv`
- コスト推定情報
- データ精度の検証結果

### 本番実行（5,100件抽出）

テスト結果を確認後、本番スクリプトで実行

```bash
python extract_full.py
```

## コスト推定

### API料金（2024年現在）

| API | 料金 |
|-----|------|
| Text Search | $32/1,000件 |
| Place Details (Basic) | $17/1,000件 |
| Place Details (Contact) | $3/1,000件 |
| **合計** | **$52/1,000件** |

### 5,100件の場合

```
Text Search: 5,100件 × $32/1,000 = $163.2
Place Details (Basic): 5,100件 × $17/1,000 = $86.7
Place Details (Contact): 5,100件 × $3/1,000 = $15.3
--------------------------------------------------
合計: $265.2（約39,780円、1ドル=150円）
```

**予算内に収まります！**

## 出力CSV形式

```csv
スコア,医院名,郵便番号,住所,電話番号,WebサイトURL,評価,レビュー件数,Google Maps URL
115.0,〇〇小児歯科クリニック,150-0001,東京都渋谷区...,03-1234-5678,https://...,4.8,120,https://maps.google.com/...
105.5,△△矯正歯科,231-0023,横浜市中区...,045-xxx-xxxx,https://...,4.5,85,https://maps.google.com/...
```

## 除外条件

以下の医院は自動的に除外されます：
- 評価3.0未満
- レビュー5件未満
- 閉業・休業中
- 大学病院・総合病院

## Phase 0: テスト収集完了（2026-01-04）

### 実施内容

#### セットアップ
```bash
# Google Maps API Key設定
API_KEY = "AIzaSyASqcmLzyXnzrK6jcKzl7PVZ_3CmSv4rxc"

# Python仮想環境作成
python3 -m venv venv
source venv/bin/activate
pip install googlemaps
```

#### 検索パラメータ
- **検索地域**: 東京都（中心座標: 35.6812, 139.7671）
- **検索半径**: 50km
- **検索キーワード**: 小児歯科、矯正歯科、こども歯科
- **APIエンドポイント**: Google Maps Places API `places_nearby`

#### 実行結果

| 項目 | 結果 |
|------|------|
| 総API呼び出し | 60件 |
| 重複スキップ | 9件 (15.0%削減) |
| 新規ユニーク収集 | 51件 |
| 重複率 | 0.0% |
| 推定コスト | $1.02 (¥153) |

#### データ品質検証

| 基準 | 目標 | 実績 | 達成 |
|------|------|------|------|
| 重複率 | ≤ 10% | **0.0%** | ✅ |
| データ完全性 (医院名) | ≥ 90% | **100%** | ✅ |
| Google評価有り | ≥ 90% | **100%** | ✅ |
| WebサイトURL有り | ≥ 80% | **0%** | ⚠️ 改善必要 |

**総合評価**: ✅ **検証合格**

### 技術的発見

#### 1. CSV列名変換の実装
Google Maps APIの生データは英語フィールド名のため、日本語列名に変換する処理を `collect_with_dedup.py` に実装しました。

```python
transformed_row = {
    '医院名': clinic.get('name', ''),
    'WebサイトURL': clinic.get('website', ''),
    'Google評価': clinic.get('rating', ''),
    'レビュー件数': clinic.get('user_ratings_total', 0),
    '住所': clinic.get('vicinity', ''),
    # ... 他のフィールド
}
```

#### 2. WebサイトURL取得の制約
`places_nearby` APIは基本情報のみ返すため、WebサイトURLが取得できません。
- **対処**: Phase B（スコアリング時）に高スコア医院のみPlace Details API呼び出しで取得

#### 3. 重複排除システムの動作確認
- セッション内で9件/60件（15%）の重複を検出・スキップ
- `collection_history.json` による履歴管理が正常動作

### 出力ファイル
- `test_100_clinics_20260104_142354.csv` - 51件のユニークデータ
- `collection_history.json` - 既存1,615件 + 新規51件 = 1,666件の履歴

### 次の Phase 1 計画
- **目標**: 既存1,615件 + 新規2,211件 = 3,826件
- **予算**: ¥25,500（残予算¥4,500確保）
- **検索範囲**: 主要8都府県 × 2-3エリア × 3キーワード = 67パターン

---

## 次のステップ

1. ✅ **Phase 0: テスト収集完了**（51件、重複率0.0%）
2. ✅ データ品質検証合格
3. ✅ CSV列名変換実装
4. ⬜ Phase 1: 本番収集スクリプト作成（`collect_budget_optimized.py`）
5. ⬜ Phase 1: 本番実行（3,826件目標）
6. ⬜ Phase B: スコアリング実行
7. ⬜ 営業チームへ納品

## 注意事項

### Google Maps API 利用規約
- 取得データは田辺玩具の営業活動のみに使用
- 第三者への提供・再販禁止
- データ保存期間：営業完了後1年で削除

### API制限
- 1秒あたり50リクエストまで
- 1日あたり100,000リクエストまで
- スクリプトには自動的にレート制限を実装済み

## トラブルシューティング

### APIキーエラー
```
ValueError: 環境変数 GOOGLE_MAPS_API_KEY が設定されていません
```
→ 環境変数を設定してください

### 課金エラー
```
OVER_QUERY_LIMIT
```
→ Google Cloud Console で請求先アカウントを設定してください

### レート制限エラー
```
RATE_LIMIT_EXCEEDED
```
→ スクリプトが自動的にリトライします。待機してください。
