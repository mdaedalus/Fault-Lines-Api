# 🌍 Fault Lines API

**Fault Lines API**, jeolojik plaka ve fay zonu verilerini GeoJSON formatında sunan hafif bir Flask tabanlı jeo-uzamsal API'dir. Üç veri setini — **Mikro Plakalar ve Ana Fay Zonları**, **Plaka Arayüzü** ve **Plaka Hareketi** — tek bir tutarlı GeoJSON yanıtında birleştirir.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![GeoJSON](https://img.shields.io/badge/GeoJSON-compatible-FF6B35?style=for-the-badge&logo=json&logoColor=white)](https://geojson.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](http://makeapullrequest.com)

[🇹🇷 Türkçe](#-türkçe) · [🇬🇧 English](#-english)

</div>

---

<div align="center">

## 🇹🇷 Türkçe

</div>

### 🎯 Nedir Bu?

**Fault Lines API**, üç jeolojik veri setini — **Mikro Plakalar ve Ana Fay Zonları**, **Plaka Arayüzü** ve **Plaka Hareketi** — tek bir tutarlı GeoJSON yanıtında birleştiren hafif bir Flask API'sidir.

Kurulumu saniyeler sürer, harici veritabanı gerektirmez, tüm veriyi bellekte tutar ve web uygulamalarınıza, harita dashboard'larınıza veya GIS araçlarınıza (Leaflet, Mapbox, QGIS, ArcGIS) doğrudan bağlanabilir.

> **Neden Fault Lines API?** Çünkü üç ayrı jeolojik veri setini tek ve tutarlı bir şemada birleştirir, CORS açıktır ve standart GeoJSON çıktısıyla herhangi bir GIS aracına doğrudan entegre olur.

---

### 💡 Neden Bu API?

<div align="center">

| 🌍 | 📦 | 🗺️ | ⚡ |
|:---:|:---:|:---:|:---:|
| **Üç veri seti, tek API** | **GeoJSON uyumlu** | **GIS hazır** | **Hafif** |
| Mikro plakalar + arayüz + hareket | Standart FeatureCollection | Leaflet, Mapbox, QGIS, ArcGIS | Flask |

| 🔓 | 📋 | 🕐 | ❤️ |
|:---:|:---:|:---:|:---:|
| **Açık CORS** | **Zengin metadata** | **Otomatik zaman damgası** | **Geliştirici dostu** |
| Her domainden erişim | Geliştirici + sürüm bilgisi | UTC formatında | Tek dosya, kolay kurulum |

</div>

---

### ✨ Özellikler

<table>
<tr>
<td width="50%" valign="top">

#### 🌍 Veri Setleri
- ✅ **Mikro Plakalar ve Ana Fay Zonları**
- ✅ **Plaka Arayüzü** (Plate Interface)
- ✅ **Plaka Hareketi** (Plate Motion)
- ✅ Üçü de **tek yanıtta** birleşik
- ✅ UTF-8 çıktı

#### 🔎 Filtreleme
- ✅ **Veri seti seçimi** — `?dataset=Plate_Motion`
- ✅ **Bounding box** — `?bbox=26,36,45,42`
- ✅ **İkisi birden** — `?dataset=Plate_Interface&bbox=26,36,45,42`

</td>
<td width="50%" valign="top">

#### 📦 Çıktı Formatı
- ✅ **Standart GeoJSON** `FeatureCollection`
- ✅ Her veri seti ayrı anahtar altında
- ✅ `meta` bloğunda **geliştirici bilgileri**
- ✅ **UTC zaman damgası**

#### 🛡️ Güvenilirlik
- ✅ **JSON 404 ve 500 handler'ları**
- ✅ **Anlamlı hata mesajları**
- ✅ `Cache-Control: max-age=60`
- ✅ **OPTIONS** desteği (CORS preflight)

</td>
</tr>
</table>

---

### 🛠️ Teknoloji Yığını

<div align="center">

| Katman | Teknoloji |
|:-------|:----------|
| **Backend** | Python 3.10+, Flask 3.0 |
| **JSON İşleme** | `json` (standart kütüphane) |
| **Zaman** | `datetime` (UTC) |
| **Çıktı** | JSON (GeoJSON uyumlu) |
| **CORS** | Manuel header + OPTIONS |

</div>

---

### 🚀 Kurulum

#### Gereksinimler
- Python 3.10 veya üzeri
- pip

#### Adım Adım

```bash
# 1. Repoyu klonla
git clone https://github.com/mdaedalus/Fault-Lines-API.git
cd Fault-Lines-API

# 2. Sanal ortam oluştur
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. API'yi başlat
python app.py
```

Tarayıcınızda açın: **http://localhost:5000**

> **Not:** GeoJSON dosyaları `data/` klasöründe bulunmalıdır. `DATA_PATHS` sözlüğünden yolları özelleştirebilirsiniz.

---

### 📂 Proje Yapısı

```
Fault-Lines-API/
├── data/
│   ├── Micro_Plates_and_Major_Fault_Zones.geojson
│   ├── Plate_Interface.geojson
│   └── Plate_Motion.geojson
├── app.py                         # Ana Flask uygulaması
├── requirements.txt
├── LICENSE                        # MIT
├── .gitignore
└── README.md
```

---

### 🔌 API Kullanımı

#### Endpoint'ler

| Endpoint | Açıklama |
|:---------|:---------|
| `GET /` | Tüm veri setleri (filtreli) |
| `GET /datasets` | Mevcut veri setlerini listeler |
| `GET /health` | Canlılık ve veri sayısı kontrolü |

#### Query Parametreleri (`/`)

| Parametre | Tip | Açıklama | Örnek |
|:----------|:----|:---------|:------|
| `dataset` | string | Sadece belirtilen veri seti | `?dataset=Plate_Motion` |
| `bbox` | string | Bounding box (minLon,minLat,maxLon,maxLat) | `?bbox=26,36,45,42` |

#### Örnek İstekler

```bash
# Tüm veri setleri
curl http://localhost:5000/

# Sadece Plate_Motion
curl http://localhost:5000/?dataset=Plate_Motion

# Türkiye çevresi bbox
curl "http://localhost:5000/?bbox=26,36,45,42"

# Hem dataset hem bbox
curl "http://localhost:5000/?dataset=Plate_Interface&bbox=26,36,45,42"

# Veri setlerini listele
curl http://localhost:5000/datasets

# Sağlık kontrolü
curl http://localhost:5000/health
```

#### Örnek Yanıt (`/`)

```json
{
  "type": "FeatureCollection",
  "name": "Fault Lines API",
  "meta": {
    "developer": "Emin Neşat Gürses",
    "github": "https://github.com/mdaedalus",
    "email": "eminnesatg@gmail.com",
    "nickname": "mdaedalus",
    "api_version": "1.0.0",
    "generated_at": "2025-01-15 14:32:00 UTC",
    "filters": { "dataset": null, "bbox": null }
  },
  "Micro_Plates_and_Major_Fault_Zones": [
    {
      "type": "Feature",
      "properties": { "name": "North Anatolian Fault", "type": "major_fault" },
      "geometry": { "type": "LineString", "coordinates": [[...]] }
    }
  ],
  "Plate_Interface": [
    {
      "type": "Feature",
      "properties": { "plate_a": "Eurasian", "plate_b": "Anatolian" },
      "geometry": { "type": "LineString", "coordinates": [[...]] }
    }
  ],
  "Plate_Motion": [
    {
      "type": "Feature",
      "properties": { "velocity_mm_yr": 24, "direction": "W" },
      "geometry": { "type": "Point", "coordinates": [32.85, 39.92] }
    }
  ]
}
```

#### Örnek Yanıt (`/datasets`)

```json
{
  "api": "Fault Lines API",
  "api_version": "1.0.0",
  "datasets": [
    { "name": "Micro_Plates_and_Major_Fault_Zones", "feature_count": 128 },
    { "name": "Plate_Interface", "feature_count": 42 },
    { "name": "Plate_Motion", "feature_count": 96 }
  ],
  "count": 3,
  "generated_at": "2025-01-15 14:32:00 UTC"
}
```

#### Örnek Yanıt (`/health`)

```json
{
  "status": "ok",
  "api": "Fault Lines API",
  "api_version": "1.0.0",
  "generated_at": "2025-01-15 14:32:00 UTC",
  "datasets": {
    "Micro_Plates_and_Major_Fault_Zones": 128,
    "Plate_Interface": 42,
    "Plate_Motion": 96
  },
  "errors": {}
}
```

#### Hata Örneği (geçersiz dataset)

```bash
curl "http://localhost:5000/?dataset=Yanlis"
```

```json
{
  "error": "Invalid dataset",
  "valid_datasets": [
    "Micro_Plates_and_Major_Fault_Zones",
    "Plate_Interface",
    "Plate_Motion"
  ]
}
```

---

### 🗺️ Kullanım Akışı

<div align="center">

| Adres | Yaptığı İş |
|:------|:-----------|
| `/` | Tüm veri setleri (filtreli) |
| `/?dataset=Plate_Motion` | Sadece belirtilen veri seti |
| `/?bbox=26,36,45,42` | Bounding box ile filtreleme |
| `/?dataset=Plate_Interface&bbox=26,36,45,42` | Hem dataset hem bbox |
| `/datasets` | Mevcut veri setlerini listeler |
| `/health` | Canlılık ve veri sayısı kontrolü |

</div>

---

### 🔧 Özelleştirme

<details>
<summary><b>📂 Veri Yolları</b></summary>

Yeni veri setleri eklemek veya yolları değiştirmek için `DATA_PATHS` sözlüğünü düzenleyin:

```python
DATA_PATHS = {
    "Micro_Plates_and_Major_Fault_Zones": os.path.join(BASE_DIR, "data/Micro_Plates_and_Major_Fault_Zones.geojson"),
    "Plate_Interface": os.path.join(BASE_DIR, "data/Plate_Interface.geojson"),
    "Plate_Motion": os.path.join(BASE_DIR, "data/Plate_Motion.geojson"),
    "Yeni_Dataset": os.path.join(BASE_DIR, "data/Yeni_Dataset.geojson")  # yeni
}
```

Ardından `DATASETS` sözlüğüne ekleyin:

```python
DATASETS = {
    # ...
    "Yeni_Dataset": Yeni_Dataset,
}
```
</details>

<details>
<summary><b>🌐 Port ve Host</b></summary>

`app.run()` satırını düzenleyin:

```python
app.run(host="0.0.0.0", port=8080, debug=False)
```
</details>

<details>
<summary><b>🔒 CORS Politikası</b></summary>

Tüm domain'lere açmak yerine belirli bir domain'e kısıtlamak için:

```python
response.headers["Access-Control-Allow-Origin"] = "https://siteniz.com"
```
</details>

<details>
<summary><b>📋 Metadata Güncelleme</b></summary>

Geliştirici bilgilerini `app.py` başındaki sabitlerden düzenleyin:

```python
API_NAME = "Fault Lines API"
API_VERSION = "1.0.0"
DEVELOPER = "Emin Neşat Gürses"
GITHUB = "https://github.com/mdaedalus"
EMAIL = "eminnesatg@gmail.com"
NICKNAME = "mdaedalus"
```
</details>

<details>
<summary><b>🎨 Yanıt Formatı</b></summary>

Pretty-print yerine kompakt JSON döndürmek için `json_response()` içindeki `indent=2` parametresini kaldırın:

```python
json.dumps(payload, ensure_ascii=False)
```
</details>

---

### 🗺️ Yol Haritası

- [x] 🟢 v0.1 — Üç veri setini tek yanıtta birleştirme
- [x] 🟢 v0.2 — GeoJSON uyumlu çıktı
- [x] 🟢 v0.3 — CORS desteği
- [x] 🟢 v0.4 — Metadata + UTC zaman damgası
- [x] 🟢 v0.5 — Anlamlı hata yönetimi
- [x] 🟢 v0.6 — Veri seti bazlı filtreleme (`?dataset=`)
- [x] 🟢 v0.7 — Bounding box filtresi (`?bbox=`)
- [x] 🟢 v0.8 — `/health` endpoint'i
- [x] 🟢 v0.9 — `/datasets` endpoint'i
- [ ] 🟡 v1.0 — GeoJSON export endpoint'leri (tek veri seti indirme)
- [ ] 🟠 v1.1 — Redis cache katmanı
- [ ] 🟠 v1.2 — Prometheus metrics
- [ ] 🟠 v1.3 — Rate limiting
- [ ] 🔴 v1.4 — Docker imajı
- [ ] 🔴 v2.0 — Harici jeolojik API'ler (USGS, GEM) entegrasyonu

---

### 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Büyük değişiklikler için önce bir **issue** açın.

```bash
# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/yeni-ozellik
git commit -m "feat: yeni özellik eklendi"
git push origin feature/yeni-ozellik
```

#### Commit Kuralları

| Prefix | Anlamı |
|:-------|:-------|
| `feat:` | yeni özellik |
| `fix:` | hata düzeltme |
| `docs:` | dokümantasyon |
| `style:` | kod formatı |
| `refactor:` | yeniden düzenleme |
| `test:` | test ekleme |

---

### ⚠️ Yasal Uyarı

Bu API, jeolojik plaka ve fay zonu verilerini **açık kaynaklardan** sunar. Resmî bir kurum değildir ve **kritik jeolojik kararlar için tek başına kullanılmamalıdır**. Akademik veya resmî veriler için lütfen ilgili kurumlara başvurun.

---

<div align="center">

## 🇬🇧 English

</div>

### 🎯 What Is This?

**Fault Lines API** is a lightweight Flask-based geospatial API that serves geological plate and fault zone data in GeoJSON format. It merges three datasets — **Micro Plates and Major Fault Zones**, **Plate Interface**, and **Plate Motion** — into a single consistent GeoJSON response.

It sets up in seconds, requires no external database, holds all data in memory, and plugs directly into your web apps, map dashboards, or GIS tools (Leaflet, Mapbox, QGIS, ArcGIS).

> **Why Fault Lines API?** Because it merges three geological datasets into one consistent schema, keeps CORS open, and exposes standard GeoJSON output that integrates directly with any GIS tool.

---

### 💡 Why This API?

<div align="center">

| 🌍 | 📦 | 🗺️ | ⚡ |
|:---:|:---:|:---:|:---:|
| **Three datasets, one API** | **GeoJSON compatible** | **GIS ready** | **Lightweight** |
| Micro plates + interface + motion | Standard FeatureCollection | Leaflet, Mapbox, QGIS, ArcGIS | Flask |

| 🔓 | 📋 | 🕐 | ❤️ |
|:---:|:---:|:---:|:---:|
| **Open CORS** | **Rich metadata** | **Auto timestamp** | **Developer friendly** |
| Access from any domain | Developer + version info | UTC format | Single file, easy setup |

</div>

---

### ✨ Features

<table>
<tr>
<td width="50%" valign="top">

#### 🌍 Data Sources
- ✅ **Micro Plates and Major Fault Zones**
- ✅ **Plate Interface**
- ✅ **Plate Motion**
- ✅ All three **in one response**
- ✅ UTF-8 output

#### 🔎 Filtering
- ✅ **Dataset selection** — `?dataset=Plate_Motion`
- ✅ **Bounding box** — `?bbox=26,36,45,42`
- ✅ **Both** — `?dataset=Plate_Interface&bbox=26,36,45,42`

</td>
<td width="50%" valign="top">

#### 📦 Output Format
- ✅ **Standard GeoJSON** `FeatureCollection`
- ✅ Each dataset under its own key
- ✅ **Developer info** in `meta` block
- ✅ **UTC timestamp**

#### 🛡️ Reliability
- ✅ **JSON 404 & 500 handlers**
- ✅ **Meaningful error messages**
- ✅ `Cache-Control: max-age=60`
- ✅ **OPTIONS** support (CORS preflight)

</td>
</tr>
</table>

---

### 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:------|:-----------|
| **Backend** | Python 3.10+, Flask 3.0 |
| **JSON Handling** | `json` (standard library) |
| **Time** | `datetime` (UTC) |
| **Output** | JSON (GeoJSON-compatible) |
| **CORS** | Manual header + OPTIONS |

</div>

---

### 🚀 Installation

#### Requirements
- Python 3.10 or higher
- pip

#### Step by Step

```bash
# 1. Clone the repo
git clone https://github.com/mdaedalus/Fault-Lines-API.git
cd Fault-Lines-API

# 2. Create virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the API
python app.py
```

Open in your browser: **http://localhost:5000**

> **Note:** GeoJSON files must be in the `data/` folder. You can customize paths via the `DATA_PATHS` dict.

---

### 📂 Project Structure

```
Fault-Lines-API/
├── data/
│   ├── Micro_Plates_and_Major_Fault_Zones.geojson
│   ├── Plate_Interface.geojson
│   └── Plate_Motion.geojson
├── app.py                         # Main Flask app
├── requirements.txt
├── LICENSE                        # MIT
├── .gitignore
└── README.md
```

---

### 🔌 API Usage

#### Endpoints

| Endpoint | Description |
|:---------|:------------|
| `GET /` | All datasets (filterable) |
| `GET /datasets` | Lists available datasets |
| `GET /health` | Liveness & feature count check |

#### Query Params (`/`)

| Param | Type | Description | Example |
|:------|:-----|:------------|:--------|
| `dataset` | string | Only the given dataset | `?dataset=Plate_Motion` |
| `bbox` | string | Bounding box (minLon,minLat,maxLon,maxLat) | `?bbox=26,36,45,42` |

#### Example Requests

```bash
# All datasets
curl http://localhost:5000/

# Only Plate_Motion
curl http://localhost:5000/?dataset=Plate_Motion

# Turkey bounding box
curl "http://localhost:5000/?bbox=26,36,45,42"

# Both dataset and bbox
curl "http://localhost:5000/?dataset=Plate_Interface&bbox=26,36,45,42"

# List datasets
curl http://localhost:5000/datasets

# Health check
curl http://localhost:5000/health
```

#### Example Response (`/`)

```json
{
  "type": "FeatureCollection",
  "name": "Fault Lines API",
  "meta": {
    "developer": "Emin Neşat Gürses",
    "github": "https://github.com/mdaedalus",
    "email": "eminnesatg@gmail.com",
    "nickname": "mdaedalus",
    "api_version": "1.0.0",
    "generated_at": "2025-01-15 14:32:00 UTC",
    "filters": { "dataset": null, "bbox": null }
  },
  "Micro_Plates_and_Major_Fault_Zones": [
    {
      "type": "Feature",
      "properties": { "name": "North Anatolian Fault", "type": "major_fault" },
      "geometry": { "type": "LineString", "coordinates": [[...]] }
    }
  ],
  "Plate_Interface": [
    {
      "type": "Feature",
      "properties": { "plate_a": "Eurasian", "plate_b": "Anatolian" },
      "geometry": { "type": "LineString", "coordinates": [[...]] }
    }
  ],
  "Plate_Motion": [
    {
      "type": "Feature",
      "properties": { "velocity_mm_yr": 24, "direction": "W" },
      "geometry": { "type": "Point", "coordinates": [32.85, 39.92] }
    }
  ]
}
```

#### Example Response (`/datasets`)

```json
{
  "api": "Fault Lines API",
  "api_version": "1.0.0",
  "datasets": [
    { "name": "Micro_Plates_and_Major_Fault_Zones", "feature_count": 128 },
    { "name": "Plate_Interface", "feature_count": 42 },
    { "name": "Plate_Motion", "feature_count": 96 }
  ],
  "count": 3,
  "generated_at": "2025-01-15 14:32:00 UTC"
}
```

#### Example Response (`/health`)

```json
{
  "status": "ok",
  "api": "Fault Lines API",
  "api_version": "1.0.0",
  "generated_at": "2025-01-15 14:32:00 UTC",
  "datasets": {
    "Micro_Plates_and_Major_Fault_Zones": 128,
    "Plate_Interface": 42,
    "Plate_Motion": 96
  },
  "errors": {}
}
```

#### Error Example (invalid dataset)

```bash
curl "http://localhost:5000/?dataset=Yanlis"
```

```json
{
  "error": "Invalid dataset",
  "valid_datasets": [
    "Micro_Plates_and_Major_Fault_Zones",
    "Plate_Interface",
    "Plate_Motion"
  ]
}
```

---

### 🗺️ Usage Flow

<div align="center">

| URL | What It Does |
|:----|:-------------|
| `/` | All datasets (filterable) |
| `/?dataset=Plate_Motion` | Only the given dataset |
| `/?bbox=26,36,45,42` | Filter by bounding box |
| `/?dataset=Plate_Interface&bbox=26,36,45,42` | Both dataset and bbox |
| `/datasets` | Lists available datasets |
| `/health` | Liveness & feature count check |

</div>

---

### 🔧 Customization

<details>
<summary><b>📂 Data Paths</b></summary>

To add new datasets or change paths, edit the `DATA_PATHS` dict:

```python
DATA_PATHS = {
    "Micro_Plates_and_Major_Fault_Zones": os.path.join(BASE_DIR, "data/Micro_Plates_and_Major_Fault_Zones.geojson"),
    "Plate_Interface": os.path.join(BASE_DIR, "data/Plate_Interface.geojson"),
    "Plate_Motion": os.path.join(BASE_DIR, "data/Plate_Motion.geojson"),
    "New_Dataset": os.path.join(BASE_DIR, "data/New_Dataset.geojson")  # new
}
```

Then add it to the `DATASETS` dict:

```python
DATASETS = {
    # ...
    "New_Dataset": New_Dataset,
}
```
</details>

<details>
<summary><b>🌐 Port and Host</b></summary>

Edit the `app.run()` line:

```python
app.run(host="0.0.0.0", port=8080, debug=False)
```
</details>

<details>
<summary><b>🔒 CORS Policy</b></summary>

To restrict CORS to a specific domain instead of opening it to all:

```python
response.headers["Access-Control-Allow-Origin"] = "https://yourdomain.com"
```
</details>

<details>
<summary><b>📋 Metadata Update</b></summary>

Edit developer info in the constants at the top of `app.py`:

```python
API_NAME = "Fault Lines API"
API_VERSION = "1.0.0"
DEVELOPER = "Emin Neşat Gürses"
GITHUB = "https://github.com/mdaedalus"
EMAIL = "eminnesatg@gmail.com"
NICKNAME = "mdaedalus"
```
</details>

<details>
<summary><b>🎨 Response Format</b></summary>

To return compact JSON instead of pretty-print, remove the `indent=2` parameter inside `json_response()`:

```python
json.dumps(payload, ensure_ascii=False)
```
</details>

---

### 🗺️ Roadmap

- [x] 🟢 v0.1 — Merge three datasets into one response
- [x] 🟢 v0.2 — GeoJSON-compatible output
- [x] 🟢 v0.3 — CORS support
- [x] 🟢 v0.4 — Metadata + UTC timestamp
- [x] 🟢 v0.5 — Meaningful error handling
- [x] 🟢 v0.6 — Dataset-based filtering (`?dataset=`)
- [x] 🟢 v0.7 — Bounding box filter (`?bbox=`)
- [x] 🟢 v0.8 — `/health` endpoint
- [x] 🟢 v0.9 — `/datasets` endpoint
- [ ] 🟡 v1.0 — GeoJSON export endpoints (single dataset download)
- [ ] 🟠 v1.1 — Redis cache layer
- [ ] 🟠 v1.2 — Prometheus metrics
- [ ] 🟠 v1.3 — Rate limiting
- [ ] 🔴 v1.4 — Docker image
- [ ] 🔴 v2.0 — External geological APIs (USGS, GEM) integration

---

### 🤝 Contributing

Contributions are welcome! For major changes, please open an **issue** first.

```bash
# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/new-feature
git commit -m "feat: added new feature"
git push origin feature/new-feature
```

#### Commit Conventions

| Prefix | Meaning |
|:-------|:--------|
| `feat:` | new feature |
| `fix:` | bug fix |
| `docs:` | documentation |
| `style:` | code formatting |
| `refactor:` | refactoring |
| `test:` | adding tests |

---

### ⚠️ Disclaimer

This API serves geological plate and fault zone data from **open sources**. It is **not** an official body and **must not be used as the sole basis for critical geological decisions**. Always refer to relevant institutions for academic or official data.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Emin Neşat Gürses**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Emin_Neşat_Gürses-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emin-ne%C5%9Fat-g%C3%BCrses-35723a284/)
[![Email](https://img.shields.io/badge/Email-eminnesatg@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:eminnesatg@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-@mdaedalus-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mdaedalus)

</div>

---

<div align="center">

### ⭐ If you like this project, don't forget to star it!

[![Star](https://img.shields.io/badge/⭐_Star_this_repo-yellow?style=for-the-badge)](https://github.com/mdaedalus/Fault-Lines-API)
[![Report Bug](https://img.shields.io/badge/🐛_Report_Bug-red?style=for-the-badge)](https://github.com/mdaedalus/Fault-Lines-API/issues)
[![Request Feature](https://img.shields.io/badge/💡_Request_Feature-blue?style=for-the-badge)](https://github.com/mdaedalus/Fault-Lines-API/issues)

**Made with ❤️ in Turkey**

</div>
