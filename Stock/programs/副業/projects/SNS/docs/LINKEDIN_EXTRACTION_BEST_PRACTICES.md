# LinkedIn投稿抽出のベストプラクティス

**作成日**: 2026-01-12
**対象スクリプト**: `scripts/late_api_multiplatform_v2.py`
**関数**: `extract_linkedin_posts()`

---

## 概要

このドキュメントは、Takano式7パターンで生成されたLinkedIn投稿Markdownファイルから3案を正確に抽出するためのベストプラクティスをまとめたものです。

**2026-01-12の重大バグ修正**により、案3抽出失敗による重複投稿問題が解決されました。

---

## 背景：2026-01-12に発生した問題

### 問題1: 案3が抽出されない

**症状**:
- `extract_linkedin_posts()` が2件しか返さない（案1、案2のみ）
- Late APIダッシュボードで同じ内容（案1または案2）が3件重複投稿される

**根本原因**:
```python
# 修正前（BROKEN）
if "## 投稿案3" in content:
    start_idx = content.find("## 投稿案3")
    end_idx = content.find("---", start_idx + 100)  # ← 問題箇所
    post3_section = content[start_idx:end_idx]

    if "### チェックリスト検証" in post3_section:  # ← 常にFalse
        # 抽出ロジック...
```

**なぜ失敗したか**:
1. `content.find("---", start_idx + 100)` が見つけた `---` は、投稿案3の**途中**にある区切り線
2. そのため `post3_section` には `### チェックリスト検証` が含まれず、抽出がスキップされた
3. 結果として `posts` リストには2件のみ追加され、3件目が空のまま

**具体例** (`posts_generated_takano_20260112_v2.md`):
- Line 137: `## 投稿案3` 開始
- Line 158: `---` 区切り線（コード内の `end_idx` がここを検出）
- Line 195: `### チェックリスト検証` セクション（ここが切り捨てられた）

### 問題2: 投稿数と日数の不一致

**症状**:
- `linkedin_posts` に2件、`linkedin_available_days` に3日分
- `zip(linkedin_posts, linkedin_available_days)` は2件しかループしない
- しかし、過去実行で3件投稿されていた（なぜか同じ内容が重複）

**根本原因**:
- `extract_linkedin_posts()` の抽出失敗（上記）により、2件しか返されない
- しかし、Late APIダッシュボードには3件投稿されていた
- 推測：過去実行時に何らかの方法で同じ投稿が3回送信された

---

## 修正内容（2026-01-12実装）

### 修正1: 案3抽出ロジックの書き直し（Lines 181-205）

```python
# 投稿案3を抽出
if "## 投稿案3" in content:
    start_idx = content.find("## 投稿案3")

    # チェックリスト検証セクションを探す（投稿案3内）
    checklist_idx = content.find("### チェックリスト検証", start_idx)
    if checklist_idx != -1:
        # チェックリスト検証が見つかった場合、その直前まで
        post3_text = content[start_idx:checklist_idx]
    else:
        # チェックリスト検証が見つからない場合、次の---または比較表セクションまで
        end_candidates = [
            content.find("---", start_idx + 100),
            content.find("## 比較表", start_idx),
            len(content)  # ファイル末尾
        ]
        # 有効なインデックス（-1以外）の中で最小値を取得
        end_idx = min([idx for idx in end_candidates if idx != -1])
        post3_text = content[start_idx:end_idx]

    # 見出し（## 投稿案3...）を除去
    post3_lines = post3_text.split("\n")[2:]  # 最初の2行（見出し+空行）をスキップ
    post3_clean = "\n".join(post3_lines).strip()

    # Markdown装飾を除去
    post3_clean = remove_markdown(post3_clean)

    # 空でない場合のみ追加
    if post3_clean:
        posts.append(post3_clean)

print(f"✅ LinkedIn: {len(posts)}投稿を抽出（Markdown除去済み）")
return posts
```

**改善ポイント**:
1. **直接 `### チェックリスト検証` を探す**: 固定の区切り文字に依存しない
2. **複数の終端候補**: `---`, `## 比較表`, ファイル末尾のいずれか最短
3. **空チェック**: 空の投稿を追加しない
4. **デバッグ出力**: 抽出件数をログ表示

