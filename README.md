# AAI-590 Capstone: Forecasting Canadian Infectious Disease Incidence

**Course:** AAI-590 — Applied AI Capstone | University of San Diego, M.S. Applied AI
**Dataset:** [CANDID / IIDDA](https://github.com/canmod/iidda) — Canadian Notifiable Disease Incidence Dataset

## Research Question

Can deep learning models (LSTM, Temporal Fusion Transformer) outperform classical statistical methods (ARIMA, Prophet) for forecasting seasonal infectious disease incidence at the Canadian provincial level?

## Dataset

The **Canadian Notifiable Disease Incidence Dataset (CANDID)** contains 934,010 unique incidence records spanning 1903–2021, covering 317 diseases across 13 Canadian provinces and territories. Data is accessed via the [IIDDA REST API](https://math.mcmaster.ca/iidda/api/).

- **Paper:** Earn et al. (2024). *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- **API Base URL:** `https://math.mcmaster.ca/iidda/api/`
- **Key dataset used:** `canmod-cdi-normalized`

## Project Structure

```
├── data/
│   ├── raw/               # Downloaded directly from CANDID API
│   └── processed/         # Cleaned, feature-engineered, model-ready data
├── notebooks/
│   ├── 01_data_ingestion.ipynb     # API access and raw data download
│   ├── 02_data_cleaning.ipynb      # Cleaning, filtering, handling missing values
│   ├── 03_eda.ipynb                # Exploratory data analysis and visualizations
│   ├── 04_baseline_models.ipynb    # ARIMA and Prophet baselines
│   ├── 05_lstm_model.ipynb         # LSTM deep learning model
│   ├── 06_tft_model.ipynb          # Temporal Fusion Transformer model
│   └── 07_results_comparison.ipynb # Model comparison and final evaluation
├── src/
│   ├── data_loader.py      # CANDID API ingestion utilities
│   ├── preprocessing.py    # Data cleaning and feature engineering
│   ├── evaluation.py       # Metrics: MAE, RMSE, MAPE
│   └── models/
│       ├── lstm.py         # LSTM model definition and training
│       └── tft.py          # Temporal Fusion Transformer model
└── reports/
    └── figures/            # Saved plots and visualizations for the report
```

## Methods

| Model | Type | Library |
|---|---|---|
| ARIMA | Classical statistical | statsmodels |
| Prophet | Classical statistical | prophet |
| LSTM | Deep learning (recurrent) | PyTorch |
| Temporal Fusion Transformer | Deep learning (attention) | PyTorch Forecasting |

## Setup

```bash
pip install -r requirements.txt
```

Then run notebooks in order (01 → 07) from the `notebooks/` directory.

## Key Diseases Analyzed

Focused on diseases with strong seasonal signals and multi-decade weekly records:
- **Poliomyelitis** — strong seasonal peaks (Aug–Oct, 1933–1963)
- **Whooping cough** — 1990s resurgence with pronounced geographic variation
- **Measles / Rubella** — classic epidemic cycles
- **Influenza** — modern weekly surveillance data

## Evaluation Metrics

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

## References

- Earn, D. et al. (2024). CANDID: Canadian Notifiable Disease Incidence Dataset. *PLOS Global Public Health.*
- IIDDA GitHub: https://github.com/canmod/iidda
