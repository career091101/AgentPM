# Clinic Address Normalizer

Google Maps Platform（Places API New / Geocoding API）を使った医院データの住所・郵便番号正規化ツール

## 概要

入力CSVに記載された医院データ（医院名＋都道府県など）から、Google Maps APIを使って以下を取得・正規化します：

- `place_id`: Google Maps上の一意識別子
- `display_name`: 施設名
- `formatted_address`: 正規化された住所
- `postal_code`: 郵便番号
- `lat`, `lng`: 緯度・経度
- `match_confidence`: マッチ信頼度（high/mid/low）
- `needs_manual_review`: 手動レビュー要否（true/false）

## 必要なもの

### 1. Google Maps Platform APIキー

以下のAPIを有効化したAPIキーが必要です：

- **Places API (New)** - Text Search, Place Details
- **Geocoding API** - 郵便番号補完用（オプション）

APIキーの取得方法: https://developers.google.com/maps/documentation/places/web-service/cloud-setup

### 2. Pythonライブラリ

```bash
pip install -r requirements.txt
```

## インストール

```bash
cd Flow/202601/2026-01-02/clinic_address_normalizer
pip install -r requirements.txt
```

## 使い方

### 1. APIキーの設定

```bash
export GOOGLE_MAPS_API_KEY='your_api_key_here'
```

または `.env` ファイルに記載して読み込む：

```bash
# .env
GOOGLE_MAPS_API_KEY=your_api_key_here
```

### 2. 入力CSVの準備

以下のカラムを持つCSVを準備します：

| カラム名 | 必須 | 説明 | 例 |
|---------|------|------|-----|
| `clinic_query` | ✅ | 医院名 | `田中歯科クリニック` |
| `prefecture` | ✅ | 都道府県 | `東京都` |
| `city` | | 市区町村（任意、精度向上） | `渋谷区` |
| `area_hint` | | 地域ヒント（任意） | `恵比寿` |
| `google_maps_url` | | Google MapsのURL（任意、place_id抽出用） | `https://maps.google.com/?q=place_id:ChIJ...` |

**サンプル**: `sample_input.csv` を参照

### 3. 実行

```bash
python main.py input.csv output.csv
```

### 4. 出力CSVの確認

出力CSVには、入力カラムに加えて以下が追加されます：

| カラム名 | 説明 |
|---------|------|
| `place_id` | Google Maps上の一意識別子 |
| `display_name` | 施設名 |
| `formatted_address` | 正規化された住所 |
| `postal_code` | 郵便番号（例: `150-0013`） |
| `lat` | 緯度 |
| `lng` | 経度 |
| `match_confidence` | マッチ信頼度（`high`/`mid`/`low`） |
| `needs_manual_review` | 手動レビュー要否（`true`/`false`） |
| `error_code` | エラーコード（エラー時のみ） |
| `error_message` | エラーメッセージ（エラー時のみ） |

## APIの優先順位と処理フロー

### フロー図

```
1. google_maps_url から place_id 抽出
   ├─ place_id が取得できた
   │   └─→ [4. Place Details] へ
   │
   └─ place_id が取得できない
       └─→ [2. Places Text Search]
           ├─ 候補なし → エラー
           └─ 候補あり
               └─→ [3. 候補スコアリング]
                   └─→ [4. Place Details]
                       ├─ postal_code あり → 完了
                       └─ postal_code なし
                           └─→ [5. Geocoding API で補完] → 完了
```

### 1. google_maps_url から place_id 抽出

- `google_maps_url` カラムに Google Maps URL が記載されている場合、URLから `place_id` を抽出
- 対応パターン: `place_id:ChIJ...`, `place_id=ChIJ...`
- place_id が取得できた場合、**Places Text Search をスキップ**して直接 Place Details へ

### 2. Places Text Search (New)

- `{clinic_query} {prefecture} {city} {area_hint}` をクエリとして検索
- 最大5件の候補を取得
- FieldMaskは最小限（`places.id,places.displayName,places.formattedAddress,places.location`）

### 3. 候補スコアリング

取得した候補を以下の基準でスコアリング：

| 条件 | スコア |
|------|--------|
| `formattedAddress` に `prefecture` 含む | +2 |
| `displayName` に `clinic_query` の主要語一致 | +2 |
| `formattedAddress` に `city` 含む（任意） | +1 |

- 上位1件を採用
- **スコアが2未満**（都道府県不一致）または **僅差**（2位とのスコア差1以下）の場合、`needs_manual_review=true` に設定

### 4. Place Details (New)

- `place_id` を使って詳細情報を取得
- FieldMaskは最小限（`id,displayName,formattedAddress,addressComponents,location`）
- `addressComponents` から `postal_code` を抽出
- **キャッシュ機能**: 同じ `place_id` は1回のみAPIを呼び出し（重複削減）

### 5. Geocoding API（補完のみ）

- Place Details で `postal_code` が取得できなかった場合のみ実行
- `formatted_address` を使って郵便番号を補完

## match_confidence の判定基準

| 信頼度 | 条件 |
|--------|------|
| `high` | ✅ postal_code あり ＆ ✅ prefecture 一致 ＆ ✅ 手動レビュー不要 |
| `mid` | ✅ postal_code あり または ✅ prefecture 一致、ただし手動レビュー不要 |
| `low` | ⚠️ needs_manual_review=true（スコア低い、僅差、県不一致等） |

