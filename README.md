# RECORD LOCK — Sanitized Public Reference

[![Quality checks](https://github.com/hr185882-creator/record-lock/actions/workflows/quality.yml/badge.svg)](https://github.com/hr185882-creator/record-lock/actions/workflows/quality.yml)
[![Live product smoke test](https://github.com/hr185882-creator/record-lock/actions/workflows/live-smoke.yml/badge.svg)](https://github.com/hr185882-creator/record-lock/actions/workflows/live-smoke.yml)

A public-safe reference architecture for converting source collections into auditable analytical records with explicit provenance, claim states, competing hypotheses, confidence labels, falsifiers, and revision conditions.

- Live product: https://record-lock-platform.vercel.app/
- Version: `1.1.0`
- Portfolio: https://github.com/hr185882-creator
- Creator: Hasan Raza Kazmi

## Verified package scope

- 1 formal Draft 2020-12 JSON Schema
- 3 fictional atomic claims
- 2 fictional source records
- 2 competing hypotheses
- 1 binding constraint object
- 1 executable domain-validation suite
- 1 scheduled production smoke test
- 2 automated GitHub workflows

These counts describe the public-safe reference package, not the production corpus.

## Why this repository exists

The production deployment contains packaged research materials and internal publication controls that are not appropriate for unrestricted redistribution. This repository exposes the system design and fictional schemas without publishing licensed documents, private research notes, credentials, sensitive personal data, or production-only moderation controls.

This is a reference implementation and documentation package, not a byte-for-byte copy of the production deployment.

## Core design objective

A RECORD LOCK entry should allow another reviewer to answer:

1. What exactly is being claimed?
2. Which sources directly support it?
3. Are those sources independent?
4. What evidence contradicts or limits it?
5. What is fact, inference, forecast, speculation, or unverified reporting?
6. What confidence level is justified?
7. What would falsify or revise the judgment?
8. Who approved the record, and when?

## Repository map

- `schema/record-lock.schema.json` — machine-enforced record schema
- `tests/validate_repository.py` — domain, reference-integrity, and publication-control tests
- `docs/ARCHITECTURE.md` — analytical pipeline and release controls
- `docs/CLAIM_SCHEMA.md` — field definitions and validation requirements
- `data/example-record-lock.json` — fictional public-safe example record
- `.github/workflows/quality.yml` — schema, domain, and link validation
- `.github/workflows/live-smoke.yml` — scheduled production-endpoint verification
- `.github/workflows/dependency-review.yml` — high-severity dependency review
- `SECURITY.md` — responsible disclosure policy
- `CHANGELOG.md` — material release history
- `RELEASE_NOTES.md` — release-ready version notes
- `CITATION.cff` — citation metadata

## Analytical labels

- `fact` — directly supported by a qualifying source
- `inference` — reasoned conclusion derived from stated facts and assumptions
- `forecast` — probabilistic judgment about a future outcome
- `speculation` — possibility not sufficiently supported for analytical reliance
- `unverified_claim` — attributed assertion not independently established

## Confidence levels

- `directional` — useful signal with substantial uncertainty
- `high_confidence` — strong evidence and limited plausible alternatives
- `verified` — outcome or proposition established by the controlling record

Confidence labels describe evidentiary support, not rhetorical certainty. Every published record must include its strongest counterargument, falsifier, and revision conditions.

## Authorship and AI assistance

Hasan Raza Kazmi directs the research questions, evidence standards, analytical framework, product architecture, editorial judgment, QA, and publication decisions. AI systems may assist with coding, synthesis, formatting, or production, but do not replace source verification or final human judgment.

## Security boundary

Never commit credentials, restricted documents, personal identifiers, internal-only notes, sealed material, or unlawful content. Public examples must be fictional or based on records whose publication and representation have been independently reviewed.

## License boundary

The original reference documentation, fictional schemas, and example records may be reused with attribution. Underlying third-party documents and source materials retain their original rights and restrictions and are not redistributed through this repository.
