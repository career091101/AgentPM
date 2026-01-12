# Deep Research to Note Rules（詳細版）

ディープリサーチからnote記事作成のための詳細実行ルール。

## トリガー

以下のいずれかのトリガーワードでエージェントを起動：

- **「ディープリサーチ」** - 汎用的なリサーチスキル起動ワード
- **「落合式リサーチ」** - 落合フォーマット明示的な起動ワード
- **「論文サマリー作成」** - サマリー作成に特化したワード
- **「6つの質問」** - 落合フォーマット直接参照
- **「研究サーベイ」** - 複数論文の体系的サーベイ
- **「note記事作成」** - note形式での出力指定

## 実行手順

### ステップ0: トリガー検出と初期化

#### 0.1 トリガーワード検出

**処理内容**:
```python
# ユーザーメッセージからトリガーワードを検出
triggers = ["ディープリサーチ", "落合式リサーチ", "論文サマリー作成", "6つの質問", "研究サーベイ", "note記事作成"]
user_message = "論文サマリー作成して：https://arxiv.org/abs/1706.03762"

if any(trigger in user_message for trigger in triggers):
    # エージェント起動
    agent = DeepResearchToNoteAgent()
    agent.initialize()
```

#### 0.2 エージェント初期化

**処理内容**:
- ロギングシステムの初期化
- 一時ディレクトリの作成（PDFダウンロード用）
- タイムスタンプの記録（読解時間計測開始）
- Notion API接続テスト（Notionモードの場合）

**ログ出力例**:
```
[2025-12-31 15:00:00] Deep Research to Note Agent v1.0 起動
[2025-12-31 15:00:00] トリガーワード検出: 「論文サマリー作成」
[2025-12-31 15:00:00] 一時ディレクトリ作成: /tmp/deep_research_xyz/
[2025-12-31 15:00:00] タイマー開始
```

---

### ステップ1: 入力受付と初期設定

#### 1.1 論文URL/PDFファイルの受け取り

**入力例**:
```
# パターン1: arXiv URL
https://arxiv.org/abs/1706.03762

# パターン2: DOI URL
https://doi.org/10.48550/arXiv.1706.03762

# パターン3: ローカルPDFファイル
/path/to/paper.pdf

# パターン4: PDFファイルアップロード
<uploaded_file: paper.pdf>
```

**処理フロー**:
```python
def parse_paper_source(user_input):
    # arXiv URLの検出
    if "arxiv.org/abs/" in user_input:
        arxiv_id = extract_arxiv_id(user_input)  # "1706.03762"
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        return {"type": "arxiv", "url": pdf_url, "id": arxiv_id}

    # DOI URLの検出
    elif "doi.org/" in user_input:
        doi = extract_doi(user_input)
        pdf_url = resolve_doi_to_pdf(doi)
        return {"type": "doi", "url": pdf_url, "id": doi}

    # ローカルファイルパスの検出
    elif user_input.endswith(".pdf"):
        return {"type": "local", "path": user_input}

    # アップロードファイルの検出
    elif is_uploaded_file(user_input):
        return {"type": "upload", "file": user_input}

    else:
        raise ValueError("論文URLまたはPDFファイルを指定してください")
```

#### 1.2 読解モードの確認

**デフォルト値**: `standard`

**ユーザー指定例**:
```
# Quick Mode（10分速読）
論文サマリー作成（クイックモード）：https://arxiv.org/abs/1706.03762

# Standard Mode（30分標準）
論文サマリー作成：https://arxiv.org/abs/1706.03762

# Deep Mode（1時間精読）
論文サマリー作成（詳細モード）：https://arxiv.org/abs/1706.03762
```

**モード別の処理内容**:
| Mode | 読解範囲 | 詳細度 | 図表抽出 | 時間目安 |
|------|---------|-------|---------|---------|
| quick | Abstract + Conclusion のみ | 簡潔 | 0-1点 | 10分 |
| standard | Abstract + Conclusion + Results + Related Work | 標準 | 1-3点 | 30分 |
| deep | 全セクション詳細分析 | 詳細 | 3-5点 | 1時間 |

#### 1.3 出力形式の選択

**デフォルト値**: `markdown`

**ユーザー指定例**:
```
# Markdown形式
論文サマリー作成（Markdown）：URL

# A4スライド形式
論文サマリー作成（スライド）：URL

# Notion登録
論文サマリー作成（Notion）：URL

# 複数形式
論文サマリー作成（Markdown + Notion）：URL
```

**形式別の出力**:
```python
output_formats = {
    "markdown": generate_markdown_summary,
    "slide": generate_slide_summary,
    "notion": upload_to_notion,
}

# 複数形式の場合
selected_formats = ["markdown", "notion"]
for format in selected_formats:
    output_formats[format](summary_data)
```

#### 1.4 オプションパラメータの設定

**パラメータ解析**:
```python
def parse_optional_params(user_input):
    params = {
        "research_theme": None,
        "reading_mode": "standard",
        "language": "ja",
        "existing_papers": [],
        "next_paper_count": 3,
        "figure_count": 3,
    }

    # 研究テーマの検出
    if "研究テーマ:" in user_input:
        params["research_theme"] = extract_after_keyword(user_input, "研究テーマ:")

    # 既読論文リストの検出
    if "既読:" in user_input:
        params["existing_papers"] = extract_list_after_keyword(user_input, "既読:")

    return params
```

**使用ツール**:
- ユーザーインタラクション（AskUserQuestion tool）
- パラメータバリデーション

**注意点**:
- 論文URLが無効な場合はエラーハンドリング
- PDFアップロードの場合はファイル形式検証
- デフォルト値の適切な設定（読解モード: standard、出力形式: Markdown）

---

### ステップ2: 論文構造解析

#### 2.1 論文PDFのダウンロード（URL指定の場合）

**ダウンロード処理**:
```python
import requests
from pathlib import Path

def download_pdf(pdf_url, save_dir="/tmp/deep_research/"):
    try:
        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()

        # ファイル名生成
        arxiv_id = extract_arxiv_id(pdf_url)
        filename = f"{arxiv_id}.pdf"
        filepath = Path(save_dir) / filename

        # PDFファイル保存
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"[INFO] PDFダウンロード完了: {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] PDFダウンロード失敗: {e}")
        raise
```

