from src.dynamics.trajectory import generate_baseline_trajectory
from src.emissions.fuel import compute_fuel_burn, compute_co2
from src.optimization.scenario import apply_hydrogen_scenario, compute_savings

def run_experiment(fuel_reduction=0.6):
    df = generate_baseline_trajectory()
    df = compute_fuel_burn(df)
    df = compute_co2(df)

    df = apply_hydrogen_scenario(df, fuel_reduction)
    df = compute_savings(df)

    total_savings = df["co2_savings"].sum()

    return df, total_savings