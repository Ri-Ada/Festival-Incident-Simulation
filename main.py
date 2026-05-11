from simulator import (
    SimulationEngine, 
    IncidentFactory
)
def main():
    engine=SimulationEngine()
    for _ in range(5):
        incident=IncidentFactory.create_incident()
        engine.add_incident(incident)
        engine.run(5)
        print("Reports:")
        for report in engine.get_reports():
            print(report)
if __name__ == "__main__":
        main()
