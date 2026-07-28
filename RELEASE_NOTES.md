# Release Notes

## 1.1.0 — 2026-07-28

This release upgrades the sanitized RECORD LOCK reference from documentation-only examples to an executable validation package.

### Added

- Draft 2020-12 JSON Schema for public-safe RECORD LOCK objects.
- Domain-rule tests for source and claim references, verified-state controls, hypothesis integrity, privacy eligibility, forecast horizons, counterarguments, falsifiers, and confidence constraints.
- Scheduled smoke test for the live RECORD LOCK deployment.
- CI installation of pinned-major validation dependencies.
- Standalone version marker and release-ready metadata.

### Public-safety boundary

No production source packages, restricted documents, private research notes, credentials, personal identifiers, sealed records, or production-only controls are included.

### Verification target

A valid release must pass the quality workflow and the live product smoke test before a GitHub Release is published.
