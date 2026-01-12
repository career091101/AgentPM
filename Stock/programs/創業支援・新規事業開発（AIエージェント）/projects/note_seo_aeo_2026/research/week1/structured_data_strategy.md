# 構造化データ実装戦略 - note.com AEO最適化ガイド

## 目次
1. [構造化データの重要性](#構造化データの重要性)
2. [AIプラットフォームにおける構造化データの役割](#aiプラットフォームにおける構造化データの役割)
3. [推奨スキーマタイプ](#推奨スキーマタイプ)
4. [note.com制約下での実装方法](#notecom制約下での実装方法)
5. [実装例](#実装例)
6. [検証と測定](#検証と測定)
7. [よくある質問](#よくある質問)

---

## 構造化データの重要性

### 従来SEOにおける役割
- リッチスニペット表示（スターレーティング、価格情報等）
- Google Assistant対応
- ボイスサーチ最適化

### AI検索エンジン時代での新しい役割
- **AI citation rate +156%**（マルチモーダル構造化データ含む場合）
- **信頼性シグナル強化**: 構造化データ存在 = コンテンツの明確性と権威性
- **エンティティ解析**: AIが著者、組織、概念を正確に識別
- **セマンティック理解**: コンテンツの意図と構造を機械可読形式で提供

### Google AI Overviewsにおける相関性

2025年のデータ分析結果（r相関値）:
- E-E-A-T信号との組合せ: r=0.89
- セマンティック完全性との相乗効果: r=0.87
- マルチモーダル要素との連携: r=0.92

**結論**: 構造化データ単独では十分ではないが、E-E-A-Tシグナルおよび高品質コンテンツと組み合わせた場合に最大効果を発揮

---

## AIプラットフォームにおける構造化データの役割

### ChatGPT
- **インデックス処理**: 定期的にウェブをクローリング、コンテンツを解析
- **構造化データの利用**: 最小限。著者情報、公開日、更新日を参考
- **優先度**: 低～中（形式フリーのテキスト解析が優先）

### Perplexity
- **実時間検索**: リアルタイムでウェブをクローリング
- **構造化データの利用**: 中程度。FAQスキーマで Q&A を認識、更新日を優先
- **優先度**: 中～高（新鮮性と構造を重視）

### Google AI Overviews
- **検索インデックス連動**: Google SERPの同じインデックスを使用
- **構造化データの利用**: 高い。Schema.org準拠データを直接参照
- **優先度**: 非常に高い（必須ではないが、強力な最適化要素）

---

## 推奨スキーマタイプ

### Tier 1: 必須スキーマ（すべての記事）

#### 1. **Article Schema**

**用途**: ブログ記事、解説記事、ニュース記事等

**なぜ重要か**:
- 公開日、更新日をAIが認識
- 著者情報の標準化
- ナビゲーション（ブレッドクラム等）の提供

**対応プラットフォーム**: Google AI Overviews（必須）、ChatGPT（参考）、Perplexity（参考）

---

### Tier 2: 高優先度スキーマ

#### 2. **FAQPage Schema**

**用途**: 質問-回答形式のコンテンツ

**効果**:
- Perplexity: 新鮮性認識 + Q&A構造を直接抽出
- Google AI Overviews: FAQ段落が直接引用される確率が高い
- Google Search: リッチスニペット表示（ただし可視性は低下）

**優先度**: 非常に高い

**実装ポイント**:
- 各 `Question` に対する `acceptedAnswer` を完全に記入
- 質問数は3-10個が適切（多すぎるとスパムと判定される）
- テキストベース（HTMLタグ不可）で記入

---

#### 3. **HowTo Schema**

**用途**: ステップバイステップのプロセス、チュートリアル、ガイド

**効果**:
- Google AI Overviews: ステップが順序付きリストとして認識され、正確に引用
- YouTube等の動画サイト: 各ステップを動画内のタイムスタンプで表示
- 音声検索: ステップの読み上げが可能

**優先度**: 高い

**実装ポイント**:
- `itemListElement` で各ステップを配列として定義
- 各ステップに `name`（ステップ名）と `text`（詳細説明）
- オプション: `image` や `video` を各ステップに含める
- `totalTime` で総実行時間を指定（ISO 8601形式: PT2H30M）

---

### Tier 3: 補完スキーマ

#### 4. **Person Schema（著者情報）**

**用途**: 著者の詳細情報提供

**効果**:
- E-E-A-T信号強化: AIが著者の専門性を認識
- ブランド信頼性: 著者情報の充実 = 記事の信頼性向上
- Google Knowledge Graph: 著者が有名人の場合、知識グラフに登録される可能性

**優先度**: 中～高（E-E-A-T強化のため）

**実装ポイント**:
- `name`, `url`, `description` は必須
- `image` でプロフィール画像を提供（顔写真推奨）
- `jobTitle`, `worksFor` で職歴を明記
- `sameAs` で LinkedIn、Twitter等への外部リンク（複数可）
- `credential` で資格情報を記入（例: 医師免許、FP資格）

---

#### 5. **Organization Schema（企業・組織情報）**

**用途**: 企業やメディアの基本情報

**効果**:
- ブランド認知: Google Knowledge Graphへの登録
- 信頼性シグナル: 正式な企業情報をAIが認識
- ローカルSEO: 住所、電話番号、営業時間を提供

**優先度**: 中（法人の場合）、低（個人は必須ではない）

**実装ポイント**（note.comの場合）:
- `name`: note.com またはメディア名
- `url`: https://note.com
- `logo`: note.comロゴのURL
- `sameAs`: TwitterアカウントURL等

---

#### 6. **BreadcrumbList Schema（ナビゲーション）**

**用途**: ページの階層構造を示す

**効果**:
- ユーザー体験向上: Google SERPでパンくず表示
- AIの文脈理解: サイト階層をAIが認識

**優先度**: 低（note.comでは通常不要）

---

### Tier 4: スペシャライズドスキーマ

#### 7. **NewsArticle Schema**

**用途**: ニュース記事、時事速報

**効果**:
- Perplexity: ニュース記事として認識、リアルタイム性が高まる
- Google News: ニュースセクションへの掲載可能性

**優先度**: 低（note.comではニュース媒体でないため不要）

---

#### 8. **Speakable Schema（音声読み上げ対応）**

**用途**: 音声検索、Google Assistant対応

**効果**:
- 音声検索: 関連コンテンツが音声で読み上げられる対象として認識
- アクセシビリティ: 視覚障碍者向け対応

**優先度**: 低～中（音声検索最適化が目標の場合は中）

**実装例**:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "speakablePassage": [
    {
      "@type": "SpeakableSpecification",
      "cssSelector": [".summary", ".conclusion"]
    }
  ]
}
```

---

#### 9. **Review/AggregateRating Schema**

**用途**: 製品レビュー、サービス評価

**効果**:
- Google Search: スターレーティングの表示
- AI Overviews: 評価情報の直接引用

**優先度**: 低～中（レビュー記事の場合は中）

---

## note.com制約下での実装方法

### note.comの技術制限

| 機能 | 可否 | 代替手段 |
|------|------|---------|
| head内へのカスタムHTML挿入 | ✗（ノーマル版） | note Pro版のHTMLコードブロック |
| JSON-LD schema挿入 | ◎ note Pro版のみ | HTMLコードブロックを使用 |
| メタタグ編集 | ✗ | 不可（note.comの制限） |
| OGPカスタマイズ | 限定的 | note の自動生成に依存 |
| robots.txt編集 | ✗ | 不可 |

### 実装手順（note Pro版）

#### Step 1: note Pro版への加入

- 月額600円（iOS/Android）または月額1,100円（Web）
- 「コンテンツの販売」「HTMLコード」機能が利用可能

#### Step 2: 記事作成時にHTMLコードブロックを挿入

記事編集画面で:
1. テキスト入力エリアを開く
2. 「+」ボタン → 「HTMLコード」を選択
3. JSON-LD schema をペースト
4. 公開

#### Step 3: 構造化データの配置位置

**推奨**: 記事冒頭（最初の段落の直後）
- AIのクローラーは、ページ上部から順にコンテンツをスキャン
- スキーマがすぐに見つかると、解析精度が向上

**非推奨**: 記事末尾
- ユーザーがスクロールする必要がなく、見出しと誤認識リスクが低い一方
- AI クローラーが記事末尾まで読み込まない場合がある

---

## 実装例

### 例1: Article + Person Schema（基本形）

note Pro版の HTMLコードブロック内に、以下を記入:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Perplexity・Google AI Overviews引用パターン分析",
  "description": "ChatGPT、Perplexity、Google AI Overviewsの引用パターンを包括的に分析し、note.com上でのAEO最適化戦略を提示します。",
  "datePublished": "2025-01-10T00:00:00+09:00",
  "dateModified": "2025-01-10T15:30:00+09:00",
  "author": {
    "@type": "Person",
    "name": "山田太郎",
    "url": "https://note.com/@yamada_taro",
    "image": "https://d2l930y2yx77uc.cloudfront.net/.../avatar.jpg",
    "description": "AI検索最適化（AEO）専門家。15年間のマーケティング経験、Google認定SEOスペシャリスト。",
    "jobTitle": "AEO Consultant & Content Strategist",
    "sameAs": [
      "https://twitter.com/yamada_taro",
      "https://www.linkedin.com/in/yamada_taro/"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "note",
    "logo": {
      "@type": "ImageObject",
      "url": "https://assets.st-note.com/production/uploads/images/logo.png"
    }
  },
  "image": {
    "@type": "ImageObject",
    "url": "https://d2l930y2yx77uc.cloudfront.net/.../thumbnail.jpg",
    "width": 1200,
    "height": 630
  }
}
</script>
```

**解説**:
- `datePublished` / `dateModified`: ISO 8601形式（UTC+09:00は日本時間）
- `author.url`: note.comプロフィールURL
- `image`: アイキャッチ画像のURL（1200×630px推奨）
- `publisher`: note.comの情報（自動で認識されることも多い）

---

### 例2: Article + FAQPage Schema（Q&A記事）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Perplexityに引用されるにはどうすればいいですか？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "著者の認定資格・経歴を明示し、リアルタイム性（2-3日ごとの更新）、高いエンティティ密度（固有名詞・数値）を重視してください。さらに、セマンティックURL構造（5-7語）を採用すると11.4%の引用増加が期待できます。"
      }
    },
    {
      "@type": "Question",
      "name": "Google AI Overviewsで引用されるための優先事項は？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "E-E-A-T（Experience, Expertise, Authoritativeness, Trustworthiness）信号の強化が最優先です。次に、マルチモーダルコンテンツ（画像、ビデオ、表）、セマンティック完全性（134-167語の自己完結した回答）を実装してください。構造化データ（FAQPage、HowTo、Article schema）も重要です。"
      }
    },
    {
      "@type": "Question",
      "name": "構造化データはAI検索に影響しますか？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "はい。構造化データ（Schema.org）は、特にGoogle AI Overviewsで重要です。Article、FAQPage、HowTo schemaを実装することで、コンテンツの明確性と権威性がAIに認識されやすくなり、引用率が向上します。"
      }
    }
  ]
}
</script>
```

**ポイント**:
- 各 `acceptedAnswer` の `text` は、完全で自己完結した答えを提供
- 複数の関連質問を網羅（3-10個が適切）
- HTMLタグ（`<p>`, `<br>`等）は含めない（プレーンテキストのみ）

---

### 例3: HowTo Schema（ステップバイステップガイド）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "note.comでAEO対応コンテンツを作成する方法",
  "description": "note.comでPerplexity、Google AI Overviewsに最適化されたコンテンツを制作するための完全ガイド",
  "image": {
    "@type": "ImageObject",
    "url": "https://d2l930y2yx77uc.cloudfront.net/.../howto_image.jpg"
  },
  "totalTime": "PT1H30M",
  "estimatedCost": {
    "@type": "PriceSpecification",
    "priceCurrency": "JPY",
    "price": "0",
    "description": "note Pro版の初期投資（月額1,100円）のみ"
  },
  "tool": [
    {
      "@type": "HowToTool",
      "name": "note Pro版"
    },
    {
      "@type": "HowToTool",
      "name": "Google Rich Results Test"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "note Pro版に加入する",
      "text": "月額1,100円（Web）を支払い、note Pro版にアップグレードします。HTMLコード機能が利用可能になります。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step1.jpg"
      }
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "セマンティックタイトルを設定",
      "text": "記事タイトルを5-7語の自然言語で表現します。例：『Perplexity・Google AI Overviews引用パターン分析』（7語）。キーワードを含め、かつ自然な日本語にします。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step2.jpg"
      }
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "構造化データ（Article Schema）を埋め込む",
      "text": "記事の冒頭にHTMLコードブロックを挿入し、Article SchemaのJSON-LDを貼り付けます。datePublished、dateModified、author情報を正確に記入してください。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step3.jpg"
      }
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "E-E-A-T信号を強化",
      "text": "著者プロフィール、保有資格、経歴をコンテンツに明記します。外部ソースへのリンクを充実させ、信頼性を高めます。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step4.jpg"
      }
    },
    {
      "@type": "HowToStep",
      "position": 5,
      "name": "マルチモーダルコンテンツを追加",
      "text": "画像（比較表、グラフ）、埋込ツイート、YouTube動画を記事内に組み込みます。各画像にはALTテキストを記入。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step5.jpg"
      }
    },
    {
      "@type": "HowToStep",
      "position": 6,
      "name": "Google Rich Results Testで検証",
      "text": "Google Search Central（https://search.google.com/test/rich-results）にnote.com記事のURLを入力。Schema markupエラーがないことを確認します。",
      "image": {
        "@type": "ImageObject",
        "url": "https://d2l930y2yx77uc.cloudfront.net/.../step6.jpg"
      }
    }
  ]
}
</script>
```

