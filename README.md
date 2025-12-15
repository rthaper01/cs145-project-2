# There's No Business Like Show Business (Redux) — BigQuery + ML (CS145 Project 2)

This repository contains my second project for the Fall 2025 edition of Stanford University's CS145 (Introduction to Big Data Systems) class.

It demonstrates **quantitative data engineering** and **statistical modeling** using **Google BigQuery** at scale, including advanced SQL patterns (CTEs, window functions, correlated subqueries, UDFs), exploratory analysis, and **two predictive ML models trained/evaluated inside BigQuery**.

> **Note on reproducibility:** The original work ran against BigQuery datasets accessible via my course credentials.  
> The notebook in `notebooks/` contains the full analysis *and saved outputs*, so reviewers can read results without running code.

---

## What’s inside

### Data engineering + analytics (BigQuery SQL)
The notebook includes a set of queries and visualizations answering questions like:

- Moving **5-year average IMDB ratings** comparing original screenplays vs adaptations (CTEs + window functions)
- **Genre performance** by decade vs expected baselines (CTEs + correlated subqueries)
- Ranking **actor–director pairings** by a collaboration score (UDF + CTEs + windows)
- Identifying **flops vs sleeper hits** under a budget cap (CTEs)
- ROI vs expected ROI by decade; relationships between macro signals (GDP, sentiment) and revenue changes (CTEs + windows)

Extracted SQL is also provided in `sql/` for quick review.

### Predictive modeling (BigQuery ML)
Two models are trained and evaluated in BigQuery ML:

1. **Adaptation success model:** predict how successful a book-to-movie adaptation will be.
2. **Hit prediction model:** classify whether a movie will be a “hit” from engineered features.

Evaluation outputs (e.g., accuracy/precision/recall/F1/AUC and error metrics like RMSE/MAE where applicable) are preserved in the notebook.

---

## Quickstart (optional)

If you *do* want to re-run the pipeline, you’ll need:
- a GCP project with BigQuery enabled
- access to equivalent datasets/tables (the course project used private tables)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export GCP_PROJECT_ID="<your-gcp-project-id>"
```

Then open the notebook:

```bash
jupyter lab
```

---

## Repository layout

- `notebooks/`
  - `cs145_project2_show_business_redux.ipynb` — cleaned notebook with outputs (recommended for review)
  - `original_submission.ipynb` — original submitted notebook for reference
- `sql/` — extracted BigQuery SQL queries
- `src/` — small “productionization” helpers (BigQuery client wrapper, metric helpers, plotting utilities)
- `reports/figures/` — figures extracted from the notebook (to keep the repo lightweight and GitHub-friendly)

---

## Why this is a good quant/data engineering code sample

- Emphasizes **data + modeling end-to-end**: feature construction → analysis → prediction → evaluation.
- Demonstrates **SQL fluency** with patterns that matter in production analytics.
- Uses **BigQuery ML** to keep modeling close to data (cost-aware, scalable).
- Presents results clearly and reproducibly (saved outputs + extracted queries).

---

## Credits (privacy-preserving)

This was a partnered course project.

**My contributions**
- Project structure + core analytics narrative
- BigQuery query design (CTEs/windows/correlated subqueries/UDF usage) and iteration
- Modeling pipeline, evaluation, and interpretation write-ups (as reflected in the notebook)

**Partner contributions**
- Data cleaning/joins and exploratory analysis support (as described in the “Assigned work” section of the notebook)

---

## License

MIT — see `LICENSE`.
