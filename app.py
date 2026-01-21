from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import generate_reply

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply = generate_reply(req.message)
    return {"reply": reply}

@app.get("/")
def root():
    return {"status": "Backend is running on Hugging Face Spaces"}
# @app.post("/reset")
# def reset():
#     from model import chat_history_ids
#     chat_history_ids = None
#     return {"status": "reset"}
