# Stripe - Developer-First API Scorecard (Patrick Collison)

**Tier 2 Case Study for `/startup-scorecard` Skill**

---

## Summary

| Item | Value |
|------|-------|
| Founders | Patrick & John Collison |
| Company | Stripe |
| Founded | 2010 |
| Valuation | $95B (2021) |
| **Total Scorecard Score** | **43/50** ⭐⭐⭐ |

---

## Scorecard Highlights

### 1. Market (8/8) ✅
- TAM: $200B+ (Global payments)
- Developer-first positioning (vs. PayPal's merchant focus)

### 2. CPF (9/10) ⭐⭐⭐
- **CPF Score**: 82%
- Problem: Payment integration takes 2-4 weeks
- Stripe: 7 lines of code, 10 minutes

### 3. PSF (9/10) ⭐⭐⭐
**10x Advantage**:
- Integration time: 10x faster (10 min vs. 2 weeks)
- Code simplicity: 7 lines vs. 100+ lines
- Developer experience: 10x better documentation

### 4. Business Model (9/10) ⭐⭐⭐
- LTV/CAC: 8-10x (exceptional)
- Revenue model: 2.9% + $0.30 per transaction
- Gross margin: 50%+ (payment processing)

### 5. Execution (8/10) ✅
- Founders: Both engineers, MIT Dropout (Patrick)
- Domain expertise: Payment infrastructure

### 6. Uniqueness (9/10) ⭐⭐⭐
- API excellence: Best-in-class documentation
- Developer community: 10K+ developers in first year

---

## Total Score: 43/50

**VC Recommendation**: ✅ **即Series A調達推奨**

---

## Key Innovation: Developer Experience

**Before Stripe (PayPal/Authorize.Net)**:
- 100+ lines of code
- 2-4 weeks integration
- Poor documentation
- Manual merchant application

**After Stripe**:
```python
# 7 lines of code
import stripe
stripe.api_key = "sk_test_..."
charge = stripe.Charge.create(
    amount=1000,
    currency="usd",
    source="tok_visa"
)
```

**Impact**:
- Integration time: 2 weeks → 10 minutes (200x faster)
- Developer NPS: 80+ (vs. PayPal: 20)

---

## Lessons for `/startup-scorecard`

### 1. Developer Experience as 10x Axis
- Code simplicity: 7 lines vs. 100+ lines
- Documentation: Best-in-class vs. poor
- Lesson: Developer UX is a measurable 10x advantage

### 2. Bottom-Up GTM Strategy
- Developers choose Stripe → Companies adopt
- CAC: $50 (developer events, documentation)
- Lesson: Developer-led growth has exceptional LTV/CAC

### 3. API-First Product
- 100% of features accessible via API
- Self-service activation
- Lesson: API-first reduces sales friction, improves CAC

---

## Quantitative Benchmarks

**Developer NPS by Company**:
- Stripe: 80+
- Twilio: 70+
- PayPal: 20
- Lesson: Developer NPS >70 predicts strong growth

**LTV/CAC by GTM Motion**:
- Developer-led (Stripe): 8-10x
- Sales-led (Oracle): 3-5x
- Product-led (Dropbox): 5-8x

---

## References
- Source: `@Sratup_Research/documents/01_Legendary/FOUNDER_007_patrick_collison.md`
- LTV/CAC: 8-10x, Developer NPS: 80+
