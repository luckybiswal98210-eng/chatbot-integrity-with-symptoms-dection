# 🏥 AROGYA VANI - AI Health Chatbot

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-success?style=for-the-badge&logo=netlify)](https://healthchatkit.netlify.app/)
[![Backend API](https://img.shields.io/badge/API-Railway-blueviolet?style=for-the-badge&logo=railway)](https://web-production-c2ec2.up.railway.app)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/luckybiswal98210-eng/chatbot-integrity-with-symptoms-dection)

> **🚀 [Try the Live App Now!](https://healthchatkit.netlify.app/)** - Your intelligent multilingual health assistant

An advanced conversational AI health chatbot that provides personalized medical advice through intelligent multi-turn dialogues. Built with Flutter and FastAPI, supporting 8+ Indian languages with text-to-speech capabilities.

---

## ✨ Features

🤖 **Conversational AI** - Asks follow-up questions about duration, severity, and additional symptoms  
🌍 **8+ Languages** - English, Hindi, Tamil, Telugu, Kannada, Bengali, Gujarati, Marathi  
🔊 **Text-to-Speech** - Audio responses in all supported languages  
💬 **Smart Conversations** - Maintains context across multiple turns  
🎨 **Modern UI** - Clean Material 3 design with smooth animations  
🤝 **Polite Responses** - Gracefully handles greetings, thank you, and goodbyes  
⚠️ **Urgency Detection** - Warns users when symptoms require immediate attention  
❓ **Smart Error Handling** - Helpful messages for unknown symptoms  

---

## 🎯 Live Demo

**Frontend:** [https://healthchatkit.netlify.app/](https://healthchatkit.netlify.app/)  
**Backend API:** [https://web-production-c2ec2.up.railway.app](https://web-production-c2ec2.up.railway.app)

### Try It Now:
1. Visit [healthchatkit.netlify.app](https://healthchatkit.netlify.app/)
2. Type a symptom (e.g., "I have a fever")
3. Answer the follow-up questions
4. Get personalized health advice!

---

## 🎬 How It Works

### Example Conversation:

```
User: I have a fever
Bot: I understand you're experiencing fever. How long have you been experiencing this symptom?

User: 2 days
Bot: Thank you. On a scale of 1-10, how severe is your symptom?

User: 8
Bot: Are you experiencing any additional symptoms?

User: headache and body aches
Bot: Based on your fever for 2 days with severity 8 and additional symptoms:
     Rest well, drink plenty of water, and consult a doctor if fever persists.
     ⚠️ Given the high severity, I strongly recommend seeking immediate medical attention.

User: Thank you
Bot: You're welcome! Take care of your health. Feel free to ask if you have any other concerns.
```

---

## 🛠️ Tech Stack

### Frontend
- **Flutter** - Cross-platform UI framework
- **Material 3** - Modern design system
- **HTTP** - API communication
- **AudioPlayers** - Text-to-speech playback

### Backend
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - ASGI server
- **Google Translate API** - Multi-language translation
- **gTTS** - Text-to-speech generation
- **Pydantic** - Data validation

### Deployment
- **Netlify** - Frontend hosting
- **Railway** - Backend hosting
- **Docker** - Containerization

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Flutter SDK 3.9+
- Git

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/luckybiswal98210-eng/chatbot-integrity-with-symptoms-dection.git
cd chatbot-integrity-with-symptoms-dection

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Server will start at `http://localhost:8000`

### Frontend Setup

```bash
# Install Flutter dependencies
flutter pub get

# Run on Chrome
flutter run -d chrome

# Or build for web
flutter build web
```

---

## 🌐 API Endpoints

### `POST /chat`
Send a message and get conversational response.

**Request:**
```json
{
  "question": "I have a fever",
  "language": "en",
  "session_id": "unique_session_id"
}
```

**Response:**
```json
{
  "response_text": "I understand you're experiencing fever...",
  "audio_url": "/audio/response_xyz_en.mp3",
  "session_id": "unique_session_id"
}
```

### `POST /reset`
Reset conversation session.

### `GET /health`
Health check endpoint.

### `GET /`
API information and documentation.

---

## 🗂️ Project Structure

```
chatbot_app/
├── lib/
│   └── main.dart              # Flutter frontend
├── app.py                     # FastAPI backend
├── responses.py               # Conversational logic & symptom database
├── chatbot.py                 # Text-to-speech functionality
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container configuration
├── pubspec.yaml              # Flutter dependencies
└── README.md                 # This file
```

---

## 🚀 Deployment

### Deploy Backend (Railway)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Create new project from GitHub repo
4. Railway auto-detects Dockerfile and deploys
5. Get your production URL

### Deploy Frontend (Netlify)

**Option 1: Drag & Drop**
1. Build: `flutter build web`
2. Go to [netlify.com](https://netlify.com)
3. Drag `build/web/` folder to Netlify

**Option 2: CLI**
```bash
flutter build web
npx netlify-cli deploy --prod --dir=build/web
```

---

## 🌍 Supported Languages

- 🇬🇧 English
- 🇮🇳 Hindi (हिंदी)
- 🇮🇳 Tamil (தமிழ்)
- 🇮🇳 Telugu (తెలుగు)
- 🇮🇳 Kannada (ಕನ್ನಡ)
- 🇮🇳 Bengali (বাংলা)
- 🇮🇳 Gujarati (ગુજરાતી)
- 🇮🇳 Marathi (मराठी)

---

## 📱 Features in Detail

### Conversational Flow
- Multi-turn dialogue system
- Context-aware responses
- Session management
- Follow-up questions about:
  - Symptom duration
  - Severity (1-10 scale)
  - Additional symptoms

### Smart Features
- **Polite Responses:** Handles "thank you", "goodbye", "okay"
- **Unknown Symptoms:** Provides helpful guidance when symptom not in database
- **Urgency Warnings:** Alerts for high-severity symptoms (8-10)
- **Personalized Advice:** Tailored recommendations based on collected information

### Multi-language Support
- Real-time translation
- Text-to-speech in all languages
- Language-specific keyword detection
- Seamless language switching

---

## 🎨 UI Features

- Material 3 design
- Responsive layout
- Auto-scrolling messages
- Loading indicators
- Language selector dropdown
- Reset conversation button
- Audio playback controls
- Smooth animations

---

## 🔒 Privacy & Disclaimer

⚠️ **Medical Disclaimer:** This chatbot provides general health information only. Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment.

- No personal data is stored permanently
- Audio files are generated temporarily
- Session data is ephemeral
- No user tracking or analytics

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

MIT License - feel free to use this project for learning and development.

---

## 👨‍💻 Author

**Lucky Biswal**

- GitHub: [@luckybiswal98210-eng](https://github.com/luckybiswal98210-eng)
- Project: [AROGYA VANI](https://github.com/luckybiswal98210-eng/chatbot-integrity-with-symptoms-dection)

---

## 🌟 Acknowledgments

- Google Translate API for translation services
- Google Text-to-Speech for audio generation
- Flutter team for the amazing framework
- FastAPI for the high-performance backend

---

## 📞 Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/luckybiswal98210-eng/chatbot-integrity-with-symptoms-dection/issues)
- Check the [documentation](https://github.com/luckybiswal98210-eng/chatbot-integrity-with-symptoms-dection)

---

<div align="center">

### 🚀 **[Launch AROGYA VANI Now!](https://healthchatkit.netlify.app/)**

Made with ❤️ for better healthcare accessibility

[![Live Demo](https://img.shields.io/badge/🌐_Try_Live_Demo-Visit_App-success?style=for-the-badge)](https://healthchatkit.netlify.app/)

</div>
