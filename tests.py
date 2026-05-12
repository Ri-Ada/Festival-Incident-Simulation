import unittest
from simulator import *
class TestFire(unittest.TestCase):
    def test_fire_creation(self):
        fire=Fire(5, "gas")
        self.assertEqual(fire._severity, 5)
        self.assertEqual(fire._type, "gas")
    def test_fire_escalation(self):
        fire=Fire(5, "gas")
        fire.escalate()
        self.assertEqual(fire._severity, 7)
    def test_fire_resolution(self):
        fire=Fire(5, "gas")
        report=fire.resolve()
        self.assertIsInstance(report, ResolutionReport)
class TestOverdose(unittest.TestCase):
    def test_overdose_creation(self):
        overdose=Overdose("opioid", 3)
        self.assertEqual(overdose._drug, "opioid")
        self.assertEqual(overdose._severity, 3)
    def test_overdose_escalation(self):
        overdose=Overdose("opioid", 3)
        overdose.escalate()
        self.assertEqual(overdose._severity, 4)
    def test_overdose_resolution(self):
        overdose=Overdose("fentanyl", 2)
        report=overdose.resolve()
        self.assertIsInstance(report, ResolutionReport)
class TestDrunkFight(unittest.TestCase):
    def test_fight_creation(self):
        fight=DrunkFight(3, 10)
        self.assertEqual(fight._severity, 3)
        self.assertEqual(fight._people_count, 10)
    def test_fight_escalation(self):
        fight=DrunkFight(5, 10)
        first_people_count=fight._people_count
        fight.escalate()
        self.assertEqual(fight._severity, 6)
        self.assertTrue(fight._people_count >= first_people_count)
    def test_fight_resolution(self):
        fight=DrunkFight(2, 3)
        report=fight.resolve()
        self.assertIsInstance(report, ResolutionReport)
    def test_transformation_to_riot(self):
        fight=DrunkFight(5, 25)
        riot=fight.transform()
        self.assertIsInstance(riot, Riot)
    def test_no_transformation(self):
        fight=DrunkFight(5, 3)
        self.assertIsNone(fight.transform())
class TestRiot(unittest.TestCase):
    def test_riot_creation(self):
        riot=Riot(5, 30)
        self.assertEqual(riot._severity, 5)
        self.assertEqual(riot._people_count, 30)
    def test_riot_escalation(self):
        riot=Riot(5, 25)
        riot.escalate()
        self.assertEqual(riot._severity, 8)
    def test_riot_resolution(self):
        riot=Riot(5, 27)
        report=riot.resolve()
        self.assertIsInstance(report, ResolutionReport)
class TestResolutionReport(unittest.TestCase):
    def test_report_creation(self):
        report=ResolutionReport(
            True, 
            "Success",
            "Fire"
        )
        self.assertTrue(report.success)
class TestSimulationEngine(unittest.TestCase):
    def test_engine_creation(self):
        engine=SimulationEngine()
        self.assertEqual(len(engine._active_incidents), 0)
    def test_adding_incident(self):
        engine=SimulationEngine()
        fire=Fire(3, "electrical")
        engine.add_incident(fire)
        self.assertEqual(len(engine._active_incidents), 1)
    def test_tick(self):
        engine=SimulationEngine()
        fire=Fire(3, "electrical")
        engine.add_incident(fire)
        engine.tick()
        self.assertTrue(len(engine.get_reports()) >=1)
    def test_run(self):
        engine=SimulationEngine()
        for _ in range(3):
            incident=IncidentFactory.create_incident()
            engine.add_incident(incident)
            engine.run(5)
            self.assertTrue(len(engine.get_reports()) >= 1)
class TestIncidentFactory(unittest.TestCase):
    def test_factory(self):
        incident=IncidentFactory.create_incident()
        self.assertIsNotNone(incident)
if __name__=="__main__":
    unittest.main()
