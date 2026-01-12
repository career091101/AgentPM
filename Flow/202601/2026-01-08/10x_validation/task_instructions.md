# 競合調査タスク指示書

## 調査対象

### 競合A: 木内翔大（SHIFT AI）
- X: @SHIFTai_kiuchi
- コミュニティ: 2万人規模
- AIエージェント学習プログラム

### 競合B: 元木大介（Zoltraak）
- X: @dai_motoki
- コミュニティ: CursorConnect 1,900名、Zoltraak 6,000人
- Cursor/Zoltraak特化

### 競合C: 今井翔太（Genesis AI）
- X: @shouta_imai
- 研究者×実践者ハイブリッド
- マルチエージェント強化学習

## 収集すべき情報

### 1. 時間効率（習得時間短縮）
- 初心者→実装可能レベルまでの想定時間
- カリキュラム構成（週次/月次）
- 学習ペース（週何時間想定か）

### 2. コスト（学習コスト）
- 月額料金
- 初期費用
- 追加コスト（教材、ツール等）

### 3. 成果（実装スキル習得率）
- 卒業生の実績（公開事例）
- 実装成功率（％）
- 就職・転職実績

### 4. 使いやすさ（学習障壁）
- 前提知識要件（プログラミング経験、数学知識等）
- サポート体制（質問対応時間、メンター制度）
- コンテンツの分かりやすさ（初心者向け/中級者向け）

### 5. 導入障壁（参加ハードル）
- 選考有無
- 参加条件（スキル要件、年齢制限等）
- コミュニティ規模感（大規模/中規模/小規模）

## 出力形式

各競合について、以下の形式でJSON出力：

```json
{
  "competitor_name": "木内翔大（SHIFT AI）",
  "time_efficiency": {
    "learning_hours": 200,
    "weeks_to_implement": 12,
    "curriculum_structure": "週1回勉強会＋自習"
  },
  "cost": {
    "monthly_fee": 5000,
    "initial_fee": 0,
    "additional_cost": 0
  },
  "outcome": {
    "success_rate": 70,
    "case_studies": 15,
    "job_placement": true
  },
  "usability": {
    "prerequisite": "プログラミング基礎（Python推奨）",
    "support": "Discord 24h質問可、週1メンタリング",
    "target_level": "初心者〜中級者"
  },
  "entry_barrier": {
    "selection": false,
    "requirements": "なし",
    "community_size": "大規模（2万人）"
  }
}
```

## 調査方法

1. X（Twitter）プロフィール・固定ツイート確認
2. 公式サイト・note記事検索
3. コミュニティ参加者の口コミ（X検索）
4. 料金体系の公開情報
5. 実績・事例の公開データ

