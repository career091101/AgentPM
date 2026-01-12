# Multi-Domain Advisor Command

**コマンド**: `/multi-domain-advisor`

**説明**: ドメイン横断戦略アドバイス・シナジー分析

**エージェント**: Multi-Domain Advisor Agent

---

## 使用方法

```
/multi-domain-advisor
```

または

```
ドメイン横断戦略を提案してください
ハイブリッド戦略を立ててください
```

---

## 実行内容

1. **ドメイン分析**: 各ドメインの強み・弱みを抽出
2. **シナジー分析**: ドメイン間の相乗効果を定量・定性的に評価
3. **ハイブリッド戦略立案**: 複数ドメインの強みを組み合わせた最適戦略を提案
4. **適応的評価基準設定**: 複数ドメインの基準を統合した独自基準を生成
5. **クロスドメインベストプラクティス**: 各ドメインの成功パターンを統合
6. **レポート生成**: hybrid_strategy.md、synergy_analysis.json、cross_domain_best_practices.md、adapted_criteria.json

---

## 入力パラメータ

1. **対象ドメイン**（必須）: 2-4個選択
   - `for_genai`: 生成AI特化版
   - `for_recruit`: 企業内新規事業特化版
   - `for_solo`: ソロプレナー特化版
   - `for_startup`: スタートアップ特化版
2. **プロジェクト概要**（必須）: 200-500文字
3. **現在の課題**（オプション）: 複数選択可
4. **アドバイスモード**（オプション）: quick / standard / deep（デフォルト: standard）
5. **既存検証結果**（オプション）: CPF/PSF/PMF等のスコア

---

## 実行例

### 例1: ForGenAI × ForSolo（AI SaaSをソロで立ち上げ）

```
ユーザー: /multi-domain-advisor

エージェント: 対象ドメインを選択してください（2-4個）
ユーザー: for_genai, for_solo

エージェント: プロジェクト概要を教えてください（200-500文字）
ユーザー: AIチャットボットSaaSをソロで立ち上げ、将来的にVC調達を目指す。現在Discovery完了、CPF検証中。ターゲットはスタートアップのカスタマーサポート担当者。

エージェント: 現在の課題はありますか？（複数選択可、スキップ可）
ユーザー: 1人での実装が困難、VC基準を満たせるか不安

エージェント: アドバイスモードを選択してください
ユーザー: standard

エージェント: ハイブリッド戦略を立案中...

[30分後]

エージェント: ✅ ハイブリッド戦略の提案が完了しました

**シナジースコア**: 1.65（強いシナジー）

**ハイブリッド戦略（3フェーズ）**:

### フェーズ1: Discovery & CPF（1-2ヶ月）
- ForGenAI: AI技術スタック選定（Claude 3.5 Sonnet推奨）
- ForSolo: ShipFastボイラープレート導入
- 統合戦略: ShipFastにLangChain統合、AIチャットボットPoC 2週間で構築

### フェーズ2: PSF & 初期トラクション（2-3ヶ月）
- ForGenAI: Product Hunt #1獲得戦略（Hunter確保、事前コミュニティ参加）
- ForSolo: Build in Publicで週次進捗共有、X/Twitterフォロワー1,000人獲得
- 統合戦略: Product Hunt #1 + Build in Public → 初期ユーザー500-1000獲得

### フェーズ3: PMF & スケール準備（3-6ヶ月）
- ForGenAI: プロンプト最適化、モデル更新対応フロー構築
- ForSolo: $1K MRR → $5K MRR達成、コスト最適化（月次$100以下）
- 統合戦略: ユニットエコノミクス検証（LTV/CAC 5.0以上）、VC調達準備完了

**期待される成果**:
- 3ヶ月: Product Hunt #1、初期ユーザー500人、$1K MRR
- 6ヶ月: $5K MRR、LTV/CAC 5.0以上、VC調達準備完了

**適応的評価基準**:
- CPFスコア: 60点（ForStartup: 70点、ForSolo: 50点の中間）
- 市場機会: 5.2点（厳格だがソロ実行可能）
- 実行可能性: 6点（1人実行可能性を重視）

**クロスドメインベストプラクティス**:
1. ShipFast × LangChain統合で開発速度10倍
2. Build in Public × Product Hunt でトラクション証明
3. ユニットエコノミクス検証でVC調達準備

詳細レポート:
- Flow/202601/2026-01-03/multi_domain_advisor/hybrid_strategy.md
- Flow/202601/2026-01-03/multi_domain_advisor/synergy_analysis.json
- Flow/202601/2026-01-03/multi_domain_advisor/cross_domain_best_practices.md
- Flow/202601/2026-01-03/multi_domain_advisor/adapted_criteria.json
```

---

### 例2: ForRecruit × ForGenAI（企業内でAI新規事業）

