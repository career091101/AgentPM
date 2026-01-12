# Perplexity・Google AI Overviews引用パターン分析 - Week 1 成果物

**実施日**: 2026年1月10日
**プロジェクト**: note.com SEO/AEO最適化戦略（2026年）
**フェーズ**: Week 1 - 研究・分析

---

## 成果物一覧

### 1. `perplexity_google_aio_citation_patterns.md` （30.8KB）

**内容**: Perplexity・Google AI Overviews・ChatGPT引用パターン包括分析

#### 主要セクション

**Perplexity引用メカニズム**
- 情報源選定基準（権威性、エンティティ密度、新鮮性）
- Perplexity特有の18個の最適化戦術
- Tier 1-5に分類した実装可能な戦術

**Google AI Overviews引用メカニズム**
- E-E-A-Tフレームワーク（Experience, Expertise, Authoritativeness, Trustworthiness）
- セマンティック完全性、マルチモーダルコンテンツ、構造化データの役割
- Google AI Overviews特有の18個の最適化戦術

**3プラットフォーム比較分析**
- ChatGPT vs Perplexity vs Google AI Overviewsの引用パターン比較
- 引用元の重複率分析（12%の全プラットフォーム重複）
- プラットフォーム別の戦術優先順位

**note.com制約下での実装戦略**
- note.com の特性（DA 88.5）と制限事項
- note Pro版でのカスタムHTML実装方法
- セマンティックURL、著者プロフィール最適化
- E-E-A-T信号強化戦略

**測定とトラッキング**
- Perplexity引用トラッキング方法（手動、Analytics、AEO専門ツール）
- Google AI Overviews表示率測定（Google Search Console）
- KPI設定と30日A/Bテストサイクル

#### 成功基準達成状況

- ✅ Perplexity引用戦術: **18個** （目標: 15個以上）
- ✅ Google AI Overviews引用戦術: **18個** （目標: 15個以上）
- ✅ 3プラットフォーム比較分析: **完全実装**
- ✅ note.com制約評価: **明確に記載**
- ✅ 測定方法: **具体的に記載**

---

### 2. `structured_data_strategy.md` （27KB）

**内容**: Schema.org / JSON-LD実装戦略ガイド

#### 主要セクション

**構造化データの重要性**
- 従来SEOでの役割との違い
- AI検索エンジン時代での新しい役割
- Google AI Overviewsにおける相関性（r値）

**AIプラットフォームごとの構造化データ活用**
- ChatGPT: 最小限の利用
- Perplexity: 中程度の優先度（FAQスキーマ重視）
- Google AI Overviews: 非常に高い優先度（必須に近い）

**推奨スキーマタイプ（9種類）**

| Tier | スキーマ | 優先度 | 実装容易性 |
|------|---------|--------|----------|
| 1 | Article | ⭐⭐⭐⭐⭐ | ◎ 簡単 |
| 2 | FAQPage | ⭐⭐⭐⭐⭐ | ◎ 簡単 |
| 2 | HowTo | ⭐⭐⭐⭐ | ◎ 簡単 |
| 3 | Person（著者） | ⭐⭐⭐⭐ | ◎ 簡単 |
| 3 | Organization | ⭐⭐⭐ | ◎ 簡単 |
| 3 | BreadcrumbList | ⭐⭐ | ◎ 簡単 |
| 4 | NewsArticle | ⭐⭐ | △ 中程度 |
| 4 | Speakable | ⭐⭐ | △ 中程度 |
| 4 | Review/AggregateRating | ⭐⭐ | △ 中程度 |

**note.com制約下での実装方法**
- note Pro版の HTMLコードブロック機能を使用
- JSON-LD形式での実装（プレーンテキスト）
- 記事冒頭への配置（AIクローラー効率化）

**実装例（4種類以上）**

1. **Article + Person Schema** - 基本形
2. **Article + FAQPage Schema** - Q&A記事
3. **HowTo Schema** - ステップバイステップガイド
4. **複合型（Article + FAQPage）** - 最も推奨