**エラーハンドリング**:
```python
try:
    pdf_path = download_pdf(pdf_url)
except requests.exceptions.Timeout:
    # タイムアウトの場合は再試行
    print("[WARN] タイムアウト発生。再試行中...")
    pdf_path = download_pdf(pdf_url, timeout=60)
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 404:
        print("[ERROR] 論文が見つかりません。URLを確認してください。")
    elif e.response.status_code == 403:
        print("[ERROR] アクセス権限がありません。DOI URLで再試行してください。")
    raise
```

#### 2.2 セクション構造の特定

**セクション検出アルゴリズム**:
```python
import re
from PyPDF2 import PdfReader

def detect_paper_sections(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()

    # 標準的なセクション見出しを検索
    sections = {
        "Abstract": None,
        "Introduction": None,
        "Related Work": None,
        "Methods": None,
        "Experiments": None,
        "Results": None,
        "Discussion": None,
        "Conclusion": None,
        "References": None,
    }

    for section_name in sections.keys():
        # セクション見出しのパターンマッチング
        pattern = rf"(?:^|\n)\s*(?:\d+\.?\s+)?{section_name}\s*(?:\n|$)"
        match = re.search(pattern, full_text, re.IGNORECASE | re.MULTILINE)

        if match:
            sections[section_name] = match.start()
            print(f"[INFO] セクション検出: {section_name} at position {match.start()}")

    return sections, full_text
```

**非標準構造のフォールバック処理**:
```python
def fallback_section_detection(full_text):
    # セクションが見つからない場合の代替処理
    print("[WARN] 標準的なセクション構造が検出できませんでした。全文を順次読解します。")

    # 最初の500文字をAbstractとみなす
    abstract = full_text[:500]

    # 最後の1000文字をConclusionとみなす
    conclusion = full_text[-1000:]

    return {"Abstract": abstract, "Conclusion": conclusion, "FullText": full_text}
```

#### 2.3 図表の抽出と重要度順ソート

**図表抽出処理**:
```python
import fitz  # PyMuPDF

def extract_figures(pdf_path):
    doc = fitz.open(pdf_path)
    figures = []

    for page_num, page in enumerate(doc):
        # ページ内の画像を抽出
        images = page.get_images()

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # 画像サイズで重要度を判定（大きい画像ほど重要と仮定）
            img_size = len(image_bytes)

            figures.append({
                "page": page_num + 1,
                "index": img_index,
                "size": img_size,
                "image": image_bytes,
                "ext": base_image["ext"],
            })

    # サイズでソート（降順）
    figures_sorted = sorted(figures, key=lambda x: x["size"], reverse=True)

    print(f"[INFO] 図表抽出完了: {len(figures)}点")
    return figures_sorted
```

**図表の重要度スコアリング**:
```python
def score_figure_importance(figure, full_text):
    score = 0

    # スコアリング要素1: 画像サイズ（大きいほど重要）
    score += figure["size"] / 1000

    # スコアリング要素2: 本文での言及回数
    figure_ref = f"Figure {figure['index'] + 1}"
    mention_count = full_text.count(figure_ref)
    score += mention_count * 10

    # スコアリング要素3: ページ位置（中盤のページほど重要）
    total_pages = 10  # 仮の総ページ数
    page_score = 1 - abs((figure["page"] - total_pages / 2) / total_pages)
    score += page_score * 5

    return score
```

#### 2.4 引用論文リストの抽出

**References欄の解析**:
```python
def extract_references(full_text):
    # Referencesセクションの開始位置を検出
    ref_match = re.search(r"(?:^|\n)\s*(?:\d+\.?\s+)?References\s*(?:\n|$)", full_text, re.IGNORECASE | re.MULTILINE)

    if not ref_match:
        print("[WARN] Referencesセクションが見つかりません")
        return []

    # Referencesセクション以降のテキストを抽出
    references_text = full_text[ref_match.end():]

    # 引用文献のパターンマッチング
    # 例: "[1] Author, A. (2020). Title. Conference."
    ref_pattern = r"\[\d+\]\s+(.+?)(?=\[\d+\]|$)"
    references = re.findall(ref_pattern, references_text, re.DOTALL)

    parsed_references = []
    for ref in references:
        parsed_references.append(parse_single_reference(ref.strip()))

    print(f"[INFO] 引用論文抽出完了: {len(parsed_references)}本")
    return parsed_references
```

**単一引用文献のパース**:
```python
import re

def parse_single_reference(ref_text):
    # 著者名の抽出
    author_match = re.search(r"^(.+?)\s+\((\d{4})\)", ref_text)
    if author_match:
        authors = author_match.group(1)
        year = int(author_match.group(2))
    else:
        authors = "Unknown"
        year = None

    # タイトルの抽出（引用符で囲まれた部分）
    title_match = re.search(r'"(.+?)"', ref_text)
    if title_match:
        title = title_match.group(1)
    else:
        title = ref_text[:100]  # 最初の100文字をタイトルとみなす

    # カンファレンス/ジャーナルの抽出
    venue_match = re.search(r"(?:In|Proceedings of|Journal of)\s+(.+?)(?:\.|$)", ref_text)
    venue = venue_match.group(1) if venue_match else "Unknown"

    return {
        "authors": authors,
        "year": year,
        "title": title,
        "venue": venue,
        "raw_text": ref_text,
    }
```

**使用ツール**:
- PDF解析ライブラリ（PyPDF2, PyMuPDF）
- OCR（必要に応じて：Tesseract）
- 図表認識AI（将来的な拡張）

**注意点**:
- スキャン画像PDFの場合はOCR実行
- セクション構造が標準と異なる場合のフォールバック処理
- 図表抽出失敗時はテキストのみで継続

---

### ステップ3: 戦略的読解（逆順アプローチ）

#### 3.1 Abstract解析

