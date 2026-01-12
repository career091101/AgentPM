# merriman-weekly-outlook

MMA（Merriman Market Analyst）週次レポートから金融占星術（Geocosmic）分析を自動抽出し、構造化されたMarkdownレポートを生成。

## Usage

```bash
/merriman-weekly-outlook [URL]
```

## Parameters

- **URL** (optional): MMA週次レポートのURL
  - 未指定の場合: 最新週のレポートを自動取得
  - 指定した場合: 指定URLからレポート抽出

## Examples

```bash
# 最新週のレポートを取得
/merriman-weekly-outlook

# 特定週のレポートを取得
/merriman-weekly-outlook https://www.mmacycles.com/free-weekly-forecast/mma-free-weekly-column-for-the-week-beginning-january-5-2025/
```

## Output

- **ファイル**: `Stock/programs/資産運用/projects/Merriman Financial Astrology Analysis/analysis/weekly/weekly_outlook_YYYY-MM-DD.md`
- **内容**:
  - 重要天体配置イベント（日付・影響度）
  - CRD（Critical Reversal Dates）リスト
  - 市場別見通し（DJIA, Nasdaq, Gold, Silver, Bitcoin）
  - 長期サイクル展望（Saturn-Neptune等）
  - トレード戦略への統合方法

## Execution Time

2-5分（自動実行）

## Related Skills

- `/trading-phase1-analysts` - TradingAgents Phase1（Geocosmic Analystとして統合可能）
- `/trading-agents` - TradingAgents全フェーズ実行

## See Also

- Skill Documentation: `.claude/skills/merriman-weekly-outlook/SKILL.md`
- MMA Official Site: https://www.mmacycles.com/
- Knowledge Base: `Stock/programs/資産運用/projects/Merriman Financial Astrology Analysis/knowledge/`
