import random
from collections import defaultdict


class QLearningAgent:
    """Small tabular Q-learning agent for the sandbox MVP."""

    def __init__(
        self,
        actions,
        learning_rate=0.2,
        discount=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,
        min_epsilon=0.05,
        seed=7,
    ):
        self.actions = list(actions)
        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.random = random.Random(seed)
        self.q_table = defaultdict(lambda: {action: 0.0 for action in self.actions})

    def choose_action(self, state, training=True):
        if training and self.random.random() < self.epsilon:
            return self.random.choice(self.actions)

        action_values = self.q_table[state]
        max_value = max(action_values.values())
        best_actions = [
            action for action, value in action_values.items() if value == max_value
        ]
        return self.random.choice(best_actions)

    def update(self, state, action, reward, next_state, done):
        current_value = self.q_table[state][action]
        next_best = 0.0 if done else max(self.q_table[next_state].values())
        target = reward + self.discount * next_best
        self.q_table[state][action] = current_value + self.learning_rate * (
            target - current_value
        )

    def decay_exploration(self):
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)
