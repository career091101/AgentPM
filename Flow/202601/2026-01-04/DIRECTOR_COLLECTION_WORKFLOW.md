# 歯科医院院長名収集タスク - ワークフロー定義

**実施期間**: 2026-01-04
**対象範囲**: CSVファイル 行108-214（107医院）
**出力ファイル**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv`

---

## タスク概要

歯科医院リストCSVファイルの行108-214（107医院）から、各医院の院長名をインターネット検索で収集し、CSV形式で出力します。

### データソース

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/歯科医院リスト - nationwide_45prefectures_split_address_20260102_233408.csv.csv`

**医院数**: 107医院（行108-214）

**データ列**:
- 医院名
- 公式ウェブサイトURL（存在する場合）
- 住所
- 評価
- 口コミ数

---

## 実装手順

### Step 1: 医院情報抽出（既完了）

CSVファイルから行108-214のデータを抽出し、以下の情報を収集：
- 医院名
- 公式ウェブサイトURL

**処理済み医院一覧** (107医院):
1. むらつ歯科クリニック
2. 博多矯正歯科KITTE博多院
3. Oh my teeth 福岡博多矯正歯科
...
107. カーナデンタル＆ビューティークリニック

### Step 2: 院長名検索（実装中）

各医院について以下を実施:

#### 2-1. 公式ウェブサイト検索（第1選択肢）

**条件**: URLが存在し、アクセス可能な場合

**処理フロー**:

```
1. WebFetch でURLを取得
   ↓
2. 以下のキーワードをHTML/テキスト内で検索:
   - 院長
   - 理事長
   - Dr.
   - 医学博士
   - 代表医師
   ↓
3. キーワード周辺のテキスト（前後50文字）を抽出
   ↓
4. 敬称（Dr., 先生等）を削除し、氏名のみ抽出
   ↓
5. 複数候補がある場合は最初の1名のみ記録
```

**実装例** (Python/Claude Code):

```python
import requests
from bs4 import BeautifulSoup

def extract_director_from_website(url: str) -> Optional[str]:
    """Extract director name from clinic website."""

    try:
        # WebFetch を使用してページ内容取得
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        text = response.text.lower()

        # 院長キーワード検索
        keywords = ['院長', '理事長', 'dr.', '医学博士']

        for keyword in keywords:
            if keyword in text:
                # キーワード周辺テキスト抽出
                idx = text.find(keyword)
                context = text[max(0, idx-50):min(len(text), idx+100)]

                # 敬称削除
                name = context.replace('dr.', '').replace('先生', '')
                name = name.strip().split('\n')[0]

                if name and len(name) > 1:  # 有効な名前か確認
                    return name

        return None

    except Exception as e:
        print(f"⚠️ WebFetch失敗: {url} - {str(e)}")
        return None
```

#### 2-2. 公開検索エンジン検索（第2選択肢）

**条件**: 公式サイトで院長名が見つからない、またはURLがない場合

**処理フロー**:

```
1. WebSearch で "[医院名] 院長" を検索
   ↓
2. 検索結果から院長名を抽出
   ↓
3. 複数結果がある場合は最初の1つのみ
```

**実装例**:

```python
def search_director_by_name(clinic_name: str) -> Optional[str]:
    """Search for director name using search engine."""

    try:
        # WebSearch を使用
        query = f"{clinic_name} 院長"
        results = websearch(query)

        if results and len(results) > 0:
            # 最初の結果から院長名抽出
            first_result = results[0]['snippet']

            # キーワード検索
            if '院長' in first_result:
                idx = first_result.find('院長')
                context = first_result[max(0, idx-20):min(len(first_result), idx+50)]
                name = context.replace('院長', '').strip()

                if name:
                    return name

        return None

    except Exception as e:
        print(f"⚠️ WebSearch失敗: {clinic_name} - {str(e)}")
        return None
```

#### 2-3. 不明の記録（第3選択肢）

**条件**: WebFetch と WebSearch の両方で見つからない場合

**記録内容**: 「不明」

### Step 3: レート制限対策

**実装**: 各医院の検索間隔を **2秒** に設定

```python
import time

for clinic in clinics:
    process_clinic(clinic)
    time.sleep(2)  # 2秒待機
```

**効果**:
- サーバー負荷軽減
- 検索エンジンブロック回避
- タイムアウト減少

### Step 4: エラーハンドリング

#### タイムアウト処理

**条件**: WebFetch/WebSearchが5秒以上応答しない場合

**対応**: 「不明」として記録

```python
def fetch_with_timeout(url: str, timeout: int = 5) -> Optional[str]:
    """Fetch with timeout handling."""
    try:
        response = requests.get(url, timeout=timeout)
        return response.text
    except requests.Timeout:
        print(f"⚠️ タイムアウト: {url}")
        return None
    except Exception as e:
        print(f"⚠️ エラー: {str(e)}")
        return None
```

#### ネットワークエラー処理

**条件**: 接続エラーやDNS失敗

**対応**: 「不明」として記録（リトライ不実施）

---

## 出力ファイル形式

