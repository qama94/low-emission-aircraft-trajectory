def apply_hydrogen_scenario(df, fuel_reduction=0.6):
    """
    Simulate hydrogen/low-emission aircraft by reducing fuel burn.
    """
    df = df.copy()

    if "fuel_burn" in df.columns:
        df["fuel_burn_h2"] = df["fuel_burn"] * (1 - fuel_reduction)
        df["co2_h2"] = df["fuel_burn_h2"] * 3.16

    return df


def compute_savings(df):
    """
    Compute emission savings between baseline and hydrogen scenario.
    """
    df = df.copy()

    df["co2_savings"] = df["co2"] - df["co2_h2"]

    return df