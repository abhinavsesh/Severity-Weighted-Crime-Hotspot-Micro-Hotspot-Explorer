# 🔥 Severity-Weighted Crime Hotspot & Micro-Hotspot Detection

This repository contains the implementation of a **Severity-Weighted Hierarchical Crime Hotspot Detection System** built using the **Chicago Crime Dataset (2024)**.  
The project identifies:
- City-level **macro crime hotspots** using K-Means clustering,
- Street-level **micro-hotspots** using DBSCAN,
- And ranks the **most dangerous street segments using cumulative crime severity**.

An **interactive web dashboard** is also provided for real-time exploration using **Streamlit and Folium**.

---

## 📌 Project Motivation

Traditional crime hotspot systems rely only on raw crime counts. This often leads to misleading conclusions where areas with many minor crimes appear more dangerous than regions with fewer but highly violent crimes.

This project introduces:
- **Severity-aware crime modeling**
- **Hierarchical clustering (macro + micro hotspots)**
- **Street-level danger ranking**
- **Interactive visualization for practical policing use**

---

## 🚀 Features

- ✅ Severity score assignment for each crime
- ✅ Severity-weighted spatial clustering
- ✅ Macro-hotspot detection using K-Means
- ✅ Street-level micro-hotspot detection using DBSCAN
- ✅ Street-level danger ranking (Top 5 most dangerous streets)
- ✅ Interactive heatmap and dashboard using Streamlit & Folium
- ✅ User controls for clustering parameters
- ✅ Clean modular Python codebase

---

## 🗂 Dataset Used

- **Chicago Crimes 2024 Dataset**
- Source: City of Chicago Open Data Portal
- Attributes used:
  - Date
  - Primary Crime Type
  - Latitude
  - Longitude
  - Arrest
  - Police District

## Dataset not provided here since it exceeds 25MB. 

## 🧠 Methodology Overview

1. **Data Cleaning & Preprocessing**
2. **Severity Score Assignment**
3. **Severity-Weighted Feature Engineering**
4. **Macro Hotspot Detection using K-Means**
5. **Micro Hotspot Detection using DBSCAN**
6. **Street-Level Danger Ranking**
7. **Interactive Web Visualization**

---

## 🛠 Tools & Technologies

- Python 3.9+
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Folium
- Matplotlib

---

## 📁 Project Structure

