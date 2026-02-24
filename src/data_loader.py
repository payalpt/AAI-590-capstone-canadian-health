"""
CANDID API data ingestion utilities.
Fetches data from the IIDDA REST API at https://math.mcmaster.ca/iidda/api/
"""

import io
import zipfile
import requests
import pandas as pd

IIDDA_API_BASE = "https://math.mcmaster.ca/iidda/api"

NORMALIZED_DATASET_ID = "canmod-cdi-normalized"


def get_dataset_ids() -> list[str]:
    """Return all available dataset IDs from the IIDDA API."""
    url = f"{IIDDA_API_BASE}/metadata"
    params = {"response_type": "dataset_ids"}
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def get_dataset_metadata(dataset_id: str) -> dict:
    """Return metadata for a specific dataset."""
    url = f"{IIDDA_API_BASE}/metadata"
    params = {
        "string_comparison": "Equals",
        "dataset_ids": dataset_id,
    }
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def download_dataset(dataset_id: str = NORMALIZED_DATASET_ID) -> pd.DataFrame:
    """
    Download a dataset from the IIDDA API and return as a DataFrame.
    The API returns a zip archive containing a CSV file.
    """
    url = f"{IIDDA_API_BASE}/download"
    params = {"resource": "csv", "dataset_ids": dataset_id}
    print(f"Downloading dataset '{dataset_id}' from IIDDA API...")
    response = requests.get(url, params=params, timeout=120, stream=True)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_files = [f for f in z.namelist() if f.endswith(".csv")]
        if not csv_files:
            raise ValueError(f"No CSV file found in zip archive for dataset '{dataset_id}'")
        with z.open(csv_files[0]) as f:
            df = pd.read_csv(f, low_memory=False)

    print(f"Downloaded {len(df):,} rows, {df.shape[1]} columns.")
    return df


def load_candid(cache_path: str | None = None) -> pd.DataFrame:
    """
    Load and lightly type-cast the normalized CANDID dataset.
    Optionally cache to a local CSV to avoid re-downloading.
    """
    if cache_path:
        try:
            df = pd.read_csv(cache_path, low_memory=False, parse_dates=["period_start_date", "period_end_date", "period_mid_date"])
            print(f"Loaded {len(df):,} rows from cache: {cache_path}")
            return df
        except FileNotFoundError:
            pass

    df = download_dataset(NORMALIZED_DATASET_ID)

    # Type casting
    for col in ["period_start_date", "period_end_date", "period_mid_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    df["cases_this_period"] = pd.to_numeric(df["cases_this_period"], errors="coerce")
    df["population"] = pd.to_numeric(df["population"], errors="coerce")

    if cache_path:
        df.to_csv(cache_path, index=False)
        print(f"Cached to {cache_path}")

    return df


def filter_disease_province(
    df: pd.DataFrame,
    disease: str,
    province_code: str | None = None,
    time_scale: str = "wk",
) -> pd.DataFrame:
    """
    Filter the CANDID dataframe to a specific disease, optional province, and time scale.

    Args:
        df: Full CANDID DataFrame
        disease: Disease name as in the 'disease' column (e.g., 'poliomyelitis')
        province_code: ISO 3166-2 code (e.g., 'CA-ON'). None returns all provinces.
        time_scale: 'wk', 'mo', 'qr', etc.

    Returns:
        Filtered DataFrame sorted by period_start_date.
    """
    mask = (df["disease"] == disease) & (df["time_scale"] == time_scale)
    if province_code:
        mask &= df["iso_3166_2"] == province_code
    return df[mask].sort_values("period_start_date").reset_index(drop=True)
