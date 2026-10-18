import os
import json
from flask import Flask, make_response, request
from datetime import datetime

# === Configuration ===
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DATA_PATHS = {
    "Micro_Plates_and_Major_Fault_Zones": os.path.join(
        BASE_DIR, "data/Micro_Plates_and_Major_Fault_Zones.geojson"
    ),
    "Plate_Interface": os.path.join(BASE_DIR, "data/Plate_Interface.geojson"),
    "Plate_Motion": os.path.join(BASE_DIR, "data/Plate_Motion.geojson"),
}

# API metadata
API_NAME = "Fault Lines API"
API_VERSION = "1.0.0"
DEVELOPER = "Emin Neşat Gürses"
GITHUB = "https://github.com/mdaedalus"
EMAIL = "eminnesatg@gmail.com"
NICKNAME = "mdaedalus"


def load_geojson(file_path: str) -> dict:
    """Safely load GeoJSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"GeoJSON file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")


def filter_by_bbox(features: list, bbox: tuple) -> list:
    """
    Filter features by bounding box.
    bbox = (min_lon, min_lat, max_lon, max_lat)
    Supports Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon.
    """
    min_lon, min_lat, max_lon, max_lat = bbox
    result = []

    def point_in_bbox(coords):
        lon, lat = coords[0], coords[1]
        return min_lon <= lon <= max_lon and min_lat <= lat <= max_lat

    for feature in features:
        geom = feature.get("geometry") or {}
        gtype = geom.get("type")
        coords = geom.get("coordinates")

        if not coords:
            continue

        if gtype == "Point":
            if point_in_bbox(coords):
                result.append(feature)
        elif gtype in ("LineString", "MultiPoint"):
            if any(point_in_bbox(c) for c in coords):
                result.append(feature)
        elif gtype in ("Polygon", "MultiLineString"):
            if any(point_in_bbox(c) for ring in coords for c in ring):
                result.append(feature)
        elif gtype == "MultiPolygon":
            if any(
                point_in_bbox(c) for poly in coords for ring in poly for c in ring
            ):
                result.append(feature)

    return result


def parse_bbox(raw: str) -> tuple:
    """Parse '?bbox=minLon,minLat,maxLon,maxLat' into a tuple of floats."""
    parts = raw.split(",")
    if len(parts) != 4:
        raise ValueError(
            "bbox must have 4 comma-separated values: minLon,minLat,maxLon,maxLat"
        )
    return tuple(float(p) for p in parts)


# === Data Loading ===
Micro_Plates_and_Major_Fault_Zones = load_geojson(
    DATA_PATHS["Micro_Plates_and_Major_Fault_Zones"]
)
Plate_Interface = load_geojson(DATA_PATHS["Plate_Interface"])
Plate_Motion = load_geojson(DATA_PATHS["Plate_Motion"])

# Convenient lookup for dataset filtering
DATASETS = {
    "Micro_Plates_and_Major_Fault_Zones": Micro_Plates_and_Major_Fault_Zones,
    "Plate_Interface": Plate_Interface,
    "Plate_Motion": Plate_Motion,
}


# === Flask Application ===
app = Flask(__name__)


def json_response(payload: dict, status: int = 200):
    """Build a JSON response with CORS + cache headers."""
    response = make_response(
        json.dumps(payload, ensure_ascii=False, indent=2), status
    )
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Cache-Control"] = "public, max-age=60"
    return response


@app.route("/", methods=["GET", "OPTIONS"])
def index():
    """
    Return a combined GeoJSON structure with metadata.

    Optional query params:
      ?dataset=Plate_Motion              -> only that dataset
      ?bbox=minLon,minLat,maxLon,maxLat  -> filter features by bounding box
    """
    if request.method == "OPTIONS":
        return json_response({})

    dataset_filter = request.args.get("dataset")
    bbox_raw = request.args.get("bbox")

    # Validate dataset filter
    if dataset_filter and dataset_filter not in DATASETS:
        return json_response(
            {
                "error": "Invalid dataset",
                "valid_datasets": list(DATASETS.keys()),
            },
            status=400,
        )

    # Validate bbox
    bbox = None
    if bbox_raw:
        try:
            bbox = parse_bbox(bbox_raw)
        except ValueError as e:
            return json_response({"error": str(e)}, status=400)

    # Build feature payload
    features_payload = {}
    for name, data in DATASETS.items():
        if dataset_filter and name != dataset_filter:
            continue
        features = data.get("features", [])
        if bbox:
            features = filter_by_bbox(features, bbox)
        features_payload[name] = features

    response_data = {
        "type": "FeatureCollection",
        "name": API_NAME,
        "meta": {
            "developer": DEVELOPER,
            "github": GITHUB,
            "email": EMAIL,
            "nickname": NICKNAME,
            "api_version": API_VERSION,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "filters": {
                "dataset": dataset_filter,
                "bbox": bbox,
            },
        },
        **features_payload,
    }

    return json_response(response_data)


@app.route("/datasets", methods=["GET", "OPTIONS"])
def datasets():
    """List available datasets and their feature counts."""
    if request.method == "OPTIONS":
        return json_response({})

    return json_response(
        {
            "api": API_NAME,
            "api_version": API_VERSION,
            "datasets": [
                {
                    "name": name,
                    "feature_count": len(data.get("features", [])),
                }
                for name, data in DATASETS.items()
            ],
            "count": len(DATASETS),
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        }
    )


@app.route("/health", methods=["GET", "OPTIONS"])
def health():
    """Liveness + dataset freshness check."""
    if request.method == "OPTIONS":
        return json_response({})

    return json_response(
        {
            "status": "ok",
            "api": API_NAME,
            "api_version": API_VERSION,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "datasets": {
                name: len(data.get("features", []))
                for name, data in DATASETS.items()
            },
            "errors": {},
        }
    )


# === Error Handlers ===
@app.errorhandler(404)
def not_found(error):
    return json_response(
        {
            "error": "Not Found",
            "message": "The requested endpoint does not exist.",
            "available_endpoints": ["/", "/datasets", "/health"],
        },
        status=404,
    )


@app.errorhandler(500)
def internal_error(error):
    return json_response(
        {
            "error": "Internal Server Error",
            "message": "Something went wrong on the server.",
        },
        status=500,
    )


if __name__ == "__main__":
    print(f"[INFO] Starting {API_NAME} v{API_VERSION}...")
    print(f"[INFO] Developer: {DEVELOPER} ({GITHUB})")
    print(f"[INFO] Loaded datasets: {list(DATA_PATHS.keys())}")
    app.run(host="0.0.0.0", port=5000, debug=True)