## エラーハンドリング

### Rate Limit (429)

- **指数バックオフ**: 最大5回リトライ（待機時間: 2秒、4秒、8秒、16秒、32秒）
- 5回リトライしても失敗した場合、`error_code=RATE_LIMIT` を記録して次の行へ

### タイムアウト

- **タイムアウト時間**: 20秒
- 最大5回リトライ
- リトライ後も失敗した場合、`error_code=TIMEOUT` を記録

### ネットワークエラー

- 最大2回リトライ
- リトライ後も失敗した場合、`error_code=NETWORK_ERROR` を記録

### エラーコード一覧

| error_code | 説明 |
|------------|------|
| `NO_CANDIDATES` | Places Text Search で候補が見つからなかった |
| `NO_PLACE_ID` | place_id を取得できなかった |
| `PLACE_DETAILS_FAILED` | Place Details API が失敗した |
| `RATE_LIMIT` | Rate Limit（429）でリトライ上限に達した |
| `TIMEOUT` | タイムアウトでリトライ上限に達した |
| `NETWORK_ERROR` | ネットワークエラーでリトライ上限に達した |
| `EXCEPTION` | その他の例外が発生した |

## コスト最適化

### FieldMask の徹底使用

Places API (New) は **FieldMask で指定したフィールドのみ課金**されます。本ツールは以下の最小限のフィールドのみ取得：

- **Places Text Search**: `places.id,places.displayName,places.formattedAddress,places.location`
- **Place Details**: `id,displayName,formattedAddress,addressComponents,location`

**余計なフィールドを取得しないこと** = コスト削減

### キャッシュによる重複削減

- 同じ `place_id` は1回のみ Place Details を呼び出し
- 入力CSVに同じ医院が複数回出現しても、API呼び出しは1回のみ

### Geocoding API は最小限

- Place Details で `postal_code` が取得できた場合、Geocoding API は呼び出さない
- 補完が必要な場合のみ実行

## 運用注意事項

### 1. API使用量とコスト

2026年1月時点の料金（参考）：

- **Places Text Search (New)**: $32 / 1,000 requests（FieldMask次第）
- **Place Details (New)**: FieldMask次第（基本フィールドで約$17 / 1,000 requests）
- **Geocoding API**: $5 / 1,000 requests

**推定コスト例**:
- 1,000件の医院データ（google_maps_url なし）
  - Places Text Search: 1,000回 → $32
  - Place Details: 1,000回 → $17
  - Geocoding（50%が補完必要と仮定）: 500回 → $2.50
  - **合計: 約$51.50**

**コスト削減策**:
- `google_maps_url` を事前に収集しておくと Places Text Search をスキップできる
- 重複データを事前に削除

### 2. Rate Limit

- **Queries Per Second (QPS) 制限**: デフォルトで数十〜数百 QPS（APIキーの設定次第）
- 本ツールは **0.1秒間隔**（10 QPS）で実行されるため、通常の制限内で動作
- 大量データ（数万件）を処理する場合、バッチ分割を推奨

### 3. needs_manual_review=true の取り扱い

以下の場合、`needs_manual_review=true` となります：

- スコアが2未満（都道府県が一致しない）
- 2位とのスコア差が1以下（僅差）
- 候補が見つからなかった

**運用推奨**:
- `needs_manual_review=true` の行を抽出して手動確認
- Google Maps で目視確認して正しい `place_id` を手動設定

### 4. postal_code が取得できないケース

- **原因**: Google Maps に郵便番号が登録されていない（特に古いデータ）
- **対処**: Geocoding API で補完されるが、それでも取得できない場合は手動補完が必要

### 5. google_maps_url の形式

対応している URL 形式：
- `https://www.google.com/maps/place/.../?q=place_id:ChIJ...`
- `https://maps.google.com/?cid=12345...` ❌ 非対応（CIDはplace_idではない）
- `https://goo.gl/maps/...` ❌ 非対応（短縮URLの展開が必要）

**推奨**: Google Maps で施設を検索し、URLから `place_id` パラメータを含む形式をコピー

## トラブルシューティング

### `Error: GOOGLE_MAPS_API_KEY environment variable not set`

→ 環境変数を設定してください：

```bash
export GOOGLE_MAPS_API_KEY='your_api_key_here'
```

### `NO_CANDIDATES` エラーが多発

→ 以下を確認：
1. `clinic_query` が正確か（誤字脱字はないか）
2. `prefecture` が正しく設定されているか
3. `city` や `area_hint` を追加して検索精度を上げる

### `needs_manual_review=true` が多い

→ 入力データの品質を確認：
1. `clinic_query` に余計な情報が含まれていないか（「〒150-0013」等の住所が混在していないか）
2. `prefecture` が正確か
3. `google_maps_url` を事前に収集できないか

### 処理が遅い

→ 以下を確認：
1. Rate Limit に達していないか（ログに `[WARN] Rate limit (429)` が出ていないか）
2. ネットワーク遅延が大きい場合、タイムアウト時間を調整（`TIMEOUT = 20` を変更）

## ライセンス

MIT License

## 作成者

Claude Code / AIPM_v0 Project

## 更新履歴

- 2026-01-02: 初版作成
