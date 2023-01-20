from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.commons.configuration.database import Base
from src.commons.dependencies.dependencies import get_db

def create_db_local():
    global engine, TestingSessionLocal
    SQLALCHEMY_DATABASE_URL = "sqlite:///../../fastapi01_test.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal()

db_test_session = create_db_local()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

async def async_get_call(url):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(url)
    return response
