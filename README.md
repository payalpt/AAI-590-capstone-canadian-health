# AAI-590 Capstone: Multi-Disease Outbreak Forecasting with Temporal Deep Learning

**Project Team:** Carrie Little, Payal Patal, Dean P. Simmer
**Course:** AAI-590 — Applied AI Capstone | University of San Diego, M.S. Applied AI
**Final Deadline:** April 13, 2026

## Research Question

> Can we accurately forecast short-term disease incidence (4–8 weeks ahead) across Canadian provinces using historical weekly case counts, and does a deep learning approach (LSTM or Transformer-based) outperform classical baselines such as ARIMA or Prophet?

**Forecast horizon:** 4–8 weeks ahead
**End users:** Provincial/federal public health agencies (e.g., PHAC), epidemiologists, health system planners

## Datasets

### Primary: CANDID / IIDDA

The **Canadian Notifiable Disease Incidence Dataset (CANDID)** contains 934,010 unique incidence records spanning 1903–2021, covering 317 diseases across 13 Canadian provinces and territories. Data is accessed via the [IIDDA REST API](https://math.mcmaster.ca/iidda/api/).

- **Paper:** Earn et al. (2024). *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- **GitHub:** https://github.com/canmod/iidda
- **Key dataset:** `canmod-cdi-normalized`

### Secondary: PHAC Notifiable Disease Data

Used for cross-validation against CANDID (annual granularity).

- **Source:** [PHAC Notifiable Disease Dataset Extraction](https://diseases.canada.ca/notifiable/extract-dataset)

### Supplementary: AHCCD Climate Data

Province-level daily temperature and precipitation used to explore climate–disease correlations.

- **Source:** [Government of Canada — Adjusted and Homogenized Canadian Climate Data (AHCCD)](https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f)
- **Coverage:** 1924–2017 (full overlap of all climate variables and all three focus diseases)
- **Station counts:** 780 temperature stations, 463 precipitation stations

> **Note:** Raw climate files (~1.1 GB) are gitignored. Download from the source URL above and place in `data/raw/climate/`. Metadata files are committed.

## Focus Diseases

| Disease | CANDID key | Weekly Records | Coverage |
|---------|-----------|----------------|----------|
| Influenza | `influenza` | — | Cross-validated against PHAC |
| Pertussis (Whooping Cough) | `whooping-cough` | 30,059 | 1903–2021 |
| Measles | `measles` | 11,164 | 1903–2019 |

**Scope notes:**
- Nunavut (`CA-NU`) excluded from modeling — very sparse data
- `whooping-cough` 1990s resurgence may reflect reporting behavior change, not true incidence
- Analysis window restricted to 1924–2017 for climate-disease merged modeling

## Project Structure

```
├── data/
│   ├── raw/                             # Downloaded from CANDID API and PHAC (gitignored)
│   │   └── climate/                     # AHCCD climate files (gitignored; metadata committed)
│   └── processed/
│       ├── candid_data_split.csv        # Cleaned and train/val/test split disease data
│       ├── climate_disease_merged.csv   # Province-level climate + disease joined dataset
│       ├── final_modeling_dataset.csv
│       └── windows/
│           ├── X_{train,val,test}.npy   # Base windowed sequences (52-week lookback, 8-step target)
│           ├── y_{train,val,test}.npy
│           └── features/                # Feature-engineered windows (6 features)
│               ├── X_{train,val,test}_feat.npy  # shape: (n_windows, 52, 6)
│               └── y_{train,val,test}_feat.npy  # shape: (n_windows, 8)
├── models/
│   └── lstm_baseline/
│       ├── lstm_baseline_best.pt        # Best model weights (lowest val Huber loss)
│       ├── lstm_baseline_config.json    # Architecture + training hyperparameters
│       └── training_history.csv         # Per-epoch train/val loss log
├── notebooks/
│   ├── 00_colab_setup.ipynb             # Google Drive mount and repo clone for Colab
│   ├── 01_data_ingestion_and_eda.ipynb  # API ingestion, PHAC cross-validation, EDA (local)
│   ├── 01_data_ingestion_and_EDA_colab.ipynb  # Colab version of notebook 01
│   ├── 02_climate_exploration.ipynb     # AHCCD data processing and climate-disease merge
│   ├── 02B_LSTM_model_colab.ipynb       # LSTM V1 — superseded by 03B
│   └── 03B_LSTM_model_colab.ipynb       # LSTM V2 — optimised model with HP search (current)
├── reports/
│   ├── figures/                         # Saved plots for the report
│   └── tables/
│       ├── hp_search_results.csv        # Full 24-trial grid search results
│       └── val_metrics.csv              # Per-horizon RMSE/MAE on validation set
├── src/
│   └── data_loader.py                   # CANDID API ingestion utilities
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

Raw disease data is gitignored. Run `01_data_ingestion_and_eda.ipynb` once to cache locally at `data/raw/`. Then run notebooks in order.

For Colab, start with `00_colab_setup.ipynb` to mount Google Drive and clone the repo, then use the `_colab` variants of each notebook.

## Climate Data Setup

Raw AHCCD station files (~1.1 GB) are gitignored. Download from the [AHCCD direct download page](https://crd-data-donnees-rdc.ec.gc.ca/CDAS/products/EC_data/AHCCD_daily/) and place in `data/raw/climate/`:

| Directory | Variable | Unit |
|---|---|---|
| `Homog_daily_max_temp_v2023_Gen3/` | Daily max temperature | °C |
| `Homog_daily_mean_temp_v2023_Gen3/` | Daily mean temperature | °C |
| `Homog_daily_min_temp_v2023_Gen3/` | Daily min temperature | °C |
| `Adj_Daily_Rain_v2017/` | Adjusted daily rainfall | mm |
| `Adj_Daily_Snow_v2017/` | Adjusted daily snowfall | mm |
| `Adj_Daily_Total_v2017/` | Adjusted daily total precipitation | mm |

Metadata files (`Temperature_Stations_Gen3_2023.xlsx`, `Adj_Precipitation_Stations.xls`, `Homog_Temperature_Stations_Segmented_List_Gen3.xls`) are committed.

## References

- Earn, D. et al. (2024). CANDID: Canadian Notifiable Disease Incidence Dataset. *PLOS Global Public Health.* https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0005550
- IIDDA GitHub: https://github.com/canmod/iidda
- AHCCD: Vincent, L.A. et al. Government of Canada Adjusted and Homogenized Canadian Climate Data. https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f
