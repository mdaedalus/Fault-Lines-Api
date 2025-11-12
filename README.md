# 🌍 Mdaedalus Geo API

**Mdaedalus Geo API** is a lightweight Flask-based geospatial API designed to serve geological plate and fault zone data in GeoJSON format.  
It combines multiple datasets into a single, well-structured JSON response for easy integration into GIS tools or frontend visualizations.

---

## 🚀 Features

- Serves three geological datasets in one response:
  - **Micro Plates and Major Fault Zones**
  - **Plate Interface**
  - **Plate Motion**
- Built with **Flask**
- Returns data in **standard GeoJSON** format
- Includes developer metadata and timestamp
- Fully **CORS-enabled** for public data access

---

## 📂 Project Structure

mdaedalus_geo_api/
├── data/
│ ├── Micro_Plates_and_Major_Fault_Zones.geojson
│ ├── Plate_Interface.geojson
│ └── Plate_Motion.geojson
├── mdaedalus_geo_api.py
└── README.md


---

## ⚙️ Requirements

Install dependencies using `pip`:

```bash
pip install flask geopandas
