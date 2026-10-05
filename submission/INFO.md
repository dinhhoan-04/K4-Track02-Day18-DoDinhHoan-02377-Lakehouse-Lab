# K4-Track02-Day18 — Thông tin nộp bài

- **Họ và tên:** Đỗ Đình Hoàn
- **MSSV:** 02377
- **Mã bài lab:** `K4-Track02-Day18`
- **Tên repository:** `K4-Track02-Day18-DoDinhHoan-02377-Lakehouse-Lab`
- **Đường chạy:** Lightweight path (Python APIs, offline, zero JVM/Docker)
- **Môi trường thực thi:** Python 3.12.8 (Windows 11)
- **Phiên bản thư viện chính:**
  - `deltalake`: 1.6.6
  - `pyiceberg`: 0.12.0
  - `duckdb`: 1.5.6
  - `polars`: 1.44.2
  - `pyarrow`: 25.0.1
  - `numpy`: 2.5.3

## Kết quả kiểm thử Reproducibility

- **Smoke test (`verify_lite.py`):** 9/9 PASS
- **Pytest test suite (`pytest`):** 24/24 PASS
- **Headless notebook suite (`run_all.py`):** 8/8 PASS (34.8 giây)

## Cấu trúc thư mục bài nộp

```text
submission/
├── INFO.md
├── REFLECTION.md
├── notebooks/
│   ├── 01_delta_basics.ipynb
│   ├── 02_optimize_zorder.ipynb
│   ├── 03_time_travel.ipynb
│   ├── 04_medallion.ipynb
│   ├── 05_iceberg_catalog.ipynb
│   ├── 06_maintenance.ipynb
│   ├── 07_vectors_multimodal.ipynb
│   └── 08_agents_provenance.ipynb
├── screenshots/
│   ├── nb01_delta_log.png
│   ├── nb02_optimize.png
│   ├── nb03_time_travel.png
│   ├── nb04_medallion.png
│   ├── nb05_iceberg_catalog.png
│   ├── nb06_maintenance.png
│   ├── nb07_vectors_multimodal.png
│   └── nb08_agents_provenance.png
└── bonus/
    ├── ARCHITECTURE.md
    └── poc/
        └── tokenization_poc.py
```
