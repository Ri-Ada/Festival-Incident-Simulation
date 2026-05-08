from abc import ABC, abstractmethod
import random

class Incident(ABC):
    def __init__(self, severity):
        self._severity=severity
    @abstractmethod
    def resolve(self):
        pass
    def escalate(self):
        pass
class Fire(Incident):
    def __init__(self, severity, type):
        super().__init__(severity)
        self.__type=type
    def resolve(self):
        success=random.random() > 0.3
        if success:
            return ResolutionReport(
                True,
                "Fire extinguised",
                self.__type
            )
        self.escalate()
        return ResolutionReport(
            False,
            "Fire spreading",
            self.__type
        )
    def escalate(self):
        self._severity=min(10, self._severity +2)
class Overdose(Incident):
    def __init__(self, drug, severity):
        super().__init__(severity)
        self._drug=drug
    def resolve(self):
        pass
    def escalate(self):
        pass
class DrunkFight(Incident):
    def __init__(self, severity, people_count):
        super().__init__(severity)
        self._people_count=people_count
    def resolve(self):
        pass
    def escalate(self):
        pass
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
    def tick(self):
        pass
class IncidentFactory:
    @staticmethod
    def create_incident():
        pass