**LLMプロンプトテンプレート**:
```
以下の論文のAbstractを読み、リサーチクエスチョンと全体像を3行で要約してください。

【Abstract】
{abstract_text}

【出力形式】
- リサーチクエスチョン: [この論文が解こうとしている問題]
- 提案手法: [問題を解決するために提案した手法]
- 主要結果: [実験で得られた主要な結果]
```

**実行例**:
```python
def analyze_abstract(abstract_text, llm_api="claude"):
    prompt = f"""
以下の論文のAbstractを読み、リサーチクエスチョンと全体像を3行で要約してください。

【Abstract】
{abstract_text}

【出力形式】
- リサーチクエスチョン: [この論文が解こうとしている問題]
- 提案手法: [問題を解決するために提案した手法]
- 主要結果: [実験で得られた主要な結果]
"""

    response = call_llm(llm_api, prompt)
    return parse_llm_response(response)
```

**期待される出力例**:
```
- リサーチクエスチョン: RNNやCNNを使わずに、Attentionだけでシーケンス変換は可能か？
- 提案手法: Multi-Head AttentionとPositional Encodingで構成されるTransformerモデル
- 主要結果: 機械翻訳でBLEU 28.4を達成し、既存最高性能を大幅に上回った
```

#### 3.2 Conclusion解析

**LLMプロンプトテンプレート**:
```
以下の論文のConclusionを読み、達成内容と主要結論を抽出してください。
また、この論文が重要論文かどうかを判定し、全文読みが必要かどうかを判断してください。

【Conclusion】
{conclusion_text}

【出力形式】
- 達成内容: [この論文で達成したこと]
- 主要結論: [研究の主な結論]
- 重要度: [High/Medium/Low]
- 全文読みの必要性: [Yes/No]
- 理由: [判断理由]
```

**重要度判定のロジック**:
```python
def judge_paper_importance(conclusion_analysis, abstract_analysis):
    score = 0

    # 判定要素1: 結果の数値的インパクト（BLEU 28.4 vs 既存最高25.8等）
    if "大幅に上回った" in conclusion_analysis or "significantly" in conclusion_analysis:
        score += 3

    # 判定要素2: 新規性（「初めて」「novel」等のキーワード）
    if "初めて" in conclusion_analysis or "novel" in conclusion_analysis.lower():
        score += 2

    # 判定要素3: 広範な応用可能性
    if "応用" in conclusion_analysis or "applicable" in conclusion_analysis.lower():
        score += 1

    # 判定要素4: ユーザーの研究テーマとの関連性
    if user_research_theme and (user_research_theme in abstract_analysis):
        score += 2

    # スコアに基づく重要度判定
    if score >= 5:
        return {"importance": "High", "full_read": True}
    elif score >= 3:
        return {"importance": "Medium", "full_read": False}
    else:
        return {"importance": "Low", "full_read": False}
```

#### 3.3 Results/Experiments解析

**LLMプロンプトテンプレート**:
```
以下の論文のExperiments/Resultsセクションを読み、検証方法、実験条件、結果データを構造化して抽出してください。

【Experiments/Results】
{experiments_text}

【出力形式】
- データセット: [使用したデータセット名、サイズ]
- 実験条件: [ハイパーパラメータ、計算環境等]
- 評価指標: [使用した評価指標]
- 主要結果: [数値結果を含む]
- ベースライン比較: [既存手法との比較結果]
- 統計的有意性: [p値、信頼区間等があれば記載]
```

**実行例**:
```python
def analyze_experiments(experiments_text):
    prompt = f"""
以下の論文のExperiments/Resultsセクションを読み、検証方法、実験条件、結果データを構造化して抽出してください。

【Experiments/Results】
{experiments_text}

【出力形式】
- データセット: [使用したデータセット名、サイズ]
- 実験条件: [ハイパーパラメータ、計算環境等]
- 評価指標: [使用した評価指標]
- 主要結果: [数値結果を含む]
- ベースライン比較: [既存手法との比較結果]
- 統計的有意性: [p値、信頼区間等があれば記載]
"""

    response = call_llm("claude", prompt)
    return parse_structured_response(response)
```

#### 3.4 Related Work解析

**LLMプロンプトテンプレート**:
```
以下の論文のRelated Workセクションを読み、先行研究との位置づけと差別化ポイントを抽出してください。

【Related Work】
{related_work_text}

【出力形式】
- 主要な先行研究: [引用されている重要な先行研究3-5本]
- 既存手法の問題点: [先行研究の限界点]
- 本論文の差別化ポイント: [先行研究と比べてどこがすごいか]
- 学術的価値: [この論文の学術的貢献]
```

**差別化ポイントの抽出ロジック**:
```python
def extract_novelty_points(related_work_analysis):
    novelty_keywords = [
        "初めて", "first", "novel",
        "既存手法では不可能", "従来手法の限界",
        "大幅に改善", "significantly improved",
        "新しいアプローチ", "new approach",
    ]

    novelty_points = []
    for keyword in novelty_keywords:
        if keyword in related_work_analysis:
            # キーワード周辺の文脈を抽出
            context = extract_context_around_keyword(related_work_analysis, keyword, window=100)
            novelty_points.append(context)

    return novelty_points
```

**使用ツール**:
- LLM（Claude/ChatGPT）による自然言語理解
- セマンティック抽出
- 構造化データ抽出

**注意点**:
- 頭から几帳面に読まず、必ず逆順（Abstract→Conclusion→Results→Related Work）を徹底
- 1論文1時間（最終的に10-20分）の時間制限を設定
- 重要論文と判断した場合のみ全セクションの精読フラグを立てる

---

### ステップ4: 6つの質問への回答生成

#### 質問1: 「どんなもの？」

**LLMプロンプトテンプレート**:
```
以下のAbstract分析結果をもとに、「どんなもの？」という質問に3行で答えてください。

【Abstract分析結果】
- リサーチクエスチョン: {research_question}
- 提案手法: {proposed_method}
- 主要結果: {main_results}

【出力形式】
1行目: 研究テーマ（何を研究したのか）
2行目: 提案手法（どのような手法を提案したのか）
3行目: 主要結果（どのような結果が得られたのか）
```

