# NeuroCore Sandbox

> RealityCodex - Rebooting intelligence from reality upward.

NeuroCore Sandbox is an experimental playground for grounded, meaning-first intelligence.
The repo now includes a first working MVP: a small agent that learns in a deterministic grid world that fire is harmful and the goal is rewarding.

## Goal

Build minimal cognitive systems that:
- interact with a simulated world
- form internal representations from experience
- learn through feedback such as pain and success
- evolve useful behavior over time

## Current MVP

The first implemented experiment is a fire-avoidance task:
- an agent moves in a 5x5 grid
- a fire tile gives negative reward
- a goal tile gives positive reward
- a tabular Q-learning agent improves through repeated episodes
- grounded features include `near_fire`, `on_fire`, and `last_reward`

## Project structure

- `env/gridworld.py`: deterministic fire-and-goal environment
- `env/grounding_engine.py`: grounding helpers and compatibility adapter
- `core/grounding.py`: interpretable concept extraction
- `core/agent.py`: tabular Q-learning agent
- `examples/train_fire_avoidance.py`: training and evaluation demo
- `tests/test_gridworld.py`: reward and termination checks
- `tests/test_learning.py`: verifies training improves behavior
- `main.py`: local demo entrypoint and optional FastAPI app

## Run the agent

```powershell
python main.py
```

## Run the tests

```powershell
python -m unittest discover -s tests
```

## Optional API mode

If FastAPI and Pydantic are installed, `main.py` also exposes a small `/ground` endpoint for text grounding compatibility.

## Current limitations

- no graphics or web UI yet
- no persistent memory yet
- no multimodal perception yet
- the current environment is intentionally tiny and deterministic

## Suggested next steps

1. Add a terminal or graphical episode renderer.
2. Save metrics to CSV or JSON logs.
3. Add randomized maps and evaluate generalization.
4. Add a lightweight web UI to watch training live.
5. Explore neural policies only after the toy loop is solid.
