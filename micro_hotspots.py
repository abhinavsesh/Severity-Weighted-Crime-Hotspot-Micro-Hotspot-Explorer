from sklearn.cluster import DBSCAN

def run_micro_hotspots(df):

    top_clusters = (
        df.groupby("cluster")["severity"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
        .index
    )

    df["micro_cluster"] = -1

    for c in top_clusters:
        subset = df[df["cluster"] == c][["latitude","longitude"]]
        db = DBSCAN(eps=0.002, min_samples=20).fit(subset)
        df.loc[df["cluster"] == c, "micro_cluster"] = db.labels_

    return df