**実行例**:
```python
def generate_answer_question_1(abstract_analysis):
    prompt = f"""
以下のAbstract分析結果をもとに、「どんなもの？」という質問に3行で答えてください。

【Abstract分析結果】
- リサーチクエスチョン: {abstract_analysis["research_question"]}
- 提案手法: {abstract_analysis["proposed_method"]}
- 主要結果: {abstract_analysis["main_results"]}

【出力形式】
1行目: 研究テーマ（何を研究したのか）
2行目: 提案手法（どのような手法を提案したのか）
3行目: 主要結果（どのような結果が得られたのか）
"""

    response = call_llm("claude", prompt)
    return response.strip()
```

#### 質問2: 「先行研究と比べてどこがすごい？」

**LLMプロンプトテンプレート**:
```
以下のRelated Work分析結果とIntroduction分析結果をもとに、「先行研究と比べてどこがすごい？」という質問に答えてください。

【Related Work分析】
{related_work_analysis}

【Introduction分析】
{introduction_analysis}

【出力形式】
- 既存手法の問題点: [先行研究が抱えていた問題]
- 本論文の解決策: [その問題をどう解決したか]
- 学術的価値: [この論文の学術的貢献]
- 差別化ポイント: [先行研究と比べてどこがすごいか、を簡潔に]
```

#### 質問3: 「技術や手法のキモはどこ？」

**LLMプロンプトテンプレート**:
```
以下のMethodsセクション分析結果と抽出された図表をもとに、「技術や手法のキモはどこ？」という質問に答えてください。

【Methods分析】
{methods_analysis}

【重要図表】
Figure {figure_number}: {figure_description}

【出力形式】
- 手法の概要: [提案手法の全体像]
- 技術的工夫: [核心的な技術的工夫]
- アルゴリズム: [使用したアルゴリズム（あれば）]
- 図表による説明: [図表を参照した視覚的説明]
```

**図表の埋め込み処理**:
```python
def embed_figure_in_summary(figure, figure_index, output_format="markdown"):
    if output_format == "markdown":
        # Markdown形式での図表埋め込み
        figure_path = save_figure_as_image(figure, figure_index)
        return f"![Figure {figure_index}]({figure_path})"

    elif output_format == "slide":
        # スライド形式での図表埋め込み
        return insert_figure_in_slide(figure, figure_index)

    elif output_format == "notion":
        # Notion形式での図表埋め込み
        figure_url = upload_figure_to_notion(figure, figure_index)
        return f"[Figure {figure_index}]({figure_url})"
```

#### 質問4: 「どうやって有効だと検証した？」

**LLMプロンプトテンプレート**:
```
以下のExperiments/Results分析結果をもとに、「どうやって有効だと検証した？」という質問に答えてください。

【Experiments/Results分析】
{experiments_analysis}

【出力形式】
- データセット: {dataset}
- 実験条件: {experimental_conditions}
- 評価指標: {evaluation_metrics}
- 主要結果: {main_results}
- ベースライン比較: {baseline_comparison}
- 統計的有意性: {statistical_significance}（あれば）
```

#### 質問5: 「議論はある？」

**LLMプロンプトテンプレート**:
```
以下のDiscussionセクション分析結果をもとに、「議論はある？」という質問に答えてください。
特に、批判的視点（限界点、今後の課題、適用範囲の制約）を必ず含めてください。

【Discussion分析】
{discussion_analysis}

【出力形式】
- 結果の解釈: [実験結果の意味するところ]
- 限界点: [この手法の限界点・弱点]
- 今後の課題: [今後解決すべき課題]
- 適用範囲の制約: [この手法が適用できない場面]
```

**批判的視点の自動生成**:
```python
def generate_critical_perspective(discussion_text, experiments_analysis):
    # Discussionセクションに限界点が明記されていない場合、自動生成
    if "limitation" not in discussion_text.lower() and "限界" not in discussion_text:
        # 実験条件から限界点を推測
        limitations = []

        # データセットサイズの限界
        if "small dataset" in experiments_analysis or "少ないデータ" in experiments_analysis:
            limitations.append("データセット規模が小さく、大規模データでの性能は未検証")

        # 計算コストの限界
        if "8 GPU" in experiments_analysis or "大規模計算環境" in experiments_analysis:
            limitations.append("学習に大規模な計算資源が必要で、個人研究者には適用困難")

        # ドメインの限界
        if "機械翻訳" in experiments_analysis:
            limitations.append("他のタスク（要約、質問応答等）への適用性は未検証")

        return {"auto_generated": True, "limitations": limitations}

    else:
        # Discussionセクションから限界点を抽出
        return extract_limitations_from_text(discussion_text)
```

#### 質問6: 「次に読むべき論文は？」

**LLMプロンプトテンプレート**:
```
以下のReferences分析結果とユーザーの研究テーマをもとに、「次に読むべき論文は？」という質問に答えてください。
3-5本の論文を推薦し、それぞれ選定理由を具体的に記述してください。

【References分析】
{references_analysis}

【ユーザーの研究テーマ】
{user_research_theme}

【出力形式】
1. [論文タイトル] (著者, 年) - [選定理由]
2. [論文タイトル] (著者, 年) - [選定理由]
3. [論文タイトル] (著者, 年) - [選定理由]
```

