---
title: "Accessibility demographics: statistics and estimation methods"
version: "0.2.0"
date: "2026-11-15"
checked_through: "2026-11-15"
language: "en-GB"
status: "Source-checked reference; customer transfer and independent review pending"
scope: "UK, EU and US, with explicitly identified international context"
purpose: "Estimate customer reach, interaction exposure and relationship opportunity"
licence: "MIT for original synthesis and methods; external sources retain their own terms"
---

# Accessibility demographics: statistics and estimation methods

This reference helps people and authorised agents estimate how many customers may benefit from accessible services, how often changing circumstances may affect interaction, and how to investigate the value of improvements. It combines published observations, attributed planning estimates, transparent derivations and formulae. It does not present a single combined percentage of everyone who needs accessibility.

**Read a number together with its population, period, denominator, source and limitation.** An annual number of people reporting an experience, a count of episodes, average time affected and affected service interactions are different quantities.

## Contents

1. [Use and evidence status](#1-use-and-evidence-status)
2. [UK disability and functional needs](#2-uk-disability-and-functional-needs)
3. [EU disability and digital participation](#3-eu-disability-and-digital-participation)
4. [US functional disability](#4-us-functional-disability)
5. [Neurodivergence and colour perception](#5-neurodivergence-and-colour-perception)
6. [Hearing, sight and ageing](#6-hearing-sight-and-ageing)
7. [Sleep, mental health, illness, injury and transient circumstances](#7-sleep-mental-health-illness-injury-and-transient-circumstances)
8. [Formulae with rationale](#8-formulae-with-rationale)
9. [Worked customer examples](#9-worked-customer-examples)
10. [Agent input and output contract](#10-agent-input-and-output-contract)
11. [Research gaps and service implications](#11-research-gaps-and-service-implications)
12. [Sources and revision record](#12-sources-and-revision-record)

## 1. Use and evidence status

| Code | Meaning | Permitted use |
| --- | --- | --- |
| OBS | Published survey, census or surveillance observation | Context or matched-population calculation, subject to methods |
| EST | Attributed estimate or published synthesis | Planning scenario with limitations; not an exact census count |
| PROJ | Published projection | Conditional future scenario, retaining assumptions |
| DER | Calculation from identified inputs | Show formula, rounding and inherited uncertainty |
| ASSUMP | Analyst-selected input | Sensitivity analysis; never describe as a finding |
| EXCLUDE | Withdrawn or unsupported for this purpose | Explain why; do not use as a multiplier |

Unless an interval is explicitly shown, **this reference has not extracted a confidence interval**. That does not mean the estimate is certain or that the source lacks one. Do not manufacture a confidence interval from a rounded percentage. Ranges such as 3–4% may be published planning ranges rather than statistical intervals.

The source list gives titles, links, dates where established and relevant sections. All sources were checked on 15 November 2026. Fieldwork dates appear beside the figures; undated synthesis pages must not be treated as new surveys conducted in 2026. A population estimate becomes a customer estimate only after assessing how well its population matches the actual audience.

Do not add country percentages or use them as a country league table. Do not infer an individual's disability, diagnosis, intoxication or decision-making capacity from a population probability, appearance, device setting or interaction pattern. Accessibility opportunities include people who do not identify as disabled.

## 2. UK disability and functional needs

**Source [D01]: FRS 2024–25, UK private households; rounded, non-age-standardised estimates.** Working-age and pension-age follow FRS definitions, not a universal age-65 boundary. Functional categories overlap. OBS throughout this table.

| ID | Population / measure | Figure |
| --- | --- | --- |
| UK01 | All people: disability | 25%; 16.7 million |
| UK02 | Children: disability | 12% |
| UK03 | Working-age: disability | 23% |
| UK04 | Pension-age: disability | 45% |
| UK05 | Disabled children: social/behavioural; learning; mental-health impairments | 61%; 32%; 26% |
| UK06 | Disabled working-age: mental-health; mobility; stamina/breathing/fatigue impairments | 46%; 40%; 33% |
| UK07 | Disabled pension-age: mobility; stamina/breathing/fatigue; dexterity impairments | 68%; 45%; 34% |

UK05–UK07 use **disabled people within the age group**, not everyone, as denominator. For a whole-age-group estimate, apply F03 below. No row measures apparency or identifies diagnosis-specific autism, dyslexia or ADHD prevalence. Household coverage excludes some communal settings.

### Derived whole-group planning proportions

These DER figures multiply rounded source rates; display about one decimal place in ordinary communication. They inherit the survey's scope and need customer-transfer assessment.

| ID | Population and functional category | Calculation | Approximate proportion |
| --- | --- | --- | --- |
| DR01 | Working-age, source-defined disabled with mental-health impairment | 0.23 × 0.46 | 10.6% |
| DR02 | Working-age, source-defined disabled with mobility impairment | 0.23 × 0.40 | 9.2% |
| DR03 | Working-age, source-defined disabled with stamina/breathing/fatigue impairment | 0.23 × 0.33 | 7.6% |
| DR04 | Pension-age, source-defined disabled with mobility impairment | 0.45 × 0.68 | 30.6% |
| DR05 | Pension-age, source-defined disabled with stamina/breathing/fatigue impairment | 0.45 × 0.45 | 20.3% |
| DR06 | Pension-age, source-defined disabled with dexterity impairment | 0.45 × 0.34 | 15.3% |

These are joint disability-and-impairment estimates. People outside the survey's disability classification can also experience functional difficulty. Do not label DR01 as prevalence of all mental-health conditions, or sum DR01–DR06.

## 3. EU disability and digital participation

### Population context

Source [D02], 2024, EU people aged 16+ reporting activity limitation. OBS; a different construct from FRS and US functional questions.

| ID | Age group | Figure |
| --- | --- | --- |
| EU01 | 16+ | 23.9% |
| EU02 | 16–24 | 7.1% |
| EU03 | 85+ | 72.3% |

Retrieve EU-SILC scope, underlying tables and uncertainty before demographic modelling. These summary figures do not provide an apparent-disability measure or a breakdown by medical condition.

### Digital participation context

Source [D03], EU, 2024. Its companion article specifies ages **16–74** [D04]; do not extend these figures to everyone aged 75+. OBS. Disability is self-reported activity limitation lasting at least six months.

| ID | Measure | Severe limitation | Moderate limitation | No limitation |
| --- | --- | --- | --- | --- |
| EU04 | Internet use in previous 12 months | 82.3% | 89.0% | 95.2% |
| EU05 | Internet banking in previous 3 months | 51.0% | 59.6% | 69.3% |

The internet-use gap is 12.9 percentage points, not a 12.9% relative difference. The companion article confirms the three-month banking period; retain the population base when retrieving dataset dsb_ictiu03. Differences can reflect multiple influences; they are not causal estimates of exclusion by inaccessible design or recoverable sales.

## 4. US functional disability

Source [D05]: 2022 BRFSS adults 18+, civilian non-institutionalised survey population. OBS summary estimates, not direct equivalents of UK/EU figures. [D06] supplies the domain percentages and definitions; confirm crude versus age-adjusted selections in underlying DHDS data before a headcount calculation.

| ID | Measure / population | Figure | Source |
| --- | --- | --- | --- |
| US01 | Any functional disability, adults | 28.7%; about 70 million | D05 |
| US02 | Any functional disability, ages 18–44 | 23.6% | D05 |
| US03 | Any functional disability, ages 65+ | 43.9% | D05 |
| US04 | Cognition: serious difficulty concentrating, remembering or deciding | 13.9% | D06 |
| US05 | Mobility: serious walking/stair difficulty | 12.2% | D06 |
| US06 | Independent living: difficulty with errands alone | 7.7% | D06 |
| US07 | Hearing: deafness or serious difficulty | 6.2% | D06 |
| US08 | Vision: blindness or serious difficulty despite glasses | 5.5% | D06 |
| US09 | Self-care: dressing/bathing difficulty | 3.6% | D06 |

Domain percentages use all adults as denominator and overlap. They do not mean the same thing as the proportion with any degree of hearing loss, any motor limitation or a diagnosis. Use [D07] to understand differences between ACS and BRFSS; method differences can produce substantially different estimates even with similar questions.

## 5. Neurodivergence and colour perception

There is no defensible combined total obtained by adding these rows. ADD is historical terminology: preserve source labels but do not count it separately from the relevant ADHD construct. AuDHD describes the autism–ADHD intersection, not an additional disjoint group. Colour vision deficiency is included as a perceptual difference, without assigning it the same clinical classification.

| ID | Population and construct | Estimate | Evidence and restriction |
| --- | --- | --- | --- |
| ND01 | UK population, dyslexia | Around 10% | EST, British Dyslexia Association [D08]; synthesis without a fieldwork year or CI in this record. Planning starting point, not exact diagnosed count. |
| ND02 | School-aged children, DCD/dyspraxia | 5–6% | EST, Canadian Paediatric Society, 2021 [D09]; professional synthesis, not UK/EU/US adult prevalence. No adult default multiplier. |
| ND03 | UK adults, ADHD | 3–4% | EST, NICE estimate reported by NHS England [D10]; no single fieldwork year or CI. Age-specific evidence is preferable. |
| ND04 | Children/young people, ADHD | Around 5% | EST, NICE estimate reported by NHS England [D10]; planning methodology, not a newly measured UK census. |
| ND05 | US adults 18+, current ADHD diagnosis, self-report | 6.0%; 95% CI 5.3–6.8%; 15.5 million | OBS, October–November 2023 Rapid Surveys System [D11], table 1. Diagnosed prevalence is not all underlying ADHD. |
| ND06 | US children 3–17, current ADHD diagnosis reported by parents | 11.7%; about 7 million | OBS, 2024 NSCH, summarised by CDC in July 2026 [D12]. Do not substitute older ever-diagnosed figures. |
| ND07 | Autism identified among 8-year-olds in 16 US surveillance sites | 32.2 per 1,000 = 3.22%; observed 95% CI 3.16–3.29% | OBS, 2022 ADDM [D13], table 1. Not all US children, adults or a representative global sample. |
| ND08 | Same surveillance population, boys / girls | 49.2 / 14.3 per 1,000 = 4.92% / 1.43% | OBS, 2022 [D13], table 2; source sex categories, site selection and ascertainment apply. |
| ND09 | Global population, autism | About 1 in 127, approximately 0.79% | EST, WHO reporting modelled 2021 prevalence [D14]; contextual only, not a substitute for national or age-specific evidence. |
| ND10 | People with autism in international studies, co-occurring ADHD | 28%; pooled 95% CI 25–32% | EST, 2019 meta-analysis [D15], studies through February 2019; substantial heterogeneity. Not a national population rate or default for every autistic cohort. |
| ND11 | England adult-autism prevalence from original APMS 2023/24 chapter | Do not use the original 0.9% estimate | EXCLUDE: NHS England says the estimate should not be used and the corrected chapter presents no prevalence estimate [D16]. |
| CV01 | Red–green colour vision deficiency, men / women in source terminology | About 1 in 12 / 1 in 200 = 8.33% / 0.50% | EST, UK public-health information [D17]; no survey year or CI supplied. Applicability varies; do not transfer indiscriminately between populations. |

NHS England's ADHD planning method uses 5% at ages 0–24 and 3.5% at 25+ [D10]. That age split is an administrative planning convention; it does not mean adulthood begins at 25 or every young adult's prevalence is known to be 5%. If using that method, reproduce and label it rather than silently blending it with other definitions.

The ADDM observed confidence interval does not describe uncertainty about transfer to an adult customer base. The same paper's Bayesian credible interval is a different statistical object; do not swap interval types without explanation.

For colour vision deficiency, source categories reflect the evidence's inheritance/population framing. Do not assign an individual biological category from their name or gender identity. If aggregate data are missing or unsuitable, use a declared audience-mix sensitivity scenario rather than collect unnecessary personal information.

Do not forecast future neurodivergent prevalence by extrapolating increases in diagnosis, referrals or educational provision. Recognition, criteria, access and recording can change. Use F12 for explicitly conditional population-composition scenarios.

## 6. Hearing, sight and ageing

### UK hearing

Source [D18], RNID page updated 13 November 2026. EST based on older audiometry combined with population data/projections; not a new 2026 survey. Hearing-loss definition includes average threshold of at least 25 dB in either ear. No intervals extracted.

| ID | Population / construct | Estimate |
| --- | --- | --- |
| HE01 | UK, hearing loss | Over 17 million |
| HE02 | UK, deaf/hearing loss/tinnitus union | Over 18 million |
| HE03 | Hearing loss, people over 40 / over 50 / over 60 / aged 70+ | 45% / 55% / 65% / almost 80% |
| HE04 | Working-age, some hearing loss | About 9 million |
| HE05 | Hearing difficulty with most conversational speech | About 2.4 million |

HE03 age thresholds overlap: do not sum them. Support needs cannot be assigned from audiometric thresholds alone. HE02 is broader than hearing loss. These numbers do not imply visible disability or sign-language preference.

### Sign-language counts and estimates

| ID | Population and measure | Figure | Interpretation |
| --- | --- | --- | --- |
| SL01 | England and Wales usual residents aged 3+, BSL main language, Census 2021 | 22,000; 0.04% | OBS [D19]. Main language, not everyone able to use BSL; not a UK adult percentage. |
| SL02 | UK BSL users, broad estimate | 151,000, including 87,000 deaf users | EST, BDA estimate reported by RNID [D18]; underlying estimate date not established here. Competing definitions yield different totals. |

### UK sight loss

Source [D20], RNIB synthesis accessed in 2026; underlying estimates span different dates. EST, no intervals extracted. Check underlying dataset dates for a business model.

| ID | Construct | Estimate |
| --- | --- | --- |
| VI01 | UK, sight loss significantly affecting daily life | More than 2 million |
| VI02 | UK, long-term irreversible sight loss | More than 1 million |
| VI03 | UK, registered sight impaired/severely sight impaired | Around 320,000 |
| VI04 | UK, people starting to lose sight | Around 250 per day |
| VI05 | Share of people with sight loss aged 65+ | Nearly 80% |
| VI06 | UK sight loss by 2050 | Over 4 million, PROJ |
| VI07 | UK people aged 75+, sight loss | About 1 in 5, EST [D21] |

VI05 is **P(age 65+ given sight loss)**, not **P(sight loss given age 65+)**. VI07 answers an age-specific prevalence question. VI03 is not all sight loss. VI04 is an approximate flow, not a net increase after deaths or recovery.

### Population ageing and global hearing context

| ID | Population / period | Observation or projection | Source |
| --- | --- | --- | --- |
| AG01 | UK age 85+, mid-2024 | 1.75 million; 2.5% of population, OBS | D22 |
| AG02 | UK age 85+, mid-2049 | 3.6 million; 4.9%, PROJ | D22 |
| GH01 | World, disabling hearing loss, WHO current synthesis | Around 430 million; over 5%, EST | D23 |
| GH02 | World, older than 60, disabling hearing loss | Over 25%, EST | D23 |
| GH03 | World, any hearing loss / rehabilitation need by 2050 | Nearly 2.5 billion / over 700 million, PROJ | D23 |

ONS projections are conditional on demographic assumptions. WHO's disabling-hearing threshold is greater than 35 dB in the better ear; it differs from RNID's broader hearing measure. Global estimates are context, not customer multipliers for the UK, EU or US.

## 7. Sleep, mental health, illness, injury and transient circumstances

### Sleep and capacity context

Source [D24], US NHIS 2024, civilian non-institutionalised adults 18+; published April 2026. OBS. Short sleep means averaging less than seven hours per 24 hours. Difficulty and well-rested measures refer to most days/every day.

| ID | Measure / age | Percentage; 95% CI where shown |
| --- | --- | --- |
| ST01 | Short sleep, all adults | 30.5%; 29.8–31.1 |
| ST02 | Short sleep, 18–34 | 27.2%; 26.0–28.5 |
| ST03 | Short sleep, 35–49 | 33.4%; 32.1–34.8 |
| ST04 | Short sleep, 50–64 | 34.5%; 33.2–35.9 |
| ST05 | Short sleep, 65+ | 27.2%; 26.2–28.3 |
| ST06 | Trouble falling asleep, adults | 15.4%; 14.9–15.9 |
| ST07 | Trouble staying asleep, adults | 18.1%; 17.6–18.6 |
| ST08 | Waking well-rested, adults | 54.8%; 54.1–55.6 |

Sleep reports are not direct measurements of cognitive impairment, fatigue prevalence at checkout, or reduced capacity at a particular hour. They do not establish that all people perform worse at the start/end of the day. Use task-specific diary or repeated-measures evidence for that question.

### Mental health and distress context

Source [D25], England APMS, March 2023–July 2024, private-household adults 16+. OBS assessed common mental-health conditions in the past week. CI below refers to the indicated group, not all adults.

| ID | Population / construct | Figure |
| --- | --- | --- |
| MH01 | All adults, any assessed common mental-health condition | 20.2% |
| MH02 | Ages 16–64, same construct | 22.6%; 95% CI 21.0–24.3% |
| MH03 | Ages 16–24 / 75+ | 25.8% / 10.2% |
| MH04 | People with problem debt / without problem debt | 39.0% / 18.4% |
| MH05 | Limiting physical-health condition / no limiting physical-health condition | 32.9% / 12.6% |

Associations support service-specific investigation, not causal claims, individual labels or a common multiplier for grief, stress, trauma and mental-health conditions. Do not equate these measures with impaired decision-making capacity.

### Injury, illness and episode frequency

| ID | Population / period / measure | Figure | Evidence and limits |
| --- | --- | --- | --- |
| TR01 | Great Britain workers, work-related ill health, 2024/25 | 1.9 million | OBS, HSE self-report LFS [D26]; includes new and longstanding conditions; not all illness. |
| TR02 | Same scope, work-related stress/depression/anxiety | 964,000 | OBS [D26]; subset, not extra to TR01. |
| TR03 | Same scope, musculoskeletal disorders | 511,000 | OBS [D26]; not all motor difficulty. |
| TR04 | Great Britain workers, non-fatal workplace injury, 2024/25 | 680,000 | OBS, LFS [D26]; workers, not a complete injury-episode incidence count. |
| TR05 | Work-related ill health/injury, working days lost, 2024/25 | 40.1 million | OBS [D26]; work absence days, not all days of functional difficulty. |
| TR06 | Work-related stress/depression/anxiety, working days lost, 2024/25 | 22.1 million | OBS [D26]; subset of absence burden. |
| TR07 | US adults, typical annual common-cold frequency | Average 2–3 episodes per year | EST, CDC public-health summary [D27]; not 2–3 unique people or a population point-prevalence percentage. |
| TR08 | England/Wales, ages 16–59, any illicit drug use in past year, YE March 2025 | 8.7% | OBS, CSEW [D28]; any use, not intoxication during service use. |
| TR09 | Same source, ages 16–24 / 25–59 | 15.1% / 7.3% | OBS [D28]; no duration or functional-effect estimate follows. |

None of these sources establishes a universal percentage of customers temporarily impaired at any moment. Work-related conditions can be long-term; illness/injury can overlap disability. Drug-use prevalence cannot be converted into time impaired without additional episode, effect and duration evidence.

For alcohol, prescription medicines, emotional trauma, bereavement, dimmed screens, muted audio, occupied hands and unsafe travel contexts, use the explicit local measurement approach below. A medicine can improve function; taking one is not evidence of impairment. Voice interaction alone does not make a task appropriate while driving.

## 8. Formulae with rationale

### Common notation and units

Use probabilities as decimals: 23% = 0.23. N is unique eligible customers; J is eligible journeys; p is a probability in a defined population/window; E is episode count; λ is episodes per person per stated time unit; d is effective duration in the same time unit; T is observation-window length. Declare whether time means calendar days, waking hours or scheduled working days. Keep people, accounts, households and visits separate.

### F01 — Basic audience estimate

`estimated_people = N × p`

**Rationale:** scales a relevant prevalence to a defined customer population. It assumes the source rate transports to those customers. Product selection, income, geography, age and prior exclusion can violate that assumption. Round the output to reflect evidence quality; do not treat it as a list of identified people.

### F02 — Demographic weighting

`estimated_people = Σ_i (N_i × p_i)`

`weighted_prevalence = estimated_people / Σ_i N_i`

**Rationale:** matches rates to mutually exclusive age/geography/other justified segments instead of applying a national average blindly. Missing strata remain unknown or use declared sensitivity assumptions. Age-standardised rates are unsuitable as direct headcount multipliers.

For colour perception: `N_m × (1/12) + N_f × (1/200)` is a **conditional planning scenario** using CV01, only where source categories and audience applicability are justified. Do not assume an unknown audience is equally split; if an equal split is chosen for illustration, the implied rate is about 4.42%, not a new measured statistic.

### F03 — Conditional proportions and denominator correction

`P(disabled AND impairment) = P(disabled) × P(impairment | disabled)`

`estimated_people = N × P(disabled) × P(impairment | disabled)`

**Rationale:** prevents treating the percentage of disabled respondents with a particular impairment as a percentage of all customers. Match ages, geography and period. This gives the intersection, not every person with that functional difficulty.

For a reverse conditional, Bayes' identity is:

`P(need | age_group) = P(age_group | need) × P(need) / P(age_group)`

Use only compatible inputs; otherwise leave the reverse conditional unknown. This explains why VI05 cannot simply be used as an older-customer prevalence rate.

### F04 — Combined reach and co-occurrence

`P(A OR B) = P(A) + P(B) − P(A AND B)`

`P(A AND B) = P(A) × P(B | A)`

With only marginals: `max(pA, pB) ≤ P(A OR B) ≤ min(1, pA+pB)`.

For several groups: `max(p_i) ≤ P(any) ≤ min(1, Σ p_i)`.

**Rationale:** counts people once. Bounds are mathematical limits, not a forecast or confidence interval. Never assume independence between conditions, age, fatigue, context or medication without justification. ND10 can illustrate conditional modelling, but its heterogeneous pooled rate is not automatically suitable for a national autistic customer cohort. Do not add AuDHD again after counting autism and ADHD.

### F05 — Recover disjoint age bands from cumulative thresholds

`affected_in_younger_band = N_above_lower × p_above_lower − N_above_upper × p_above_upper`

`p_younger_band = affected_in_younger_band / (N_above_lower − N_above_upper)`

**Rationale:** HE03 thresholds are nested. A rate for over-40s minus a rate for over-50s is not the prevalence among 41–50-year-olds. Counts, not percentages, must be subtracted. Use source-population counts for the same thresholds and period, then transfer the derived band rate to customers. Do not substitute a different customer age distribution into national cumulative rates. Approximation and rounding may produce inconsistent results; prefer original disjoint-age data.

### F06 — Episode burden and average time affected

`episode_rate = E / person_time_observed`

`expected_episode_days_per_person_year = λ_year × d_days`

`average_concurrent_episodes = annual_episode_count × d_days / 365`

For rare, non-overlapping, steady episodes:

`approx_time_fraction_affected = λ_year × d_days / 365`

**Rationale:** converts a flow of episodes into average occupied time, analogous to stock-flow accounting. Use effective task-relevant duration, not automatically the clinical illness duration. Recurrence, overlapping episodes, seasonality and changing incidence affect the result. The concurrent-episode result is episodes, not necessarily unique people. A result above one signals episode intensity or overlap, not over 100% of people affected.

### F07 — Probability of an active episode under a stated model

If episode starts follow a stationary Poisson process and duration is independent of start timing:

`P(active at a random time) = 1 − exp(−λ × mean_duration)`

Use matching units. With λ per year and d in days: `1 − exp(−λ_year × d_days/365)`.

**Rationale:** handles overlapping active episodes under this particular model. It is a conditional model result, not measured prevalence. Persistent individual differences, seasonal clustering and illness-driven changes in service use can invalidate transfer. Record why the model is suitable or use observed person-time instead.

### F08 — People with an episode during a window

Under a homogeneous Poisson model:

`P(at least one new episode starting in T) = 1 − exp(−λ × T)`

`expected_people_with_new_episode = N × [1 − exp(−λ × T)]`

**Rationale:** separates unique people from episode counts. It counts starts during the window; people already affected when it begins are not included unless the model is extended. Do not derive an event rate from annual affected workers such as TR04 without recurrence evidence.

### F09 — Observed person-time and interaction exposure

`time_fraction = total person-time in the union of relevant states / total observed eligible person-time`

`journey_exposure = exposed eligible journeys / all observed eligible journeys`

`potentially_affected_journeys = J × P(relevant state/context | eligible journey)`

**Rationale:** a service's users may interact more, less or at different times while affected. Random-time prevalence is not necessarily the probability during service use. Merge overlapping intervals within each person before summing time; deduplicate journeys when contexts overlap. Use appropriately governed diaries, optional surveys or observations; missing context is not proof of no exposure.

### F10 — Time-of-day and environment weighting

`overall_journey_exposure = Σ_h [J_h × p(context or relevant difficulty | journey in h)] / Σ_h J_h`

**Rationale:** weights by when actual journeys occur. Use measured within-period probabilities, not an invented morning/evening capacity curve. Hourly segments must be disjoint; state the time zone and account for shift work where relevant. For one-handed use, muted audio, glare or low brightness, measure both occurrence and whether it creates a barrier in the task.

### F11 — Service-specific selection

`estimated_people_in_need = N_service × P(need | service audience)`

For a journey: `affected_journeys = J_service × P(barrier | service journey)`.

**Rationale:** healthcare, bereavement, justice or support services can attract circumstances unlike a national average. Use service evidence or relevant studies. If transferring a general rate, show it as an assumption and test sensitivity. Do not invent a standard bereavement multiplier, or multiply deaths by a universal number of grieving customers. A death can generate several service tasks and affect overlapping families/accounts.

### F12 — Future audience composition

`estimated_people_at_t = Σ_i [projected_N_i,t × assumed_p_i,t]`

**Rationale:** makes demographic composition and prevalence assumptions explicit. Constant p produces a demographic scenario, not a forecast of changing underlying prevalence. For existing relationships, national population ageing is not customer survival: model cohort ageing, acquisition, exits and changing needs separately. Do not extrapolate diagnosis growth as if it were underlying prevalence growth.

### F13 — Changes over time

`percentage_point_change = 100 × (p_new − p_old)`

`relative_change = (p_new / p_old − 1) × 100%`, if `p_old > 0`.

`ratio = p_new / p_old`

**Rationale:** a change from 20% to 25% is 5 percentage points and 25% relative growth. Compare only compatible questions/populations/periods and evaluate uncertainty; descriptive change is not proof of causality or future trend. A prevalence ratio between age groups is not an individual's probability of becoming disabled.

### F14 — Existing business associated with an audience

`associated_revenue = Σ_i [N_i × p_i × average_revenue_per_customer_i]`

**Rationale:** estimates existing business under a within-segment spend assumption. It is not lost revenue, recoverable opportunity or an incremental benefit. Condition-related spend differences and shared accounts need explicit handling. Use contribution instead of revenue for a margin analysis. Do not count loan principal, deposits or pension assets as revenue.

### F15 — Additional completion and commercial value

`additional_completions = eligible_exposed_journeys × absolute_change_in_success_probability`

`incremental_revenue = additional_purchases × average_transaction_value`

`incremental_net_contribution = incremental_revenue × contribution_margin − incremental_delivery_support_costs − implementation_and_maintenance_costs`

**Rationale:** connects a particular barrier and improvement to a plausible outcome. Define exposed journeys without double-counting. Do not apply the same uplift again to a demographic subset already included. A two-percentage-point increase is 0.02, not a relative 2% multiplier. Completion of a useful task need not create a purchase; measure customer benefit separately.

### F16 — Retained relationship value

`incremental_PV = Σ_t [(S_improved,t × m_improved,t − S_baseline,t × m_baseline,t − incremental_cost_t)/(1+r)^t] − initial_cost`

S is probability a relationship remains active at t; m is contribution conditional on activity; r is the stated discount rate. Multiply by cohort size when the terms are per relationship.

**Rationale:** reflects long-term mortgages, pensions and subscriptions. Define horizon, continuation, transitions, costs and attribution. Avoid adding a separate retention total to lifetime value if lifetime value already includes it. Report trust, autonomy and successful participation alongside money.

### F17 — Uncertainty and scenario propagation

For fixed N and a suitable published interval `[p_low, p_high]`:

`conditional_estimated_count_interval = [N × p_low, N × p_high]`.

**Rationale:** carries uncertainty in the population rate through a simple calculation. It is not an exact prediction interval for a particular customer base and excludes transfer error. For multiple dependent inputs, do not multiply confidence endpoints and label the result a new 95% CI. Use a stated statistical model with covariance/design information, or label outputs low/central/high assumption scenarios. Keep sampling uncertainty, transport uncertainty and analyst assumptions separate.

## 9. Worked customer examples

All customer counts, audience mixes, durations and commercial effects below are **illustrative assumptions**, not observed customer research. Published rates remain subject to their stated limits.

### A. Working-age customer mix

Assume 100,000 UK working-age customers match the FRS population. UK03 suggests about 23,000 source-defined disabled customers. DR02 suggests about 9,200 source-defined disabled customers reporting mobility impairment. They are nested groups: the total is not 32,200. Neither count establishes failure in a digital journey.

### B. Colour perception

Assume a 100,000-person audience with 60,000 and 40,000 people in categories compatible with CV01, and assume its rates transfer. F02 gives `60,000/12 + 40,000/200 = 5,200`. This is an estimated potentially relevant audience. Investigate colour-dependent tasks; do not describe 5,200 people as excluded customers or known diagnoses.

### C. Common-cold episodes and task-relevant days

TR07 supplies an average 2–3 episodes per adult per year. **Assume**, for illustration, three days per episode during which a particular task would benefit from lower effort. This is not a sourced duration of cognitive impairment.

F06 gives 6–9 effective episode-days per person-year, or about 1.64–2.47% of calendar time under a rare/non-overlap approximation. For 100,000 adults, that is roughly 1,640–2,470 concurrent episode-equivalents on an average day. The stationary Poisson F07 estimate of people with an active relevant episode is approximately 1,630–2,440 instead.

Do not apply these rates to winter days, specific checkout hours or a different country without further assumptions. People may defer or increase digital interactions when unwell; F09 measures what matters to the service.

### D. A measured contextual barrier

Assume 50,000 eligible journeys, with a suitable local study estimating 20% occur one-handed; 30% of those encounter a particular control barrier. Then `50,000 × 0.20 × 0.30 = 3,000` barrier-exposed journeys, assuming the estimates apply jointly as stated. If the conditional 30% came from a different population, investigate before multiplying.

Suppose an improvement increases purchase probability in those journeys by an assumed 0.02: 60 additional purchases. At £50 per purchase and 30% contribution margin, that is £3,000 revenue and £900 contribution **before** implementation, maintenance and additional service costs. Wider customer benefit can be worthwhile even when this isolated financial scenario is small.

### E. Combining known and unknown overlap

For an illustrative audience with pA=0.10 and pB=0.08, the union is between 0.10 and 0.18 without joint evidence. If compatible evidence establishes pAB=0.03, the union is 0.15. Never select 0.14 just because it is the midpoint of the bounds, or add an overlapping transient group without modelling its intersection.

## 10. Agent input and output contract

### Inputs required before a numerical estimate

Record customer unit, count, geography, age bands, period, journey, relevant functional construct, source ID and date, source definition, uncertainty status, transfer rationale, overlap evidence and any timing/duration assumptions. Counts and rates must refer to compatible populations; percentages must be converted to probabilities exactly once.

Use an unknown field rather than invent a value. Numerical fields must be typed, with explicit units. Keep source records attached to all retrieved chunks or generated summaries.

### Example calculation record

```json
{
  "calculation_id": "EXAMPLE-COLOUR-01",
  "status": "illustrative scenario; not measured customer prevalence",
  "target": {
    "unit": "unique customers",
    "geography": "UK",
    "period": "organisation-defined annual customer base",
    "age_range": "adult; transfer must be justified"
  },
  "source_ids": ["CV01", "D17"],
  "formula_id": "F02",
  "inputs": {
    "N_source_compatible_m": 60000,
    "N_source_compatible_f": 40000,
    "p_m": 0.08333333333333333,
    "p_f": 0.005
  },
  "result": {"expected_people": 5200},
  "uncertainty": {
    "source_interval": null,
    "transfer_validated": false,
    "audience_mix": "assumed",
    "interpretation": "planning scenario, not a confidence interval"
  },
  "not_estimated": ["barrier exposure", "incremental revenue"],
  "next_validation": "Check audience applicability and test colour-dependent tasks"
}
```

### Required outputs

1. State the question and whether the result concerns people, time, interactions or relationships.
2. Identify source observation versus estimate, assumption, derivation or projection.
3. Show the formula, inputs, units, rounding and source IDs.
4. Explain overlap treatment and limits on transfer.
5. Separate potential audience, barrier exposure and improvement effect.
6. Report source uncertainty separately from scenarios and unresolved gaps.
7. Explain customer outcomes and the next useful validation; do not manufacture a business case when commercial inputs are missing.

### Calculation checks

- N, J, E and durations must be non-negative; probabilities must lie in [0,1].
- Customer strata must be mutually exclusive for F02; timestamps/windows must align for F09/F10.
- A joint proportion must satisfy `max(0,pA+pB−1) ≤ pAB ≤ min(pA,pB)`.
- Named cumulative age groups are nested; never add HE03 thresholds.
- Fractions of active time must not exceed one; episode-days can exceed available days because of overlap, but then are not unique affected time.
- Changes in success probabilities must keep both baseline and improved probabilities in [0,1].
- Do not substitute a global rate or school-age estimate for a missing national adult estimate without labelling a separate, justified transfer scenario.
- Do not use withdrawn ND11 or the supplied 6–8% apparent-disability hypothesis as validated customer benchmarks.
- Sources may be corrected. Recheck the owning source before consequential reuse, and preserve the historical version supporting an earlier decision.

## 11. Research gaps and service implications

| Topic | What this reference can support | What remains local or unknown |
| --- | --- | --- |
| Apparent/non-apparent disability | Define context and inspect the supplied report's methodological review | No validated common UK/EU/US apparency proportion; cannot calculate hidden disability by subtraction |
| Adult dyspraxia and national neurodivergent totals | Use condition-specific evidence and overlap methods | Do not transfer school-age DCD or add overlapping diagnoses into a total |
| Age-related motor/cognitive needs | FRS/US functional evidence and age weighting | Detailed age-specific customer-task estimates; clinical diagnosis is not an interaction outcome |
| Bereavement/trauma/justice/healthcare | Service-selected recruitment, task demand and support planning | No universal prevalence or duration of grief, reduced capacity or required support |
| Alcohol/medicines/recreational drugs | Explicit exposure/effect/duration models, where suitable evidence exists | Taking a substance is not the probability of impairment in a customer journey |
| Time of day/fatigue | Sleep context plus repeated observations and F10 | No universal start/end-of-day capacity curve |
| Glare, low brightness, muted audio, occupied hands | Measure task exposure and preference using F09/F10 | No adopted general population rate applicable to every service |
| Long-term relationships | F12/F16, cohort evidence and changing needs | Population projections alone do not predict a customer's future condition or retention |

### From numbers to an opportunity

Choose an actual customer activity and identify the information, interaction and service-policy demands. Establish whether customers can discover the offer, understand choices, complete the task, receive the outcome and return later. Estimate relevant audience scale, then investigate barriers and preferences directly.

For service improvement, use the repository's [service optimisation guide](https://github.com/Double-FW/Accessibility_Demographics/blob/main/guides/service-optimisation.md) and [Double-FW resource map](https://github.com/Double-FW/Accessibility_Demographics/blob/main/resources/double-fw-resource-map.md). These connect cognitive task continuity, accessible typography, branding/CX, inclusive research, email and QA. Implement recurring lessons in accessible UX design systems, branding systems, content practice and service operations.

Measure understanding, effort, confidence, autonomy, task success, chosen support and continued use alongside financial outcomes. National prevalence is an opportunity signal, not proof that a particular change creates revenue. Small groups and essential services can justify improvement through customer benefit even where a revenue estimate is unavailable.

## 12. Sources and revision record

All links checked 15 November 2026. Statistics above are concise summaries; original methodology, limitations and reuse terms govern further interpretation. Publication/review year below is not always the fieldwork year.

| ID | Source and location | Date / provenance |
| --- | --- | --- |
| D01 | [DWP, Family Resources Survey 2024–25][D01], section 4, age prevalence and impairment types; table 4.6 | Published 26 March 2026; April 2024–March 2025 fieldwork |
| D02 | [Eurostat, Find out more about people with disabilities in the EU][D02], opening paragraph | 3 December 2025; 2024 data |
| D03 | [Eurostat, 80% of disabled people used the internet in 2024][D03], text and methodological note | 27 August 2025; 2024 data |
| D04 | [Eurostat, Disability statistics—access to ICT][D04], figure populations | 2026 article; ages 16–74; confirms age scope; retrieve original datasets before new calculations |
| D05 | [CDC, Disability and Health Data Now][D05], key findings | 8 April 2025; 2022 BRFSS |
| D06 | [CDC, PLACES disability measure definitions][D06], summary | 29 October 2024; summary of 2022 domain rates; retrieve underlying DHDS estimates for crude/adjusted status |
| D07 | [CDC, Disability datasets][D07], survey-method comparison | 3 April 2025 |
| D08 | [British Dyslexia Association, dyslexia factsheet][D08], facts and figures | 2025-hosted factsheet; estimate, no single fieldwork date recorded |
| D09 | [Canadian Paediatric Society, DCD assessment/diagnosis/management][D09], opening paragraph | 2021 professional statement; school-aged estimate |
| D10 | [NHS England, ADHD MI supporting information][D10], estimated prevalence methodology | Current page; NICE planning estimates; no new survey date |
| D11 | [Staley et al., adult ADHD diagnosis, MMWR][D11], abstract and table 1 | 10 October 2024; October–November 2023 survey |
| D12 | [CDC, Data on ADHD in Children][D12], current diagnosis section | Updated 8 July 2026; 2024 NSCH |
| D13 | [Shaw et al., ADDM autism surveillance, MMWR][D13], tables 1–2 | 17 April 2025; 2022 surveillance |
| D14 | [WHO, Autism][D14], epidemiology | 2025 fact sheet; modelled 2021 global estimate |
| D15 | [Lai et al., co-occurring diagnoses in autism, Lancet Psychiatry][D15], abstract | 2019 meta-analysis; studies to February 2019; not a new national survey |
| D16 | [NHS England, APMS 2023/24 autism chapter][D16], highlight and methodological correction | Current replacement for chapter withdrawn May 2026; original estimate excluded |
| D17 | [nidirect, colour vision deficiency][D17], types and symptoms | Current public-health summary; no fieldwork year recorded |
| D18 | [RNID, hearing loss/tinnitus/BSL prevalence][D18], age groups and calculation methods | Updated 13 November 2026; older audiometry plus population data; BSL estimate separately attributed to BDA |
| D19 | [ONS, Language, England and Wales, Census 2021][D19], British Sign Language section | 29 November 2022; Census 2021 |
| D20 | [RNIB, key sight-loss information and statistics][D20], headline sections | Current synthesis; mixed underlying dates; retrieve projection model before forecasting |
| D21 | [RNIB, complex needs and older people's services][D21], older people and sensory loss | Current synthesis; underlying age-specific estimate date not recorded |
| D22 | [ONS, National population projections, 2024-based][D22], age structure | 2026 release; 2024 base and 2049 projection |
| D23 | [WHO, Deafness and hearing loss][D23], overview and projections | Current fact sheet; global synthesis and 2050 projections; reference years vary |
| D24 | [NCHS, Data Brief 559, sleep, US 2024][D24], tables 1–4 | April 2026; 2024 NHIS |
| D25 | [NHS England, APMS common mental-health conditions][D25], key findings and results | 27 November 2025; March 2023–July 2024 |
| D26 | [HSE, Health and safety statistics 2025][D26], ill health, stress and non-fatal injuries | 2025 publication; Great Britain 2024/25; self-reported LFS estimates |
| D27 | [CDC, About common cold][D27], overview | 19 February 2026; public-health synthesis, no single survey year |
| D28 | [ONS, Drug misuse, England and Wales, YE March 2025][D28], main points and age comparison | 11 December 2025; CSEW YE March 2025 |

### Revision and maintenance

Version 0.2.0, 15 November 2026: first standalone statistical reference and calculation guide. Source checks include an explicit exclusion of the withdrawn APMS autism estimate. This file supplements the earlier repository framework; it does not silently replace its historical evidence records. Original text/formula explanations use the repository MIT licence; third-party data and documents retain their own terms.

For repository integration, place this file at the repository root and link it from README.md and index.json. Log the actual publication commit in CHANGELOG.md after upload. Publication is not implied by preparation of this file.

[D01]: https://www.gov.uk/government/statistics/family-resources-survey-financial-year-2024-to-2025/family-resources-survey-financial-year-2024-to-2025
[D02]: https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20251203-1
[D03]: https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250827-1
[D04]: https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/134943.pdf
[D05]: https://www.cdc.gov/disability-and-health/articles-documents/disability-and-health-data-now.html
[D06]: https://www.cdc.gov/places/measure-definitions/disability.html
[D07]: https://www.cdc.gov/dhds/datasets/
[D08]: https://cdn.bdadyslexia.org.uk/uploads/documents/Downloadable-Resources/British-Dyslexia-Association-Dyslexia-Factsheet.pdf
[D09]: https://cps.ca/en/documents/position/developmental-coordination-disorder
[D10]: https://digital.nhs.uk/data-and-information/publications/statistical/mi-adhd/supporting-information
[D11]: https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm
[D12]: https://www.cdc.gov/adhd/data/index.html
[D13]: https://www.cdc.gov/mmwr/volumes/74/ss/ss7402a1.htm
[D14]: https://www.who.int/news-room/fact-sheets/detail/Autism-spectrum-disorders
[D15]: https://pubmed.ncbi.nlm.nih.gov/31447415/
[D16]: https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/10.-autism-spectrum-disorder
[D17]: https://www.nidirect.gov.uk/conditions/colour-vision-deficiency-colour-blindness
[D18]: https://rnid.org.uk/what-we-do/evidence-hub/prevalence-of-hearing-loss-tinnitus-and-bsl/
[D19]: https://www.ons.gov.uk/peoplepopulationandcommunity/culturalidentity/language/bulletins/languageenglandandwales/census2021
[D20]: https://www.rnib.org.uk/professionals/research-and-data/key-information-and-statistics-on-sight-loss-in-the-uk/
[D21]: https://www.rnib.org.uk/professionals/social-care-professionals/complex-needs-and-older-peoples-services/
[D22]: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2024based
[D23]: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss
[D24]: https://www.cdc.gov/nchs/products/databriefs/db559.htm
[D25]: https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/common-mental-health-conditions
[D26]: https://www.hse.gov.uk/statistics/assets/docs/hssh2425.pdf
[D27]: https://www.cdc.gov/common-cold/about/
[D28]: https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/articles/drugmisuseinenglandandwales/yearendingmarch2025
