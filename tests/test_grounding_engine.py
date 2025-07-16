import unittest
from env.grounding_engine import GroundingEngine

class TestGroundingEngine(unittest.TestCase):
    def test_grounding_engine_runs(self):
        engine = GroundingEngine()
        try:
            engine.run()
            success = True
        except Exception as e:
            print(f"GroundingEngine run() failed: {e}")
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()

