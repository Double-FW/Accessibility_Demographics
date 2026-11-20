---
title: "Changelog"
version: "0.3.0"
date: "2026-11-15"
status: "exploratory guidance; independent review pending"
language: "en-GB"
document_type: "guide"
---

# Changelog

## 20 November 2026 — Word report replaced with Markdown

- Replaced the root Word report with `Apparent_Disability_Proportions_UK_Report.md`, using the existing supplied transcription after comparison with the Word source.
- Preserved all report paragraphs, the four-column table with seven data rows, and all eleven external source hyperlinks. Equivalent Word fallback text-box copies are represented once.
- Added a clearly labelled editorial status note and retained the separate methodological review and unvalidated-hypothesis status.
- Updated navigation, agent guidance, source/index references, export configuration and dataset documentation to the canonical root Markdown path. Kept the old evidence-folder path as an unexported forwarding page to preserve existing links.
- The original Word file remains in Git history at source commit `986b1d13a4b0da97e91b8322065d53a4f6b9f98c`; its SHA-256 is `824fba3dc50c19ace888fdc13c62e38ed605e33468777a8a17a01490652ecd71`.
- Report document IDs/source paths in regenerated datasets now use the root Markdown path instead of the evidence-folder path. Consumers using the old path should update it; the review-pairing requirement is unchanged. No new prevalence research, source audit or licence change is claimed.

Earlier entries below describe their historical updates, including the previous decision to retain Word. They do not override this replacement.

## 0.1.0 — 14 November 2026 — prepared update

- Reframed the repository around customer reach, engagement, service quality, brand and relationship opportunity.
- Added models/definitions, demographic estimation, overlap and lifetime-value methods.
- Added research guides for geography, apparency, neurodivergence, ageing, everyday contexts and illness/distress.
- Added human and agent workflows, specialist resource routing, research prompts, templates and synthetic examples.
- Preserved the supplied Markdown report unchanged and added a separate methodological review of its unsupported aggregate estimate.
- Retained the existing MIT licence. The existing remote Word file remains untouched.

Subsequent repository observation: the framework and statistical reference were visible on main at baseline commit `9083fd9cedb1bdb561528e404fc99f36c661f8d8` when retrieved on 15 November 2026. This confirms file presence, not customer validation or that the assistant published them.

## 0.2.0 integration — 15 November 2026 — prepared update

- Connected the statistical reference to README, agent instructions, source records, topic guides, methods, prompts and evidence templates.
- Added typed observations for all 80 reference entries, preserving approximation, range, population and exclusion status; retained explicit legacy source/observation aliases.
- Migrated population-observations.json to schema 2.0: consumers must resolve legacy observation aliases and use named metrics/evidence codes rather than the former direct value/claim_type fields. The migration note in that file explains the change.
- Added stable formula/statistic navigation and removed the stale index entry for INSTALL.md, which was absent from the retrieved repository.
- Replaced outdated no-records wording with available evidence and remaining gaps; kept backlog work partially addressed where appropriate.
- Reconciled historical publication wording with the observed baseline and recorded checks in VALIDATION.md.
- Preserved the statistical reference, supplied report and MIT licence; no new prevalence research or empirical service outcomes are claimed.

Publication of this integration is pending: the connection reported no write access. The baseline above identifies the source used for preparation, not a commit containing these changes. Record the actual publication commit after upload.

## 0.3.0 quick guides — 15 November 2026 — prepared update

- Added quick-guides/ with six human-first guides and a beginner reading menu.
- Connected medical/social models, EAA functional lenses, ageing/retention, financial value, everyday barriers and neurodivergent research to practical customer decisions.
- Linked selected public Double-FW guidance, including the EAA customer-outcomes guide; retained official-law and source limitations.
- Added navigation and index entries while preserving the prepared statistics integration.
- The guide set does not add new epidemiological estimates or claim completed customer studies. Publication and independent reader evaluation remain pending.
