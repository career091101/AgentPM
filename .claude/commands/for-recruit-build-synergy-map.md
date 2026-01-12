# for-recruit-build-synergy-map

新規事業と既存事業とのシナジー効果を可視化し、カニバリゼーション回避とクロスセル戦略を設計

## 使用方法

```bash
/for-recruit-build-synergy-map
```

## 説明

新規事業と既存事業とのシナジー効果を4象限マップで可視化し、6カテゴリ（既存顧客基盤、営業チャネル、ブランド力、技術インフラ、人的リソース、データ資産）で定量評価。カニバリゼーションを回避しながら、既存リソースを最大活用するクロスセル戦略を設計します。

### 主な機能

1. **4象限シナジーマップ**: カニバリゼーションリスク × シナジー効果で判定
2. **6カテゴリ評価**: 各10点満点（合計60点）でシナジー効果を定量化
3. **2方向クロスセル戦略**: 既存→新規、新規→既存の両方向で設計
4. **ROI定量化**: シナジー効果を金額換算してROI算出

### ForRecruit成功パターン

- **Airペイ**: シナジー52点、ROI 8,500%、クロスセル率57%
- **Geppo**: シナジー48点、ROI 4,100%、クロスセル率40%
- **統合事例（Airキャッシュ）**: カニバリ60% + シナジー45点 → Airペイ統合
- **撤退事例（CODE.SCORE）**: カニバリ60% + シナジー12点 → 撤退

## 前提条件

- `/validate-cannibalization` の事前実行（カニバリゼーションスコア取得）
- 既存事業リスト（リクルート、SUUMO、ホットペッパー、Air等）
- 既存顧客数、営業網規模等の基本データ

## 入力例

```yaml
project_name: "Airペイ"
new_business_description: "飲食店向けキャッシュレス決済サービス"
target_customer: "飲食店（個人店、チェーン店）"
value_proposition: "複数決済手段の一元管理、低コスト、簡単導入"
existing_businesses:
  - "ホットペッパーグルメ"
  - "Airレジ"
internal_resources:
  - "営業網（2,000名）"
  - "顧客基盤（30万店舗）"
  - "ブランド力（Air）"
  - "技術インフラ（決済基盤）"
  - "人的リソース（開発3名）"
  - "データ資産（決済データ10万件）"
```

## 出力例

```yaml
synergy_map:
  quadrant: "Quadrant 4: 理想的"
  cannibalization_score: 15
  synergy_score: 52
  recommendation: "クロスセル戦略構築"
  success_rate: 100
  expected_roi: 8500

  synergy_breakdown:
    existing_customer: 10点（クロスセル率57%、138.5億円）
    sales_channel: 10点（営業網2,000名、CAC 1/10）
    brand: 10点（Airブランド、広告費削減5億円）
    tech_infrastructure: 10点（開発コスト削減1.5億円）
    personnel: 7点（人件費削減900万円）
    data: 5点（与信審査優位性）

  total_synergy_value: 143.5億円
  roi: 8500%

  cross_sell_strategy:
    forward_cross_sell:
      direction: "Airレジ → Airペイ"
      expected_rate: "57%"
      expected_acquisition: "17.1万店舗"
    reverse_cross_sell:
      direction: "Airペイ → Airレジ"
      expected_rate: "30%"
      expected_acquisition: "1.5万店舗"
```

## 関連コマンド

- `/for-recruit-validate-cannibalization`: カニバリゼーション評価（前提）
- `/for-recruit-cross-reference-product-research`: 製品リサーチ参照
- `/for-recruit-run-cpf-simulation`: CPFシミュレーション
