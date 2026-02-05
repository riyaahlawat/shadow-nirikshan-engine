import pandas as pd

def compute_silence_baseline(
    usage_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes average usage during silence for each building and resource.
    Returns a baseline DataFrame.
    """

    silence_df = usage_df[usage_df["is_silence"] == True]

    baseline = (
        silence_df
        .groupby(["building", "resource"])["usage"]
        .mean()
        .reset_index()
        .rename(columns={"usage": "baseline_usage"})
    )

    return baseline
