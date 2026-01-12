# ForStartup Validate Ring Criteria Command

Invokes the `validate-ring-criteria` skill (ForStartup Edition).

## Usage

```bash
/for-startup-validate-ring-criteria
```

## Description

VC調達ステージ基準（Seed/Series A/Series B）を検証する自律実行型スキル。各ステージの達成要件（CPF 70%+、TAM $1B+、月次成長率20%+）をチェックします。

## Parameters

None required - the skill runs autonomously and will prompt for metrics data if needed.

## Output

`Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Agent_ForStartup/documents/5_monitoring/vc_stage_validation.md`

## Related Skills

- `/for-startup-validate-cpf` - CPF検証
- `/for-startup-validate-pmf` - PMF検証
- `/for-startup-validate-unit-economics-strict` - ユニットエコノミクス検証
