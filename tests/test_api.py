"""Tests for Hello World API — Written by Wire (WIRE)."""
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


@pytest.mark.anyio
async def test_root_returns_hello(client):
    """GET / should return JSON with 'Hello World' message."""
    r = await client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert data["message"] == "Hello World"
    assert data["agent"] == "Bolt"
    assert data["codename"] == "BOLT"
    assert "managed_by" in data
    assert "timestamp" in data


@pytest.mark.anyio
async def test_health_check(client):
    """GET /health should return ok status."""
    r = await client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert data["service"] == "hello-world"
    assert data["version"] == "0.1.0"


@pytest.mark.anyio
async def test_app_returns_html(client):
    """GET /app should return HTML page."""
    r = await client.get("/app")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]
    assert "Hello World" in r.text
    assert "fetch('/')" in r.text


@pytest.mark.anyio
async def test_root_json_schema(client):
    """GET / response should have exactly the expected keys."""
    r = await client.get("/")
    data = r.json()
    expected_keys = {"message", "agent", "codename", "managed_by", "timestamp"}
    assert set(data.keys()) == expected_keys
