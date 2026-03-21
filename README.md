# AAI-590 Capstone: Forecasting Canadian Infectious Disease Incidence<br>

**Project Team** Carrie Little, Payal Patal, Dean P. Simmer <br>
**Course:** AAI-590 — Applied AI Capstone | University of San Diego, M.S. Applied AI<br>
**Dataset:** [CANDID / IIDDA](https://github.com/canmod/iidda) — Canadian Notifiable Disease Incidence Dataset<br>

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

## Climate Data (AHCCD)

A supplementary climate dataset is used to explore whether temperature and precipitation correlate with disease incidence. See `notebooks/02_climate_exploration.ipynb`.

**Source**: [Government of Canada — Adjusted and Homogenized Canadian Climate Data (AHCCD)](https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f)

### Files in `data/raw/climate/`

Metadata files are committed. Raw station files (~1.1 GB) are gitignored — download from the source URL above and place them in `data/raw/climate/`.

| Directory / File | Variable | Unit | Coverage | Committed |
|---|---|---|---|---|
| `Homog_daily_max_temp_v2023_Gen3/` | Daily max temperature | °C | ~1840–2023 | No |
| `Homog_daily_mean_temp_v2023_Gen3/` | Daily mean temperature | °C | ~1840–2023 | No |
| `Homog_daily_min_temp_v2023_Gen3/` | Daily min temperature | °C | ~1840–2023 | No |
| `Adj_Daily_Rain_v2017/` | Adjusted daily rainfall | mm | ~1840–2017 | No |
| `Adj_Daily_Snow_v2017/` | Adjusted daily snowfall | mm | ~1840–2017 | No |
| `Adj_Daily_Total_v2017/` | Adjusted daily total precipitation | mm | ~1840–2017 | No |
| `Temperature_Stations_Gen3_2023.xlsx` | Temperature station metadata | — | — | Yes |
| `Adj_Precipitation_Stations.xls` | Precipitation station metadata | — | — | Yes |
| `Homog_Temperature_Stations_Segmented_List_Gen3.xls` | Temperature station segment manifest | — | — | Yes |

**Analysis scope**: 1924–2017 (full overlap of all climate variables and all three focus diseases).
**Station counts**: 780 temperature stations, 463 precipitation stations, all 13 provinces/territories.

### File format

Each `.txt` station file uses a fixed-width format: `YEAR  MONTH  val1flag ... val31flag` (one row per month, 31 day columns). Missing values: `-9999.99M` (precip) / `-9999.9M` (temp). Flags: `Y` = valid, `M` = missing, `T` = trace, `a` = adjusted.

### Province code → ISO 3166-2 mapping

Temperature files use `QUE`, `ONT`, `ALTA`, `SASK`, `MAN`, `NFLD`, `NWT`, `PEI` — mapped to `CA-QC`, `CA-ON`, `CA-AB`, `CA-SK`, `CA-MB`, `CA-NL`, `CA-NT`, `CA-PE` respectively. Precipitation files use near-ISO codes (`QC`, `ON`, etc.) with one exception: `YK` → `CA-YT`.

## References

- Earn, D. et al. (2024). CANDID: Canadian Notifiable Disease Incidence Dataset. *PLOS Global Public Health.*
- IIDDA GitHub: https://github.com/canmod/iidda
- AHCCD: Vincent, L.A. et al. Government of Canada Adjusted and Homogenized Canadian Climate Data. https://open.canada.ca/data/en/dataset/d6813de6-b20a-46cc-8990-01862ae15c5f
