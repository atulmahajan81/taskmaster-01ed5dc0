# conftest.py

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.database import Base
from backend.main import app
from backend.auth import get_current_user
from unittest.mock import Mock

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture(scope="function")
def async_client():
    async def _get_test_client():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac
    return _get_test_client

@pytest.fixture(scope="function")
def test_db():
    engine = create_async_engine(DATABASE_URL, echo=True)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    async def _override_get_db():
        async with TestingSessionLocal() as session:
            yield session
    app.dependency_overrides[get_db] = _override_get_db
    async def setup_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    return setup_db

@pytest.fixture
async def user_token(async_client):
    response = await async_client.post("/api/v1/auth/register", json={"email": "user@test.com", "password": "test1234"})
    login_response = await async_client.post("/api/v1/auth/login", json={"email": "user@test.com", "password": "test1234"})
    return login_response.json()["access_token"]

@pytest.fixture
async def mock_send_email(mocker):
    mocker.patch("backend.services.email_service.send_email", return_value=True)