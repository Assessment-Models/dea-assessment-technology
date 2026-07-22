# Contributing to dea-assessment-technology

This is one of four domain-specific assessment repositories under [Assessment-Models](https://github.com/Assessment-Models):

| Domain | Repository |
|--------|-----------|
| Architecture Modernization | [dea-assessment-modernization](https://github.com/Assessment-Models/dea-assessment-modernization) |
| Technology | (this repo) |
| Operations | [dea-assessment-operations](https://github.com/Assessment-Models/dea-assessment-operations) |
| Services Delivery | [dea-assessment-services-delivery](https://github.com/Assessment-Models/dea-assessment-services-delivery) |

The umbrella index lives at [dea-catalog-assessment-tools](https://github.com/Assessment-Models/dea-catalog-assessment-tools).

## Adding questions

1. Fork this repo
2. Edit `assessments/v1-alpha/instrument.yaml`
3. Add question to an existing dimension, OR add a new dimension (4–6 total)
4. Question format: 4-point scale `[0, 1, 2, 3]` and at least one evidence item
5. Open PR — CI validates schema and dimensions count

## Versioning

- **MAJOR** — instrument dimensions fundamentally change
- **MINOR** — new dimension or question added
- **PATCH** — clarifications, corrected phrasing

## Code of Conduct

Be respectful. Argue ideas, not people.