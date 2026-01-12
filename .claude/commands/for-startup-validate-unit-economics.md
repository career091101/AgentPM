# ForStartup Validate Unit Economics Command

Invokes the `validate-unit-economics` skill (ForStartup Edition).

## Usage

```bash
/for-startup-validate-unit-economics
```

## Description

PSF達成後のビジネスモデルをUnit Economics（単位経済性）で検証し、VC投資水準のスケール可能性を判定します。LTV/CAC比率5.0以上達成を目指し、比率が5.0未満の場合は改善施策を自動提案。セグメント別分析により、最適な顧客層を特定します。

## Parameters

None required - the skill runs autonomously.

## Output

`documents/2_discovery/unit_economics.md`

## Related Skills

- `/for-startup-validate-psf` - PSF達成確認（前提）
- `/for-startup-monitor-burn-rate` - バーンレート監視
- `/for-startup-measure-aarrr` - AARRR分析
- `/for-startup-create-fundraising-plan` - 資金調達ロードマップ作成