**推薦アルゴリズムの詳細**:
```python
def recommend_next_papers(references, user_research_theme, existing_papers, count=3):
    scored_papers = []

    for ref in references:
        score = 0

        # スコアリング要素1: 引用頻度（Google Scholarで確認）
        citation_count = get_citation_count(ref["title"])
        score += min(citation_count / 100, 10)  # 最大10点

        # スコアリング要素2: 年代（新しい論文を優先、ただし古典は例外）
        year = ref.get("year", 2000)
        if year >= 2020:
            score += 5
        elif year >= 2015:
            score += 3
        elif year >= 2000 and citation_count > 1000:  # 古典的論文
            score += 7

        # スコアリング要素3: 著者の権威性（h-index）
        h_index = get_h_index(ref["authors"])
        score += min(h_index / 10, 5)  # 最大5点

        # スコアリング要素4: ユーザーの研究テーマとの関連度
        if user_research_theme:
            similarity = calculate_semantic_similarity(ref["title"], user_research_theme)
            score += similarity * 10  # 最大10点

        # スコアリング要素5: 既読論文との重複チェック
        if ref["title"] in existing_papers:
            score = 0  # 既読論文はスコア0

        scored_papers.append({"reference": ref, "score": score})

    # スコア順にソート
    scored_papers_sorted = sorted(scored_papers, key=lambda x: x["score"], reverse=True)

    # 上位N本を推薦
    recommendations = []
    for i in range(min(count, len(scored_papers_sorted))):
        paper = scored_papers_sorted[i]
        recommendations.append({
            "reference": paper["reference"],
            "reason": generate_recommendation_reason(paper["reference"], paper["score"]),
        })

    return recommendations
```

**推薦理由の生成**:
```python
def generate_recommendation_reason(reference, score):
    reasons = []

    # 引用頻度による理由
    citation_count = get_citation_count(reference["title"])
    if citation_count > 1000:
        reasons.append(f"被引用数{citation_count}回の古典的論文")

    # 年代による理由
    year = reference.get("year", 2000)
    if year >= 2023:
        reasons.append("最新の研究動向を反映")

    # 内容による理由（タイトルからキーワード抽出）
    if "survey" in reference["title"].lower() or "review" in reference["title"].lower():
        reasons.append("この分野の包括的なサーベイ論文")
    elif "理論" in reference["title"] or "theoretical" in reference["title"].lower():
        reasons.append("提案手法の理論的背景を詳述")
    elif "応用" in reference["title"] or "application" in reference["title"].lower():
        reasons.append("別ドメインへの応用事例")

    return "、".join(reasons)
```

**使用ツール**:
- LLMプロンプトチェーン
- 批判的思考モデル
- 引用ネットワーク解析
- セマンティック類似度計算（sentence-transformers等）

**注意点**:
- 各質問への回答は簡潔に（1-3段落以内）
- 理論論文の場合は質問のバリエーション適用（批判されている理論、文脈・理路の追跡等）
- 必ず批判的視点（限界点、今後の課題）を含める

---

### ステップ5: サマリー生成

#### 5.1 A4 1枚スライド生成（PowerPoint/PDF）

**スライド生成処理**:
```python
from pptx import Presentation
from pptx.util import Inches, Pt

def generate_slide_summary(six_questions, figures):
    prs = Presentation()
    prs.slide_width = Inches(11.69)  # A4横
    prs.slide_height = Inches(8.27)

    # タイトルスライド
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # 空白レイアウト

    # タイトル部分
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(10.69), Inches(0.6))
    title_frame = title_box.text_frame
    title_frame.text = six_questions["title"]
    title_frame.paragraphs[0].font.size = Pt(18)
    title_frame.paragraphs[0].font.bold = True

    # 6つの質問を6つのボックスに配置
    box_positions = [
        (0.5, 1.2, 5.0, 1.8),  # 質問1: どんなもの？
        (5.7, 1.2, 5.5, 1.8),  # 質問2: 先行研究と比べてどこがすごい？
        (0.5, 3.2, 5.0, 2.0),  # 質問3: 技術や手法のキモはどこ？（図表含む）
        (5.7, 3.2, 5.5, 1.3),  # 質問4: どうやって有効だと検証した？
        (5.7, 4.7, 5.5, 1.3),  # 質問5: 議論はある？
        (0.5, 5.4, 5.0, 1.8),  # 質問6: 次に読むべき論文は？
    ]

    for i, (question, answer) in enumerate(six_questions["answers"].items()):
        left, top, width, height = box_positions[i]
        text_box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
        text_frame = text_box.text_frame

        # 質問見出し
        p = text_frame.paragraphs[0]
        p.text = f"{i+1}. {question}"
        p.font.size = Pt(12)
        p.font.bold = True

        # 回答
        p = text_frame.add_paragraph()
        p.text = answer
        p.font.size = Pt(10)

    # 図表の挿入（質問3のボックス内）
    if figures:
        figure = figures[0]
        slide.shapes.add_picture(figure["path"], Inches(0.5), Inches(3.5), width=Inches(4.5))

    # PDFとして保存
    prs.save("summary_slide.pptx")
    convert_pptx_to_pdf("summary_slide.pptx", "summary_slide.pdf")

    return "summary_slide.pdf"
```

#### 5.2 Markdown形式生成

**Markdownテンプレートエンジン**:
```python
def generate_markdown_summary(six_questions, figures, metadata):
    template = """# {title}

**著者**: {authors}
**発表**: {venue}, {year}
**URL**: {url}

## 1. どんなもの？
{question_1}

## 2. 先行研究と比べてどこがすごい？
{question_2}

## 3. 技術や手法のキモはどこ？
{question_3}

{figure_1}

## 4. どうやって有効だと検証した？
{question_4}

## 5. 議論はある？
{question_5}

## 6. 次に読むべき論文は？
{question_6}

---
**読了日**: {read_date}
**読解時間**: {read_time}分
**自分のテーマとの関連**: {relevance_note}
"""

    # テンプレートへのデータ埋め込み
    markdown_content = template.format(
        title=six_questions["title"],
        authors=metadata["authors"],
        venue=metadata["venue"],
        year=metadata["year"],
        url=metadata["url"],
        question_1=six_questions["answers"]["どんなもの？"],
        question_2=six_questions["answers"]["先行研究と比べてどこがすごい？"],
        question_3=six_questions["answers"]["技術や手法のキモはどこ？"],
        figure_1=f"![Figure 1]({figures[0]['path']})" if figures else "",
        question_4=six_questions["answers"]["どうやって有効だと検証した？"],
        question_5=six_questions["answers"]["議論はある？"],
        question_6=six_questions["answers"]["次に読むべき論文は？"],
        read_date=datetime.now().strftime("%Y-%m-%d"),
        read_time=metadata["read_time"],
        relevance_note=metadata.get("relevance_note", ""),
    )

    # Markdownファイルとして保存
    with open("summary.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return "summary.md"
```

