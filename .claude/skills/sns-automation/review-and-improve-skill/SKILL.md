# SNS投稿自己レビュー＆スキル改善スキル

## スキル概要

生成されたSNS投稿案を自動的にレビューし、品質問題を検出して、投稿生成スキル（SKILL.md）を継続的に改善するスキル。

**目的**: 投稿品質の継続的向上とスキル定義の自動最適化

**実行タイミング**:
- 投稿生成後（手動実行）
- 定期実行（週次/月次）
- 問題検出時（Late API投稿後のフィードバック時）

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 生成済み投稿ファイル（`posts_generated_takano_*.md`）<br>または Late API投稿履歴 |
| **出力** | 1. レビューレポート（`review_report_*.md`）<br>2. 改善提案（`improvement_recommendations_*.md`）<br>3. スキル更新案（`skill_update_proposal_*.md`） |

---

## 実行フロー

### Phase 1: 投稿レビュー（品質評価）

**目的**: 生成された投稿案の品質を多角的に評価

#### Step 1-1: 禁止事項チェック

**評価項目**（各項目 Pass/Fail）:

1. ❌ **SNS数値データ**: いいね数、リツイート数、ビュー数、インプレッション数
2. ❌ **個人SNSアカウント名**: @ユーザー名、"〜のスレッド"、"〜のツイート"
3. ❌ **メタ情報**: "想定エンゲージメント"、"予測いいね数"、"狙いは〜"
4. ❌ **曖昧表現**: "〜かもしれない"、"〜と思われる"、"〜の可能性がある"
5. ❌ **伝聞型表現**: "〜と述べた"、"〜との見解を示した"、"〜と報じられた"
6. ❌ **ハッシュタグ過多**: 3個以上のハッシュタグ
7. ❌ **絵文字過多**: 本文の4%以上の絵文字使用
8. ❌ **呼びかけ表現**: "経営者のあなたへ:"、"CEOのあなたへ:"
9. ❌ **本文URL**: 本文内のURL記載（コメント欄推奨）
10. ❌ **文字数不足**: 700字未満
11. ❌ **パターン重複**: 同一バッチ内で同じパターンの重複使用

**検出方法**:

```python
import re

def check_prohibited_items(post_text: str) -> dict:
    """禁止事項を自動検出"""

    issues = []

    # 1. SNS数値データ検出
    sns_metrics_patterns = [
        r'いいね\s?\d+',
        r'リツイート\s?\d+',
        r'\d+\s?ビュー',
        r'\d+\s?インプレッション',
        r'フォロワー\s?\d+',
    ]
    for pattern in sns_metrics_patterns:
        matches = re.findall(pattern, post_text)
        if matches:
            issues.append({
                "type": "SNS数値データ",
                "severity": "高",
                "matches": matches,
                "suggestion": "SNS数値を削除し、'大きな反響を呼んでいる'等の表現に置き換える"
            })

    # 2. 個人SNSアカウント名検出
    account_patterns = [
        r'@[a-zA-Z0-9_]+',
        r'[a-zA-Z0-9_]+のスレッド',
        r'[a-zA-Z0-9_]+のツイート',
    ]
    for pattern in account_patterns:
        matches = re.findall(pattern, post_text)
        if matches:
            issues.append({
                "type": "個人SNSアカウント名",
                "severity": "高",
                "matches": matches,
                "suggestion": "'AI開発者コミュニティ'、'業界専門家'等の一般的表現に置き換える"
            })

    # 3. メタ情報検出
    meta_patterns = [
        r'想定エンゲージメント',
        r'予測いいね\s?\d+',
        r'狙いは',
        r'戦略として',
        r'意図は',
    ]
    for pattern in meta_patterns:
        if re.search(pattern, post_text):
            issues.append({
                "type": "メタ情報",
                "severity": "高",
                "matches": [pattern],
                "suggestion": "メタ情報セクションを削除"
            })

    # 4. 曖昧表現検出
    vague_patterns = [
        r'かもしれない',
        r'と思われる',
        r'の可能性がある',
        r'おそらく',
    ]
    for pattern in vague_patterns:
        matches = re.findall(pattern, post_text)
        if matches:
            issues.append({
                "type": "曖昧表現",
                "severity": "中",
                "matches": matches,
                "suggestion": "断定型表現に変更（'〜だ。'、'〜である。'）"
            })

    # 5. 伝聞型表現検出
    hearsay_patterns = [
        r'と述べた',
        r'との見解を示した',
        r'と報じられた',
        r'と言われている',
    ]
    for pattern in hearsay_patterns:
        matches = re.findall(pattern, post_text)
        if matches:
            issues.append({
                "type": "伝聞型表現",
                "severity": "中",
                "matches": matches,
                "suggestion": "断定型表現に変更（'〜と断言した。つまり、〜だ。'）"
            })

    return {
        "total_issues": len(issues),
        "issues": issues,
        "status": "FAIL" if len(issues) > 0 else "PASS"
    }
```

