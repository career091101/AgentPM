# 院長名収集実装ガイド

このドキュメントでは、Claude CodeでWebFetch/WebSearchを使用して107医院の院長名を収集する詳細な実装手順を記載します。

---

## 実装方針

### 使用ツール

1. **WebFetch**: 公式ウェブサイトからの直接取得
2. **WebSearch**: 公開検索エンジンでの検索
3. **Grep**: 텍스트 抽出と整形

### 実行戦略

**全107医院を効率的に処理するため、以下の2つの方法を推奨します:**

#### 方法A: 逐次処理（推奨 - 確実性重視）

```
医院1 → WebFetch/WebSearch → 院長名抽出 → 記録
     ↓ 2秒待機
医院2 → WebFetch/WebSearch → 院長名抽出 → 記録
     ↓ 2秒待機
...
医院107 → WebFetch/WebSearch → 院長名抽出 → 記録
```

**実行時間**: 約8-10分
**メリット**: 安定性が高い、レート制限対策が確実
**デメリット**: 時間がかかる

#### 方法B: バッチ並列処理（高速化 - 時間優先）

3-5グループに分割して並列実行：

```
グループ1 (医院1-21)    → 並列実行 → 3-4分
グループ2 (医院22-42)   → 並列実行 → 3-4分
グループ3 (医院43-63)   → 並列実行 → 3-4分
グループ4 (医院64-84)   → 並列実行 → 3-4分
グループ5 (医院85-107)  → 並列実行 → 3-4分
```

**総実行時間**: 約4-5分（並列実行）
**メリット**: 高速処理
**デメリット**: 複雑性増加、API制限でブロックされる可能性

---

## 実装手順

### Step 1: 医院データの準備

出力先ディレクトリで医院リストを確認：

```bash
cd /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04

# 医院リスト（collect_directors_batch_2.py内に組み込み）
cat collect_directors_batch_2.py | grep "^DENTAL_CLINICS" -A 150 | head -20
```

### Step 2: 手動WebFetch検索パターン

**最初の5医院でパターン確認:**

#### 医院1: むらつ歯科クリニック

```
URL: https://muratsu-dc.jp/

1. WebFetch実行:
```

実装例：

```markdown
/fetch https://muratsu-dc.jp/

クエリ: ページから「院長」「理事長」キーワードを検索し、前後50文字を抽出
```

**期待される結果**:
```
院長: 村津太郎（敬称削除後）
```

#### 医院2: 博多矯正歯科KITTE博多院

```
URL: https://www.hakatakyousei.com/

WebFetch実行:
```

#### 医院3: Oh my teeth 福岡博多矯正歯科

```
URL: https://www.oh-my-teeth.com/locations/hakata/

WebFetch実行:
```

#### 医院4: MC天神こが歯科・矯正歯科

```
URL: https://mctenjin-kogadental.com/

WebFetch実行:
```

#### 医院5: Sagan歯科こども歯科医院

```
URL: https://sagan-dental.com/

WebFetch実行:
```

### Step 3: 院長名抽出ロジック

#### パターンA: 「院長」タグで抽出

```
HTML: <span class="director">山田太郎</span>

処理:
1. 「院長」の後ろ30文字を抽出
2. HTMLタグを削除
3. 改行・余分なスペースを削除
4. 氏名部分（漢字のみ）を抽出
→ 「山田太郎」
```

#### パターンB: 「理事長」タグで抽出

```
HTML: <p>当診療所の理事長は<strong>鈴木花子</strong>です</p>

処理:
1. 「理事長」の後ろテキストを抽出
2. HTMLタグを削除
3. 氏名部分を特定
→ 「鈴木花子」
```

#### パターンC: 人物紹介セクション

```
HTML:
<div class="staff">
  <h3>院長紹介</h3>
  <p>佐藤次郎医学博士</p>
</div>

処理:
1. 「院長」「紹介」セクションを特定
2. テキスト抽出
3. 「医学博士」などの敬称を削除
→ 「佐藤次郎」
```

### Step 4: WebSearch フォールバック

**WebFetchで見つからない医院の場合:**

```markdown
/search [医院名] 院長

例:
/search むらつ歯科クリニック 院長
```

**検索結果から院長名を抽出:**

```
検索結果スニペット:
"むらつ歯科クリニックの院長は村津太郎です。..."

処理:
1. 「院長は」の後ろテキストを抽出
2. 敬称を削除
3. 氏名を確定
→ 「村津太郎」
```

---

## 実装例（Claude Code内）

### シンプルな逐次処理実装

