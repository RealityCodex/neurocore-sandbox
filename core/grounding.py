def ground_observation(observation):
    """Turn raw environment state into simple interpretable concepts."""
    agent_x, agent_y = observation["agent"]
    fire_x, fire_y = observation["fire"]
    goal_x, goal_y = observation["goal"]

    return {
        "agent": observation["agent"],
        "goal": observation["goal"],
        "fire": observation["fire"],
        "near_fire": abs(agent_x - fire_x) + abs(agent_y - fire_y) == 1,
        "goal_visible": True,
        "last_reward": observation["last_reward"],
        "on_fire": observation["agent"] == observation["fire"],
        "at_goal": observation["agent"] == observation["goal"],
    }


def grounding_state_key(grounded):
    """Compact state used by the tabular learner."""
    agent = grounded["agent"]
    goal = grounded["goal"]
    fire = grounded["fire"]
    return (
        agent[0],
        agent[1],
        goal[0],
        goal[1],
        fire[0],
        fire[1],
        int(grounded["near_fire"]),
    )
