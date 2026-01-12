# Command: /for-recruit-validate-ring-criteria

## Trigger

```
/for-recruit-validate-ring-criteria
```

## Description

リクルートのRing制度（社内起業制度）において、Ring 1-3の各段階で承認要件を満たしているかを診断し、次のRingへの移行可否を判定します。

リクルート製品研究（31製品）から、成功製品の共通パターンとして「CPF 65%以上でRing 1突破、10倍優位性2軸でRing 2突破、外部顧客獲得でRing 3突破」が抽出されています。

## Usage

```
/for-recruit-validate-ring-criteria
```

実行すると、以下の対話形式でRing基準診断を行います:

1. 現在のRing段階確認（Ring 0/1/2/3）
2. 各Ring基準の自動チェック（必須基準、推奨基準）
3. ベンチマーク比較（Airレジ、Airペイ、Geppo等）
4. 改善推奨事項の提示（未達基準がある場合）
5. 次のRing移行可否判定

## Ring基準概要

### Ring 1: CPF検証（Customer Problem Fit）

| 基準 | 必須/推奨 | 基準値 | ベンチマーク |
|------|----------|--------|------------|
| **CPFスコア** | 必須 | ≥ 50% | Airレジ 65%、スタディサプリ 70% |
| **課題共通率** | 必須 | ≥ 60% | Airレジ 75%、Airペイ 85% |
| **User Research** | 推奨 | ≥ 10件 | Airレジ 30件、Airペイ 100件 |

### Ring 2: PSF検証（Product Solution Fit）

| 基準 | 必須/推奨 | 基準値 | ベンチマーク |
|------|----------|--------|------------|
| **10倍優位性** | 必須 | ≥ 1軸 | Airレジ 4軸、Airペイ 4軸 |
| **MVP完成** | 必須 | 完成 | Airレジ（PoC 30社） |
| **ROI見込み** | 推奨 | ≥ 1000% | Airペイ ROI 11,450% |
| **社内リソース活用** | 推奨 | ≥ 3種 | Airレジ 3種（顧客基盤、営業網、ブランド） |

### Ring 3: PMF検証（Product Market Fit）

| 基準 | 必須/推奨 | 基準値 | ベンチマーク |
|------|----------|--------|------------|
| **外部顧客獲得** | 必須 | ≥ 100社/人 | Airレジ 1年で10万店舗 |
| **収益化開始** | 必須 | 発生 | Airペイ 初年度売上5億円 |
| **3年黒字・5年累損解消計画** | 必須 | 策定済み | Airレジ 3年黒字達成 |
| **LTV/CAC比** | 推奨 | ≥ 5.0 | Airレジ 15-30倍 |

## Output

- **Ring診断レポート**: Markdown形式、必須基準・推奨基準チェック結果、ベンチマーク比較、改善推奨事項
- **Quality Gate**: 各Ring基準クリア判定、次のRing移行可否
- **Next Actions**: 具体的なアクションプラン

## Examples

### Example 1: Ring 1診断（承認可）

```
現在のRing: Ring 1（CPF検証中）

【必須基準チェック結果】
- CPFスコア: 65%（基準値 ≥ 50%）✅ PASS
- 課題共通率: 75%（基準値 ≥ 60%）✅ PASS

【推奨基準チェック結果】
- CPFスコア: 65%（基準値 ≥ 65%）✅ PASS
- 課題共通率: 75%（基準値 ≥ 70%）✅ PASS
- User Research: 30件（基準値 ≥ 30件）✅ PASS

【ベンチマーク比較】
あなたのプロジェクトはAirレジと同等レベルです。

【総合判定】
Ring 1承認可（Ring 2移行可）
```

### Example 2: Ring 2診断（承認可、改善推奨あり）

```
現在のRing: Ring 2（PSF検証中）

【必須基準チェック結果】
- 10倍優位性: 1軸（基準値 ≥ 1軸）✅ PASS
- MVP完成: 完成 ✅ PASS

【推奨基準チェック結果】
- 10倍優位性: 1軸（基準値 ≥ 2軸）⚠️ PASS_WITH_WARNING
- ROI見込み: 800%（基準値 ≥ 1000%）⚠️ PASS_WITH_WARNING
- 社内リソース活用: 1種（基準値 ≥ 3種）⚠️ PASS_WITH_WARNING

【改善推奨事項】
1. 10倍優位性を2軸以上に強化（現在1軸のみ）
2. 社内リソース活用を3種以上に増やす（ROI向上）
3. 営業チャネル活用でCAC削減（ROI 1000%以上達成）

【総合判定】
Ring 2承認可（ただし改善推奨事項あり）
```

### Example 3: Ring 3診断（撤退警戒）

```
現在のRing: Ring 3（PMF検証中）

【必須基準チェック結果】
- 外部顧客獲得: 150社（基準値 ≥ 100社）✅ PASS
- 収益化開始: 開始 ✅ PASS
- 3年黒字・5年累損解消計画: 策定済み ✅ PASS

【撤退基準チェック結果】
- 3年目単月黒字: 未達成 ⚠️ Yellow Alert
- 10倍優位性維持: 維持 ✅ Green
- 市場成長率: 3%（基準値 ≥ 5%）⚠️ Yellow Alert

【総合判定】
Ring 3承認可（ただし撤退基準Level 1該当、改善必要）

【改善アクション】
1. 3年目単月黒字達成に向けたコスト削減策
2. 市場成長率低下への対応（新規市場セグメント開拓）
3. 4年目単月黒字未達の場合、撤退検討（Level 2 Orange Alert）
```

## Skill Location

`/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_recruit/validate-ring-criteria/SKILL.md`

## Related Commands

- `/for-recruit-inventory-internal-resources`: 社内リソース6カテゴリ棚卸し、ROI定量化
- `/for-recruit-build-approval-deck`: 社内承認用資料作成
- `/for-recruit-validate-cpf`: CPF検証（基準50%）
- `/for-recruit-validate-psf`: PSF検証（10倍優位性1軸以上）
