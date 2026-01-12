---
description: ソロプレナー事例を参考にSNSマーケティング戦略を策定する
---
# ソロマーケティング戦略ワークフロー

Solo_SNSの成功者200名のデータを参照し、個人開発者向けのSNSマーケティング戦略を策定する。

## 概要

TikTok/Twitter/Instagram/LinkedIn別の成功パターンを分析し、再現可能なマーケティング戦略を生成する。

## 入力

| パラメータ | 必須 | 説明 |
|-----------|------|------|
| `product_category` | ○ | プロダクトカテゴリ |
| `target_platform` | - | `twitter` / `tiktok` / `instagram` / `linkedin` / `auto` |
| `budget` | - | 月間予算（0=無料のみ） |

## 出力

`{IDEA_FOLDER}/documents/4_executing/solo_marketing_strategy.md`

## 実行手順

### STEP 1: 類似事例検索
// turbo
```text
ツール: /reference_solo_cases category=marketing
処理:
  1. Solo_SNSから類似カテゴリの成功者を検索
  2. Tier1-2（収益＋SNSバズ実績あり）を優先抽出
  3. SNS活用タイプ別に分類
```

### STEP 2: プラットフォーム選定
// turbo
```text
処理:
  プロダクトカテゴリに基づいて最適なプラットフォームを推奨:
  
  | カテゴリ | 推奨プラットフォーム | 理由 |
  |---------|---------------------|------|
  | B2B SaaS | Twitter + LinkedIn | 開発者・ビジネス層がメイン |
  | B2C アプリ | TikTok + Instagram | 一般ユーザー層にリーチ |
  | 開発者ツール | Twitter | #buildinpublic コミュニティ |
  | 教育/コース | YouTube + Twitter | 信頼構築が重要 |
  | ニュースレター | Twitter + LinkedIn | 専門性アピール |
```

### STEP 3: 戦略生成
// turbo
```text
処理:
  選定プラットフォームに基づいて戦略を生成:
  
  【Twitter戦略】
  - Build in Public 投稿テンプレート
  - #buildinpublic #indiehacker タグ活用
  - 成功事例: @levelsio, @marc_louvion スタイル
  
  【TikTok戦略】
  - ショート動画トピック案
  - 投稿頻度・最適時間
  - 成功事例: Brock氏, Steven Cravotta スタイル
  
  【LinkedIn戦略】
  - 専門性コンテンツ
  - ストーリーテリング投稿
  - B2Bリード獲得
```

### STEP 4: コンテンツカレンダー生成
// turbo
```text
処理:
  30日間のコンテンツカレンダーを生成:
  
  Week 1: ローンチ準備
  - Day 1-3: ティーザー投稿
  - Day 4-5: 課題共有
  - Day 6-7: 解決策示唆
  
  Week 2: ローンチ
  - Day 8: Product Hunt投稿
  - Day 9-14: 反響共有、フィードバック対応
  
  Week 3-4: 継続的成長
  - 週2-3回の進捗共有
  - ユーザーの声引用
  - 機能アップデート告知
```

### STEP 5: レポート生成
// turbo
```text
ツール: write_to_file
出力: {IDEA_FOLDER}/documents/4_executing/solo_marketing_strategy.md

内容:
  # ソロマーケティング戦略
  
  ## 推奨プラットフォーム
  1. {primary_platform}（メイン）
  2. {secondary_platform}（サブ）
  
  ## 参照成功事例
  | 人物 | プラットフォーム | フォロワー | 手法 |
  |------|-----------------|-----------|------|
  | ... | ... | ... | ... |
  
  ## 戦略概要
  ### {primary_platform}戦略
  ...
  
  ## 30日コンテンツカレンダー
  ...
  
  ## KPI設定
  | 指標 | 1ヶ月目標 | 3ヶ月目標 |
  |------|----------|----------|
  | フォロワー | +500 | +3,000 |
  | エンゲージメント率 | 3% | 5% |
  | LP流入 | 100 | 1,000 |
```

---

## SNS成功者ベンチマーク（Solo_SNSより）

| タイプ | 人数 | 代表例 |
|--------|------|--------|
| Twitter型 | 62名 | Pieter Levels, Marc Lou, Arvid Kahl |
| TikTok型 | 18名 | Brock氏, Steven Cravotta |
| LinkedIn型 | 18名 | Justin Welsh, Sahil Bloom |
| マルチ型 | 46名 | Alex Hormozi, Tim Ferriss |

---

## 使用例

```
/plan_solo_marketing product_category="AI SaaS" target_platform=auto budget=0
```