**検証と測定**
- Google Rich Results Test
- Google Search Console での確認
- Schema.org 公式バリデーター
- Semrush AI Visibility Toolkit（有料）

**よくある質問（8個）**
- メタディスクリプション最適化の必要性
- 複数スキーマの同時使用
- 効果が出るまでの期間
- 古い記事へのスキーマ追加効果
- プラットフォーム別の違い
- 構造化データだけでの保証可能性
- スキーマ間の関係性
- Google AI Overviews vs ChatGPT の求める schema

#### 成功基準達成状況

- ✅ 構造化データ実装例: **4種類以上** （目標: 3種類以上）
- ✅ note.com制約下での実装可能性: **明確に評価**
- ✅ 検証方法: **具体的に記載**
- ✅ よくある質問: **8個の詳細回答**

---

## 成果物の活用方法

### ドキュメント1: 引用パターン分析レポート

**対象読者**:
- note.com コンテンツ制作者
- AEO戦略を検討する経営層
- SEO/AEOコンサルタント

**活用シーン**:
1. **コンテンツ制作の指針**: Perplexity・Google AI Overviews・ChatGPT各プラットフォームへの最適化戦術を確認しながら記事作成
2. **KPI設定**: 月間Perplexity引用数（目標30+→100+）、Google AI Overviews月間インプレッション（目標1000+）等の目標設定
3. **優先施策決定**: 即座（1-2週間）、短期（1ヶ月）、中期（3ヶ月）の優先順位付け
4. **競合分析**: 他のnote.com執筆者との差別化要素の特定

### ドキュメント2: 構造化データ実装戦略ガイド

**対象読者**:
- note Pro版利用者
- テクニカルSEOに興味がある執筆者
- 自社Webサイト運営者（参考）

**活用シーン**:
1. **実装準備**: note Pro版加入、HTMLコード機能の確認
2. **スキーマ選択**: 記事タイプ別のスキーマ推奨（Article必須、FAQPage/HowToは記事内容で判定）
3. **コード実装**: 実装例をコピー・ペーストし、記事情報を置き換え
4. **検証**: Google Rich Results Test、Schema.org Validatorで動作確認

---

## Week 1 実行内容サマリー

### リサーチ活動

**実施日時**: 2026年1月10日
**リサーチ方法**: WebSearch（複数キーワードで並列実行）

**検索クエリ**（計9回）:
1. Perplexity citation mechanism 2025 how sources selected
2. Google AI Overviews citation selection criteria E-E-A-T 2025
3. AEO optimization strategy Perplexity Google AI Overviews 2025
4. structured data FAQ schema HowTo schema AI search results
5. note.com domain authority AI search visibility 2025
6. Perplexity optimization content structure expertise author credentials 2025
7. "semantic URL structure" AI search citation optimization 5-7 words
8. Google AI Overviews schema.org JSON-LD implementation guide 2025
9. ChatGPT Perplexity Google AI Overviews citation comparison analysis 2025
10. AI search visibility tracking measurement tools Semrush 2025

**情報源**（主要）:
- Semrush AI Overviews Study
- Google Search Central Blog
- Schema.org 公式ドキュメント
- Conductor 2026 AEO/GEO Benchmarks Report
- 各種SEO/AEO最適化ガイド（30+記事）

### 分析実施内容

**定量分析**:
- 3プラットフォーム間の引用元重複率: 12%（全プラットフォーム）
- Perplexity最上位引用元: Reddit 6.6%
- Google AI Overviewsの47%引用は従来検索5位以下から
- セマンティックURL（5-7語）による引用増加: 11.4%
- マルチモーダルコンテンツ（r=0.92）: 156%高い選定率

**定性分析**:
- E-E-A-Tの重要性（96%のAI Overview引用が高E-E-A-Tシグナルから選定）
- プラットフォーム別戦術優先度の違い
- note.com制約（メタタグ編集不可、カスタムHTML Pro版のみ等）
- セマンティック完全性とマルチモーダルコンテンツの相乗効果

### ドキュメント生成

