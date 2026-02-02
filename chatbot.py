from responses import get_response
from gtts import gTTS
import os

def text_to_speech(text, lang_code='en', filename="response.mp3"):
    # Languages supported by gTTS
    SUPPORTED_TTS_LANGS = ['en', 'hi', 'mr', 'ta', 'bn', 'te', 'kn', 'gu', 'pa', 'ml', 'ur',]
    
    if lang_code not in SUPPORTED_TTS_LANGS:
        print(f"[Audio not supported for language '{lang_code}', skipping TTS]")
        return None
    
    try:
        tts = gTTS(text=text, lang=lang_code)
        # Save the audio file in 'audio/' directory for serving with FastAPI
        audio_dir = "audio"
        os.makedirs(audio_dir, exist_ok=True)
        audio_path = os.path.join(audio_dir, filename)
        tts.save(audio_path)
        print(f"[Audio response saved as {audio_path}]")
        return audio_path
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
