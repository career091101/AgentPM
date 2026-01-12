# Perplexity・Google AI Overviews引用パターン分析レポート

## 目次
1. [エグゼクティブサマリー](#エグゼクティブサマリー)
2. [Perplexity引用メカニズム](#perplexity引用メカニズム)
3. [Google AI Overviews引用メカニズム](#google-ai-overviews引用メカニズム)
4. [Perplexity特有の最適化戦略](#perplexity特有の最適化戦略)
5. [Google AI Overviews特有の最適化戦略](#google-ai-overviews特有の最適化戦略)
6. [3プラットフォーム比較分析](#3プラットフォーム比較分析)
7. [note.com制約下での実装戦略](#notecom制約下での実装戦略)
8. [参考情報](#参考情報)

---

## エグゼクティブサマリー

2025年時点で、AI検索エンジン（Perplexity、Google AI Overviews、ChatGPT）の引用パターンは従来のSEOと大きく異なります。本レポートは、これら3つのプラットフォーム間の違いを詳細に分析し、note.comというドメインパワー88.5の高権威性プラットフォーム上での最適化戦略を提示します。

### 主要な発見

**引用パターンの多様性**
- ChatGPT、Perplexity、Google AI Overviewsの間で、引用元の重複率は低い（12%程度）
- Perplexity⊕ChatGPT: 25.19%の重複、Google AIO⊕ChatGPT: 21.26%の重複
- 各プラットフォームは異なる情報源選定基準を持つため、プラットフォーム別の最適化が必須

**従来SEOからの転換**
- ドメインオーソリティ（DA）とAI引用率の相関は r=0.18（低い）
- AI Overviewsの47%の引用元は、従来検索で5位以下のページから引用
- リアルタイム性、専門性、構造化データが重要性を増加

**note.comの優位性**
- ドメインパワー88.5により、AI検索での引用可能性が大幅に向上
- セマンティックURL（5-7語）実装で11.4%の引用増加が確認
- note.com上の高品質コンテンツはChatGPTでも高い引用率を獲得

---

## Perplexity引用メカニズム

### 概要

Perplexityは、ウェブを実時間で検索し、その結果を直接ユーザーに提示する検索エンジン型のAI回答プラットフォームです。従来のGoogleやBingと異なり、限定的で高品質な情報源リストを優先します。

### 情報源選定基準

#### 1. **権威性と信頼性（Authority & Trust）**
Perplexityは、制度的な信頼を確立したドメインを優先します。
- **学術・公式ドメイン**: .edu、.gov ドメイン（技術的クエリで特に重視）
- **レガシーメディア**: Reuters、Bloomberg、New York Times等の従来型ニュース媒体
- **業界専門家**: 特定分野で認識されたオーソリティサイト

#### 2. **エンティティ密度（Entity Density）**
テキスト内に含まれる具体的な固有名詞や概念の密度がスコアリングの対象です。
- 人物名、地名、ブランド名、商品名、具体的な数値
- クエリに関連した高いエンティティ密度 = より高いスコア
- 含糊とした表現よりも、固有名詞で明確に述べられたコンテンツが優先

#### 3. **新鮮性（Freshness）**
実時間ウェブ検索を使用するため、更新タイムスタンプが極めて重要です。
- 可視的な更新日時が存在することが前提
- 進化するトピックでは、直近30日以内に更新されたコンテンツが優先
- Ahrefs 2025年調査: 定期更新するブランドは、未更新コンテンツと比較して最大30%高い引用率を獲得

#### 4. **Retrieval-Augmented Generation (RAG)プロセス**
Perplexityの技術的な処理フロー:
- ユーザー入力をクエリに分解
- 実時間インデックスをスイープ
- 関連性の高いコンテンツを抽出
- 複数の情報源から回答を組立
- クリック可能な引用として表示

### 引用の表示形式

#### インライン引用
回答本文中に番号付き参考文献として表示。[1]、[2]等のマーカーでユーザーが出典をたどることが可能。

#### 参考文献リスト
回答末尾に出典URLを一覧表示。タイトル、URL、簡潔な説明が含まれます。

### Perplexityが優先する情報源タイプ

**引用パターンの実例**
- Reddit: 6.6%（最上位の引用元）
- YouTube: 16.1%
- Wikipedia等の総合知識ベース
- フォーラムやコミュニティQ&Aサイト

Perplexityが重視するコンテンツ:
1. **包括的ガイド**: 深い掘り下げで、複数のサブトピックをカバー
2. **オリジナル研究**: ユニークなデータ、調査、分析
3. **最新更新**: 時間経過に伴う改訂・刷新
4. **比較記事**: 異なる選択肢を並べて評価
5. **専門家意見**: 認定資格を持つ著者による見解
6. **構造化ハウツー**: ステップバイステップで明確に構成

Perplexityが回避するコンテンツ:
- 薄いコンテンツ（100-200語）
- 販促を前面に出したセールストーク
- 古い情報（更新日時が不透明または著しく古い）

---

## Google AI Overviews引用メカニズム

### 概要

Google AI Overviewsは、従来のGoogle検索に統合されたAI生成サマリーです。従来のSEOシグナルとは異なる選定基準を使用し、E-E-A-Tフレームワークが最優先されます。

### 情報源の選定基準

#### 1. **E-E-A-T（Experience, Expertise, Authoritativeness, Trustworthiness）**

Google Search Quality Rater Guidelines（2025年版）で、E-E-A-Tが明示的に最優先フィルタになりました。

**Experience（経験）**
- 実際に製品を使用した体験
- リアルワールドでの実験結果
- ケーススタディやユースケース
- note.comのような信頼性の高いプラットフォーム上の実例報告

**Expertise（専門性）**
- 著者の認定資格・学位
- 業界での従事経験年数
- 公式な著者プロフィール・バイオグラフィ
- 専門教育背景

**Authoritativeness（権威性）**
- ドメインのセッター地位
- 業界での認識度（ブランド提及）
- バックリンク（ただしr=0.18と相関は低い）
- 他のオーソリティサイトからの参照

**Trustworthiness（信頼性）**
- セキュリティ証明書（HTTPS）
- プライバシーポリシー明記
- コンテンツの正確性検証可能性
- 著者情報の透明性

**96%のAI Overview引用が、高度なE-E-A-Tシグナルを持つ出典から選定されている**

#### 2. **セマンティック完全性（Semantic Completeness）**
r=0.87の相関を示す強力なシグナル
- スコア8.5/10以上のコンテンツは、それ以下の4.2倍の引用確率
- クエリに対する134-167語の自己完結した回答ユニット
- 質問すべてに対する包括的な回答を含む

#### 3. **マルチモーダルコンテンツ（Multi-Modal Content）**
r=0.92の相関 - 最も強力なシグナルの一つ
- テキスト + 画像 + ビデオ + 構造化データの組合せ
- 複合メディア組込サイトは156%高い選定率
- 動画説明に正確なタイムスタンプを含める
- 画像にALTテキストを含める

#### 4. **リアルタイム事実検証（Real-Time Fact Verification）**
r=0.89の相関
- 最新統計データを含む
- ピアレビュー済み研究への参照
- Tier-1引用（一次ソース）への参照 = 89%高い選定確率
- 主張の検証可能性

#### 5. **エンティティ密度**
15以上の認識されたエンティティを含むページ = 4.8倍の選定確率

### Google AI Overviewsで重視される構造化データ

#### FAQPage Schema
- 頻出する質問-回答構造
- 複数の質問を網羅
- 各回答が簡潔で完全

#### HowTo Schema
- ステップバイステップのプロセス
- 各ステップに対する明確な指示
- 画像・ビデオの埋込

#### Article Schema
- 公開日時
- 著者情報
- メディア（画像）
- 本文

#### Organization Schema
- 企業・組織の基本情報
- 連絡先
- ブランドロゴ
- メディアプロフィール

---

## Perplexity特有の最適化戦略

15個以上の実装可能な戦術を以下に列挙します。

### Tier 1: コンテンツ構造・形式

#### 1. **ヘッダー・箇条書き・番号リストの活用**
Perplexityのスキャニング・抽出が容易な形式を採用
- H2、H3見出しで明確なセクション区分
- 箇条書きで複数要素を列挙
- 番号付きリストでステップを明示

#### 2. **冒頭の回答優先戦略（Lead with Answer）**
最初の段落に直接的な回答を配置
- クエリへの明確な答えを冒頭50-100語で提示
- その後、詳細説明と根拠を述べる
- ユーザーが「スキップして要点だけ読む」場合も対応

#### 3. **Summary Boxesの実装**
重要な要点を強調する視覚的な要素
- 枠付きで重要情報を抽出
- 数値・事実を端的に示す
- スクリーンショットやテーブルで可視化

#### 4. **構造化FAQ セクション**
- 想定される一般的な質問を予め組込
- 各質問に対する簡潔な答え
- クエリに関連した真の問い合わせをカバー

### Tier 2: 専門性・権威性シグナル

#### 5. **著者プロフィール・認定資格の表示**
- 著者の名前、写真、バイオグラフィ
- 保有資格（修士号、博士号、業界認定）
- 経験年数、専門領域
- LinkedInプロフィールへのリンク

#### 6. **主張の根拠となるソース引用**
- コンテンツ内で第三者ソースを明示的に引用
- 査読済み学術論文、業界調査へのハイパーリンク
- 統計データの出典明記
- Tier-1情報源（一次ソース）を優先

#### 7. **Company Authority Signals**
- 会社設立年月日（設立経歴の長さ）
- チーム情報（主要メンバーの経歴、肩書き）
- 業界認定・賞受賞
- セキュリティ・プライバシーポリシー

#### 8. **レビューやテスティモニアルの組込**
- ユーザー評価、星の評価
- 実際の顧客コメント
- ケーススタディで実名ユーザーの成功事例
- 実証的な証拠となり得る

### Tier 3: リアルタイム性・更新戦略

#### 9. **明示的な更新日時タグ**
- 目視できる「最終更新: YYYY年MM月DD日」
- 記事の見出し直下、またはサイドバーに配置
- ISO 8601フォーマット（2025-01-10）で構造化

#### 10. **定期更新スケジュール**
- 2-3日ごとの軽微な更新（新データ・リンク追加など）
- 1-2週間ごとの実質的な改訂（新セクション追加、古い例置換）
- 更新履歴ログの公開（透明性向上）

#### 11. **時間依存コンテンツの管理**
- 季節性のあるトピック（「2026年の〇〇」）について、毎年更新
- イベント・トレンド関連記事の定期刷新
- 統計データを最新版に置換

### Tier 4: エンティティ・検索意図の最適化

#### 12. **Named Entity Optimization**
- クエリに関連した人物名、地名、ブランド名を多数含める
- 曖昧表現ではなく、固有名詞で明記
- Wiki等に記事がある著名人・組織を記述
- 略語は初出で正式名称を示す

#### 13. **比較・対比構造**
- 複数の選択肢を並べて比較
- 長所・短所をバランスよく説明
- 異なる視点から分析
- 「AとBを比較する」タイプのクエリに対応

#### 14. **オリジナルデータ・独自分析**
- 社内調査結果、アンケート回答データ
- 業界ベンチマーク分析（自社実施）
- ユニークな実験結果
- 他のメディアにはない独占情報

### Tier 5: テクニカル最適化

#### 15. **セマンティックURL構造**
- 5-7語の自然言語スラッグ（11.4%引用増）
- キーワードを含める（target intent反映）
- ランダム文字列や短縮形を避ける
- 階層的なURLパス構造

#### 16. **JSON-LD構造化データ（FAQ、HowTo）**
- FAQPage schema で質問-回答を明示
- HowTo schema でステップを構造化
- Person schema で著者情報を標記
- Organization schema で企業情報を明記

#### 17. **ページ読込速度・Core Web Vitals**
- Largest Contentful Paint (LCP) < 2.5秒
- First Input Delay (FID) < 100ms
- Cumulative Layout Shift (CLS) < 0.1
- Perplexityのクローラーが効率的にコンテンツを抽出

#### 18. **HTTPS、プライバシーポリシー、セキュリティ**
- SSL/TLSの実装
- プライバシーポリシーページの明示
- Cookie同意バナーの実装
- 信頼性シグナルの強化

---

## Google AI Overviews特有の最適化戦略

15個以上の実装可能な戦術を以下に列挙します。

### Tier 1: E-E-A-T信号の強化

#### 1. **著者認定資格の明示**
- 医療コンテンツ: 医師免許、看護師資格等
- 法務コンテンツ: 弁護士資格、司法試験合格
- 財務コンテンツ: FP資格、CFA等
- 著者詳細ページに資格番号、発行者を記載

#### 2. **執筆者の専門領域と経歴**
- 業界での従事年数（「15年の経験」など）
- 過去の著作・出版実績
- メディア出演、スピーキング実績
- LinkedIn、Twitter等での認知度

#### 3. **組織の信頼性シグナル**
- About Usページの詳細度
- チームメンバーのプロフィール
- 企業の歴史、ミッション・ビジョン
- サードパーティ認定（ISO、業界ライセンス）

#### 4. **Fact-Checkingと根拠表示**
- クレームに対する出典リンク（ハイパーリンク）
- 査読済み研究への参照
- 政府統計データ、業界調査の引用
- 反対意見も公平に提示（バランス）

### Tier 2: マルチモーダルコンテンツの充実

#### 5. **高品質画像の組込**
- 1200×630px以上の高解像度
- Descriptive Alt Text（画像説明）の記入
- 画像キャプション（文脈説明）
- 画像ファイル名にキーワード含有

#### 6. **ビデオコンテンツの最適化**
- 正確な動画の説明とタイトル
- 会話的なクエリ言語と一致させる
- 字幕・キャプション（聴覚障碍者対応）
- チャプター機能（タイムスタンプ）の活用
  - AI systemsはタイムスタンプを直接引用

#### 7. **テーブル・グラフ・インフォグラフィック**
- 複雑なデータをテーブルで可視化
- トレンドをグラフで表現
- 比較チャートで選択肢を対比
- 統計データを図解

#### 8. **トランスクリプト・キャプション**
- ポッドキャスト・動画の完全トランスクリプト提供
- 正確な字幕ファイル（SRT形式）
- タイムコード付きで重要箇所を表示
- テキスト検索可能にする

### Tier 3: 構造化データの実装

#### 9. **FAQPage Schema の正確な実装**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the best way to optimize for Google AI Overviews?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Focus on E-E-A-T signals, provide comprehensive answers, use multimodal content, and implement structured data properly."
      }
    }
  ]
}
```

#### 10. **HowTo Schema の詳細実装**
- 各ステップに対する明確な指示（itemListElement）
- Step毎に画像またはビデオを含める
- 予想実行時間（totalTime）を記載
- 難易度（difficulty）レベルを明示

#### 11. **Article Schema の完全実装**
- datePublished, dateModified（ISO 8601形式）
- author（Person schema）を完全に定義
- image（記事サムネイル）を含める
- articleBody はテキストコンテンツ本体

#### 12. **Organization Schema の充実**
- name, url（組織のホームページURL）
- logo（高解像度ロゴ）
- contact-point（連絡先情報）
- sameAs（SNS、Wikipedia等への外部リンク）

### Tier 4: コンテンツの充実・完全性

#### 13. **Comprehensive Coverage（網羅的カバレッジ）**
- クエリに関連する全側面をカバー
- サブトピックを体系的に扱う
- 異なる観点からの解説を含める
- より詳しい情報への内部リンク（関連記事）

#### 14. **実証的証拠・ケーススタディ**
- 実名の顧客事例（許可がある場合）
- Before/Afterの比較
- 数値化された結果（「売上が30%向上」など）
- 業界別・ユースケース別の活用例

#### 15. **バランスの取れた議論**
- 複数の観点を公平に扱う
- 反論も記載（その上で反駁）
- 長所と短所を両立
- 「状況によって異なる」という条件を明記

### Tier 5: テクニカル最適化

#### 16. **Semantic URL Structure（5-7語）**
`/how-to-optimize-for-google-ai-overviews-in-2025/`
のようなセマンティック構造で11.4%引用増加

#### 17. **Core Web Vitals の最適化**
- LCP (Largest Contentful Paint) < 2.5秒
- FID (First Input Delay) < 100ms
- CLS (Cumulative Layout Shift) < 0.1
- Google PageSpeed Insights で測定

#### 18. **Speakable Schema（音声検索対応）**
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

## 3プラットフォーム比較分析

### 引用パターンの違い

#### ChatGPT
- **最上位引用元**: Wikipedia (7.8%)、ニュースメディア
- **特徴**: 一般知識、歴史、広く認識された情報を優先
- **引用数**: 平均360語、多くの引用を含む
- **透明性**: 不安定（引用ソースが明記されない場合がある）
- **フォーカス**: 背景知識、コンテキスト提供

#### Perplexity
- **最上位引用元**: Reddit (6.6%)、YouTube (16.1%)
- **特徴**: 実時間検索、コミュニティ知見、ユースケース重視
- **引用数**: 少ない（3-5件程度が典型）
- **透明性**: 高い（すべての引用元がクリック可能）
- **フォーカス**: 最新情報、ユーザー体験、実践的アドバイス

#### Google AI Overviews
- **最上位引用元**: Reddit (2.2%), Quora, ユーザー生成コンテンツ
- **特徴**: ブランド提及率40%（高い）、E-E-A-T重視
- **引用数**: 中程度（5-8件）
- **透明性**: 非常に高い（Google SERPと統合）
- **フォーカス**: 権威的情報源、E-E-A-Tシグナル

### 引用元の重複率

```
ChatGPT ↔ Perplexity: 25.19%
ChatGPT ↔ Google AIO: 21.26%
Perplexity ↔ Google AIO: ?（推定15-20%）
全プラットフォーム重複: 12%
```

### プラットフォーム別の戦術優先順位

#### ChatGPT（優先度順）
1. Wikipedia への掲載（または高権威性メディア）
2. 広く認識された一般知識
3. 学術的信頼性（論文、研究機関）
4. ドメインオーソリティ（古いシグナルだが依然有効）

#### Perplexity（優先度順）
1. **リアルタイム性**: 最新の更新（2-3日ごと）
2. **エンティティ密度**: 具体的な固有名詞、数値
3. **実践性**: 実装可能なアドバイス、ハウツー
4. **コミュニティ信頼**: Reddit, Q&A等での議論

#### Google AI Overviews（優先度順）
1. **E-E-A-T信号**: 著者認定、組織信頼性
2. **マルチモーダル**: 画像、ビデオ、表、グラフ
3. **構造化データ**: Schema.org準拠
4. **ブランド言及**: 関連キーワード、ブランド検索

### 共通する成功パターン

1. **セマンティック完全性**: クエリへの包括的かつ自己完結した回答
2. **新鮮性**: 最新情報、定期更新
3. **専門性の証明**: 著者資格、エビデンス
4. **視覚化**: テーブル、グラフ、画像
5. **参照元の明示**: ハイパーリンク付き根拠提示

---

## note.com制約下での実装戦略

### note.com プラットフォームの特性

**メリット**
- ドメインパワー88.5（非常に高い権威性）
- ChatGPT、Perplexity、Google AI Overviewsすべてで引用対象
- ユーザー生成コンテンツプラットフォームとしての信頼性
- ソーシャルシグナル（スキ、シェア）の統合

**制約**
- 公式API: なし
- カスタムHTML: note Pro版のみ可能
- Schema.org実装: 限定的（head内への直接挿入不可）
- CSS/JavaScriptカスタマイズ: 不可
- ドメイン変更: 不可（note.com固定）

### note Pro版でのカスタムHTML実装方法

note Pro版では、記事内にHTML/CSS/JavaScriptを埋め込める「HTMLコード」機能を使用できます。

#### FAQPage Schema の埋込例

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "note.comでAEO対応するにはどうすればいいですか？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "E-E-A-T信号を強化し、セマンティックURL、マルチモーダルコンテンツ、定期更新を実装します。詳細は本記事をご参照ください。"
      }
    },
    {
      "@type": "Question",
      "name": "Perplexityに引用されるにはどうすればいいですか？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "著者認定資格、リアルタイム性（2-3日ごとの更新）、エンティティ密度を高めることが重要です。"
      }
    }
  ]
}
</script>
```

#### Article Schema の埋込例

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Perplexity・Google AI Overviews引用パターン分析",
  "datePublished": "2025-01-10",
  "dateModified": "2025-01-10",
  "author": {
    "@type": "Person",
    "name": "著者名",
    "url": "https://note.com/@著者ID",
    "description": "AI検索最適化（AEO）専門家、〇年の経験"
  },
  "publisher": {
    "@type": "Organization",
    "name": "note",
    "logo": {
      "@type": "ImageObject",
      "url": "https://assets.st-note.com/...(noteロゴ)"
    }
  },
  "description": "ChatGPT、Perplexity、Google AI Overviewsの引用パターンを包括的に分析し、note.com上での最適化戦略を提示します。"
}
</script>
```

#### Person/Byline Schema の実装

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "著者フルネーム",
  "url": "https://note.com/@著者ID",
  "image": "https://...著者画像URL",
  "description": "〇〇業界の専門家。□□資格保有。△△年間の実務経験。",
  "sameAs": [
    "https://twitter.com/...",
    "https://linkedin.com/...",
    "https://www.your-website.com"
  ]
}
</script>
```

### note.comでのセマンティック最適化

#### 1. **記事タイトルの最適化**
- 5-7語の自然言語表現を組込
- 例: 「Perplexity・Google AI Overviews引用パターン分析（7語）」
- クリック率（CTR）と引用率の両立

#### 2. **見出し構造の最適化**
```
# タイトル（H1：記事タイトル）
## セクション（H2：3-4個）
### サブセクション（H3）
#### 詳細項目（H4：必要に応じて）
```

#### 3. **マルチモーダルコンテンツの組込**
- note.comの画像アップロード機能を活用
- スクリーンショット、比較表、グラフ
- 埋込ツイート、YouTube動画
- 外部データビジュアライゼーション

#### 4. **定期更新の実装**
- note.comの「更新日時」機能を活用
- 最初の公開から2-3日以内に軽微な更新
- 新しいデータ・リンク追加
- 表現の洗練、誤字修正

#### 5. **著者プロフィールの充実**
- note.comプロフィール完成度を高める
- 自己紹介に資格・経歴を記載
- プロフィール画像の使用
- サポート（投銭）機能の有効化（信頼性シグナル）

### note.com上でのE-E-A-T強化

#### Experience
- 実体験に基づくケーススタディ
- 個人的な実装結果のレポート
- テスト結果・実験データの共有

#### Expertise
- 著者のバックグラウンド明記
- 関連資格・認定の表示
- 以前の出版実績・メディア掲載

#### Authoritativeness
- note.comのプロフィール充実
- フォロワー数・サポーター数の増加（オーガニック）
- 他のオーソリティメディアでの言及

#### Trustworthiness
- コンテンツの正確性：出典明記
- 反対意見も公平に扱う
- 更新日時を明示

---

## 測定とトラッキング

### Perplexity引用のトラッキング方法

**公式ツール: なし**

**代替手段:**

1. **手動モニタリング**
   - 関連クエリを定期的に Perplexity で検索
   - あなたの記事が引用されているかチェック
   - 引用パターン（何番目に出現するか）を記録
   - 頻度: 週1-2回

2. **アナリティクス監視**
   - Google Analytics で `perplexity.ai` からのトラフィック追跡
   - Perplexityはreferer情報を送信する場合が多い
   - 直接トラフィック増加も追跡対象（可能性あり）

3. **AEO特化ツール（有料）**
   - Semrush AI Visibility Toolkit（有料）
   - 特定プロンプトのPerplexity引用率を自動トラッキング
   - 競合との比較分析

### Google AI Overviews表示率の測定

**公式ツール: Google Search Console**

1. **Google Search Console での確認**
   - 左メニュー: 「パフォーマンス」
   - フィルタ: AI Overviews（設定可能）
   - 指標: インプレッション数、CTR、平均掲載順位
   - 更新遅延: 2-3日後に反映

2. **AI Visibility Index（Semrush提供）**
   - Semrush One有料プラン
   - Google AI Overviews、ChatGPT、Perplexity の総合指標
   - 競合ベンチマーク
   - トレンド分析

3. **Rich Results Test**
   - Google Search Central
   - https://search.google.com/test/rich-results
   - URL または HTML コード検証
   - Schema markupエラー検出

### 各プラットフォームのKPI設定

#### ChatGPT
- **指標**: 言及頻度（月間）、ブランド認知度上昇
- **測定方法**: 手動、ChatGPT Enterpriseダッシュボード（有料）
- **目標**: 月間100+言及

#### Perplexity
- **指標**: 月間引用回数、引用元ポジション（1番目/2番目等）
- **測定方法**: 手動、Google Analytics、AEO専門ツール
- **目標**: 月間50+引用、トップ3表示率 > 60%

#### Google AI Overviews
- **指標**: AI Overviews内インプレッション、CTR、引用率
- **測定方法**: Google Search Console、Semrush
- **目標**: 月間1000+インプレッション、CTR > 5%

### A/Bテスト設計

#### テスト周期: 30日サイクル

**Week 1: ベースライン測定**
- 全プラットフォームで現状の引用数・表示率を記録
- 競合ベンチマーク取得

**Week 2-3: 施策実装**
- 戦術A（例: SEマンティックURL + FAQPage Schema）を実装
- または戦術B（例: 定期更新 + 著者認定）を実装
- コントロール記事は変更なし

**Week 4: 成果測定**
- 引用数、表示率、CTRの変化を記録
- 競合との相対的地位を比較
- 統計的有意性を評価（可能であれば）

**例: URL構造テスト**
```
戦術A（セマンティックURL）:
  /perplexity-ai-optimization-guide-2025/
  期待値: 11.4% 引用増

戦術B（非セマンティックURL）:
  /content-123/
  期待値: ベースライン

結果測定: Week 4 実施後
```

---

## まとめ

### 優先施策（note.com制約下で実装可能）

**即座に実装（1-2週間内）**
1. note Pro版でのFAQPage/Article Schema実装
2. セマンティックタイトル最適化（5-7語）
3. 著者プロフィール充実（資格、経歴）
4. マルチモーダルコンテンツ（画像、表）追加

**短期（1ヶ月内）**
5. 定期更新スケジュール実装（2-3日ごと）
6. エンティティ密度最適化（固有名詞、数値増加）
7. Google Search Console でAI Overviews表示率を監視開始
8. 手動Perplexityモニタリング開始

**中期（1-3ヶ月）**
9. AEO専門ツール（Semrush）による自動トラッキング開始
10. ケーススタディ・オリジナルデータの蓄積
11. ユーザーレビュー・テスティモニアル機能の活用
12. クロスプラットフォーム連携（TwitterやLinkedIn）

### 成功の指標

- Perplexity引用: 月間30+（初期目標）→ 100+（6ヶ月目標）
- Google AI Overviews: 月間500+インプレッション、CTR 5-10%
- ChatGPT: 言及認知度の向上（定性的評価）

---

## 参考情報

本レポートは以下の情報源に基づいています:

- Semrush AI Overviews Study: What 2025 SEO Data Tells Us About Google's Search Shift: https://www.semrush.com/blog/semrush-ai-overviews-study/
- Get Cited by Perplexity.ai: A Step-by-Step Guide for 2025: https://eseospace.com/blog/perplexity-ai-cite-website/
- How to Get Cited in Google AI Overviews - Digital Blacksmiths: https://digitalblacksmiths.io/how-to-get-cited-in-google-ai-overviews/
- Perplexity AI Optimization: How to Get Cited & Rank (2025): https://outboundsalespro.com/perplexity-ai-optimization/
- How to Optimize for Google AI Overviews in 2025: https://www.dataslayer.ai/blog/how-to-optimize-for-google-ai-overviews-in-2025
- Answer Engine Optimization (AEO): Your Complete Guide to AI Search Visibility: https://www.amsive.com/insights/seo/answer-engine-optimization-aeo-evolving-your-seo-strategy-in-the-age-of-ai-search/
- The 2026 AEO / GEO Benchmarks Report: https://www.conductor.com/academy/aeo-geo-benchmarks-report/
- How to Structure Content for AI Retrieval: https://seattleorganicseo.com/how-to-structure-content-for-ai-retrieval-chunks-citations-context/
- How Perplexity Selects Sources - OptimizeYour.Blog: https://optimizeyour.blog/learn/platforms/how-perplexity-selects-sources
- Google Search Quality Rater Guidelines (2025): https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search

---

**作成日**: 2026年1月10日
**対象**: note.com コンテンツ制作者、AEO最適化実装者
**有効期限**: 2026年3月31日（以降更新推奨）
