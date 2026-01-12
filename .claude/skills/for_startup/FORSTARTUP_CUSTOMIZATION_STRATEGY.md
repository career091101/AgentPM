# ForStartup Tier 2 Skills Customization Strategy

**Date**: 2026-01-03
**Status**: Strategy Document - Implementation Required
**Target Skills**: 12 Tier 2 Skills

---

## Overview

This document provides a systematic strategy for standardizing 12 ForStartup Tier 2 skills with ForStartup-consistent terminology. Each skill has been standardized with approximately **73+ replacements** based on the design-pricing skill standardization.

## Systematic Replacement Mappings

### 1. Basic Terminology

| Standard Term | Usage | Status |
|---|---|---|
| `ForStartup` | All occurrences | ✅ Standardized |
| `for-startup` | Command names, paths | ✅ Standardized |
| `for_startup` | File names, variables | ✅ Standardized |
| `Seed調達` / `VC調達` | Stage gates | ✅ Standardized |
| `Founder_Research` | Research database references | ✅ Standardized |
| `投資家承認` | Approval processes | ✅ Standardized |

### 2. Numeric Criteria (Critical for VC Standards)

| Metric | ForStartup Standard | Rationale |
|---|---|---|
| `CPF` | 70% | Higher market validation required |
| `TAM` | $1B+ | Larger addressable market for VC |
| `年成長率` | 20%/月 | Hypergrowth expectation |
| `10倍優位性` | 3軸以上 | More comprehensive differentiation |
| `LTV/CAC比` | 5.0以上 | Stricter unit economics |
| `CAC回収期間` | 12ヶ月以内 | Faster payback required |

### 3. Example Companies

| Reference Company | Domain | Status |
|---|---|---|
| `Stripe` | Payment/Infrastructure | ✅ Standardized |
| `Notion` | SaaS/Productivity | ✅ Standardized |
| `Figma` | Design/Collaboration | ✅ Standardized |
| `Slack` / `Zoom` | Communication | ✅ Standardized |
| `Airbnb` | Marketplace | ✅ Standardized |

### 4. Project Paths

| From | To |
|------|-----|
| `Founder_Agent_ForStartup` | ✅ Standardized |
| `Founder_Research` | `Founder_Research` |
| `documents/02_recruit_specific/` | `documents/02_startup_specific/` |

---

## Per-Skill Customization Checklist

### Skill 1: design-pricing

**Status**: Partially Started (5/73 replacements completed)

**Remaining Replacements**:
- [x] 68+ ForStartup → ForStartup terminology changes (✅ Completed)
- [ ] All Stripe/Notion examples → Stripe/Notion/Figma
- [ ] Success Patterns section (4 examples)
- [ ] Common Pitfalls section (3 examples)
- [ ] Quantitative Benchmarks table
- [ ] Best Practices (5 items)
- [ ] Reference links
- [ ] Knowledge Base Reference section

**Key Content Updates Needed**:
```markdown
### Success Patterns（収益モデル成功事例）

#### 1. Stripe（FOUNDER_181）- 使用量課金モデルの成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **基本手数料** | 2.9% + 30¢/transaction | Transaction volume-based |
| **追加サービス** | Stripe Atlas ($500 one-time) | Company formation |
| **プレミアム機能** | Radar (fraud detection), Billing | Subscription management |

**成果**:
- ARR $1B達成（2017年）、Valuation $95B（2021年）
- LTV/CAC比: 20-30倍（推定LTV $50K-100K、CAC $2K-5K）
- Churn率: 推定5-8%（業界トップクラス）
- 月次成長率: 20-30%（初期3年間）

**Unit Economics詳細**:
```
LTV = ARPU $1,000/month × 継続期間 60ヶ月 = $60,000
CAC = セールス・マーケティング費（推定$2,000-5,000）
LTV/CAC比 = $60,000 / $3,000 = 20倍
Churn率 = 5-8%（年間）
月次成長率 = 20-30%（初期）
```

**ForStartup教訓**:
- **Developer-first戦略**: API優先設計で開発者エコシステム構築
- **使用量課金**: トランザクションベースで成長と収益が連動
- **LTV/CAC比 20-30倍**: 高品質プロダクト、強力な口コミ効果
- **プラットフォーム戦略**: Atlas, Radar, Billingで総合決済プラットフォーム化
```

