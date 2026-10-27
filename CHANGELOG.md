1.0.0-alpha
└── initial release
    ├── Assessment instrument with 5 dimensions and 19 questions
    ├── Gap analysis template
    ├── Target state design template
    ├── Facilitator guide
    ├── Self-assessment guide
    └── GitHub Actions CI validates against instrument.schema.json
## [1.1.0-alpha] — ecosystem federation

### Added
- Root `model.yaml` contract handshake (CR-AM-11 §15): opendea-assessment-metamodel, v1.0, pinned to technehub-labs/dea-metamodel.
- Level 2 contract-conformance workflow reusing Assessment-Models/assessment-ci.
- Level 1 structural validation (`scripts/check_structure.py`) wired into CI.

### Changed
- Registered in Assessment-Models/assessment-registry as `candidate-for-migration` at v1.1.0-alpha.
