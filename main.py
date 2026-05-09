from abc import ABC, abstractmethod
import random

class Incident(ABC):
    def __init__(self, severity):
        self._severity=severity
    @abstractmethod
    def resolve(self):
        pass
    @abstractmethod
    def escalate(self):
        pass
    def transform(self):
        return None
class Fire(Incident):
    def __init__(self, severity, fire_type):
        super().__init__(severity)
        self.__type=fire_type
    def resolve(self):
        fire_difficulty={
            "electrical":0.4,
            "gas": 0.4,
            "chemical":0.6        
            }
        base_success=fire_difficulty.get(self.__type, 0.5)
        success_rate=max(0.05, base_success - self._severity * 0.02)
        success=random.random() < success_rate
        if success:
            return ResolutionReport(
                True,
                "Fire extinguised",
                self.__type
            )
        self.escalate()
        return ResolutionReport(
            False,
            "Fire spreading.Run.",
            self.__type
        )
    def escalate(self):
        self._severity=min(10, self._severity +2)
class Overdose(Incident):
    def __init__(self, drug, severity):
        super().__init__(severity)
        self.__drug=drug
    def resolve(self):
        drug_difficulty={
            "nitrous_oxide":0.2,
            "ketamine":0.4,
            "opioid":0.6,
            "fentanyl":0.8,
            "unknown":0.5
        }
        base_success=drug_difficulty.get(self.__drug, 0.5)
        success_rate=max(0.05, base_success - self._severity * 0.03)
        success = random.random() < success_rate
        if success:
            return ResolutionReport(
                True, 
                "Patient stabilised",
                "Overdose"
            )
        self.escalate()
        return ResolutionReport(
            False,
            "Doctors praying as intervention is ongoing",
            "Overdose"
        )

    def escalate(self):
        self._severity=min(10, self._severity + 1)
class DrunkFight(Incident):
    def __init__(self, severity, people_count):
        super().__init__(severity)
        self.__people_count=people_count
    def transform(self):
        if self.__people_count >= 20:
            return Riot(
                self._severity,
                self.__people_count
            )
        return None
    def resolve(self):
        success_rate=max(
            0.1,
            0.8-self.__people_count * 0.05 - self._severity*0.02)
        success=random.random() < success_rate
        if success:
            return ResolutionReport(
                True, 
                "Fight was solved by security",
                "DrunkFight"
            )
        self.escalate()
        return ResolutionReport(
            False, 
            "Seems like we have the whole UFC division out there.",
            "DrunkFight"
        )
    def escalate(self):
        self._severity=min(10, self._severity +1)
        self.__people_count += random.randint(1, 5)
class Riot(Incident):
    def __init__(self, severity, people_count):
        super().__init__(severity)
        self.__people_count=people_count
    @property
    def people_count(self):
        return self.__people_count
    def resolve(self):
        success_rate=max(
            0.05,
            0.6 - self.__people_count*0.02-self._severity*0.02)
        success=random.random() < success_rate
        if success:
            return ResolutionReport(
                True, 
                "Riot under control, thanks to the millitary.",
                "Riot"
            )
        self.escalate()
        return ResolutionReport(
            False,
            "Frenchmans decided to stsrt another revolution today. Waiting for group Alpha",
            "Riot"
        )
    def escalate(self):
        self._severity=min(10, self._severity+3)
class ResolutionReport:
    def __init__(self, success, message, type):
        self._success=success
        self._message=message
        self._type=type
    @property
    def success(self):
        return self._success
    def __str__(self):
        return f"[{self._type}] {self._message}"
class SimulationEngine:
    def __init__(self):
        self._active_incidents=[]
        self._reports=[]
    def add_incident(self, incident):
        self._active_incidents.append(incident)
    def get_reports(self):
        return self._reports
    def tick(self):
        new_incidents=[]
        for incident in self._active_incidents:
            transformed=incident.transform()
            if transformed:
                new_incidents.append(transformed)
                continue
            report=incident.resolve()
            self._reports.append(report)
            if not report.success:
                new_incidents.append(incident)
        self._active_incidents=new_incidents
    def run(self, steps):
        for _ in range(steps):
            self.tick()
class IncidentFactory:
    @staticmethod
    def create_incident():
        pass

