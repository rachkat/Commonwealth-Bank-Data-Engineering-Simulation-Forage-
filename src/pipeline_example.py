"""
Minimal example pipeline: read raw, transform, write processed.
"""
from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "sample_transactions.csv"
OUT = Path(__file__).resolve().parents[1] / "data" / "processed" / "transactions_clean.csv"

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Basic cleaning
    df["txn_timestamp"] = pd.to_datetime(df["txn_timestamp"], errors="coerce")
    df = df.dropna(subset=["txn_timestamp", "amount"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    return df

def main():
    df = pd.read_csv(RAW)
    df = clean(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"Wrote {len(df)} rows -> {OUT}")

if __name__ == "__main__":
    main()