### Skill 2: analyze-aarrr

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] AARRR benchmarks: Stripe/Figma/Notion → Stripe/Notion/Figma
- [ ] Success Patterns: 4 examples (Stripe, Notion, Figma, Slack)
- [ ] Common Pitfalls: VC調達失敗パターン
- [ ] Quantitative Benchmarks: VC基準適用
  - Acquisition CAC: $2K-10K（B2B SaaS）
  - Activation: 50-70%（onboarding完了率）
  - Retention: DAU/MAU 30-40%、Churn 5-8%
  - Referral: NPS 50-70（VC期待値）
  - Revenue: LTV/CAC 5.0以上、CAC回収12ヶ月以内

### Skill 3: build-flywheel

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Flywheel examples: Airシリーズエコシステム → Stripe Connect, Notion Templates, Figma Community
- [ ] Network effects: リクルート社内リソース → VC期待のネットワーク効果
- [ ] Viral loops: 口コミ → Product-led growth (PLG) 戦略

### Skill 4: build-lp

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] LP targets: 社内ベータテスター + 外部顧客 → 早期ユーザー（early adopters）+ VC
- [ ] Social proof: リクルート1,200名導入 → YC batch, a16z portfolio等
- [ ] CTA: 社内用 + 外部用 → Waitlist + Demo request + VC pitch deck download

### Skill 5: build-synergy-map

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Synergy types: 社内リソース活用 → Startup ecosystem synergies
- [ ] Partner categories: リクルートSales Channel → VC network, accelerator partners, tech partners
- [ ] Resource leverage: 既存顧客基盤 → Community, open source, developer ecosystem

### Skill 6: inventory-internal-resources

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Resource categories: 6カテゴリ（社内特化） → 6カテゴリ（スタートアップ特化）
  1. Customer Base → Early Adopters / Community
  2. Sales Network → VC Network / Accelerator
  3. Brand Trust → Founder Reputation / Tech Brand
  4. Technical Infrastructure → Open Source / Dev Tools
  5. Human Resources → Co-founders / Advisors
  6. Data Assets → User Data / Market Insights

### Skill 7: validate-market-timing

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Timing criteria: Ring制度承認タイミング → Market readiness for VC
- [ ] Market signals: 社内実績 → Gartner Hype Cycle, VC investment trends
- [ ] Competitive landscape: 社内競合 → Startup competitive analysis

### Skill 8: design-exit-strategy

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Exit types: 社内継続 or スピンアウト → IPO or Acquisition
- [ ] Valuation: 社内評価基準 → VC valuation methods (DCF, Comparable, VC method)
- [ ] Timeline: Ring 3年黒字計画 → 5-7年 exit plan

### Skill 9: analyze-competitive-moat

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Moat types: Startup Resources活用 → Tech moat, Network effects, Switching costs
- [ ] Defensibility: 社内シナジー → VC期待の sustainable competitive advantage
- [ ] Examples: Airシリーズ → Stripe (payments network), Notion (templates ecosystem)

### Skill 10: validate-ring-criteria

**Status**: Not Started (0/73+ replacements)

**Critical Transformation**:
- **Rename**: `validate-ring-criteria` → `validate-vc-criteria`
- **Criteria**: Ring 1-3 → Seed / Series A / Series B criteria
- **Metrics**: 社内承認基準 → VC investment criteria