#### Step 1-2: 必須要素チェック

**評価項目**（各項目 0-100点）:

1. **口語体の使用**（最低2回）
   - 検出: "ヤバい"、"マジで"、"完全に"、"〜の件"、"これ、〜。"
   - 基準: 0回=0点、1回=50点、2回以上=100点

2. **拡張フレーズのローテーション**（パターン1・3のみ）
   - 検出: 10種類の拡張フレーズのいずれかを使用
   - 基準: 未使用=0点、使用=100点
   - 重複チェック: 同一バッチ内で同じフレーズ使用=-50点

3. **具体的数値データ**（5個以上）
   - 有効数値カウント: 財務、市場、技術、研究、時系列、人員
   - 基準: 0-4個=不合格、5-6個=70点、7-9個=85点、10個以上=100点

4. **企業名・人名**（3回以上）
   - 基準: 0-2回=不合格、3回=80点、4回=90点、5回以上=100点

5. **文字数**（700字以上）
   - 基準: 700字未満=0点、700-899字=80点、900-1499字=100点、1500字以上=90点

**検出方法**:

```python
def check_required_elements(post_text: str) -> dict:
    """必須要素を自動検出して採点"""

    scores = {}

    # 1. 口語体の使用回数
    casual_phrases = ["ヤバい", "マジで", "完全に", "の件", "これ、"]
    casual_count = sum(post_text.count(phrase) for phrase in casual_phrases)

    if casual_count == 0:
        scores["口語体"] = {"score": 0, "count": 0, "status": "不合格"}
    elif casual_count == 1:
        scores["口語体"] = {"score": 50, "count": 1, "status": "改善推奨"}
    else:
        scores["口語体"] = {"score": 100, "count": casual_count, "status": "合格"}

    # 2. 拡張フレーズの使用
    expansion_phrases = [
        "でも、ここからが本当の話だ",
        "でも、本質はここからだ",
        "でも、ここからが重要だ",
        "真実はここにある",
        "本当の問題はこれだ",
        "核心はここだ",
        "でも、見逃せない事実がある",
        "本当に注目すべきはこれだ",
        "でも、最も重要なのはこれだ",
        "真の意味はここにある",
    ]

    used_phrases = [p for p in expansion_phrases if p in post_text]

    if len(used_phrases) == 0:
        scores["拡張フレーズ"] = {"score": 0, "used": None, "status": "未使用"}
    else:
        scores["拡張フレーズ"] = {"score": 100, "used": used_phrases[0], "status": "使用"}

    # 3. 具体的数値データ
    numeric_patterns = [
        r'\d+億ドル', r'\d+兆円', r'\d+億円', r'\d+万円',  # 財務
        r'\d+%', r'年率\d+%', r'CAGR\s?\d+%',  # 成長率
        r'バージョン\s?\d+\.?\d*', r'v\d+\.?\d*',  # バージョン
        r'\d{4}年', r'\d+月', r'\d+日',  # 時系列
        r'\d+人', r'\d+社', r'\d+件',  # 数量
    ]

    numeric_count = sum(len(re.findall(p, post_text)) for p in numeric_patterns)

    if numeric_count < 5:
        scores["数値データ"] = {"score": 0, "count": numeric_count, "status": "不合格"}
    elif numeric_count < 7:
        scores["数値データ"] = {"score": 70, "count": numeric_count, "status": "最低基準"}
    elif numeric_count < 10:
        scores["数値データ"] = {"score": 85, "count": numeric_count, "status": "良好"}
    else:
        scores["数値データ"] = {"score": 100, "count": numeric_count, "status": "優秀"}

    # 4. 企業名・人名（カタカナ連続2文字以上、または英字連続3文字以上）
    company_patterns = [
        r'[ァ-ヴー]{2,}',  # カタカナ2文字以上
        r'[A-Z][a-z]{2,}',  # 英字（頭文字大文字）3文字以上
    ]

    company_count = sum(len(re.findall(p, post_text)) for p in company_patterns)

    if company_count < 3:
        scores["企業名・人名"] = {"score": 0, "count": company_count, "status": "不合格"}
    elif company_count == 3:
        scores["企業名・人名"] = {"score": 80, "count": company_count, "status": "最低基準"}
    elif company_count == 4:
        scores["企業名・人名"] = {"score": 90, "count": company_count, "status": "良好"}
    else:
        scores["企業名・人名"] = {"score": 100, "count": company_count, "status": "優秀"}

    # 5. 文字数
    char_count = len(post_text)

    if char_count < 700:
        scores["文字数"] = {"score": 0, "count": char_count, "status": "不合格"}
    elif char_count < 900:
        scores["文字数"] = {"score": 80, "count": char_count, "status": "最低基準"}
    elif char_count < 1500:
        scores["文字数"] = {"score": 100, "count": char_count, "status": "最適"}
    else:
        scores["文字数"] = {"score": 90, "count": char_count, "status": "やや長い"}

    # 総合スコア計算
    total_score = sum(s["score"] for s in scores.values()) / len(scores)

    return {
        "total_score": total_score,
        "scores": scores,
        "status": "合格" if total_score >= 70 else "不合格"
    }
```

