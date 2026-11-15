---
title: "Customer value and long-term relationships"
version: "0.2.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "guide"
---

# Customer value and long-term relationships

## Separate the value questions

| Quantity | What it means | What it does not prove |
| --- | --- | --- |
| Existing associated revenue | Revenue from a defensibly estimated audience | Revenue currently lost or recoverable |
| Additional conversion | Purchases enabled by an improvement | That all disabled customers were previously excluded |
| Retained contribution | Expected future contribution preserved through continued use | Guaranteed lifetime revenue |
| Service-cost change | Change in avoidable rework and support cost | That reducing access to support is beneficial |
| Customer and brand outcomes | Understanding, trust, autonomy, preference and recommendation | A monetary return without an evidenced relationship |

## Existing audience

Segment counts by relevant demographics and customer relationship. Apply compatible prevalence estimates using [the estimation method](estimating-demographics.md). Where cohort revenue is unknown, a proportional allocation assumes similar spend; label it and test sensitivity. Do not infer disability from transaction patterns. Accounts, people, households and assets under management are not interchangeable units.

For colour vision deficiency, a population estimate may be available while customer-specific barrier exposure is unknown. A colour-only chart can affect some tasks; redundant cues can help. Neither prevalence nor fixing one chart establishes additional sales.

## Incremental value

Additional transaction revenue = eligible affected journeys × incremental conversion probability × average transaction value, using matching periods and populations. Net contribution deducts variable delivery costs, implementation, research, maintenance and any extra support. Keep customer acquisition, existing-customer conversion and retention cohorts distinct to avoid counting the same benefit twice.

## Long-term relationships

For mortgages, pensions, subscriptions and financial services, use a cohort model over a stated horizon. Track acquisition, continuation, renewal, transfers, product changes, bereavement and exit. Compare current and improved journeys across life stages and changing needs.

Expected incremental net value = sum over t of [(S_improved,t × m_improved,t) − (S_baseline,t × m_baseline,t) − incremental_cost_t] / (1+r)^t, minus initial investment. S is probability of an active relationship; m is expected contribution conditional on activity; r is the chosen discount rate. Record every source or assumption. Do not treat mortgage principal, pension assets or deposits as revenue.

Use local finance definitions and organisation-approved assumptions. Model changing needs with longitudinal or transition evidence where available. Without it, compare explicit future scenarios; do not assert everyone becomes disabled by a particular age.

## Interpretation

Low, central and high scenarios should vary evidenced uncertainties and named assumptions, not arbitrary optimism. Show the break-even improvement, major cost drivers, attribution limits and outcomes that remain worthwhile without monetisation. Include customer effort, trust and equitable participation alongside financial value.

See [synthetic examples](../examples/retail-and-long-term-services.md) and [measurement](../guides/research-and-measurement.md).

## Calculation references and provenance

Use [F14](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f14--existing-business-associated-with-an-audience) for existing associated business, [F15](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f15--additional-completion-and-commercial-value) for additional completion/contribution and [F16](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f16--retained-relationship-value) for retained relationship value. These definitions own the formula IDs; the explanations above provide application context. Use [F02](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f02--demographic-weighting) for customer-demographic inputs and [F12](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f12--future-audience-composition) only for explicit future-composition assumptions.

Trace every estimate from statistic ID and metric through audience transfer, barrier exposure and improvement effect. None of the statistical reference's prevalence records measures a universal conversion uplift or customer value. If spend, costs, continuation or effect sizes are missing, keep the financial result unknown or show a labelled scenario. Do not apply both a retention uplift and a lifetime-value uplift to the same benefit twice.
