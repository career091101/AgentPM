# Founder Agent Videos Index

## 概要

このディレクトリには469本のYouTube動画のトランスクリプトが含まれています。
全ファイルにYAML frontmatterメタデータが適用されており、効率的な検索とナビゲーションが可能です。

## インデックスファイル

統合index.yamlは4つのパートに分割されています：

- **index_part1.yaml**: ファイル 1-117（117ファイル）
- **index_part2.yaml**: ファイル 118-234（117ファイル）
- **index_part3.yaml**: ファイル 235-351（117ファイル）
- **index_part4.yaml**: ファイル 352-469（118ファイル）

## 統計情報

- **総ファイル数**: 469
- **主要カテゴリ**: AI Agents, Tutorial, AI技術, Startup, Technology
- **頻出タグ**: AI, Agents, LLM, machine_learning, Tutorial, PMF

---

## フェーズ処理戦略

### Phase 1: パイロットバッチ（50ファイル）

**実施日**: 2025-12-31
**対象**: 50ファイル（pilot_50_videos.txt）
**目的**: 処理パイプライン検証、品質確認、サンプルデータ収集

**選定基準**:
- ランダムサンプリング（469本中50本）
- カテゴリバランス考慮（AI Agents, Tutorial, Startup等）
- 多様性確保（異なるspeaker、topics、video_id範囲）

**処理内容**:
1. Whisper APIでトランスクリプト生成
2. LLM分析でYAML frontmatter生成
3. テーママッピング適用
4. 品質検証（完全性、正確性、メタデータ整合性）

**成功基準**:
- トランスクリプト生成成功率: 95%以上
- メタデータ完全性: 100%
- 平均処理時間: 5分/ファイル以内
- 品質スコア: 85点以上

---

### Phase 2: 残り419ファイル（本番処理）

**予定日**: Phase 1成功後
**対象**: 419ファイル（remaining_419_videos.txt）
**目的**: 全469ファイルの完全処理達成

**処理戦略**:
- Phase 1で検証されたパイプラインを適用
- バッチ処理（50-100ファイル/バッチ）
- 並列処理で効率化（最大5並列）
- エラーハンドリング強化（再試行ロジック）

**スケジュール想定**:
- バッチ1（100ファイル）: 1日目
- バッチ2（100ファイル）: 2日目
- バッチ3（100ファイル）: 3日目
- バッチ4（119ファイル）: 4日目
- 品質検証＆修正: 5日目

**リソース要件**:
- Whisper API予算: 約$200-$300（419ファイル×$0.5-$0.7）
- 処理時間: 約35-40時間（419ファイル×5分）
- ストレージ: 約2-3GB（トランスクリプト+メタデータ）

---

## ファイル一覧

### Pilot 50ファイル（Phase 1対象）

```
1WImBwiA7RA.md, 6B0p9rCN_p0.md, 847eGg-X7Us.md, 8_liatgLkLc.md,
8tg8z-Fi0MU.md, 9HZVqxGV55g.md, AXsrrF07u2k.md, Awvj4yLYafo.md,
BER3EhUIyz0.md, ESIL0Rzl5VQ.md, FXgOgAJrhis.md, GJpfVaRaPNY.md,
GjWQsfQX7C0.md, HFEwfd7OMLQ.md, Hu3lQfg20Og.md, JfM1mr2bCuk.md,
NoVMk_P6fgY.md, OSeVMcz8p-A.md, OtJV9SCyfuE.md, PYJSIp6JU94.md,
RJXio_jpc_Y.md, SsqwRLy0CNQ.md, SyS-GJ1p8Fo.md, T5ry8nlFAkg.md,
ULszsXDyjMY.md, US18jDIDUfQ.md, UjQBgwTcvng.md, VCLgnUQVnPk.md,
WhooDE1x2P4.md, X95MFcYH1_s.md, Y-rQSxACvOg.md, _vrPvYBtmTk.md,
ddoPk6DwCFE.md, fqcKRn4ZjDI.md, gYlA_xSslQE.md, guXhZ_q6sVY.md,
i5kwX7jeWL8.md, jVazhPkg-8Q.md, knT3kN4EpOo.md, mcxeEUC5B4M.md,
mv7G38U8iYY.md, nKuXMDCtyQI.md, pablEq295Wc.md, q6DU_9CzgXA.md,
slN-Ms8rdxw.md, t8jNXTe2_Gk.md, tHoJAwrs1q8.md, w5xtbdoPfTg.md,
xRmzLHnssXE.md, z7JijNu5j4w.md
```

**総数**: 50ファイル

### Remaining 419ファイル（Phase 2対象）

419ファイルのリストは `remaining_419_videos.txt` を参照。

---

## 使用方法

各パートのindex_part*.yamlファイルを参照して、目的のコンテンツを検索してください。
各ファイルには以下の情報が含まれています：

- video_id, title, speaker
- tags, topics, category
- summary

## 次のアクション

1. **Phase 1実行**: Pilot 50ファイルの処理開始
2. **品質検証**: Phase 1成果物の検証
3. **Phase 2計画**: 419ファイル処理の詳細スケジュール策定
4. **本番実行**: Phase 2バッチ処理実行

## メタデータ生成日

2025-12-31