#### Step 1-3: 表現品質チェック

**評価項目**（各項目 Pass/Fail + 改善提案）:

1. **拡張フレーズの既視感**
   - 検出: 過去3回の投稿で同じフレーズを使用していないか
   - 提案: 使用していない別のフレーズを推奨

2. **口語体の配置**
   - 検出: 口語体がタイトルまたは冒頭段落に集中しているか
   - 提案: 全体に分散させる

3. **数値データの質**
   - 検出: 無効な数値（SNS数値、予測値）が混入していないか
   - 提案: 有効な数値に置き換える

4. **企業名の多様性**
   - 検出: 同じ企業名の繰り返しが多すぎないか
   - 提案: 複数企業を引用してバランスを取る

---

### Phase 2: 問題パターン分析

**目的**: 複数の投稿から共通する問題パターンを特定

#### Step 2-1: 問題の集計

**分析対象**: 過去5-10回分の投稿レビュー結果

**集計項目**:

1. **頻出問題トップ5**
   - 各禁止事項違反の発生頻度
   - 必須要素の不足頻度

2. **スコア傾向**
   - 総合スコアの平均値・標準偏差
   - 各評価項目の平均スコア

3. **改善トレンド**
   - 時系列でのスコア変化（改善/悪化の傾向）

**出力フォーマット**:

