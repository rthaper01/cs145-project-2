"""Modeling helpers.

This repo is intended primarily as a *code sample*; the notebook contains the full
end-to-end analysis and saved outputs. These helpers show how the project would be
productionized (clean interfaces, reproducible preprocessing, evaluation hooks).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, Optional

import numpy as np
import pandas as pd

@dataclass(frozen=True)
class SplitConfig:
    test_size: float = 0.2
    random_state: int = 145

def train_test_split_df(df: pd.DataFrame, *, cfg: Optional[SplitConfig] = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Simple deterministic split for tabular data."""
    from sklearn.model_selection import train_test_split
    c = cfg or SplitConfig()
    train, test = train_test_split(df, test_size=c.test_size, random_state=c.random_state)
    return train, test

def classification_report_dict(y_true, y_pred, y_score=None) -> Dict[str, Any]:
    """Return a compact dict of common classification metrics."""
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
    out = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }
    if y_score is not None:
        try:
            out["auc"] = float(roc_auc_score(y_true, y_score))
        except Exception:
            pass
    return out
