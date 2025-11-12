import os
import json
from flask import Flask, make_response
from datetime import datetime
import geopandas as gpd

# === Configuration ===
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DATA_PATHS = {
    "Micro_Plates_and_Major_Fault_Zones": os.path.join(BASE_DIR, "data/Micro_Plates_and_Major_Fault_Zones.geojson"),
    "Plate_Interface": os.path.join(BASE_DIR, "data/Plate_Interface.geojson"),
    "Plate_Motion": os.path.join(BASE_DIR, "data/Plate_Motion.geojson")
}


def load_geojson(file_path: str) -> dict:
    """Safely load GeoJSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"GeoJSON file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")


# === Data Loading ===
Micro_Plates_and_Major_Fault_Zones = load_geojson(DATA_PATHS["Micro_Plates_and_Major_Fault_Zones"])
Plate_Interface = load_geojson(DATA_PATHS["Plate_Interface"])
Plate_Motion = load_geojson(DATA_PATHS["Plate_Motion"])


# === Flask Application ===
app = Flask(__name__)


@app.route("/")
def index():
    """Return a combined GeoJSON structure with metadata."""
    response_data = {
        "type": "FeatureCollection",
        "name": "Micro Plates and Major Fault Zones",
        "meta": {
            "developer": "Emin",
            "github": "https://github.com/Peyxw",
            "email": "eminnesatg@gmail.com",
            "nickname": "Peyxw",
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        },
        "Micro_Plates_and_Major_Fault_Zones": Micro_Plates_and_Major_Fault_Zones.get("features", []),
        "Plate_Interface": Plate_Interface.get("features", []),
        "Plate_Motion": Plate_Motion.get("features", [])
    }

    response = make_response(json.dumps(response_data, ensure_ascii=False, indent=2))
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    print("[INFO] Starting Mdaedalus Geo API server...")
    print(f"[INFO] Loaded datasets: {list(DATA_PATHS.keys())}")
    app.run(debug=True)