```markdown
## 問題パターン分析サマリー

### 頻出問題トップ5（過去10回分）

| 順位 | 問題タイプ | 発生回数 | 発生率 | 重要度 |
|------|----------|---------|--------|--------|
| 1 | SNS数値データ | 8/10 | 80% | 高 |
| 2 | 口語体不足 | 6/10 | 60% | 中 |
| 3 | 拡張フレーズ重複 | 5/10 | 50% | 中 |
| 4 | 数値データ不足 | 3/10 | 30% | 高 |
| 5 | 伝聞型表現 | 2/10 | 20% | 中 |

### スコア傾向

| 評価項目 | 平均スコア | 標準偏差 | 最低点 | 最高点 |
|---------|----------|---------|--------|--------|
| 口語体 | 65.0 | 25.3 | 0 | 100 |
| 拡張フレーズ | 80.0 | 30.0 | 0 | 100 |
| 数値データ | 72.5 | 15.2 | 50 | 100 |
| 企業名・人名 | 85.0 | 10.5 | 70 | 100 |
| 文字数 | 90.0 | 8.7 | 80 | 100 |
| **総合** | **78.5** | **12.4** | **60** | **95** |

### 改善トレンド

- ✅ **改善中**: 文字数（平均90点、標準偏差8.7）
- ⚠️ **停滞**: 口語体（平均65点、改善なし）
- ❌ **悪化**: SNS数値データ（発生率80%→85%に増加）
```

#### Step 2-2: 根本原因の推定

**分析手法**: 問題発生の根本原因を3つのカテゴリに分類

1. **スキル定義の不備**
   - 禁止事項の記載が不明確
   - 推奨表現の例が不足
   - チェックリストの検証項目が不足

2. **生成プロセスの問題**
   - ソースデータに問題が含まれる（例: X投稿にSNS数値が記載）
   - 生成時のプロンプトが不適切

3. **検証プロセスの不足**
   - 自動検証スクリプトが未実装
   - レビュー基準が曖昧

**出力フォーマット**:

```markdown
## 根本原因分析

### 問題1: SNS数値データ（発生率80%）

**根本原因**: スキル定義の不備

**詳細**:
- 禁止事項9に記載はあるが、ソースデータ（X投稿）にSNS数値が含まれるため、自動的にコピーされる
- 代替表現の例が2つのみで不足
- 自動検出スクリプトが未実装

**推奨対策**:
1. ソースデータの前処理でSNS数値を自動削除
2. 代替表現の例を10種類に拡充
3. 自動検出スクリプトの実装（正規表現ベース）

### 問題2: 口語体不足（平均65点）

**根本原因**: スキル定義の不備

**詳細**:
- 「最低2回使用」の記載はあるが、配置場所の指定がない
- 推奨フレーズが5種類のみで選択肢が少ない
- 使用箇所の明示的な指示が不足

**推奨対策**:
1. 口語体の配置場所を明示（タイトル、冒頭段落、CTA段落）
2. 推奨フレーズを15種類に拡充
3. 各段落での使用例を追加
```

---

### Phase 3: スキル改善提案の生成

**目的**: Phase 2の分析結果から具体的なスキル修正案を生成

#### Step 3-1: 改善提案の優先順位付け

**優先度評価基準**:

| 優先度 | 条件 | 対応期限 |
|--------|------|---------|
| **緊急（P0）** | 発生率70%以上、重要度「高」 | 即時対応 |
| **重要（P1）** | 発生率50%以上、重要度「中」または発生率30%以上、重要度「高」 | 1週間以内 |
| **推奨（P2）** | 発生率30%以上、重要度「中」 | 2週間以内 |
| **低（P3）** | 発生率30%未満 | 1ヶ月以内 |

**出力フォーマット**:

```markdown
## 改善提案の優先順位

### P0: 緊急対応（即時）

#### 提案1: SNS数値データの自動削除機能追加

**問題**: SNS数値データの混入（発生率80%、重要度: 高）

**修正箇所**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`

**修正内容**:

1. **禁止事項9の拡充**（161-167行目）

