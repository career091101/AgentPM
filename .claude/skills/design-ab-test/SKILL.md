---
name: design-ab-test
description: |
  A/Bテストの仮説設計、サンプルサイズ計算、統計的有意性検定（p値 < 0.05）を実施。データドリブンな意思決定を支援し、コンバージョン率を最適化します。

  使用タイミング：
  - LP改善時
  - UVP最適化時
  - コンバージョンファネル改善時

  所要時間：30-40分
  出力：A/Bテスト設計書、サンプルサイズ計算、結果判定
trigger_keywords:
  - "A/Bテスト"
  - "統計的検定"
  - "コンバージョン最適化"
  - "仮説検証"
stage: Phase2-3（Discovery-Executing）
dependencies: []
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/ab_test_design.md
execution_time: 30-40分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P2
framework_compliance: 100%
---

# Design A/B Test Skill

A/Bテストの仮説設計から統計的有意性検定まで、データドリブンな意思決定を支援する自律実行型Skill。

---

## このSkillでできること

1. **仮説設計**: 何を改善するか、期待効果を明確化
2. **サンプルサイズ計算**: 最低限必要なトラフィック数を算出
3. **バリエーション設計**: コントロール vs バリアント（最大4つ）
4. **テスト期間推定**: 統計的有意性を得るために必要な期間
5. **統計的有意性検定**: p値 < 0.05、Confidence Interval計算
6. **Winner自動判定**: 有意差あり → Winner、なし → 再テスト
7. **ロールアウト判断**: Winner確定後の展開計画

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `persona.md`, `psf_diagnosis.md`, `lp/index.html` |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/ab_test_design.md` |
| **次のSkill** | `/build-lp`（Winner反映）または `/create-sns-content` |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-40分

---

### STEP 1: 仮説設定

**目的**: 何を改善するか、期待効果を定量化

**実行内容**:

1. **改善対象の特定**（LP/UVP/CTAから選択）
   ```markdown
   ## 改善対象
   - [ ] **Hero Section** - UVPキャッチコピー
   - [ ] **CTA Button** - テキスト・色・配置
   - [ ] **Problem Section** - 課題共鳴文言
   - [ ] **Pricing** - 価格表示方法
   - [ ] **Features** - 機能説明の順序
   ```

2. **現状のパフォーマンス測定**（ベースライン）
   - CVR（Conversion Rate）: 現在の値
   - 平均滞在時間: 現在の値
   - 離脱率: 各セクションごと

3. **仮説文の作成**
   ```markdown
   ### A/Bテスト仮説

   **H0（帰無仮説）**: バリアントAとコントロールの間にCVRの差はない
   **H1（対立仮説）**: バリアントAはコントロールよりもCVRが高い

   **期待効果**:
   - CVR改善: 3% → 5%（+67%）
   - 根拠: ペルソナインタビューで「価格が見えにくい」という声が40%
   ```

4. **成功判定基準**
   - **Primary Metric**: CVR（メール登録率）
   - **Secondary Metrics**:
     - 平均滞在時間（60秒以上維持）
     - 離脱率（Hero 30%以下維持）
     - デバイス別CVR（Mobile/Desktop）

---

### STEP 2: サンプルサイズ計算

**目的**: 統計的有意性を得るために必要な最低トラフィック数を算出

**計算式**（Two-Proportion Z-Test）:

```python
import math
from scipy.stats import norm

def calculate_sample_size(p1, p2, alpha=0.05, power=0.80):
    """
    p1: コントロールのCVR（現在値）
    p2: バリアントの期待CVR
    alpha: 有意水準（デフォルト 0.05 = 95%信頼区間）
    power: 検出力（デフォルト 0.80 = 80%）
    """
    z_alpha = norm.ppf(1 - alpha/2)  # 両側検定
    z_beta = norm.ppf(power)

    p_pooled = (p1 + p2) / 2

    n = ((z_alpha * math.sqrt(2 * p_pooled * (1 - p_pooled)) +
          z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) /
         (p1 - p2)) ** 2

    return math.ceil(n)

# 例: CVR 3% → 5%への改善を検出する場合
n_per_variant = calculate_sample_size(p1=0.03, p2=0.05)
print(f"各バリアントに必要なサンプル数: {n_per_variant}")
```

**出力例**:
```markdown
## サンプルサイズ計算結果

**設定パラメータ**:
- コントロールCVR: 3%
- 期待CVR: 5%
- 有意水準（α）: 0.05（95%信頼区間）
- 検出力（1-β）: 0.80

