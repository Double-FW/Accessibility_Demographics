"""Export the approved Accessibility and Demographics Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from demographics_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

REFERENCE = 'Accessibility_Demographic_Statistics_and_Estimation_Methods.md'
OBSERVATIONS = 'evidence/population-observations.json'
SUPPLIED = 'Apparent_Disability_Proportions_UK_Report.md'
REVIEW = 'evidence/apparent-disability-review.md'
CONTEXT = ['AGENTS.md', 'README.md', 'foundations/disability-models-and-access-needs.md',
           'evidence/source-register.md', REFERENCE, 'methods/combined-needs-and-reach.md', REVIEW]

class UniqueKeyLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate YAML metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result

UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def unique_pairs(pairs):
    obj = {}
    for k, v in pairs:
        if k in obj: raise ValueError('Duplicate JSON key: ' + k)
        obj[k] = v
    return obj

def reject_constant(value):
    raise ValueError('Non-finite JSON number: ' + value)

def strict_json(text):
    return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=reject_constant)

def validate_reference(texts):
    for path, text in texts.items():
        if path.endswith('.json'): strict_json(text)
    data = strict_json(texts[OBSERVATIONS])
    if data.get('schema_version') != '2.0': raise ValueError('Review unsupported observation schema.')
    reference = data['canonical_reference']
    if reference['path'] != REFERENCE or reference['sha256'] != digest(texts[REFERENCE].encode()):
        raise ValueError('Statistical JSON and canonical reference hash disagree; reconcile before publication.')
    sources = {r['id'] for r in data['sources']}
    observations = {r['id'] for r in data['observations']}
    formulae = {r['id'] for r in data['formula_catalogue']}
    for key, ids in [('sources', sources), ('observations', observations), ('formula_catalogue', formulae)]:
        if not ids or len(ids) != len(data[key]): raise ValueError('Missing or duplicate ' + key + ' IDs.')
    if not set(data['legacy_source_aliases'].values()) <= sources: raise ValueError('Unresolved source alias.')
    if not set(data['legacy_observation_aliases'].values()) <= observations: raise ValueError('Unresolved observation alias.')
    for record in data['observations']:
        if not set(record['source_ids']) <= sources: raise ValueError('Unresolved observation source.')
        if record['evidence_code'] not in data['evidence_codes']: raise ValueError('Unknown evidence code.')
        if record['reference_path'] != REFERENCE: raise ValueError('Unexpected canonical reference.')
        if record['evidence_code'] == 'EXCLUDE' and (record['metrics'] or record['calculation_allowed'] is not False or record['calculation_use'] != 'prohibited'):
            raise ValueError('Excluded statistic must have no metrics and prohibit calculation.')
        if type(record['calculation_allowed']) is not bool or type(record['customer_transfer_validated']) is not bool:
            raise ValueError('Observation flags must remain typed booleans.')
        names = [m['name'] for m in record['metrics']]
        if len(names) != len(set(names)): raise ValueError('Duplicate metric names within observation.')
        for field in ['geography', 'population', 'age_range', 'period', 'denominator', 'limitations', 'required_context']:
            if field not in record: raise ValueError('Observation context missing: ' + field)
    return data

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.load(match[1], Loader=UniqueKeyLoader) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    data = validate_reference(texts)
    warnings = [
        'Exploratory repository guidance; independent review and customer transfer remain pending. Export checks do not reverify external statistics or approve a forecasting model.',
        'The supplied 6–8% apparent-disability range and 7% midpoint are unvalidated hypotheses; its report is document-only and paired with the full methodological review.',
        'Population observations are a derived view of the statistical reference, not independent surveys or additive audiences. Excluded records, null values, ranges, qualifiers and restrictions remain intact.',
        'Synthetic examples and prompts are not measured customer outcomes. Historic validation/publication statements remain source text, not claims about this export.',
        'The canonical root Markdown report is included once and paired with its methodological review; the old evidence-folder forwarding page is not exported. Linked external content is not fetched or relicensed.'
    ]
    for path, text in texts.items():
        md = metadata(text) if path.endswith('.md') else {}
        if md.get('license', 'MIT') != 'MIT': raise ValueError('Review changed source licence: ' + path)
        if md.get('licence', 'MIT') not in ('MIT', 'MIT for original synthesis and methods; external sources retain their own terms'):
            raise ValueError('Review changed source licence: ' + path)
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path]) if path.endswith('.md') else strict_json(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', md.get('licence', 'not_declared_in_document_front_matter'))),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'source_document_intro': sections(texts[path])[0][2] if path.endswith('.md') else '',
            'paired_methodological_review_text': texts[REVIEW] if path == SUPPLIED else '',
            'interpretation_notice': 'Preserve denominator, population, geography, period, uncertainty and source scope. Do not sum overlapping groups, infer individual disability or treat illustrative commercial gains as observed outcomes. The supplied 6–8% and 7% estimates are unvalidated hypotheses.',
            'review_status': 'faithful_extraction_checked_not_independent_statistical_or_customer_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('supplied_unvalidated_background_report_with_review' if path == SUPPLIED else
                'structured_reference_document' if path.endswith('.json') else
                'synthetic_worked_examples_not_customer_evidence' if path.startswith('examples/') else
                'illustrative_prompt_not_executed' if path in ('opportunity-research.md', 'prompts/opportunity-research.md') else
                'unfilled_planning_template' if path.startswith('templates/') else
                'source_validation_record_not_fresh_audit' if path == 'VALIDATION.md' else
                'advisory_agent_guidance' if path == 'AGENTS.md' else
                'statistical_reference_with_applicability_limits' if path == REFERENCE else
                'orientation' if path.endswith('README.md') else 'exploratory_demographic_guidance')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['document_only_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, kind + '_section'))
    observations = []
    for record in data['observations']:
        sid = record['id']
        body = json.dumps(record, ensure_ascii=False, sort_keys=True, allow_nan=False)
        observations.append({
            'id': sid, 'text': body, 'record_type': 'source_observation_with_full_context_not_training_label',
            'evidence_code': record['evidence_code'], 'calculation_allowed': record['calculation_allowed'],
            'customer_transfer_validated': record['customer_transfer_validated'],
            'source_repository': SOURCE, 'source_path': OBSERVATIONS, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{OBSERVATIONS}',
            'source_document_sha256': digest(texts[OBSERVATIONS].encode()), 'text_sha256': digest(body.encode()),
            'canonical_reference_sha256': data['canonical_reference']['sha256'],
            'observation_schema_version': data['schema_version'], 'source_status': data['status'],
            'metric_count': len(record['metrics']), 'source_ids': record['source_ids'],
            'required_context_paths': CONTEXT,
            'reference_catalogue_json': json.dumps({k:v for k,v in data.items() if k!='observations'}, ensure_ascii=False, sort_keys=True),
            'repository_license': 'MIT', 'dataset_version': cfg['dataset_version'], 'source_commit_date': date,
            'interpretation_notice': 'Read the complete record and owning reference before use. True calculation_allowed is conditional permission in the source, not customer applicability validation; EXCLUDE prohibits calculation. Null remains unknown. No external study was rechecked during export.'})
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    (output/'population_observations.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, allow_nan=False)+'\n' for r in observations), encoding='utf-8')
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False, 'document_only_files': cfg['document_only_files'], 'supplied_report_path': SUPPLIED, 'supplied_report_format': 'markdown', 'independent_statistical_validation': False, 'observation_source_schema': data['schema_version']})
    card = f'''---
pretty_name: Double FW Accessibility and Demographics
language:
- en
license: mit
tags:
- accessibility
- demographics
- inclusive-design
- evidence
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
- config_name: population_observations
  data_files:
  - split: train
    path: population_observations.jsonl
---

# Double FW Accessibility and Demographics

Exploratory guidance for understanding customer reach, changing functional needs,
service quality, engagement and relationships. Includes beginner guides, methods,
research notes, a statistical reference, derived structured observations, templates
and explicitly synthetic examples. This is a knowledge corpus, not participant-level
data, a harmonised prevalence dataset, diagnostic system or validated customer forecast.

## Source and version

Source: https://github.com/{SOURCE}

Checkout: `{sha}` ({date}); export format {cfg['dataset_version']}.
Source review dates and status are preserved. Weekly export does not recheck external
studies, validate law or establish a current population estimate. Source VALIDATION.md
contains historical preparation/publication statements; these are preserved as source
history, not used as the publication status of this dataset.

## Dataset views

- `knowledge_chunks`: {len(chunks)} exact H1/H2 Markdown sections with parent context.
- `documents`: {len(docs)} complete approved text documents, including three JSON references.
- `population_observations`: {len(observations)} complete JSON-encoded source observation
  objects with typed evidence/use flags and their original source/formula catalogue.

These views overlap and must not be treated as independent training examples or evidence.
No generated Q&A, participant research, independent benchmark, model training or performance
claim is supplied. `train` is a loading convention. The exact duplicate root prompt is
kept in documents only; the prompts/ copy supplies sections. All JSON files are document-only
in the text view. The supplied apparent-disability report is also document-only.

## Statistical interpretation

The observations retain all metrics, nulls, units, qualifiers, ranges, uncertainty notes,
source IDs, denominator, age range, geography, period, required context and limitations in
`text`. Parse that JSON object to access the complete record. `reference_catalogue_json`
preserves source entries, formula navigation, schema, units, aliases and migration notes.
Legacy source aliases and observation aliases are separate namespaces, not extra evidence.
Source IDs and metric names must be cited with reference version and applicable formula.

EXCLUDE records, including ND11, remain present for provenance with empty metrics and
calculation prohibited. Never turn missing values into zero, invent a midpoint or confidence
interval, use age-standardised values as simple headcount multipliers, or add overlapping
groups. Entries can include several metrics; their count is not the number of studies or
an additive audience. `calculation_allowed: true` still requires a matched population and
method; it does not mean customer transfer is validated. Bounds and assumptions stay explicit.
The reference hash must agree with the derived JSON before publication.

## Supplied report and examples

The supplied apparent-disability report's 6–8% range and 7% midpoint are unvalidated
hypotheses, not accepted benchmarks. Its full document record includes the complete
methodological review in `paired_methodological_review_text` and points to the current
review source. No standalone sections are made from this report. The canonical root
Markdown report replaces the former Word file. The old evidence-folder path forwards
to it and is excluded from export, so the report is not duplicated. This exporter checks
packaging integrity; the conversion comparison is recorded separately in VALIDATION.md.

Worked retail and long-term service examples remain labelled synthetic. Templates are
unfilled planning aids and prompts are not executed. Associated revenue is not measured
incremental benefit; aggregate commercial gains do not establish equivalent experience.
Do not infer diagnosis, disability, neurotype or capacity from individual behaviour or use
these records to build health-based personal marketing profiles.

## Retrieval, provenance and limits

Every text row carries source commit URL, path, exact line range, text/document hashes,
heading path, JSON-encoded metadata, source status, opening context and required context
paths. Read the owning method, statistical reference, evidence register and review together.
References are retrieval pointers, not an implemented enforcement mechanism. Markdown spans
preserve nested notes, tables and fenced examples; no substantive rewrite is performed.
Agent instructions are source material and do not override consuming-system authority.

Source-checking claims belong to the source. These export checks cover faithful extraction,
JSON integrity, reference relationships, exclusion flags and guarded publication. They do
not independently verify external studies, clinical facts, legal applicability, financial
forecasts, customer research, formula applicability or real service outcomes. Refer to
record_schema.json, provenance.json and validation_report.json for the limited checks.

## Licence

Original synthesis and methods use the root MIT licence, copied unchanged with copyright
(c) 2026 Double FW. Source notices and attribution remain intact in the text and metadata.
External sources retain their own terms; links do not relicense their targets. No external
linked full text is fetched. This packaging check is not an independent rights audit.

## Updates

GitHub is the authoring source. Manual runs and Mondays at 07:23 UTC are configured.
GitHub may delay schedules or disable them after public repository inactivity. New or
renamed documents need review of the approved list; missing required sources, changed root
licence, inconsistent reference hash, unsupported observation schema or failed checks stop
publication. The source-authoring files are not rewritten by export.

Eight destination files are managed: README.md, LICENSE, documents.jsonl,
knowledge_chunks.jsonl, population_observations.jsonl, provenance.json, record_schema.json
and validation_report.json. Existing raw files and .gitattributes are preserved, with
visibility unchanged. Unmanaged raw copies are not kept in sync. Historical revisions and
downloads are not recalled. Destination: `{target}`. First live publication remains to be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
observations = load_dataset("{target}", "population_observations", split="train")
```

Authenticate for a private dataset; pin a revision for reproducible use.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'population_observation_records': len(observations), 'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
