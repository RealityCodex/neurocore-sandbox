from core.agent import QLearningAgent
from core.grounding import ground_observation, grounding_state_key
from env.gridworld import FireGridWorld


def run_episode(env, agent, training=True):
    observation = env.reset()
    total_reward = 0.0
    touched_fire = False
    reached_goal = False

    while True:
        grounded = ground_observation(observation)
        state = grounding_state_key(grounded)
        action = agent.choose_action(state, training=training)
        next_observation, reward, done, info = env.step(action)
        next_state = grounding_state_key(ground_observation(next_observation))

        if training:
            agent.update(state, action, reward, next_state, done)

        total_reward += reward
        touched_fire = touched_fire or info["event"] == "fire"
        reached_goal = reached_goal or info["event"] == "goal"
        observation = next_observation

        if done:
            break

    return {
        "reward": total_reward,
        "touched_fire": touched_fire,
        "reached_goal": reached_goal,
    }


def train_agent(episodes=800):
    env = FireGridWorld()
    agent = QLearningAgent(actions=env.ACTIONS)
    history = []

    for _ in range(episodes):
        history.append(run_episode(env, agent, training=True))
        agent.decay_exploration()

    return env, agent, history


def evaluate_agent(env, agent, episodes=200):
    original_epsilon = agent.epsilon
    agent.epsilon = 0.0

    results = [run_episode(env, agent, training=False) for _ in range(episodes)]

    agent.epsilon = original_epsilon
    return {
        "avg_reward": sum(item["reward"] for item in results) / episodes,
        "fire_rate": sum(item["touched_fire"] for item in results) / episodes,
        "goal_rate": sum(item["reached_goal"] for item in results) / episodes,
    }


def summarize(history):
    sample = history[-100:] if len(history) >= 100 else history
    return {
        "avg_reward": sum(item["reward"] for item in sample) / len(sample),
        "fire_rate": sum(item["touched_fire"] for item in sample) / len(sample),
        "goal_rate": sum(item["reached_goal"] for item in sample) / len(sample),
    }


def main():
    env, agent, history = train_agent()
    training_snapshot = summarize(history)
    evaluation = evaluate_agent(env, agent)

    print("NeuroCore Sandbox MVP")
    print(f"Training snapshot avg reward: {training_snapshot['avg_reward']:.3f}")
    print(f"Training fire rate: {training_snapshot['fire_rate']:.2%}")
    print(f"Training goal rate: {training_snapshot['goal_rate']:.2%}")
    print(f"Evaluation avg reward: {evaluation['avg_reward']:.3f}")
    print(f"Evaluation fire rate: {evaluation['fire_rate']:.2%}")
    print(f"Evaluation goal rate: {evaluation['goal_rate']:.2%}")


if __name__ == "__main__":
    main()
