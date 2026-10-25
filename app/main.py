"""Hello World — ACS Agent Comms Demo."""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone

app = FastAPI(title="Hello World", version="0.1.0")


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "agent": "Bolt",
        "codename": "BOLT",
        "managed_by": "Saarah (SAA)",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health")
async def health():
    return {"status": "ok", "service": "hello-world", "version": "0.1.0"}


@app.get("/app", response_class=HTMLResponse)
async def frontend():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello World — ACS</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #0f0f23; color: #e0e0e0;
      display: flex; justify-content: center; align-items: center;
      min-height: 100vh;
    }
    .card {
      background: #1a1a2e; border: 1px solid #333;
      border-radius: 12px; padding: 2rem 3rem; text-align: center;
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
    .emoji { font-size: 3rem; margin-bottom: 1rem; }
    .message {
      font-size: 1.2rem; color: #8be9fd; padding: 1rem;
      background: #16213e; border-radius: 8px; margin: 1rem 0;
      font-family: monospace; text-align: left; white-space: pre;
    }
    .meta { color: #666; font-size: 0.85rem; margin-top: 1rem; }
    .agent { color: #50fa7b; }
    .manager { color: #bd93f9; }
    #status { margin-top: 0.5rem; font-size: 0.8rem; }
    .ok { color: #50fa7b; }
    .err { color: #ff5555; }
  </style>
</head>
<body>
  <div class="card">
    <div class="emoji">🌍</div>
    <h1>Hello World</h1>
    <div class="message" id="msg">Loading...</div>
    <div class="meta">
      Built by <span class="agent" id="agent">...</span>
      · Managed by <span class="manager" id="manager">...</span>
    </div>
    <div id="status"></div>
  </div>
  <script>
    fetch('/')
      .then(r => r.json())
      .then(d => {
        document.getElementById('msg').textContent = JSON.stringify(d, null, 2);
        document.getElementById('agent').textContent = d.agent + ' (' + d.codename + ')';
        document.getElementById('manager').textContent = d.managed_by;
        document.getElementById('status').innerHTML = '<span class="ok">● Connected</span>';
      })
      .catch(() => {
        document.getElementById('status').innerHTML = '<span class="err">● Error</span>';
      });
  </script>
</body>
</html>"""
