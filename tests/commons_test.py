from fastapi.testclient import TestClient
from httpx import AsyncClient

from main import app

client = TestClient(app)

async def async_get_call(url):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(url)
    return response