**計算結果**:
- **各バリアント必要サンプル数**: 1,571 visitors
- **合計必要サンプル数**: 3,142 visitors（コントロール + バリアント）
- **現在の週間トラフィック**: 500 visitors
- **推定テスト期間**: 6.3週間 → **7週間**

**警告**:
⚠️ テスト期間が長すぎる場合（8週間以上）、シーズン変動の影響を受けるリスクあり。
   → 対策: 期待効果を大きくする（CVR 5% → 6%）、トラフィック増加（広告配信）
```

---

### STEP 3: バリエーション設計

**目的**: コントロール vs バリアント（最大4つ）の明確化

**実行内容**:

1. **コントロール（A）**: 現在のLP
2. **バリアント（B/C/D）**: 改善案（最大3つ）

**例: CTAボタンのA/Bテスト**

```markdown
## バリエーション設計

### コントロール（A）
- **CTA文言**: "無料で試す"
- **ボタン色**: #4CAF50（緑）
- **配置**: Hero下部、固定位置なし

### バリアント（B）- 緊急性訴求
- **CTA文言**: "今すぐ無料で試す"（緊急性）
- **ボタン色**: #FF5722（オレンジ）
- **配置**: Hero下部、固定位置なし

### バリアント（C）- 価値強調
- **CTA文言**: "初月無料で試す"（価値）
- **ボタン色**: #4CAF50（緑）
- **配置**: Hero下部 + スティッキーフッター

### バリアント（D）- 社会的証明
- **CTA文言**: "1,000人が利用中 - 無料で試す"（社会的証明）
- **ボタン色**: #2196F3（青）
- **配置**: Hero下部、固定位置なし

**注**: バリアントが多いとサンプルサイズが増加。3バリアント（A/B/C）推奨。
```

**トラフィック分配**（均等分配）:
- 2バリアント（A/B）: 50% / 50%
- 3バリアント（A/B/C）: 33% / 33% / 34%
- 4バリアント（A/B/C/D）: 25% / 25% / 25% / 25%

---

### STEP 4: テスト期間推定

**目的**: 統計的有意性を得るために必要な期間を算出

**計算式**:

```python
def estimate_test_duration(sample_size_per_variant, weekly_traffic, num_variants=2):
    """
    sample_size_per_variant: 各バリアント必要サンプル数
    weekly_traffic: 週間トラフィック数
    num_variants: バリアント数（コントロール含む）
    """
    total_sample_size = sample_size_per_variant * num_variants
    weeks = total_sample_size / weekly_traffic
    return math.ceil(weeks)

# 例: 各バリアント1,571、週間500、2バリアント
duration = estimate_test_duration(1571, 500, 2)
print(f"推定テスト期間: {duration}週間")
```

**出力例**:
```markdown
## テスト期間推定

**計算条件**:
- 各バリアント必要サンプル数: 1,571
- バリアント数: 2（A/B）
- 合計必要サンプル数: 3,142
- 現在の週間トラフィック: 500
- 推定期間: **7週間**

**テストスケジュール**:
- Week 1-2: テスト実装・動作確認
- Week 3-9: データ収集（7週間）
- Week 10: データ分析・Winner判定
- Week 11: Winner展開

**リスク**:
- 7週間以上のテストはシーズン変動の影響を受ける可能性あり
- 対策: 週次でデータ確認、早期終了（Early Stopping）の検討
```

---

### STEP 5: 統計的有意性検定

**目的**: p値 < 0.05、Confidence Interval計算で有意差を検証

**検定手法**: Two-Proportion Z-Test

**計算式**:

```python
from scipy.stats import norm
import math

def two_proportion_z_test(n1, p1, n2, p2):
    """
    n1, n2: 各バリアントのサンプル数
    p1, p2: 各バリアントのCVR
    """
    # Pooled proportion
    p_pooled = (n1 * p1 + n2 * p2) / (n1 + n2)

    # Standard error
    se = math.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))

    # Z-score
    z = (p1 - p2) / se

    # P-value (two-tailed)
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # Confidence Interval (95%)
    ci_diff = 1.96 * se

    return {
        'z_score': z,
        'p_value': p_value,
        'ci_lower': (p1 - p2) - ci_diff,
        'ci_upper': (p1 - p2) + ci_diff
    }

