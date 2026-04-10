# AAI-590 Capstone: Multi-Disease Outbreak Forecasting with Temporal Deep Learning

**Team:** Carrie Little, Payal Patel, Dean P. Simmer

**Course:** AAI-590 — Applied AI Capstone | University of San Diego, M.S. Applied AI

**Final Deadline:** April 13, 2026

## Overview 

This project investigates whether short-term disease incidence can be forecast at the province level in Canada using historical weekly surveillance data. We compare a clasical statistical baseline (ARIMA) with a deep learning approach (LSTM) to evaluate how well each method predicts weekly disease activity on held-out test data.

Our final project focuses on three diseases: **influenza, measles, and pertussis (whooping cough)**. Using weekly province-level case data, we build forecasting datasets, train both models, compare error metrics, and validate aggregated outputs against Public Health Agency of Canada (PHAC) reference totals. The goal is to better understand which modeling appraoch is more useful for short-term public health forecasting and how performance varies by disease.

## Research Question

Can short-term disease incidence be forecast accurately across Canadian provinces using historical weekly case counts, and does a deep learning model such as LSTM outperform a classical baseline such as ARIMA?

**Forecast horizon:** 4–8 weeks ahead

**End users:** Provincial/federal public health agencies (e.g., PHAC), epidemiologists, health system planners

## Data
This project uses Canadian infectious disease surveillance data prepared for time-series forecasting.

### Primary data source:
- **CANDID / IIDDA weekly notifiable disease data**