```markdown
9. **SNS数値データの具体的言及**
   - ❌ 禁止: いいね数、リツイート数、ビュー数、インプレッション数
   - ❌ 禁止: SNSアカウント名（@ユーザー名、ユーザー名のスレッド）
   - ❌ 例: "SuguruKun_aiのスレッドがいいね1,132、リツイート105、163,736ビューを記録"
   - ✅ 代替: "AI開発者コミュニティで大きな反響を呼んでいる"
   - ✅ 代替: "OpenAI Cookbookで正式公開され、注目を集めている"

   **追加**: 代替表現のバリエーション（10種類）

   1. "大きな反響を呼んでいる"
   2. "注目を集めている"
   3. "話題になっている"
   4. "業界で注目されている"
   5. "開発者コミュニティで話題になっている"
   6. "AI研究者の間で議論を呼んでいる"
   7. "専門家が注目している"
   8. "業界関係者の関心を集めている"
   9. "技術コミュニティで評価されている"
   10. "エキスパートが支持している"

   - **理由**: SNS数値は時間経過で変化する一時的情報。LinkedIn投稿では不要
```

2. **自動検出スクリプトの追加**

新規ファイル: `.claude/skills/sns-automation/generate-sns-posts-takano/validators/check_sns_metrics.py`

```python
import re
import sys

def detect_sns_metrics(text: str) -> dict:
    """SNS数値データを自動検出"""

    patterns = {
        'いいね数': r'いいね\s?\d+',
        'リツイート数': r'リツイート\s?\d+',
        'ビュー数': r'\d+\s?ビュー',
        'インプレッション数': r'\d+\s?インプレッション',
        'フォロワー数': r'フォロワー\s?\d+',
        'アカウント名': r'@[a-zA-Z0-9_]+',
    }

    detections = []

    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            detections.append({
                'type': name,
                'matches': matches,
                'severity': 'ERROR'
            })

    return {
        'has_issues': len(detections) > 0,
        'detections': detections
    }

if __name__ == '__main__':
    # テスト実行
    test_text = "SuguruKun_aiのスレッドがいいね1,132、リツイート105、163,736ビューを記録。"
    result = detect_sns_metrics(test_text)

    if result['has_issues']:
        print("❌ SNS数値データが検出されました:")
        for d in result['detections']:
            print(f"  - {d['type']}: {d['matches']}")
        sys.exit(1)
    else:
        print("✅ SNS数値データは検出されませんでした")
        sys.exit(0)
```

**期待効果**:
- SNS数値データの混入率: 80% → 10%以下
- 代替表現のバリエーション不足解消
- 自動検証による品質向上

---

### P1: 重要対応（1週間以内）

#### 提案2: 口語体の配置ガイドライン追加

**問題**: 口語体不足（平均スコア65点、発生率60%）

**修正箇所**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`

**修正内容**:

新規セクション挿入（228行目付近、「言語スタイル」セクション内）

```markdown
### 口語体の配置ガイドライン

**最低使用回数**: 2回以上（推奨: 3-4回）

**推奨配置場所**:

1. **タイトル**（必須1回）
   - ✅ 「〜の件」、「マジでヤバい」、「完全に壊れる」
   - ❌ タイトルなしの場合は冒頭段落で2回使用

2. **冒頭段落**（推奨1回）
   - ✅ 「これ、〜。」、「ヤバい。」、「マジで〜だ。」

3. **CTA段落**（推奨1回）
   - ✅ 「あなたの会社、大丈夫？」、「これ、どう思う？」

**推奨フレーズ15種類**:

