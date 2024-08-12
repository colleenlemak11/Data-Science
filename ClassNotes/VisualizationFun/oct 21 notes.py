# Oct 21 Notes

import pandas as pd

def warmup_task():
    msrp_df = pd.read_csv("msrp.csv")
    print(msrp_df)
    print()
    new_row = pd.Series(["chevy corvette", 77, 2212], index=["CarName", "ModelYear", "MSRP"])
    msrp_df = msrp_df.append(new_row, ignore_index=True)
    print(msrp_df)
    print()
    counts_series = msrp_df["ModelYear"].value_counts() # counts number of unique values in ModelYear column
    print(counts_series)
    print()
    # split-apply-combine
    # split on ModelYear, apply mean to MSRP, combine mean MSRPs
    grouped_by_modelyear = msrp_df.groupby("ModelYear")
    mean_msrp_ser = grouped_by_modelyear["MSRP"].mean()
    print(mean_msrp_ser)
    print()

warmup_task()