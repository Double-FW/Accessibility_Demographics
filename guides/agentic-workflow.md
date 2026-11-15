---
title: "Human and agentic workflows"
version: "0.2.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "guide"
---

# Human and agentic workflows

## What agents can contribute

Agents can retrieve sources, compare definitions, draft evidence records, calculate declared models, identify gaps, propose service improvements and help maintain traceability. Humans remain accountable for research design, interpretation of lived experience, business decisions and authorised service changes.

## Workflow contract

| Stage | Agent contribution | Human responsibility | Output |
| --- | --- | --- | --- |
| Frame | Draft questions and missing-input list | Confirm scope and intended decision | Organisation brief |
| Retrieve | Fetch owning sources and metadata | Review source fitness | Evidence records |
| Estimate | Compute stated assumptions and bounds | Accept or revise modelling choices | Reproducible calculation |
| Explore | Suggest task/context combinations | Validate relevance with customers | Scenario records |
| Design | Retrieve specialist guidance and draft options | Decide trade-offs and implementation | Opportunity assessment |
| Evaluate | Summarise actual research and metrics | Interpret and approve conclusions | Outcome evidence |
| Maintain | Flag stale sources and dependent claims | Resolve substantive changes | Changelog and revised records |

## Retrieval rules

Use [index.json](../index.json) for navigation, then read the owning document and relevant evidence records. Keep source ID, date, denominator, uncertainty and status attached when chunking for RAG or exposing content through MCP. A snippet or an embedding match does not establish a population estimate.

Represent facts, calculations, assumptions, hypotheses and unknowns separately. Reject requests to output a unique combined total when overlap evidence is absent; provide bounds or a conditional scenario instead. Refusal to invent a number should still produce the next useful research action.

## Customer-controlled assistance

When a product supports customer agents, provide accessible semantics, clear state and authorised actions with scope limits. Distinguish read, draft and execute capabilities. Preserve customer choice, inspectability, correction and usable human support. Do not disclose private preference or health information to a service unless needed and authorised.

This repository grants no operational permission and implements no API, preference exchange, authentication or consent system. Its machine index is a retrieval aid, not executable automation.

## Response format

Return scope; evidence; calculation and assumptions; opportunity; customer benefit; financial/brand implications; limitations; next validation. Follow [AGENTS.md](../AGENTS.md) and use [the research prompts](../prompts/opportunity-research.md).

## Statistical retrieval and calculation handoff

1. Retrieve [the reference](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md), [the source register](../evidence/source-register.md) and [typed observations](../evidence/population-observations.json).
2. Select statistic ID and metric; check source/date, denominator, age, geography, standardisation, evidence status and calculation restrictions.
3. Select an identified formula. Keep formula version, inputs, units, derivation and rounding with the result.
4. Separate source uncertainty, audience-transfer assumptions, overlap assumptions and model assumptions. Return unknown where a required input is missing.
5. Ask the accountable team to assess relevance and validate service outcomes. Keep a correction trail if sources or representations disagree.

OBS, EST, PROJ and DER do not imply automatic customer applicability; EXCLUDE prohibits use. ND11 must remain blocked. The input/output contract in section 10 of the reference is the calculation handoff. S-series source aliases do not create independent corroboration, and formula identifiers are not executable tools.