### 修正2: 末尾の`---`区切り線除去（Fix 9: 2026-01-12追加）

**問題**: LinkedIn投稿の末尾に`---`区切り線が残る

**修正内容**: `remove_markdown()`関数に末尾の`---`除去ロジックを追加（Line 146）

```python
# --- 区切り線を末尾から除去（Fix 9: 2026-01-12追加）
text = re.sub(r'\n*---\s*$', '', text)
```

**正規表現の説明**:
- `\n*`: 0個以上の改行
- `---`: リテラル文字列「---」
- `\s*`: 0個以上の空白文字
- `$`: 文字列の末尾

**検証方法**:
```python
test_text = "投稿本文\n\n---\n"
result = remove_markdown(test_text)
assert result == "投稿本文"  # 末尾の---が除去される
```

### 修正3: 投稿数と日数の不一致チェック（Lines 461-474）

```python
# LinkedIn 3日分散投稿
print("LinkedIn 3日分散投稿:")

# 投稿数と利用可能日数の不一致チェック
if len(linkedin_posts) != len(linkedin_available_days):
    print(f"⚠️  警告: LinkedIn投稿数({len(linkedin_posts)})と利用可能日数({len(linkedin_available_days)})が一致しません")
    print(f"  → 投稿数に合わせて日数を調整します")
    linkedin_available_days = linkedin_available_days[:len(linkedin_posts)]

if len(linkedin_posts) == 0:
    print("⚠️  エラー: LinkedIn投稿が1件も抽出されていません")
else:
    for i, (content, scheduled_at) in enumerate(zip(linkedin_posts, linkedin_available_days), 1):
        post_id = f"top_{i}_linkedin"
        result = schedule_linkedin_post(content, scheduled_at, post_id)
        results.append(result)
```

**改善ポイント**:
1. **事前チェック**: `zip()` 実行前に長さを比較
2. **自動調整**: 日数リストを投稿数に合わせて切り詰める
3. **警告メッセージ**: ユーザーに問題を通知
4. **ゼロ件エラー**: 投稿が1件もない場合のエラーハンドリング

---

## ベストプラクティス

### 1. Markdown構造の仮定を最小限にする

**Bad**:
```python
# 固定の区切り文字に依存
end_idx = content.find("---", start_idx + 100)
```

**Good**:
```python
# セクション見出しを直接探す
checklist_idx = content.find("### チェックリスト検証", start_idx)
if checklist_idx != -1:
    post3_text = content[start_idx:checklist_idx]
```

### 2. 複数の終端候補を用意する

```python
# 終端候補のリスト
end_candidates = [
    content.find("---", start_idx + 100),    # 区切り線
    content.find("## 比較表", start_idx),    # 次のセクション
    len(content)                             # ファイル末尾
]

# 有効な（-1以外の）最小値
end_idx = min([idx for idx in end_candidates if idx != -1])
```

### 3. 空チェックを追加

```python
# 空でない場合のみ追加
if post3_clean:
    posts.append(post3_clean)
```

### 4. デバッグ出力を充実させる

```python
print(f"✅ LinkedIn: {len(posts)}投稿を抽出（Markdown除去済み）")
```

### 5. 投稿数と日数の事前検証

```python
# zip()実行前に長さチェック
if len(linkedin_posts) != len(linkedin_available_days):
    print(f"⚠️  警告: 投稿数({len(linkedin_posts)})と日数({len(linkedin_available_days)})不一致")
    linkedin_available_days = linkedin_available_days[:len(linkedin_posts)]
```

---

## テスト方法

### 単体テスト

```bash
cd /Users/yuichi/agentpm/Stock/programs/副業/projects/SNS

# extract_linkedin_posts()のテスト
python3 -c "
import sys
sys.path.append('scripts')
from late_api_multiplatform_v2 import extract_linkedin_posts

posts = extract_linkedin_posts()
print(f'\n抽出された投稿数: {len(posts)}')

for i, post in enumerate(posts, 1):
    print(f'\n【投稿{i}】冒頭100文字:')
    print(post[:100] if len(post) > 100 else post)
    print(f'\n文字数: {len(post)}')
"
```

