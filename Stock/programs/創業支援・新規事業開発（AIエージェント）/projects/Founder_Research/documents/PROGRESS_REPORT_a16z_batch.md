# Andreessen Horowitz (a16z) Portfolio - ケーススタディ作成進捗レポート

**作成日**: 2025-12-28
**対象**: a16zポートフォリオ創業者8名
**完了**: 3件 / 7件（Slack除く）

---

## 完成したケーススタディ

### 1. GitHub - FOUNDER_157（成功企業）✅
- **ファイル**: `/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_157_github.md`
- **創業者**: Tom Preston-Werner & Chris Wanstrath
- **結果**: Microsoft $7.5B買収（2018年）
- **a16z投資**: Series A $100M（2012年、a16z史上最大のSeries A投資）
- **a16zリターン**: $1B+（10倍以上）
- **主要VC**: Peter Levine (a16z)

**特徴**:
- 開発者コミュニティ主導の成長
- ネットワーク効果の典型例
- 4年間の自己資金運営後に初の外部調達
- ソーシャルコーディングという新概念の創出

**fact_check**: PASS（15ソース確認済み）

---

### 2. Coinbase - FOUNDER_355（成功企業・IPO）✅
- **ファイル**: `/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents/05_IPO_Global/FOUNDER_355_coinbase.md`
- **創業者**: Brian Armstrong
- **結果**: IPO（NASDAQ: COIN、2021年4月14日、評価額$86B）
- **a16z投資**: Series B $25M（2013年12月、Chris Dixon主導）
- **a16z保有株**: IPO時$6B以上
- **主要VC**: Chris Dixon (a16z), Fred Wilson (USV)

**特徴**:
- 規制準拠ファーストの戦略
- ウォレット単独→ウォレット+取引所へのピボット
- Y Combinator S2012出身
- Buy Button追加が転換点

**fact_check**: PASS（12ソース確認済み）

---

### 3. Jawbone - FAILURE_008（失敗企業）✅
- **ファイル**: `/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Research/documents/07_Failure_Study/FAILURE_008_jawbone.md`
- **創業者**: Hosain Rahman
- **結果**: 清算（2017年7月）
- **a16z投資**: Series C $49M（2011年）参加
- **総調達額**: $930M
- **ピーク評価額**: $3.2B（2014年）
- **主要VC**: Sequoia Capital, a16z, Khosla Ventures

**失敗パターン**:
- **P13**: スケールしないモデル（ハードウェア薄利多売、リピート収益なし）
- **P17**: 大企業の参入（Apple Watch、Fitbit、Samsung）
- **P23**: 品質問題（初代UPの大規模リコール）
- **P28**: 過剰調達（Death by Overfunding）

**教訓**:
- 初代製品リコールの致命的ダメージ
- ハードウェア単独モデルの限界
- 過剰調達が会社を破壊（$930M調達）
- Bluetoothヘッドセットからウェアラブルへのピボット失敗

**fact_check**: PASS（12ソース確認済み）

---

## 残りのケーススタディ（優先順位順）

### 4. Color - FAILURE_009（失敗企業）【優先順位: 高】
- **創業者**: Bill Nguyen
- **概要**: Series A $41M調達（プロダクトリリース前）、PMF未達成で失敗
- **失敗パターン予測**: P12（PMF未達成のまま調達）
- **参考情報**: a16zも投資、写真共有アプリ

### 5. Oculus - FOUNDER_158（成功企業）【優先順位: 中】
- **創業者**: Palmer Luckey
- **概要**: Facebook $2B買収（2014年）
- **VR/AR市場のパイオニア
- **Kickstarterからの成功事例

### 6. Lyft - FOUNDER_356（成功企業・IPO）【優先順位: 中】
- **創業者**: Logan Green & John Zimmer
- **概要**: IPO（NASDAQ: LYFT、2019年）
- **Uberとの競争
- **ライドシェア市場

### 7. Instagram（a16z視点拡張版）- PIVOT_008【優先順位: 低】
- **既存ファイル**: `PIVOT_003_instagram.md`
- **a16z視点の追加**: Sequoia Series B $7Mにa16zも参加、Facebook買収時のリターン分析
- **注**: 既存ケーススタディが充実しているため、優先度は低い

---

## 作成済みファイルの品質評価

### GitHub（FOUNDER_157）
- ✅ 基本情報完備
- ✅ a16z投資詳細（Peter Levine、$100M、リターン$1B+）
- ✅ 10倍優位性分析
- ✅ フライホイール分析
- ✅ 15ソース確認
- ✅ orchestrate-phase1対応フィールド完備

### Coinbase（FOUNDER_355）
- ✅ 基本情報完備
- ✅ a16z投資詳細（Chris Dixon、Series B $25M、IPO時$6B+）
- ✅ ピボット分析（ウォレット→ウォレット+取引所）
- ✅ 規制対応戦略の詳細
- ✅ 12ソース確認
- ✅ YC S2012バッチ情報