**ポイント**:
- `step`: 各ステップを配列で順序付けして定義
- `position`: ステップの順番（1から始まる）
- `image`: 各ステップに対応した画像（高品質推奨）
- `totalTime`: ISO 8601形式（PT1H30M = 1時間30分）
- `tool`: このハウツーに必要なツールを列挙

---

### 例4: FAQPage + Article Schema（複合型 - 最も推奨）

note.comの記事が、単に「ブログ記事」ではなく、「よくある質問に答えるコンテンツ」である場合、両方のスキーマを組み合わせることで、複数のAIプラットフォームに対応できます。

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Perplexity・Google AI Overviews引用パターン分析",
    "datePublished": "2025-01-10T00:00:00+09:00",
    "dateModified": "2025-01-10T15:30:00+09:00",
    "author": {
      "@type": "Person",
      "name": "山田太郎",
      "url": "https://note.com/@yamada_taro"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Perplexityに引用されるにはどうすればいいですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "..."
        }
      }
    ]
  }
]
</script>
```

**利点**:
- Perplexity: FAQページとして認識、Q&A構造を直接抽出
- Google AI Overviews: Article schemaとして認識、公開日・著者情報を参照
- ChatGPT: Article情報を参考にしながらコンテンツを引用

---

## 検証と測定

### 1. Google Rich Results Test

#### アクセス方法
https://search.google.com/test/rich-results

#### 検証手順
1. URLを入力（note.com記事のURL）
2. 「テストする」をクリック
3. 以下の情報を確認:
   - ✅ Passed: エラーなし
   - ⚠️ Valid AMP: 関連なし
   - ℹ️ Errors: 修正が必要
   - 対応する Rich Results タイプ（Article, FAQPage等）

#### 典型的なエラーと対処

| エラー | 原因 | 対処 |
|--------|------|------|
| `Missing field "xxx"` | 必須フィールドが不足 | 該当フィールドを追加 |
| `Invalid property name "xxx"` | プロパティ名にタイポ | 正しい Schema.org 仕様を確認 |
| `The value provided for "datePublished" is not a valid ISO 8601 date/time` | 日付形式が不正 | ISO 8601形式に統一（例: 2025-01-10T15:30:00+09:00） |

---

### 2. Google Search Console での確認

#### 方法1: 拡張データレポート（企業情報）

左メニュー → 「拡張」 → 「企業情報」
- Organization schema の検証結果を表示
- エラー・警告があれば表示

#### 方法2: 検査ツール

1. URL検査ツールで記事URLを入力
2. 「ウェブから取得」をクリック
3. 「リッチリザルトの可用性」セクションで確認
   - Article schema: ✅ Eligible
   - FAQPage schema: ✅ Eligible 等

#### 方法3: パフォーマンスレポート

左メニュー → 「パフォーマンス」
- フィルタ: 「AI Overviews」を選択可能（設定により）
- AI Overviews内での掲載数、CTR、平均掲載順位を確認

---

### 3. Schema.org 公式バリデーター

#### アクセス
https://validator.schema.org/

#### 使用方法
1. JSON-LDコードをコピー
2. テキストエリアに貼り付け
3. 「Validate」をクリック
4. エラーと警告を確認

---

### 4. 自動検証ツール（推奨）

#### Semrush AI Visibility Toolkit

**有料ツール（月額9,900円以上）**

機能:
- schema.org 準拠性の自動チェック
- 複数記事の一括検証
- 修正履歴の追跡
- 競合との schema 実装比較

#### Rank Math（WordPressプラグイン）

**note.com非対応**（自社サイトのみ）

参考情報:
- 無料版でSchema validation
- JSON-LD自動生成機能

---

## 注意事項と制約

### note.comの構造化データに関する制限

1. **メタタグ挿入不可**
   - `<meta name="description">` 等をカスタマイズできない
   - 自動生成される description に依存
   - 対応: Article schema の `description` フィールドで補完

2. **robots.txt編集不可**
   - AIクローラーの巡回制御不可
   - note.comの robots.txt に依存

3. **rel="canonical" 設定不可**
   - URLの正規化ができない
   - note.comの自動処理に依存

4. **OGP カスタマイズ限定的**
   - og:title, og:image は自動生成
   - アイキャッチ画像を設定することで部分的に対応

### 対応方法

**note.com側での自動認識に依存する場合が多い**

- 記事タイトル = og:title, headline
- アイキャッチ画像 = og:image
- 更新日 = dateModified（自動取得）

**note Pro版のHTMLコードブロックで追加情報を補完**

- 著者情報の詳細
- schema の完全性

---

## よくある質問

### Q1: note.comでもメタディスクリプション最適化は必要ですか？

**A**: 不要です。note.comは `<meta name="description">` をカスタマイズできないため、自動生成されたディスクリプションに依存します。代わりに、Article schema の `description` フィールドで、コンテンツの概要を記入することで、AI がコンテンツを理解しやすくなります。

---

### Q2: HTMLコードブロックに複数の schema を同時に入力できますか？

**A**: はい。JSON配列形式で複数のスキーマを同時に指定できます（例2参照）。ただし、スキーマ間の矛盾が生じないよう注意してください。例えば、Article と FAQPage は互いに補完関係にあり、同時使用が推奨されます。

---

### Q3: 構造化データを実装してからどのくらいで効果が出ますか？

**A**: 通常、Google Search Console に反映される（検索インデックス化される）には、数時間～3日かかります。AI Overviews への引用増加は、実装後2-6週間で観測可能になる場合が多いです。Perplexity は実時間検索のため、早期に反映される傾向があります。

---

### Q4: 古い記事に schema を追加しても効果はありますか？

**A**: はい。古い記事でも schema を追加することで効果が期待できます。加えて、記事の `dateModified` を更新することで、AI プラットフォームに「再度注目すべき記事」と認識させることができます（ただし、実質的な更新を行った場合のみ）。

---

### Q5: note.com以外のプラットフォーム（ブログ、Webサイト）での構造化データ実装は異なりますか？

**A**: 基本的な schema タイプと実装原則は同じです。しかし、以下の点で異なります:

| 項目 | note.com | ブログ/Webサイト |
|------|----------|------------------|
| 実装方法 | HTMLコードブロック（note Pro版） | head内への直接挿入 |
| メタタグ | カスタマイズ不可 | カスタマイズ可 |
| robots.txt | 編集不可 | 編集可能 |
| canonical | 設定不可 | 設定可能 |

自社Webサイトの場合、WordPress等の CMS で Yoast SEO や Rank Math 等のプラグインを使用すると、schema 実装が大幅に簡単になります。

---

### Q6: 構造化データ実装だけで AI citation を保証できますか？

**A**: いいえ。構造化データは必要条件の一つですが、十分条件ではありません。AI citation を獲得するには、以下の要素が同時に必要です:

1. **高品質コンテンツ**: 正確で最新の情報
2. **E-E-A-T信号**: 著者の認定資格、組織信頼性
3. **セマンティック完全性**: クエリへの包括的な回答
4. **マルチモーダル**: 画像、ビデオ、表
5. **新鮮性**: 定期的な更新

構造化データは、AIがこれらの要素を正確に認識するための「助言」役です。

---

### Q7: note.com記事の Person schema と Publisher schema の関係は？

**A**:
- **Person schema**: 著者（個人）の情報
- **Organization schema**: メディア（note.com）の情報

Article schema では、両方を指定することが推奨されます:

```json
{
  "author": {
    "@type": "Person",
    "name": "著者名",
    ...
  },
  "publisher": {
    "@type": "Organization",
    "name": "note",
    ...
  }
}
```

AIは、著者個人の専門性と、メディア（note.com）のブランド信頼性の両方を評価します。

---

### Q8: Google AI Overviews と ChatGPT で、求める schema は異なりますか？

**A**: 基本的には同じですが、優先度が異なります:

- **Google AI Overviews**: Schema.org 準拠（FAQPage、HowTo、Article が高優先度）
- **ChatGPT**: 構造化データをあまり重視しない（コンテンツの質が最優先）
- **Perplexity**: FAQPage schema を好む（Q&A構造の認識に有利）

3つのプラットフォーム全てに対応するには、**Article + FAQPage の複合型 schema** が推奨されます。

---

## チェックリスト

### 実装前の準備

- [ ] note Pro版に加入済み
- [ ] HTMLコード機能へのアクセス確認
- [ ] schema.org 公式ドキュメント確認
- [ ] Google Rich Results Test アカウント取得

### 実装中

- [ ] Article schema 実装（必須）
- [ ] Person schema 実装（著者情報）
- [ ] FAQPage schema 実装（Q&A記事の場合）
- [ ] HowTo schema 実装（ステップバイステップ記事の場合）
- [ ] 日付形式を ISO 8601 に統一（UTC+09:00）
- [ ] 画像URL、プロフィール画像URL を確認
- [ ] HTMLコードを note Pro版のコードブロックに挿入

### 実装後の検証

- [ ] Google Rich Results Test で検証（エラーなし）
- [ ] Schema.org 公式バリデーターで検証
- [ ] 24時間後、Google Search Console で確認
- [ ] 記事が Google インデックスされたか確認
- [ ] 2-6週間後、AI Overviews 内での引用を確認

### 継続的なメンテナンス

- [ ] 記事更新時に `dateModified` を自動更新
- [ ] 定期的（月1回）に schema エラーをチェック
- [ ] Google Search Console でパフォーマンス監視
- [ ] Semrush AI Visibility Index で追跡（有料版）

---

## 参考資料

### Google 公式ドキュメント
- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Mark Up FAQs with Structured Data](https://developers.google.com/search/docs/appearance/structured-data/faqpage)
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search)

### Schema.org 公式仕様
- [Article Schema](https://schema.org/Article)
- [FAQPage Schema](https://schema.org/FAQPage)
- [HowTo Schema](https://schema.org/HowTo)
- [Person Schema](https://schema.org/Person)

### 検証ツール
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [Google Search Console](https://search.google.com/search-console)

### 関連記事
- [Are FAQ Schemas Important for AI Search, GEO & AEO?](https://www.frase.io/blog/faq-schema-ai-search-geo-aeo/)
- [Structured Data for AI Search: A Practical Guide](https://blog.langsync.ai/structured-data-ai-search-schema-guide/)

---

**作成日**: 2026年1月10日
**対象**: note.com Pro版利用者、AEO実装者
**有効期限**: 2026年3月31日（以降更新推奨）