**期待される出力**:
```
✅ LinkedIn: 3投稿を抽出（Markdown除去済み）

抽出された投稿数: 3

【投稿1】冒頭100文字:
AIエージェントの本質は「スキル」にある。
...
文字数: 1250

【投稿2】冒頭100文字:
「AIコーディングは補助ツールではない」松尾研究所の衝撃レポート
...
文字数: 1320

【投稿3】冒頭100文字:
AI時代のコードレビューは「人間がやるもの」じゃなくなった
...
文字数: 1180
```

### 統合テスト

```bash
# Late API予約投稿の実行（dry-run無し）
python3 scripts/late_api_multiplatform_v2.py

# 出力ファイル確認
cat data/late_api_v2_$(date +%Y%m%d).json | jq '.posts[] | select(.platform == "linkedin") | {post_id, status, post_id_late_api}'
```

**期待される出力**:
```json
{
  "post_id": "top_1_linkedin",
  "status": "scheduled",
  "post_id_late_api": "65f1c0a9e2b5af0012ab34cd"
}
{
  "post_id": "top_2_linkedin",
  "status": "scheduled",
  "post_id_late_api": "65f1c0a9e2b5af0012ab34de"
}
{
  "post_id": "top_3_linkedin",
  "status": "scheduled",
  "post_id_late_api": "65f1c0a9e2b5af0012ab34ef"
}
```

### Late APIダッシュボード検証

1. https://getlate.dev/dashboard/posts にアクセス
2. LinkedIn投稿を確認:
   - 3件すべてが**異なる内容**（案1、案2、案3）
   - 本文に `**` が含まれていない
   - 予約日時が正しい

---

## トラブルシューティング

### 問題: 抽出件数が2件のまま

**確認項目**:
1. `posts_generated_takano_*.md` に `## 投稿案3` セクションが存在するか？
2. 案3セクション内に `### チェックリスト検証` が存在するか？
3. コード内の `checklist_idx != -1` 条件が満たされているか？

**デバッグ方法**:
```python
# 案3セクションの位置を確認
with open("data/posts_generated_takano_20260112_v2.md", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find("## 投稿案3")
checklist_idx = content.find("### チェックリスト検証", start_idx)

print(f"案3開始位置: {start_idx}")
print(f"チェックリスト位置: {checklist_idx}")
print(f"セクション長: {checklist_idx - start_idx if checklist_idx != -1 else 'N/A'}")
```

### 問題: 投稿が空になる

**原因**: `post3_clean` が空文字列
**確認**: `post3_text.split("\n")[2:]` が空リストになっていないか？

**修正**:
```python
# 見出し行数を確認
post3_lines = post3_text.split("\n")
print(f"総行数: {len(post3_lines)}")
print(f"最初の3行: {post3_lines[:3]}")

# 見出しスキップ数を調整
post3_lines = post3_lines[1:]  # または [2:], [3:]
```

### 問題: Markdown記法が残る

**原因**: `remove_markdown()` が呼ばれていない、または不完全
**確認**: `post3_clean = remove_markdown(post3_clean)` が実行されているか？

**テスト**:
```python
from late_api_multiplatform_v2 import remove_markdown

test_text = "**太字**テスト、_イタリック_、`コード`"
result = remove_markdown(test_text)
print(result)  # 期待値: "太字テスト、イタリック、コード"
```

---

## 関連ファイル

| ファイル | 役割 |
|---------|------|
| `scripts/late_api_multiplatform_v2.py` | メインスクリプト（修正済み） |
| `data/posts_generated_takano_*.md` | 入力Markdownファイル |
| `data/late_api_v2_*.json` | 出力JSON（Late API結果） |
| `Flow/202601/2026-01-12/late_api_fixes_implementation_report.md` | 修正詳細レポート |

---

## まとめ

**重要な教訓**:
1. Markdown構造に依存する抽出ロジックは、セクション見出しを直接探す方が安全
2. 固定の区切り文字（`---`）は予測不可能な位置に出現する可能性がある
3. 投稿数と日数の不一致は、Late API重複投稿の原因になる
4. 空チェックとデバッグ出力は必須

**2026-01-12の修正により**:
- ✅ 案3が正確に抽出される
- ✅ 重複投稿が防止される
- ✅ 投稿数と日数の不一致が検出される

---

**作成者**: Claude Code (Sonnet 4.5)
**最終更新**: 2026-01-12
**バージョン**: 1.0
