import pandas as pd

CO2_FACTOR = 3.16


def compute_fuel_burn(flight_df, fuel_coeff=0.00002):
    """
    Estimate fuel burn using simplified velocity-based proxy model.
    """

    df = flight_df.copy()

    dt = df["t"].diff().fillna(10)

    df["fuel_burn"] = fuel_coeff * (df["v"] ** 2) * dt

    return df


def compute_co2(df):
    """
    Compute CO2 emissions from fuel burn.
    """

    df = df.copy()

    df["co2"] = df["fuel_burn"] * CO2_FACTOR

    return df
