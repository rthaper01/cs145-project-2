"""BigQuery helper utilities (credentials via ADC)."""
from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Optional

from google.cloud import bigquery

@dataclass(frozen=True)
class BQConfig:
    project_id: str = os.getenv("GCP_PROJECT_ID", "")
    location: str = os.getenv("BQ_LOCATION", "US")

def client(config: Optional[BQConfig] = None) -> bigquery.Client:
    """Create a BigQuery client using Application Default Credentials."""
    cfg = config or BQConfig()
    if not cfg.project_id:
        # Let google-cloud-bigquery infer project if possible.
        return bigquery.Client()
    return bigquery.Client(project=cfg.project_id, location=cfg.location)

def query(sql: str, *, cfg: Optional[BQConfig] = None) -> bigquery.table.RowIterator:
    """Run a SQL query and return an iterator of rows."""
    bq = client(cfg)
    job = bq.query(sql)
    return job.result()
