# /for-recruit-build-approval-deck

Ring段階別の社内承認用ピッチデッキを自動生成します。

## Usage

```
/for-recruit-build-approval-deck <ring_stage>
```

### Parameters

- `<ring_stage>`: Ring段階（1/2/3）
  - `1`: Ring 1（課長承認向け、10-12スライド）
  - `2`: Ring 2（部長・事業部長承認向け、15-18スライド）
  - `3`: Ring 3（役員承認向け、20-25スライド）

### Examples

```bash
# Ring 1承認デッキ生成
/for-recruit-build-approval-deck 1

# Ring 2承認デッキ生成
/for-recruit-build-approval-deck 2

# Ring 3承認デッキ生成（役員向け）
/for-recruit-build-approval-deck 3
```

## Prerequisites

以下のファイルが存在すること:

- `lean_canvas.md` (必須)
- `ring_criteria_check.md` (必須)
- `resource_inventory.md` (Ring 2以降で推奨)
- `persona.md` (推奨)
- `interview_simulation.md` (推奨)
- `competitor_research.md` (Ring 2以降で推奨)

## Output

- `documents/internal_approval/approval_deck_ring{N}.md`
- サマリーレポート（参照事例、ベンチマーク、改善提案）

## Next Steps

- PowerPoint/Keynoteに変換
- ステークホルダーへプレゼン実施
- フィードバック反映
- `/validate-ring-criteria` で承認後の検証

## Related Skills

- `/for-recruit-inventory-internal-resources` - 社内リソース棚卸し
- `/for-recruit-validate-ring-criteria` - Ring基準準拠チェック
- `/create-lean-canvas` - Lean Canvas作成
- `/validate-cpf` - CPF検証

## Reference

- Skill定義: @.claude/skills/for_recruit/build-approval-deck/SKILL.md
- Research事例: @Recruit_Product_Research/analysis/integrated_analysis_report.md
