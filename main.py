from fastapi import FastAPI, Request
from pydantic import BaseModel
from grounding_engine import ground_text  # adjust if your import path is different

app = FastAPI()

class GroundingRequest(BaseModel):
    text: str

@app.post("/ground")
def ground_endpoint(request: GroundingRequest):
    response = ground_text(request.text)
    return {"grounded": response}

