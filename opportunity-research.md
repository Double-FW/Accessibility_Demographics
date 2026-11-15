---
title: "Prompts for accessibility opportunity research"
version: "0.2.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "research prompts"
---

# Prompts for accessibility opportunity research

## Organisation assessment prompt

Use the following prompt with this repository available for retrieval.

> Assess how accessibility and inclusive design could improve customer reach, engagement, successful participation and sustained relationships for the organisation below. Follow AGENTS.md and retrieve the owning methods before calculating.
>
> Inputs: organisation and brand purpose; products/services; markets and jurisdictions; intended and existing audience; customer demographics; channels; key journeys; relationship duration; available research, analytics and financial data. Ask only for missing information that materially changes the analysis; otherwise state conditional assumptions.
>
> Consider long-term and fluctuating disability, apparent and non-apparent needs, neurodivergence and perceptual differences, ageing, illness/injury, distress, environment, task circumstances and preferences. Investigate combinations relevant to the actual service without assuming diagnostic characteristics apply to every individual.
>
> Separate unique people, affected interactions and relationships. Estimate demographics using compatible sources and explicit denominators. Do not add overlapping populations. Show joint evidence, bounds or scenarios, and distinguish source intervals from analyst assumptions. Leave unsupported values unknown.
>
> For each priority journey, identify evidence of barriers, customer consequence, likely improvements, relevant public Double-FW guidance, customer outcomes, financial/brand hypotheses and validation needed. Retrieve actual owning guidance before attributing a recommendation to it.
>
> Distinguish existing associated business, additional conversion, retained contribution and service-cost change. Include understanding, effort, trust, autonomy and preference without forcing monetary values. Show low/central/high scenarios only where assumptions are explicit; do not infer causality from correlation.
>
> Return: scope and missing inputs; evidence table; audience estimates and calculations; prioritised opportunities; implementation dependencies; customer research plan; measurement plan; limitations and next decisions. This is opportunity analysis, not a regulatory-risk report. Do not fabricate research, diagnoses, forecasts or ROI.

## Individual demographic prompt

> Investigate [demographic/functional need] in [geography], [age group], [period], for [decision]. Define the estimand and source terminology. Search authoritative surveys and relevant original research. Separate diagnosis, functional difficulty, identity, registration and service use. Record full source provenance, population coverage, threshold, uncertainty, exclusions and comparability. Assess overlap and whether estimates transfer to the customer audience. Return a defensible range only if evidence supports it; otherwise provide bounds or an evidence-development plan. Do not fill missing countries or age bands by unsupported extrapolation.

## Service improvement prompt

> Examine [journey] for [audience/context]. Use the five dimensions in foundations/objectives-and-scope.md. Map barriers across discovery, comprehension, interaction, fulfilment, support and exit. Retrieve relevant public Double-FW source guidance through resources/double-fw-resource-map.md. Propose changes to UX design systems, brand systems, content and service operations. For each, give the source/revision, barrier, intended customer benefit, alternatives, dependencies and validation. Preserve customer choice and do not infer diagnosis from behaviour.

## Evidence challenge prompt

> Review this opportunity assessment critically. Check denominators, age bands, geography, periods, source definitions, overlap, selection effects, projection assumptions, customer/account distinctions, revenue versus contribution, and double-counted benefits. Identify unsupported causal claims and universal design claims. Recalculate supplied examples. Separate correctable errors from research gaps; preserve uncertainty and provide concrete next actions.

## Statistics integration instruction

Add this instruction to the assessment, demographic and evidence-review prompts above:

> Retrieve Accessibility_Demographic_Statistics_and_Estimation_Methods.md, evidence/source-register.md and evidence/population-observations.json. Cite statistic IDs, named metrics, canonical source IDs and formula IDs in calculations. Use the source crosswalk for S-series aliases; do not count aliases as independent evidence. Keep OBS/EST/PROJ/DER/ASSUMP/EXCLUDE distinct and never calculate from EXCLUDE records, including ND11. Check population, geography, age, recall period, units, standardisation and customer transfer before using a value. A planning range is not a confidence interval. Use F04 for overlap, F06–F10 for transient exposure, F12 for conditional composition and F14–F17 for value and uncertainty where applicable. Return the formula/version, inputs, derivation, rounding, assumptions, result meaning and next validation. Do not infer missing effect sizes, durations or customer behaviour from prevalence. If required data are absent or representations conflict, state the gap and continue with the supported analysis.

This instruction supplements the task-specific questions; it does not convert national estimates into approved organisational inputs.
