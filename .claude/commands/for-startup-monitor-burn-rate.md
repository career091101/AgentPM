# ForStartup Monitor Burn Rate Command

Invokes the `monitor-burn-rate` skill (ForStartup Edition).

## Usage

```bash
/for-startup-monitor-burn-rate
```

## Description

バーンレート（月次支出）とランウェイ（資金枯渇までの期間）を自動計算。24ヶ月ルール（ランウェイ<24ヶ月で資金調達開始）に基づく警告を発行し、資金ショートを防止します。VC投資推奨基準に準拠した資金管理を実現します。

## Parameters

None required - the skill runs autonomously.

## Output

`Flow/{YYYYMM}/{YYYY-MM-DD}/burn_rate_report_forstartup.md`

## Related Skills

- `/for-startup-validate-unit-economics` - ユニットエコノミクス検証
- `/for-startup-create-fundraising-plan` - 資金調達ロードマップ作成
- `/for-startup-build-pitch-deck` - VC向けピッチデッキ作成
