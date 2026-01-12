# Late API LinkedIn投稿 - タイトル重複問題の根本原因分析

## 調査日時
2026-01-06

## 根本原因（確定）

### 問題の発生箇所
**投稿生成時点で既にタイトルが重複している**

### 詳細分析

#### 1. 投稿元データの構造（posts_generated_takano_20260105.md）

**案2の構造**:
```markdown
## 案2: パターン3（ニュース引用 → 深掘り解説 → 示唆）

### タイトル
**OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か**

### 本文（1,195文字）

OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が報じた衝撃のレポート。
...
```

**問題点**:
- **行65**: タイトル = `**OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か**`
- **行70**: 本文1行目 = `OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。`

👆 **本文の1行目にタイトルが既に含まれている**

#### 2. fix_late_api_multi_post.py の処理（68行目）

```python
# 完全なコンテンツ = タイトル + 本文（タイトル重複なし）
full_content = f"{title_clean}\n\n{body_clean}"
```

**処理フロー**:
1. 正規表現でタイトルと本文を抽出
   - `title_clean` = "OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か"
   - `body_clean` の1行目 = "OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。"
2. 結合処理
   - `full_content` = タイトル + "\n\n" + 本文
3. **結果**: タイトルが2回表示される

```
OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か

OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が報じた衝撃のレポート。
...
```

#### 3. 投稿生成スキルの意図

**generate-sns-posts-takano スキル**の出力フォーマット指示:
- `### タイトル`: 投稿のタイトル（太字Markdown）
- `### 本文（N文字）`: **タイトルを含む完全な投稿本文**

👆 **設計意図**: 本文1行目にタイトルを含めることで、LinkedIn投稿として完結した形式にする

#### 4. fix_late_api_multi_post.py の誤解

スクリプトは以下を想定していた:
- タイトルと本文は**分離されている**
- Late API投稿時に「タイトル + 本文」を結合する必要がある

**実際**:
- 本文に既にタイトルが含まれている
- Late API投稿時に再度タイトルを追加すると重複する

## 根本原因まとめ

### 原因1: 投稿生成スキルの設計
- 本文1行目にタイトルを含める設計（高野式パターンに準拠）
- これは**意図的な設計**であり、バグではない

### 原因2: fix_late_api_multi_post.py の誤った仮定
- 「タイトルと本文は分離されている」という誤った仮定
- `full_content = title + body` で重複が発生

### 原因3: late_api_post.py の extract_post_content() の同様の問題
- late_api_post.py:800-834 の `extract_post_content()` 関数も同じロジック
- タイトルを本文から除去せずに、そのまま使用している

## 影響範囲

### 影響を受けるスクリプト
1. `fix_late_api_multi_post.py` - 68行目
2. `late_api_post.py` - 800-834行目の `extract_post_content()` 関数
3. その他、同じロジックを使用している可能性のあるスクリプト

### 影響を受けるプラットフォーム
- **LinkedIn**: 確認済み（スクリーンショット）
- **Twitter/Threads**: 未確認（同じロジックの場合、同様の問題が発生する可能性）

## 修正方針

### オプション1: 投稿処理スクリプトの修正（推奨）

**修正内容**: `extract_variant_content()` 関数で、本文からタイトル1行目を除去

**メリット**:
- 投稿生成スキルの設計を変更する必要がない
- 既存の投稿データをそのまま使用できる
- 修正箇所が少ない（2-3ファイル）

**デメリット**:
- 本文の1行目が必ずタイトルと同じという仮定に依存

### オプション2: 投稿生成スキルの修正

**修正内容**: 本文1行目からタイトルを除去

**メリット**:
- データ構造が明確化（タイトルと本文が完全に分離）
- スクリプト側で複雑な処理が不要

**デメリット**:
- 既存の投稿データが使用不可（再生成が必要）
- スキル定義の大幅な変更が必要
- 高野式パターンの意図（タイトルと本文が一体）に反する可能性

### オプション3: Late API投稿時にタイトルを追加しない

**修正内容**: `full_content = body_clean` （タイトルを追加せず、本文のみを使用）

**メリット**:
- 最も簡単な修正（1行変更）
- 投稿生成スキルの設計意図（本文にタイトル含む）に合致

**デメリット**:
- タイトルフィールドが活用されない