# 例: A（3%、n=1571）vs B（5%、n=1571）
result = two_proportion_z_test(n1=1571, p1=0.05, n2=1571, p2=0.03)
print(f"P値: {result['p_value']:.4f}")
print(f"95%信頼区間: [{result['ci_lower']:.4f}, {result['ci_upper']:.4f}]")
```

**出力例**:
```markdown
## 統計的有意性検定結果

**テスト期間**: 2025-01-01 ~ 2025-02-18（7週間）

**データ収集結果**:
| バリアント | Visitors | Conversions | CVR |
|-----------|---------|-------------|-----|
| A（コントロール） | 1,571 | 47 | 2.99% |
| B（緊急性訴求） | 1,571 | 79 | 5.03% |

**統計検定結果**:
- **Z-score**: 3.42
- **P値**: 0.0006
- **95%信頼区間**: [0.0086, 0.0322]
- **判定**: ✅ **統計的有意差あり**（p < 0.05）

**解釈**:
- バリアントB（緊急性訴求）はコントロールAよりも2.04%高いCVRを示した
- この差は偶然ではない（p = 0.0006 < 0.05）
- 95%の確率で、真の差は0.86% ~ 3.22%の範囲にある
```

**Early Stopping（早期終了）の検討**:

```markdown
### Early Stopping判定（Week 5時点）

**データ収集中間結果**（Week 5 / 7週間）:
| バリアント | Visitors | Conversions | CVR |
|-----------|---------|-------------|-----|
| A | 1,122 | 34 | 3.03% |
| B | 1,122 | 57 | 5.08% |

**中間検定結果**:
- P値: 0.0012
- 判定: ✅ 有意差あり

**Early Stopping判定**:
✅ **Week 5で早期終了可能**
   理由: 既に統計的有意差が確認され、残り2週間で逆転する可能性は低い（<1%）
   メリット: 2週間早くWinnerを展開可能、機会損失削減
```

---

### STEP 6: Winner決定

**目的**: 統計的有意差に基づきWinnerを決定

**判定ルール**:

```markdown
## Winner判定ルール

### ケース1: 有意差あり（p < 0.05）
✅ **Winner**: CVRが最も高いバリアント
   → 直ちにロールアウト

### ケース2: 有意差なし（p ≥ 0.05）
⚠️ **再テスト検討**
   原因分析:
   - サンプルサイズ不足（期待効果が小さすぎた）
   - バリアント設計が不適切（差別化不足）
   - ターゲット誤り（ペルソナとのミスマッチ）

   対策:
   1. 期待効果を大きくする（CVR 5% → 7%）
   2. バリアント再設計（より大胆な変更）
   3. ターゲットセグメント変更（新規 vs 既存）

### ケース3: マイナス結果（バリアントがコントロールより悪い）
❌ **コントロール維持**
   学び:
   - 仮説が誤っていた
   - バリアント実装でユーザー体験が悪化
   → レトロスペクティブ実施
```

**出力例**:
```markdown
## Winner決定

**Winner**: バリアントB（緊急性訴求）

**決定根拠**:
- CVR: 5.03%（コントロール 2.99%から+68%改善）
- P値: 0.0006（統計的有意差あり）
- 95%信頼区間: [0.86%, 3.22%]

**期待インパクト**（月間1,000 visitors換算）:
- コントロールA: 30 conversions/月
- バリアントB: 50 conversions/月
- **増加**: +20 conversions/月（+67%）

**次のアクション**: ロールアウト計画へ
```

---

### STEP 7: ロールアウト判断

**目的**: Winnerを段階的に展開

**ロールアウト戦略**:

```markdown
## ロールアウト計画

### Phase 1: 段階的展開（Week 1）
- **トラフィック配分**: Winner 80% / コントロール 20%
- **目的**: Winner展開後の異常検知（CVR急落、エラー増加）
- **監視指標**: CVR、離脱率、エラー率、平均滞在時間

### Phase 2: 完全展開（Week 2）
- **トラフィック配分**: Winner 100%
- **コントロール廃止**: 旧バージョン削除

### Phase 3: 次のA/Bテスト設計（Week 3）
- **改善対象**: Pricing Section（次の仮説）
- **仮説**: 「月額表示よりも年額表示（月額換算）の方がCVR高い」
```

**モニタリング計画**:

```markdown
## ロールアウト後モニタリング

