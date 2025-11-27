import pandas as pd

def load_and_clean_data(path):
    df_raw = pd.read_csv(path, low_memory=False, on_bad_lines="skip", dtype=str)

    df_raw.columns = (
        df_raw.columns.str.replace('"', '')
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df_raw = df_raw.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)

    usecols = ["date","primary_type","description","arrest","district","latitude","longitude"]
    df = df_raw[usecols].copy()

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    df.dropna(subset=["latitude","longitude","date"], inplace=True)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df.dropna(subset=["date"], inplace=True)

    df["primary_type"] = df["primary_type"].str.upper()

    return df