#### 5.3 視覚的デザイン

**色分けルール**:
```python
# 質問ごとの色コード（スライド形式）
question_colors = {
    "1. どんなもの？": "RGB(200, 220, 255)",  # 水色
    "2. 先行研究と比べてどこがすごい？": "RGB(255, 220, 200)",  # オレンジ
    "3. 技術や手法のキモはどこ？": "RGB(220, 255, 200)",  # 緑
    "4. どうやって有効だと検証した？": "RGB(255, 255, 200)",  # 黄色
    "5. 議論はある？": "RGB(255, 200, 220)",  # ピンク
    "6. 次に読むべき論文は？": "RGB(220, 200, 255)",  # 紫
}
```

**使用ツール**:
- スライド生成API（python-pptx）
- Markdownテンプレートエンジン（Jinja2）
- 図表埋め込みツール

**注意点**:
- A4半分〜1枚への圧縮を徹底（情報優先度付けの訓練）
- 完璧主義を避け、フィードバックループ重視
- 図表が抽出できない場合はテキストのみで構成

---

### ステップ6: データベース登録

#### 6.1 Notionデータベースへの自動登録

**Notion API接続**:
```python
import requests

NOTION_API_KEY = "secret_xxxxxxxxxxxxxxxxxxxx"
DATABASE_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

def create_notion_page(six_questions, metadata, references):
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    # Notionページのプロパティ設定
    properties = {
        "Title": {"title": [{"text": {"content": six_questions["title"]}}]},
        "Authors": {"multi_select": [{"name": author} for author in metadata["authors"].split(", ")]},
        "Year": {"number": metadata["year"]},
        "Conference/Journal": {"select": {"name": metadata["venue"]}},
        "PDF": {"url": metadata["pdf_url"]},
        "Tags": {"multi_select": generate_tags(six_questions, metadata)},
        "Summary": {"rich_text": [{"text": {"content": format_summary_for_notion(six_questions)}}]},
        "Read Date": {"date": {"start": datetime.now().strftime("%Y-%m-%d")}},
        "Read Time": {"number": metadata["read_time"]},
        "Relevance": {"select": {"name": metadata.get("relevance", "Medium")}},
    }

    # Notionページの本文（6つの質問への回答）
    children = generate_notion_blocks(six_questions)

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": properties,
        "children": children,
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        page_url = response.json()["url"]
        print(f"[INFO] Notionページ作成完了: {page_url}")
        return page_url
    else:
        print(f"[ERROR] Notionページ作成失敗: {response.text}")
        return None
```

#### 6.2 タグ自動生成

**タグ生成アルゴリズム**:
```python
def generate_tags(six_questions, metadata):
    tags = []

    # 研究分野タグ（タイトルとAbstractから抽出）
    field_keywords = {
        "Machine Learning": ["machine learning", "深層学習", "neural network"],
        "NLP": ["natural language processing", "自然言語処理", "言語モデル"],
        "Computer Vision": ["computer vision", "画像認識", "object detection"],
        "HCI": ["human-computer interaction", "ユーザインタフェース"],
        "Robotics": ["robotics", "ロボット", "制御"],
    }

    title_and_abstract = six_questions["title"] + " " + six_questions["answers"]["どんなもの？"]

    for field, keywords in field_keywords.items():
        if any(keyword in title_and_abstract.lower() for keyword in keywords):
            tags.append({"name": field})

    # 手法タグ（Methodsから抽出）
    method_keywords = {
        "Transformer": ["transformer", "attention"],
        "CNN": ["convolutional", "畳み込み"],
        "RNN": ["recurrent", "LSTM", "GRU"],
        "Reinforcement Learning": ["reinforcement", "強化学習", "Q-learning"],
    }

    methods_text = six_questions["answers"]["技術や手法のキモはどこ？"]

    for method, keywords in method_keywords.items():
        if any(keyword in methods_text.lower() for keyword in keywords):
            tags.append({"name": method})

    # 応用領域タグ
    application_keywords = {
        "Machine Translation": ["machine translation", "機械翻訳"],
        "Image Generation": ["image generation", "画像生成", "GAN"],
        "Speech Recognition": ["speech recognition", "音声認識"],
    }

    for application, keywords in application_keywords.items():
        if any(keyword in title_and_abstract.lower() for keyword in keywords):
            tags.append({"name": application})

    # 既存タグとのマッチング優先（一貫性保持）
    existing_tags = get_existing_tags_from_notion(DATABASE_ID)
    matched_tags = []

    for tag in tags:
        if tag["name"] in existing_tags:
            matched_tags.append(tag)
        else:
            # 新規タグの場合は類似タグを検索
            similar_tag = find_similar_tag(tag["name"], existing_tags)
            if similar_tag:
                matched_tags.append({"name": similar_tag})
            else:
                matched_tags.append(tag)  # 新規タグとして追加

    return matched_tags
```

#### 6.3 引用ネットワーク構築

**Notion Relation機能での論文間リンク**:
```python
def link_references_in_notion(current_page_id, recommended_papers):
    # 推薦論文がすでにNotionデータベースに存在するか確認
    for paper in recommended_papers:
        existing_page = search_paper_in_notion(paper["reference"]["title"])

        if existing_page:
            # Relation機能で既存ページにリンク
            add_relation_to_page(current_page_id, "Next Papers", existing_page["id"])
            print(f"[INFO] Relation追加: {paper['reference']['title']}")
        else:
            # 存在しない場合は新規ページ作成予定として記録
            print(f"[INFO] 次回読解時に自動リンク: {paper['reference']['title']}")
```

