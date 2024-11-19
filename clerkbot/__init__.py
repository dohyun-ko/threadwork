from fastapi import FastAPI, Request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from pydantic import BaseModel
import uvicorn

app = FastAPI()
slack_client = WebClient(token="")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/slack/events")
def slack_events(payload: SlackEvent):
    return {"event": event}