| カテゴリ | フレーズ | 使用例 |
|---------|---------|--------|
| 驚き | ヤバい | 「この数字、ヤバい。」 |
| 驚き | マジで | 「マジで異常事態だ。」 |
| 強調 | 完全に | 「完全に壊れる。」 |
| カジュアル | 〜の件 | 「SoftBankが3.5兆円ぶち込んだ件。」 |
| カジュアル | これ、〜 | 「これ、経営者は見逃せない。」 |
| カジュアル | 〜だけど | 「異常だけど、これが現実だ。」 |
| カジュアル | 〜すぎる | 「速すぎる。」 |
| 疑問投げかけ | 〜、大丈夫？ | 「あなたの会社、大丈夫？」 |
| 疑問投げかけ | どう思う？ | 「これ、どう思う？」 |
| 断定 | 間違いない | 「これ、間違いない。」 |
| 断定 | 確実だ | 「変化は確実だ。」 |
| 比較 | 桁違い | 「桁違いの投資だ。」 |
| 比較 | 次元が違う | 「次元が違う。」 |
| 評価 | ありえない | 「ありえない現象だ。」 |
| 評価 | 前代未聞 | 「前代未聞の事態だ。」 |

**配置例**:

```
【タイトル】（口語体1回目）
SoftBankが3.5兆円ぶち込んだOpenAI投資、マジでヤバい件。

【冒頭段落】（口語体2回目）
2026年1月、OpenAIへの追加投資が発表された。これ、経営者は見逃せない。

【中間段落】
[データ・事例の展開]

【CTA段落】（口語体3回目）
あなたの会社、AI戦略は大丈夫？
```

**チェックリスト追加**:

```markdown
- [ ] タイトルまたは冒頭段落で口語体を1回使用
- [ ] 本文全体で口語体を最低2回使用（推奨3-4回）
- [ ] 口語体が特定段落に偏らず全体に分散
```
```

**期待効果**:
- 口語体平均スコア: 65点 → 85点以上
- 読者との距離感の改善
- エンゲージメント率の向上
```

#### Step 3-2: スキル修正案の生成

**目的**: 具体的な修正内容をSKILL.mdへの適用形式で出力

**出力フォーマット**:

```markdown
## スキル修正案（適用準備完了）

### 修正1: 禁止事項9の拡充（P0）

**ファイル**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`

**修正箇所**: 161-167行目

**修正前**:

```markdown
9. **SNS数値データの具体的言及**
   - ❌ 禁止: いいね数、リツイート数、ビュー数、インプレッション数
   - ❌ 禁止: SNSアカウント名（@ユーザー名、ユーザー名のスレッド）
   - ❌ 例: "SuguruKun_aiのスレッドがいいね1,132、リツイート105、163,736ビューを記録"
   - ✅ 代替: "AI開発者コミュニティで大きな反響を呼んでいる"
   - ✅ 代替: "OpenAI Cookbookで正式公開され、注目を集めている"
   - **理由**: SNS数値は時間経過で変化する一時的情報。LinkedIn投稿では不要
```

**修正後**:

```markdown
9. **SNS数値データの具体的言及**
   - ❌ 禁止: いいね数、リツイート数、ビュー数、インプレッション数
   - ❌ 禁止: SNSアカウント名（@ユーザー名、ユーザー名のスレッド）
   - ❌ 例: "SuguruKun_aiのスレッドがいいね1,132、リツイート105、163,736ビューを記録"

   **代替表現（10種類から選択）**:

   1. "大きな反響を呼んでいる"
   2. "注目を集めている"
   3. "話題になっている"
   4. "業界で注目されている"
   5. "開発者コミュニティで話題になっている"
   6. "AI研究者の間で議論を呼んでいる"
   7. "専門家が注目している"
   8. "業界関係者の関心を集めている"
   9. "技術コミュニティで評価されている"
   10. "エキスパートが支持している"

   - **理由**: SNS数値は時間経過で変化する一時的情報。LinkedIn投稿では不要
```

**適用コマンド**:

```bash
# Editツールで適用
Edit(
    file_path=".claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md",
    old_string="[修正前の内容]",
    new_string="[修正後の内容]"
)
```

---

### 修正2: 口語体配置ガイドライン追加（P1）