### CSV形式

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv`

**カラム**:
1. `医院名` - 医院の正式名称
2. `院長名` - 検索で見つかった院長名（敬称なし）

### データ例

```csv
医院名,院長名
むらつ歯科クリニック,村津太郎
博多矯正歯科KITTE博多院,山田花子
Oh my teeth 福岡博多矯正歯科,不明
MC天神こが歯科・矯正歯科,小賀健太
...
```

### 院長名の形式

- **正常な例**: `山田太郎`, `鈴木花子`
- **敬称あり（削除対象）**: `Dr. 山田太郎`, `山田太郎先生`
- **複数候補（最初の1名のみ）**: `山田太郎（代表）` → `山田太郎`
- **見つからない場合**: `不明`

---

## 実装体系

### 対象医院（107医院）の地域分布

```
九州地方:
- 福岡県: むらつ歯科クリニック 他（行108-120）
- 佐賀県: Sagan歯科こども歯科医院 他（行112-121）
- 長崎県: 田口歯科医院 他（行122-128）
- 熊本県: ひかる歯科ちえこども歯科 他（行130-149）
- 大分県: たけお歯科クリニック 他（行150-156）
- 宮崎県: 宮崎台デンタルクリニック 他（行157-160）
- 鹿児島県: ななつ星歯科 他（行161-171）

東北地方:
- 青森県: 松尾歯科･おとなこども矯正歯科 他（行172-177）
- 岩手県: 盛岡となん歯科 他（行178-182）
- 宮城県: 泉中央おとなこども歯科 他（行183-196）
- 秋田県: クローバーデンタル 他（行197-200）
- 山形県: ティーズデンタルオフィス 他（行201-210）
- 福島県: 須賀川みらい歯科クリニック 他（行211-214）
```

---

## パフォーマンス予測

### 処理時間

```
医院数: 107
検索間隔: 2秒/医院
平均WebFetch時間: 3秒
平均WebSearch時間: 2秒
エラー率: 20%（21医院）

計算式:
- WebFetch成功: 80医院 × 3秒 = 240秒
- WebSearch実行: 27医院 × 2秒 = 54秒
- 待機時間: 106 × 2秒 = 212秒
-------
合計: 506秒 ≈ **8-9分**
```

### API使用量

**WebFetch**: 80リクエスト（Web取得）
**WebSearch**: 27リクエスト（検索エンジン）
**合計**: 107リクエスト

---

## 品質管理

### 検証基準

1. **完全性**: 107医院すべてがCSVに記録されている ✓
2. **形式統一**: 敬称が削除されている ✓
3. **エラーハンドリング**: タイムアウト時は「不明」として記録 ✓
4. **レート制限**: 2秒間隔が維持されている ✓

### テスト方針

- **手動テスト**: 最初の5医院を実施して動作確認
- **自動検証**: 出力CSVの行数確認（107行 + ヘッダー = 108行）
- **サンプル検査**: ランダムに10医院選択して院長名の妥当性確認

---

## 注意事項

### ✅ 推奨される実装

- WebFetchで公式サイトを優先的に確認
- 見つからない場合にWebSearchで検索
- 2秒のインターバルでレート制限対策
- タイムアウトエラーは「不明」として記録
- 敬称（Dr., 先生等）は削除
- 複数候補がある場合は最初の1名のみ

### ❌ 避けるべき実装

- WebSearchを最初に使用（精度低下）
- インターバルなしでの連続リクエスト（ブロック危険）
- タイムアウト時のリトライ（無意味、「不明」で対応）
- 敬称を含めたまま記録
- 複数名をコンマ区切りで記録（指定は1名のみ）

---

## 参考情報

### 使用API

**WebFetch**: Claude Code組み込みツール
- 単一URLのコンテンツ取得
- Markdown変換機能あり
- タイムアウト: 30秒

**WebSearch**: Claude Code組み込みツール
- 複数の検索結果を返却
- スニペット表示機能あり
- 最新情報に対応

### 関連スクリプト

`/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/collect_directors_batch_2.py`

---

## チェックリスト

実装前の確認:

- [ ] CSVファイル読み込み確認（行108-214）
- [ ] 出力ディレクトリ作成確認（`Flow/202601/2026-01-04/`）
- [ ] WebFetch/WebSearch動作確認（テスト5医院）
- [ ] 2秒インターバル実装確認
- [ ] エラーハンドリング実装確認（タイムアウト→「不明」）
- [ ] 敬称削除ロジック確認
- [ ] CSV出力形式確認（医院名, 院長名）

実装後の検証:

- [ ] 出力CSVファイル存在確認
- [ ] 行数確認（107医院 + ヘッダー）
- [ ] ランダムサンプル5医院の院長名妥当性確認
- [ ] 「不明」の件数確認（20%程度が目安）
- [ ] 出力ファイルのエンコーディング確認（UTF-8）

---

## 実行コマンド

```bash
cd /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04

# スクリプト実行
python3 collect_directors_batch_2.py

# 出力確認
cat director_names_batch_2.csv | head -20

# 統計情報
wc -l director_names_batch_2.csv
```

---

## 成果物

**最終出力**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv`

**期待される結果**:
- 107医院の院長名リスト
- 85医院程度の成功（79%）
- 22医院程度の「不明」（21%）

---

## 関連ドキュメント

- **元データ**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/歯科医院リスト - nationwide_45prefectures_split_address_20260102_233408.csv.csv`
- **処理スクリプト**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/collect_directors_batch_2.py`
- **出力ファイル**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv`
