# Evidence and source register

Updated 15 November 2026 for statistical integration. The original conceptual sources retain their S-series identifiers. The [statistical reference](../Accessibility_Demographic_Statistics_and_Estimation_Methods.md) owns the source-checked wording, statistic IDs and formula definitions; [population-observations.json](population-observations.json) is its derived machine-readable view. Neither is a completed epidemiological review or a validated customer forecast.

## Concepts and design

| ID | Source and location | Use here | Limits |
| --- | --- | --- | --- |
| S01 | [WHO: Disability](https://www.who.int/health-topics/disability), overview | Interaction between health conditions and personal/environmental factors | Conceptual framing, not customer prevalence |
| S02 | [Scope: Social model of disability](https://www.scope.org.uk/social-model-of-disability) | Barrier-focused perspective | Conceptual explanation; not a separate demographic category |
| S03 | [W3C WAI: Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/) | Situational benefits such as sunlight or unavailable audio | Does not quantify frequency or commercial uplift |
| S08 | [W3C WAI: Older users and web accessibility](https://www.w3.org/WAI/older-users/) | Relationship between older-user needs and accessibility | Does not establish an age-specific prevalence forecast or universal usability |

The medical-model summary is an explanatory contrast with barrier-focused and interactional models. It is not a clinical taxonomy. Task/circumstance tables elsewhere are proposed research frameworks, not epidemiological claims.

## Source identity crosswalk

| Existing source ID | Canonical statistical source | Matching observation | Interpretation |
| --- | --- | --- | --- |
| S04 | D01, DWP FRS | UK01; UK02–UK07 and DR01–DR06 add detail | Same source, not separate corroboration |
| S05 | D02, Eurostat activity limitation | EU01; EU02–EU03 add age context | Same source |
| S06 | D07, CDC survey methods | Methodological source; no prevalence metric | Same source |
| S07 | D05, CDC disability summary | US01; US02–US03 add age context | Same source |

S01, S02, S03 and S08 remain conceptual source IDs. D08 is a different namespace and refers to the dyslexia factsheet, not S08. Legacy observation identifiers S04/S05/S07 map to UK01/EU01/US01 in the JSON's explicit alias map. Existing citations remain intelligible, but new calculations should use canonical source IDs plus statistic IDs and named metrics.

## Statistical source catalogue

All sources were checked for the reference on 15 November 2026. Fieldwork and publication dates are distinct. A current synthesis can rely on older studies; preserve that limit. Unknown fields remain unknown. Source listing does not approve a value for every customer population.

| ID | Source and location | Date / provenance |
| --- | --- | --- |
| D01 | [DWP, Family Resources Survey 2024–25](https://www.gov.uk/government/statistics/family-resources-survey-financial-year-2024-to-2025/family-resources-survey-financial-year-2024-to-2025), section 4, age prevalence and impairment types; table 4.6 | Published 26 March 2026; April 2024–March 2025 fieldwork |
| D02 | [Eurostat, Find out more about people with disabilities in the EU](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20251203-1), opening paragraph | 3 December 2025; 2024 data |
| D03 | [Eurostat, 80% of disabled people used the internet in 2024](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250827-1), text and methodological note | 27 August 2025; 2024 data |
| D04 | [Eurostat, Disability statistics—access to ICT](https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/134943.pdf), figure populations | 2026 article; ages 16–74; confirms age scope; retrieve original datasets before new calculations |
| D05 | [CDC, Disability and Health Data Now](https://www.cdc.gov/disability-and-health/articles-documents/disability-and-health-data-now.html), key findings | 8 April 2025; 2022 BRFSS |
| D06 | [CDC, PLACES disability measure definitions](https://www.cdc.gov/places/measure-definitions/disability.html), summary | 29 October 2024; summary of 2022 domain rates; retrieve underlying DHDS estimates for crude/adjusted status |
| D07 | [CDC, Disability datasets](https://www.cdc.gov/dhds/datasets/), survey-method comparison | 3 April 2025 |
| D08 | [British Dyslexia Association, dyslexia factsheet](https://cdn.bdadyslexia.org.uk/uploads/documents/Downloadable-Resources/British-Dyslexia-Association-Dyslexia-Factsheet.pdf), facts and figures | 2025-hosted factsheet; estimate, no single fieldwork date recorded |
| D09 | [Canadian Paediatric Society, DCD assessment/diagnosis/management](https://cps.ca/en/documents/position/developmental-coordination-disorder), opening paragraph | 2021 professional statement; school-aged estimate |
| D10 | [NHS England, ADHD MI supporting information](https://digital.nhs.uk/data-and-information/publications/statistical/mi-adhd/supporting-information), estimated prevalence methodology | Current page; NICE planning estimates; no new survey date |
| D11 | [Staley et al., adult ADHD diagnosis, MMWR](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), abstract and table 1 | 10 October 2024; October–November 2023 survey |
| D12 | [CDC, Data on ADHD in Children](https://www.cdc.gov/adhd/data/index.html), current diagnosis section | Updated 8 July 2026; 2024 NSCH |
| D13 | [Shaw et al., ADDM autism surveillance, MMWR](https://www.cdc.gov/mmwr/volumes/74/ss/ss7402a1.htm), tables 1–2 | 17 April 2025; 2022 surveillance |
| D14 | [WHO, Autism](https://www.who.int/news-room/fact-sheets/detail/Autism-spectrum-disorders), epidemiology | 2025 fact sheet; modelled 2021 global estimate |
| D15 | [Lai et al., co-occurring diagnoses in autism, Lancet Psychiatry](https://pubmed.ncbi.nlm.nih.gov/31447415/), abstract | 2019 meta-analysis; studies to February 2019; not a new national survey |
| D16 | [NHS England, APMS 2023/24 autism chapter](https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/10.-autism-spectrum-disorder), highlight and methodological correction | Current replacement for chapter withdrawn May 2026; original estimate excluded |
| D17 | [nidirect, colour vision deficiency](https://www.nidirect.gov.uk/conditions/colour-vision-deficiency-colour-blindness), types and symptoms | Current public-health summary; no fieldwork year recorded |
| D18 | [RNID, hearing loss/tinnitus/BSL prevalence](https://rnid.org.uk/what-we-do/evidence-hub/prevalence-of-hearing-loss-tinnitus-and-bsl/), age groups and calculation methods | Updated 13 November 2026; older audiometry plus population data; BSL estimate separately attributed to BDA |
| D19 | [ONS, Language, England and Wales, Census 2021](https://www.ons.gov.uk/peoplepopulationandcommunity/culturalidentity/language/bulletins/languageenglandandwales/census2021), British Sign Language section | 29 November 2022; Census 2021 |
| D20 | [RNIB, key sight-loss information and statistics](https://www.rnib.org.uk/professionals/research-and-data/key-information-and-statistics-on-sight-loss-in-the-uk/), headline sections | Current synthesis; mixed underlying dates; retrieve projection model before forecasting |
| D21 | [RNIB, complex needs and older people's services](https://www.rnib.org.uk/professionals/social-care-professionals/complex-needs-and-older-peoples-services/), older people and sensory loss | Current synthesis; underlying age-specific estimate date not recorded |
| D22 | [ONS, National population projections, 2024-based](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2024based), age structure | 2026 release; 2024 base and 2049 projection |
| D23 | [WHO, Deafness and hearing loss](https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss), overview and projections | Current fact sheet; global synthesis and 2050 projections; reference years vary |
| D24 | [NCHS, Data Brief 559, sleep, US 2024](https://www.cdc.gov/nchs/products/databriefs/db559.htm), tables 1–4 | April 2026; 2024 NHIS |
| D25 | [NHS England, APMS common mental-health conditions](https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/common-mental-health-conditions), key findings and results | 27 November 2025; March 2023–July 2024 |
| D26 | [HSE, Health and safety statistics 2025](https://www.hse.gov.uk/statistics/assets/docs/hssh2425.pdf), ill health, stress and non-fatal injuries | 2025 publication; Great Britain 2024/25; self-reported LFS estimates |
| D27 | [CDC, About common cold](https://www.cdc.gov/common-cold/about/), overview | 19 February 2026; public-health synthesis, no single survey year |
| D28 | [ONS, Drug misuse, England and Wales, YE March 2025](https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/articles/drugmisuseinenglandandwales/yearendingmarch2025), main points and age comparison | 11 December 2025; CSEW YE March 2025 |

## Evidence status and calculation routes

The reference uses OBS (published observation), EST (attributed estimate), PROJ (projection), DER (explicit derivation), ASSUMP (analyst input) and EXCLUDE (not usable for calculation). The 80 reference entries include one EXCLUDE entry; some entries contain multiple metrics. They are not 80 independent studies or mutually exclusive groups.

ND11 records the withdrawn APMS 2023/24 adult-autism prevalence estimate. Its JSON metrics are empty and calculation is prohibited. Historical provenance is retained; no valid replacement prevalence is asserted. The original apparent-disability hypothesis remains outside the approved numerical input set.

F01–F17 identify formulae in section 8 of the reference. Record the reference version, statistic ID, metric name, units, formula, input sources, derivation, uncertainty and transfer assumptions. Topic guides link the relevant routes. If the reference, JSON or an external source disagrees, flag the discrepancy before calculation and update dependent views together after correction.

## Supplied background

| ID | Material | Status and reuse |
| --- | --- | --- |
| U01 | [Apparent Disability in UK Society](supplied/Apparent_Disability_Proportions_UK_Report.md), received 14 November 2026; authorship not independently verified | Preserved unchanged. Its 6–8% range and 7% midpoint remain unvalidated hypotheses. Always pair retrieval with [the review](apparent-disability-review.md). Its external bibliography has not been audited in full. |

## Double-FW guidance

The [resource map](../resources/double-fw-resource-map.md) records eight public repository entry points and four retrieved owning guides. [Retrieval metadata](double-fw-retrieval.json) retains its original review scope and dates. Guidance supports design and research; it is not independent population or commercial-outcome evidence.

## Revision and reuse

Recheck before consequential reuse, after corrections or when scope/definitions change. Record old/new values, the reason, affected documents and actual review. Structural checks do not establish source truth, customer transfer or independent approval. Linked documents retain their own rights; repository MIT terms do not relicense them.
