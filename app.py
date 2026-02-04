from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from chatbot import text_to_speech
from responses import get_response, reset_conversation
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
    session_id: str = "default"

class ResetRequest(BaseModel):
    session_id: str = "default"

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    # Get chatbot response text with conversation context
    response_text = get_response(
        req.question, 
        lang_code=req.language,
        session_id=req.session_id
    )
    
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
            "audio_url": audio_url,
            "session_id": req.session_id
        },
        media_type="application/json; charset=utf-8"
    )

@app.post("/reset")
async def reset_endpoint(req: ResetRequest):
    """Reset conversation for a given session."""
    message = reset_conversation(req.session_id)
    return JSONResponse(
        content={
            "message": message,
            "session_id": req.session_id
        },
        media_type="application/json; charset=utf-8"
    )

@app.get("/")
def root():
    """Root endpoint with API information"""
    return JSONResponse(content={
        "name": "AROGYA VANI Health Chatbot API",
        "version": "3.0",
        "status": "running",
        "endpoints": {
            "POST /chat": "Send a message and get conversational response",
            "POST /reset": "Reset conversation session",
            "GET /health": "Health check endpoint",
            "GET /docs": "Interactive API documentation"
        },
        "features": [
            "🩺 Intelligent diagnostic questioning",
            "🎯 Disease suggestion based on symptoms",
            "💬 Conversational AI with follow-up questions",
            "🌍 Multilingual support (8+ languages)",
            "🔊 Text-to-Speech responses",
            "📊 Session management",
            "✅ 25+ health conditions supported",
            "🤝 Polite closing responses",
            "🛡️ Smart error handling"
        ],
        "supported_conditions": [
            "Dengue, Malaria, Typhoid, Chikungunya",
            "COVID-19, Tuberculosis, Pneumonia",
            "Gastritis, GERD, Ulcer, UTI",
            "Chickenpox, Measles, Mumps",
            "Diabetes, Hypertension, Thyroid, Anemia",
            "And many more..."
        ]
    })

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"})

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting AROGYA VANI Health Chatbot Server v3.0...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🩺 New: Intelligent diagnostic capabilities with 25+ conditions!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
