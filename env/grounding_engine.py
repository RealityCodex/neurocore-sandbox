from core.grounding import ground_observation, grounding_state_key


def ground_text(text):
    """Simple text-grounding placeholder kept for API compatibility."""
    return f"[grounded]: {text.strip().lower()}"


class GroundingEngine:
    """Small adapter that exposes the environment grounding layer."""

    def ground(self, observation):
        grounded = ground_observation(observation)
        return grounded, grounding_state_key(grounded)