**Neo4jでのグラフデータベース構築**（将来的な拡張）:
```python
from neo4j import GraphDatabase

def build_citation_network(paper, references):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    with driver.session() as session:
        # 現在の論文をノードとして追加
        session.run(
            "CREATE (p:Paper {title: $title, year: $year, authors: $authors})",
            title=paper["title"],
            year=paper["year"],
            authors=paper["authors"],
        )

        # 引用論文をノードとして追加し、CITESエッジを作成
        for ref in references:
            session.run(
                """
                MERGE (r:Paper {title: $ref_title})
                ON CREATE SET r.year = $ref_year, r.authors = $ref_authors
                WITH r
                MATCH (p:Paper {title: $paper_title})
                CREATE (p)-[:CITES]->(r)
                """,
                ref_title=ref["title"],
                ref_year=ref["year"],
                ref_authors=ref["authors"],
                paper_title=paper["title"],
            )

    driver.close()
    print(f"[INFO] 引用ネットワーク構築完了: {len(references)}本のリンク")
```

**使用ツール**:
- Notion API
- グラフデータベース（Neo4j等）
- タグ自動生成AI（LLMベースのキーワード抽出）

**注意点**:
- Notion API失敗時はローカルファイルとして保存し、後で手動登録を促す
- タグの一貫性を保つため、既存タグとのマッチング優先
- 引用ネットワークは段階的に構築（初回は単独ノードでOK）

---

### ステップ7: 次の論文推薦

（ステップ4の質問6で実装済みのため、ここでは省略）

---

### ステップ8: 出力返却と統計表示

#### 8.1 サマリーファイルの返却

**ユーザーへの出力**:
```python
def return_output_to_user(summary_files, notion_url, recommendations, stats):
    output_message = f"""
✅ 論文サマリー作成完了

📄 生成ファイル:
"""

    for file_type, file_path in summary_files.items():
        output_message += f"- {file_type}: {file_path}\n"

    if notion_url:
        output_message += f"\n📊 Notionページ: {notion_url}\n"

    output_message += f"""
📚 次に読むべき論文:
"""

    for i, rec in enumerate(recommendations):
        output_message += f"{i+1}. {rec['reference']['title']} ({rec['reference']['year']}) - {rec['reason']}\n"

    output_message += f"""
⏱️ 読解時間: {stats['read_time']}分
📈 累計読了論文数: {stats['total_papers_read']}本
"""

    print(output_message)
    return output_message
```

#### 8.2 統計情報の可視化

**週次統計レポート**:
```python
import matplotlib.pyplot as plt

def generate_weekly_stats_report():
    # Notionデータベースから今週の読了論文を取得
    this_week_papers = get_papers_read_this_week()

    stats = {
        "total_papers_read": len(get_all_papers()),
        "this_week_count": len(this_week_papers),
        "avg_read_time": calculate_average_read_time(this_week_papers),
        "field_distribution": calculate_field_distribution(this_week_papers),
    }

    # 分野別分布の円グラフ
    plt.figure(figsize=(8, 6))
    plt.pie(
        stats["field_distribution"].values(),
        labels=stats["field_distribution"].keys(),
        autopct="%1.1f%%",
    )
    plt.title("今週の読了論文 分野別分布")
    plt.savefig("weekly_stats_field_distribution.png")

    # 読解時間の推移グラフ
    plt.figure(figsize=(10, 6))
    weekly_read_times = get_weekly_read_times_last_12_weeks()
    plt.plot(weekly_read_times.keys(), weekly_read_times.values(), marker='o')
    plt.xlabel("週")
    plt.ylabel("平均読解時間（分）")
    plt.title("週次平均読解時間の推移")
    plt.grid(True)
    plt.savefig("weekly_stats_read_time_trend.png")

    return stats
```

**励みになる表示**:
```python
def generate_encouragement_message(stats):
    messages = []

    # 前週比の改善
    last_week_avg = get_last_week_average_read_time()
    if stats["avg_read_time"] < last_week_avg:
        improvement = last_week_avg - stats["avg_read_time"]
        messages.append(f"🎉 先週比{improvement:.1f}分短縮！効率化が進んでいます！")

    # 目標達成率
    weekly_goal = 25  # 週25本目標
    achievement_rate = (stats["this_week_count"] / weekly_goal) * 100
    if achievement_rate >= 100:
        messages.append(f"🏆 週次目標達成！({stats['this_week_count']}/{weekly_goal}本)")
    else:
        messages.append(f"📊 週次進捗: {achievement_rate:.1f}% ({stats['this_week_count']}/{weekly_goal}本)")

    # マイルストーン達成
    if stats["total_papers_read"] == 100:
        messages.append("🎊 累計100本達成！素晴らしいペースです！")
    elif stats["total_papers_read"] == 500:
        messages.append("🌟 累計500本達成！研究分野の約2年分の知見を習得しました！")

    return "\n".join(messages)
```

**使用ツール**:
- ファイルホスティング
- 統計ダッシュボード（Matplotlib, Plotly）
- 進捗管理ツール

**注意点**:
- 出力形式が複数選択されている場合は全形式を生成
- 統計情報は励みになるよう、前回比や目標達成率を含める
- エラーが発生した場合も部分的な成果物は返却

---

## エラーハンドリング詳細

### エラー分類と対処法

#### レベル1: 軽微なエラー（処理継続可能）

**例1: 図表抽出失敗**
```python
try:
    figures = extract_figures(pdf_path)
except Exception as e:
    print(f"[WARN] 図表抽出失敗: {e}")
    print("[INFO] テキストのみでサマリー生成を続行します")
    figures = []
```

**例2: セクション検出失敗**
```python
sections, full_text = detect_paper_sections(pdf_path)

if sections["Abstract"] is None:
    print("[WARN] Abstractセクションが検出できませんでした")
    print("[INFO] 全文の最初の500文字をAbstractとみなします")
    sections = fallback_section_detection(full_text)
```

#### レベル2: 中程度のエラー（代替処理必要）

**例1: Notion API失敗**
```python
try:
    notion_url = create_notion_page(six_questions, metadata, references)
except requests.exceptions.HTTPError as e:
    print(f"[ERROR] Notion API失敗: {e}")
    print("[INFO] ローカルファイルとして保存します")

    # ローカルファイルとして保存
    save_as_local_file(six_questions, metadata)

    # 後で手動登録を促すメッセージ
    print("[INFO] 後でNotionに手動登録してください:")
    print(f"       ファイル: summary_local_backup.json")

    notion_url = None
```

