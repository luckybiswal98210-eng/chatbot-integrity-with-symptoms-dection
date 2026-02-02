from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from chatbot import get_response, text_to_speech
import uuid
import os

app = FastAPI()

# Ensure audio directory exists on startup
audio_dir = "audio"
os.makedirs(audio_dir, exist_ok=True)

# Allow frontend/client access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve audio files from 'audio' directory
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

class ChatRequest(BaseModel):
    question: str
    language: str = "en"

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    # Get chatbot response text
    response_text = get_response(req.question, req.language)
    
    # Generate a unique audio filename for each request
    audio_filename = f"response_{uuid.uuid4().hex}_{req.language}.mp3"
    
    # Generate and save audio file
    audio_path = text_to_speech(response_text, req.language, audio_filename)
    
    # Provide audio URL path for frontend to use
    audio_url = f"/audio/{audio_filename}" if audio_path else None
    
    # Return JSONResponse with UTF-8 charset for correct multilingual display
    return JSONResponse(
        content={
            "response_text": response_text,
            "audio_url": audio_url
        },
        media_type="application/json; charset=utf-8"
    )


@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"})
