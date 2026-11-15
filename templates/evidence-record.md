---
title: "Evidence record template"
version: "0.2.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "template"
---

# Evidence record template

Use one record per bounded claim, not one record for an entire topic. Unknown fields must remain unknown.

| Field | Required content |
| --- | --- |
| Evidence ID and version | Stable local identifier; revision |
| Statistic ID and metric | Reference row ID plus metric name when a row has several measures |
| Source identity and aliases | Canonical D-series ID where available; preserve legacy S-series alias mapping |
| Formula identity | F-series ID, owning reference version and anchor; or not applicable |
| Reference evidence code | OBS / EST / PROJ / DER / ASSUMP / EXCLUDE; retain underlying meaning |
| Withdrawal/supersession | Active / contextual / excluded / superseded, reason, date and replacement if valid |
| Claim and status | Fact / source estimate / calculation / assumption / hypothesis / unknown |
| Source | Author, title, full URL, publication and retrieval dates |
| Location in source | Table, page, section or dataset query |
| Population | Geography, age, coverage and exclusions |
| Definition | Exact construct, functional threshold and source terminology |
| Unit and denominator | People, episodes, households, journeys; base population |
| Period | Fieldwork/measurement year; not just publication year |
| Estimate and uncertainty | Value, interval if supplied, method and missing uncertainty |
| Methods | Sampling, weighting, crude/standardised and study design |
| Comparability and overlap | What can be combined or compared and why |
| Derivation | Inputs, formula, source IDs and rounding |
| Transfer to customers | Assumptions and selection effects |
| Limitations | Known bias and unanswered questions |
| Rights and reuse | Source terms; no blanket MIT assumption |
| Dependencies | Documents and decisions using the claim |
| Review | Reviewer/status, checked date and recheck trigger |

Read [the source register](../evidence/source-register.md). Presence in a register records provenance, not automatic endorsement.

## Statistical reference use

Use [the statistical reference](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md) and [machine-readable observations](../evidence/population-observations.json) as starting records. Preserve a null value when unknown; never convert it to zero. Record whether an estimate is approximate, a lower bound, a planning range or a confidence interval. An excluded record is retained for provenance and must not become an input. Source-checking is separate from audience-transfer review and empirical validation.
