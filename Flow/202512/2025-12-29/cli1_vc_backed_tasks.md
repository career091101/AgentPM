# CLI-1: VC投資成功企業タスクリスト

**担当**: VC_Backed (43件) + IPO_Global Part1 (21件) = **64件**
**難易度**: 中
**推定時間**: 4-5時間
**優先度**: 高

---

## タスク概要

このCLIでは、トップティアVC投資先の成功企業を調査します。
- VC情報が豊富
- 資金調達データが明確
- ソースが充実

---

## 03_VC_Backed (43件)

### Benchmark Capital投資先 (10件)
- [ ] FOUNDER_161: Uber (Travis Kalanick)
- [ ] FOUNDER_162: Snapchat (Evan Spiegel) - 既存と重複確認
- [ ] FOUNDER_163: Twitter (Jack Dorsey)
- [ ] FOUNDER_164: Instagram (Kevin Systrom)
- [ ] FOUNDER_165: Dropbox (Drew Houston)
- [ ] FOUNDER_166: WeWork (Adam Neumann) - Failureと重複の可能性
- [ ] FOUNDER_167: eBay (Pierre Omidyar)
- [ ] FOUNDER_168: Zillow (Rich Barton)
- [ ] FOUNDER_169: Nextdoor (Nirav Tolia)
- [ ] FOUNDER_170: Stitch Fix (Katrina Lake)

### Founders Fund投資先 (10件)
- [ ] FOUNDER_171: SpaceX (Elon Musk)
- [ ] FOUNDER_172: Palantir (Peter Thiel) - 既存確認
- [ ] FOUNDER_173: Stripe (Patrick & John Collison)
- [ ] FOUNDER_174: Airbnb (Brian Chesky)
- [ ] FOUNDER_175: Lyft (Logan Green)
- [ ] FOUNDER_176: Wish (Piotr Szulczewski)
- [ ] FOUNDER_177: Affirm (Max Levchin)
- [ ] FOUNDER_178: Oscar Health (Mario Schlosser)
- [ ] FOUNDER_179: Flexport (Ryan Petersen)
- [ ] FOUNDER_180: Anduril (Palmer Luckey)

### Index Ventures投資先 (10件)
- [ ] FOUNDER_181: Dropbox (Drew Houston)
- [ ] FOUNDER_182: Figma (Dylan Field)
- [ ] FOUNDER_183: Discord (Jason Citron)
- [ ] FOUNDER_184: Revolut (Nikolay Storonsky)
- [ ] FOUNDER_185: TransferWise (Wise) (Kristo Käärmann)
- [ ] FOUNDER_186: Robinhood (Vlad Tenev)
- [ ] FOUNDER_187: Supercell (Ilkka Paananen)
- [ ] FOUNDER_188: King (Candy Crush) (Riccardo Zacconi)
- [ ] FOUNDER_189: Sonos (John MacFarlane)
- [ ] FOUNDER_190: Etsy (Rob Kalin)

### Kleiner Perkins投資先 (8件)
- [ ] FOUNDER_191: Google (Larry Page & Sergey Brin)
- [ ] FOUNDER_192: Amazon (Jeff Bezos)
- [ ] FOUNDER_193: Netscape (Marc Andreessen)
- [ ] FOUNDER_194: Genentech (Herbert Boyer)
- [ ] FOUNDER_195: AOL (Steve Case)
- [ ] FOUNDER_196: Sun Microsystems (Vinod Khosla)
- [ ] FOUNDER_197: Compaq (Rod Canion)
- [ ] FOUNDER_198: Segway (Dean Kamen)

### Lightspeed Venture Partners投資先 (5件)
- [ ] FOUNDER_199: Snap (Evan Spiegel)
- [ ] FOUNDER_200: Nest (Tony Fadell)
- [ ] FOUNDER_201: Nutanix (Dheeraj Pandey)
- [ ] FOUNDER_202: AppDynamics (Jyoti Bansal)
- [ ] FOUNDER_203: Affirm (Max Levchin)

---

## 05_IPO_Global Part1 (21件)

### FOUNDER_353-373 (グローバルIPO成功企業)

- [ ] FOUNDER_353: Shopify (Tobias Lütke)
- [ ] FOUNDER_354: Canva (Melanie Perkins)
- [ ] FOUNDER_355: Coinbase (Brian Armstrong) - 既存確認
- [ ] FOUNDER_356: Roblox (David Baszucki)
- [ ] FOUNDER_357: Unity (David Helgason)
- [ ] FOUNDER_358: Databricks (Ali Ghodsi)
- [ ] FOUNDER_359: UiPath (Daniel Dines)
- [ ] FOUNDER_360: CrowdStrike (George Kurtz)
- [ ] FOUNDER_361: Snowflake (Frank Slootman)
- [ ] FOUNDER_362: ServiceNow (Fred Luddy)
- [ ] FOUNDER_363: Reddit (Steve Huffman) - 既存確認
- [ ] FOUNDER_364: MongoDB (Dev Ittycheria)
- [ ] FOUNDER_365: Twilio (Jeff Lawson)
- [ ] FOUNDER_366: ZoomInfo (Henry Schuck)
- [ ] FOUNDER_367: Elastic (Shay Banon)
- [ ] FOUNDER_368: Atlassian (Mike Cannon-Brookes)
- [ ] FOUNDER_369: DocuSign (Tom Gonser)
- [ ] FOUNDER_370: Workday (Aneel Bhusri & Dave Duffield)
- [ ] FOUNDER_371: Splunk (Michael Baum)
- [ ] FOUNDER_372: New Relic (Lew Cirne)
- [ ] FOUNDER_373: HubSpot (Brian Halligan & Dharmesh Shah)

---

## 実行方法

### ステップ1: 並列バッチ実行開始

```
このタスクリストの全64件を並列バッチで実行してください。

条件:
- 並列数: 10-15エージェント
- 各ファイル形式: Founder_Research標準テンプレート
- Research Guidelinesに完全準拠
- Null補完: 全フィールド必須
- ソース: 最低12件目標
- Fact Check: 全件PASS必須
```

### ステップ2: 進捗確認 (30分ごと)

```
現在の進捗を報告してください:
- 完了件数 / 64件
- 平均実行時間
- エラー・失敗件数
```

### ステップ3: 品質チェック (完了後)

```
全64件の品質チェックを実行してください:
- 平均スコア算出
- Fact Check Pass率
- Null残存チェック
- ソース数分布
```

### ステップ4: Git Commit

```
CLI-1の64件をコミットしてください:

git checkout -b cli1-vc-backed
git add Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/*
git add Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/05_IPO_Global/FOUNDER_353_*.md
...
git add Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/05_IPO_Global/FOUNDER_373_*.md
git commit -m "feat: CLI-1完了 - VC_Backed 64件達成"
```

---

## 注意事項

1. **重複チェック**: 既存ファイルと重複する場合はスキップ
2. **VC視点**: 各VCの投資判断・支援内容を重点的に記載
3. **Exit詳細**: IPO/買収の詳細データを収集
4. **データ精度**: 資金調達額・バリュエーションは複数ソース確認

---

**作成日**: 2025-12-29
**ステータス**: 実行準備完了