**ファイル1**: `perplexity_google_aio_citation_patterns.md`
- 文字数: 30,841文字
- セクション数: 8
- 戦術数: Perplexity 18個 + Google AI Overviews 18個 = 36個

**ファイル2**: `structured_data_strategy.md`
- 文字数: 27,100文字
- セクション数: 7
- スキーマ種類: 9種類（Tier 1-4）
- 実装例: 4種類（複合型含む）

---

## 次フェーズ（Week 2-4）への推奨タスク

### Week 2: 初期実装テスト

- [ ] note Pro版加入（月額1,100円）
- [ ] セマンティックタイトル最適化（既存記事3-5件）
- [ ] Article + FAQPage Schema実装（テスト記事1件）
- [ ] Google Rich Results Test で検証
- [ ] Google Search Console 設定確認

### Week 3: 定期更新・author profile強化

- [ ] 著者プロフィール完成度向上（資格、経歴明記）
- [ ] 定期更新スケジュール実装（2-3日ごと）
- [ ] マルチモーダルコンテンツ追加（既存記事3件）
- [ ] Perplexity手動モニタリング開始（週1-2回）

### Week 4: トラッキング開始・効果測定

- [ ] Google Analytics で Perplexity referrer 設定
- [ ] Google Search Console での AI Overviews 表示確認
- [ ] ChatGPT引用手動テスト（3-5プロンプト）
- [ ] 4週間後の効果測定（引用数、表示率等）

---

## 成功の指標（目標値）

### 短期（1ヶ月）
- Perplexity: 月間30+引用、トップ3表示率 > 60%
- Google AI Overviews: 月間500+インプレッション、CTR 3-5%

### 中期（3ヶ月）
- Perplexity: 月間100+引用、トップ3表示率 > 80%
- Google AI Overviews: 月間2000+インプレッション、CTR 5-8%
- ChatGPT: 月間20+言及

### 長期（6ヶ月）
- 3プラットフォーム合計トラフィック: 月間3000+セッション
- ブランド認知度（Google検索ボリューム）: 5倍向上
- note.com フォロワー数: 月間平均+30%

---

## ドキュメントの信頼性

### 情報源の質

- ✅ Google公式ドキュメント（Search Central、Developers）
- ✅ Schema.org公式仕様
- ✅ 2025-2026年の最新研究（Conductor、Semrush、Ahrefs等）
- ✅ 学術的相関分析（r値等の統計指標）

### 検証プロセス

- ✅ 複数のWebSearch結果を相互検証
- ✅ 矛盾する情報がないか確認
- ✅ 数値データの出典を明記
- ✅ note.com制約については公式機能から検証

### 更新スケジュール

- **有効期限**: 2026年3月31日
- **推奨更新周期**: 月1回（AIプラットフォームのアルゴリズム更新追跡）
- **緊急更新**: Google公式ガイドライン更新時

---

## 付録: ファイル構成図

```
note_seo_aeo_2026/
├── research/
│   └── week1/
│       ├── README.md （このファイル）
│       ├── perplexity_google_aio_citation_patterns.md （30.8KB）
│       ├── structured_data_strategy.md （27KB）
│       ├── aeo_geo_trends_2025_2026.md （既存）
│       ├── note_platform_analysis.md （既存）
│       ├── note_technical_constraints.md （既存）
│       ├── competitor_analysis.csv （既存）
```

---

## 今後の改善提案

1. **プラットフォーム別ケーススタディ**: 実際のnote.com記事でこれらの戦術を検証
2. **自動化ツール開発**: Perplexity引用トラッキング自動化スクリプト
3. **競合ベンチマーク**: note.com上の競合執筆者との引用率比較
4. **動的コンテンツ最適化**: ChatGPT、Perplexity、Google AIで異なる回答を獲得するコンテンツ設計
5. **音声検索最適化**: Speakable Schema実装と Google Assistant 対応

---

**作成者**: Claude Code（Anthropic）
**作成日**: 2026年1月10日
**形式**: Markdown
**対応プラットフォーム**: note.com Pro版, WordPress, Webflow, その他CMS

