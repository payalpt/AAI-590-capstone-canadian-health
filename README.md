# AAI-590 Capstone: Forecasting Canadian Infectious Disease Incidence

**Project Team** Carrie Little, Payal Patal, Dean P. Simmer
**Course:** AAI-590 — Applied AI Capstone | University of San Diego, M.S. Applied AI
**Dataset:** [CANDID / IIDDA](https://github.com/canmod/iidda) — Canadian Notifiable Disease Incidence Dataset

## Research Question (Proposed)

Can deep learning models outperform classical models for forecasting seasonal infectious disease incidence at the Canadian provincial level?

## Dataset

The **Canadian Notifiable Disease Incidence Dataset (CANDID)** contains 934,010 unique incidence records spanning 1903–2021, covering 317 diseases across 13 Canadian provinces and territories. Data is accessed via the [IIDDA REST API](https://math.mcmaster.ca/iidda/api/).

- **Paper:** Earn et al. (2024). *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- **API Base URL:** `https://math.mcmaster.ca/iidda/api/`
- **Key dataset used:** `canmod-cdi-normalized`

## Project Structure (Proposed, Most of this doesn't exist yet! We could plasibly take the single-notebook approach as well)

```
├── data/
│   ├── raw/               # Downloaded directly from CANDID API
│   └── processed/         # Cleaned, feature-engineered, model-ready data
├── notebooks/
│   ├── 01_data_ingestion.ipynb     # API access and raw data download
│   ├── 02_data_cleaning.ipynb      # Data cleaning and Feature Engineering
│   ├── 03_eda.ipynb                # EDA & Visuals
│   ├── 04_baseline_models.ipynb    # baseline classical models
│   ├── 05_lstm_model.ipynb         # LSTM model
│   ├── 06_another_model.ipynb      # placeholder for second comparison model
│   └── 07_results_comparison.ipynb # Model comparison and final evaluation
├── src/
│   ├── data_loader.py      # CANDID API ingestion utilities
│   ├── preprocessing.py    # Data cleaning and feature engineering
│   ├── evaluation.py       # Metrics: MAE, RMSE, MAPE, Others?
│   └── models/
│       ├── lstm.py         # LSTM model code (or something different)
└── reports/
    └── figures/            # Saved plots and visualizations for the report
```

## Methods

TBD

## Setup

```bash
pip install -r requirements.txt
```

Then run notebooks in order from the `notebooks/` directory.

## Key Diseases Analyzed

TBD

## Evaluation Metrics (Proposed, others prob needed)

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

## References

- Earn, D. et al. (2024). CANDID: Canadian Notifiable Disease Incidence Dataset. *PLOS Global Public Health.*
- IIDDA GitHub: https://github.com/canmod/iidda