## 推奨修正案（オプション1の詳細）

### 修正対象ファイル

#### 1. fix_late_api_multi_post.py

```python
def extract_variant_content(markdown: str, variant_number: int) -> dict:
    """
    案Nのタイトルと本文を抽出（Markdown装飾除去版）

    修正: 本文1行目がタイトルと同じ場合は除去
    """
    # 案N: パターンX → ### タイトル → ### 本文 → --- の構造を抽出
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    # タイトルと本文を抽出
    title = match.group(1).strip()
    body = match.group(2).strip()

    # Markdown装飾を除去
    def remove_markdown(text):
        """Markdown装飾を除去"""
        # **太字** → 通常テキスト
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # - 箇条書き → 通常テキスト
        text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
        # 1. 番号付きリスト → 通常テキスト
        text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
        return text

    title_clean = remove_markdown(title)
    body_clean = remove_markdown(body)

    # 【修正】本文1行目がタイトルと同じ場合は除去
    body_lines = body_clean.split('\n')
    if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
        # 1行目（タイトル重複）を除去
        body_clean = '\n'.join(body_lines[1:]).strip()

    # 完全なコンテンツ = タイトル + 本文（タイトル重複除去済み）
    full_content = f"{title_clean}\n\n{body_clean}"

    return {
        "title": title_clean,
        "body": body_clean,
        "full_content": full_content
    }
```

#### 2. late_api_post.py

```python
def extract_post_content(markdown: str, variant_number: int) -> Optional[str]:
    """
    案Nの本文を抽出（タイトル重複・装飾除去版）

    修正: 本文1行目がタイトルと同じ場合は除去
    """
    import re

    # Regexパターン: 案N → タイトル → 本文 を抽出（---区切りまで）
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\n## 案|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if match:
        title = match.group(1).strip()
        body = match.group(2).strip()

        # Markdown装飾を除去（**太字**を通常テキストに変換）
        body = re.sub(r'\*\*(.+?)\*\*', r'\1', body)
        title_clean = re.sub(r'\*\*(.+?)\*\*', r'\1', title)

        # その他のMarkdown装飾も除去
        # - 箇条書き（- item → item）
        body = re.sub(r'^\- ', '', body, flags=re.MULTILINE)

        # - 番号付きリスト（1. item → item）
        body = re.sub(r'^\d+\. ', '', body, flags=re.MULTILINE)

        # 【修正】本文1行目がタイトルと同じ場合は除去
        body_lines = body.split('\n')
        if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
            # 1行目（タイトル重複）を除去
            body = '\n'.join(body_lines[1:]).strip()

        # タイトルと本文を結合
        full_content = f"{title_clean}\n\n{body}"

        return full_content

    return None
```

### 修正の検証方法

#### テストケース1: タイトル重複あり
```
### タイトル
**OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か**

### 本文（1,195文字）

OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が報じた衝撃のレポート。
```

**期待される出力**:
```
OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か

日本経済新聞が報じた衝撃のレポート。
```

#### テストケース2: タイトル重複なし（既存データとの互換性確認）
```
### タイトル
**テストタイトル**

### 本文（100文字）

これは本文の1行目です。
これは本文の2行目です。
```

**期待される出力**:
```
テストタイトル

これは本文の1行目です。
これは本文の2行目です。
```

## 次のアクション

1. **修正実装**: オプション1（投稿処理スクリプトの修正）を実装
2. **テスト実行**: 上記テストケースで検証
3. **再投稿**: 修正版スクリプトで過去の投稿データを再投稿
4. **モニタリング**: Late APIダッシュボードで投稿確認

## 関連ファイル

- 問題発生スクリーンショット: `Flow/202601/2026-01-05/スクリーンショット 2026-01-06 7.18.54.png`
- 投稿元データ: `Stock/programs/副業/projects/SNS/data/posts_generated_takano_20260105.md`
- 修正対象スクリプト1: `Stock/programs/副業/projects/SNS/scripts/fix_late_api_multi_post.py`
- 修正対象スクリプト2: `Stock/programs/副業/projects/SNS/scripts/late_api_post.py`
- 投稿生成スキル: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`

---

**作成日**: 2026-01-06
**調査者**: Claude Code (Sonnet 4.5)
**ステータス**: 根本原因特定完了、修正案確定
