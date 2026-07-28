# Claim Schema

## Required top-level fields

- `record_id` — stable unique identifier
- `version` — controlled record version
- `decision_question` — precise question addressed
- `horizon` — time boundary for forecasts; null otherwise
- `sources` — source-registry entries
- `claims` — atomic claim objects
- `hypotheses` — competing explanations or outcomes
- `constraints` — binding limits and gate conditions
- `assessment` — resolved judgment, confidence, and action state
- `review` — reviewer, approval state, and timestamp
- `revision_conditions` — evidence or events that would change the record

## Claim object

Each claim should include:

- `claim_id`
- `text`
- `type`: `fact`, `inference`, `forecast`, `speculation`, or `unverified_claim`
- `state`: `supported`, `plausible`, `not_proven`, `contradicted`, or `verified`
- `source_ids`
- `contradictions`
- `assumptions`
- `evidence_ceiling`
- `independence_notes`
- `privacy_status`: `public`, `restricted`, `withhold`, or `not_applicable`

## Source object

A source entry should include source ID, title, issuer or author, publication and access dates, source class, locator, independence group, integrity notes, and rights or handling restrictions.

## Hypothesis object

A hypothesis should include an ID, statement, supporting and contradicting claim IDs, discriminating indicators, and status.

## Assessment object

The assessment should include judgment, confidence, confidence basis, strongest counterargument, falsifier, action state, and action rationale.

## Validation rules

1. Every source identifier must resolve to one registry entry.
2. A `fact` cannot rely only on an unverified source class.
3. A `verified` claim must identify the controlling record.
4. Confidence cannot be `verified` while material contradictions remain unresolved.
5. Every forecast requires a horizon and revision conditions.
6. Every published record requires a strongest counterargument and falsifier.
7. Restricted or withheld claims must not enter the public export.
8. Material edits require a version increment and revision note.
