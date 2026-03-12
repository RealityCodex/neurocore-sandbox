import unittest

from examples.train_fire_avoidance import evaluate_agent, train_agent


class LearningTests(unittest.TestCase):
    def test_training_learns_to_reach_goal_more_than_fire(self):
        env, agent, _ = train_agent(episodes=600)
        results = evaluate_agent(env, agent, episodes=150)

        self.assertGreater(results["goal_rate"], 0.80)
        self.assertLess(results["fire_rate"], 0.10)


if __name__ == "__main__":
    unittest.main()