### Jawbone（FAILURE_008）
- ✅ 基本情報完備
- ✅ 失敗パターン4つ分類（P13, P17, P23, P28）
- ✅ 詳細な失敗経緯（初代UPリコール、過剰調達）
- ✅ ピボット分析（Bluetoothヘッドセット→ウェアラブル）
- ✅ 12ソース確認
- ✅ 避けるべきパターン明記

---

## 次のステップ（推奨作業順序）

### Phase 1: 失敗企業完成（優先度: 最高）
1. **Color（FAILURE_009）** を作成
   - Bill Nguyen（Serial entrepreneur、LaLa創業者）
   - Series A $41M調達（プロダクトリリース前）
   - PMF未達成パターンの典型例
   - 推定作業時間: 2-3時間

### Phase 2: 成功企業完成（優先度: 高）
2. **Oculus（FOUNDER_158）** を作成
   - Palmer Luckey（若手創業者、19歳）
   - Kickstarter $2.4M → Facebook $2B買収
   - VR/AR市場の先駆者
   - 推定作業時間: 2-3時間

3. **Lyft（FOUNDER_356）** を作成
   - Logan Green & John Zimmer
   - IPO（2019年）、Uber競合分析
   - ライドシェア市場
   - 推定作業時間: 2-3時間

### Phase 3: Instagram拡張版（優先度: 低）
4. **Instagram a16z視点拡張版**（PIVOT_008拡張）
   - 既存PIVOT_003をベースにa16z視点を追加
   - Sequoia Series B $7M参加状況
   - Facebook買収時のa16zリターン分析
   - 推定作業時間: 1-2時間

---

## 統計サマリー

### 完成済み（3件）
- **成功企業**: 2件（GitHub、Coinbase）
- **失敗企業**: 1件（Jawbone）
- **IPO**: 1件（Coinbase）
- **買収**: 1件（GitHub）
- **清算**: 1件（Jawbone）

### 残り（4件）
- **成功企業**: 2件（Oculus、Lyft）
- **失敗企業**: 1件（Color）
- **Pivot拡張**: 1件（Instagram）

### a16z投資総額（完成済み3件）
- GitHub: $100M（Series A、2012年）
- Coinbase: $25M（Series B、2013年）+ フォローオン投資
- Jawbone: $49M（Series C、2011年）+ 追加ラウンド

### a16zリターン（完成済み3件）
- GitHub: $1B+（10倍以上）
- Coinbase: $6B+（IPO時保有株価値）
- Jawbone: 全損（$49M+の損失）

**成功率**: 2/3（67%）
**総リターン**: $7B+（GitHub $1B + Coinbase $6B）
**総損失**: $49M+（Jawbone）

---

## 学んだ主要な洞察

### a16zの投資戦略
1. **大胆な投資**: GitHub Series A $100Mは当時a16z史上最大
2. **長期保有**: すべての重要ラウンドに参加（Coinbase）
3. **エンタープライズ重視**: Peter LevineがGitHub取締役に就任

### 成功パターン
- **開発者ファースト**: GitHub、Coinbase共に開発者・技術者向け
- **ネットワーク効果**: GitHubの強力なネットワーク効果
- **規制準拠**: Coinbaseの規制ファースト戦略

### 失敗パターン
- **過剰調達の罠**: Jawbone $930M調達が逆効果
- **ハードウェアの難しさ**: 製造品質管理の失敗
- **大企業参入**: Apple Watchの登場でJawbone終了

---

## 推奨される次のアクション

### 即座に実施
1. **Color（FAILURE_009）** を作成して失敗企業2件完成
2. **Oculus（FOUNDER_158）** を作成して成功企業バランスを取る

### その後
3. **Lyft（FOUNDER_356）** を作成してIPO企業を充実
4. Instagram拡張版は必要に応じて後回し可能

### 総推定残り時間
- Color: 2-3時間
- Oculus: 2-3時間
- Lyft: 2-3時間
- Instagram拡張: 1-2時間
- **合計**: 7-11時間（1-2日の作業）

---

## ファイル保存場所

### 完成済み
- `FOUNDER_157_github.md` → `documents/03_VC_Backed/`
- `FOUNDER_355_coinbase.md` → `documents/05_IPO_Global/`
- `FAILURE_008_jawbone.md` → `documents/07_Failure_Study/`

### 今後作成予定
- `FAILURE_009_color.md` → `documents/07_Failure_Study/`
- `FOUNDER_158_oculus.md` → `documents/03_VC_Backed/`
- `FOUNDER_356_lyft.md` → `documents/05_IPO_Global/`
- `PIVOT_008_instagram_a16z.md` → `documents/06_Pivot_Success/`（既存PIVOT_003の拡張版）

---

**作成者**: Claude (Anthropic)
**最終更新**: 2025-12-28
**ステータス**: 3/7完成（43%）、残り4件
