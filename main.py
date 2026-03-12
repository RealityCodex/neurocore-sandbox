from examples.train_fire_avoidance import main as run_demo
from env.grounding_engine import ground_text

try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError:
    FastAPI = None
    BaseModel = object


if FastAPI is not None:
    app = FastAPI()

    class GroundingRequest(BaseModel):
        text: str

    @app.post("/ground")
    def ground_endpoint(request: GroundingRequest):
        return {"grounded": ground_text(request.text)}


if __name__ == "__main__":
    run_demo()