**例2: LLM API失敗**
```python
try:
    response = call_llm("claude", prompt)
except Exception as e:
    print(f"[ERROR] LLM API失敗: {e}")
    print("[INFO] 代替モデル（GPT-4）で再試行します")

    try:
        response = call_llm("gpt4", prompt)
    except Exception as e2:
        print(f"[ERROR] 代替モデルも失敗: {e2}")
        print("[ERROR] このステップをスキップします")
        response = None
```

#### レベル3: 致命的なエラー（処理中断）

**例1: PDF読み込み失敗**
```python
try:
    pdf_path = download_pdf(pdf_url)
    reader = PdfReader(pdf_path)
except Exception as e:
    print(f"[ERROR] PDF読み込み失敗: {e}")
    print("[ERROR] 処理を中断します。以下を確認してください:")
    print("       1. URLが正しいか確認")
    print("       2. PDFファイルが破損していないか確認")
    print("       3. ローカルPDFファイルを直接アップロード")
    raise
```

---

## ベストプラクティス（詳細版）

### 1. 効率的な論文読解の週次ルーティン

**月曜（計画フェーズ）**:
```
1. 今週読むべき論文リスト作成（25本選定）
   - カンファレンス（CVPR, NeurIPS等）のプログラムから選定
   - 引用ネットワークから次に読むべき論文を選定
   - 自分の研究テーマとの関連性でフィルタリング

2. 優先度付け
   - High Priority（5本）: 自分の研究テーマに直結
   - Medium Priority（15本）: 関連分野の重要論文
   - Low Priority（5本）: 興味本位の論文
```

**火-木（実行フェーズ）**:
```
1. Quick Modeで20本読解（1日7本×3日）
   - 朝: 3本（9:00-10:30）
   - 午後: 4本（14:00-16:00）
   - 1本10分×7本 = 70分/日

2. その場でNotionに登録
   - 読解完了直後にNotionに登録（記憶が新しいうちに）
   - タグ付けを忘れずに
```

**金曜（精読フェーズ）**:
```
1. Standard Modeで重要論文5本を精読
   - High Priority論文を1本30分×5本 = 150分

2. 週次統計レポートを確認
   - 累計読了論文数
   - 今週の平均読解時間
   - 分野別分布
```

**週末（振り返りフェーズ）**:
```
1. 今週読んだ論文を振り返る
   - Notionデータベースで今週のタグを確認
   - 引用ネットワークを可視化
   - 自分の研究テーマとの関連を再確認

2. 次週の目標設定
   - 来週読むべき論文リストを作成
   - 読解時間の目標設定（平均15分/本等）
```

### 2. LLM活用のハイブリッドアプローチ

**フェーズ1: LLMによる自動要約**
```python
# 6つの質問をプロンプトに組み込み、自動回答生成
six_questions_auto = generate_six_questions_with_llm(pdf_path)
```

**フェーズ2: 人間による批判的評価**
```python
# LLM出力を読み、以下を追加
critical_notes = {
    "限界点": "データセット規模が小さく、大規模データでの性能は未検証",
    "今後の課題": "他のタスク（要約、質問応答等）への適用性の検証",
    "自分のテーマとの関連": "LLMエージェントの並列実行に応用可能",
}
```

**フェーズ3: 統合サマリーの作成**
```python
# LLM自動生成 + 人間の批判的視点 = 最終サマリー
final_summary = merge_auto_and_critical(six_questions_auto, critical_notes)
```

---

## プロンプトテンプレート集

### テンプレート1: Abstract分析

```
あなたは学術論文の専門家です。以下の論文のAbstractを読み、リサーチクエスチョンと全体像を3行で要約してください。

【Abstract】
{abstract_text}

【出力形式】
- リサーチクエスチョン: [この論文が解こうとしている問題]
- 提案手法: [問題を解決するために提案した手法]
- 主要結果: [実験で得られた主要な結果]

【注意事項】
- 各項目は1行で簡潔に記述してください
- 専門用語を使用する場合は、必要に応じて括弧内に日本語訳を追加してください
- 数値結果がある場合は必ず含めてください
```

### テンプレート2: 批判的視点の生成

```
あなたは批判的思考に優れた研究者です。以下の論文のDiscussionセクションを読み、限界点と今後の課題を抽出してください。

【Discussionセクション】
{discussion_text}

【実験条件】
{experiments_analysis}

【出力形式】
- 限界点:
  1. [限界点1]
  2. [限界点2]
  3. [限界点3]
- 今後の課題:
  1. [課題1]
  2. [課題2]
- 適用範囲の制約:
  - [この手法が適用できない場面]

【注意事項】
- Discussionセクションに明記されていない限界点も、実験条件から推測して記述してください
- 必ず批判的視点を含めてください（単なる要約ではなく、問題点の指摘）
- 「この手法は完璧」といった記述は避けてください
```

### テンプレート3: 次の論文推薦

```
あなたは研究分野の専門家です。以下のReferences分析結果とユーザーの研究テーマをもとに、次に読むべき論文を3本推薦してください。

【References分析】
{references_analysis}

【ユーザーの研究テーマ】
{user_research_theme}

【既読論文】
{existing_papers}

【出力形式】
1. [論文タイトル] (著者, 年) - [選定理由（具体的に）]
2. [論文タイトル] (著者, 年) - [選定理由（具体的に）]
3. [論文タイトル] (著者, 年) - [選定理由（具体的に）]

【注意事項】
- 既読論文は推薦しないでください
- 選定理由は具体的に記述してください（「重要だから」ではなく「提案手法の理論的背景を詳述しているから」等）
- 引用頻度が高い古典的論文と、最新の研究動向を反映した論文をバランスよく推薦してください
```

---

## 参照

- **エージェントファイル**: @.claude/agents/deep_research_to_note.md
- **統合分析結果**: @aipm_v0/Flow/202512/2025-12-31/deep_research_methodology_integrated.md
- **動画抽出結果**: @aipm_v0/Flow/202512/2025-12-31/ochiai_video_deep_research_extract.md
