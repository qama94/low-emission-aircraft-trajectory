# Low-Emission Aircraft Trajectory Analysis

Exploratory trajectory analysis comparing conventional A320 and hydrogen fuel 
cell aircraft on European short-haul routes, with mixed-fleet ATM capacity 
implications.

## Research question

How do the operational trajectory constraints of hydrogen fuel cell aircraft 
differ from conventional aircraft on European short-haul routes, and what are 
the implications for mixed-fleet climb sector occupancy?

## Background and motivation

OpenAP (Sun et al., 2020) provides a validated open framework for conventional 
aircraft trajectory modelling using ADS-B surveillance data. Onorato et al. 
(2022, TU Delft) quantified hydrogen aircraft performance parameters at the 
design level but did not study operational trajectories or ATM implications. 
This project bridges both — applying Onorato's performance parameters within 
the OpenAP framework to assess mixed-fleet airspace capacity on a real European 
corridor.

## Methodology

Three modules:

**Module 1 — Conventional A320 baseline**  
Full trajectory generated using OpenAP FlightGenerator. Fuel flow calculated 
using OpenAP FuelFlow model across all flight phases.

**Module 2 — Hydrogen fuel cell aircraft model**  
A320 parameters modified using Onorato et al. (2022) SMR hydrogen aircraft data:
- TSFC ratio: 0.357 (hydrogen vs kerosene specific energy)
- MTOM: 62,370 kg (−5.5%)
- L/D penalty: −5% (Option B only)

Two modelling assumptions compared:
- Option A: fuel flow scaling only, kinematic profile unchanged
- Option B: fuel flow scaling + 5% climb rate penalty

**Module 3 — Mixed-fleet capacity analysis**  
Climb sector occupancy modelled across hydrogen fleet penetration scenarios 
(0–100%) on the Amsterdam–London corridor (50 daily flights).

## Key results

| Metric | Value |
|--------|-------|
| Conventional A320 climb duration | 22.3 min |
| Hydrogen climb duration (Option B) | 23.5 min |
| Extra climb time per flight | +1.2 min (+5.3%) |
| Fuel reduction (hydrogen vs conventional) | −65.7% |
| Extra sector occupancy at 50% penetration | 29.4 min/day |
| Climb sector capacity impact at 100% penetration | +5.3% |

## Figures

![A320 conventional baseline trajectory](figures/01_baseline_trajectory.png)

![A320 conventional vs hydrogen fuel cell trajectory comparison](figures/02_trajectory_comparison.png)

![Mixed-fleet capacity implications Amsterdam-London corridor](figures/03_mixed_fleet_capacity.png)

## Limitations and future work

- Kinematic parameters are held constant from conventional A320 WRAP model — 
  no validated ADS-B data exists yet for hydrogen aircraft in commercial operation
- Option B climb penalty is a first-order approximation from design-level data
- Single corridor analysis — network-level implications not modelled
- Full validation requires operational data from hydrogen aircraft test flights

This project is a small-scale exploration of the methodological gap that 
ZEUS (Horizon Europe) addresses at the system level.

## References

- Sun, J., Hoekstra, J.M., Ellerbroek, J. (2020). OpenAP: An open-source 
  aircraft performance model for air transportation studies and simulations. 
  *Aerospace*, 7(8), 104.
- Sun, J., Ellerbroek, J., Hoekstra, J.M. (2019). WRAP: An open-source 
  kinematic aircraft performance model. *Transportation Research Part C*, 98, 118–138.
- Onorato, G., Proesmans, P., Hoogreef, M.F.M. (2022). Assessment of hydrogen 
  transport aircraft: Effects of fuel tank integration. 
  *CEAS Aeronautical Journal*, 13, 813–845.
- Schäfer, M. et al. (2014). Bringing up OpenSky: A large-scale ADS-B sensor 
  network for research. *IPSN*, 83–94.

## Requirements

Install dependencies:

```bash
pip install openap matplotlib pandas numpy
```