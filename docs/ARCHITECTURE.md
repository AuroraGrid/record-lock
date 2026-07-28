# Architecture

## System purpose

RECORD LOCK transforms a decision question and its source record into a reproducible analytical object. The system preserves what was known, which assumptions were used, how alternatives were tested, what confidence was assigned, and what evidence would change the judgment.

```mermaid
flowchart LR
  A[Decision question] --> B[Source intake]
  B --> C[Provenance map]
  C --> D[Atomic claims]
  D --> E[Fact and inference separation]
  E --> F[Competing hypotheses]
  F --> G[Constraints and falsifiers]
  G --> H[Confidence and action state]
  H --> I[Human review and release gate]
  I --> J[Immutable record version]
  J --> K[Revision event]
  K --> D
```

## Components

- **Decision-question registry:** exact question, owner, horizon, scope, exclusions, and required evidence.
- **Source registry:** identifiers, issuer, dates, source class, independence, rights constraints, and integrity notes.
- **Claim ledger:** atomic claims with type, state, supporting sources, contradictions, assumptions, and evidence ceiling.
- **Competing-hypothesis layer:** strongest plausible alternatives and discriminating observations.
- **Constraint and trigger map:** binding constraints, gate states, activation triggers, and blocking conditions.
- **Confidence and action router:** separates analytical confidence from recommended action.
- **Record versioning:** stable identifiers, versions, and dated revision reasons.

## Integrity model

A valid record preserves source identity and provenance, the exact proposition, supporting and contradicting evidence, assumptions, alternatives, confidence basis, falsifiers, revision conditions, reviewer identity, approval time, and the relationship between conclusion and action.

## Public versus restricted data

Production systems should maintain separate stores for restricted source files, internal research notes, public-safe metadata, reviewed claims, public exports, credentials, and correction evidence. Only approved public fields should enter a public build artifact.

## Release gate

1. Decision question is precise and time-bounded.
2. Source provenance and independence are assessed.
3. Claims are atomic and correctly typed.
4. Facts and inferences are separated.
5. Strongest competing hypothesis is represented.
6. Binding constraint and falsifier are explicit.
7. Confidence is supported by the record.
8. Action state is separated from confidence.
9. Privacy, security, and rights checks pass.
10. Automated validation and human review pass.
