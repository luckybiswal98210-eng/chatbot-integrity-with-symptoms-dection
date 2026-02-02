# AROGYA VANI - Multilingual Health Chatbot 🏥

A conversational health chatbot that provides personalized medical advice in multiple Indian languages. The chatbot asks follow-up questions about symptom duration, severity, and additional symptoms before providing tailored health recommendations with text-to-speech support.

## Features

- 🗣️ **Conversational AI**: Asks follow-up questions for personalized advice
- 🌍 **Multilingual Support**: English, Hindi, Tamil, Telugu, Kannada, Bengali, Gujarati, Marathi
- 🔊 **Text-to-Speech**: Audio responses in all supported languages
- 💬 **Session Management**: Maintains conversation context across multiple turns
- 🎨 **Modern UI**: Clean, responsive Flutter web interface with Material 3 design
- ⚡ **Fast API Backend**: Built with FastAPI for high performance
- 🤝 **Polite Responses**: Gracefully handles thank you, goodbye, and closing statements
- ❓ **Smart Error Handling**: Provides helpful messages for unknown symptoms
- ⚠️ **Urgency Detection**: Warns users when symptoms require immediate medical attention

## Architecture

- **Frontend**: Flutter Web (Dart)
- **Backend**: FastAPI (Python)
- **Translation**: Google Translate API
- **TTS**: Google Text-to-Speech (gTTS)

## Local Development

### Prerequisites

- Python 3.10+
- Flutter SDK 3.9+
- pip and virtualenv

### Backend Setup

1. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Build Flutter web app:

```bash
flutter pub get
flutter build web
```

2. For development, you can run:

```bash
flutter run -d chrome
```

### Test the API

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"I have fever","language":"en","session_id":"test123"}'
```

## Deployment

### Option 1: Railway (Recommended)

Railway provides free hosting with automatic deployments from GitHub.

1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Updated chatbot with conversational features"
   git push origin main
   ```

2. **Deploy to Railway**:
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect the Dockerfile and deploy
   - Get your public URL (e.g., `https://your-app.railway.app`)

3. **Update Flutter App**:
   - Open `lib/main.dart`
   - Update line 34: `final String apiBaseUrl = "https://your-app.railway.app";`
   - Rebuild: `flutter build web`
   - Deploy the `build/web` folder to a static host (Netlify, Vercel, GitHub Pages)

### Option 2: Render

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new "Web Service"
4. Connect your GitHub repository
5. Render will detect Dockerfile and deploy
6. Update Flutter app with your Render URL

### Option 3: Docker (Any Platform)

Build and run with Docker:

```bash
docker build -t arogya-vani .
docker run -p 8000:8000 arogya-vani
```

## Environment Variables

Create a `.env` file (optional):

```env
PORT=8000
CORS_ORIGINS=*
```

## How It Works

### Conversational Flow

1. **User describes symptom** → Bot identifies the symptom
2. **Bot asks about duration** → "How long have you had this?"
3. **Bot asks about severity** → "Rate 1-10"
4. **Bot asks about additional symptoms** → "Any other symptoms?"
5. **Bot provides personalized advice** → Based on all collected information

### Example Conversation

```
User: I have a fever
Bot: I understand you're experiencing fever. How long have you been experiencing this symptom?

User: 2 days
Bot: Thank you. On a scale of 1-10, how severe is your symptom?

User: 7
Bot: Are you experiencing any additional symptoms?

User: headache and body aches
Bot: Based on your fever for 2 days with severity 7 and additional symptoms (headache and body aches), here's my advice:
     Rest well, drink plenty of water or oral rehydration fluids, and consult a doctor if fever is high or lasts more than a few days.
     ⚠️ Please consider consulting a doctor soon.
     
User: Thank you
Bot: You're welcome! Take care of your health. Feel free to ask if you have any other health concerns.
```

### Handling Unknown Symptoms

```
User: I have dragon pox
Bot: I'm sorry, but information about that specific symptom is currently unavailable in my database. 
     I'm continuously being updated with more health information. For now, I recommend consulting 
     a healthcare professional for personalized advice. Is there another symptom I can help you with?
```

## API Endpoints

- `POST /chat` - Send message and get response
  - Body: `{"question": "text", "language": "en", "session_id": "unique_id"}`
  
- `POST /reset` - Reset conversation
  - Body: `{"session_id": "unique_id"}`
  
- `GET /health` - Health check

## Supported Languages

- English (`en`)
- Hindi (`hi`)
- Tamil (`ta`)
- Telugu (`te`)
- Kannada (`kn`)

## Project Structure

```
chatbot_app/
├── lib/
│   └── main.dart          # Flutter frontend
├── app.py                 # FastAPI backend
├── responses.py           # Conversation logic
├── chatbot.py            # TTS functionality
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── pubspec.yaml        # Flutter dependencies
```

## Notes

- Audio files are stored temporarily in the `audio/` directory
- For production, consider using cloud storage (S3, GCS) for audio files
- The chatbot provides general health advice - always consult a healthcare professional for serious conditions

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License
