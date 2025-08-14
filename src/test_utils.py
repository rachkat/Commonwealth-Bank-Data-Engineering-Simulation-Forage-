import pandas as pd
from src.utils import monthly_agg

def test_monthly_agg():
    df = pd.DataFrame({
        "txn_id":[1,2],
        "txn_timestamp": pd.to_datetime(["2025-01-01","2025-01-10"]),
        "amount":[10.0, 20.0],
        "region":["NSW","NSW"]
    })
    out = monthly_agg(df)
    assert out["txn_count"].iloc[0] == 2
    assert round(out["total_amount"].iloc[0],2) == 30.00
