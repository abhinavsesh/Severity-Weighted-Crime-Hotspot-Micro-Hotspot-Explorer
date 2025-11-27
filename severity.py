def apply_severity_scores(df):

    severity_map = {
        "HOMICIDE": 10,
        "CRIMINAL SEXUAL ASSAULT": 9,
        "ROBBERY": 8,
        "BATTERY": 7,
        "ASSAULT": 7,
        "BURGLARY": 5,
        "MOTOR VEHICLE THEFT": 4,
        "THEFT": 3,
        "NARCOTICS": 2
    }

    df["severity"] = df["primary_type"].map(severity_map).fillna(1)
    df["weighted_lat"] = df["latitude"] * df["severity"]
    df["weighted_lon"] = df["longitude"] * df["severity"]

    return df
