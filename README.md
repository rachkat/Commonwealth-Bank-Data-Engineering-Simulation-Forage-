# Commonwealth Bank Data Science/Engineering Simulation

> Portfolio project based on a job simulation focusing on data engineering and analysis with realistic transactional data.

## 🧭 Project Overview
This repo demonstrates:
- The importance of data engineering & analysis in a long-term, data-focused vision.
- Working with realistic transactional data (cleaning, validation, feature building).
- Answering concrete business questions with analysis and clear communication.

## 📂 Repository Structure
```
.
├── data/
│   ├── raw/                # (Place original dataset here; keep as-read-only; do NOT commit if restricted)
│   └── processed/          # Cleaned/derived datasets safe to share
├── notebooks/              # EDA, modeling, and storytelling notebooks
├── src/                    # Reusable Python modules (ETL, features, utils)
├── reports/
│   └── figures/            # Exported charts
├── docs/                   # Write-ups, diagrams, and notes
└── .github/workflows/      # CI: linting & tests
```

## 🚀 Quickstart
```bash
# 1) Create and activate a virtual environment (one option shown)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run data pipeline example
python -m src.pipeline_example
```

## 🔐 Data Policy
- If the simulation T&Cs restrict publishing raw data, **do not commit** files in `data/raw/`. 
- Use the provided `DATA_README.md` to describe how a reviewer can obtain or simulate data.
- Commit **synthetic samples** instead (see `data/raw/sample_transactions.csv`).

## 📝 What this project answers (examples)
- Transactional summary metrics (e.g., monthly volume, avg basket size, churn proxy).
- Segmentation by customer/product/region.
- Anomaly detection or rule-based fraud signals (optional).
- Simple feature table for downstream modeling.

## 📊 Reproducible Outputs
- Key charts exported to `reports/figures/`.
- Notebook to PDF/HTML exports in `reports/` (optional).

## 🧪 Tests
Minimal examples included under `src/` to validate core transforms.

## 🧰 Tech Stack
- Python, Pandas, Polars (optional), PyTest
- Jupyter for EDA
- Pre-commit hooks for formatting (Black, isort, Ruff)

## 📄 License
MIT — see `LICENSE`.

---

*Last updated: 2025-08-14*
