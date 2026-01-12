# ForStartup Build Approval Deck Command

Invokes the `build-approval-deck` skill (ForStartup Edition).

## Usage

```bash
/for-startup-build-approval-deck
```

## Description

VC承認デッキ（ピッチデッキ）を自動作成する自律実行型スキル。10-15スライド構成、データ可視化、ストーリーテリング、想定Q&A 30問を提供します。

## Parameters

None required - the skill runs autonomously and will prompt for business information if needed.

## Output

- デッキ: `Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Agent_ForStartup/documents/3_planning/vc_approval_deck.md`
- Q&A: `Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Founder_Agent_ForStartup/documents/3_planning/vc_qa.md`

## Related Skills

- `/for-startup-build-pitch-deck` - ピッチデッキ作成
- `/for-startup-prepare-vc-meeting` - VC Meeting準備
- `/for-startup-build-synergy-map` - シナジーマップ作成