**ファイル**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`

**挿入箇所**: 228行目付近（「言語スタイル」セクション内）

**挿入内容**:

[上記の詳細内容]

**適用コマンド**:

```bash
# Editツールで適用
Edit(
    file_path=".claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md",
    old_string="### 断定的な言い切り型\n\n- 曖昧な表現を排除し、明確な立場を示す",
    new_string="### 口語体の配置ガイドライン\n\n[新規内容]\n\n### 断定的な言い切り型\n\n- 曖昧な表現を排除し、明確な立場を示す"
)
```
```

---

### Phase 4: 自動適用とテスト

**目的**: 提案された修正を自動適用し、効果を検証

#### Step 4-1: スキル修正の自動適用

**実行手順**:

1. **バックアップ作成**
   ```bash
   cp .claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md \
      .claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md.backup_$(date +%Y%m%d_%H%M%S)
   ```

2. **修正適用**
   - Edit toolを使用して各修正を順次適用
   - 適用後にファイルを読み込んで確認

3. **適用ログ記録**
   ```markdown
   ## スキル修正適用ログ

   - 修正日時: 2026-01-06 14:30:00
   - 修正ID: skill_update_20260106_001
   - 適用内容:
     - 修正1: 禁止事項9の拡充（P0）
     - 修正2: 口語体配置ガイドライン追加（P1）
   - バックアップ: SKILL.md.backup_20260106_143000
   ```

#### Step 4-2: 効果検証テスト

**テスト手順**:

1. **修正前の投稿を再生成**
   - 同じソースデータを使用
   - 修正前スキルで生成（バックアップから復元）
   - 品質スコアを記録

2. **修正後の投稿を再生成**
   - 同じソースデータを使用
   - 修正後スキルで生成
   - 品質スコアを記録

3. **スコア比較**

```markdown
## 効果検証結果

### テストケース: X投稿 "OpenAI GPT-5.2リリース"

| 評価項目 | 修正前スコア | 修正後スコア | 改善率 |
|---------|------------|------------|--------|
| 口語体 | 50点（1回） | 100点（3回） | +100% |
| SNS数値データ | FAIL（3件検出） | PASS（0件） | +100% |
| 数値データ | 70点（5個） | 85点（8個） | +21% |
| 文字数 | 80点（750字） | 100点（920字） | +25% |
| **総合スコア** | **67.5点** | **93.8点** | **+39%** |

### 改善された問題

1. ✅ **SNS数値データ削除**: "いいね1,132"等が"大きな反響を呼んでいる"に自動置換
2. ✅ **口語体増加**: タイトル、冒頭、CTAの3箇所に配置
3. ✅ **数値データ補強**: 市場規模データを追加して8個に増加
4. ✅ **文字数向上**: 代替表現の追加で920字に増加

### 残存する問題

1. ⚠️ **拡張フレーズ重複**: 同一バッチ内で"でも、ここからが本当の話だ。"を2回使用
   - 次回修正: P2優先度で対応予定
```

---

## 実行コマンド

### 基本実行

```bash
# 最新の投稿をレビュー
claude-code skill sns-automation/review-and-improve-skill \
  --input "Flow/202601/2026-01-06/posts_generated_takano_20260105.md"

# 過去10回分の投稿を一括レビュー
claude-code skill sns-automation/review-and-improve-skill \
  --input "Flow/202601/*/posts_generated_takano_*.md" \
  --batch 10
```

### 自動修正モード

```bash
# レビュー + 改善提案 + 自動適用
claude-code skill sns-automation/review-and-improve-skill \
  --input "Flow/202601/2026-01-06/posts_generated_takano_20260105.md" \
  --auto-apply \
  --priority P0,P1

# テスト実行（バックアップのみ、適用なし）
claude-code skill sns-automation/review-and-improve-skill \
  --input "Flow/202601/2026-01-06/posts_generated_takano_20260105.md" \
  --dry-run
```

---

## 出力ファイル構成

### 1. レビューレポート

**ファイル名**: `review_report_YYYYMMDD_HHMMSS.md`

**内容**:
- Phase 1の評価結果（禁止事項チェック、必須要素チェック、表現品質チェック）
- 検出された問題の一覧（重要度順）
- 総合スコア（0-100点）