**Week 1-2: 集中監視**
| 指標 | 目標値 | アラート条件 |
|------|--------|-------------|
| CVR | 5.0%以上 | 4.5%以下に低下 |
| 離脱率（Hero） | 30%以下 | 35%以上に増加 |
| エラー率 | 0.5%以下 | 1%以上 |
| 平均滞在時間 | 60秒以上 | 50秒以下に低下 |

**Week 3-4: 通常監視**
- 週次レポート
- 次のA/Bテスト候補の優先順位付け
```

---

### STEP 8: 成果物出力

**目的**: A/Bテスト設計書を `Flow/{YYYYMM}/{YYYY-MM-DD}/ab_test_design.md` に出力

**出力フォーマット**:

```markdown
---
title: A/Bテスト設計書
date: {YYYY-MM-DD}
test_target: Hero CTA Button
hypothesis: 緊急性訴求でCVR向上
status: Winner決定・ロールアウト完了
---

# A/Bテスト設計書

## 1. 仮説設定
[STEP 1の内容]

## 2. サンプルサイズ計算
[STEP 2の内容]

## 3. バリエーション設計
[STEP 3の内容]

## 4. テスト期間推定
[STEP 4の内容]

## 5. 統計的有意性検定
[STEP 5の内容]

## 6. Winner決定
[STEP 6の内容]

## 7. ロールアウト計画
[STEP 7の内容]

## 8. レトロスペクティブ

**学び**:
- ✅ 緊急性訴求（"今すぐ"）はCVR +67%改善に貢献
- ✅ オレンジ色CTAは視認性向上に有効
- ❌ スティッキーフッター（バリアントC）は離脱率悪化

**次のA/Bテスト候補**:
1. Pricing Section: 月額 vs 年額表示
2. Problem Section: 課題文言の3パターン
3. Features: 機能順序の入れ替え

**Framework準拠**:
✅ 起業の科学 - 起業大全5（UX）準拠
✅ 統計的有意性検定（p < 0.05）実施
✅ サンプルサイズ計算実施
```

---

## 成功基準

| 項目 | 合格条件 |
|------|----------|
| **サンプルサイズ計算** | Two-Proportion Z-Test公式を使用 |
| **統計的有意性検定** | p値、95%信頼区間を計算 |
| **バリエーション管理** | コントロール + 最大3バリアント（計4つ） |
| **Winner自動判定** | p < 0.05で有意差あり → Winner決定 |
| **ロールアウト計画** | 段階的展開（80% → 100%） |
| **成果物出力** | `ab_test_design.md` 生成 |

**総合判定**:
- 6/6: ✅ 完了 → 次のスキル実行
- 4-5/6: ⚠️ 要修正
- 0-3/6: ❌ 再設計

---

## Knowledge Base参照

- A/Bテスト概要: `@startup_science/01_stages/ux/ab_testing.md`
- 統計的有意性検定: `@startup_science/01_stages/ux/statistical_significance.md`
- UXフレームワーク: `@startup_science/01_stages/ux/ux_frameworks.md`

---

## 補足: A/Bテストツール推奨

**無料ツール**:
1. **Google Optimize**（2023年終了） → **代替**: VWO、Optimizely Free Tier
2. **Mixpanel A/B Testing**（無料枠: 1,000 MTU）
3. **Firebase A/B Testing**（モバイルアプリ向け）

**有料ツール**（PMF後推奨）:
1. **Optimizely**（$50,000/年～）
2. **VWO**（$199/月～）
3. **AB Tasty**（$500/月～）

**自社実装**（MVP段階推奨）:
- Google Analytics + カスタムイベント
- Cloudflare Workers（トラフィック分配）
- 計算スクリプト（Python/JavaScript）

---

## 自動実行時の注意事項

1. **トラフィック不足時**: サンプルサイズ計算で8週間以上必要と判定された場合、広告配信を推奨
2. **複数バリアント**: 3バリアント以上はサンプルサイズ増加（推奨: 2バリアント）
3. **Early Stopping**: 中間検定で有意差が出た場合、早期終了を検討
4. **シーズン変動**: 年末年始・祝日はテスト期間から除外

---

## 起業の科学準拠チェック

- ✅ **A/Bテスト**: 起業大全5（UX）準拠
- ✅ **統計的有意性検定**: p値 < 0.05
- ✅ **サンプルサイズ計算**: Two-Proportion Z-Test
- ✅ **仮説検証サイクル**: Build-Measure-Learn

**フレームワーク準拠率**: 100%

---

**作成日**: 2025-12-31
**最終更新**: 2025-12-31
**バージョン**: v1.0
