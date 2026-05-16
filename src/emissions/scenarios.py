def apply_hydrogen_scenario(df, efficiency_factor=0.4):
    """
    Simple scenario model for hydrogen aircraft.

    Assumption:
    Hydrogen aircraft reduces effective fuel-related emissions.
    This is a HIGH-LEVEL research approximation, not engine physics.
    """

    df = df.copy()

    df["fuel_burn_h2"] = df["fuel_burn"] * efficiency_factor

    df["co2_h2"] = df["fuel_burn_h2"] * 3.16

    df["co2_savings"] = df["co2"] - df["co2_h2"]

    return df