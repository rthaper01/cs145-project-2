"""Plotting helpers (matplotlib-based)."""
from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd

def savefig(path: str) -> None:
    plt.tight_layout()
    plt.savefig(path, dpi=200, bbox_inches="tight")

def lineplot(df: pd.DataFrame, x: str, y: str, *, title: str = "", xlabel: str = "", ylabel: str = "") -> None:
    plt.figure()
    plt.plot(df[x], df[y])
    plt.title(title)
    plt.xlabel(xlabel or x)
    plt.ylabel(ylabel or y)
