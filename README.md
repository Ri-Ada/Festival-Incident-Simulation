Festival simulation system

A simulation of festival management, where incidents appear and staff members attempt to resolve them based on their roles and chosen strategies. 
The simulation runs in ticks. Cycle of each tick:
Events/Incidents appear - Available staff check incidents - Strategy chosen - Staff attempts - Outcome (successful/unsuccessful) - Unresolved incidents escalate
Incidents appear randomly during the simulation. Each incident requires a specific type of staff. Staff attempts to resolve incidents using strategies. If not resolved, incidents escalate over time.

Components:
-SimulationEngine: controls the simulation loop, stores staff and active incidents, assigns staff, and triggers resolution. 
-Incident(ABC):
Attributes: severity (1-10). Methods: resolve(staff, strategy), escalate(), handled_by(staff)
-Incident Subclasses:
DrunkFight: handled by SecurityStaff, severity (1–4)
Overdose: handled by MedicalStaff,severity(4–9)
Fire: handled by Firefighter, severity (5–10)
-Staff(ABC):
Methods: handle(incident, strategy), choose_strategy()
-Staff Subclasses:
SecurityStaff, Firefighter, MedicalStaff
-Strategy(ABC):
Methods: bonus(), failure_chance()
-Strategy Subclasses:
BasicStrategy(small bonus, reliable)
RiskyStrategy(higher bonus, may fail even if condition is met)

How it works:
Resolution: success = strategy_bonus >= severity (risky may still fail).
Escalation:
DrunkFight: +1 severity
Overdose: +1 severity
Fire: +2 severity
If severity reaches 10, it cannot increase further.
Strategy selection:
Firefighter:
70% RiskyStrategy
30% BasicStrategy
MedicalStaff:
40% RiskyStrategy
60% BasicStrategy
SecurityStaff:
30% RiskyStrategy
70% BasicStrategy
Incident: removed if solved, stays active if failed.