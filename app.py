import streamlit as st
import pandas as pd
from modules.data_loader import load_and_clean_data
from modules.severity import apply_severity_scores
from modules.clustering import run_kmeans
from modules.micro_hotspots import run_micro_hotspots
from modules.mapping import generate_map

st.set_page_config(page_title="Crime Hotspot Explorer", layout="wide")

st.title("🚨 Severity-Weighted Crime Hotspot & Micro-Hotspot Explorer")
st.markdown("Analyzing **Chicago 2024 Crime Data** with Severity Weighting & Micro-Hotspot Detection")

# Sidebar Controls
st.sidebar.header("Visualization Controls")
k = st.sidebar.slider("Number of Main Hotspots (K-Means)", 5, 15, 10)
show_micro = st.sidebar.checkbox("Show Micro-Hotspots (DBSCAN)", True)

DATA_PATH = "Crimes_-_2024_20251111.csv"   # keep CSV in same folder

# Load Data
@st.cache_data
def load_all():
    df = load_and_clean_data(DATA_PATH)
    df = apply_severity_scores(df)
    df, kmeans_model = run_kmeans(df, k)
    df = run_micro_hotspots(df)
    return df, kmeans_model

df, kmeans_model = load_all()

# ================================
# 🔥 TOP 5 MOST DANGEROUS STREETS
# ================================

# Create a street ID using rounded coordinates (~100 meters)
df["street_id"] = (
    df["latitude"].round(4).astype(str) + "_" +
    df["longitude"].round(4).astype(str)
)

# Aggregate severity at street level
street_severity = (
    df.groupby("street_id")
      .agg(
          total_severity=("severity", "sum"),
          crime_count=("severity", "count"),
          avg_severity=("severity", "mean"),
          latitude=("latitude", "mean"),
          longitude=("longitude", "mean")
      )
      .reset_index()
)

# Get Top 5 most dangerous streets
top_5_dangerous_streets = street_severity.sort_values(
    by="total_severity",
    ascending=False
).head(5)


# KPIs
st.subheader("📊 Overall Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Crimes", len(df))
col2.metric("High Severity Crimes", len(df[df["severity"] >= 7]))
col3.metric("Micro-Hotspots Found", (df["micro_cluster"] >= 0).sum())

# Map
st.subheader("🗺️ Severity-Weighted Hotspot Map")
crime_map = generate_map(df, show_micro)
st.components.v1.html(crime_map._repr_html_(), height=600)

# Table
st.subheader("📍 Sample Crime Records")
st.dataframe(df[["primary_type","severity","cluster","micro_cluster"]].head(30))

st.subheader("🔥 Top 5 Most Dangerous Streets (Severity-Weighted)")
st.dataframe(top_5_dangerous_streets, use_container_width=True)

