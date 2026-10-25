# 🌍 Hello World — Agent Comms Demo

> Built by **Bolt** (BOLT) under **Saarah** (SAA) management via ACS.

A minimal fullstack app to demo the Agent Communication System.

## Stack
- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla HTML/JS served by FastAPI
- **Container**: Docker + docker-compose

## Run

```bash
# Local
pip install -r requirements.txt
uvicorn app.main:app --reload

# Docker
docker compose up --build
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | JSON greeting |
| GET | `/health` | Health check |
| GET | `/app` | HTML frontend |

## Agents

| Agent | Codename | Role |
|-------|----------|------|
| Saarah | SAA | Manager / Orchestrator |
| Bolt | BOLT | Fullstack Developer |
| Wire | WIRE | Tester & QA |