```python
# Claude Code Executableコード

import csv
import time
import json
from datetime import datetime

def collect_director_names():
    """メイン処理関数"""

    # 医院リスト（簡略版 - 最初の10医院）
    clinics = [
        ("むらつ歯科クリニック", "https://muratsu-dc.jp/"),
        ("博多矯正歯科KITTE博多院", "https://www.hakatakyousei.com/"),
        ("Oh my teeth 福岡博多矯正歯科", "https://www.oh-my-teeth.com/locations/hakata/"),
        ("MC天神こが歯科・矯正歯科", "https://mctenjin-kogadental.com/"),
        ("Sagan歯科こども歯科医院", "https://sagan-dental.com/"),
        # ... 残り102医院
    ]

    results = []

    for idx, (clinic_name, website_url) in enumerate(clinics, 1):
        print(f"[{idx}] {clinic_name} を処理中...")

        director_name = "不明"

        # Step 1: WebFetchで公式サイトから検索
        if website_url:
            try:
                # WebFetch でページ取得
                page_content = fetch(website_url)

                # 院長キーワード検索
                if "院長" in page_content:
                    # 院長の前後テキストを抽出
                    idx_keyword = page_content.find("院長")
                    context = page_content[max(0, idx_keyword-50):min(len(page_content), idx_keyword+100)]

                    # 敬称削除と氏名抽出
                    director_name = extract_director_name(context)

                elif "理事長" in page_content:
                    # 理事長で検索
                    idx_keyword = page_content.find("理事長")
                    context = page_content[max(0, idx_keyword-50):min(len(page_content), idx_keyword+100)]
                    director_name = extract_director_name(context)

            except Exception as e:
                print(f"  ⚠️  WebFetch失敗: {str(e)}")

        # Step 2: WebSearchでフォールバック
        if director_name == "不明" and website_url:
            try:
                search_query = f"{clinic_name} 院長"
                search_results = search(search_query)

                if search_results:
                    # 最初の結果から名前抽出
                    snippet = search_results[0].get('snippet', '')
                    director_name = extract_director_from_snippet(snippet)

            except Exception as e:
                print(f"  ⚠️  WebSearch失敗: {str(e)}")

        # Step 3: 結果記録
        results.append({
            "clinic_name": clinic_name,
            "director_name": director_name
        })

        print(f"  → 院長名: {director_name}")

        # レート制限対策: 2秒待機
        if idx < len(clinics):
            time.sleep(2)

    return results


def extract_director_name(context):
    """コンテキストから院長名を抽出"""

    # 敬称削除
    for honorific in ["Dr.", "先生", "医学博士", "院長", "理事長"]:
        context = context.replace(honorific, "")

    # 改行・余分なスペース削除
    context = context.strip().replace("\n", " ")

    # 最初の氏名部分を抽出（スペースまで）
    name = context.split()[0] if context.split() else ""

    return name if len(name) > 1 else "不明"


def extract_director_from_snippet(snippet):
    """検索スニペットから院長名を抽出"""

    if "院長" in snippet:
        idx = snippet.find("院長")
        context = snippet[idx:idx+50]
        return extract_director_name(context)

    return "不明"


# メイン実行
if __name__ == "__main__":
    results = collect_director_names()

    # CSV出力
    output_file = "director_names_batch_2.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['clinic_name', 'director_name'])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✓ 完了: {output_file} に {len(results)} 件の結果を保存")
```

---

## 検証方法

### 方法1: 手動検証（最初の5医院）

```bash
# 医院1の院長名を Google で確認
https://www.google.com/search?q=むらつ歯科クリニック+院長

# 医院2の院長名を確認
https://www.google.com/search?q=博多矯正歯科KITTE博多院+院長

# ... 医院3-5
```

### 方法2: 自動検証スクリプト

```python
import csv

def validate_results(csv_file):
    """出力ファイルの整合性チェック"""

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"総医院数: {len(rows)}")

    # 「不明」の件数
    unknown_count = sum(1 for row in rows if row['director_name'] == '不明')
    print(f"「不明」: {unknown_count} 件 ({unknown_count/len(rows)*100:.1f}%)")

    # 敬称が残っている件数
    honorific_count = sum(
        1 for row in rows
        if 'Dr.' in row['director_name'] or '先生' in row['director_name']
    )
    print(f"敬称が残っている: {honorific_count} 件")

    # 複数名が含まれている件数
    comma_count = sum(1 for row in rows if '、' in row['director_name'])
    print(f"複数名含む: {comma_count} 件")

    # サンプル表示
    print("\n最初の10行:")
    for i, row in enumerate(rows[:10], 1):
        print(f"  {i}. {row['clinic_name']} → {row['director_name']}")
```

---

## トラブルシューティング

### 問題1: WebFetchがタイムアウト

**症状**: 医院のWebサイトが応答しない

**対応**:
```python
try:
    page_content = fetch(url, timeout=5)
except TimeoutError:
    # WebSearchにフォールバック
    director_name = search_director(clinic_name)
```

### 問題2: 院長名が複数候補

**症状**: 「山田太郎、田中花子」のように複数名が抽出される

**対応**:
```python
# 最初の1名のみ抽出
director_name = director_name.split('、')[0].split(',')[0]
```

### 問題3: 敬称が削除されない

**症状**: 出力に「Dr. 山田太郎」が含まれる

**対応**:
```python
# 削除ロジックの拡張
remove_patterns = [
    "Dr.",
    "先生",
    "医学博士",
    "医博",
    "Ph.D",
    "（代表）",
]
for pattern in remove_patterns:
    text = text.replace(pattern, "")
```

---

## 完了基準

実装が完了したと判断する基準:

- [ ] 107医院すべてがCSVに記録されている
- [ ] 「不明」が20%程度（21医院程度）である
- [ ] 敬称が削除されている
- [ ] 複数候補がある場合、1名のみが記録されている
- [ ] ファイルがUTF-8で保存されている
- [ ] 実行時間が10分以内である

---

## 参考資料

### WebFetch 使用方法

```markdown
/fetch [URL]

例: /fetch https://muratsu-dc.jp/
```

### WebSearch 使用方法

```markdown
/search [クエリ]

例: /search むらつ歯科クリニック 院長
```

---

## 次のステップ

1. **正規表現による敬称削除の高度化**
   - 正規表現で複数パターンの敬称に対応
   - 漢字抽出の精度向上

2. **キャッシングの実装**
   - 同じURL/クエリへのリクエストをキャッシュ
   - 処理時間の短縮

3. **品質スコアリング**
   - WebFetch vs WebSearch の信頼度を異ならせる
   - WebFetchで見つかった場合のスコア: 100
   - WebSearchで見つかった場合のスコア: 80
   - 「不明」のスコア: 0

---

**完了日**: 2026-01-04
**処理医院数**: 107
**推定実行時間**: 8-10分
**出力ファイル**: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv`
