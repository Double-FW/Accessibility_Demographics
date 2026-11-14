---
title: "Estimating individual demographics"
version: "0.1.0"
date: "2026-11-14"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "guide"
---

# Estimating individual demographics

## Start with the estimand

Write the exact quantity being estimated: for example, the number of UK adult customers with a specified functional difficulty during a defined year. Decide whether the unit is a unique person, household, account, journey, interaction or relationship. Joint accounts and repeat visits need separate handling.

## Procedure

1. Define geography, age, period, condition or functional threshold, and population coverage. State whether the audience means intended market, existing customers or observed users.
2. Find an authoritative population survey or suitable research study. Administrative registrations and service use can answer narrower questions; absence from a register is not absence of need.
3. Inspect the questionnaire, denominator, sample, exclusions, uncertainty and crude versus age-standardised status. Do not use an age-standardised rate as a direct customer headcount multiplier.
4. Select estimates matching the audience. Prefer age-specific and country-specific estimates where justified. Do not transfer a children's estimate to adults or one country to the whole EU.
5. Record each finding in the [evidence record](../templates/evidence-record.md). Missing uncertainty must be labelled, not invented.
6. Calculate demographic estimates by segment and state transport assumptions. Keep estimated population membership separate from barrier exposure and commercial effect.
7. Compare with inclusive customer research. Low voluntary disclosure can reflect question design, trust or sampling; it does not establish low prevalence.
8. Review sensitivity and evidence gaps before making a decision.

## Basic model

For mutually exclusive customer segments i, estimated people = sum(N_i × p_i), where N_i is unique people and p_i is the relevant prevalence estimate. The transport assumption is that source prevalence is applicable within each customer segment. Record reasons this might fail, including product selection, income, language, geography and unequal access to the service.

If defensible source intervals are available, calculate their implications. If analysts choose low/central/high assumptions, label them scenario ranges, not confidence intervals. Do not average incompatible studies simply to obtain a midpoint.

For a temporary condition, annual incident episodes × average duration / period length can approximate average simultaneous episodes under steady-state assumptions. It is not necessarily unique people: recurrence, overlapping episodes, seasonal patterns and duration variation require investigation. Use daily prevalence or longitudinal data when available.

## Evidence hierarchy for the question

National surveys can support population scale; representative epidemiological studies can support defined conditions; administrative sources support recorded eligibility or service use; customer studies support observed experiences within their recruitment limits. None automatically answers all four questions.

For an apparently precise number, ask: what exactly was counted, who was excluded, what was the threshold and does the source support this use?

## Customer data

Use aggregate, minimum-necessary information. Offer voluntary, accessible ways to describe access needs without requiring diagnosis. Keep participant-level information in approved organisational systems. Do not turn population probabilities into individual labels or advertising audiences based on inferred health.

Output: audience definition, source records, calculation, assumptions, uncertainty, overlap treatment, decision relevance and next validation. Continue with [combined reach](combined-needs-and-reach.md).
