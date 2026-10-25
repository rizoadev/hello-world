# 🌍 Hello World — Agent Comms Demo

> Built by **Bolt** (BOLT) under **Saarah** (SAA) management via ACS.

## Stack
- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla HTML/JS served by FastAPI
- **Container**: Docker + docker-compose

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# or
docker compose up --build
```

## Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | JSON greeting |
| GET | `/health` | Health check |
| GET | `/app` | HTML frontend |
