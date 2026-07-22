# Self-Assessment Guide — Technology Assessment

How to self-administer the technology assessment without a facilitator.

---

## When to self-assess

- Initial baseline scan
- Annual health check
- Quarterly tech radar preparation
- Pre-engagement readiness check

---

## Setup (30 minutes)

1. Pull the latest `instrument.yaml` from this repo
2. Identify one person per dimension:
   - **Stack Fitness** — Platform Engineering Lead
   - **Technical Debt** — Engineering Manager
   - **Lifecycle** — Platform Engineering Lead
   - **Skill Coverage** — People Manager / Engineering Manager
   - **Tooling Integration** — Platform Engineering Lead
3. Send instrument to each scorer
4. Agree a deadline (typically 1 week)

---

## Scoring

For each question:
1. Read the question
2. Read the evidence list
3. Score 0–3 based on evidence present
4. Cite evidence for scores of 2+

---

## Aggregation

For each dimension:
- Sum question scores (max = questions × 3)
- Compute `(sum / max) × 100`

For overall score:
- Multiply each dimension score by its weight
- Sum weighted scores

---

## Output

Fill in `gap-analysis-template.md` with scores, gaps, and quick wins.

---

## Follow-up

- **Within 30 days:** publish results
- **Within 90 days:** re-run assessment
- **Track trend** — more important than absolute score

---

## Tips for accurate technology scoring

1. **Be honest about ATL adherence.** Most organisations score 1 here.
2. **Quantify debt if possible.** "Lots of debt" scores 0. "$2.3M quantified debt" scores 2.
3. **Skill SPoFs are everywhere.** Even small teams. Score 0 if not formally addressed.
4. **Lifecycle maturity is binary.** Either you track it or you don't.

---

## When to escalate to a facilitated workshop

- Score < 50
- Significant organisational change
- Board-level reporting
- Conflict between scorers

---

## Related

- `gap-analysis-template.md`
- `target-state-template.md`
- `instrument.yaml`