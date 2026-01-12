# /for-recruit-validate-pmf

**Domain**: ForRecruit (企業内新規事業)
**Skill Path**: `.claude/skills/for_recruit/validate-pmf/SKILL.md`

## 概要

PMF（Product Market Fit）達成を7指標で総合判定するForRecruit特化版スキル。起業の科学の4指標（Sean Ellisテスト、月次成長率、Churn Rate、NPS）に加え、Ring 3基準（外部顧客獲得100社/人以上、収益化開始、3年黒字計画）を統合評価。リクルート製品研究31件の成功パターンを参照。

## 使用タイミング

- Ring 2突破後、外部顧客獲得段階
- MVP稼働、初期顧客100社/人以上獲得後
- Phase2（PMF検証）開始時

## 前提条件

- PSF達成済み（`/for-recruit-validate-psf` 完了）
- Ring 2突破済み（`/for-recruit-validate-ring-criteria` Ring 2承認可）
- MVP稼働中（実プロダクトが動作している）
- 外部顧客100社/人以上獲得（社内顧客除外）
- 直近3ヶ月の利用データ存在
- 収益化開始（初期売上発生）
- 3年黒字・5年累損解消計画策定済み

## 実行

```
/for-recruit-validate-pmf
```

## 出力

`Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md`

## 判定基準（ForRecruit調整）

### 7指標評価

| 指標 | 目標値 | ForRecruit調整 |
|------|--------|---------------|
| **外部顧客獲得** | ≥100社/人 | Ring 3必須要件（新規追加） |
| **Sean Ellisテスト** | ≥40% | 起業の科学準拠（維持） |
| **月次成長率** | ≥10%/月 | 起業の科学準拠（維持） |
| **Churn Rate** | ≤5%/月 | 起業の科学準拠（維持） |
| **NPS** | ≥50 | 起業の科学準拠（維持） |
| **収益化開始** | 初期売上発生 | Ring 3必須要件（新規追加） |
| **3年黒字計画** | 策定済み | Ring 3必須要件（新規追加） |

### 総合判定

- ✅ **PMF達成（Ring 3承認可）**: 外部顧客100社/人以上 + 4指標すべて✅ + 収益化開始 + 3年黒字計画
- ⚠️ **要改善**: 外部顧客100社/人以上 + 2-3指標✅
- ❌ **PMF未達成**: 外部顧客100社/人未満 OR 0-1指標✅

## ForRecruit Benchmark（統合研究より）

### 成功事例

**Airレジ（PMF達成）**:
- 外部顧客獲得: 1年で10万店舗、3年で90.4万アカウント
- Sean Ellis推定: 45%
- NPS推定: 60-70
- 収益化: Airペイ連携で手数料収益、3年黒字達成

**Airペイ（PMF達成）**:
- 外部顧客獲得: 1年で20万店舗、3年で51.5万加盟店
- クロスセル率: 57%（業界標準5-15%の4-11倍）
- NPS推定: 70-80
- 収益化: 初年度売上5億円、3年黒字達成

**Geppo（PMF達成）**:
- 外部顧客獲得: 2年で300社（BtoB）
- 回答率: 96%（DAU/MAU換算90%以上）
- 継続率: 98%
- NPS推定: 70-80

### 失敗事例

**エリクラ（PMF未達成）**:
- 外部顧客獲得: 6年で10万人（目標1,000万人未達）
- DAU/MAU推定: 10%未満
- 教訓: 社内実証のみで長期化は避ける、1-2年でPMF判断

**スタディサプリ個別指導（PMF未達成）**:
- Unit Economics不健全（講師人件費を賄えず）
- 1.5年で撤退
- 教訓: 収益性犠牲の成長は持続しない

## 次のステップ

### PMF達成時
- `/for-recruit-build-approval-deck` で役員承認用資料作成
- `/measure-aarrr` でAARRRファネル測定
- 本格事業化（Ring 3承認申請）

### 要改善時
- 未達成指標の改善アクション実行
- 1-2ヶ月後に再診断

### PMF未達成時
- `/pivot-decision` でPivot判断
- 撤退検討（リクルート撤退基準: 1.5-6年）

## 所要時間

30-50分（アンケート設計、データ分析含む）

## 参照

- Skill詳細: `.claude/skills/for_recruit/validate-pmf/SKILL.md`
- Research: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- 起業の科学: `startup_science/01_stages/pmf/`
