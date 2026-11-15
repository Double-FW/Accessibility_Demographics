# Weekly dataset updates

Source: https://github.com/Double-FW/Accessibility_Demographics

Destination: https://huggingface.co/datasets/GarethFW/Accessibility_and_Demographics

The destination is fixed in export-config.json. No HF_DATASET_ID variable is needed.
Save a dataset-scoped Hugging Face token as GitHub repository secret HF_TOKEN.
Create .github/workflows/huggingface-sync.yml from WORKFLOW_TO_COPY.txt in the
setup download, then run it manually and check the result. Weekly runs are
Mondays at 07:23 UTC (07:23 UK winter; 08:23 UK summer). Never commit credentials.

The source records retain evidence limits, exclusion flags and unknown values.
A changed canonical statistical reference must be reconciled with its structured
JSON hash. All approved sources are required; new or renamed documents need
review of the export configuration. Raw unmanaged Hub files are not synchronised.
