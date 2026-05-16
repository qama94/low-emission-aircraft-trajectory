from openap.gen import FlightGenerator

def generate_baseline_trajectory(aircraft='A320', dt=10):
    fgen = FlightGenerator(ac=aircraft)
    flight = fgen.complete(dt=dt)
    return flight