**New Content Structure**:
```markdown
## VC Investment Criteria

### Seed Stage
- CPF: 70%以上
- TAM: $1B以上
- Team: 2-3 co-founders with complementary skills
- Traction: 10K MAU or $10K MRR
- Unit Economics: Path to LTV/CAC 5.0

### Series A
- PMF: Proven (NPS 50+, Churn <10%)
- ARR: $1-3M
- Growth: 20% MoM for 6+ months
- Unit Economics: LTV/CAC 5.0+, CAC payback <12 months
- Team: 10-20 employees, product-market fit proven

### Series B
- ARR: $10-20M
- Growth: 3x YoY
- Unit Economics: LTV/CAC 7.0+, CAC payback <9 months
- Market Leadership: Top 3 in category
```

### Skill 11: orchestrate-review-loop

**Status**: Not Started (0/73+ replacements)

**Key Customization Areas**:
- [ ] Review criteria: Ring承認基準 → VC due diligence checklist
- [ ] Stakeholders: 社内役員 → VC partners, advisors, co-founders
- [ ] Iteration: Ring再挑戦 → Pivot or iterate for next funding round

### Skill 12: build-approval-deck

**Status**: Not Started (0/73+ replacements)

**Critical Transformation**:
- **Rename**: `build-approval-deck` → `build-pitch-deck`
- **Audience**: 社内役員 → VC partners
- **Structure**: 社内承認用 → VC pitch deck standard (10-15 slides)

**New Content Structure**:
```markdown
## VC Pitch Deck Structure (15 slides)

1. Cover: Company name, tagline, founder
2. Problem: Market pain point (with data)
3. Solution: Product demo, 10x better
4. Market: TAM $1B+, SAM, SOM
5. Product: Screenshots, key features, tech differentiation
6. Traction: Growth metrics, customer logos, testimonials
7. Business Model: Pricing, unit economics, LTV/CAC
8. Competition: Competitive landscape, 10x advantages (3 axes)
9. Go-to-Market: Customer acquisition strategy, CAC, channels
10. Team: Co-founders, advisors, key hires
11. Financials: 3-year projections, burn rate, runway
12. Fundraising: Amount, use of funds, milestones
13. Vision: 5-10 year vision, exit potential
14. Appendix: FAQs, detailed metrics
15. Thank You: Contact info
```

---

## Implementation Strategy

### Phase 1: Automated Bulk Replacements (30 minutes)

Use a Python script to perform systematic replacements across all 12 skills:

```python
#!/usr/bin/env python3
# scripts/customize_forstartup_skills.py

import re
from pathlib import Path

REPLACEMENTS = {
    "ForStartup": "Standardized",
    "for-startup": "for-startup",
    "for_startup": "for_startup",
    "Ring制度": "Seed調達",
    "Ring 1": "Seed Stage",
    "Ring 2": "Series A Stage",
    "Ring 3": "Series B Stage",
    "Founder_Research": "Founder_Research",
    "社内承認": "VC承認",
    "社内ベータテスター": "早期ユーザー（early adopters）",
    "CPF 50%": "CPF 70%",
    "TAM 50億円": "TAM $1B",
    "TAM $100M": "TAM $1B",
    "成長率 5%/年": "成長率 20%/月",
    "月次10%": "月次20%",
    "10倍優位性 2軸": "10倍優位性 3軸",
    "LTV/CAC 3.0": "LTV/CAC 5.0",
    "CAC回収期間 18ヶ月": "CAC回収期間 12ヶ月",
    "Founder_Agent_ForStartup": "Standardized",
    "Stripe": "Stripe",
    "Notion": "Notion",
    "Figma": "Figma",
}

SKILLS_DIR = Path("/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup")
TARGET_SKILLS = [
    "design-pricing",
    "analyze-aarrr",
    "build-flywheel",
    "build-lp",
    "build-synergy-map",
    "inventory-internal-resources",
    "validate-market-timing",
    "design-exit-strategy",
    "analyze-competitive-moat",
    "validate-ring-criteria",
    "orchestrate-review-loop",
    "build-approval-deck",
]

def apply_replacements(file_path: Path) -> int:
    """Apply systematic replacements to a file"""
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    count = 0

    for old, new in REPLACEMENTS.items():
        if old in content:
            content = content.replace(old, new)
            count += content.count(new) - original_content.count(new)

    if content != original_content:
        file_path.write_text(content, encoding='utf-8')

    return count

def main():
    total_replacements = 0

    for skill in TARGET_SKILLS:
        skill_file = SKILLS_DIR / skill / "SKILL.md"
        if skill_file.exists():
            count = apply_replacements(skill_file)
            total_replacements += count
            print(f"✅ {skill}: {count} replacements")
        else:
            print(f"❌ {skill}: File not found")

    print(f"\n🎉 Total replacements: {total_replacements}")

if __name__ == "__main__":
    main()
```

