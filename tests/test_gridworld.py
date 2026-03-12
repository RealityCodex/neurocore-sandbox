import unittest

from env.gridworld import FireGridWorld


class GridWorldTests(unittest.TestCase):
    def test_fire_tile_ends_episode_with_negative_reward(self):
        env = FireGridWorld(start=(2, 1), fire=(2, 2), goal=(4, 4))
        env.reset()
        _, reward, done, info = env.step("down")

        self.assertTrue(done)
        self.assertEqual(info["event"], "fire")
        self.assertLess(reward, 0)

    def test_goal_tile_ends_episode_with_positive_reward(self):
        env = FireGridWorld(start=(3, 4), fire=(1, 1), goal=(4, 4))
        env.reset()
        _, reward, done, info = env.step("right")

        self.assertTrue(done)
        self.assertEqual(info["event"], "goal")
        self.assertGreater(reward, 0)


if __name__ == "__main__":
    unittest.main()
