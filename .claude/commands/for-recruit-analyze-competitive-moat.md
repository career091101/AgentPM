---
name: for-recruit-analyze-competitive-moat
description: ForRecruit向け経済的堀（Competitive Moat）分析スキルを起動
trigger: /for-recruit-analyze-competitive-moat
skill_path: for_recruit/analyze-competitive-moat
---

# ForRecruit: Analyze Competitive Moat

競争優位性の持続可能性（Economic Moat）を分析し、10倍優位性が一時的か持続可能かを評価します。

## 使用タイミング

- `/for-recruit-validate-10x` 実行後
- PSF/PMF検証の一環として
- Ring 2/Ring 3申請前の持続可能性確認

## 実行内容

1. **Economic Moat 5次元評価**（0-10点）
   - Network Effects（ネットワーク効果）
   - Switching Costs（スイッチングコスト）
   - Brand & Trust（ブランド力・信頼）
   - Cost Advantages（コスト優位性）
   - Proprietary Assets（独自資産・技術）

2. **Moat Score算出**（5次元平均、0-10点）
   - 8.0-10.0: Deep Moat（後発参入極めて困難）
   - 6.0-7.9: Moderate Moat（一定の持続性あり）
   - 4.0-5.9: Shallow Moat（競合追い上げリスクあり）
   - 0.0-3.9: No Moat（持続可能性低い）

3. **持続可能性リスク評価**
   - Red Flag（高リスク）: Moat Score < 4.0
   - Orange Flag（中リスク）: Moat Score 4.0-6.0
   - Yellow Flag（低リスク）: Moat Score 6.0-8.0
   - Green（リスク小）: Moat Score 8.0以上

4. **堀強化戦略策定**
   - 弱い次元（5点未満）の改善案
   - 社内リソース活用拡大案
   - Ring 2/3通過基準達成ロードマップ

## 必要な前提条件

- `/for-recruit-validate-10x` 実行済み
- `/for-recruit-competitor-research` 実行推奨
- `/for-recruit-inventory-internal-resources` 実行推奨

## 所要時間

60-90分（自動実行）

## 出力ファイル

`Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/3_planning/competitive_moat_analysis.md`

## ForRecruit調整ポイント

- **Ring 2通過基準**: Moat Score 6.0以上、2次元で6点以上、社内リソース1種以上活用
- **Ring 3通過基準**: Moat Score 8.0以上、3次元で8点以上、社内リソース3種以上活用
- **社内リソース活用重視**: 営業網、顧客基盤、データ資産等の活用度を評価
- **リクルート成功パターン統合**: Airレジ、Geppo、SUUMO等のDeep Moat事例を参照

## 参照データ

リクルート製品研究31件から抽出した深い堀パターン:
- **Airレジ**: Moat Score 8.6（4軸で9-10点）
- **Geppo**: Moat Score 7.8（継続率98%、年次チャーン2%）
- **SUUMO**: Moat Score 8.2（ネットワーク効果10点）
- **CODE.SCORE**: Moat Score 3.2（技術優位性のみ） → 撤退

## 使用例

```bash
/for-recruit-analyze-competitive-moat
```

## 次のステップ

- Moat Score 8.0以上 → `/for-recruit-validate-pmf`
- Moat Score 6.0-7.9 → 堀強化戦略実施後 `/for-recruit-validate-pmf`
- Moat Score < 6.0 → 差別化戦略見直し、再度 `/for-recruit-validate-10x` 実施
