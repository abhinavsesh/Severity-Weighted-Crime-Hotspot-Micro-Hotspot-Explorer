from sklearn.cluster import KMeans

def run_kmeans(df, k):

    coords = df[["weighted_lat","weighted_lon"]]

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(coords)

    return df, kmeans
