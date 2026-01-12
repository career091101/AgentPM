# ForStartup Create Fundraising Plan Command

Invokes the `create-fundraising-plan` skill (ForStartup Edition).

## Usage

```bash
/for-startup-create-fundraising-plan
```

## Description

スタートアップの資金調達ロードマップ（Pre-Seed → Seed → Series A → Series B）を自動生成する自律実行型スキル。VC投資基準に準拠した現実的な調達額・評価額の目安、各ラウンドで達成すべきマイルストーン（CPF/PSF/PMF/成長率等）、資金使途の最適配分、次のラウンドまでの期間とランウェイ設計を提供します。

## Parameters

None required - the skill runs autonomously.

## Output

`Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/fundraising_roadmap.md`

## Related Skills

- `/for-startup-validate-cpf` - CPF達成確認（Pre-Seed準備）
- `/for-startup-validate-psf` - PSF達成確認（Seed準備）
- `/for-startup-validate-pmf` - PMF達成確認（Series A準備）
- `/for-startup-build-pitch-deck` - VC向けピッチデッキ作成
- `/for-startup-validate-unit-economics` - ユニットエコノミクス検証
