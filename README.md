# Chatbot App

A FastAPI-based multilingual health-advice chatbot that returns text and optional TTS audio.

## Quick local run

1. Create virtualenv and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

3. Test endpoint:

```bash
curl -s -X POST http://localhost:8000/chat -H "Content-Type: application/json" \
 -d '{"question":"I have a fever","language":"en"}' | jq
```

## Free deployment (recommended: Railway)
Railway provides a simple free-tier workflow (GitHub integration) and will give you a public URL.

Steps:
1. Push this repository to GitHub.
2. Sign in to https://railway.app and create a new project.
3. Choose "Deploy from GitHub" and connect your repository.
4. Railway will detect the `Dockerfile` and build the container. If it asks for a start command, use:

```
uvicorn app:app --host 0.0.0.0 --port $PORT
```

5. Set any environment variables in Railway (none are required by default).
6. Deploy — Railway will provide a public URL (one link) for your app.

Notes:
- `audio/` is stored on the app filesystem and is ephemeral on most PaaS platforms. For persistent audio, configure an S3 bucket and update `chatbot.py` to upload audio there and return the public URL.
- `googletrans` and `gTTS` require outbound internet access from the host. If the host restricts outbound requests, translation or TTS may fail.

## Alternative free-ish hosts
- Render or Fly.io: also support Docker; similar flow (connect GitHub or push Docker image).
- Google Cloud Run: has a free tier but requires a billing account.

## If you want me to deploy
I can deploy to Railway for you, but I need one of the following:
- You add me (an admin) to your Railway project (not recommended), or
- You grant me a temporary Railway API/deploy token (not recommended), or
- You follow the above 6 steps — it's quick and I can guide you live.

Tell me which option you prefer and I'll continue.