The **Canadian Notifiable Disease Incidence Dataset (CANDID)** contains 934,010 unique incidence records spanning 1903–2021, covering 317 diseases across 13 Canadian provinces and territories. Data is accessed via the [IIDDA REST API](https://math.mcmaster.ca/iidda/api/).

- **Paper:** Earn et al. (2024). *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- **GitHub:** https://github.com/canmod/iidda
- **Key dataset:** `canmod-cdi-normalized`

### External reference (secondary):
- **PHAC Notifiable Disease Online totals**

PHAC totals were used as a directional validation benchmark for aggregated outputs.

- **Source:** [PHAC Notifiable Disease Dataset Extraction](https://diseases.canada.ca/notifiable/extract-dataset)

### Supplementary dataset:
- **AHCCD Climate Data**

Province-level daily temperature and precipitation used to explore climate–disease correlations.

- **Source:** [Government of Canada — Adjusted and Homogenized Canadian Climate Data (AHCCD)](https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f)
- **Coverage:** 1924–2017 (full overlap of all climate variables and all three focus diseases)
- **Station counts:** 780 temperature stations, 463 precipitation stations

> **Note:** Raw climate files (~1.1 GB) are gitignored. Download from the source URL above and place in `data/raw/climate/`. Metadata files are committed.

> Climate exploration was ultimately not included in the final modeling pipeline because findings were not strong enough to justify moving forward. That work is avaiable in `notebooks/02_climate_exploration.ipynb`.

**Scope notes:**
- The final comparison highlights results from **Ontario (ON)** and **Alberta (AB)**, since these provinces provided the most consistent coverage across the targeted diseases.
- Nunavut (`CA-NU`) excluded from modeling due to very sparse data.
- PHAC totals were used as a reference for cross-validation, but they are not identical to the province-level modeling data used in this project.
- Climate data was explored as a supplementary analysis, but it was not included in the final forecasting pipeline.

## Project Highlights
- Built a province-level weekly disease forecasting workflow using Canadian surveillance data
- Compared a local ARIMA baseline against a global LSTM model
- Evaluated both models on held-out test data using RMSE and MAE
- Found that performance depended on the metric and the disease
- Used PHAC totals as an external directional validation check for aggregated model outputs

## Approach 

Our workflow follows six main steps:

1. Ingest and clean weekly disease surveillance records
2. Create province-disease time series
3. Engineer features and assign train, validation, and test windows
4. Train an ARIMA baseline and an LSTM model
5. Compare held-out test performance
6. Validate aggregated outputs against PHAC totals

### Models
- **ARIMA:** trained separately for each province-disease time series
- **LSTM:** trained globally across sequences

Because ARIMA is a local model and LSTM is a global model, results should be interpreted carefully when comparing performance directly.

## Results Summary
The final comparison showed the the two models had different strengths: 

- **ARIMA** performed better on overall RMSE
- **LSTM** performed better on overall MAE
- Performance also varied by disease rather than following one consistent pattern across all series

This suggests that model choice depends not only on the forecasting method, but also on the disease behavior and the evaluation metric being emphasized.

## Notebook Guide
The main notebooks used in the final project are:

- `00_colab_setup.ipynb`
  Sets up and verifies the project environment for Google Colab
  
- `01_data_ingestion_and_eda_fixed.ipynb`
  Loads, cleans, validates, and prepares the weekly modeling dataset
  
- `03A_V1_ARIMA_model.ipynb`
  Trains and evaluates the ARIMA baseline model
  
- `03B_V3_LSTM_model_colab.ipynb`
  Trains and evaluates the LSTM forecasting model
  
- `04_V3_Compare_models_colab_Added.ipynb`
  Compares ARIMA and LSTM results on the held-out test set and summarizes findings

- `05_V2_PHAC_Validation_and_Analysis_colab.ipynb`
  Compared aggregated model outputs against PHAC totals for cross-validation

These notebooks reflect the final modeling and evaluation workflow used in the report and presentation.

## Key Outputs

Important project outputs include:

- Final modeling dataset
- ARIMA test results and summary tables
- LSTM test metrics
- Forecast comparison tables
- Figures used in the final report and presentation
- Final paper and presentation materials

## Reproducibility

This project can be reproduced by running the notebooks in sequence, since each stage depends on outputs created earlier in the workflow. This begins with environment setup, followed by data preparation, model training, model comparison and external validation.

When running in Google Colab, some file paths may need to be adjusted to match local or Google Drive storage locations used during development. 

## Project Structure

```text

├── data/
│   ├── raw/                             # Raw source files and PHAC reference files
│   │   ├── climate/                     # AHCCD climate data for supplementary exploration
│   │   ├── phac-data.csv
│   │   └── phac-notes.txt
│   └── processed/
│       └── phac-clean.csv               # Cleaned PHAC reference data
├── models/
│   └── lstm_baseline/
│       ├── lstm_baseline_best.pt        # Best saved LSTM model weights
│       ├── lstm_baseline_config.json    # LSTM architecture and training settings
│       └── training_history.csv         # Training and validation loss history
├── notebooks/
│   ├── 00_colab_setup.ipynb
│   ├── 01_data_ingestion_and_eda_fixed.ipynb
│   ├── 02_climate_exploration.ipynb
│   ├── 03A_V1_ARIMA_model.ipynb
│   ├── 03B_V3_LSTM_model_colab.ipynb
│   ├── 04_V3_Compare_models_colab_Added Visuals.ipynb
│   └── 05_V2_PHAC_Validation_and_Analysis_colab.ipynb
├── reports/
│   ├── figures/                         # Figures used in the report and presentation
│   └── tables/                          # Saved model outputs, summaries, and validation tables
├── src/
│   └── data_loader.py                   # CANDID API ingestion utilities
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

Raw disease data is gitignored. Run `01_data_ingestion_and_eda.ipynb` once to cache locally at `data/raw/`. Then run notebooks in order.

For Colab, start with `00_colab_setup.ipynb` to mount Google Drive and clone the repo, then use the `_colab` variants of each notebook.

## References

- Earn, D. et al. (2024). CANDID: Canadian Notifiable Disease Incidence Dataset. *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- IIDDA GitHub: https://github.com/canmod/iidda
- AHCCD: Vincent, L.A. et al. Government of Canada Adjusted and Homogenized Canadian Climate Data. https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f