### 2. 改善提案レポート

**ファイル名**: `improvement_recommendations_YYYYMMDD_HHMMSS.md`

**内容**:
- Phase 2の分析結果（問題パターン分析、根本原因推定）
- Phase 3の改善提案（優先度付き、具体的修正内容）

### 3. スキル更新案

**ファイル名**: `skill_update_proposal_YYYYMMDD_HHMMSS.md`

**内容**:
- Phase 3の修正案（適用準備完了、Editコマンド付き）
- バックアップファイルのパス
- 適用ログのテンプレート

### 4. 効果検証レポート

**ファイル名**: `validation_report_YYYYMMDD_HHMMSS.md`

**内容**:
- Phase 4のテスト結果（修正前後のスコア比較）
- 改善された問題の一覧
- 残存する問題と次回修正計画

---

## 定期実行の推奨スケジュール

| 頻度 | 実行内容 | 目的 |
|------|---------|------|
| **投稿生成後**（毎回） | レビューレポート生成 | 品質チェック、即座の問題検出 |
| **週次**（月曜朝） | 改善提案レポート生成 | 週間の問題傾向分析 |
| **月次**（月初） | スキル更新案生成 + 自動適用 | スキル定義の継続的改善 |
| **四半期**（四半期末） | 効果検証レポート生成 | 長期的な品質トレンド分析 |

---

## カスタマイズオプション

### 評価基準のカスタマイズ

評価基準を変更する場合は、以下のファイルを編集：

**ファイル**: `.claude/skills/sns-automation/review-and-improve-skill/config/review_criteria.json`

```json
{
  "prohibited_items": {
    "sns_metrics": {
      "severity": "high",
      "patterns": ["いいね\\s?\\d+", "リツイート\\s?\\d+"],
      "suggestion": "SNS数値を削除し、代替表現を使用"
    }
  },
  "required_elements": {
    "casual_tone": {
      "min_count": 2,
      "score_weights": {
        "0": 0,
        "1": 50,
        "2+": 100
      }
    }
  },
  "quality_thresholds": {
    "total_score": {
      "fail": 70,
      "pass": 80,
      "excellent": 90
    }
  }
}
```

### スキル修正の承認フロー

自動適用を無効化し、手動承認フローを有効化：

```bash
# 手動承認モード
claude-code skill sns-automation/review-and-improve-skill \
  --input "Flow/202601/2026-01-06/posts_generated_takano_20260105.md" \
  --manual-approval

# 実行結果
# → 修正案を表示
# → ユーザーに承認を求める（y/n）
# → 承認後に適用
```

---

## トラブルシューティング

### 問題1: レビュースコアが常に低い

**原因**: ソースデータ（X投稿）に問題が含まれている

**対処法**:
1. ソースデータの前処理を実施
2. SNS数値の自動削除スクリプトを実行
3. ソースデータの品質基準を設定

### 問題2: 自動修正が適用されない

**原因**: 修正箇所の文字列が一致しない（行番号がズレている）

**対処法**:
1. バックアップから復元
2. 手動でEditコマンドを実行
3. old_stringを短くして部分一致させる

### 問題3: 効果検証で改善が見られない

**原因**: 修正内容が不十分、または別の問題が優先

**対処法**:
1. 問題パターン分析を再実行
2. 優先度の再評価
3. 複数の修正を同時適用

---

## 参照

- **投稿生成スキル**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`
- **過去のレビューレポート**: `Flow/202601/2026-01-06/past_posts_quality_analysis.md`
- **Phase 1修正サマリー**: `Flow/202601/2026-01-06/skill_update_summary.md`
- **Phase 2修正サマリー**: `Flow/202601/2026-01-06/skill_phase2_update_summary.md`

---

**スキル作成日**: 2026-01-06
**バージョン**: 1.0.0
**最終更新**: 2026-01-06
**メンテナンス**: 月次更新推奨