```
ユーザー: 企業内でAI新規事業を立ち上げたいのでハイブリッド戦略を提案してください

エージェント: 対象ドメインを選択してください（2-4個）
ユーザー: for_recruit, for_genai

エージェント: プロジェクト概要を教えてください
ユーザー: 既存BtoBサービスにAIレコメンデーション機能を追加し、新規事業化。Ring 1-2を目指す。ターゲットは既存顧客基盤1,000社。

エージェント: 現在の課題はありますか？
ユーザー: 社内承認プロセスが不明、AI倫理リスクの評価方法がわからない

エージェント: アドバイスモードを選択してください
ユーザー: deep

エージェント: ハイブリッド戦略を立案中...

[60分後]

エージェント: ✅ ハイブリッド戦略の提案が完了しました

**シナジースコア**: 1.55（強いシナジー）

**ハイブリッド戦略（4フェーズ）**:

### フェーズ1: Discovery & 社内承認準備（1ヶ月）
- ForRecruit: 既存リソース棚卸し（顧客基盤、営業網、技術スタック）
- ForGenAI: AI技術スタック選定、倫理評価フレームワーク構築
- 統合戦略: 既存顧客50社にインタビュー、AIレコメンデーションニーズ検証

### フェーズ2: Ring 1達成（2-3ヶ月）
- ForRecruit: 社内承認デッキ作成、ステークホルダーマップ整備
- ForGenAI: AI PoC構築、プロンプト品質評価
- 統合戦略: 既存顧客5社でPoC実施 → 満足度80%以上 → Ring 1達成

### フェーズ3: Ring 2達成（3-6ヶ月）
- ForRecruit: 本格開発承認獲得、社内リソース配分
- ForGenAI: プロンプトライブラリ構築、モデル更新対応フロー
- 統合戦略: 既存顧客100社に展開 → 満足度75%以上 → Ring 2達成

### フェーズ4: 新規事業化（6-12ヶ月）
- ForRecruit: 新規事業部立ち上げ、外部顧客開拓
- ForGenAI: AI倫理検証、バイアス対策
- 統合戦略: 外部顧客50社獲得 → ARR $500K達成 → 新規事業化

**期待される成果**:
- 3ヶ月: Ring 1達成、PoC満足度80%以上
- 6ヶ月: Ring 2達成、既存顧客100社展開
- 12ヶ月: 新規事業化、ARR $500K

**適応的評価基準**:
- CPFスコア: 50点（社内PoC前提でForRecruit基準を採用）
- Ring制度準拠: Ring 1 → Ring 2 → 新規事業化
- AI倫理評価: ForGenAI基準で厳格に実施

**課題への対処**:
1. **社内承認プロセス**: ステークホルダーマップ作成 → 事前根回し → 承認デッキ提示
2. **AI倫理リスク**: ForGenAI倫理評価フレームワーク適用、バイアステスト実施

詳細レポート:
- Flow/202601/2026-01-03/multi_domain_advisor/hybrid_strategy.md
- Flow/202601/2026-01-03/multi_domain_advisor/synergy_analysis.json
- Flow/202601/2026-01-03/multi_domain_advisor/cross_domain_best_practices.md
```

---

### 例3: ForStartup × ForSolo（スタートアップ品質をソロで実現）

```
ユーザー: VC調達を見据えてソロで立ち上げたい。ハイブリッド戦略を提案して

エージェント: 対象ドメインを選択してください
ユーザー: for_startup, for_solo

エージェント: プロジェクト概要を教えてください
ユーザー: フィットネスアプリをソロで立ち上げ、トラクション証明後にVC調達。ターゲットはジム通い初心者。

エージェント: 現在の課題はありますか？
ユーザー: VC基準の厳格な検証をソロで実行できるか不安

エージェント: アドバイスモードを選択してください
ユーザー: [Enter]（デフォルト: standard）

エージェント: ハイブリッド戦略を立案中...

[30分後]

エージェント: ✅ ハイブリッド戦略の提案が完了しました

**シナジースコア**: 1.70（非常に強いシナジー）

**ハイブリッド戦略（3フェーズ）**:

### フェーズ1: 厳格なPMF検証（3-6ヶ月）
- ForStartup: VC基準のPMF検証（リテンション40%以上、NPS 50以上）
- ForSolo: 1人実装可能性重視、ShipFast活用
- 統合戦略: 厳格な検証で市場確信 → ソロで高速実装 → 品質担保

### フェーズ2: トラクション証明（6-12ヶ月）
- ForStartup: ピッチデッキ作成、週次成長率20%以上
- ForSolo: Build in Publicで透明性の高い進捗共有
- 統合戦略: X/Twitterフォロワー5,000人 + 週次成長率20% → トラクション証明

### フェーズ3: VC調達準備（12-18ヶ月）
- ForStartup: ユニットエコノミクス検証（LTV/CAC 5.0以上）
- ForSolo: $10K MRR達成、コスト最適化
- 統合戦略: ユニットエコノミクス証明 + トラクション → VC調達成功

**期待される成果**:
- 6ヶ月: PMF達成、リテンション40%以上
- 12ヶ月: $10K MRR、週次成長率20%
- 18ヶ月: VC調達成功（$1-2M Seed Round）

**適応的評価基準**:
- CPFスコア: 65点（ForStartup: 70点、ForSolo: 50点の間、厳格だがソロ実行可能）
- PMF基準: リテンション40%以上（ForStartup基準）
- 成長率: 週次20%以上（ForStartup基準）

**クロスドメインベストプラクティス**:
1. 厳格なPMF検証で市場確信 → VC投資判断材料
2. Build in Publicでトラクション可視化 → ピッチデッキに活用
3. ユニットエコノミクス証明 → VC調達成功率向上

詳細レポート:
- Flow/202601/2026-01-03/multi_domain_advisor/hybrid_strategy.md
- Flow/202601/2026-01-03/multi_domain_advisor/synergy_analysis.json
```

---

## 成功指標

| 指標 | 目標値 |
|------|--------|
| ハイブリッド戦略採用率 | > 70% |
| シナジースコア妥当性 | > 80% |
| 適応的基準精度 | > 85% |
| レポート生成時間 | < 60分 |

---

## 参照

- **エージェント仕様**: `@.claude/agents/multi-domain-advisor-agent.md`
- **Research Index Agent**: `@.claude/agents/research-index-agent.md`
- **Review Agent**: `@.claude/agents/review-agent.md`

---

**作成日**: 2026-01-03
**Week 7-9実装**: Multi-Domain Advisor Agent（P2）