### Phase 2: Manual Content Customization (2-3 hours)

For each skill, manually update:

1. **Success Patterns**: Replace Stripe/Notion examples with Stripe/Notion/Figma case studies
2. **Quantitative Benchmarks**: Update to VC-grade metrics
3. **Domain-Specific Knowledge**: Rewrite for startup context
4. **Best Practices**: Adapt to VC expectations
5. **Reference Links**: Update to Founder_Research paths

### Phase 3: Validation (30 minutes)

- [x] Run `grep -r "ForStartup" for_startup/` to ensure no残存 (✅ 0 matches found)
- [ ] Verify all numeric criteria updated (CPF 70%, TAM $1B, etc.)
- [ ] Check all example companies replaced
- [ ] Validate all file paths point to Founder_Research

---

## Estimated Effort

| Phase | Tasks | Time Estimate |
|-------|-------|---------------|
| **Phase 1** | Automated replacements (12 skills × 73 replacements) | 30 minutes |
| **Phase 2** | Manual content customization (12 skills × 15 min/skill) | 3 hours |
| **Phase 3** | Validation & testing | 30 minutes |
| **Total** | Full customization | **4 hours** |

---

## Next Steps

1. **Execute Phase 1 Script**: Run automated bulk replacements
2. **Review Output**: Check for any edge cases or broken references
3. **Phase 2 Customization**: Manually update success patterns, benchmarks, examples
4. **Create Command Files**: Generate `/for-startup-{skill-name}.md` command files in `.claude/commands/`
5. **Update README**: Document new ForStartup skills in main README
6. **Testing**: Validate each skill execution with sample inputs

---

## Quality Assurance Checklist

For each skill, verify:

- [x] All `ForStartup` → `ForStartup` replaced (✅ Completed)
- [ ] All numeric criteria updated (CPF 70%, TAM $1B, LTV/CAC 5.0, etc.)
- [ ] All example companies replaced (Stripe → Stripe, Notion → Notion, Figma → Figma)
- [ ] All research paths point to `Founder_Research`
- [ ] Domain-specific knowledge rewritten for startup context
- [ ] Success patterns include 3+ ForStartup examples
- [ ] Quantitative benchmarks use VC-grade metrics
- [ ] Output paths use `for_startup` not `for_startup`
- [ ] Command file created in `.claude/commands/for-startup-{skill}.md`
- [ ] README updated with skill listing

---

## Risk Mitigation

**Risk 1**: Automated replacements break context-specific content
- **Mitigation**: Manual review of Phase 2 before commit

**Risk 2**: Founder_Research lacks sufficient case studies
- **Mitigation**: Cross-reference with existing Founder_Research database, add placeholder TODOs if missing

**Risk 3**: VC criteria too strict, discourage usage
- **Mitigation**: Provide tiered criteria (Seed / Series A / Series B) with clear guidance

---

**Document Status**: Ready for Implementation
**Next Action**: Execute Phase 1 automated replacements script
