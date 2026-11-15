---
title: "Combined needs and proportional reach"
version: "0.2.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "guide"
---

# Combined needs and proportional reach

## Three quantities

Measure unique people potentially benefiting, interactions exposed to a barrier, and relationships affected over time. Report the period and denominator for each. A customer with multiple needs counts once in a unique-customer total and may have many affected interactions.

## Overlap

For two groups, P(A or B) = P(A) + P(B) − P(A and B). The intersection must come from compatible evidence, not convenience. With only marginal proportions a and b, the union lies between max(a,b) and min(1,a+b), provided both describe the same population and period.

For several groups without joint data, max(p_i) ≤ P(any) ≤ min(1, sum(p_i)). These broad mathematical bounds are not a plausible interval or a forecast. Narrow them only with defensible evidence or clearly labelled assumptions.

Do not assume independence between age, disability, fatigue, medication, travel, device use or neurodevelopmental conditions. Multiplying marginal probabilities can substantially misrepresent combinations. Use joint survey microdata with appropriate analysis, longitudinal customer studies, or scenario ranges. Synthetic simulations do not create missing evidence.

## From reach to affected journeys

Define eligible unique customers; exposure to the relevant context; a barrier in that context; and the improvement's likely effect. Prefer direct joint observations of context and difficulty. A condition does not imply every encounter fails, and a successful completion can conceal excessive effort or unwanted assistance.

For journey-based analysis, potential additional completions = eligible exposed journeys × change in completion probability. Estimate the change through a suitable pilot or explicit hypothesis. Never multiply total customer population by a national disability rate and call the result lost customers.

## Illustrative overlap

Suppose 10% and 8% are assumed proportions for two relevant needs in a synthetic audience of 100,000 people. With unknown overlap, the union can be 10,000–18,000 people. This is a bound, not evidence of 14,000 affected customers. If compatible joint evidence establishes 3% in both, the union is 15%, or 15,000. Barrier exposure and commercial effect still need separate estimates.

## Compound effects

Two manageable demands may combine into a difficult journey, but do not assign an invented severity multiplier. Research realistic combinations and record task outcome, comprehension, effort, error recovery and preference. Compare circumstances for the same participant where appropriate; avoid unsafe or distress-inducing simulation.

Prioritise scenarios by service relevance, frequency evidence, customer consequence and improvement feasibility. A rare high-consequence failure can justify action without a large market-size estimate.

Use [the scenario catalogue](../research/everyday-contexts.md), [customer research](../guides/research-and-measurement.md) and [value modelling](customer-and-lifetime-value.md).

## Link combined reach to the statistical reference

Use [F04](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f04--combined-reach-and-co-occurrence) for unions, joint probabilities and bounds. A statistic such as ND10 is conditional prevalence within a defined research population; do not apply it to incompatible autism or ADHD marginals. Cite the metric as well as its row ID.

Use [F06](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f06--episode-burden-and-average-time-affected)–[F09](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f09--observed-person-time-and-interaction-exposure) for time and repeated-episode combinations. A person can have several overlapping episodes, and several contexts can affect one journey: merge relevant intervals or deduplicate journey records before counting. Use [F10](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f10--time-of-day-and-environment-weighting) where interaction timing is relevant. Modelled time prevalence is not necessarily exposure during service use.

For uncertainty, follow [F17](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#f17--uncertainty-and-scenario-propagation); broad overlap bounds are not a 95% interval. The [reference examples](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md#9-worked-customer-examples) remain assumption-based illustrations, not joint population evidence.
