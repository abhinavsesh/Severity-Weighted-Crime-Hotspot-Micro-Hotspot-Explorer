import folium

def generate_map(df, show_micro=True):

    m = folium.Map(location=[41.8781, -87.6298], zoom_start=11, tiles="CartoDB positron")

    # Severity Points
    sample = df.sample(min(12000, len(df)), random_state=42)

    for _, row in sample.iterrows():
        color = "red" if row["severity"] >= 7 else "orange" if row["severity"] >= 4 else "blue"
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=2,
            color=color,
            fill=True,
            fill_opacity=0.4
        ).add_to(m)

    # Micro-Hotspots
    if show_micro:
        micro = df[df["micro_cluster"] >= 0]
        for _, row in micro.iterrows():
            folium.CircleMarker(
                location=[row["latitude"], row["longitude"]],
                radius=4,
                color="purple",
                fill=True,
                fill_opacity=0.8
            ).add_to(m)

    return m
