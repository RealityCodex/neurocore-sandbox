class FireGridWorld:
    """Deterministic 5x5 grid for learning fire avoidance."""

    ACTIONS = ("up", "down", "left", "right")

    def __init__(
        self,
        size=5,
        start=(0, 0),
        fire=(2, 2),
        goal=(4, 4),
        step_penalty=-0.04,
        fire_penalty=-1.0,
        goal_reward=1.0,
        max_steps=30,
    ):
        self.size = size
        self.start = start
        self.fire = fire
        self.goal = goal
        self.step_penalty = step_penalty
        self.fire_penalty = fire_penalty
        self.goal_reward = goal_reward
        self.max_steps = max_steps
        self.agent = start
        self.steps = 0
        self.last_reward = 0.0

    def reset(self):
        self.agent = self.start
        self.steps = 0
        self.last_reward = 0.0
        return self.observe()

    def observe(self):
        return {
            "agent": self.agent,
            "fire": self.fire,
            "goal": self.goal,
            "last_reward": self.last_reward,
        }

    def step(self, action):
        x, y = self.agent
        if action == "up":
            y = max(0, y - 1)
        elif action == "down":
            y = min(self.size - 1, y + 1)
        elif action == "left":
            x = max(0, x - 1)
        elif action == "right":
            x = min(self.size - 1, x + 1)
        else:
            raise ValueError(f"Unsupported action: {action}")

        self.agent = (x, y)
        self.steps += 1

        reward = self.step_penalty
        done = False
        event = "step"

        if self.agent == self.fire:
            reward = self.fire_penalty
            done = True
            event = "fire"
        elif self.agent == self.goal:
            reward = self.goal_reward
            done = True
            event = "goal"
        elif self.steps >= self.max_steps:
            done = True
            event = "timeout"

        self.last_reward = reward
        return self.observe(), reward, done, {"event": event}
