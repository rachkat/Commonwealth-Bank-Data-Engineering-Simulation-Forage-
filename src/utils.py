from __future__ import annotations
import pandas as pd

def monthly_agg(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate monthly volume and spend per region."""
    g = df.copy()
    g["month"] = g["txn_timestamp"].astype("datetime64[M]")
    return g.groupby(["region","month"], as_index=False).agg(
        txn_count=("txn_id", "count"),
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
    )
